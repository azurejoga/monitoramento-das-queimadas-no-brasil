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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7450321-1121-39c5-9de6-60daed407bf7 | -16.41803 | -57.32711 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2352e64d-ea88-322e-881f-0d2cdb3de047 | -16.41163 | -57.33578 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f01591da-a4a9-31af-81bc-3c618db50f04 | -16.38705 | -57.38724 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 82d483e1-5453-3390-8919-404a935cac5b | -16.13924 | -57.58878 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0ac67888-c9d8-3769-8f4d-519208a7d115 | -16.13826 | -57.59381 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 23837caa-8d56-3811-8e61-baa954292c91 | -16.11861 | -57.55394 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 82b3009b-72c2-3f0c-9016-1fa6add01833 | -16.11777 | -57.55125 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 918c8e57-b349-3196-a8a7-072aafcda571 | -16.09515 | -57.55099 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bedbe6a6-09e3-3e60-887b-f1e724975487 | -16.03898 | -57.51861 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c0d223f-d35c-3d48-bb50-3c55f7a29074 | -15.96896 | -57.22181 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bb1fb7e-1030-34cd-bf73-2e0ec8a6d50f | -15.95515 | -57.21608 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1e40417-abdd-36db-9e62-740b4e0bfdd8 | -15.89228 | -57.47205 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb36a147-a5be-3fa2-8b2f-48c6e4ccf01e | -15.8885 | -57.46674 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 09528151-acfb-3dfe-bae0-6d99bc513db4 | -15.88008 | -57.46066 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e60323bc-7c1b-3f0b-885d-6a87af9ef4ed | -15.87925 | -57.46496 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d4828ed-b320-3103-b71d-c3c403a79682 | -15.87737 | -57.47478 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a2bc7745-3538-3de3-bce9-931fe329f719 | -15.68437 | -57.39476 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c28fa4b0-f035-363e-a060-f6446ca434fc | -15.62456 | -57.38189 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc0137b8-0d3e-3f3f-ac11-36ae0a4d76f8 | -15.60706 | -57.37334 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b57d829-4c6b-3b40-917c-273192988573 | -15.52866 | -56.89505 | 2024-10-08 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 985182b1-400d-3c8f-8076-9cc73399c470 | -16.14865 | -57.4189 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff08d7d4-1f19-3b06-a54f-b4074b69415f | -16.14754 | -57.59562 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 642bf76a-4546-3e6b-bf8b-a8a511035872 | -16.14496 | -57.41348 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b03094ce-3adc-3feb-8d25-bdbf4a7d2b1c | -16.14476 | -57.41599 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bf0d4f8-6f71-3062-bb97-4d8a421378e2 | -16.14408 | -57.41798 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09a7d3c9-4734-341e-bd5e-29a9d52fa0ae | -16.14384 | -57.5899 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 71d0c906-cf2e-368d-a1c2-62d2de3419c1 | -16.14291 | -57.59464 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d9850188-6a20-3194-9b36-c214e11a4ff1 | -16.14022 | -57.41483 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39c439f6-f172-3a1a-ac0c-67629d36bbd3 | -16.13465 | -57.58764 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 34f79542-7c70-3e6e-8870-98a592872323 | -16.12225 | -57.56006 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b992ac00-53d3-344e-8b78-11982dc78357 | -16.12149 | -57.55676 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 52391a35-0b03-3ce2-a8e1-20fc980f33c6 | -16.11761 | -57.55918 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 207c3006-1f6d-3152-8cb8-f5495603fd26 | -16.1169 | -57.55567 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9e1c700f-f46b-3277-b0a5-8386c8e1fd52 | -16.11608 | -57.58408 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 23c4c972-dc4c-3939-af6f-7fd7e2649785 | -16.10467 | -57.55146 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b40ab790-ea99-358d-8435-53c7a918c63e | -16.09992 | -57.55119 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 675437a2-a375-3401-bddb-7b4a3b05cf73 | -16.09606 | -57.54627 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c97889ad-a938-345f-9f77-347cabe83a56 | -16.03547 | -57.51206 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1774bb40-740c-34d3-9332-f0f5c57de5d8 | -15.96809 | -57.22625 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c99117f8-b92b-34a8-bfff-8c1300aeda48 | -15.96727 | -57.47488 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d07f6fa-34d0-3fd6-8448-8d259b64439f | -15.96266 | -57.47391 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17fcac4f-6a80-33c1-ade7-51f9014e83a0 | -15.95806 | -57.47291 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96e9553d-c42c-3d25-ac64-89768bb8cedd | -15.8997 | -57.48349 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa679dd5-aaea-351c-8509-47888db73e0b | -15.8914 | -57.4767 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07e5d55a-f705-3e56-8abe-ae1a5cfc2bee | -15.88388 | -57.46585 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 354979e8-75ed-32f8-b353-cc50fbcf7d77 | -15.87622 | -57.48075 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c154a40-1456-34b1-bcca-e9974e5708c2 | -15.87548 | -57.45961 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4776ff5-9f66-3049-9cf2-40944a4454a1 | -15.87266 | -57.47427 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e176b281-c2cc-316c-af97-9b4700d8fb01 | -15.77587 | -57.16515 | 2024-10-08 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67eff39f-e959-3ea1-a8be-c1f22a23394e | -15.68358 | -57.39891 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 763736f3-a221-3a49-8883-cebbd951bd3e | -15.64407 | -57.38013 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2df24c7e-4cc3-32b4-8aee-2aaafa9263e4 | -15.63952 | -57.37891 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 670772b9-7e1f-3186-b330-7cb987d6b113 | -15.63115 | -57.37265 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b78bbd6-308f-3c2c-abec-6e156b97b496 | -15.6266 | -57.37146 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1e3563-b2d1-34b1-84e8-7987062c4bc1 | -15.62206 | -57.37019 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29c554e9-2eb0-3760-9a4d-fbab43ef28e7 | -15.61989 | -57.38127 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6922c03b-2118-3d86-bfd0-360480b33171 | -15.61746 | -57.3692 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf9249c-005d-3b27-8028-a6073e3b97d7 | -15.60885 | -57.37056 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6269bda0-5e24-3804-a038-024164d748c4 | -15.60814 | -57.36782 | 2024-10-08 04:36:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e0356a3-7f33-318f-be38-7a1bcc58a627 | -16.65343 | -57.12887 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 1115b5f8-4ea8-31c1-bf93-373348da823d | -16.65109 | -57.13109 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ea8b22c2-7d06-346d-8760-a0b590493dcc | -16.65019 | -57.13571 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| aecc40e8-5a6e-3fce-9134-c14d1a1340fa | -16.64929 | -57.14033 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 0008bc9c-672e-3a5c-97e7-0004d79f0231 | -16.64811 | -57.13258 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 8e0d8f54-6e0d-3b86-86ca-5d4a09ec5893 | -16.64724 | -57.13721 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 277ac5b9-d247-3053-aea4-7e2c80388b08 | -16.64308 | -57.12466 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 09824615-4f06-35be-ba9f-843ab4bf45de | -16.62845 | -57.11416 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 677e3084-b14d-3b1d-a304-5558bf588ae7 | -16.57149 | -57.14576 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6d0b1c25-b90b-33e3-8ae5-0fc1ff584110 | -16.55546 | -57.71644 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 00fca3cc-9bfc-3d90-be42-30565bb3d522 | -16.55343 | -57.72674 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4cacd701-47d9-3a91-8305-481d94dcda45 | -16.54881 | -57.72575 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| efc4f09e-dc14-3e44-b36f-fd9f223f9bee | -16.50924 | -57.71537 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ddf9c66e-383f-3d35-8e73-62b893e60256 | -16.49427 | -57.71798 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 11bc8b4c-5e7c-3afe-88e6-9f9647052e9f | -16.49265 | -57.70146 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1462d50f-a605-3338-b62e-c6a132c9d6a6 | -16.49228 | -57.72832 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7fbde883-3f11-3cfa-8245-bfb4db5bc8b0 | -16.49165 | -57.70662 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c1cc060b-b2d7-3f24-b991-d8ac29367e73 | -16.44094 | -57.2573 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 529d1ecc-c70f-3f31-8acf-62a1dfed688e | -16.43882 | -57.34137 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 6f6aa49a-2a54-36b5-b2bf-7799762669d0 | -16.43734 | -57.25167 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e9e938f5-407f-333a-b103-86fa058eabec | -16.4355 | -57.26118 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 85d3cf7c-ee73-3276-9b49-39a480b81fbe | -16.43191 | -57.25551 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 4829abd5-90f3-3529-bf49-6cd86d4dfe62 | -16.42976 | -57.33951 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 346b45de-fceb-3db6-a770-94080bfb72b0 | -16.41616 | -57.33672 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4c7fd70d-7668-3942-b120-0bb3d5ed6be4 | -16.4135 | -57.32619 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3958b587-0ae1-3a74-a76a-2a9e958cc58b | -16.38675 | -57.39071 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d1f83795-7371-3aee-9f47-35697993125f | -16.38614 | -57.39207 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 65240510-7458-31b6-b17d-af2ca7153dca | -16.87272 | -57.67516 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 097e2e43-2859-3f05-8ddd-ca0a8b8e99c5 | -17.16692 | -56.74666 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f09f7349-b163-3fd5-89c6-5be3315686de | -17.16262 | -56.7458 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 0bc80acc-7c89-3d4d-a147-1f5ec03f5d8f | -17.16096 | -56.75437 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 54d772ec-66e9-3bfd-94f9-d832d375ea6f | -17.1607 | -56.74578 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 66317c03-b227-354d-9b74-fb174e53f709 | -17.15911 | -56.75438 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 596818de-4043-35b9-a58c-39561968ee92 | -17.15749 | -56.74921 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| b5a9098c-a231-3c19-b2b2-612b4bce01cf | -17.14348 | -56.74227 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 14836b8b-abe1-3a98-9bd8-21b627d23509 | -16.75049 | -56.7106 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c507f048-f2f2-3535-8d7e-9d0c3ab771af | -16.74616 | -56.70974 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bd5a8eb4-6577-391a-8402-e6acda676799 | -16.74266 | -56.70455 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 662f9d0f-9eca-3657-9a0b-01ad400547a2 | -16.74183 | -56.70887 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6548313e-79f9-34eb-909f-ea9c28adb0ec | -16.70434 | -57.46494 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 7a1cd31a-5d1e-3772-9971-04b82c83c092 | -16.69714 | -57.45342 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README68.md)
