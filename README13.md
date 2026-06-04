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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fa5e0bb-6a2e-361f-86df-1a90bcce00fb | -12.73723 | -54.20519 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 079d3e93-0c9d-3d20-86a6-3ae57825d2d1 | -11.888 | -57.83003 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 971c192a-a09c-3b36-9475-f058a00deecf | -11.57239 | -48.14087 | 2026-06-04 05:01:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c937717b-9a55-38cf-99d1-c9717e5023a9 | -13.5412 | -49.9032 | 2026-06-04 05:01:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf4d3b5e-2f8c-36e1-8659-17e8247aaddc | -12.22057 | -57.28583 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 6f7ad190-948a-3367-9139-877335c4d614 | -11.554 | -52.78322 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41fb01e8-2ee6-39de-9cbf-ff2cbab8ef50 | -9.51691 | -50.26031 | 2026-06-04 05:01:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3c76b3a-985c-3f50-a0c9-70440066625f | -12.21562 | -57.27348 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de1b40b9-486b-3378-bc88-2955adcc0ee4 | -11.73497 | -54.80206 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be7c056-2f5a-3a5b-9e16-e9ef8508a1cc | -10.39048 | -49.44275 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| cb83c05d-fdb2-3330-baa5-1a84017bd333 | -10.57167 | -57.32418 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b3ca8a0-b9f7-330f-9a5c-3310d72f6fbf | -8.35254 | -48.14126 | 2026-06-04 05:01:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c45b5fe-5613-3db1-9027-62f06e61b97c | -10.86227 | -53.73639 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0b5bd77-12b4-30df-a9d9-5455ca1bb380 | -10.84313 | -53.74837 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5599f203-6049-364e-bb98-482871783b38 | -11.63123 | -55.18247 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4a4339aa-ee0e-3112-86f6-cbc04ab836b9 | -10.61017 | -46.68738 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 896a9c06-e063-3fa4-9677-0648be096cac | -7.34921 | -49.83429 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 841981f6-a043-38d2-92fa-aa1d21555245 | -11.61374 | -52.55276 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26bdca82-2983-31d3-92b8-1f6f8094bc01 | -10.9879 | -47.07514 | 2026-06-04 05:01:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a3455a42-2ee7-353a-b7dd-1ca414b53b65 | -12.46514 | -58.47568 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbab9b3c-c61e-3e9b-98c9-5426fc8c8cd0 | -12.17252 | -54.53967 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fadae17-09d4-3d45-a7a3-5f63d399c90a | -11.79519 | -54.02192 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5c5db56-ceb7-3e25-a81b-245094a86dd9 | -11.62957 | -55.193 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cff6dbb-ae95-37c8-9c15-37bb39116d19 | -12.56059 | -48.35128 | 2026-06-04 05:01:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8bdff46a-78a3-3777-bc1b-843068472d36 | -11.47738 | -57.10943 | 2026-06-04 05:01:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30535f0c-5974-3c54-9241-b2037bf8b1cf | -8.07157 | -46.18808 | 2026-06-04 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91822f1d-e5a9-3929-a39b-1d0d5fc8e60e | -11.62681 | -55.18895 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abb3e423-ec8f-3792-a5ef-dd3026f53d7b | -10.8988 | -54.13422 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b50746e0-7197-3b1f-8a21-5c68329c2869 | -11.744 | -57.82584 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3698c0b4-a4d9-343d-9ee6-efb13694a2eb | -12.45805 | -58.47442 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df0dde6f-6b2a-3880-ad6e-2a67c98a5fb3 | -14.04451 | -46.33881 | 2026-06-04 05:01:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d770be2b-ed2b-3db3-9d20-70fe62abeb04 | -10.8137 | -56.59642 | 2026-06-04 05:01:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fda47c32-c51e-32ad-9f93-4231f724d49b | -10.82102 | -56.59392 | 2026-06-04 05:01:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c9343b7-c265-3e3f-896c-67f2818f51fc | -11.54287 | -52.78556 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4843d23c-0b69-37f9-a230-64c5ae3e39aa | -12.46228 | -58.47098 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1fe4c83a-4ffa-391a-9e98-a4d6e50360df | -12.73385 | -54.20465 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3edc096a-77ae-37a3-b7f2-24a81c689b5e | -12.23043 | -57.26835 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 84e971d5-05e7-3336-b7b1-9437f3d68f43 | -9.4671 | -46.06181 | 2026-06-04 05:01:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8c1e6af-b0e4-303a-9b38-c34161f6e9c8 | -10.03112 | -59.33776 | 2026-06-04 05:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a0ec802-cadf-3ca0-b69a-98e8f3062ff7 | -12.46583 | -58.47162 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46c82c7e-2ed0-3023-90e8-50103a0f128a | -7.34674 | -49.82366 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42c6ff8c-8a73-38fb-ab95-fd9650a85ec0 | -11.62792 | -55.18193 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 32648b7d-4135-32fe-9f26-df1773272663 | -10.57575 | -57.32095 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bc345bc-cbef-3b4a-bce8-ec2b6c12eb05 | -7.34941 | -49.83315 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fab640-c4fa-3cbd-be77-4110c41e3635 | -12.5468 | -57.18025 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b7a685f-9904-366d-a919-b378c7edae4e | -12.17975 | -54.53714 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80c0bb9b-6bdd-3d00-b1b1-dc67ed14f94e | -12.21161 | -57.27662 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b9f4d48-c8eb-36aa-96d6-637848e74007 | -9.38923 | -48.62096 | 2026-06-04 05:01:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13578c0e-a144-373c-b8bd-c481df36e7de | -10.1388 | -52.12954 | 2026-06-04 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc968dc-0567-333f-9d6d-e0ea5145ac40 | -11.63398 | -55.18652 | 2026-06-04 05:01:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45f29f82-b4b4-309b-995c-ed9cdd8c9c16 | -10.38519 | -49.44985 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f9c7e79f-bb1c-33ce-95e1-18dc953ac48b | -12.22798 | -57.28326 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df74ada0-0716-3865-8078-b3fc6a606b8d | -9.88667 | -52.43733 | 2026-06-04 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff6d104c-f67c-37eb-9a46-13d945066ab1 | -8.07356 | -46.18433 | 2026-06-04 05:01:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c349f25-7095-37ed-97da-d7083e0de7b5 | -7.35017 | -49.82814 | 2026-06-04 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac340d01-e742-3286-89a0-03026dfe343e | -12.73835 | -54.19786 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a44a25-7fdf-35e9-a2b1-646304b61eb7 | -10.57231 | -57.32035 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ce483d8-4d4c-30a5-ac3f-e633b68a877a | -11.33569 | -53.96197 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7043de62-10ed-3a2c-92f3-11cd42decfe1 | -10.86284 | -53.73273 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 244cb97b-b882-36ae-8e2a-1a466022111d | -10.84538 | -53.75621 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b91be742-9f8e-3124-a3a4-33ae88e8a2be | -12.22982 | -57.27207 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 82e8473a-ee87-3665-9365-92a7c4511950 | -12.21439 | -57.28093 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 26c22365-40aa-3d0e-adc8-ff2640663656 | -11.88323 | -57.83721 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1fe427a2-c248-3d61-8419-ea1b10a1d5e1 | -12.31221 | -47.90351 | 2026-06-04 05:01:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f70c92c-d430-3a24-b8af-3acd7e91cce4 | -10.60155 | -55.42136 | 2026-06-04 05:01:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c34376d-730b-3b66-96d7-e243ec44277a | -12.46091 | -58.47912 | 2026-06-04 05:01:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0583c6a-5da0-3021-ae27-229d8262236a | -10.61216 | -46.71186 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 154fe300-736c-3e11-880b-4d6084088189 | -12.21378 | -57.28466 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d88da204-b7ea-31ea-93a3-731c4b365d59 | -10.38574 | -49.446 | 2026-06-04 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 020f4b7d-44c7-35f8-b3d9-83ae26c0dd97 | -10.00465 | -46.56755 | 2026-06-04 05:01:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bd1ed4d-9381-3d81-b3c5-c4fb00608bde | -11.16392 | -49.24411 | 2026-06-04 05:01:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa0b1ca-4d7f-3294-b4fb-aa24afa61d9e | -9.46754 | -46.05855 | 2026-06-04 05:01:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5600545-ec24-3f75-9f5b-01a4c4a0a174 | -11.60412 | -55.33278 | 2026-06-04 05:01:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8827d4a7-359b-36fb-a240-2585a457b643 | -10.56823 | -57.32359 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f3e139f-f4cb-3fd2-848f-26742150c6ab | -10.57638 | -57.31711 | 2026-06-04 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14861351-26dc-35f8-89d7-19b743b36d07 | -12.22581 | -57.27522 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b57e2c13-a979-33fb-bad4-2acb9e338c93 | -12.236 | -57.27695 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41328789-02d3-3059-b677-4ce6b276cb1a | -12.73779 | -54.20153 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7ad3ce5-1af1-30e1-91dc-4fe8db7b8cc8 | -12.73442 | -54.20099 | 2026-06-04 05:01:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 453a9c06-6465-3f36-86b2-1c2933da78b0 | -8.57151 | -46.00251 | 2026-06-04 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd58fd10-537e-35c4-be3a-3de9d4f26162 | -10.81034 | -56.59587 | 2026-06-04 05:01:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2d118861-d7aa-3832-b713-7447bb00388c | -9.89573 | -47.85851 | 2026-06-04 05:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb788b1c-304f-3d90-999c-83cbcb7716e3 | -8.57758 | -45.99662 | 2026-06-04 05:01:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed7a2085-b55a-3227-975b-e014e061523f | -12.1792 | -54.54073 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9619af4b-7998-3b11-bd8e-dd2a28b856ed | -12.21901 | -57.27406 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e5c86e60-b1c9-3857-9e56-0e5995fed174 | -14.04408 | -46.34249 | 2026-06-04 05:01:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b5d3551-9818-348c-94ce-4ab1117d4729 | -12.09543 | -51.9864 | 2026-06-04 05:01:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2716baff-5d53-3d50-bc5b-4443406cef7c | -8.27813 | -48.22563 | 2026-06-04 05:01:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da3523b-5088-3919-9e29-2825de70bbe2 | -12.4379 | -58.39941 | 2026-06-04 05:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0571c71f-d504-35dc-ac11-19d81272ded4 | -12.2252 | -57.27894 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7c059ace-546a-3885-b7fc-b869cad833d6 | -12.20915 | -57.29155 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| e4bb9975-c2f6-3141-9355-3f6edfe7a0f8 | -12.22642 | -57.2715 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ec5b476-56c0-329d-9cf7-d0c373b924d7 | -10.45222 | -46.57676 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee8434c5-b910-34aa-8183-ae039162ab91 | -10.86621 | -53.73325 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d5dfba4-6ce6-348f-99d0-5399a8e9191b | -12.09478 | -51.99075 | 2026-06-04 05:01:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db528e3b-1b29-32f5-80f2-8268b3d46e76 | -12.22703 | -57.26778 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da2800d9-cd21-36f8-9d73-6e96db4b8b8a | -10.80697 | -56.59532 | 2026-06-04 05:01:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b7e699cc-9df5-304b-a658-3fbaa525497a | -12.21255 | -57.29214 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba2998ea-12bf-3fcf-8e0a-cac71c567c3c | -11.26396 | -53.96958 | 2026-06-04 05:01:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5562d599-1ae8-3e2c-a3cd-324c4e2efac4 | -10.86565 | -53.73692 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README14.md)
