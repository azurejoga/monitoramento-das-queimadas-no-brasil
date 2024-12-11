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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d2343cc-d465-3a73-9c1c-68bb712095b2 | 2.7627 | -60.6567 | 2024-12-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a8324da8-b1c7-31a8-b3b9-ae820daac54f | -3.1133 | -53.2381 | 2024-12-11 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 586dd24a-c65d-337d-bb6f-53a23d744aee | 3.2362 | -61.1982 | 2024-12-11 00:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f9de67ea-44e3-3b5f-91a6-662eb5646f09 | -6.9589 | -43.023 | 2024-12-11 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.3 |
| 8eda2e3a-dede-391d-aec3-9bc0b150a4b4 | 2.7445 | -60.6191 | 2024-12-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 22331776-f2ee-39de-b8c9-76c5c40dd7b6 | 2.7444 | -60.657 | 2024-12-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b419d141-3600-352c-a5bf-f745b70a93a4 | -6.9158 | -43.5185 | 2024-12-11 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 66fbf993-bdd2-3aeb-9c9b-4d4735ff5c97 | 2.7627 | -60.6378 | 2024-12-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 149.0 |
| e02007e4-c41e-3a56-ab75-929a86dda156 | -6.897 | -43.5202 | 2024-12-11 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 294.0 |
| 41df7d76-d11e-36fa-873d-1a2a06c71cc6 | -6.9161 | -43.4952 | 2024-12-11 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 153.8 |
| cd540236-472d-30d7-b900-8515398b09a2 | -11.1109 | -54.6204 | 2024-12-11 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 8a17f50f-a782-388c-be94-d600d9c77619 | -15.0865 | -59.6487 | 2024-12-11 00:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 32ccc21a-8f60-305f-b9f4-d2b60e572cad | -11.1106 | -54.6408 | 2024-12-11 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| b35dc4d7-95d7-32a9-91de-5782a4f6169f | -18.0989 | -40.1368 | 2024-12-11 00:30:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 132.7 |
| 02558b72-31f8-330d-a597-76df029cd95e | -3.8165 | -52.3813 | 2024-12-11 00:30:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| bad538c9-9797-3222-ab8d-f46e00289d31 | -15.971 | -57.1669 | 2024-12-11 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5ca76308-bf9a-33e7-a25f-c50c12ad457f | -3.1287 | -54.1054 | 2024-12-11 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 29f8e8e8-a66d-3f7d-98ba-fb92eaf06b1a | -18.1192 | -40.1311 | 2024-12-11 00:30:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 306.2 |
| 6ec95e2f-6d1b-3721-a188-961ed3078337 | -11.1295 | -54.6391 | 2024-12-11 00:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d392af0d-48f0-3e9d-a20f-4fc749154863 | -18.0067 | -52.9645 | 2024-12-11 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 763b256f-c1b2-3df8-bdce-1c9a59d7a743 | -18.1184 | -40.1572 | 2024-12-11 00:30:00 | GOES-16 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 100.0 |
| 519cb9d7-3f51-3868-aa1d-b331d023978d | -6.9594 | -42.9759 | 2024-12-11 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| b1f8d475-534c-3d61-a52c-cecea64ef4cc | -3.1288 | -54.0853 | 2024-12-11 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 41f9c2fc-b324-345b-8c2e-f08a80ced558 | -18.0062 | -52.9861 | 2024-12-11 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d09ed92e-6838-3016-a044-97a5b7118faf | -6.8972 | -43.4969 | 2024-12-11 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 59f24fce-3dcd-38de-bc00-7209a4321409 | -18.0266 | -52.9614 | 2024-12-11 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| c453c33b-c809-3aa4-b26e-ead1f40db584 | -6.9403 | -43.0012 | 2024-12-11 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.3 |
| 955554a7-f9e6-33cf-b992-c41a57466b5c | -6.9783 | -42.9741 | 2024-12-11 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| f5e9e87d-98d4-3a58-b710-3f9f73ca2efb | -18.0261 | -52.9829 | 2024-12-11 00:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9ae8f5b0-a13c-3dd0-9ec3-15eef0786f55 | -6.978 | -42.9977 | 2024-12-11 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 149.6 |
| ccaca3f5-0ac9-3028-b54e-88a925d27ca7 | 2.7444 | -60.6381 | 2024-12-11 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 9ece04f7-18c3-353e-afa5-0db1e426b1f6 | -6.9592 | -42.9994 | 2024-12-11 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.8 |
| 11a7052a-d626-3b90-94f8-9364181a6d3c | -3.5894 | -53.702801 | 2024-12-11 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf09243c-30df-3166-816b-c21948b8f0bc | -6.8915 | -43.510101 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 14dd5f30-7f63-3056-ba29-7c4724e5269a | -10.5927 | -37.0723 | 2024-12-11 00:31:00 | METOP-C | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22e692a3-8e89-32f1-b448-4202e36b33ae | -10.5106 | -44.927502 | 2024-12-11 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95ce48ba-a195-36bf-9403-345041c8dadf | -18.116199 | -40.1334 | 2024-12-11 00:31:00 | METOP-C | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0134c552-f4f0-3c0a-9d33-6b21ca2227f4 | -6.0995 | -44.053902 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9728b2-f505-34ac-b8f6-d50913a381e2 | -6.8995 | -43.500301 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d3ee2b75-4ac8-3ae3-afc4-4e9df421cf2a | -18.1182 | -40.1418 | 2024-12-11 00:31:00 | METOP-C | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 55f2102a-5649-32a6-bab0-c00f07b5641e | -6.903 | -43.5154 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ab113c6-9c62-30fc-8863-b7d55ad90f6b | -6.8977 | -43.492699 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 47bceb14-f2aa-3e14-953f-6b3f5899a877 | -18.0103 | -52.9482 | 2024-12-11 00:31:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efc78a63-bd4c-3646-8c75-8354e3a286fa | -18.114201 | -40.125 | 2024-12-11 00:31:00 | METOP-C | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd98ea19-d00a-3474-b4d2-6349c79e21fc | -18.0179 | -52.991901 | 2024-12-11 00:31:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 518f20ac-86a2-3e75-ae33-181e7958749c | -4.4831 | -46.712799 | 2024-12-11 00:31:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6753c382-c9f0-35e7-9ecb-e5a87db6ca29 | -10.8896 | -37.264599 | 2024-12-11 00:31:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a4415ea-74bb-3f13-94bf-b80dcee9507d | -3.107 | -53.2365 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 096e05a0-2221-340a-9ba2-b7e5513780b0 | -6.9649 | -42.986198 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 59f3c13f-2dbe-3bf8-a40c-df6c5cb873c9 | -18.0044 | -52.971699 | 2024-12-11 00:31:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 59e5360d-52b4-389a-8edd-3ab267b6a7f6 | -3.8069 | -52.3825 | 2024-12-11 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f3aca7-297a-389d-aa83-60452b3b3974 | -11.1124 | -54.634899 | 2024-12-11 00:31:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abdecee8-1850-3fb0-bebf-f8f7acd4aa9b | -6.9111 | -43.5056 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4053a8a-424c-3c0f-949a-0c1612d40389 | -2.8131 | -53.067001 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad089a58-9845-3b62-825e-3d1c50452c4c | -18.754801 | -40.1185 | 2024-12-11 00:31:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b2becf4-ba1d-3669-ba9f-357ce3b2c79c | -5.2994 | -43.278801 | 2024-12-11 00:31:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a27eadc-217e-32e9-ac7b-231e9a1cfd40 | -5.9765 | -44.591702 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6a218e8-6aaf-3fce-a16f-411da58c21fa | -6.957 | -42.9963 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7bb6d80e-8a91-360e-b3fd-4504fc4acfad | -2.8297 | -53.049801 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d855ebbb-0b15-36af-be5c-0e19a1114f25 | -9.4999 | -36.109699 | 2024-12-11 00:31:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5a14e14b-5d70-378f-84fd-3c38ca4aceb7 | -9.5049 | -36.1292 | 2024-12-11 00:31:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a4adab9-9b84-3e3b-ba59-db3e1d716810 | -12.8908 | -43.649502 | 2024-12-11 00:31:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa931f94-b692-39df-ae95-b7eb716a2a41 | -14.9697 | -44.408501 | 2024-12-11 00:31:00 | METOP-C | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 474f505d-4afe-3272-acfb-9aad6dcf4018 | -3.3342 | -53.0625 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c88651d8-1b14-378f-bd20-2046e596575d | -10.8857 | -37.2491 | 2024-12-11 00:31:00 | METOP-C | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 333ca70a-597c-3b06-accd-8d389c6eb1b7 | -3.1456 | -54.460701 | 2024-12-11 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e0c6090-6ead-381b-940d-b7cebc5fcb2c | -12.8561 | -43.813499 | 2024-12-11 00:31:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f3ff444-6886-3ff7-8630-9716c91cdac1 | -3.1329 | -54.083599 | 2024-12-11 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2663e5f9-f231-365e-8688-2af6e761e3e2 | -14.2654 | -45.789799 | 2024-12-11 00:31:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 005bf1c0-91a4-3b89-92e4-cac34849790d | -6.9668 | -42.994099 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71a0f6fa-1c07-33a0-9626-211e20fb59fd | -18.0238 | -52.968201 | 2024-12-11 00:31:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f29a9d6e-be20-3d65-bb02-6656002f6c6a | -6.9093 | -43.498001 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ec2cac54-4c4c-3dd9-afc4-86f29ebc107c | -3.1231 | -54.085701 | 2024-12-11 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273fda16-c0f3-3354-b0b4-9bf89b65b064 | -6.9747 | -42.983898 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb8a8075-d658-3d99-87d4-e7d1e4ada800 | -3.2435 | -42.427502 | 2024-12-11 00:31:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df271d32-e331-3094-93c0-8ddb1f60927e | -6.8852 | -43.5275 | 2024-12-11 00:31:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6cbf972a-2a37-326b-842f-d131192aeac3 | -6.9551 | -42.9884 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 763cb27b-4020-36f7-a9e3-f4f88683597e | -6.164 | -44.4212 | 2024-12-11 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1871001b-f2ab-37d6-89dc-778ecd7aea5d | -3.1265 | -54.101002 | 2024-12-11 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad931b10-f854-354d-9a72-4bcfc1842227 | -3.2413 | -42.418201 | 2024-12-11 00:31:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f0c2f46-d8dc-383b-9ff8-9a6e6be64524 | -3.6025 | -53.715401 | 2024-12-11 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92e6496b-f826-31a3-8878-b808c7706e3f | -6.9491 | -43.006599 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2fbaa169-4e46-3c60-aa9a-b1721dbdbbe6 | -6.9589 | -43.004299 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ee37503-ba9b-37da-9077-5653a7bd7c08 | -2.6102 | -54.2132 | 2024-12-11 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da241fb1-4db6-3c1c-9f4d-56dd954d32f2 | -6.2968 | -43.837101 | 2024-12-11 00:31:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cb24e8b-8f47-3416-9841-35f990f7fd88 | -3.0731 | -40.045799 | 2024-12-11 00:31:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f9960474-319e-3a1d-bedf-1603ba28930f | -11.4642 | -44.9501 | 2024-12-11 00:31:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21211faa-1798-378a-8963-5f056479bef3 | -11.0467 | -44.563999 | 2024-12-11 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26b0b2ee-ed67-346a-a0ee-2a5c7a82542c | -6.895 | -43.5252 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51f80906-2ed5-343b-9fb5-f7904aa2b26f | -18.106501 | -40.135899 | 2024-12-11 00:31:00 | METOP-C | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40a3db06-b550-37d7-9806-3e1d416da26b | -3.321 | -53.232201 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0e8ffa-fcf5-3342-9d2d-7f3e2ddbae85 | -3.3371 | -53.0756 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd17ac7-d582-3003-92d8-eea42db51bc5 | -12.419 | -43.797199 | 2024-12-11 00:31:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5cb5b4d9-f74d-3bbc-a53c-e94d21db74a6 | -6.9785 | -42.999802 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 628fd646-b40a-3f94-b6d0-0e6298e7008a | -5.9798 | -44.6059 | 2024-12-11 00:31:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9afe265-ddb2-3b64-9864-e9fca6cc09a2 | -6.9472 | -42.9986 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3fac9dbf-e4f6-3f41-a588-51420d14cc0b | -11.8299 | -43.838299 | 2024-12-11 00:31:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0558c1d-7c48-379a-954f-f0583888e52a | -5.6026 | -41.327999 | 2024-12-11 00:31:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 62cbc562-59a4-3605-badb-731ad7561899 | -3.1197 | -54.070499 | 2024-12-11 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d60cb36-f812-3e77-965f-9855c043a140 | -3.3307 | -53.230099 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
