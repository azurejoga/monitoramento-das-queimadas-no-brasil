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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d377a104-e0e3-3fd3-aea3-63ebdeff48aa | -9.55283 | -62.38775 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8af7e9e9-83bc-30bd-8391-ed0be7f6890a | -9.51099 | -62.0513 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd6cafe3-f6b0-3bed-8ea3-aa4786859bba | -9.48937 | -62.37825 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4252f7c6-fe0d-362d-b12c-6725dc2e167a | -9.4867 | -62.39441 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42ce5240-5c6b-3509-b0f2-f9e956d933e3 | -9.48316 | -62.39381 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d6f7d82c-c9b0-3fcc-9fab-46cce319bd65 | -9.47895 | -62.39724 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b013d9a6-8d3d-316a-bccf-4e7626cea497 | -9.47674 | -62.3886 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63f07b1a-ae45-3721-accf-deda165692d1 | -9.4754 | -62.39665 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 49a0ac53-b332-3e4a-badf-e0683f966a47 | -9.46966 | -62.38736 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47af8787-071e-3eb8-9ecb-eea4b58e338d | -9.43993 | -62.10522 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01e01d6f-25ea-35e4-a897-6d846ed29793 | -10.16705 | -62.314 | 2024-10-03 05:16:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d43e517-f60f-38a3-9d12-59d8ad5c2b6d | -10.03761 | -62.46112 | 2024-10-03 05:16:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cb3faa69-998e-3f9c-9b7e-36b07052450d | -9.59052 | -62.27055 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4a5282e-4056-337d-a43e-ca103b52f3ac | -9.49446 | -62.39154 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327533b6-d285-3161-ab49-18c8b7a0f5f3 | -9.49379 | -62.3956 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e855681-2734-3dfc-999f-bc507674f3b2 | -9.49291 | -62.37886 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27ebc3d0-11bf-30f1-a607-0e8cf4ab2708 | -9.49225 | -62.38288 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5a9053d-e46e-3690-a370-117ce0aa0fda | -9.49024 | -62.395 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1e41eb9-fce2-370a-a08d-21d6c112f8ce | -9.48871 | -62.38227 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c5ac9a3-244d-3717-80f4-90907edf54ca | -9.48249 | -62.39785 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d75fd2d-0150-3e01-89ed-184f9234438a | -9.48028 | -62.38921 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afe49b48-135e-3526-8505-6fd2d4ca32f3 | -9.47961 | -62.39322 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9d17c094-da78-34a4-98b1-0c88b36b6768 | -9.47607 | -62.39262 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6a8b88a5-577f-3fcf-8ade-8181721e96c2 | -9.4732 | -62.38798 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 032abcfd-6511-3fff-a077-7fab5f08232c | -9.47033 | -62.38333 | 2024-10-03 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8e5e17c-6bc8-3bcc-bde0-429826ed3e5e | -10.65545 | -61.75245 | 2024-10-03 05:16:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32302a85-7bfb-35d2-804a-48b2e143b5f2 | -10.64957 | -61.76686 | 2024-10-03 05:16:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 745f7cc9-9748-37ac-8133-3664212b6c9b | -10.64615 | -61.76626 | 2024-10-03 05:16:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb28ead6-7a9b-3ba7-a66a-38570307beb8 | -10.61358 | -61.64244 | 2024-10-03 05:16:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b9633ec-e761-33f1-b1aa-d6cce7da4c87 | -10.2054 | -61.41227 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61b2aac5-0cfc-37a3-93c6-55290839df71 | -10.19069 | -61.9535 | 2024-10-03 05:16:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3289d97-9e3a-341b-9aeb-aaffb648a070 | -10.63952 | -62.81187 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea7c3a26-f0e8-3c30-ac10-206e5bb79b88 | -10.63884 | -62.81599 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d06287bd-50a3-3929-ae10-a0b872be3c13 | -10.63527 | -62.81537 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc0c6462-81a7-3b3f-b57f-d7f0f895c581 | -10.49671 | -62.81832 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9760b643-0fed-3613-8203-15bec25f45ce | -10.03365 | -62.70779 | 2024-10-03 05:16:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 353bc72c-9004-3d34-8bd3-88acbde0e054 | -11.91976 | -62.63717 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c2bb1cc8-e2d2-38a6-b985-3848478344d6 | -11.91692 | -62.63271 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f61e7709-cfe3-3e5e-b2be-aaa1ccc62ef9 | -11.91627 | -62.63659 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0aaeb1d1-daca-37ec-801b-fea14a1db0fb | -11.81128 | -62.36648 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e758df31-c22b-3d33-b77b-4d4e6ad283af | -11.80782 | -62.3659 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 305a1399-3bc6-33f6-ad6c-7180781422d3 | -11.48402 | -62.48223 | 2024-10-03 05:16:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f24c223-a45d-3a9e-bdd3-2dd9817acc8f | -11.01613 | -62.50744 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db26240a-f06a-3149-8dc1-c8bcdafc5aa7 | -11.01265 | -62.50671 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f0817ef-5d38-3fc5-b5a4-98dbbdb67bfb | -11.30791 | -62.07637 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1e9d68b-802b-362c-bf58-47dde025933f | -11.3051 | -62.07199 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87a3dc7a-60bf-33eb-8e02-014983931e9c | -11.30447 | -62.07581 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8dcd685-52d8-302c-80a1-be36292ac586 | -11.2976 | -62.07465 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b5234c0-b170-30f1-b532-07363d250812 | -11.29416 | -62.07406 | 2024-10-03 05:16:00 | NOAA-20 | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f01691ed-814f-3de5-9620-ba981c792538 | -11.34344 | -63.0474 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1a74ea2-d5d6-3d6b-a5cc-245028009585 | -11.34275 | -63.05152 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3e7e925d-87a9-3720-a0a7-7ca7109fce34 | -11.33918 | -63.05088 | 2024-10-03 05:16:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6cc25cf9-b136-374d-a1a7-abd244f61082 | -12.25376 | -62.36461 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e8237a7-f136-3f30-966e-e6a443bf4577 | -11.68082 | -62.47758 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f328d19b-eb54-3b93-b674-dc34e9ddfe2e | -10.93132 | -62.44881 | 2024-10-03 05:16:00 | NOAA-20 | NOVA UNIÃO | RONDÔNIA | Brasil | 1101435 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 354b586e-22ca-39bd-99fa-186efe638498 | -12.07974 | -62.05468 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2ee5ff8-0345-36cb-8936-f4b7be7f7bb2 | -11.83427 | -61.7766 | 2024-10-03 05:16:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 003b23a2-fede-3a35-b089-ef4f2dd26eba | -11.31603 | -62.06989 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56505699-161b-3080-839b-ad7f36a19d0f | -11.31259 | -62.06932 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0416e4-b2f2-391b-b053-76a4f94b28a2 | -11.31197 | -62.07313 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f139a8e-590f-3dcf-9daf-ae1715230415 | -11.30853 | -62.07256 | 2024-10-03 05:16:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c650cd9-1870-3f09-aa16-2e158f161b13 | -12.04223 | -62.62046 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27cbd19e-5152-3219-9f2f-f1d0f2921be3 | -11.88353 | -62.85297 | 2024-10-03 05:16:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aefacdc7-c0a6-3ef6-81f6-83461eef0c00 | -12.90513 | -62.48045 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7b7201ef-2f57-3c08-b9d2-c2c1325b3120 | -12.9051 | -62.47608 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f00ab61d-1fd1-3ca4-a091-68de665cc9ef | -12.90325 | -62.49197 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4701d522-6290-35cd-bedb-431999eed2ff | -12.90232 | -62.47602 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f1df10a1-295e-3696-9cd6-330413ae7b69 | -12.90189 | -62.49526 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b7f19abc-3f21-34bf-8f34-533cc5c259fc | -12.90169 | -62.47986 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c8daa4b4-8e82-33b9-bc6f-1773e18a5a12 | -12.90076 | -62.46391 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9514b912-e886-3140-889d-615c5c753c1d | -12.89981 | -62.49138 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f2c339a7-2a21-31c5-a15b-df74dd8e57e6 | -12.89855 | -62.49907 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 97b50be6-249a-39e5-956b-129e09dd468a | -12.89795 | -62.45948 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e77dafb7-4339-3aa2-bf7f-f95bdf3c776b | -12.89792 | -62.50291 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73c7b4ad-bee8-3464-b52e-46aae81ae63f | -12.89445 | -62.54591 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 44c01ad0-a341-30a2-b181-d431858c5a57 | -12.89388 | -62.46273 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fa17696-ff38-371f-be40-a62e5fa3f788 | -12.89385 | -62.50616 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dec08f0e-e31d-34b0-903b-578ebc8a2974 | -12.89352 | -62.54527 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| c1ac3ebe-7cf5-3c6a-9a94-ab6173e1ee4f | -12.89325 | -62.46656 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c93f8d9-959a-35b1-aeb4-2cb5ed4e4d64 | -12.89289 | -62.53372 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2327f43e-c545-34f9-8e9e-53fd7bc35ec5 | -12.8917 | -62.45444 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 77450395-ccde-318f-81a5-3c86d7b91df8 | -12.89107 | -62.45828 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| df6300b5-d4b8-30dd-a115-831c36c54fe3 | -12.891 | -62.54531 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 46c3d0d3-c33c-318d-a7c6-8dd3c62ff351 | -12.89044 | -62.46213 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a6a759b-179d-3154-9f56-758dd8379d24 | -12.8842 | -62.4571 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f041638a-697e-35e3-88fa-773c69881d4d | -12.88347 | -62.54798 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a860dd81-6004-3fdf-b917-62a7b0dc0895 | -12.88284 | -62.55183 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c43ecf55-fa45-38c2-8dd7-3e2944c61a70 | -12.88076 | -62.4565 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7357fa59-dd16-3fa3-99c9-0bf6ea0da6ab | -12.88013 | -62.46034 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6fdd32b3-f9bb-3365-a811-b7218d51f759 | -12.87887 | -62.46801 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4f92a88-58e2-3ec9-897f-d894e3befeda | -12.87606 | -62.46358 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 569330b3-d3f7-32ca-a442-fc0ed49218f2 | -12.87543 | -62.46742 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf80b278-c965-3364-bb12-064dae16472c | -12.87509 | -62.49107 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a142a9c-c2ae-34f6-937d-b77a73888751 | -12.87325 | -62.45915 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e1d9a8c-529c-3dab-a59a-5ae4fc5453d4 | -12.87262 | -62.46299 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 82c5a424-c1c7-3dfa-af88-4a9619aafd84 | -12.87199 | -62.46683 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7ea8dd6-c59c-3214-9813-372aa484b451 | -12.87164 | -62.49047 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ff7e365-9f7f-332e-9f38-d2bbe510f46e | -12.86982 | -62.45856 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7a60ac0c-da2c-3f40-a42c-be7acec2b37d | -12.86883 | -62.48603 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb901c1d-02cf-3ca0-95df-4f44e9cc2acf | -12.86539 | -62.48544 | 2024-10-03 05:16:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README167.md)
