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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 559e2b63-19f3-3c1a-aec0-985a14ab239b | -2.59053 | -53.38164 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 689b16ff-b25f-351f-beed-d358915e3637 | -2.58971 | -53.37761 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 463732c5-60e0-3f5c-a7bf-cc1c7d23eb24 | -2.58906 | -53.38177 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 37d6b2f6-ec81-31fd-980d-7a54bed7c05a | -2.58759 | -53.37693 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e6007559-b42a-30c8-9dde-8100913e1ce5 | -2.58691 | -53.38108 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b902bc65-a09d-39d7-bc6c-10e8e968778e | -2.58624 | -53.38525 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f88dd73d-7166-3b7a-85b1-1a082d1c466b | -2.5861 | -53.37705 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e878d079-2fbf-301d-9bfa-b569653b3d2d | -2.58545 | -53.38122 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4c42c927-02d7-3d48-9a51-c5f556a552ad | -2.5848 | -53.38539 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| df3054da-55ad-37cf-bb23-4b32ca71b1a8 | -2.58249 | -53.3765 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6726e8f9-f918-33d0-97a8-7bba36930399 | -2.58184 | -53.38067 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 42b49ad9-1ef2-3237-aed5-f9ae3c0da4d7 | -2.58119 | -53.38484 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 998f4de0-a760-3ef1-b8d0-bc271615d852 | -2.57822 | -53.38013 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a110764e-9444-305d-ae87-be70f0bea7f8 | -2.57757 | -53.38429 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a55432a9-b5c9-3959-ad4d-6c7fe84758e2 | -2.57692 | -53.38847 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| afc3f1b4-06f1-318d-a059-85d291c60613 | -2.57396 | -53.38376 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 07624484-5ce1-3f77-83d8-5693b864c775 | -2.5733 | -53.38793 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 32b9918a-8618-34f6-ad61-a11e1fe8385e | -2.57265 | -53.3921 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f521dc5f-0fdd-35c1-9c4d-854f118d36f9 | -2.57034 | -53.38321 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a65e2162-68d5-3ced-9fc3-5cda88eae82b | -2.56969 | -53.38738 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b54862a2-6a8d-3708-a33e-a5f271f36e74 | -2.56904 | -53.39153 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 75e6b260-0332-39e9-8172-bb925ae11bf7 | -2.56608 | -53.38679 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 169f16a3-d3a8-3c36-bf4b-caf565bf5f5e | -3.31263 | -52.85697 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81cefedb-6e49-3b13-999b-65159167e3b1 | -3.31202 | -52.86087 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70e0c44e-61cb-3313-ac6e-3de995fa1d79 | -3.30373 | -52.95969 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e98d475-2b17-3991-a888-a9f533160e09 | -3.30022 | -52.95914 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d9af7e8-0f69-32ec-a79f-e45759009707 | -3.2791 | -53.2527 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2ba6930-8795-33b6-9330-86737d4b0544 | -3.27845 | -53.25671 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 54f97dcd-dc00-38b2-9d66-4a13f022af34 | -3.27167 | -52.73193 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af7346c6-4860-3262-8307-1ecabe09d15d | -3.27104 | -52.73582 | 2024-11-03 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d881f8e-e98c-37e7-9886-17388b6b0fa2 | -3.25983 | -53.34963 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb644724-a3a9-3dad-9b32-3efbc5930bcc | -3.25916 | -53.35374 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53257946-e826-3691-b9f0-badc62a93b3d | -3.25849 | -53.35788 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d006f244-5982-3e8d-aa64-95a1c7589dd3 | -3.25783 | -53.36202 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9b2e418-13a7-3e4d-a0f1-815444d58a48 | -3.25411 | -53.06889 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf0f34ad-0d57-377e-87ea-be8e69f68b75 | -3.25348 | -53.07286 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d328073e-52bb-39a9-8bbf-ccfde0a54ee0 | -3.2522 | -53.33603 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6065130e-d573-3756-9c49-57a61cc4a750 | -3.25156 | -53.34011 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da46be9f-f15c-3186-a5b7-196d9a1edbfa | -3.25109 | -53.33566 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99b8bb78-861d-3bd6-bf51-c16755345d94 | -3.25057 | -53.06836 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5370f5c-04b6-37a6-8219-40724c6ca2ec | -3.24995 | -53.07233 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28f3f352-3a68-3fb5-8be6-5061f2984922 | -3.24932 | -53.07631 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5e051e0-771f-303b-bfba-adb524b02d44 | -3.24862 | -53.33546 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85935910-0f3f-38c3-bfc6-2d9a596dc992 | -3.24641 | -53.0718 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72314d4c-fe91-365a-96e2-12330a524b0a | -3.24578 | -53.07578 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9fb0cb5-e8bf-3969-92cd-756c343a0995 | -3.23991 | -53.36774 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47f49fb0-3ea2-3373-9d0c-a9301e6e5b9d | -3.23927 | -53.37186 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813bbcfa-62b8-3c38-9d0d-74ffecd15ef7 | -3.23698 | -53.36304 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d337babe-7b40-387f-a272-90dce8d2de57 | -3.23633 | -53.36715 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0af31c4f-ec70-3b86-a6e5-ae3831fb3cca | -3.23569 | -53.37126 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea5a27e4-1805-3f6d-b317-b3eaa7c4be62 | -3.23276 | -53.36657 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2693fcfa-9d62-311f-8393-41709c62aba7 | -3.21419 | -53.00193 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5772bfbc-ccff-3b3f-9afe-6aea0b3e65c4 | -3.21356 | -53.00586 | 2024-11-03 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6bfa47b4-7a03-3e98-b6ee-b8cc65bc5c70 | -3.80617 | -52.35141 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 779b0eb4-7f4b-349a-b584-b067ac31924c | -3.76285 | -52.36 | 2024-11-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 725c0c57-4f63-3a4e-bde7-423f5de05714 | -3.73251 | -53.39068 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 354d37a3-0f70-3d7b-8460-0cf32da3f628 | -3.71209 | -53.75223 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e6978c-9e70-320c-b875-f3900b395f2f | -3.62444 | -53.52528 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34bc5d0f-c4e3-3cd1-9c30-8e70511a9003 | -3.62084 | -53.52473 | 2024-11-03 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9a26080-b26d-3433-b412-e2c4a21ddb7b | -2.23924 | -53.48634 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9a65ede-ddaf-38a4-9bb0-12dfe52e7df4 | -2.23858 | -53.49058 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c9b8e96-061d-3a4d-8c9f-aaf81c771612 | -2.184 | -53.67148 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb900c20-35f9-3c28-9169-cebee700795d | -2.18332 | -53.67583 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cd237e6-88ff-3ceb-8103-f3c21871176f | -2.18263 | -53.68019 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7dac561e-90ab-3701-b58c-4fb9bd4b2b4c | -2.18237 | -53.65786 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd18d524-03c8-3613-9e6c-cb1bb999bab0 | -2.18169 | -53.6622 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28b75e3a-3d35-35e4-a4b2-775646e141c5 | -2.18032 | -53.6709 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f42c2d43-7a7f-319f-91b7-a1b0842bab04 | -2.18013 | -53.72022 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2cdee9a3-0546-36f7-8a5c-749e34d28310 | -2.17963 | -53.67525 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b529c9f-e429-37da-8ae4-b8e5cb8ee5ec | -2.17944 | -53.72458 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64e34b8a-28b7-31da-aa98-925e6f7d66b0 | -2.17895 | -53.67961 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1f99fb7a-5b62-3aef-8bb8-1fce1c1612ab | -2.17868 | -53.6573 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5337d5d8-31f0-30c2-b0b1-4f9170b6127b | -2.17826 | -53.68399 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 98e88c7c-5199-3095-8ae7-a388d223a82f | -2.178 | -53.66163 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26496aef-8379-3717-bb4e-1d69b9a17a1e | -2.17757 | -53.68838 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bef5909e-ab3f-39b0-a7a1-6fd4692a0ac9 | -2.17594 | -53.67469 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02cfc628-e99d-3cc2-9399-e99fbb68687e | -2.17526 | -53.67906 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 46a1cb9b-496a-3c57-a0c8-007db3034fe8 | -2.17456 | -53.68344 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 61c1b56b-842b-3d49-9543-c9ac26633ea3 | -2.17431 | -53.66108 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f4f4ca-609b-3bab-8cfe-ebc5425d2cdc | -2.17387 | -53.68782 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0150b6bf-3ed0-3129-b54e-9c07a99a32b6 | -2.17318 | -53.69221 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c2d1bf1c-f296-3c1f-b342-2af833dd7a67 | -2.17294 | -53.66978 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef97a27c-cd37-30e9-9d20-bc2f2e7bc5a3 | -2.17225 | -53.67413 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dca97be0-07fd-3870-90ea-57431b35db5e | -2.17087 | -53.68289 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7202f283-6504-320e-bd36-78f108937aa0 | -2.16949 | -53.69165 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bd90b96-ebc9-3fe1-a631-db0ec1bf90b5 | -2.1688 | -53.69603 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa9fe843-e913-3003-be84-839262ef5f63 | -2.1681 | -53.70042 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a726b65a-b0d8-3229-af07-abe120c8745e | -2.16487 | -53.67304 | 2024-11-03 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b4d12c8-f027-3b51-a682-297b5d016951 | -1.91047 | -54.64394 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41fbb6ce-bf11-335f-bf84-e13302fe829b | -1.87109 | -54.68908 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 659eabc8-fb8c-3346-90f1-a11d6b02d05f | -1.87029 | -54.69411 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d146050a-053e-3294-b914-9546b369102e | -1.86716 | -54.68845 | 2024-11-03 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8153a0a0-fdbd-318b-b739-481962229000 | -1.60407 | -53.88011 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a846819-c1c8-35b0-b916-788eb450e57f | -1.56846 | -54.20731 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 655c9fe2-9925-3d77-acd3-db9739c1df1e | -1.56536 | -54.20197 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 059e7a7a-e56a-3584-b6a3-713b5f9b9c7c | -1.56463 | -54.20669 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 2187db7b-b245-3b9c-99ad-073fa9ff7988 | -1.53656 | -54.28533 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6816eed9-f739-3a78-9ffd-657f4553b26d | -1.50573 | -54.28058 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c6e6e94-1f6a-3b8a-8b9f-212959d538f9 | -1.50114 | -54.28462 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e41e250-1194-3bc0-9164-9a5ba65ee32d | -1.50038 | -54.28934 | 2024-11-03 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README57.md)
