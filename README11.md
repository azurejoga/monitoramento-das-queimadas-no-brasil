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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebda4301-f794-3a01-b573-f061d945ff8b | -13.4023 | -47.87945 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3235aa58-f044-358b-b7c3-0ac5c310dde3 | -18.65038 | -55.72585 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 049fae80-252d-3d50-b6b0-5e6d92e11692 | -19.9008 | -41.73841 | 2025-07-09 03:57:00 | NOAA-21 | IPANEMA | MINAS GERAIS | Brasil | 3131208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e2ff346b-ea7b-3124-b325-98c4dc67b9fc | -20.47815 | -45.20692 | 2025-07-09 03:57:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 71500a05-f06b-38f8-b746-91797fdc8d58 | -18.6366 | -55.72223 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| e4dc6696-d1e8-3e52-bca0-a2b5d9728314 | -20.13266 | -41.56035 | 2025-07-09 03:57:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 73b1f98f-12f9-389e-a90b-07d0d72ee864 | -17.69382 | -46.74432 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f73cee37-31c6-305a-8fc2-a69876b56416 | -17.21391 | -44.80689 | 2025-07-09 03:57:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f0d507b-786f-36d4-9d7f-a8df73da490f | -13.39182 | -47.88266 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3a0ded6-c6f7-34b2-840b-e0457be3eda0 | -20.29235 | -46.67847 | 2025-07-09 03:57:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c1897bb-9bf8-335e-b01f-0e2bc42b25a6 | -13.00962 | -46.75088 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4b239e2-9e82-3b1d-a60e-5b60c19217c5 | -13.3994 | -47.89488 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8140b356-9aac-3eca-af40-2d4e07d94caf | -19.85828 | -47.44351 | 2025-07-09 03:57:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab58beb4-93e1-3b0a-b162-f8b8e6da2851 | -13.39664 | -47.88331 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 390083d0-fd47-3a34-a5c9-348539f0eba1 | -16.66222 | -46.03014 | 2025-07-09 03:57:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28fd2e64-9f53-3c47-8829-0ae6ba34c8a6 | -13.39751 | -47.87865 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ae061f8-ff6c-3dcd-b24e-de62b9d00ddc | -13.63621 | -44.41822 | 2025-07-09 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4bdd9298-abd6-3ca8-abc5-d553418448e0 | -13.70387 | -45.61996 | 2025-07-09 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e04097f-7da9-313f-b387-dbb47f8f537b | -15.6611 | -51.09623 | 2025-07-09 03:57:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cee6d66f-4b79-35eb-9cc9-9ed3f22e7cdf | -13.01148 | -46.29084 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db834533-a10f-37b6-a7f0-4d88274b7f80 | -13.92693 | -43.94584 | 2025-07-09 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5beda3f5-4e64-3695-a7f9-fb96533adff6 | -16.62648 | -42.21292 | 2025-07-09 03:57:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 753588f3-21ef-3183-a263-d667592dd917 | -18.64211 | -55.72406 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 38af843d-38e3-35ef-8a30-30a53c426440 | -20.42034 | -45.5801 | 2025-07-09 03:57:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 531cc05f-d944-39a2-bf47-e027d8517bcb | -17.20622 | -47.23318 | 2025-07-09 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 038438b2-d76a-3c5f-91cd-bf3c0ed259ce | -13.01069 | -46.29514 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5dec312d-c980-339b-b437-cec8dd4c3578 | -17.69112 | -46.73584 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a0edd119-ec25-3256-8a4d-306a84276807 | -17.33313 | -47.50093 | 2025-07-09 03:57:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25e6be77-8073-33ad-924c-2e047407f5f2 | -13.01409 | -46.75164 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f408597c-4363-300d-897f-20a488addc02 | -17.68971 | -46.74357 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3960eda0-0263-3b68-b53d-5883ac4db87a | -13.39828 | -47.90078 | 2025-07-09 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5cb1abf8-3957-33a8-8765-6988b329d99b | -19.37158 | -51.40585 | 2025-07-09 03:57:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef9e006e-ffd6-3084-9cc8-73cf1204962d | -13.70112 | -45.61174 | 2025-07-09 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 111fa09e-d617-3f69-8449-c1c8c2cbc3cc | -17.33586 | -47.50319 | 2025-07-09 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8f56d35-c6a3-3248-859a-f77ca3cd11be | -19.37232 | -51.40234 | 2025-07-09 03:57:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97243f54-f7e2-3cd3-ab14-958bae56f787 | -17.69661 | -46.74501 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4be191f-dfb9-3b5d-acbd-004e8a677d17 | -18.64734 | -55.73274 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 1b767fa7-590d-3c5a-97b0-fdfdcdea1654 | -13.93062 | -43.94651 | 2025-07-09 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7056461-c448-3268-bc57-d5a2c2789e05 | -12.97736 | -47.82611 | 2025-07-09 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45a14a89-5544-376c-a5e6-6e870b4ce7ca | -20.41808 | -43.55224 | 2025-07-09 03:57:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5b6d8860-a19e-3802-a4f6-54a7a97ee577 | -15.63955 | -46.43835 | 2025-07-09 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1208b854-4bbe-3c21-bd43-56f6c5522d7b | -15.7884 | -48.25625 | 2025-07-09 03:57:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 723b154b-89d0-36c8-82d5-7251c5b43d8c | -16.63043 | -42.20985 | 2025-07-09 03:57:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4f7dfb9f-3bf4-311b-a57f-863bbf0718ae | -15.7791 | -39.36329 | 2025-07-09 03:57:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5695385d-5bfa-30b5-b72a-1f42c36615ff | -16.67978 | -43.88435 | 2025-07-09 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44a48703-d3b8-309d-bf89-60f2905f0cb0 | -15.7763 | -39.35904 | 2025-07-09 03:57:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab4191dd-8d5a-3017-a746-5d5b258da609 | -14.86174 | -45.12701 | 2025-07-09 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 57d2e5f9-a6e8-38bf-9e67-4f6b7543c4e6 | -16.66156 | -46.03377 | 2025-07-09 03:57:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73ccd469-1f14-3a85-85fe-57d3f565e920 | -17.69651 | -46.75287 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e6d53c4-4fe8-3efb-a565-c40720566c80 | -19.39258 | -41.26898 | 2025-07-09 03:57:00 | NOAA-21 | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4023c75b-021c-3559-9dbe-2e7591c72008 | -17.26776 | -49.00905 | 2025-07-09 03:57:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a71ed87f-5f2a-39a2-8264-ca31659d42c2 | -18.64187 | -55.73092 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b703ee3f-5a38-3d3f-9672-37e3aa30a909 | -16.68036 | -43.88572 | 2025-07-09 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d49866e6-18b7-3038-967f-7492bb953471 | -13.01169 | -46.75508 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1a7d3c4-81b9-3bb3-97cb-c6f0776c5b00 | -17.71263 | -46.7278 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1db8ef58-8251-3334-a0aa-e3d42d63f1c2 | -13.0161 | -46.75615 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dff14837-822e-3bcc-8608-f2dce3fa145d | -17.09402 | -43.80265 | 2025-07-09 03:57:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea51cecd-fb74-3d54-a36c-eb54aa5b7f95 | -18.08718 | -54.2877 | 2025-07-09 03:57:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c639399a-3876-3f63-a272-4514fb92946d | -18.08832 | -54.28443 | 2025-07-09 03:57:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e49fdbe1-4f3b-3eec-b026-1873a72d9273 | -19.43795 | -44.34164 | 2025-07-09 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c170030-0c6e-3d8d-a29f-0d055b536d3e | -13.1041 | -46.88138 | 2025-07-09 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6ac1bd7-ec03-3bc1-8741-38e51b501ae4 | -15.76313 | -45.05506 | 2025-07-09 03:57:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a863d01-f173-3071-8e69-b72dcb8a14e0 | -20.93267 | -41.6838 | 2025-07-09 03:57:00 | NOAA-21 | SÃO JOSÉ DO CALÇADO | ESPÍRITO SANTO | Brasil | 3204807 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f7345a31-7fbb-3170-aac2-f5afae232bbe | -18.40552 | -44.19142 | 2025-07-09 03:57:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befcd4f6-1f05-319d-b45d-81749a78a280 | -14.20649 | -45.52662 | 2025-07-09 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3c03ee3-03ed-34ea-9fb6-3d56df81b55b | -18.64876 | -55.73275 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 4a2086f2-ee26-383e-8329-2eb4c8828c66 | -15.12507 | -44.01554 | 2025-07-09 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b19ab0c-9370-30fa-9ee0-d35b4eb54b55 | -17.69514 | -46.7528 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7987d87-5ffb-3469-a3f7-e306d54cee0a | -18.28305 | -42.59676 | 2025-07-09 03:57:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4ef5ffa-21d2-3308-8636-8d729dc5d6ae | -12.97154 | -47.83069 | 2025-07-09 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e34b5d12-a733-347d-afa1-c5c0f12ba6bd | -18.58095 | -43.9317 | 2025-07-09 03:57:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c722b9f2-9e07-363f-bd08-e4b78d505a05 | -18.6435 | -55.72402 | 2025-07-09 03:57:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d228e514-212f-328d-87f0-6a0b27c13a24 | -15.77575 | -39.36274 | 2025-07-09 03:57:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7bca8f61-f2f4-3ba2-ba51-72c5ea8cbad9 | -13.00048 | -46.30209 | 2025-07-09 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 569833ff-f989-357e-b572-7afb00698a28 | -13.64003 | -44.41882 | 2025-07-09 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0856ba4a-4d2a-35d2-a49c-52b64f3e0949 | -15.77375 | -39.36286 | 2025-07-09 03:57:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 163126b7-8106-3269-9c8b-874bc2b6795f | -17.6924 | -46.75211 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7f72dfd-c2ea-3f9d-9670-dea34bba9950 | -19.43835 | -44.34096 | 2025-07-09 03:57:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b961c62b-f490-323a-8932-0f5a4f89a049 | -17.69794 | -46.74504 | 2025-07-09 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 387c3270-f310-326b-b815-3942d9ca3506 | -14.85694 | -45.13137 | 2025-07-09 03:57:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2629224f-b280-3fe8-ac4f-cca8547ba3c9 | -16.62708 | -42.20922 | 2025-07-09 03:57:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bf511559-dab7-30f1-86e2-81997ce93fba | -17.7782 | -42.80532 | 2025-07-09 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5e05cf9-9408-3cef-bec9-5383914f2bb8 | -11.4393 | -45.1154 | 2025-07-09 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| e5f39344-c80c-3065-bbba-6549ef8a7dcc | -8.5028 | -43.2614 | 2025-07-09 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.3 |
| e14830b3-7163-327a-a755-1daae00ba885 | -6.1792 | -48.0494 | 2025-07-09 04:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9b494ce3-c68e-3a6c-9096-737e6a1a5a9f | -8.5214 | -43.2828 | 2025-07-09 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 178.2 |
| 15b693f7-e23b-3c30-8b9a-bcb201ff15e2 | -11.4201 | -45.1181 | 2025-07-09 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| f2fb7c7d-8bff-39f1-82f2-003a9ce72d6f | -8.5217 | -43.2593 | 2025-07-09 04:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| f80c1148-3574-3d65-a51b-22515f514ec2 | -11.4205 | -45.095 | 2025-07-09 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 3052c786-ae29-35ad-9525-83fc52227dc4 | -11.4584 | -45.1126 | 2025-07-09 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 7b3bccd1-dcc6-3f6c-941a-66b07fa03c87 | -11.4397 | -45.0923 | 2025-07-09 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 0e983b50-5240-3307-a5c4-63c258b8e94b | -8.5025 | -43.285 | 2025-07-09 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 242.4 |
| 7323571a-e9f0-3fb2-bf00-c328069f6693 | -20.40281 | -48.61098 | 2025-07-09 04:00:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e441268-00a4-352b-ac78-e5e0c03f13ef | -20.40371 | -48.60867 | 2025-07-09 04:00:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc56b53b-c405-31f1-a805-a21a5d1d88f0 | -19.09272 | -56.05072 | 2025-07-09 04:00:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d669b187-e796-3819-902e-66f5bb22d02c | -20.76523 | -46.76946 | 2025-07-09 04:00:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9bf96309-0728-3415-a548-5e5cd02c7196 | -22.67695 | -42.85363 | 2025-07-09 04:00:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b2aa41e-b80b-3701-94e3-a908354bdcda | -22.62904 | -47.9142 | 2025-07-09 04:00:00 | NOAA-21 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb0b72aa-b115-342f-8971-c4d225f2e3e7 | -21.04684 | -45.27463 | 2025-07-09 04:00:00 | NOAA-21 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 436fb5c5-c684-3523-ae5f-0e81c53cca5f | -23.33922 | -46.77211 | 2025-07-09 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
