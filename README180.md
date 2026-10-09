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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8781d013-f228-3655-a314-28851a5213b7 | -3.70121 | -61.3263 | 2026-10-09 05:23:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7d38643-fb1e-3321-9bf1-482bc9f67303 | -3.47228 | -59.58055 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94d2e25c-1b20-38d6-bdf7-defff2778735 | -3.15462 | -50.59393 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53da5dc1-d17d-3be5-8e5f-5e9f79abd25b | -3.97995 | -56.11347 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd97409-e2fe-3c1a-80d3-fd079c461565 | -3.88844 | -51.93758 | 2026-10-09 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5ea353e-8349-3ff9-9ba7-4b2ea1b794fc | -1.53093 | -54.54896 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9afc84c2-fe09-3b8f-8efa-f037f8ac6f2a | -3.04221 | -54.15388 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d92c45ed-99fe-3996-abc3-05c240fb4b69 | -3.58789 | -54.58095 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b804859-9a68-3728-a382-f9c7c3a17e8c | -3.53257 | -59.4819 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dda9fec5-e292-3bbd-b64a-7f680b4a6a1e | -2.54064 | -58.02533 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ac61e38-434c-31e8-a0fa-a5fb4fa472a8 | -2.30859 | -57.98917 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c7f7635-ce77-3559-8007-f5d4c1be9879 | -3.84481 | -55.79658 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 715680db-5128-3c64-bdb2-22c5392b836e | -8.71167 | -62.42076 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75e168a0-85fc-3a10-a08c-69f0e6e38b9a | -4.63093 | -50.95935 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07822068-8de7-3b30-b9ae-7f4d55177ced | -2.50091 | -56.06615 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| a9748c75-c636-3308-8c06-516531fee421 | -3.77755 | -56.79824 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| feba0c53-0b92-3309-93e1-b4e22dbdda43 | -3.11769 | -60.67383 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bc197bc-a35c-3ad3-b8c4-d999dc9feed4 | -2.64284 | -56.55075 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96515bbc-92a2-3494-8531-0fc5506ebf9c | -1.81038 | -57.11994 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a93cfea4-8b6c-3926-a26b-09115f5c34d0 | -3.67285 | -60.53576 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d14d4cdb-a568-3597-b3bb-20fd316cc887 | -3.49657 | -59.30411 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a93f4f1-32b3-3385-88bf-e90c245eaeb5 | -2.93723 | -54.18364 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6377ca57-06e7-3276-8aff-3faf1428979f | -3.16453 | -61.08201 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d1df451-c13b-39da-9cd0-7f118284c485 | -1.89656 | -54.67345 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1cd656c-8f5a-3b03-be74-ea14c2dc832c | -3.26726 | -54.02116 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9a60809-7d7a-3887-bf12-75833aaccef5 | -3.00085 | -54.07734 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3471671b-3d8b-33a5-bc01-8f24de6d18a8 | -3.01705 | -54.08694 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 705f7c1d-fc1b-3e74-af3b-6315303917e0 | -4.27999 | -49.09285 | 2026-10-09 05:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c613b705-f74a-3b40-96e2-4773c377a59d | -3.27924 | -54.07228 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 856b2320-a1e9-364a-8ee7-a1de2fae351a | -2.97882 | -54.11759 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e36d7ad8-6e0b-3f88-8d0c-c581e2e932bb | -4.40448 | -50.79966 | 2026-10-09 05:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c557b91e-8ec8-3bcb-bf90-3bf356052893 | -8.96706 | -45.91374 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d725de3-7fa5-3b8a-8957-ddef66a6ae43 | -2.51843 | -56.35898 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90c6358f-6641-37be-9dd5-e42d8cb9c4c3 | -3.7479 | -59.62432 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| feddaf45-864f-3632-91d3-969950d27021 | -2.84202 | -54.12307 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63c4b064-1d27-38a1-b9c6-1110fa012734 | -4.12617 | -55.03299 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83424170-a8fe-362d-bed3-1de4ead0371a | -3.01203 | -54.74402 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4c2c1f1-99d1-3497-b3f3-c65404c5cf30 | -3.3034 | -54.67015 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb20c8c2-96e2-3d06-a5cf-b05dee3bbfaf | -2.04337 | -56.88956 | 2026-10-09 05:23:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44f32692-28a0-32b9-acf9-c04eeffc997e | -2.75502 | -54.11221 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25ac1674-9cd6-32a9-8eb5-849b4a97042d | -8.6554 | -54.53361 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7284799-83db-3675-b121-0d9fbbe9c107 | -2.82815 | -54.11129 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a728b884-8cc9-3ba7-8b1d-561148efd274 | -3.28881 | -51.5401 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41fcae41-67c9-3926-ab13-828774431961 | -3.55759 | -59.49666 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 440de789-3ce2-3a08-8f50-800c28f92c8d | -9.08643 | -61.04705 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a988eada-b2cf-34be-8fb6-fd150f393b30 | -3.11116 | -53.78242 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa95dfe6-ab4a-3eee-9c1e-2ae3452c465a | -3.01825 | -54.05288 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d0bee12-7e79-39f9-9bab-1f8a6337cdaf | 0.3077 | -60.44217 | 2026-10-09 05:23:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a674f1e-c5ee-3fee-9933-c390d3876a7f | -2.94633 | -54.17535 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e731ba0c-de6c-329f-a83b-7e4fd7bc824c | -6.48394 | -62.85981 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4f34907-1b1f-3b57-867b-33024cc68f8e | -2.83219 | -54.13601 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea5db90d-6a9c-3092-97c3-f57e94b0a722 | -9.29322 | -47.47262 | 2026-10-09 05:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf621c55-ecd4-31d8-bd41-8e8e0ffb1396 | -2.48802 | -56.17191 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaca87cd-2f6a-3158-bb8c-4d28f8690ba8 | 0.44579 | -60.53736 | 2026-10-09 05:23:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28eda499-bc4a-3ffd-aed3-8f9ed1deed92 | -2.30913 | -57.98573 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8be491ef-0745-3196-8855-f8f4f4cbda85 | -3.10676 | -54.19248 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dea265c8-1f25-3024-9c9d-c205fa588758 | -3.77969 | -59.25278 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32601203-b3a8-3b36-b22c-296113b702a6 | -3.0929 | -59.19036 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd9faa2f-c825-323a-a1b5-2a4af7fcc5c0 | 1.82413 | -55.53107 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f62da82e-92f3-3309-90b8-b76050ab1f24 | -3.01997 | -57.78677 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be6fec75-e52b-32ad-b0d4-0debfb10b569 | -2.52098 | -56.61403 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 138cdec1-a887-376c-9b95-e67d8772dcfe | 1.73185 | -55.59002 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb1ef667-84ab-34c4-906b-0e39ed534000 | -3.55896 | -54.69182 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8bced8a-8c09-3107-9bbc-a15f1392b2b7 | -3.50443 | -59.27319 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9abdf2f-b53c-3106-8ff8-eafa48be295e | -2.513 | -56.25976 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62ca214f-6fa7-3099-a400-8ae8e1558f66 | -3.09096 | -53.96534 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8a15621-7145-3ac8-a1eb-64b537b61f4d | -3.96188 | -60.00402 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 801d9fde-32c5-32e5-9850-a94d23bf6644 | -3.29037 | -53.99978 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3bd30ae-f00e-3d04-9e0d-d284b57d3497 | -2.48754 | -56.12961 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a370ce82-5001-38d7-b58e-eca5d024f00c | -3.1796 | -58.83833 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bde44f7-993b-33b4-ab0c-7c17a6f29a1f | -7.22087 | -55.08372 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4f6a1a32-60bd-37d5-859c-067491b47818 | -4.29153 | -54.8122 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9c3c2b7-fd19-3b9a-973a-8f4ab7df2f2f | -3.56643 | -54.69295 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 085f7698-2f31-33f0-8d00-b21ecaa3ba85 | -4.11383 | -54.01703 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3153a5f-c120-3c7d-b8f6-fa9bbe4202fd | -1.28482 | -55.41459 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aab2995-445e-3a87-9be2-f955e6862d33 | -3.02234 | -54.07799 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f565a4dc-fa6c-35e9-b296-10678791feec | -3.5325 | -55.43393 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a64fe9a-5f70-3c53-a173-bae61acdcbdb | -8.97016 | -45.91597 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c21b6331-3073-3f13-8531-b232451dca5e | -2.56962 | -56.14616 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5991338-4b89-3a81-ab2c-ce633014b87f | -2.43838 | -55.9756 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 160dd645-7731-3cb5-8976-c87c7ab4bea9 | -3.4751 | -60.50109 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d920f76a-12e8-3948-8dd9-3489889c8fc4 | -4.61761 | -49.21339 | 2026-10-09 05:23:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 942834a1-0e61-36f9-9b62-3187d53b9afc | -3.05561 | -58.41989 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84b021e-d39e-349d-b47a-3a727c333ddf | -2.57982 | -56.17082 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d738ad2-00a2-3dad-bbbb-b7ebecb4b1fa | -8.54103 | -46.90862 | 2026-10-09 05:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2753dba-2506-399c-a1c7-c9bf8c975dbd | -3.72509 | -57.1085 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dea04c90-b2c1-39c5-964c-e7462fe16d5d | -7.0003 | -59.10551 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e76546b-19b4-3c50-8c18-8e38d014f033 | -3.71944 | -57.14427 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2da021c1-fe79-3ccb-89f8-240b5b16621c | -2.49282 | -56.3437 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53053ef5-f9c1-33ab-94c1-18cb96afda7c | -1.90022 | -54.67405 | 2026-10-09 05:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 429608b7-b3d2-33b6-9030-7e234766efe1 | 1.70529 | -55.59789 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 6282955d-71cb-3634-9dfb-ea3e44c3f761 | -2.56559 | -56.14938 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143a382b-1067-3552-aea1-287ba6229ece | -3.02894 | -57.85902 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80a49110-7b41-3264-9aab-a21266ae25f9 | -3.1788 | -58.62993 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c17d67b3-649c-36c2-bc5c-03d20da8e578 | -2.92676 | -54.12429 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| caef42e2-39eb-3a2c-830e-d44a2825e8c8 | -1.34123 | -55.46709 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f164a7ed-3015-3989-9b5f-128af6c7d902 | -3.62703 | -59.46478 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1b6d5d-907a-394b-8f9d-bfbd25f985b4 | -3.07659 | -54.26001 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a14bf38b-0cf0-3143-9e0b-6f5f90443bea | -3.09709 | -53.95139 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c1a64f8-e728-3654-9a6a-52eddba3b08b | -3.18916 | -60.40346 | 2026-10-09 05:23:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README181.md)
