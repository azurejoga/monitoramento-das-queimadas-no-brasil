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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3829d33d-9d9e-328c-a077-3a6f6c1f9b95 | -4.9102 | -43.4666 | 2025-10-15 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 320.6 |
| 3651f12f-1e90-3c6d-903c-2176e896500d | -4.8915 | -43.4678 | 2025-10-15 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 90acecc2-e65f-3515-bb6a-273dc8d4e346 | -4.8916 | -43.4446 | 2025-10-15 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 140.5 |
| cba08b03-6c65-30e0-9380-a67abffe8eff | -5.4276 | -44.2402 | 2025-10-15 03:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| be62917d-9f27-3a6c-b523-0dba31803f07 | -4.9104 | -43.4434 | 2025-10-15 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 97281d25-a9ee-3dae-886f-2071d3ee4a9a | -5.4278 | -44.2172 | 2025-10-15 03:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 159.0 |
| a04d0274-84c4-3c83-a47c-983a03b7f794 | -4.8915 | -43.4678 | 2025-10-15 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 99cf01c9-0bb3-32dd-a6cb-0e1c738ab722 | -13.4872 | -43.6867 | 2025-10-15 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6f56076f-30e9-31ea-9f10-67d20fcb18c1 | -5.4278 | -44.2172 | 2025-10-15 03:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| b00abaac-d013-3b73-84cb-8911e17f6c75 | -4.9102 | -43.4666 | 2025-10-15 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 265.6 |
| f0b6f794-fffc-3cb3-bace-2e29f1becece | -13.4678 | -43.6902 | 2025-10-15 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 71726f01-d9fa-3ee4-804b-4b05ad652002 | -12.2113 | -50.4096 | 2025-10-15 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 58eb65e0-153a-396f-92f6-622102b40dae | -13.4867 | -43.7106 | 2025-10-15 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d1f34aed-05b9-3098-ad16-2de7a32352d1 | -5.4463 | -44.2388 | 2025-10-15 03:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 11ca5257-aeea-316d-a740-e93c6b4b8510 | -4.6509 | -43.1337 | 2025-10-15 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 07064d5b-f2c9-3020-8576-dda484ad6e68 | -12.2311 | -50.3643 | 2025-10-15 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c6a44788-a039-3932-9330-53e25dfc91af | -5.4276 | -44.2402 | 2025-10-15 03:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 8a36d113-0f2b-333d-bec1-ee7ed5083025 | -12.2116 | -50.3881 | 2025-10-15 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 048f1a51-6e8e-3797-bdd5-c05749b0fe1d | -13.4673 | -43.7141 | 2025-10-15 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 688473b9-ade7-382b-a28a-f14d1e071ab3 | -7.9439 | -44.1381 | 2025-10-15 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 6bd15177-ed1c-39a7-bb9d-2bb3bd567365 | -12.2307 | -50.3858 | 2025-10-15 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 51da4780-52b3-3075-8211-0b84ec8000f2 | -12.2304 | -50.4073 | 2025-10-15 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6e2c0372-7504-3ce7-91f3-cd2214387189 | -5.4465 | -44.2159 | 2025-10-15 03:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 907731e2-7d3d-3286-8171-b7e7a1272141 | -4.9104 | -43.4434 | 2025-10-15 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 47c83f8b-8174-3fa6-8a1c-3d7bf5317705 | -4.6696 | -43.1326 | 2025-10-15 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 23c674c4-9f53-3834-916e-2aab4c103307 | -12.2498 | -50.3835 | 2025-10-15 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| de4ac10d-683c-3b27-907f-8ee342775c48 | -4.8916 | -43.4446 | 2025-10-15 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 05132ed0-c451-3475-83f8-a4c9fe442150 | -5.4465 | -44.2159 | 2025-10-15 03:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| dd536741-537b-3efe-9140-5a476e5db017 | -4.6509 | -43.1337 | 2025-10-15 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 4408739e-b6cf-3d87-917c-5f945f909cad | -13.4867 | -43.7106 | 2025-10-15 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 8b0adfda-6641-3fcd-96bc-34b732989f88 | -5.4463 | -44.2388 | 2025-10-15 03:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4bc40c62-4bdc-36d0-a3af-259e7f23bbde | -5.4278 | -44.2172 | 2025-10-15 03:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 4a2fabac-5994-347a-8f15-0594b8a88829 | -4.8915 | -43.4678 | 2025-10-15 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 01da36f4-cbfa-3208-9586-cc55094b954a | -4.9102 | -43.4666 | 2025-10-15 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 08425ec3-784c-3a00-b6f9-e8dcb0515d14 | -5.4276 | -44.2402 | 2025-10-15 03:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d37f88fd-1d79-378d-91fc-54386de11cff | -13.4678 | -43.6902 | 2025-10-15 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 99d20d53-cace-3c1f-a001-c80542cc2c82 | -4.9104 | -43.4434 | 2025-10-15 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 54380ea4-94d7-3d4c-baae-dc98f09591dc | -7.9439 | -44.1381 | 2025-10-15 03:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 88276d35-ceef-3325-a523-b251903ddd15 | -13.4673 | -43.7141 | 2025-10-15 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 9de54b1a-5365-3856-b2d7-09719507f402 | -13.4872 | -43.6867 | 2025-10-15 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 8c658852-f28e-309a-b2be-3e632e4d6a23 | -4.15078 | -43.13387 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1c7b44d-385c-37ab-b171-6c6b420e1384 | -3.73511 | -44.14444 | 2025-10-15 03:45:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26b2fc2f-f096-366b-8dd5-4a4b1dd8fc39 | -3.53525 | -44.02539 | 2025-10-15 03:45:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b69c0f7-0826-3b08-b367-756d01b7faf0 | -3.83594 | -44.54155 | 2025-10-15 03:45:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe90e18a-332e-33a7-9dca-7e34e7cda0ac | -2.24015 | -47.87752 | 2025-10-15 03:45:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d7e2fab-9697-3a0a-8f26-1db58a3e1a8a | -4.39101 | -43.46332 | 2025-10-15 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c02673a4-cd19-3cd6-894a-f650be48c12f | -3.05614 | -44.46852 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e63efbd-7cd6-33d1-9dde-7f476135637f | -4.15391 | -43.12872 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdf10207-c3a2-3289-b11d-a6c2f378352e | -3.05551 | -44.47237 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34d93b14-200b-39ac-a2d9-94ddea7df835 | -3.59803 | -41.62296 | 2025-10-15 03:45:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 08eb2e75-3743-3721-a146-42a311391ba7 | -4.41877 | -42.90073 | 2025-10-15 03:45:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6baf7925-7f6d-37d2-9a0b-b3f389b5735c | -2.92779 | -48.30932 | 2025-10-15 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| db64372a-936e-3130-8340-912882f257ff | -2.92183 | -48.30093 | 2025-10-15 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0582f7cd-5c36-3365-8937-d85cd0d391ed | -3.05487 | -44.47622 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46d6a4ea-3245-3cbe-bf19-28dd70d0f59b | -4.03083 | -38.35518 | 2025-10-15 03:45:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6cfc0902-7c5d-3032-873e-159d042ce12d | -4.29032 | -41.73892 | 2025-10-15 03:45:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2cb87be1-b408-33d8-a6b3-6df89183125c | -4.14623 | -41.65261 | 2025-10-15 03:45:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 738e61b6-ca8a-3f1a-9698-1c3d198544bf | -4.39153 | -43.46023 | 2025-10-15 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3314e270-c95b-3c62-9d48-552c9bb84a76 | -3.67202 | -45.22221 | 2025-10-15 03:45:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1077298-2994-30b6-aab8-9338597bc0ca | -3.57133 | -41.07961 | 2025-10-15 03:45:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3081396b-8bc3-3295-b644-3843e56caadc | -4.14473 | -44.18906 | 2025-10-15 03:45:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ea12c6-13c1-33b7-bb36-216ceb6fd4ec | -4.1332 | -41.64557 | 2025-10-15 03:45:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc931633-1b55-3a4c-99a2-84bdaafe923f | -4.75637 | -40.8679 | 2025-10-15 03:45:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92043e2d-1fcf-3d1c-9586-954a85cc6643 | -4.39672 | -43.46109 | 2025-10-15 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df0cdf91-0079-3779-98f0-63fd2debda50 | -4.03155 | -38.35075 | 2025-10-15 03:45:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ecec8297-9921-3e7a-9ec1-59b034442e03 | -2.52697 | -47.81562 | 2025-10-15 03:45:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31e73671-3c5c-3aef-8cf5-ad9b5ec4ac19 | -4.08196 | -39.82288 | 2025-10-15 03:45:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82b05bb2-6d90-3460-8d5f-de3ba1279fd8 | -3.56735 | -43.51005 | 2025-10-15 03:45:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf617872-16ef-30b3-b4fb-6730758cbf2c | -4.78635 | -37.72272 | 2025-10-15 03:45:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c94c3ef-3b66-3a20-8a03-d9870336c2c4 | -0.8992 | -47.55522 | 2025-10-15 03:45:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 16ea55bd-3457-36de-af66-5c851193ddcb | -4.1534 | -43.13169 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1076d5b-a4dd-3905-bb01-ba35c68508a3 | -3.05047 | -44.46754 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 786e096d-7499-3dda-966b-d00cfedea4f3 | -4.13628 | -42.21059 | 2025-10-15 03:45:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0fe45dd3-979d-3157-b32f-db07293f4c29 | -4.41658 | -40.17031 | 2025-10-15 03:45:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d865930-3ffa-33c7-9b80-ab66eddad093 | -3.72475 | -44.13882 | 2025-10-15 03:45:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b1b0d16-4542-390d-a416-36f6bab9f451 | -2.24723 | -47.87868 | 2025-10-15 03:45:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6cfec21a-2bad-3d6d-ba44-7d3128049dad | -0.90031 | -47.54849 | 2025-10-15 03:45:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 65736184-75a1-3822-8033-1e2ebefd6126 | -4.1409 | -41.65615 | 2025-10-15 03:45:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 286a4a37-db2b-3218-a5e1-a05d21c6bed3 | -3.05423 | -44.48007 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4e43a33-144c-3141-99ee-373125d928d1 | -3.83464 | -44.5491 | 2025-10-15 03:45:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 44145e31-bfde-301f-8c9f-90ac20cbde5f | -3.0823 | -47.73438 | 2025-10-15 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29cf0e10-de59-3510-a871-dfe9372a7b31 | -4.75832 | -40.86296 | 2025-10-15 03:45:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 846a0e05-e682-35ce-96fc-a47cb9d5235e | -4.3962 | -43.46418 | 2025-10-15 03:45:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2884f0b3-c862-3d1c-aae7-85ee216ac18d | -4.02782 | -38.35014 | 2025-10-15 03:45:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b5022d3-4f46-3a6f-88c8-24d94d161ecb | -2.92376 | -48.30419 | 2025-10-15 03:45:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 032742ff-b58f-34e0-9a7d-da1a398fcc43 | -4.15176 | -43.12794 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8bc252a-ae48-327c-b56c-1a301eb6e09c | -4.45315 | -38.44306 | 2025-10-15 03:45:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a2d1dd87-588f-3260-b235-9ff6495ea2bc | -4.14831 | -43.13077 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7eadba32-d5eb-3730-a1b0-071fbb4737f2 | -3.94693 | -40.92787 | 2025-10-15 03:45:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cd9f1c72-eded-3435-ac9a-9491f1e5415c | -3.73023 | -44.13986 | 2025-10-15 03:45:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dc3c262-2ac3-39df-b2cd-94ec3321a063 | -3.04983 | -44.47139 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01316da7-083c-32cf-907c-4c0f97ddd010 | -4.0271 | -38.35458 | 2025-10-15 03:45:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe7c0918-f8af-38c8-997a-cca84426e909 | -3.67791 | -45.22325 | 2025-10-15 03:45:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 808e3d94-8a5e-3b44-80f6-37ad94af055e | -4.15127 | -43.13093 | 2025-10-15 03:45:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99ce7014-3281-3a3b-a4b5-91f9ba231a51 | -4.9317 | -40.13841 | 2025-10-15 03:45:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d92feceb-f671-3ae4-af1e-e195175db1d3 | -4.14106 | -42.21144 | 2025-10-15 03:45:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d0635cae-5f09-3c40-b4e6-b43545ece083 | -3.08342 | -47.72798 | 2025-10-15 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f22b6dae-ff7d-3c98-b59b-355c3e28fabb | -3.05642 | -44.4765 | 2025-10-15 03:45:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82fb687e-c90b-323c-8bec-4216674358db | -3.47503 | -38.94386 | 2025-10-15 03:45:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 362549f1-6335-3605-b7a7-52787d0f694e | -3.67131 | -45.22641 | 2025-10-15 03:45:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
