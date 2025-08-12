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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e75112a3-3a05-3c06-aaee-c85279da01ac | -15.57643 | -47.32739 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b68210a9-3a87-35b3-a1b4-4bc6e62c8f51 | -13.00076 | -44.88643 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3db27e20-cb30-3cfa-8014-bc6925ac93a9 | -13.12712 | -46.87563 | 2025-08-12 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3000dba1-b79e-396f-b491-654ae70ffbed | -11.78523 | -49.55411 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97652c28-cfbc-3a42-9ee5-d5e592e3e757 | -9.34496 | -60.32699 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5d56c39-e64e-3b13-9de6-ea99ab44b3fb | -11.54637 | -47.3095 | 2025-08-12 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b9ee3fe-ab55-3de1-bc8d-6ecb10628211 | -14.68349 | -53.71997 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 103aa430-9940-36a0-8b55-51d6e83ac8c5 | -11.7029 | -51.59733 | 2025-08-12 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33e4a5a6-fa28-3832-8ab5-d00ac5df103d | -11.54674 | -47.30995 | 2025-08-12 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc316400-6275-3c34-b346-614d2eee13bc | -11.47469 | -50.15577 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d5ca718-9612-3dea-a548-0d7d6a0e7618 | -13.00028 | -44.89089 | 2025-08-12 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e6967cf-637f-3529-9164-1d0204a2fa4c | -10.35225 | -50.81932 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 65fd63a0-b187-3610-81bc-bf44ddfe557d | -15.45127 | -47.01462 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d4555a4-a8ac-3813-a06a-5d30bc90cadc | -13.04312 | -56.84319 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 108ae54f-b5c9-3318-85fb-4551ae800086 | -12.56335 | -46.99316 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 156ea9d1-0c2c-33f3-b28f-72e250f03ead | -9.53442 | -66.14101 | 2025-08-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afe32489-be2f-3f8d-8103-4738a1a41b20 | -14.02661 | -47.4408 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 684e485e-c414-3c68-befb-1df7a2d23613 | -12.54905 | -47.04859 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33e6fb39-a032-3be4-a14b-5ab8317216b4 | -9.38779 | -61.52986 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 597484d4-43ab-39b8-8602-88ce54e277e4 | -12.57401 | -47.07838 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 294329a7-3e1e-3180-8cfe-6d194e32df9a | -11.65235 | -48.33135 | 2025-08-12 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5620218-6f99-3bd0-bb26-690a6c093b9c | -9.20324 | -59.66243 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9b16b84-7cdc-3813-9da4-3618db6ed949 | -12.67181 | -46.97832 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13d07ed5-48dd-3733-bd4a-fac4368bedbd | -13.89863 | -51.83646 | 2025-08-12 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4060388-da7c-3e14-9e4d-21ae01400c4a | -9.37921 | -61.52971 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 683f9ec9-e59b-378a-855d-f08bdc64f9df | -13.87971 | -45.57844 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88a138ca-86e0-320a-ba34-fd81a37ceca4 | -9.92901 | -60.48157 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8676fed7-5d83-3848-8af2-fa48a2eb8f99 | -12.56812 | -46.99716 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d0b73bb-1c27-3df7-9550-d31d99291906 | -10.62826 | -65.00551 | 2025-08-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75c3774f-3775-3d09-be6b-ffc16bd23a5d | -14.694 | -53.7216 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bdf1d90-3ac2-33d0-869c-99e9daed5c42 | -12.49893 | -46.33916 | 2025-08-12 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 966d2ef3-f5d6-3af8-a703-6de39ded4005 | -11.67694 | -50.13309 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67298836-6810-3979-be3c-aaa92e7a1c20 | -8.93495 | -60.74438 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93c00ae4-2993-3e5c-8722-08f5ed2729e1 | -12.67253 | -46.97233 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7a74a82-eb76-3428-891e-d90c29d1f3d0 | -11.70599 | -51.60256 | 2025-08-12 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70f33529-15ad-3e92-9200-b5c56869d01a | -9.373 | -61.5363 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23478431-d797-3c06-a126-4163a7abaab4 | -12.56369 | -46.99034 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8651cb35-9491-3fb2-96e6-328973c7444b | -14.6905 | -53.72107 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffcd34b2-d7e2-39bf-a4f4-0aac8b3d4500 | -9.17976 | -59.65836 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24d7b395-c83c-3258-9fda-f3b1850d13a0 | -10.76012 | -48.78843 | 2025-08-12 04:59:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6ac69871-6c5d-362e-80fd-298f8fe00ece | -13.60154 | -46.92606 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04e068a6-422f-3f28-b97b-78256be62113 | -8.93359 | -60.75229 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93582c13-d8c3-36f5-8740-40dd425bbd4f | -11.19161 | -55.01499 | 2025-08-12 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5c96cc3-c2e1-330e-a64a-67e8ae5d1fef | -13.63203 | -46.93866 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d86b45a-e889-318f-b8a6-3ece853fd451 | -11.45209 | -50.16768 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a36b19c-0908-3633-86dc-551295933700 | -10.35932 | -50.82533 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12fa7db1-bf7f-36d4-af41-2d6eb5bbec58 | -10.34818 | -57.60532 | 2025-08-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74072d15-a763-390c-b40b-e76da2a43f64 | -9.93308 | -60.4823 | 2025-08-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f09a5a4-d90e-30b5-950a-19121def7a3d | -14.63918 | -45.85568 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 597b40c3-964d-36c4-a0a9-a4dc25b00dde | -8.92245 | -60.76662 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c786f490-4bd3-3fcd-b925-0f7b3de65a3d | -13.63283 | -46.93168 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1964d3d-a8b8-3863-98e9-5a6f1e9a2855 | -10.62759 | -65.00906 | 2025-08-12 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f4aa2ea-dff1-3ac2-a353-64912ef53790 | -12.67109 | -46.98431 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9047f28c-4533-3969-ab95-40de9965487d | -11.72156 | -48.34619 | 2025-08-12 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 699ac362-2287-3998-8ea6-471f8dbdfaa3 | -9.54039 | -66.14204 | 2025-08-12 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 015c89cf-5bc1-3c2a-b886-3743faa34409 | -10.76663 | -48.80753 | 2025-08-12 04:59:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48000d26-8bd7-3d2f-8775-a8d58c397b23 | -10.36181 | -50.83566 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15bcd911-575c-3930-9328-93c362909105 | -8.93291 | -60.75627 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9559916-7f55-37fb-beba-dde93aafeb40 | -12.56227 | -47.00217 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53715d6d-e104-3dc2-9e0a-ffb34cd08b8a | -12.57179 | -47.01029 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cb1a897-ddd7-3f9a-9094-4ac56216f898 | -11.02693 | -45.07222 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc375562-604b-3c03-a33f-f771aa480448 | -15.57682 | -47.32401 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e80646d-81c6-33cc-9f4a-c47675db3c21 | -13.06979 | -56.8476 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 393a3733-d5b4-3484-94d5-455ec890fa53 | -13.06646 | -56.84703 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1414c0d0-128b-3cc1-8fb7-9acdfe56895e | -11.12407 | -50.46134 | 2025-08-12 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 493af5f4-7464-373f-ab12-ae753c80da11 | -10.35612 | -50.81989 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b8ad42d5-ba00-37fa-adbb-67e99a21416f | -8.93208 | -60.73576 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08bdc1e0-2ed9-38ca-9b05-f7160097dd1e | -10.3445 | -50.81809 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 184156d8-e775-35e6-a024-ea74ce798825 | -13.62719 | -46.93504 | 2025-08-12 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf8fd758-6a15-34d0-82c0-4f3c27af6386 | -12.57474 | -47.07232 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7527894e-2a46-3831-bf45-dbf48976662a | -11.68519 | -50.13428 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f86c460-37ac-3c56-92d3-956872d8cded | -14.04015 | -47.41423 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3d417f05-3cb5-3317-92ad-477847a648ab | -10.75951 | -48.79302 | 2025-08-12 04:59:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ed3702e-0129-3161-a10c-542f94390208 | -12.57505 | -47.02663 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a67e70c-cd2f-397c-8a6f-efcf97e27ee4 | -12.57063 | -47.01983 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3509e7a3-d87a-3cf6-9fca-12481de5dec3 | -11.02743 | -45.06807 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a543d85d-172e-3514-b225-dd8e16e9a82a | -10.347 | -50.8285 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53db18c9-13a6-3a90-938f-64bcb08fbb43 | -10.34769 | -50.82361 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1580070-fd5f-3553-a58c-dc469925e303 | -13.34922 | -50.24478 | 2025-08-12 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 46397509-e817-3c61-974b-e1fac9fa6129 | -12.55893 | -46.98615 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60899f90-bf09-3491-9360-31e824e69579 | -11.72151 | -50.08551 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 551fb99b-a6cf-3638-ab8d-d2a6cd2ffb9e | -11.33514 | -54.63575 | 2025-08-12 04:59:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef007b1f-a976-3bb8-8686-54954d969e31 | -11.00845 | -55.07941 | 2025-08-12 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fc849f3-bf1f-30ae-b556-99e08c62621b | -9.37996 | -61.52535 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 267c5fed-a38a-3976-80cf-fa3586200b77 | -12.56071 | -47.01517 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5dd781a7-b1d8-3430-80b5-e404fd4abc87 | -12.55657 | -46.98951 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5078581b-451d-3d25-bc04-e7b377c5019c | -15.58249 | -47.32113 | 2025-08-12 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1dbc2d8-921e-3f0d-b35a-d6d5ea93c9ef | -13.0637 | -56.8429 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a636d414-5679-3b83-8e06-6ffb7a1f23b9 | -14.69514 | -53.71366 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0ad3e7c-1f64-3086-a7ee-784a9684956b | -12.56738 | -47.0033 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d994124f-b7af-3a18-8ebf-13d9e1a6dacd | -10.74224 | -58.01887 | 2025-08-12 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aadd911a-54a9-3fed-94a8-7006be1f1e15 | -9.68358 | -63.59761 | 2025-08-12 04:59:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 64d7a7ee-30fe-3dd9-866a-67b01032e6c0 | -14.11292 | -45.39193 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1d19890-e476-30ab-a5ef-5d70cab468cb | -12.55112 | -47.0514 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16d9b026-af2e-3574-bfe9-ec9572705841 | -13.04646 | -56.84373 | 2025-08-12 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aec3761f-86dc-35fd-80e7-fa9abfe0683b | -14.687 | -53.72053 | 2025-08-12 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c44960b-03fd-3745-b9f2-134f3d024e2e | -9.37897 | -61.52835 | 2025-08-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebd2ab65-6003-30d3-90fa-dec4d3d0fc32 | -12.55821 | -46.99215 | 2025-08-12 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 85ccdc57-8edf-3714-b787-3a5cdf4e9023 | -10.36847 | -50.81653 | 2025-08-12 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82902724-7487-34e1-b376-de5fa09a8e8b | -14.11182 | -45.39277 | 2025-08-12 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README27.md)
