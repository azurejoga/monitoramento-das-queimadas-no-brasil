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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 742d17b8-e824-3142-b078-4aec34450f94 | -10.352 | -44.24655 | 2024-11-05 04:10:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 277a832a-8581-3f6b-84f8-a03a1e9de8bf | -9.18665 | -44.21603 | 2024-11-05 04:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54f1f272-4d74-3b5b-97c7-eed71a1fea8c | -11.75579 | -44.21643 | 2024-11-05 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9534399e-ecb6-3599-bd02-ca04a7924587 | -11.52366 | -49.08133 | 2024-11-05 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15abbbe4-a898-3ab3-8511-cf50818b32fb | -11.06394 | -38.43602 | 2024-11-05 04:10:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e4d6696-27b2-3ac8-b2b7-bd36e96dd787 | -10.2754 | -36.31971 | 2024-11-05 04:10:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c691b1b8-f604-3407-80f3-7029f359ab73 | -9.79412 | -43.86936 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e77510e5-c73a-3108-8a42-7914247c3a3a | -12.69572 | -43.25463 | 2024-11-05 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf2ee275-b9de-3a29-9e3b-e82071694707 | -14.29754 | -43.18726 | 2024-11-05 04:10:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 69687560-80af-3cef-8f14-7b2f6c204f67 | -10.45591 | -44.94218 | 2024-11-05 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2d0e19b-e3ad-3b7f-8267-8d367d0da09a | -10.356 | -44.24337 | 2024-11-05 04:10:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec6b355-a7e4-385a-8969-b157e3a5d638 | -9.79075 | -43.86882 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb093b05-3a9f-37d9-b8fb-c7889fa3d13f | -11.98893 | -42.90207 | 2024-11-05 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 45c2b55d-df98-3253-afa1-581a30e9eb75 | -13.28153 | -42.52493 | 2024-11-05 04:10:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fa0bfe22-2220-3f8e-a8c5-ff38a12d05f5 | -11.98508 | -42.90504 | 2024-11-05 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 902c126f-c244-3259-8a34-621c13c0e38c | -11.85853 | -43.87736 | 2024-11-05 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0255eada-576d-3bd1-8d1d-b409bfb62804 | -11.98044 | -44.32414 | 2024-11-05 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18c234c2-a1fa-34e4-a924-89952f1589a8 | -13.44025 | -44.41695 | 2024-11-05 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afbe9d28-0178-3a93-b6d0-003feaab2e8a | -10.28205 | -42.44019 | 2024-11-05 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7edc29d9-68ae-309f-902e-1b3eabc42d75 | -10.8038 | -44.49244 | 2024-11-05 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 264ec9e9-70ce-38e2-b9ad-6cb2ce47bd29 | -12.16378 | -44.62267 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f025840-1c1e-3af1-b569-d485f5fa159b | -11.53542 | -45.02525 | 2024-11-05 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0aa1f3b-16b9-3c4a-b9e0-18be0c9a991b | -12.16657 | -44.62697 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b993e470-2e3d-30fc-9eea-d660ec871323 | -12.16778 | -44.61953 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbf03bbb-6400-3bf7-93f1-cfd0a162c2e6 | -12.22476 | -44.68218 | 2024-11-05 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26e6fcd0-2348-3542-99ab-1f6d45dcc7fd | -12.16039 | -44.6221 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7df6fe5-8119-3aec-921e-52173471436d | -12.02856 | -41.783 | 2024-11-05 04:10:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3f88f3b1-1769-36a3-b7cb-24dfb029dbea | -11.98103 | -44.32048 | 2024-11-05 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8154fd95-8001-34bf-992a-8e73016e2156 | -15.29092 | -42.98376 | 2024-11-05 04:10:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 338c4997-4f02-3656-aa9f-500851541cec | -10.68627 | -44.78077 | 2024-11-05 04:10:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed81b38b-a21f-3735-b392-10d7441cbaa3 | -11.13604 | -43.30681 | 2024-11-05 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dda47da-01d2-3ecf-b655-bbebeaf7ec55 | -15.02645 | -42.28568 | 2024-11-05 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9627268-9b53-365b-97ec-b9839deb01a1 | -17.66844 | -57.52391 | 2024-11-05 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7234013b-48ff-34c3-adf4-0cfb6015bfed | -20.47602 | -53.67686 | 2024-11-05 04:12:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56278bff-b160-38b8-a32d-5df2887707c2 | -23.33917 | -46.77271 | 2024-11-05 04:14:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f487f72d-8a93-3501-afae-4784c83c72cd | -23.40539 | -46.55695 | 2024-11-05 04:14:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 35273371-bca5-3dcf-9fa2-578e83951136 | -3.5447 | -47.3636 | 2024-11-05 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 0c170f78-cf11-3700-9175-de35a7483454 | -3.5631 | -47.3847 | 2024-11-05 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 227.2 |
| 1f17c559-cc59-3950-b0a0-5daa325b0d11 | -3.2242 | -53.093 | 2024-11-05 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 29911bf9-4c29-3784-a971-281a7df2d743 | -2.6506 | -48.5844 | 2024-11-05 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e25e5632-7c51-36e1-9a4f-c870fc5a3b67 | -3.563 | -47.4066 | 2024-11-05 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 08ce5b2d-c81e-3593-8d5d-6130f5a8fcef | -2.6507 | -48.5629 | 2024-11-05 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| e86c78f2-5518-3c35-80e7-93046b09f67d | -6.1041 | -43.9593 | 2024-11-05 04:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 766714b3-0206-3176-8c8f-bd39b542a8bf | -3.5444 | -47.4073 | 2024-11-05 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 4649e38d-95df-322e-8fc4-85f5ca6f146b | -3.5446 | -47.3855 | 2024-11-05 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 272.0 |
| 445bf8b3-0ca5-348e-b7f0-c767488cc90f | -2.6691 | -48.5624 | 2024-11-05 04:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 94351546-7b01-31da-af1c-51f1d026cbfc | -3.5632 | -47.3629 | 2024-11-05 04:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 3f8f404c-a236-3060-aeab-13e1c394b4cb | -3.5444 | -47.4073 | 2024-11-05 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1aac20c8-73f6-34a4-96af-ca4153e049a1 | -2.6691 | -48.5624 | 2024-11-05 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ff943896-2faa-3e00-914e-ec24b4c0870d | -3.5447 | -47.3636 | 2024-11-05 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 945eedb5-1feb-3d9c-a79b-1ad8b21b1761 | -2.6506 | -48.5844 | 2024-11-05 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| abde88bf-09ee-3463-a328-9a7f0f204494 | -2.6507 | -48.5629 | 2024-11-05 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| bc6e0529-7529-3df9-be84-ba3e5f782566 | -3.5446 | -47.3855 | 2024-11-05 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 275.1 |
| 4ef1dec3-fe4d-33d7-b3d5-475f16dbb56e | -6.1041 | -43.9593 | 2024-11-05 04:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 77b63469-fd5f-3e80-9745-44b401f1682e | -3.5632 | -47.3629 | 2024-11-05 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 490f9751-db35-3cd0-b3a8-38e6f1e77a4f | -3.563 | -47.4066 | 2024-11-05 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3dc1ab67-7fbe-3267-a292-7483e5e7c2c8 | -3.5631 | -47.3847 | 2024-11-05 04:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 300.6 |
| 10c7afbe-9fbc-3687-840e-500f826cb31a | -6.09194 | -43.94024 | 2024-11-05 04:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 457a0e05-47d4-3aba-934b-8d27cb4d5952 | -10.1199 | -36.48499 | 2024-11-05 04:33:00 | AQUA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7bdb881e-df3c-37f2-ad25-6d30692dc12f | -6.09235 | -43.94806 | 2024-11-05 04:33:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| fb07aaac-1b5d-31f0-b1e3-89d070772089 | -6.10955 | -43.95066 | 2024-11-05 04:33:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| debbdba8-ce76-3f37-a43a-8b2c1efa4cb2 | -10.12142 | -36.47522 | 2024-11-05 04:33:00 | AQUA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 13.9 |
| ec4f529a-6f01-3e2c-be3c-ec0af53dbfa3 | -6.10914 | -43.94283 | 2024-11-05 04:33:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 602f1d30-265a-3cb6-928c-441a516f4565 | -10.11218 | -36.47375 | 2024-11-05 04:33:00 | AQUA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5e4bcc35-5bf4-3fa9-839a-6185f0a94578 | -3.5632 | -47.3629 | 2024-11-05 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 79acf576-57e8-3b5e-8904-ef686cc69956 | -3.5444 | -47.4073 | 2024-11-05 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d1c3e952-2c4a-3ab9-a346-4ae9b6869552 | -2.6691 | -48.5624 | 2024-11-05 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| eb861d4c-8097-3068-8cea-9bb1c0253668 | -3.0397 | -53.2603 | 2024-11-05 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 2f2d32d9-9025-30c3-a059-df1f5f4f0ffe | -2.6507 | -48.5629 | 2024-11-05 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| da856e8e-57a1-35c9-840a-34748e37cd00 | -6.1229 | -43.9578 | 2024-11-05 04:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| fb1da0c5-8b96-3081-a0b2-b2c17bb8ea20 | -3.5447 | -47.3636 | 2024-11-05 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 69c41d7e-6ddf-3a2e-8f1d-30f980edef70 | -6.1041 | -43.9593 | 2024-11-05 04:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 9d864cdb-39e2-3d20-8c91-0df3b2f8616c | -3.5446 | -47.3855 | 2024-11-05 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 223.9 |
| a58a0606-3ebc-3ee2-9944-a1f91efced00 | -3.563 | -47.4066 | 2024-11-05 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| aebf6979-1b23-3f85-8243-336090b6284b | -3.5631 | -47.3847 | 2024-11-05 04:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 358.0 |
| 2844cf76-58b4-3e6d-bb6a-45e6b8d37db7 | -6.1041 | -43.9593 | 2024-11-05 04:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 7fb1c595-5803-3b56-a709-1addee9d74f6 | -3.5632 | -47.3629 | 2024-11-05 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c04c054b-7dd6-3c80-bb51-09ff63704400 | -2.6691 | -48.5624 | 2024-11-05 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 22940bcf-b0e5-323e-9dec-d09312cbd213 | -3.5444 | -47.4073 | 2024-11-05 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ec1704e2-cc59-3d09-a7d4-c4e7eabc517f | -2.6507 | -48.5629 | 2024-11-05 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| acef2c62-2736-379d-8540-17aae0274924 | -3.0397 | -53.2603 | 2024-11-05 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e011cb17-2eed-33ae-97d0-713c733e1e87 | -3.5447 | -47.3636 | 2024-11-05 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 7e7738cb-46e3-3e2f-bbca-5dff88e03137 | -3.563 | -47.4066 | 2024-11-05 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d7815028-8acb-3fbe-aa28-9896c9465a77 | -2.6506 | -48.5844 | 2024-11-05 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 21536112-26f6-3577-bd6d-a28c27c69f90 | -3.5631 | -47.3847 | 2024-11-05 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 306.4 |
| 2f9830f9-6e6a-37e4-ae7c-1192b2f9ae98 | -3.5446 | -47.3855 | 2024-11-05 04:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| a878e0a4-3d84-361e-9318-6e8c34fb0af6 | 0.64664 | -51.64331 | 2024-11-05 04:53:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7cbcbdf-0417-30b9-9ca3-38d954874551 | 1.00902 | -52.21785 | 2024-11-05 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 289030be-ee62-382a-bbcb-a5dda3632cf0 | 1.78406 | -50.43365 | 2024-11-05 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eebde9c1-0a73-39c3-a272-d022cf14ead5 | 0.2524 | -51.33564 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c786aee1-0875-3351-87fa-6dcabed08187 | 0.19349 | -51.06886 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f85dab6f-daa5-3bc4-abc9-571098fada8c | 0.0479 | -49.55475 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3846dde1-cc32-3c9b-ab70-61428f0d5787 | 0.0492 | -49.56305 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 754d791f-5d99-3152-b851-6385c932bbc0 | 1.79148 | -50.43628 | 2024-11-05 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df28c54e-4a1f-3fd5-b294-fba4d391fe4c | 1.78065 | -50.43418 | 2024-11-05 04:53:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d57847-4d1b-30a7-890a-eb90c4966e6f | -0.17197 | -51.30227 | 2024-11-05 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74de89aa-e520-3274-b6fb-32e3751d0bf5 | 0.04725 | -49.55058 | 2024-11-05 04:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 663ee4f6-6efa-3af1-a18d-5ee428912e1b | 0.80561 | -51.91738 | 2024-11-05 04:53:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a4e5c00c-ae75-384c-a100-166106739ff8 | -2.15873 | -47.55771 | 2024-11-05 04:53:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39115411-3bc1-34fa-afb7-637776ec92f6 | 0.21219 | -51.02567 | 2024-11-05 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
