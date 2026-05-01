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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3aabb159-162e-36dc-ac9f-a34c25c6afcb | -12.08829 | -51.22351 | 2026-05-01 04:49:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ca7b5f1-6e58-31a4-9479-57a476cc1b7f | -10.97971 | -45.08105 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| f6565fe9-1a93-365a-9451-d04973f19207 | -10.98751 | -45.09186 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| cf05d6f5-c044-3b24-a95f-5b4c79514caa | -11.43091 | -55.09829 | 2026-05-01 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 393bcd2f-e41e-384a-8a5f-4f3873865376 | -14.38565 | -47.92025 | 2026-05-01 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b2b9893-618b-3551-9134-9a8f9a91a7a4 | -10.97658 | -45.10429 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 02f55c90-f68f-3f4d-8011-b16e0ce99bd7 | -10.98424 | -45.08175 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f7998703-ef6e-3272-b98e-51ce49164739 | -12.98943 | -54.67906 | 2026-05-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5afe256-f6ef-3a05-9077-4cf5b95241c4 | -11.95204 | -43.38256 | 2026-05-01 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a81382c6-16c3-34f5-a8fe-d58d09fd3c4f | -12.29175 | -57.3878 | 2026-05-01 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 156e05a3-2c45-3a65-9257-c0d829f5eaba | -10.98814 | -45.08719 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0b3c898f-9b11-3a16-9621-8e81f6603dba | -15.42513 | -46.67049 | 2026-05-01 04:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4262aa70-795d-3f5e-a980-61223fa4ba46 | -12.99289 | -54.67965 | 2026-05-01 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09462579-9899-3478-8af1-ad0add5599dd | -13.40402 | -45.63937 | 2026-05-01 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b2244db-3d43-3efa-a2ea-27ccb3572a42 | -12.34302 | -50.00763 | 2026-05-01 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 523bd0ad-061a-3567-949c-ddff6bd888d1 | -14.69423 | -52.94964 | 2026-05-01 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2f45e63-730a-3cc1-ace3-9ed4beeb0723 | -10.99395 | -45.07847 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2a9ac3fb-556e-32e3-9064-add46bd7ee00 | -10.98361 | -45.08648 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| e22d372b-6a9c-311d-a690-5b829001bc30 | -11.95164 | -43.3857 | 2026-05-01 04:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dda8a40-6fe8-3145-bd7d-5d5b646013e0 | -11.38121 | -55.17557 | 2026-05-01 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04acd1d6-5f4c-3e42-b606-0b5fab7a5b47 | -12.41122 | -52.15294 | 2026-05-01 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 048d9c22-d091-3643-9d93-4738ee38833f | -13.3686 | -39.90536 | 2026-05-01 04:49:00 | NOAA-21 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4ce964c6-155b-36a7-a392-2292b3af4501 | -10.98034 | -45.07632 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 60f4a8f4-f3ce-3db6-bd9b-622d97dd7164 | -10.97781 | -45.09512 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 3a877816-4d58-348d-99db-160da29177c8 | -11.06182 | -49.50286 | 2026-05-01 04:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bbf8fa9-61b0-33af-a7b3-890f8271bc80 | -14.72359 | -52.78326 | 2026-05-01 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb5422ec-ae12-3119-a2f8-cb28d7941638 | -12.39201 | -50.02675 | 2026-05-01 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 343f9483-673c-3add-a43c-3520eb2511f1 | -13.40682 | -45.64291 | 2026-05-01 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f50f2bde-9818-3a21-84c8-71999f860999 | -13.38059 | -54.2672 | 2026-05-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41093ec3-30ce-3097-bc8b-33fed93efd79 | -12.05567 | -57.41917 | 2026-05-01 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebd08ac1-a281-3a86-ae48-51dbe4d7ca4f | -10.97907 | -45.08576 | 2026-05-01 04:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 772cff98-903c-3eb5-a8b8-411f755ed31c | -11.001 | -45.0617 | 2026-05-01 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 119f1b37-03a0-363d-82bd-84589dd02f11 | -10.9624 | -45.09 | 2026-05-01 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9561f2b0-dab8-3105-9241-7d751a2b122f | -11.0006 | -45.0847 | 2026-05-01 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 6f1f589a-c9ea-3b69-9dd7-4813fc01f99b | -10.9815 | -45.0874 | 2026-05-01 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 270.2 |
| c7d76568-d8cb-3e7e-a953-835e83c86ed9 | -10.9811 | -45.1104 | 2026-05-01 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| fd2f0adc-a054-3462-bba6-7f005885b37a | -10.9819 | -45.0643 | 2026-05-01 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| eb882580-9a1d-3c00-ade5-459b962593f1 | -18.01349 | -53.00163 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dec77d1e-e775-3bc8-b956-84ad323e80dc | -21.70288 | -48.42409 | 2026-05-01 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f83f8135-582b-392f-9401-f114773e523f | -19.43747 | -46.88926 | 2026-05-01 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88ab562a-bd44-3c36-9921-70b2cddbe9f0 | -18.2319 | -54.60045 | 2026-05-01 04:51:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcf894ea-208f-30dd-9984-a9992b564e7f | -18.48914 | -49.69394 | 2026-05-01 04:51:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 48913cbc-858c-3ba4-a21c-926c5ac6f8c8 | -18.02455 | -52.99601 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7973e0cd-998a-340c-811a-33b2d9d8cdf6 | -16.37692 | -52.64045 | 2026-05-01 04:51:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ceac874-6882-3007-85de-7ed71665a5f3 | -17.01751 | -54.34518 | 2026-05-01 04:51:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d97e0124-eb8a-30b3-95c2-446f657f7578 | -18.02843 | -52.99293 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 892b9bc4-8c3b-301f-8a5b-7862262ecaf0 | -20.20722 | -46.46024 | 2026-05-01 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8892ed04-86ff-309f-8deb-7112aa15d196 | -18.00662 | -48.18002 | 2026-05-01 04:51:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98544aeb-3abd-3e73-8173-611cf0a1903c | -20.21248 | -46.45579 | 2026-05-01 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f768b183-78f0-329d-898d-caea99ad7167 | -20.61207 | -48.92841 | 2026-05-01 04:51:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c2f4c1eb-41d6-3261-bf9e-dbd433e16d4c | -18.48431 | -51.68795 | 2026-05-01 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abfcddb9-75e7-3dae-90c7-0b798d1cbb5c | -18.51396 | -55.51838 | 2026-05-01 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4b0c9727-38d6-3707-9996-87be797e989d | -17.25029 | -47.07896 | 2026-05-01 04:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62adb995-2494-3349-8111-7135454f7b72 | -23.31969 | -47.55108 | 2026-05-01 04:51:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 058291d7-5f95-3872-81ba-0fa90cf9abf1 | -23.32024 | -47.54606 | 2026-05-01 04:51:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 995d9db2-63fb-3e49-bde6-b81254d5fb5a | -18.42121 | -49.62332 | 2026-05-01 04:51:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f96c4053-6c06-3ae6-9edd-a9ef6a54169e | -20.81541 | -45.18467 | 2026-05-01 04:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac6e4657-8e80-3baf-9ea3-8afcba1ea184 | -20.05734 | -50.45724 | 2026-05-01 04:51:00 | NOAA-21 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e3d4e5b-fc60-3ef5-9b18-8e774910099e | -20.05795 | -50.45271 | 2026-05-01 04:51:00 | NOAA-21 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd5ccc39-913b-3e14-880a-71e49c2c1f9a | -18.50844 | -55.50948 | 2026-05-01 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 85afb8d3-daa8-3e28-b1eb-0f2b49d3bcc1 | -18.48863 | -49.69196 | 2026-05-01 04:51:00 | NOAA-21 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 63133227-6ae9-303c-a9d6-e24f3fc44e99 | -17.24976 | -47.08325 | 2026-05-01 04:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a3d2316-83db-3425-b3a1-59cc3411b2bd | -18.02124 | -52.99546 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c4795e1-bce0-35f2-a2eb-5d10679f8cee | -18.02511 | -52.99237 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4fd61e7-b5d1-3842-8387-c102729dd71b | -16.44802 | -51.06294 | 2026-05-01 04:51:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 681539c3-8a58-355e-95e7-a31d71be668f | -21.70339 | -48.41982 | 2026-05-01 04:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e659fbc5-b090-3543-976f-1fd87bb38026 | -18.00712 | -48.17616 | 2026-05-01 04:51:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75a2914b-3ea3-3cc7-a053-d39364ce7481 | -18.48774 | -51.6885 | 2026-05-01 04:51:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a54dfc-7684-3905-b147-eddc49c9ab81 | -18.51184 | -55.51009 | 2026-05-01 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ab85c732-a3fa-3913-abca-5f0f3d6aba3d | -18.5146 | -55.51454 | 2026-05-01 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9c27611c-ce8c-34fc-a8f2-3920177e3528 | -16.4251 | -52.79186 | 2026-05-01 04:51:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e791efac-fe51-3393-ba61-bbd62f746e3b | -20.81577 | -45.18125 | 2026-05-01 04:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c458017e-aac6-3a32-a2af-b0dc35153a7a | -18.01736 | -52.99854 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6adb1678-031b-3f55-85e8-75fcd6512901 | -20.71483 | -55.1792 | 2026-05-01 04:51:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0d0ced6-6ab8-317c-b0cf-4a00a8974f5c | -18.23249 | -54.59677 | 2026-05-01 04:51:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 768adf12-8b53-34fc-8098-5b1e0cbbafb7 | -19.43692 | -46.89396 | 2026-05-01 04:51:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bad5c6e7-619f-3d0b-90a3-dfd4c98a7c42 | -17.25464 | -47.07948 | 2026-05-01 04:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df8a50c3-7ecf-3f34-9467-dada6d8c4721 | -18.42497 | -49.62393 | 2026-05-01 04:51:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a6f27566-f4db-3278-a068-f82004c47ae0 | -20.2119 | -46.46105 | 2026-05-01 04:51:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f69e01-0dbe-367c-86a1-6c6ad1a3c921 | -18.01405 | -52.99799 | 2026-05-01 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fed11c0a-09c0-3ade-991d-3039e345bb19 | -28.78229 | -50.2171 | 2026-05-01 04:53:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f6beae2-e88a-34a0-862f-74a1207902c8 | -29.25073 | -55.94333 | 2026-05-01 04:53:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 10d37e2c-41b3-3867-a7d4-901108fe70ae | -7.31754 | -46.20475 | 2026-05-01 05:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d021ac5-6ed9-345f-8c0a-990bc8c8d495 | -10.97474 | -45.09079 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ffe47fc0-981b-3b04-9b3c-3483215ac64e | -10.55459 | -44.3375 | 2026-05-01 05:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1df3aa0-1a43-3922-90c8-2aa61fc4371d | -12.98774 | -54.68108 | 2026-05-01 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa3e487e-cd08-331f-87c3-a53b8d45b6ba | -10.5473 | -44.33673 | 2026-05-01 05:21:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28a67608-afc8-3912-89ff-57687220e2d5 | -11.57032 | -54.56233 | 2026-05-01 05:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b791418-99a8-3630-b89f-7b1a77d8622e | -12.36937 | -54.75164 | 2026-05-01 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5b51368-67d6-3ae1-9b28-9a197c0b4b9f | -12.38112 | -50.03473 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08e9c91f-a2e5-3a38-8a92-a001674b8993 | -11.43502 | -55.10346 | 2026-05-01 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f914734-ecde-354b-9c1b-72dff9827588 | -10.96778 | -45.08954 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f7fcd66f-66af-3d69-ae85-c92e609d7efb | -12.34165 | -50.00713 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8160c8c-71cf-3d80-97b2-10eaa5d78093 | -12.37319 | -54.75222 | 2026-05-01 05:21:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fd5ff65-9f3c-3dad-b518-72b431171609 | -10.96627 | -45.10269 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 78ec9195-90ae-36d3-89fb-2ba40bb22128 | -12.3763 | -50.0308 | 2026-05-01 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e70c79df-48f5-3ce7-93bf-918036583168 | -10.96701 | -45.09621 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 04ad3ef6-a1cb-379f-be5d-ac8f955011fd | -13.3795 | -54.26614 | 2026-05-01 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f217aa49-3fe9-3a91-896e-44103639eac6 | -10.9817 | -45.092 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 0cd993dc-6650-3157-80a0-7a9fdf35fe8a | -10.98868 | -45.09304 | 2026-05-01 05:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |


[Clique aqui para ver as próximas entradas](README6.md)
