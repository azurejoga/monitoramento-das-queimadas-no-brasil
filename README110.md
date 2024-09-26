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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a045c819-fa91-33d8-9d12-3194dc3f3cea | -7.49256 | -60.66846 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab4bded4-4422-3b57-8c87-a3fef80a50bf | -7.47949 | -60.66631 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fc9d520-07d6-38c9-a2ab-e72f6ce117d9 | -7.47877 | -60.67045 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e311d503-ce42-32b7-aa09-db88ac034377 | -7.47814 | -60.66736 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 524a62e6-519d-316a-b3ac-33c05d151a94 | -7.45508 | -60.41099 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 067af225-d58e-3f52-a805-c6fd61def7ff | -7.45078 | -60.4104 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec700f65-61e3-3e02-839d-08ce62f8d190 | -7.43604 | -60.62534 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eea1ae01-8ec6-3c0a-b2cc-c1bc968e6e4a | -7.43242 | -60.62036 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5192679-4f96-3722-8aba-fe1377405345 | -7.4317 | -60.6246 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 085bec64-9f79-388a-b915-a95227e2ddc3 | -7.42845 | -60.28982 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb281fd9-9da4-3fec-9be8-5f9b6db0e9e1 | -7.42808 | -60.61962 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 127a43d5-7d10-3f5c-a135-21e1d2cc2e82 | -7.42776 | -60.29395 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef3b41b7-fe1f-3fa1-82de-0d107911c77a | -7.4235 | -60.29334 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2ca0ea07-e387-3542-b2bc-b36fc6709d8e | -7.41797 | -60.52337 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08aef5f8-5b3a-35a0-9f16-5bc3ce632fc1 | -7.4143 | -60.29607 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f7905c5-898e-3109-b827-866aa561dae5 | -7.41004 | -60.29538 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 563f733f-826d-3eac-8d6a-4eb08311350c | -7.40937 | -60.29936 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d574ec44-6408-35f8-9033-05acace12342 | -7.39595 | -60.30112 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85620012-8cd8-322b-be53-5433716eb598 | -7.39459 | -60.30916 | 2024-09-26 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae2f33e7-1165-3421-a803-6c0d53a1d734 | -7.22321 | -60.67794 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cab31139-e616-3c47-97c3-cdcb601ea5d7 | -7.20721 | -60.6662 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0c7bcd5c-30b0-322f-abd5-8aeea8807a39 | -7.20355 | -60.66129 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a85c3aa-d5bb-326d-b8f6-c60ed9401228 | -7.19989 | -60.68264 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a80f10c-4260-3dbd-9d93-edc129ec8add | -7.19916 | -60.68689 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 242857a4-0b38-3cdf-8716-4ba7b3339fa2 | -7.19914 | -60.66077 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 03aac721-6da7-3140-9e42-6c54cf7fc376 | -7.19553 | -60.68179 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5944bb68-23cb-31f8-97d6-651e695dc04d | -7.1948 | -60.68604 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c6e8febe-edae-3148-acde-74e43ef34bd3 | -3.45264 | -60.61675 | 2024-09-26 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 267d5a96-be6d-37de-8c9c-074db940c697 | -3.45186 | -60.6216 | 2024-09-26 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30cb5118-b4f1-37f1-b915-a45e9f269e08 | -3.09142 | -60.46161 | 2024-09-26 04:57:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77f54118-1ad5-3e8b-a78e-1ab0d90c1d67 | -3.78301 | -60.13293 | 2024-09-26 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55113954-8827-3cef-b6c8-b843b7259778 | -7.906 | -61.51315 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a84f7c7a-1012-326e-9365-9f3aa6425ba3 | -7.85 | -61.34693 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5486099f-0db0-3a93-962e-bbdf2422e2c7 | -7.78283 | -61.32319 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb6d3ba3-4861-3d79-be35-ebcb0914f06d | -7.62684 | -61.22131 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f937aa7a-df8b-3865-b1c9-d0217b655d21 | -7.00524 | -60.68283 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e477278-0fa7-3dbe-9627-9ece9ad57846 | -7.00451 | -60.68715 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c6003b0-7690-3204-b5c4-38cd696e4bd3 | -7.80519 | -61.11168 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07e214a4-5565-3798-8ba3-85c707a157a1 | -7.73824 | -61.10024 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a1c1b3a-8e3e-374b-9909-b9293dcdf865 | -7.73545 | -61.10019 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2398b450-862d-32f8-be97-8c6e0faca335 | -7.7347 | -61.10465 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d76dfc5b-69a0-3d1f-867a-bb733c74e097 | -7.73378 | -61.09944 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2054fe6f-01ca-3b7a-8254-b156bcc60874 | -7.733 | -61.10386 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c62618b-83c3-37f0-b092-703968084349 | -7.73221 | -61.10831 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5c7315a-d273-3418-90ba-f3100a0a53fb | -7.72949 | -61.10829 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8887f8c-0736-3a01-9ef4-2a9391306007 | -7.72873 | -61.11276 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc27a332-91c1-3f20-987a-1b53c67065ad | -7.72775 | -61.10752 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88e2336d-2f98-3099-b47d-b71c109f3210 | -7.72696 | -61.112 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a108bcd0-18fc-3b77-b62d-dab98b6d1575 | -7.72501 | -61.10755 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f6f43ef-2e88-3426-9e6b-fbe5d60809a9 | -7.29513 | -61.09552 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 389582fa-6eae-30b2-848a-200e876bd9cd | -7.29433 | -61.10003 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 72fbebd6-7e6b-305f-bf5d-a9efab70e485 | -7.293 | -61.0959 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| bcaa91b5-229b-3e3e-a902-4b67024fc79f | -7.29272 | -61.10912 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea024050-a294-37a5-ad83-e3e7f39ddf98 | -7.29224 | -61.10043 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| f25e0208-6ee9-35c3-9a82-c6ded322eaa5 | -7.29112 | -61.11819 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79a76a5b-a297-382e-8cb5-aacb0bc89f87 | -7.29063 | -61.09477 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 36a43389-5ff0-35f8-8371-3c30b364f8e4 | -7.28982 | -61.09932 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3f3b8871-b0e9-30c2-95f1-f0874499aedc | -7.28902 | -61.10386 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a77efc68-e245-3618-ad18-fea68046554b | -7.2885 | -61.09515 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 133b2d50-bcff-3ae7-bd1c-9b81bc840108 | -7.28773 | -61.0997 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a45800f1-7a9a-3b42-961d-389e82422335 | -7.28696 | -61.10425 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70f918e5-fb87-3e53-84f1-f256ea79921d | -7.28247 | -61.10345 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4867275-f68c-32ab-a2de-26f70928923a | -7.2817 | -61.10796 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2923891-7a5b-3406-b4d2-3c87d5c4ee95 | -7.2637 | -61.10487 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 816ea76c-5396-39b7-a1a5-5029515b258a | -7.25919 | -61.10413 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 614284a8-345a-38af-af2b-d1c420068c13 | -7.25547 | -61.09881 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d131ddf6-708f-30bc-87f9-846609c0d1b3 | -7.89368 | -61.4744 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f5ae1a5-e974-3acd-bada-1b0a2c2855eb | -7.78362 | -61.31852 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b19c2e97-7920-3cbd-8c3f-0f6623a13df0 | -7.55583 | -61.35421 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 898f6424-d174-3115-b913-257838b7275e | -7.52528 | -61.50484 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3dc43c07-8db9-3ec2-8124-eacbf131215c | -8.22572 | -61.49533 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 984f4e39-14d0-32fa-a01b-2172b2588c1c | -8.2249 | -61.5 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1b56b76-4c3a-35d0-b44f-e1e037790979 | -8.21951 | -61.50393 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b11b4505-a48f-3915-a5d2-0a3b690c88cf | -8.21662 | -61.49379 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 675632c9-35a8-39bc-bc0d-c5147c902637 | -8.1988 | -61.40193 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eb4e9389-a59f-33dd-ab5d-2a32dd8ade7f | -8.17169 | -61.39714 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b24fa5a-82ac-3081-81d9-095e6cd99ba0 | -8.17089 | -61.40173 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b65c9750-1540-39bf-9bcd-9c190e15830f | -8.16716 | -61.39638 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ef13712-6c74-3fe9-8497-adc4d1d83155 | -8.16631 | -61.53581 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4a947be-5a83-3077-b7d8-3ca512471029 | -8.16259 | -61.53019 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de7e815-0006-371f-8fcc-57504de4e401 | -8.16176 | -61.53497 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d68e500-c12d-3e5f-b33f-e80979794f90 | -8.15811 | -61.39489 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9810b5f-32aa-398c-a4e1-0b92b66c415e | -8.15801 | -61.52948 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e77398e-5b3a-326f-9954-b4c37b7165ca | -8.14514 | -61.28413 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4f6262d3-0cdd-3726-838c-87b7eb69b8a9 | -8.1427 | -61.28547 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3095e3f4-b864-36ef-872a-baa35b2031d5 | -8.14064 | -61.28341 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7a44158c-8e8f-3f77-ab9e-4a7ea5d54d71 | -8.13984 | -61.28791 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 13ab99b7-7605-3a67-b885-f94487e99b2f | -8.1382 | -61.28473 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f03c7ae5-8073-34bb-b53f-494321a6a201 | -8.13614 | -61.28268 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29131b08-d69f-3b84-a8fe-f3c799117efa | -8.13217 | -61.293 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd043dbf-4a58-3c12-b3fd-8b47bf2b097a | -8.07049 | -61.30161 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee5c9702-f6c0-3dc1-947c-06dbeda33ef6 | -8.22406 | -61.50468 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0e09878-ed2a-39cf-920c-b060c6b60889 | -8.22117 | -61.49457 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b606623-9445-390a-947c-2cc9a8b2975f | -8.22034 | -61.49926 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983f6232-8c57-3627-921e-acf41b69b2aa | -8.21159 | -61.40881 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f57a1d7b-879c-37d8-b818-c9982dd351d4 | -8.16796 | -61.39179 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebcc580f-5839-3b43-8478-8ad84a9d3dc9 | -8.16636 | -61.40095 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 185c3bd0-50f5-39d0-b15a-79e83cc66a49 | -8.16549 | -61.54057 | 2024-09-26 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c1896e4-c2ae-3c66-ad03-8c95c3965e2f | -8.16343 | -61.39105 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2769119f-1532-3308-ad9f-e2a78de0b9a2 | -8.16263 | -61.39563 | 2024-09-26 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README111.md)
