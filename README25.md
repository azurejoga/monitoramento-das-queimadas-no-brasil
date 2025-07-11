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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0754ec7-57d1-3c31-87ac-fe420c1ccc7e | -13.01187 | -47.82592 | 2025-07-11 12:12:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6bebc42c-66e7-3bb8-80b1-d2bc3525155c | -13.21844 | -44.98647 | 2025-07-11 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0be57614-6f66-3e44-a14d-0f080c139fe3 | -18.43049 | -44.71521 | 2025-07-11 12:12:00 | TERRA_M-T | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aaf830fa-2a9c-3f68-bb63-5a9bdae38327 | -13.99223 | -49.34108 | 2025-07-11 12:12:00 | TERRA_M-T | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6a8a3255-012e-3dfd-9944-ee29e79e8026 | -12.87618 | -49.18133 | 2025-07-11 12:12:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a9bb6c6f-8b7c-3035-b7bb-346e3ccd9689 | -16.03632 | -43.8419 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5d6d2b1c-e22c-3497-b045-c33924ef1369 | -14.26301 | -47.03199 | 2025-07-11 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f7e42f6-a94e-387a-9c95-f2b0a18966d5 | -12.51057 | -51.28883 | 2025-07-11 12:12:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e2f32653-c33b-3d93-aada-38435ed863fd | -16.63921 | -44.34802 | 2025-07-11 12:12:00 | TERRA_M-T | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bc39be0a-6663-36ec-8414-7fb272753cd5 | -13.86455 | -45.8755 | 2025-07-11 12:12:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cc28be48-bc07-3c57-aeb2-1dc72f6edbb0 | -13.17774 | -47.29193 | 2025-07-11 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1eee4bbc-50a6-3b16-99e3-e319197ad37d | -12.99836 | -44.85882 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4e5d9c05-71cf-33a5-b76b-3444f5fb3405 | -13.00455 | -46.31681 | 2025-07-11 12:12:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7136138b-06d9-372f-a0a4-73fc5475fda6 | -18.26841 | -51.12695 | 2025-07-11 12:12:00 | TERRA_M-T | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 846f0902-37b8-3ce6-9c26-bf6f32548ef5 | -12.88709 | -49.18313 | 2025-07-11 12:12:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 692763da-59a9-39e8-813a-ace50e53d9d9 | -14.25371 | -47.03052 | 2025-07-11 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d305d2f4-2b31-3219-88c4-ed42b179c89f | -19.37902 | -51.39732 | 2025-07-11 12:12:00 | TERRA_M-T | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6ea4c40a-b823-3651-9d00-14659153186d | -12.98954 | -44.85752 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0a741363-91fd-3800-8792-3b1fd0ed836f | -13.46079 | -46.71667 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c4a96083-d1d2-38b2-b5b7-ab4a172a0949 | -17.85638 | -44.73225 | 2025-07-11 12:12:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac81ae87-cf15-3220-9151-6e58fb889525 | -12.98694 | -44.87548 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f22dbdf6-76d0-31a3-9e27-b1854f00036f | -14.61833 | -46.81633 | 2025-07-11 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d9ca7482-66c0-3b1d-b5ce-1a3b60ca197c | -13.14292 | -47.2999 | 2025-07-11 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 19b21313-e0ab-3880-807d-e17d24265be3 | -13.20345 | -47.25201 | 2025-07-11 12:12:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0990c0cf-f1e9-31a2-9cc0-ebe58d240abc | -16.04537 | -43.84322 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8cfee9d4-6212-3a2f-9ec7-83c5fcd1dbef | -12.98824 | -44.8665 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 98db0a4e-9b00-359c-a35a-36492d168bfc | -19.74248 | -47.44224 | 2025-07-11 12:12:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d3ae9f51-121c-3279-a002-55799f9fa605 | -13.69266 | -45.40882 | 2025-07-11 12:12:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7e0c97d-883b-31c4-a22d-9520dc9b948d | -13.4623 | -46.70673 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d47107bb-3f7a-3ebb-9ef2-26af67803a01 | -12.99575 | -44.87678 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6f0bc00d-ccba-3b00-b529-2de93bfdf2e4 | -19.74394 | -47.43258 | 2025-07-11 12:12:00 | TERRA_M-T | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ebe5fbf-1694-3b9b-86c4-1624eb9d22df | -14.26455 | -47.02187 | 2025-07-11 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa2049b4-3d3b-3ee3-be65-6617a97eaced | -13.86593 | -45.86618 | 2025-07-11 12:12:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1144d19-ba57-346e-8321-53bfa1dddaa7 | -12.51161 | -51.27454 | 2025-07-11 12:12:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d0aab4b5-101b-3708-8b73-f2def5ed8efb | -13.00197 | -47.82446 | 2025-07-11 12:12:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 796cb874-5dfc-34cb-898b-e9680add475d | -12.34391 | -49.97446 | 2025-07-11 12:12:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 98fbed7a-5216-3d69-843c-8a99a2f2ced0 | -13.01013 | -45.22586 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f00b05a-0b14-3862-8f08-89fc8122e3e5 | -12.99398 | -46.32505 | 2025-07-11 12:12:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 95b83285-d96c-39c2-a325-382c22f46b43 | -12.99253 | -46.33473 | 2025-07-11 12:12:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f254456c-8d31-3223-8e18-bd8f6607f148 | -12.99706 | -44.8678 | 2025-07-11 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| dd3af1e7-9bb6-3af5-b4d5-b892c2711029 | -9.9148 | -47.8282 | 2025-07-11 12:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 402542c4-f234-3246-95e9-762a8a90f81d | -6.1421 | -45.9125 | 2025-07-11 12:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 87399fae-2d95-399d-9885-8e0fbf4fa7f2 | -9.9148 | -47.8282 | 2025-07-11 12:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 47284917-6701-3fd9-9e78-b2a2a452c315 | -6.1421 | -45.9125 | 2025-07-11 12:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 76a34563-26e8-3002-b832-61cee1d1ca94 | -6.1421 | -45.9125 | 2025-07-11 12:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 035bfdad-79aa-398d-a2ae-68514e619d65 | -9.9148 | -47.8282 | 2025-07-11 12:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 26d21c2f-cfe9-318e-a440-7d983ca5ad3f | -9.9148 | -47.8282 | 2025-07-11 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 73134783-f7c7-3207-9955-c2bd8333dcbf | -6.1421 | -45.9125 | 2025-07-11 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 129d5a90-bcd1-3d8c-beae-03c006cf64d6 | -9.9148 | -47.8282 | 2025-07-11 13:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 3cc5220b-0bac-3da0-8aba-8469eed6c16c | -7.6396 | -46.0131 | 2025-07-11 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 337.7 |
| 593dd490-6aa9-3f90-807d-2ca1d634ede9 | -6.1421 | -45.9125 | 2025-07-11 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 05d7798f-852b-3c50-8af1-bdb3a98da78b | -6.4498 | -45.0314 | 2025-07-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| be91871f-a234-3800-8907-a316f4eb9cd4 | -7.6396 | -46.0131 | 2025-07-11 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 1ef7fe0c-00f7-3f65-8bb4-7e59fcddacfd | -9.9148 | -47.8282 | 2025-07-11 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 211.0 |
| 9910ebf8-be41-3058-830b-e0c87299c2eb | -6.1421 | -45.9125 | 2025-07-11 13:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1f5e6404-f63c-3f81-ae39-830082970708 | -9.9148 | -47.8282 | 2025-07-11 13:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 65c14bb9-e3f8-36b6-928e-336b0598088a | -7.6396 | -46.0131 | 2025-07-11 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 6dca49aa-2cfe-3c19-a21e-706b69a55a72 | -6.1421 | -45.9125 | 2025-07-11 13:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 7b214e41-c9fb-3a39-a463-16e07e29acd9 | -12.4121 | -45.3628 | 2025-07-11 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 0159ccba-a821-3a40-a71e-e4898682fdbb | -6.1421 | -45.9125 | 2025-07-11 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 228.6 |
| ac8a456c-954d-3f8f-9888-b2d2117973c2 | -12.4121 | -45.3628 | 2025-07-11 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e8134c3e-81ac-3ee0-89c6-7aafd1c432b7 | -9.9148 | -47.8282 | 2025-07-11 13:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 253.9 |
| ee2a7ec1-54de-3a45-808f-cc581c1099f5 | -7.6396 | -46.0131 | 2025-07-11 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 089420df-1966-3feb-b298-80416865c65e | -6.4498 | -45.0314 | 2025-07-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| c027aebe-11ab-3985-8908-15c0577e9c0b | -6.8485 | -42.7979 | 2025-07-11 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| c97541f0-d5b6-3e20-9d79-6db8f671e62f | -7.6396 | -46.0131 | 2025-07-11 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 0998dc12-0141-38aa-9db1-6e3c84a08a70 | -12.4121 | -45.3628 | 2025-07-11 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 3fae118a-ba67-3fc3-81bb-8b3c7067bafd | -6.118 | -42.5323 | 2025-07-11 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 9cb43b3c-6991-37d9-a7af-91d5dd17b878 | -9.9148 | -47.8282 | 2025-07-11 13:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 205.3 |
| 43af8bfd-bfb7-3fbc-89d9-6cb7e245b95a | -6.1421 | -45.9125 | 2025-07-11 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 39dfcf78-240b-310f-8498-22977fd155ab | -6.4498 | -45.0314 | 2025-07-11 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| acc11385-3460-3da8-9481-cce3cc2f7adb | -9.9337 | -47.8261 | 2025-07-11 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 395a824a-e294-3ddd-bd63-de511113e4e3 | -6.8485 | -42.7979 | 2025-07-11 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 0b0107b5-3fbc-3765-8ff4-7fd32cf2e832 | -6.4498 | -45.0314 | 2025-07-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 52f3be22-f0d9-331f-98a7-24bce02ffd9d | -7.6396 | -46.0131 | 2025-07-11 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| e42700a2-ab5b-3ce6-b1d4-3ec0453d800f | -12.4121 | -45.3628 | 2025-07-11 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 52f91317-fb23-3aee-b53c-34cf1aed6e92 | -6.1421 | -45.9125 | 2025-07-11 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 6c42885a-426a-3d47-8a00-0e1853ad4bc4 | -6.1419 | -45.9349 | 2025-07-11 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 5c8ac0f4-b8e1-36c5-857a-a417066b0057 | -9.9148 | -47.8282 | 2025-07-11 13:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| fb8ffb15-0f2d-3fd0-82ee-f287d839a90d | -11.157 | -49.6938 | 2025-07-11 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| be687b73-8944-310f-b7a0-c4805d1fe18c | -6.1419 | -45.9349 | 2025-07-11 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 9ef3a6c8-299e-377f-844b-ed3fcb861ed8 | -6.4498 | -45.0314 | 2025-07-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| f42a0a9e-8b53-3a7d-a4ce-20fa578103bc | -6.8485 | -42.7979 | 2025-07-11 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 5f6b7b53-9ef5-33f5-98ac-389eafccc544 | -6.5824 | -44.884 | 2025-07-11 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| fcc52df0-eb39-3a6d-aa86-c3925e92ac39 | -6.1421 | -45.9125 | 2025-07-11 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 17c2295f-22fc-3621-a126-b4884838ac5a | -9.9148 | -47.8282 | 2025-07-11 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 206.4 |
| c5c0ad6c-56d8-3eec-b4f8-27216e254080 | -12.4121 | -45.3628 | 2025-07-11 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 157ef180-21cf-38de-812c-6b319bba4bb6 | -14.4252 | -58.7325 | 2025-07-11 14:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 78f489fc-9d3a-3d88-a541-b534729605ff | -7.6396 | -46.0131 | 2025-07-11 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a1ba62b9-cecc-32e1-89fc-b62f34752b84 | -6.1419 | -45.9349 | 2025-07-11 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4ba216c7-1aaa-3fd2-af42-6e4b7f1af36c | -14.4252 | -58.7325 | 2025-07-11 14:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| eb9fdc09-5006-38ca-bbd7-05513a26a5aa | -7.6396 | -46.0131 | 2025-07-11 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c3c80efa-6e49-3e40-86f4-f690c59be6d9 | -9.9148 | -47.8282 | 2025-07-11 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| d7e7aca4-d548-30c5-af40-2623f905de01 | -7.6553 | -44.6506 | 2025-07-11 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b7a567ec-9211-35c9-a7a3-47fe0d06d1d6 | -6.1421 | -45.9125 | 2025-07-11 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 446b2596-dce3-3c4f-b5ff-5f0771588beb | -6.1234 | -45.9139 | 2025-07-11 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7de520ed-495c-3bb3-826b-4ab0603d838d | -12.4121 | -45.3628 | 2025-07-11 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3303430f-e0eb-34ee-a36d-32aa0bc090aa | -6.8485 | -42.7979 | 2025-07-11 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| dddd29b1-944b-3971-9a2a-e47cb56d6e69 | -6.713 | -44.9415 | 2025-07-11 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 178615e9-cbd9-3292-8679-7cdffec9d3c6 | -6.4498 | -45.0314 | 2025-07-11 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 497.4 |


[Clique aqui para ver as próximas entradas](README26.md)
