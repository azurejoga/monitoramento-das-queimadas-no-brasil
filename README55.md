# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2165b067-9c2c-3961-8516-b2f6d77979e8 | -7.36003 | -39.1706 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5247764-63dd-3890-9bba-5a3ecff2829e | -7.37541 | -39.19675 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e8eb29a-46e4-3f3f-b9c2-dbbc5d87425c | -5.94487 | -43.29326 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78b22a3e-e4d0-347a-8cc0-6f807335aa0f | -7.77084 | -44.13933 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7beae81e-2dca-343e-a2b1-12a6db95fb16 | -7.69454 | -42.57922 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 639878d8-b45f-3bd9-85ee-3b7b30a1b7f8 | -6.98941 | -42.3329 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e1b75093-b8e5-3a88-8eca-ac59170bdd0d | -7.71721 | -42.56485 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f37caf77-78dc-3b95-ae4a-1b3dd995ed0c | -6.3708 | -44.30434 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d10bdf2c-bece-3f3a-8575-855fd67369ae | -6.05551 | -41.24492 | 2025-10-04 04:12:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 817d1626-1879-399b-ad54-342404ea6577 | -5.87528 | -42.52856 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c75ff24a-0f12-37f1-8ddd-3bd4f7e40d2a | -6.34264 | -43.46304 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cfb87392-b92d-3d8e-a9ea-1dfec8113abc | -5.68734 | -42.83857 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c1f20d10-3e0a-3e83-b3e5-92d7266a01d4 | -5.90812 | -42.77411 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca46cc8c-4a4b-3b9b-b2f5-1a33b68034a1 | -4.44094 | -43.2435 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 6b4cf234-3d5d-3d83-b94f-1e1d24c2f01f | -6.22636 | -42.9308 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88c1c094-dd20-3958-a4dd-1df4aaa6fc38 | -7.57313 | -42.39829 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5aa1060-bd76-37f0-9f2b-b2036cb0c568 | -5.49286 | -44.10714 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 778d56b3-64ec-3592-89bd-7d31095024f3 | -6.15853 | -44.61562 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 675cf5f2-45c1-3ab3-bf4e-a5c6580df686 | -5.24012 | -45.5464 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9239cbf-22c8-3fbe-b43d-86f0647afdd9 | -7.75105 | -42.51991 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d6559fcb-85a7-3d10-b7e5-c3eee49c96dd | -5.82856 | -42.84671 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7a132a50-4a73-313c-a056-323287908153 | -5.38731 | -37.70887 | 2025-10-04 04:12:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a4a4af7-2997-3080-8b5f-516a4405f56a | -4.40593 | -41.46152 | 2025-10-04 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1c1682bc-8649-3b79-b1be-1917c39a79e8 | -6.17318 | -43.93129 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d69126a4-fb1e-3d4d-bd18-eb083a05eb64 | -5.77911 | -42.9238 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| a9c31a9a-8b7c-349d-809a-af522c524bc1 | -6.36872 | -42.88988 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9b8ba1de-5a48-3dc6-b81b-b9d0b974cc3f | -7.5151 | -44.27173 | 2025-10-04 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9325abb5-f292-3b64-8d3d-a65578581fb6 | -6.01124 | -44.57439 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3c6a86b-3e22-3d11-8227-b0c92424211a | -5.91052 | -44.27972 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9a9e898-23e7-38ec-accf-312f070d8615 | -5.93991 | -43.30313 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aad661b-3598-3c58-a8cb-6845ad529539 | -7.04722 | -42.78751 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| acdd7844-c5b2-3455-8a8c-96b295f1e5ad | -5.52458 | -44.39288 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e10ccbe-d9dd-3da9-bf27-5f80e5891c0f | -7.15359 | -44.21442 | 2025-10-04 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d33daeeb-0fc7-36ff-be7c-b2f34f497c4d | -5.75985 | -42.93845 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 116b822b-f9a1-3b70-8fde-54e2a43263b9 | -5.9676 | -43.49291 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43848d0a-cb02-3235-b703-60f6b8c6ab2a | -6.87501 | -47.23795 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 8e3c94f5-2890-3a4b-b2d9-cb89511fb547 | -5.78593 | -45.7789 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f8ace2f-bbd4-3572-9e1b-0d273ed6a89b | -4.55571 | -50.47573 | 2025-10-04 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c0cfb92-d79e-3f6a-bd25-5ea2e07ff209 | -7.31046 | -39.13958 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df976904-c4d9-3f11-bca1-4cd2003c0bee | -7.77617 | -42.59919 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a85bdc79-6d5c-3d40-82a7-ddffd469b94b | -7.27549 | -45.49082 | 2025-10-04 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 884744a7-e92a-3760-bae7-ead3ce498c44 | -6.35588 | -43.44381 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9309eebb-5d19-3d8f-9581-7521432ff155 | -5.74386 | -42.9324 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8651cb54-56f4-31ce-8c29-e0da304f9299 | -4.70166 | -45.60592 | 2025-10-04 04:12:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd30d4f3-47f4-3db8-a1b6-a38a80fae839 | -5.89687 | -38.4816 | 2025-10-04 04:12:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 988d9e12-ba3d-3d61-90ab-b22062fec01d | -6.33099 | -43.89807 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a0f3c6d-8294-3d3e-81a7-a6a65f232c9c | -5.84674 | -43.37724 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa4d81f2-0322-310c-bc44-530861b462da | -5.19459 | -45.06778 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 97cb2a4f-6bf8-3a0e-9ce6-538f5ce7ea12 | -6.36904 | -44.30426 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a9db4b7f-bc9b-3752-8a0e-fcffa74593bc | -5.952 | -42.88364 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ec47e58-c2b0-3b82-9c1d-d511a35786b1 | -7.74664 | -42.52637 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 51be2f3d-7254-321f-859a-43ea485e7170 | -7.72108 | -42.56188 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d6247fa3-0195-34e9-9cc6-3b9dd543b7b7 | -6.68831 | -42.84444 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6cd5a1b6-1bd9-3357-88c9-806195f56063 | -5.79966 | -42.729 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed6769f7-ebd2-362f-86d2-4fcb7e356ecf | -7.08736 | -46.64522 | 2025-10-04 04:12:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b07b1c74-ed0e-392b-8c67-86396de27e7c | -4.43651 | -43.24993 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60972232-390e-3939-9763-aeb0f820754b | -7.05591 | -45.78793 | 2025-10-04 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98bf87f7-f8bc-31ae-b74a-69b8877e0d70 | -5.6868 | -42.84202 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c03261ef-35f9-3abe-a26d-e56447e3e65b | -6.68501 | -42.84392 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91f5bf91-e876-32fb-bc7f-ec76c6bb0be9 | -6.71097 | -42.15641 | 2025-10-04 04:12:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 44af1441-0448-3c56-99e4-e6608dc8b3c6 | -5.79912 | -42.73245 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 964f4238-4a5b-3411-ba87-2371fab7df5a | -7.56037 | -42.63301 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3588874b-73d4-38b6-90c6-3bbb3f26dbd0 | -5.21669 | -46.17207 | 2025-10-04 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f3bff2e-8a4e-315e-9a26-c81e77a659fd | -7.348 | -39.17344 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77c23264-49b1-32ac-b46e-d89b3a0238ed | -6.7435 | -44.59655 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2fccafd-4245-3201-b5da-601dbddd7035 | -5.62565 | -44.70208 | 2025-10-04 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eede2e55-a1d9-3a7e-87cf-a40428c1a173 | -6.29213 | -42.49117 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 978b97df-ab0e-3ed6-9c43-8f3b3d30ed50 | -6.27052 | -42.45585 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 873c65e8-802d-35c2-bd0e-818bcc71f62c | -5.68796 | -49.31017 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b1e54c6-eafa-3e5b-8a4e-5621286196a7 | -6.99328 | -42.32992 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d9682cae-a28a-3209-9dd2-f08073614c9d | -4.14489 | -42.17136 | 2025-10-04 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 39d604bb-2d5d-37af-9c86-e493a6c0ae90 | -7.2956 | -47.95876 | 2025-10-04 04:12:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efd478c2-b862-307c-b03a-5fbff9cbd37f | -6.66956 | -42.83439 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b5e48cc-73b0-356d-b090-a49939ef743c | -5.73612 | -42.91703 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f01b8b5e-b7a1-3b5e-b6b9-959376c21ce7 | -6.29753 | -42.43515 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7271c99c-dc13-31c5-bfb4-400540ae8319 | -5.63668 | -43.22343 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 744bfa10-866d-378f-a0f3-95991bbfa5d3 | -5.19048 | -45.07111 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6d3c78e-cc49-3cc2-876d-b1a4926ec3f6 | -6.35037 | -43.45716 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92b8550f-6755-3ee7-ac16-ea37001c540f | -7.48722 | -43.03461 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2fbfe21-9a45-3e8c-aef3-a2811d6f3eb0 | -5.98254 | -43.48456 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84b8322d-4c93-3f16-be69-2b37307a6798 | -3.96707 | -41.59672 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f815195b-4eb5-3591-b03d-b73e3127145a | -7.29164 | -47.95811 | 2025-10-04 04:12:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7783990-d88a-31e5-b4af-33eebe1d7c20 | -5.87582 | -42.5251 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5796446d-545d-34f0-8502-0aa92f783071 | -5.84055 | -42.88022 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf744b8a-9095-3e5d-a431-5aa94851f82b | -5.92876 | -44.84504 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b311a2a6-7bce-328e-8fb2-f8394b85d111 | -7.71447 | -42.58235 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2a3a618c-c386-3bbc-96a7-e2f5c18eb72d | -7.76735 | -42.61209 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1340dbf-5f11-358f-99a8-aa23c0eb9a41 | -3.84253 | -41.56702 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 6ed3a15e-29a6-3521-bf13-f1a526ce25eb | -5.97319 | -45.26822 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06f534a6-69a0-361b-bda7-d6e772574478 | -6.36657 | -43.8893 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b5f4673-ca94-398e-9abf-5ac27c40b7de | -5.32748 | -43.35192 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb8f8ac-2988-3ab3-ae37-6924f091a78e | -7.83847 | -44.44007 | 2025-10-04 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e00724a1-91c4-32ec-9f6c-8eedcff08e22 | -5.47306 | -44.31802 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae1ec731-b989-33d9-b6ab-d4d2316388e8 | -2.89079 | -50.73 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 14b98da2-1edd-3893-b43c-3085b4b97f0d | -7.7389 | -42.53233 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9c5ed9ed-edbc-3362-9a7c-1b65c175e002 | -5.82918 | -42.8857 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 92a443a7-a0a1-33c3-b740-59b5961ccb03 | -6.26467 | -42.79524 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1cd28ecd-72bb-3eeb-9a00-2b0094730a79 | -5.90422 | -42.51867 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 796d4433-34e0-3073-a0ee-f8d8a7e525f2 | -6.12212 | -45.93332 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c65de54b-08ff-383d-9dfa-fec4b14f7b82 | -4.61201 | -43.14981 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |


[Clique aqui para ver as próximas entradas](README56.md)
