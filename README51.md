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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4885db6e-e877-3599-a3e5-39a2a9cd873c | -8.89583 | -46.6878 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c8cf2fe-4b76-311f-89b5-dad722dfa3fd | -6.46101 | -44.57821 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a2a8b034-5a1d-3672-b6bf-62e97f294afa | -6.36253 | -42.87945 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ca8ad7a7-3c92-3400-b10f-50cbdf5609fc | -7.69885 | -42.58886 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 982557d9-d74e-3b0c-b4db-540be964fd15 | -7.61109 | -45.46676 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b5cf33a-db52-3ce0-9555-10969e3c6046 | -4.87665 | -45.07896 | 2025-10-05 03:53:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82498eb9-30ea-3b43-acb2-16af94de0b32 | -5.92054 | -43.32629 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfd22b13-2382-3f5d-8200-d2950231bea0 | -5.93215 | -43.33197 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ddc91d3c-6427-317a-abc7-89178bc98ece | -9.28193 | -45.66443 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a6998e4-4b91-3bd0-8daf-6fa18f7eeb61 | -5.84215 | -42.89178 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0bb409b0-1f5c-3f73-9136-7f2e34b03792 | -6.3496 | -43.91459 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 283e1bbe-eefc-30dd-bf60-365cf0002f54 | -7.23987 | -44.88382 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 953727b8-11b0-3ab8-ab57-93871eb5e51f | -9.95712 | -43.76991 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ff13c3e-fe50-33a6-b221-47a20a1529a8 | -7.50031 | -37.79465 | 2025-10-05 03:53:00 | NOAA-20 | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6ceac4f0-7e76-3219-8e7c-ac61fc69a89c | -5.12484 | -46.2402 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 243aa49b-dbfd-3f09-a27a-d90c039fe00a | -9.15364 | -50.0652 | 2025-10-05 03:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 24474152-91a5-3ec8-b258-b5a2a8439a2c | -7.46021 | -47.17771 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e17256fe-c48a-31b9-bad9-79aa3a69325a | -6.66172 | -41.59092 | 2025-10-05 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0eebc676-8e55-327f-88b1-c6eebc2ed612 | -10.39253 | -45.4127 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 562d936f-db8c-3337-affe-75498b3858f3 | -7.37715 | -39.19934 | 2025-10-05 03:53:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e4b36196-10c3-3017-a56d-974538d22344 | -9.32432 | -45.77497 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27638cc9-b99e-3c6b-b233-2ec5be883039 | -8.59066 | -46.29709 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 97bcf940-588a-33ec-b3a0-35cc2f8aac91 | -6.3491 | -41.62354 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3460791-9ce3-3439-9695-bc016bebd395 | -10.64382 | -46.30653 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4fc155b-d7ff-3b86-ab44-04b3d6912aeb | -10.71964 | -41.34596 | 2025-10-05 03:53:00 | NOAA-20 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea6833af-d2b4-3a86-90ac-18c55b963aa4 | -9.72878 | -45.20417 | 2025-10-05 03:53:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc1a2b49-7178-3318-8522-9008bb1b5fe3 | -6.29451 | -44.44266 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12b1e22a-3354-3889-9b17-8092dfbf8d05 | -5.81687 | -43.72941 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc3c6fad-2e28-38f7-8443-b45e10c10778 | -6.26727 | -42.44277 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fa78438e-14a0-3b01-88fa-3e2e7feacd3e | -5.46118 | -43.15423 | 2025-10-05 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2400b3a-de78-3d54-905f-5a4e11370e1e | -5.36471 | -45.95522 | 2025-10-05 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1038e5ff-1e62-347b-b916-a02d21be41c3 | -6.16088 | -44.66953 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 70584444-64b0-3267-8465-b32a6589e28b | -6.35935 | -41.62973 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a4a47ae-1c9d-3096-b607-98b64766c95c | -8.18695 | -44.13906 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e35cab6b-34f5-3f00-9dc4-0a4edd548c03 | -7.34752 | -45.22242 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 190b9261-24be-3737-9eb8-3916ae5ad565 | -8.86285 | -46.81761 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a6710504-da2e-3ada-a8f5-caf82d4a5c55 | -5.77808 | -42.9332 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| cfc2a34b-924e-323d-a751-312f74da6523 | -5.22904 | -49.07297 | 2025-10-05 03:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa32d0cf-3f88-3413-b30b-3fb65fe6ca17 | -6.14394 | -44.63509 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5d109ba-074d-30d7-ab4c-08aef924a35d | -6.36645 | -42.88018 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 986e0d5e-c3fe-36a0-9b5c-dd503df37aa8 | -8.89559 | -46.04374 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31ba53a6-1a9b-3e79-b2e6-deb53a3cc502 | -7.93341 | -39.88456 | 2025-10-05 03:53:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4d57080-299b-32b8-a868-2975346c8b56 | -10.1876 | -46.72832 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c37670d7-c688-390c-b65c-373bbd2ecbde | -6.34109 | -41.62658 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c300e0c9-8877-3e20-ad01-ea4a78b28ca1 | -7.73106 | -46.31686 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ccb53a1e-251a-322d-ac9e-a0966debd743 | -5.464 | -42.79128 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9c89e81-1494-325c-81ef-022c68e9ffa7 | -6.25961 | -42.7725 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6293652a-83c0-35ba-aa00-ac2ee4b1044c | -8.5489 | -46.31 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f530495-e669-3f93-ba2e-c494a18583e7 | -8.60206 | -46.2882 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 72ea73e1-1206-32fe-9487-83595b3d9287 | -10.40049 | -45.39302 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6adac81-e83a-3699-a2d6-3397bcf55e7c | -7.51519 | -41.27514 | 2025-10-05 03:53:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2f5f5703-c741-308f-a21d-dc0484eb369b | -7.46979 | -43.04063 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1310548d-2cc0-3c33-8bf8-ec260d0aa115 | -6.03194 | -44.23104 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52198cc8-bf1e-397b-80d7-b0cde877d9a3 | -3.60532 | -51.04536 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8656ec5-57ba-3033-a5ae-d05d3a851a8a | -6.83918 | -45.48686 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df051c02-560d-3913-87c6-345added5045 | -7.42477 | -46.50207 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82bc2e01-395f-3aa5-9c5d-c9e8d05fe860 | -6.32131 | -41.63264 | 2025-10-05 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8268ae41-04ed-3649-8875-5be118f3c184 | -6.26939 | -42.44101 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f1e4551f-f2d9-37e8-958a-a014c7b94f6c | -5.90101 | -44.73379 | 2025-10-05 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53599443-3b02-3d91-9599-a9c8b349897c | -6.40587 | -43.04971 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| dfe39eaf-95de-3efd-8805-02655fbe5473 | -9.9535 | -43.77268 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b7e2d362-545f-36f6-a32d-f69686301ee9 | -6.70376 | -42.15521 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 00d41f36-c0fe-34aa-82fe-d2da1a6be579 | -5.40656 | -41.33784 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5e955544-35cd-383b-b8ac-5bf8a03fabd6 | -9.31091 | -45.66742 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85643bf7-8389-3577-b0ca-84a9357fca5d | -10.35116 | -48.15973 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 786dcfad-a8ba-36fa-8d20-281e9fe15c6e | -7.52359 | -41.26825 | 2025-10-05 03:53:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba9cbed3-4d73-38fe-b5e5-03e46c3747fc | -6.29225 | -44.05042 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2155b952-02a4-3205-be2d-bd1ea9c784b6 | -5.77881 | -42.92884 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 99f1470d-b8d6-3d4a-b6c1-15e0b5dc86a3 | -5.9884 | -44.35645 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cd27278-076a-388a-98e4-60f7cade961a | -6.19838 | -39.70385 | 2025-10-05 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 72698c07-da2f-39cb-ad9a-0a35441735c0 | -7.60602 | -45.46919 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 025007d9-f426-3205-8a27-90818a436156 | -5.83645 | -44.45355 | 2025-10-05 03:53:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a00952e5-7828-3424-900c-8031fb2a8ffd | -5.78604 | -42.93457 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 41.5 |
| 02dfd041-4a41-3173-b16f-140dac0e2e3f | -8.33715 | -49.4975 | 2025-10-05 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db9522e-80e7-3509-9817-744a04e6e2a1 | -10.29851 | -47.94521 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca342a07-1cd4-30e0-aeca-a40b2c3b79aa | -8.57462 | -46.33186 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 96b113e8-6041-3cbf-a151-27736bb9ca7f | -5.77472 | -45.74784 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0ba6dd6-3192-302f-98de-258698521d3c | -7.22346 | -42.18156 | 2025-10-05 03:53:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0e5a9c33-79e3-3a61-ac15-2f94b89d9c41 | -5.28938 | -43.10812 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82e633c6-05c5-3a59-aa5a-d3ead17818ee | -5.93682 | -42.87755 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ab6ee4d1-8b6d-3f64-b0a7-75b543e579f5 | -5.91759 | -42.89528 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d82b80a2-9910-335a-b957-f7447de82883 | -6.65516 | -41.58543 | 2025-10-05 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7a554d94-b220-3173-a4cb-e9e9b23da5b6 | -7.74979 | -42.51651 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 69a95827-793d-30cc-b9f6-767ca201494b | -7.04166 | -42.76191 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ddeb51cc-e41b-3de2-80d4-f81c66fd8270 | -9.95228 | -43.77432 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02121efe-2ad6-3d43-a9b7-0bb692d25f41 | -9.06396 | -47.01881 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acf51a39-eeb5-3a42-b254-d75ff50dbd5d | -5.48615 | -43.40242 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d37d712-0bac-3a6b-b553-3442d1f232dc | -8.86097 | -46.85693 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 17c64c29-6651-3e9c-9d68-f3b981a914c0 | -6.98387 | -44.21738 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 53681ad9-44fe-3139-9b93-d77ef30bf07d | -7.31567 | -45.9926 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dff86718-d6ca-3313-9a15-962ab96fdb90 | -7.16005 | -46.09134 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 83d79bee-19bb-3e19-baf8-d992d14bc52a | -5.31839 | -42.65432 | 2025-10-05 03:53:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efba32bd-ccad-311b-9f2f-4ec4aa96ac90 | -9.91027 | -45.95467 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 88cce8ff-d135-38a4-b040-a5e7ebacfa37 | -5.53783 | -45.14972 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea478357-d201-3c58-b583-b6b5bc6dd3c2 | -6.67022 | -42.38177 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f6f5e32-99f8-3942-b214-5323605a27c8 | -7.48387 | -43.0289 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a3a0015c-a897-3e63-9ed5-b6ce045be0b8 | -6.43365 | -46.02728 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95d75546-455b-3df9-b439-e251e5013684 | -5.69052 | -43.02949 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d91dae6-d534-3e6d-adfb-0714543962b3 | -6.96831 | -41.34058 | 2025-10-05 03:53:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 62a30fd2-ff35-3f01-a8c2-67c25bc7b613 | -6.14319 | -44.66603 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |


[Clique aqui para ver as próximas entradas](README52.md)
