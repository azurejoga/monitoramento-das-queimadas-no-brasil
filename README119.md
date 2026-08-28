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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e823ea7b-3d5b-35cd-ad5e-340c2062c2c9 | -6.08154 | -63.42984 | 2026-08-28 17:28:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9cb03c22-1bb3-332d-a58b-e86c05041ac0 | -6.583 | -56.53837 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a3a6a79b-756a-39a1-a754-422cb0946d5f | -6.01277 | -57.78103 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 341684c6-5e27-36f8-ae46-50a69556c2e7 | -8.56582 | -64.17391 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 7aa867a8-7f13-3f71-821f-0ee747dacd4a | -6.82844 | -55.61686 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 75ba4981-ee80-30e8-9e5b-94cca91f2a9e | -7.04508 | -55.6851 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 10e6b716-a09b-3d12-bcaa-7197c604693b | -9.0742 | -61.4134 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6887ba8e-a60e-38fc-8fc9-cde63f63c9a3 | -7.99891 | -61.40649 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e050a36b-b752-38f4-b846-cdb66d2f4076 | -8.21806 | -54.95292 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4fce4de5-28c7-3dd3-8f9c-0490c62b6def | -6.19074 | -57.93639 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 586cae11-9ccd-35a3-a9a1-f96958b52a66 | -6.75178 | -55.68456 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 19131946-b521-3af4-bacc-f506d0ed5a52 | -8.80465 | -50.495 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 470c95b1-192f-376d-9c89-b12e56638341 | -6.36165 | -54.7798 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dc4af67a-8060-3620-a7ee-d06da82a6753 | -9.2497 | -57.07851 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fea5959e-695d-38c1-b1a2-45c699aa5930 | -7.91498 | -61.31647 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| d8f01bab-98cb-37d0-a6d5-acdebbc88e93 | -7.75575 | -61.09221 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b8fe64d0-32b3-32a6-8973-7e7b760b1b89 | -8.7952 | -62.48164 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 19ac74dd-04bf-3b43-938f-169c5b8cceed | -6.01867 | -55.68392 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6002c6e-d421-3f58-813c-05097fdef09b | -7.35343 | -55.18062 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 9f74b412-4729-3bc2-8b71-bd337712a896 | -6.24434 | -55.42862 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60926544-f137-3f10-acdd-20efe139932b | -8.95106 | -50.79124 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b336b6c-428f-3e8f-a320-2c2b7d5e4703 | -3.5442 | -54.49022 | 2026-08-28 17:28:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7aa7c8fd-0508-37e9-8aa6-4835f226a4cb | -4.89829 | -56.26391 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 83c75f6e-f61e-3328-a20e-cf0d3bfaf2e2 | -9.69807 | -65.09258 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4a997fae-f296-3f2a-acd8-054c3ac378f0 | -6.62666 | -59.08092 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 33f2dac3-a751-3847-9885-c5644de06dbf | -9.25974 | -57.07697 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 230a7fad-eb00-3e0d-a612-0b18d1e4394f | -10.75799 | -53.982 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7e9b2d4c-c04f-379f-9c94-895436dff8f5 | -6.8451 | -52.45259 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6f2b6cdb-28db-3033-b073-f9ad5cd99d98 | -8.60553 | -54.71149 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cfb89df1-b8e6-3e73-8c64-75b3ae17e1f2 | -7.84077 | -62.31013 | 2026-08-28 17:28:00 | NPP-375 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dbf71cba-2a37-31dd-823f-89271adaf2dd | -4.30635 | -59.47563 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0f9a1076-5adb-3928-b945-86f27b854dae | -10.06376 | -69.10595 | 2026-08-28 17:28:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0d729ba6-9aee-396d-b327-ec3925b1b6e5 | -5.09243 | -56.14252 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b1271c15-3d8c-30dc-a045-0437c55a42e8 | -8.16142 | -54.969 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0d88347d-5488-36b7-9a40-b2bc1a2b387b | -8.72065 | -68.20023 | 2026-08-28 17:28:00 | NPP-375 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a2fad03e-a688-34b4-b9a4-319904ed37d6 | -8.089 | -47.57934 | 2026-08-28 17:28:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dde7b5bd-554f-33fb-bef3-5146a9bc504d | -6.41098 | -51.6954 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 9747e604-0775-35ed-8ecf-78156b7509b5 | -8.77279 | -68.98175 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 16.2 |
| e0c6caaf-e07d-3958-98ee-19f3bd2a84dc | -8.68069 | -62.94942 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ab4ded88-0c2e-37a3-85c8-7092b4a7ba48 | -10.20587 | -69.36375 | 2026-08-28 17:28:00 | NPP-375 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 30.8 |
| edabcc9a-0824-3c77-abea-ded86fa5e875 | -6.32164 | -54.73842 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1f5413e2-21e0-32c9-b070-3da5906d13ed | -9.44606 | -51.57403 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9fab2e27-ff34-3c62-ad60-e842e7660b16 | -4.46953 | -54.96803 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ef8519e-e001-31a0-9cba-2f1d13bbb987 | -6.16055 | -53.50512 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6b719e0f-30cd-3d58-9091-17552b9eaa77 | -7.43318 | -59.77866 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1dbd7840-ebcb-3f2d-a70d-185b47e1bf5e | -8.66809 | -49.54831 | 2026-08-28 17:28:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7473fad3-9802-3064-8ea6-b1b5db8ef49d | -9.46994 | -48.21437 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 306668a1-4ab7-33df-a169-2cd25476d6c9 | -6.84804 | -59.94881 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| eef2aff8-9354-36ba-897d-5d5cc9cd5e08 | -9.66921 | -55.08183 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 91da12da-b2e7-3bec-86d9-c1a6e54cab3b | -6.84564 | -59.95774 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e5834283-7ea8-3619-877c-b7e42bc1eb29 | -6.26247 | -55.41082 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ffbc6694-4b0d-324d-bfe1-cf063e860eea | -6.27572 | -53.14577 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 9c98ab82-254a-3e8a-86e0-3cfea9785665 | -6.15201 | -57.9428 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cba78fc3-dce6-3c01-aa4a-d354ae5348ac | -10.392 | -61.23589 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1cf79a57-bcb9-3b17-a11f-4b96baeac023 | -10.76779 | -61.5036 | 2026-08-28 17:28:00 | NPP-375 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6f3eb1d6-b3be-3a43-8044-28751f281d5f | -6.53718 | -55.25056 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 3510f649-5c3f-34ee-b1df-6be6cb720802 | -6.94113 | -58.94823 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| ffb78a4a-0ebd-3bc3-a509-79b03ed7795e | -8.5963 | -54.78191 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0c25191c-f93f-32bd-8140-f1c4d3ff4423 | -6.94057 | -58.94442 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5973f68-0db1-3e4b-8cdf-74bffd37f8ab | -8.04575 | -54.0093 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aed089e9-87fc-3a26-acba-35c37f989a80 | -6.2101 | -55.41184 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 19b8ecc1-6df5-34e7-af9c-ce9a4db39a40 | -7.34558 | -55.66229 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64a3950c-9ece-316b-8472-d926c34f8009 | -8.60029 | -54.78506 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cf92354b-2097-3a08-a45d-6cfe4def9843 | -6.77539 | -55.68094 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 28d186b2-ba9e-304f-80ff-90491e2f835a | -4.95943 | -56.27198 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| acba5f81-8427-33aa-9feb-180ed944ec4a | -7.59501 | -61.3333 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5406155-4be8-3612-a826-0642ccd6a152 | -6.2642 | -55.42186 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e142a6a3-8441-3f27-b1dd-fe7dcbc9eaa1 | -8.67621 | -62.95003 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1dcceec6-211f-3387-8ea8-c093c16f46d8 | -6.15405 | -57.7984 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b5631fec-1282-36ea-b243-1c62bfafb8a8 | -6.15686 | -57.79438 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a0aefe1d-a31f-3934-bc7a-2bf27f1d5e9d | -6.71774 | -59.45107 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 18c58d56-0a97-3074-b068-9491e1e904a9 | -6.75571 | -55.68761 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 10566869-19eb-39ae-8a62-0f8877f67e54 | -5.48417 | -45.12397 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 1a14462b-671f-3057-a72b-7212cc7fd514 | -6.75289 | -55.6917 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9f576098-04c0-3b90-827c-a073585daaca | -6.77362 | -59.46709 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cdeedf94-d712-36ef-bb04-c8d491f5a547 | -7.60114 | -61.34793 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0b92b255-8777-3b85-b169-3a37a8967517 | -6.79253 | -59.39992 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 339c4572-d4a5-38ba-a96e-71e45633c737 | -8.98649 | -52.386 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9cccb22-d764-34df-9441-06b0b4579549 | -8.59913 | -54.77767 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 7cf81cc1-206e-3c9c-8218-9de254ad065c | -10.38742 | -61.23285 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 43d052b5-5f11-33ee-92c8-961fd9917f16 | -10.05167 | -68.82537 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 6165284d-9c7d-3770-bf03-898878d0e457 | -6.7248 | -59.45001 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 70feb246-0e3a-3372-9044-b104c88110b7 | -6.60051 | -55.45392 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3739a3ef-ea7a-3f3c-ae91-8ee1fa1ee47e | -9.27928 | -57.07035 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3605117a-55b2-3940-82b5-c70a5c5e1f20 | -8.43377 | -70.32865 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 29.3 |
| b25158f7-696d-361e-8dce-04f339ec5b4d | -7.58566 | -61.32435 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6aebd443-994e-319d-84bb-152c29c1e631 | -7.18141 | -55.42057 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 588e5aca-1c0b-3adf-9cce-d404f731ace1 | -6.54285 | -55.24214 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 9b5add77-7421-32a0-a86b-4b663e5dfb42 | -10.47178 | -64.48687 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9b63e54f-7738-3033-9b53-e11d5e8ffb37 | -6.90645 | -43.64769 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| f582789d-5dae-34e3-be3c-2b5da3ca9a80 | -6.75897 | -59.44108 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9264b3f5-9aca-3b19-8ca4-7645ac0960a7 | -9.27983 | -65.54639 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 74082f27-09f9-3b29-83d1-4b638884f782 | -10.38791 | -61.23642 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aa654c68-b733-31d1-aa22-e90293c75020 | -10.75786 | -54.04047 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8a319f69-5347-31e7-899e-210de98c8231 | -5.00688 | -57.01363 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e6e4285-4dd5-31fc-8966-d4bebb17f5bf | -5.64127 | -61.09013 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f6cca611-d606-38f2-b742-c3e88fd24fd3 | -7.48253 | -61.41401 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| fdfdacc1-f465-35b2-bec3-a2bbfee32147 | -6.59937 | -55.44665 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af0ba92a-474b-3878-a487-5980b4fd7701 | -8.43647 | -70.33341 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b21b96ce-4058-3631-a605-b2fcadb57e46 | -6.84083 | -58.99832 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README120.md)
