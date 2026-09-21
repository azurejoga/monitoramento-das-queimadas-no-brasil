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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9af75e27-7346-37b6-a451-99f5ad95f3ce | -8.0279 | -61.3626 | 2026-09-21 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 85eb4f32-8d50-38d4-ba26-712e8eea3e4b | -10.4675 | -50.2624 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dd0ad81a-5e59-3e03-9aff-8591c14fbf9c | -16.9964 | -56.4525 | 2026-09-21 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 04d23bc0-1e93-32bf-9138-09998414440b | -9.8325 | -48.3198 | 2026-09-21 14:40:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| f6dee95b-17bb-3233-ad9e-b467952ae5e2 | -10.3728 | -48.8936 | 2026-09-21 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 49b89591-faa5-3164-9884-9019d062cad8 | -8.7706 | -45.8567 | 2026-09-21 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 7ad50699-1c43-3b34-bac7-344f39965d11 | -8.7914 | -48.7285 | 2026-09-21 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 5576aecb-7b29-33a5-9df2-78eebc339911 | -3.7129 | -60.5832 | 2026-09-21 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 5649ac08-558e-331e-94f3-28f45a7a4621 | -6.8264 | -55.5222 | 2026-09-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| d9bb6943-a0c5-3802-8d14-cd0f2ceabf86 | -10.8921 | -53.9857 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 52f89245-b770-3854-adf3-bc1f8f4d80c3 | -9.0239 | -48.1622 | 2026-09-21 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| cf2afc57-2c48-39d1-b87b-79bc9aa26927 | -2.9157 | -57.7983 | 2026-09-21 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 59760800-0141-3868-916c-2cc7723296a8 | -3.4555 | -50.5927 | 2026-09-21 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9a6d7fc6-2021-337d-bdd3-63f1ac5a5f44 | -10.3914 | -48.9133 | 2026-09-21 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 177.3 |
| cb12e1dc-e563-366a-a5f5-db0db96a729c | -3.1698 | -58.5859 | 2026-09-21 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 780cd722-d850-3ad1-9c97-d41339deb0f2 | -7.5477 | -61.3247 | 2026-09-21 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8708c3f1-3fdd-3893-a8ca-9c5e24c7b00d | -12.1853 | -50.8623 | 2026-09-21 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| afa65470-a41d-3cdc-9545-1412879beb20 | -10.2152 | -53.9216 | 2026-09-21 14:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 4c6f79c4-35d1-3dc9-8498-433ee82d197b | -6.3197 | -59.9764 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e13664ea-52c3-3724-89d7-bb1ad6e3424b | -10.4919 | -51.279 | 2026-09-21 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| fc2ba0be-031d-31f4-917b-f540f63b95cb | -10.5906 | -53.9918 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 03600db7-20d1-392e-926c-c32280e592dc | -5.7504 | -43.7091 | 2026-09-21 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 895d3bde-0835-3ba1-9c07-b4d7fda22f8d | -6.6014 | -58.9844 | 2026-09-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 193428db-ad2e-30ab-935d-6d3fb43e90f8 | -10.8014 | -50.7391 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 71b1d4c4-2b9a-3ce3-bced-4b392817bbd5 | -6.3196 | -59.9956 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| cd282373-8be9-3138-b9cc-e9127da0f024 | -8.7912 | -44.301 | 2026-09-21 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 38a04427-bba6-3868-8539-a4335286d206 | -7.5704 | -57.6766 | 2026-09-21 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 5020967c-15f8-311a-b405-931021bcefe5 | -10.9361 | -50.5759 | 2026-09-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| d18ff668-8219-3a4b-8f8e-366396e1e1a3 | -3.6449 | -58.8647 | 2026-09-21 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| f53ede5c-8cf6-3f53-acb3-ee74bfbfb4a8 | -5.8274 | -47.7898 | 2026-09-21 14:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3fb0a37c-d8eb-3a87-8602-acf97b2340ab | -10.7115 | -60.7312 | 2026-09-21 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4823139a-5049-3fd4-91f2-346a9df9277e | -7.2519 | -55.5994 | 2026-09-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| df14e52f-e72f-3cb4-a9d7-a5af0883a57f | -10.3546 | -50.2313 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| c3a6848e-936d-3e68-a0b8-822e2e0bafae | -6.8243 | -55.8208 | 2026-09-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4954bc90-2059-3567-94e4-66165509621a | -11.0223 | -54.1379 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 7da9ba04-0c92-3569-b8f4-95d9c6435f5a | -6.3195 | -60.0147 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 63d72569-9568-35d1-9d1a-bdeb6af47610 | -12.026 | -50.0663 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6973a462-a727-32ca-9652-9ae7660092e3 | -6.7484 | -59.075 | 2026-09-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a2e59eac-18c6-3c07-aa5f-48968b9c3cf3 | -10.955 | -50.5738 | 2026-09-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 893a1397-8d9c-3478-adbb-4c24da21f221 | -11.8362 | -50.0244 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| f8801ecd-57c3-385e-9086-2a90b3efc790 | -8.1871 | -54.7824 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9f0a976a-6f62-3dd6-94c0-5497a0e8ff96 | -9.0428 | -48.1603 | 2026-09-21 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 228.2 |
| 794c93c0-d42b-3c84-9e35-f9c320f8b3e3 | -3.2817 | -57.8685 | 2026-09-21 14:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 466f75a6-528a-3884-bbf1-0dbfb8d318b5 | -6.6763 | -50.9172 | 2026-09-21 14:40:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| aac06cad-337a-372b-baa5-4f3983d2ba64 | -12.4012 | -47.0255 | 2026-09-21 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 222f955a-ce8c-3dc3-bbc9-d78163b80954 | -6.3383 | -59.9374 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 52401220-fe8d-34d1-8ff2-e99d8f14bf18 | -10.9544 | -50.6165 | 2026-09-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 2583ecf4-223e-34a8-8b3f-4332f01c6be9 | -10.3357 | -50.2333 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a0e76729-8167-3126-8403-4d432cf6cb8b | -3.3453 | -42.7832 | 2026-09-21 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| f945bb33-00d2-3cf7-9650-70f0c60e2ed2 | -6.9037 | -42.9105 | 2026-09-21 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| 3b476677-8412-3e93-a449-726e2ad6d90c | -9.457 | -45.395 | 2026-09-21 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 24138c5c-1ff1-3e67-bce4-e0bd43d5b354 | -6.4486 | -59.9717 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 284c1a52-d4b6-307d-a332-6c70121995f2 | -3.4599 | -59.5209 | 2026-09-21 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0fce8f87-fa69-3be2-a9d0-e76df85d8b5d | -10.8911 | -54.0677 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 815ced39-bfcb-3cbf-99a5-fcda8636b5de | -10.9358 | -50.5972 | 2026-09-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8c8ac94b-cef7-33b6-a3e8-c9bb5b317bbd | -9.2756 | -46.2077 | 2026-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 43f25b1a-87d0-3094-a21a-42b2ed912281 | -5.6223 | -43.3701 | 2026-09-21 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 301.4 |
| b127f453-4dbe-394f-99c6-9977933ae2fe | -11.041 | -54.1567 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 269.2 |
| 913c4a40-01ee-3faa-b20b-5bbc09727333 | -6.7463 | -59.4416 | 2026-09-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 752b7f4e-15f5-35f9-b300-b1f89d66447f | -13.2404 | -51.7997 | 2026-09-21 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| d425c429-d78e-3504-9ab0-f9b59718055d | -3.3267 | -42.7606 | 2026-09-21 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 206.0 |
| 6e8b60ce-3285-3c4a-8cad-e2cf4f4995e7 | -9.3986 | -48.3213 | 2026-09-21 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 9034443d-ab3a-3083-98b4-9cfcf96d82b9 | -7.5889 | -57.6757 | 2026-09-21 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 446599a4-f1b4-39b4-81ed-fa9183eea48e | -11.7823 | -49.8152 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ce2b3c02-4868-3906-9ca2-9298099dcc5c | -8.845 | -45.9391 | 2026-09-21 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 8a98f47f-0c31-367e-b590-c0d6e2b58427 | -6.9034 | -42.9341 | 2026-09-21 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 183.4 |
| c2644f24-ac2e-365a-af46-a3fd40009524 | -6.8058 | -55.8217 | 2026-09-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| d87a7f0f-b5a1-315b-a5fe-2c2fa14f4891 | -10.8735 | -53.9668 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| d67949e2-0882-3b7a-aafc-fe2c19444524 | -6.3014 | -59.9579 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c5863961-6716-3b99-9357-e68e177669c5 | -9.831 | -48.4292 | 2026-09-21 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 9dae1f05-ac18-34a4-8c50-b7ad5d500388 | -12.0451 | -50.064 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 3767d852-681a-3fd7-890f-0fb02f0680d7 | -5.9151 | -59.9522 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| eee89cbb-468b-38a7-a3e9-c5d9ddd22f44 | -8.7911 | -48.7502 | 2026-09-21 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 33875003-200d-3b0b-94e4-f2af2904aaff | -10.8924 | -53.9652 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9fe81587-d5fa-3dcc-9282-f6476d728cbe | -10.473 | -51.2808 | 2026-09-21 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9728f290-64bc-3a8b-8404-1e63134fb4ed | -10.2979 | -50.2372 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 72bc2312-632a-30fd-b6b3-5129d5f77bef | -6.8263 | -55.5421 | 2026-09-21 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| f318eeb5-01c2-3848-a8a7-87468730fab9 | -10.3924 | -50.2275 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f5384560-403f-38b2-b0f1-a122d34bb531 | -3.0507 | -50.2702 | 2026-09-21 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9fd274b4-a437-300a-96e7-f7755da8f3d2 | -3.3454 | -42.7597 | 2026-09-21 14:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 8c7f1c12-fb86-36bb-ac86-7606f9cdcc49 | -10.3725 | -48.9153 | 2026-09-21 14:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 5d92abae-3122-3783-ad85-701765317605 | -6.0197 | -51.7686 | 2026-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4474140e-36c4-33ac-931b-cbca6b5151e4 | -6.9223 | -42.9323 | 2026-09-21 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.7 |
| e4723599-ec4a-3315-a871-fb61e77fd33c | -10.4483 | -50.2858 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ffcd1ffb-6191-374b-afd8-e9955b1cd57c | -10.3921 | -50.2488 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 15564896-40fe-3952-bba0-1b91164c1620 | -8.3164 | -46.016 | 2026-09-21 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 22e67d02-44f9-34b6-bb70-a8b7b333a756 | -3.3823 | -50.4486 | 2026-09-21 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7e0bbed4-fc49-3155-a235-b2bf38896386 | -11.0804 | -49.7456 | 2026-09-21 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 3804778e-c566-3a2d-b4e5-f5b2f3a684e7 | -11.8014 | -49.8129 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 97f845b7-f1da-395e-8433-d3a51593d28c | -5.6408 | -43.392 | 2026-09-21 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| ea3b522d-2822-363a-8493-2cb5dd02ce2d | -6.2585 | -41.6617 | 2026-09-21 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| 9a37845b-8b11-33a8-bbe6-f0e651dccafb | -6.0194 | -51.81 | 2026-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 891fb547-187b-373f-8703-c7d16443e24a | -6.4554 | -48.4423 | 2026-09-21 14:40:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c376b88c-cd7c-36a2-8e90-4c0dc7df7f59 | -6.8985 | -41.6976 | 2026-09-21 14:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 43db595f-ea3f-35e0-b2d5-46b165c0eebc | -3.4461 | -58.0199 | 2026-09-21 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 20f53b79-bba2-3fc9-9513-ff6da48bcd1f | -10.0898 | -50.2795 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| c21efe21-57b2-3b99-bc27-3ef2634c11e5 | -12.3025 | -50.6774 | 2026-09-21 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 7ec7cdef-fe43-3234-9dec-b390243496c5 | -6.4107 | -45.1934 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 03946274-4b14-39f7-85c3-527f5aafe9c0 | -10.9112 | -53.9635 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 221edff9-4af5-3867-8cb6-b648e820f9ce | -10.7813 | -50.8262 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |


[Clique aqui para ver as próximas entradas](README132.md)
