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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9b6f0f0-526e-3c26-a4b6-7da271cb58ef | -11.36579 | -38.24969 | 2025-01-26 00:00:00 | TERRA_M-M | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b9e3ebad-eef5-3c39-9d06-6c4a8833a4a8 | -11.95247 | -41.33127 | 2025-01-26 00:00:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 2dfe03da-4a2f-3105-93d2-90b608715392 | -7.68453 | -35.27676 | 2025-01-26 00:02:00 | TERRA_M-M | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 47c42ebb-59d6-347b-961a-140943c444b0 | -7.36324 | -35.02474 | 2025-01-26 00:02:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 30cf4a5a-0b43-3c44-8fe2-4873cf705f6c | -7.2295 | -35.78238 | 2025-01-26 00:02:00 | TERRA_M-M | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 831ae7cd-f44a-3ac2-9e51-1528e33512f4 | -7.27256 | -39.66135 | 2025-01-26 00:02:00 | TERRA_M-M | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| eec110bd-d170-3a95-83fe-3d8aa953b706 | -7.41476 | -35.1951 | 2025-01-26 00:02:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9d4f21b6-d18f-3e53-ad86-e3890bfe118e | -3.80785 | -38.68686 | 2025-01-26 00:02:00 | TERRA_M-M | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 81692825-af6f-31a4-b57b-2fafad1f0af1 | -7.22066 | -35.78365 | 2025-01-26 00:02:00 | TERRA_M-M | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e3258c1f-d7b1-38ee-b94a-7287889be957 | -20.227501 | -40.215 | 2025-01-26 00:23:00 | METOP-B | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31a4a396-d8e3-37ca-8bbc-18b0e147840d | -11.9421 | -41.302898 | 2025-01-26 00:23:00 | METOP-B | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 092782c3-5d26-3ddf-80e5-09c58a303424 | -15.0381 | -45.622398 | 2025-01-26 00:23:00 | METOP-B | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b70f4c29-bcd5-3f80-afca-93af60d7c035 | -13.4691 | -44.004501 | 2025-01-26 00:23:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5b91a4-7c4f-3971-bbe1-e431bbe155c5 | -15.6661 | -41.557301 | 2025-01-26 00:23:00 | METOP-B | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5846ba4f-cb33-3674-bab8-8d8a18813fb4 | -5.2701 | -45.756001 | 2025-01-26 00:23:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5298304-e347-3017-b53e-b61c8c848883 | -13.2231 | -43.9687 | 2025-01-26 00:23:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed5734d-6e87-3062-88ed-e569274f1fe8 | -9.7946 | -36.004002 | 2025-01-26 00:23:00 | METOP-B | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7fc04471-e1db-301e-beef-a03763a78ad9 | -13.2212 | -43.9604 | 2025-01-26 00:23:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 575404b7-aee2-324b-a4af-3c7dd4c3c92e | -10.8048 | -45.156601 | 2025-01-26 00:23:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cc238e3-1bff-3596-9a5c-8be917b87658 | -15.0397 | -45.629601 | 2025-01-26 00:23:00 | METOP-B | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 77cb31dc-b799-3be1-a5d0-f79faf5d5eea | -16.5469 | -43.690201 | 2025-01-26 00:23:00 | METOP-B | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c42b36f-f2f7-3fd3-9ba5-ce78eb95fb86 | -7.8725 | -44.175999 | 2025-01-26 00:23:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c8f813a2-811f-340a-b805-cfe21cf48a65 | -13.4936 | -52.920898 | 2025-01-26 00:23:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dec0a5ed-99eb-38b9-88e0-76be29a02c1b | -17.2973 | -53.762901 | 2025-01-26 01:18:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9c17bec1-eb7b-33e6-ba06-e8d356cc04d2 | -13.4842 | -52.940899 | 2025-01-26 01:18:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a666b203-8ab4-32ae-a250-271e3dde92e1 | -9.2614 | -60.3069 | 2025-01-26 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66b53266-59b6-3d9a-9e23-e10b2197dbb3 | -17.299101 | -53.770401 | 2025-01-26 01:18:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 473f0815-f73b-3cd0-a9bc-52997799b3f6 | -9.2632 | -60.314999 | 2025-01-26 01:18:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b35ca22-53af-3671-87dc-a1da9c8d5487 | -21.61938 | -57.04786 | 2025-01-26 01:36:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 244b8ae9-7629-3664-93c7-b93e5dd1eafe | -5.42255 | -35.56948 | 2025-01-26 03:27:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80996ba2-41b1-3be9-9100-4f59ca486b39 | -5.41881 | -35.5689 | 2025-01-26 03:27:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84b22d30-6c16-3e8c-9775-cea847f73daa | -8.11673 | -43.14212 | 2025-01-26 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2688c7a3-2954-3360-b798-458217f44ebd | -11.42981 | -38.40971 | 2025-01-26 03:29:00 | NOAA-21 | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab3ff8c6-4c78-3383-9a75-b7d2ef9c4bca | -8.11753 | -43.13782 | 2025-01-26 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7dce7cdc-e6d9-3a9e-8d0a-9b3ef6896131 | -7.88215 | -44.18868 | 2025-01-26 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a3e3027-3e18-3e86-94af-454a0aba922e | -7.39289 | -35.16479 | 2025-01-26 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 15d5449e-622c-38ca-b791-faa7b52f0965 | -7.2701 | -39.66692 | 2025-01-26 03:29:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f40d849-6d00-3f48-bfdf-186ede7f6a5a | -5.68966 | -39.722 | 2025-01-26 03:29:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 86436bf3-c95d-317e-839b-25a212e1434c | -8.15203 | -35.03114 | 2025-01-26 03:29:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e182069f-b861-304c-8d3f-338e227cdc3d | -7.22291 | -35.78254 | 2025-01-26 03:29:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1def313-a4d9-3eef-97b4-f73fddbb9506 | -7.39646 | -35.16537 | 2025-01-26 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d4fe54b4-68b5-3533-9f36-1f5023563a87 | -7.39357 | -35.1607 | 2025-01-26 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 635c29cb-6774-37b8-8552-0408e1f2a730 | -7.27145 | -39.66409 | 2025-01-26 03:29:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f23d9ebd-b44a-3620-b272-376c95e5b860 | -7.2266 | -35.78314 | 2025-01-26 03:29:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b6f5557c-f164-31f9-bf58-212b1c37ddbf | -13.2228 | -43.97894 | 2025-01-26 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20cbb1b1-b9c9-3d04-899f-5ee15b39ede6 | -13.22845 | -43.98022 | 2025-01-26 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4b128c7-38fd-3525-b95c-25df59f99926 | -19.00807 | -40.50283 | 2025-01-26 03:32:00 | NOAA-21 | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 89925c2c-b44c-3659-a5fe-68725320bb99 | -12.11644 | -43.63813 | 2025-01-26 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8306704-60f9-3fb0-a882-09231a862a69 | -16.68347 | -43.88555 | 2025-01-26 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b98abb7-2cc1-3571-9302-0a26ffb932ff | -10.80448 | -45.1766 | 2025-01-26 03:32:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bd3f4e7-9ae4-3baf-b54a-9526a024f2c4 | -19.10876 | -40.19098 | 2025-01-26 03:32:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 476ad229-0621-38ab-99e4-c65ac3209cf7 | -19.13106 | -40.40857 | 2025-01-26 03:32:00 | NOAA-21 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9792ebd6-bafd-320e-bcb0-5fdbefa560ed | -10.80272 | -45.17673 | 2025-01-26 03:32:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1dba7985-5760-344d-af05-af7b6fc86b49 | -15.03902 | -45.64324 | 2025-01-26 03:32:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72effe0e-5cb0-39e7-bbc7-b13b530fba57 | -12.11076 | -43.63704 | 2025-01-26 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f557160-a211-3066-bf34-2202de60047f | -16.35082 | -43.69826 | 2025-01-26 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 189d99d8-26af-36f2-9483-ae7f621f7f77 | -21.51605 | -41.0939 | 2025-01-26 03:34:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b08787cc-3064-3189-8ed3-ea528f1498ed | -20.34749 | -40.36086 | 2025-01-26 03:34:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e3b62488-b153-373b-a217-7a778a4478eb | -19.71718 | -40.35482 | 2025-01-26 03:34:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4cf8e516-3315-3177-a706-b26d673f7bbe | -22.78764 | -43.75668 | 2025-01-26 03:34:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3fefd58f-7276-3b5e-875e-ffe6637a1e94 | -5.4147 | -35.5603 | 2025-01-26 03:40:00 | GOES-16 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 84.1 |
| fe47db25-b570-393b-a88c-031db974450b | -3.24792 | -48.07792 | 2025-01-26 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6102da6-86bd-33be-9b85-dda02ecdc856 | -3.24812 | -48.07491 | 2025-01-26 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d2c1535-a22e-3b6d-a5f4-b16837ba2c5b | -3.8099 | -40.98611 | 2025-01-26 03:53:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0f320a95-24eb-3005-80ce-3fe1b073ae4a | -4.69836 | -38.43475 | 2025-01-26 03:53:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42405e95-2d7f-346b-92ac-3c281b1d7383 | -3.24861 | -48.07392 | 2025-01-26 03:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f970dc63-e81a-37cd-821b-d4bad0205702 | -5.27544 | -45.77232 | 2025-01-26 03:55:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fa16d62-3edf-3771-85bf-7454dac1b583 | -10.80903 | -45.17378 | 2025-01-26 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e641f3d1-c76c-39ec-8fc3-a1b5475aac7f | -5.34921 | -40.65724 | 2025-01-26 03:55:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5ecaf8ef-638c-3fbb-b0d9-a88b2bfd1da2 | -11.4289 | -38.40926 | 2025-01-26 03:55:00 | NPP-375D | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9afa219d-ee35-3edc-b3f1-e20885daaab0 | -10.77202 | -44.55117 | 2025-01-26 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43e413cd-0b24-3af9-ad21-a91e92163073 | -9.55227 | -40.632 | 2025-01-26 03:55:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 016dcbae-bfa3-3f43-a831-fac57e740c79 | -12.11096 | -43.63785 | 2025-01-26 03:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a9e6000-96ac-3881-9070-2ac6c89ac667 | -7.87876 | -44.191 | 2025-01-26 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a515787f-404f-33d0-85f9-99ba9ecd6e33 | -5.35271 | -40.65779 | 2025-01-26 03:55:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e58e6c05-640a-33af-9c97-cdf6e0cdd84a | -12.1147 | -43.6385 | 2025-01-26 03:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1cf9328-1ace-35c3-a006-91bf63135796 | -7.88353 | -44.18796 | 2025-01-26 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd323cbb-a441-3b10-a6c1-bd2c83c62b61 | -9.5256 | -47.78029 | 2025-01-26 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83786c22-2798-38a1-81aa-2315cc206518 | -5.68831 | -39.72292 | 2025-01-26 03:55:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c12048bc-9991-3859-8b5a-3a8e19f8a935 | -8.12007 | -43.13747 | 2025-01-26 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7263c46-36dd-35b5-bbd0-2da15352caa5 | -8.11927 | -43.14224 | 2025-01-26 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3442748-eb4b-33ae-8942-742a12462e24 | -10.85041 | -44.31326 | 2025-01-26 03:55:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7456a1fc-10b5-31c8-8ea8-e9ce2471d30d | -7.2732 | -39.66606 | 2025-01-26 03:55:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6872aa2e-431d-3f7f-a220-2b0230985e3d | -6.37814 | -39.25337 | 2025-01-26 03:55:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 347740be-9752-3dfb-a6aa-da742e14c815 | -7.59483 | -46.45781 | 2025-01-26 03:55:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26a7ecda-eaec-3914-91ab-7562edcbfe00 | -7.22426 | -35.78021 | 2025-01-26 03:55:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c647cff1-9fff-3de7-b341-2068d8b7bff7 | -6.39936 | -46.32955 | 2025-01-26 03:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25d192b4-6450-3af1-a59a-d6c55addf6a0 | -10.80486 | -45.1729 | 2025-01-26 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b57759b-632c-326a-9b84-f3bc222c5e24 | -7.26985 | -39.66552 | 2025-01-26 03:55:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b0e708a-3f6b-3100-94d7-d00f76614f01 | -9.52615 | -47.7773 | 2025-01-26 03:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25dcd12b-c700-35fd-acdf-0e06cae516a2 | -8.97933 | -44.25327 | 2025-01-26 03:55:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f02b9bf-4c04-3997-a7ec-ee6a5de5958a | -7.87675 | -44.19156 | 2025-01-26 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1430608-16ef-3cea-bc66-2df85edd13a0 | -11.36658 | -38.24683 | 2025-01-26 03:55:00 | NPP-375D | OLINDINA | BAHIA | Brasil | 2923100 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d825b73c-4e30-3c95-8ba1-d7243e38f99f | -7.88149 | -44.18853 | 2025-01-26 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76c48e45-55c3-307a-804c-d9088a136301 | -5.68887 | -39.71933 | 2025-01-26 03:55:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ae4871d-9376-3a5c-bdbe-5aa5782914ef | -10.80419 | -45.17673 | 2025-01-26 03:55:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6df48d8-d565-3188-a85d-340d4618e87d | -9.49403 | -40.37029 | 2025-01-26 03:55:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01d3dfe0-77d2-3b0a-8ff0-c3d4a64b88e3 | -7.22365 | -35.78429 | 2025-01-26 03:55:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 049c3ec4-cdf9-37ac-b2e5-2ac9dfa1c504 | -13.22805 | -43.98133 | 2025-01-26 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d5b83d4-c889-330b-acc2-c67946b859ee | -13.22499 | -43.97837 | 2025-01-26 03:57:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README2.md)
