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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04030f69-eb98-3760-a930-e3a64d57124a | -19.6399 | -44.144501 | 2024-09-26 00:53:00 | METOP-B | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3973ae29-acc1-3762-8d31-93c6bfc2a10a | -19.630199 | -44.147301 | 2024-09-26 00:53:00 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f24d475f-48c8-351b-ac28-06c728416d02 | -19.623899 | -44.163101 | 2024-09-26 00:53:00 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 97f02ddd-1ece-3182-bce5-8ad3dfe890e5 | -20.030701 | -45.655201 | 2024-09-26 00:53:00 | METOP-B | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25e64196-b377-3627-ba04-4f55d8504516 | -19.972799 | -45.547001 | 2024-09-26 00:53:00 | METOP-B | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7c2e0a24-129c-39a2-859b-be4ca412b590 | -21.264999 | -50.985199 | 2024-09-26 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edf66130-adee-39e7-b8f6-3bcc17f82c52 | -21.2665 | -50.992599 | 2024-09-26 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad52f04f-0206-3ce9-b5fb-d0815898cd5e | -21.268101 | -51.0 | 2024-09-26 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0ee1089-2af7-3a14-83f5-2d79f2502dd9 | -20.1507 | -46.571602 | 2024-09-26 00:53:01 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe4055a1-0d8e-30c2-8cfb-30687ece7bf0 | -19.1768 | -42.5741 | 2024-09-26 00:53:01 | METOP-B | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f8ce084-98ec-389e-94ce-2a369d0bacb2 | -19.186501 | -42.571201 | 2024-09-26 00:53:01 | METOP-B | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9078c86-d432-3f2f-a726-74393abc9c4d | -19.1724 | -42.557499 | 2024-09-26 00:53:01 | METOP-B | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f313aa34-59b4-3ad2-90f4-daeebaada6bc | -19.1313 | -42.4426 | 2024-09-26 00:53:01 | METOP-B | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cda2a4ba-db2c-3db5-8f1f-8dbe4a0bf8b2 | -19.135799 | -42.459499 | 2024-09-26 00:53:01 | METOP-B | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6787ead1-fb11-3b73-a4be-3c316bee749e | -19.140301 | -42.476398 | 2024-09-26 00:53:01 | METOP-B | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf0256ef-59f2-34a3-8ab2-654ec8e5eec1 | -20.918301 | -49.669601 | 2024-09-26 00:53:01 | METOP-B | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 621fcfff-e109-3770-96ab-a08e5c80bc99 | -20.919901 | -49.676998 | 2024-09-26 00:53:01 | METOP-B | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b302908-05c9-32ec-a49c-8eac99735869 | -20.908501 | -49.6721 | 2024-09-26 00:53:01 | METOP-B | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 58913d70-e515-3d5c-a556-1f0d54fc0e60 | -19.5212 | -44.492802 | 2024-09-26 00:53:03 | METOP-B | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 235f1eac-a861-3657-95cf-267f45e95e9f | -19.511499 | -44.495602 | 2024-09-26 00:53:03 | METOP-B | CACHOEIRA DA PRATA | MINAS GERAIS | Brasil | 3109600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a3876a90-0e2e-3b64-8c34-2b1ea1caf8d3 | -19.5933 | -44.900101 | 2024-09-26 00:53:04 | METOP-B | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f1294d5b-7714-37a7-9fa0-655c0beb0e2a | -19.596201 | -44.9118 | 2024-09-26 00:53:04 | METOP-B | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ffe24ac9-3abd-3a47-8e6b-b13ac682fcd2 | -19.599199 | -44.9235 | 2024-09-26 00:53:04 | METOP-B | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 85cbe132-c97e-3b03-99e0-f047e38a8418 | -19.9881 | -47.146599 | 2024-09-26 00:53:06 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 13ef8ea5-6db3-3e18-9a27-84ecc1c3f07e | -21.3878 | -54.594898 | 2024-09-26 00:53:09 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9d3253f-c3be-31b3-b603-6fc2feceb3aa | -21.3897 | -54.6049 | 2024-09-26 00:53:09 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3daf50ca-da03-3647-a16d-1e012d1aec94 | -21.3916 | -54.614799 | 2024-09-26 00:53:09 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 296741fb-473c-3c3b-b8e3-5091132a921d | -21.397301 | -54.644798 | 2024-09-26 00:53:09 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 75b018e3-6195-343b-9397-a554738da8c3 | -21.379999 | -54.606998 | 2024-09-26 00:53:10 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0d19da48-b142-36c3-9e8b-4f01437d5d12 | -21.387501 | -54.6469 | 2024-09-26 00:53:10 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 92c76a4c-3590-3fe6-a8a2-2fa5ed2c32f6 | -20.5959 | -51.464199 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec619fbd-3eb3-32e9-af6c-dd0bab15ea95 | -20.6187 | -51.474499 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c389c4a3-0580-342a-b935-d4fe8c234592 | -20.6203 | -51.481998 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| affaf9f6-c3f1-348b-9281-efe99a383818 | -20.621799 | -51.489399 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d36b951-c3d4-39a1-bca8-0214bf6e9304 | -20.6073 | -51.469299 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b4cfef3-e4fa-36a9-9ffe-f0b14d7f8aef | -20.6089 | -51.476799 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20855b4f-2a89-3301-b5f2-70501ed39a82 | -20.6105 | -51.484299 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e6e5982-8744-38f3-9c15-d8e90037c8a8 | -20.612 | -51.491699 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa2596b5-9659-3eda-9e8d-c80ba28ec2ff | -20.5944 | -51.456799 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 986add1e-2e62-3fdc-bd49-5027d712a84c | -20.5975 | -51.4716 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 76b572b6-8320-346c-baf6-fcc3ffaf49d0 | -20.5991 | -51.479099 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 50c81d9a-39e9-3c20-a5c8-ad2834f45b73 | -20.6007 | -51.486599 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5cb3e030-6215-3120-bcc1-1efa4ba37a4d | -20.6022 | -51.493999 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cceec60d-238e-38d1-9635-8a9225a9d998 | -20.5861 | -51.466499 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c4892cc5-2bea-3f40-a0d6-fccda74ce2eb | -20.5877 | -51.4739 | 2024-09-26 00:53:12 | METOP-B | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c21aabf5-e46f-376f-a31d-21382263cb9a | -18.143801 | -42.752602 | 2024-09-26 00:53:18 | METOP-B | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1daeee5-af99-3de0-8437-326889b2a345 | -17.9743 | -42.273399 | 2024-09-26 00:53:19 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61a58cf5-c71d-3606-a978-71a4fe53b2aa | -17.9792 | -42.291599 | 2024-09-26 00:53:19 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77da8b0e-beeb-39d3-bfaa-b0b7d14650a5 | -19.064699 | -47.268902 | 2024-09-26 00:53:22 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce55cc5-b19a-3b37-893a-6c2aee42fb8c | -19.066799 | -47.277699 | 2024-09-26 00:53:22 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bd9f14c3-6c4d-3235-a77f-767d8e85fda1 | -19.4566 | -49.130501 | 2024-09-26 00:53:22 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 816b75eb-ea53-374b-974c-22f79874ab15 | -19.4583 | -49.138 | 2024-09-26 00:53:22 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a8dbc83c-0044-30c0-859f-cd2815cc8ca5 | -18.426201 | -45.087002 | 2024-09-26 00:53:23 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 94cb4eff-b20e-3c9f-aa57-e70c7ea9729d | -19.107599 | -48.019699 | 2024-09-26 00:53:24 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8fdd0e22-9abe-35ee-a253-816eef61fe54 | -19.109501 | -48.028 | 2024-09-26 00:53:24 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d95ef541-3d1a-3c17-9b16-750e20e3d1c0 | -19.2768 | -49.111599 | 2024-09-26 00:53:25 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 05401077-a095-343f-a2e6-52da07fb93db | -19.2785 | -49.119202 | 2024-09-26 00:53:25 | METOP-B | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25339a23-73d3-3b57-b794-50c39effd061 | -19.8001 | -51.488701 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c99dcc96-f44f-3536-af1d-d8d56f013a28 | -19.785601 | -51.468899 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fdef6976-664a-37f9-893b-b534916c08cd | -19.7871 | -51.476299 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3c373365-54eb-3683-84ef-d847e3258151 | -19.7887 | -51.4837 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fd7cd46a-18eb-360f-9569-9f7d17ca16bb | -19.7903 | -51.491001 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f7acadba-794f-301a-8895-80a0125e66d8 | -19.7918 | -51.498402 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ef1cfbf5-b907-399a-ae4d-983ed9f23ca2 | -19.777399 | -51.4786 | 2024-09-26 00:53:25 | METOP-B | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d0e71813-dbe7-3ea5-b1a4-ce1812e4e39f | -18.024401 | -44.362999 | 2024-09-26 00:53:27 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 620be87c-4504-345f-ad1c-8b2805fcebdf | -18.0278 | -44.3764 | 2024-09-26 00:53:27 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c265b1e5-de1c-3b95-b883-0dbcb050a020 | -18.018101 | -44.379101 | 2024-09-26 00:53:27 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cda78965-429b-371c-a360-1895db9c1574 | -17.9737 | -44.448502 | 2024-09-26 00:53:28 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 87c76dcc-b505-3ca4-81cd-54156149125d | -17.983299 | -44.445801 | 2024-09-26 00:53:28 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1af69e29-d97c-32c2-baf2-d3b8f7af16c7 | -17.9867 | -44.459 | 2024-09-26 00:53:28 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e1cdd031-65ef-36bf-9b31-d96b441852da | -17.9771 | -44.4617 | 2024-09-26 00:53:28 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3cb6b73-f38b-3d81-9e53-75590df4f280 | -18.504299 | -47.090401 | 2024-09-26 00:53:30 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8ae4da35-0077-33b9-9217-b798bc2aa103 | -20.0898 | -55.523102 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3c13b3a0-5e57-3715-a231-7626cd06e838 | -20.091801 | -55.533798 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ed60651a-a9bf-3e0d-ae98-f0da4193e126 | -20.076 | -55.503799 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5fde6e-2776-36ea-bb4f-ca73838ee657 | -20.077999 | -55.5145 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d3452cd2-6fca-3366-b3d9-c3074a0f9f66 | -20.08 | -55.5252 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 049e8275-abe3-353e-9bfc-a56151b3bcce | -20.082001 | -55.5359 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a2d19897-eabf-3de4-895a-e08c0dd42602 | -20.0662 | -55.505798 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 311d601c-6766-3a68-9c26-35ab4829c4e1 | -20.0683 | -55.516499 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58473c7a-b9a6-3020-99e4-988c21875cec | -20.070299 | -55.527199 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 22254917-705c-316d-b924-2fa1d55d40d7 | -20.0723 | -55.537899 | 2024-09-26 00:53:34 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f09fc84e-38af-3635-bdf2-9d9f55dc7328 | -20.0093 | -55.473499 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cf458a13-002a-3718-8536-5884d1460d6c | -19.9995 | -55.475601 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1752cead-a25d-36b0-83a6-72a116600d0a | -20.001499 | -55.486198 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1942e07b-f03b-3ef5-81a7-7d3f139f2619 | -19.9897 | -55.4776 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ff388e58-f26d-317e-a1de-550ac8298054 | -19.991699 | -55.488201 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 31bfcfcd-36a5-3435-a78b-383bf5964bde | -19.9937 | -55.498798 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| df3a0fd4-f1f7-36e3-977b-1265fa82810a | -19.982 | -55.490299 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ac8a3283-1183-3655-af7a-b20e1ad1857d | -19.983999 | -55.5009 | 2024-09-26 00:53:35 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb46f51-426e-3924-92c7-9a1eca8739c1 | -19.0448 | -51.512699 | 2024-09-26 00:53:37 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d5d22550-7d68-3ace-96bc-a602b8f68120 | -19.0464 | -51.52 | 2024-09-26 00:53:37 | METOP-B | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8b4bc131-98eb-3c42-976c-4c8196d37be4 | -18.4501 | -49.198399 | 2024-09-26 00:53:39 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 625e07d9-6628-3c6e-85cf-1f98c4821835 | -18.451799 | -49.206001 | 2024-09-26 00:53:39 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22435f27-c02c-3607-868b-d925f3140829 | -18.209999 | -49.097 | 2024-09-26 00:53:42 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b222bb9-edaa-3fc3-bd29-6867413b49e4 | -18.200199 | -49.0994 | 2024-09-26 00:53:42 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee76070e-3c04-3393-975b-69eb9de2d950 | -18.1905 | -49.101898 | 2024-09-26 00:53:43 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e3b08ab-2654-30cb-ace0-fa19cb02d5be | -18.6374 | -51.769402 | 2024-09-26 00:53:45 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 14df8da1-c3bd-32b1-8b0e-45423ad47808 | -17.2281 | -46.271301 | 2024-09-26 00:53:47 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 543dae76-c107-3749-a5a9-725535a1a5d4 | -19.139999 | -57.448101 | 2024-09-26 00:53:55 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README18.md)
