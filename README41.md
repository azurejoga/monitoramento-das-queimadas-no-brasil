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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c014c65d-c222-3d40-b24d-8de82a68b4a5 | -6.42976 | -46.021 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ed686d0-d5a9-3e74-b668-6fc0e37ed089 | -4.99688 | -47.34225 | 2025-10-05 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e274b5d9-aba9-3468-95a7-a9224bfb99f8 | -5.54433 | -42.6741 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4c0ce4c3-59c9-32c5-a681-44962c8494d2 | -8.33633 | -49.50189 | 2025-10-05 03:53:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ef2a246-9953-3a6c-a60e-d27105d4a908 | -6.61005 | -44.3181 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 874e5682-3588-3e7e-94ab-8862a3a1b5d2 | -7.54227 | -42.41072 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4e839046-cd86-3cf5-a2eb-ea9d3dd94b2c | -5.97969 | -44.35488 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eaa7cec-2880-3fa4-a197-172623d46144 | -7.79647 | -44.53905 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1c20942-3199-3e8b-ad3f-a76826433f75 | -6.61908 | -42.40712 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b37d0e91-c9d3-38ce-ba3e-c3744b6afc84 | -8.8901 | -46.04764 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 496365ec-5d18-321a-ba8e-e38f167460bb | -6.61355 | -44.31168 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c51ecec-befc-34fd-8b25-1a251637d217 | -6.52652 | -43.37207 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c6700dc-4daa-3684-b2f1-143349f355cb | -5.84694 | -42.81323 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b880c865-03ba-33a8-acf1-f716c0336283 | -7.87996 | -42.59628 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e63adc58-6a44-36ed-b313-540c756182f4 | -10.63677 | -46.34545 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| bffbfe85-d5a6-3377-9dd8-88d981589d1c | -7.74904 | -42.52106 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 2bc733af-4cff-3a20-b1d2-01e289a93f9e | -7.61567 | -45.46757 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98f37fa6-a5dc-34f0-b121-4d9a59c84380 | -7.78669 | -42.5965 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b0f2554-f74d-31a8-a533-a0df0284330f | -7.52006 | -37.99397 | 2025-10-05 03:53:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fe4bdc13-e55b-317e-ac05-38a3c9aee89c | -10.39836 | -45.40509 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50a7048a-0671-31af-8c87-855905a01fb0 | -7.75509 | -46.32217 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f0ab0e9c-17f6-3612-a243-053fe4158e4d | -4.25121 | -48.56307 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1eeacc8-87c6-3912-ba5d-af0132fb376c | -5.92401 | -43.33057 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9121b9c0-18b7-3b0f-a9eb-d31818bf5a7b | -5.67445 | -42.73928 | 2025-10-05 03:53:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14481229-eabc-36e6-83c1-29380fd9f45a | -6.35001 | -43.91427 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| db19649d-7859-3f84-a8a3-aba2cb924985 | -5.21209 | -46.18254 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fba1de98-9ac6-3aff-984f-03e433f1510a | -6.02643 | -44.13264 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ddb1829-f0d7-39d4-ab40-538441227f18 | -8.86385 | -46.81196 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16a6fe64-e584-31ea-878d-430b3263e7dc | -9.20978 | -46.92937 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5162bd83-68a1-3470-9b20-9dfb146332b9 | -6.08629 | -44.03817 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c4a7812-401a-3181-a92b-a2194651c3df | -5.27916 | -42.91724 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 395b482e-acbc-352d-b8e7-3c6217b72dd6 | -5.62223 | -43.21456 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2e61393-be91-373d-b531-fb69f64a6c01 | -6.2468 | -44.21601 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65925c4d-8429-3658-a01e-1833db9555ae | -5.78453 | -42.91916 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3bdb4b69-4aa4-3ca6-a67b-8b2ca5275613 | -6.06386 | -41.23893 | 2025-10-05 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b44e4119-affe-3b8e-80b9-e1f40cc25f24 | -5.89108 | -42.54496 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6491a7b3-b77d-3391-b467-ee94586c1079 | -8.11853 | -44.10456 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebb09bbc-be45-361e-a0e9-a013e51d92e2 | -6.11103 | -45.88172 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6b79b59-ce5c-3f5b-a6ec-32a43f802337 | -5.00506 | -47.22081 | 2025-10-05 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c395d435-ec1a-3c9d-af4b-2593fc070b7c | -5.87171 | -42.54155 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9fb20507-4fa1-3811-836c-449e8b36677d | -9.54137 | -43.03358 | 2025-10-05 03:53:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c07b1abe-a018-316a-ac0a-0683e8c876c3 | -5.88642 | -42.91095 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| f3cc8f24-fd1a-3f22-8677-d0daa9c2e115 | -6.39578 | -44.778 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 750220d0-b753-3b5a-bc32-bafadf0ea5a0 | -8.63628 | -44.90691 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90a23e50-b795-337e-8b75-0dcb619da020 | -9.2905 | -46.01785 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c1830916-63f4-3342-8331-764c2f99a144 | -8.89773 | -46.04613 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 436f2677-61c2-3dec-b1c4-7876809ba9a3 | -5.44977 | -42.92453 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2406c85-400a-36b9-8c3f-babfe34ccc19 | -7.01071 | -47.21583 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 330c3dbd-18e8-3323-9225-69cab358e57e | -8.53741 | -46.31956 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9bc60878-7cd3-3cd2-b27e-4052997dd0c2 | -6.33322 | -43.88295 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc915f68-0e69-33b9-aa5f-ccf2f85822f7 | -6.21474 | -44.07601 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd194fd4-975e-3337-b64f-0e4559cfbd38 | -6.2129 | -42.93035 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 893e8557-73dc-33b0-b09c-c808e7cb8652 | -7.03435 | -42.80587 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2673d7ad-1091-3b69-8187-84cd22b03d23 | -7.34008 | -45.21171 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fb56869-d2c0-3d4a-afa3-5e5df4ae79a4 | -10.35614 | -48.16212 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92315ec4-aa87-3521-b03c-0a8f44582d6c | -9.25763 | -46.77727 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b56c3484-7de0-32de-bb90-402dc88ecc62 | -6.11116 | -43.1102 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25ae7943-96c3-32af-9c19-9284d878878d | -6.60356 | -44.31849 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3556fa1a-1145-3368-a94f-f915fd70ee2c | -8.57368 | -46.33709 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ab78af8d-9cec-343c-9154-cb6dab6fbe17 | -6.37346 | -42.88667 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e6d58e8e-f950-37b1-a682-b5e8d34ee88e | -7.77758 | -44.11882 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64b878dd-2feb-3155-9c71-70191a4ec64d | -6.60142 | -44.31675 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51b2a7c1-364a-39df-9927-b853eb4981a3 | -8.55834 | -46.31277 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b982c122-ef20-366d-930e-66d5207ea27d | -7.54442 | -47.28176 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 364fe570-09f8-3050-be02-bd18e6bbf31b | -6.14847 | -44.60875 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cc4b5c3-389c-35dd-aee1-47c3400a2cf5 | -5.8509 | -42.8138 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1c631413-95d5-3bbf-870a-19bb7e3b8ed3 | -10.30087 | -48.55332 | 2025-10-05 03:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3da62593-784c-3fe4-8657-73776a048969 | -6.21832 | -44.08089 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637ba1f2-ddbb-31db-85aa-55984fe4044a | -6.54622 | -45.80679 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52d62c64-ae35-3b25-ad86-9a61bc4a6c52 | -6.34313 | -44.02999 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3521a91d-1c06-3398-a9b7-3256d80d2ca9 | -5.79526 | -42.49216 | 2025-10-05 03:53:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ccf03e26-bc94-3def-aa42-47869b09c167 | -5.94702 | -43.52017 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22cf0583-0e72-398d-990f-823ea347a9a5 | -8.23121 | -46.81167 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| d371f7c8-618d-3b01-a899-2faed7e1c898 | -6.2573 | -45.37162 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba3729aa-0a17-3385-9630-a1d87132ce6b | -9.7252 | -45.19914 | 2025-10-05 03:53:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4817e032-d068-375c-9466-0f1e8cd5329e | -5.97426 | -42.94748 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 675f12b5-980d-3b18-ae22-67b546351412 | -9.059 | -47.01791 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dbe114e-2a14-314a-971e-f68045d6555a | -9.90949 | -45.95901 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c4d82eea-b593-35ee-8274-8814f26cff24 | -6.13431 | -44.63801 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b92d8527-3495-3c92-838e-e93812033124 | -7.74939 | -46.32626 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90569a44-0795-3c74-8c7d-97919c7e296a | -5.34563 | -45.30152 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3283a6f-a95e-381d-a97d-08230a54a20b | -5.94472 | -42.87898 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| de2605dd-97da-3878-bf14-8760939c306e | -7.46316 | -43.05584 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 82bbbda1-5a49-364c-be61-725147d84643 | -8.63561 | -44.91079 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66535abb-1427-332c-9ee5-c5203800f298 | -5.3417 | -42.97009 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4d6bfed5-db12-3100-a744-b7758b696cd0 | -5.99275 | -44.35724 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2635875-14ac-3c7b-808e-4aaa42fcc551 | -6.59924 | -48.05496 | 2025-10-05 03:53:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4759759-71cc-3979-8233-03b8644da7e8 | -9.25663 | -46.78276 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4f0d4886-3d4e-3d06-bcea-899d68e8572e | -7.25844 | -39.41081 | 2025-10-05 03:53:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7691f95e-441b-31c8-982e-b6e1c13f7955 | -5.85509 | -42.78833 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 651998c0-5a0e-337d-be50-872fb3ef96f9 | -7.73546 | -40.08624 | 2025-10-05 03:53:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0a9a3db-e0b4-3705-98f2-29ce97640262 | -5.94866 | -42.87973 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa73e4a0-242a-3bb9-80dd-327e5198aeef | -6.13356 | -44.64233 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28321255-bb8b-36e1-9d7a-650cb5b06ef7 | -6.14244 | -44.64381 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe86b727-923b-32be-91d3-810ee44e0c43 | -5.4081 | -41.35127 | 2025-10-05 03:53:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c084cc12-ba9b-3a45-aff1-07a238dbd62d | -6.60574 | -44.31742 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c0e1006-91aa-3ce0-991e-040c5030096c | -10.35782 | -43.73684 | 2025-10-05 03:53:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd9dd310-7b18-359b-93d2-3799cb778cd3 | -8.58699 | -46.31773 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 6d6cabbc-554f-3f50-8da9-08ac8403d507 | -5.10948 | -45.47042 | 2025-10-05 03:53:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c225d3e-0cea-3f91-a917-994ca15a5885 | -5.45719 | -43.40946 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README42.md)
