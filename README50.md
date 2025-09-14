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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ea63f0b-8010-38f0-a58a-beaa787e5048 | -15.2288 | -52.81951 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aeb554a2-0f4f-306a-8f2d-78be427d95b5 | -17.56054 | -46.50811 | 2025-09-14 04:42:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a69865e-01f3-3496-91b2-80a64103b443 | -18.06356 | -45.41782 | 2025-09-14 04:42:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 759725e1-4270-36fa-a815-b501168699d2 | -15.11021 | -52.49652 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94ee3f73-f591-3c85-b2e6-2537d6e28883 | -17.42192 | -49.23577 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c0c1fe-8937-34d8-a178-94e06b1ff542 | -12.92479 | -54.7418 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4a2fc55a-f015-3d50-94ea-0cd61d931b5c | -15.2696 | -51.40254 | 2025-09-14 04:42:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ba2b30f-9a7d-3cbf-b61e-ec1d6edaaf64 | -16.3361 | -51.52051 | 2025-09-14 04:42:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de310d75-5f69-3956-a2f8-82e26eb32401 | -12.94632 | -54.74385 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5478000f-292e-30f0-bd00-558555496263 | -14.47976 | -47.32985 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba462c0e-9934-3051-a18d-fc797c9edbfc | -14.38404 | -52.92153 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aff91291-6719-395b-9475-416fe2297902 | -14.19374 | -46.1638 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12d005c7-9ff5-3487-8866-266e71b65742 | -14.61978 | -52.07206 | 2025-09-14 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b073629c-d414-322c-b7ba-43f098046f7e | -17.58625 | -42.73774 | 2025-09-14 04:42:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3418ea59-51f2-3895-9ee5-1cfc336be49c | -17.7961 | -51.72939 | 2025-09-14 04:42:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 62281687-7593-3ae2-bcc1-02b1224f0c57 | -14.18614 | -46.15899 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84bb00d2-dd0d-3084-b3f3-a518704e131d | -15.28811 | -53.77354 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 835715cc-18df-3fdf-85ed-3870d88dc441 | -14.42742 | -47.34647 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4d43ed08-3ec3-3a26-8874-1d73b70b7918 | -18.26411 | -49.46183 | 2025-09-14 04:42:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 16705d8c-27c6-319f-80c4-f84aafaebbaf | -13.50517 | -51.73997 | 2025-09-14 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 695d8cf5-3453-3dbc-abd2-14c648cf0c15 | -19.70695 | -45.43615 | 2025-09-14 04:42:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25aef296-ae50-3136-9caa-da925ef0c510 | -12.91591 | -54.74942 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02fe5a56-9a80-3b8b-9302-137c2b766d2d | -14.47633 | -47.35476 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 052b38bb-5613-36f2-9a96-f2fe219b1e2c | -15.09095 | -52.46761 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7190824-63d7-3ab8-9d90-2d7e5a4e94be | -14.93709 | -55.96262 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c8d535b-aec6-3149-9353-a119f9c6e19f | -14.33264 | -46.61952 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84b7408e-1971-3a6c-b3e5-e92fc51d0d5a | -16.18929 | -43.12862 | 2025-09-14 04:42:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c38be230-d4ab-3ce1-8092-79539ca30ba5 | -15.60439 | -47.94079 | 2025-09-14 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bee0927-337b-31e6-9240-d78927e2c381 | -15.55376 | -54.79763 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 165eecc5-0285-3542-90f6-b26aa9e08f49 | -14.19989 | -46.17945 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d173cfd-c742-3901-b9b1-33ff0e192d13 | -17.36326 | -52.90368 | 2025-09-14 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c86f1b8e-c2a4-30ac-992e-db7eaffa1122 | -14.31608 | -46.08715 | 2025-09-14 04:42:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baa12c45-5b91-3dfc-a6fc-f16e4299839f | -12.70605 | -54.70187 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| add3fc33-bfc7-39c9-a3b7-fa838eb31ca8 | -15.70296 | -47.02097 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da235d0a-c9e8-3158-9507-073d2da48c5b | -17.28407 | -46.09749 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ae9d0ff-e74f-34d9-873d-6c648f280310 | -18.0004 | -46.96475 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a163c2c2-3a1f-3c6e-a62f-5b288bf29d2b | -15.67202 | -49.89775 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5df49d9e-c438-3f9c-a157-a2568f668d2d | -15.5836 | -54.74541 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fa3eeb3-7f9b-3954-b334-34162c5bc1b3 | -12.67226 | -54.67758 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c5d2d32-7de9-3367-97be-cb68e20abe7c | -15.54663 | -54.79627 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3126d95-5565-3ddd-b454-df65e6a8a0d3 | -14.63546 | -46.36514 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7aaf85fe-45c1-3541-9852-5b73975d46fa | -18.91011 | -47.01257 | 2025-09-14 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5419900d-ab6a-3fac-8818-c1bd8a5c3cec | -12.9196 | -54.75005 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc304b27-7ec1-320f-9987-635fd54dee20 | -14.15744 | -46.25199 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1b040f73-e7f6-3987-9968-9de676b97446 | -14.63495 | -46.3689 | 2025-09-14 04:42:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb0dc597-379c-3671-9275-277c0627fbb7 | -17.98922 | -46.95558 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f597944a-813e-357e-b732-b25ecc68f7d0 | -18.06375 | -50.73925 | 2025-09-14 04:42:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f8295e7-d86e-38ba-8869-867fe19a63d3 | -17.42075 | -49.24418 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c7fee1c-62be-3cb0-b66e-f64f18916941 | -12.92404 | -54.74624 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cf4098ed-83e4-3301-890e-d56185396ef9 | -15.12145 | -52.46904 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6059ba67-0704-39d3-b4cb-6c34f3b17cda | -15.15861 | -52.47152 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a8b9ebd-53d0-337d-8d06-5d4824d7c342 | -12.68254 | -54.68397 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f8a46899-e848-3d33-964f-1d220fd306b7 | -18.29298 | -52.10167 | 2025-09-14 04:42:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4886726b-4fa3-35fc-acbd-25629e2d0d2d | -17.83164 | -47.77213 | 2025-09-14 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31847d66-ccb3-3c94-9776-e7c40adb0596 | -12.70822 | -54.71145 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9e8d566d-a9a3-313f-92a8-c57d698d4083 | -15.65095 | -47.04751 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6912899b-2b68-3d72-9ba9-3b427f080b93 | -17.26084 | -47.24109 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4e0f98bf-2be3-337b-aa33-a050614fc0b7 | -18.36528 | -45.0365 | 2025-09-14 04:42:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4724411d-604c-3e70-89dd-3245d960e8fc | -16.4407 | -45.68701 | 2025-09-14 04:42:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c63f681-4cae-38f6-8c45-6b502664044d | -14.17758 | -54.05633 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d72c8721-3808-34e8-a5ae-7f1e08b3e2fa | -16.58196 | -55.17478 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 720c4f27-0a24-3af0-90c6-45fd23b3655f | -15.77273 | -53.47642 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32205840-5e06-303a-8d6f-e812c1a9a7f0 | -15.11296 | -52.50067 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90c2b87d-b613-3536-814f-474311c8e066 | -14.18567 | -46.16259 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd573539-e4a3-3e59-9211-1959961ae6bb | -22.51462 | -52.9873 | 2025-09-14 04:44:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 60238111-b18d-39fb-864b-36a4a23bf4ed | -22.29728 | -47.94733 | 2025-09-14 04:44:00 | NOAA-21 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbabb04c-ab3f-308c-be93-40c6ef00a41d | -20.26707 | -57.16127 | 2025-09-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d9092a3-9bcc-3061-b6da-e2b80be3092b | -20.85107 | -56.88577 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 49717431-7cd4-33f1-89b5-9901ddffa749 | -22.79896 | -47.80114 | 2025-09-14 04:44:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22c716c3-e821-3f5c-b811-ae0dba563085 | -24.50567 | -48.99131 | 2025-09-14 04:44:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 08c12959-05c0-38e6-900a-8bf6408eb26c | -20.90522 | -55.18913 | 2025-09-14 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1dbd845-310f-3a46-aecf-c4849ffd3477 | -23.79387 | -49.94516 | 2025-09-14 04:44:00 | NOAA-21 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 87c2eba3-d2a7-3cf4-a57e-4be4d533cba4 | -22.28303 | -45.96458 | 2025-09-14 04:44:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e9781434-9bf4-3c15-95b4-91934bcf4612 | -22.5234 | -52.99652 | 2025-09-14 04:44:00 | NOAA-21 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 8fdac87c-db2d-37ab-b067-68595c476cf7 | -21.76763 | -45.45799 | 2025-09-14 04:44:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 097deb3d-6d03-35b7-b426-2422bdc669f5 | -20.75403 | -45.27227 | 2025-09-14 04:44:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a001efc-b5e7-38a9-8bcf-1c438bc204ce | -20.13144 | -46.87354 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf46bc0e-781f-37f0-b9df-198d0b099d55 | -21.58868 | -46.80308 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 371cc64a-3877-3892-adbc-ce7b6a19c55a | -20.82766 | -56.86699 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d385fc8-51b5-395c-993f-25cc9ad0cdb5 | -22.20634 | -48.35496 | 2025-09-14 04:44:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fddc6404-d594-30c0-bfb0-ca8b9296c38c | -20.0896 | -46.89312 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0e05b68-dbec-3847-8e6b-4ae57c275e5b | -22.04917 | -47.4049 | 2025-09-14 04:44:00 | NOAA-21 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 219896b9-a5d3-30eb-b97f-d6ad67e18f9e | -22.91392 | -47.06847 | 2025-09-14 04:44:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 041e2712-8ce7-3259-9309-975f635b7695 | -20.19769 | -54.73045 | 2025-09-14 04:44:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51cab3dc-d999-3b8d-a7c0-cc76925c8bc6 | -20.7669 | -56.94852 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| afd308a8-0157-3b66-8ee8-2eaf52627e60 | -20.72631 | -56.73798 | 2025-09-14 04:44:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbbe3e25-3323-304d-a302-f7161fa07251 | -20.76864 | -56.93898 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0383fa94-b4e4-31d7-ab0f-6937f9b9f694 | -24.34818 | -50.6717 | 2025-09-14 04:44:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 10946ff7-e0bd-35cf-872c-eb835942dd31 | -22.65863 | -53.11202 | 2025-09-14 04:44:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 91b245ab-38d1-3e99-90fe-f6a714764d98 | -20.78834 | -56.9575 | 2025-09-14 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 909a3d0a-96a2-3bab-86f9-76f557d27ee5 | -21.65248 | -50.19865 | 2025-09-14 04:44:00 | NOAA-21 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 31304f91-216e-3876-ab40-5ea5da02dff4 | -20.12263 | -46.87595 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a88abbe-0c32-336c-bb68-1af00ccf0d56 | -20.10189 | -54.60893 | 2025-09-14 04:44:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 26e2bc01-f682-370f-84d5-89df368bef8e | -22.67071 | -53.12185 | 2025-09-14 04:44:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e30bfe5c-12e4-3c3d-9fb1-0c9d3dd595c4 | -23.16155 | -47.56555 | 2025-09-14 04:44:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 60882fee-7df4-3876-acd3-ec49001d220b | -25.16459 | -52.46129 | 2025-09-14 04:44:00 | NOAA-21 | NOVA LARANJEIRAS | PARANÁ | Brasil | 4117057 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8600b11d-4f8d-3774-a567-c203b2134909 | -22.79945 | -47.79696 | 2025-09-14 04:44:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6954c18b-6d8c-35d2-9409-0b9d6afc4c40 | -21.58488 | -46.79838 | 2025-09-14 04:44:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d47284ff-6489-318d-80e4-e4278143a1b1 | -20.90657 | -55.18114 | 2025-09-14 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d91aa758-a59e-3a85-b51f-bc2dc8480056 | -20.13095 | -46.87755 | 2025-09-14 04:44:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README51.md)
