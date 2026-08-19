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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4fd8c15-9493-3c20-8bc2-e7eafcf305cb | -7.30507 | -44.56744 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1ebe2fb-0119-33f4-8b73-14180b5cbc18 | -5.9124 | -43.617 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39463ff4-d49e-3618-ba80-5f3132a40b50 | -6.40822 | -54.9381 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea2ab8f-8ddc-3362-8b7f-a395a437456e | -3.97903 | -49.19691 | 2026-08-19 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13eeba75-0de5-3c9e-99ec-51bce5335d13 | -5.42276 | -48.41156 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de843ced-b94a-3bef-aa94-b8e692619976 | -5.91553 | -43.62241 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a01a6dbd-7b19-30b3-8bb7-05153486f6af | -6.14545 | -57.86467 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29814c7a-b647-32f1-855d-a41ef282fa97 | -6.88255 | -59.05854 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db284eb4-9dda-310e-8a7e-8714db867d30 | -6.75186 | -59.17059 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6d14cf4-5fd3-3cbd-9f54-f8673a233b9b | -6.16131 | -47.76032 | 2026-08-19 04:38:00 | NOAA-20 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d10362c2-4f9f-334c-8e41-a42a2f60d765 | -6.64453 | -56.35064 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb6af0a6-7582-3513-89d8-77839080bc60 | -6.64502 | -56.34788 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ed8f1c8-d921-36fe-bd9c-0f5cb16e7923 | -6.68259 | -59.07619 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac01173-81fd-302e-b1a7-9a33b94ffafc | -8.09688 | -51.6591 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e0426021-c5c6-3d93-99e3-481864e57a5c | -3.09884 | -61.22397 | 2026-08-19 04:38:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff4f25d7-a7e6-355b-a4b9-bc52cf3c8bc0 | -3.2681 | -49.51937 | 2026-08-19 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aafe5adb-88e3-3052-9020-1d5eea560ac3 | -3.66151 | -48.96875 | 2026-08-19 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc3719b6-d2f4-328a-af80-57a9da29bdd6 | -6.13917 | -57.86755 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b1dc7c2-0d2a-3fb1-a7bd-eb132edd4c16 | -6.34533 | -54.91999 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 355de25b-db71-315c-ad70-e26757cccb21 | -3.27155 | -49.51993 | 2026-08-19 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85c2d711-6421-3589-8c1d-83200ff64fa9 | -6.00229 | -57.84661 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79417076-c17a-3fe2-ad82-5b7b3344bd18 | -4.01023 | -48.0628 | 2026-08-19 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88b689b4-44d2-3c93-bfd9-b32f64a2d047 | -8.1048 | -51.65617 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55c8e767-8090-3d39-9d6b-85c7627e81c8 | -7.17697 | -43.10664 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5b2d21d-e5a1-358f-8467-e556b2f5ecc2 | -7.05352 | -59.83821 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2d35d65-2395-3e2a-8110-af3cb70840fe | -5.71008 | -46.02879 | 2026-08-19 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ae270b1-fc35-3b33-b3e3-9929af2087f7 | -5.42884 | -48.41607 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| dd80e377-7d32-376a-8a18-9b6801dc04bd | -6.80688 | -59.46094 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42fd9ed0-fe56-3769-bf22-77d32b917ec7 | -6.30588 | -55.71125 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02e38eb6-0e66-30cb-be9c-c0013bb85244 | -6.95269 | -59.04416 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71b83f9c-dd95-372d-81b1-506df13f4e96 | -3.30855 | -48.80235 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d20fbeae-b489-32aa-a002-30512aaf02c3 | -4.00415 | -48.05832 | 2026-08-19 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc751734-4b47-3c4f-815b-31c64b5f1c6b | -6.34467 | -54.89593 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2797bb8-f132-3ca7-a2e5-000ee8646d4d | -8.04247 | -50.10247 | 2026-08-19 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5560d3ec-0388-3437-bd98-e660e3935d4f | -6.75706 | -59.15475 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10f9b8e5-8565-343f-ae42-56979b14d378 | -6.70416 | -58.94101 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16d51a4e-f1b5-3a24-b147-f99dc3299847 | -5.92252 | -43.62836 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f200bc81-66c6-377d-9bf3-4f0ccdd44970 | -6.03666 | -57.80636 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844e1d82-0deb-3227-9e2b-53847b6a1bae | -5.73523 | -51.70452 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7077f641-7d20-3e29-a7e4-ef1427cd7288 | -3.68869 | -47.64776 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4582c8f-c49f-309c-b534-39faf2897247 | -6.89175 | -59.04222 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da4ffc8c-252b-3451-80c1-e2cf65b1b358 | -6.79554 | -59.454 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58f2b7db-c98c-30d7-a71b-49867feb83c6 | -6.33703 | -54.91359 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0fac169-121d-3fe7-9a6d-e152b1d3c85a | -3.67768 | -47.65308 | 2026-08-19 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 882dd8dc-12ef-38e9-ad82-e9dbd9a06bf0 | -6.06806 | -45.36095 | 2026-08-19 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18d2926f-e763-37ae-a756-ebc7584f0179 | -5.91931 | -49.25891 | 2026-08-19 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cbad98f-3fe3-3bf5-9444-770ab16afafd | -6.75465 | -59.16761 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f8b5bea-d2f9-359e-8dcf-c70cea49e5bd | -6.99252 | -59.04656 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd04e7fa-2b3b-3cb9-b7a8-9df74c286928 | -5.37047 | -47.47606 | 2026-08-19 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfa9dd66-7998-3ffb-85cc-cf04e814fd88 | -5.91626 | -43.61757 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51e3e980-d264-3d91-9b09-774edfd43d74 | -7.55063 | -55.57087 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 169eab70-77a0-3d55-9890-587279167cac | -6.27676 | -55.97231 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2fa2e0e-4638-3ff1-aa8e-0506df8a2dad | -3.09295 | -61.2156 | 2026-08-19 04:38:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 07fdddfd-949d-3587-bd75-e5b18f688938 | -6.75545 | -59.16338 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae75525-6ce6-3170-b2aa-da19962dfdf1 | -6.74739 | -59.16104 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f0bd6e-f7b4-328c-9982-4f7806ad3418 | -6.69083 | -58.9472 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 01b03daf-27a3-322e-abb0-fecc88bdffe7 | -5.43879 | -48.41765 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f3e90f33-d98b-3fe6-b6b4-0eb9ae7a912f | -6.41117 | -54.94833 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de01c82c-6b0b-3517-ba33-fcd7795d12a5 | -6.44307 | -52.72349 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1784c740-b126-369c-aa77-765ad24854a3 | -6.13674 | -57.88988 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ab93730-2d72-37f1-bcc8-a5c280d15c61 | -5.99734 | -57.84209 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4031c406-462a-3514-a080-dd017f107413 | -7.05637 | -59.84723 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 614db579-765c-3356-8e6a-57d5aea8200d | -6.90613 | -43.25736 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7a6c41f-9893-35bc-8842-a63c7f450143 | -7.53954 | -55.57916 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d46c652-b2ed-3d72-9236-add0eecfba44 | -6.84428 | -59.01629 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f1a15e1-1b0f-3a4c-9e81-dfa88e50601c | -5.91482 | -43.62717 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 039c0378-5546-376f-9438-bc0b897a8b09 | -6.80746 | -59.45837 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e005e1ee-79a9-3eb4-8063-729a4098883f | -7.44967 | -45.14368 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 728ed7a7-9c9c-315c-b746-b64f7bff4f7a | -6.0793 | -57.92136 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7552c5e0-4325-3c2a-b914-77d67cee1924 | -7.21578 | -43.28934 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 047dae0d-54c5-3200-baaf-5cebb08e6550 | -6.39472 | -51.75119 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e6025d2c-6d4d-3124-8a7a-9130925cc284 | -7.94865 | -44.6344 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54a4e8c7-1352-36c6-a646-f9ca92b5c3bb | -6.33866 | -54.90662 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbf208ec-04bc-3678-8629-642b837755ab | -8.55837 | -47.41295 | 2026-08-19 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c57dea3e-d7a3-3ead-a6ed-6ddbd71e3153 | -6.09174 | -57.91636 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 62711200-fff0-33ae-b00e-1dcbd7b42397 | -7.53486 | -55.57838 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 56cbc187-b6ad-33f0-80ca-2942d842107c | -6.4476 | -52.74488 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58e07546-c577-302f-88ce-f765a4842481 | -7.45327 | -45.14423 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f23d40e-0939-3d07-bfe5-c39331971b60 | -6.14133 | -57.86352 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f240eacd-f2bd-3971-b08a-bfb34bc275f4 | -5.91816 | -49.26606 | 2026-08-19 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7e80d143-0925-333b-b4e2-4ad5611d0016 | -6.28936 | -43.63675 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc0a72a5-f48e-32b2-aaf0-24dc923c4f3a | -6.76174 | -59.15003 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 943da5c4-b2f7-3f31-92d3-b4c654f3788c | -6.75423 | -59.15743 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0ec886-3091-3e75-823c-f9b5db65a571 | -8.02451 | -54.00676 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77479e31-45b5-3ddc-a8f9-98d65230366f | -6.85018 | -59.01752 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 011cfa92-f665-3e77-98e6-2131f681cd61 | -6.13737 | -57.88626 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5067ca9d-f9f0-31b0-a5f0-1c7a86562b8a | -8.10772 | -51.66093 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c951d594-22c4-3416-bac6-6a7b3210c72f | -7.19889 | -43.26532 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 548211d8-5642-30dd-9b44-4d8a9d8d839e | -6.78332 | -59.45189 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a877baf9-93e3-380a-b459-7af3c8c5e1b6 | -6.33934 | -54.8998 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 39bb0e15-c979-3f50-9ba5-b766c3624fc3 | -5.9941 | -57.8604 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ef24f02-32fd-38df-96e9-e528595aa01a | -5.91874 | -49.26248 | 2026-08-19 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c3d4a20d-d1d8-322f-bb3b-eab7028e1951 | -6.88521 | -59.06115 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6269b8f-50dd-3a1e-a46b-9de977df935b | -6.75384 | -59.17198 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b324cbe-4513-38b1-8df5-2eb9ed3ffb90 | -6.4445 | -52.73918 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e56f1389-e1e0-3f5e-8f5b-9055746e6605 | -7.28275 | -44.07084 | 2026-08-19 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17bb5797-b84f-3db1-87e4-89aa0fd3927e | -6.00356 | -57.83941 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 774e9d2f-d111-373c-87b0-485f56c32e5d | -6.87653 | -59.04119 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc962efa-9a60-3dda-aa21-1dffe06455bb | -6.70263 | -58.94959 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29e7ab85-b3dc-370f-8934-d2b69c372d58 | -7.05262 | -59.84311 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README33.md)
