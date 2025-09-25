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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0f28cfc-df91-3203-b005-b2bc8abcbee0 | -20.9871 | -50.01525 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 27f83963-8b69-33fb-b0bc-d459dc0b498a | -15.89699 | -59.3478 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 06b01f4c-e9f4-3019-bfbf-49c103984157 | -15.88609 | -59.41922 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e28145fc-64c5-386f-a57a-b64462f2ad6a | -20.9796 | -50.02023 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| e98daa40-96fc-3bb8-b6e4-6bb8ccc69dfd | -21.97389 | -49.50359 | 2025-09-25 05:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| dc7256c6-75cd-395e-b0fa-6a30582a323f | -20.70449 | -57.86211 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7bb97b74-efe6-3292-a65d-82b087878b38 | -20.70501 | -57.85801 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a163a439-17f7-3f58-8962-75f8d66ed050 | -17.93994 | -55.85287 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d2f11fdd-74d6-3e16-ad66-17512d9935a0 | -15.90397 | -59.3469 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 39d9036a-b013-30fd-a701-5314bcaef0ff | -17.93411 | -55.86222 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 23c922ce-ae56-31de-a57e-c575f447aa59 | -15.92247 | -59.35105 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7da20bf9-17ee-352a-8310-b9787f79b862 | -20.70116 | -57.81979 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 212c44ab-eeca-3d00-a513-72fae59191f6 | -15.88863 | -59.40171 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f537d03b-5e1a-3521-aba2-aca5ac70b39f | -15.90913 | -59.39339 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14f8eb84-93ed-3db0-836d-ebf9c97b8d3f | -17.93068 | -55.85167 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 8dc9a706-eadc-3156-bb17-7db6d21caa57 | -15.97048 | -59.50672 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e028a87c-2bba-3d7f-b2cc-93fc86b6b5d4 | -15.89672 | -59.34584 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 09d4b816-b4a9-3226-8489-1f88635e9732 | -15.88676 | -59.4213 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b3af603-cb3a-3d40-84a4-1192774719fc | -17.93351 | -55.86719 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| a9e55879-b8d0-37cd-987b-a1c695b96aaf | -15.9085 | -59.39786 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0429aa-a2b1-3ae7-953b-7d9919ec221b | -21.99535 | -56.06289 | 2025-09-25 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea73cd0c-c209-3e7e-b391-de1c72732614 | -17.93933 | -55.85785 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 96d7c450-71b4-382b-ac7a-2c4c201fcf45 | -15.97408 | -59.50728 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31a1c4bc-7fd4-3a53-8164-ead88cbe0c17 | -17.92888 | -55.86659 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 2fa11e39-49c2-374f-a3da-89c3318ec464 | -17.93531 | -55.85228 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 57d855de-ccad-3b7d-aaa9-136f296eda86 | -15.96627 | -59.5104 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2625499a-c05d-32f3-a6c5-9c8613f98aba | -17.95443 | -55.84967 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2631ed0e-f824-3305-9564-10c617790be6 | -20.73494 | -57.82444 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 73d5830b-d36a-3260-8456-21534dfecae0 | -21.00122 | -50.01003 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 861085a5-e820-3c22-a25f-bf0d27698e06 | -20.99337 | -50.02201 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c01a403c-d9fb-3903-9561-1e70ae92be1d | -21.99599 | -56.05706 | 2025-09-25 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 240ce259-abe4-309e-8484-95a1ab2e094d | -20.7096 | -57.82095 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b8ec2db5-886e-3e3c-b826-60b6e751c381 | -22.36316 | -54.63833 | 2025-09-25 05:25:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1a84f543-9ca6-3eeb-8214-c15c0de1772d | -18.18337 | -53.33571 | 2025-09-25 05:25:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f2e2b8f7-6942-3fa9-9fbb-09e4056ad5fa | -20.7351 | -57.82352 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3171d0e5-44f8-3adc-8623-77fb3cd4c0de | -15.91884 | -59.35052 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b314edc-2bfd-39dc-8c53-ae10fd671a63 | -20.70547 | -56.74189 | 2025-09-25 05:25:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b6d797d-8e3e-320d-b6b9-ac6641b6ac8b | -15.9079 | -59.34925 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5c7d734-837a-35cc-a63e-a6cf07c1af3c | -15.91218 | -59.34514 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17fb019a-7a92-34a7-be45-03332980c129 | -15.8916 | -59.40669 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07c1de56-a19a-363e-a46d-a00e0b1151d0 | -15.97109 | -59.50247 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c90ee8e-9cb8-31ba-b06b-82506dda3204 | -20.98695 | -50.01485 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 0f2d34cc-7b4c-375b-9919-c1cf9ccfe78a | -15.8892 | -59.40377 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 44180cf4-20f8-3ba0-8da2-877362014453 | -20.99501 | -50.00346 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 31f373e8-a5a8-3feb-99ab-a1415a8f6b93 | -17.95845 | -55.85526 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2717832a-d773-3e90-87ac-42bc0bffcbf2 | -15.90034 | -59.34638 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 46b2814d-0919-33c5-a9b5-207625f71fcc | -21.00075 | -50.01624 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 751a9810-2e6f-3161-8b21-fbfcc033dc94 | -18.87928 | -51.52222 | 2025-09-25 05:25:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fe4455c-454a-3c31-8490-cc280a3532b6 | -22.36412 | -54.63979 | 2025-09-25 05:25:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 72434637-b742-3d51-bd39-60de58f0b526 | -15.90124 | -59.34389 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 461767bb-fd4f-3772-a43e-8e9e92cdf9d6 | -20.97972 | -50.02065 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 72195b9b-1a1d-3bf6-ab21-b9d04e2762c5 | -20.99348 | -50.02236 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| afae2b44-0a09-315a-a8e9-3e4f359541bf | -20.99384 | -50.01573 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 50770c57-2352-3f73-9aab-497c85ee846c | -20.99399 | -50.01608 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 0c44cce5-58f1-31ec-ba98-161d3998fd32 | -17.93291 | -55.87215 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 9c12db08-a40d-3e19-9422-ba1d2dfbfb3e | -20.7265 | -57.82328 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 94239c5c-c1fd-366d-860c-8b329990435a | -22.37928 | -53.73674 | 2025-09-25 05:25:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15e92a79-f338-30c6-a25d-453e22e79748 | -20.98686 | -50.46632 | 2025-09-25 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| efc7a1db-e43c-35bf-8326-41a58b1ff231 | -17.94396 | -55.85844 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| ac440732-8f38-3130-8b29-7fece0752b58 | -17.93471 | -55.85726 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 3db3103d-c102-33b4-b9d5-4b29067a48ec | -15.89761 | -59.34332 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92b6d0a9-51d1-3fd8-9a04-d5b62bf0c0b1 | -20.98762 | -50.00882 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5108d8bd-0c0d-31c2-81a4-68b1fde202e9 | -18.8731 | -51.52146 | 2025-09-25 05:25:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 105b4361-78e0-3b04-ab1c-5ddffa13280b | -20.98647 | -50.02134 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| a4821378-cdc0-33ce-90df-bc924b470b0b | -19.59086 | -57.73679 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 020c7e31-c689-3167-a353-57481dc3dc8b | -18.18371 | -53.33243 | 2025-09-25 05:25:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 40a95a12-a28d-32c3-9f6b-5e0ac3264f6d | -21.9702 | -49.50957 | 2025-09-25 05:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a1456a4b-6a0d-3139-86bd-0ce899fb2a2a | -20.9943 | -50.00949 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0903b2bc-99e1-3b94-926c-9d6c4b8fa908 | -15.96987 | -59.51097 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 47cc6379-3d65-303c-a632-13ac2069cf96 | -20.70096 | -56.74117 | 2025-09-25 05:25:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1ee73f9-da58-3428-8603-a1e7550261a7 | -17.95906 | -55.85028 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3ffd0292-ce68-38eb-9089-a8168ffa3279 | -20.73913 | -57.86181 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| affd2a11-6719-3b0b-833c-d26effbdc576 | -21.01406 | -50.0242 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7902a624-614e-3e36-a441-d47e114eb932 | -20.70028 | -57.86152 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3a11527d-6844-395d-850a-60cff4a4412e | -20.99296 | -50.0289 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 90456f33-551a-3d70-96e4-b2a6ed8b9415 | -15.90487 | -59.34441 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d9a53a76-7fa0-3f35-9c07-b8ab591fbb52 | -17.93873 | -55.86282 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| e2d81236-820b-3443-83be-6b8731e95d96 | -21.00669 | -50.02982 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 56a4ba37-2072-3bec-ad47-7dcb75b0f996 | -21.99511 | -56.05889 | 2025-09-25 05:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d6b19e32-180f-3d3a-bb8a-9063c55836c3 | -9.00179 | -63.67468 | 2025-09-25 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba0b6d83-6761-31a2-ab12-9e934c09d40c | -15.91947 | -59.34598 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a33f222f-9024-3a54-8194-cb6ac30d11b7 | -15.888 | -59.4061 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5cbe108-3d22-3085-ac03-8f7b6c2138b3 | -20.76468 | -57.82763 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 285f5f6a-652c-35bd-8213-f8c544860156 | -21.97341 | -49.51079 | 2025-09-25 05:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 54dca812-f7d0-333f-8e4a-90de01bd496a | -20.98743 | -50.0084 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a1ed4141-c126-3d48-9d7d-62bca55e7bc8 | -21.0009 | -50.01655 | 2025-09-25 05:25:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 96db5b04-330c-3cc2-97b0-4118bdb39f80 | -20.69607 | -57.86094 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e9e0f7bb-4f1e-3ab3-90ff-9332206a812b | -15.93634 | -59.35778 | 2025-09-25 05:25:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a9c4155-4b31-30e6-8ae4-9467784237d1 | -20.24452 | -56.05863 | 2025-09-25 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29e03df2-396c-3596-b6f8-69309c0c017d | -22.36282 | -54.6419 | 2025-09-25 05:25:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d7a30f4f-fbe3-3df2-a8ec-a533bf069aa0 | -17.92828 | -55.87155 | 2025-09-25 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| d9aa7d43-50cc-3d2b-8ced-e142798292ab | -17.9506 | -55.8731 | 2025-09-25 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 9bdb93a7-d790-3953-8feb-c896add028cf | -17.9304 | -55.8967 | 2025-09-25 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 25490dca-9678-3eb2-bc0b-ac71904f883e | -17.9308 | -55.8758 | 2025-09-25 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 308.1 |
| e5a3b923-de80-30e5-b740-67a81ad58224 | -17.9304 | -55.8967 | 2025-09-25 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 9c9c3156-6022-3dc5-aeee-dffe6f7d5135 | -17.9312 | -55.8548 | 2025-09-25 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 177.1 |
| 63b3b446-09c1-34b5-be6f-3a4b68b76757 | -17.9506 | -55.8731 | 2025-09-25 06:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| 190a224f-7d00-3535-b623-efc73b2ae7c8 | -3.08098 | -52.91568 | 2025-09-25 06:16:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9546e953-e60b-3823-821b-b8541b8bb0c8 | -2.92264 | -48.29814 | 2025-09-25 06:16:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0841c725-7d29-3c91-94c3-491a237969c8 | -3.6391 | -49.13789 | 2025-09-25 06:16:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |


[Clique aqui para ver as próximas entradas](README37.md)
