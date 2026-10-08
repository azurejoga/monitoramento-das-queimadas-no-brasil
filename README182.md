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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 278d96b3-67c4-3e75-a6f5-4896f79399b6 | -3.03336 | -54.10602 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| abc33ba3-b3e2-399f-95f1-417ff72c7fea | -3.53467 | -54.66727 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40d9d9c1-b98a-3ade-ab74-9204061660f1 | -2.84916 | -59.11726 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4014caf2-83af-3631-b77b-e8309d72fa56 | -2.94094 | -54.18198 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e9c8157-9e6b-3326-a99a-0d1f301fe8b7 | -3.5521 | -59.48212 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 059e5650-64c9-337a-bfcf-efbc460ec462 | -3.07817 | -54.26913 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17146875-dd65-394a-b9f7-ed2dc2025b2b | -4.09239 | -52.06882 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a8c0dc-e89a-3193-913f-cc7a013e4b80 | -3.28237 | -54.05877 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b85791c-03e3-34f1-97e8-4765b3d5a85f | -3.18299 | -58.65829 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8ac619-4f4c-3479-babb-b69356b1d00f | -3.92502 | -56.06033 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6e73a4b-17d0-37b7-9a7a-04c1bd27d034 | -2.76976 | -54.07182 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8aca6f4e-197c-31fe-ab54-27d8154c600a | -4.57097 | -54.95454 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 287ae6f3-d361-38c7-994c-58b8be4db008 | -4.77028 | -55.73463 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50036a0a-7e41-3402-98ca-f8ce028402d0 | -3.28087 | -54.06856 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b02a8c7f-0ef3-3036-b631-a24f019dd7b2 | -4.44649 | -54.98062 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 096676a8-fd56-3522-87ae-86ab264b790e | -3.27754 | -54.05466 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 463ffc5e-36d0-3508-b156-37f802ea6d50 | -3.10579 | -53.77502 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8962b046-eff2-35ff-ab83-6eaf94a0f26a | -3.2953 | -54.67429 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3dd408c7-728b-3da3-8769-dd784caedf49 | -5.34492 | -50.98463 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1aefb12f-b97a-30b3-a1a6-dcd5ac490df6 | -3.63749 | -60.62953 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 540b4808-ad8d-3c4e-a6c1-ccad068b3bab | -2.79576 | -54.07898 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607e3623-6ad6-350c-881d-d4959649a84f | -3.59229 | -54.66904 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7e3d4c4f-f5ee-3765-9787-c7cb5441fac9 | -3.75885 | -61.17736 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce1ade0e-5a41-30be-9f19-ae5ad922df02 | -3.19478 | -50.56635 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15097801-578e-37e9-ab3c-d4caf0ebcf12 | -3.30457 | -54.04158 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e22aff4-5d7f-3c75-a346-1cbe897b9512 | -3.71661 | -54.22917 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c232fecb-81e3-3ee8-9a18-ee81ebc2bcdf | -3.64806 | -60.63113 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46182b77-e0e6-362b-a2df-c008c27c3d7b | -3.58904 | -54.69062 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc8bf082-4935-3d06-9937-9a32ba618b7c | -3.07434 | -54.25878 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dd59f88-4131-3fc9-a2fd-908e9eca6a4e | -3.07529 | -54.25238 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b4c6e04-19d5-34bf-8ab8-2a11608136e8 | -3.13273 | -54.36832 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17db9831-5f60-3143-aab9-4e97aff13323 | -3.0691 | -54.25787 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 075123e3-0ce0-3a24-9a5f-266907e75927 | -3.10896 | -54.17131 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 97cf1b4c-25f9-3e73-9450-ed2a37e676d8 | -3.59792 | -61.62523 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd87d677-dfc6-31a5-8d5c-079a97dd7983 | -2.7784 | -54.08643 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37d4dd99-5930-3213-af0e-1628262b8287 | -3.3006 | -53.86725 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85fcc5e2-13c5-3f57-a718-c2e540247840 | -3.67369 | -55.94645 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4333cdb-6307-380c-8b50-3ff2ac9f6794 | -3.72098 | -55.49083 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b4d4146-7d58-38bd-b325-db96e3a5f440 | -2.75665 | -54.09193 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eceeba09-251c-3191-af75-22c2a8159e4f | -2.94144 | -54.18097 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1516a8a1-1944-3b3b-88d0-d507f3a606f0 | -3.55185 | -59.47495 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6906a142-a7b9-382a-a3d9-058d600f31dc | -3.6551 | -60.63222 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3dca165-4d53-3004-a2b7-68c7bb5523d9 | -3.67613 | -54.5053 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41003647-3722-3a4c-b1c3-cd2ee3382334 | -3.29944 | -54.05438 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57eb7845-075b-369d-9a38-52585ad2eb59 | -3.11225 | -53.7691 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a5a7b0f-f9cf-3ecf-bfaf-4b3abe568d3c | -3.07864 | -54.3019 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e8f7cc2-8b33-3e30-98ba-190063660d4d | -3.5406 | -59.50773 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98a0a880-39f8-3051-afea-9370deb0e47e | -3.69112 | -60.54063 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2739a634-fa2a-3046-af06-ec30ce5270a2 | -3.33326 | -58.16791 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff70e52e-ef2e-31f4-85ba-34c192a9681a | -2.8128 | -59.24809 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e26ae15-7810-30b8-9188-79382e01f9c8 | -3.27928 | -54.06519 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19f6b938-9204-39c9-8ce8-c437cbcf1c73 | -3.1674 | -54.74026 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc296644-c59f-3eae-8f7d-c2cb8825be83 | -3.29634 | -54.02304 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fb55a70-f89a-343b-b4b9-4c0373dee16a | -3.59678 | -61.63248 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f660bfdf-468c-335c-bd5f-0d84d70d8ec2 | -3.00055 | -54.10784 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17624012-4351-30f3-9ebd-514cb01e506f | -3.40053 | -60.84875 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25c5611d-67f4-345e-afa5-632c27b8a45d | -4.14098 | -54.02865 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9550e08-3360-3403-8fa0-b932b988b4fb | -3.43284 | -59.54086 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d76f4f1-ad3a-3211-ad4a-68808512af02 | -3.47303 | -50.08599 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbd0fbd6-82c4-339c-96a3-f992f86377d6 | -2.99721 | -54.09388 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3cda3a2d-8ebc-3fe0-afab-65bb919dbb92 | -2.98568 | -54.06184 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 668de3d2-93d0-371d-b27f-a673e337c8da | -4.08637 | -55.33484 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f46e1202-821c-37ef-ae6b-637aaff637c2 | -3.98685 | -59.2195 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 631a32c5-a749-3f6c-b1d3-73caf0b343aa | -3.52654 | -54.67083 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2604c30-7f76-3c97-bcc6-644a1ac9dae1 | -3.2919 | -54.05348 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccb00d5f-c9cd-3174-a67f-68d5530c525a | -2.6135 | -59.92676 | 2026-10-08 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b32ee738-8d0c-370e-8d2a-5b27a178e845 | -4.78163 | -55.725 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04e31b94-c3e0-37e6-b299-a8e5ea1527b4 | -6.99427 | -59.1057 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cffd19ee-ae79-353d-af37-08276ae16610 | -4.11216 | -54.02487 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b3e57a3-ce56-324d-9458-5934636b88b0 | -3.00672 | -54.13893 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 362c8150-b439-32df-8003-c2637cedd444 | -3.1283 | -53.70709 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82236e9-d837-327f-b7db-27aea70ac29c | -3.05866 | -59.26571 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3007c57-d8fe-3fc3-b9df-504b620d727d | -2.57323 | -56.16434 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 230ccd02-772e-3433-b43a-394f72f052cc | -3.67759 | -60.53448 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c42d863-af32-3698-b41e-26cdf9bc63d8 | -3.51362 | -59.32635 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da4e0e48-4098-3f1e-aa05-0bd679f5f4b0 | -3.2684 | -54.0429 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4f9a057-307c-3a92-a279-cb8af4f27d00 | -3.05528 | -53.92545 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbd0b065-7cd2-36d0-b1be-72c71daff4f2 | -3.57498 | -54.67918 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 85fbdcba-bad5-3f19-a5c7-c801650dcbbd | -3.67343 | -60.53792 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a93a314-fb74-3fa7-86d5-5aa1797d4ac8 | -6.99376 | -59.10917 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d67e6113-5be2-36c5-beb2-6d5a206c0b3e | -2.99002 | -54.06926 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f86fb040-a2e0-3955-84f9-24a3dbe9b36f | -2.85397 | -59.26219 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33f8eb9c-3916-3306-be08-659dedbfcffa | -2.83944 | -57.48219 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275abfac-f738-3130-ac4f-d7b1312bdc40 | -4.06327 | -59.83457 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b98d723a-c2d4-3daa-abf6-14102d713ebc | -3.52605 | -54.67401 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c78e444d-6eb5-3fa9-8efb-f80d29bfae5d | -3.31195 | -53.86544 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d288255-5bfa-3fbf-8e3c-4ed11fc23424 | -3.29196 | -54.01555 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed25d71f-a6a6-3fbf-bc05-78cb12f34ef2 | -4.0084 | -56.25377 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4781c5dd-0a6a-3d46-895d-1ccdbd90f62c | -3.05763 | -54.22964 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 838af1a6-568a-339c-8b4c-0bdd2e4b3cae | -2.93962 | -54.15771 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37cf99dd-dcba-3f00-b244-bffd368cd1f4 | -2.89181 | -54.08044 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34a0cb68-2a7f-35d3-98bc-b5fbd7e45d69 | -3.19944 | -50.5592 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 03ad5261-ce18-3699-b288-5ce58ed9334b | -3.1063 | -53.77166 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d543dc1d-0b91-32f9-a53e-e309066d2a55 | -3.07053 | -54.24824 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cd0cb0d-d048-37cc-91de-f59b5adc114e | -3.27881 | -54.06843 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 710c388e-e54f-3ae8-9fe8-5051f663fc84 | -2.7582 | -54.11322 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 30a58365-92fa-39bc-9616-f055e95c8948 | -3.12734 | -53.70713 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b796476e-1b76-331b-8d51-5d9d9c01fc10 | -4.10794 | -54.41117 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 956a5e29-6fd7-3d8d-b25d-1a110b52d12e | -3.09527 | -53.73457 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ed5bd6f-0bfe-312e-94e7-516d60f6e3c5 | -3.44501 | -56.94133 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README183.md)
