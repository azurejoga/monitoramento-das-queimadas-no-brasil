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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4d5c5e4-eb02-3092-bdee-7d9ba5a1f4bd | -14.95572 | -49.98208 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 483973af-c5a6-37b7-9e15-5e0b1a61970b | -13.29481 | -47.80743 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0252ad00-e124-32a6-8572-5750c87b846a | -14.87312 | -51.50738 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c526ef1-68e4-39a9-be58-eb52a5b6b2cf | -10.6087 | -49.12744 | 2025-10-06 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 932c3d64-3647-3977-bda8-8e0d157cb585 | -12.42455 | -51.1054 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25b04379-577d-3c5c-9a59-c6be97f447aa | -15.24044 | -49.27957 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b6b3eb3-c365-3d2b-83c4-7d0d37e14b1b | -11.32025 | -54.34467 | 2025-10-06 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b1070dd-17a0-32a3-9e23-6cc8b476ed9c | -11.1765 | -47.73494 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9178dd2b-f1ef-3a57-bc7c-d28c9e254641 | -10.49889 | -51.50043 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2a4778c-4f62-391a-89c6-b8458a1906b3 | -15.87994 | -46.26472 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db980cce-26d7-3a50-865d-47d42ad062cb | -13.72991 | -47.96555 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bd49226-9b16-36f1-90fc-d3ba7dce2b7a | -14.91229 | -46.8601 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64df602f-f085-3e0a-bad4-f355f8e9105d | -16.02742 | -50.9645 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af897ebe-0812-3b99-9b4f-8a32d3264dab | -14.6932 | -48.28751 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19221c51-a7f4-3f62-bcc8-77b9bf9659cd | -11.4228 | -55.06754 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc3f2818-f7d4-36f4-8f46-bfe3707f1a11 | -13.25438 | -47.23664 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa10abdc-725a-3b2c-ab25-f99ac62b6668 | -12.45071 | -45.55069 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02e58de6-7bb5-3631-a33b-265274859ed6 | -16.0092 | -50.83961 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d62945b6-d38d-3c7f-aaf2-7b55ca2314f6 | -10.23175 | -52.70101 | 2025-10-06 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09922719-387d-3cc0-9b80-f2af9daee075 | -15.75083 | -46.26142 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56cc7fac-4c47-3be3-b0c3-5d6e68970afa | -15.97827 | -50.85441 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed0961ff-89e2-3865-af29-021911c20dd4 | -12.9056 | -47.29295 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efdb9bad-6598-3489-9a1f-96fbfa7522dd | -15.60772 | -46.93894 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f918c9d-6615-3a95-b2db-5d453f65f1ed | -15.23538 | -49.28989 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7147522d-77a7-399c-9c54-a155ea647fa9 | -9.54688 | -54.59505 | 2025-10-06 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c92b00af-6803-3162-93c3-7b1538436534 | -15.28782 | -46.31468 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb52103a-448f-324c-85fe-995d22914f20 | -10.21759 | -48.1777 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66e64c9f-9b64-3415-b1dc-9a40ef3ce329 | -9.78943 | -48.27934 | 2025-10-06 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09e60415-dcb4-3fc6-bae1-8de6cca208d1 | -13.3759 | -43.62563 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f704c115-d88c-39df-ab0e-f97980943221 | -16.01245 | -50.82025 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dc32986-931f-37ac-b911-0b9a20f31d4a | -9.62485 | -46.62487 | 2025-10-06 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1a7bc41-3e28-37eb-97f5-9816e70e7397 | -16.012 | -50.8441 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5688348f-b9ef-379a-8ff2-6b20df09caa5 | -12.2504 | -47.85257 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1e9f59a-a808-309e-9ef1-e206f6bfe914 | -12.48452 | -45.55978 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 07accf58-376d-3ed0-8493-4af81dec00c2 | -14.3221 | -47.65684 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cbe3f51-0181-3cd9-9449-e044711ae8f5 | -15.23712 | -49.27902 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aac19871-58b6-31de-bf6b-8fb993de602b | -8.60887 | -54.97291 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e28d22d3-731e-359a-a2e9-fc678670cbdb | -11.66927 | -47.47803 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 314bfeae-877c-37da-a494-96c03f92036c | -11.68577 | -47.48068 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac875272-6788-38c6-afa1-be115cf6088b | -15.50096 | -46.85781 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7977b505-1f4a-3b10-ad3d-4263fe3bd666 | -11.84535 | -45.05383 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56e615ed-cfac-37df-9972-d2d8be61e8d3 | -13.25873 | -48.47075 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3807358-54af-33c5-b72a-3cb1d08cec9a | -12.90505 | -47.29649 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31703921-b086-30d9-92c9-6ef2fc5938e0 | -13.09473 | -47.93707 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f445174-1b81-334c-86a0-7c54399600b7 | -11.49609 | -45.04352 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8bf9a9b-2d7b-3274-b628-b93e8409b6a2 | -10.2227 | -45.49641 | 2025-10-06 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98b562b9-4925-3fee-8ecc-8b2fd5227abf | -9.68326 | -49.95844 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0299675a-ebee-3a55-b11d-cb367d691efe | -14.54499 | -46.95219 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 501b53f5-5428-3347-be26-c09948c48458 | -13.35547 | -47.19817 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 655036b3-a05a-3923-b65e-45012fd8afcb | -14.08525 | -53.00575 | 2025-10-06 04:27:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c86cf58-55b2-3ec2-aeb6-a17397b08024 | -10.31864 | -50.26466 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 604b6448-720c-3df5-bd80-40dff5161a68 | -14.60445 | -52.49979 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 216bbc3c-760c-3e27-8063-02fb55ef949f | -13.10353 | -47.92408 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5017f1b-1757-313a-b5b0-dafea2a20e25 | -14.27103 | -45.86749 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26977d33-7459-3826-b4d8-fc95481f79d2 | -13.26845 | -47.84637 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 090fa541-0075-3686-a38a-8eba108e69aa | -13.71999 | -48.07239 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36c58a34-5d03-3cec-a54b-0ee0479b1e83 | -11.5213 | -47.68373 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11ba63b5-522c-32a0-b102-8ab333726098 | -13.36957 | -47.5709 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bf12a87-d105-3492-9d18-a5109acb3b49 | -13.10956 | -47.79895 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b2d2a83-f4c1-3f88-b210-2da5d101a0d1 | -14.5649 | -46.68098 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| caf0557a-2fe9-31b7-a87b-3e3c85931ac3 | -15.65929 | -53.83656 | 2025-10-06 04:27:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eb3bcc19-4c06-381d-8cbe-b087df1aaea2 | -11.74575 | -51.51412 | 2025-10-06 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f3d9f60-f63f-3871-9fbd-a4f750a2c2ea | -14.95911 | -49.98264 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d7db9fd-b02b-3038-af74-dc23a6e4c49f | -11.38424 | -54.35178 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b47d214e-9a0f-3dd8-82c6-ac4b5101fd3e | -13.22174 | -47.82076 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15e24b23-d977-3a93-9ea6-6216ec0edd0a | -13.29096 | -47.81041 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab8dfccb-d092-3a11-82fd-70236065c210 | -13.48491 | -47.24102 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ef48909-8456-3c7b-9849-94d9befcd605 | -16.0146 | -50.8286 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a10d132-d87c-3a38-90dc-f4d7b4af7f1f | -11.15923 | -47.92985 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e14faa4e-ef40-311f-a6f9-820078bd98bf | -11.07551 | -47.92004 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 173a5ad2-7cff-3450-a3d2-454ee5c660a1 | -11.91633 | -55.91016 | 2025-10-06 04:27:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c95561ea-d699-3095-93c7-1e84f9be2dc7 | -14.69306 | -48.37463 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fa00f71-416a-35f0-ad6a-8d6538a49473 | -15.29703 | -46.32344 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5996d96c-9b1f-3da7-90d4-03ebdc033209 | -9.02433 | -50.6843 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3977ccf-1a63-3c9b-b68c-9ef10f024109 | -13.26807 | -47.19185 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93942ccb-b19e-3cc3-aaa6-ae31d2579a62 | -13.35879 | -47.19867 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38bf3009-cb74-318c-b0b3-f1a25d8810f3 | -12.41003 | -51.12513 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bd28570-a804-3dd7-83c4-d159d1853f4d | -11.92155 | -46.63922 | 2025-10-06 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 73e45b99-18f8-3da6-b90c-df05ad64097c | -15.29751 | -47.32475 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bc67b20-77ee-32f9-934e-8d6ebeff23a1 | -13.08648 | -47.83846 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6387e4f1-5393-3cc0-acb3-507b772e1be0 | -11.71588 | -45.37944 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b7624a3-9ae9-3713-aa95-a44931d5bde7 | -15.57704 | -47.2726 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a1cadfa-3472-3920-a47e-4e1fd14d51b8 | -13.68635 | -47.34606 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1daf409-916e-373e-a7d4-39a78cde58c6 | -15.28962 | -46.32625 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85f9d859-c8f7-351c-83e3-3917c085edda | -14.36233 | -47.72512 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7d0d53fe-c860-3a70-b89a-64230446b154 | -15.88106 | -46.25705 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf82f3a8-ddfe-3ae4-925a-686ab96fc17c | -14.46441 | -46.33791 | 2025-10-06 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cb40dab-8794-326c-a0b9-dfa357815d34 | -13.50353 | -43.62616 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 292dbe78-6b42-3df5-928c-9e940cd2528c | -14.91112 | -46.84499 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cae49221-2591-3826-a1ff-ff027f0b8663 | -14.67435 | -48.38606 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43138dff-ef18-34cc-ba05-5b976ebf27b9 | -11.03081 | -43.09966 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60e8ccc6-8ec5-3336-bbd8-f52f0425ac13 | -10.40441 | -51.59301 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f69cc62e-5a6b-3d58-a89c-f01e72ee8ddf | -13.31349 | -48.05982 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3dcfd43-1e13-3929-92a2-a7d2630b4f9f | -11.43943 | -43.4859 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92373296-0723-3937-a7e5-ae6ab39652a0 | -12.58057 | -46.73183 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba5c4376-017f-3ba5-b87e-92c7f5a4a7f0 | -10.06704 | -50.48739 | 2025-10-06 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d76034ce-b36e-39db-bc8d-8666701ce07a | -13.33879 | -47.59473 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd4c7bff-92b1-3a06-a451-f24a0085c398 | -15.34699 | -47.3109 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2b676d3a-99d3-357c-81ae-b8f223edf05a | -14.91277 | -46.83396 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| de703772-e32b-317c-a23c-926342712362 | -16.01359 | -50.96187 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README51.md)
