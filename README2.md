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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f30daaca-fc29-3f6d-ae5c-fc270dd6246b | -11.1818 | -55.920502 | 2026-05-24 01:21:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c956378-2778-33c3-81b1-517c3a328714 | -15.0972 | -57.6334 | 2026-05-24 01:21:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9da2cf7a-c2f8-3776-bf28-960d159b406a | -12.9004 | -58.175201 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebb08de8-dac4-3023-85b1-856e5d879874 | -12.889 | -58.170502 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e58b97ca-9d23-3c39-9ed7-861009f1f928 | -14.0271 | -53.350899 | 2026-05-24 01:21:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 918ed1fe-370a-38d6-ac58-a44a91d905aa | -12.8906 | -58.177502 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6106818d-63ce-3d94-adbc-742acf539d23 | -12.5587 | -57.174702 | 2026-05-24 01:21:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd20d7f-209f-319b-bb33-13b65c62de15 | -11.5474 | -56.952599 | 2026-05-24 01:21:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2c352e2-8f20-30e2-bc49-8eaaaf8d1401 | -14.0174 | -53.353401 | 2026-05-24 01:21:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 34ca2f54-66f3-3d03-a0c2-03ae5bdcd0ac | -12.5571 | -57.1675 | 2026-05-24 01:21:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92b90f9b-0a97-3efd-9f8e-c6548d759f74 | -11.1799 | -55.912498 | 2026-05-24 01:21:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcd62a5c-1f44-3cc0-9d50-6f69546d5e57 | -11.5457 | -56.945202 | 2026-05-24 01:21:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7adb1c21-c25d-3e84-be33-0266365f0440 | -12.8874 | -58.163502 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8400206f-792e-34ea-bd5f-597b7f34dd43 | -15.0956 | -57.6264 | 2026-05-24 01:21:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9aad4681-9f2a-37c0-a5c5-cf976ca11b07 | -12.5554 | -57.160301 | 2026-05-24 01:21:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d20319a8-b160-3062-be93-7dde29a66908 | -12.8937 | -58.191502 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae43742-c64e-386a-be7f-b7a68f72b94a | -15.1054 | -57.6241 | 2026-05-24 01:21:00 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afe0b9c5-e892-3a30-a302-c65cab12b4f8 | -12.8988 | -58.168201 | 2026-05-24 01:21:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54535d68-bd97-3309-a853-688143781697 | -12.8859 | -58.1891 | 2026-05-24 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 63e00ccd-f8ad-34bd-a73b-27bb835e0d9e | -12.8861 | -58.1692 | 2026-05-24 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d0c6f770-e9c7-3e15-852e-0791454057b4 | -18.657 | -48.8785 | 2026-05-24 01:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 007c83cf-6e66-3dc2-8362-06d10e814cb7 | -12.8861 | -58.1692 | 2026-05-24 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 826ec613-e15a-3ec3-b3b0-97b613f4d490 | -12.9052 | -58.1676 | 2026-05-24 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 5eb4e2b6-c81b-3d7d-a1f3-931089520842 | -12.8861 | -58.1692 | 2026-05-24 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0beef36a-a146-3bfd-90ba-0668ece13345 | -12.9052 | -58.1676 | 2026-05-24 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 51563544-1641-3f93-acdc-ff26e1f11a86 | -12.8861 | -58.1692 | 2026-05-24 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| dd467b75-1734-3c01-b095-43c7ec17cf1b | -12.9052 | -58.1676 | 2026-05-24 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 1b8799de-4e46-3d03-8f06-9ce1744a204e | -12.8861 | -58.1692 | 2026-05-24 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| bfa6c4f4-c0c7-3a89-83cf-e51514bf909f | -12.8861 | -58.1692 | 2026-05-24 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b40a7990-28a2-39ce-9a67-c5b98f95a7c8 | -12.8861 | -58.1692 | 2026-05-24 02:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 6cd2ee0e-0113-327e-9ca6-7d47a923fdd2 | -12.8861 | -58.1692 | 2026-05-24 02:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 4a3c6aa3-4cb0-3d72-8403-0836a4dfccd0 | -12.8861 | -58.1692 | 2026-05-24 02:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 0eaa9dfd-1616-3091-a8cc-c1d42c99fd53 | -12.8861 | -58.1692 | 2026-05-24 03:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 5369ae33-ad01-3329-bda8-0ca9150dd7fd | -8.13937 | -41.18193 | 2026-05-24 03:25:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae540c1e-0dff-33d0-9574-c3e109899ba2 | -8.13977 | -41.18237 | 2026-05-24 03:25:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cf50154b-ccc4-37db-bf39-596176593a0e | -3.9578 | -43.1277 | 2026-05-24 03:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ede3edad-7583-3de0-8fda-efebb8bf928e | -3.95661 | -43.13435 | 2026-05-24 03:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa364b8c-ddac-3e7c-9de5-aa663890c5b9 | -20.91297 | -46.79115 | 2026-05-24 03:30:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5134b54c-07dc-34d4-8a7c-311c5a640a1c | -20.91474 | -46.78904 | 2026-05-24 03:30:00 | NOAA-20 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 41f54f04-7840-3a5e-9f8d-b4f0dc3359c2 | -12.8861 | -58.1692 | 2026-05-24 03:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| f683e603-c434-317a-9020-57ebe3ee89ed | -3.95823 | -43.12497 | 2026-05-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6859ae0d-16bd-312a-82c6-971dc90cbfee | -8.4158 | -46.82752 | 2026-05-24 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a573444d-efb1-36e9-b713-019f0ea56081 | -7.73204 | -44.55052 | 2026-05-24 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 373c4095-9d2e-3331-b376-86dac69be0fd | -3.96154 | -43.12549 | 2026-05-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c658cb2-aa3e-3b36-a971-78ec2a2585f5 | -3.95769 | -43.12844 | 2026-05-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2d468ee-281e-3357-944d-c7edd2a4eb08 | -3.42443 | -43.16533 | 2026-05-24 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 131f1a38-3f3c-3684-bfc3-2857189f9159 | -7.13391 | -44.07058 | 2026-05-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 381ab0a3-a148-34a9-8805-e57ca562d32a | -6.08224 | -44.00801 | 2026-05-24 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3a534b14-a052-322e-ba81-cb3beb7681ba | -4.64857 | -43.14851 | 2026-05-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4b622b5-12cd-3dd1-8463-a673e92fa47e | -3.9076 | -40.97954 | 2026-05-24 04:14:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 578c46db-65a8-3872-9ec4-c40ccbe310ee | -7.3612 | -43.85915 | 2026-05-24 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b401244a-a120-393c-a5f3-e5c15b8a3cd1 | -5.94962 | -43.48915 | 2026-05-24 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4a3e91e-2149-30a1-a775-64389fcfcf7f | -4.64803 | -43.15197 | 2026-05-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a8ff2e7-ba7f-3e3a-874c-7d3d1cec5f75 | -8.24964 | -43.72707 | 2026-05-24 04:14:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8556cff3-ccca-38c6-ba78-4200f64dc146 | -3.95714 | -43.13191 | 2026-05-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4435c9c-6a43-3ccb-9ea4-e60500a63c0c | -4.14345 | -44.19505 | 2026-05-24 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d8a3ba7-33a4-3d6d-b7e3-d865c60248f4 | -4.38516 | -43.28806 | 2026-05-24 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d95934b2-b69d-3b00-b700-125aa77bdc35 | -4.4321 | -47.73138 | 2026-05-24 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 93829ba3-315f-36d3-94db-1a5ca706334f | -4.65242 | -43.14557 | 2026-05-24 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abae7c46-27e7-353d-b10e-e89dde1f7958 | -6.85163 | -48.73304 | 2026-05-24 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3bbe8d7-0afb-3d90-98f0-a90c39cca231 | -3.961 | -43.12895 | 2026-05-24 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d67b5e3a-e896-3c2e-b165-4084469898d2 | -4.14684 | -44.19558 | 2026-05-24 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33a787c2-7fc5-3fa8-bfa1-d5eff05702de | -7.22323 | -46.96133 | 2026-05-24 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9610a58e-8bdf-38b9-bdd8-c1f0693010d8 | -8.14246 | -41.18196 | 2026-05-24 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 82c3e894-8c85-3b4a-926b-939a870c06f3 | -6.85581 | -48.73374 | 2026-05-24 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d767119-0365-3719-9330-e6570b69fd7b | -7.13447 | -44.06706 | 2026-05-24 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c45abf-a76b-32ac-97b5-096a22a0b248 | -8.70815 | -47.91804 | 2026-05-24 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3719e962-9058-3d26-9dca-140a61928328 | -12.54591 | -54.61955 | 2026-05-24 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2377c62c-3b7a-352c-b331-dae659eefe1e | -14.01215 | -53.36077 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e6d3d0c-3d14-3858-bc69-7d96e17d0b1c | -11.94817 | -49.29739 | 2026-05-24 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa26414b-ccbb-3287-ab92-690434cf8b8c | -11.18339 | -55.91494 | 2026-05-24 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 68d645c1-56f8-3c5f-8263-94cbece56be4 | -22.5814 | -44.08264 | 2026-05-24 04:17:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32592b49-dad2-3bb2-b6dc-ce4e8fa617b2 | -8.85978 | -46.93494 | 2026-05-24 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f958e046-7278-375d-8af8-ae23e280efa9 | -9.60158 | -44.43366 | 2026-05-24 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f8e03b9-1ab9-399f-af63-d8535e7ea582 | -11.17622 | -55.91864 | 2026-05-24 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4adf3003-6b48-3b71-95fa-f0ef89c2b503 | -11.17413 | -55.92028 | 2026-05-24 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 93d241e3-8148-321f-a35c-6c34c7cc985d | -11.44525 | -54.09318 | 2026-05-24 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06d873fa-4727-3af4-91b2-eb67ba0cce50 | -11.17511 | -55.91545 | 2026-05-24 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6307c776-ae01-38fa-9ec7-d28fbe7d1a86 | -11.45114 | -52.92788 | 2026-05-24 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa79cb25-df08-32c6-aaed-90c95cc8e197 | -11.44032 | -52.92905 | 2026-05-24 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21b800a4-820b-3b44-b052-29e432147064 | -11.92747 | -45.00427 | 2026-05-24 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74cfa24f-b8e5-3f91-a772-e0ca1ee64b08 | -12.04627 | -47.33529 | 2026-05-24 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a877b714-38d3-3ba4-aa55-1262b08c0db5 | -8.70678 | -47.9146 | 2026-05-24 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8674937-a26e-30f8-995c-e1e1ec4b376e | -10.97841 | -49.43379 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c1c555b-9941-3135-b604-47f3594b22fd | -12.88924 | -58.17002 | 2026-05-24 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 98ba040f-7909-3f95-b790-4c1b111ec822 | -12.55125 | -57.16301 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 223d9711-f091-38ee-8e34-843489875b84 | -8.85906 | -46.93932 | 2026-05-24 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a754796-92b5-384c-8a59-99fdb45c6599 | -11.276 | -53.96531 | 2026-05-24 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d4e0976-16d8-3b59-a431-dd5df6a279e6 | -12.88635 | -58.18345 | 2026-05-24 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d5bdd4d3-f222-3a23-a047-f6bfa9658fea | -14.01272 | -53.35778 | 2026-05-24 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a344e4f-08c3-3ddb-bf86-7302e8eb7c0e | -11.60649 | -55.33676 | 2026-05-24 04:17:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3759ad36-b1d1-32be-86a6-195fb47d90f1 | -10.53346 | -46.46823 | 2026-05-24 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01c50b62-b2c5-32d8-bf18-79047bf5bdaf | -14.77719 | -52.66902 | 2026-05-24 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d8a186-215a-36bf-ab7e-0cac4fa6d9d1 | -12.88778 | -58.1768 | 2026-05-24 04:17:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 897093df-1a33-3a99-99bd-7526723042ae | -11.18039 | -55.92126 | 2026-05-24 04:17:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 202bba66-d6aa-39f4-9852-bee6ffb0cd55 | -12.55391 | -57.17731 | 2026-05-24 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c506c5-94c9-347d-bc06-6d4e618d1415 | -11.55036 | -56.95142 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5f7ff84-87a1-3850-a124-66b2a68dca3c | -14.73236 | -52.69529 | 2026-05-24 04:17:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f84283bf-f62a-3bac-afb3-bd990e0f6938 | -11.54266 | -56.95571 | 2026-05-24 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 43bef30c-26d1-35a6-8fe1-cd31488e9b2e | -10.97907 | -49.43007 | 2026-05-24 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
