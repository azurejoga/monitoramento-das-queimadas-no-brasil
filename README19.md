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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9655435d-6edc-3e92-9efe-af82469202ba | -7.7493 | -44.19033 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6765eed-a4bc-3693-83a4-d6ec2e3cd632 | -8.16281 | -43.18748 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e145c9d1-c2f7-3c33-b3ec-6fab14cca690 | -8.03731 | -43.13235 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3c571800-3a4d-3b6b-8315-2ed06dadec86 | -12.01736 | -49.27219 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8fc90983-8fbb-3fdf-b8bb-0bf60a23710c | -12.01376 | -49.27165 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e3a61f3c-3e14-3620-8563-26016912a3b3 | -7.73991 | -44.18926 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 21bedce4-a782-3ed0-85ad-22adf22787c3 | -6.3071 | -43.81337 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54645cb2-d7be-34c7-9247-2d8610ee1eba | -12.01797 | -49.26797 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa39ae7b-44a3-31c2-a130-94a4da881ad9 | -6.30493 | -43.81047 | 2025-11-30 04:46:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2592d3e-4804-372d-a33a-872a55d04c69 | -8.04781 | -43.13081 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 45f7759e-eb23-3421-be93-1a23a669c53e | -8.0377 | -43.1294 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6cb96b8f-eb0e-36f9-998e-cf074bbda217 | -12.01315 | -49.27588 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5293fab-5c60-3078-8fee-147174c9beb9 | -12.00656 | -49.25877 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38b06e8f-7c26-3440-b968-b5f8ae0bf881 | -7.22337 | -40.28204 | 2025-11-30 04:46:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af342f9b-d7f1-31c2-b9a8-afb74ca5a404 | -8.0381 | -43.12645 | 2025-11-30 04:46:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4fe78fc2-a690-3b3d-bdaa-fcf743021014 | -7.7446 | -44.18987 | 2025-11-30 04:46:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0d8b9b9-2c3d-3876-98be-c755fc68277d | -12.0017 | -49.26669 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7949172-1eff-31f8-98db-50250b263188 | -12.00357 | -49.26582 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 792d0124-783f-3b7e-b4d5-ec5339b22617 | -12.01138 | -49.26265 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 21dc7221-d2f3-383f-aea8-a26421f7ffc3 | -12.00955 | -49.27534 | 2025-11-30 04:46:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a601ebcf-116c-3d76-a9a0-7aa11fb8e6f4 | -17.48666 | -57.11547 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9bf52c70-efbc-3cb2-aadc-81a1f32f4155 | -17.64597 | -50.79482 | 2025-11-30 04:48:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96a913ba-22c1-3cfc-af7f-bfc88b4fc2af | -18.41302 | -46.84423 | 2025-11-30 04:48:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c701782d-efd8-3928-baf0-ca018d6d77da | -14.45527 | -52.88916 | 2025-11-30 04:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6d9575f-12d6-3970-8630-2c569605fb9a | -16.7114 | -54.42163 | 2025-11-30 04:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12447e7d-0996-3810-bf17-f80757b25565 | -17.47727 | -57.12426 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 30f3e5ff-0369-37c3-afbb-c0e908f379c9 | -17.50658 | -57.15116 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e0558a22-f046-36c0-82ae-624bf2bd4d3a | -12.83254 | -47.39074 | 2025-11-30 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbac638b-3065-37be-9c03-cc7cdc611ab3 | -17.51099 | -57.14745 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 101ba2cd-8df7-34be-8797-be491b40ec44 | -17.48242 | -57.11616 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 30ad04ce-3cd7-3801-bb96-e68f7daf331e | -16.21763 | -52.18702 | 2025-11-30 04:48:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1c2a41a-79bd-351a-a5af-9b98b8001e90 | -18.13359 | -47.15812 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdfc4959-1df8-37fb-86ba-ad4bb30ff6ad | -17.49028 | -57.11616 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 79daeee5-d772-31af-8520-b8ded11e56ad | -12.82799 | -47.39381 | 2025-11-30 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0133779a-c5ab-35bd-a991-85fe40b0e3e7 | -18.11636 | -47.15149 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24254bd3-9579-3511-b351-f0bdd4c2d447 | -14.45028 | -52.89926 | 2025-11-30 04:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f86ce7a3-1b9b-3783-a8d8-fb52f6f40c26 | -17.48558 | -57.14256 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fd022b9c-09e2-3176-8e95-9359a37195da | -18.13412 | -47.15371 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 404be7ac-9b0e-366b-b43d-fa54b71c2a7a | -12.49825 | -54.41007 | 2025-11-30 04:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b8e173a6-be95-3439-a617-cba05313711d | -13.72235 | -48.73832 | 2025-11-30 04:48:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eca90251-056d-3771-a829-a7a07e98c5ee | -17.48605 | -57.11685 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 85c681b8-7e5c-3f33-93bc-2e41ffc13449 | -14.45196 | -52.88861 | 2025-11-30 04:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e71bd92e-3bf3-33b3-a38c-20b609e49e28 | -18.12026 | -47.15652 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25a1c840-c605-375d-ba51-f0a7d4115254 | -17.51021 | -57.15186 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c0954367-032c-354a-86cd-48198ca8e7da | -14.87899 | -52.98079 | 2025-11-30 04:48:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 012448d6-e1fa-3422-982e-dfb2258dbcfb | -16.79818 | -53.77504 | 2025-11-30 04:48:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa8893e4-4021-3266-8a6b-c8d8fe92ee23 | -17.50038 | -57.12263 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 44d5976a-108f-3410-9656-1bb7ae286d5b | -18.14959 | -47.13768 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52b74047-16c5-3b86-a092-10e41e3b6286 | -16.21819 | -52.18333 | 2025-11-30 04:48:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d325c9b-dcc0-3648-b0f1-ce88d0e3daa3 | -18.15352 | -47.14246 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3355191-dd41-317c-b5c2-b3b3fcae43ca | -18.40846 | -46.84377 | 2025-11-30 04:48:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec596caf-f6e2-3004-8997-099ff4c33744 | -18.15404 | -47.13822 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fa585ee-177d-3b2d-824c-6b65b28e8dca | -18.15454 | -47.13406 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f861ae3f-ccf0-3c0f-bbe2-7e1e6a49026a | -17.47575 | -57.13307 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 88150059-3dd6-37a7-8928-287e9c150300 | -12.22924 | -54.38104 | 2025-11-30 04:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97145bb7-a86a-3b6c-a130-f33ccad248c8 | -16.79875 | -53.77145 | 2025-11-30 04:48:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93b84be7-9a33-3026-8c13-83087fa013f9 | -15.19564 | -51.91926 | 2025-11-30 04:48:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0db385b-5d39-3032-b8f3-f63efdaafdc4 | -16.22154 | -52.18389 | 2025-11-30 04:48:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cea9e22-eae5-3ac8-aee1-1c27029ee41e | -12.50317 | -52.38879 | 2025-11-30 04:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 68673ac0-3629-3368-a0ea-147c635ad1fd | -17.49205 | -57.14837 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 35b0a32d-88f8-359d-b6f9-6213378eb236 | -13.48768 | -46.71208 | 2025-11-30 04:48:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8bb81c1-8c70-3ce0-a5bb-5d04189b904b | -17.84852 | -50.35725 | 2025-11-30 04:48:00 | NOAA-20 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3feac82-689d-3350-aa2a-4eaa09e906c6 | -13.48713 | -46.71619 | 2025-11-30 04:48:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b8e945a-a79b-3a22-9c86-53e658a9f51d | -14.99875 | -56.82167 | 2025-11-30 04:48:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fc8c057-9602-3116-93f9-cf2c9d7a2a99 | -17.51177 | -57.14303 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 71485295-9df4-37b8-83e6-bdacc3fd0ca9 | -17.48799 | -57.14912 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7fe9173e-7a2f-3ad9-8e20-10cff618e7cc | -16.2307 | -58.81889 | 2025-11-30 04:48:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 90d2b0d5-46b0-35bc-9625-dc4af0b5baa5 | -15.19509 | -51.92292 | 2025-11-30 04:48:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a080f60-645d-3280-98d0-8615cb30581c | -17.48842 | -57.14767 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 3d4e5397-693f-31d6-8684-09833067bcfd | -17.47938 | -57.13377 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e21f6e82-6bb1-3dbc-b21f-22f6ebe05002 | -17.48587 | -57.11987 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5582046a-a863-3e2d-bd3e-542945a79ddc | -13.62173 | -53.51693 | 2025-11-30 04:48:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d389136-2635-3fa9-8d64-2b4c66207895 | -12.82393 | -47.39328 | 2025-11-30 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b8df6fe-b4b0-3b70-96cb-a140955fef25 | -17.49569 | -57.14907 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| d7bb558c-2528-3cb6-95b4-3615beb785c4 | -12.82848 | -47.39017 | 2025-11-30 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3add7f53-f91e-3087-9180-9b5b2fde2406 | -15.09551 | -50.34374 | 2025-11-30 04:48:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1f2420-6820-378b-99b9-5dbd9fae1ef6 | -12.82442 | -47.38963 | 2025-11-30 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdfad991-6f89-36f8-8be0-878d752c377f | -15.7097 | -50.00724 | 2025-11-30 04:48:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be78ee06-ea4f-3c38-9f6d-32fc7d6224dd | -15.71332 | -50.00772 | 2025-11-30 04:48:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5510017-477e-3f86-9829-709dd264c7f0 | -18.15009 | -47.13353 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0c1caf1e-5bdc-35ce-b29f-a5a4f58c1698 | -15.199 | -51.9198 | 2025-11-30 04:48:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 548ad235-5f4a-32f3-afb8-732d7e262c8c | -17.48512 | -57.144 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b5c9f6df-dfc3-3798-aea1-03aa83a8ab80 | -15.0954 | -50.34464 | 2025-11-30 04:48:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6866172e-4371-35b3-b1ce-b2135c90192d | -17.47804 | -57.11986 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 90e36160-c5a3-314d-ac5d-de100fb8c21c | -17.49932 | -57.14976 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3b787f71-b57e-3530-8749-eb8be3dd6e68 | -17.51462 | -57.14814 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c92a6513-47b9-3ba8-8511-318d3eb0bf00 | -17.48166 | -57.12056 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 69af356f-d146-36c3-953f-8f2175f5cbb5 | -17.48588 | -57.13959 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fc2f0855-7ea8-3523-a8ac-9d1de2505ef1 | -13.62562 | -49.65627 | 2025-11-30 04:48:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dd1da11-65ba-33ed-af4c-6a4608683ae9 | -16.763 | -51.35529 | 2025-11-30 04:48:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3ff2da0c-978c-34f0-bd9e-93ce980fe512 | -17.50295 | -57.15046 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 94d70e50-a929-38f3-84fa-6bc2708b288e | -17.48968 | -57.11755 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c9e30b49-a808-367a-b67e-80ffaf27e330 | -17.48875 | -57.14471 | 2025-11-30 04:48:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f6e07cb9-5dbb-311c-85fb-102da09be1e8 | -16.22098 | -52.18757 | 2025-11-30 04:48:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8814d77-9088-3b2b-929d-a88313ce1218 | -18.12913 | -47.15768 | 2025-11-30 04:48:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1698ea6-9212-337f-83de-a3893ca55806 | -12.0195 | -49.2659 | 2025-11-30 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1ebec7a8-d6c6-3bfa-8e3a-f110fc565fa3 | -12.0004 | -49.2683 | 2025-11-30 04:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d1197a62-b9d4-3f24-87eb-60d15b44d79e | -8.1633 | -43.2055 | 2025-11-30 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 85c6dcd8-503d-3a5b-9c9f-1129903bd3d4 | -19.93121 | -57.4219 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0c971b72-42c1-3b12-8a7b-fe38082f0a07 | -19.86023 | -57.78537 | 2025-11-30 04:50:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README20.md)
