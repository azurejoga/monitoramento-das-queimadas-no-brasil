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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7357a7-cbd2-3a08-81a9-e0aece627de0 | -10.13108 | -58.21576 | 2025-07-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f92408b1-50f7-3ca6-877d-d3ebc23be880 | -9.52097 | -45.44113 | 2025-07-03 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 524da073-d1e6-3b53-829a-4daeb5d92ed7 | -10.08411 | -47.99275 | 2025-07-03 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5a0083e-735e-33f7-b166-5b6d88767c19 | -10.92747 | -49.27782 | 2025-07-03 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12d3aedc-7552-3788-9f9e-fdb768388504 | -9.73027 | -61.40216 | 2025-07-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f74ad045-7d7d-3005-80c3-621fe96ff2e7 | -9.17286 | -48.7761 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 288c13eb-5000-3e17-bf7f-acbc23acddce | -12.57065 | -48.88418 | 2025-07-03 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdee0619-c648-30d0-952e-e507e902859f | -10.67922 | -49.4923 | 2025-07-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1ec507a-3eb9-346c-8cc9-0ffc555bb95c | -13.38756 | -47.84155 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a6e558a-c53c-3a75-96fc-f21569f5e9a4 | -11.65062 | -44.59965 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| feab24e1-b75a-37b6-a0a4-5682f80bf14f | -9.51552 | -45.44024 | 2025-07-03 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcaa5e39-12d1-3eb2-b871-e69077b04775 | -11.14191 | -43.32935 | 2025-07-03 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a1f54151-9b49-327e-97d8-c40024bef181 | -10.88245 | -56.45016 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1f2285f-0aa2-3a74-b7be-d635c0ffcb74 | -11.50378 | -48.95652 | 2025-07-03 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a87b4161-a73f-37ab-8067-590f475cdd7d | -11.40891 | -55.36375 | 2025-07-03 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45ba3dfb-5408-3b63-9f87-20860ac3f2c0 | -11.65866 | -44.58267 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f512ac79-5abd-3768-9473-c10bda496066 | -10.66365 | -49.4498 | 2025-07-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84df4a87-2a81-301a-ae66-c217e665b12d | -11.1441 | -43.3268 | 2025-07-03 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 691531c9-1193-3d0e-a2a9-acce400942de | -11.54334 | -47.31145 | 2025-07-03 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e99547ad-2d8f-3099-83ec-9c55737ba78a | -9.17346 | -48.77194 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 995dcc1b-56b8-3e17-9797-97909b2512d8 | -9.62938 | -61.46217 | 2025-07-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2d63c2db-a652-3df7-b19b-860cecd28e10 | -11.79437 | -48.08327 | 2025-07-03 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a1fecbd-10ce-398d-8054-f2087e46066b | -9.53351 | -58.19492 | 2025-07-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 580c2a13-6432-3395-b540-5bd8b95884b5 | -12.0495 | -62.99069 | 2025-07-03 04:57:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c226397f-46fc-3967-8fc8-9487c1251f1c | -11.63523 | -48.07699 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 767b0f6c-587a-3364-9c12-2b9ed36c0248 | -10.6516 | -44.48512 | 2025-07-03 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 860d6b66-44df-3bcf-a0aa-a49fcc46750b | -14.15272 | -45.22352 | 2025-07-03 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48e0bcde-873e-373d-a089-a8425e61a450 | -11.65114 | -44.59521 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e6c8849e-8a15-3ec0-9858-12928ea26f07 | -8.4334 | -49.20355 | 2025-07-03 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 488bb300-c49b-3b48-8756-2f16f96bab38 | -13.40701 | -47.80542 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 886c19b0-d1de-3b62-a64b-ced00aec7d59 | -11.65658 | -44.60039 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6321d89f-443e-3431-8995-dc3734ba9412 | -12.57002 | -48.88891 | 2025-07-03 04:57:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e67189de-047d-310a-b444-d1fa348f657b | -10.88971 | -56.44769 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fca3cd2b-f172-3db4-af61-079cbbbe1972 | -11.53837 | -47.31084 | 2025-07-03 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a83ce11-74cc-3ddd-b460-8d170b84e122 | -9.87189 | -48.46 | 2025-07-03 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8427c589-e37a-3795-802d-f8ab6c996384 | -11.84453 | -43.80252 | 2025-07-03 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48cd7ff4-ce74-3b50-ade1-117a8727523b | -13.43099 | -47.81388 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e961f5ef-2c9d-35ee-947f-c7e6c9705e07 | -12.11305 | -54.58945 | 2025-07-03 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e0de1f7-cbb9-3700-9b57-c3dc924485f7 | -11.65861 | -44.60406 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 50a2e208-542d-3da8-bf21-521062b8a8d6 | -11.14127 | -43.33464 | 2025-07-03 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 405e2348-a6b9-338b-bf65-b622872ef6bd | -9.17091 | -48.77058 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fb2422f-e0cf-37f6-8b78-cdb808ce38f6 | -9.03981 | -49.72069 | 2025-07-03 04:57:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2618d721-3d7e-371f-afbb-2da22fc325fa | -12.63188 | -54.21335 | 2025-07-03 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d1e5346-e4a3-327f-aea8-70a5e1ffa939 | -9.51322 | -65.58848 | 2025-07-03 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a646462-1dd5-3903-9b00-a051e6d3506d | -10.3671 | -57.49791 | 2025-07-03 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58177476-c8d2-3759-a835-9b8cf6bbc7b9 | -8.86731 | -49.03746 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cab90f92-1248-3d82-bece-79ab208901f5 | -13.39031 | -47.84139 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc45ee43-30c1-397c-a973-398aeabf781b | -9.7957 | -47.74461 | 2025-07-03 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40dfeacf-cfb2-328d-a508-1f455accbc78 | -10.88735 | -54.04938 | 2025-07-03 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 13118626-e646-35e6-83cc-d1000299f593 | -12.11232 | -44.98862 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73e4f1b5-914e-3631-8d82-3cb9365c4c3b | -10.88914 | -56.45127 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c15bc81c-81ea-33f8-9567-654bfdb18028 | -11.6385 | -48.07504 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9851ccae-e9b9-32e4-8076-9efab7ae2a26 | -8.43812 | -49.20038 | 2025-07-03 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cf8a42a-220d-3844-b94c-b215ffd306b8 | -9.63301 | -61.46732 | 2025-07-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 47006242-0549-3b25-94fb-5e163bdd3c59 | -10.1011 | -58.22882 | 2025-07-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1764af2-f60a-3dd1-8995-6de73de4ebdb | -11.65376 | -44.59452 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c0cf213b-57bb-3385-aef9-496cc1253b7c | -12.42336 | -50.03124 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22ae4915-cb80-3125-9e00-5fc4948b9a32 | -10.29771 | -57.13213 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d63a7d8e-f86a-3276-a50a-55a3283dca58 | -7.6074 | -45.74401 | 2025-07-03 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d25b5d01-8772-30b8-b9af-329817e80138 | -11.31447 | -46.20858 | 2025-07-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4edb045-9f6e-3a21-b025-22bd123d354b | -10.65941 | -49.44921 | 2025-07-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1361e6f9-187f-38ef-bd6b-fedbd63b262c | -13.44883 | -47.83118 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59ed36c8-594f-3cc6-a4bf-6ccf35b903f9 | -12.1664 | -45.53219 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1eb1645-a90d-3ae4-bcda-8e11e253ccc0 | -10.16632 | -52.62132 | 2025-07-03 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5caa5d15-1e1c-38af-9be7-41a486a7bb59 | -10.81466 | -56.95348 | 2025-07-03 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a232af66-53b0-3bb8-a810-535806b3af3b | -12.11207 | -44.98453 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5b199b9-80e5-3902-8072-bc35c8d4a208 | -11.63782 | -48.08008 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 62f7bcf8-21c3-36e3-aa2a-86e8d8ba0986 | -12.11285 | -44.9842 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bce73bd-1c88-39e2-a559-c56edb7b5a61 | -11.66357 | -44.5923 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 79305c9a-d37f-3c04-bcb4-cddf7f55d6c1 | -11.66082 | -44.58642 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0c834d7-f9ed-3713-902d-d40977ae7273 | -11.66253 | -44.60113 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3607d598-fd08-3ce1-8357-66165aaf02cf | -12.4328 | -50.02459 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5b6d455-2f35-3691-ba28-3049a5ad7689 | -9.03956 | -49.72054 | 2025-07-03 04:57:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bf1819e-8992-3f11-97ba-3cf74d257977 | -12.16077 | -45.53133 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdb6a5f1-ca80-3040-9b88-b40d089ef5d5 | -8.72479 | -64.17177 | 2025-07-03 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48ab44c1-996f-3b84-ae54-7a64e62af1c8 | -10.08477 | -47.98784 | 2025-07-03 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e282a7d-0660-330c-a54f-c5fedca533ac | -10.60708 | -52.78909 | 2025-07-03 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c813fa59-5951-34f2-9e27-53ecd38e2e13 | -13.3919 | -47.84692 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8a16718-4a5d-3aff-8645-e5271da1ec03 | -12.58111 | -56.98536 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a17c71b-2d72-390c-afda-159d1e533b6d | -10.29709 | -57.13587 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7326d5-5b09-3536-92ac-ea077e43f706 | -9.17524 | -48.77122 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 61bcd961-5f9d-3e79-8c6e-9afbdd526f2e | -11.11148 | -48.87131 | 2025-07-03 04:57:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f3a4b3c-21db-3490-88f1-c22f3e321f6f | -9.17034 | -48.77473 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f7b5db3-0f4d-3000-ba30-dc55ec2480cd | -14.15221 | -45.22802 | 2025-07-03 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0660ee55-4746-327c-bf3f-6a7c77d7a343 | -11.47841 | -54.67908 | 2025-07-03 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8443f01-85a7-3fc9-8365-acf2d54168d1 | -13.38967 | -47.84628 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd4f9eb5-a99b-33ae-94b5-329ec5308595 | -10.99421 | -45.19609 | 2025-07-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 724d1868-a85f-305d-8c5c-e7052335398a | -11.63919 | -48.06999 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e76e71dd-874e-3206-98d2-85b30833a98f | -11.1377 | -43.32595 | 2025-07-03 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 89d2714d-9b82-3700-8b0c-1907157bb60f | -11.14254 | -43.32407 | 2025-07-03 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ed497a3f-7e29-3aef-b441-cf0a9d92178c | -7.60696 | -45.74719 | 2025-07-03 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2eff06e-2770-35f9-8458-9723986e28fb | -12.58052 | -56.98899 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01819689-f30b-3a56-8678-efa964180319 | -10.68344 | -49.49285 | 2025-07-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20d32384-82ee-308d-9256-2830377de4bc | -11.47404 | -47.92598 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7cc789a-d502-38bc-b651-7ac5ba4b66b1 | -11.78441 | -57.24561 | 2025-07-03 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb0b6804-491b-32d7-ad95-4f374af04bf8 | -10.0894 | -47.98855 | 2025-07-03 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b8c0111-2dd9-3b4f-83cf-bd1e2237ed75 | -12.63133 | -54.21702 | 2025-07-03 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 506365ac-37fa-37fd-9e73-e41a889495ca | -13.40632 | -47.81095 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67278c61-65d4-3c15-93cc-9744e0e9fc44 | -12.42862 | -50.02403 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fc076f9-f69e-36c4-b2e5-4fbaa9b7cc70 | -9.24705 | -58.74765 | 2025-07-03 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
