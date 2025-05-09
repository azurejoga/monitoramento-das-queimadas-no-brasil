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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9ee02c7-7823-3d44-9d93-4f5108a179b6 | -7.88988 | -61.46678 | 2025-05-09 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e78f24cc-6786-3677-99f6-fdd23281f833 | -14.30913 | -54.65784 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93a8264a-ce6d-39c6-b168-84142fbbd436 | -13.03477 | -45.07978 | 2025-05-09 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e72c671-873f-34a5-b46f-b60ba52e1bdf | -8.90929 | -50.01435 | 2025-05-09 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12115516-d2b7-3ffd-8cf5-10af3f161346 | -14.64153 | -45.12138 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 544dd394-b8b2-3641-bd20-e8447a0e1619 | -11.51257 | -48.21666 | 2025-05-09 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d7eb660-1b5c-39ed-8089-3f419e61770e | -13.04415 | -53.72813 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 825d39db-71f6-30c8-9031-cff48794b16e | -15.82642 | -46.57328 | 2025-05-09 04:40:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc8d2927-a024-33fd-978c-76893f6623df | -13.03055 | -45.07918 | 2025-05-09 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bca93005-a505-3e66-9ec0-f740c19ee838 | -12.35107 | -52.48779 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f149ebcc-abab-388f-b211-5c4beb0b72f4 | -13.79966 | -53.30016 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdc252f6-3f0b-3a70-bfaf-84a78d0b924e | -12.17397 | -54.23932 | 2025-05-09 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d9ac9663-7a0f-39e9-8ccc-e8d83d777939 | -13.50295 | -52.96807 | 2025-05-09 04:40:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6e610a0-c868-3bf4-b9f0-cfa9c218a2ef | -15.57031 | -47.85596 | 2025-05-09 04:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13609032-f853-382e-ba33-5db4af8d7689 | -14.20448 | -45.46555 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f0e54c4-00ea-336d-942f-0a342117e996 | -10.05972 | -50.59527 | 2025-05-09 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2881b7f4-0ae1-3c0c-ba6a-04e69440520d | -13.37002 | -54.25513 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25eec56e-8c7c-3bbf-bfc2-971f15dbf3a8 | -12.35785 | -52.48892 | 2025-05-09 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e599cca4-173e-37e7-b40c-ef7d1d3a7950 | -11.56162 | -47.61592 | 2025-05-09 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04dcd8b6-b5c2-3365-a867-743a2d271614 | -11.40067 | -52.94796 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 525c703a-5496-36fd-90a6-d11e81882459 | -10.48762 | -59.15324 | 2025-05-09 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34a4a725-9854-363a-89b9-72265bdf26e9 | -11.38742 | -52.94172 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a1f17517-1e11-3e89-9d2b-ffeeeb63abc1 | -10.96905 | -44.44109 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a029138-7ed6-3d84-89b3-80420a0032e6 | -13.05187 | -53.72534 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be25a3ea-b465-367b-b31d-b7c71ade365f | -12.11501 | -47.98814 | 2025-05-09 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b81ca6c9-7e4c-3f8d-9e3c-57a34cea73ca | -10.97875 | -44.4341 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2de0a916-97b1-3100-8461-923204c906b6 | -11.40414 | -52.94855 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18dd53de-6cd1-3240-ba55-7d1bc4e512a6 | -11.39373 | -52.94678 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 06fda03e-f416-38e5-91ed-b5f356be7c98 | -11.07366 | -46.12701 | 2025-05-09 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3279d7dc-eb3c-3f97-a6ea-f8275516c393 | -11.4035 | -52.95245 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d84adc24-3ac7-3c86-9bf8-5e3ca394647a | -10.67145 | -44.37932 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 09135b70-0da2-3e14-8b1a-5df28e2c1639 | -12.83298 | -47.40494 | 2025-05-09 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1074719-ed28-338a-ae98-c9c937c0ad45 | -11.25983 | -52.47649 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b24c90c1-b334-323f-a79f-203bc67085ad | -12.6461 | -54.06771 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6fbf00e-2b5f-3ba8-9011-2879db8f78d0 | -13.04834 | -53.7247 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be084d12-6c38-3fa4-8c3e-88ce79676afe | -11.62354 | -54.93921 | 2025-05-09 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96420288-31d2-343c-91d7-eb8a6824ab9d | -12.11853 | -47.98869 | 2025-05-09 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89b29807-f532-3731-bcb3-5f6aa78938ab | -11.36197 | -55.12526 | 2025-05-09 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a86abd0-79db-3040-8671-45f22f9594ea | -14.64474 | -45.13037 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bcc7e18-c182-3f4d-a464-2301fbecec57 | -13.3729 | -54.26001 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ffc43a4b-ddd1-3ddc-a778-04025e808997 | -12.33196 | -55.16226 | 2025-05-09 04:40:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7e3e007-c212-38aa-abae-40db48a71200 | -14.20397 | -45.46948 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbd1c51a-1ae0-3f65-8840-a92f9f4ba327 | -12.63097 | -54.06953 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0838f058-3249-3fa3-8da1-1e6032f5c9f3 | -10.67042 | -44.37751 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f1c572c6-669f-3c81-935c-89a931f40718 | -14.2008 | -45.461 | 2025-05-09 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 842baa44-d63d-3f66-9378-473453f03daa | -13.37939 | -54.26556 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 85add449-9f4f-3a29-b7c1-31c3c2c468e5 | -11.38308 | -55.11879 | 2025-05-09 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2a31336-262c-372f-85c7-2951046c8aac | -11.53631 | -54.35991 | 2025-05-09 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 154d8820-0c95-32c5-8433-ab14ad828674 | -14.64099 | -45.12558 | 2025-05-09 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3f64778-82c9-3e37-a961-37e8342d2d8c | -11.35807 | -55.12461 | 2025-05-09 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43bf3a56-8915-3cf7-bd90-9800167dee11 | -13.0413 | -53.72344 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ae01446-6d76-3052-8ef1-5c18788f4ea6 | -13.37434 | -54.25146 | 2025-05-09 04:40:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f49cc26-aca9-38be-b99f-34448751eda0 | -10.97818 | -44.43819 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fac2bcf-a2cf-368e-a3f3-a391d999d4d5 | -12.32154 | -44.5116 | 2025-05-09 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f5d4dee-d5fa-3618-8ef8-c733cd6089c6 | -13.04902 | -53.72065 | 2025-05-09 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea877d05-c0bc-3c6a-8d20-6caefbae536f | -8.67063 | -48.27874 | 2025-05-09 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd72959d-d5af-3327-9d43-994e02532ca5 | -13.66758 | -43.72632 | 2025-05-09 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64de0df3-076a-3306-8cf7-fb87ab4e88c2 | -10.97276 | -44.44579 | 2025-05-09 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0eca0bd5-81cf-3147-bc12-2ff595b115f5 | -11.40761 | -52.94915 | 2025-05-09 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c47d2b80-7726-34ba-b4d5-357abf59be25 | -22.6761 | -42.85477 | 2025-05-09 04:42:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 85a02db5-5ac0-3b58-842b-7f61dda9e02d | -18.71542 | -47.17285 | 2025-05-09 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96a98954-76a2-3919-af85-308828ff4138 | -18.28428 | -53.00196 | 2025-05-09 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eda72636-4596-3eed-9070-f44cdeca18ed | -21.89167 | -47.19525 | 2025-05-09 04:42:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0cceae72-68d6-3b94-a2b5-179de6c79404 | -18.87625 | -52.42401 | 2025-05-09 04:42:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfe3e8ed-1232-3bdb-b32e-e34e8bf74e35 | -21.18121 | -48.68208 | 2025-05-09 04:42:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cbb992d6-1278-312f-9ed5-a6a22e3f9993 | -18.26317 | -53.00579 | 2025-05-09 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe01f1b2-30c5-3ce5-a057-004d3ec48404 | -17.2332 | -47.38991 | 2025-05-09 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 768244e8-41ff-33f6-bd2b-ec82756b3bc7 | -18.25985 | -53.00522 | 2025-05-09 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1286b9f6-2551-3929-bee9-e2e9cd2f3ded | -19.56597 | -49.6814 | 2025-05-09 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b0c40e41-98b5-32d6-8ee4-b7b2ffd3561b | -20.47936 | -55.83848 | 2025-05-09 04:42:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 781d0f83-8bf6-3b1c-8b2b-a57d5b98e7ea | -16.68081 | -43.88412 | 2025-05-09 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2badbf73-567d-3f32-9e2e-1ab766603e81 | -19.9838 | -47.19466 | 2025-05-09 04:42:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e628e430-0e62-32f1-9c72-c8373e7a3c1d | -19.84708 | -54.22139 | 2025-05-09 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea5eab05-9f64-32cc-8797-217bd8dad426 | -20.47754 | -53.67422 | 2025-05-09 04:42:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 919eba8d-bf97-3f07-b596-0d9a69f177a4 | -20.17268 | -49.68169 | 2025-05-09 04:42:00 | NOAA-21 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| aaef5641-e199-3899-ae10-00c33e37d278 | -20.06466 | -49.36299 | 2025-05-09 04:42:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d7de38ba-210e-3bec-9c45-0d359aa3f1f2 | -19.56598 | -49.68389 | 2025-05-09 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 145354e4-8f6a-33b3-87db-6718d93f7796 | -21.18186 | -48.6772 | 2025-05-09 04:42:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ff92a21d-ed5e-3bf6-9d8a-e12fa2e57d6c | -21.39289 | -50.47646 | 2025-05-09 04:42:00 | NOAA-21 | BILAC | SÃO PAULO | Brasil | 3506409 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6da8f17-e4db-3244-be8a-950ed2b36880 | -21.05294 | -55.9972 | 2025-05-09 04:42:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1982880f-15f0-34ef-951b-51f1ea3c20ec | -17.53259 | -52.12068 | 2025-05-09 04:42:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8f2a8db-0285-3e42-9cfb-1ae8a47a4a72 | -19.84307 | -54.22459 | 2025-05-09 04:42:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb763333-d040-3f0e-828c-9b1f317e4bc3 | -15.36372 | -60.16822 | 2025-05-09 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2565fb-235d-31b6-9508-07413ece30b7 | -17.68589 | -48.63974 | 2025-05-09 04:42:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 255e54ee-409d-3cd5-b8e7-c6d352455129 | -17.75888 | -52.43325 | 2025-05-09 04:42:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a043b8ea-b675-3590-80c8-fe3502b88e96 | -17.52928 | -52.12012 | 2025-05-09 04:42:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bc011f8-7cef-363f-84f0-543435d389f5 | -19.15922 | -47.81914 | 2025-05-09 04:42:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b35afddc-62b3-3cb9-bddb-4476f2a7617a | -17.53645 | -52.11764 | 2025-05-09 04:42:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27aa28e9-8ea3-3d77-8923-d61e7c0ce44d | -16.60769 | -53.39935 | 2025-05-09 04:42:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e30225ce-d334-37d4-b76e-0af4be635466 | -16.38277 | -54.57764 | 2025-05-09 04:42:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 388c4c68-d7a9-346e-a3d6-4951bac0e67d | -18.50072 | -47.6021 | 2025-05-09 04:42:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 744eb6bf-2cd7-3877-abf5-1c69c6e483ce | -20.06047 | -49.36682 | 2025-05-09 04:42:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ae3d62bb-58c2-3729-85ae-0da4168d26f9 | -19.1608 | -47.82056 | 2025-05-09 04:42:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50688f9-0fa4-3ed1-aef0-56f6ddd99a2f | -21.24035 | -54.60539 | 2025-05-09 04:42:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e0db983-1491-394c-889f-bc4c1f5cb7fb | -21.0522 | -56.00149 | 2025-05-09 04:42:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b94061ff-699a-38cb-b80c-2d616bbdb099 | -20.06097 | -55.77528 | 2025-05-09 04:42:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b95654e-0914-3af7-aeea-3b3462e0f1e0 | -18.43159 | -50.33649 | 2025-05-09 04:42:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 28621883-4103-3629-990d-ab3ad9f3ec33 | -21.39737 | -48.53252 | 2025-05-09 04:42:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1265f517-7004-357a-ba27-0af4edb5a1ee | -16.10669 | -59.7732 | 2025-05-09 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19dda57b-168d-3216-9a36-8bb2eb79294a | -17.36155 | -52.01768 | 2025-05-09 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
