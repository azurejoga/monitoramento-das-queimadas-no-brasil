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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24ef5d35-e116-3ed0-b57a-c64352d72f11 | -7.8369 | -54.401 | 2026-09-12 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2ecd0063-0db4-3ea3-92c7-9a4591eeb995 | -18.8868 | -46.9692 | 2026-09-12 01:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a1ade4a2-cada-3309-aa1c-c243962d79d4 | -3.2128 | -46.9602 | 2026-09-12 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5b80d969-bcb3-3c54-bf61-0c5230f79851 | -10.7015 | -54.1663 | 2026-09-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 224.3 |
| 7fc11005-5716-3112-a018-7d5546fcf6fe | -3.2313 | -46.9596 | 2026-09-12 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 183.7 |
| b94c2b8d-4c27-3156-ad3f-4faaeeaf3abf | -5.7569 | -45.084 | 2026-09-12 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 255.3 |
| e944ac84-e2fe-35fe-b8c5-e8f1b12a48e2 | -5.7756 | -45.0826 | 2026-09-12 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 452.4 |
| c919d630-a9f1-3107-abee-f0f6f011dd0f | -10.7018 | -54.1458 | 2026-09-12 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 25155c23-84e2-3395-b712-4aa1ac420be4 | -14.579 | -52.67645 | 2026-09-12 01:00:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e6aeb577-c14a-39df-b114-d58777b3afe8 | -8.11894 | -54.81264 | 2026-09-12 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 1a11a668-f326-36ec-b8f5-9f6a00c0c481 | -6.61539 | -58.84028 | 2026-09-12 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6e09dd69-c085-3846-bb6d-ddea05af7e4c | -10.25445 | -69.08128 | 2026-09-12 01:02:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1fb96dff-8347-35e5-a63d-e636c2f034f9 | -8.75936 | -70.81432 | 2026-09-12 01:02:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f36812c4-26e5-37ee-9fdb-01b8a2d866c5 | -9.68993 | -67.39046 | 2026-09-12 01:02:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0382040a-5269-3254-8d99-d2757a220ddf | -9.69163 | -67.39604 | 2026-09-12 01:02:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 00cf4bc3-6283-3aca-a5d0-7527ad5d1cf4 | -8.95652 | -67.39333 | 2026-09-12 01:02:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 26b39437-c48e-370e-af03-42bb543755b3 | -9.17369 | -65.94219 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b76da270-3dd6-318a-ae76-0cc7cc54394f | -12.15455 | -64.13838 | 2026-09-12 01:02:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 73bb766d-fa2b-36d1-9e92-baafaff8d49b | -10.67812 | -54.14631 | 2026-09-12 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.9 |
| dc1ad495-4586-3d98-b868-29f7da9f4b40 | -8.9551 | -67.38215 | 2026-09-12 01:02:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c7662448-516a-3f2f-9288-f78857251138 | -10.28213 | -68.75401 | 2026-09-12 01:02:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 14.7 |
| cb6e5da1-19b9-39c3-b2ae-749c2ca28f18 | -8.69415 | -71.02744 | 2026-09-12 01:02:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e5c6c8b5-8ef5-312a-819c-d1d81a35aab9 | -8.98294 | -70.60382 | 2026-09-12 01:02:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 15120bbc-b077-3f04-b4c3-0c63e4ed9618 | -11.91639 | -63.27436 | 2026-09-12 01:02:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 569ae67b-4da8-3625-ae30-3897df4efc4b | -8.95393 | -67.38819 | 2026-09-12 01:02:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| bbf950df-c3ac-3ee5-b1a1-382b6a19b08c | -8.92009 | -66.88174 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0f0e9cc2-61a5-314e-85ee-23b5e1e8978b | -6.77185 | -59.43277 | 2026-09-12 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| fc135be7-958e-36f0-a40a-a6c1214e1be7 | -9.31294 | -68.78001 | 2026-09-12 01:02:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8bf130f7-dd3b-3c21-85b2-8c948c3fd987 | -9.33727 | -68.28285 | 2026-09-12 01:02:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 17.2 |
| f3ffeaa6-f829-37ee-aa95-86ad15db3c4d | -9.33559 | -68.26995 | 2026-09-12 01:02:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 2f747a1c-0a28-3601-a4d3-d86cc8974d3e | -9.46639 | -67.09203 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e07c814-272b-3cd1-bf5b-58f763f7b68c | -6.18599 | -57.72852 | 2026-09-12 01:02:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| dba3e53b-e271-36fd-8fa7-d63632916114 | -9.50799 | -66.78716 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 887d03f3-d68b-315b-8358-4f43c093f9bd | -8.63979 | -69.26887 | 2026-09-12 01:02:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6e719f48-c4fc-36a6-9020-f836cec08186 | -9.30906 | -68.77192 | 2026-09-12 01:02:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c9a34850-1412-3ce4-923e-0ab55faba9ed | -8.98191 | -70.60948 | 2026-09-12 01:02:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0825fa6f-d150-3589-8984-0d48b35ae9bf | -6.1793 | -57.72284 | 2026-09-12 01:02:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 2fa895d4-f3cb-3444-b31a-33f92cc501ca | -6.11868 | -55.64779 | 2026-09-12 01:02:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8e5cedb6-9836-38bb-8882-12f039666ea7 | -12.15578 | -64.14739 | 2026-09-12 01:02:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 45be90b4-4d25-344d-8f5d-727d13a1becf | -9.47975 | -67.09557 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4b4699da-37db-3914-93eb-31650947bdd6 | -9.6902 | -67.38464 | 2026-09-12 01:02:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6432fadd-8c06-3490-904b-5e912109ce2d | -6.8832 | -55.64232 | 2026-09-12 01:02:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1cbcdce8-77f8-3940-8d23-5c7886bf614c | -9.44806 | -67.02824 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f7184917-406d-36ce-9acd-5512e321eb5e | -9.46784 | -67.10292 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 600c6db0-93c6-3ac4-a755-f695f346e308 | -9.52858 | -67.16713 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3df0e85f-5021-3a58-84d1-48426ca012ac | -6.88984 | -55.6464 | 2026-09-12 01:02:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| ee64846a-92f0-3507-b520-dc3492b61f7b | -8.69581 | -71.03273 | 2026-09-12 01:02:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 066a5e0b-c504-36f8-95c1-183f2208e02f | -6.60302 | -58.84215 | 2026-09-12 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 8bed6244-e19d-3dff-868f-75b521e7251e | -8.63376 | -66.51398 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f37d5779-4a59-32ab-b01c-01b9c4877c20 | -6.33731 | -55.30758 | 2026-09-12 01:02:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| cb41d81b-8ccf-320b-84a6-746a09579c5e | -6.20955 | -55.27512 | 2026-09-12 01:02:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| f37d0d74-329c-31de-b5b0-81d7481bc460 | -6.85481 | -55.26498 | 2026-09-12 01:02:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 64d6741f-85b7-38be-b6a8-1785f625af97 | -8.64305 | -66.5127 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 19b4ba7c-59c8-3462-8c44-87419ef67d3a | -9.47004 | -67.09689 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| c72c0a72-0d0d-3c13-87cb-52984772c8cd | -10.6946 | -54.14318 | 2026-09-12 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.0 |
| e0167347-ef99-36f3-aac6-57fbbedd0036 | -10.70095 | -54.1797 | 2026-09-12 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 325.8 |
| 3b8195ae-a1f4-374a-b203-7408bc402b49 | -6.60578 | -58.86042 | 2026-09-12 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4f0558bf-b384-3a98-8fe6-a048180145ef | -9.4384 | -67.02953 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5af04329-0c0e-3c0d-a726-3719cd7582fd | -8.64029 | -69.27451 | 2026-09-12 01:02:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 01856802-c6dc-375a-bdb6-f1984df30be0 | -9.3461 | -68.2686 | 2026-09-12 01:02:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12df89d1-896e-3ef0-971a-ce8afd5ca076 | -9.34272 | -68.27585 | 2026-09-12 01:02:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4858ec94-d9af-3898-930a-3cc48951630d | -6.11054 | -55.6544 | 2026-09-12 01:02:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 45de4f0c-71a9-3c7b-bea1-011894ded3b0 | -9.54598 | -68.26351 | 2026-09-12 01:02:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0ccfdd27-fce4-326e-8dba-d18cf7d5b335 | -6.61812 | -58.85851 | 2026-09-12 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 656b1c65-df8f-3fd8-bc19-2298007c4c5f | -8.64183 | -67.01218 | 2026-09-12 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5772a82b-0393-3034-9ea9-aa1e1ff97aa7 | -9.13498 | -67.83398 | 2026-09-12 01:02:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e8ca2881-1ec9-317e-9089-96173e8c01e0 | -10.68931 | -54.14951 | 2026-09-12 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 429.8 |
| e17e8a52-ce31-35fe-a873-50a968961eb2 | -10.69542 | -54.18604 | 2026-09-12 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 351.1 |
| 05f94e6c-7eb4-37b8-b38a-48a7dc6b351f | -10.68452 | -54.18284 | 2026-09-12 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 261.5 |
| 82d7530b-e087-3074-bcc1-2fa9f5582990 | -8.9604 | -67.374298 | 2026-09-12 01:03:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5aa0b62-c017-3b49-bb30-d09a2974658e | -20.7202 | -54.602901 | 2026-09-12 01:03:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 144c1d34-62ff-30d6-b6aa-1db753c5260b | -6.6037 | -58.850498 | 2026-09-12 01:03:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8793bf1-270a-323a-9dd3-bdafe28eba15 | -9.4788 | -67.07 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edbadac4-1876-3e10-919b-dc2876e0ccfe | -6.2066 | -51.6777 | 2026-09-12 01:03:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e842a31-14ad-376c-be71-6a9dd495bfbc | -6.1989 | -51.647499 | 2026-09-12 01:03:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b104d8b0-0bf0-3133-9b62-f9591fd8c4b9 | -6.1934 | -55.248901 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 543aa2c5-b27b-3d61-b718-993b44bb7e99 | -12.1489 | -64.121399 | 2026-09-12 01:03:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f0bba31-e196-3ac9-95cb-b6ba59bcc115 | -6.3263 | -55.288502 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb7d7794-705b-3a4c-ae1a-adfad0c4794f | -6.874 | -55.637402 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273a3fcc-1870-39b2-91d8-a2ffdceaf115 | -9.4809 | -67.079697 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f5d1e8e-0495-391c-9651-552943f8bfc5 | -10.661 | -54.1385 | 2026-09-12 01:03:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 496f406f-de0a-3d12-9790-7ae1cfac81d1 | -6.9043 | -62.9245 | 2026-09-12 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 897f1843-0925-31ca-9144-13cb0ef62331 | -2.7035 | -57.621399 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8de3c0bd-3f0b-3eed-8597-6b7d49eb720d | -3.3479 | -59.4193 | 2026-09-12 01:03:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f391936e-9d92-3325-b29c-8ea66fa31345 | -10.1876 | -50.353802 | 2026-09-12 01:03:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd1167a-e416-3c31-b9ac-6fe1a6e09596 | -12.1522 | -64.136497 | 2026-09-12 01:03:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4650f18-b038-371b-a95b-867b8530f2e1 | -6.0862 | -55.610199 | 2026-09-12 01:03:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3a152f-0914-33ae-9ccb-1a12cdd3644a | -20.7355 | -54.6227 | 2026-09-12 01:03:00 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 60bdd14a-ffb8-3358-9dc5-ec9046c54bc1 | -6.9161 | -62.8857 | 2026-09-12 01:03:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 409d7b43-5c99-3187-8517-db61d212817f | -2.7066 | -57.6348 | 2026-09-12 01:03:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a12912f8-664d-3b9f-b855-b241f84bd338 | -6.0926 | -59.882198 | 2026-09-12 01:03:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6ad67b-19f2-3c63-b018-4d17d35d44e7 | -14.5746 | -52.658298 | 2026-09-12 01:03:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1412d3da-a570-343f-94f3-302ba3907063 | -15.966 | -52.712101 | 2026-09-12 01:03:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07ee7e1b-8933-377b-9464-9457ad832bd9 | -6.8643 | -55.639801 | 2026-09-12 01:03:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7c8dd6-5e44-34e1-b10b-60aa9c124054 | -9.5366 | -67.1492 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81a79a78-3d37-3e82-a2bf-0b4fc3a4e729 | -8.6481 | -66.489197 | 2026-09-12 01:03:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73cd389e-d196-3fa6-961e-244ba6c67422 | -15.9614 | -52.6945 | 2026-09-12 01:03:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0430f62-bc4f-3bd5-ae01-496197bf8388 | -8.0923 | -54.778099 | 2026-09-12 01:03:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9724bbf8-ea49-3790-b61a-6da31021dac6 | -10.6653 | -54.155701 | 2026-09-12 01:03:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ebc7d72-af8c-32a4-bb13-086e9fc39792 | -14.5551 | -52.6236 | 2026-09-12 01:03:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
