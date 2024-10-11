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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b61febe-3da4-3b17-95d0-be907304bf26 | -3.0273 | -49.549099 | 2024-10-11 00:47:03 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c162678d-823e-3dc4-920c-ca9a9d214010 | -3.029 | -49.556702 | 2024-10-11 00:47:03 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2030c4f9-b15c-3f58-968a-efe011767086 | -3.2826 | -50.944599 | 2024-10-11 00:47:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e58e33f2-0706-31cd-a4ac-8b07d1336db1 | -3.2842 | -50.9515 | 2024-10-11 00:47:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd72360d-8641-3278-942f-643713632603 | -2.869 | -48.901199 | 2024-10-11 00:47:04 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88932d65-319b-3350-9626-005e3cd73d13 | -5.3357 | -60.082199 | 2024-10-11 00:47:04 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07025252-bcf3-30cc-b6da-739e53f407f8 | -5.3397 | -60.101002 | 2024-10-11 00:47:04 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c70cd63-3f40-345d-80d2-893780eb939e | -2.8006 | -48.6922 | 2024-10-11 00:47:04 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b7219d-cd18-3e52-b232-998a6bf9cb1a | -2.8025 | -48.7005 | 2024-10-11 00:47:04 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea145558-1f00-3eb9-8e36-965c9379b00c | -5.3259 | -60.084202 | 2024-10-11 00:47:04 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98fae178-204a-3484-b335-be58fb006540 | -5.334 | -60.121899 | 2024-10-11 00:47:04 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56736f05-7010-330d-9c55-1d361c9582cd | -3.4465 | -51.578602 | 2024-10-11 00:47:04 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 157e7eee-7098-3e8c-81b8-05ee57d55127 | -3.4481 | -51.5854 | 2024-10-11 00:47:04 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5144af5-fa58-3a6d-8e40-ea65624479cd | -5.3202 | -60.105 | 2024-10-11 00:47:04 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad8888d-b70d-3320-8de8-fd68df2c5f9a | -5.3243 | -60.123901 | 2024-10-11 00:47:04 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb41b44d-3bd2-3888-b708-322cc432d4c1 | -3.165 | -50.426102 | 2024-10-11 00:47:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bd0482d-1883-3118-bd2b-2d3a3b80a03e | -3.1667 | -50.433201 | 2024-10-11 00:47:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f1c456e-1935-3cda-b556-84c113b9f761 | -3.1683 | -50.4403 | 2024-10-11 00:47:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8d15e81-14b6-3124-a561-174e8a7ab58e | -3.2811 | -50.937698 | 2024-10-11 00:47:04 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d137e27-8916-34b9-90eb-7d885151e52d | -3.1552 | -50.428299 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c41d7dd6-b42a-310d-800a-d4a2c6964d2d | -3.1568 | -50.435398 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 591114b2-0c4c-35ed-988c-c0fd13f887bd | -3.1584 | -50.442501 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d65e7572-586d-3c04-8cc0-490f3b2269f2 | -3.2712 | -50.939899 | 2024-10-11 00:47:05 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bfb5507-16d5-33c3-832c-d976e77a50fd | -3.0967 | -50.216099 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23effe3e-780f-3a32-af0a-9662cc7e557a | -3.0983 | -50.223301 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85f24917-d781-35ad-8c79-d6ce9a2e1716 | -3.1454 | -50.4305 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a06ca9-3ddb-3075-bcdf-a163a2177295 | -3.147 | -50.437599 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91f0cff4-8e32-3948-9e14-1c2372ab9335 | -3.1486 | -50.444698 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ade8057a-c846-3368-86b7-23073135b3b2 | -3.2378 | -50.837898 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd9c11fb-fc5a-354c-8fe7-552f970ab3a5 | -3.2394 | -50.844898 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fd6f5a8-fdc1-3bfe-ac30-6a7ec734e402 | -4.2665 | -55.435501 | 2024-10-11 00:47:05 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad25c434-eb32-353a-95f3-83be1266e21b | -3.0869 | -50.2183 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589fd59f-4d54-3916-a511-1ecfeb55c302 | -3.1323 | -50.418499 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21938260-04fa-3c6f-8444-9b0d17956aad | -3.134 | -50.425598 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd703a1d-8906-34c2-b989-cf458e9d6d27 | -3.228 | -50.840099 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070b61eb-8631-3e18-9d79-27b2dbb206e8 | -3.2296 | -50.847099 | 2024-10-11 00:47:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10830a70-df47-3dc5-aeeb-3498fc199fa6 | -3.8321 | -53.570999 | 2024-10-11 00:47:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f53dc195-cc64-391d-b7ac-992d8161afb6 | -3.8337 | -53.5783 | 2024-10-11 00:47:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 312d9395-2b53-3f26-b22c-f4637c7b00c3 | -3.9101 | -54.152 | 2024-10-11 00:47:06 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 919cdd32-dcee-3165-9c98-66abc7e197fc | -2.4537 | -47.8078 | 2024-10-11 00:47:06 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7fcbfd6-3c3c-3b29-9134-421872279fca | -2.7797 | -49.231701 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f323eba-c29c-3bd7-ac66-bc881320826b | -2.7815 | -49.239601 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd02c5c-4d17-367b-a9ce-27029dc31f45 | -2.7833 | -49.247398 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90ee7ad0-8e47-3612-bd34-bab9d0fe6f68 | -2.7681 | -49.226101 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad9cd21-2ac0-3907-92e6-d7b0b7b093fc | -2.7699 | -49.233898 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4b6cf53-61d4-3916-92b4-58ebb0c3c7fc | -2.7717 | -49.241798 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19295b50-5e64-37fb-a088-0701c5de11bd | -2.7735 | -49.249599 | 2024-10-11 00:47:06 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e461ad7c-5961-3fda-87c2-1c307b970a9b | -2.8353 | -49.520401 | 2024-10-11 00:47:06 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17e693b0-aacd-3382-b3f6-cbe0c67019b7 | -2.8255 | -49.522598 | 2024-10-11 00:47:07 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0105fc04-7538-335e-be6c-94a9a0217826 | -3.1664 | -51.296101 | 2024-10-11 00:47:08 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c0c61d-20d6-3750-a245-e1929c774012 | -3.1679 | -51.303001 | 2024-10-11 00:47:08 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d5435b-03db-345f-8de5-88c5413d1b7e | -3.2128 | -51.5014 | 2024-10-11 00:47:08 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7bc283d-0cdc-31de-8d35-58adfd9a2ab7 | -3.2143 | -51.508301 | 2024-10-11 00:47:08 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6145fa26-8e47-360a-946b-d4b574d7437f | -3.4881 | -52.815899 | 2024-10-11 00:47:08 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a87643-b7f6-3278-b71c-6ea698fedf99 | -2.6008 | -48.944599 | 2024-10-11 00:47:08 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e07189b7-4e09-3246-a88f-ad18ccbec047 | -2.5679 | -49.070801 | 2024-10-11 00:47:09 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb974c06-73c3-3914-94a9-4174ee95e0a8 | -2.4155 | -48.449501 | 2024-10-11 00:47:09 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd61def-5524-374f-ae34-d713803a7d31 | -2.8976 | -50.701 | 2024-10-11 00:47:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4af78275-c8dc-3031-886b-e3446ca89189 | -2.8992 | -50.708 | 2024-10-11 00:47:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e050cf5e-f21e-3126-9e14-ef246224af9c | -3.653 | -54.151901 | 2024-10-11 00:47:10 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30780179-bb39-3097-b1d4-241691a3e3d9 | -2.5022 | -49.144402 | 2024-10-11 00:47:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7fcc1e2-15fc-3ee1-852e-2555c611ee77 | -2.2334 | -48.013599 | 2024-10-11 00:47:11 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a6be89-efd7-3bcd-bd69-93d1eab2c9de | -2.2355 | -48.0228 | 2024-10-11 00:47:11 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02856b97-186f-38e5-9494-a8d1a29b8bd6 | -2.9717 | -51.346699 | 2024-10-11 00:47:11 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2d839f9-af38-368b-adf0-3b1292258e45 | -2.9732 | -51.3535 | 2024-10-11 00:47:11 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95422b03-960b-3e0f-b3e7-ee266a0d4778 | -2.9748 | -51.360401 | 2024-10-11 00:47:11 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb6dd466-50d2-3b5e-a986-305b2fbf4d77 | -2.9763 | -51.367199 | 2024-10-11 00:47:11 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 324f7247-94df-3191-87c3-5a5a4c0c8f88 | -3.3331 | -52.996899 | 2024-10-11 00:47:11 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39ccdd0f-2fbf-3777-a156-61ffd4ad1142 | -3.3217 | -52.9921 | 2024-10-11 00:47:11 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab68fde-fe40-398b-95a1-3334b7a3a8c5 | -3.3232 | -52.9991 | 2024-10-11 00:47:11 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e78167e-9737-3c18-a70f-1b5766604139 | -3.9958 | -56.069099 | 2024-10-11 00:47:11 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65d4d739-386a-3007-80ff-0101da340a38 | -1.9946 | -47.242298 | 2024-10-11 00:47:12 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0c76ccc-7227-3132-b0c6-374eec1824e2 | -1.997 | -47.252602 | 2024-10-11 00:47:12 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4a4ae5f-0cf4-3165-a246-c1f1dbcf7330 | -1.9873 | -47.254799 | 2024-10-11 00:47:12 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6c970bf-9a7f-3331-b8b9-a4c3c76507e8 | -3.3299 | -53.212502 | 2024-10-11 00:47:12 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3bb8da-9606-3eb0-a9f4-557eb67dd97a | -3.3315 | -53.219601 | 2024-10-11 00:47:12 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6b7bee-5c98-35f9-855d-6dc53d6ae1e3 | -2.8007 | -51.001099 | 2024-10-11 00:47:12 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecf3c9ae-f8a4-3958-91f3-b6a66490c76d | -2.8023 | -51.007999 | 2024-10-11 00:47:12 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c4eaa8e-177e-36a7-874a-b0cecdd951dc | -2.8039 | -51.0149 | 2024-10-11 00:47:12 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 237c0785-8d2f-3ff4-b9ed-79924709031d | -2.8105 | -51.5909 | 2024-10-11 00:47:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbbc5f8d-3b49-3733-91d0-5050c468c055 | -2.812 | -51.597801 | 2024-10-11 00:47:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad224f9-5ea6-3651-a6a2-e2f67d2c3088 | -1.9027 | -47.8731 | 2024-10-11 00:47:15 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4916a6f1-07c6-3f0f-bd67-76f4cf3f407b | -1.9049 | -47.882599 | 2024-10-11 00:47:15 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef7f777-8352-33cd-af6b-604485e1fafd | -2.9527 | -52.541801 | 2024-10-11 00:47:16 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e13f4db5-041d-3398-9c2c-a2a77a034c2a | -2.9896 | -52.889301 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59c0cdc3-9cac-3fd5-b521-62f56d3a1d00 | -2.9912 | -52.896301 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc2761b-f7a8-3dfe-9f82-849ad9e37a46 | -2.9928 | -52.903198 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 702a9831-9b60-325a-b682-f26a79a33f76 | -2.9783 | -52.884499 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 814b478f-9bf9-3c03-8fce-55f84c2377d9 | -2.9798 | -52.891499 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e48ff488-b012-3175-8df1-1d0dd6700b69 | -2.9814 | -52.898499 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7635f7-9df7-36ec-8819-5f2840d389dd | -2.983 | -52.905399 | 2024-10-11 00:47:16 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4693d89-2d5f-3176-a3b4-3a2e708c5d35 | -2.9685 | -52.8867 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc3ea317-1287-35d4-8e6d-99b9b2de8f01 | -2.97 | -52.8937 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42b128d8-a743-3b51-94a9-2f006d481f71 | -2.9716 | -52.9007 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 972d00ac-b158-3e0b-9e9b-9dd6a1ce3db3 | -2.9732 | -52.9076 | 2024-10-11 00:47:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c756b737-ab0d-391b-adeb-4a5eeac5da2d | -3.2552 | -54.167099 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1256d0c4-4ee5-3394-a751-99c6b27aed1e | -3.2569 | -54.174702 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b980e5b-4f6c-30bf-ac0b-936d53cb4e33 | -3.2587 | -54.1824 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494e26b7-99a5-3cd0-8eb2-f7cec0c9c544 | -3.2604 | -54.189999 | 2024-10-11 00:47:17 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39970e37-4afc-3b69-bd83-8410b6d1892a | -2.3775 | -50.316399 | 2024-10-11 00:47:17 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
