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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e096984b-fa20-3b89-a319-56092f166219 | -6.60458 | -39.40242 | 2025-11-19 03:59:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4439c315-a19f-304a-9007-6a209e367b3c | -3.80327 | -38.45533 | 2025-11-19 03:59:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2bf6a27-b1a7-3184-9570-5eaaae9ae988 | -3.57044 | -40.35314 | 2025-11-19 03:59:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 51e4853a-c344-32b1-8acd-ebfaefe41e40 | -3.35706 | -43.49688 | 2025-11-19 03:59:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5df15135-66de-3ca3-8cb7-65382742b0b3 | -2.97615 | -41.75702 | 2025-11-19 03:59:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 35e678c8-d55a-317d-a8ce-2532eaa7e431 | -5.24334 | -38.48855 | 2025-11-19 03:59:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ca39f9c-9bde-3371-9441-bbaf299a3c66 | -6.21968 | -39.60381 | 2025-11-19 03:59:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f95bbb5b-7e77-324a-98e0-92dcf7f88154 | -6.88125 | -39.35012 | 2025-11-19 03:59:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 492f33fb-e264-3997-be69-8cfc9df88e58 | -6.62497 | -39.57582 | 2025-11-19 03:59:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 32cf9cce-c3c2-38e7-ba8e-3a80ab3c7c9d | -10.55338 | -44.11731 | 2025-11-19 04:01:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d780af9-49a7-3170-9ff7-cb72d4cebaec | -8.30482 | -42.25529 | 2025-11-19 04:01:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 78f17b82-90ca-30a6-b8f5-076857d58436 | -11.20493 | -49.41441 | 2025-11-19 04:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd950c61-f913-3272-a398-4c47c9268c37 | -11.66808 | -47.97374 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3a60a5da-9887-39ae-9bb3-acf9d02498b1 | -8.13368 | -47.58902 | 2025-11-19 04:01:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2db1bd5c-41d6-3c26-8374-a0e50f427416 | -10.03369 | -36.35627 | 2025-11-19 04:01:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6395b0d-735f-3dca-b7c7-0726165fe13e | -9.66354 | -43.89344 | 2025-11-19 04:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8ecc082d-a72b-3a9a-ac12-4059ad1c917a | -12.45584 | -54.44709 | 2025-11-19 04:01:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 96ffac59-6e20-3a81-96fc-7ef8d94f4eb9 | -10.52293 | -43.95695 | 2025-11-19 04:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceb0a5c9-8bbd-3f5b-8ac2-4ac9d53c55c9 | -12.07819 | -46.87446 | 2025-11-19 04:01:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2565113-177d-3d88-b62d-68968720225c | -10.59613 | -41.43066 | 2025-11-19 04:01:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b7ddac3b-bdf6-30f6-99b2-1cb05ef15f51 | -11.61117 | -47.62309 | 2025-11-19 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a296d78-31c0-3248-b41f-a8751024f48e | -9.69988 | -48.29771 | 2025-11-19 04:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8934a79-975a-3657-8cde-07dd25f2565c | -10.76294 | -44.81381 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc11ce86-a9b2-3f26-82bb-0769b431c8a7 | -8.03845 | -40.95219 | 2025-11-19 04:01:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00f9ec69-5899-3390-96a2-1ff40ff8e052 | -9.38478 | -48.43447 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9625d3a3-49c2-3480-ba8b-f877662b2351 | -11.61945 | -43.90779 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 513f6ce1-1c6c-3ff1-afec-de43f24ef8f0 | -12.60147 | -48.87625 | 2025-11-19 04:01:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bc46a0f7-3c05-3f17-be52-ae7c858e8124 | -11.28226 | -48.8709 | 2025-11-19 04:01:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07d24c92-d5a4-3649-866e-530041eb5237 | -11.66757 | -47.96978 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa9ecfde-3a7f-3dac-8a30-0ec4b4936b42 | -10.79595 | -47.98187 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08759f4a-89eb-33cf-8d83-461e06961ae3 | -8.21693 | -50.48158 | 2025-11-19 04:01:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3c64dea-89ca-3592-adfe-e678ef0ff4b7 | -9.35647 | -50.7415 | 2025-11-19 04:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bf9ebc3-1145-37d9-a562-b163f9f0ff49 | -10.54975 | -44.11671 | 2025-11-19 04:01:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa2cc1ff-c7f9-31f9-8a9d-e0b83ca43b88 | -12.88459 | -50.16095 | 2025-11-19 04:01:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62967488-6842-3389-9916-020afa55f6e7 | -10.10048 | -47.88387 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77826543-cb27-35c6-9370-cbe47f0b82c9 | -8.12345 | -47.59232 | 2025-11-19 04:01:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f793dd6-2240-334e-b1c1-0b050dc4b845 | -10.09809 | -49.58619 | 2025-11-19 04:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d774249-37a6-313a-a37d-c168c96e2a9f | -10.88069 | -49.54665 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b9fa815-805a-3061-bf39-245b4601d041 | -7.85678 | -39.8133 | 2025-11-19 04:01:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 157b4a45-e82a-3b50-8097-91592ff6d3e9 | -11.66894 | -47.96909 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 483febb9-21f5-3f83-b8ec-32cae5f9d6bb | -10.12056 | -36.39532 | 2025-11-19 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 4f22f89a-0b12-36a3-85fa-ecbcb4f4a8cb | -13.91329 | -45.28532 | 2025-11-19 04:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 08566f7a-d165-310a-aa3d-2edf6d3935d7 | -7.73822 | -47.25684 | 2025-11-19 04:01:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5824e3c1-2ac8-3e6f-8c71-be5e8c716084 | -10.34824 | -44.019 | 2025-11-19 04:01:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd514def-567c-3cb4-9d57-4f94568ffd9e | -9.37799 | -48.41644 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2281affe-a813-3e4e-861d-4dfcde805961 | -13.65674 | -43.80268 | 2025-11-19 04:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78beb80d-2dde-3365-a114-d99589b6a96c | -13.39114 | -44.06731 | 2025-11-19 04:01:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 403d5a28-594b-312e-86b1-63b55c3152ac | -11.20997 | -49.41527 | 2025-11-19 04:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c43a8dda-2a9d-3f06-bba8-87fdaba500ec | -10.69287 | -44.78991 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ebfba86-07eb-3b58-8870-a836f03be43f | -10.2115 | -43.46513 | 2025-11-19 04:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985a69c6-8166-3765-90f4-495e9da88ba0 | -12.04258 | -43.76594 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4f56704-07bb-35ba-b458-c81057ee0c9e | -11.41691 | -40.62334 | 2025-11-19 04:01:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ab73d8b-c67e-3c9b-98ba-46270e8a6f9b | -8.38813 | -44.06488 | 2025-11-19 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ead667f-2d09-3fc1-b143-71ce2ee070ac | -8.2869 | -43.9495 | 2025-11-19 04:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b30f1bd0-a842-3546-93e5-bff4fe968a8f | -11.02673 | -43.89194 | 2025-11-19 04:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f82e9a8-4dc4-3d5d-a348-4b29cc4a4ff9 | -10.12124 | -36.39055 | 2025-11-19 04:01:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 6641ee89-c370-3d24-a006-f386e59354b4 | -13.93317 | -47.51205 | 2025-11-19 04:01:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0901de82-121a-36d9-b9df-2e4bd59e85cd | -9.37992 | -48.43366 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a70eb1b8-519a-3fa3-97bb-ff5563755b6a | -10.01303 | -39.18583 | 2025-11-19 04:01:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b20d5c6-e382-30b1-916f-64256d86e128 | -10.53933 | -47.99266 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 629437c0-72cb-3188-8027-09fe150ec37f | -9.36827 | -48.41483 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b342497-802b-3739-bea7-6ceab185b047 | -7.55139 | -44.09646 | 2025-11-19 04:01:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dd018aa-dfe7-34e8-8dac-88c61b1191a0 | -8.91541 | -40.44058 | 2025-11-19 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b43740a4-0736-389c-8ca2-64fd98fae82b | -10.07127 | -47.91334 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f0b0b38-67d7-3603-aed4-477658660fd5 | -10.6908 | -44.26199 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f2eb4f-7052-3052-8173-52e40d29fb41 | -9.40132 | -48.45426 | 2025-11-19 04:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73327006-a144-3705-8003-0c4cd839416e | -10.69041 | -44.26271 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e953b311-a191-399b-8722-dfff6dba048e | -12.00373 | -49.26684 | 2025-11-19 04:01:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49ed406a-1fd8-374f-8a5a-17b74ae9c325 | -11.67208 | -47.97065 | 2025-11-19 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6bd45b68-7693-3dfc-a921-dcef35eab869 | -10.1379 | -44.19946 | 2025-11-19 04:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5336e40-1e6f-325f-ab71-469e97dd4c0d | -10.19619 | -44.8993 | 2025-11-19 04:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72b90cb8-0de9-3e54-bca0-24c849ee1d0c | -10.3804 | -47.53609 | 2025-11-19 04:01:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b520178-acc3-3c88-80c3-6da854d4f251 | -8.13454 | -47.58404 | 2025-11-19 04:01:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c852c85-efd0-3180-9273-df0b990868ea | -11.57221 | -44.12989 | 2025-11-19 04:01:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4ab36e3-9a82-38b9-b678-20444b9e42f2 | -10.9233 | -45.08286 | 2025-11-19 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00d4c450-d27f-3e35-9160-be6c71b10b49 | -10.47452 | -36.91922 | 2025-11-19 04:01:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 1d3e2ce8-9a9b-37a7-919c-4f0a08596204 | -9.85239 | -48.90549 | 2025-11-19 04:01:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b383680a-0686-358b-8c40-e5af57733831 | -10.00856 | -39.19256 | 2025-11-19 04:01:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cdb98871-24da-3a2f-a357-f09219f012e2 | -10.79604 | -47.98402 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03894833-55ff-3651-8e41-4cdf0ad6ae0c | -9.33934 | -42.44044 | 2025-11-19 04:01:00 | NOAA-21 | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f8ed67a3-a256-30cc-ac8b-fd3e6b04530e | -11.88304 | -40.9503 | 2025-11-19 04:01:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 16c4cccc-4041-3dc5-ab56-4006808338e1 | -12.01147 | -46.76616 | 2025-11-19 04:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33d12501-4db8-39a8-9542-771f18720d14 | -8.3725 | -36.05139 | 2025-11-19 04:01:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b66b49a0-28c8-398f-ab43-bba1e577fe45 | -12.01602 | -40.13113 | 2025-11-19 04:01:00 | NOAA-21 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 65dd7664-9535-35a5-b171-c6ea8d6be8be | -12.88518 | -50.15781 | 2025-11-19 04:01:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccaa7690-407c-300c-98ad-c78b2aeb12be | -12.04324 | -43.76196 | 2025-11-19 04:01:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a403553-ff6f-31c5-aeee-7a3a6e5f8e45 | -11.5129 | -45.00145 | 2025-11-19 04:01:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 95a4abed-8ae5-38c7-adc2-28c340d80cab | -10.03437 | -44.07605 | 2025-11-19 04:01:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c65b27b-add0-37f4-95f8-d112a71ebf53 | -8.21765 | -50.47766 | 2025-11-19 04:01:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc5a635-c1ac-35f2-a7d3-c6e4dd7c0421 | -8.38516 | -44.05979 | 2025-11-19 04:01:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10f20472-7983-3c10-81a7-d1dd15319cc3 | -10.06753 | -47.90763 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 111c801d-cd74-3b4e-ae80-1471ad08f328 | -9.6563 | -43.8922 | 2025-11-19 04:01:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c4dd29ec-4c8a-323a-a34a-1433507bae81 | -10.06384 | -47.90849 | 2025-11-19 04:01:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f087124-9239-3b36-b0c0-9135df6d9e1f | -10.88011 | -49.54974 | 2025-11-19 04:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6d80347-3045-30fc-9793-27b5f0277083 | -11.02316 | -43.89132 | 2025-11-19 04:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f62401d-67d9-3aa6-8da2-f21dcb1f38dc | -8.87699 | -47.33095 | 2025-11-19 04:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dcaec55b-f0a6-333e-ba6a-26dedb51a394 | -10.52362 | -43.95275 | 2025-11-19 04:01:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47555f61-876c-3961-831d-3ef7ed2226da | -10.79514 | -47.98626 | 2025-11-19 04:01:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b440019-77fb-3449-9676-17a4db999f8d | -10.44519 | -49.35817 | 2025-11-19 04:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c82e00a-5022-3142-a0c2-2f6564d4c72c | -12.36156 | -41.02034 | 2025-11-19 04:01:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
