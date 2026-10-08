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

## Dados Diários - Página 394

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 558b32e7-039e-350b-bdb0-2ba30d8792c8 | -1.5123 | -54.556 | 2026-10-08 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c928b5d3-4707-37e1-961a-a38fd6a8dfb5 | -11.47 | -43.3824 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 61804a0d-e8d1-3d1d-860e-5e4fd8cb3f21 | -5.4142 | -45.8734 | 2026-10-08 18:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4231972e-0916-3cde-aa82-603f3c0f0cd8 | 3.7462 | -51.6224 | 2026-10-08 18:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8e5109d2-33bb-31e0-b4c1-182d981ddf22 | -1.8232 | -54.9904 | 2026-10-08 18:30:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fac8b396-fc16-3e82-aa56-5357bc8137ad | -6.9331 | -43.6566 | 2026-10-08 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| e3ac222f-09c0-35eb-82f2-349a7b65ac97 | -3.5726 | -58.5581 | 2026-10-08 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| c489f76d-84de-37f2-b656-3f7c74ae06cc | -6.4905 | -55.9563 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 11f041a4-d54a-3120-b9c8-7eb0a99c1c79 | -6.2355 | -52.6841 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 5ce8e5b3-3a35-3c71-8ad1-145f694efb4d | -3.2957 | -49.1202 | 2026-10-08 18:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 550f2e70-7fcb-39a4-bed3-6b78f2848716 | -2.7796 | -54.0937 | 2026-10-08 18:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 90a97126-e77e-3e5a-ae69-4f092474481c | -1.091 | -54.1603 | 2026-10-08 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| baa74fe5-75f8-3bb5-adbc-0457d0278d51 | -5.9835 | -40.9367 | 2026-10-08 18:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 4da687cd-d102-36f3-b56e-8546c4b1928a | -3.0799 | -58.0083 | 2026-10-08 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 6423359e-a17b-31c8-a459-b05139c517e2 | -3.2268 | -57.8696 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 374c03cf-1a82-3258-a1da-13361a569a81 | -8.5924 | -66.975 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 6fd4abaa-a01b-36d0-ae04-ce0532bf5e54 | -5.6932 | -53.487 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 254.1 |
| 21d4ef6f-8139-3cf8-b953-e9779736e12e | -6.3134 | -54.7884 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| b0ed3401-70da-3aff-80f6-1d01b2f0c297 | -3.2214 | -53.8818 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 3e9c64fc-95f4-3b9d-b294-204a16a7d6e3 | -3.4312 | -56.9502 | 2026-10-08 18:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 44320a39-a267-316c-92ae-bb8849987b88 | -11.6382 | -43.6166 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.7 |
| ff7d6e64-77b4-3d74-bfa4-160badef62ea | -3.6708 | -41.438 | 2026-10-08 18:30:00 | GOES-19 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 205.0 |
| 9b1b8206-3f8f-3704-9fcc-32a30c71689d | -3.4095 | -58.0013 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6e165d37-cbd8-3035-8085-df383bcd1c3b | -6.2127 | -53.2779 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 624616a1-5e15-38fe-b059-3ea26aeb86de | -7.5847 | -55.7205 | 2026-10-08 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| d6481059-890d-35ee-9ca1-0f5a25366d6a | -4.1025 | -44.1149 | 2026-10-08 18:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 70b44400-fd12-32cd-be62-caf0fbe04968 | -8.5184 | -66.9954 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 8a75a297-2212-3e44-a581-6c2d5dfb1ba9 | -6.5127 | -55.3984 | 2026-10-08 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| aa42ac2d-2fa6-3491-9d97-007b6212bfae | -3.0992 | -57.6589 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 33b3f749-3bf4-3634-9c63-5f9a1707a934 | -6.895 | -43.7066 | 2026-10-08 18:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 223.3 |
| eb17bb92-23e4-3476-8cac-6e0fca3b1bbb | -3.1114 | -53.7839 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 15922b1d-1478-33ba-b987-a680517c01af | -2.9707 | -57.7779 | 2026-10-08 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 7a0e33e8-d707-3038-bf60-918adbf2ab90 | -11.1145 | -44.0009 | 2026-10-08 18:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| fbfac9d2-8161-346c-ac0c-c4dbca81b55f | -2.9449 | -54.1099 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| e1fc19ba-907f-3764-b579-f27631fd75d9 | -6.1615 | -52.6676 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 277fc4b9-8f33-39f5-968f-297aaf4eeac6 | -9.0065 | -45.15 | 2026-10-08 18:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 928.8 |
| c4558fbe-ae15-39c4-a007-6c7bbae31c8f | -6.1974 | -52.8295 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 5abc1f99-1567-3386-9dfe-49b0a83e8480 | -5.9772 | -55.344 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f568204e-ae5a-355f-bfad-047f23a78ba1 | -2.1361 | -54.4671 | 2026-10-08 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 0d6403d0-afe4-334e-ac86-c8f09bd46be5 | -2.8434 | -57.4696 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 9b9e70c4-d386-3f74-809a-98bdae6888cf | -3.188 | -58.6241 | 2026-10-08 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 85cf5167-4a36-3dd9-a786-44a49f48c09a | -3.195 | -42.9772 | 2026-10-08 18:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 191e356e-af7c-3473-b053-e393c3876ada | -6.6711 | -45.3761 | 2026-10-08 18:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 29a43a9f-1452-39bd-ae8f-25393bcd929a | -5.2853 | -48.1053 | 2026-10-08 18:30:00 | GOES-19 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 219e8d07-baa8-3ca0-b68e-88a0869abc8a | -6.1298 | -51.9281 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 24661f30-7891-36e5-b14e-caee4a4f76cf | -5.3953 | -45.897 | 2026-10-08 18:30:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7affdfc4-495b-30a7-a4b9-7be5e8a27b25 | -6.2357 | -52.6635 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 894115c9-7c96-30c1-9bac-81063972a89a | -1.8233 | -54.9307 | 2026-10-08 18:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2630d5a3-faef-34ec-b3d3-5f886877949c | -3.2215 | -53.8616 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cbe24fb7-9d1d-376b-b68a-557be5529518 | -11.7738 | -43.5482 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 8346cb58-a8c7-39e9-9be7-402e059bc137 | -9.1257 | -67.8137 | 2026-10-08 18:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 4e3bb828-41f4-383e-8446-6de6d7a49e5e | -3.2634 | -57.8689 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 5b99921d-6080-35ff-81a7-7d23329b98b0 | -7.5354 | -42.088 | 2026-10-08 18:30:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 7508a032-bd7b-3d3e-8f5b-cec4a6e7b31e | -6.1496 | -51.7614 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f3cd4a22-13f0-36fd-a7f5-97a8950f2939 | -13.3671 | -43.8742 | 2026-10-08 18:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 92d594a5-545b-3c98-bf8e-53e7f30fe8d4 | -6.8907 | -45.8988 | 2026-10-08 18:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 2e8e6baa-a143-354e-ac76-32fadebf9b32 | -2.9271 | -53.9295 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 1368eca4-5457-32d0-acb7-8db43482d2ce | -3.2085 | -57.87 | 2026-10-08 18:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| a2e2144e-52a3-33dc-bbf1-2cec05ba21d7 | -9.1294 | -45.8405 | 2026-10-08 18:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 39a04cee-6013-3ff5-8d9a-a7e64119ff5f | -3.8566 | -55.9967 | 2026-10-08 18:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| e543f884-ecd3-3af3-a0f1-01af50362a1f | -6.1482 | -51.9477 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 382877fa-e703-3778-81d0-918f3889d0d8 | -6.2162 | -52.7876 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 13191acc-9986-3498-8932-4483f01748fb | -7.5849 | -55.7005 | 2026-10-08 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 66156954-14f4-31e1-ad8b-34b9d034c6bd | -2.5492 | -58.0373 | 2026-10-08 18:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 914984b0-9620-3fc5-90d3-e34fce0f872e | -6.1001 | -53.5075 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 92b7e23a-528a-3bb6-a47f-46a7cfeae915 | -9.0362 | -44.3654 | 2026-10-08 18:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c859e4a0-eb32-3b5a-bafd-e4121da588cb | -1.091 | -54.1803 | 2026-10-08 18:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 0ed21140-b63d-37f1-9d3c-b6209c126a1f | -3.1697 | -58.6244 | 2026-10-08 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 7e28672c-8514-3e16-ac82-7ee28a6180b7 | -12.2311 | -44.7661 | 2026-10-08 18:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 405899dc-80ec-3cdd-92f6-d402cb69c280 | -6.234 | -52.8889 | 2026-10-08 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 206.4 |
| b71200ec-42a4-3b9d-a115-4e9114c7918c | -5.9587 | -55.3448 | 2026-10-08 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 8223e146-b9a9-3a63-b590-f395b6ac5b90 | -7.4508 | -42.8334 | 2026-10-08 18:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 1d4176a6-c806-3aca-982b-6c75416d2ebd | -6.3811 | -42.5332 | 2026-10-08 18:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 861a7693-050b-3faa-b5e0-7af9cb775dee | -6.3623 | -42.5349 | 2026-10-08 18:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| 734c07f0-279a-3fe5-ab91-fe32dc016b10 | -11.7935 | -43.5215 | 2026-10-08 18:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| ffd3d14a-3e99-394a-be07-71386e279a68 | -6.3133 | -54.8084 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 81c1337e-0ac4-317b-94a4-2b32b3ec8c12 | -5.8599 | -53.4586 | 2026-10-08 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c6c8b1db-b34e-3ee8-8083-a536372197f6 | -6.4589 | -46.023 | 2026-10-08 18:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| faaf142a-8e66-3f36-be30-b3a843bdca75 | -2.77 | -57.5293 | 2026-10-08 18:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 166.0 |
| c5839f90-f676-3655-8ca6-7106a06f2a25 | -3.1874 | -58.8358 | 2026-10-08 18:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| f325a23d-849a-35cd-8709-b4d1f23cffa8 | -7.0281 | -45.3008 | 2026-10-08 18:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d94ae05d-eeef-3fd1-9a05-0b8948b7e027 | -3.1115 | -53.7637 | 2026-10-08 18:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| fd0d9a5c-be8e-39d7-826d-bb5d1bc6d485 | -3.724 | -57.0993 | 2026-10-08 18:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6c5efba8-8783-3393-bce1-72e4e969571a | -12.8303 | -44.6239 | 2026-10-08 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 9f39d299-fc54-3edd-9c5c-fd471b97bd11 | -2.8163 | -54.133 | 2026-10-08 18:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b3aa160d-4d2d-3d15-b735-566e19a2cd8f | -8.537 | -66.9764 | 2026-10-08 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 42ea4f35-3f5d-3b07-8133-5066dc8d6d21 | -6.8952 | -43.6833 | 2026-10-08 18:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 48450bdc-3063-337b-ba4c-34a5f7b5b846 | -11.1988 | -49.4297 | 2026-10-08 18:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| f9e162a8-a9d1-34e9-b0fa-404dfd4adbd6 | -3.8012 | -44.6104 | 2026-10-08 18:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 907f6bb7-0f3d-3bc7-b182-70e0afc6ca9e | -8.9769 | -45.9475 | 2026-10-08 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 119c8179-f1af-3ade-98ae-b115f53188b1 | -1.1094 | -54.1802 | 2026-10-08 18:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| acf74ced-16a4-335a-b4a1-93be31fb1923 | -9.9014 | -44.8147 | 2026-10-08 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d8e99782-f294-393b-bd99-b70cf7949523 | -6.2355 | -52.6841 | 2026-10-08 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 4be33dd5-3c54-3a4b-bd2e-5dfb07ef3b6b | -3.1874 | -58.8358 | 2026-10-08 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 81e257e6-23ea-37b4-84df-18805aac77ca | -11.6369 | -43.6876 | 2026-10-08 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 9a6ce9a9-0a93-3c4e-bc01-ad0477fcd783 | -6.1746 | -53.4427 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 81ac804f-0a9f-3828-b955-42baffc53910 | -7.4977 | -54.9854 | 2026-10-08 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| b5881f00-9397-3052-96db-702348c5660b | -12.2311 | -44.7661 | 2026-10-08 18:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 471b8292-073e-387f-bd1f-7916e4412c1d | 2.0047 | -55.8786 | 2026-10-08 18:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 01919a11-c986-3345-ae94-10cd1022017b | -2.5492 | -58.0373 | 2026-10-08 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 150.1 |


[Clique aqui para ver as próximas entradas](README395.md)
