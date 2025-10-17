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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9912b36a-5415-33fe-9307-809d20a4ba9c | -5.84608 | -43.88317 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8736ad5b-aaab-36b8-91b5-fee6e6801ec0 | -6.32183 | -40.94683 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 716d8088-a112-3732-98eb-bc494df64441 | -8.12302 | -45.55304 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e46a14bc-ec7b-342b-aa96-4d90cc96df82 | -8.39961 | -46.23867 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81243545-8c0f-36a1-a261-4fedd52d4042 | -7.40426 | -44.75464 | 2025-10-17 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ef2f219-8244-3690-bac4-b300be24266c | -9.15948 | -41.05281 | 2025-10-17 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| a07a5fbc-8f6a-3162-8534-d19284935e57 | -6.56625 | -42.96059 | 2025-10-17 03:28:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bd54462-28cc-3d83-8aa3-0e3b442fe077 | -5.09539 | -45.43754 | 2025-10-17 03:28:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 163aa99b-eb13-3768-9db8-15abe79fea62 | -6.56296 | -38.84632 | 2025-10-17 03:28:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65b7b9df-2e3f-3b5a-a8d3-696b537ad495 | -6.08288 | -42.38496 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c3c1d0b-fca0-34ec-9832-23f8c6a35973 | -8.25736 | -44.02892 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5afcf44d-28cf-3d6b-b328-fb2d08a6acfe | -6.76737 | -37.76761 | 2025-10-17 03:28:00 | NOAA-20 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 77257e35-20b0-3e80-b02d-5e5106e8de80 | -3.2398 | -42.07635 | 2025-10-17 03:28:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eafaae2-9726-35e5-9585-297b76bc1672 | -6.81848 | -41.69165 | 2025-10-17 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6fe90a68-042b-3a01-a529-26c284b9116d | -7.3271 | -44.16579 | 2025-10-17 03:28:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 927b1421-8d02-3ba9-a7d8-a9870b6a5687 | -6.75226 | -42.38331 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 529247d8-4e29-3c6d-96d0-c456c7d67772 | -9.15273 | -41.061 | 2025-10-17 03:28:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| c0777bd8-325c-360e-b876-d1730ea7643d | -8.23602 | -43.32961 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71656d2d-939c-37e4-be1e-3e078aacaf39 | -8.28375 | -43.38317 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2d0fbc1d-e0ff-3f7e-b5be-6000f8fad078 | -7.1137 | -44.74144 | 2025-10-17 03:28:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c27986b9-2845-399f-927c-6f00e5aa09a0 | -5.87995 | -43.91906 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd3b3976-006f-36be-9ed9-6648a6fbe591 | -7.74055 | -42.50633 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4e605680-d728-3586-ba18-323545824662 | -10.5132 | -43.4289 | 2025-10-17 03:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| bcb73265-8590-3e82-b349-5040583ff1ac | -2.7401 | -49.3927 | 2025-10-17 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c200b231-4011-31d3-be39-46c575f5e86e | -10.2748 | -44.0247 | 2025-10-17 03:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 70e73be2-3a93-3a30-9497-4dca8872c903 | -10.4941 | -43.4315 | 2025-10-17 03:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e57979a0-2314-38b1-ad6c-c84f211156d6 | -11.3976 | -44.2167 | 2025-10-17 03:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 627732d4-b353-37d4-b584-9c58b5c48f37 | -11.4172 | -44.1904 | 2025-10-17 03:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| a38c30b6-e23f-3ab6-a8d3-1191281e081f | -11.398 | -44.1933 | 2025-10-17 03:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 5a2dfc31-5917-3a79-9b31-022ad226e29c | -3.5028 | -52.4938 | 2025-10-17 03:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b5a67610-a538-3746-b995-5e529d90c724 | -9.1567 | -46.6241 | 2025-10-17 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| bb31ec49-5932-3f1d-9a74-becf277f6977 | -11.4581 | -44.0439 | 2025-10-17 03:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 36beca60-22a2-3ce3-bccc-943860de919d | -12.4455 | -51.3004 | 2025-10-17 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 561e31a7-7d85-3902-907d-f07d68a248d2 | -8.1996 | -43.3189 | 2025-10-17 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| fac53ce9-c3df-32da-a165-25337f6efe48 | -10.534 | -49.5471 | 2025-10-17 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 378a0e0d-e746-307c-9421-e079ef4c6b93 | -10.5136 | -43.4052 | 2025-10-17 03:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 260eda6a-bfa2-36f7-839a-47346085321c | -12.4451 | -51.3217 | 2025-10-17 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 07317f1f-3b63-3190-bcde-71d5622517c2 | -9.1378 | -46.6261 | 2025-10-17 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| bce468e7-a92e-3426-8781-d6100152ce74 | -9.1375 | -46.6485 | 2025-10-17 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 83bcb753-5ef3-3671-b944-0f1457c0858b | -4.4059 | -43.4049 | 2025-10-17 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| d78e91fb-5354-32f9-87f3-5b8202642202 | -10.2935 | -44.0455 | 2025-10-17 03:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| fd14b6ce-5138-3c44-abab-466c8106dc54 | -9.1564 | -46.6465 | 2025-10-17 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 4d3fb8db-706d-313d-a1db-a2e52d56880f | -11.4168 | -44.2139 | 2025-10-17 03:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| d4082cc2-1cc8-38f0-982d-edef5803f763 | -10.2745 | -44.0481 | 2025-10-17 03:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 325306e3-af96-3415-9220-9fdfb8b00e3c | -10.2939 | -44.0221 | 2025-10-17 03:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 849b7363-2459-30c2-9a9f-d5be0793efb7 | -10.9475 | -49.7605 | 2025-10-17 03:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 194229c0-64b1-34f3-a461-a19d7098b839 | -10.5337 | -49.5687 | 2025-10-17 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 281fdf82-b3c7-3b53-bd27-d1987edd14b1 | -13.71394 | -40.98537 | 2025-10-17 03:30:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dfb6fc97-614d-3758-a4c7-331f39b1d615 | -11.41082 | -44.21209 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8b454f1b-9326-3534-b6f4-6189a063a595 | -12.14113 | -43.26836 | 2025-10-17 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8634cf9e-4b8b-393d-8cf0-8a25083b4476 | -11.40395 | -44.21535 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 254b5d78-f0f3-3246-8818-1a7ac85fb55c | -10.13022 | -44.54963 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d26d7e8-5cb8-3aeb-877b-1575783ee231 | -9.24051 | -44.3681 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de16dc7c-a0dd-3662-b3a3-d47e136aead2 | -10.15482 | -44.54114 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 626c0564-489f-3d1d-a319-9a73dc69010d | -10.64793 | -45.29803 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b5db260-642a-342e-beb5-e5e5b8df125d | -10.11402 | -44.61469 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbf886d7-e9cf-37da-9377-558e7c33cf3b | -11.47431 | -44.28596 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acbdcce4-cfd4-3ec4-9ae1-eee21916c3c1 | -9.14959 | -46.63184 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efdaf51b-eb6a-3d5f-8552-87af8667bff9 | -13.39019 | -47.217 | 2025-10-17 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8511c4e6-a8c8-3329-8e32-246ba05bf0ae | -10.27736 | -44.05041 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2514e4ad-b155-3858-b790-0a6d03b7963c | -11.45806 | -44.0472 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 134a8f19-52e9-32c9-9097-d1e00e7e0730 | -10.05389 | -43.86757 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2fdca45-9724-36c9-a0d9-e6b8bb5e4175 | -10.29245 | -44.03752 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 9dff0f63-eba6-384e-8c9e-40f3e3bccf59 | -11.44315 | -44.18441 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8863cf2-81a8-3be4-b01d-bde2375bcf26 | -10.13749 | -44.54565 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d122c4e-fa4b-39d1-8d79-6c11d1caee29 | -11.3587 | -45.27273 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92b04a79-ed17-3d7c-bf95-ad5fad664765 | -11.47667 | -45.09094 | 2025-10-17 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad8f18ba-1a73-387b-8d1b-25f3d64aa521 | -11.39905 | -44.21778 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4f430cfd-af81-30e9-85de-0e00c6ea1ed3 | -11.40596 | -44.21449 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e81122c7-898d-3f45-a328-3d18ad81bc52 | -9.13086 | -46.65081 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 81daf3be-b5ae-34f6-9185-e3fcc0e18bca | -10.10632 | -44.57219 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 553d09ce-6dc6-3f08-b9d1-17d52fdd2e34 | -11.47155 | -44.26175 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c32144be-a19c-3829-bb08-716d2db5d53d | -10.15572 | -44.53658 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 78f244d8-e522-3997-a28f-75e0307f7dfd | -11.39305 | -44.21652 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 367d2bc8-9b71-39af-9e53-886569d30907 | -11.40137 | -44.2373 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9f256d3a-9809-3129-9e50-dc256364feba | -11.41171 | -44.20751 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 98835afe-489a-3f64-9591-87e78aeda092 | -9.28263 | -45.38697 | 2025-10-17 03:30:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bcdbd8ae-5529-342c-bf16-b89b80913817 | -13.07033 | -46.93921 | 2025-10-17 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c6cc313a-987e-3cdc-8886-d1fc67ef04e6 | -10.05433 | -43.83382 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e59fd5b6-47bd-3a98-88a5-40e3ec6c9826 | -10.27143 | -44.04853 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e7601bd-fce0-30d1-87d9-d89dd724fa2c | -10.13531 | -44.59072 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c474f33-6679-3bac-ae8d-6afb272bfb09 | -10.26831 | -44.03239 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6b4185f-06b8-37fe-ba1c-666932ffca0c | -10.71372 | -44.536 | 2025-10-17 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 653f612d-a1af-3a42-82f7-8fd6bf54884a | -10.14246 | -44.5379 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e48d50e9-05c6-3130-b643-190b87722644 | -11.44823 | -44.19021 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff30e7c8-869e-3505-adce-5c4e49d88533 | -10.65543 | -45.29765 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 976945f6-09b4-3d09-a009-21112b94b44f | -11.4092 | -44.22942 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6063eec6-584f-3b4b-a4b3-03b3122fbcf5 | -10.11569 | -44.55745 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fec74a6f-b30d-3b47-bdd3-e69ae85d3869 | -11.35344 | -45.26574 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a50261fb-1a13-30be-bed6-9389c90d45f0 | -9.15381 | -46.61073 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7dec9af-5347-384a-8d99-32f02641af32 | -10.27524 | -44.02911 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9b03747-58a6-3a8e-a101-3455174f3087 | -9.24147 | -44.36316 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34f29c36-f3ad-366d-b0c9-452d159d9dc0 | -11.46704 | -44.28475 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78a2e56d-517d-3929-89b5-db55d606e760 | -11.47724 | -44.20102 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 17985cca-fbe5-3445-abbf-8e34927c567b | -10.50358 | -43.44415 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41a8d11f-7bc2-370c-86dd-16bf72f32432 | -11.37669 | -44.19521 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3918fa8f-3306-346c-ac68-8dfabfad8f30 | -12.61826 | -43.44433 | 2025-10-17 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cca8192-4d67-3598-8f38-98b0e655ac40 | -11.46399 | -44.04845 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 20c9b01f-2631-379b-846b-7ddca781de9b | -11.47017 | -44.27548 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd7d6179-4998-3d86-8d43-ccc9628acaf8 | -12.62058 | -43.44465 | 2025-10-17 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
