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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f3be876-cb07-3acf-a7a6-fb7163199f66 | -11.1771 | -44.8064 | 2026-09-29 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 13b5800a-b549-3704-b9ef-6e878c8bfde0 | -10.3894 | -61.2502 | 2026-09-29 12:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 271.7 |
| dbbf3ea8-c002-3c82-82ae-9f17a43c605b | -12.7614 | -47.2656 | 2026-09-29 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| a61aaf95-1636-3ddb-8a3e-98112266c866 | -12.7421 | -47.2684 | 2026-09-29 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 9bfdf2ee-1746-30b1-8776-7f5f75645ebb | -12.6463 | -47.2598 | 2026-09-29 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 8b51c4a2-20d1-3e87-a382-253cc2a969aa | -11.4311 | -43.4121 | 2026-09-29 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| fad2dd9c-ec12-358d-8228-cd80b0453df2 | -14.4839 | -47.0414 | 2026-09-29 12:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d3300592-6c04-3957-9a2d-680c1fa75b75 | -12.6271 | -47.2626 | 2026-09-29 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.1 |
| fdb2bd5f-4c0f-39bd-8733-816ab567228e | -12.761 | -47.2881 | 2026-09-29 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 18fe045b-a40f-3bbe-83d1-2fe763f1bd21 | -18.0943 | -44.4035 | 2026-09-29 12:10:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f5d4f855-c81e-3f61-96a9-9c31f5f0e8db | -10.2843 | -44.6274 | 2026-09-29 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 07094cdc-9a91-3bf1-ac45-a7f41d3104c7 | -11.3962 | -45.3973 | 2026-09-29 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b6c00124-15cd-3b16-8f5e-da31b3b8aec3 | -8.9633 | -44.1655 | 2026-09-29 12:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 128.2 |
| fb0c666b-e3fd-3462-a417-86e79530bf79 | -8.9823 | -44.1633 | 2026-09-29 12:10:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7889f719-7e40-3a7f-8000-5c68c15006e7 | -11.4307 | -43.4358 | 2026-09-29 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 219.8 |
| a137fec7-aca3-35e3-8329-8aa28434b597 | -12.6467 | -47.2373 | 2026-09-29 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8d1d13ba-2dad-355a-9c84-c094be40f569 | -8.6451 | -45.3489 | 2026-09-29 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c1918bb6-b6f3-30a4-be7c-56ff027576b5 | -11.1775 | -44.7832 | 2026-09-29 12:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 3e5fc2b4-b085-3e94-acd6-36d12021b4a2 | -5.73 | -45.18 | 2026-09-29 12:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5eedaaa4-1526-3433-a8db-ac6406a559e0 | -17.52 | -45.51 | 2026-09-29 12:15:00 | MSG-03 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 21dc7b49-28a5-3557-ae27-6036bea76401 | -17.51 | -45.46 | 2026-09-29 12:15:00 | MSG-03 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 186f0aa4-5c83-3089-9d03-1f66d01206dd | -10.3894 | -61.2502 | 2026-09-29 12:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 245.2 |
| 76ee1b42-a3fe-3cd9-b416-0592981cf39d | -11.1771 | -44.8064 | 2026-09-29 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| b96bca73-3b42-3bc3-9d7f-6af9b7288ca6 | -18.0943 | -44.4035 | 2026-09-29 12:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 8debad6b-5178-3512-9be8-907f746bf8e1 | -12.761 | -47.2881 | 2026-09-29 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 181.3 |
| 8291394b-c234-323e-84ec-83360abcbc2d | -7.5245 | -44.5715 | 2026-09-29 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e69da6ae-392d-3716-a4be-de8ebe5f86c2 | -8.6451 | -45.3489 | 2026-09-29 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ceef65b4-164d-3935-8638-d81cb572a8e8 | -8.9633 | -44.1655 | 2026-09-29 12:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5eddbc61-9a97-381e-9da9-02fbdf3bf421 | -14.1309 | -46.2801 | 2026-09-29 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 21843d4f-a3e8-3912-9681-36d2028aa3dc | -14.1115 | -46.2834 | 2026-09-29 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 80ef020c-fd34-3d44-ab8c-55070f53077c | -11.1907 | -45.1274 | 2026-09-29 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a75b909a-55bb-390b-bae5-0cb9dec2ef77 | -12.7417 | -47.2909 | 2026-09-29 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 999cc037-ca5a-32a3-99b9-2671fcfcc6b8 | -14.4839 | -47.0414 | 2026-09-29 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6e60b261-1a6c-3aaa-b170-0d03d14664a9 | -12.7421 | -47.2684 | 2026-09-29 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| c2a83c28-2286-3a41-ac97-fe32e9c1abfb | -18.1144 | -44.3988 | 2026-09-29 12:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ca482ed2-9260-38bf-b706-2c056baa08ce | -10.3895 | -61.231 | 2026-09-29 12:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| ad971620-ca3a-356d-a625-ba64199c8b91 | -18.095 | -44.3793 | 2026-09-29 12:20:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 146.8 |
| acea3a51-8af5-3527-a19e-7b37c2b6954c | -11.4302 | -43.4596 | 2026-09-29 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 3bc935c3-3d1d-3cb0-ac50-7a7bfb47da71 | -9.4702 | -45.8023 | 2026-09-29 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 3cd6622a-8f8b-37ce-83d9-77b0c09b7ef4 | -12.7614 | -47.2656 | 2026-09-29 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 249.7 |
| 15e277d9-062c-33fe-89ee-3be4804e8894 | -12.6267 | -47.2851 | 2026-09-29 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| c433a8a1-dd1f-3ec4-8924-39b61f63dfc3 | -11.1775 | -44.7832 | 2026-09-29 12:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 0ea0b0f0-d5c7-3020-8ee3-480f7528fac0 | -13.1992 | -48.5603 | 2026-09-29 12:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ff540701-e72c-3917-9108-5464bba51a4e | -11.4307 | -43.4358 | 2026-09-29 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.4 |
| e90d7907-bb6d-3d15-aca7-4d86c05c0537 | -7.5248 | -44.5485 | 2026-09-29 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cfd8662d-a2c5-319c-ab09-97c2b284897a | -14.4644 | -47.0447 | 2026-09-29 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 4e3866c4-b334-3065-b73c-e05c0c83d64e | -8.9823 | -44.1633 | 2026-09-29 12:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| aec6bf4f-188b-3dd6-baaa-41e5738d8185 | -14.1309 | -46.2801 | 2026-09-29 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 5e17cfb3-8036-3707-a343-4b01985e88e1 | -11.1775 | -44.7832 | 2026-09-29 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 3e0b9946-c609-3d10-bdc0-53fcf0c3251e | -11.4307 | -43.4358 | 2026-09-29 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| afe0df9e-3217-31e8-8f62-9bbbfdbff9aa | -11.4302 | -43.4596 | 2026-09-29 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| d81383a2-78d8-33c7-8605-29de83972849 | -11.1771 | -44.8064 | 2026-09-29 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 7c1ee424-0916-35b3-97cb-08af05c4731b | -10.3895 | -61.231 | 2026-09-29 12:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 123.5 |
| c1b3d48e-fc9a-35e4-9562-0e20dc5fae6d | -10.3894 | -61.2502 | 2026-09-29 12:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 204.7 |
| 0b30fc8c-618e-3caa-a190-62dcc3dfb17c | -14.1115 | -46.2834 | 2026-09-29 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 007b84b4-f5d1-3806-9759-ef6bb306727c | -12.7036 | -47.274 | 2026-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 0e5ee068-f345-33f5-8437-7b26572fc762 | -12.6463 | -47.2598 | 2026-09-29 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 00c512a7-4845-3af7-ab95-e40f56bc0577 | -9.1337 | -49.9656 | 2026-09-29 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 68872b2b-ac9d-3302-8c5d-8f5fcfa14be7 | -12.7417 | -47.2909 | 2026-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| da76edbd-ea45-306f-ad17-ba360de8e9ad | -9.0977 | -46.8088 | 2026-09-29 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 636d8b9e-a40f-34c7-8112-d5eba50a8a7b | -12.7421 | -47.2684 | 2026-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| f88525ec-701f-31c6-a85d-49685bf26e3b | -13.1992 | -48.5603 | 2026-09-29 12:30:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8b24d135-ec1e-3c46-9b7a-3e816a5db2b6 | -14.5362 | -48.2927 | 2026-09-29 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| bd22aaaf-cb32-361f-878b-a572c8992a9b | -12.6271 | -47.2626 | 2026-09-29 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 4be6a18f-447b-3942-bdab-3e8b9b8008c7 | -12.704 | -47.2515 | 2026-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 3b675cdc-5dfd-31d8-aa86-9280e07ccd35 | -18.1144 | -44.3988 | 2026-09-29 12:30:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 386c547e-2cac-32d9-a5c9-5569162bd57d | -7.064 | -42.0648 | 2026-09-29 12:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| f2f6a965-9d4e-3f4a-916a-7f028037be64 | -12.761 | -47.2881 | 2026-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c690626e-76bc-37bd-aa5e-faae52e4787a | -7.506 | -44.5503 | 2026-09-29 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| aef8e320-c881-3d4d-92d0-eb83565b680c | -14.4644 | -47.0447 | 2026-09-29 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 4c70d10a-2ee1-3e4c-9cd0-c8a35519ec92 | -8.9823 | -44.1633 | 2026-09-29 12:30:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 35df1b42-a581-3da9-a572-b314477faca3 | -8.7453 | -44.9045 | 2026-09-29 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 455a2649-e99b-31de-8fa3-b0c9554ccd6d | -11.8675 | -50.4718 | 2026-09-29 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2fc3ad24-451c-325a-af80-f66f037363c8 | -11.4302 | -43.4596 | 2026-09-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 432692e5-8154-3156-9940-5ff266c8222b | -13.1992 | -48.5603 | 2026-09-29 12:40:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| b791fbb4-03b1-36cd-8824-4c07bf9387d0 | -12.704 | -47.2515 | 2026-09-29 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 013ddec3-a782-3e43-a102-eddb706c3232 | -10.2843 | -44.6274 | 2026-09-29 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 665b2a72-9a79-3700-89de-c93785352713 | -10.3895 | -61.231 | 2026-09-29 12:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| dfea46f4-cfdf-3501-b4ea-f619e8da157f | -11.1907 | -45.1274 | 2026-09-29 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 5fb3aeb4-90e3-36bb-8e2a-14f3df800c5d | -12.6848 | -47.2542 | 2026-09-29 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 2703fdce-8424-363a-a4d3-57806ffdcd7e | -9.4702 | -45.8023 | 2026-09-29 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 19eb8fd4-0e33-3f22-8883-38d888d4af26 | -11.4307 | -43.4358 | 2026-09-29 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 38b423b7-b9ac-3944-bce7-69f4dcebc446 | -11.1775 | -44.7832 | 2026-09-29 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| a872b93a-1105-3c46-90bd-bcd4d98e242c | -14.1115 | -46.2834 | 2026-09-29 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 132.4 |
| f055365b-0d70-3cc0-8c63-6e381c8f6403 | -12.7421 | -47.2684 | 2026-09-29 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| c0200900-d210-32ac-bcc3-9e015479c205 | -14.4644 | -47.0447 | 2026-09-29 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7fdaed60-b364-317d-b821-6ee5a568c100 | -11.1771 | -44.8064 | 2026-09-29 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| b519c5c5-b06a-3156-a974-6df344573ace | -10.3894 | -61.2502 | 2026-09-29 12:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 218.1 |
| e6c51ec5-346c-3b19-8226-c238169e477e | -12.761 | -47.2881 | 2026-09-29 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| abf838cd-7039-383e-b9be-ec128eb19661 | -14.1309 | -46.2801 | 2026-09-29 12:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 023b6556-ea1a-34b6-a6bc-da3af2deba45 | -7.064 | -42.0648 | 2026-09-29 12:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 21238596-e8fb-38d0-b9e3-65aef5d619b0 | -11.8678 | -50.4504 | 2026-09-29 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b05fd050-834b-31f7-9281-4fc9031046e1 | -7.506 | -44.5503 | 2026-09-29 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 275a63f4-1e38-31f7-b29f-5158e384cfbe | -18.1151 | -44.3745 | 2026-09-29 12:50:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 042560de-ae25-3389-b2a8-15b0078d8f37 | -12.6074 | -47.2878 | 2026-09-29 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| c779e1f3-855c-362a-be8a-5b39a25d1bef | -11.1583 | -44.7859 | 2026-09-29 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 18695db4-06c4-3857-a5e9-7979fda10aad | -13.1799 | -48.5631 | 2026-09-29 12:50:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 50d40ecd-3e0d-3ca8-bbb6-654f42419019 | -11.1771 | -44.8064 | 2026-09-29 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 324.3 |
| 6c9d62e5-47bc-3b93-9f99-1454c1585f8c | -10.3895 | -61.231 | 2026-09-29 12:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| de20b93a-8879-3fcd-b60a-13a9df60fef8 | -12.7417 | -47.2909 | 2026-09-29 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |


[Clique aqui para ver as próximas entradas](README75.md)
