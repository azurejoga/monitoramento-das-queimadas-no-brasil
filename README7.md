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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96bd2f29-5031-3003-9b95-089f3008e7e6 | -17.1083 | -56.84632 | 2026-09-05 01:22:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| d0cd4ac8-1414-3e22-8341-970d1cdf1d21 | -17.09969 | -56.80311 | 2026-09-05 01:22:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.8 |
| 1dbe31b7-84db-3ab5-8955-c580207aba1e | -17.09979 | -56.8079 | 2026-09-05 01:22:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 389a3216-fe12-3eae-a1f5-7acde4939b75 | -17.10813 | -56.85118 | 2026-09-05 01:22:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| d97a0c98-6348-36f5-a164-2535c2b54d74 | -8.96886 | -69.28199 | 2026-09-05 01:24:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2af47c8c-d726-3e0a-8730-49bc783c03ee | -9.22143 | -65.86307 | 2026-09-05 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7e5f5bd0-0e90-3555-99f6-408e3d390aba | -9.02771 | -70.71826 | 2026-09-05 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15fe5758-334d-3147-8ef4-a06218f5bcf7 | -10.16727 | -69.34737 | 2026-09-05 01:24:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| de857224-c56d-3281-9bcf-87062249cff4 | -9.18368 | -66.03073 | 2026-09-05 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4a1a8110-c206-31f6-b9b9-35fdce0cfe9f | -9.18188 | -66.01877 | 2026-09-05 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b02e9221-6df5-31fc-a334-560909eb77b7 | -8.96764 | -69.27312 | 2026-09-05 01:24:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b959cd84-84ca-31d9-98f8-ca32864428ef | -9.02648 | -70.7091 | 2026-09-05 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9aad66b3-2880-30e7-b6cf-32f60ce2dae2 | -9.75323 | -66.62423 | 2026-09-05 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 162ab350-9c1f-3d74-b80d-ed8b389b9dba | -8.77117 | -69.57531 | 2026-09-05 01:24:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a7d964ba-2a70-38ea-8832-1531000e9b41 | -8.75101 | -69.2349 | 2026-09-05 01:24:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 877b65c5-3e08-31b9-9868-223574b7e4c9 | -8.86911 | -68.49851 | 2026-09-05 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a63c733-b1bf-397b-a0bd-4223beea3bd1 | -9.65049 | -69.0079 | 2026-09-05 01:24:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 38b69da7-dbe8-33b7-a930-c0592e2c81b2 | -9.46406 | -67.43397 | 2026-09-05 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 68b57456-8c3c-3fb3-a165-3dd0ed330f04 | -9.46261 | -67.42404 | 2026-09-05 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b94babf9-ed38-3dde-a615-8481649ed5bb | -8.86783 | -68.48933 | 2026-09-05 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 59dfbf97-d4c2-3112-9972-caec349b6d2f | -8.74977 | -69.22601 | 2026-09-05 01:24:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bb29b5fd-8bc2-3a60-ae21-055cd77d58ed | -8.88568 | -70.54897 | 2026-09-05 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4830dfa0-0118-3dc9-956d-e6f985bd05d3 | -9.13257 | -67.8131 | 2026-09-05 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 5ebbcc6e-4e6b-3d9e-8d42-ad04cc2debb1 | -9.53255 | -68.62841 | 2026-09-05 01:24:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 28894e66-7cf0-3a82-ab9f-0c7619e94139 | -10.01573 | -67.66961 | 2026-09-05 01:24:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b70aa832-274e-3b2f-90fc-daaceab6f312 | -8.82657 | -70.79587 | 2026-09-05 01:24:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c1b40fc-8f3d-307e-a68e-71f53b1483ef | -9.13121 | -67.80345 | 2026-09-05 01:24:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 5d70aebf-1f3e-3757-b8ad-10f07b027a52 | -9.5338 | -68.63744 | 2026-09-05 01:24:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fdf8f10f-b673-3874-8af7-5fa503054a03 | -13.4458 | -43.8128 | 2026-09-05 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e13d8ccb-80c7-303d-8e15-68ac19a39ab6 | -5.6565 | -60.2475 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 23f9e019-55f2-3d4d-9c7f-59a8a4221944 | -6.5963 | -59.9087 | 2026-09-05 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f2313304-a0f7-3c31-ac3a-16565fc3dd3c | -5.1802 | -56.0518 | 2026-09-05 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f5398f52-baf3-3da4-b6df-10db68ea67bc | -5.7758 | -45.0599 | 2026-09-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 37124143-88e7-3a0e-9815-5933f34ceea4 | -6.6513 | -59.9642 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2fb92467-b8f1-3464-b533-5f064e4ddcb5 | -4.6669 | -55.635 | 2026-09-05 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 20b497c0-beb6-3992-9d03-2dd4e13bc379 | -9.5534 | -40.3254 | 2026-09-05 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 245.8 |
| 1cd9b2a0-5620-3637-a2dd-4f2555a7d06f | -3.7827 | -61.7733 | 2026-09-05 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 2786cb1b-902d-3678-94a5-7aad77e6cd23 | -5.9197 | -47.8927 | 2026-09-05 01:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 396bd20e-2b6d-3c53-b012-a100a96a5f35 | -3.7645 | -61.7548 | 2026-09-05 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 333f52e3-97d0-3b55-a24b-5c0085ba46fa | -5.1801 | -56.0715 | 2026-09-05 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 773a64e6-325f-32a2-8ab0-d01003964bba | -4.6853 | -55.6343 | 2026-09-05 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1284ad80-62cb-3365-9df3-c60844b2748f | -5.7756 | -45.0826 | 2026-09-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9e2c3135-4765-3835-9b78-0ca7e6d68efe | -5.1618 | -56.0525 | 2026-09-05 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 264ed4d3-dfcd-3bd4-99f4-e20531e509c1 | -10.7677 | -60.7279 | 2026-09-05 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 20790f4e-2b32-3b22-9c9f-608a22f3bfca | -6.0244 | -60.1781 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 098f4101-e5af-31f3-82f0-03e38bf374f9 | -5.7571 | -45.0613 | 2026-09-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 758ac1e1-ff64-31e4-8def-47d0ff1cf013 | -5.9383 | -47.8915 | 2026-09-05 01:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 59b53cd0-cdbf-3f9e-9c68-8972ff7eb209 | -5.8402 | -60.2607 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6e508ff9-d6d2-3462-ae74-24b8f4f45206 | -6.6698 | -59.9443 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 81e35a2f-a9c7-3cad-ab47-203dbf4599f6 | -6.6514 | -59.945 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| a1f26aab-57dd-3111-a0e8-9a98e9c70531 | -5.6566 | -60.2284 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| b259d6b6-d471-355f-bd02-30217e1fd683 | -14.905 | -44.6782 | 2026-09-05 01:30:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 239ace09-08b1-3f8a-bbfd-90a44f640ed1 | -6.6697 | -59.9635 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 47d3761c-9fa9-3827-93cd-9052735b5d5d | -20.2498 | -51.2127 | 2026-09-05 01:30:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 91.2 |
| 43de2538-e247-3e80-b8ac-af68193e20bf | -5.565 | -60.1739 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 24a19a4e-97f9-3984-9548-3ae75e936c0a | -9.553 | -40.3503 | 2026-09-05 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 2bd05bb6-7793-3961-9125-7400d7060eaa | -5.851 | -52.0465 | 2026-09-05 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b4d7e786-13cf-3d47-8c77-2d9565091f39 | -3.7645 | -61.7737 | 2026-09-05 01:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 24b8f609-490f-368c-a018-aa75280ae19a | -6.0245 | -60.159 | 2026-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 641fea7e-c7d1-3bc3-8851-7aafb5d0587b | -17.1078 | -56.8304 | 2026-09-05 01:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.4 |
| 3281e4c0-e8f2-32f0-9977-26e058e6c0c4 | -10.7677 | -60.7279 | 2026-09-05 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 5217494f-9017-3534-b40a-05542e1ea9e4 | -13.4264 | -43.8163 | 2026-09-05 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e4b254f6-761a-3199-9754-a0c0479739bd | -17.1274 | -56.828 | 2026-09-05 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 8a1ba399-5c71-3a35-bc2e-4a18fde0dbd9 | -10.7865 | -60.7268 | 2026-09-05 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 18b08c7b-cd16-39e0-813e-3a0b121c7a7f | -5.6566 | -60.2284 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| c91f0807-c452-3c43-8090-513332cad463 | -6.0244 | -60.1781 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ed568cf5-9ea0-3626-936a-2622da819d8a | -6.6698 | -59.9443 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| fd382627-88ef-3d43-93d1-a9f892874c13 | -10.7863 | -60.7461 | 2026-09-05 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| dcf89ea3-0651-3a07-99e1-6120a82ec7ce | -17.1074 | -56.851 | 2026-09-05 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.0 |
| d19d10e2-74bf-3017-8b86-804448c16db0 | -13.4259 | -43.8401 | 2026-09-05 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6c47dc09-ebb4-3362-ae93-0c1d98c78abc | -13.4453 | -43.8366 | 2026-09-05 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3c69dd53-285d-38b9-8d63-1bd610166a7a | -5.7756 | -45.0826 | 2026-09-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f13ade16-25bf-30ef-bd3b-cb6b1f000746 | -9.5725 | -40.3227 | 2026-09-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.4 |
| c34f3211-235d-3fdf-876a-abb78ef4d9cd | -6.0428 | -60.1775 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| fa1c8182-3c2b-355e-b8be-99f2c7a02f54 | -6.6699 | -59.9251 | 2026-09-05 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0a3e6e9e-aa33-3ba6-86a3-ab4faef107b8 | -10.7676 | -60.7472 | 2026-09-05 01:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| cd57b7b7-cefa-38e7-b54e-8254fd9232ae | -6.6514 | -59.945 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| bae6578f-e2d5-34c3-8736-111606dc970a | -6.6513 | -59.9642 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f5eae8df-6d02-3187-a579-0f010589e96b | -5.7758 | -45.0599 | 2026-09-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| fa5f53fc-9b40-3f0d-a089-0c54f5e887c3 | -6.6697 | -59.9635 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| e62df09b-8945-347c-888a-23d15336eef0 | -4.6669 | -55.635 | 2026-09-05 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 161b00cf-14b8-3891-8f14-494cb9569c3b | -5.851 | -52.0465 | 2026-09-05 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ba355b41-d4c4-3010-afec-1fea44b5a2f4 | -5.8695 | -52.0455 | 2026-09-05 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f00ea9ea-1674-300e-b970-6445d95c94f8 | -15.0773 | -52.5183 | 2026-09-05 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f5a0a974-d82f-31b1-a81a-a56fac297f7b | -13.4458 | -43.8128 | 2026-09-05 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 6317b2d2-f988-3147-8cc1-9c0d55b3f3c9 | -9.5534 | -40.3254 | 2026-09-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 1741b23a-5a44-3bf0-9d4d-f8d54b074c74 | -4.6853 | -55.6343 | 2026-09-05 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| dedde968-570a-38c5-9ae7-435d0dc3b235 | -6.6515 | -59.9258 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 7541cd79-6ac0-3798-9410-746dc291e4bf | -9.5721 | -40.3475 | 2026-09-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.6 |
| b901ce4b-d554-3211-9516-682e1980c587 | -17.1078 | -56.8304 | 2026-09-05 01:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 930d11c1-bd47-3c3b-98cc-acc044415113 | -5.6565 | -60.2475 | 2026-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4a94943a-0290-3efe-b79d-84e7816e8ad6 | -5.7756 | -45.0826 | 2026-09-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 217d3836-0299-393b-afc9-43d4e0189ad4 | -5.6566 | -60.2284 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 748a0b3f-9199-31d7-85cc-7908cb04550f | -10.7865 | -60.7268 | 2026-09-05 01:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 16917f01-4d09-3878-a457-be23787db500 | -7.6767 | -46.0546 | 2026-09-05 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0508ca1f-13f1-348f-9896-7ac5026b94e7 | -4.6669 | -55.635 | 2026-09-05 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| f4394f86-926f-3dc3-9509-f7017ae18de3 | -6.6514 | -59.945 | 2026-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 89dfc44d-e66d-3c4e-9b54-01047eb1c304 | -13.4259 | -43.8401 | 2026-09-05 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4f9e54d4-6b61-33c1-9e25-fca9bb5af5c3 | -5.7758 | -45.0599 | 2026-09-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4f102956-e023-3641-a41f-42f290d1b340 | -9.5538 | -40.3005 | 2026-09-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.0 |


[Clique aqui para ver as próximas entradas](README8.md)
