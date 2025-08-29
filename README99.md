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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7501bed7-9e1d-300b-b1df-72a6c0725a16 | -12.6552 | -60.2563 | 2025-08-29 14:30:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| cf842243-266c-3795-b0a1-e248f55b7448 | -14.3303 | -53.2898 | 2025-08-29 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 6af48e93-400e-37d4-b58d-b23b282735cf | -6.2741 | -43.8299 | 2025-08-29 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5894418a-6a3b-3922-9c22-d9af3b345ad8 | -10.8419 | -60.8202 | 2025-08-29 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 21306085-9e23-3e5d-b6e3-0eb060b90cc1 | -7.6036 | -42.6758 | 2025-08-29 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 82ff00fd-72db-3250-8287-2c72170d8bdd | -9.4246 | -60.5701 | 2025-08-29 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| f61ab5fd-8c52-3708-a464-5efcb73c072e | -13.5774 | -46.8714 | 2025-08-29 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 8ee86282-d89e-35fa-87c6-35f96639a448 | -12.0362 | -50.6448 | 2025-08-29 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7535d942-f5fb-3ffc-8fcf-a7b1898145c5 | -9.7728 | -64.2657 | 2025-08-29 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| fe4ec4f8-d0d5-3314-a70a-9680a45e330c | -10.025 | -48.058 | 2025-08-29 14:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f586aad1-740e-34e0-a60e-fc7a29696b88 | -9.171 | -65.7869 | 2025-08-29 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e8f8576a-8e44-3d73-ab6c-6901facfb666 | -9.4618 | -60.5682 | 2025-08-29 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 0cb8fa06-4bcb-32da-af32-9c9e6bd3122a | -6.3327 | -43.593 | 2025-08-29 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b75dba59-cd2f-354a-86fa-99b54ec3e0eb | -9.1715 | -59.5599 | 2025-08-29 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 212aaed8-667c-306d-9bde-1487622a8da0 | -12.8413 | -48.1685 | 2025-08-29 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 812356fc-cf15-337d-bcf2-5ede312a56c7 | -7.6036 | -42.6758 | 2025-08-29 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 3b6cb210-1c6e-3501-ba25-5b5835e50d65 | -14.3296 | -53.3318 | 2025-08-29 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c734cb5e-1499-3349-b439-82654bf4940a | -9.4618 | -60.5682 | 2025-08-29 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 179.3 |
| d5bddd37-551b-3e39-a5f4-943bbed12e46 | -8.4599 | -43.6411 | 2025-08-29 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 266.6 |
| 2126fd74-1a5b-359c-846f-01c21fea5618 | -11.0826 | -44.7503 | 2025-08-29 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0fce3004-0fef-314c-805b-069ce25abecf | -11.8756 | -46.4234 | 2025-08-29 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 4e94f0d9-5e1e-3d15-adbe-4cdd6035bde8 | -9.171 | -65.7869 | 2025-08-29 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| faea2f63-7a40-3185-9e67-eb3e2380c876 | -9.1904 | -59.5201 | 2025-08-29 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5d9acd1c-6c8b-34a6-9704-d6e3c32bed0d | -9.7915 | -64.265 | 2025-08-29 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 5050a7cb-d8e5-353f-ba91-47393835add8 | -9.4246 | -60.5701 | 2025-08-29 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 275.3 |
| 874ee569-9b42-3787-9688-9dd31f5bf278 | -12.0362 | -50.6448 | 2025-08-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 18a3ac50-257f-30c9-a26a-67acea8a7729 | -6.19 | -44.7788 | 2025-08-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 35a94a09-d38f-3631-b319-e85e195d9db9 | -6.9867 | -59.3354 | 2025-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| eebd2581-d8c4-3a40-a3a2-cdf71a4e79a1 | -13.5774 | -46.8714 | 2025-08-29 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 471.9 |
| bdb31c36-c0c7-328b-831d-b219b62d5900 | -10.4736 | -57.9563 | 2025-08-29 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6009d531-bb83-37ea-ad0c-abce14fe75d6 | -9.5447 | -45.8842 | 2025-08-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 230.6 |
| 77b45393-25b7-38ab-8a82-4b0d9583cdb3 | -15.0835 | -48.1367 | 2025-08-29 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 0c4c0ee1-9a29-372c-9eae-e4bf9255844d | -9.1719 | -59.5017 | 2025-08-29 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 254562e5-b28b-3600-994f-88ff4a9c13cf | -12.9385 | -56.9655 | 2025-08-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d9179ad6-cda4-3f6c-802a-f66862f78428 | -7.415 | -44.283 | 2025-08-29 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e4586eda-aa40-3a48-b120-6eba25ab3504 | -6.3916 | -45.2402 | 2025-08-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| c4cc7020-ef51-31eb-813f-039617bada84 | -12.6875 | -48.1899 | 2025-08-29 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 83de87e9-ed2b-321c-a5d2-4499952c84f3 | -11.3521 | -43.5423 | 2025-08-29 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.7 |
| f46ecd2f-6f7c-3f9f-ab7c-99872a97e6ec | -6.9866 | -59.3547 | 2025-08-29 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a5f0ac1f-8403-3c4f-b1ad-413171a169e9 | -12.6742 | -60.255 | 2025-08-29 14:40:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 7d5670cf-d47b-3727-b669-635eabdf3a97 | -15.1225 | -48.1302 | 2025-08-29 14:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| b3f36170-b000-31bf-9870-5185ab02b418 | -9.1718 | -59.5211 | 2025-08-29 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| bfb6ac64-9e1c-3b28-a481-90e68baaea47 | -9.4432 | -60.5692 | 2025-08-29 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 562.0 |
| 857f3bc4-ab97-32db-b36f-954745318b8d | -7.1106 | -44.6099 | 2025-08-29 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 990a46d0-da02-3ff9-8b93-0bddc60d23a9 | -12.4345 | -63.9173 | 2025-08-29 14:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 6981b93a-d62e-3bca-95c0-962cc1f8627f | -7.6219 | -42.7212 | 2025-08-29 14:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 132.1 |
| 2d7c0bb8-56fc-3c8f-a152-bc4fdc3780e5 | -8.4788 | -43.639 | 2025-08-29 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f0f0f257-8715-3e4e-bb91-9991fd759f4e | -7.6222 | -42.6975 | 2025-08-29 14:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 192.6 |
| 14fd6b26-6007-39ea-9f21-16cc86eb06e6 | -11.3325 | -43.5689 | 2025-08-29 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 6b18147f-22f7-3038-9f29-73d32b61d849 | -7.6033 | -42.6995 | 2025-08-29 14:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 201.8 |
| d57d5850-e35f-3e57-ad75-a38828e719c9 | -8.4596 | -43.6645 | 2025-08-29 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| bb952087-7a97-346b-85c8-2ccbbc93a8a0 | -7.6225 | -42.6738 | 2025-08-29 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 71bde819-099d-3572-bf6f-c369d6a7dc35 | -15.6749 | -52.7552 | 2025-08-29 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e11f365b-75eb-36a6-a33f-57dd353fa167 | -9.7916 | -64.2461 | 2025-08-29 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 278902cd-e5f9-3530-919d-ad205f106821 | -6.3616 | -44.4679 | 2025-08-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8969a67f-c410-3ef8-83a8-bdd3564e8eac | -14.5445 | -52.0156 | 2025-08-29 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 15d51fe5-d350-3703-8e77-0592ea42ccf7 | -9.1906 | -59.5007 | 2025-08-29 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| fc254767-53f1-3eb1-b5f0-89a80d6c15fe | -10.025 | -48.058 | 2025-08-29 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 678c3a8c-ce39-3f3f-9ebf-2abdc52fc6db | -14.3695 | -53.243 | 2025-08-29 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 08468acc-fbfa-3181-85da-c2868c67b2d8 | -14.0328 | -44.487 | 2025-08-29 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 315.4 |
| fcdaf9e9-f278-3435-b3f6-d831b4ff5b6a | -8.7714 | -68.7082 | 2025-08-29 14:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 01c1c049-0622-3412-b357-ae20aa26a15e | -9.545 | -45.8616 | 2025-08-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 6a9e2717-fed9-3986-87c6-8116facc4117 | -9.1907 | -59.4813 | 2025-08-29 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| fd9db857-6c88-3045-ac67-aa29918f68de | -12.6552 | -60.2563 | 2025-08-29 14:40:00 | GOES-19 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 9a0c5d44-ea3c-30fa-95f2-7a375b2f2191 | -12.9382 | -56.9856 | 2025-08-29 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 1e96c4a7-8fdb-3175-80e1-4b1d74d77849 | -13.3543 | -54.38 | 2025-08-29 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8d7c11c6-1218-3994-9f1c-2fd7d1ba2669 | -6.3918 | -45.2175 | 2025-08-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 916340c6-b01a-356d-a1a9-f53ce8aa0e83 | -9.3238 | -56.9064 | 2025-08-29 14:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5a197027-5add-32b0-970c-7ea61cec037a | -7.233 | -45.4413 | 2025-08-29 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e2c795f6-ac79-3c4f-a487-860ef2b1f18d | -11.3856 | -63.2653 | 2025-08-29 14:40:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 64c5f949-dce2-3fd1-b581-fe5c2f0bfb22 | -9.2493 | -56.8914 | 2025-08-29 14:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ded9173b-219a-3e33-88db-9f125d44deaa | -6.0992 | -59.9267 | 2025-08-29 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 85ddf49b-0b06-3e77-99f6-f69b20e7dfa1 | -13.558 | -46.8745 | 2025-08-29 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 343.4 |
| b8c697a4-7abe-3587-85a1-5ef919bab262 | -12.0553 | -50.6425 | 2025-08-29 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 4f694492-a8d6-39d2-a2dd-6b3b9da2ac6b | -6.3327 | -43.593 | 2025-08-29 14:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| d91cafd5-8b6f-3f34-adce-e1b47f8d4eaa | -9.5637 | -45.882 | 2025-08-29 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 03bcfdae-f52a-323c-9be4-16733e6b0be9 | -14.3299 | -53.3108 | 2025-08-29 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 13e244cc-912f-38a9-a383-30b517d85bbe | -14.3502 | -53.2453 | 2025-08-29 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4bb17cc2-6516-3c1a-b67d-7bf2c035d969 | -10.0247 | -48.08 | 2025-08-29 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 163.0 |
| d1dbff26-37f5-3bd1-a1da-08a1c4e35036 | -12.4156 | -63.9183 | 2025-08-29 14:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 77f30de9-6988-3170-803e-68a9902aaa14 | -9.7322 | -64.9067 | 2025-08-29 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3d5c647f-af51-32c5-95f7-c04b6f050c89 | -9.462 | -60.549 | 2025-08-29 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 441.5 |
| 8576ec55-62a8-34e8-aa54-2688bf02bfe7 | -13.5967 | -46.8684 | 2025-08-29 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 379.5 |
| 57f588e5-2f7f-39fb-beb0-2d23a87a771c | -6.1372 | -44.417 | 2025-08-29 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f999923a-d9b6-355e-936b-e76b634cc8ce | -5.7156 | -45.5388 | 2025-08-29 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a9ef127e-0e2b-3b72-95c3-f8854e89ba55 | -6.2741 | -43.8299 | 2025-08-29 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 51aaeb9d-ddfe-3508-9263-ca0c01102a82 | -11.1775 | -44.7832 | 2025-08-29 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5393a98d-813e-3da3-964f-700d4be54e1f | -6.3881 | -45.6018 | 2025-08-29 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 088755f0-7bcb-3c72-b50f-40b915e85d87 | -8.8854 | -45.7314 | 2025-08-29 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| f29907c0-7411-370b-b51c-2ed848adee6c | -10.8607 | -60.8191 | 2025-08-29 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 15d78994-4c86-39e9-987f-1af66308b8b9 | -11.876 | -46.4007 | 2025-08-29 14:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 202.1 |
| e049849c-31c6-3051-8ab1-cfd0b53b8b0b | -7.6183 | -46.2392 | 2025-08-29 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |


