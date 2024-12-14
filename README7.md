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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67bd60a4-bc37-31ad-a625-38339e80a6ed | -17.09483 | -43.80373 | 2024-12-14 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d0d6fd0-9c1b-3d20-b45d-4e83c5ea4d0d | -14.97337 | -44.40517 | 2024-12-14 04:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c466523-2b20-3f4f-b074-a5c79f7dc3b1 | -14.69418 | -52.62162 | 2024-12-14 04:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e51a086-88c6-311b-81bf-18f08024d996 | -14.84678 | -53.67508 | 2024-12-14 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfe3b1b2-aeaa-3d9a-b02d-8e1493dd9198 | -16.3511 | -43.69458 | 2024-12-14 04:04:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1415c15b-26b3-3c39-9cea-9a333bdc9f3a | -14.84171 | -53.6687 | 2024-12-14 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 102dc767-2ef8-3a74-8e65-e07e42ceb801 | -14.69335 | -52.62564 | 2024-12-14 04:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08fd4f44-a97c-3189-9f4f-cc4a4d7014c9 | -21.18139 | -43.97963 | 2024-12-14 04:04:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bc4e8013-4e95-32c0-be90-7f1ce28144d2 | -17.96428 | -44.57263 | 2024-12-14 04:04:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20097232-d290-33eb-8379-5c168ece9448 | -14.9727 | -44.40916 | 2024-12-14 04:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6651a974-9f07-3250-85d4-d4dbc6167b15 | -16.92227 | -43.59505 | 2024-12-14 04:04:00 | NPP-375D | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24e947bd-6247-3a9e-8996-16166a60e536 | -20.41661 | -43.55276 | 2024-12-14 04:04:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2630f488-dd10-3993-9e46-907172e622f7 | -14.9762 | -44.40978 | 2024-12-14 04:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e8892a4-628b-3f30-8a6f-623d2087b8c6 | -14.70001 | -52.62257 | 2024-12-14 04:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2101afef-e47b-357d-a9dd-0f9ba0021906 | -13.17964 | -53.28086 | 2024-12-14 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd996fd9-f9ea-3270-8b12-ce2bebbcff59 | -13.17347 | -53.27959 | 2024-12-14 04:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82efab63-3f1f-3b4c-9a27-65e44e8c6dcc | -14.97686 | -44.40579 | 2024-12-14 04:04:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d72731d-151a-36fd-9cc9-bdfa0dc2b3b8 | -21.20991 | -42.83625 | 2024-12-14 04:04:00 | NPP-375D | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4618d0ec-0f24-315a-ba15-ea9dee014829 | -14.69916 | -52.62668 | 2024-12-14 04:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c357b983-0920-33c2-a354-16fd3f0729de | -16.83681 | -46.12809 | 2024-12-14 04:04:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b98a72b-00a6-3586-9f3c-9fe7b77c5611 | -14.69251 | -52.62967 | 2024-12-14 04:04:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3275fd14-7809-381d-8824-15791c8cc101 | -15.16023 | -43.57629 | 2024-12-14 04:04:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fcea7b11-2630-3b1d-8262-4c9acce9ffca | -14.8407 | -53.67352 | 2024-12-14 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 994e6557-74c2-375e-b42f-c002646ac885 | -14.8478 | -53.6702 | 2024-12-14 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3d56abb-c08e-39da-9c2a-c54f238bf720 | -15.57017 | -47.85355 | 2024-12-14 04:04:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03f34f5a-4736-3118-9c68-df346d808274 | -14.83433 | -52.86887 | 2024-12-14 04:04:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05186f6a-c638-3c77-bad7-88206f60ca3f | -22.99693 | -46.9844 | 2024-12-14 04:06:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 907b5146-1f22-39fb-9bc6-969c16f5cbef | -12.5499 | -57.6996 | 2024-12-14 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6e7a0a16-31e5-33ba-b246-44d543cc6749 | -4.1057 | -46.6142 | 2024-12-14 04:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 51dbcd42-d220-301c-9ac0-68a4c89e3c7f | -12.5497 | -57.7196 | 2024-12-14 04:10:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3080bf83-4271-3991-9dbb-2d5d47bfd90c | -12.5499 | -57.6996 | 2024-12-14 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b603120f-cfe2-3b0d-9e80-c26991071d45 | -4.1057 | -46.6142 | 2024-12-14 04:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| b2320ae6-389b-384e-9719-529e0945a694 | -12.5682 | -57.7579 | 2024-12-14 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4a2e1b9f-aa12-3bd0-a254-fa1f4180c990 | -12.5497 | -57.7196 | 2024-12-14 04:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 4e7503c4-73dc-3d39-a667-13adea0b258a | -4.12264 | -43.24331 | 2024-12-14 04:23:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 499f94e9-1201-3c41-b8b7-c2af48647d61 | -3.79857 | -46.70694 | 2024-12-14 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 193cf8d4-aa53-3bbc-99c6-128d87c5c2f4 | -7.99366 | -39.42742 | 2024-12-14 04:23:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34d3a950-2aeb-3cfc-aff5-7fb222103d68 | -4.17438 | -42.43629 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63127ed1-4b7c-3a17-8847-7958f5cf6e81 | -4.16715 | -42.43519 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| fbdc78da-8806-3824-8383-8d28b7a21a73 | -3.56466 | -44.67861 | 2024-12-14 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89ec883a-9f44-3e89-8d44-12cba3975395 | -3.73 | -39.95546 | 2024-12-14 04:23:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b4d3641-260e-39f6-a7e1-abd7b467a958 | -4.49573 | -42.86044 | 2024-12-14 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df377f50-c0c1-34c4-8577-4ee72e22abec | -2.75005 | -45.71364 | 2024-12-14 04:23:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd5e68ce-6ae7-35e5-a010-4e0b46bcf4c0 | -3.47727 | -43.34312 | 2024-12-14 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40726f7a-5951-3777-9225-896ba727a6e8 | -4.24901 | -41.92525 | 2024-12-14 04:23:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d652573b-68a2-35f2-9da5-64b5ea058d0d | -2.86276 | -46.7217 | 2024-12-14 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40f73bdf-16b4-31d2-aca9-eb95670c4ef1 | -6.47953 | -54.92699 | 2024-12-14 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c50110-f4a5-3d15-860c-7034a39742cc | -4.52492 | -42.07324 | 2024-12-14 04:23:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d4503946-f423-385f-bbc8-56b986f1e607 | -7.99717 | -39.43056 | 2024-12-14 04:23:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 17d1c966-9f46-38fa-a4ff-37f394958cb5 | -2.99762 | -44.41899 | 2024-12-14 04:23:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2282257d-1e60-30b2-a14d-62dc22c18c87 | -3.56419 | -43.66352 | 2024-12-14 04:23:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4a5a635-2dda-3f92-82c7-b821852d3b39 | -3.79521 | -46.70643 | 2024-12-14 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f712c70-0545-304e-ad4a-8c834b802852 | -3.795 | -46.83746 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d53c5949-1a73-3336-9022-da01049f9921 | -5.2402 | -37.69443 | 2024-12-14 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d7b57bbc-fdf6-3b2c-9e5e-90065567a5f8 | -3.29338 | -42.52139 | 2024-12-14 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71b11095-f228-3da0-af02-b49db80dae29 | -4.14766 | -44.28863 | 2024-12-14 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fdebd08-a63d-3d00-96c9-2ee3cc664f5f | -7.99432 | -39.42277 | 2024-12-14 04:23:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0b258f8f-0944-358a-ba4a-4ec3011a08fa | -3.30389 | -40.55445 | 2024-12-14 04:23:00 | NOAA-20 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d724435-f14e-32e3-a181-8e4db60479d1 | -8.13654 | -43.59328 | 2024-12-14 04:23:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89cd53c9-130f-3a9a-9859-2f2281287e62 | -3.84994 | -46.51287 | 2024-12-14 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8528942e-81b6-3e4d-9570-0c3499e9a57a | -9.28143 | -40.17792 | 2024-12-14 04:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3e19c0b-24ee-3572-a267-9e458c76cfdf | -4.01566 | -44.5511 | 2024-12-14 04:23:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a85cc954-49a1-3222-8cfd-0762eca14a38 | -3.62104 | -46.71539 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 368ad921-a4f6-3f69-997b-6825967331b8 | -4.17502 | -42.43213 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 83432f78-42c3-3f39-8a79-95a6f1c9102a | -3.73826 | -43.1286 | 2024-12-14 04:23:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd38d32b-69e5-3add-86fa-f10c4d6343a0 | -2.92141 | -41.46967 | 2024-12-14 04:23:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f14fea8-a5f9-3ccd-8304-d0e485297702 | -3.38615 | -44.15054 | 2024-12-14 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57295694-ca63-3b06-baf0-fcf9706e256e | -3.68877 | -42.60593 | 2024-12-14 04:23:00 | NOAA-20 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d389bb4-b16e-31c0-97a9-784d1bce83c5 | -5.24062 | -37.69159 | 2024-12-14 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c81ebf79-5884-3c04-a240-e6acfd79473f | -8.94162 | -44.24744 | 2024-12-14 04:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c85468a2-3f0e-37a3-b581-099a28fb2b65 | -4.14587 | -44.28853 | 2024-12-14 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65ffa91c-7c2d-3718-8d20-213db571d1db | -2.53737 | -45.38048 | 2024-12-14 04:23:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52036800-a9f6-34c0-abd6-db798fc35242 | -2.26008 | -44.8121 | 2024-12-14 04:23:00 | NOAA-20 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f06ffc1-7867-3923-b200-255a56490385 | -3.00428 | -44.42002 | 2024-12-14 04:23:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec46460-6668-33c9-80dc-1b75f5834b96 | -4.40022 | -41.43758 | 2024-12-14 04:23:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 86bbca12-ed51-3e8f-bbd8-4f9f805072f9 | -3.29044 | -42.5168 | 2024-12-14 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 583dc8fd-c608-34cb-b604-5ad92193ade1 | -1.7217 | -52.55691 | 2024-12-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0e583a2-e3bc-32ee-b8ff-ac1dac2c0d36 | -1.87348 | -45.51942 | 2024-12-14 04:23:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f70ab008-1103-33fd-9396-10e43f477724 | -7.9976 | -39.43279 | 2024-12-14 04:23:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 39f30d2d-766a-348b-acb8-54a69a1c9b37 | -3.88063 | -44.41887 | 2024-12-14 04:23:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d103a528-4e03-3f15-856e-d9460b697807 | -3.88008 | -44.4224 | 2024-12-14 04:23:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce88e5e7-2c92-377e-88fb-eb17b16d53ce | -1.54299 | -45.65498 | 2024-12-14 04:23:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 367dbe3e-d6ef-35c4-8874-9fb1f60fb231 | -4.52559 | -42.06885 | 2024-12-14 04:23:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ffedafa8-e0f1-3962-980e-96c545527d78 | -3.62161 | -46.71183 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c363cea-efef-3e9c-be7c-8d032b991a21 | -3.79107 | -46.84053 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d98e4ee1-c40e-3307-a0bc-971a71774b2f | -3.38895 | -44.15461 | 2024-12-14 04:23:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 719ec8d2-f2c9-3922-b6fd-c5a7f8d2807c | -3.87728 | -44.41835 | 2024-12-14 04:23:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d0c8ea0-6b12-330a-a3c9-bc6a1b9e16b1 | -4.17077 | -42.43575 | 2024-12-14 04:23:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0a5bfc2-344d-324f-a463-bd2f7c2f88fc | -6.48007 | -54.92389 | 2024-12-14 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abf05f7d-2c9e-352d-9b32-f05fc25adedc | -3.45156 | -40.8167 | 2024-12-14 04:23:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1379ef43-0834-33f3-9400-2bd2f2a9a3aa | -3.24526 | -45.67479 | 2024-12-14 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df53dea7-eadc-3331-8eff-f6b470d81caf | -3.29757 | -42.51789 | 2024-12-14 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c4cada6-b7f1-366e-b0d4-3f483be1bb34 | -3.62217 | -46.70828 | 2024-12-14 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40ca4e33-964d-3961-abc8-12377bf51756 | -1.72088 | -52.56207 | 2024-12-14 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83c074ab-04fc-3a5f-836f-231399a15596 | -4.019 | -44.55162 | 2024-12-14 04:23:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 524f367b-ce8e-34bc-938b-5a09f5e2ae93 | -3.4555 | -40.81727 | 2024-12-14 04:23:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 68152d22-83cd-3f5c-a9aa-13b40c80490b | -3.87673 | -44.42188 | 2024-12-14 04:23:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63c7326a-0e11-3228-8a0e-a2b674876ecc | -9.25667 | -40.95705 | 2024-12-14 04:23:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 57c22eba-a6bf-3ba8-9460-6f87d220a895 | -9.27756 | -40.17299 | 2024-12-14 04:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 28e99b9b-764f-3a4e-801d-7dcbeea9e916 | -4.24529 | -41.9247 | 2024-12-14 04:23:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README8.md)
