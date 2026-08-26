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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad6133e7-bb5e-317c-8ac9-7eb7bdb82de5 | -4.59545 | -56.05616 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 366e07b8-a710-33e9-8995-3ecc3b8a497b | -6.12742 | -57.82343 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2e3bc6ab-66ab-3094-a058-b777b9d498da | -8.61007 | -50.01733 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aec4e981-f74d-3c70-aedf-495c0732eed2 | -7.50972 | -55.58621 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e46f125c-20e1-328e-8901-10f9d6dda818 | -9.44932 | -51.58046 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ec4ee92-065c-305f-aaa5-efb11a1ba099 | -6.14339 | -57.70224 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00776d84-de14-348a-b972-81a4cf2a6e5c | -7.32234 | -42.97426 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eacceb02-7ce3-3b0d-b53e-b05d9551183d | -6.99672 | -59.27417 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 617e4117-90a9-37b9-af1a-3e91258da0c8 | -6.15145 | -57.70345 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4645e703-9702-3967-a830-fa3723472d6d | -6.13137 | -57.84985 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bda1150d-ae03-3167-a9a3-2c05bcfad29e | -7.26177 | -49.85817 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f795ab2-cff0-3f2a-921f-4c493cb21e42 | -7.02959 | -59.23984 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60c3dfef-b1c6-399a-b48f-377aebaaa3c3 | -7.3749 | -55.17954 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5bbd21e-919c-3023-89dc-d21853a1d121 | -8.16076 | -54.98394 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 90318d33-e4c4-3bff-911f-26049833c5db | -8.99284 | -52.38793 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bea5edc-b5f8-3cab-8cb5-46d8900b50f3 | -6.5458 | -58.51817 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd9aa3d9-ce4f-3201-8d10-5dd8f58308c3 | -7.78518 | -61.56173 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf3fbde6-9e80-3b54-bd1c-d141ed4c005e | -6.20232 | -55.64317 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96a9aa0c-8d13-3a29-a433-1f9288467de6 | -8.12254 | -47.46166 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f3e6a3e-8b57-323d-9f08-7366a44d9de0 | -5.77141 | -46.11438 | 2026-08-26 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b5e1bcc-b354-3d25-9fae-3bce9209fbc4 | -7.1123 | -56.56036 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efba4472-31cd-3cb8-918c-fe2fdd611427 | -5.65898 | -46.94888 | 2026-08-26 04:51:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d13c6a3-6f1d-3251-b6b2-a3d60a389c07 | -8.08646 | -47.49733 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f61a838-296d-3ced-b630-41add3573ff9 | -6.63726 | -58.51791 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 242dc34d-3505-3cfe-afd8-60dfda71a180 | -5.17326 | -44.60973 | 2026-08-26 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd970a8d-341d-3e05-9dcc-71d3cbd8c263 | -3.54464 | -48.18035 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3d7cd376-0bf7-356c-954a-cae856667e04 | -6.51635 | -55.22679 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 517daa9a-526a-366b-92f7-bd6b56b68e5e | -6.14742 | -57.70285 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff6d7ab0-56a1-3f0f-84e1-d817740d71ce | -2.79229 | -49.58361 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f3c381c-0e8d-3b05-ab69-4506c5b6b76c | -8.01567 | -51.81929 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db817791-0ed2-31c0-8f90-0c144a1ee494 | -6.58228 | -55.44582 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6869a4d-0a27-387d-8f3f-e64ddec1f319 | -7.3166 | -61.14804 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a89a7aa-af63-30a9-a85e-2a9eb5d15c9a | -8.58892 | -54.70285 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b39a14f0-2b06-3374-b3fb-d4745b37336c | -6.91406 | -44.66663 | 2026-08-26 04:51:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a550f5b-8deb-3f8d-8d43-48e701ead9bb | -6.26118 | -53.37936 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97ed001f-b965-3508-9882-923d9148ab2b | -6.75105 | -56.33522 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29299783-1ba6-360d-9e91-e1f415155afc | -9.44826 | -51.67896 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f5ae4a0-f3e1-3d2e-93e1-9b8e83b80ea4 | -6.13208 | -44.07035 | 2026-08-26 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6faac85d-3ef3-3d84-aa2e-79c6660e3d87 | -6.20153 | -53.08894 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bad31238-3fab-3318-8234-b3b20b6b70fe | -7.31999 | -42.97391 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 42407e98-436b-3e6a-baf5-56f3dd2cb1e4 | -4.33578 | -49.80072 | 2026-08-26 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2574ff6-17cc-3a79-b3b0-56937d6c2b61 | -8.76931 | -49.95612 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71bc1f12-9aa7-3771-b919-1e086b6e5564 | -7.52727 | -55.58908 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ccc9d7e-308c-3dde-8edc-fd3c1c96bda4 | -6.1187 | -57.82574 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ce73b3d7-9d17-329a-8425-b6046dc9b85d | -6.55042 | -55.14892 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f924489-b08f-3917-8a7f-9690c3d6f1f8 | -6.51222 | -55.23011 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a763338-a3ae-3a77-a246-fa1d9f307f22 | -6.16508 | -53.49302 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba80ba2-9ac8-3a93-9e52-e0e95a3ae2cf | -6.32233 | -44.84853 | 2026-08-26 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d272800f-0d26-3025-99c3-2237cf7465a5 | -5.34069 | -45.15981 | 2026-08-26 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d82361fc-3172-3e65-9440-ee182496acf1 | -6.247 | -55.431 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83faae8c-7486-33af-ad9e-e4e0cdb69f34 | -5.94631 | -57.73036 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c75584bc-1693-344f-a236-26c43df3094b | -8.51966 | -55.35237 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c0e70e0-fc6f-3910-aa4f-e76e53830a1f | -6.28439 | -53.36157 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6ef32fd-6bd2-3ab5-ae10-6eae9ddc2778 | -9.59534 | -45.99518 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54619458-93a0-3b40-9c8a-e7f8caf598d6 | -7.52196 | -61.38486 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| cbb1ce70-b1e0-36e3-8ed1-e612493e1bad | -4.80874 | -45.77126 | 2026-08-26 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23db49f5-caf8-3fbb-a688-a9ea1e282da1 | -6.88909 | -43.74778 | 2026-08-26 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 502f25f7-b99d-3a27-a408-b52b73ba346a | -9.5695 | -49.26628 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebe9a8fb-a55b-33aa-a1b5-43bc125a7d83 | -6.88378 | -43.74699 | 2026-08-26 04:51:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50220910-70ec-351a-b387-aa25fcb1e836 | -7.16388 | -42.7998 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 849f3440-e2d6-3701-be07-5edb35390684 | -9.41586 | -51.61708 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b2d8969-66de-37dd-a729-1c2cd4d8268d | -6.2294 | -55.47329 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7f89549-5d71-389e-a224-e6517562cd68 | -8.61919 | -54.73002 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79d57fe3-5645-3b43-8a6b-29f7f5807fe3 | -6.80617 | -59.59576 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a36e6221-7f5f-30ce-9275-6f4b22595a85 | -6.1475 | -59.92572 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b8f363a1-6526-3a7e-8e7d-c1f1935a8d3d | -5.78403 | -50.18542 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8abf4863-210c-3f18-bc5d-6a0053a55c43 | -2.89063 | -48.80622 | 2026-08-26 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6147eeb1-790d-3cb2-aa83-b9bb3d080394 | -6.68155 | -56.34811 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7629b26d-ec42-39c3-9b14-597c77c9e4eb | -7.39218 | -55.15443 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e73525c-be9f-3d1d-b7ed-3ad5d2a58b62 | -7.29229 | -44.09038 | 2026-08-26 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3e43ef2-7554-3032-a531-2d818f216e44 | -3.77888 | -59.28158 | 2026-08-26 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98cb91be-dee3-3aef-9bd3-bd9244de686c | -6.15932 | -57.80655 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b28d1793-ad30-3c8d-85a4-e2d7a01a3c63 | -6.84276 | -59.46213 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4afd89cf-d6a6-3c5e-bd78-9240b486e14b | -6.62575 | -58.48401 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6785fcd-e5ed-379c-91fa-bb791835203f | -7.26782 | -49.86688 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eb4b2d27-4ca9-31ae-b185-2f36c7722fda | -6.50534 | -53.25436 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75d96444-9acc-393f-8447-909bb9411ffb | -5.56296 | -50.4912 | 2026-08-26 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8b3de9-713f-3f4a-8ddd-eb84a566d326 | -7.40132 | -55.16359 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5bbe6ff-1a0c-3e71-aef1-b0f8f614d3d4 | -4.19245 | -54.57591 | 2026-08-26 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9896d001-f927-3467-a510-1f85b677a8c6 | -6.15126 | -53.68872 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3a93368-d382-3c94-a30b-b9093839b0f1 | -7.37502 | -55.19447 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a454381b-6683-37a8-8abe-59c513098f37 | -6.83386 | -52.50135 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb756ee4-211d-3fd6-9bad-bcacdf53f7eb | -6.84048 | -52.50236 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae18b645-a8d6-33aa-80a6-e62a9ffaf0a2 | -9.57019 | -49.26154 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d20660f-f05c-30fa-a957-4d82fa257172 | -2.72001 | -48.80261 | 2026-08-26 04:51:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f8a59a8-b9c0-3d8c-bc6f-ab809063f89f | -8.16317 | -54.9688 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc4c4013-29c9-359f-834c-d9a621a43aad | -6.23231 | -55.47783 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91ea426f-8765-3f6f-ae4f-c10c502d2c34 | -5.77058 | -57.55256 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f18707aa-d1fa-3e49-bda2-ddeefd906a68 | -6.25287 | -53.36736 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a72ec61-ac72-30b1-a3a8-858bd4a7c80a | -8.53402 | -55.35093 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f1fb1e6-3aa9-3068-9c94-d0e0c8889188 | -6.8394 | -52.5093 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 562dd74c-76d2-3293-88ad-ee557fa39c9b | -6.27114 | -53.38092 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f43988d0-9fbb-38ab-afac-5cc6d6da3e04 | -6.14475 | -57.8446 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37d9c545-b8cb-3b8d-a6a6-77f0b55cb749 | -9.44192 | -51.58319 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecea40a6-0a3d-3c1d-8dd8-f6a0fa6521ab | -7.83017 | -51.37181 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3b2cb0d-f09a-3fef-bb51-37f12814a864 | -6.53952 | -55.08415 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c94cdf9a-cf39-3e61-b8cb-11e8a86ad5b7 | -6.17612 | -57.70405 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cb651b1-4682-3048-a8ff-29a76b3ff749 | -9.51771 | -51.68558 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbe6a32e-a63e-3934-a83a-0ae41866c81a | -6.95633 | -59.08868 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef9d8701-e3f8-3f66-b58f-8c5cd5e6868e | -6.63483 | -58.48145 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README36.md)
