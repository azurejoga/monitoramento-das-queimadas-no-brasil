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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 183a8171-f7ef-33b1-916b-4c4b0ec7f5e2 | -8.6327 | -46.3208 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 640c7a6d-7f88-3a37-8e01-553f6c74522d | -13.7738 | -45.7429 | 2025-10-06 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f62a44b7-5193-38e7-9bba-7eb2162711e3 | -14.4099 | -45.9335 | 2025-10-06 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 16db367e-a1ed-3322-9571-735b2627807b | -18.0011 | -57.5238 | 2025-10-06 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 57e9e9cc-b77c-3278-9062-f0e0b2fa6799 | -7.6804 | -42.5728 | 2025-10-06 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 46631310-1e04-319d-8393-d058892053b9 | -8.6139 | -46.3227 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| c8951850-b902-334d-a240-c18b562aa7d5 | -15.5901 | -47.259 | 2025-10-06 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 190e81b9-8cf8-31d9-93cf-103dd77ed377 | -17.9807 | -57.5674 | 2025-10-06 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| e3859aef-3cd0-3878-b9dd-73c78f45dd9e | -7.4669 | -43.0674 | 2025-10-06 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 64b46d6d-6c24-390d-b982-9e2e4ba1a2b4 | -7.7206 | -42.3784 | 2025-10-06 13:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 04cd5c2e-cb79-3d28-8341-7e47108e7f96 | -14.863 | -51.5019 | 2025-10-06 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 9691b98c-acdd-3bfb-a100-e859de75a67b | -15.3541 | -47.3235 | 2025-10-06 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c3aea3ea-5369-35a7-b774-85ea6f63f345 | -14.5438 | -46.9633 | 2025-10-06 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 7c451934-106b-3faf-aeb5-43893d3f0d36 | -21.3855 | -45.0425 | 2025-10-06 13:10:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.3 |
| cc94afd4-14a5-3ab4-bf21-d8e2e18f02e1 | -16.0038 | -50.8365 | 2025-10-06 13:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ac31fafe-d91a-369d-b950-a5d3f8944d10 | -14.6893 | -48.4021 | 2025-10-06 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a4c40d37-60e6-3cfa-b4f5-ad76baf048e0 | -8.1879 | -44.2283 | 2025-10-06 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 33a876ef-601f-3420-b24f-47698d86ae4c | -8.0866 | -44.791 | 2025-10-06 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| a0371d3c-943d-3026-a52d-dad34b7ffa38 | -14.5623 | -47.0056 | 2025-10-06 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 148.1 |
| d781c0bb-a8c6-3004-a491-5b857386a1b6 | -7.4672 | -43.0438 | 2025-10-06 13:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 40492784-e623-3745-8f76-c0b057a335f1 | -21.1171 | -49.9537 | 2025-10-06 13:10:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.1 |
| 1ae30909-17ef-311a-8a32-3cb2483a64ee | -12.8954 | -47.2909 | 2025-10-06 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 91a6e1dd-b5b8-3edd-b2fc-5da0bb725aec | -14.2754 | -45.8647 | 2025-10-06 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f703f91d-7c89-35b5-93e1-d107433673d5 | -14.6135 | -52.495 | 2025-10-06 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 69348a1e-ccae-368f-9334-022b60d32a3a | -9.6801 | -48.4232 | 2025-10-06 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7387c6f7-dcd6-34c8-9bf2-ba0549279c1e | -13.3044 | -48.0575 | 2025-10-06 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 6918e765-562b-3b01-9ad5-180260ff031d | -13.3237 | -48.0547 | 2025-10-06 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 69abf223-59de-30cb-8b1e-5e381df6deb1 | -8.6141 | -46.3003 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 3119bb9e-372b-37d3-961f-965049dfb274 | -8.633 | -46.2984 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 356.0 |
| f39804b3-8b1d-30b4-8d7c-5d85fefb15a1 | -17.8417 | -57.6254 | 2025-10-06 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.0 |
| 9b3b2f2f-5cf9-3df5-89de-940be4464464 | -21.4055 | -45.0614 | 2025-10-06 13:10:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.1 |
| 37c9c564-148a-3f62-94a2-884e24ff735c | -14.882 | -51.5207 | 2025-10-06 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 4e283032-3a41-3a5c-9904-1fdfef4c22c3 | -15.2351 | -49.2914 | 2025-10-06 13:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 1823aba6-5173-356b-a6d3-770548d1a021 | -14.6897 | -48.3797 | 2025-10-06 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| eb9233b3-9612-355e-b8a4-377e952425f8 | -17.9741 | -44.4077 | 2025-10-06 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4ee81a0c-162e-3ad1-8d45-ab9a01d8739c | -18.2869 | -45.4109 | 2025-10-06 13:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 998fb0a6-f478-3dc1-ad73-4dc04e939ee0 | -9.6614 | -45.6667 | 2025-10-06 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 8743b7fb-9563-3563-9e15-b25e0b900ca9 | -13.7738 | -45.7429 | 2025-10-06 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e22572c8-e1a4-34ad-806e-490c7726cacd | -18.018 | -44.9965 | 2025-10-06 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2bcca975-b92a-3637-8f89-6321d4ef3955 | -8.5196 | -46.3323 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e49f0e2b-ce31-31a7-97d8-48866682ff93 | -13.2515 | -47.7979 | 2025-10-06 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 86e9a6b6-bdac-3eec-8ee1-7086072a74b5 | -14.5433 | -46.9861 | 2025-10-06 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 5565c2be-858e-39aa-9fea-406afce16b31 | -12.9812 | -46.8051 | 2025-10-06 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 5dcdf9cb-8318-33b0-b958-fab56c95ae8f | -8.1687 | -44.2534 | 2025-10-06 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 37cea753-4cba-3bf8-acb7-c37377cd7c5f | -14.5504 | -46.6433 | 2025-10-06 13:10:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d920e387-9434-3c47-bf14-e176f09e5859 | -12.3346 | -45.3977 | 2025-10-06 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 152e85b4-b4a6-3e4d-9055-35fc14461e1f | -20.1001 | -44.1921 | 2025-10-06 13:10:00 | GOES-19 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.4 |
| 8c3a087c-11dd-32aa-838a-f80528ad2ee4 | -9.9776 | -48.7622 | 2025-10-06 13:10:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| aa318a26-9e39-3f5c-828c-953a26f3a2c0 | -9.6804 | -48.4014 | 2025-10-06 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 389d1098-69c7-3e48-b453-2eb4da96d3a9 | -17.7045 | -46.2927 | 2025-10-06 13:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 4b6290db-5942-3a74-bad0-7a71f98767a2 | -8.8803 | -47.6061 | 2025-10-06 13:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 595b1746-00dd-3fa2-9285-4fcf3c6aa6ff | -10.4054 | -45.3931 | 2025-10-06 13:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| da19eedf-8cb3-3ba1-a57d-15b1b5873c77 | -8.6144 | -46.2778 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 239.1 |
| d8adac9b-905d-3338-ac7e-a89c66a2d810 | -15.2347 | -49.3136 | 2025-10-06 13:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e97ee619-f78f-3d06-9ba1-bf0f435a5505 | -11.8033 | -45.0856 | 2025-10-06 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 473c12a4-0a28-3a84-95a7-6df50e32a81d | -21.4063 | -45.0368 | 2025-10-06 13:10:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 142.1 |
| c59d50d4-ec97-3e09-b3e2-b73ed1723635 | -10.4652 | -50.4334 | 2025-10-06 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 57289239-8b9a-3e87-98f3-36876345fe24 | -8.5193 | -46.3547 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| fbbb3a41-8f21-33f0-adcd-a8287d60fe94 | -7.7935 | -42.5845 | 2025-10-06 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 401a5595-9ab5-3a11-b8e6-7158e5fd0c24 | -13.2586 | -48.4635 | 2025-10-06 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 89dc0445-4123-3a43-99ff-af4f33b02ad6 | -17.9803 | -57.588 | 2025-10-06 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| bffe44b5-3070-3504-90b7-0e24cfc537ec | -18.0008 | -57.5444 | 2025-10-06 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 7dff8489-80ff-3264-b771-58b1a2f6c1d2 | -7.6801 | -42.5966 | 2025-10-06 13:10:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 3c0366cf-a9ee-35d7-9730-a53e81647b7c | -7.7014 | -42.4043 | 2025-10-06 13:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 7a180456-1853-3b3d-975c-806c1e58f26b | -12.9844 | -51.0433 | 2025-10-06 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 859c5ac4-34f0-3e2d-8b23-e8a821175423 | -9.9779 | -48.7405 | 2025-10-06 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 0ca1f70c-8b3f-300d-ac7b-0fcd855d0808 | -14.8626 | -51.5234 | 2025-10-06 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 275.8 |
| 4e14c3d6-43d3-3115-88d5-722d0cf6d1fd | -10.3643 | -48.1519 | 2025-10-06 13:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| fbec6d0b-9eda-332f-b876-081e8d22ce98 | -15.3546 | -47.3007 | 2025-10-06 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0bfcfcc4-e395-3077-9277-17472252a26a | -9.4863 | -46.0039 | 2025-10-06 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| d3875f3a-1b29-38b2-8cc3-8e65ea4ee545 | -15.3788 | -47.9972 | 2025-10-06 13:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c37d3258-2f9f-3a71-b652-e823ae2ce223 | -7.7203 | -42.4023 | 2025-10-06 13:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| e0a87823-3750-3584-98fe-b4ef946dfa8f | -10.158 | -45.4244 | 2025-10-06 13:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| a2e7167e-9a97-30c0-b71b-7c222e197a93 | -12.5929 | -48.1144 | 2025-10-06 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 45f7d13f-3f7a-32c0-838f-784365337ddd | -11.6554 | -47.0166 | 2025-10-06 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9e79c87d-27fd-3fbe-a988-50bdc591e54c | -11.655 | -47.039 | 2025-10-06 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 68f1c700-76ef-375b-a385-6bef77cf7cfd | -17.842 | -57.6048 | 2025-10-06 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| a6f1cb33-9bf6-3d84-9afe-4210cc21c551 | -14.5628 | -46.9828 | 2025-10-06 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 403.7 |
| 295c91c1-564a-36b3-902e-551f40616444 | -8.5198 | -46.3098 | 2025-10-06 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b0ae79b5-e1f6-3590-8dee-bffeefbdde42 | -10.465 | -50.4547 | 2025-10-06 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 48dd093b-477a-38b5-b312-28f43be95a8c | -9.6801 | -48.4232 | 2025-10-06 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| eb7a030f-c767-39de-893b-f7b78d592caf | -17.8417 | -57.6254 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| c74277f9-d4b5-3286-bb7c-0f394c7b3d55 | -8.5196 | -46.3323 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 5f5774e8-471e-34b8-8dda-60963d9287c0 | -10.4054 | -45.3931 | 2025-10-06 13:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3e776e98-6332-34a4-98d8-a79d2aaf2b49 | -15.5901 | -47.259 | 2025-10-06 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| bb3acd72-5910-3c57-8499-b9baab0620b7 | -12.5541 | -48.1419 | 2025-10-06 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| b28c7ff6-2c00-362b-95f6-bb4f916812c5 | -11.1181 | -47.243 | 2025-10-06 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| dfee689a-41ba-3cfc-9a56-7ba8e3038e55 | -17.9803 | -57.588 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 83317e96-4dfc-3259-984e-c948a7245a3f | -17.9813 | -57.5262 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 3a59b3a3-a120-3115-bf5c-a15f7b13c675 | -12.4468 | -45.5646 | 2025-10-06 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f6859dce-1471-3658-88dc-abae47af47bc | -14.5438 | -46.9633 | 2025-10-06 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 3f7c8e96-d75d-345c-a060-e13837cae966 | -8.6141 | -46.3003 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 3730437d-c969-3f58-ba79-ec0dd6c8d36f | -8.5193 | -46.3547 | 2025-10-06 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 267.0 |
| 8d8e4a48-6674-367c-9bfd-5503c265e561 | -7.7014 | -42.4043 | 2025-10-06 13:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 67fdc9db-92bc-3593-820f-4c93d0d51dd1 | -9.4863 | -46.0039 | 2025-10-06 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 72c5af4d-2477-3d68-ad12-3dc399e80df7 | -17.98 | -57.6086 | 2025-10-06 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 6f57089d-a3bd-391c-91c7-b489848f3e63 | -12.1458 | -50.9523 | 2025-10-06 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 4fab977a-2c56-301a-835d-197fa71d9a54 | -12.4464 | -45.5876 | 2025-10-06 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| ac0346ff-7562-3d3d-addc-7aa1faa2975d | -10.9684 | -47.0834 | 2025-10-06 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 78ea87d5-b5cc-33a7-a46d-bf04b8f45d06 | -7.6804 | -42.5728 | 2025-10-06 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |


[Clique aqui para ver as próximas entradas](README88.md)
