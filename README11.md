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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed66dddc-925d-3738-ab6c-abfa8dc49838 | -12.8432 | -47.38806 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 192d0061-05fc-3a9c-a874-0d2e0f9245ca | -10.63572 | -48.0899 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d76353d-528e-322d-89cd-593a9c6478fa | -12.37836 | -49.99579 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8780b69c-8cff-34ce-8ce0-181525a2daeb | -10.65663 | -49.47655 | 2025-05-24 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07b9ee98-8022-31b1-ad8d-cfe8a92d090d | -10.94709 | -48.1486 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65bd836b-a261-397d-85f6-5292aa8873f5 | -12.39577 | -49.9789 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ac0ff5a-fbe6-331b-99c7-8323ccefe043 | -11.42299 | -54.30488 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41a43ea3-93cb-3b89-ae75-dc1a7ba3a912 | -10.46709 | -47.94444 | 2025-05-24 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63f7d63e-b46d-3eeb-8ed0-a6a172817fdd | -14.23156 | -44.63469 | 2025-05-24 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3edc9fc-87c8-3d70-b34f-6f4205cca89b | -14.03144 | -55.14101 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7d9f369-e5de-370a-afd8-49e987b953e9 | -17.26805 | -48.62313 | 2025-05-24 04:08:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be7820bb-edbd-3739-8e31-96d5ab64a8e8 | -12.13884 | -54.66327 | 2025-05-24 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45a8768a-1b25-371b-85cc-9a69702672b0 | -14.03246 | -55.13612 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6f141b9-1cf8-3f5e-b8b2-d76712f6cd04 | -14.01396 | -55.13207 | 2025-05-24 04:08:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3c02e85-ed03-33f0-a9fe-0e49730babd3 | -13.90186 | -43.81511 | 2025-05-24 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82c37289-d63f-3138-8b3b-fbf269fd34ed | -12.84116 | -47.39157 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80d9f3f9-1065-35b2-92c1-2635d5d40b08 | -14.2288 | -44.63045 | 2025-05-24 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ddb2a36-f726-357d-8628-d6c3c6c2d919 | -10.72321 | -45.04042 | 2025-05-24 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2f41f69-4fd8-3bc3-8371-533c1c260cdd | -12.3811 | -49.98124 | 2025-05-24 04:08:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f408b0e4-7590-336d-a4c8-994e3ac45940 | -10.72702 | -52.4724 | 2025-05-24 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fb14132-a3d7-3d6a-b67e-a83f3bd935e4 | -12.83262 | -47.39503 | 2025-05-24 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed141b8e-8861-3649-8f4c-913400d85666 | -11.7549 | -54.2337 | 2025-05-24 04:08:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e5100e37-a9d3-360b-b515-63f2220e7ccc | -8.0889 | -43.1196 | 2025-05-24 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| a12c390b-48b2-3c4b-a246-e02e4c4a6aca | -8.07 | -43.1216 | 2025-05-24 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 9825da16-eb5c-3ff5-aa90-eaff32d6b424 | -6.2226 | -43.3459 | 2025-05-24 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 08df3831-5040-329d-8242-ef8a8a0c5e3d | -19.88038 | -54.36501 | 2025-05-24 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea3c511b-0ae4-3f5a-90a0-41f83d00027b | -21.59989 | -56.04237 | 2025-05-24 04:10:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c83ed56-2363-38b7-a1f0-2e8b62b330f7 | -19.15434 | -41.56835 | 2025-05-24 04:10:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e26ffba-c61a-3b2b-9bbb-c6e535bfea7d | -19.66647 | -49.90019 | 2025-05-24 04:10:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 595ba7ff-d02c-3185-ab51-0d42a1008e9e | -21.12992 | -47.80008 | 2025-05-24 04:10:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bc3cf2e-6784-31ac-8cbb-68f346f65d92 | -17.3382 | -51.90636 | 2025-05-24 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0827ac18-2df4-3d46-adfc-5eedce216bea | -19.87154 | -54.36246 | 2025-05-24 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d7fe8d-f6f7-3309-a7a8-74534d7ed0f7 | -19.97113 | -44.21502 | 2025-05-24 04:10:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2ec2d499-0230-3da1-859c-fabf538c062b | -19.87077 | -54.36609 | 2025-05-24 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15b54ac7-caff-307b-84c2-21ae6b4c89b6 | -20.94043 | -56.59759 | 2025-05-24 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4da46d6f-ae80-3733-b716-b37e134f8e08 | -22.71402 | -46.35266 | 2025-05-24 04:10:00 | NOAA-20 | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a1ef4954-99f7-39bc-a311-d32669288f50 | -23.54859 | -47.63412 | 2025-05-24 04:10:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b1fbe10-bbd2-3c57-a563-0634196149a3 | -20.41551 | -43.55136 | 2025-05-24 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6868f69c-e567-308a-9bd7-5b5fcf597d89 | -19.4549 | -45.30832 | 2025-05-24 04:10:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9395a69-5ca4-3135-afa0-91b7f98b60a9 | -19.76043 | -40.87524 | 2025-05-24 04:10:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 293931be-cc6e-374f-bd91-22010c4a108c | -20.94153 | -56.59284 | 2025-05-24 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 66c2e332-cc02-39fc-afac-959ec48b3fa5 | -24.24186 | -50.73891 | 2025-05-24 04:10:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 96287347-c684-3fb3-b3a1-4af798efd7cc | -21.21993 | -48.61399 | 2025-05-24 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 36105628-f776-33f8-a4c9-ca13eceddc9d | -22.98512 | -47.03928 | 2025-05-24 04:10:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 769c4403-bb7c-3bd9-8fb2-3244b38372b7 | -21.62465 | -43.46423 | 2025-05-24 04:10:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3b8b896f-fcbc-3618-9439-308a4ac480ad | -19.87959 | -54.36865 | 2025-05-24 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9267ff64-0a99-34d7-8a8a-b75cae13bf06 | -20.54897 | -44.92565 | 2025-05-24 04:10:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e23153af-024d-3425-a3c4-b3fa82ca6f6a | -20.44507 | -46.37435 | 2025-05-24 04:10:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24b4d854-8163-30b3-82c2-47f9c8aa5939 | -18.64219 | -53.31635 | 2025-05-24 04:10:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0a419a8-fc4a-3346-955b-08cf02725b00 | -21.957 | -56.07739 | 2025-05-24 04:10:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17189e0c-a4c4-357a-86e7-d9b913c38c92 | -23.33892 | -46.77324 | 2025-05-24 04:10:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c2b6d9c6-4670-3284-a47e-218cd26d0ae3 | -20.40204 | -46.33534 | 2025-05-24 04:10:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bdf8743-7a55-33fb-a42d-5646fc392274 | -17.33792 | -51.90864 | 2025-05-24 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9403030-c3b5-38ab-b734-74bd3ddef62d | -20.9474 | -56.59441 | 2025-05-24 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 585f8b88-ddc9-32e6-9601-718b95949af6 | -19.87608 | -54.36716 | 2025-05-24 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff2edf57-4e95-3565-8558-0b8c17306e89 | -21.59895 | -56.04662 | 2025-05-24 04:10:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c90a9b3f-d348-3f5f-9dde-3bf7effcffc6 | -21.21628 | -48.61325 | 2025-05-24 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 720fd485-4cff-3a78-9b0d-0d6cca3576d9 | -20.85134 | -53.74857 | 2025-05-24 04:10:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd3bec9d-d0c7-34d8-8694-452b0b2725ad | -22.53848 | -48.81155 | 2025-05-24 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0ab5d13-2f43-31ee-a50e-055ee3808443 | -19.79307 | -53.83504 | 2025-05-24 04:10:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed8c033b-2361-328b-9522-c7f8aff82977 | -17.15441 | -54.00385 | 2025-05-24 04:10:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd7f4c88-7720-36fd-bf1a-c1d67aa40f11 | -19.60364 | -45.01685 | 2025-05-24 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 029d460d-8c6e-30f7-8a4f-e58811010f59 | -20.99484 | -51.79346 | 2025-05-24 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 58d098c8-cf47-3cf2-bf68-c68cd91055a5 | -19.79238 | -53.83826 | 2025-05-24 04:10:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f37940f3-a2a8-3d5b-bfa5-60c1a0408520 | -21.6067 | -56.04658 | 2025-05-24 04:10:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b30ab0e2-18b9-33f4-9b97-21200c2ae7be | -19.59974 | -45.01992 | 2025-05-24 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 85e33228-f286-395c-9062-b4208d6a760c | -21.60202 | -56.04099 | 2025-05-24 04:10:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce44f043-2a3a-36b9-9648-4d920058f058 | -19.97261 | -47.18682 | 2025-05-24 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78714822-6394-3fb5-a671-3b3f28c8f5b7 | -20.85068 | -53.75172 | 2025-05-24 04:10:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10ea06bd-da34-3d43-bcdd-2c738713e4bb | -18.59583 | -46.55149 | 2025-05-24 04:10:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b840d2bc-285d-313c-8e13-75c8367d824c | -18.81537 | -46.43655 | 2025-05-24 04:10:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7532b550-19de-3c0c-923e-5e4e7a74dfde | -19.51357 | -44.27656 | 2025-05-24 04:10:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b31e3435-9639-3afa-82f4-996ad796c720 | -21.17721 | -48.90572 | 2025-05-24 04:10:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f98cdc5-fcb5-3d5c-b9d2-8c15026ab7d4 | -20.31083 | -45.58558 | 2025-05-24 04:10:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1243b4e-b964-3447-886f-75b5d2a1ea0b | -20.40268 | -46.3315 | 2025-05-24 04:10:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d7bfc60-cc31-3ad6-ba64-66eb42eac4ba | -19.60032 | -45.01626 | 2025-05-24 04:10:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7144fac-67c0-3b90-8b15-68f5e2167c3e | -18.64282 | -53.3133 | 2025-05-24 04:10:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6984df0b-b339-3814-b831-1c458cb9752d | -21.31905 | -49.4654 | 2025-05-24 04:10:00 | NOAA-20 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 883f5e0a-87c1-39e7-b6f9-a62aee6368c9 | -19.87429 | -54.36753 | 2025-05-24 04:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f9702a-2641-3524-a14d-04d9d50243d1 | -19.94882 | -44.7043 | 2025-05-24 04:10:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0573dd27-4fef-3d11-a52d-21b90945708b | -20.76505 | -46.76895 | 2025-05-24 04:10:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c514ad1d-629d-3064-808b-0c08d7bcf708 | -18.35736 | -55.17546 | 2025-05-24 04:10:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0542f5e6-c47b-3d53-ae09-f28b78ed7aca | -17.15363 | -54.00756 | 2025-05-24 04:10:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 918d75f9-d62e-3d7c-a848-45ed338f7ba3 | -20.94263 | -56.58809 | 2025-05-24 04:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 88bc105a-1c08-3bfe-8a15-d3795e1be93c | -20.27942 | -50.74685 | 2025-05-24 04:10:00 | NOAA-20 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 70f7a71b-5b93-3859-b3c2-d137441a9996 | -21.62408 | -43.4681 | 2025-05-24 04:10:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c9783973-59e7-31b3-b0eb-faaf35dbbac0 | -19.85259 | -48.22802 | 2025-05-24 04:10:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 545b6bfe-bbe7-3492-a87b-714ba495f407 | -21.60105 | -56.04523 | 2025-05-24 04:10:00 | NOAA-20 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 088b568a-951a-3cc3-b5cf-f0dfdf6fc405 | -20.44235 | -46.36984 | 2025-05-24 04:10:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60acf216-231f-3ee3-b7ce-26745b551533 | -20.44572 | -46.37051 | 2025-05-24 04:10:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 76272a4a-9b04-3928-a105-bb0d8e97624e | -29.6101 | -49.94559 | 2025-05-24 04:12:00 | NOAA-20 | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 9f167afd-cad0-3ad4-ae10-add92d2f6b20 | -30.15129 | -52.02499 | 2025-05-24 04:12:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 65899891-793b-327d-b63d-b4634c50216e | -29.61089 | -49.94116 | 2025-05-24 04:12:00 | NOAA-20 | TERRA DE AREIA | RIO GRANDE DO SUL | Brasil | 4321436 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 78c541a0-cd8b-3948-949a-ed792ee2b8f1 | -8.07 | -43.1216 | 2025-05-24 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| d9553b3e-23e2-3442-9969-ae32859ecdca | -6.2226 | -43.3459 | 2025-05-24 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ba667652-d532-3d4c-bd38-9e68247b5641 | -4.3001 | -48.2647 | 2025-05-24 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0aed9ff3-ca16-383a-b249-ee1d43926138 | -8.07 | -43.1216 | 2025-05-24 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| fb71d4fe-3b46-33ff-bef9-61172b700f11 | -8.07 | -43.1216 | 2025-05-24 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 824870ea-4038-32fd-81b2-d6f4b544d230 | -8.07 | -43.1216 | 2025-05-24 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 7fc22805-a8f4-3553-9fa5-12707f53bb1e | -4.29291 | -48.27659 | 2025-05-24 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |


[Clique aqui para ver as próximas entradas](README12.md)
