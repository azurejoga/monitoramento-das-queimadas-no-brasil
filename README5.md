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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b9ab12b-73f8-3512-8a8a-bf794c3cd6cf | -3.76535 | -46.97145 | 2025-11-29 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f67c4fb7-7937-3ba7-8f2a-1d6814cf5759 | -3.97022 | -48.99647 | 2025-11-29 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a912bfb-872c-39da-acc9-1eb695d513c3 | -2.70367 | -47.41828 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bb5a73ef-5cf6-3d39-b94e-0860247f4ab5 | -3.22506 | -50.32465 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 23a5aee9-8b2a-37ad-871b-dc2befb6c635 | -2.35115 | -45.70085 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 163.8 |
| ad3ea78c-3fb5-349a-9fcb-9116d7f7ce39 | -4.1087 | -44.9055 | 2025-11-29 00:34:00 | TERRA_M-M | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 3d371b49-5941-3744-901f-777d24d92b1a | -2.92273 | -45.24219 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 66cd0ecb-18b3-3fcb-98eb-a7b96eaa692a | -2.89205 | -49.45856 | 2025-11-29 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d26d37fa-a9a3-3a23-9a1c-5a3876d3b95d | -4.08669 | -50.75237 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c52430e-3e17-3235-a7ca-5170606bef87 | -2.60182 | -47.35032 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| efdd4c1f-1ee1-3acd-a83b-ac5650eadbc1 | -4.3808 | -43.83152 | 2025-11-29 00:34:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e935bdbf-3ea2-32d6-9391-8bb8ba458b9b | -2.25906 | -51.93359 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97097a76-266c-3e62-b21e-6e561ea26256 | -3.83838 | -44.13408 | 2025-11-29 00:34:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ba6edaad-7a8c-31fe-b31d-93fe9b6bb085 | -2.77067 | -49.64177 | 2025-11-29 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4144d9e4-a45e-32cc-8bfb-52da135954b6 | -2.23004 | -47.52316 | 2025-11-29 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 496ee648-8f63-3988-8034-32cae96fc7b1 | -1.76233 | -54.77603 | 2025-11-29 00:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83372ef9-3a15-35fe-b4f2-501ca2566d8f | -3.98355 | -49.0243 | 2025-11-29 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| aa0869c1-26ce-326a-9974-ea00715529e2 | -3.47034 | -47.62807 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 59e711c6-09a6-314e-9eff-90adc0c2c195 | -0.77541 | -52.33521 | 2025-11-29 00:34:00 | TERRA_M-M | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9ca69b7-7333-3ed1-8a52-91f5b9db188a | -4.17298 | -43.76225 | 2025-11-29 00:34:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| f968a529-497a-3dba-8d1c-c203c6f75ffe | -3.42038 | -50.00372 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2620d0f5-8839-34ff-83da-c8e6267616e7 | -3.32534 | -52.98719 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 102fb495-8f85-3f39-a521-260c49324dd4 | -2.74622 | -49.86293 | 2025-11-29 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0f338c1d-740e-3a52-b2cb-58d59451ff1e | -3.88974 | -40.76063 | 2025-11-29 00:34:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 3e82bf13-ed72-31de-9c18-46102ff77d61 | -2.96519 | -45.58458 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0ca788a6-66ef-3788-aae2-74fb2fe6b7aa | -2.91286 | -53.07829 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 42898fc9-862e-3782-a978-a3977844af07 | -2.72219 | -45.20992 | 2025-11-29 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ffc7dc02-9c5e-3024-88a4-5894f1114b25 | -3.08031 | -50.34822 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fd7dd43-725a-3568-8a29-9158f8d5ec70 | -3.94803 | -47.03673 | 2025-11-29 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 53b49414-292d-31d4-804b-bb728b4a2ff8 | -2.5565 | -46.00951 | 2025-11-29 00:34:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| db67a725-8e83-3f70-a0d2-3f80313cac8e | -3.47894 | -51.36203 | 2025-11-29 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4661c292-eb64-3fea-b673-7bc81a9aec17 | -1.12508 | -47.74199 | 2025-11-29 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e5656e7c-4e34-3035-9a68-39843ea7121f | -2.60647 | -45.64479 | 2025-11-29 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 77c88978-89e0-31b4-8940-92cc2a110ff3 | -3.98491 | -49.03403 | 2025-11-29 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b660e4b2-7334-31b0-be6d-86d7a83547d1 | -2.35331 | -47.46796 | 2025-11-29 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ad3c4bad-c686-331a-968b-ea33b7fd5ca4 | -2.42243 | -47.23243 | 2025-11-29 00:34:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| e9d8720a-f706-3fee-b5b7-0bc3e22766bc | -2.43726 | -46.36895 | 2025-11-29 00:34:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 06cf1cd3-f989-322e-92fc-11aac4802294 | -3.47128 | -52.98462 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebd09105-398a-3401-ba1c-0ad5b2f7bb08 | -3.17426 | -52.42466 | 2025-11-29 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f6aa90e4-8113-3bf0-83a9-2c4771000118 | -1.48155 | -45.78408 | 2025-11-29 00:34:00 | TERRA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 104.7 |
| a2114ee6-40b3-360a-afd1-01c9cfd705f4 | -3.24899 | -50.6919 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c48b30e-32ef-34d6-8505-7b7ac7e0edbe | -2.96518 | -45.24753 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 112.6 |
| c27a68fe-9b23-3edb-ac85-5aa1d61e1943 | -3.9321 | -47.56636 | 2025-11-29 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 23b89ddb-7b0f-3aa7-99fb-bd89dfe0c106 | -2.96482 | -49.18719 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3b46b0ff-f798-3b4f-88cf-98655a2cff24 | -2.64889 | -47.38195 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 15a7abb1-a092-39f1-abae-a370cd07336e | -3.42878 | -45.36405 | 2025-11-29 00:34:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 071453a2-68df-3e64-a5a5-4ed5a3dbcd77 | -2.06921 | -53.22645 | 2025-11-29 00:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ba4626a-d997-3d7c-bf68-b5fea1420f5c | -2.77436 | -45.49212 | 2025-11-29 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b9cb578a-d840-3f92-97d4-3eac265872cc | -2.9037 | -50.40353 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d68a679d-769c-32ad-b945-81490f3a1a66 | -3.61825 | -50.37182 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 56c857d1-18af-389b-ae53-82179c4f1bbf | -4.47451 | -50.09871 | 2025-11-29 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 525b13f1-fe2d-3cf2-971a-6d2397f81ef3 | -2.74505 | -45.25575 | 2025-11-29 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 34560493-532b-3499-b263-29f5603bc2a3 | -2.39407 | -49.38049 | 2025-11-29 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| b4568c04-f96d-3d87-bc5b-fdc763b4e584 | -3.10021 | -45.79493 | 2025-11-29 00:34:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 40e23a19-c390-3747-8373-0f0e6a57478e | -2.46457 | -45.84751 | 2025-11-29 00:34:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b755339a-02b2-37ce-a6dd-f262b8f322a0 | -3.40732 | -47.19079 | 2025-11-29 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 98b453e1-6fc4-302b-8a12-04e17198b326 | -1.33411 | -53.1713 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2d3c0049-bf7b-3419-a730-6731f2d69b58 | -2.34579 | -45.70729 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 5f63d68e-e5a7-3d62-93aa-36102ed83d59 | -3.89593 | -40.79991 | 2025-11-29 00:34:00 | TERRA_M-M | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 6f1b3528-276c-343b-8eab-fdaa80aba191 | -3.40719 | -53.26233 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8fcc5cd6-614d-3c2e-bc7b-16210a6ac6e6 | -3.32104 | -50.28665 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 57257962-6556-3267-9354-92c77fc7bfb2 | -3.55509 | -50.30817 | 2025-11-29 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 375f62c7-74cc-3bda-9e18-f6aa7108cb57 | -4.04156 | -50.7022 | 2025-11-29 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 292cbbb0-4bad-3b20-ba95-248f3ae1b303 | -1.28826 | -53.17771 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| ae22ea6e-32fc-31ae-a0ed-e422de9d734e | -3.76476 | -52.63118 | 2025-11-29 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 04a69390-e4ff-38f2-b437-19d756630395 | -3.67736 | -52.5372 | 2025-11-29 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9e62808f-50fa-31f8-9838-f0c1701b54d4 | -2.84155 | -51.80983 | 2025-11-29 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| faf9d877-f36f-3719-b75a-037a1c6af2b1 | -3.51065 | -47.19584 | 2025-11-29 00:34:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1dd0b0e3-7633-37ae-af06-0aa2d37efc2c | -2.95419 | -49.17883 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 74bb456c-53b2-3dfe-a5f3-4c1794fba04b | -2.91609 | -45.25488 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cd6706b8-63fb-3373-b94d-e04f2ca57363 | -2.95907 | -50.9994 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d40937c5-5985-3253-91ea-2be1e4c030d9 | -3.67609 | -52.52778 | 2025-11-29 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2e2e6da-7632-33d0-8d4e-1d283aef4c30 | -2.82476 | -52.36007 | 2025-11-29 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cca631ca-e729-3e71-9833-5019c4c1c03c | -2.78798 | -47.43811 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 5e978bca-822b-3f00-ad87-00170e44445c | -2.91155 | -53.06857 | 2025-11-29 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 1809e293-71df-3490-be71-3bc67c342b58 | -3.88752 | -40.76809 | 2025-11-29 00:34:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 8143053d-b408-3bdb-a9d7-85d07f7424a8 | -2.93026 | -45.29581 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d45226d8-7b52-37d2-86b3-8758f1b1baf0 | -1.38093 | -52.51012 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 067cc47e-084f-3b10-ab7d-3c2a42786418 | -2.57417 | -49.09707 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a587fc5b-adb6-3dd6-bff1-1025448953ea | -1.12334 | -47.72955 | 2025-11-29 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0da9d3a7-3260-306b-8006-1cf4d56636e7 | -2.61228 | -47.34887 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| deea7426-72be-32fc-b407-c427660e1f1d | -2.35363 | -45.71775 | 2025-11-29 00:34:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 9d512467-2385-3e65-b0fe-72c0ad8f9fab | -2.22834 | -47.5108 | 2025-11-29 00:34:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| cc87d4a9-d12b-350a-9de6-6ce7ce1c164d | -1.37073 | -52.50232 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ecbe8ef-f50d-3e4f-9e7b-921584f62f4f | -2.62924 | -48.4874 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| afcf97d8-e21b-30a6-bb65-ff93deb7a1cd | -4.96136 | -48.18612 | 2025-11-29 00:34:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| be9e17d3-9639-3e4a-801d-16146bd62544 | -2.11014 | -46.07887 | 2025-11-29 00:34:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c92cc809-85ed-3a60-98c8-d098d6870d74 | -2.96923 | -45.57346 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 08ba5f29-55d3-3a8d-831c-f3f681fd25b7 | -1.08567 | -53.17928 | 2025-11-29 00:34:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 99bca759-b133-37d2-bda6-5ab40b1fa48f | -4.01407 | -49.10843 | 2025-11-29 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b7af0c13-f06f-3127-99db-218824d416e1 | -2.62844 | -48.5524 | 2025-11-29 00:34:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| d28d9f34-0e44-33ef-ac9f-db9f562cac3c | -1.2915 | -55.42736 | 2025-11-29 00:34:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e3d4fcb3-059e-3fac-bf1a-3aabb2ee8177 | -2.70545 | -45.69311 | 2025-11-29 00:34:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 18.1 |
| d8205608-b11b-31fb-bf0d-eecaa34a20a6 | -3.94563 | -48.44201 | 2025-11-29 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cc0114dd-0d6c-3d0b-9836-748c954c817f | -2.65065 | -47.39454 | 2025-11-29 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a6d69fa1-0d0c-351d-a735-dc9720a6b5b1 | -2.97465 | -45.56607 | 2025-11-29 00:34:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b9ade2bd-c5eb-3144-8ca0-6d092f0a4c42 | -2.95556 | -49.18853 | 2025-11-29 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e0ef4130-82a6-3596-b30f-4addcba78681 | -2.23548 | -51.56747 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7410009f-6edc-3a9c-8b2e-b9b7e846e38c | -4.06279 | -54.81538 | 2025-11-29 00:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4f463180-e49d-3c28-b782-7f0fcfa077ed | -3.23271 | -50.31447 | 2025-11-29 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README6.md)
