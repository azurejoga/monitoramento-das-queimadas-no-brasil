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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d00818a7-dff4-3550-b7a3-8681225d0642 | -6.02328 | -57.77918 | 2025-10-17 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d66a4f1-3c4b-37d6-a111-81920613ac86 | -7.95687 | -44.11657 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8ceb9d2-095e-3845-a25e-9d127601850e | -10.87561 | -55.99613 | 2025-10-17 05:10:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f55f2af-5d97-3aa9-80d9-d1b7eb56cb15 | -8.49476 | -48.49677 | 2025-10-17 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b09f2524-5686-39c6-8ec9-643d3941c259 | -13.43961 | -47.95163 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 299160b8-94b7-3c7f-97e1-e50184542129 | -10.85214 | -51.29119 | 2025-10-17 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e593f07-eebf-332f-b8a0-3faff8157f00 | -9.28878 | -46.9051 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f34f2844-1187-3e77-b2b1-7c7df595940c | -11.19066 | -51.75989 | 2025-10-17 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0496db0e-1540-3c7a-84c4-ae0714e8623d | -9.14258 | -46.64378 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1b64327d-1821-31f3-9340-fa9beb56a86e | -9.73277 | -62.95303 | 2025-10-17 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 617728ad-f164-3503-a393-ef08493116ff | -9.13543 | -46.65166 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27c788d1-75d2-3e2e-90e9-de5723de473e | -9.3093 | -46.9342 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beab57ee-49d2-3f49-bc05-1e440f7ac4a4 | -9.72877 | -62.95233 | 2025-10-17 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d96584a6-5d48-3445-b380-f482bbeceaea | -9.7218 | -48.91568 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bcbef46-21fc-3beb-a94a-2b9452b0225d | -7.34236 | -43.86867 | 2025-10-17 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f8895eb2-ae87-34c6-8d73-dcc87e4e5c3d | -7.95093 | -44.11469 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a773a928-373d-331c-9499-c2f07abefa0b | -10.10397 | -56.77021 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eac98f34-a265-3d07-89be-9dfd2f50a366 | -10.27172 | -44.04053 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c380bff-3a62-3ac2-9c77-5bc77f35c315 | -7.94661 | -44.14811 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce5117ca-e207-39e3-9cb1-3e912c583b60 | -8.47205 | -50.10693 | 2025-10-17 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c48c572-65ab-3b4a-b64e-f856d16d5974 | -10.15658 | -44.54269 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80f0c590-2204-30cc-8ad0-cf39586d83ff | -7.3344 | -44.15602 | 2025-10-17 05:10:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20a06904-2cea-3c1f-a96c-cb03e3abf06e | -8.25565 | -44.03522 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f86fac26-032e-385d-8473-846088107586 | -8.23536 | -44.02611 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b1f62cd-7d3a-3149-bc23-bc21efa46a5c | -10.95586 | -49.76996 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 69bf775e-4147-36dc-909b-f3995a296553 | -13.41854 | -47.94053 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ae85071-3cc8-3924-946b-d174f855f70e | -6.94612 | -47.72018 | 2025-10-17 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f844a341-5998-3479-83d4-189ba3a96295 | -9.09329 | -46.68039 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126b65b7-edd7-3351-80d8-7d9d15870c19 | -8.47276 | -50.10173 | 2025-10-17 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e397864-bdec-34d1-be44-b6fde5d1ee1a | -6.20263 | -52.73623 | 2025-10-17 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aab884cf-601c-3586-b89f-d14f22734038 | -12.42933 | -51.29962 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acff994c-58aa-35e0-8433-aa94ce06083c | -7.35098 | -43.85683 | 2025-10-17 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a3962e25-c7d9-3332-8ac2-6acf5fb2dbe3 | -9.26557 | -45.27651 | 2025-10-17 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92dfe29c-946c-39df-a856-ecb4b30f4cfe | -13.43323 | -47.96805 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b71f5422-e13c-3cc7-9840-58fb90fd33d9 | -10.29269 | -44.04833 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 13615058-6117-3fdc-a276-18cfa98b820c | -10.2958 | -44.04639 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3590da36-3361-3277-82fd-fe740b58de2e | -8.15858 | -47.98127 | 2025-10-17 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57dbe1f1-009b-3bce-bb23-1cea17045e54 | -11.29537 | -56.48465 | 2025-10-17 05:10:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7726a948-f44a-3fdf-9821-5a3c32aaa205 | -8.40172 | -46.23866 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 821aec31-58ff-34ee-b9af-9157234d0fe7 | -10.2807 | -44.05088 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e44dee2-3803-3ae1-b987-1e346911af42 | -10.38811 | -57.50161 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 930904a3-e64b-3836-939e-fa79adfc7413 | -7.12123 | -55.6655 | 2025-10-17 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ad0000a-fb38-3d14-bae0-96b624af208a | -7.90553 | -50.39074 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb5120d3-1fad-34dc-9b1f-a13e900ce60a | -13.39598 | -47.22118 | 2025-10-17 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8db3e732-a7d6-35c8-a028-333c36641729 | -9.29734 | -46.93265 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54401c0f-03cb-3bf4-8e86-cb5b8f3d8df2 | -11.36664 | -54.32516 | 2025-10-17 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec66828f-003b-3478-b562-958deb8b0401 | -7.17421 | -46.93595 | 2025-10-17 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2937fb7d-8247-3ae8-aa98-b19e72cca6b8 | -13.44029 | -47.94551 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc6bfcf-e380-327f-acf1-5a51b56660b5 | -9.12899 | -46.64309 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c611b7f9-55fe-33cc-a8b1-e413310a2279 | -9.06273 | -48.84805 | 2025-10-17 05:10:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa8306e8-9591-3a9f-83d9-b66094bb2e35 | -9.919 | -57.69951 | 2025-10-17 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cc5bc714-6d4e-3f41-8d1f-0e4609775c73 | -12.20135 | -61.83443 | 2025-10-17 05:10:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dea1944-847c-3cf2-98fd-220d706e22af | -13.42482 | -48.58678 | 2025-10-17 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5c0f858-272b-3756-8da3-71fec082488b | -8.55711 | -44.58725 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9303458d-870d-3e99-962d-44d8c58a12fe | -8.08468 | -45.42032 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3546c65f-2155-3972-a32b-9e47a177f3d1 | -7.35017 | -43.86337 | 2025-10-17 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 21d417ed-521a-3142-88e0-78455ef13a0c | -13.44619 | -47.9463 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e7ef724-049f-3c68-9d1b-8eea01740025 | -7.34317 | -43.86216 | 2025-10-17 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0641a97d-9565-3724-993a-16c00039905d | -12.42402 | -51.30394 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 43e1dee2-c54e-3a7e-916f-e3051f57fd37 | -8.8229 | -47.30529 | 2025-10-17 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddd6ab05-4389-3ace-9be6-ba2429c81a5c | -10.13341 | -44.54745 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f7131dd1-e709-3f14-a9b6-6e69b50369eb | -9.61898 | -49.12605 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aaf8724-8465-3ad6-8e95-117cdeed69ca | -9.63385 | -57.85017 | 2025-10-17 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ff27402-e714-3052-b289-e869a7612825 | -10.12645 | -44.54639 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 330f2030-eb3f-3b13-939c-3547dfecc4a1 | -8.3786 | -46.31988 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2402d65-c118-38f5-9c87-8a266a94ec1e | -9.64182 | -55.13323 | 2025-10-17 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c587c269-e399-3780-806f-c0780ac3d1ef | -10.14951 | -44.54253 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75cf6aad-b537-382b-8935-412d05ba0f5e | -8.72802 | -43.87873 | 2025-10-17 05:10:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a834c63c-7342-339b-8fd3-ac0467fc53e1 | -9.09267 | -46.68514 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 521b9943-9c43-3788-a70d-7bdc9808eace | -9.13997 | -46.65348 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 44a0758a-8403-3ec4-854f-074617039f32 | -10.41908 | -59.69361 | 2025-10-17 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78076646-b8eb-32d8-9f9d-56bc955ed35a | -10.95001 | -49.77523 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 47c48197-5291-3b57-a190-6ba2ef7f676b | -8.6249 | -54.56509 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c17ea8f-d097-3b7a-be25-ce3c933c77ab | -7.69044 | -55.17299 | 2025-10-17 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a4b6921-cb70-3b97-9560-576a189d8eea | -8.24326 | -44.02011 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd326493-eebb-3e1a-a2b7-2427be71d915 | -10.23416 | -49.86703 | 2025-10-17 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0f713ab-5dc1-3320-9d29-9d8336c9f4be | -8.8224 | -47.30584 | 2025-10-17 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79167ed7-b787-37d2-b7ce-824ad6815f0a | -13.42404 | -47.94465 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7e8825f-d670-378e-a64d-dec0520d92ae | -6.94561 | -47.72379 | 2025-10-17 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 356a12c4-ea79-33ec-a081-cb77b89d76b0 | -8.0878 | -45.44675 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a25c8ad-d389-3391-9840-5dda890c34d3 | -9.14482 | -62.30112 | 2025-10-17 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0fec26d-e12f-3486-ac00-b0d6802539c4 | -8.15309 | -47.98049 | 2025-10-17 05:10:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e26efaa9-11b5-361c-b0d1-9d713a1c6acc | -13.42254 | -47.94357 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36ad3720-2037-3167-9a5f-38b87d7578e8 | -9.33913 | -46.91469 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 068cbb34-c4ca-3b89-a0b5-f3381aa2abd3 | -9.44637 | -56.65367 | 2025-10-17 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32060620-3380-3448-a90c-b24028465f4a | -10.13611 | -44.5852 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 279d7c46-c6c7-33b7-ad06-4c0f9d4cbdf7 | -10.28189 | -56.4738 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13b9dc37-1df4-3cd6-a738-b67938985d94 | -8.64211 | -54.59739 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b1f6a7e-21f6-3d88-84b9-e2bc9af56a4b | -9.24564 | -44.36011 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d4ea894-6ceb-3a83-bc9c-95124beeec80 | -10.2556 | -44.05354 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03ef3cd5-b629-3882-aa49-2171d4e0c924 | -7.3344 | -44.15779 | 2025-10-17 05:10:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c094b8f-607e-3838-b4d1-e3af5554cb72 | -10.9206 | -47.86492 | 2025-10-17 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2222333b-5631-30e9-89bd-d8cb9d9b33fe | -10.42841 | -45.02417 | 2025-10-17 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 482ae84b-6423-315a-b618-e4f676f2e09f | -10.95704 | -59.12218 | 2025-10-17 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 198b202a-c9b6-3c8e-9e34-096534ea92bb | -12.42273 | -51.31383 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e34e654d-761a-3630-a762-27a407df8699 | -10.95119 | -49.76631 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 666c6e4c-64ce-392e-be5e-e565ad257fb5 | -9.13502 | -46.64417 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 741cadbb-e23f-3509-833b-58358f1f70e1 | -9.13561 | -46.63968 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15dd0751-3c6a-34f2-8b75-0c80d4f93fbc | -10.8567 | -51.29181 | 2025-10-17 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef87a18-a321-322f-a319-73a394f3ee09 | -8.44984 | -46.24855 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README110.md)
