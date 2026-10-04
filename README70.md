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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9c03a4d-da84-33cb-8f97-26da5da7debb | -8.57722 | -66.82401 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bde007a-87aa-362e-b1d0-5f62b59a5048 | -9.92468 | -65.04604 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd1266b4-73fc-3da4-bb0d-1c795d08db77 | -8.89526 | -66.88712 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b12424f2-be2a-36b5-a419-0732199cf4c4 | -9.9182 | -65.04529 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b132f40d-ab81-3b23-9b05-dd05d8628c50 | -9.04919 | -65.42829 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a524393a-6bf6-34d4-881a-34ae571441a7 | -8.59277 | -66.81283 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40322c4c-babb-345f-91de-18d20e6fe617 | -9.47945 | -67.15765 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f1e56c8-9b10-328d-95d8-e3bdbbdb13db | -9.13384 | -65.94881 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53cd8151-d2a0-32d4-ba53-595cef7a9ece | -9.13442 | -65.94421 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87df09bc-fb02-38f6-ad65-40ea233a53fa | -9.01733 | -65.69356 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d32e8bd8-e7dd-3e60-984d-57dcff2fe749 | -9.89628 | -65.00976 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75c691f-5ff9-3e49-9fb4-0e98cbefaa3e | -8.59328 | -66.80897 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ddfa25f-b8ee-3446-ab28-85d1dede5fe2 | -8.57473 | -66.8182 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6131696-21c9-3c35-a289-d0871fa2bf20 | -8.34482 | -62.82965 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d3b7a94-ee02-34a7-830e-f2983bef6350 | -9.91306 | -65.0338 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb40796e-0ead-3a9c-9186-284cc38525e1 | -9.01656 | -65.69244 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10014269-9dc7-3eaa-9254-3dd08934092f | -8.57423 | -66.82202 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 532101dc-710b-37f0-b4c9-a5d8171a181c | -9.05544 | -65.42915 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc6ac04-d21e-3cab-a020-e66ce3dbca09 | -8.58448 | -66.81329 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a85defa-6ea5-3ae9-b606-78c77096dfb2 | -9.47387 | -64.33311 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97d4d6cb-39de-3bfc-9274-c107e9f7fa61 | -8.89721 | -66.73156 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f9fc313-bddc-3a1b-b5ff-ebe85d4f3059 | -9.11237 | -67.71155 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c7307b3-a040-3cce-8f29-523adccc2b6f | -8.57292 | -67.00788 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5e34eb1-78eb-3726-8a61-3c52b957c6ca | -9.50264 | -68.49587 | 2026-10-04 06:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d28fbc1-a8ed-3763-b1f1-27b4e65caba4 | -9.15485 | -65.39766 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 982ebdcd-c49e-31d3-817b-c846f13fe718 | -9.9124 | -65.03912 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cfe2c81-e872-3b6c-bdd4-5cc592c5c29d | -9.48059 | -64.3339 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3015392-e621-31ab-804e-ce31448626a7 | -8.89358 | -66.88645 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a358820-5b7a-3de8-94a3-e62ab4247354 | -9.91372 | -65.02844 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f60e3ff-d0fb-3fba-884b-dd7bc9ad1f8a | -9.03116 | -67.4748 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e44d6e-498a-3271-b65f-ae025dde1a69 | -9.92601 | -65.03539 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2341503d-c496-331d-9549-eafa64be03c5 | -8.86011 | -66.79089 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f9b2b60-bc10-346f-a47d-e4456abec279 | -8.88686 | -66.89333 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fb608f0-f28d-3296-8ead-c06c6496abf6 | -8.0503 | -72.44102 | 2026-10-04 06:40:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d9289a7-ccac-31cf-ada9-1482208c6c25 | -9.01548 | -65.70764 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1db8edb-c9df-3a37-ad8d-37d53ccf3780 | -9.13288 | -65.46935 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a993d388-0b1e-36b0-9146-4693062f165c | -8.89092 | -66.73494 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85ebe27d-2ceb-36d2-8cde-7e292ceab5d8 | -9.12665 | -65.46846 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf23ee15-75f9-33f8-bfe6-e0cf90565630 | -9.01608 | -65.70308 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71ca0c9b-20e8-300e-9a03-9c3759da7aee | -7.42319 | -70.10645 | 2026-10-04 06:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c98d7a7-f850-39b2-bc4c-222bdd73fb37 | -8.88738 | -66.88954 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a650d045-ab26-38e8-9fc2-956dfd2da75d | -8.57827 | -66.81635 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 070051a1-5ea3-3b9a-b44a-92ff19cad79b | -8.89781 | -66.73188 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f86f16ca-0bbc-3f82-8d9f-86516995b18c | -8.59896 | -66.80972 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c684e602-30b4-3fc1-ae3e-9a8f20900ecb | -8.54805 | -67.02348 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee2ae87c-d729-35c8-8107-47161f87f435 | -9.54172 | -68.52796 | 2026-10-04 06:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 961131ac-c5a9-3b2f-946b-8862e49ed31c | -9.48274 | -67.15576 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61111f09-8609-32ab-8839-fce15f99da46 | -8.56879 | -66.99586 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23789812-048c-398e-a15e-fba44f78d84a | -8.5804 | -66.81904 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7181fae7-ed8b-3619-8947-b76c407c474f | -9.01597 | -65.69726 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82243d83-52fa-3eb7-bf15-f970474512c6 | -9.13129 | -68.24978 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25f3a79e-c070-3203-8a23-c4c21416e14b | -9.04618 | -65.42429 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c0f523f-1923-375a-84c3-fbe9b60fb8cf | -8.05122 | -67.2684 | 2026-10-04 06:40:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e1b78d8-1d0f-3de1-a2a9-ad30c9b2beb9 | -9.88702 | -65.13847 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2defd85-eb5c-39fb-9924-b75cc1070546 | -9.89562 | -65.01517 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 910d381d-1161-3874-ace4-c5b4876a50ad | -9.0167 | -65.69834 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df180b72-c857-3458-a87e-23ad81409c0e | -8.3496 | -62.83999 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72b4357f-3cb5-38e8-b64c-86acd4de3880 | -9.03162 | -67.47126 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62ebfe04-1346-3c9b-bd0f-32788f7004fd | -9.01538 | -65.70201 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 105f140e-e613-3c36-88ea-65c2f5cd9aec | -9.13284 | -67.92609 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 291a2f80-34d9-3251-839e-b5fba9d3801b | -8.8544 | -66.79011 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28ba07b3-4512-39df-9b1e-1862f306d244 | -9.48824 | -64.69084 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e280baf7-12fd-3aad-b7de-0137d0bb57ea | -9.54213 | -68.52488 | 2026-10-04 06:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75e742fb-4b4f-3487-9d08-c0eca7e50b60 | -8.35205 | -62.8306 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f38b49d0-dbb5-3a7d-9c09-9276cb669ac1 | -8.58708 | -66.81208 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f3b91c3-0e6b-3bda-b600-a359c8c84068 | -9.13086 | -68.2529 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dd11939-b3d5-3182-822d-a10885b6757d | -9.91887 | -65.03999 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31689b79-81ce-3779-8c5b-7035aebbbe0e | -8.88292 | -66.8932 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46c81e72-bf72-35ee-8ba6-0c301d0d9b7e | -9.92534 | -65.04073 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff9826ec-aa27-3cbc-b954-9a06178a5beb | -9.46714 | -64.33231 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dad3d1b5-f0c8-3193-8011-c31ceaedb71b | -9.1278 | -65.94791 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ca5b503-d852-3e79-9a2e-6ecd1ca2c807 | -8.8941 | -66.88262 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbe64341-e8e0-3307-aed8-9bc265860cbe | -8.35116 | -62.83781 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| df382d96-418d-3d01-ad9e-367953cbd159 | -9.88059 | -65.1377 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab4bf1d0-5c6e-3292-8052-13b3bdd557d9 | -9.91953 | -65.03465 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 754ea776-dbb1-376c-88e4-4915d02bf911 | -9.05242 | -65.42513 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e963f7d-3673-3d57-9e62-ea4b9709bdc4 | -9.48509 | -67.15833 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fab4d1f-0f08-3c17-827a-cb5d3c6ef074 | -8.89147 | -66.73089 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9b421e3-d4de-38df-ab9c-8bb01a6b83b6 | -9.47314 | -64.33895 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3d99979-661c-34f1-bf7e-9db280d3dc61 | -9.88915 | -65.01429 | 2026-10-04 06:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f45729f-3b6f-30ef-b0eb-0224413b7edb | -9.0498 | -65.42338 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7e2f828-2bf8-3bb0-a9fc-306d0055838c | -8.59227 | -66.81665 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3008274-7632-34ce-a83e-32b6df8e7b60 | -9.1324 | -67.92938 | 2026-10-04 06:40:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48aaee5f-c1c2-39db-b37d-ea878f1abf9d | -8.89206 | -66.73116 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3136af5-f789-349d-9894-536100aa97d1 | -8.54757 | -67.02721 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 207227c2-7ab1-39b5-948e-31eca5caa03b | -7.49891 | -69.99529 | 2026-10-04 06:40:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb4d87d8-265b-3d17-9bba-d4fc8974960d | -8.89576 | -66.88329 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3baf2f4-4d2e-322e-9b5c-dc12f1caea48 | -8.5683 | -66.9996 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96df2ac0-ac59-3f27-9317-0d8d808bbf43 | -8.5799 | -66.82286 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecb3d88e-ddf8-3345-894e-4bc1f56b4b24 | -8.89201 | -66.72686 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a46e2bef-ebe7-3fe0-8a45-c3f1538d94e1 | -9.01481 | -65.70663 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c5511a1-4739-3ddb-bb60-ffb29f718eb3 | -9.02211 | -65.69807 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f908ff2-9312-361d-b547-8d383ffb76b0 | -8.89258 | -66.72713 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17d9401f-1546-33b6-b5d7-34bfc4e5a549 | -9.01717 | -65.6876 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4fa472e-a5c0-3412-922b-9c31df301a9f | -8.60651 | -66.97017 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a915a8a-a87d-397c-b773-12aca78b3e3c | -8.05074 | -67.2719 | 2026-10-04 06:40:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b80c6f1c-9505-313c-a949-74e8d894f507 | -9.50221 | -68.49894 | 2026-10-04 06:40:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce905994-c573-382b-a271-ecb818b9e6f9 | -9.01796 | -65.68871 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1d9b948-9063-3da7-b934-64db4dbae4ea | -8.58658 | -66.81594 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e70f5265-7ff7-3de9-9bda-9e5b1be540a2 | -8.88908 | -66.89021 | 2026-10-04 06:40:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README71.md)
