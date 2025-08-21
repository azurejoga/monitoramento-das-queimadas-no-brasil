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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a39d70f-63aa-3bc9-8ebc-a6350b2e168c | -9.87069 | -45.97683 | 2025-08-21 04:40:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fa7c251-966d-38bb-9ffa-027753eab7e7 | -15.93843 | -46.93266 | 2025-08-21 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01276b7a-7c3d-3614-9f16-cbc8b31e3d10 | -14.8529 | -47.93651 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e629346a-cb79-31ce-896d-47867124fed8 | -14.62195 | -54.87889 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1b95056-905b-35fe-95e2-18cf3947482e | -12.9563 | -46.21981 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9357dd5-d541-33b2-95a5-b9ab59d8abc0 | -8.84113 | -52.03892 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25d91538-2205-369c-b271-3f2585630374 | -13.14724 | -54.92471 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cc186b7-1295-33d4-87ff-c7728fbc632d | -13.01263 | -45.17794 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b43580c4-07ea-3c61-bb9f-45729a784cee | -10.59683 | -49.16399 | 2025-08-21 04:40:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5321f584-d2ef-3e00-ad6f-7598ffd8af87 | -15.02425 | -54.85197 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3808fda8-6e4e-39a3-a6db-fb9754a63070 | -17.39475 | -44.24729 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6ced7267-f803-3615-bcc4-9d33e0029f27 | -12.88599 | -46.0656 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90a05dc8-9cf2-325f-897b-34c675a8c18f | -12.66724 | -44.9597 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04006ff2-251a-3774-aa35-d152a7986a2a | -8.86877 | -62.40163 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 496229df-778b-3510-9f68-83f972eeb59f | -12.95487 | -46.23014 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25bb7b90-b047-3a1d-a8d3-23fc0ef4b3aa | -13.591 | -43.35208 | 2025-08-21 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2daf910b-7202-36fd-9bb3-631299c283d3 | -14.85534 | -47.94579 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bf76402-2fc4-3c8c-9ae4-3e7d8f2bcf3d | -14.47003 | -48.37262 | 2025-08-21 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b350deb-4ff5-3068-ba3d-03f7dd282ced | -8.86112 | -62.40857 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b92a120a-df25-3948-a536-8bb7d3338414 | -13.63882 | -46.88277 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0288d48-e543-3d95-a2f2-790497994275 | -12.97815 | -45.20975 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42d1215b-9f74-36cc-8512-ab13ca21ef59 | -15.92208 | -47.34423 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfb6d156-e80d-3cd1-a6dc-9402125b2cad | -10.40927 | -59.37479 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d9dbc3a0-f74b-3a53-8931-cd99abcee4cc | -15.00829 | -54.83616 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72fa2459-274d-3760-9cac-2f2e61886375 | -12.67098 | -44.96435 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4791412-8865-386f-98e3-eff38865bb5c | -10.71744 | -48.2337 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bc916a2-0e49-33e8-8029-7e667ad4a439 | -13.14862 | -54.93914 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2349886-9ba1-3ed3-bca2-2a2554ef69d0 | -8.86568 | -62.41792 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 7ca1fc0d-5cbb-34fa-b341-1e33e05eedea | -12.98467 | -56.87947 | 2025-08-21 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16585f99-d1b3-3b0c-9841-582deb05616a | -14.57592 | -51.93833 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9abea158-0d24-3479-9cf9-abc81b1f0e7a | -10.72612 | -48.24666 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eede5f22-604b-30a7-9b9a-15f15446b131 | -15.6763 | -53.8512 | 2025-08-21 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b0fa7b1-6cf0-320e-a846-b730b78bcf79 | -11.08961 | -44.81426 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c64071e5-e8f4-3660-85fd-32dbd150f74c | -9.66315 | -48.37989 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32e921f5-359d-37bd-94af-36db26278fc0 | -17.39536 | -44.24212 | 2025-08-21 04:40:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ff41d8af-1cf3-35e0-8f21-87857c5ddbc0 | -10.70995 | -48.23635 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba0aa10e-909a-3e56-bd9a-69efc14e1088 | -14.84494 | -47.93989 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 920b5c1c-a695-3747-a0d5-7b70c2249577 | -13.03584 | -45.19746 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1dc17a9a-3315-3744-9840-f62b253787b1 | -12.97499 | -45.20119 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 159a2690-89df-3e0d-9f24-f8dd06969ea0 | -14.75098 | -56.02016 | 2025-08-21 04:40:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc4979cc-7445-3003-ba9f-0ae03c1796dd | -15.50811 | -48.04818 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cad28d6-af12-3092-8d73-dcc93afdb739 | -12.51964 | -45.59824 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1049362-3fbd-3523-820d-5d877c6c3934 | -8.86754 | -62.40997 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 120f04ac-a7ef-3bd3-8b00-2ac31d82c030 | -12.94279 | -46.23001 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f7a943-357d-3fe1-b485-99d4202ed4d5 | -14.85046 | -47.95383 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6303ff3e-e28b-3a2d-8e1a-6b0c23ca68a0 | -8.88792 | -62.40839 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19d1943a-f977-315f-b52f-2db83734f425 | -13.40609 | -46.34959 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1b8e42d-f2a3-3e92-81a3-862f933ea417 | -12.91029 | -46.09526 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18fd85cb-762b-3b54-8268-67acaf7cb580 | -8.87416 | -62.40844 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a564ac21-eaf5-3f7f-bdd8-994de7f75274 | -13.03177 | -45.16428 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e5a9c362-ab05-36a1-a6dd-4384e4c2a8c2 | -9.91558 | -49.24575 | 2025-08-21 04:40:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6cb4083-a83a-360d-a333-e79a94184e3e | -15.43196 | -46.71529 | 2025-08-21 04:40:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d28a24ed-1e87-3a8f-8c4b-f3a895dd907a | -13.03547 | -45.16886 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| affda691-66f6-31c0-b925-f137928c95a9 | -12.22523 | -45.42046 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d63ab8d-02b9-32d6-8683-880303f5a015 | -12.08535 | -47.9016 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b246e8e-3848-32b8-b396-7ba1bd367229 | -12.89732 | -46.0719 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 532a6c3e-bb74-34b0-8c23-0417026457ec | -16.62356 | -49.42237 | 2025-08-21 04:40:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c7847ae-ee76-3638-8493-a5a703300deb | -9.92379 | -48.68855 | 2025-08-21 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7797d3ac-e3e3-3291-a90c-d919b17af422 | -13.03639 | -45.19343 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec822cc8-ec18-33d4-87f6-1272ba8237d6 | -14.99955 | -54.84362 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a1de2b2-f692-395c-8bfb-4eab1cc62e8c | -8.36568 | -54.99628 | 2025-08-21 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da9bdfb6-cc0d-394c-ab84-049412efe4e7 | -13.03122 | -45.1683 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 9e8cc74d-bdd6-398e-a987-4fde0f2542ec | -14.12785 | -45.39982 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c96b970-de9f-3f58-8d71-f3aecd99dc12 | -11.579 | -47.00387 | 2025-08-21 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88208171-848e-35cc-9cdb-515a1a19e475 | -15.56777 | -50.31815 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc3a6b67-9903-3f55-8282-2970d51c8dd0 | -15.72917 | -49.44332 | 2025-08-21 04:40:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f098bdd6-94e2-38da-843b-bdaf72f4d74c | -14.65331 | -54.87135 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b3946912-8932-33f5-93ea-8461ede94a97 | -12.9447 | -46.24535 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 851a2522-2105-363c-af23-d5777aa6d797 | -13.02164 | -45.17515 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 35b81238-f718-3c57-9a1e-463902282e23 | -12.9345 | -46.20235 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2082b9b9-f7a7-32c3-941b-caef2fc7ad02 | -13.02943 | -46.82909 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37faca35-1aca-3afb-99fe-6a4113cb89e3 | -12.89659 | -46.0771 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfc448f2-a56d-346e-aed6-e7eab9bdb80e | -13.65479 | -42.48148 | 2025-08-21 04:40:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c5b63cb-8aab-37dc-b465-a4f998ca605d | -8.37433 | -55.00029 | 2025-08-21 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 076a20a0-27e5-306e-b958-9e94fe9d729c | -13.14194 | -54.93322 | 2025-08-21 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d916622-c0f9-3c38-b209-c56094c59d57 | -14.87626 | -48.06109 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a5c35cc-f6b3-38da-a830-76806adf25fd | -12.94871 | -46.24548 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e503f04c-5a7a-3c7b-9959-62cc18044dde | -10.7209 | -48.23426 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e5a814a-effb-3ca4-b32d-a26165ede71e | -13.01632 | -45.18254 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5b9e0d6-37ce-325c-a9f9-1f22ee19f81b | -8.86543 | -62.38674 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 8861083d-a4ef-337b-8176-f3f946fec35b | -11.29647 | -44.93913 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74a0604d-162c-3ab8-bc73-2cd3ffeac068 | -15.50873 | -48.0438 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4180d7fe-9a12-3b65-9d60-d96877024d0c | -15.88549 | -49.01389 | 2025-08-21 04:40:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a11e778-c369-3a40-9f4d-4e5a9dac42dd | -8.87109 | -62.42466 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e1f886a-4a5a-3420-8f6a-0894fe3570d8 | -13.03483 | -45.20483 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c1ca9067-08a1-3692-8110-84eb9ffafe07 | -13.03901 | -46.80933 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 217261fa-a52d-3993-8d2e-e0bcde5419ee | -14.5017 | -45.95374 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12360ad7-0150-335e-8cf0-e270ec9dd3bf | -13.57942 | -47.55642 | 2025-08-21 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79d8ee74-a8be-3aff-b76c-f2c05af0efdb | -12.20722 | -45.42918 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1256d4bd-dd4d-37e8-85f5-c503975e5778 | -7.55696 | -63.85495 | 2025-08-21 04:40:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bc752ff-9f1e-343f-8521-52d215ec75d5 | -12.94607 | -46.23545 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d051d9f-7e92-32e2-aa5e-dcee1a5910f6 | -14.37907 | -52.02267 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d400372e-f527-3b1e-aaad-5f9636a6b8f7 | -12.07998 | -47.91328 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0692c5e-7005-352e-865b-5282823a9df0 | -10.99333 | -45.62517 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb54d046-d742-3987-95d2-72aa36663dbe | -14.53489 | -56.23721 | 2025-08-21 04:40:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc774695-906a-38e3-bf7e-d373dcd858a1 | -9.65916 | -48.38309 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4292a46e-bd46-3553-a684-60ec58c2cb59 | -15.51116 | -48.05314 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecbf3630-bb35-381a-a773-c8d4beffc9bd | -10.40877 | -59.37436 | 2025-08-21 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e44a52a9-d122-30bc-b1f0-3bc68ac613ae | -14.493 | -45.95617 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8d7c4d1-4d11-32d6-872b-6fe93a19d415 | -12.95415 | -46.23531 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README49.md)
