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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61a8141e-34dc-3ca6-871a-bfbda890f021 | -9.24382 | -60.4122 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc8bfe4-ddb4-3be2-81a6-a9fd270790a7 | -9.64581 | -63.47018 | 2025-09-13 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06542fed-9eb2-38d6-86db-246d3800e73b | -9.25143 | -51.24309 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6155031-7df8-34c7-bb2a-428c9f9b0c33 | -11.09513 | -51.43082 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| daf4bcb2-acb5-3bda-abd7-c8b372142e5d | -7.31396 | -46.5848 | 2025-09-13 05:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dbea846a-ab7e-3c1f-9c4a-3a328dff546d | -11.82084 | -50.5488 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 79bff266-94c4-3c9f-ae19-084e641ab6d7 | -11.1608 | -50.70766 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed8a78fc-0e1a-3628-9149-37c8c63ff60f | -8.361 | -62.75638 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02f68a38-54b4-30d5-a29d-ab842de892d9 | -9.79433 | -61.51073 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 340cb044-8575-3f66-af9d-c5a8fcc0904c | -11.84201 | -50.57973 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf798a65-2533-38af-98f5-f167b3e803ba | -9.25789 | -59.41558 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6b89379-e906-3011-96db-512b91bd685e | -11.42504 | -50.74407 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c258fc81-810a-357d-965f-d254b7bb48ba | -9.96977 | -50.2921 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3604495a-a524-3208-b85f-79c7e944144c | -9.42301 | -58.94475 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb8bfa65-a5a1-3a02-b251-a53f799a1e51 | -11.81473 | -50.54801 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e580529e-7afa-364b-aa8b-7d7deb6979d5 | -9.96355 | -50.38736 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d272fe3-d12f-3c8b-9146-aa933f68e441 | -11.06033 | -51.50747 | 2025-09-13 05:25:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0938c909-bda9-3642-9511-8e19ee29c843 | -9.90627 | -57.05554 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cb0b337-b966-35eb-9b6b-6ea793ff5fc3 | -11.18763 | -55.075 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e470910-f19f-36e4-9f95-c3d9ffc81756 | -9.275 | -59.41823 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6942a489-0de0-3658-b342-da9a2ce11ba5 | -12.1193 | -47.59345 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1bbabbc-100f-3fe3-89ac-cecf4170acaa | -9.62593 | -64.18364 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d25d511-9053-3f37-857c-4da66b853df8 | 0.69609 | -50.65067 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65be524d-fdc6-316c-a700-45245a96b21e | -11.83289 | -50.54662 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fa720f4-13f1-3ed8-9bd1-ceec65586247 | -10.50751 | -51.55247 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ba4e542-2cb9-3863-9019-3288e8788d46 | -9.22062 | -59.56872 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ab4320c-3422-3f7b-9977-e78f879970f9 | -9.81041 | -61.51692 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b9ccb53-a9e8-3b67-a2eb-47d10dfa4687 | -11.08219 | -51.42672 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c2041310-4d74-3f4c-b21d-edd2ff3e2239 | -11.80127 | -50.55209 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a2180b90-7b05-3355-ab94-ff54608fbb7d | -11.18258 | -55.07871 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39249e1d-7319-3303-9cfe-144482f529f0 | -10.51894 | -51.50792 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57807b9d-1c78-3049-b347-319d043474c3 | -9.23408 | -51.24413 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f585dbc-b25a-339d-b07d-fafe2c4e9cd1 | -11.38233 | -47.33176 | 2025-09-13 05:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c2e7768-3926-373a-8a55-09c6a5893623 | -11.86747 | -50.57356 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 54a01a01-0c29-3a9a-95dc-9c64542b6e13 | -9.25845 | -59.41186 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0593c7f9-f7c6-31b9-a1eb-f19be0c5a938 | -11.15393 | -51.37815 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46f784d6-9882-3c4d-87fd-c5ec3e16abae | -9.81207 | -61.52797 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1509c6e2-57b7-399a-ac30-65adcbabec0d | -9.24265 | -51.22221 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b77a6c4-9cbc-36df-befa-2d3b90a86e36 | -11.10666 | -51.33541 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f4f323c-2c6d-318f-97e8-794102a5d035 | -11.07548 | -51.43385 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 79d64efa-4c81-33f3-b0a9-ba89d4767bca | -9.89175 | -51.86452 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6731e362-730c-3352-904d-bd4a4dc8b3cd | -9.79765 | -61.51127 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59eb1e57-d34f-393c-9102-9ffe31ee27e3 | -9.90489 | -51.89187 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 278bdf43-d150-37fd-aa1b-de0fabd215c8 | -11.19661 | -51.4157 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4b86066-763a-31e1-b5d9-e7c7afe4a2e1 | -10.33918 | -48.82582 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4d8506f-be6d-3375-8f25-e6e064826718 | 0.69563 | -50.64774 | 2025-09-13 05:25:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea42360-76ce-340d-8b11-9349f58ab466 | -9.23164 | -51.26305 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 966d6473-c675-309f-81c6-82beb6d9853b | -10.42325 | -60.8008 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c02574-1c65-313d-b6ad-15f29da94935 | -9.55586 | -66.73409 | 2025-09-13 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9cc1463-3a74-3db5-94a7-1a1c6f39fa75 | -10.76671 | -50.52658 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59997d24-f9da-3cb6-a6da-a6566194dfb9 | -11.39395 | -50.4805 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75f08daa-df04-378f-9df4-3bc37a44a8ce | -11.0968 | -51.44859 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aae6356d-2d11-3226-a63c-b74f1a8eeef4 | -9.48953 | -55.96661 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64893440-6e59-3fa3-9538-e40aba55f7fc | -11.81346 | -50.55362 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| faf3b997-e20d-39ab-8836-5517290d2803 | -11.18611 | -51.40623 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91d12570-1f0f-3a44-8c81-ee2bc47df29d | -9.26643 | -59.40548 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 48776112-0ae5-3f98-9478-2c797161ff46 | -11.11105 | -51.33772 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 58d30f7b-c583-353a-85f3-681df3f5a117 | -9.9192 | -63.18665 | 2025-09-13 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8208f095-5336-3902-8931-bc41c04ab042 | -9.73569 | -65.01045 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3945ee06-70e7-3d63-85ff-03b7cb6dfadb | -11.1124 | -51.33617 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e45dd33b-6330-394a-b6a5-bc051f92d031 | -11.13793 | -50.69574 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 51fc0234-59a8-3479-adca-2e8e5de641f0 | -11.5821 | -50.5681 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 2b0996ff-8d51-398b-a446-866a428a6dd0 | -8.0941 | -50.18248 | 2025-09-13 05:25:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1db95b9-6bf4-331c-aea2-3b916d36ef1d | -7.86301 | -61.17254 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4042d5ee-cdf5-31dc-88a2-adef6a5a50b1 | -11.8411 | -50.58057 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eda06106-fb5d-3e57-a73f-8c616ee116cc | -9.26072 | -59.39697 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a95628bc-c28a-3890-889d-81ebe1135ba2 | -9.24949 | -51.25796 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd1c7860-1610-3ec4-9900-8558b9684a11 | -9.14596 | -58.916 | 2025-09-13 05:25:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09fdde95-5b9c-3426-b7a2-bf8946404a84 | -9.62661 | -64.17954 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29d6d884-b489-3137-9063-4987fc37beee | -11.33239 | -50.78423 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 882bf6c8-926a-334f-8af6-59b7bba38074 | -11.10403 | -51.43754 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 34f137b3-3576-3b23-ae9d-dad62eac2cf6 | -11.27246 | -51.1286 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9fff0a5-a75a-3eb4-8f7e-d78b65f895c4 | -4.92719 | -55.78031 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb9cf2b9-107c-37dd-a53b-3055bf16faaf | -9.51603 | -54.63517 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 901790f7-b9f2-3587-81a3-9acd9c7de136 | -10.69986 | -54.44343 | 2025-09-13 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31bfdb74-cc84-39b9-aa15-dad08b94bb7c | -9.49364 | -55.96719 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3021edb2-296f-3a96-95d6-6a385b545884 | -11.18141 | -55.08749 | 2025-09-13 05:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39e4fffb-c825-383b-a7d6-a1dd192ac4f7 | -11.86028 | -50.58206 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a170ed79-0ff8-319c-bba2-4d4483108a90 | -9.80653 | -61.51989 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c85597-8c3c-33e8-8494-cd0b47ecaf6c | -12.11128 | -47.59936 | 2025-09-13 05:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 04f40148-b1d5-3a7e-8404-10befdb85d31 | -10.35938 | -50.50115 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 729b5a43-7092-3e57-a643-24e45d3db64e | -11.76692 | -51.51233 | 2025-09-13 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06950e08-4116-3fc5-9550-03874d77627b | -9.24533 | -51.24583 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e23af19-3b14-33a6-b1f8-d4bfdb20749b | -11.09361 | -51.42821 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a59cf0ee-0df6-306f-aadf-6a3d6260b40e | -9.23213 | -51.25927 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2585dd06-e3cf-35d0-8948-d084e5ce81f5 | -3.44036 | -59.57475 | 2025-09-13 05:25:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22892cfd-1d43-39e6-be08-f5b347339f3b | -11.09941 | -51.44337 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ed7907de-8879-3244-993d-420a2713243c | -10.33639 | -48.82536 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b36646c-ac47-3766-8071-72b8493da7eb | -10.77551 | -50.52039 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d633f00d-ef48-3f01-a67a-dd774b40b884 | -11.19005 | -51.41513 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 0baa827c-15ce-3d2c-bb03-d0e3cdf75a1d | -11.82679 | -50.54586 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3a05a1d8-7abc-3dd1-a2a7-5a11397f6c31 | -7.85968 | -61.17202 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38865fbd-9f28-3efe-af3d-a24eb6d7fdfe | -9.24437 | -51.2533 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 3779b8b9-7a39-3ff8-954b-ce2957ed3725 | -10.23712 | -48.63873 | 2025-09-13 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ed0f7b9-6ea8-3952-b1ec-1a2c4df7059d | -4.84566 | -55.87202 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b8d0664-5a4d-3b55-baf4-9115996726f2 | -11.07648 | -51.42598 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 597823aa-606d-39e1-b08e-d9530a9cee0f | -9.91086 | -51.88863 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b61fc8f-89df-30ef-9ae7-4b39081b8838 | -11.13194 | -50.69497 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 333ab584-af2b-385e-a34b-8b56673db619 | -9.83715 | -54.53347 | 2025-09-13 05:25:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fac46ca-7926-3563-abb1-28002de7b685 | -11.10607 | -51.43625 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README108.md)
