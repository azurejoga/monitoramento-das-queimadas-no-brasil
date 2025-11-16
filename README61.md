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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f1cf0ba-bdea-39a5-bbd7-6cf0c3dfa1d7 | -14.41398 | -48.29934 | 2025-11-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d2581e6e-36a0-3190-8965-46af2f71f98f | -14.64276 | -46.58657 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5429f0be-d158-3ac3-b1cc-6df0e24a888c | -14.67952 | -46.55041 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2b8d9e45-b9cc-33a0-af76-a4f2a21d77c1 | -14.67529 | -46.53968 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1627ac4b-0634-3dcd-abf3-41a7e8b8c854 | -12.98566 | -49.93765 | 2025-11-16 04:59:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef60602d-cfce-3c6f-b8b1-84fb00649794 | -13.81934 | -42.54976 | 2025-11-16 04:59:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 99c614bf-9aa0-32a6-b54a-9512b89d6a32 | -14.648 | -46.58836 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eee79f23-4b16-30f6-bfc7-3e5f5615d514 | -13.75492 | -48.66968 | 2025-11-16 04:59:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 372067c1-3ae6-31d6-9132-cc980919cc28 | -16.57017 | -47.60886 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9f070d7-57dc-3f64-91a2-b05fcfbd5f1c | -14.65324 | -46.59014 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dd97cf9-8afb-3c7f-803b-b83c1c6dfc8e | -14.89963 | -47.3716 | 2025-11-16 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c5dc418-619f-3a2b-a0ca-f11b1b9a78b4 | -14.64317 | -46.58292 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b1ddff8-6869-32cc-b0b8-8ab50f3d5550 | -14.64767 | -46.56459 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e388ce76-c83a-377b-a310-2cee8cbb2e59 | -16.5647 | -47.61119 | 2025-11-16 04:59:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86f323ec-21e6-35e8-a86b-bb55c9c4c0a3 | -14.64546 | -46.56252 | 2025-11-16 04:59:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e693a70-2fe1-364f-8434-7da7aa7d3e27 | -13.05818 | -53.95168 | 2025-11-16 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9639658-ae11-3a53-9fe9-90d567d088a7 | -12.0004 | -49.2683 | 2025-11-16 05:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 977b54b1-ed95-3703-8bde-cf0ab0fc675c | -11.9779 | -44.9671 | 2025-11-16 05:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a91af346-1cfe-3c57-b46d-10baca61376d | -6.3121 | -43.7804 | 2025-11-16 05:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d48a5a8c-23f9-37b2-a613-d153262d32d2 | -6.3119 | -43.8036 | 2025-11-16 05:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| c604045d-0583-3a02-91a0-1a62f892b97a | -2.5238 | -47.8115 | 2025-11-16 05:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9bec1435-7af4-3603-bf1c-8b964aa4a22a | -11.9779 | -44.9671 | 2025-11-16 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9b210549-a0bb-3bfe-afbe-3db5cf4dd7ec | -6.3121 | -43.7804 | 2025-11-16 05:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 243e85c3-fd85-38f2-8997-e6aa39d9541c | -12.0004 | -49.2683 | 2025-11-16 05:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 77d51dba-66b8-31ca-b4e8-94e69e529844 | -3.7806 | -44.9521 | 2025-11-16 05:10:00 | GOES-19 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a42afe70-3613-33e9-a38b-d8b6faa72d53 | -3.762 | -44.9529 | 2025-11-16 05:10:00 | GOES-19 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 74e110a2-6c1f-3d6d-94c9-35da5938312f | -6.3119 | -43.8036 | 2025-11-16 05:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 2e9c7567-67be-3b9c-b2ff-8629dff3509a | -2.5238 | -47.8115 | 2025-11-16 05:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d6894c2e-bda7-3a92-8c5e-0d6412242330 | -6.3119 | -43.8036 | 2025-11-16 05:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 38fe1ca5-cb67-3a04-a12e-fda1b0b28351 | -3.762 | -44.9529 | 2025-11-16 05:20:00 | GOES-19 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| f2aef7fe-1abf-3c34-9c4c-9477eb3d7bf5 | -3.7806 | -44.9521 | 2025-11-16 05:20:00 | GOES-19 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 753f58a5-f367-3fac-a8b4-09e7b10cfe98 | -11.9779 | -44.9671 | 2025-11-16 05:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| ec5b2765-d836-33bf-a9bf-607375d59f74 | -9.8305 | -47.0852 | 2025-11-16 05:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fdd774f9-9cb2-3a5a-9558-52ebfcc203b8 | -6.3121 | -43.7804 | 2025-11-16 05:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a8247187-862b-3a2e-bc5c-b36f6e5762b0 | -2.5238 | -47.8115 | 2025-11-16 05:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 36feb991-3bfd-31ca-af9d-27a24f041ca9 | -12.0004 | -49.2683 | 2025-11-16 05:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1a2018b8-602c-3523-b23c-f59c23f7f0af | -6.30509 | -43.78716 | 2025-11-16 05:20:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6fd1c362-2ab9-351b-8933-c71b07d2becd | -6.71687 | -42.93359 | 2025-11-16 05:20:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 32d11ed9-9aa1-3538-8270-62716d15fd30 | -5.33474 | -43.0262 | 2025-11-16 05:20:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 9f883eaa-3154-331e-8b2f-9a7c5bd41949 | -4.4063 | -43.39527 | 2025-11-16 05:20:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cd424438-9c51-3533-9f0b-18c7ee0cd80d | -6.31819 | -41.82686 | 2025-11-16 05:20:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| e81913d5-2d4e-326b-8802-d90fdd885787 | -6.29651 | -43.80807 | 2025-11-16 05:20:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| b65daf53-d404-3dac-bde7-d64296280a19 | -5.31754 | -35.9348 | 2025-11-16 05:20:00 | AQUA_M-M | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 570f7ec0-fa80-33cc-8e59-b7d809b4ad01 | -5.31887 | -35.92604 | 2025-11-16 05:20:00 | AQUA_M-M | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 92e18df3-30cf-3f8e-9a66-eb72cd09a313 | -5.33104 | -43.04933 | 2025-11-16 05:20:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 61ff1b4c-bb3c-336f-9d50-1499f3880881 | -4.42061 | -43.39773 | 2025-11-16 05:20:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| f265a865-0dc9-3e15-b343-5ede20512531 | -6.70419 | -42.12523 | 2025-11-16 05:20:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 79076adf-018c-3cba-855a-b41195151ff5 | -3.76799 | -44.96033 | 2025-11-16 05:20:00 | AQUA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 76908b37-efe7-394b-a4fe-8ef830ec2285 | -5.34253 | -43.03269 | 2025-11-16 05:20:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 10c88724-64a0-342f-923e-3b0a28105cc3 | -5.4651 | -40.96556 | 2025-11-16 05:20:00 | AQUA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e61e9cb9-f5eb-3ba1-a991-0e4f0eb6e776 | -6.30085 | -43.7816 | 2025-11-16 05:20:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 5a567ca0-73c6-3df6-a735-320530c6e589 | -4.26103 | -38.0811 | 2025-11-16 05:20:00 | AQUA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8dcd303c-858c-31b5-9a69-edff03b2afd9 | -3.76013 | -44.95404 | 2025-11-16 05:20:00 | AQUA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 104.4 |
| f45c6aa0-27ee-3183-89fe-2436929da832 | -11.9745 | -44.97111 | 2025-11-16 05:22:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 50d7014f-dd17-3de8-9bc4-7cddfa440446 | -9.99846 | -44.76261 | 2025-11-16 05:22:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 8b1021c5-793c-378d-82c6-b48bf315ae67 | -11.97895 | -44.94616 | 2025-11-16 05:22:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a228fd27-d26a-3ce6-bba4-f9becec0e9bf | -11.96072 | -44.96715 | 2025-11-16 05:22:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 2c0a8ce1-5e01-3765-abef-94ae15fa8a91 | -9.74017 | -43.96056 | 2025-11-16 05:22:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 9cfdfbf0-a6d4-3989-9dfc-6d5d220a32fd | -11.96523 | -44.94206 | 2025-11-16 05:22:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 66e1067a-1cc6-3e10-9f3a-7803633627a7 | -8.05716 | -43.09604 | 2025-11-16 05:22:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| a08b24d7-5489-3845-baf6-4f5036789f7f | -9.72666 | -43.95802 | 2025-11-16 05:22:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 2b3b530e-8c77-3de3-9b07-2351b8dbee35 | -13.55486 | -44.0971 | 2025-11-16 05:22:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e44375dd-8c65-3199-837a-f064e7124e80 | -7.40172 | -40.05823 | 2025-11-16 05:22:00 | AQUA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9a6b6ca5-03e1-3ca1-a198-577761d5c987 | -13.80759 | -42.5481 | 2025-11-16 05:22:00 | AQUA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 3fa6d8b7-1320-3087-8297-fa76105b960a | -10.83838 | -44.0899 | 2025-11-16 05:22:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| c0491a6f-37dd-3764-ae74-42955cad59e2 | -9.83172 | -47.06733 | 2025-11-16 05:22:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| ae4e3d40-783d-3b5c-8ad3-4d4349579036 | 3.2331 | -60.7024 | 2025-11-16 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 993ca5d4-e7f2-3cda-99bf-6fc555830f67 | 4.01717 | -59.66101 | 2025-11-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b85eb560-ebb9-3687-9dea-95949b967b74 | 2.75157 | -60.36596 | 2025-11-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc0f0a39-ae60-3e88-a813-659e68514752 | 1.61644 | -55.81543 | 2025-11-16 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dbdc1e4-b949-3cd9-bb37-dfbc6f7b1f9b | 4.02449 | -59.66353 | 2025-11-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fb2106c-cd76-36a8-b2c4-b45170b74c1c | 3.88812 | -60.3403 | 2025-11-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa863d8a-2028-3d7b-bdb2-e225eb713889 | 3.8863 | -60.34042 | 2025-11-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b012d531-111f-3455-8b6a-567a5e2af824 | 1.994 | -50.87822 | 2025-11-16 05:22:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73d91a1f-baff-3dbb-b794-77d4b5bbcfb0 | 4.01773 | -59.66461 | 2025-11-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d229bd9-e1ba-3ebb-9b8f-571785761f2a | 4.01662 | -59.65746 | 2025-11-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6f7c6936-1446-348f-badc-b406b20dc685 | -14.67193 | -46.52805 | 2025-11-16 05:25:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 5caa6e46-73c8-3744-a5a9-9dd4e1ba579a | -14.67153 | -46.53325 | 2025-11-16 05:25:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 58a94335-e49a-3b7d-92e4-65cf1de01d7c | -1.21999 | -53.36598 | 2025-11-16 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c182a4c-d13a-3a10-857b-32efd68748d1 | -4.01929 | -48.81212 | 2025-11-16 05:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b126d1a6-a4ff-34b6-a7d2-4f9507e14b13 | -6.14313 | -48.04425 | 2025-11-16 05:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26cb5be2-78a9-3649-a486-0e28823a21af | -3.9331 | -47.04913 | 2025-11-16 05:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0545541d-14ea-3020-bd9e-6c71b0062a95 | -4.64832 | -47.94862 | 2025-11-16 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0dab621e-9d4b-382e-a9b4-abd8ed8f1dd8 | -4.2449 | -50.04814 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9480bfee-e93b-3a10-b5fc-60095257b539 | -6.13223 | -48.04823 | 2025-11-16 05:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31555aef-aeef-3667-8adf-f4d6f5ab83a1 | -6.32142 | -55.16611 | 2025-11-16 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70d46d08-8174-3855-b4a9-f47a3e68ae57 | -3.33563 | -50.27768 | 2025-11-16 05:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfb475c8-bad7-3bfe-be2e-b88153aa8d4e | -2.96622 | -53.22305 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1917376-893d-3de9-a16b-32a401ad439e | -6.13581 | -48.04863 | 2025-11-16 05:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 463a4d6d-752b-3500-877b-71261632dc99 | -4.5 | -50.79543 | 2025-11-16 05:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04fb1f8a-819c-391c-b4d0-4d13979ed662 | -5.12613 | -55.97058 | 2025-11-16 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ee99b94-6e58-3563-b2bd-ed98ab56f044 | -2.17878 | -52.08816 | 2025-11-16 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f503648d-5bf7-3565-8281-c20e9b871080 | -2.96454 | -53.21946 | 2025-11-16 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2be48710-b80a-34f1-9556-c4ad75d78933 | -4.70013 | -46.31414 | 2025-11-16 05:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8f795899-2bc3-3fec-93fe-eece00ea17d5 | -6.81428 | -48.7909 | 2025-11-16 05:25:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be74fa27-dbe0-36a4-87f5-1e4437049478 | -2.14201 | -52.76814 | 2025-11-16 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a431f68-1900-3282-9da3-a0ad2b846944 | -1.83167 | -53.79168 | 2025-11-16 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1392c2f-3f97-3881-b0d0-848702575775 | -3.77432 | -52.10263 | 2025-11-16 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cad3ca4-b7a2-34ee-afa2-b755bbe7f2fd | -7.70877 | -47.29358 | 2025-11-16 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97fe3c92-4442-304e-8336-e5d515e85b23 | -1.04329 | -57.4803 | 2025-11-16 05:25:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README62.md)
