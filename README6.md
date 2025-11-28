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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 750d4632-c9c5-3c26-bd60-97bddb5b5134 | -6.10923 | -44.71226 | 2025-11-28 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bb1dd30-6e77-3325-88d8-66c7982ea02e | -4.52769 | -44.61664 | 2025-11-28 03:42:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6452501-c578-3ee0-af5c-e7f8fcca85fa | -4.7273 | -46.44427 | 2025-11-28 03:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3c30e23-f699-366f-b5c2-fc0d2b7d790d | -3.08666 | -40.66185 | 2025-11-28 03:42:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4542b349-60e8-36df-a353-bdcd190d8c23 | -4.94261 | -41.14632 | 2025-11-28 03:42:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 54ecde90-d2c1-3b39-bebd-195db834d34d | -5.34756 | -44.88449 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4657acab-db1d-3538-ac29-8c1303da3510 | -4.94852 | -41.19154 | 2025-11-28 03:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 972eab37-fafb-37b5-8829-5b0b05b9f9cf | -7.52081 | -40.582 | 2025-11-28 03:42:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba3f5bb2-9029-396c-a2b4-2bc0c012f13f | -5.29648 | -44.72663 | 2025-11-28 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3321386-d258-367a-920f-5aa1ea6ac8e9 | -2.41927 | -47.23465 | 2025-11-28 03:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d545bc9b-e225-3068-9358-5395b9bd7e28 | -3.51639 | -43.68015 | 2025-11-28 03:42:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed7072bb-4018-3fcb-a7d7-bc314d5f9ba2 | -3.32032 | -44.16406 | 2025-11-28 03:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fee3484a-45b9-3521-9ded-ddd61c73da79 | -6.85845 | -39.35652 | 2025-11-28 03:42:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81f55aca-37c9-3b96-8729-a9a5a61c1ac0 | -4.9478 | -41.19588 | 2025-11-28 03:42:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a4f4140-eab6-3035-a8d2-dc55208b9e17 | -5.34914 | -44.88571 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5e87a74-7eab-3937-9d9d-0676ed3e642d | -5.1014 | -46.1154 | 2025-11-28 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da7d2ae9-fdf7-38cc-bc60-9903ad0e2c19 | -7.45785 | -34.81339 | 2025-11-28 03:42:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ab2038e7-26fc-367b-bc15-923905a7335f | -5.54347 | -39.24049 | 2025-11-28 03:42:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71e6a675-1549-3ada-92bd-b211e0acf814 | -5.06137 | -40.82372 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1f3cff62-cbcb-3231-bff9-627433e82b63 | -6.24047 | -40.30035 | 2025-11-28 03:42:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fd1a314c-319e-34d3-b58d-0c1ed1ec027c | -3.0594 | -40.08517 | 2025-11-28 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95c17c90-57e1-39e2-9def-eea54de17e8a | -6.65831 | -39.32306 | 2025-11-28 03:42:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 220f1993-627f-37b7-a476-614e0bb73a16 | -5.10187 | -46.1177 | 2025-11-28 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 514b50ac-7c2e-3aa3-b540-d827380f9144 | -3.08733 | -40.65772 | 2025-11-28 03:42:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 1cf86f88-b3cf-3392-b490-2690509b5cde | -4.93824 | -41.14565 | 2025-11-28 03:42:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 699775ad-baa6-36f0-8ab6-e38cd7256d78 | -4.72637 | -46.44938 | 2025-11-28 03:42:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aac4161e-5ba3-3d3d-a6ff-894b4c8a8ee1 | -5.84392 | -42.5953 | 2025-11-28 03:42:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| e0bf2489-5984-3bb7-a2f6-748421d0b596 | -5.84333 | -42.59402 | 2025-11-28 03:42:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ba851241-35d7-3b3d-8508-9e2d840c598b | -5.05779 | -40.819 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e219d217-dced-3aa4-b5dc-bf2223763042 | -2.70817 | -47.41379 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70c2c85d-e84c-3c39-9bf3-b051e8a9ab1b | -4.25302 | -46.24235 | 2025-11-28 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4be9fc4d-0069-35b0-b2ad-583ce7fddfb7 | -4.94093 | -48.63011 | 2025-11-28 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8ef84cb-bc7d-3d79-b6b5-2f4b31cab285 | -4.04427 | -40.44995 | 2025-11-28 03:42:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7a5c7dcf-e182-3285-adba-108a21b645eb | -3.34787 | -45.42976 | 2025-11-28 03:42:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d79a4ee1-b11d-3154-ae58-16c825068c1d | -4.97395 | -44.82249 | 2025-11-28 03:42:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d585a82b-2ae9-3e2d-ab84-3f4fc2ea1168 | -2.70732 | -45.21714 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dca94870-5b71-3dff-b1b4-611ce7e26d7a | -6.72368 | -40.82344 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 41617d5e-bef9-3a10-b082-708c89c23164 | -2.71919 | -45.21934 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b234d12e-41f0-3476-b2ef-22615e23bd09 | -6.1044 | -44.7077 | 2025-11-28 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e01fdbe8-e5b5-3a0f-9621-f776f3b5286c | -5.0663 | -40.82043 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 97092ca2-1cdf-332b-bc59-2231ef7b70b8 | -5.22977 | -44.92098 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f70d2b4-c857-3508-9538-d6031748daf8 | -3.66695 | -45.4101 | 2025-11-28 03:42:00 | NOAA-20 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8be698e8-3131-3805-9cc9-3092e529e5a0 | -5.06563 | -40.82441 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 64da3530-bb73-3bde-a73b-6896d1cfe04a | -5.74928 | -45.11209 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 18d2786e-026b-37d7-857b-ba63aabf317e | -2.71064 | -45.21552 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 99dc8014-c039-31f7-8536-78bd802a5595 | -3.093 | -40.06319 | 2025-11-28 03:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88a76d06-4f88-3e38-ac82-301ec37a7c24 | -4.30859 | -40.68995 | 2025-11-28 03:42:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92175479-709b-311f-a6cb-b0b314d355f1 | -3.75236 | -46.95749 | 2025-11-28 03:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe7c53d1-744e-3b4f-9f6c-75a37d206d6a | -3.75817 | -44.94936 | 2025-11-28 03:42:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b98a0ce8-0154-3446-8c39-51b6034b0997 | -2.71657 | -45.21663 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 469c7fc2-4c53-38e1-91a4-75cb2671fc5d | -5.30206 | -44.72731 | 2025-11-28 03:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb0aa2d9-6f6a-32b1-bb30-fb03a3dda94f | -5.75485 | -45.11344 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9fe778a-cccf-3f20-bfa7-582378c4fa71 | -3.34712 | -45.43414 | 2025-11-28 03:42:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3dc8ad86-d6b8-365d-bd00-55875df3e857 | -6.72434 | -40.81958 | 2025-11-28 03:42:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b1401c0f-f708-3dbf-8c72-d03b7b62ef49 | -6.10377 | -44.71132 | 2025-11-28 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bdba748-eb97-3271-bf48-7bc13bf55395 | -5.06334 | -40.81734 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44fe56f7-b7f5-3c6b-a1d0-03aa1076c625 | -7.37369 | -34.9181 | 2025-11-28 03:42:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f7b27c1-6e58-391d-9045-bc4aee6f614d | -3.66769 | -45.40576 | 2025-11-28 03:42:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c354e1b2-cc82-3578-b03e-3b7fb51b65ff | -4.2441 | -43.67844 | 2025-11-28 03:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a1bc63-9b5d-3ae8-a3c3-82c443c298b1 | -2.70989 | -45.21988 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| addf95df-d03c-3925-8c63-e57afc15e223 | -6.46814 | -38.86869 | 2025-11-28 03:42:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6f865a75-b3bc-38ca-95bd-c7c0a8554236 | -2.41822 | -47.24086 | 2025-11-28 03:42:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c42f37-469d-3e03-b444-a064da5ebb14 | -8.92967 | -35.17381 | 2025-11-28 03:42:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3fa15b2a-ebca-3dbc-9798-08e36695ae32 | -2.99024 | -45.42518 | 2025-11-28 03:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0bb248b-d3f0-3714-a2e6-118fee9bdd18 | -5.97079 | -35.28462 | 2025-11-28 03:42:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ac23e85-62ce-3e83-b323-10863d939209 | -4.0485 | -40.45063 | 2025-11-28 03:42:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 15d6ead8-c57c-3359-916a-a5dd5428ccd9 | -4.24466 | -43.67522 | 2025-11-28 03:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9603a713-2227-31d4-a0a1-8f2ee938ed49 | -2.4236 | -45.75306 | 2025-11-28 03:42:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80790c72-c353-3863-8078-5920f48c827d | -2.2301 | -47.51567 | 2025-11-28 03:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 924e4e6f-6864-3466-80fd-1278bec79661 | -8.81892 | -36.96728 | 2025-11-28 03:42:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f3a2caa1-d4c4-395d-b2dc-5e40b06c4cee | -5.59546 | -35.63608 | 2025-11-28 03:42:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d9b7ac1-a326-38d9-99e0-98306f4bb004 | -4.53325 | -44.6176 | 2025-11-28 03:42:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27b9bfb1-7568-332a-a43f-4da43f08c22b | -7.92958 | -37.8274 | 2025-11-28 03:42:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bb166804-47cf-374d-b2f6-366bb2117f84 | -4.53437 | -44.61863 | 2025-11-28 03:42:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b120dd53-b846-311d-8a9f-1e1cafbdbaf9 | -4.254 | -46.24553 | 2025-11-28 03:42:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9d919512-6a25-338f-aff9-6a98b0a741d1 | -2.4244 | -45.7483 | 2025-11-28 03:42:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04aaa9d7-2bbb-31eb-a0fe-03a20edd83ff | -4.29918 | -48.61055 | 2025-11-28 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 963d207d-722c-34db-b69a-8e12cfbb61af | -4.60305 | -38.58479 | 2025-11-28 03:42:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 16eca2a4-4b1e-3589-9a50-0c0ed4297399 | -5.06268 | -40.82138 | 2025-11-28 03:42:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 836492cc-8d16-3ab1-8679-3a4824c9b68e | -6.51902 | -38.87487 | 2025-11-28 03:42:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e38e7a0-11e7-38c4-9865-e88d9ff60fa2 | -3.63833 | -44.88332 | 2025-11-28 03:42:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e0c9f65-50bd-3369-aa63-d47a2ae15a71 | -2.71255 | -45.2226 | 2025-11-28 03:42:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 95784f97-b8b0-3414-9c3e-439e531208aa | -6.10985 | -44.70866 | 2025-11-28 03:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc9745fd-0c3c-3790-8486-866d4e90c5d4 | -5.5427 | -46.50847 | 2025-11-28 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0001c790-bbf5-3219-83c0-3dd3cdb53d0a | -3.75693 | -46.96993 | 2025-11-28 03:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 68e50a7d-2306-330a-8014-11c4f62d4262 | -3.86496 | -40.64642 | 2025-11-28 03:42:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2b3535f4-a17a-3472-a59c-de6c4fbefe79 | -6.50511 | -38.25293 | 2025-11-28 03:42:00 | NOAA-20 | VIEIRÓPOLIS | PARAÍBA | Brasil | 2517209 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 411c6695-32af-3a44-a717-7f5593e0d2f9 | -4.68578 | -44.42672 | 2025-11-28 03:42:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87ee6277-4604-38fc-ab67-4a06fc3d9a9f | -7.45731 | -34.81688 | 2025-11-28 03:42:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f64c0f35-5c73-302f-b5b4-77580aa32f3d | -6.96508 | -39.162 | 2025-11-28 03:42:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9daf7b9-07c9-327b-a09c-56797ae65900 | -5.63831 | -39.45741 | 2025-11-28 03:42:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f55f730-25fe-3ecd-8061-2b78df57439b | -2.61258 | -47.34945 | 2025-11-28 03:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fb129e93-0aa9-3e81-9369-103a704e123b | -5.57625 | -45.16995 | 2025-11-28 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a29bd9b8-0100-3938-97b0-dbcd5d318eb0 | -4.52881 | -44.61765 | 2025-11-28 03:42:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86331076-fd6b-3816-8c55-654bf7200000 | -6.28157 | -38.42546 | 2025-11-28 03:42:00 | NOAA-20 | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7971ce1-8a2c-3a53-bed0-b7213681abdf | -7.73085 | -40.72182 | 2025-11-28 03:42:00 | NOAA-20 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 68fa2e66-f18d-3669-b8e1-06ee12633e5c | -3.76519 | -47.14705 | 2025-11-28 03:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae9d85d3-42a4-3f3c-863e-cbffc16bd9f2 | -5.10277 | -46.11271 | 2025-11-28 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 186f82a2-5dc3-3770-925a-9de6e36d2c9e | -7.72307 | -38.43169 | 2025-11-28 03:42:00 | NOAA-20 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e368fb3a-6700-3b91-9f30-7e07fb44c8da | -6.74208 | -39.07164 | 2025-11-28 03:42:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README7.md)
