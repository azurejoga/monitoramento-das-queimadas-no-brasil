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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb24d085-407b-31e9-807c-0294cff2b300 | 3.2918 | -60.8756 | 2025-12-09 00:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fc13a39c-ed7d-30ca-9471-c9431c7c2aa8 | -1.5087 | -46.7647 | 2025-12-09 00:00:00 | GOES-19 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f6c8a7f8-cae5-34c5-9edc-330e88a4c584 | -3.4264 | -41.6423 | 2025-12-09 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 199.1 |
| 135644f3-eda0-362f-bdc5-75f23547e05c | -2.7374 | -45.3102 | 2025-12-09 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fe003f78-7bdf-3f5e-8560-d1445faa24c3 | -1.459 | -53.4723 | 2025-12-09 00:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f535c863-8c98-38d1-9c06-064a2b501eba | -1.5086 | -46.7867 | 2025-12-09 00:00:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 46163bee-0154-38ac-999e-1936a97d64ae | -2.03 | -45.8459 | 2025-12-09 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1ddee262-c84c-32d9-a064-ece6161f4c62 | -3.4262 | -41.6662 | 2025-12-09 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 256.7 |
| 2b9b6f59-5d89-3c74-a4a7-891eddbfe2d1 | -2.0301 | -45.8236 | 2025-12-09 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 3c5f7005-0c8d-3a37-bff8-7efaed4fbd2f | -3.4449 | -41.6653 | 2025-12-09 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 358.2 |
| bd825e4d-6c12-355a-b6fa-e5c0af8ab752 | -3.4451 | -41.6413 | 2025-12-09 00:00:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 288.8 |
| 97f428bb-6999-3a05-be0c-14a73dc961d9 | -2.0301 | -45.8013 | 2025-12-09 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| e7dcda83-7da5-30e7-a1df-fc40f3be5c07 | -3.4449 | -41.6653 | 2025-12-09 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 364.4 |
| ce01aae7-1969-3234-9b72-7849f4e4ce5a | -4.2773 | -45.9171 | 2025-12-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 17f43414-3ad1-300d-a5d5-fca9185736fa | -4.2958 | -45.9385 | 2025-12-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 313.5 |
| c3977514-17bb-3113-b69b-8187dcb4ec8b | -4.2772 | -45.9394 | 2025-12-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 2ccd4382-addb-3356-ac37-f934af2ed25f | -4.2957 | -45.9608 | 2025-12-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a64a4e0e-b4de-3ab2-b3dd-bb3e0dabb088 | -4.2959 | -45.9161 | 2025-12-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 94c9500c-931a-330f-b63e-98cb0b6dded4 | -4.3144 | -45.9375 | 2025-12-09 00:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| e20e4ccd-1d0d-388a-9e24-9da288c5afe7 | -3.4451 | -41.6413 | 2025-12-09 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 209.6 |
| e0fe3895-9298-337e-b1e2-683fbfd2f5c9 | -3.8389 | -47.8305 | 2025-12-09 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 8e72f6f2-f5ea-3cc0-a947-54ea38cae64d | -2.0301 | -45.8236 | 2025-12-09 00:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 162.0 |
| e265960c-4069-3911-a9e4-ae7f69f69fda | -3.4262 | -41.6662 | 2025-12-09 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 318.8 |
| acdf27dd-1a70-3bcc-8cfd-026da1e517db | -3.4264 | -41.6423 | 2025-12-09 00:10:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 185.9 |
| 88d6842c-c9ff-30e3-a1e0-81fa07030445 | -1.459 | -53.4723 | 2025-12-09 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| da13c5db-0bc2-39fe-abe6-53113a11d511 | -5.7089 | -42.072102 | 2025-12-09 00:17:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46632329-520c-3837-ae61-9b241df39afb | -10.0003 | -36.327999 | 2025-12-09 00:17:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a42ac740-07fa-38e3-8771-176ba6e7fa39 | -5.2556 | -37.7318 | 2025-12-09 00:17:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| c8801fb8-2c4f-3463-8e4c-00edd9a235b7 | -5.218 | -39.264301 | 2025-12-09 00:17:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1b9bf2fe-4173-39db-96b9-e9196372f04f | -5.7073 | -42.064999 | 2025-12-09 00:17:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 136518bc-1b06-3a4e-b37a-dd56e69a8415 | -2.369 | -45.863201 | 2025-12-09 00:17:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 875edc46-a03f-3c93-bb8f-ef3757f8e8f0 | -6.604 | -39.540199 | 2025-12-09 00:17:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b870734a-d6eb-3208-be6c-803426851e62 | -4.2943 | -45.950001 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 139591a7-854f-3859-9fdd-8032c6440d14 | -3.6782 | -43.6049 | 2025-12-09 00:17:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06678ef6-dbd5-3ab5-9e6e-bab9e305f76e | -3.8429 | -47.828499 | 2025-12-09 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d788fda-27e6-3926-a47c-213077e80296 | -3.4747 | -43.3922 | 2025-12-09 00:17:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c70a7f6e-8753-34f9-a56f-ea8d23e5ba9f | -1.5235 | -45.816799 | 2025-12-09 00:17:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 84429c88-df84-31ad-b133-c62ca1101b21 | -10.436 | -36.8377 | 2025-12-09 00:17:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 670fe590-ee97-3b86-a82f-dea20e05d653 | -3.8449 | -47.837799 | 2025-12-09 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3389daa1-ce89-304e-a576-b2b246828af8 | -3.3374 | -44.053101 | 2025-12-09 00:17:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d46da0a-7dbd-3d64-9031-af574359853f | -4.2926 | -45.942402 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dff96410-ca8f-3c96-aab8-74589d8d31d4 | -6.4696 | -39.234402 | 2025-12-09 00:17:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 85fc2254-a3d1-31c9-8597-e368c1d93df7 | -2.6267 | -47.3148 | 2025-12-09 00:17:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 811b7cba-6afd-3b2b-bf12-30a3ef41d93a | -2.3706 | -45.870499 | 2025-12-09 00:17:00 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b83dddf-ff23-369a-9e6d-4a51565c8c10 | -2.3184 | -45.550701 | 2025-12-09 00:17:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 998ff0a2-6a25-32ec-94c0-c3f6c21db0e1 | -2.3265 | -45.586201 | 2025-12-09 00:17:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7192d7d2-b6c1-3373-9d89-60695049d412 | -6.6019 | -39.531502 | 2025-12-09 00:17:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d07bf66c-add1-3209-9329-9d3c6f300065 | -10.4387 | -36.848801 | 2025-12-09 00:17:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3add614-b9b6-39d6-bf0c-2b752aed6f14 | -1.5218 | -45.8097 | 2025-12-09 00:17:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 674e28e7-376a-3701-b476-c66d0c44de82 | -2.3788 | -45.861 | 2025-12-09 00:17:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9fb36ce-4154-33ce-a69b-806e0f52945d | -10.4485 | -36.846401 | 2025-12-09 00:17:00 | METOP-C | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fbb31937-870f-3658-9343-ee9d16761347 | -8.483 | -40.505798 | 2025-12-09 00:17:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| acc488eb-c22f-3d6d-a9bb-3044bd23dae8 | -3.7403 | -44.552898 | 2025-12-09 00:17:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 308fa620-c8a3-34bd-840d-86da1073de9e | -4.2892 | -45.927299 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98b85fc4-b4fb-3ed0-b494-4a1178776cc1 | -5.0037 | -41.299801 | 2025-12-09 00:17:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 739f8a15-c7d9-3b85-98f8-fe1a1e2e3b30 | -4.3025 | -45.9403 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2ea2bf5-98c6-3ed8-8bb4-4a839a9ef5f7 | -4.3008 | -45.932701 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4482d7ef-f690-3e51-bf51-0ecb87401858 | -6.053 | -39.436298 | 2025-12-09 00:17:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 44d51451-43e5-3638-baae-2a657420cb86 | -2.6365 | -47.312599 | 2025-12-09 00:17:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f02be2de-22e0-3017-9bda-79a6608cdfc6 | -2.3804 | -45.868301 | 2025-12-09 00:17:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fc9ee1d2-7932-3c60-b3a5-a3ec3735df7a | -4.9587 | -40.531101 | 2025-12-09 00:17:00 | METOP-C | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 38caadec-4db5-3ccd-b4e4-ea24859be073 | -6.0551 | -39.445202 | 2025-12-09 00:17:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 71c66cc5-549e-3e8a-a786-9e5068570765 | -2.3754 | -45.665298 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9824b509-b67a-3a42-ae8e-76567ca28524 | -1.5202 | -45.802601 | 2025-12-09 00:17:00 | METOP-C | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23a4569d-f9dc-3e5d-80d1-aec800b55e15 | -6.4016 | -39.513699 | 2025-12-09 00:17:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0ff0fceb-7dbb-3076-bc5d-874c19c8f8eb | -5.2158 | -39.254902 | 2025-12-09 00:17:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d26a2e75-bbfc-3176-b7a5-380785920102 | -6.5942 | -39.5425 | 2025-12-09 00:17:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 20d84a00-360b-3a3c-86be-9cf34e41a2c3 | -2.7407 | -45.323399 | 2025-12-09 00:17:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fba91d63-de66-33a5-b4ae-6a6fd051b444 | -6.7162 | -35.1022 | 2025-12-09 00:17:00 | METOP-C | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6be82823-eef0-3c04-8fcb-669809435f0f | -2.377 | -45.672401 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 55dc205e-77b3-3013-bc78-c24ed44dc718 | -3.9326 | -40.731998 | 2025-12-09 00:17:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0a80eddb-b2da-31ba-a014-177ae1fd2e8d | -2.3786 | -45.724701 | 2025-12-09 00:17:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 765c28c1-d46f-3871-a4c9-4015c475878a | -6.5921 | -39.533798 | 2025-12-09 00:17:00 | METOP-C | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9fcbb151-b4f7-3781-a2bb-98f29dd06195 | -2.7391 | -45.316299 | 2025-12-09 00:17:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b78f9979-4be9-3638-81ea-a1b7d6a47124 | -2.3249 | -45.579102 | 2025-12-09 00:17:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97a8be17-7ccf-3d8e-bd73-f8d930147b3a | -2.377 | -45.717602 | 2025-12-09 00:17:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd2f92d1-fc2d-37f3-9dc5-16144f339550 | -4.9606 | -40.5392 | 2025-12-09 00:17:00 | METOP-C | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5d36d3f1-6dac-33f7-b0c7-af88f05e1d45 | -4.2991 | -45.925201 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8475c2d-0d1b-3281-a07c-eca84518bf06 | -3.339 | -44.059898 | 2025-12-09 00:17:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6973c9f9-bf3e-33ef-be2d-8f5bdda525b6 | -9.9973 | -36.3158 | 2025-12-09 00:17:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3cea7e49-fa38-307a-b3d8-8533ce38e7c3 | -3.8408 | -47.819302 | 2025-12-09 00:17:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cbc6cbe-2dd9-3db1-801e-205cd3bffccf | -4.2909 | -45.934898 | 2025-12-09 00:17:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0af71c52-ea22-3036-8864-c81930cd755f | -6.4599 | -39.236698 | 2025-12-09 00:17:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b3428c25-78ec-3641-b4a9-c6fcf460e3bf | -5.2528 | -37.7202 | 2025-12-09 00:17:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| cd32f611-dc66-3699-817c-72c3c35943e8 | -2.3232 | -45.571999 | 2025-12-09 00:17:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb58119-208e-3377-a7e8-44f12857d48f | -2.3754 | -45.7104 | 2025-12-09 00:17:00 | METOP-C | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1be9bcc-db3e-3059-bf51-6c3a84893875 | -3.2667 | -45.415199 | 2025-12-09 00:17:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a16db5f-fadd-3ed9-b5be-2e081c0be6d2 | -6.3996 | -39.505001 | 2025-12-09 00:17:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a524daa4-335f-328c-abe9-a4091a71153c | -6.4718 | -39.243401 | 2025-12-09 00:17:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b5623365-b1b0-340c-b4c3-be3211f8aea4 | -3.9345 | -40.740101 | 2025-12-09 00:17:00 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 5f21723a-4a4e-3dd1-8440-900ce8610909 | -4.2773 | -45.9171 | 2025-12-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a994320c-7a4a-3137-bd61-5d8cbee9bc10 | -4.2957 | -45.9608 | 2025-12-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5c8d286b-9ce0-3f1d-a1fc-a815d194b4dd | -3.4262 | -41.6662 | 2025-12-09 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 230.6 |
| 11dbd423-e6b4-3842-8249-087fd90e55d0 | -3.4451 | -41.6413 | 2025-12-09 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 265.9 |
| 55005780-964d-334a-9ce5-4b874f0eb457 | -4.2959 | -45.9161 | 2025-12-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 150.5 |
| d9c7d5a5-316d-3148-9f1f-10309cd1f4cb | -2.0301 | -45.8236 | 2025-12-09 00:20:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 04a035ff-b3e2-35d0-a5c8-87c2739b6be6 | -4.2958 | -45.9385 | 2025-12-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 313.9 |
| ecb3de5d-22fe-3f12-9268-c3d1e29e2f89 | -4.1821 | -46.2782 | 2025-12-09 00:20:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 45b76c2d-c55e-33a9-8a80-f81916c11f4f | -4.2772 | -45.9394 | 2025-12-09 00:20:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 854ce535-4e8d-3363-bc6c-4e542da3acb3 | -3.4264 | -41.6423 | 2025-12-09 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 203.0 |


[Clique aqui para ver as próximas entradas](README2.md)
