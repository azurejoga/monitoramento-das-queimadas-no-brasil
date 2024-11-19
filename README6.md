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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea700c2-8576-376a-9243-515dee6049ec | -3.5125 | -50.2343 | 2024-11-19 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9de3cb32-6631-3dc5-8cdb-3764f801ee75 | -8.6876 | -47.976 | 2024-11-19 00:40:00 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| bd019f96-4a9c-341d-873f-04d03d9bf320 | -2.7843 | -52.6158 | 2024-11-19 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 79931d8a-a5e1-3008-8dbe-79b605ce323f | -6.0657 | -44.0547 | 2024-11-19 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| ff11a10b-ec0c-3dd0-ab76-8e29741e6e7a | -2.7659 | -52.6163 | 2024-11-19 00:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 5dac4341-8be7-3900-ad2a-2852bbc04215 | -5.9975 | -45.3607 | 2024-11-19 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| aec66da4-92f8-31a2-9280-fb5e9bfd9975 | -2.5012 | -49.0162 | 2024-11-19 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f7a13a14-5dc3-3c1b-a989-ff255599ddd7 | -3.5126 | -50.2133 | 2024-11-19 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| f833dd4e-bcee-32cd-80ff-f544cd97d821 | -9.2543 | -45.0074 | 2024-11-19 00:40:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 3e7b1c4c-09ae-3641-a893-00089f42caef | -5.979 | -45.3395 | 2024-11-19 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6d00b596-f757-3161-b47a-38653832269e | -8.2659 | -44.0348 | 2024-11-19 00:40:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f2dec751-62c6-38c9-a3df-60afda2ba711 | -0.1196 | -51.4393 | 2024-11-19 00:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 41.3 |
| a42b2bc2-fa50-3c86-8f2f-6da5e3102520 | -22.3365 | -52.0415 | 2024-11-19 00:40:00 | GOES-16 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.0 |
| a81d7f73-9126-36af-9cd9-de9fb78a3caa | -9.2546 | -44.9845 | 2024-11-19 00:40:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 159735d1-e469-3bc4-a2ed-69d117481273 | -8.2662 | -44.0115 | 2024-11-19 00:40:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 6fa3781b-6ad9-367b-aef7-eff6b3e0b24c | -18.62807 | -41.66193 | 2024-11-19 00:41:00 | TERRA_M-M | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 7b202946-fb3a-30bb-8f3b-41bfae4c947e | -12.55318 | -43.74192 | 2024-11-19 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8740496-d1b1-3cbe-814c-c6da0b4beef2 | -12.27301 | -43.52109 | 2024-11-19 00:41:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 3b39367c-2bb7-39fe-ab7a-27358370923d | -12.27437 | -43.53047 | 2024-11-19 00:41:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 29c7a208-c119-36bb-8368-7bec1c0e4ee6 | -13.2501 | -43.65311 | 2024-11-19 00:41:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 475d8983-454f-3066-8c0b-f2b54aada373 | -12.45611 | -43.57644 | 2024-11-19 00:41:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e92358a-932a-33f0-b54b-e13e85e041f4 | -12.28339 | -43.52908 | 2024-11-19 00:41:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3a31722-7ba3-33be-810f-2f7a76621315 | -14.506 | -42.71022 | 2024-11-19 00:41:00 | TERRA_M-M | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9c89a5f7-1f37-31ca-8a95-292b700185b7 | -15.21282 | -42.88306 | 2024-11-19 00:41:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0afef937-39af-3589-97f5-7e6df72a8659 | -13.45044 | -44.02256 | 2024-11-19 00:41:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf714ece-ddd9-3050-8843-39bd24dcaa7a | -5.97491 | -45.3615 | 2024-11-19 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 5d990a9c-5350-3fee-be4b-cdc635904513 | -8.43499 | -45.6304 | 2024-11-19 00:43:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3dafd9e3-130c-301f-9e61-ae33be94e4d8 | -10.84956 | -44.26394 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| abd4d418-d032-375e-a280-056c8fa1d1c9 | -5.71096 | -43.83121 | 2024-11-19 00:43:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a16ecdf7-0352-3499-a048-4e595eec7994 | -6.29377 | -46.12834 | 2024-11-19 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 091f32ce-8310-3dce-a411-4c4506f5d66c | -10.90195 | -44.57084 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ad274be-cd83-3a6d-8fe4-1018f6ac6804 | -6.25362 | -43.55794 | 2024-11-19 00:43:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 42cdc30d-9f34-34f4-bec1-86a33d26fbdc | -5.7219 | -44.81502 | 2024-11-19 00:43:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3c4285ac-6853-31dc-9156-5b63cf1cc914 | -10.97606 | -44.4433 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b5db411a-540f-3984-91a7-e4fde14c02b0 | -8.00165 | -44.38723 | 2024-11-19 00:43:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 4a03b0e4-006d-3da1-8d46-ef5bde9d1522 | -11.14032 | -45.34859 | 2024-11-19 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6231fae0-1af5-34b7-bd63-2d4263894242 | -5.72057 | -44.80578 | 2024-11-19 00:43:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 20e33f26-8788-377d-9e3c-d7f5a65cdd98 | -9.89696 | -44.42917 | 2024-11-19 00:43:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 184cd025-39ac-380b-96b4-8038735684d4 | -6.20104 | -46.31944 | 2024-11-19 00:43:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8411170d-e376-3eac-a897-72a9500012df | -6.70421 | -43.9552 | 2024-11-19 00:43:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6f0c31d3-c6d4-334e-b4dc-2e31e03960be | -6.00843 | -46.40108 | 2024-11-19 00:43:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b1aaaad-55a6-3e54-8e40-4f3ad3e486fe | -6.31337 | -45.22118 | 2024-11-19 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b6867a2d-dea9-3ea2-997b-c031c91b7b88 | -8.26342 | -44.02274 | 2024-11-19 00:43:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| bc5d6d74-d29c-365d-820b-146ad1edc0eb | -10.76027 | -44.34869 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7318b507-5d22-392a-867c-3abaabc0bebe | -10.97102 | -44.53633 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7581ea47-c121-373b-b60b-b00b975c7fb3 | -9.98379 | -44.72118 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 3239eef3-f5f2-3f91-8296-cb5c1d473999 | -9.26964 | -45.01212 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9007a71e-be09-3ca8-850d-387a270c0db4 | -8.26477 | -44.03226 | 2024-11-19 00:43:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 3f6fc333-bf6b-3e7b-92ed-07ffe796e4e6 | -5.85764 | -39.6643 | 2024-11-19 00:43:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| e77ece0f-56bd-3f73-9901-3dbcd3e392fd | -5.98382 | -45.36024 | 2024-11-19 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 64f58762-d441-3119-a286-5be2dd25cb6d | -13.16969 | -53.2949 | 2024-11-19 00:43:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 31c98d47-a5a1-37ff-99e0-c21a12b2deb4 | -9.26078 | -45.01341 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 55a3d46f-0cc9-3894-96fa-fa1acb12c005 | -6.3935 | -44.74156 | 2024-11-19 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 96cfbe11-225b-3086-98ae-3201176ddf36 | -11.89185 | -43.81863 | 2024-11-19 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 96565bc3-ec23-357f-a5fc-25d6a7f8adc6 | -10.9799 | -44.535 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5db41e73-db6b-312b-9b69-bffde0ae4e3d | -5.97872 | -45.38841 | 2024-11-19 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ee16e39e-5079-350d-9e4c-13f57c2b61a7 | -6.93066 | -45.08921 | 2024-11-19 00:43:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6597804-f5f3-3bd9-aac5-c022a77e1738 | -6.48303 | -47.50484 | 2024-11-19 00:43:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 41dd63c0-2071-3a26-947c-ede926a1ca51 | -9.82948 | -48.17256 | 2024-11-19 00:43:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e42d5ee4-c13c-3d9c-8ca6-d0dbbfcb04fc | -11.14918 | -45.34731 | 2024-11-19 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3d5a0205-a326-34fa-9515-0cccb5f84329 | -6.2876 | -47.3537 | 2024-11-19 00:43:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e693ada7-acff-3095-9cb9-07e9cd66673d | -9.25065 | -45.00576 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 36.6 |
| ee819684-560f-3b61-8482-66f0f583a387 | -8.68239 | -47.98779 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 4caafd68-b83e-388d-a653-98a7c7b36259 | -6.22956 | -46.13473 | 2024-11-19 00:43:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41d2855b-1943-3d2e-aeec-e2ca3ee9372b | -11.88156 | -43.81073 | 2024-11-19 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3abe7164-96b8-3a56-94c3-2b19a6f2ad6a | -9.79606 | -44.63209 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4cd7cf05-3850-35d1-ba14-ee5af1131a24 | -10.70835 | -48.811 | 2024-11-19 00:43:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 71a35483-1b65-38f6-9d46-3e74f2124348 | -8.27191 | -44.02536 | 2024-11-19 00:43:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 4d7a8f87-6af8-3225-bc96-2c7463e46350 | -10.76155 | -44.35778 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a54f442-2fc8-3741-ac87-4db6bc491d0a | -10.8192 | -44.37069 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| cccd94a1-abd6-3d33-ac13-2bfc8e93430a | -8.27053 | -44.01585 | 2024-11-19 00:43:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b241db73-3da3-3153-859c-07dd61a9297d | -5.94951 | -39.6644 | 2024-11-19 00:43:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 48.5 |
| 94da6392-4136-31cc-8dfa-9e62e48cc575 | -6.39481 | -44.75084 | 2024-11-19 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b2d4b81e-45a8-3aff-8ff8-6a2dfa8d43af | -10.8541 | -44.88704 | 2024-11-19 00:43:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 88239062-6c71-38c6-abd1-268dbd588604 | -9.85739 | -48.14025 | 2024-11-19 00:43:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df559b11-87b0-3472-a0cf-001a9af3f2b8 | -7.56265 | -46.4504 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 31ddde82-4c6b-3ced-8783-429984e35d88 | -7.88691 | -44.22832 | 2024-11-19 00:43:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ac95ce3c-d682-39f2-9173-92947ddee0f2 | -5.95148 | -39.67841 | 2024-11-19 00:43:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 211aba2a-905f-32c3-8eb0-2032322af23c | -10.8281 | -44.36936 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aadaee6b-89d8-300b-8c9c-11d138ffbd09 | -6.40254 | -44.74033 | 2024-11-19 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7e06cc2f-5656-3902-b2a6-ccb9a1009010 | -10.84525 | -44.88834 | 2024-11-19 00:43:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aec2f82c-4957-39dc-bd4c-23b0d4092a5c | -11.15043 | -45.35632 | 2024-11-19 00:43:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff5a48c5-9065-3479-9867-c0ec42af148c | -6.87693 | -44.77215 | 2024-11-19 00:43:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c025da6-c4a7-3e3f-aac6-32c58b338846 | -7.57405 | -46.46712 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a7cc2365-d93a-32c2-91c5-43cbca216bc2 | -5.97618 | -45.37048 | 2024-11-19 00:43:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c5791e52-83af-3ef7-a3d2-4fca0a16e55d | -6.412 | -46.1869 | 2024-11-19 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d14237fa-4c17-3d38-b48d-8388d74e91d4 | -6.93561 | -42.81501 | 2024-11-19 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5334bf19-9a9b-30d5-bdd9-1d78291e6317 | -7.88556 | -44.21885 | 2024-11-19 00:43:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6c1e6941-06f3-373d-bde1-3ff04fbddc6d | -7.43532 | -44.68203 | 2024-11-19 00:43:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fbc294ab-60bc-34c5-8427-779cd4eaa3ff | -10.4015 | -44.48184 | 2024-11-19 00:43:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4a555637-25d0-30e2-b72c-e7671254d1b1 | -11.88288 | -43.81998 | 2024-11-19 00:43:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0bf019cc-2b78-367b-8a21-50d85e27c247 | -6.48176 | -47.49545 | 2024-11-19 00:43:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6cc0413e-587b-328b-b1b9-6dcdd8619205 | -8.27825 | -44.00471 | 2024-11-19 00:43:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 92758243-c551-37dc-b857-4f35cd56df29 | -7.89466 | -44.2175 | 2024-11-19 00:43:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b0b33e63-e56a-3ba1-a152-b16f8e935951 | -10.78443 | -44.32652 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 955cefbc-1238-32ef-a39f-4f1243c563c0 | -10.84076 | -44.33033 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad496bf4-ad1c-3d1d-bb82-fd732db40a90 | -7.39006 | -42.77327 | 2024-11-19 00:43:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2aae8c7a-5917-3955-b080-b4a60d5b5108 | -10.81791 | -44.3616 | 2024-11-19 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 78f56712-f41d-3514-a0ca-a96350736898 | -9.26838 | -45.00317 | 2024-11-19 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ce1bc8e5-257b-3067-a576-01ec0b30a1e8 | -7.56389 | -46.45939 | 2024-11-19 00:43:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README7.md)
