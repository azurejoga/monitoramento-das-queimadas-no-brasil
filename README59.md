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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 013112b8-1ea7-3f35-839b-4f71686fa55f | -15.81261 | -57.35485 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24698dcf-7d28-3a23-b438-0127f6240cb1 | -15.56984 | -56.92154 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b16683cc-2499-3024-a1a9-6f636f45706a | -15.56918 | -56.92542 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcda30ff-6f18-3ebd-8eb3-3d77bf7c6862 | -15.56853 | -56.92932 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d47f877-3a71-30e1-b649-a2186b6aaeca | -15.5664 | -56.92079 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9f7cbe2-fc61-3338-a5e5-eb3bb4f76c5f | -15.56359 | -56.91629 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd53aa75-ff34-35b9-bf98-ebfd3340957e | -15.56015 | -56.91554 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bd47397-82ce-30d6-8341-b7bb89621b20 | -15.55672 | -56.91477 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 504a19ec-1df1-3080-9a1f-1b45feafea3e | -15.55392 | -56.91021 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fc07e69-ea73-37f6-a22d-d9b5c9dcc665 | -15.55194 | -56.92199 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54ba2b4a-3e8c-324d-aa9f-1316215d8ac6 | -15.54702 | -56.90887 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4440134f-216f-3d60-8732-e0809c7702d5 | -15.54636 | -56.91276 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0633a57e-1fd4-31cc-963c-a34c825fa20d | -15.54357 | -56.90821 | 2024-09-29 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cc483f4-ce10-3ba5-99a3-951c177467fd | -15.95053 | -57.20446 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 329ee117-b638-3135-b806-244424670647 | -15.94771 | -57.19987 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdc0b31a-8ef9-369e-8d60-786649f7a8a2 | -15.94706 | -57.20372 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a84e25d3-869c-34e4-a331-54c52691eb01 | -15.94423 | -57.1992 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 058cae58-db5f-30d3-afe8-c22a6e4ec166 | -15.94358 | -57.20304 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3af71306-4cab-397b-bfa5-1f3416760bd3 | -15.94141 | -57.19464 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26cd8125-49a1-32bb-867f-f7e2bdd68335 | -15.94076 | -57.19851 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e06895ad-e004-3dff-b786-455c70d1a216 | -15.93729 | -57.1978 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 308fd292-67c3-3dbf-aa3e-884fcf7eff94 | -15.93447 | -57.19322 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 442a1517-aa78-3d0f-8a5c-819186bfc98d | -15.93382 | -57.19706 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7474c6ea-d065-3c22-993d-654036ef4bd8 | -15.93164 | -57.1887 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86c256d0-0708-3406-b5e8-b5834afd8729 | -15.931 | -57.1925 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9d56d01-69c2-31a5-8b70-1536e624284a | -15.93035 | -57.19632 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baf3cb2b-aa41-3d27-9b17-58a2c873953e | -15.92968 | -57.20027 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53c70fc9-b8ba-3d35-b900-84c1a0fc8a2c | -15.929 | -57.20426 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7d0054b-44c5-385e-847f-08e8d2483394 | -15.92817 | -57.18798 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b252fac9-f6fb-374a-83ad-6b48d0384cf2 | -15.92753 | -57.19176 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20deec28-e871-3b2f-90a6-e3fa322e9d99 | -15.92689 | -57.19555 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af2a6722-e998-3137-8d5b-a1c657d19217 | -15.92484 | -57.20758 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e042017-fc71-3de9-b28f-50381cda33e9 | -15.92472 | -57.18716 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8116ae14-2fd6-383e-a942-be44ab0090d4 | -15.92408 | -57.19095 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a18b3cfa-ef2f-3cfe-a577-8e96891d8eb8 | -15.92127 | -57.18638 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a7a254c9-ac56-3757-98a2-a2a86b3b9017 | -15.92066 | -57.21103 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e304d976-8cb3-3fe8-be7d-9459f8f42810 | -15.92062 | -57.19016 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7f52618-308d-3659-8d49-35c38c435c1d | -15.9178 | -57.18566 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f0abd93a-b3b4-3fd7-bed8-3eabdc208e69 | -15.91717 | -57.21041 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 848edf20-5e4c-335d-858f-5c737d5e3f28 | -15.91715 | -57.18946 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb32dfaf-49e1-3600-87be-05ed1b5c3b81 | -15.91368 | -57.18876 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b55b8b7b-38c7-35ae-9ffc-255f88c2ffa2 | -15.91091 | -57.20496 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1c1fb66-fe82-33d6-b02f-ae13ef363446 | -15.91019 | -57.18814 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82683036-c81c-3b0e-bb3e-0693d6d6ba35 | -15.90952 | -57.1921 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51a48b0c-a6a7-3298-87cf-eaa9cfefce85 | -15.909 | -57.18902 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 836bb304-96cd-32eb-bb35-35b483421eb8 | -15.90833 | -57.193 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e13aa0fd-7548-3331-a032-1ec1064bea02 | -15.90741 | -57.20441 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2dc129a-1d00-3522-8db1-0dc9f69a09c7 | -15.90697 | -57.20122 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 176da794-8eb5-30ae-95ee-d855e71c701a | -15.90628 | -57.20539 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f77ef8-f829-3368-88ef-61fc4c170175 | -15.90602 | -57.19152 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b1299f3-cda5-3308-8999-93ef83b169fd | -15.90534 | -57.19551 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53aeda8f-a0da-3d45-86ae-2327b26dfda1 | -15.90484 | -57.19242 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d0d7807-d25b-349f-a14b-bdce72d6250b | -15.90463 | -57.19967 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0291ffc7-98cd-39f3-beec-ba6974bbe029 | -15.90417 | -57.19645 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bc3de87-6928-347a-9bea-42c5c470a511 | -15.90348 | -57.20063 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b39804fc-1f02-382d-9294-e62092b39671 | -17.05486 | -56.73344 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a32d3c61-bb0f-3592-bca2-06bf2c5c4ea5 | -17.05424 | -56.73725 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 218db81e-a21a-347e-83f1-95c4c4cda29d | -17.05147 | -56.73283 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2da1aeac-9997-381a-9d7d-580068920893 | -17.05084 | -56.73664 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1c2e7257-4810-31a0-8b79-388efeeab50f | -17.04807 | -56.73221 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 18af11f5-cdf5-3cf8-9f7a-0743e0f07716 | -17.04744 | -56.73603 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d377ea21-9f34-3c6e-8d62-c5cb0570cff0 | -17.04467 | -56.7316 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 22b54379-b103-30dc-9744-807f3ea3cb54 | -16.85316 | -56.72188 | 2024-09-29 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3a48097b-98d7-3a24-849c-e7065b89d3be | -16.81981 | -57.49146 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 94444592-283a-3339-9bf8-217e73b69400 | -16.78765 | -57.48972 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| abcd317f-d9f1-3e3c-99da-29ede59ebcab | -16.73519 | -57.48008 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d019de20-d522-3dc0-847e-657324038cd2 | -16.73169 | -57.47943 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d836f861-3e6d-34a2-8fff-e8121b45027b | -16.73092 | -57.48056 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3c021bbd-5692-3813-b816-13af062bc4dd | -16.7303 | -57.48754 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eb898f3f-b2e3-3574-8fab-1e93ddeefaa0 | -16.7296 | -57.49159 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 66f43857-78fd-3700-a08c-7bf1666a4a71 | -16.72956 | -57.48866 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ece013a5-b121-31e2-9e32-6076b783748b | -16.72819 | -57.47879 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 694aea20-24f2-37c7-9dc6-b5b33a5f1d6d | -16.72742 | -57.47991 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d451d991-a47c-3cfd-b84e-a4d5f2b336f8 | -16.7177 | -57.49485 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 966f5ad4-0cd4-3b59-8532-66f545f4bce8 | -16.71061 | -57.47263 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 31dcaba9-fd76-38a0-a696-69c020f29116 | -16.70317 | -57.53829 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 6754c32c-06a8-31bb-88c1-79643bde0d72 | -16.68255 | -57.44662 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c4b8c602-38ea-3b3e-99cc-e63968fd625c | -16.67837 | -57.45002 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4d551284-c2c6-3483-82fd-824f85fd33f7 | -16.67488 | -57.44938 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| feb8f1f7-e68b-37a8-b0b6-9988fed6c0a7 | -16.6707 | -57.45279 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5cc81878-e0f9-334a-aec4-28daa145088c | -16.67001 | -57.45683 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7ad196ea-5e7f-3048-be4d-2b713a203b2f | -16.6672 | -57.45214 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 341cde32-dd1a-3e47-9979-faa57e07550d | -16.66651 | -57.45619 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c7ec39f9-39a1-38a6-b47d-68078bc162a6 | -16.91509 | -57.97603 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 9cb6602a-0ef4-35fa-9843-f1dc3a5f31d5 | -16.91444 | -57.95847 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bf53e14c-1727-3c8f-9404-05cc43c8df13 | -16.91436 | -57.98026 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 4cdc90ab-e2f7-3043-ba6e-d564afa73d24 | -16.91378 | -57.94094 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f084b436-8b84-38a9-a09b-3fb9d350e8a3 | -16.91371 | -57.96269 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 9b587bf7-735e-3d0e-9940-2ffbe656e508 | -16.91298 | -57.96692 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| e45b1d63-9e06-308a-ac78-9b66163678c7 | -16.91225 | -57.97113 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 5b97b2ae-cb89-3f10-a10b-002b1121ae7d | -16.91087 | -57.9578 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 15b24f11-f5af-3fbb-9033-912c5e60b354 | -16.91014 | -57.96203 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 75aee3c8-b29a-34bd-8e86-f2c6d4c10a71 | -16.90942 | -57.96625 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 4fdf7f58-76a9-3299-b47a-a9fd4feae62d | -16.90804 | -57.95292 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3a9227c7-cb3e-30a3-85b3-cf555265e93c | -16.90593 | -57.94383 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 81c7cde7-e50a-3621-8db8-aa3fe8060eba | -16.9052 | -57.94804 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6718463d-ce0e-3deb-8af8-9aed42bbcaaa | -16.87847 | -57.72493 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 41e6cceb-46c2-334a-9789-262bb95677ad | -16.87774 | -57.70778 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 49fdf881-c2ac-3a4f-83e7-4d2deaf07489 | -16.87564 | -57.72016 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7fb4e5c5-1e5a-3000-8de6-42ed777cb737 | -16.87494 | -57.72429 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README60.md)
