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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5fef1ef-bac4-365c-9f25-fe50f6bcccef | -7.5292 | -61.3254 | 2025-08-15 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.4 |
| fcc95e48-3668-333a-a731-bf5d3c30c62a | -7.3116 | -60.628 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b77b319a-b39e-3bc6-a87c-71829a5f00ff | -3.4254 | -49.0517 | 2025-08-15 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9d8cca4c-8b45-32c7-8dfc-f01c8cf49d93 | -11.3468 | -55.4124 | 2025-08-15 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 179.6 |
| 9bdb69ba-4592-301f-9f44-9aa70d61f6f2 | -7.9517 | -61.7464 | 2025-08-15 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a0336078-343f-32d4-ba86-014f9ff06e8c | -14.2449 | -44.5661 | 2025-08-15 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9a95a28d-fd5a-328a-8f49-f31886da31f9 | -9.5179 | -60.5461 | 2025-08-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e2342826-fb3c-300b-9c77-b05fe80cdbb2 | -7.0796 | -59.2351 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 53fc1a01-6d5b-3cf5-b972-708e66e661b3 | -11.3655 | -55.431 | 2025-08-15 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| e9cfcbfa-09c5-343f-b986-354454450fea | -9.3875 | -60.5528 | 2025-08-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 626cd0f6-1d66-30a9-a6bd-af215736c6d3 | -7.9516 | -61.7654 | 2025-08-15 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 493cffaf-84b5-3a0a-830a-7c7ba246e12b | -9.5351 | -63.5771 | 2025-08-15 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3a28cd49-f1b0-3006-892f-a45badd39375 | -6.9302 | -59.5497 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 53ed30e1-90b3-3555-84a8-a5f9e490e767 | -11.3466 | -55.4326 | 2025-08-15 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| a4f28cf4-3735-3da7-97d5-3f6dcb3d95c3 | -5.455 | -60.1391 | 2025-08-15 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.6 |
| efbea6c9-2177-333d-8aad-cba6e8d68914 | -6.9303 | -59.5305 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 8902b2a0-38da-3fc4-abfb-28054c51b8c2 | -7.0982 | -59.215 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b80f10c3-3485-3a5d-99f3-13144716accf | -5.762 | -46.6741 | 2025-08-15 00:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5ffce103-57d6-3b68-ada0-a0549e96644a | -7.6104 | -63.4972 | 2025-08-15 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 56693aa7-2d63-33a2-90bb-ae22404106da | -5.455 | -60.12 | 2025-08-15 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 3d3ddc3e-227e-363e-8f3c-f27b591ed5cb | -7.0613 | -59.2165 | 2025-08-15 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 081fe506-6456-3713-a457-4c27fbb6d4fd | -14.2444 | -44.5897 | 2025-08-15 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| fa1c2675-603d-35cb-8bbf-2860f230f52d | -11.3657 | -55.4107 | 2025-08-15 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| b9fd3b23-1ef2-34c5-8747-09d15fa8dd3a | -9.4994 | -60.5278 | 2025-08-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 3db5ea97-857e-33e1-8312-aff21efbeebb | -9.518 | -60.5268 | 2025-08-15 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7896397d-fe07-359b-887f-5650cbefb3a1 | -7.5291 | -61.3444 | 2025-08-15 00:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| f20d213e-0d50-3dc8-b1a3-8c51da85c795 | -6.9303 | -59.5305 | 2025-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 4a1d30f7-65df-3adf-bd81-130e0e535df0 | -6.0622 | -59.9663 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 364b53ec-3107-3324-85b0-183cf2c55d21 | -6.0808 | -59.9274 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| acdb5fa8-884a-301d-adcc-61a072a097c4 | -8.3099 | -45.0196 | 2025-08-15 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d5ba231a-f376-39d5-b692-f06bded7454c | -3.4254 | -49.0517 | 2025-08-15 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7445484a-c614-3a06-ab69-8bb14a3a8d4f | -2.4876 | -47.5737 | 2025-08-15 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| cedc9890-a483-3736-89ae-156954e28d18 | -7.6103 | -63.516 | 2025-08-15 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 7cec544f-ba6f-385f-97d6-3f69ee5c9c28 | -9.4992 | -60.547 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| a93b1818-431c-307c-b330-69a29c37d0b8 | -6.0806 | -59.9657 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 65474202-0570-3ec9-be43-2fb609fb5120 | -6.0991 | -59.9459 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 18917c67-51dd-32af-a2d0-a39f0749a49a | -6.0623 | -59.9472 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 7c8e8371-dd5f-3d9d-be15-ea8d4640e1a2 | -9.5179 | -60.5461 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ae7dc924-1675-328d-989c-8c86df25e8ab | -11.3466 | -55.4326 | 2025-08-15 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d53befdb-5f3b-377d-9362-7d1f323600e3 | -9.2683 | -40.2668 | 2025-08-15 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 3b48b772-bdf4-34a9-9979-d1574a70ddd0 | -9.3876 | -60.5335 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2f4cda87-089f-3e2f-ac96-f89bca5b5fd0 | -6.0807 | -59.9465 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 310.7 |
| ed1ea4e7-a7d3-3351-81cb-3eed3657678d | -7.5291 | -61.3444 | 2025-08-15 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 458dc595-a59c-32c0-b606-1d83d2ad5339 | -9.4994 | -60.5278 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 59df1c75-165b-35b5-8b13-3f55acfd0cab | -7.0796 | -59.2351 | 2025-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0789f00d-e894-3822-ac7a-6b73f67b30f5 | -7.6104 | -63.4972 | 2025-08-15 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| e8f8b2e9-6c19-377c-bcd6-a6cedcf5345b | -7.5292 | -61.3254 | 2025-08-15 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 9abae858-8051-3464-83b8-3c4b8e0e90a2 | -5.455 | -60.1391 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 24d4febc-83e9-3282-9d1c-20e25e8557db | -14.8262 | -49.3335 | 2025-08-15 00:50:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 4e53f6b2-4518-3ba1-aa91-3f635108df08 | -11.3657 | -55.4107 | 2025-08-15 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| dc206551-d1bd-3504-ba89-5e9f4e12b73b | -14.2444 | -44.5897 | 2025-08-15 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 57ab8d97-8678-36b0-80be-413082ba05c4 | -9.3875 | -60.5528 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ac3c21cb-a801-3675-8fcd-0bc393000b1d | -11.3655 | -55.431 | 2025-08-15 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 0089a679-df52-3555-a69e-3a9a61022b73 | -7.0797 | -59.2157 | 2025-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| e1f6f793-d447-3012-bb80-6a882bb71825 | -5.455 | -60.12 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0b707175-2b82-317a-ab6b-846b1d7fc73f | -5.762 | -46.6741 | 2025-08-15 00:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9ce37165-e793-3f25-98c3-bd54b75780b4 | -14.8266 | -49.3114 | 2025-08-15 00:50:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 73bbffba-4767-3d0b-98a4-aaae5d9bdeb2 | -7.3116 | -60.628 | 2025-08-15 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1205274b-4193-3700-83e9-76eb863525bb | -5.4366 | -60.1397 | 2025-08-15 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fa53eda0-72d5-373c-8b81-efeea294ca98 | -9.4995 | -60.5085 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4a072f2e-ad7b-3a2e-9324-d01b9181d7ec | -6.49 | -62.9306 | 2025-08-15 00:50:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 50760cd3-09d6-373b-816a-e1031df8c52e | -13.3203 | -45.2177 | 2025-08-15 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 71c10b4a-2a67-3d61-8c8e-ffc4ab50c178 | -11.3468 | -55.4124 | 2025-08-15 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 94e032b0-4b5f-3717-82e9-5e4e216218c8 | -9.518 | -60.5268 | 2025-08-15 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 737cea6c-154c-3246-8412-4c8a104dbb17 | -11.3468 | -55.4124 | 2025-08-15 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 75aec553-0ec6-38c3-9f86-4234de052bd7 | -6.0623 | -59.9472 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.6 |
| b88b46fa-716e-3521-a3ff-a769d2276ab4 | -11.3655 | -55.431 | 2025-08-15 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| b1c797b3-e2b7-3b12-8cf1-c6b41e58adc7 | -10.87 | -62.0115 | 2025-08-15 01:00:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 471b5763-c336-35da-b213-6b4e1d068b71 | -5.762 | -46.6741 | 2025-08-15 01:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 149b7e66-f980-3dbc-a6f7-5fee04c31159 | -11.3466 | -55.4326 | 2025-08-15 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8bcf7801-6850-3b17-981f-a50898f08ed2 | -8.585 | -45.6275 | 2025-08-15 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 8e107e00-50c1-373a-9853-6285d1013b4b | -9.4994 | -60.5278 | 2025-08-15 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 17baf151-05ab-3791-9464-e1b5d6fd0373 | -5.455 | -60.1391 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 1321a2a0-2a6f-363c-91bd-55a608279b51 | -9.3875 | -60.5528 | 2025-08-15 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fdcdb246-3d7b-3bd5-8232-d70c12ed36f4 | -6.0622 | -59.9663 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 5c796bf4-c5dc-3e3e-ad11-b475c63ab4b2 | -2.4876 | -47.5737 | 2025-08-15 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 370e49af-55ae-3397-b834-7edc4e1d4c71 | -9.4992 | -60.547 | 2025-08-15 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0db53719-8645-31a8-8a26-1b1d4543e9bd | -7.6103 | -63.516 | 2025-08-15 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1c2940cb-8996-3519-a75f-e559fb03750d | -6.49 | -62.9306 | 2025-08-15 01:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ad0a54ea-7ea9-3b68-9b6e-4b4f8faca5e4 | -8.6041 | -45.6029 | 2025-08-15 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 02c17bc8-7563-3d4d-a955-cf6aa85e2169 | -11.3657 | -55.4107 | 2025-08-15 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| a36b988f-3340-3346-8c6e-57e00f65e891 | -6.0991 | -59.9459 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 99456a05-1845-3ee8-b5a0-533a963ba4da | -9.518 | -60.5268 | 2025-08-15 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 17eef246-0ea5-3925-a5e4-340263dc8392 | -8.623 | -45.6009 | 2025-08-15 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 3051e65a-b6a5-36d2-b7ea-674a51c8cf65 | -5.4366 | -60.1397 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7581a22d-11b1-3dff-8cb1-01d7f213fbfc | -3.4254 | -49.0517 | 2025-08-15 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e61f5c4b-563c-38ea-a9f4-39dbc1bc2ee6 | -9.5179 | -60.5461 | 2025-08-15 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e3f0da8c-695a-3d4c-b9d3-7efafd0e6ecd | -9.4995 | -60.5085 | 2025-08-15 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a6d21b1b-e528-3534-bdac-580fca51fac3 | -5.455 | -60.12 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| de2640c1-3d6d-313e-896b-80835cb14ca3 | -7.0797 | -59.2157 | 2025-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 881eb66c-bde0-3383-818f-83d9c4ad601a | -6.0806 | -59.9657 | 2025-08-15 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.1 |
| daaf7658-dfa3-31a4-8901-d204b54d03de | -6.9303 | -59.5305 | 2025-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d276c1ce-6e8d-3787-846a-7dc17fecca63 | -11.3471 | -55.3921 | 2025-08-15 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 40df70e1-907b-3441-82cd-1ddddd702536 | -7.5291 | -61.3444 | 2025-08-15 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 04620847-572d-3b66-bceb-1491e423cfa3 | -8.6227 | -45.6236 | 2025-08-15 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 5e6e4ce9-cc70-3c58-ba13-b643c3765de5 | -8.6038 | -45.6256 | 2025-08-15 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 310.9 |
| e527c48c-af43-3310-88a5-4ff260eb3424 | -8.6036 | -45.6482 | 2025-08-15 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| ad79b60f-7c01-3fbb-ad42-1775e28df95f | -7.5292 | -61.3254 | 2025-08-15 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 3e51f5fd-896d-3541-ab50-0fbab8318217 | -10.8513 | -62.0125 | 2025-08-15 01:00:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 9b724593-977f-3a29-ac33-52254b8cdec9 | -7.0796 | -59.2351 | 2025-08-15 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |


[Clique aqui para ver as próximas entradas](README6.md)
