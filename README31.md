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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f149ee47-077d-338f-95b6-71001efa2822 | -17.1571 | -57.4198 | 2024-10-07 01:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 138.4 |
| b07d82ab-bedd-3675-8d4b-0dd091ff731b | -17.1581 | -57.3582 | 2024-10-07 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.4 |
| d3435eda-4b41-37a1-8d08-e8be73ef6216 | -17.1584 | -57.3377 | 2024-10-07 01:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 2ce17958-62e8-3494-9d83-bc0cf05c2b12 | -17.6279 | -53.1094 | 2024-10-07 01:46:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 145.8 |
| d7a79a8f-bed8-35d6-8025-53c8edf7f917 | -17.6283 | -53.088 | 2024-10-07 01:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| e5f5238e-5922-3227-9d60-9c1f25de25c7 | -17.6477 | -53.1064 | 2024-10-07 01:46:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3546ef0f-ac68-3d56-95f1-8733a7851d2e | -17.6481 | -53.0849 | 2024-10-07 01:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ee437556-a63c-3f5c-805d-8e50b7b53c5f | -17.6679 | -53.0819 | 2024-10-07 01:46:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 121a2bc0-6802-3237-9ed9-61be5f5977d2 | -18.4518 | -53.5165 | 2024-10-07 01:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0283f99c-028c-31f3-8542-bee39f0077ca | -18.4523 | -53.495 | 2024-10-07 01:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 40b38e51-87de-31fb-ba44-d969aae0a3fe | -18.4718 | -53.5134 | 2024-10-07 01:46:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| dd3951a7-78a8-3e77-85ae-e5a9e16d7542 | -18.8886 | -54.5587 | 2024-10-07 01:46:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8a5f8df7-e8d4-331e-b464-c1273cfba8fc | -19.8318 | -42.3542 | 2024-10-07 01:46:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| 8980d94a-5bc1-3147-bee3-0dc6c6736171 | -20.1223 | -49.0748 | 2024-10-07 01:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c33e6a3f-3a8f-3eae-9aff-c7364c21a27a | -20.1229 | -49.0518 | 2024-10-07 01:46:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 204.6 |
| e804537b-558b-337a-bbf0-ad19dfa3feef | -20.4449 | -47.6875 | 2024-10-07 01:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 63941626-d251-33d5-8ab9-1308ef077098 | -20.4456 | -47.664 | 2024-10-07 01:46:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 197.2 |
| 251fce1a-00c6-3a36-9722-97fd7a4933d8 | -20.4655 | -47.6827 | 2024-10-07 01:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 169.0 |
| f344a4a1-9da0-310a-aa13-05d4663e4e59 | -20.4661 | -47.6592 | 2024-10-07 01:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 503.0 |
| 471e3696-5096-3989-b7ab-d94246bc4d68 | -20.4668 | -47.6357 | 2024-10-07 01:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3d603ff1-4ad2-3428-bf4e-04f39cda476e | -20.4866 | -47.6544 | 2024-10-07 01:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 1722fc5b-640f-3ec7-9599-262c86d6659b | -20.5848 | -48.5137 | 2024-10-07 01:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 638f8167-c901-36bf-8bd0-c7945cfccc52 | -20.5855 | -48.4904 | 2024-10-07 01:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 170c6eee-5188-3249-8e52-df0daac2306d | -20.6053 | -48.509 | 2024-10-07 01:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 161.0 |
| ffdb9f0c-aaa3-30ef-8280-a08f9b0fbeee | -20.606 | -48.4858 | 2024-10-07 01:47:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 455.5 |
| 971b91b7-a3a0-3005-aa6a-61014b131c74 | -21.0712 | -47.2331 | 2024-10-07 01:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 038a2ecb-59a9-37c8-9627-0f70619f5713 | -21.0919 | -47.228 | 2024-10-07 01:47:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 53.5 |
| fddf1bb8-6f9f-3791-96a1-9b6c00a56835 | -21.5843 | -47.9536 | 2024-10-07 01:47:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 120.8 |
| fc1da1b9-7ac6-3810-93c8-f8ef9d328656 | -21.605 | -47.9485 | 2024-10-07 01:47:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| a978ef9b-452c-3c0a-976b-59f47a5ee855 | -21.6529 | -47.7255 | 2024-10-07 01:47:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3e0900a8-aeba-308b-8785-a03e91af1914 | -22.9341 | -48.58 | 2024-10-07 01:47:12 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 56a3d203-117b-3a51-86f9-5be57ed62cc2 | -22.9551 | -48.5746 | 2024-10-07 01:47:12 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7fb5bb1f-ec02-3c84-be59-8fdad5eacf3a | -22.9558 | -48.551 | 2024-10-07 01:47:12 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1f2b15aa-ff18-32e3-a6e1-dea309c2a274 | -1.0365 | -53.7389 | 2024-10-07 01:55:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 923e0f15-2008-3a45-b29f-b1816dd8c379 | -2.2113 | -53.7029 | 2024-10-07 01:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 6cb81f11-15c5-309f-a1ec-de59825b62b3 | -2.8569 | -52.9197 | 2024-10-07 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a7f21ab2-2dcb-3528-b02a-370f1ad64294 | -2.857 | -52.8993 | 2024-10-07 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 33764095-6304-3479-9cf8-60f2d222795b | -2.8753 | -52.9192 | 2024-10-07 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 338f0396-1400-3b36-b7eb-d1af536f45ca | -2.8754 | -52.8989 | 2024-10-07 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 778b9dc2-3e3d-3eb4-a6d2-7335d630cdf6 | -2.8937 | -52.8984 | 2024-10-07 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0e673226-aed4-36f2-84e0-1996ed2188dd | -3.538 | -65.0414 | 2024-10-07 01:55:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f1e17a22-539d-3d47-9afb-0e87c88e7962 | -3.5381 | -65.0229 | 2024-10-07 01:55:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 12729fbd-99d7-3139-b17a-75e01f0fb82a | -3.5563 | -65.0227 | 2024-10-07 01:55:27 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1778b483-9327-3ac1-86f6-da3c52f53ef6 | -4.2542 | -43.7381 | 2024-10-07 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e73784d2-5486-3b7c-b90a-675339bb52ee | -4.2728 | -43.7601 | 2024-10-07 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 80accb4c-a69a-39d3-b055-55945525b47f | -4.2729 | -43.737 | 2024-10-07 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 9c7f0414-61ec-398b-a551-acb2c2c60354 | -4.2731 | -43.7139 | 2024-10-07 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| fdbbbb5e-6f51-3d0d-a6e7-11e5c971c2e8 | -4.2916 | -43.736 | 2024-10-07 01:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 660dc18a-d958-361f-b249-77a11a40da85 | -6.1116 | -47.2457 | 2024-10-07 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 973ecc3d-fce5-32ed-aed0-705975752edd | -6.1118 | -47.2237 | 2024-10-07 01:55:41 | GOES-16 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 60472a06-a449-3d9f-9d11-2f50ccc937a4 | -6.1302 | -47.2444 | 2024-10-07 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0660355d-7a38-3abc-a9cd-41c5ebaa3ba9 | -6.1304 | -47.2224 | 2024-10-07 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| f9969e9d-34ac-3b84-9b4a-1460e94f920a | -9.5152 | -40.331 | 2024-10-07 01:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 8a77c040-3723-391c-b379-6ea254170f29 | -9.5343 | -40.3282 | 2024-10-07 01:55:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 177.6 |
| 512a5f74-2f37-3731-a3e9-f79c9e9f57fa | -10.8754 | -63.9169 | 2024-10-07 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 7358df25-914e-37ef-b717-f3b6f1b7c8af | -10.8755 | -63.8979 | 2024-10-07 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 34688fdb-6bb8-3970-86b2-4bb50fb75c18 | -12.0585 | -63.7841 | 2024-10-07 01:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f1de3e49-004f-3e19-9c2a-c4bdbf32cc7c | -13.5719 | -50.3223 | 2024-10-07 01:56:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 186.1 |
| db962099-6fe9-34ce-80b8-65067477bb14 | -13.5723 | -50.3006 | 2024-10-07 01:56:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 240.6 |
| c043ac8a-c906-3501-84ef-148048769432 | -13.5911 | -50.3197 | 2024-10-07 01:56:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 182.3 |
| 9ef66a73-7e94-364b-b1d1-09bd0519490b | -13.5915 | -50.298 | 2024-10-07 01:56:23 | GOES-16 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 236.1 |
| f43e2d50-4534-3dd4-ab59-1aa700f62728 | -13.7342 | -60.6471 | 2024-10-07 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e3fb757d-a7ef-3fad-9758-1118fb3f06ca | -15.0422 | -51.24 | 2024-10-07 01:56:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 016277cc-880e-3937-a7ba-0253bc7080a6 | -16.4877 | -57.7408 | 2024-10-07 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 223.4 |
| 564714f7-f172-39b5-9c48-9b03faa92fce | -16.488 | -57.7205 | 2024-10-07 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.4 |
| ea26e8e1-7f3b-3c3d-96f3-5f1eec4dfddd | -16.5072 | -57.7387 | 2024-10-07 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 284.7 |
| 980a68cd-a137-30cd-9ce8-20af9b0c2040 | -16.5075 | -57.7183 | 2024-10-07 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.7 |
| 0308d3b0-16c3-3db7-b7d4-6d27c67b0e4a | -16.5267 | -57.7365 | 2024-10-07 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 126.8 |
| b64d2459-3fb1-3b9d-96da-ed9bd0b8384e | -16.527 | -57.7161 | 2024-10-07 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 848818d1-c9cc-3f43-a729-758d2b932ff8 | -16.6136 | -57.1555 | 2024-10-07 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 10907e2e-2ab4-38d5-93d7-61b98a5fa559 | -16.6332 | -57.1533 | 2024-10-07 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| 7a44fda1-ca67-3ddd-b473-7b1d810faa33 | -16.8051 | -57.3993 | 2024-10-07 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.0 |
| 5ab94850-a181-3a3c-95cb-7cdd6be64330 | -16.8055 | -57.3788 | 2024-10-07 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| 78021df2-ff25-3b94-af33-8579e0fb653b | -16.8238 | -57.4584 | 2024-10-07 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 98398b12-6d9b-3782-80ef-47d5a983179f | -16.8241 | -57.438 | 2024-10-07 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| d298ed88-9548-38bc-9043-b1a0425a8ff5 | -16.8247 | -57.397 | 2024-10-07 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.3 |
| 8fa6dc35-e1e8-3e7f-a430-89a61681775d | -16.825 | -57.3765 | 2024-10-07 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 128.7 |
| 286e4f96-a7fc-3df8-8593-2c2f2c86ec8a | -16.992 | -56.721 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| d14d8352-49e0-32f4-ad27-c2b13feaf63b | -17.012 | -56.698 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.2 |
| 63162971-b27a-3af9-9b08-fc84ca4f1e3b | -17.0685 | -56.8352 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.3 |
| a936afc7-35f4-3e9a-8efe-3f77f5b95fe8 | -17.0881 | -56.8328 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 151.6 |
| 68e944f5-0ed6-3e03-8c86-457d47bc4da6 | -17.0982 | -57.4267 | 2024-10-07 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 143.5 |
| feeb29fc-b1c9-383d-b2d4-e69422a7ba33 | -17.0985 | -57.4062 | 2024-10-07 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.4 |
| e779b738-68d6-3de5-8071-ddc37f076ed8 | -17.0989 | -57.3857 | 2024-10-07 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.6 |
| d85bfc48-22c8-3e40-ba3b-f2402b47ef0f | -17.1074 | -56.851 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.6 |
| 4010ab74-c1e8-3768-99ef-aa6d79b04dbb | -17.1078 | -56.8304 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| 96194625-14b7-3345-9111-0220e47f1841 | -17.1182 | -57.4039 | 2024-10-07 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 6ad73750-0b76-3bcc-bacb-71577332dcbc | -17.1274 | -56.828 | 2024-10-07 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.1 |
| c1bcd89b-4a13-3e23-b12a-f1a432684eee | -17.1375 | -57.4221 | 2024-10-07 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| b09953b1-0136-37a2-81c7-eb609b8d3f74 | -17.1571 | -57.4198 | 2024-10-07 01:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.7 |
| 26ea1021-d229-306b-9cf1-e6d0afafec7c | -17.1581 | -57.3582 | 2024-10-07 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.6 |
| ba0395c8-1b2d-35c6-8b91-5a036acacd0e | -17.1584 | -57.3377 | 2024-10-07 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| fa4b5e35-0fd1-39b4-aa14-6776cc19027e | -17.6081 | -53.1125 | 2024-10-07 01:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 98268c89-cf86-3736-b152-8d9a39df4053 | -17.6279 | -53.1094 | 2024-10-07 01:56:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 312.9 |
| 5d39e294-c289-3467-bdae-5c95337b72d1 | -17.6283 | -53.088 | 2024-10-07 01:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| b94452fd-31e9-3f84-8b3f-dfa2299db840 | -17.6477 | -53.1064 | 2024-10-07 01:56:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 7e1cae7f-5429-3f73-81ef-a5c6bd690a77 | -17.6481 | -53.0849 | 2024-10-07 01:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1288ad3c-63d7-30aa-b045-a16176b9b96e | -17.6679 | -53.0819 | 2024-10-07 01:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 117.8 |
| b892a4e6-ccb9-368a-9c78-d54823f78713 | -18.4518 | -53.5165 | 2024-10-07 01:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d3c6e642-2961-3f2e-8b51-e7164106b4fb | -18.4718 | -53.5134 | 2024-10-07 01:56:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 120.8 |


[Clique aqui para ver as próximas entradas](README32.md)
