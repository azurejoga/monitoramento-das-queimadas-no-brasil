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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72cee6eb-66db-37a8-845d-aaedf59ed765 | -13.7624 | -45.3519 | 2026-10-10 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 423.9 |
| 98042d4f-320a-3890-85f0-b89987f4f8f9 | 1.3162 | -50.8505 | 2026-10-10 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8c5c9696-70e7-3a95-8836-97f7962125ab | -2.4806 | -56.0875 | 2026-10-10 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 64ddd1a5-e63b-304b-8454-46f08fbe6cd2 | -8.9311 | -45.1355 | 2026-10-10 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.9 |
| e133749f-ffb6-3796-99ba-6dafc7b77bbb | -1.6579 | -55.1912 | 2026-10-10 15:00:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 36cdb3ef-5fff-38b5-8782-4790d3582d61 | -9.1257 | -67.8322 | 2026-10-10 15:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f5947541-f582-3ed8-84dd-aa7300aea377 | -11.47 | -43.3824 | 2026-10-10 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| d0fb8d0f-f309-3a6a-8b1f-918ff40f729e | -12.7072 | -43.0611 | 2026-10-10 15:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 118.4 |
| 64ad80f5-9dee-391f-931a-5bfd543aae46 | -1.3447 | -56.4175 | 2026-10-10 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 30ae6ae3-0b25-3286-8258-e7388757e8e4 | -2.4806 | -56.0678 | 2026-10-10 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| ce91a039-b946-3dc8-840e-4ac2047526ab | -13.7819 | -45.3485 | 2026-10-10 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 166.3 |
| ab83caa0-9fdf-3ee0-8a54-1f8eb47b408c | -13.5062 | -48.6046 | 2026-10-10 15:00:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 47303b09-6604-342a-b56f-d969b629a017 | -3.2755 | -54.1819 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| da36c800-2064-3a0f-95c0-bc655964f51d | -2.7243 | -54.1552 | 2026-10-10 15:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2fa70de4-a029-36b5-9091-beb52ad73b8a | -3.1284 | -54.1857 | 2026-10-10 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 7fcd6697-d014-329b-8efe-304352a864be | -9.5541 | -45.2239 | 2026-10-10 15:00:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| fba277d5-1bd6-3c0d-aeb5-718d1fd9bb9e | -1.6395 | -55.1914 | 2026-10-10 15:00:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| cc8820a6-2848-3659-ab7d-3a45c4fec471 | -3.2571 | -54.1824 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 47742f45-afa0-3ff5-8dfb-81a417fbe0ef | -11.8692 | -43.5805 | 2026-10-10 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 512c1ab5-16e4-3356-bfe9-2fad54d03dfb | -1.245 | -49.3384 | 2026-10-10 15:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ca482b07-521f-3c5c-a12a-c24f33e8f514 | -3.496 | -54.196 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a72e3d41-425f-308a-b406-ea617928de30 | -3.11 | -54.1862 | 2026-10-10 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 24a38231-dda4-382f-9a8d-cf19a295fc73 | -3.2532 | -50.4108 | 2026-10-10 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| c42e041a-49a7-3280-983b-4f59fefca776 | -15.3832 | -41.9029 | 2026-10-10 15:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 160.7 |
| 973974ea-b025-3cee-bf4b-54e922941ec8 | -12.1819 | -45.3518 | 2026-10-10 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 34707ed2-46e7-3140-bc78-19301903be4d | -1.2907 | -55.7295 | 2026-10-10 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 6206fa2b-ce64-3caa-975e-85e0c5e2ce06 | -2.8712 | -54.1719 | 2026-10-10 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 04690274-d019-3b00-bf56-19fec984fc36 | -18.3125 | -42.3901 | 2026-10-10 15:00:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.8 |
| 21d9847d-1b89-311b-ac5a-982057185c32 | -11.0332 | -45.4246 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| e1671992-c3b3-317d-8219-aa48056cad24 | -9.9384 | -44.8791 | 2026-10-10 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 795d6a5c-eebd-3ebc-a241-7dfc424a6931 | -11.0328 | -45.4475 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 03a0d8c3-cf5a-3d0c-81a8-d42a09b321b9 | -11.0144 | -45.4042 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 14947704-6586-3181-bc2b-2aeeba76ebd4 | -1.2175 | -55.6512 | 2026-10-10 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 432462c4-e512-3ff0-a570-48b89631549d | -1.254 | -55.7496 | 2026-10-10 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 68a0bf10-a5f7-35ab-b161-ea4c8ff65a40 | -10.9575 | -45.389 | 2026-10-10 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 8ad21125-1f8e-37d2-8960-fbaadf41f756 | -0.8768 | -48.7033 | 2026-10-10 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ba3fe7f1-ff94-3a9e-81d2-f416cb479805 | -10.8591 | -50.6692 | 2026-10-10 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 46ebdaa8-6c07-30ae-bda8-6ce7d30a2601 | 2.4212 | -50.9557 | 2026-10-10 15:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 29ec685e-4d9e-3b01-b0bd-84fa00cdec76 | -3.0375 | -53.8865 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| c1e5815b-3a47-3e31-9c23-12c31c5fdf86 | -3.1285 | -54.1657 | 2026-10-10 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 8908a9e5-1de7-35a4-a7ec-bc3fdb3ef0fb | -11.3823 | -54.0434 | 2026-10-10 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 13cd53c0-1d32-3a72-95d2-6286032612dd | -15.0713 | -41.7982 | 2026-10-10 15:00:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 1209f065-5f98-3d83-b349-bd2c667947b7 | -11.3447 | -54.0264 | 2026-10-10 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 619d9b9c-2308-30e8-a385-3c4161682bf6 | -8.9501 | -45.1334 | 2026-10-10 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 4ff485d0-0805-3e3c-ab54-3f4961073b15 | 3.8754 | -61.3187 | 2026-10-10 15:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8ea2adba-05fa-3c2f-85ce-00b34e36cdb2 | -8.9119 | -45.1605 | 2026-10-10 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 5cb0b7b6-7fce-3e08-88c8-630ebb6cbfe2 | -18.3327 | -42.3849 | 2026-10-10 15:00:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.1 |
| b228c3c4-c90f-3f2c-ad1d-eefc417a0d06 | -1.3264 | -56.398 | 2026-10-10 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 88550215-2118-3b60-ad49-58481571ffcf | -1.6578 | -55.211 | 2026-10-10 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 1852753f-5edc-35ff-a30a-168c1fb76728 | -11.9476 | -43.497 | 2026-10-10 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 160.6 |
| df085dbf-7a44-398b-ba10-6cfa98644176 | -3.1059 | -50.3105 | 2026-10-10 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1e13dbf1-2765-32c7-b666-60595dbf37be | -1.3264 | -56.4176 | 2026-10-10 15:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 75d32ac2-0fbc-369e-a80e-9781dbadf8d8 | -2.8491 | -49.8763 | 2026-10-10 15:00:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| f1b41d60-c78d-3d3c-bd3e-43baac6e14e7 | -3.2717 | -50.4102 | 2026-10-10 15:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 33e0d6d2-ef6e-3ec0-97b9-a1e3e1695cfc | -11.3633 | -54.0452 | 2026-10-10 15:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 5e7c2c87-764d-3560-a0ad-e3a95c3d182a | -6.5519 | -61.4177 | 2026-10-10 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| b6e0ba04-4821-3f3c-9a3b-ed52a80950e4 | -14.7318 | -48.2167 | 2026-10-10 15:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 9e314f2c-0995-38ec-9d8b-3d39610d2f78 | 4.2607 | -60.913 | 2026-10-10 15:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 0117cc5f-3033-3594-9ccd-c9a5114224ea | -1.2175 | -55.671 | 2026-10-10 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a88aa185-2947-374b-b54b-0f8bf59f5499 | -12.4837 | -51.2959 | 2026-10-10 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 63d32c4c-6445-35ad-a9e4-db26ebed8e65 | -10.7302 | -45.305 | 2026-10-10 15:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 160.0 |
| cb1be505-7ed1-3a79-9292-f11854fdb18c | -15.1088 | -46.9343 | 2026-10-10 15:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 961fa3cb-837a-32fa-9be0-094138f4c494 | -10.2488 | -49.6636 | 2026-10-10 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 26582aaf-71f5-3db3-acd1-41e411b665f7 | -3.0531 | -54.7479 | 2026-10-10 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 18537966-4ce1-3603-a7fb-25be3ba45d31 | -3.0008 | -53.8874 | 2026-10-10 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c565e59c-a4f3-361c-a35d-92c233ade503 | -10.26189 | -36.44677 | 2026-10-10 15:03:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.7 |
| cfee67e2-c983-3262-9070-319f1ca1b197 | -5.19916 | -36.94486 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 18.0 |
| aecbb860-c85d-36a2-b6ce-8506e93caa6e | -8.95221 | -35.18284 | 2026-10-10 15:03:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 4e3596e5-4d68-36d7-9bc8-2731a7380923 | -10.25534 | -36.44085 | 2026-10-10 15:03:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.3 |
| e167addf-8a08-30fb-95ac-6c4f4ad87820 | -5.12837 | -37.09821 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| a44475f6-982a-3e81-a3fc-9279da28201e | -8.33733 | -36.06137 | 2026-10-10 15:03:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e8261d1a-08c8-3e48-b15c-c993f8de5815 | -5.19319 | -36.95171 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 08ddde2d-352a-3361-90cd-f977ff134c25 | -7.35142 | -37.31578 | 2026-10-10 15:03:00 | NOAA-21 | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 180388fd-3cef-37b5-98d4-48de6410bd80 | -10.26314 | -36.44679 | 2026-10-10 15:03:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 9098cdeb-dcbb-3150-898d-b90f4df401ad | -8.70306 | -36.83434 | 2026-10-10 15:03:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 40a6ef21-72d5-36f6-b3c3-ed0a1b820b0a | -10.26115 | -36.4401 | 2026-10-10 15:03:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.7 |
| b38eb161-a76c-3253-a36b-02fe25c4e235 | -8.56329 | -36.43708 | 2026-10-10 15:03:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| eb3726bd-eb46-38e0-bf7d-994ed77b964e | -5.19713 | -36.94589 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 1314859c-e9bf-35ac-9837-4c148e576813 | -5.19801 | -36.95207 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 93d5450b-5697-3b60-bc61-d90d5ad38714 | -7.1753 | -35.41285 | 2026-10-10 15:03:00 | NOAA-21 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 19.7 |
| f1ccb965-319a-3521-8172-af012ab59c9a | -10.26234 | -36.44012 | 2026-10-10 15:03:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.3 |
| e9254009-1fd8-3cdf-8133-542a12c2d6bb | -8.33467 | -36.0636 | 2026-10-10 15:03:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e2e23d5f-845c-37b7-9182-427cf5399955 | -6.18801 | -35.16864 | 2026-10-10 15:03:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 5f8749a1-4988-3420-b375-12842c9a80ae | -7.17248 | -35.4148 | 2026-10-10 15:03:00 | NOAA-21 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 2ad5f9b1-3ab9-3afd-adf7-54bb90b5db9e | -5.24677 | -36.36983 | 2026-10-10 15:03:00 | NOAA-21 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 10a3a19d-1813-3bb9-9b2b-367d69e4543e | -5.12156 | -37.09929 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 1a954846-04b0-334d-87be-a0ccf17ac3b8 | -7.17318 | -35.42006 | 2026-10-10 15:03:00 | NOAA-21 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 83b5d062-20c7-3a75-a872-be356cdf5433 | -5.12066 | -37.09278 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 54.6 |
| f4323865-2164-358c-9022-724d9cc11f72 | -5.2 | -36.95105 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9c2f24cd-ae44-31ca-a37c-39fe8e949a23 | -7.27843 | -37.22934 | 2026-10-10 15:03:00 | NOAA-21 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 512e0779-68b4-3773-be22-05e125fbeb51 | -6.18868 | -35.17026 | 2026-10-10 15:03:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b63443d5-452f-31e5-b6fc-336912baaa82 | -5.12748 | -37.09176 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| ad291401-c28a-32b2-abaa-92c377ecd936 | -8.56215 | -36.43756 | 2026-10-10 15:03:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 34976483-8e61-34d7-8d5b-4bf8323ec2dc | -5.1343 | -37.09073 | 2026-10-10 15:03:00 | NOAA-21 | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 06ee0bb5-8564-3cda-9cc4-2a765da766b0 | -10.25414 | -36.44085 | 2026-10-10 15:03:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 146dbfe5-25a4-31ef-b174-2863beac0865 | -8.94785 | -35.18472 | 2026-10-10 15:03:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b9a1a2d9-553a-33ed-bb9b-5b175def8a8d | -5.93828 | -35.6197 | 2026-10-10 15:03:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5d727c0c-a5b8-32a3-9b7f-e196628bc6f5 | -7.17597 | -35.41813 | 2026-10-10 15:03:00 | NOAA-21 | GURINHÉM | PARAÍBA | Brasil | 2506400 | 25 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 71275a70-121c-3d32-8472-e4f86de4bb75 | -15.0713 | -41.7982 | 2026-10-10 15:10:00 | GOES-19 | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 215.4 |
| 3affa166-d3a1-32e4-9656-6874dd3f93ab | -9.9384 | -44.8791 | 2026-10-10 15:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |


[Clique aqui para ver as próximas entradas](README165.md)
