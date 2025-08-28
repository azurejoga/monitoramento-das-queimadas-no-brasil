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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ae02cf-8ea8-37e8-a09b-f38dae859901 | -13.1846 | -45.297001 | 2025-08-28 00:51:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9eda64bf-ff49-3e1f-981e-a492df2aaead | -11.3519 | -43.535198 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fdd81dbe-bc04-3996-943b-fa0d9c362750 | -14.3653 | -53.208099 | 2025-08-28 00:51:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe3c43d-502c-390d-9694-d8c7caa9b48f | -13.7589 | -51.893799 | 2025-08-28 00:51:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 617fe4d2-6a2c-39a3-8816-11566e0584e3 | -4.1584 | -43.875702 | 2025-08-28 00:51:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 352ee645-3b64-3810-96c5-d997ec4dd11c | -12.7429 | -48.180401 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 395faf87-61d9-3b50-a649-48909cd02a89 | -12.6986 | -48.1679 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4e464b8-e78e-32e8-a56c-551fc0d1ea2c | -4.2852 | -40.919498 | 2025-08-28 00:51:00 | METOP-C | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| eb7ca5d4-366b-373b-9cb7-21d22c33fb2a | -11.1397 | -46.336399 | 2025-08-28 00:51:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17617242-95e0-35ac-9cfd-335b3ab44dc6 | -12.7003 | -48.175201 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3f0e6e2-29cf-3deb-a00a-e5faaa8d532c | -12.6905 | -48.177502 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 123a9734-7ee0-3b99-9803-bd7d63b8aa47 | -11.566 | -46.389801 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61488b1b-916e-3575-ad61-3ade19e6788d | -13.5066 | -46.853199 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e725bae1-b4b3-3558-b305-2fa9aaf72023 | -13.5202 | -46.8666 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 205a67ac-d890-3924-8d4c-0a0366201c20 | -12.7331 | -48.182701 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ff4d2d2-8948-30f0-8390-47b492fa7030 | -3.7427 | -48.943001 | 2025-08-28 00:51:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d17bad-1908-371a-b922-8846e911903a | -6.8712 | -43.612202 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c03654c1-142a-388c-8c80-34d01e3a0dc4 | -15.6684 | -52.736301 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34723c93-7b3a-3bf5-9736-903e524f4b34 | -9.467 | -51.961498 | 2025-08-28 00:51:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f78ffcc-b740-379e-961a-c581c728d3c9 | -12.8144 | -48.132599 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d035bde6-b660-3304-a6fa-112b489607fc | -6.8943 | -43.622299 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| af1d77c4-d1e4-3462-a572-625978a25ab4 | -12.7935 | -48.175999 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db65cf70-6b8b-39fb-97fe-2be5068e28a6 | -8.4489 | -43.697899 | 2025-08-28 00:51:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ce93777-f6ec-3c4d-a955-8cb1af6f91ec | -11.339 | -43.5247 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e04eb097-c17c-3d22-98b1-5ff4bc2cdc64 | -10.4833 | -57.917 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecbd44e1-abbb-3681-b0e8-55f831bfcb70 | -3.7292 | -48.354801 | 2025-08-28 00:51:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3bdd0a-1a9d-304f-b079-e05f351bd9db | -20.121401 | -44.341301 | 2025-08-28 00:51:00 | METOP-C | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0b217e6-4be1-33cd-b0ec-298ba3a9edc1 | -13.427 | -46.997799 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 046e5e6e-d422-3ba1-89f0-6b52b6c5f45d | -11.3293 | -43.527199 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6c8e021-0c03-3d5f-8b66-2eefec1dfee8 | -7.2635 | -45.3437 | 2025-08-28 00:51:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd7740d-82ed-3086-9313-5e5ad935741c | -9.0064 | -48.720402 | 2025-08-28 00:51:00 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 247772bb-7c26-3dea-abcc-b6bb00f12463 | -3.757 | -54.810299 | 2025-08-28 00:51:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f424bb-ad3e-3016-8255-f52c723c8e13 | -12.441 | -48.706299 | 2025-08-28 00:51:00 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e713d81b-8036-35bc-b5aa-bfdc461357c8 | -11.5758 | -46.387402 | 2025-08-28 00:51:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abb562ab-74bd-3048-a9a0-ed11d75ac1ec | -12.4375 | -45.970901 | 2025-08-28 00:51:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 11e05680-8949-395c-a271-561ce1c6e5ad | -11.3261 | -43.514301 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f369b30-780f-33d9-a908-3a981c95d313 | -13.435 | -46.987499 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3243c9dc-a6e8-3d39-ae04-947734b34442 | -21.0312 | -46.223801 | 2025-08-28 00:51:00 | METOP-C | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27821dcb-6445-3aa4-8227-225cdb1617ad | -10.1832 | -51.665401 | 2025-08-28 00:51:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43d08a0c-22bc-3fc8-b56e-c2f889bcff28 | -13.4521 | -46.841301 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3acb913d-bb14-3d0a-bb1e-108109249f9a | -13.4345 | -46.854 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e182f6c9-72b0-32c5-973c-a494a564f220 | -9.322 | -57.7034 | 2025-08-28 00:51:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da59e344-31d5-3335-9644-74846a00e2e1 | -10.8067 | -60.753899 | 2025-08-28 00:51:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72a3c028-77c4-3fa9-bdc5-37bc48f04a5c | -9.4172 | -48.224201 | 2025-08-28 00:51:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87051d5c-d8fb-3d30-adfd-d567debc3fd4 | -5.903 | -45.560699 | 2025-08-28 00:51:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c261604-23ed-3645-a400-5103012b1090 | -14.3743 | -52.085098 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84f14b0b-fc90-324f-bb03-29f88ea35046 | -10.4866 | -57.933102 | 2025-08-28 00:51:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4170ff9c-3272-361a-99c8-78c2bace262e | -11.3358 | -43.511799 | 2025-08-28 00:51:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f977d668-425b-3c19-a387-da824ed50171 | -7.412 | -40.050499 | 2025-08-28 00:51:00 | METOP-C | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| adbc8617-9009-3623-a802-abcadbe60f1e | -9.3092 | -57.690498 | 2025-08-28 00:51:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4719121-acb5-3fab-bfc9-c11383499895 | -13.18 | -45.278 | 2025-08-28 00:51:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc0c2f6-a056-36d9-93fa-42df4dcbd0b5 | -12.4332 | -45.952999 | 2025-08-28 00:51:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12e90809-bd42-3bf1-bd04-948e8deab3a8 | -13.4625 | -46.9725 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1e9e19b2-113c-35b4-ae30-f8b2a15643f8 | -15.6292 | -52.744801 | 2025-08-28 00:51:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f78cc91c-4351-3fce-91b8-f60fca637a7b | -11.5767 | -44.646702 | 2025-08-28 00:51:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf4db2c3-9f0e-3ce6-9eff-d751083093f8 | -12.8276 | -48.144901 | 2025-08-28 00:51:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eea0d617-b7da-3df5-918b-70bba061f0bc | -20.252701 | -41.995201 | 2025-08-28 00:51:00 | METOP-C | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6aa882c7-8787-3f3d-94b5-8d1b34a355bd | -10.4937 | -51.580898 | 2025-08-28 00:51:00 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2021ccd5-a75a-39f4-a6ad-884e3968b2a7 | -17.817301 | -44.501598 | 2025-08-28 00:51:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9bc2b5aa-fe62-3ac9-811a-62fe33a0e99e | -3.4067 | -52.722801 | 2025-08-28 00:51:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601efc8b-8bd9-3e30-8517-37725a43820c | -14.3445 | -51.897301 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce5fc18-e5e1-34e2-9ca1-01140a485003 | -6.8749 | -43.627102 | 2025-08-28 00:51:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cea43cc0-2dfd-3178-b2d8-4c329ff02b1c | -7.0675 | -44.368999 | 2025-08-28 00:51:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14afd31d-3911-3b14-9ae3-d2f24efff5f8 | -19.063299 | -42.141102 | 2025-08-28 00:51:00 | METOP-C | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80bf3e5f-0842-301d-911c-f391a5fbe3f6 | -13.5253 | -46.932201 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf2ae560-1ae9-3c82-a9ed-f1fc0d1158af | -16.998301 | -48.929501 | 2025-08-28 00:51:00 | METOP-C | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0eaffb4e-1acb-3802-b1f7-78c4f546e8f9 | -13.6333 | -48.235802 | 2025-08-28 00:51:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37734947-eb2c-3908-b942-1cb0d2c6f3ca | -13.4252 | -46.989899 | 2025-08-28 00:51:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 43f625c5-93c2-3a17-adbe-dbe60746166f | -6.9112 | -62.900799 | 2025-08-28 00:51:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 900f4229-8a0d-3f28-90eb-f4bbf98d846b | -3.7907 | -45.0396 | 2025-08-28 00:51:00 | METOP-C | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24e12f8b-ef05-3c08-b46e-1341e0606ce7 | -14.3347 | -51.899502 | 2025-08-28 00:51:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4f82b3b9-c4c6-3ffd-947c-3af3474a64c7 | -21.381201 | -48.7882 | 2025-08-28 00:51:00 | METOP-C | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7bbe3a42-84dc-3762-9845-aefa4d0ba988 | -11.2378 | -55.0569 | 2025-08-28 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a455f693-3ae5-366f-8d07-07dc6bddeac4 | -10.5375 | -46.6894 | 2025-08-28 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 14c2994f-c1e0-321e-b3c9-27bb1f7eb4e3 | -7.3357 | -59.6484 | 2025-08-28 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 18afc45c-5adf-338c-8ef8-65aef9f1eaa0 | -3.2299 | -43.4414 | 2025-08-28 01:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 59920208-6925-38e1-8565-a7c86b3292a6 | -12.8032 | -48.1516 | 2025-08-28 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e40d2eef-77d0-3e37-bccb-69bbab6d8ee9 | -10.4738 | -57.9366 | 2025-08-28 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 62478c41-b5ec-39fc-878a-29298bf7c06e | -13.7566 | -51.9053 | 2025-08-28 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6f8fa5c6-85b1-3687-8b21-6c8dc68eae84 | -18.457 | -49.7062 | 2025-08-28 01:00:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 131.8 |
| 87af09d1-b8fb-3d9b-8ac2-d2991e403e18 | -9.406 | -60.5711 | 2025-08-28 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 2d3659c9-1449-306c-8c74-a7de6b65bad3 | -13.4406 | -46.9607 | 2025-08-28 01:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 85bb8771-f768-3f52-bebc-b91069675332 | -9.1363 | -65.2835 | 2025-08-28 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 42e2981c-89f3-3e8b-b309-17c1621abaf6 | -11.3334 | -43.5216 | 2025-08-28 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| fd7dbcfe-424b-3a4d-9e3f-4e8b5d2d7f82 | -10.4736 | -57.9563 | 2025-08-28 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 9c34b0ac-c990-39d1-860a-6aa989afe124 | -12.9963 | -56.9 | 2025-08-28 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 21fb3a97-79c6-3cdb-b4fa-0272ce5046f8 | -18.477 | -49.7024 | 2025-08-28 01:00:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 2db1f9f9-3900-3a00-b80a-97aaeff8f50b | -13.1644 | -45.2897 | 2025-08-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| b8342ac3-6dac-38da-b217-ef69b43ba68b | -4.7893 | -47.2614 | 2025-08-28 01:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 7e83b708-2863-311c-b510-c803046dad77 | -6.8772 | -43.6152 | 2025-08-28 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 6b9a0eed-c412-3d67-8548-785d799c9884 | -11.3526 | -43.5187 | 2025-08-28 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f8ba43d1-4c35-3852-b110-a6336205330a | -7.3542 | -59.6476 | 2025-08-28 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| ac056988-630e-312b-88f7-d2eb13fb86fb | -7.3541 | -59.6669 | 2025-08-28 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| da06f937-f60a-3c18-9895-798374eb6e94 | -9.0786 | -65.7338 | 2025-08-28 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a91d4141-8cd0-3444-b592-3d8ccc5a3fb3 | -6.9129 | -62.9366 | 2025-08-28 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 42c10c71-cab2-36fe-a55a-6153a962a6d0 | -12.4396 | -45.9551 | 2025-08-28 01:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 1aaf61aa-d5fb-39ab-94f9-fd4180038062 | -8.9479 | -65.9616 | 2025-08-28 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 3c264b17-99d1-3558-9921-b8c80cefc058 | -13.2031 | -45.2834 | 2025-08-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e4582a92-213e-32e8-b140-bd254e03b45f | -9.6104 | -40.342 | 2025-08-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 68.2 |
| aa5ca1e4-2dd1-34d3-bc7b-5e4cc4932a6c | -11.2189 | -55.0585 | 2025-08-28 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |


[Clique aqui para ver as próximas entradas](README11.md)
