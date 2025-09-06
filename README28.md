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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a5b702e-8caa-3f1e-9e28-45514e9f4d7c | -18.00996 | -49.26213 | 2025-09-06 03:51:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 040e7680-7e42-31c5-81b3-c64da838dab3 | -13.72234 | -46.90903 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1f705a9-4c9d-301f-a577-66ff51524638 | -14.90084 | -49.45922 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| a848bbd7-73dc-3fd5-8732-a555f2d503e2 | -21.49269 | -46.19496 | 2025-09-06 03:51:00 | NOAA-21 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ea01cb1-47ae-3b5e-87ed-505848f42f5c | -14.12068 | -51.71263 | 2025-09-06 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a67746a5-0996-3984-a4cc-220a2d764cfe | -13.88082 | -48.02978 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 039b6f9e-917b-3e46-af1f-5cbd7aa97bf3 | -14.74897 | -42.65137 | 2025-09-06 03:51:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b598f6da-a0c1-33e0-97b5-2082232a570c | -14.89598 | -49.45408 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 21c2bfba-d93f-3bab-99f3-ccfffd761ce5 | -18.56018 | -44.04047 | 2025-09-06 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a93e776-33bc-335c-97a3-af55afede4c6 | -13.85189 | -46.26216 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cfb0548-2a54-3b2b-9227-55dc49628096 | -17.96562 | -44.41799 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3da9c68c-9096-3b04-97c7-0c721d10ef9d | -14.83222 | -48.1913 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aea50b4f-2103-3667-9cc7-160bb943510b | -19.2104 | -42.87624 | 2025-09-06 03:51:00 | NOAA-21 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 48a963fe-a298-3952-90d3-6b5bd4fba244 | -16.92286 | -45.75566 | 2025-09-06 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 760d8cea-62be-3f4b-b300-50d7114f76db | -13.84703 | -46.26873 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9cd74e33-b6a1-307a-822c-fe2a200ad8d2 | -15.54915 | -49.8235 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| adb8967d-bf22-30be-94e8-14a5df6da503 | -15.72589 | -53.58466 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cacfddd1-fb2a-3197-96e1-d54ec2aa6bed | -19.79224 | -40.84512 | 2025-09-06 03:51:00 | NOAA-21 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 47aac222-be23-3ebf-9f01-a3898cd78075 | -15.64371 | -41.85271 | 2025-09-06 03:51:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0221b293-87b0-3478-84bd-9156fd46073b | -19.69358 | -47.96731 | 2025-09-06 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40dda780-1e4d-3796-bfaa-de168a2ebaeb | -20.48504 | -45.15091 | 2025-09-06 03:51:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 146fde8b-bec7-3f41-8002-b927d7bad835 | -15.54428 | -49.81817 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91470338-fd22-3fe9-9b78-42731984b5b1 | -20.53339 | -46.45776 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dbe23b1-9eca-3722-a059-d13fe26321ef | -15.55 | -49.81636 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f37f96b4-2a28-3ee6-9c36-c02d794bfff6 | -18.26157 | -43.02567 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96e5be19-de52-39c0-aa67-ee13a96f4516 | -15.07564 | -48.11558 | 2025-09-06 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6f27fbe8-a86b-3272-9549-e1ab48f4dbf9 | -14.58725 | -48.08533 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48385739-62ec-3554-aecd-62938cd05371 | -15.57577 | -52.91849 | 2025-09-06 03:51:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 03190f45-b770-3fc5-8d93-a90fe1eb157e | -19.40427 | -44.31269 | 2025-09-06 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 96cc7374-4c9c-30ba-94d7-1a54951855a3 | -15.72222 | -53.58507 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6be97902-9905-34c4-afc9-4f581834bdf9 | -16.60279 | -48.95148 | 2025-09-06 03:51:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e1428b9-59ad-30a8-a184-7c97652e9461 | -18.5395 | -47.41698 | 2025-09-06 03:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3838fde3-d7b8-3461-a691-46109f5a08fe | -20.54159 | -46.46082 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 602353f1-67af-3896-885d-5f223c44e4f7 | -13.7203 | -46.91297 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d4f9dd3b-9a28-3864-9df4-d98b794414ab | -14.59054 | -48.09644 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b039e62-35e8-336b-afb0-a6ba1365eaf4 | -14.80393 | -48.11503 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64f6b5e1-6516-365a-a016-35f3b3a413a0 | -14.59124 | -48.09097 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea400f49-231d-39d8-b69c-b73167954ad1 | -14.59115 | -48.09328 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37d807e0-b7ee-38c4-ac43-00841d43a920 | -15.18338 | -47.98629 | 2025-09-06 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f729e39d-06b2-3046-8352-c3afaefde6a4 | -13.73686 | -46.91324 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65b9a137-3cff-3a31-9a32-9fb559a62bac | -15.71832 | -53.5693 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c616be9-8294-358d-b7c4-12ff3f0ef099 | -21.29572 | -43.52448 | 2025-09-06 03:51:00 | NOAA-21 | SANTA BÁRBARA DO TUGÚRIO | MINAS GERAIS | Brasil | 3157302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a2b41518-5a8e-3493-ad5c-1f6fe07a2f3a | -16.5471 | -42.35107 | 2025-09-06 03:51:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ded572f8-ae37-3210-9dbd-c342ea24caa7 | -18.27097 | -43.02178 | 2025-09-06 03:51:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 324ba522-5587-3660-b798-cfcaa452733f | -14.58666 | -48.08833 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cb0ec48-d76f-3a5e-baf2-120acd125101 | -19.41171 | -44.31493 | 2025-09-06 03:51:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13141abe-90cb-3c05-9e54-4c86b5265e78 | -15.54342 | -49.82226 | 2025-09-06 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 01a5eeed-415b-3a38-b6b7-d187f28a3c67 | -19.93686 | -43.60863 | 2025-09-06 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 642b6234-32bd-37a6-8afb-2ba512b70fd3 | -18.14551 | -51.77878 | 2025-09-06 03:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 23a772c3-7d52-3fe1-8bf8-8d9f8a70923e | -18.14651 | -51.77928 | 2025-09-06 03:51:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| da563606-bfbf-314a-a3a0-0d9f289c4e0f | -14.83614 | -48.19901 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16f86510-3657-34e3-96a8-afc24d00f503 | -14.58782 | -47.99883 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbfccace-cfc7-360c-add8-6c80f73d05a0 | -17.70501 | -44.49359 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d32ed7f-f976-36d9-b47a-24e3707f499e | -17.87388 | -44.32213 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a500133d-c82c-392f-b985-6d4c62e82c18 | -20.53752 | -46.45913 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77d0030f-e7eb-31cb-9d0c-9081817aeed8 | -20.5358 | -46.46801 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0185dac9-944f-3f59-8d93-1999b9a7da1a | -20.18169 | -44.24135 | 2025-09-06 03:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a10e6ba9-0099-3ae3-a0df-c424e0928eb3 | -13.88689 | -48.02689 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e43c56f-38cb-3088-9ab3-1d018c2f516d | -14.58115 | -48.00523 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29f6ac6f-a5a2-32c3-abc0-fcd61e4a1065 | -13.84236 | -46.2676 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d7234d41-5b6b-398c-b1a5-ad055c946f6f | -16.54785 | -42.34674 | 2025-09-06 03:51:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 173e7434-00fe-3ae8-9827-5c510cbd1e86 | -14.19162 | -53.02364 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77b77a1b-238a-3e63-ad3e-88b506e95799 | -17.7 | -44.49863 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd068d5c-9084-3c25-bbff-89beb5325739 | -16.91586 | -45.74542 | 2025-09-06 03:51:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 303b24d1-7115-3aac-975e-66f24f43a803 | -20.5251 | -46.11044 | 2025-09-06 03:51:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b884ff45-50b7-35a6-82eb-08c7e43c4f00 | -13.72122 | -46.91473 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3d40696-3d60-336f-989b-29b3e113670e | -20.35154 | -48.64092 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ce6c7d8-3a46-318b-94c6-ea9ac798dd98 | -19.50651 | -42.57097 | 2025-09-06 03:51:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 98f67e2e-66d6-359f-8457-99381d769d53 | -15.71868 | -53.58359 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65f83e11-5f8f-3b21-ba5a-3c75d4d1a6dd | -15.63596 | -41.85555 | 2025-09-06 03:51:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f07a70ea-affd-300f-97ce-bd7eedfbe987 | -15.72196 | -53.5694 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 253faf3b-9166-31b3-8ed6-0e4192a3c169 | -14.57573 | -49.12659 | 2025-09-06 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6a1292f-e17b-3f23-b2c3-fba9cd7c8b3f | -13.90416 | -48.02288 | 2025-09-06 03:51:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e482db44-fe54-3535-8749-3e88d5e67b82 | -18.43936 | -45.93638 | 2025-09-06 03:51:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7bc303f-5e11-372a-a030-2a3dbc2cd93a | -14.57722 | -48.08091 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd97f324-cb86-303c-939a-ee689a549099 | -21.09632 | -44.22712 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0ffc29d-de37-38fd-b96a-d54a2f17f065 | -14.1926 | -53.06897 | 2025-09-06 03:51:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 092e3c76-865b-33e1-92bf-76fbf406d552 | -14.56988 | -48.09056 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee877a73-55e5-33d2-86b8-f4af65558d2e | -14.58051 | -48.00854 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65950081-a66d-3860-9a1f-4c9c144a9884 | -13.75017 | -46.92376 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 897fa4d6-134d-38cf-be8f-7fe8eb84473a | -20.53988 | -46.46966 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 385dfe6f-515b-348c-ab48-130268340375 | -17.71278 | -44.49562 | 2025-09-06 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c8f6a83-c052-3425-bcaa-17e0104636a4 | -15.72036 | -53.57634 | 2025-09-06 03:51:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7950202-f920-3f52-8893-5168643343c6 | -17.91662 | -45.90739 | 2025-09-06 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46d0e8b9-92cc-399d-98f3-9398ae7e20a4 | -13.74913 | -46.92913 | 2025-09-06 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76614cd7-e5d0-3cb0-bcac-d196a7a9018e | -14.90002 | -49.46318 | 2025-09-06 03:51:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34d17dd7-0133-3c8e-9f7b-cd087b937c02 | -14.57787 | -48.07759 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e09946f7-1842-3ab0-82ab-fcb85b30c40a | -20.46373 | -48.78492 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| eacd7738-0623-3bb5-945c-b8165c995e0b | -21.02935 | -45.1178 | 2025-09-06 03:51:00 | NOAA-21 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f8b0d14-1aa7-3faf-b156-e2738f76fb47 | -14.57203 | -48.02411 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d475a74f-8c49-3e3b-9c4e-81be73e4c547 | -15.18269 | -47.98974 | 2025-09-06 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6dec3a6-86d3-3ebf-bb50-f666eea077d8 | -16.54429 | -42.34606 | 2025-09-06 03:51:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94689be1-5390-3e22-8231-828f63f6f854 | -20.35639 | -48.64207 | 2025-09-06 03:51:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc2c4106-0618-3de4-8ef5-ffd32d8addc8 | -14.59248 | -48.00272 | 2025-09-06 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4564b4b-0346-38a1-9325-4739900de4d8 | -18.56039 | -43.82452 | 2025-09-06 03:51:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c513239-7be9-3971-8bb0-cb6b07344aa2 | -13.85661 | -46.26309 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f092970c-e259-30dd-9bce-f63571eb16fc | -15.58243 | -52.92089 | 2025-09-06 03:51:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b6310bf1-3bbc-39c6-b41c-5df60bca0e0d | -20.54074 | -46.46519 | 2025-09-06 03:51:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b01be569-2026-390d-b7ff-a403b780d797 | -13.85288 | -46.25681 | 2025-09-06 03:51:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec8b65e8-522e-37df-84d3-bc3832ae39e1 | -17.00826 | -43.7816 | 2025-09-06 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README29.md)
