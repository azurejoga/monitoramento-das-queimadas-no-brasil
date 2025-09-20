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
| 8ad91559-62d7-3ca4-b30e-872968b2968b | -11.467 | -43.5485 | 2025-09-20 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c542c328-667c-3349-b113-bf39caa8b268 | -12.8018 | -44.1129 | 2025-09-20 00:00:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 52c53cfe-16c3-3533-8bd8-1a754f108271 | -15.2783 | -56.8555 | 2025-09-20 00:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 40.8 |
| b62cb1ad-77f7-320f-8897-57e621305796 | -5.1181 | -43.1964 | 2025-09-20 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 431331c0-3900-31bb-b90e-bb21ef8e8427 | -19.6073 | -57.7531 | 2025-09-20 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 151.4 |
| bdeb3211-d595-31e3-ab29-b309fb9cabb1 | -4.368 | -46.291 | 2025-09-20 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 196.4 |
| e174c342-9fb0-3d5b-afe2-60aba082a8b6 | -19.6274 | -57.7504 | 2025-09-20 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.5 |
| 68c7a6d2-df85-31a0-80cc-6190a5ed60aa | -11.4665 | -43.5722 | 2025-09-20 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3777ee88-38e2-34dd-a65b-3a3363f42322 | -19.607 | -57.7739 | 2025-09-20 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 2509f07f-4323-3e3a-8d4e-31a1f4d3d9eb | -19.6077 | -57.7323 | 2025-09-20 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.7 |
| 0e8aba9c-03d9-3aa5-a609-a644d5069dbd | -4.3495 | -46.2698 | 2025-09-20 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5b6cb521-5079-384c-9361-9d9ecbf05a7d | -5.0994 | -43.1977 | 2025-09-20 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 152.2 |
| eda99b42-b4f7-3f08-a3b4-950732245319 | -3.5202 | -52.7384 | 2025-09-20 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ac174343-b122-3fbc-9c73-e706c90291d5 | -12.782 | -44.1397 | 2025-09-20 00:00:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| aeec4848-06d2-3d40-aa8e-5f1494acdfeb | -5.118 | -43.2198 | 2025-09-20 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| f855ec21-10f7-331d-a9e4-dda09a2e2e85 | -7.3847 | -47.0378 | 2025-09-20 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 274cca83-f4b9-3983-89ee-ca796f27b625 | -5.0992 | -43.2211 | 2025-09-20 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1251f67e-f3db-3ecd-b1f4-4690cbb07080 | -11.6731 | -44.8736 | 2025-09-20 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 2c837133-8f50-35e3-b9f2-c804a5276c27 | -3.5161 | -49.4528 | 2025-09-20 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| febd17a3-78e7-31a3-aea0-4238ef92b31c | -5.1934 | -45.4835 | 2025-09-20 00:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| b16c9477-ffd2-3aaa-85e7-dda8b407cec1 | -4.3681 | -46.2688 | 2025-09-20 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 8e0d97d7-08a6-3337-9990-deddf2dfd004 | -12.8014 | -44.1365 | 2025-09-20 00:00:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 164.3 |
| cbb6ad16-0623-3448-b351-8fa43a650384 | -4.3494 | -46.292 | 2025-09-20 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 63a9189d-cf84-3077-a989-cfbff6a93be8 | -12.8207 | -44.1333 | 2025-09-20 00:00:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4040a8c1-13ea-35a3-904e-a59269bf74fe | -5.1181 | -43.1964 | 2025-09-20 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.6 |
| a483c311-a880-3fcc-9464-280b4d59828e | -11.4665 | -43.5722 | 2025-09-20 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 225f3daa-8c06-3234-b131-c4cf181423c9 | -5.0994 | -43.1977 | 2025-09-20 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 6c13c4d1-10f0-38d0-bc15-c4d9cbbf01c3 | -11.467 | -43.5485 | 2025-09-20 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| f3c27a6b-d91c-3dec-80aa-c4be90d9266f | -12.8014 | -44.1365 | 2025-09-20 00:10:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| cdc6ab95-1ed6-312f-b833-9cf2906c61aa | -4.3494 | -46.292 | 2025-09-20 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 165.9 |
| af91aa88-0df7-3f6d-b849-9e756c19ac54 | -5.118 | -43.2198 | 2025-09-20 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7ba4b83d-979f-31a9-a2b2-8bf0ccb116d2 | -20.3532 | -48.7955 | 2025-09-20 00:10:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7c06b894-402d-3961-8aa0-286021a270a2 | -5.0992 | -43.2211 | 2025-09-20 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dd32ebb2-e1cb-35fd-9878-b746a72e859c | -5.1934 | -45.4835 | 2025-09-20 00:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 559b772d-0980-3404-88a1-6e2fbf7b8c63 | -7.3847 | -47.0378 | 2025-09-20 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 21b28694-b3e6-3c59-8357-56560816ba2d | -4.3681 | -46.2688 | 2025-09-20 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 0a5ab024-8783-398a-ac94-ba366d40b060 | -4.3495 | -46.2698 | 2025-09-20 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 41ee54c0-2116-3a9e-9165-ed2a4dc9622e | -7.3844 | -47.0599 | 2025-09-20 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 9c04d472-3d3b-3fe6-b209-f06dc0242b0b | -11.6731 | -44.8736 | 2025-09-20 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 692885d1-1fe5-3d7c-bee8-36df2ae8e015 | -3.5161 | -49.4528 | 2025-09-20 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b3168e39-2405-32be-aa64-b4aee3b8b79a | -4.368 | -46.291 | 2025-09-20 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 535edee7-10fa-32ba-91c3-456751d2231a | -5.0994 | -43.1977 | 2025-09-20 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 30c1a961-debf-38e1-a201-0ab3db70e0d6 | -5.0992 | -43.2211 | 2025-09-20 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 04cdbcb4-ce7c-36db-81be-02620e8eb91f | -23.1396 | -48.6923 | 2025-09-20 00:20:00 | GOES-19 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 852d764b-1ef1-3632-911f-c8cfe621c5b1 | -4.368 | -46.291 | 2025-09-20 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 4a1c6c17-a6b5-3793-9541-481d3f730420 | -7.3847 | -47.0378 | 2025-09-20 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b1cf10e0-949d-3ce4-89b5-76b79c04f8db | -3.4528 | -51.2179 | 2025-09-20 00:20:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 280dfc60-5fda-37ea-a0c5-5ad8d69abba3 | -4.3681 | -46.2688 | 2025-09-20 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 55d1b8fc-6b84-34cb-b0b7-c69fc81263d9 | -19.6073 | -57.7531 | 2025-09-20 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.0 |
| d4382328-10ff-388d-989d-9ea319413679 | -5.1934 | -45.4835 | 2025-09-20 00:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 67e1fe7b-90f8-3fae-adc5-a43a37d8a803 | -6.2417 | -47.3025 | 2025-09-20 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 0a004c2b-e9d0-3534-8424-61584d280f43 | -11.4665 | -43.5722 | 2025-09-20 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 8fb6e2f7-0764-3180-be82-9ca6bd941540 | -5.118 | -43.2198 | 2025-09-20 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 8b343739-0791-34ba-8d13-cadcc54a808f | -11.4857 | -43.5692 | 2025-09-20 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 4a0bd09a-3aec-3bbc-b6c5-63950ac4f967 | -11.467 | -43.5485 | 2025-09-20 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| b1ac3240-0874-3397-a0b3-df0fa8e4e6c9 | -7.3844 | -47.0599 | 2025-09-20 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 44.9 |
| dadcc784-e692-3faf-b31a-a0c589a264b9 | -3.5161 | -49.4528 | 2025-09-20 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c9ab7ca5-df7e-330e-b966-9bd1ba8b94bf | -11.6731 | -44.8736 | 2025-09-20 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| c124f2c8-15cb-3888-a11e-d80b22105305 | -5.1181 | -43.1964 | 2025-09-20 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 172.8 |
| e5b3ab35-1434-32bd-8bbe-6204ff1a622b | -4.3494 | -46.292 | 2025-09-20 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 108.1 |
| db2fc216-ff4b-35a0-8dc6-7be94cfd4a33 | -25.04509 | -49.23905 | 2025-09-20 00:26:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| ebf6b611-fa8f-3778-a72f-038512879b7d | -25.04342 | -49.22409 | 2025-09-20 00:26:00 | TERRA_M-M | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| e6c1c5d7-f73c-32ce-86bd-afd5e860b9f0 | -25.50071 | -49.75462 | 2025-09-20 00:26:00 | TERRA_M-M | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| 4fe484d7-1c35-3f5b-85cc-0295007132b5 | -21.39944 | -45.54859 | 2025-09-20 00:28:00 | TERRA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 352bfc1f-92d6-3872-ade8-e96875308de8 | -21.29541 | -45.6064 | 2025-09-20 00:28:00 | TERRA_M-M | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e893c67f-b5bf-32b1-8dda-efcb541b7eac | -23.29059 | -45.78416 | 2025-09-20 00:28:00 | TERRA_M-M | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| e354c776-c66f-3254-a603-59907614b00e | -23.01416 | -46.90049 | 2025-09-20 00:28:00 | TERRA_M-M | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 70e16fef-99fc-33d3-bb20-f015a8af909b | -20.34648 | -48.7892 | 2025-09-20 00:28:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7b17c358-7134-3540-9ea0-4392a6cd38e6 | -23.43301 | -47.61749 | 2025-09-20 00:28:00 | TERRA_M-M | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| adbc4e19-7082-300b-ab7b-543b48b3fd2a | -22.47279 | -47.5481 | 2025-09-20 00:28:00 | TERRA_M-M | SANTA GERTRUDES | SÃO PAULO | Brasil | 3546702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 7b643852-ad24-3355-a571-15043ddc057f | -22.63955 | -42.12456 | 2025-09-20 00:28:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 7295e119-cecc-31c3-8d90-4514a928c81d | -22.63662 | -42.11935 | 2025-09-20 00:28:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 82de27f5-862f-3c4e-8cd4-5dbe00b4e89f | -23.33718 | -49.34305 | 2025-09-20 00:28:00 | TERRA_M-M | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| c80767a1-0a6f-34db-a3a7-caac9fba9234 | -23.33073 | -49.33577 | 2025-09-20 00:28:00 | TERRA_M-M | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| dd3e4611-1f8e-32bb-9a3f-5a1f9e3aef22 | -21.50156 | -45.83132 | 2025-09-20 00:28:00 | TERRA_M-M | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| de47367d-febc-3053-987b-556cd9a5e5bc | -21.5942 | -41.26632 | 2025-09-20 00:28:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| d7d7cb8f-d70c-306c-91d9-630e8e462d7b | -23.33229 | -49.34927 | 2025-09-20 00:28:00 | TERRA_M-M | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.0 |
| 4cd43871-9e15-3358-be67-2bf08710d7f1 | -23.23759 | -46.64044 | 2025-09-20 00:28:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 73078ac4-9ec4-3780-a175-bac90033b6ee | -20.35625 | -48.78792 | 2025-09-20 00:28:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 8c58f601-f90f-34da-bcc6-9cf5552e2817 | -22.63764 | -42.11275 | 2025-09-20 00:28:00 | TERRA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 9560b665-e474-385f-b55f-96997de6ee4b | -23.52059 | -47.19884 | 2025-09-20 00:28:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1999d8a6-5fcb-36a7-bc2d-656a56e8827d | -23.42355 | -47.61912 | 2025-09-20 00:28:00 | TERRA_M-M | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2f7c05ec-bc1c-3b22-ac79-e53d9856d694 | -22.83583 | -47.59143 | 2025-09-20 00:28:00 | TERRA_M-M | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 71a577d5-7d9b-32ae-a4ca-e85f1816618f | -23.23889 | -46.65058 | 2025-09-20 00:28:00 | TERRA_M-M | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4a7dccc2-84fe-30a2-ae60-e07f366bfbf4 | -23.50998 | -47.1898 | 2025-09-20 00:28:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9712ea47-19f9-34dc-9be0-4a4510c7d741 | -23.20608 | -50.25544 | 2025-09-20 00:28:00 | TERRA_M-M | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| 482df734-3afd-304d-bcf5-7abadf79f3ba | -22.38069 | -49.03696 | 2025-09-20 00:28:00 | TERRA_M-M | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c5a9d76-b44f-3f23-9742-bd644aff14ac | -23.01546 | -46.91058 | 2025-09-20 00:28:00 | TERRA_M-M | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 473bd656-7afa-338c-a6a6-462a25e13d7b | -22.83447 | -47.58055 | 2025-09-20 00:28:00 | TERRA_M-M | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1370e89f-f731-30be-8468-01caaf7fb1db | -23.51131 | -47.20037 | 2025-09-20 00:28:00 | TERRA_M-M | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 75093499-f237-3cfd-898d-ab0643e3874e | -11.6731 | -44.8736 | 2025-09-20 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 98110233-4123-36e9-959b-e97fa55cb3d1 | -11.4857 | -43.5692 | 2025-09-20 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 89e902d0-3324-3203-af19-f283c22c0148 | -6.5631 | -51.1126 | 2025-09-20 00:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7d7bf197-e1db-35dd-8c32-8c734f1878d5 | -11.4665 | -43.5722 | 2025-09-20 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 8e2c9065-35f4-382b-91a5-80481913555d | -7.3847 | -47.0378 | 2025-09-20 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| fe2ef507-39ed-33b8-b496-e42678134811 | -16.3198 | -43.0684 | 2025-09-20 00:30:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0abfcd8d-911a-320f-97de-571f86ecd397 | -3.5161 | -49.4528 | 2025-09-20 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f354dca7-c1e9-305c-b4b4-ec8b72bbfede | -19.6073 | -57.7531 | 2025-09-20 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| 272d0c18-304c-395e-b1b8-f0050307e099 | -11.467 | -43.5485 | 2025-09-20 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 59849d7a-00fe-3b7f-bb2f-7d94732dfacf | -16.3204 | -43.0438 | 2025-09-20 00:30:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |


[Clique aqui para ver as próximas entradas](README2.md)
