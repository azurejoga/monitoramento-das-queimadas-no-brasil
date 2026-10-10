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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db7d6312-bbdf-336d-bceb-615174c143f1 | -2.92601 | -54.079 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5205f93b-aac4-3c23-b46b-bcfa45c6e85d | -3.95151 | -55.33619 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c18467-4ede-3ab9-9ce9-1dab96b57bfb | -6.77082 | -48.66967 | 2026-10-10 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c58d7127-9438-3822-8572-a9533fc04219 | -5.96605 | -55.36638 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cab90729-55cb-31bf-a527-4f658272797b | -3.86688 | -55.96819 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d38acdf-cfa2-39d7-9bc1-a18f5e450166 | -6.36802 | -55.16744 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b23b70-3b59-3d4e-a39e-3a14504a9187 | -5.18703 | -60.31216 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c23dddc2-93ae-3b71-9a9f-27c2065f9d7d | -2.93372 | -54.07314 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbaaf3ba-7f4a-3d2f-b562-bab15427595c | -3.51587 | -59.94527 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb25bfa-ce93-3a17-b82e-2cd67db069b2 | -7.24001 | -44.16442 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 085ce24f-4571-36a8-925d-9f6adff97249 | -6.25363 | -52.85946 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27f51cf6-b25c-371a-af99-610f7c8b492f | -4.81587 | -56.08528 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c6dbac5-2a23-3e06-8a05-25f059192bad | -2.89343 | -54.07034 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7982cc6-2ba7-37ae-be51-51313db9044c | -2.01998 | -61.27047 | 2026-10-10 05:04:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15d449b1-680a-3ba8-a740-4dade06cd851 | -2.95112 | -51.97706 | 2026-10-10 05:04:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2326d4b3-92b4-361c-9efa-3a32733080a5 | -5.08447 | -60.22251 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2de8fe02-73a4-3f0f-8d2d-e3e7b574626d | -5.04334 | -49.35112 | 2026-10-10 05:04:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41e60988-c44f-3f77-a632-164ff85f352b | -2.93038 | -54.05139 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9d3365d-1aa8-30c0-9666-45f9ad692200 | -2.65551 | -57.42756 | 2026-10-10 05:04:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbcc7795-b47a-3741-af05-2a7b6668b5a8 | -3.47091 | -59.254 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a541916f-6073-34ae-8832-9166f482a03e | -7.18117 | -52.61756 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2f8d71a-145f-3121-8258-c925f003af44 | -1.21642 | -55.66093 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 448a3fbe-9785-3f48-95d2-dcdc55a955d9 | 0.22929 | -60.38449 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a43e93a2-5b53-3e8c-9614-a62c8e173c86 | -2.43647 | -55.98454 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7c62432-a6bc-33c2-8a61-14f3c7d5dcae | -6.25231 | -55.44426 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcae3a22-2d2d-3808-9d05-be120052ac34 | -3.84963 | -55.79343 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45e857dc-ce16-33e9-9001-74888f56e5b0 | -3.57897 | -51.49569 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83546e72-9c69-31ac-9eb1-5527cdbcf439 | -4.84928 | -42.83082 | 2026-10-10 05:04:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| e01fafa6-8f2a-35d1-9b56-f3855fe63c30 | -9.0043 | -44.37405 | 2026-10-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69d96fa3-5ed9-37af-8d21-42e09a11b500 | -3.19039 | -58.65133 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c75b1f7c-c65e-322c-8444-c84e74f13665 | -3.31128 | -53.83644 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2172d72-f6c5-3977-b254-301d7175838b | -3.2505 | -50.41617 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad2afe44-ccd8-387b-8588-47e93857d156 | -3.2637 | -54.6922 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de217961-3685-371c-99dd-1375c73c591b | -5.07215 | -60.21614 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a94f0c01-a46a-3ba8-8e6f-6a70bf3f34ac | -4.12821 | -50.83948 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 959fd5f4-21ca-3dd9-8033-0afd3dec0644 | -3.01145 | -54.73885 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 598e4dff-d54d-3a0b-8bde-b84c3621709e | -9.00992 | -44.36996 | 2026-10-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 689a780f-b566-3400-a6f9-b044558e9e00 | -3.43748 | -57.88671 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77f0d9b3-cb94-329a-b693-7a40c5386ef5 | -2.97457 | -54.07257 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 169116ee-eb22-3986-bf4e-e5b52ced1ec6 | -2.88525 | -54.16467 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99b5a30e-8b37-3218-8e27-52d8ed7ce069 | -2.97898 | -54.06618 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b657336f-0269-3da2-8a7a-848630ded613 | -6.99873 | -47.72041 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9692a89-3cf3-3389-beae-a3f6bd71ddbc | -3.57911 | -54.69482 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c035a817-d3f5-380b-b64d-e932b665fb5a | -3.00654 | -54.04223 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c157bdb4-0545-3966-85aa-f43adc88c5b4 | -2.86261 | -54.17883 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a46d168c-8dc9-3a16-a6ba-847760803a8d | -3.86971 | -55.97254 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42a39758-0222-38df-b864-404db4e95443 | -3.57744 | -54.70535 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65f50fd8-04d6-3a99-a08e-239c79cdaa38 | -7.02821 | -47.67705 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3c60c9f-2e33-3f79-9528-f63f9eac561e | -4.15709 | -55.14071 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42fff2eb-0375-3741-8f60-0927dbf0cd58 | -5.18336 | -60.30722 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 577fe1f2-7a6e-3c6e-ba58-2542bf385a85 | -3.18177 | -54.75499 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fc21966-7bd0-3d45-9e01-782c03a4595b | -3.73686 | -54.64105 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41ef7326-85d1-38bc-8b65-1cc3676dde0e | -2.95929 | -51.49576 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fde6a859-b045-358f-9f03-b547c77943d0 | -4.89497 | -54.98657 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cc528bf-2585-3d53-ab3d-6479b8dd7641 | -3.99175 | -59.35682 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21ee69db-3a53-3945-a7f3-c43d24a9d82a | -1.88166 | -54.68146 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53f455fd-e122-3777-b6c3-268891d63e57 | -2.58461 | -56.18828 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 355bc831-93e6-3b65-94d0-e4f8434ede9d | -6.92291 | -59.27311 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f320ffec-8c58-3d86-a4d2-49d6fc5ccb2d | -6.43963 | -55.0607 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a6ee29fa-6847-3940-9220-528886fd263e | -3.59928 | -59.42406 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e853cdc6-4572-3b07-b8f9-9639b52a7f9f | -3.48786 | -59.20253 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aede2a9c-55a8-3581-8b6d-3cd9315d7347 | -2.39242 | -51.2923 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 090c0edf-2d8b-31a8-9172-e9904db92711 | -3.56856 | -54.69674 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a2178ef-6280-3ab7-a5c4-884c86b88997 | -5.93542 | -57.73604 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17815c27-5cd4-39de-a5c6-1fe5ad60d593 | -4.38485 | -55.16228 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72c9301a-6328-3567-8683-0da12e0b7d65 | -2.57196 | -57.78364 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d000cc24-60a9-3fec-b4de-91d863b487e8 | -3.95711 | -55.34447 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8a953df-191d-3072-b2cc-538531a39dc0 | -3.16617 | -50.59084 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6039b743-9202-3b80-83c6-c205c2bf679e | -3.55522 | -54.69461 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93287f81-4b8b-3501-af72-e4fb56335cc1 | -2.944 | -51.41247 | 2026-10-10 05:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f80a8b-c28c-30f4-8305-a18569177b57 | -2.78454 | -54.02806 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec0a7b9-7f6d-3e7a-94d5-9d70641868eb | -3.00271 | -54.06638 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6d84806-dade-34bb-8793-d764a08baf26 | -5.89595 | -57.7266 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a9f9e5e-375a-3eca-81b6-3e49519f2404 | -1.11391 | -54.17038 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a909cfb5-ce56-33bd-bef8-7df7fae06758 | -3.11896 | -54.16936 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94ad2ed5-3819-3fbf-b60c-59ab267f48ef | -1.10653 | -57.27471 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae87edc6-053e-30e8-9556-81573a1a0b75 | -2.80366 | -58.26765 | 2026-10-10 05:04:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 662a7af3-26aa-3535-89e4-697836d357fc | -2.73289 | -54.90618 | 2026-10-10 05:04:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d608597f-263d-3a16-a7d5-f7cff843ca8f | -3.08065 | -53.94067 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 328e7f87-78af-3c35-b6ad-a995025724b7 | -6.80232 | -52.77976 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98f0982c-31e6-3879-93e7-433c59870fa4 | -7.17455 | -55.16071 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 741b722c-042c-3871-8ea5-e95c1a83cedf | -3.54701 | -56.84969 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e63ca2c6-b21c-34d3-b7e4-c2bf4be265c4 | -1.30442 | -54.18949 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c1bcb2-2eac-3f33-8295-07683073588d | -3.10685 | -53.77565 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10380040-f308-3cbf-a7ea-e64628cbc0d5 | -3.67805 | -54.49969 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 598d8b0e-f98e-3362-a3a6-f5948589257f | -3.7969 | -55.88084 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4f9cbcb-22e9-3966-a46c-26b46e13c361 | -3.03363 | -54.08538 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172ae3bc-adfd-3563-8c0b-b43003ad2c47 | -2.88582 | -54.1825 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be53cf63-99f6-335d-b041-21be143b93f0 | -3.68439 | -58.86629 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e971279e-3a17-32df-8ca3-e81729a1cfa3 | -2.83054 | -54.12417 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eaed3a6-7fed-3f4b-96bf-9ee778b86340 | -6.03256 | -55.35148 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5226487a-bfb3-3537-82b1-54cf576ee3f3 | -2.3496 | -54.75524 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4268ae1-8485-37b8-ab98-1d3ee681e454 | -3.20469 | -53.86509 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d26c22-d73e-37d7-91be-caf069eb9d7c | -7.18855 | -52.63768 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06a2dcb0-2304-3b65-a804-8ebeb0e4bfe9 | -3.34104 | -50.4114 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bb306aa-25f8-3387-8943-30a0370783b1 | -3.18959 | -50.54721 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45c1b9a2-e97b-3eef-ac78-7173b7efe790 | -1.32468 | -55.35388 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77bf155f-d7ab-336c-bdc1-40657aaf4a70 | -7.23101 | -55.14795 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2edce134-7c4d-3523-a4af-e8b4c984941c | -6.55202 | -61.41267 | 2026-10-10 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99bd57a5-ddbf-3dfe-9b0a-7179d3f17ee3 | -3.75687 | -58.50834 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README108.md)
