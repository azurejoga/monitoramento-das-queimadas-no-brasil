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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcd5b3c5-0eeb-3478-a306-c3caa0b38875 | -12.42837 | -50.02633 | 2025-06-17 04:10:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6986ecbf-d3ce-3838-81af-459b0152a320 | -17.00856 | -49.7823 | 2025-06-17 04:10:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f94c3cdd-0590-32f4-978f-06d86baec23a | -12.82743 | -47.37401 | 2025-06-17 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7219152a-9e19-3604-86bb-a7cda97519b4 | -16.29532 | -52.93521 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 128fcf39-7fb3-355b-a289-6fe717c8cce2 | -18.31943 | -49.88758 | 2025-06-17 04:10:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd1520f-3297-3232-a8f5-4b87f901c5d1 | -11.08331 | -55.06097 | 2025-06-17 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ae09c4f-a69a-393a-9aa2-a276c8065ee7 | -13.29269 | -57.07126 | 2025-06-17 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a94c73c-afa0-32b7-824e-2bc5ad97652e | -11.08279 | -55.0587 | 2025-06-17 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 749d094e-c29b-37eb-8763-0c1588e7431b | -11.93435 | -47.84391 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f14cfe9-19ed-3418-8534-67e5d3213566 | -11.89518 | -47.46987 | 2025-06-17 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55043f6f-637e-3267-a917-aac82a26f88b | -18.3242 | -49.88461 | 2025-06-17 04:10:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d8e37bb-2e51-3d29-b748-6f1a1173cfcb | -11.71972 | -47.73857 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed50ea9d-12b8-3607-b562-18ab101cf163 | -10.9296 | -56.83757 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9f7478f8-1e2c-3a11-8475-49c8ceec3cff | -15.891 | -48.89366 | 2025-06-17 04:10:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 590db1e3-0adc-35e4-8620-ee2526d3a1c5 | -15.38558 | -47.84682 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0fb0d0d-5d90-3fa8-aead-6f3d0e8bc80f | -15.39018 | -47.84267 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a113011-93e5-3616-8d07-4a871a0ccd06 | -10.93548 | -55.32491 | 2025-06-17 04:10:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b471478-8333-3331-abe3-84f6bc71e25e | -10.84724 | -53.77885 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5040c4ea-f484-33eb-9264-05c6353a80f1 | -14.85249 | -52.28562 | 2025-06-17 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90bd7bca-900d-3a73-8656-dfc0e9486c50 | -15.27232 | -51.47493 | 2025-06-17 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd867fc-fad0-3ff6-bf28-72ef6fcbe79b | -14.84805 | -52.28155 | 2025-06-17 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f60e1220-21b1-3dd7-89a8-679af941da91 | -13.39244 | -48.46048 | 2025-06-17 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cfcc890-80d0-33b2-a3b5-c67f2d385a33 | -12.22904 | -44.21616 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4183a8bb-74b7-3a55-bd79-320fc17d1c84 | -18.06063 | -48.89877 | 2025-06-17 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 31c4da13-7ba9-3796-901a-f88e1a27d262 | -11.92975 | -47.84674 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d9c4b60-1e77-3d9f-9954-de8926409766 | -11.91159 | -44.17904 | 2025-06-17 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4b90afa-8416-3d26-8616-1724e27a7f7d | -13.28584 | -57.06948 | 2025-06-17 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5078114-68cb-303d-ace1-2fdc07c1049c | -14.8226 | -48.43369 | 2025-06-17 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5e2f1be-ef79-36bb-bb77-47dfb1290073 | -16.30263 | -52.93615 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d55e615a-654d-3b08-acd4-3c7cb4f185f7 | -14.03285 | -44.11526 | 2025-06-17 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 310be5e0-46c1-3a71-9981-80c15db5803f | -16.59443 | -45.87839 | 2025-06-17 04:10:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 402c35c5-b11b-360b-926f-c7e146302700 | -14.02263 | -55.12047 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6561513-e932-3592-a517-3714812f01d4 | -12.22962 | -44.21254 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 462b60e8-1a5f-387e-b4a6-2f74049dec65 | -18.10586 | -42.3577 | 2025-06-17 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f5426e2-149f-3d12-84fc-84e511ffcb9b | -13.73719 | -45.24981 | 2025-06-17 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4631dbf-62ed-3ec1-9dec-ac6b0687ec70 | -11.4037 | -47.62329 | 2025-06-17 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 952c78bb-eb0d-32eb-8691-14dec54e4b5d | -14.81861 | -48.4333 | 2025-06-17 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10172bd1-70ca-3c35-b558-31a5489176a9 | -15.89167 | -48.89 | 2025-06-17 04:10:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d1b0e84-da6e-34b7-80fc-f6821654868c | -13.28684 | -57.0692 | 2025-06-17 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2583252e-a3b6-3520-b44d-f7a7c5c68703 | -16.29018 | -52.93422 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56b47406-eb69-3eed-a446-f279bb9b1d26 | -11.14104 | -53.93189 | 2025-06-17 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 57ff983e-9626-356b-9943-fe45b9dde98b | -18.32492 | -49.88078 | 2025-06-17 04:10:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bb0fa16-ac5d-3acb-b001-f1c703cda0b5 | -16.29684 | -52.93835 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1ff2200-03f5-3560-9a55-eb6601954a8a | -18.32015 | -49.88376 | 2025-06-17 04:10:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320d90e9-eb51-341b-a696-89e4de34b86e | -15.27229 | -51.47715 | 2025-06-17 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 296075a5-2b2a-31bb-b65c-84b602843263 | -13.3587 | -47.85108 | 2025-06-17 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8aa32faa-751b-3f9c-b430-ac927bc4be1a | -17.67853 | -42.7415 | 2025-06-17 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e01d82e-830d-3e79-bc0a-68db5d0b3343 | -11.39449 | -47.63546 | 2025-06-17 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f9a914a9-1a27-38dd-9fb9-6aadf0bc91e2 | -14.8519 | -52.28864 | 2025-06-17 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3bc799e-1776-38e3-bb57-2b8a535b8bd3 | -13.4409 | -56.85362 | 2025-06-17 04:10:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 759c1a49-798c-3917-8f3f-a22e19fdc005 | -13.47276 | -46.25282 | 2025-06-17 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42871444-f118-3345-abc8-bc86dab4477f | -17.4906 | -47.37984 | 2025-06-17 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86245632-2bad-3528-89df-039ccfddd77b | -13.46641 | -46.26887 | 2025-06-17 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29a9eb77-4bd9-3496-9f38-dc39d4338bc7 | -12.21149 | -49.62951 | 2025-06-17 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe6b218-e80d-326d-8c10-cf7f465a82c9 | -14.02825 | -55.12457 | 2025-06-17 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8527fcf-6b90-3958-b0a7-4a4229d27fd1 | -12.2297 | -54.29958 | 2025-06-17 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8900c1ec-eb58-3942-b3bc-7e892b2ef391 | -12.22845 | -44.21978 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4965781b-bd33-3f16-a58f-50979e7eee9b | -16.29746 | -52.93534 | 2025-06-17 04:10:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3764ce9-a1df-3ca9-8639-0a62f0970b1d | -10.92809 | -56.84491 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 91d6e2d5-2c8c-3d20-8fb6-b5c98a3b548f | -15.39099 | -47.83802 | 2025-06-17 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9fb41021-fdb7-3ba7-872e-d55342cc775e | -10.92563 | -56.83768 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1b6b60e2-63fe-3213-b2cc-3f364af0f84b | -13.89695 | -48.73435 | 2025-06-17 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d4c454-d3d0-3b05-9f41-313afeec2c69 | -11.91101 | -44.18266 | 2025-06-17 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| caa670fb-cd30-394f-aa80-10a785f09e7d | -14.64637 | -48.06106 | 2025-06-17 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86b674a6-efb9-3216-ac2c-09675d079ad5 | -11.56491 | -54.57633 | 2025-06-17 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9da9a0a4-ef40-34bb-833c-2c7a3b8cddd9 | -11.71826 | -47.74046 | 2025-06-17 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 968586b0-9054-30d4-b9d2-513aa7a88402 | -11.9103 | -54.82253 | 2025-06-17 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dca12eb-c3a3-3e70-b4d0-71a6212346a7 | -12.2318 | -44.22033 | 2025-06-17 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c24dae08-64d5-3de7-9f4e-c86bfa05be64 | -10.93667 | -56.83918 | 2025-06-17 04:10:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94a5e6a6-b541-3f74-a336-bf45538c2233 | -11.89606 | -47.46486 | 2025-06-17 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58c5b9fd-ccfd-3e95-a889-612c94eca4d8 | -23.63056 | -46.4264 | 2025-06-17 04:12:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a38661b0-553e-3795-b6ea-55b0715cb758 | -21.42901 | -48.64577 | 2025-06-17 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 627ac56d-6f9a-3300-91cc-de2a535df40b | -20.37873 | -45.60223 | 2025-06-17 04:12:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc657cc6-ae14-3320-b432-3a96757315ec | -22.77544 | -49.3141 | 2025-06-17 04:12:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 86df8870-f8b9-310f-ad77-f06ef7583379 | -20.83759 | -50.53452 | 2025-06-17 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f1a63929-f8df-31bf-a70f-81b093fd47a4 | -20.31303 | -45.58723 | 2025-06-17 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f7ac4fd-36e1-3f24-afaa-4ae4f1d12f3e | -20.19367 | -41.99019 | 2025-06-17 04:12:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68825a9e-995f-364d-abbd-7f3155172642 | -22.85776 | -42.98011 | 2025-06-17 04:12:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9760dcf3-8521-3c87-956e-c89b42e3858b | -20.15248 | -45.20705 | 2025-06-17 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3202c823-d3e7-38ae-ad6f-55b62380f122 | -22.69774 | -43.34786 | 2025-06-17 04:12:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36646f44-58b5-3c95-ae9b-551988efc717 | -22.76812 | -49.31254 | 2025-06-17 04:12:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e40b3fe0-8ee2-3762-b033-2b099b7911ec | -19.00246 | -52.08165 | 2025-06-17 04:12:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0295b941-7fea-3431-a7fb-1aeea9c9bd7f | -20.55109 | -54.12551 | 2025-06-17 04:12:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4c8bbdc-e722-3e19-b8e7-29a895e166f9 | -21.4254 | -48.64502 | 2025-06-17 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d79f8fdf-548b-3ad6-9106-83974b5a8557 | -22.77461 | -49.31874 | 2025-06-17 04:12:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbffcc2a-2783-3273-8432-9368650f4b6c | -21.97851 | -42.80353 | 2025-06-17 04:12:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 13a0b778-bbf9-39b2-a6f0-4568160e4720 | -22.78584 | -43.75611 | 2025-06-17 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 487b80ec-5607-3830-9fd5-f772ac0e31c2 | -19.30677 | -49.50291 | 2025-06-17 04:12:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 568fa9e9-672d-3c72-b994-67751fba7a1e | -20.8096 | -49.62911 | 2025-06-17 04:12:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9637b705-2f63-3efd-9333-20c3111a59c5 | -21.19503 | -44.93717 | 2025-06-17 04:12:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c316825-923c-30ca-8114-ac8441c3a54e | -22.67627 | -42.85558 | 2025-06-17 04:12:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9ce90e15-2e2d-3645-abfd-1cc7bb29bc13 | -23.71114 | -46.89609 | 2025-06-17 04:12:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b93c341b-f1ea-3c25-a65b-3b35fd7dbd4f | -21.69005 | -45.01231 | 2025-06-17 04:12:00 | NOAA-21 | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7926475-9078-31c2-89ce-0bd434d39733 | -19.98614 | -47.18451 | 2025-06-17 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52907e00-f257-347a-b688-8ca236518f6c | -20.1972 | -41.99076 | 2025-06-17 04:12:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f3e428c-96fe-33ec-9835-f97062bbcfbf | -22.90154 | -43.75508 | 2025-06-17 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fab3fbec-e5d5-3073-8d1e-6c31136546a4 | -21.13092 | -47.79277 | 2025-06-17 04:12:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 249c6b0e-c9ce-3535-b4c4-83697e0bc139 | -23.40668 | -46.4205 | 2025-06-17 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cfebcc76-5524-3d99-94b3-be15ebcfffc7 | -23.98501 | -48.91916 | 2025-06-17 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5408667-703e-3226-9cb4-bf57d369abda | -20.76281 | -46.77064 | 2025-06-17 04:12:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README10.md)
