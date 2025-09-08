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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57ff90ac-f3d2-32d6-8f55-8c3ae2f28642 | -16.4341 | -49.28595 | 2025-09-08 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45133007-c82b-3140-a75e-16db581291f5 | -15.76593 | -53.55699 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b198d8a9-a4c3-3e0b-ab70-a59ea0fdd9d8 | -18.95982 | -46.79818 | 2025-09-08 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 26caf889-c782-34ba-809b-1effb136f439 | -19.86609 | -44.3297 | 2025-09-08 04:04:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a36c3f6b-f5cc-354b-8d29-f101ef4eadfc | -16.908 | -45.82341 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 786c9597-f47f-3c4a-b674-b52e9cb47189 | -16.34384 | -52.93832 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ec8af6d-b6dc-34e3-88a9-eb7921776a1b | -17.25371 | -46.69665 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c5f615b-af84-34ad-8b48-59979bb19a75 | -22.06736 | -45.20169 | 2025-09-08 04:04:00 | NOAA-20 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 70ca0330-1238-32a4-a7a0-74b23ce8366b | -17.71636 | -44.48734 | 2025-09-08 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e93ad152-982e-3299-a36d-8093df5758b6 | -20.10618 | -47.32802 | 2025-09-08 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5211f6be-156f-3017-81e1-f09f52ef6887 | -16.89383 | -45.77518 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc93bc07-7a38-3ca1-9f7e-f6176459adf1 | -15.74927 | -53.53775 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dba5aff-c115-3f3f-a57a-c54fe2c0979c | -16.33727 | -52.94125 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 22cc6d2f-f5a0-3550-b27a-b0be68cba7a7 | -17.16604 | -44.43956 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30e6b50b-2184-38a4-bb89-b568d65bf37c | -15.82189 | -52.26681 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a0454e8-384c-32f7-8062-43978e3a840a | -15.66568 | -53.87547 | 2025-09-08 04:04:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3971b7b7-9f8c-3214-ade9-40f3460cb635 | -17.69942 | -43.52394 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abafb6e8-4ccd-3eca-9e1e-e7765db7a7a4 | -21.21714 | -44.33684 | 2025-09-08 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93ca94ef-d6d3-3dd4-84aa-9b00b4217fa7 | -16.5507 | -45.10897 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bd00b4e-488b-32a8-b189-9237637023be | -20.91381 | -42.82636 | 2025-09-08 04:04:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 383db1fb-ebf0-347d-b97e-2b6588ef7894 | -18.24576 | -46.63168 | 2025-09-08 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f188b05-b4ea-3f36-ae8c-6b45226d08e0 | -15.27117 | -52.39124 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04089049-0076-35c2-82b0-4f394f426b0d | -19.21045 | -43.74274 | 2025-09-08 04:04:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac8b0bd-9b92-36e9-aa68-e7c6a2b9fe7d | -16.63622 | -49.151 | 2025-09-08 04:04:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29a4097b-f983-3ddd-bfbd-0dbc961a038c | -16.93643 | -45.85494 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccded59f-4871-318b-a935-08a27f2d56c6 | -16.54011 | -45.107 | 2025-09-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6caf0bd-0e41-3073-adff-8d863633f61c | -18.73717 | -48.05805 | 2025-09-08 04:04:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 353b0b65-c215-37d1-a88f-cf0ee7e28288 | -16.91363 | -45.81399 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4269551-1fba-38b3-a508-ef215454c709 | -16.28229 | -45.68603 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ffed5ce-b480-3581-a09e-7d62995305b1 | -17.91644 | -42.61301 | 2025-09-08 04:04:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b501c986-5821-39ca-bc3d-5f3ded4d2d85 | -23.18803 | -47.25021 | 2025-09-08 04:04:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7a6a614e-f256-3c1f-9a04-0c1b216b1ad2 | -16.89442 | -45.79343 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32c01ad4-c7c8-3eab-9f6c-ee06bfca2a39 | -19.39758 | -44.51088 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c2a90f9-2e2e-3b5d-b26d-84720346def1 | -16.28593 | -45.68671 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b5802b6-da58-311d-b647-d605aa0340a9 | -18.11052 | -44.50348 | 2025-09-08 04:04:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df395b97-7872-38ee-a732-0e89feea4070 | -18.34292 | -51.95942 | 2025-09-08 04:04:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5dd8d3d-81b7-3a30-ab88-35e64982de5b | -21.47961 | -46.38341 | 2025-09-08 04:04:00 | NOAA-20 | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 983bf687-6608-3126-8660-f747d358d968 | -18.3579 | -43.92317 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 25480c96-79c6-3f89-ae32-bbeddd0ea155 | -17.15648 | -44.43358 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0a5424f4-9572-3c63-b0d1-105458bab4fd | -19.53209 | -47.88787 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d5c352b-199b-32d3-9db6-3176b74d8707 | -18.03697 | -44.33168 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b74706c4-4c52-3385-97af-6a2672d4960f | -18.0305 | -47.11454 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| defc029c-27a7-3482-a606-129f94868476 | -19.39822 | -44.50705 | 2025-09-08 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56d186db-e6db-3a48-87e4-64c17d2a200a | -16.91176 | -45.84568 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 828ebf52-a5ee-3940-b95d-6c561fb04cb3 | -19.82685 | -47.27908 | 2025-09-08 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2efe2fdb-93e5-36c7-8073-e8f5a126eb0c | -15.83245 | -52.29927 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80dce3d6-c1ce-36f9-97e3-90eca32f050f | -16.33901 | -52.93303 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fbce69c1-7416-39b4-973f-10e0dc71e5ea | -18.33779 | -51.95818 | 2025-09-08 04:04:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed4152aa-0ed7-3ff1-bf01-1ab39021a6c9 | -20.469 | -47.24219 | 2025-09-08 04:04:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a6baca3-5622-3b9e-8dea-7bab183ebaa1 | -16.44299 | -49.28834 | 2025-09-08 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 967e39b7-1e16-3226-a48f-d8c5326e5098 | -15.75338 | -53.5479 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fd3f7ad-a9d9-3144-9b8a-6ca0ca8e86da | -19.00706 | -46.90045 | 2025-09-08 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bccf627e-064e-3c2c-8551-fb011eb8d5b7 | -16.28887 | -49.54935 | 2025-09-08 04:04:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8b90dc0-03dc-373d-91af-c756c439950f | -15.1257 | -52.34333 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f7d8eb7-b210-3983-997d-7360bb2b3cb7 | -18.02365 | -47.1086 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5e8152ac-aacd-35f3-8b98-e1a3d9ee3ff4 | -15.23444 | -52.35522 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 144723d1-aad7-37ba-8dcf-f0ed44bf3e8e | -16.28305 | -45.68162 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 926b4e17-0c17-345f-8044-50104a2b5671 | -17.66006 | -46.68718 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22943fdd-a922-335b-bee3-d753baf571d5 | -15.26088 | -52.3843 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 596e8b74-93ae-3a3f-8c33-756187344956 | -15.68745 | -53.56422 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da40dfdf-a4bc-3e90-8eba-1af39efc1b57 | -17.58593 | -44.53226 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee9bb6b0-3c20-3771-aa1c-8f12fbf3c3dd | -17.16486 | -49.02454 | 2025-09-08 04:04:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a38dfb85-0062-3787-a607-0b03be1865fe | -16.8988 | -45.78972 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7779ffa9-e6ee-3830-a815-a23807feb0af | -18.02926 | -47.09957 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe07f064-a69b-30af-aeb4-c879d4385586 | -19.75996 | -48.01102 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48070178-9158-3e8e-88c3-00d124238593 | -17.8374 | -44.24865 | 2025-09-08 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 482cdefd-4007-365a-bfef-cf01d0a76e53 | -17.14859 | -44.44071 | 2025-09-08 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11648f69-2a9b-3b53-94b7-6aaa0eba1c99 | -16.97452 | -45.83028 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d623abd4-b5ca-3482-ab29-598633248239 | -17.24991 | -46.69597 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eccc9b2f-4aaf-3761-9b40-8928c6a9d842 | -16.90166 | -45.79488 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1eec1e78-23e0-365a-8210-8c50e3d3be21 | -18.0245 | -47.10398 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 513bace9-977c-315d-8a16-f30bc4997a94 | -17.56271 | -44.5255 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c187fe3c-1b27-390d-8a6f-63d2af9e5155 | -16.29367 | -45.68588 | 2025-09-08 04:04:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7ba6d10-8f62-3831-947b-9410f77cdf7d | -18.35729 | -43.92688 | 2025-09-08 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2207371a-d12c-3a4b-af00-7ee818c7e46f | -15.75582 | -53.54591 | 2025-09-08 04:04:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78a2e19e-e6b0-3266-ad72-6afa0d802c92 | -18.0275 | -47.10923 | 2025-09-08 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1b641e9c-e40c-3e12-947e-30e31d7fb8fe | -20.90848 | -44.25013 | 2025-09-08 04:04:00 | NOAA-20 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c7e67671-49a5-3906-9f8d-2a6d3137427f | -15.26564 | -52.38962 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f38fb05b-7b72-33ec-9bac-80f55e8d8ebd | -16.90813 | -45.84496 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2a8c7ac-85e1-32cc-af18-085ef59d694f | -19.02817 | -43.56671 | 2025-09-08 04:04:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb3c3fe-b9f4-372d-b732-fd20bc7eb3f0 | -15.11991 | -52.34301 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46a3a2a0-f2fa-311a-8e4f-4e158cdebd39 | -22.68613 | -46.92169 | 2025-09-08 04:04:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c8b68145-eca6-31d5-acba-ce1e0b9cf44f | -16.34069 | -52.92512 | 2025-09-08 04:04:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8717e10d-9113-33c9-a4f5-b3d333be4406 | -15.83864 | -52.26931 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b5b821b-991e-3670-a223-75cf4dc4d866 | -17.62024 | -44.83362 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24ed72a8-4d89-391b-ba99-ad0667400d6c | -17.53465 | -43.74139 | 2025-09-08 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43a10a94-316c-3b86-b0c5-ce50da4d8641 | -17.44492 | -50.22001 | 2025-09-08 04:04:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e732eb98-986a-332a-afa9-443609e055c7 | -16.16119 | -47.91533 | 2025-09-08 04:04:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cde9fa0-b75d-3b96-91dd-a4dd1fe8e35c | -20.92498 | -45.2685 | 2025-09-08 04:04:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0ab03640-1577-3432-9588-0d93dfbbdee9 | -19.52427 | -47.88626 | 2025-09-08 04:04:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a0db471-1224-3b43-a73e-b45cc872710c | -23.18723 | -47.25473 | 2025-09-08 04:04:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e3f702a-2ed4-394a-b095-f623c0fbbcd9 | -17.31716 | -45.95427 | 2025-09-08 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af4a6d9b-fabf-3411-a7a9-f121fb31d122 | -17.23478 | -46.693 | 2025-09-08 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48e00212-df2a-3fbb-baf5-fe5d02f09362 | -17.88874 | -39.83153 | 2025-09-08 04:04:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7c9c215a-7ced-3a98-8af2-c2e77a72347b | -18.23919 | -46.62537 | 2025-09-08 04:04:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 537e198c-4604-3949-8af5-584e8ab20caf | -16.91086 | -45.82857 | 2025-09-08 04:04:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ea5d4f3c-4985-3eb2-9a8a-b944bd26d5cf | -18.03761 | -44.32783 | 2025-09-08 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 596457ac-f267-3e6e-85d4-2a2b76049de3 | -17.59144 | -44.54136 | 2025-09-08 04:04:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c455d8d7-c52a-3eee-ba76-7a5f04a95448 | -15.23677 | -52.35954 | 2025-09-08 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2d6bc37-5f1c-3eef-9b7d-5b26a88ce233 | -18.14453 | -43.39767 | 2025-09-08 04:04:00 | NOAA-20 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README48.md)
