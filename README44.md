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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18c8ccde-3c87-383f-8c2b-eb5383da7cdc | -14.19566 | -45.19029 | 2026-09-18 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65ed6d2c-bd41-36cc-a0b8-08b0b6b13a58 | -11.22417 | -43.47781 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ab9f219-a6a7-3ef3-a77f-ae7d8775aad3 | -8.38703 | -47.2087 | 2026-09-18 04:21:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eff7ded-364a-32d0-af6f-9f0d7e6f0fae | -12.61853 | -50.88276 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38124dc3-52f5-369a-b026-8be4a1a6026e | -8.68159 | -45.43839 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 32e5e65b-5960-34f5-8fae-0d4c57266373 | -9.71182 | -47.09783 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd62efb7-806c-33b1-b036-dcf49e090f62 | -12.99328 | -46.92272 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f96dcdee-4404-3fd1-8850-c2434542e95d | -12.1748 | -46.97712 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10d30b55-9f40-394a-a8ca-ddac169a0d33 | -12.13389 | -45.14413 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed16632d-aa8d-3dba-974e-509bf0c55060 | -11.38427 | -47.29939 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a038cb1e-7192-3896-845a-6e58fc37031a | -10.49718 | -46.29085 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7df27006-e0b9-317f-9db8-8f662d810184 | -13.23273 | -42.32699 | 2026-09-18 04:21:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 121bd7ff-d390-364c-bd5b-62f5c93f193e | -12.71715 | -43.20393 | 2026-09-18 04:21:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54e4d7ea-7a49-39f2-8901-54713acde70a | -14.94905 | -49.92132 | 2026-09-18 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 596baa74-8d2c-3dfd-a825-3d1c021b0276 | -9.9485 | -45.34117 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 008d9367-35fe-34bf-8fcc-38e73f97f9e5 | -9.74461 | -46.10127 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 988547bc-9ee4-3117-9593-539d70352587 | -9.76768 | -46.59894 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b726149b-1a9f-3666-992a-fc9e1d714b27 | -11.52377 | -46.85559 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65661d1f-a113-328b-a1c2-ebf38d956691 | -9.71693 | -47.0875 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03fd0d37-4256-3434-be37-022f197f1cc0 | -12.65675 | -54.7196 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0ea961df-6c9b-3abe-b22e-d7363f5adae4 | -12.53376 | -47.09462 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99d2df09-dee1-3b65-a9ca-e5eae0de2044 | -13.76719 | -48.03542 | 2026-09-18 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c027a0ab-f98f-37c7-98ee-05d4db626881 | -9.85635 | -48.37542 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0566a386-2133-3ff9-a88b-06cedc7cdd1b | -8.57392 | -44.57634 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9835c0a0-1dd7-3885-9574-6a1ad2440f18 | -8.46427 | -44.51614 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f7a1cf1-c785-30e1-8448-fc75368097b6 | -9.77713 | -45.04156 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b0b5616-df9e-37cb-9d3a-781aa5dea135 | -12.55742 | -50.72898 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b8e398d-07c1-3673-be3b-5ff62e6119e4 | -8.67519 | -45.30587 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 428bf81d-913e-3986-bf65-59e557bac542 | -12.39568 | -48.46427 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5081ba75-05e3-3029-bd33-1ae134e516fc | -10.11799 | -46.3014 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4456a5c3-47d8-3cc9-bd5f-ec7e34f27efd | -12.44772 | -55.00021 | 2026-09-18 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ff1ac2a-d0e5-3586-abdc-037fff4a0747 | -11.16311 | -42.80755 | 2026-09-18 04:21:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 032d104b-24c8-3ab7-bb38-db154abcf952 | -8.71451 | -44.87778 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e04d42d-2edb-3539-9109-22cc9965d1b7 | -12.47571 | -50.68687 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48fdc7a6-00e6-31c2-8367-dc5f0b502581 | -8.7666 | -44.22998 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69263745-dde8-36b3-b5ca-d90d4f413038 | -12.21083 | -53.2176 | 2026-09-18 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4fcf6948-1b4a-397a-a57a-665349e70586 | -11.7693 | -47.42974 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7adf13e-e51c-3c18-8fa5-58480ee3d095 | -10.19016 | -45.40474 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 2f94d6c5-26bc-3054-b09b-fd19f1503bed | -11.80756 | -46.80409 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 842d7296-b5e6-3e01-b2aa-5b5141ba1a36 | -10.01721 | -45.50912 | 2026-09-18 04:21:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 270c2899-8ee1-3aa3-a104-555b05462e5a | -9.93564 | -46.59312 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59e451ab-a5ed-3c45-8450-2c3dc05d56f9 | -11.88104 | -47.61667 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3a4b057-8e30-31c9-b323-f3bd2c567890 | -9.46604 | -45.44575 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 29f851d7-5703-316d-a41f-36cf59a02fac | -9.46274 | -45.44523 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fddec514-90a5-3cea-a491-e7f23121e795 | -10.90031 | -53.99287 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3bdee59c-31de-314d-b88d-687f1b47cbe3 | -9.60532 | -45.33667 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44ee9ad6-3c66-3705-9d8f-6e8405dc84a6 | -8.8544 | -46.92529 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76255760-f2f2-32e2-8986-bd4be66305cf | -8.68544 | -45.43544 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a066c8e7-e21e-3c71-8f43-ca3a38d5d84b | -13.42649 | -51.90213 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cd3a4ca-f1e1-3af8-807d-89a75b88f7ae | -9.55779 | -45.46808 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a3432a3-0b7b-39f4-b2dc-73c3d6c6cc45 | -9.76003 | -46.08945 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38a1251b-6cdf-327f-ac62-105c45efa365 | -10.54796 | -44.84821 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e6d41d-df00-3136-b483-c10c07d614a5 | -12.177 | -46.98473 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f27ea12-675a-3968-9f27-419c9111c496 | -8.93816 | -51.46442 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e665c7f-c05e-328a-b2bb-c2c7686636c6 | -11.33754 | -44.01661 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a8af230-237d-3bf8-88ae-8e5acd565ff4 | -12.53879 | -47.08447 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0a5400f-216d-36b0-95fe-39dfb10ced4b | -10.13007 | -45.57391 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53b67ed0-2c6c-3b29-a079-a81821128e6f | -13.59958 | -46.93901 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81317fbf-ee17-3ce3-b815-955688fda1cd | -13.68212 | -48.59416 | 2026-09-18 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebbe5b38-f0f0-3ad6-a58d-8683b79c2824 | -7.75449 | -54.75315 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ad191a9-3da1-33d4-b55a-309780f24169 | -8.93398 | -44.40101 | 2026-09-18 04:21:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d571e24f-8235-3a0f-8416-15ad50619edc | -11.81311 | -46.79054 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0c6df094-c313-3e63-b72c-80bff0f002ec | -8.88466 | -45.88049 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8147942e-411e-3736-b40e-65fdf5f36581 | -11.16775 | -42.85096 | 2026-09-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 43008304-aa1e-3c82-8549-378e227de0d5 | -14.13506 | -48.72594 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 25a1c10b-11f0-3973-955d-ae45afdf32ca | -9.3989 | -46.86173 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54553a63-c347-3293-81ef-590f639e837d | -9.55584 | -48.10378 | 2026-09-18 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55d7be21-c211-3033-a568-d01d6b68baec | -9.91863 | -46.50683 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce604c16-e264-314b-9fa0-364929ed99d4 | -9.94147 | -45.31859 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 309300c1-9588-3422-833f-d736e1a460dc | -11.3237 | -47.25615 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef6ad7c6-0585-3991-96e6-4b268cba7f17 | -11.84091 | -44.85909 | 2026-09-18 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7d8e6b2-1ae0-3427-9bcd-5f2cb6d54dca | -12.34805 | -50.74815 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e8afbcf-52d4-338f-8ac4-a366c018b83c | -13.2536 | -46.91091 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35c03a48-cbf4-3193-ba8c-9e5321c0ef29 | -9.59548 | -45.85892 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 816c70d8-d840-3aa6-bc2f-5340bfe6d57d | -12.17148 | -46.97656 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 62a9cd54-7c2c-3196-b961-61398d0ea8c9 | -13.34588 | -43.78089 | 2026-09-18 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34e008db-54e1-3894-b1e8-5391f80c4ee5 | -12.43808 | -50.67518 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1cdc38c-4034-3cb8-89a2-8eea48a8c2e5 | -9.37181 | -46.90169 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f95dfe87-f020-3a38-9ec3-3d53791cd8b9 | -9.86339 | -48.37663 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a0ca1b6d-150d-3e8b-9642-c8e53e86b141 | -9.76712 | -46.60245 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61f187df-0704-3576-9d88-e787cd0a2765 | -9.71177 | -54.81617 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4127fb65-7333-302d-b8b1-4332bff75c78 | -9.76776 | -46.08349 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8757bf4c-116d-31a2-bdf7-01b53a69b39e | -9.85987 | -48.37602 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2526c513-2fdd-3b4b-9f22-5a9526c4dfdf | -11.6727 | -54.45356 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aacfe533-d82c-37ec-aeca-38378395a84b | -8.47486 | -44.53571 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6438f97f-6711-300e-906d-e51e8d2b3242 | -9.62135 | -45.34623 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0870a8d-e45f-35de-9d6c-a708895ad284 | -10.13061 | -45.57043 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c53923c-28af-300e-90f8-494aa4fea43a | -12.39441 | -48.47193 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdd903a5-2b3e-3bd0-8c4b-194736452932 | -8.95098 | -51.46665 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86c0d109-7133-3e81-9b8e-caf1fcc09a65 | -8.351 | -45.98425 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d44cc09-c57a-393e-b43a-692ac33cefcc | -13.75623 | -48.82458 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35fc70d5-6a15-32dd-9748-bd1f756b412d | -9.62189 | -45.34274 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4584f351-f3cf-3af6-bf23-0fad5ac94dec | -14.17162 | -47.85461 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94afc6f9-1d26-3838-8eb2-fd24ce877315 | -11.29631 | -43.47279 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c359eed2-8ed9-38e3-abde-fc54fff9345c | -8.65072 | -43.86946 | 2026-09-18 04:21:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d38914ad-45b6-3310-ab20-42fc161f8fd8 | -13.74572 | -48.80252 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91c0ad8c-003a-3551-b494-ec7ad3535a78 | -11.58229 | -46.89404 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60c1d9a4-4f95-3fe9-a616-7e2578ab78f6 | -9.83224 | -49.22968 | 2026-09-18 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 218c934c-f26b-3d82-bf03-3aecabb7ce32 | -13.6073 | -48.29839 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 42ae7ce5-0feb-3198-a25d-535673f3fc00 | -9.7511 | -46.57445 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
