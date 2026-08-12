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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbcdd5cb-1e98-3dce-9c41-08697ee20395 | -8.8964 | -60.56533 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e24572f9-a63f-31db-b56b-c7ab86ba207b | -11.95098 | -46.32271 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 102fdabb-d69d-38c7-81de-f9b6d292dfcf | -15.29632 | -48.86996 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c1279b7-41ae-3134-b3d6-b703ded419ad | -14.58614 | -46.75629 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db1b18e5-b9ba-37b8-8ec3-14f272289370 | -8.89846 | -60.5866 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4426db5b-080f-39b1-9097-63126ecd39db | -11.93603 | -47.38741 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed9693ed-619f-3693-924c-68d739afccf9 | -13.89033 | -53.8258 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e5072c1-696c-36e9-95c4-5ebac87d2cfe | -9.37434 | -47.44075 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4720e7a-d137-3323-9961-1ec008353777 | -15.17031 | -49.26271 | 2026-08-12 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74d7870a-4d28-3c1c-827a-b640da0c1556 | -14.28754 | -45.28593 | 2026-08-12 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52396a87-b30d-3a6f-a0a6-67f1c9960e80 | -13.89313 | -53.83054 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7b1fd1e-5d1f-3178-b2ce-63b00a158390 | -10.63783 | -47.48634 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a6ab41bb-3fd5-3f60-a90e-7790664f6efc | -13.90216 | -53.81986 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f4e57af-ab4f-3bf9-bdd0-e5420a791be9 | -14.83688 | -52.61685 | 2026-08-12 04:51:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1528bad-9b01-3a08-ba2e-5d70666959f3 | -11.95032 | -46.32738 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e077a78a-2f3a-348e-a26c-2243146970ac | -9.75953 | -60.77031 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 966b6351-e25d-3f37-94d4-d99c19a27ce1 | -11.80982 | -51.82041 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79bac820-f304-3d91-85e9-aa079a6e3c18 | -14.38012 | -52.02807 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 949150f7-c6e6-3b5c-893a-7e003ccff65d | -14.55009 | -50.40358 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c1abe65-33d7-3661-979c-616a2a6146d7 | -12.78711 | -51.78392 | 2026-08-12 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 518738a8-4978-3f5f-847f-129e980b83e3 | -16.16165 | -46.80805 | 2026-08-12 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d14f2ac1-f926-3160-b0e0-0f54b2fbc901 | -9.33056 | -47.53722 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3beefc9-a87e-320a-a18b-e4a99e0a1359 | -9.34131 | -47.5142 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f54823f-a3ad-3679-9457-9d357ed78ecb | -16.16107 | -46.8124 | 2026-08-12 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dc3e312-36e4-305d-82aa-36ac675c8521 | -12.10373 | -47.18858 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9dd1d5ee-ed84-3f4c-8e24-4e0735f0c9df | -16.7067 | -49.15447 | 2026-08-12 04:51:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa679d38-2c3a-38da-879f-752fc63c778c | -13.54509 | -46.27579 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ac4d22a0-d7b3-3d43-9c30-d93b6a0977a7 | -9.76184 | -60.75819 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2625adf6-7e7e-32d6-8ab2-9240db2d74d4 | -8.95909 | -60.55063 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cec3dc9-8ce0-3a8f-9fff-d518a76288f0 | -14.25783 | -49.66165 | 2026-08-12 04:51:00 | NPP-375D | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed81eee7-2413-306f-94fe-9d339ff5ee8a | -11.49035 | -44.56926 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 12d2df34-aba7-3a43-812f-b21fdfb36d80 | -14.33395 | -54.04457 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39d2d784-a9d3-31d1-abad-2783be892502 | -11.94632 | -46.35568 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8062b33b-8417-386e-872c-53bf059ea7f1 | -16.64249 | -49.42547 | 2026-08-12 04:51:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| affa9d50-445b-3ab2-be8d-907f1a9cd4cc | -11.7867 | -51.85706 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ac9b8c0-1e47-307e-8834-39144dd8bcc8 | -13.86848 | -53.7617 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31a462f2-3ece-31f2-a058-1fa27da05013 | -14.34028 | -54.04994 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ff28706f-90f7-39ad-a8e3-a7937fe3dc4f | -9.58204 | -48.42059 | 2026-08-12 04:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be29b86a-5329-3ddf-a991-2229c4ae2a05 | -9.7603 | -60.76624 | 2026-08-12 04:51:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ee78dde-3f6a-320b-8c47-1af0f3fc0e31 | -14.48414 | -51.86158 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dcbda59-aad3-30b3-ba2c-afe5f0737d64 | -15.16683 | -49.26212 | 2026-08-12 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fac3a14e-df59-3514-aa52-d6dbfadf9a40 | -9.3727 | -47.44358 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8256bee4-f6ff-321b-b52a-c14181fc9a63 | -11.78786 | -51.8499 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77564669-b881-38d4-945d-cac4ed3c45f6 | -12.14349 | -57.19993 | 2026-08-12 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d0eaeed7-ee26-3b54-90df-856aa6731c32 | -13.86061 | -53.83021 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 674a6e7e-25ee-3feb-9632-38409b78b920 | -10.30174 | -48.3028 | 2026-08-12 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcea2839-6f5a-3347-8bf9-be6cbe72cca7 | -14.5908 | -46.75173 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f9d5016-bee4-382f-8003-f70ceaecaf3b | -12.82215 | -49.70214 | 2026-08-12 04:51:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0701e9e0-5ef3-3b76-9d2c-738b7dcca2c1 | -11.81917 | -51.84773 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab95a066-b6be-3169-bfe5-6cf0d82cdb16 | -13.28053 | -49.66771 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6a98fb14-11a4-3e7f-806a-502d197caf4a | -13.86412 | -53.83079 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfbbbd59-539a-30c2-b04d-12826dde5719 | -13.88962 | -53.78592 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0d028a4-b468-31ef-b9b2-05189b3920f5 | -9.35183 | -47.54047 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0062aa2f-cb07-3662-88db-ac7be0c8af49 | -13.30314 | -49.70159 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb62b070-7645-30bd-b8ec-1fe4c6302324 | -13.86763 | -53.83134 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 808203af-f821-3de6-bf22-3e419c529cf6 | -14.03692 | -53.6036 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8dc315a0-3e78-348c-b1cf-2b2b0ef21c49 | -14.4791 | -51.87174 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33f9c871-8c15-3704-ad54-ff0c23907993 | -13.876 | -53.82442 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 662c2374-b7ad-34e2-a399-13efa694ac35 | -11.46538 | -44.5571 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7818928c-677d-3105-8cb0-bf70d7ec6bb6 | -9.36119 | -47.45529 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25529d81-dafb-3e12-b236-2881adb47cc6 | -11.60866 | -54.6492 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0f3f6d7-c56d-38a3-bf1b-b57043950246 | -12.10307 | -47.1931 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d8aa6ad-2542-3848-854b-24c0d1a63d0d | -14.99976 | -46.6053 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7acb0ab2-2a80-39f6-8ebd-24f4b06c0b04 | -8.65874 | -54.95436 | 2026-08-12 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a18a8e76-f4af-372c-825d-95c8a3a3a254 | -13.86695 | -53.83544 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26bf44d5-ff4c-396a-9169-b94601a64c8b | -13.89364 | -53.7854 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31134ef1-1f7f-3d69-8ee8-dc2f0e0fbbb4 | -14.58685 | -46.75114 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0da247a3-f5e3-381a-8bce-008ff1d614ec | -8.95637 | -60.53342 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9012acec-3e59-36fe-a438-822c6ac0c1d8 | -11.65353 | -50.14467 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27e8237c-dce9-39d0-88b9-24eccd91c9cd | -11.95769 | -46.38776 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c99f4076-552f-3d65-bf27-d21ce6ffe09c | -9.51921 | -47.42712 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 362064b0-7557-3e31-90d8-2791a65930f6 | -14.98837 | -46.5921 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4aced112-fa87-3493-83a2-2f0c0b9ea199 | -11.61003 | -54.66359 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a5d1803-d1eb-367e-bfc8-e73956be9c1c | -11.97618 | -45.78536 | 2026-08-12 04:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d6cbb31-b408-3610-b298-3921f641f85e | -11.49678 | -54.60361 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94b2ce85-e6b1-3031-a071-3b4030dd1738 | -9.15899 | -48.83494 | 2026-08-12 04:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4002d38e-9ce5-3649-9f3a-0feb603bd399 | -8.95139 | -60.5283 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a103d0fe-dfa5-33ca-9137-86b9e725168e | -16.35667 | -48.91953 | 2026-08-12 04:51:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c56c3b6f-9752-3720-ac02-66b4460e49b8 | -13.29975 | -49.70105 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e03912ef-de2b-3b39-94f0-96cea0e51108 | -8.54816 | -54.58958 | 2026-08-12 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f8bc7ce-eb7d-3855-aff2-dbd9e75da1fb | -13.87545 | -53.76302 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bb81131-cf36-32f5-b7ee-08466cf0d8d8 | -14.0313 | -53.5947 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90dd75b4-b123-3b17-bf94-791b0a104e8e | -9.34915 | -47.48654 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db972653-94e1-305d-93da-9e87826ee4e1 | -14.02962 | -53.5947 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1ffce8f-d3ed-3a06-9378-6a0ff2d135ae | -12.32015 | -53.18595 | 2026-08-12 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07fb2bfe-819c-394f-9b98-7d9429e3bebc | -9.35598 | -47.53701 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a19331aa-e017-3f4f-801d-27d13c418ba9 | -10.22449 | -45.93252 | 2026-08-12 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94945121-d4b3-3eb6-9945-8b68437619a7 | -13.89646 | -53.78993 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 08ece350-dab8-35f9-85f1-7059d90bccbc | -9.07008 | -60.40423 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ded529e-589b-3c8d-83f9-640f7ba535a1 | -15.29866 | -48.87871 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 009ec9bc-d59a-3ad3-84c3-0b633bda58db | -12.18119 | -50.16306 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2000141d-0aa8-365c-903a-ed54778d778b | -11.9506 | -46.3817 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2c5a285c-1b74-3444-ae16-e67e6b7042f1 | -13.29072 | -49.69204 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e0a0242-359b-3358-99e0-c2134780561b | -13.89082 | -53.78084 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24bfdf3a-a640-3f96-a7b0-b2906cec2a46 | -15.20584 | -52.75804 | 2026-08-12 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d222dcbe-ad02-314e-90d6-1dd5ad346e4e | -8.89921 | -60.58253 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e6c7724-0c10-3c6c-b8dd-a0bc3b7b3533 | -9.36598 | -47.44775 | 2026-08-12 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e096740-ffec-3338-82d6-e0ecbf4d6c00 | -12.1044 | -47.18406 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c87ec2e-616b-313b-a7b8-4d7e99661665 | -11.96936 | -46.38958 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58fb1df8-6856-3d5f-998a-ea455bebd4c1 | -14.52682 | -52.78539 | 2026-08-12 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
