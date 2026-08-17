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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d910d3c-3e68-381c-83a5-67a4e88cef0c | -6.86954 | -56.40736 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb619416-5970-3b88-b525-930a066e171c | -6.6292 | -58.95966 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 289c2ed9-4afb-3698-80a1-53b0167b3b36 | -8.52514 | -54.89753 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5e09edc-27d1-34a9-bb05-3b46b0ea1271 | -6.82368 | -56.45494 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be53fb5a-8c3a-3ddb-9d38-35877998e267 | -14.47444 | -45.67791 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6565827-a014-3937-aa13-81f7dc5a0521 | -6.65438 | -58.95853 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e936ea19-fe46-3eb2-83e0-f5e04cc41f70 | -11.53828 | -46.22311 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f0bc359-c9c0-3f2b-97a7-5e2cc7b232c5 | -9.47935 | -51.64029 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc019f2-74a3-361e-bef6-ae7aaf4d0c83 | -6.62827 | -58.96495 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cc5fa573-38b9-3eaf-adbc-b249159e7f95 | -8.67313 | -54.77018 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7aa5b3f-ae45-30a3-b77c-a157fe2d212e | -8.89734 | -60.60305 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dcb5ee02-5199-3b82-8785-da227244a3f2 | -12.55285 | -47.85173 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33539e28-d75f-3ff4-920c-d203a8f9099a | -13.78713 | -53.80328 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 194bf401-767c-30dd-853e-fac191b547f9 | -14.31917 | -53.048 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14aabb8f-03a1-3e8e-940c-e9d44493dcdb | -6.70645 | -58.93653 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4e184d20-34ef-3fd2-8bdb-e393044f8678 | -7.37024 | -55.48473 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f0aed2-f15f-317f-b01d-07897951fc7d | -6.60406 | -58.97488 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 24ce1fee-a541-3823-9380-06a5dc448e40 | -11.47487 | -46.58189 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 586ee3fb-098e-33ba-9f35-03cb19cec142 | -8.63832 | -54.71304 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d94a974-1b95-321e-9651-4315eb7d70d1 | -13.51269 | -46.28429 | 2026-08-17 04:57:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ea1e4bb-a1b7-3cd5-ada1-bced4afe6797 | -12.03931 | -46.47922 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2ea50ab-6eaf-3350-a310-50c5c39fca48 | -11.13532 | -46.52319 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 122a9b88-080d-3828-bda4-7cf0dcab373c | -8.65918 | -54.72081 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e272735-9d6f-339f-ad35-7fe29e0ac539 | -7.45613 | -59.99794 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5b47f02-659a-3fd6-891d-f69cc79b3206 | -6.70735 | -58.94067 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 330ff5b3-cbf9-3673-9219-08bb67adb734 | -8.95669 | -60.60117 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f90aa7-dd70-3edd-b59d-308617299c06 | -11.40869 | -46.41439 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45931f7a-a45c-3a01-b024-4a6cc8a84baa | -11.46539 | -46.58807 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| afa8125d-557c-3707-bbb2-9bcd005291b5 | -9.12505 | -45.1787 | 2026-08-17 04:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb0586b1-c20d-324a-bebc-604fc6f4421a | -6.71397 | -58.93106 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5a6f7c9-8720-36cb-b357-e44b7812da43 | -8.09364 | -61.35911 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6013a6c0-63be-3204-95f4-5b04b9741173 | -12.6944 | -48.51051 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ced9d72-3387-3838-81a4-e8353160184c | -9.98166 | -53.93938 | 2026-08-17 04:57:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea9ccafe-4a9a-3280-a872-26f60d038a77 | -14.87882 | -46.64515 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7c4040d-3d71-321b-b7ba-9da02b1f5061 | -11.72819 | -54.60482 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3656c455-7bda-3840-b9bc-418c3c461efb | -14.40325 | -51.87347 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8148642-62d9-3aef-841b-632524698e84 | -9.30417 | -56.9194 | 2026-08-17 04:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cecdea37-d2dd-3f38-bcf3-61071d1c27f2 | -8.98488 | -60.50551 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 609651d6-428b-35ff-b32a-788fcf946488 | -11.72408 | -54.60806 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be40386e-cf93-3700-91dd-aa8f74b78698 | -11.32038 | -46.21451 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0765d0bb-769f-31ac-85ce-2730bc8cb8e7 | -11.1375 | -46.50755 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66e80c80-ca88-3b62-b6e2-af67dc435dd1 | -11.70394 | -54.60063 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66bc7942-3987-3480-b603-33c4413f310f | -11.9817 | -46.45248 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e71553d5-d23a-38fb-b3ef-c740d24d018b | -8.6484 | -54.71899 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa02810b-1e55-31b1-b808-a82ad066e241 | -11.14485 | -49.04211 | 2026-08-17 04:57:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd368567-dcc8-3518-9c09-dde2c9dc8987 | -6.82 | -56.45882 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d58eaf8c-e601-3cd6-8df0-f1edcaf2bdbb | -6.70266 | -58.9577 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43e1d3c9-8317-3908-a71f-29154c8b8e80 | -10.92493 | -57.12654 | 2026-08-17 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10afaf2b-5e09-3daf-b05c-460c3c8912a4 | -7.88497 | -63.75883 | 2026-08-17 04:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 335c147f-ee52-35d0-9714-43b9f33cbd30 | -8.73021 | -62.90226 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c2992f8-721a-35d9-9619-2f987796e216 | -11.72537 | -54.60037 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c869f82-f8b6-3794-9fbb-ae8902d74a70 | -8.95329 | -60.53199 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7597e90-c469-39fd-82cb-63dfc9705766 | -9.18063 | -56.98312 | 2026-08-17 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e072e14-bf22-372a-a49e-c369b191aaf0 | -11.88338 | -51.95355 | 2026-08-17 04:57:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9d9327e-b9e8-3e7f-b879-df1eae1c4970 | -9.08918 | -61.39059 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c869cf9-8d1a-38d5-a639-128bc77a48e7 | -11.71434 | -54.60241 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47e493be-1d2d-3cf0-8021-f49f53932a7e | -14.42405 | -53.17143 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36a38d14-0179-37ec-978e-a5da65b9a4d5 | -8.02736 | -55.14378 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b57e4d7-e51b-37c3-a264-cce0fb310518 | -12.04517 | -46.48251 | 2026-08-17 04:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdf8d168-a818-389e-a01e-0a1e6d752e6e | -11.72255 | -54.59592 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83cf9f92-63ef-36bb-bbb0-d77a6322de0a | -8.73538 | -62.90803 | 2026-08-17 04:57:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 084d3028-1254-3e41-a8af-ec42683eefeb | -7.37405 | -55.48536 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f953f8f-c033-395f-a95d-3fe0c6b6f697 | -6.85789 | -58.97042 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08a93a55-3b3d-3504-bc13-3552d7e657eb | -8.06435 | -48.53622 | 2026-08-17 04:57:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f950dc1b-e75e-35db-a8e5-5f94df2131b6 | -8.37057 | -46.37687 | 2026-08-17 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80eb9090-049a-3570-8ac7-253316693f09 | -14.45929 | -51.84513 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bce2eb2-c1ad-39f0-bba7-159157dc873b | -11.88184 | -50.22156 | 2026-08-17 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a0c590f-6df5-3915-97a2-45e0931acfa4 | -11.71087 | -54.60181 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04838199-ac87-38d7-a084-93f4534a84d7 | -11.23795 | -54.0181 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52fc60b8-8f32-3b69-90e1-d88af689dc2e | -8.66278 | -54.72139 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9781f05-a61a-3b68-9d78-fbd18f340f54 | -15.14797 | -50.04892 | 2026-08-17 04:57:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95abca6d-5fd4-3f75-9111-1d18b19d5081 | -10.0502 | -62.45694 | 2026-08-17 04:57:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97745586-e704-3b7b-b8a3-bab946482095 | -8.50996 | -54.92109 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f02a232b-2899-38e0-a3f1-2494fb8992fe | -12.54747 | -47.86134 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10463715-af4a-3853-b52d-09a993c3c039 | -14.14791 | -52.88463 | 2026-08-17 04:57:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2fbb1d6-cab0-30ec-9d4b-37afaa9cb8a2 | -8.95101 | -60.51533 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2b2e6b5-40a8-3323-81c2-76aa6ce7002a | -9.17888 | -59.66982 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5cae365e-9e6e-38f6-a0c1-34ca70c24f1f | -11.10289 | -47.28342 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6cc2902-1d12-3f7f-b5b6-7eab842ed3fe | -13.43333 | -57.05866 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ccabedd-6358-3c58-b026-4fce236bd3ac | -7.90973 | -48.52658 | 2026-08-17 04:57:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccb91f91-fa80-38f7-a5f0-d819969053fd | -12.24428 | -47.04049 | 2026-08-17 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3b19b64-46ad-3b6b-b811-d7b8fd84cbde | -11.72191 | -54.59975 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c11c81d-7c2d-3392-ace1-3ab429055444 | -12.6702 | -48.51669 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f1abad4-ceef-33c0-978f-287e2a0e60da | -8.90008 | -60.58733 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe868d2e-a7eb-3530-be01-66c2fbee47d5 | -11.71498 | -54.59856 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ccccd80-bd20-3b8f-af70-71e9306e3c38 | -6.62637 | -58.97569 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86dd2b84-156e-3f81-9b4d-af9d98315196 | -11.23804 | -54.01797 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6d3d6b1-8009-3492-83b8-7f7c4154ea93 | -14.40717 | -51.87037 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26cb1432-5161-3ccf-af32-5c73962d0817 | -12.69306 | -48.51982 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 14df0803-ab01-371f-95af-53e0e3a1db0a | -6.6184 | -56.27013 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e9d9056-27d3-34ea-95f4-8d4afca06a8e | -11.71522 | -54.61844 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02298a17-5a36-3019-b392-33cac01cdbc6 | -14.40505 | -53.05883 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78eecd6e-20cb-3908-af84-1b8641765745 | -11.71998 | -54.6113 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 276e0c2d-4e93-3eaa-9f8c-c1c2254eac00 | -14.53074 | -53.26566 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ed3bcab-f721-38e1-8f41-965481c6d456 | -12.35926 | -50.88951 | 2026-08-17 04:57:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3cbdd7b-c70e-3344-9f69-ed3a76ed535f | -14.49905 | -45.68264 | 2026-08-17 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c92128a6-c413-32da-8c1b-6309cc03d126 | -8.90062 | -60.55484 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64620d3d-172e-323f-aabd-aecdccf6dd09 | -12.54064 | -47.88136 | 2026-08-17 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81a24f43-bd87-3818-be61-a161fd831583 | -11.7111 | -54.62173 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65fe1161-4d13-3bf9-a96b-f32e796baf44 | -8.95324 | -60.59068 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README34.md)
