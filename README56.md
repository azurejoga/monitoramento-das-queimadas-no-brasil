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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 104f4937-1a16-3a4d-9780-a881f4e8d8ee | -2.57366 | -47.57423 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ad96b1c-91df-3a50-8a8b-928bbdef87c3 | -3.53319 | -50.2621 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e61d2f17-8fb8-3127-bc03-81e9937ef18b | -5.97623 | -45.36971 | 2024-11-17 04:29:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3f6b31f-d33d-30d0-9007-4dd0aeb45941 | -3.74219 | -44.53157 | 2024-11-17 04:29:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2844f652-0256-34c2-a8a7-ca0dee124844 | -2.36522 | -48.53093 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6924ef12-6c0b-3bb3-9400-601d584e9806 | -4.06868 | -46.86015 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d41ef18-327b-3aa0-9886-58bc06929cfc | -2.68129 | -46.82671 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 543d3ba3-d5aa-3809-9af6-b9b3d6e2ce72 | -3.62437 | -43.15937 | 2024-11-17 04:29:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c7cd3ee6-23cd-34d5-bc10-f23d604824b4 | -2.59803 | -48.32404 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22daefe6-d98c-3cda-b6dc-3b1301221642 | -1.48871 | -51.16115 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef5538c4-c29e-37fd-8bcf-6d4d638f3a14 | -2.23482 | -53.61006 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3bea6af4-b527-3766-90b2-fd4f45bad852 | -3.80916 | -46.52215 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd999d5d-e2df-3f4d-9653-a2510883a167 | -3.76455 | -50.78897 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 540ac094-c976-38e4-ba8c-19adfebbc778 | -4.91146 | -44.80907 | 2024-11-17 04:29:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f97c7b-58b0-35dc-be23-733d8ec8f099 | -2.07407 | -46.47459 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8560074f-0230-31b5-adb3-8ffb1130c0ad | -1.06598 | -46.74944 | 2024-11-17 04:29:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ee6df7-a146-30e3-a412-c2cc48aa4d0e | -2.15355 | -48.53881 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7d04af5-975f-3c21-9a30-772673196ce1 | -2.5669 | -54.73121 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a0dfe46-1903-303f-8da3-9311b3788722 | -2.66968 | -46.18503 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ba87e4-6f1f-363c-a679-b1bf1d5631c8 | -2.5112 | -46.39437 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ba1d4e3-bb08-3f4c-8af2-15e80779ceb6 | -3.09559 | -51.31383 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 309b1812-8e17-3516-a062-f131f80bbb78 | -0.95195 | -51.73186 | 2024-11-17 04:29:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4abfb330-518c-32f9-a18e-4a17a324e699 | -4.18948 | -48.5726 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bb65515-6c11-3bdd-adaa-8e1d83541699 | -1.97017 | -48.38864 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 78dfa783-ab2c-3e77-bebc-2d87a5a5fb26 | -3.0046 | -45.42683 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d8ba324-e428-3ae1-b5bf-bde89b5a012c | -4.667 | -49.51577 | 2024-11-17 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50324265-956d-3eb2-a7aa-5c6478370a09 | -3.7586 | -42.72808 | 2024-11-17 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a960889f-d401-3aaa-9fc4-35da4c235462 | -1.29194 | -51.74203 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fa0c11e-1d2d-3bfc-8a19-6b8d8f79a941 | -2.89897 | -48.30922 | 2024-11-17 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7de27d8f-ecc3-3a42-9eb0-2c0504b6a565 | -2.64024 | -46.82727 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29377870-2c39-3697-b4c2-2cca748beb7f | -5.42405 | -45.33988 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e3044367-ae19-3606-a805-90b9f9e0da59 | -2.82933 | -46.66287 | 2024-11-17 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0f862be-73c4-359a-9cc6-1981115a4895 | -2.32867 | -47.85593 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8557735-7ed0-3df5-bd89-e6c9937d7746 | -2.64099 | -46.15176 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0e4b523-1711-38da-a47a-42778aa07d2e | -4.26164 | -48.54422 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d80ba75-b8de-32d9-97e5-fe551a043060 | -4.13788 | -48.85392 | 2024-11-17 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5bda70e-b24a-36a9-ab2d-2e94d3243c32 | -3.46009 | -50.0142 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdc551f7-01c3-30a5-b28a-07673d57ded0 | -3.21026 | -46.68022 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6391e771-bdc6-3faa-85a6-2ea193020ca8 | -3.18058 | -53.24796 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ab1efe37-cde0-36a8-bd24-bd4b4fc2cc91 | -2.62664 | -48.56707 | 2024-11-17 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 39564d03-cfe1-33d8-8ba1-b9cfda907718 | -5.31653 | -45.44822 | 2024-11-17 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ffb5a4d-8a8f-3e3a-9a99-67879c560590 | -4.3694 | -40.59156 | 2024-11-17 04:29:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d3ee919-aa75-30fe-8c6b-8e8d059965af | -2.55852 | -47.28228 | 2024-11-17 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b52f1535-bf65-3205-954d-6506960d6f93 | -4.64647 | -45.0029 | 2024-11-17 04:29:00 | NOAA-20 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb93de27-0e16-3dae-84e4-87a957207083 | -4.23074 | -48.03302 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1f78836-3172-3ff1-b1bd-b2b1ce58744f | -3.79218 | -46.02042 | 2024-11-17 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae066ea7-c5b4-3fee-b51f-f0381a0176cf | -2.09975 | -48.39713 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d7bc585-b160-342c-b039-b44fa04fa19d | -2.97044 | -45.82501 | 2024-11-17 04:29:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cff2a2e-8e5a-30bc-bf27-e8e9dd22040e | -2.17126 | -48.33844 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ac454f9-7b18-3675-823d-2cadd3fc73ee | -2.59518 | -47.56696 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c5fddfea-6192-32b5-9f00-431a1629cd79 | -2.1033 | -48.25438 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d17d61-8511-3021-91aa-743e735bc831 | -4.35795 | -48.13166 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07c5d976-2615-3826-bbf3-c03fdeb70b77 | -1.13378 | -51.69169 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86fd4fd1-9e02-3601-8064-df3c0b49be8a | -3.82382 | -50.2301 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ba3f45-7a8d-3a3b-87c9-a476bca25e3e | -1.95538 | -48.97272 | 2024-11-17 04:29:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97093e5d-616b-3682-9b6c-9c21748607c8 | -3.88519 | -46.64413 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a2e1e97-06cd-3686-a89c-2c794af30db5 | -2.14164 | -46.41101 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6560992-be3e-34cb-b30d-11819b7ffc97 | -2.16203 | -46.41064 | 2024-11-17 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac08070d-15e2-3014-8a20-f5e09cc8b59f | -4.18352 | -46.82176 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce2c39ba-ec8f-3fb2-9cc3-15b4ad026826 | -2.10546 | -50.74292 | 2024-11-17 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34c90f0c-75f1-3e78-919d-542b4ae2d8ba | -0.123 | -51.62502 | 2024-11-17 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f41c69d9-082f-3dd3-86a3-dde29da9e1a6 | -5.18566 | -37.99874 | 2024-11-17 04:29:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22a2a763-b8f5-3cd0-9f03-e3fecb449bb3 | -3.95846 | -46.71912 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e36baa1-b3e9-3a58-9add-271b93b8476e | -4.095 | -47.8168 | 2024-11-17 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 040963c3-b04c-380e-be48-80c051b8f8bd | -3.58521 | -49.88605 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0811875f-97a6-3bd6-9b41-973d3d8e94dd | -2.22887 | -53.61842 | 2024-11-17 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4a7bdcc-4ca1-3eea-b8f6-cac97ccfbe21 | -3.89232 | -46.6204 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d56d482-e6b8-39cc-98a0-1f6f95d00c27 | -3.99883 | -51.02777 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37a5936d-094c-3d69-831e-15b6158bf2ee | -2.61964 | -46.027 | 2024-11-17 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc9c7e2c-d8e7-3760-b77d-1e196c467ff9 | -2.20309 | -46.04114 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05344a67-4be2-3583-8476-0847086033c5 | -4.2807 | -48.21196 | 2024-11-17 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9ccd52e-172f-374d-b0fe-ab46c3f50a09 | -3.88846 | -46.62334 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53125f68-d6e8-3244-9200-2242619d6db1 | -4.72715 | -46.84258 | 2024-11-17 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08b9c502-ae87-3abf-9c55-6659b4a8e1c8 | -2.61891 | -46.184 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b59c3277-d95f-36f4-9e48-d63edcfd4de8 | -5.62998 | -46.36726 | 2024-11-17 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c05035eb-ff38-3052-9548-75a7cf7e8572 | -3.99811 | -51.03223 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 482cdada-d6ba-3b84-80e5-35d469372506 | -1.70499 | -46.16281 | 2024-11-17 04:29:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e0e602d-23cb-33a3-8696-8ffd525ede25 | -6.94302 | -42.81922 | 2024-11-17 04:29:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a29a419f-d557-3834-bc77-d75a10b4c154 | -2.59904 | -47.56402 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fca7a38-f593-34c4-b32b-5072d2d2fc82 | -3.25013 | -46.53436 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde6e90c-c707-3f36-9e79-f668007b4222 | -3.51881 | -50.25993 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6e99157c-984c-3f22-ba5d-441fe7f6f04c | -2.59572 | -47.5635 | 2024-11-17 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30b2d22d-0bbe-3faa-b95a-5f698075015a | -2.25474 | -48.41012 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09b5e939-f968-3ccf-9a3e-a8874a681867 | -3.52012 | -50.25166 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 84ed3e89-8225-326b-b3d6-8418c15909ef | -4.18406 | -46.81831 | 2024-11-17 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37c1e5d7-e811-3f6b-9b21-29635cbbf6fe | -2.6246 | -46.25601 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7ffd3b0-00c6-3549-a7f1-e447bcae211e | -3.25637 | -46.53923 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cf1f65e-a8f9-348c-97cf-16df93d7fed6 | -3.08955 | -51.40048 | 2024-11-17 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57a2fe65-afff-302c-8e22-3c481e3ac5c1 | -2.54693 | -54.30596 | 2024-11-17 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 832b69e0-4393-3c90-983a-22f0fc5787e6 | -2.36465 | -48.53454 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9db1530-2bed-34be-9087-9adb1bd192ad | -2.08204 | -48.61705 | 2024-11-17 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03bfe852-a1b8-371c-aa3a-7d12e643506b | -2.50843 | -46.39041 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2390f8b-93f9-3ba2-ab78-7cab625acdfa | -2.65326 | -46.20354 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef9d00c0-a4e3-348c-922a-a20734f33473 | -1.40096 | -51.08012 | 2024-11-17 04:29:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd561d16-ff98-3a8f-9716-9cd945c8a6c6 | -2.11785 | -48.20554 | 2024-11-17 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c42d805-1765-35f9-9ad2-ed6a66a1ef42 | -0.91903 | -51.64716 | 2024-11-17 04:29:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e1790db-aade-36b3-bff9-de2c67617187 | -2.625 | -46.18851 | 2024-11-17 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96bd3e45-fad3-399d-b6f8-40f0582801bc | -3.69344 | -50.11444 | 2024-11-17 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce52b56-6606-3cdd-ad97-c860f1ef7477 | -3.00854 | -45.42372 | 2024-11-17 04:29:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e61afce-a94a-3b9d-97a4-9dd0977b1b62 | -3.18423 | -53.25286 | 2024-11-17 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README57.md)
