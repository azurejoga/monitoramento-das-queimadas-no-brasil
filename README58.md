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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2105b20-d89d-3139-90d9-95c3926a133f | -3.7652 | -47.7468 | 2025-11-17 14:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| b1cd4f68-97ed-30f4-92dd-d5d1ba90eb6b | -9.0022 | -45.4693 | 2025-11-17 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.9 |
| f4982a2c-ad61-3ec0-a9f8-7e0d5d05f03a | -10.3939 | -44.9129 | 2025-11-17 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 3919cf58-77c0-3ade-ae6c-1dc46b11c4c5 | -3.9554 | -43.7773 | 2025-11-17 14:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 415f83a0-2985-3390-b52a-4e957b79f451 | -4.4059 | -43.4049 | 2025-11-17 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 27784f12-1ce9-389b-ba44-cb835e3257a0 | -3.7292 | -44.1797 | 2025-11-17 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 637972db-8a81-31e2-a956-953e0f37460a | -10.8516 | -44.8748 | 2025-11-17 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 09f7ffca-5281-3d46-9555-d89d86acab5f | -4.843 | -47.5646 | 2025-11-17 14:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 59c7b89f-1834-3357-a5c6-0278258a1a89 | -9.0214 | -45.4445 | 2025-11-17 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 11645370-0c61-3f79-919c-eef548d1dd40 | -4.4246 | -43.4038 | 2025-11-17 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c318c439-059a-363b-87db-628ced94ec92 | -3.7838 | -47.746 | 2025-11-17 14:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 789f62a6-585c-316d-a6c6-7dd4b7f9ecea | -10.3041 | -44.5785 | 2025-11-17 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 04cf8eaa-b786-3e0c-81fe-3cb34c06f3c3 | 3.9353 | -59.6446 | 2025-11-17 14:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 21a009cc-4b63-3244-8381-71dd52a837c6 | -10.8512 | -44.8979 | 2025-11-17 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b3533b71-f650-3c81-a5dc-86c821987c7f | -10.7889 | -47.6392 | 2025-11-17 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 735c9d29-434c-3168-a364-803d79c45a19 | -3.3601 | -43.5053 | 2025-11-17 14:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| c36f6a2c-ff76-3f89-a153-5b9d42c5bbe5 | -9.2088 | -45.5599 | 2025-11-17 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 4ae57237-a8a1-3dba-ae0d-5a7d434a141f | -10.092 | -44.7676 | 2025-11-17 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 77b38146-0426-37d0-b709-1741bc42cc30 | -3.3552 | -44.4255 | 2025-11-17 14:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d215bbf3-552d-3ea3-a79e-ce6027d5a328 | -4.8432 | -47.5428 | 2025-11-17 14:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 1977b879-4df9-3d86-8170-0f1ae3a391f4 | -12.4347 | -43.1793 | 2025-11-17 14:30:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 7f5c020e-12c9-371b-9d08-e9eced93c6f3 | -3.2117 | -43.3494 | 2025-11-17 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1724200f-9143-3d30-b33f-5a9f4fac1c03 | -9.6232 | -44.3876 | 2025-11-17 14:30:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 65025391-2527-3cd5-bbc8-49eadeb67a71 | -10.0917 | -44.7907 | 2025-11-17 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| bb68603c-c412-3f70-9c61-c0ff9f6b7771 | -3.4036 | -42.3567 | 2025-11-17 14:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 4cc53790-6394-3949-a9a0-88a99aeeebe9 | -2.4201 | -45.7238 | 2025-11-17 14:30:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| d22c17bc-f67a-3a54-8353-bbf0c9a2f075 | -6.3705 | -41.7477 | 2025-11-17 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| cb60a12f-dbeb-3676-a798-ebb72a19dc09 | -3.2251 | -44.3853 | 2025-11-17 14:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2322c321-d065-33fb-9a6b-886f77ab2554 | -10.8707 | -44.8722 | 2025-11-17 14:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b4854fda-84e4-32f5-8d25-28af9dd67fdb | -3.0895 | -41.6819 | 2025-11-17 14:30:00 | GOES-19 | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 666f8ae0-3498-36ea-b665-3c3b2a2252ba | -4.3621 | -44.353 | 2025-11-17 14:30:00 | GOES-19 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e750d385-cc41-309c-aaaf-d59d65572b80 | -8.5418 | -46.0607 | 2025-11-17 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e0b70c4f-1f31-3f1a-b50c-2014beab08e5 | -10.3936 | -44.936 | 2025-11-17 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1307604b-2aeb-3c9e-b817-b5eb27fbf95f | -12.7189 | -45.4074 | 2025-11-17 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 832d0c51-69c3-3fd3-aff5-5cb2db944b6b | -3.3601 | -43.5053 | 2025-11-17 14:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5635b563-1381-30a8-9581-0168a97a7954 | -8.9836 | -45.4486 | 2025-11-17 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| f2542505-afb3-366d-b8fb-4e62416dab18 | -11.4136 | -43.32 | 2025-11-17 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| cbfb00cb-d3d3-33fd-a049-2566afe81160 | -4.843 | -47.5646 | 2025-11-17 14:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 118.4 |
| bd0406d0-3de3-3b8a-a2c3-4159da52764b | -3.906 | -45.8013 | 2025-11-17 14:40:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b71b1df4-d524-3e82-a0da-e6654b827a29 | -4.1203 | -47.2951 | 2025-11-17 14:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 94d79aa4-7894-36b6-aa84-9ba5608570bc | -2.4201 | -45.7015 | 2025-11-17 14:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b5565304-91ee-32a4-8c2b-51045a7c78fd | -9.4645 | -44.868 | 2025-11-17 14:40:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 85fd3f9c-9d5e-3315-91ea-ec56aeadd080 | -9.9775 | -44.8052 | 2025-11-17 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 481b2825-726f-363f-9598-89990ec3aec1 | -8.5607 | -46.0588 | 2025-11-17 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 5fe52f31-ce96-3fe8-a7e2-43bfc76d3d77 | -4.7292 | -45.196 | 2025-11-17 14:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 968d0ce9-71f8-3b4d-8741-ae483c4c199b | -2.4201 | -45.7238 | 2025-11-17 14:40:00 | GOES-19 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 6e5df5d6-6970-3a6e-9063-e5e13f8d614c | -1.3008 | -49.0613 | 2025-11-17 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f8b7c6fc-9552-38d4-9ef5-1564cafb44ea | -4.54 | -48.4689 | 2025-11-17 14:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ebcbc0de-94ee-3bd7-97d0-031d5d61b9c1 | -10.3936 | -44.936 | 2025-11-17 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 98eb102a-3bd8-3645-8586-7be2d5c9a21e | -11.152 | -44.0423 | 2025-11-17 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7af9ddd8-94cc-3615-aa2d-9753a48c297f | -11.6947 | -44.7314 | 2025-11-17 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 375.6 |
| 1563a305-fbc0-3928-b808-299d0577253a | -11.7996 | -45.2935 | 2025-11-17 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 9fb8758f-2696-3afe-b327-4833aedf6870 | -8.5415 | -46.0832 | 2025-11-17 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3501fb00-1b2d-330f-a0cb-6f25661dccee | -4.4059 | -43.4049 | 2025-11-17 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 7d719fc1-8389-3d35-a6a5-69d506a467b7 | -8.3049 | -43.9377 | 2025-11-17 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 1a9a2fab-3468-3cc5-9017-2a0a8e4cb9bb | -3.3842 | -46.0472 | 2025-11-17 14:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 63f965af-51e5-37ea-9b7c-721bb7ab4847 | -11.8001 | -45.2704 | 2025-11-17 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 102a3dd8-e54f-30f8-816d-0189cbda6bd9 | -3.6515 | -44.7312 | 2025-11-17 14:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 16105e5d-79ca-3560-8462-831dabde709a | -11.3944 | -43.323 | 2025-11-17 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f08237a9-1f51-32d4-89da-1552c291a44d | -8.2827 | -44.1951 | 2025-11-17 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 26252324-29f6-3676-9cc1-a4a0ec709162 | -0.3401 | -51.7688 | 2025-11-17 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 14b74f0e-3a5b-330a-8cb9-dc04dc8a4bb9 | -3.3415 | -43.4829 | 2025-11-17 14:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| c63ba52d-e00b-3f82-9d1e-85f6e0f5509a | -3.3602 | -43.4821 | 2025-11-17 14:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 55d1821f-50ee-31ec-ae95-de5d80909331 | -4.5586 | -48.468 | 2025-11-17 14:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 104115f7-2c7c-3388-a186-5b01310d5fe2 | -8.5609 | -46.0363 | 2025-11-17 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| bc5e0589-2445-3c53-9ddb-b33bb2f71a5d | -11.676 | -44.711 | 2025-11-17 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 291.5 |
| eed2508f-49e0-346c-8e9e-d66277cbe16a | -2.5238 | -47.8115 | 2025-11-17 14:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 69ea0dbc-2462-32fe-8338-639c4a759f62 | -3.4468 | -44.7176 | 2025-11-17 14:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 086b5acf-5904-33e9-b9b4-b376a62ce52d | -4.2295 | -44.657 | 2025-11-17 14:40:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e44de820-36fe-3cbb-8eb7-f9597f7cadd2 | -3.5833 | -43.6108 | 2025-11-17 14:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| e3bac2b5-c326-35e0-bc9d-8516a58f68ea | -10.1111 | -44.7652 | 2025-11-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 977c1b5f-98c9-3f29-becd-9c2cb058cac4 | -4.4246 | -43.4038 | 2025-11-17 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 3100298a-c09d-392a-be7a-178c4c020f8b | -9.0022 | -45.4693 | 2025-11-17 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 50734587-2fb3-30a1-8bc8-fb4e505c7548 | -8.5418 | -46.0607 | 2025-11-17 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 55345e0a-79a4-3468-8a0c-1894dc9fb11b | -0.3585 | -51.7687 | 2025-11-17 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 2c491517-58bc-3684-81c5-75bbd0f46f86 | -9.3272 | -46.5833 | 2025-11-17 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 303e5f7d-9c85-3c46-a311-f8a4e9390341 | -4.2673 | -44.5866 | 2025-11-17 14:40:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| fa70ef53-3a7e-35e8-a9d0-244ac3974776 | -5.3252 | -43.065 | 2025-11-17 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6d397371-394b-32d9-a11b-840966580b8b | -9.9754 | -44.9435 | 2025-11-17 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| dad6e5c9-bc19-3709-a77e-499d18b9082c | -2.989 | -43.1259 | 2025-11-17 14:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 750613ab-6a3e-3afd-8991-4625008a36cb | -1.4116 | -49.0384 | 2025-11-17 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 562900eb-a7af-32b0-afeb-4713bd01fb29 | -13.0584 | -44.7962 | 2025-11-17 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| c7533f14-683d-3372-b48e-1c37f2f2ce05 | -2.5053 | -47.812 | 2025-11-17 14:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b6452680-e368-3c1a-83ec-729e7f8bce9b | -3.7293 | -44.1568 | 2025-11-17 14:40:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8ac93fe4-2071-3c14-8090-5d04f67dd251 | -3.2117 | -43.3494 | 2025-11-17 14:40:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ca17a433-4554-3321-9000-dd5a56150cb1 | -3.9959 | -43.2651 | 2025-11-17 14:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e537a970-8f89-3389-b846-ac6162893aac | -3.7652 | -47.7468 | 2025-11-17 14:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 233.7 |
| 21136e56-039d-3aac-87ba-2ee9e6387c11 | -10.1909 | -44.5239 | 2025-11-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 33c443d4-d019-3d8d-8d6c-da5db602f3cf | -11.9784 | -44.9439 | 2025-11-17 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| d5de69e9-f228-3766-9e4d-a90113149fa0 | -0.3401 | -51.7893 | 2025-11-17 14:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b4a8b322-8daa-363c-bb57-e9686143585a | -9.6236 | -44.3644 | 2025-11-17 14:40:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8bea33c9-5b9f-3e51-aae6-f65e5baf5661 | -9.2088 | -45.5599 | 2025-11-17 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f790d874-705e-3a9a-93a9-b049218f7de8 | -0.8399 | -48.6822 | 2025-11-17 14:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 9115f2c7-7de0-3c9b-a11e-84b9decc04e2 | -5.3444 | -43.0167 | 2025-11-17 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 90.5 |
| 817e3846-f494-34c5-9a92-4150516972f3 | -7.491 | -45.8693 | 2025-11-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 16bf0137-3864-3507-acbb-8c5fae567a3c | -10.0917 | -44.7907 | 2025-11-17 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| c5a6f247-a225-305b-af52-ed5afb38de20 | -9.0825 | -51.1566 | 2025-11-17 14:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8cbd515e-3ff2-3f41-a74a-999d643db149 | -8.5604 | -46.0813 | 2025-11-17 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 687980b5-e6b4-39af-a146-dd6c37c6c3cc | -11.7992 | -45.3166 | 2025-11-17 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 6f859a6f-1f5f-3932-9f40-1fd75e34d29d | 3.9353 | -59.6446 | 2025-11-17 14:40:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README59.md)
