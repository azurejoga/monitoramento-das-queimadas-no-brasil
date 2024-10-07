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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87858a6d-32e7-3c79-ab4c-6f732f53a3c9 | -17.00875 | -56.72255 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 6b5e3635-7871-3ae2-a8a7-920064f8b364 | -17.00747 | -56.71274 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 8d9bd06f-589a-34e8-b3aa-645220b74040 | -17.00683 | -56.83929 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 8812a992-e2f5-346a-86c5-105a6efb1355 | -17.00619 | -56.70293 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| f534c85e-1b9b-3c6c-8444-7faf85374b9e | -17.00551 | -56.82939 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| e26597bf-9f64-3b64-9ce5-6a9bc04b2ccb | -17.00154 | -56.72953 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 33e29b84-9441-3911-8fab-6204fb2ae45a | -17.00023 | -56.71973 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| c87e6c09-b6e8-33fe-8a6f-153f1df0bb84 | -16.99892 | -56.70993 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.2 |
| 580290ba-5fa3-3b23-be0d-15adbce69b35 | -16.99761 | -56.70013 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| aa6f9d91-cd47-3466-8e9f-bb66abe6bb4f | -16.99635 | -56.83072 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| f8fb96f5-da6b-330a-9c07-d1c964c7aea6 | -16.99504 | -56.82083 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 69f9fda6-4182-3a8c-96a2-5e0106ae8ac3 | -16.99241 | -56.73087 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.1 |
| 0d27e4b0-4db5-3d55-ad80-1345323d25db | -16.9911 | -56.72105 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 119238c6-8ccc-33e3-a58b-09e796137c12 | -16.9898 | -56.71125 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 00b46ed5-2edc-3a25-a5f0-6361de6d4eda | -16.98849 | -56.70146 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| ff794bb3-3c7a-3681-8df3-b14de47a39c7 | -16.97541 | -56.81359 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 459b4fd9-ba9f-31d9-8adf-0ae4d1269f9d | -16.97411 | -56.80372 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 98b93dd1-8159-3f7d-83d2-da3b4c6602de | -16.97151 | -56.784 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| fcffdefd-1507-3141-a7c4-5224278877d7 | -16.96891 | -56.76432 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 4cbafab7-87ec-39b3-887b-670b00ea3d7a | -16.96761 | -56.75448 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| b1e9fdc4-b42b-36e3-8cbc-e3d86bd8800e | -16.96625 | -56.81491 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| ea84d0d3-ddc0-3724-9e90-3efe6c106c48 | -16.96495 | -56.80505 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| e087eb81-cfa4-3dc7-9f0e-0bb0f9c8e1c3 | -16.96236 | -56.78532 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 8daa18e9-a6a1-35d1-8f28-e7f0be158037 | -16.96106 | -56.77548 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 83b644c0-90f5-3dcb-9176-793389c72bbc | -16.95977 | -56.76564 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 700cadb0-4ec3-3a01-8974-3f4b884026d6 | -16.87301 | -56.7345 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 96696e8c-58c1-35a2-b508-b4914b685396 | -16.86388 | -56.73583 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| db3eef9c-593c-3016-a94f-5cd6ba0b13d3 | -16.8613 | -56.71626 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 52fec76c-8059-30da-8436-650deac2feb5 | -16.85605 | -56.74696 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| ee109778-d934-36c2-a4f6-6d1ef3d2f033 | -16.85476 | -56.73716 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.7 |
| cbae7034-d97b-3d74-b554-bb50c8fc43a4 | -16.85218 | -56.71759 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5b5ea7f6-4c6d-3384-9225-55b4d7dfd851 | -16.84692 | -56.74829 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| cff979a4-085f-3c54-ab15-47f751e1da8e | -16.84563 | -56.73849 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 54def8c4-77ee-3f1a-9694-47048ced6581 | -16.93747 | -57.71185 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 3b51bc3d-2d88-3938-a22e-f71d76b2513a | -16.93608 | -57.70108 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| d56d943f-ba12-3165-baa0-911c3fb0f58e | -16.92653 | -57.70241 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 4056e803-7c2b-3084-9c68-b745f9584e60 | -16.82155 | -57.45344 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| f2d2c8f9-054c-3a92-8d11-9f5c7da7bb11 | -16.81761 | -57.49664 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| c3f1b0f0-9bde-3cce-822a-2b174b39e31a | -16.81705 | -57.37362 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| cb9122ac-6d65-3b6a-a100-8b02f17e7e3c | -16.81199 | -57.3806 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 3fdd0d9b-b767-32af-9170-798dd4a7583f | -16.81078 | -57.44433 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 5ca28f6f-233a-329e-922e-e2da708a91d8 | -16.80942 | -57.4339 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 7e573f58-577e-3b76-bc75-9493b6278b3c | -16.80533 | -57.40268 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| e6c332d1-2ed4-3da4-b756-cd467df3d85a | -16.80397 | -57.3923 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 67bdc37a-5263-3d93-b3e8-eb08ac10a512 | -16.79595 | -57.40401 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| 06a24ebf-451b-3168-9c8b-dcac8265b681 | -16.79459 | -57.39363 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| 4cfdcd93-5fd2-3348-af06-8c7394d5dfe1 | -16.79061 | -57.43655 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| ef44339a-2af7-33ce-a026-331990202099 | -16.78791 | -57.41573 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| b24db39c-7637-3254-8f12-69d30a2c9c16 | -16.78656 | -57.40534 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 395ce170-de26-32ca-8e08-9715e2278a8e | -16.78121 | -57.43789 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.5 |
| 298b09e7-2134-3e57-a459-0d7982eae265 | -16.77987 | -57.42747 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 8e91d6d2-f2b6-3466-9371-4afd4e1fe482 | -16.77852 | -57.41706 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 1a136adc-6156-3241-b5e3-ba1b64c09b74 | -16.77719 | -57.481 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 97e42aa5-1a52-3b14-8ca2-1a21579fc29b | -16.76777 | -57.48233 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| dee6972b-d33e-3e26-a11a-a34d3a95fd80 | -17.13324 | -56.82898 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| c91181dd-e0e1-3ae9-a91e-c166f1df278c | -17.13194 | -56.81905 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 2dfcba2c-59af-347a-9f05-98b80c375fe9 | -17.13065 | -56.80914 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 7813cefc-e32a-39d0-a861-51a3a7049ffe | -17.12814 | -57.42853 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 4fdd2327-1d43-3b9e-a362-4581be33962c | -17.12806 | -56.78932 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.5 |
| 488736ef-df37-3f05-89ab-644785331a0c | -17.12677 | -56.77942 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.6 |
| 0eefddbc-04ef-3a24-9c39-a859ba859ad8 | -17.12548 | -56.76954 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 7e7a3690-3bbc-3ca3-8d14-2d42940392fa | -17.12535 | -56.84023 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 1309cdc8-448f-333b-a9eb-1ea29c489953 | -17.12406 | -56.8303 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 29bd4730-4325-3cbd-9be7-173b492f1aae | -17.12277 | -56.82038 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| fad21f95-ac8f-396c-a656-40d07e68efb5 | -17.12148 | -56.81046 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| ae0b946e-a694-3190-bafd-d452dcb481dc | -17.12144 | -57.3761 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 3f2d97ac-ed6c-311b-b7dd-662fdbb4e983 | -17.12019 | -56.80055 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.5 |
| d13ef60b-2615-39ca-8ee4-f1bcba1ba5bb | -17.1189 | -56.79065 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| effd1ae4-bb2e-317f-9206-27c2c5500c3e | -17.11871 | -57.42987 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 6e8c1cab-b9b4-3036-88d8-d9ab3b6ad6dc | -17.11737 | -57.41935 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 426d04fa-57fe-31d2-8bba-938e14a5f18d | -17.11617 | -56.84156 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| ea83f629-e26b-3866-b850-27c03685709c | -17.11603 | -57.40886 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 6de3d3f8-4e71-3a78-8d1e-eff1719af9d4 | -17.11488 | -56.83163 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.1 |
| 66aa2f8e-e812-38d9-80aa-6d75b2d115c7 | -17.1147 | -57.39837 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| b588b01c-3a44-3231-bfc3-d68e781d2363 | -17.11336 | -57.3879 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 0d4bc234-5ea1-3586-8592-be70bd47ad67 | -17.11203 | -57.37743 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.3 |
| 07da06a0-2260-3136-8dd9-1d91d554840b | -17.10936 | -56.84886 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| d75408af-309b-3e00-8a34-ba6d0ecc6b9f | -17.10928 | -57.4312 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 09bdd052-d40e-36da-a8c2-99e1982e31f3 | -17.10804 | -56.83893 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| 72a2a8ce-097a-3a83-9aab-8fbc609c3ac6 | -17.10794 | -57.42069 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| ea04ca8b-0a62-3cc0-a7f2-e92b4e33a446 | -17.10672 | -56.82901 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 342d58c4-fc21-304f-8908-76940599c9c7 | -17.10661 | -57.41019 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.4 |
| 6bfea049-0f57-3881-9a1d-b4da826eeb74 | -17.10528 | -57.3997 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| 178f8b53-5ebe-31e0-85a6-085fc452794a | -17.10395 | -57.38923 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 54f3b629-b20a-3a07-9948-9a800d186004 | -17.10262 | -57.37877 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 783abea2-3c24-3cf2-9593-9fc149170b9e | -17.09984 | -57.43254 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.8 |
| a3829656-7ba4-36e5-9c22-1a11654aba8d | -17.09886 | -56.84026 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.7 |
| a11b9887-cf30-35f3-b174-9bbea8524029 | -17.09852 | -57.42203 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.2 |
| 3e225cf0-e525-326a-a505-6da8c72af029 | -17.09754 | -56.83034 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| 3cab785f-49c3-305a-8a79-184424d49468 | -17.09719 | -57.41153 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 0b66f722-812b-33b6-acdb-97111678a8fa | -17.09623 | -56.82043 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| f369cd3b-0503-36e1-ba14-d3bbb6ce8d5d | -17.09586 | -57.40104 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| dfe063b5-572d-3d2c-9a3a-51c82f65f722 | -17.09491 | -56.81052 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 2d7a6e39-a549-3b82-b929-6cccabc66ab4 | -17.09395 | -57.42858 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| d44b1a35-5e57-342f-9771-a09c89815f25 | -17.09258 | -57.41809 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| caf36415-652a-3f48-bddc-7d8c3cdde50e | -17.09121 | -57.40762 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| c705bdfa-2d51-373c-99f9-3ac3867f2471 | -17.08968 | -56.84158 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.4 |
| 13744df5-ed33-3909-aa62-8dca49545010 | -17.08837 | -56.83167 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.1 |
| a8ca0e79-0b82-3904-ae77-b16a9fc6c5cd | -17.08706 | -56.82175 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 0cdc6f5c-6dd3-3b54-9c80-b261f47f7976 | -17.08574 | -56.81185 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |


[Clique aqui para ver as próximas entradas](README29.md)
