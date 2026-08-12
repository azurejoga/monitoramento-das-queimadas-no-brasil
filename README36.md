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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65919b48-9605-33f1-94a0-0ea6bb305583 | -13.8989 | -53.8217 | 2026-08-12 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 9d07744b-60c9-34da-a785-d58bd10a274b | -11.7902 | -51.8611 | 2026-08-12 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 36818c3d-9641-374c-8a87-bf3bb1859e31 | -15.2088 | -52.7552 | 2026-08-12 13:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 57b5b95c-f8ae-3f49-99be-9fea63ef919f | -13.8992 | -53.8009 | 2026-08-12 13:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4737c48b-ed03-33bf-91a3-55196390377e | -11.9347 | -46.3244 | 2026-08-12 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 19d9483a-f68e-36a8-b194-527d6c66cb7c | -13.8797 | -53.824 | 2026-08-12 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 190.1 |
| f1ea7a6a-5403-33c7-8532-2bd4bb190883 | -13.8989 | -53.8217 | 2026-08-12 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 080d24f1-b114-33e9-bd6a-35fd812b4735 | -13.8992 | -53.8009 | 2026-08-12 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 96ed6170-97e7-306a-9f32-3e05368bcc02 | -9.3336 | -47.5158 | 2026-08-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 3d91fe1d-7a0e-3fc8-abbc-491e11f60de8 | -9.3339 | -47.4937 | 2026-08-12 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 203cbb04-8c1e-3fcd-8868-28f55c6d6b65 | -14.4309 | -53.0252 | 2026-08-12 13:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| daf157c3-6a06-3439-bda2-a63d7e77df28 | -11.7905 | -51.84 | 2026-08-12 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| dc6d8bfe-a920-3587-ac3a-dd1c2ab40987 | -11.8277 | -51.8992 | 2026-08-12 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| ebe53b7a-099f-397d-9ae1-d06f7477ac86 | -11.8086 | -51.9012 | 2026-08-12 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| aa3d0eb1-d17a-3d87-b4aa-38e4861eb3c2 | -11.8285 | -51.8359 | 2026-08-12 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 503f35c2-8fe8-3ce0-b3e1-1f3353d97656 | -6.544 | -43.1313 | 2026-08-12 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 272.6 |
| ee4f7619-9d5f-3c05-af68-85068283e238 | -14.3135 | -51.9823 | 2026-08-12 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| df5bf99f-7ea6-3f85-9f0d-ebe9ed03f19b | -11.029 | -45.6765 | 2026-08-12 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| fc56f3cf-c834-32de-a0e0-88c37f0e2c96 | -6.5631 | -43.1061 | 2026-08-12 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ec7a095a-32bd-3bb1-b188-0b418c5d1129 | -14.2941 | -51.9848 | 2026-08-12 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| bc67c3e5-7052-3caf-94c5-c7410e490ceb | -11.7902 | -51.8611 | 2026-08-12 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| daabee31-79d5-393c-900f-0a157130edea | -13.8986 | -53.8426 | 2026-08-12 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 158d50c6-35bf-30e5-9351-3350238f98f5 | -6.5443 | -43.1078 | 2026-08-12 13:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 8bb6af5c-e2eb-32a3-8c55-f3b8297331fe | -6.5443 | -43.1078 | 2026-08-12 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| fb987191-de03-31ce-91f7-7cf75e7f4487 | -11.9915 | -46.3617 | 2026-08-12 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 536.2 |
| ddc8155f-0064-3cb0-93c1-323f50947f50 | -11.7905 | -51.84 | 2026-08-12 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 03743aac-8f53-399b-afb9-0ac36140e291 | -14.2941 | -51.9848 | 2026-08-12 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 1eaf8158-da73-3d99-9772-3b8b4cb893b7 | -11.029 | -45.6765 | 2026-08-12 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 4c2d7c38-6654-387a-8063-99d08f9b10e1 | -15.3019 | -48.8818 | 2026-08-12 13:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e069977b-6fa8-3940-9a32-216c1e07f9f1 | -11.8285 | -51.8359 | 2026-08-12 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 7ee769ea-3ee0-3ddc-b5fa-83486f72f00e | -11.9343 | -46.3472 | 2026-08-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 7930e553-df76-3fb6-a242-66a2a585de69 | -11.7902 | -51.8611 | 2026-08-12 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 89062196-8eb2-33d8-ba33-a6d13672bf7e | -11.9911 | -46.3844 | 2026-08-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 453.2 |
| 391234ea-85cd-3ebc-b1e9-32aff82c3110 | -11.8277 | -51.8992 | 2026-08-12 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 714625f7-64bc-3b63-be00-e38e5733cd14 | -14.4309 | -53.0252 | 2026-08-12 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 07cc7eb5-37bd-3380-9149-c049efefaad5 | -11.8282 | -51.857 | 2026-08-12 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 7c1d7343-b5fc-31f5-b3fe-b0d5112d08fe | -11.9539 | -46.3217 | 2026-08-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7ed6cde8-3af5-30c7-8f52-27c2cb9610c2 | -15.189 | -52.779 | 2026-08-12 13:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4d2c53ed-ae81-3811-a0c2-f2026422d57c | -11.8086 | -51.9012 | 2026-08-12 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| b6c4ef41-9eb3-3647-849f-dbcf0491677f | -11.9535 | -46.3444 | 2026-08-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| d1a4a6e9-4213-315b-95c2-03eb4bffdb5e | -6.5631 | -43.1061 | 2026-08-12 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 69a25033-52f5-319c-920b-2c2e82fb0db5 | -11.8859 | -45.831 | 2026-08-12 13:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4de59d5d-b4c2-35cb-9a4e-34d3d8b2b00a | -9.3336 | -47.5158 | 2026-08-12 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9fd672a2-b568-30b4-a670-c8a875be6d39 | -14.3135 | -51.9823 | 2026-08-12 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 57b1d4b7-b8fd-344e-8295-91dff3894d5f | -6.544 | -43.1313 | 2026-08-12 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 348.7 |
| d1a57fcb-6401-3dfb-a5cb-3c3fdbad3dca | -13.6273 | -46.2948 | 2026-08-12 13:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 8c017f45-cf92-3887-ab5d-56b7521bfe6b | -14.2877 | -45.2835 | 2026-08-12 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 59547051-13f9-3f10-a975-eb129952d84c | -11.9347 | -46.3244 | 2026-08-12 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 54dd0142-2cb3-3999-8928-5200275ebfb2 | -14.4309 | -53.0252 | 2026-08-12 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 34be2f61-43f1-3045-b70d-a38dbe43fc56 | -6.5252 | -43.1329 | 2026-08-12 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| dced2d81-faec-3542-a868-92815b9c28b3 | -6.544 | -43.1313 | 2026-08-12 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 335.7 |
| c0371e3a-c861-3b8c-98b8-1e0e9291f350 | -15.1897 | -52.7365 | 2026-08-12 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 581ad616-373a-36e5-ba6d-989263163461 | -9.3723 | -47.4455 | 2026-08-12 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 87c192e4-a863-35a2-b3fc-4dac01f9fbe1 | -11.8859 | -45.831 | 2026-08-12 13:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 2149a44e-0546-30ee-aad7-7606bd53a449 | -14.3135 | -51.9823 | 2026-08-12 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f0bc64cc-ea33-347a-8bf0-191596c89ad9 | -11.9539 | -46.3217 | 2026-08-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| ece6c809-4dbc-34af-8832-537aca4e3872 | -11.029 | -45.6765 | 2026-08-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 50303aed-41b8-3b75-b86e-0f278020d504 | -11.9347 | -46.3244 | 2026-08-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 066b2dba-b723-3e8b-a3e9-a0873932fa16 | -11.9719 | -46.3871 | 2026-08-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 8dd567c1-1280-3efe-89d3-eafb507d4465 | -11.956 | -47.3117 | 2026-08-12 13:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 70fc47eb-35a1-3f7b-b2fc-deb781f2d773 | -9.3534 | -47.4475 | 2026-08-12 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 05558364-a8c0-34b5-8a95-99f33eed248d | -13.6273 | -46.2948 | 2026-08-12 13:40:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 009b8516-a829-32ce-b04e-120ae87d3765 | -11.8285 | -51.8359 | 2026-08-12 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 0f8bb898-3505-3ad0-b40f-e1cba5117ace | -15.2091 | -52.7339 | 2026-08-12 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 21a388c3-6749-3d9a-8ccc-93d4a18df110 | -11.9535 | -46.3444 | 2026-08-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 184.2 |
| 1b675b13-cfb6-34e9-bfec-6614d58446df | -11.0286 | -45.6993 | 2026-08-12 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| d72faf1b-7cb6-3724-80e1-3901c140bdb7 | -15.3019 | -48.8818 | 2026-08-12 13:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| cca46d5c-adcf-3a56-aa30-1f10365d962d | -6.5443 | -43.1078 | 2026-08-12 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 203.9 |
| badfe9d3-a6cc-301b-b638-b4594eb9e585 | -6.5631 | -43.1061 | 2026-08-12 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| f176cec3-b5c5-3603-b66f-3bae7e239737 | -11.9915 | -46.3617 | 2026-08-12 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 475.1 |
| 893dc3f0-792d-31f3-b7d4-05d852b83e71 | -15.1714 | -52.6754 | 2026-08-12 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| bbf3bf34-a4b7-35ef-be9c-39e3e527c3d5 | -11.9343 | -46.3472 | 2026-08-12 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| a7ecf1c4-c0ca-3902-beb1-73205cbb562d | -6.5443 | -43.1078 | 2026-08-12 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 2ec90f76-cf65-3bea-a03a-89b56975cdc8 | -6.9516 | -42.0042 | 2026-08-12 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| d1b35d10-3df7-306a-9754-bbde560ab6ac | -14.3695 | -53.243 | 2026-08-12 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| f40741e3-e9b2-3acd-9173-1ddda317ed21 | -14.5229 | -52.1461 | 2026-08-12 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a8b93e33-13c3-359c-a4f9-d10566e58679 | -11.029 | -45.6765 | 2026-08-12 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 8e0d5517-fc9b-3249-a969-e3750259107f | -13.6268 | -46.3177 | 2026-08-12 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| ecf6c078-2f60-3181-a81e-0102f1b83dbb | -14.2941 | -51.9848 | 2026-08-12 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d191a44e-8643-360d-ba6d-90482ee5e6c5 | -15.171 | -52.6967 | 2026-08-12 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b065e2d6-4bb2-3d39-ae26-87f15f39e289 | -11.7905 | -51.84 | 2026-08-12 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 230.3 |
| 1c7f7fac-fa39-337e-ad73-4e6d681f2f45 | -15.1714 | -52.6754 | 2026-08-12 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0ef8b50d-931a-3093-a250-d52f0ac3fc0c | -11.0286 | -45.6993 | 2026-08-12 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 372.3 |
| 8e69a457-b8d6-3962-add9-a5741c849b62 | -11.7902 | -51.8611 | 2026-08-12 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 204.0 |
| b9ff8afb-0009-319e-83c3-59015f8b1fb9 | -5.5907 | -42.7164 | 2026-08-12 13:50:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| fc446f27-db13-3efe-8a05-f0d5e84d3541 | -14.3502 | -53.2453 | 2026-08-12 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 42bda258-a040-3220-8dc1-5d7cf54f01cc | -5.5909 | -42.6929 | 2026-08-12 13:50:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| ed87099d-c9a9-30be-8552-973eaa4e32e6 | -6.5631 | -43.1061 | 2026-08-12 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 62ae1144-53f1-3813-ba10-c73a87443c2d | -14.4313 | -53.0041 | 2026-08-12 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ec67c1fa-7ae2-39e2-990c-a3b46945e11f | -15.152 | -52.678 | 2026-08-12 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1d5b5f1b-d4ef-371c-a92d-1ecd93795ec1 | -14.2877 | -45.2835 | 2026-08-12 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 71025297-d3d6-328d-95ac-e827950531f7 | -13.6273 | -46.2948 | 2026-08-12 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 89c99047-820f-3954-af49-bf33f0b31d9a | -15.189 | -52.779 | 2026-08-12 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 141.4 |
| f32d5817-3ab4-3089-ad39-6536bdef2424 | -6.544 | -43.1313 | 2026-08-12 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 378.7 |
| 3ab8e493-1f6a-314b-9819-dbcb91a7819d | -14.4309 | -53.0252 | 2026-08-12 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 15e78760-99ca-3522-9d76-27aaf6af05a0 | -9.3336 | -47.5158 | 2026-08-12 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| e5f28b78-c996-37af-956b-8f10a3f5da0c | -13.6268 | -46.3177 | 2026-08-12 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 58ca2708-97f3-3cae-aa79-e75da7417a80 | -6.5631 | -43.1061 | 2026-08-12 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| b234e710-6693-3f0f-91e5-71ab8a7c18d8 | -14.3506 | -53.2243 | 2026-08-12 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ede36383-6650-36a5-b495-c6de2f298cc5 | -11.9539 | -46.3217 | 2026-08-12 14:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |


[Clique aqui para ver as próximas entradas](README37.md)
