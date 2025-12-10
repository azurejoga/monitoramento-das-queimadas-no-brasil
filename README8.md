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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9245123d-cb5c-327d-aa01-dc844b059121 | -3.58264 | -41.66639 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 31dce6dc-d94e-34d9-8c27-0d78011251e9 | -2.41975 | -48.27339 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a59436a3-f568-3c0e-ac22-2033a24f7304 | -2.08321 | -52.05375 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85ff5b92-5cea-314d-b23b-71e687dc04a8 | -4.34779 | -46.09129 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16da4770-8741-3955-97f6-f776a6cb3188 | -2.74832 | -45.39954 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 261b3fb0-e2a1-3b31-b372-1b2970087899 | -3.69473 | -43.82381 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f8a6194-d045-3ca7-9fc6-657c31332638 | -2.08786 | -52.05083 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4f83b46-ac89-3500-855b-0f66138bc603 | 2.02965 | -55.66576 | 2025-12-10 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db0c6de-bc85-36f4-a797-2f5b4c91eccd | -5.58816 | -39.77241 | 2025-12-10 04:36:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 09b443b0-81c0-32b7-b8fe-fc06a597f8ce | -3.68252 | -42.03355 | 2025-12-10 04:36:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3010ef2-cc2e-3fb9-b4be-af2d3f3cc63c | -3.39388 | -42.10662 | 2025-12-10 04:36:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3d8e2341-b0c3-3321-a20b-1b199d6f13eb | -3.98191 | -42.56997 | 2025-12-10 04:36:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 89864ad6-fe8c-361e-9756-b1f4e9e40f89 | -2.63396 | -45.39282 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f3a8cb5-169e-363a-bcd3-be888bd2e8d1 | -1.75929 | -45.51426 | 2025-12-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4385e79e-0517-31e9-b23d-2ff94ea394ad | -2.21446 | -45.41838 | 2025-12-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17b0c738-7c1e-3115-8f33-66bb52b49c55 | -1.19671 | -54.1927 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 630c9436-e31e-3290-a594-69735a3a78e1 | -3.62127 | -50.98904 | 2025-12-10 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9e7ef22-71bf-3122-abc2-b8158af12635 | -3.96556 | -41.52265 | 2025-12-10 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9fabb31a-fcca-3637-b4b3-882ee1814bd6 | -4.34723 | -46.09489 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c9ea7c0-b21e-36be-8ae8-b97c43044ef9 | -2.81979 | -45.27902 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8867693f-7eac-335b-a828-b128e7beae1e | -3.17271 | -43.1063 | 2025-12-10 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 792376a6-48a4-301a-aa92-4f86feee21a4 | -3.41884 | -52.65092 | 2025-12-10 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ceacd0-7c6a-387e-92c7-517187782bb0 | -3.43845 | -41.64917 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bb851f63-199d-307c-8461-4bd798afe903 | -0.50895 | -49.17373 | 2025-12-10 04:36:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef365bd2-c96c-3b46-b2f2-272e087cd9a1 | -1.58439 | -54.12424 | 2025-12-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba8d77d8-b856-3cda-a5c5-68bb994644a9 | -2.01745 | -45.53603 | 2025-12-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01176320-8326-3fae-bd33-5d4294f9cb61 | -4.29533 | -45.93219 | 2025-12-10 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 435006cc-c1e3-3086-b283-141e92617165 | -0.84541 | -48.11235 | 2025-12-10 04:36:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 872ea31c-7a61-3dd1-9ba4-c60136cd52c8 | -2.36797 | -46.31252 | 2025-12-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d8ced4a-7b84-3998-a67a-3436917d35da | -2.83963 | -48.90843 | 2025-12-10 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0abd347-2a22-33bb-8b5a-28e66946029a | -3.23619 | -45.29562 | 2025-12-10 04:36:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5587b374-0b1d-386a-a5b0-1c93d667e1db | -3.83813 | -51.295 | 2025-12-10 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8495ea4-c34c-382d-b045-554586bb5cd1 | -0.84597 | -48.10876 | 2025-12-10 04:36:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8709f1b1-1d4b-32b6-94d9-1a54435c536c | -3.42887 | -41.65554 | 2025-12-10 04:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 817d72cd-fae5-3d92-9950-eda2baaa2bff | -3.68999 | -47.13654 | 2025-12-10 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 357c2469-06ce-3313-a896-dd68cf80b184 | -2.82037 | -45.27534 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb678f0a-e760-3254-847c-61578eb8784d | -2.26106 | -47.86544 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d9d99c39-4d24-3bda-bebb-fba6eb9e90e7 | -4.74289 | -44.43935 | 2025-12-10 04:36:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2d0538a-e997-3c8b-9d72-e0119843cacf | -2.2644 | -47.86596 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a0da870-aa8d-3344-93b0-d97494629a5b | -1.75985 | -45.51069 | 2025-12-10 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 733540d9-180f-3cb4-b2b1-1c5a38f7494a | -2.48448 | -47.77923 | 2025-12-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 075ef200-2a6c-342d-8368-21935b42d5b0 | -4.50128 | -40.51974 | 2025-12-10 04:36:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f617da72-72f9-381c-b4e6-4e5ff4cd8fbe | -3.957 | -41.52129 | 2025-12-10 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 605db1c1-8ffe-3586-adfe-b8c400bd42f9 | 0.79167 | -51.96722 | 2025-12-10 04:36:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a2e0c73-5aba-3166-87b2-452c7ae0d671 | -4.75802 | -45.69534 | 2025-12-10 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99c4e339-b250-3361-847b-b6d4f8a1984d | -2.65482 | -54.84568 | 2025-12-10 04:36:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e9b6b19-7910-3304-849d-e25e0cdcd841 | -6.07737 | -41.50375 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c0e70d7c-c342-3439-92c0-765809235c3d | -3.68538 | -40.72965 | 2025-12-10 04:36:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 55071fc2-b633-33ad-8c68-ccb11f55c49b | -2.74378 | -48.38944 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eaec224-6619-30b1-b9cb-87b7fa0c9b76 | -2.75173 | -45.40008 | 2025-12-10 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d52ac654-fca1-3109-aaaa-d01f88403260 | -2.38505 | -56.05754 | 2025-12-10 04:36:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6db71b3-5b03-36e2-bc89-249eabb789c0 | -3.68667 | -43.82699 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ef8dbc1-11d0-3861-ab4c-067d12aaf2e0 | -2.18348 | -52.12565 | 2025-12-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3b2c057-cfc2-396c-b218-7a91158b038a | -6.07297 | -41.50296 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c31c2d4-1b18-3c60-9bbe-9c3f0e038b1f | -3.69553 | -42.11421 | 2025-12-10 04:36:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aa8e71cf-ff25-3335-a477-82072d9076e3 | -5.84365 | -42.46135 | 2025-12-10 04:36:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed793235-3988-3eb3-b79c-a072aeaf3f92 | -3.40219 | -42.46263 | 2025-12-10 04:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44555e47-c45d-3b20-9bb9-429017109071 | -4.49276 | -40.51348 | 2025-12-10 04:36:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a758ed30-650d-3f85-92cc-087a100183fb | -2.26718 | -47.86998 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64e1a3c6-3c67-3273-906e-44f4fc096805 | -0.32796 | -49.98515 | 2025-12-10 04:36:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbf41a6d-79b8-3104-90ab-29b851c13021 | -4.11059 | -46.48726 | 2025-12-10 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4af1938-cfb1-332c-a3f5-0faa2a598ff8 | -3.93645 | -40.73538 | 2025-12-10 04:36:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aff19d49-58b2-34e0-9525-9ac8b07642bd | -2.2966 | -47.79228 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4fc47ae-c0b2-3325-9f37-955647474b25 | -4.50059 | -40.52433 | 2025-12-10 04:36:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6d79aae0-436e-3914-9836-8fd1adbf889a | 1.16042 | -50.70704 | 2025-12-10 04:36:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91bcf475-5cd1-3b5b-868e-e4dd214029c1 | -2.06229 | -49.00486 | 2025-12-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e01e0e9f-5f6c-3e46-854c-cb508b79162a | -2.63679 | -45.39699 | 2025-12-10 04:36:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd1cd61f-ce1f-3bfe-85c3-ebf3b30822fd | -3.69608 | -43.81519 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fff0dbb-022f-35e3-a51a-20b482a71f9a | -3.39743 | -42.4671 | 2025-12-10 04:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6332b3d3-284f-3a37-b784-78b2c534c192 | -5.17179 | -43.11895 | 2025-12-10 04:36:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d52e9b84-392a-348f-ac91-2db83faf2f11 | -4.4779 | -44.07988 | 2025-12-10 04:36:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eef95fa-b6d1-3308-be98-6beac8e6e174 | -2.72165 | -53.19644 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20c8053f-3ece-3e43-9efe-20d28395eaa7 | -3.18303 | -48.02828 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5eb389b-231c-33de-937c-6e5b3efddf77 | -2.38734 | -56.0582 | 2025-12-10 04:36:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33199379-c13b-3ca7-b52f-5a647ba78896 | -2.78887 | -54.41846 | 2025-12-10 04:36:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c426f142-b1ce-35ac-b1be-9b2d84118ab9 | -2.26774 | -47.86649 | 2025-12-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ae7aa44-3aa2-3841-a1c2-3db910e8212d | -1.01577 | -53.73473 | 2025-12-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfef39e0-46d8-32e2-833a-d35f6168aca8 | 2.02537 | -55.66533 | 2025-12-10 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08e85b1b-1f27-3635-a922-15a24c69100f | -2.93073 | -48.23004 | 2025-12-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4141083-453d-3eac-913d-3b5d1ab27583 | -2.79992 | -47.3496 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c69e4bd-f285-3634-9d52-d1e86660f374 | -2.79715 | -47.34563 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31e8ec26-59e5-3b68-b5ed-186bb6351a0e | -3.69172 | -43.8189 | 2025-12-10 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 63d55ff0-4a17-3d6d-a88f-07c9c439b2cb | -2.05671 | -47.10609 | 2025-12-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9baca904-c591-3682-ade2-dfa59a9d7d2f | -2.84558 | -45.79875 | 2025-12-10 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2600b0b3-1ba6-3265-b126-81aec3bf3835 | -2.21106 | -45.41785 | 2025-12-10 04:36:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51797282-ce55-3261-8352-0f1aee694959 | -1.01652 | -53.73005 | 2025-12-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87833a05-e623-3211-b15c-1aac3d57406f | -3.23169 | -47.46724 | 2025-12-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f193313-5733-383c-bae8-0174ca5a1e5d | -1.43118 | -45.66809 | 2025-12-10 04:36:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013d32d0-a176-3da0-a632-d190af59a1f3 | -5.84496 | -42.46434 | 2025-12-10 04:36:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 80a8d32c-5552-37b6-ae51-ca0bef60fc7d | -5.74488 | -42.05737 | 2025-12-10 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6c477b80-8690-3ffd-8b28-df271de0e249 | -1.87629 | -54.68507 | 2025-12-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc755cc2-fbae-31d7-bf13-d254226fd534 | -4.18161 | -41.94697 | 2025-12-10 04:36:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e3cb2d38-637c-3ed7-9148-21fcb288808f | -5.00258 | -41.29249 | 2025-12-10 04:36:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97c00a78-221b-3e01-8c40-a6bdae8800a7 | -5.33135 | -43.5659 | 2025-12-10 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36fa9fa9-da20-37c6-acb0-a6e6525ef24f | -2.26535 | -53.70654 | 2025-12-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0c0f140-7d6f-3c5a-afb9-f724789ef8fa | -5.36068 | -38.06425 | 2025-12-10 04:36:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 102fa1ca-4791-3d73-b396-b890026ef589 | -6.07288 | -40.01152 | 2025-12-10 04:36:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 23314d73-ad1a-3298-8325-8bff95733615 | -1.84683 | -46.39809 | 2025-12-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b365841-9812-3ee8-82af-bf0c3d2d5b31 | -3.1704 | -52.87438 | 2025-12-10 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeba0de5-7434-306d-bff0-051151eb0e2c | -2.80269 | -47.35357 | 2025-12-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README9.md)
