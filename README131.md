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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a19e02c2-46c0-33a1-809b-cbbbeb0c3ca3 | -6.52278 | -60.05657 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9b55e640-b753-3c3e-b604-8990d5efe5ec | -6.51908 | -60.05598 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a93bd37e-8469-3136-86f8-4fc159c10cc3 | -6.51687 | -60.05358 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0d22d872-690e-3fe0-8aca-68764d740dcc | -6.5162 | -60.05794 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eeb30c4e-8f37-3b5e-8448-f0cc9961695d | -6.51538 | -60.05537 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a2a8063a-cf92-332f-8d95-5cf09a49ab81 | -6.51474 | -60.05975 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e5160ae-b597-33d1-8618-dcc7d04c6350 | -6.49873 | -60.07329 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d37225f9-3321-34df-90b7-c03067ae979b | -7.02736 | -59.41982 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d5db5e4-ef05-3b60-b2f9-ac681e21bf58 | -7.02664 | -59.42468 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fef41abc-35f7-377c-99de-9eda60aed772 | -7.02591 | -59.42956 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba08c886-0e56-3aa9-8574-1534b23f04ce | -7.02349 | -59.41923 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 446320d0-ee8d-326a-8fd6-74222d604aaa | -7.02276 | -59.42411 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87b6ac9f-ca80-3d5d-9bd9-0f82aa85c670 | -7.0172 | -59.4083 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e782329-1790-32ac-ad3a-a9a07356b2fd | -6.96781 | -59.47537 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1672d4c7-39f7-3afb-b229-1388750105a4 | -6.96395 | -59.47477 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93c50341-811e-37c9-b1de-88642d5db263 | -6.91755 | -59.79123 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5457922a-99ad-31a4-a6f9-7c860b644fdc | -6.91566 | -59.67159 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef6ffdf4-289a-3436-bc15-7e6c301a8d56 | -6.91545 | -59.7528 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76ff4b66-85fb-3aab-aa41-68a0e9bdd9b4 | -6.91166 | -59.75228 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25e69b79-4791-38c7-b9f0-d3200e253f29 | -6.90998 | -59.79017 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43e6bd8f-0b1d-3f11-a192-2c1557e7d708 | -6.77919 | -60.04613 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f2a4327e-ac79-380c-859f-162823be3c61 | -6.77854 | -60.05054 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 468f2e42-7869-3a94-a4e9-ce8b471a4ccc | -6.77482 | -60.05001 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daedda12-e49c-3dd3-9d39-ea5376719599 | -6.77416 | -60.05442 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a47a5ec9-32c3-3e74-b860-f8cc3bf6b68c | -6.76979 | -60.05828 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 590e424e-a30d-3a1c-8af6-9666e7686bc3 | -6.76738 | -60.04889 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 109f9f1b-b2c5-3a24-9010-fa35552bb991 | -6.76608 | -60.05768 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ef99b13-1ce8-3c65-83d0-0c936fc824fb | -6.76302 | -60.05272 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 607b0111-aa2c-3768-bad9-3c8bcfa08f98 | -6.76237 | -60.0571 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a0821bd-3bbb-3966-8fc3-4750abfe6f5b | -6.71618 | -60.11363 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2c85313-4f57-39b9-b23a-a932ad0bae23 | -6.71405 | -60.1104 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4ff3fac-9dc6-337e-b6a5-bba23c7b60b4 | -6.71035 | -60.10985 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3a7108b-0fc3-3093-8aef-926b914cea29 | -6.67967 | -59.46469 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65d5b1de-b393-34e2-b1b1-c5479effd7fb | -6.65992 | -59.78032 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c9c99a0-63c7-3b50-92e6-cffc6095515c | -6.65614 | -59.77975 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a673b676-2621-325c-9b8c-dd98e89f7673 | -6.6553 | -59.78222 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 448857eb-bebf-32e9-a3f8-251bb5771674 | -6.6069 | -60.00123 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05f30c5c-e47b-3bfa-85f5-23a0f0c04252 | -6.5485 | -60.01057 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1f7047c-2b2a-3af9-8287-3f079f7a6f29 | -6.54784 | -60.01503 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23328991-e4fc-33cf-a89b-9804253f2dda | -6.54544 | -60.0056 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efb695e6-1e1d-377e-b45d-03411e3dd024 | -6.54413 | -60.01445 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2984d477-a640-3add-95f4-b3b308197d61 | -6.54238 | -60.00055 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39c7231b-efe7-37a0-9ecd-eecfd5491d7e | -6.54173 | -60.00499 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37a999ed-2494-3c0e-9369-d1205407666b | -6.54108 | -60.00941 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e46f358c-d374-3de7-b9f8-11056d4a0850 | -6.53018 | -60.05776 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2fecf42-4233-3e61-b790-dbf2ef20e7c7 | -6.52647 | -60.05718 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0d97e95b-3684-390e-be52-4a9690d3e276 | -6.52583 | -60.06153 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0630597d-d909-3b00-81c1-014fe0a590a6 | -6.52214 | -60.06092 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b5b9352b-42c4-36fc-99d3-3ee32c736ea6 | -6.51844 | -60.06032 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7de4fa8f-af5f-3a6e-87b5-99f7c881f317 | -6.5178 | -60.0647 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 73cacb4d-423b-3cf8-a782-2b2033f6ef05 | -6.51554 | -60.0623 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f4ac5519-a4f9-3c65-b572-e5e079dcd3ef | -7.14522 | -59.30349 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61ea0916-9256-3535-81d4-d0389d1389c8 | -7.14448 | -59.30849 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 629ea1b1-ed6d-388f-a116-b40516491c8d | -7.14132 | -59.30291 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5af969ae-97fc-3da3-bb13-b43602732753 | -7.14058 | -59.3079 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab71e484-82f6-3bae-8dfc-a37b188abb6e | -7.13741 | -59.30232 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30b35860-dfaf-370d-9d52-e0d952cf1068 | -7.13667 | -59.3073 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9f2b2e3-9d42-316b-997d-21aee929768e | -7.13277 | -59.3067 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0840373-ba2c-3a3d-851a-ad11bad1a05c | -7.12961 | -59.30112 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e61536-889e-343e-805e-08ce0ce7a7e2 | -7.12887 | -59.3061 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e64859db-cd5c-3d28-bb76-f15e9e7ddad6 | -7.1257 | -59.30052 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f40c2ab8-8d9d-33bb-8a85-4a965f833794 | -7.12497 | -59.3055 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28b22b25-0392-3582-abf5-ff8153d9e700 | -7.08779 | -59.25912 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2e07a69-08f2-3f9b-9195-c045358a6ce4 | -7.08707 | -59.26413 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad5a9a8e-0460-325e-a2c7-3c0f0c097f6b | -7.08388 | -59.25854 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3c74b3c0-7f3c-35b2-be50-0a0b45ec3bad | -7.08315 | -59.26356 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a9466c5-d5cd-3a7e-a486-d45f44821a9b | -7.08099 | -59.27858 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aefcca68-6544-3e5f-be29-01d5108980df | -7.07924 | -59.26299 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e404f840-0016-35fe-bdb1-9c3d858e23a0 | -7.07852 | -59.26799 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53291f31-fa34-3837-8e9a-35df3da20063 | -7.07708 | -59.27798 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a53fc49-0c4c-32be-afcf-080a387fb8d1 | -7.07532 | -59.26242 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7af5f5d7-9f97-3119-9309-98340b52c2a2 | -7.07461 | -59.26742 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2330901f-2e65-3372-949e-529a0103d947 | -7.07069 | -59.26684 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7da0e544-ba36-326c-bca4-365f67e9a7a9 | -7.07043 | -59.26532 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 617ce9d7-2b19-3b07-aaea-c1864630439a | -6.81146 | -59.1452 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04ed8bc3-c3aa-386a-88af-8b0c9571cb32 | -6.80753 | -59.14462 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c8b1eb8e-e4de-3d6b-a567-708b3b30440d | -6.78975 | -59.31987 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d88a4b07-dbca-33a6-b599-4d69779060b0 | -6.78659 | -59.31437 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cb30c4bd-6a6f-3c18-9288-1b1902fc7793 | -6.78586 | -59.31931 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acd23575-fe94-3b14-af42-242beb73bdc4 | -6.78514 | -59.32424 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ebbe065-af0f-38c3-894d-27a762251894 | -6.78343 | -59.30889 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c805c7ab-8e6e-35ea-b420-76166737f5b3 | -6.7827 | -59.31381 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9c6551a6-9bf0-3d92-be09-c41a9aa9eed8 | -6.77954 | -59.30833 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3c9351e9-cb7f-3e4a-b011-65ba54b47014 | -6.77882 | -59.31325 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4a7bc596-90db-352c-a682-3159c71cc12b | -6.77809 | -59.31821 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 09a17276-8f0c-31e3-ae26-1e2604f21056 | -6.77737 | -59.32312 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4b1b9909-0b8e-3eab-b7d3-e96f290e30c4 | -6.77421 | -59.31762 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c3ac2c99-71bf-3e75-8547-67f07bea142e | -6.77349 | -59.32255 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2a140ab7-906e-3e96-8341-38e5cd6fe44b | -6.77104 | -59.31211 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 838483d6-f8b4-3610-b59a-bc11dc70502f | -6.77032 | -59.31704 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a921582c-c4ea-35a4-b8a8-56e53cd82dfb | -6.76572 | -59.32137 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 17e3bd3f-715c-3336-b109-336d613ec335 | -6.76502 | -59.32623 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 419d2507-7806-3692-a57c-94ae93059b00 | -6.76256 | -59.3159 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cafb5c39-6b75-3447-ac83-97833d14d691 | -6.76184 | -59.3208 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| da883844-d9e1-3bf6-a344-93e4aec7bc90 | -6.76114 | -59.32564 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3be54aaf-ba8a-3a5c-b43b-12b0dd11a39c | -6.75796 | -59.32021 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f6542cd-bebe-3fee-9fd4-d94d69bfd555 | -6.75726 | -59.32506 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8735a66f-bf7e-3057-ae7c-f23f8e67a013 | -6.75408 | -59.31963 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c3fbc4f1-afcb-36af-974f-106577f1bf1d | -6.74879 | -59.32878 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 64aaabba-304a-30fa-9633-29c82771f558 | -6.73986 | -59.30067 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README132.md)
