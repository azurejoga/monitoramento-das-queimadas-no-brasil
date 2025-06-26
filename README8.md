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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d709ed6-6852-3504-b1e9-41f2cf7594bb | -20.25312 | -46.72498 | 2025-06-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98608516-9adb-35e0-8a09-c23d2455776f | -20.2575 | -46.72578 | 2025-06-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e7e3d97-7df6-3153-8f96-575c7ec9ba08 | -23.40366 | -46.55601 | 2025-06-26 03:51:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 42ee5ef1-af07-35ee-be3f-5c382bc2c2b4 | -20.25401 | -46.72044 | 2025-06-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ac58473-43f9-3f37-ac9d-d313e41a8e70 | -20.30991 | -45.58472 | 2025-06-26 03:51:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dd7a977-f9db-39ff-816d-49a91d55f158 | -22.85604 | -42.98113 | 2025-06-26 03:51:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 18f7f28f-906c-376e-b3d3-57432d52a0e0 | -23.98479 | -48.91512 | 2025-06-26 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f58e4f0-d91a-3577-997b-b01dca4e45e8 | -22.14252 | -43.04412 | 2025-06-26 03:51:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ba8bbc4a-f4dc-39c1-90c4-83b51bb3fb80 | -22.79702 | -45.15693 | 2025-06-26 03:51:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 87ee54a0-897c-344d-a158-bbaa24579221 | -23.59441 | -47.43945 | 2025-06-26 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 120e267f-4fed-33aa-8979-c9e9b3fa1380 | -20.25128 | -46.73437 | 2025-06-26 03:51:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ae682df-3116-332b-bde3-0a33808ea3d5 | -22.93865 | -43.41993 | 2025-06-26 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92ea268a-bab4-3737-8af6-c3cf7f6df75c | -22.13905 | -43.04337 | 2025-06-26 03:51:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a271fc33-5858-3c8e-9ec9-4f7bbe5dfff5 | -22.78473 | -43.75826 | 2025-06-26 03:51:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0e329ef5-26a5-3bda-af9d-61ca724d5b02 | -20.50209 | -45.58865 | 2025-06-26 03:51:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a75453d8-de25-3616-a90b-f995226b84cb | -22.85717 | -42.98222 | 2025-06-26 03:51:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a0e129a8-bc52-3816-8245-08d9ebc2f28a | -22.93936 | -43.41589 | 2025-06-26 03:51:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4253bf2f-ff1e-3217-a509-696e7c2f30ea | -22.67754 | -42.85535 | 2025-06-26 03:51:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4c863415-af16-3744-8a21-47f547dddf43 | -20.5028 | -45.58493 | 2025-06-26 03:51:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab3ccd31-0445-3785-9f82-77747e9c80f6 | -20.30961 | -45.58384 | 2025-06-26 03:51:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecea3a50-f565-3b0d-8600-8882bf895102 | -22.14326 | -43.03983 | 2025-06-26 03:51:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 63d0051f-185f-3789-b044-876864017fc2 | -20.76326 | -46.76881 | 2025-06-26 03:51:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09ee9dc8-57b8-3f1e-8bb0-d8b2e4fe975c | -23.33759 | -46.77122 | 2025-06-26 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 379ae82c-8203-3f1f-98f6-9f30f9cd1086 | -22.14672 | -43.04056 | 2025-06-26 03:51:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| f54252f0-e528-3253-8ed9-e17d25400ee3 | -22.87013 | -42.38683 | 2025-06-26 03:51:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d0fa12f0-3b25-35c7-a057-9f669cec8072 | -27.68583 | -48.75029 | 2025-06-26 03:53:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f8c21193-3822-362e-bfc8-8d0562d2d71e | -9.1213 | -49.4313 | 2025-06-26 04:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 16b18f2f-6b1a-3d8b-a8eb-5317e58db7d1 | -11.0644 | -55.3757 | 2025-06-26 04:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| aa5906c2-7184-37d4-a3ac-0e2731f901a6 | -9.121 | -49.4528 | 2025-06-26 04:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 470fc278-6b29-3dda-b7a7-0fadb5f276ce | -6.1791 | -48.0712 | 2025-06-26 04:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fabad6a7-5109-3b54-a0d9-5161347d895a | -9.1213 | -49.4313 | 2025-06-26 04:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ef89ec84-5673-32c6-b981-065e58d8476c | -9.121 | -49.4528 | 2025-06-26 04:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9c21108e-52b7-3400-b54c-9f24ea1824f7 | -6.1791 | -48.0712 | 2025-06-26 04:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 5becd8de-c40e-327a-9ae5-0367e09b8eea | -11.0644 | -55.3757 | 2025-06-26 04:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 7770989d-d208-3ee0-a934-018f710e2a3a | -9.1213 | -49.4313 | 2025-06-26 04:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 705dda45-30af-39ac-81e7-ac191d0eb2c4 | -9.121 | -49.4528 | 2025-06-26 04:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 015dcdc5-a347-3164-b83e-4d8066782f72 | -9.1213 | -49.4313 | 2025-06-26 04:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 251d09ca-e25c-35b7-86ea-24d2cd38494d | -6.1791 | -48.0712 | 2025-06-26 04:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e4ba8793-eef1-3de8-8712-685665115050 | -4.84526 | -47.70828 | 2025-06-26 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 074795aa-9b34-34d5-b595-b9167dc14e30 | -4.42298 | -47.73534 | 2025-06-26 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1655b830-c2b7-37db-8f97-9fbc82ad29f5 | -3.98057 | -48.4134 | 2025-06-26 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8b37710-b7b3-3fb9-b3da-a3e75c889591 | -4.6888 | -48.86688 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5507cf2-f7a2-399e-9910-548c0649703a | -3.98388 | -48.41391 | 2025-06-26 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e92b3ad-4359-3d54-bffc-8ed42f658c7d | -4.53038 | -48.04905 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7a6ac291-a83f-3ca4-a863-93a71ffec2c6 | -4.66707 | -40.56018 | 2025-06-26 04:38:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a662bcbd-bb73-35e7-865d-e754e4622b4f | -2.7509 | -54.59192 | 2025-06-26 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bff2bb71-efa9-3b96-bf25-c24b5fc22a38 | -2.53553 | -53.95902 | 2025-06-26 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0018ed6-31c6-38e7-8c4b-abbdf902978f | -4.27182 | -48.18159 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 450e23b5-9eff-3bfe-a4ce-4014906488d6 | -5.43798 | -46.56547 | 2025-06-26 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 144ecb20-6f6b-3d7a-b056-6acfb7a5c3fb | -4.10057 | -48.69325 | 2025-06-26 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0952625-180e-3818-9ad1-95482427e917 | -4.68827 | -48.87032 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1820fc4-16e6-3003-be23-0648bd7efbf0 | -4.42008 | -47.6654 | 2025-06-26 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d4c2a49-2cf2-313a-930b-42c5b73e9485 | -4.12431 | -43.06877 | 2025-06-26 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1977aae-806d-3ffe-b380-ca8f42e1ba40 | -4.53357 | -48.0062 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 38161e8a-f8d9-3a7d-aab8-dd4eebfbd0f2 | -4.97692 | -48.04245 | 2025-06-26 04:38:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78ac2fb7-c989-32e4-9dc1-b8753cc0ae64 | -6.2207 | -43.36432 | 2025-06-26 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 92b2c30e-1c33-3be1-b6ab-b126cbc3af6d | -4.53691 | -48.00674 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60d973c0-ea08-3652-a9ea-81f3adc5c891 | -4.12877 | -54.8993 | 2025-06-26 04:38:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7515930-7fa9-3fec-b9f5-6966cca4d971 | -3.87566 | -47.55632 | 2025-06-26 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f1b3bb3-5d35-34ff-bb87-e86cc128eb19 | -4.1286 | -43.06943 | 2025-06-26 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ae28434-e49f-3249-b1c1-9acfb7b36a9e | -4.52984 | -48.05256 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bbb3557-e961-322b-a7ec-bbcee8db2cc1 | -4.12921 | -43.06539 | 2025-06-26 04:38:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e56887c-2bc3-3fbd-90e5-ab2f33b527cd | -4.27515 | -48.1821 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c0bfcf5-3ffe-31ef-95c1-493ec86677dc | -4.52371 | -48.04802 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7213f188-3e7a-313d-9f37-a73d77e4e402 | -4.01192 | -43.24086 | 2025-06-26 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 993e8b0e-8782-36fc-97fe-c1944f299f10 | -4.18828 | -48.15032 | 2025-06-26 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e74fdd40-fadc-345a-9fba-00890d540f96 | -3.54808 | -43.5744 | 2025-06-26 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec8200a6-a15e-3fc2-89e0-1e69bb3c3699 | -5.84133 | -48.39177 | 2025-06-26 04:38:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebd7f00a-775e-3f24-9fc3-1ae1f56e5aa1 | -4.70873 | -55.99345 | 2025-06-26 04:38:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 290ceb34-d030-3dbf-9661-edaeb6d2aabf | -2.44587 | -47.49689 | 2025-06-26 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac030e82-9518-346e-a6fa-b95308b1fd9d | -5.84078 | -48.39528 | 2025-06-26 04:38:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 939fe3dc-eba2-3ba2-8406-bb2013f9345c | -4.27236 | -48.1781 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9e81897-1a57-3327-ba1a-99231842179c | -4.18882 | -48.14686 | 2025-06-26 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08d5079f-f0a8-3d8d-828f-ad7693bb9513 | -3.38013 | -43.1235 | 2025-06-26 04:38:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1409c859-11d4-3c0f-b401-0660ba7d35c1 | -4.66664 | -40.56326 | 2025-06-26 04:38:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9d802cdf-b066-3058-81da-e17064cc8ca7 | -4.52705 | -48.04854 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f1865426-67b6-3a0e-88eb-a8d2e7cae488 | -4.67988 | -48.26975 | 2025-06-26 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 163ef142-ba3c-33c6-8ebe-d05eafca3a56 | -5.33391 | -43.75194 | 2025-06-26 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 049a13e3-1ba2-385c-8ce3-d26569880a3e | -2.44411 | -47.46416 | 2025-06-26 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5ae4d60-c20c-33d1-be13-571e46c8532e | -5.44152 | -46.56596 | 2025-06-26 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f6f7882-1432-3789-a941-3f5a47a6c7d7 | -4.08005 | -47.94717 | 2025-06-26 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 181f02c3-12a8-35b8-be82-7a8a7a8c2f89 | -5.45111 | -43.57407 | 2025-06-26 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec8e1a4e-57b1-3ab7-aca1-cbe7d09a20d5 | -6.21637 | -43.36359 | 2025-06-26 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cacc1aeb-e64d-3997-9632-7f0195ad2a52 | -9.1213 | -49.4313 | 2025-06-26 04:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 6704ee4f-6d3b-38b9-aa63-9e094a1a31ba | -6.1791 | -48.0712 | 2025-06-26 04:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| a685d1c4-0a5f-3465-9c60-fc94cff6f5f6 | -10.71227 | -59.13044 | 2025-06-26 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2dc7a00-2b0e-3210-ae5c-fb470a51e269 | -7.75348 | -47.61641 | 2025-06-26 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b68df0c0-e880-3711-9d90-712edb313367 | -9.1215 | -49.43518 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c94498b8-c9dd-3924-b2d0-ef89da58f296 | -11.364 | -48.7112 | 2025-06-26 04:40:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 02d38dd8-6cf3-3d75-9565-80ffbbce6e36 | -11.23741 | -49.48899 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 506ec4b6-31f8-34bb-b0e2-0625331fed0d | -10.87605 | -56.4567 | 2025-06-26 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 551ece7e-c0ec-30c5-900b-2433682e83b4 | -10.99203 | -49.54255 | 2025-06-26 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0daab7c-09d9-3880-9eab-a1a9c6e949e5 | -9.70972 | -49.48008 | 2025-06-26 04:40:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4b28895-f0f4-3936-a412-4cbecba6bad7 | -10.70773 | -59.12674 | 2025-06-26 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eed26c3-646f-334c-94aa-2f566b4ba08c | -11.11313 | -46.65788 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 164c69b3-19b6-3564-8fb1-c3e3ed2a7feb | -11.81613 | -47.54739 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc97f3fd-30d7-3e2b-9fb3-ff8642fd4828 | -12.48717 | -45.90031 | 2025-06-26 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3154c5bc-0b6f-347e-8d59-f050d47fb0f4 | -7.98225 | -49.65475 | 2025-06-26 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d225a5-c809-3126-a4aa-000a1c594094 | -8.72405 | -48.0157 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5741d450-3783-3fa2-aad6-7f4313a33bb6 | -10.87675 | -56.45277 | 2025-06-26 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README9.md)
