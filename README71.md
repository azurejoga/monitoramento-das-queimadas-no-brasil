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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 173a1be8-4eaa-39cb-a982-4a97adb3b2dd | -20.73538 | -41.76485 | 2025-08-24 05:21:00 | AQUA_M-M | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| a5079374-dd3c-3c99-90f6-cf000a1dfb51 | -14.93973 | -48.00002 | 2025-08-24 05:21:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| e8aca93d-bc38-3c01-859e-377c807a3d0f | -20.0805 | -46.10757 | 2025-08-24 05:21:00 | AQUA_M-M | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ae9c9208-7d3c-3ade-8246-1dc33e398311 | -16.79205 | -51.34681 | 2025-08-24 05:21:00 | AQUA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 7e8b3384-cff5-354b-89a2-fdb5b51efecf | -20.3718 | -46.7388 | 2025-08-24 05:21:00 | AQUA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e475c4a7-5d20-3e8c-a257-70ab063f2c8a | -19.63398 | -43.1801 | 2025-08-24 05:21:00 | AQUA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| a7b29de7-bfc8-3cc5-b4b7-dfb709fc6eda | -13.4729 | -47.01371 | 2025-08-24 05:21:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 579b2588-82d3-39a5-9f07-b5452906ca98 | -2.26152 | -47.85554 | 2025-08-24 05:21:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88936549-df98-3abb-8db3-a818e49fe185 | -13.03707 | -45.22255 | 2025-08-24 05:21:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3c758708-a7b4-341d-bd83-935d074cce62 | -20.36074 | -51.66766 | 2025-08-24 05:23:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4545cbf3-6579-3c29-b0db-5ddd86f5ec32 | -3.51165 | -47.21029 | 2025-08-24 05:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4b2f177a-2c4d-3155-ad79-65e11e4264a3 | -7.75432 | -47.3569 | 2025-08-24 05:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 487593b2-6733-395b-9422-07e39661273c | -6.2317 | -55.94186 | 2025-08-24 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3f7af3a-31b1-3ce6-b6fa-5170e05c4df5 | -7.56115 | -63.85771 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98eba2c4-8793-353e-8fa7-5a094247b0ff | -6.46196 | -53.40312 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce28168f-7236-3122-9558-6ae6e3ef4038 | -8.06096 | -49.65664 | 2025-08-24 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3063fe5-dc92-349c-b774-325c86cea3a7 | -9.02964 | -47.64705 | 2025-08-24 05:23:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce24f93e-6d3b-3347-93fa-6acee143950c | -5.45151 | -60.1925 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dad07dda-b1d6-34b7-add5-4735087b3684 | -6.31119 | -59.88659 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1667a03f-437a-39ca-9ea9-dde8d8a15070 | -15.33801 | -53.91217 | 2025-08-24 05:23:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57de2f65-caef-3781-ace1-645ab63bb8d3 | -10.41435 | -64.41759 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 72e86735-6f0c-391f-827e-1fdbc8ede9c2 | -2.91201 | -48.30629 | 2025-08-24 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f76c7c4-899f-3413-b89d-1402a149dace | -7.30543 | -59.62574 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dbcfed4-1385-34d5-a239-f52373d5e1df | -14.49158 | -53.09529 | 2025-08-24 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 455023b9-b0db-32eb-869d-4e463df1cca8 | -9.61888 | -48.33308 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb71fd2d-caa2-3a27-90db-171b0194fd02 | -2.92643 | -53.70488 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 311c3690-5d7a-3f2d-98a6-af74932cd526 | -6.74622 | -62.86673 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27bf8da3-cf43-38ca-a327-8fe4c31893e8 | -6.46266 | -53.39813 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e1ab33e-a2e2-3b87-b08c-f9ccaa56c7d6 | -10.42008 | -64.42699 | 2025-08-24 05:23:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 149c1115-f0cb-3d8c-9d51-27a7af9b4634 | -14.28309 | -60.37322 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 463a0b1a-b0a4-334d-b73b-141ebe1af452 | -21.69861 | -46.90269 | 2025-08-24 05:23:00 | AQUA_M-M | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 2de832eb-1add-3b7c-8b06-6f4fd5119179 | -5.75442 | -57.58793 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f51f8fcd-6a48-336e-9fbd-8f9ca54f9204 | -3.13668 | -58.04173 | 2025-08-24 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| caee880f-9666-34ce-b9c2-32627161dc66 | -4.95986 | -55.81928 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0898d044-16dc-3f48-8de8-001356ddd33c | -9.56298 | -68.58281 | 2025-08-24 05:23:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6d284dc-7a7e-3eed-ab94-aee76642b12b | -5.74547 | -57.59896 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0268079a-6f60-3b17-a6b1-db22ee273ed4 | -4.31318 | -48.09897 | 2025-08-24 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96ec8500-c6e2-3dd2-a2a3-df37841495d1 | -5.80066 | -59.22312 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e58693-a3b9-383d-9749-79afa3c72d4b | -12.73378 | -48.11827 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08d11304-0d0f-39bb-8868-ecad2ad50b73 | -7.7874 | -61.57571 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66503f71-7abf-3b16-9b13-657189e8f72a | -7.55333 | -63.86062 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b366e902-23b1-3eb5-93a1-48d69a524381 | -5.74018 | -57.5857 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b37df9ec-a327-3610-8138-27f7673c516e | -5.74079 | -57.58167 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d517ce3a-a424-3c8a-97f2-5cf3eaa1a779 | -14.81915 | -55.97789 | 2025-08-24 05:23:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 73de7d7e-4e00-304e-9832-a53b990be065 | -9.50223 | -68.47536 | 2025-08-24 05:23:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e504ac-e347-3597-96f7-ba3a98de6312 | -7.78795 | -61.5722 | 2025-08-24 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39dcb22a-d2d8-3ef5-93e3-832fec96aac0 | -6.78368 | -59.64352 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2771c429-9ded-3a0b-8cbf-5cd92c32d7dc | -3.39659 | -52.83654 | 2025-08-24 05:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b31816e2-3e75-3df6-b9bb-ee8896aab5b1 | -7.57113 | -63.43928 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cbce47e-9c18-3c4c-be2d-713d6ff5afd1 | -2.58524 | -51.9183 | 2025-08-24 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37319060-e4dc-3477-819d-7d08f1af87e2 | -5.4559 | -60.18612 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e511c7c9-91c7-3abd-ac5d-9e0a246a3eaa | -7.55043 | -63.85592 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34ec7a54-0deb-3ed2-805d-5aea76293b71 | -5.74495 | -57.57819 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d18c86b5-9754-32ae-95a1-2d201571ca4b | -14.29219 | -60.38284 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bcef12b-0d77-340c-9aef-b5fc5c525a62 | -12.16076 | -60.81844 | 2025-08-24 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dadd49de-85d2-3ccd-b7a3-b8b8cbe1e084 | -6.98086 | -60.03436 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23a55b7c-454e-3439-a64f-e5eed6afec7e | -21.2709 | -43.74897 | 2025-08-24 05:23:00 | AQUA_M-M | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| d03d989d-c318-3349-9671-88c20156f4b2 | -3.06195 | -49.50529 | 2025-08-24 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dbae40c-f8b1-3dd3-b50c-c160fbb2b95d | -20.34191 | -51.70833 | 2025-08-24 05:23:00 | AQUA_M-M | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4d03580b-0dcc-3510-800f-1622702341c7 | -7.31769 | -59.61305 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fabb402d-3a01-35f5-b58a-be8728ef810a | -7.574 | -63.44379 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43f39a0d-88f8-35fb-81d1-12b03d893c2e | -6.87883 | -59.81718 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6092065-940d-360a-8ca2-01a82ea7ef80 | -3.05575 | -49.50476 | 2025-08-24 05:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f69e4b2-bd7c-3085-a3da-9e7cad16e3a5 | -12.73794 | -48.11179 | 2025-08-24 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df5950b9-186d-3476-b053-b5d5f6cb29ea | -6.57487 | -59.87014 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fbf0573-fd6e-336f-9d2e-2c438afde09e | -7.56181 | -63.85361 | 2025-08-24 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fbb55f7-766b-3d75-94db-81d27d017b91 | -5.80457 | -59.22011 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0985ec1c-73e5-3286-b2c5-0cf7f746c773 | -2.58715 | -51.92265 | 2025-08-24 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ae9412b-3f3d-3424-91ab-9e87f09ede25 | -5.79786 | -59.21904 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c9e8019-5493-3222-961c-c8a8e4abc56b | -2.62826 | -58.11382 | 2025-08-24 05:23:00 | NOAA-20 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0116c1c5-1992-304d-b660-62fe9ae3a5f4 | -7.30153 | -59.62877 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aed1d04-2ed7-3604-a50b-a2c8f6c85fa1 | -11.99661 | -61.02384 | 2025-08-24 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 30ef4450-f29c-309f-8aed-af630cf45338 | -6.68198 | -58.8532 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e94e5cf-9d65-319d-9cf6-f816f813bae3 | -11.69812 | -60.184 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e412a5c8-b2f2-34ff-929a-2eb210682d97 | -7.29482 | -59.62771 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f31ff0ce-6ed5-3f75-b4ec-5e21414cbad9 | -23.30858 | -45.53165 | 2025-08-24 05:23:00 | AQUA_M-M | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| baca79aa-1c82-3e07-8ad8-b764e33282c8 | -7.44855 | -59.92755 | 2025-08-24 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 276f5d30-4b2b-383d-92dc-b9037dee28df | -6.58098 | -59.87469 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| faa9e53e-e360-31b6-a52f-72ac954f4d3b | -6.62462 | -58.54263 | 2025-08-24 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3d7d556-def7-3e66-b40a-1c413deb9770 | -2.91582 | -48.30862 | 2025-08-24 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8debffd3-6477-3bb2-b76a-daed953e7540 | -4.30673 | -48.09808 | 2025-08-24 05:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe68be21-7fd8-3be2-8a13-5adb5d55a8ec | -4.96375 | -55.81988 | 2025-08-24 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e12156a5-d764-3dc8-af8c-ed9ac19a1a0c | -11.70039 | -60.19192 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd941c12-e1f3-3594-bcdf-ea813e33d074 | -5.42379 | -60.17396 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| bcb9aa33-cc23-396e-8b4a-1f8ae58e3318 | -6.92775 | -62.89148 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e8cd2fd-10e5-303d-8a34-212a51dda8d0 | -8.76204 | -49.9784 | 2025-08-24 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 761c41ad-8880-3cc2-ba74-86ee601bbe18 | -5.74791 | -57.58279 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c6b31b49-3a5e-35c8-98d5-8660bea020fd | -15.12259 | -48.63414 | 2025-08-24 05:23:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bf52331-5cc3-382a-b3bc-9cb0a4b30b55 | -14.28935 | -60.37839 | 2025-08-24 05:23:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4edf25a9-5816-33a0-937b-fa0e0ed67d62 | -6.74798 | -62.87025 | 2025-08-24 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 265e7ff6-b33e-30fd-bce7-475dc6f73f4f | -9.67959 | -48.34496 | 2025-08-24 05:23:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 33a98e1c-24f6-32e3-934c-ecb10b522d71 | -5.74252 | -57.59437 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd698693-38b3-32ac-a2a1-7506c4d6b54f | -11.99716 | -61.02026 | 2025-08-24 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0ae5d15c-93cb-3970-9e17-ff2d39a8b970 | -15.35301 | -53.91744 | 2025-08-24 05:23:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4007e25d-2d82-3820-b4a4-c2ff7cc56da2 | -6.42866 | -53.38625 | 2025-08-24 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb47d4b1-a6e0-3b22-b178-51c621482b8e | -5.79562 | -59.2114 | 2025-08-24 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ea822cf-217f-3630-82b1-68e5fe304b11 | -5.74842 | -57.60353 | 2025-08-24 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5bed5fd-6f4e-3edd-b2f3-323e0e36ba33 | -11.69022 | -60.1903 | 2025-08-24 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d141dd1f-edef-387a-a799-45bc7d4a1a52 | -5.42048 | -60.17344 | 2025-08-24 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| be18d8c0-7834-3fc1-99c4-dc521d667c58 | -10.94818 | -63.01406 | 2025-08-24 05:23:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README72.md)
