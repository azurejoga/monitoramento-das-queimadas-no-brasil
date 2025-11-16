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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3573723d-63cb-3974-b85f-d7d12351c924 | -13.82304 | -43.19024 | 2025-11-16 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ed103a0-99ba-3f4c-b7e2-3573fb4f10a9 | -13.55097 | -44.27382 | 2025-11-16 04:10:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13c0cc23-dbc7-33a7-aa4f-3ed066998f73 | -14.64442 | -46.56618 | 2025-11-16 04:10:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8918ea37-1016-3615-9033-0137a8cff595 | -12.66347 | -47.16939 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea2c4f98-4e93-3158-9150-29b1dcead650 | -12.85794 | -46.78088 | 2025-11-16 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe9add30-3d9c-3ff8-95b2-4421ae45bd61 | -26.10057 | -50.17601 | 2025-11-16 04:12:00 | NOAA-20 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd096adb-eccd-370e-94a3-8b304874387d | -29.73986 | -51.2647 | 2025-11-16 04:14:00 | NOAA-20 | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 2f24e38d-b5ff-36dd-b79b-f0155dd171f7 | -2.5238 | -47.8115 | 2025-11-16 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3ad0e592-068b-3362-9152-fa9ee1c3a65f | -4.4246 | -43.4038 | 2025-11-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 772721a5-0679-34d2-bf12-0ba41a80d2cd | -12.0004 | -49.2683 | 2025-11-16 04:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 810e852a-e343-369a-85c1-fa8c6b9abbae | -4.4246 | -43.4038 | 2025-11-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| e4cd007d-de22-3083-901d-1ac49fabca41 | -10.8648 | -44.0835 | 2025-11-16 04:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 080975a5-d778-3c0b-a2db-82415c852829 | -10.8456 | -44.0862 | 2025-11-16 04:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 8c69368c-9b5b-3d15-9d41-3ddd6f475c1c | -2.5238 | -47.8115 | 2025-11-16 04:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 288d6ce4-5033-3609-a659-09632770da24 | -6.3119 | -43.8036 | 2025-11-16 04:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6c7bd63d-db64-35e1-b8a8-9844ada37b60 | -2.5238 | -47.8332 | 2025-11-16 04:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c64b37e1-4998-36e2-ac47-266c91357e83 | -12.0004 | -49.2683 | 2025-11-16 04:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 205fce8e-1a20-3ca6-85a9-ab74ff7317df | -10.8456 | -44.0862 | 2025-11-16 04:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ce541663-cbe1-3c22-ab60-b081aeb3d654 | -6.3121 | -43.7804 | 2025-11-16 04:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 45a28481-aac1-3ef7-a323-35877a32414c | -11.9784 | -44.9439 | 2025-11-16 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6cfe324c-64d1-327c-8963-f6e85dee8dec | -2.5238 | -47.8115 | 2025-11-16 04:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 4a0e47aa-734f-327f-b0b5-49490b639070 | -11.9779 | -44.9671 | 2025-11-16 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b4931d3e-4260-342e-901e-db4ec5fc17e1 | -4.4246 | -43.4038 | 2025-11-16 04:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| e5ba75a3-05b8-32cd-9780-2a7f98aaf271 | -11.9779 | -44.9671 | 2025-11-16 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 15e3f504-a023-35db-9746-007019533301 | -12.0004 | -49.2683 | 2025-11-16 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8c44d72a-99fc-3208-9018-a6f2e2370c0a | -4.4246 | -43.4038 | 2025-11-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 18754d93-cb38-33ec-b71b-3dd94a08ca8c | -2.5238 | -47.8115 | 2025-11-16 04:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1c729c3d-ecf3-3732-a0be-1314268a8239 | -6.3121 | -43.7804 | 2025-11-16 04:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e81fb5c0-8dfd-3139-b5c3-8da040a77687 | -11.9784 | -44.9439 | 2025-11-16 04:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 986ea20f-6de2-35b8-942d-2c0c7f490d9a | -12.0 | -49.2901 | 2025-11-16 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| cf3fcad9-d562-3005-92ca-0dae4337d5fc | -6.3119 | -43.8036 | 2025-11-16 04:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3b026c5f-81ed-319c-9f92-5045302affe3 | 3.52848 | -51.47074 | 2025-11-16 04:53:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98c4b90f-7cad-3819-9def-94c07f9208d1 | -3.18362 | -50.65779 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5870699d-412c-3b22-8535-913fa68a4ace | -3.99517 | -44.28117 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38bad693-5eff-3d2a-b598-fd277af9e431 | -3.1258 | -52.26265 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b79287ea-b34d-31e3-b19d-540a0910a773 | -2.79842 | -52.96439 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd70b775-8508-3275-b3f4-42155b39541b | -4.73495 | -46.37724 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 312fef61-999f-331f-a46d-4697fb54155b | -2.57535 | -51.8623 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 537598e6-0dc3-3b56-8829-520c30c21b13 | -4.46527 | -46.30608 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 327bc1f1-53ba-3d8e-92d0-9b5996d92335 | -3.09052 | -51.54543 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a70fd90-5ef4-3951-ba83-5e512c11f5bc | -0.8376 | -48.65821 | 2025-11-16 04:55:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 201b2ab4-7595-3a31-a52b-9d19b59d8b1c | -2.73511 | -49.56012 | 2025-11-16 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00b885f7-9ba0-3a87-97ab-26f0bc1b0916 | -4.18849 | -55.0299 | 2025-11-16 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77ffdd70-5164-3317-a19d-d0db65f8e2dd | -2.80226 | -52.96146 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6f31acd-6b08-36ad-8fa2-2e65713487dd | -3.76411 | -47.72559 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ec5f99-4b1b-3edb-aeff-48ca2f18de88 | -3.58961 | -41.66556 | 2025-11-16 04:55:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cbba823a-36f2-390d-8c74-699003d30180 | -2.89281 | -50.40509 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa609514-bdaf-3ac7-bc3d-2311c01a1b40 | -3.75139 | -52.17445 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91fa0284-ea20-3b51-af11-3209ab4beb38 | -2.41646 | -53.94709 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e628063d-d7c3-3c09-86db-731363addfbb | -5.99932 | -41.90964 | 2025-11-16 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bb119b01-c349-35e7-b23b-b149e0860586 | -1.83413 | -53.7993 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1394517f-9db0-3aed-9f00-8ed62c9dd975 | -5.71472 | -41.40696 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 411f8613-a740-3b1d-8af3-bb39354e647c | -3.11376 | -51.03364 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 848cedeb-fe31-345e-880f-9274bffd132f | -3.32235 | -51.61062 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a550125-e752-3004-9807-eca08b0e9841 | -4.43076 | -43.41352 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f6a4b483-5c45-3f3c-86e2-2baa968268b8 | -5.45455 | -47.01259 | 2025-11-16 04:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30315d79-157f-3c91-b571-107f668c6ae5 | -2.51918 | -47.81929 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6e1c2d98-4d62-3976-b90d-b29e9eba4991 | -3.28682 | -53.8223 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04acf495-cf5c-3404-ba05-aca1fc58e02f | -1.39871 | -55.83044 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 839349f6-ede0-33e5-b3a4-b73ebd61727f | -2.85482 | -51.276 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e41aaac-3312-35e9-b41e-7d56bd5eabad | -2.81764 | -48.45742 | 2025-11-16 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69d3dbb-c859-30b4-ae2a-f27be51c09a2 | -3.90931 | -54.68724 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8ab683d-0695-3b59-be42-59d3d072c48e | -4.93973 | -44.53795 | 2025-11-16 04:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b6ed4be3-802c-3dac-87eb-ccf86cd2b818 | -3.28351 | -53.8218 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 880343dd-f613-3a1e-a4b9-4edb736df0ef | -3.66444 | -44.81818 | 2025-11-16 04:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02478bca-2369-3856-962e-d36c57ce26b5 | -5.71686 | -41.40789 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4cc09839-f955-385f-a190-3f7072a838a6 | -2.51563 | -47.81495 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1290376c-c0f0-36ae-88c6-11774c7ccb4c | -4.64798 | -47.9503 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7a5ee06f-21fe-360d-8c9e-320c41a368d8 | -4.23541 | -46.10622 | 2025-11-16 04:55:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1139fc1f-9962-3c8d-8ab9-24c04b53fd74 | -3.76849 | -51.80865 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00ab91c3-553f-313c-808e-f2d2a038753c | -0.31086 | -51.83612 | 2025-11-16 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4634e7b9-d46f-3e0c-8931-2bb4948cd301 | -3.89799 | -54.24124 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dd18602-52bf-3766-962d-6a92adae333f | -1.0637 | -48.85034 | 2025-11-16 04:55:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58f28487-aa4f-3e42-9b6c-c969273fc3a0 | -2.58367 | -51.8307 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 228923f1-a89a-3519-9ee5-82b2a4a43ed6 | -2.00392 | -48.21268 | 2025-11-16 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c482c277-6fe4-3b0a-b99c-e9b3c787bfe1 | -1.9133 | -54.59769 | 2025-11-16 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd75f43b-92e6-3ac4-a210-a4036816ee59 | -3.18358 | -50.65504 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65d0e850-0642-3026-ba54-7ce7d9e42ba8 | -5.71766 | -41.40218 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0ea21091-b59c-321d-b672-a759a2e610a5 | -3.11196 | -49.4747 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c79d2c05-5455-30cf-af00-3bd08c8e39ad | -3.60167 | -54.67496 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a4fbd80-1992-3af8-ae8a-e89aed0005e9 | -3.39693 | -50.18239 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6a2c99b-b937-395f-9fac-9aec7022061d | -4.81437 | -45.50391 | 2025-11-16 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00703515-fe28-316c-a4bf-03da1d7a1613 | -2.9342 | -51.76324 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 095753c0-7536-3e59-b9ea-fd2074e0f024 | -4.69509 | -46.30854 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22f7e4ec-b545-30e1-ac13-f79e1c0e501f | -4.42675 | -43.40057 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba9c6992-38e8-3e0c-bb6b-8880db4bc191 | -1.65016 | -53.6708 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d954af9f-74bb-3d9c-9bd5-5562bb4d0f30 | -4.97495 | -49.65994 | 2025-11-16 04:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 532d9314-f9f0-3069-82ff-272f9ea0e382 | -1.34619 | -54.61176 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9010dd85-41d6-3dd1-8534-9e46c9e83647 | -1.8358 | -53.81021 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1f57760-8c4e-3b62-998a-f110bd34107e | -4.42045 | -43.40359 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 411dea6f-64dc-3436-9a69-f4e3a7531b1f | -4.62491 | -47.41063 | 2025-11-16 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3df0388-20ad-3a65-8bbe-f92ce3cc6488 | -5.22087 | -44.51472 | 2025-11-16 04:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 173199ee-f714-3998-8538-d8fc554ade22 | -2.74101 | -53.20155 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ecc9e5-17f4-3b0d-ae10-12ed80fd892d | -2.83322 | -48.43529 | 2025-11-16 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76dbe854-148c-37fe-a58f-fffb05c3517d | -3.59033 | -41.66051 | 2025-11-16 04:55:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6668787f-a7a2-3b63-b134-25df8ef074bb | -2.79128 | -52.9668 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f13ce98-e2c6-3e7e-ba96-72e55f568a6b | -3.96154 | -44.84515 | 2025-11-16 04:55:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af7b6779-db1c-34c0-878e-c1f3d8e16628 | -4.62994 | -47.40696 | 2025-11-16 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2177752-98be-3a97-8df7-2a73c26f5c85 | -5.57971 | -46.14739 | 2025-11-16 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5384897a-8287-345a-a246-65cd926e7cc0 | -5.48532 | -44.84303 | 2025-11-16 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README48.md)
