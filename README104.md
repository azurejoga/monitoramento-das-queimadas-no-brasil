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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5240c03-b958-35f5-97ec-21e235c645cb | -6.2275 | -60.018 | 2025-08-26 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 2b8286a7-1ee3-3b94-a1ef-656a3b3bd60a | -15.0244 | -48.1689 | 2025-08-26 13:00:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| be90e568-8068-387a-856a-ffa3d63c4fb6 | -10.3087 | -46.762 | 2025-08-26 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 290.7 |
| 3ab2e22c-17d8-36c3-b411-a6476dc5d996 | -10.7212 | -47.0918 | 2025-08-26 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 1a04a97a-97f0-3806-bcfa-44ad5a3ecb60 | -12.6741 | -47.8589 | 2025-08-26 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 2729d334-c6f6-36e2-9f71-447a9c398265 | -6.8229 | -58.956 | 2025-08-26 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| c2673675-d70a-3194-a424-51502116191d | -6.2459 | -60.0174 | 2025-08-26 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 246.7 |
| b8714ecf-420b-3390-9576-ff3592b72d1a | -12.7651 | -48.1348 | 2025-08-26 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 59905068-c1b3-3e81-a359-2b8db3f13859 | -6.8228 | -58.9753 | 2025-08-26 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7b12ddbb-8f7d-3958-930e-21bc88e5e556 | -11.2014 | -50.5685 | 2025-08-26 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 2932f4db-dfb4-3d9d-9505-70d9de7452f4 | -10.7209 | -47.1142 | 2025-08-26 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| a5b3d995-9262-30c3-93fb-ae8816f0eb85 | -6.8062 | -45.0019 | 2025-08-26 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 254987fd-4960-3735-a333-1be4369a2009 | -6.246 | -59.9982 | 2025-08-26 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c6225042-be04-37be-be65-70bb8ac3ddfb | -10.76 | -47.0424 | 2025-08-26 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ca0bf759-3f5e-33a8-8cd6-779ae22540ed | -8.0841 | -44.997 | 2025-08-26 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 6d98f33e-8cfb-3136-8ca8-3e7d3645985b | -9.1904 | -59.5201 | 2025-08-26 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9297294f-a75f-32b8-b374-6ddc277da63a | -11.9129 | -47.6074 | 2025-08-26 13:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 396c5af7-b5c4-393d-b584-5c8bab889ee3 | -10.3087 | -46.762 | 2025-08-26 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 7ad54275-a79c-36c2-9310-3b1945fa7cc9 | -6.7819 | -59.6711 | 2025-08-26 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4b15e4ae-890e-35ea-9a28-cebfa0385d3b | -6.8229 | -58.956 | 2025-08-26 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| d7bd4073-6bef-31d1-ad24-d892f31788a1 | -6.246 | -59.9982 | 2025-08-26 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e2ee30e5-8846-3240-aafc-bcc44079937a | -6.7635 | -59.6718 | 2025-08-26 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b6eace1f-db8d-33a8-a8f7-b62b5b69bb6b | -9.1717 | -59.5405 | 2025-08-26 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 72c11c23-8b28-370b-bf23-3c5677e49e6b | -8.2524 | -45.094 | 2025-08-26 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8f9da2e7-9e28-382c-b52d-7e3f3bd40a26 | -9.1718 | -59.5211 | 2025-08-26 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 622c4a61-7e5b-36a2-890d-269f294ae0d8 | -10.797 | -47.1048 | 2025-08-26 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f7d2debe-daca-3877-847c-30aca2c9a0b0 | -16.6224 | -49.3708 | 2025-08-26 13:10:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 7199292c-67dd-3ffb-9866-4dba7813d608 | -8.2522 | -45.1168 | 2025-08-26 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f63c8738-4f1e-3fbe-be0b-ddd13f85188c | -9.1375 | -45.2493 | 2025-08-26 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 2190e375-d138-3569-9e5c-401736fbc236 | -7.7433 | -45.1673 | 2025-08-26 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| aa5f5a3f-abf2-3be2-bd77-ea96e627693c | -9.1529 | -59.5609 | 2025-08-26 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5d43d5f7-ec65-399f-b8bb-9436a0202120 | -12.8123 | -49.8599 | 2025-08-26 13:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| dff221b5-d102-35cf-8bb4-de690111c40a | -6.2458 | -60.0365 | 2025-08-26 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a330e853-d79a-3348-9f6c-c2321175289c | -9.1903 | -59.5395 | 2025-08-26 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ac5ed3a4-6e6f-3bd1-b3a5-ccad9d7d6322 | -11.2014 | -50.5685 | 2025-08-26 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 36740f90-c9af-37f5-90bd-a58230cadb6a | -6.8062 | -45.0019 | 2025-08-26 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2c895fd2-80f0-3173-a6d1-6bc6f6200f41 | -6.8228 | -58.9753 | 2025-08-26 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 82ae397c-1eb2-347e-bd46-317661caf576 | -12.7932 | -49.8624 | 2025-08-26 13:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 4c1b888b-9035-3759-ac77-ae73641f60a3 | -10.7787 | -47.0624 | 2025-08-26 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| f620e43a-c2d8-302a-a4b3-982d098d507b | -6.2459 | -60.0174 | 2025-08-26 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 237.1 |
| e396d6cd-69b1-39f9-8382-25d1ac0ba9e8 | -6.8064 | -44.9791 | 2025-08-26 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 3b93f89e-782b-38b4-b8f0-3e39ac0ee836 | -9.1375 | -45.2493 | 2025-08-26 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 8aae0ffa-81a3-3c43-87f7-acbb65768f69 | -12.6737 | -47.8812 | 2025-08-26 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 5079f12e-13ad-327d-af7a-4963ae110913 | -6.7819 | -59.6711 | 2025-08-26 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b6b607f1-0f09-3bb6-bf68-7e96c78da22a | -9.1903 | -59.5395 | 2025-08-26 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 2b5c0836-21e6-3597-96cb-9227d934991d | -6.2275 | -60.018 | 2025-08-26 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7c45b1ea-60a1-3e22-88fe-6c890a4231db | -12.7932 | -49.8624 | 2025-08-26 13:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 6f77ceb8-1597-351c-af67-32b84759151a | -12.7455 | -48.1597 | 2025-08-26 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a9db6dfd-22b8-324c-aad8-f3ba7aee9cb4 | -13.423 | -46.873 | 2025-08-26 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a7abd2d5-d8fe-3f34-990b-9b34955aeb80 | -10.7787 | -47.0624 | 2025-08-26 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 45c4c2d9-ca89-3e3b-ae1b-f1b9af4ce698 | -9.1564 | -45.2472 | 2025-08-26 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a27ba18e-4cf3-351b-80bf-462474677a86 | -6.8229 | -58.956 | 2025-08-26 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.1 |
| b3f01a30-bd16-3d80-8edb-8215e1672142 | -8.0755 | -47.3082 | 2025-08-26 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| fe586d61-427b-378f-92f1-db567b6aae83 | -12.8123 | -49.8599 | 2025-08-26 13:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| f43436e6-1a37-3a89-bb2e-fb137a27321e | -8.2524 | -45.094 | 2025-08-26 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e40702ea-a23b-3995-9ca9-1527628d26b3 | -11.6277 | -46.3899 | 2025-08-26 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 0eefd656-cb7b-3fc0-b4e6-fc046bf5ccd8 | -12.6741 | -47.8589 | 2025-08-26 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 4c73915b-e228-3c45-a668-df485bfb6e98 | -6.8413 | -58.9552 | 2025-08-26 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8aa52c49-1613-3d5c-a9b3-4f7182d2caef | -11.559 | -52.117 | 2025-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| e305cd84-5edb-3cc9-897e-303d49876b57 | -11.5017 | -52.1439 | 2025-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c54e7d7f-cfb1-36ef-83c5-e27600328b28 | -6.8228 | -58.9753 | 2025-08-26 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 98c8682d-4498-3879-8a6b-6936f6ef3e36 | -6.8062 | -45.0019 | 2025-08-26 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 0edca05d-530b-3db0-b1c4-401f730a4a3c | -12.7451 | -48.1819 | 2025-08-26 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 0b6b2a21-2b3b-32d1-83de-02b155e5b2e6 | -6.246 | -59.9982 | 2025-08-26 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 49e13c92-06f5-3822-900c-c0e56e18e946 | -12.4933 | -47.2369 | 2025-08-26 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 07cd8a1c-3b79-3933-beb4-a321e3dcf0df | -11.5779 | -52.115 | 2025-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 711f5b41-bd57-33d2-9b34-f50a93de2798 | -9.1904 | -59.5201 | 2025-08-26 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 496747a0-8eeb-3113-9716-6ed9221ad790 | -11.54 | -52.119 | 2025-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9c67aad5-acdf-370a-b0f3-b513ee1fd55d | -9.1717 | -59.5405 | 2025-08-26 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 3b143cbd-9017-32a5-8999-36790a446cfb | -11.6082 | -46.4152 | 2025-08-26 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 2d81142a-b970-3dd5-add2-730a815da28f | -11.521 | -52.1209 | 2025-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| a269eb16-9a32-3a9d-ab60-ce001edc9081 | -6.7635 | -59.6718 | 2025-08-26 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| f0bc8c27-a547-37e5-bd9a-89d74f8660e3 | -6.2459 | -60.0174 | 2025-08-26 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 243.1 |
| 3c511085-198c-3393-8846-0eec84b362a5 | -11.6273 | -46.4126 | 2025-08-26 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 346.2 |
| a95b9e8c-b781-3389-9341-3cd491f3fd8d | -6.2458 | -60.0365 | 2025-08-26 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5edb49bf-9231-3ea4-8905-38a573f91005 | -11.6086 | -46.3926 | 2025-08-26 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 189.0 |
| d4598b15-7a88-3a4a-922a-631ce7ea5a8b | -11.6308 | -46.2083 | 2025-08-26 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b3667b64-844f-3095-8048-4cc331b38896 | -11.502 | -52.1229 | 2025-08-26 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 749018ce-f1bd-3b05-9861-b8d1aa6f5992 | -12.7455 | -48.1597 | 2025-08-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e19a46ca-193c-31c7-b7f3-4573e9c1fa5e | -6.246 | -59.9982 | 2025-08-26 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 73f6abb6-71df-3e88-8fc2-4085a1ae026d | -6.8228 | -58.9753 | 2025-08-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 7785d3ba-e6bd-3f39-ae2f-6b65d45b3c9c | -11.6351 | -44.8561 | 2025-08-26 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 63251d1e-db63-3bc2-b320-dfdcc8e8117c | -10.6822 | -47.1635 | 2025-08-26 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 7c7b1d6e-5904-3bf9-bd1e-0f9d8a5c460a | -12.952 | -46.3104 | 2025-08-26 13:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 26af00f9-887f-365c-a11d-be07d189f6f6 | -12.6741 | -47.8589 | 2025-08-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 2f59ec35-de2c-3eaf-9cc7-f7225c62c986 | -11.6277 | -46.3899 | 2025-08-26 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| fb9e43d5-03c5-38aa-9576-8ebf806f2cbb | -13.394 | -51.7808 | 2025-08-26 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 55001163-53af-3880-93d5-1709a55fc790 | -8.0841 | -44.997 | 2025-08-26 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| eede3764-0075-34bf-812e-9fc8d7886e96 | -15.1101 | -48.7352 | 2025-08-26 13:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 8301faed-6475-3073-86ba-c6ad7f56d1cd | -6.2275 | -60.018 | 2025-08-26 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 3e115da5-8c29-3881-945f-c8609542cdb3 | -6.8064 | -44.9791 | 2025-08-26 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 47b171a5-a9af-3592-af48-adf44cdbbd60 | -11.5779 | -52.115 | 2025-08-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 8fbca39e-ce18-3c2c-8087-b41d952455ba | -6.7819 | -59.6711 | 2025-08-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 4f127800-5505-3f90-a315-db1723d9cf7b | -8.2522 | -45.1168 | 2025-08-26 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8c9d1258-5d93-350b-b351-1bdc949ad036 | -6.7635 | -59.6718 | 2025-08-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| e21f58f7-fd63-3b0d-9c66-466916801be7 | -11.521 | -52.1209 | 2025-08-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 08541c2a-005d-3baa-baf6-93a62286bee1 | -6.2458 | -60.0365 | 2025-08-26 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 334c65ba-b592-3a71-bba3-3772d38c656a | -16.6224 | -49.3708 | 2025-08-26 13:30:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 674d370a-5c6d-388c-a4f6-876fc804133e | -11.6308 | -46.2083 | 2025-08-26 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 175.3 |
| d7f33e6b-22b5-3617-9fdf-8840c3a3a610 | -6.1377 | -44.3711 | 2025-08-26 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |


[Clique aqui para ver as próximas entradas](README105.md)
