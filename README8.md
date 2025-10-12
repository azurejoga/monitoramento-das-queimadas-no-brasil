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
| 86a48775-85ff-35af-a121-7d19741266c9 | -5.8224 | -44.0273 | 2025-10-12 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 84260adb-465a-3700-92b3-1980643a5b16 | -2.5423 | -47.811 | 2025-10-12 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 184dce7e-214e-371f-ae77-648e0d66eecb | -7.5212 | -46.538 | 2025-10-12 01:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 89457612-3db7-3c1a-b821-c1ab32ed1c95 | -19.02858 | -57.5611 | 2025-10-12 01:49:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 4fc74297-c724-3c16-a9b2-2813befeeb0e | -19.02639 | -57.55618 | 2025-10-12 01:49:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 2a600950-e28e-3a02-980f-980cf6a85314 | -17.81728 | -57.67396 | 2025-10-12 01:49:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.7 |
| bb954eaf-8dc8-3284-ab22-234b2c3acda7 | -19.04133 | -57.55283 | 2025-10-12 01:49:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 94e860fc-73b7-3a8b-be55-64677907eb59 | -19.02291 | -57.5305 | 2025-10-12 01:49:00 | TERRA_M-M | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 9a888d36-1bc9-3d7b-8c0b-bd1ede6d1795 | -15.16142 | -56.828 | 2025-10-12 01:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 87c7abab-6371-3e95-bb86-d9d1e937375d | -15.16336 | -56.82275 | 2025-10-12 01:49:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 286a9a14-891e-3a58-859e-2bfeb083817d | -19.0319 | -57.5382 | 2025-10-12 01:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 1c5db14a-7221-3c0b-9f9f-2e6261b40f35 | -9.0161 | -67.4275 | 2025-10-12 01:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0e3efa96-6788-3ff3-b308-35a1ea153219 | -12.7685 | -45.8363 | 2025-10-12 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d69ff878-5e1a-3290-81f2-f56543422d78 | -12.7492 | -45.8393 | 2025-10-12 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 315b43c0-0909-3616-ae84-153f13112e8c | -9.016 | -67.446 | 2025-10-12 01:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 7809c89c-9ded-3e9e-ba55-795cd9488abe | -4.271 | -46.9369 | 2025-10-12 01:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8d799b85-bea5-37af-8bd6-c652d7286d0d | -14.0155 | -43.4943 | 2025-10-12 01:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 48b31a31-75a3-3a14-a3f9-476ef9e1ed40 | -17.5897 | -42.4246 | 2025-10-12 01:50:00 | GOES-19 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 02271c7d-2f9a-3625-9440-691fea29727c | -2.5423 | -47.811 | 2025-10-12 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 0214d591-ba14-3bd6-80b4-af8d26697550 | -7.5212 | -46.538 | 2025-10-12 01:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 123.1 |
| dfae9bb0-3211-3288-a327-9914f454475a | -7.864 | -44.5152 | 2025-10-12 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 45bf6bc0-214a-3512-afe1-c5dc2f0017b3 | -2.5424 | -47.7893 | 2025-10-12 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3d81b180-9699-3cd8-a10d-a4409ae3e85f | -10.64459 | -69.51117 | 2025-10-12 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 92808896-e0e1-38ba-bd27-449eab11463e | -9.01161 | -67.43301 | 2025-10-12 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 62230526-156a-356e-90a8-b80af301b461 | -12.21776 | -64.3666 | 2025-10-12 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 19.9 |
| b5d459b5-aada-31e2-a869-d04271b1bd5c | -10.73686 | -69.44483 | 2025-10-12 01:52:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 80ca58d4-53b0-3213-a93d-42950bd39590 | -10.73812 | -69.45406 | 2025-10-12 01:52:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1a2745cb-27d7-3301-9cfc-1a7b2421f843 | -9.12345 | -67.83692 | 2025-10-12 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 346c726b-da79-3d7d-be0e-d9dff95277cd | -11.24714 | -61.17031 | 2025-10-12 01:52:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 88232854-d294-351e-ad60-2ef843c73d85 | -12.20754 | -64.36822 | 2025-10-12 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 18.0 |
| e8eed386-ae6a-356e-bcf0-02f56843ba08 | -10.64145 | -69.34587 | 2025-10-12 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4d1bc492-1d9b-3479-8f57-fd8b3d22e878 | -10.62998 | -68.73022 | 2025-10-12 01:52:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 382670cd-f81b-36cc-9542-f21c75357ca2 | -10.88304 | -68.4142 | 2025-10-12 01:52:00 | TERRA_M-M | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0f7d7dde-0f5b-3060-8b10-6264ca6db2ce | -12.2057 | -64.35606 | 2025-10-12 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5468a084-30bb-3295-9047-e61a9f420a21 | -9.01293 | -67.44227 | 2025-10-12 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| c63bd221-2f0c-38e9-bf1c-0523747d7097 | -10.65517 | -69.11189 | 2025-10-12 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d24ce07-528f-3623-9e63-308c4d072ba0 | -10.1624 | -68.74603 | 2025-10-12 01:52:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 761c453d-ea99-390b-9652-c56987faa7e6 | -9.02061 | -67.43168 | 2025-10-12 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| abfa319b-7baa-3cde-b2dc-c706c8cac45c | -10.63224 | -69.35349 | 2025-10-12 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 37d8e95e-5ec5-3036-885a-66a49c1e8cdc | -9.02193 | -67.44094 | 2025-10-12 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b1a8785c-652f-350f-9b33-e26376ffc08c | -12.21592 | -64.35435 | 2025-10-12 01:52:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9076200-ced1-3754-99e0-335830d959d8 | -10.64268 | -69.35504 | 2025-10-12 01:52:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b7669f73-1a7b-32a8-8956-39495eb3ccd0 | -10.88231 | -68.21404 | 2025-10-12 01:52:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 62155c99-7241-345a-82c9-bc315301b951 | -9.01426 | -67.45153 | 2025-10-12 01:52:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8f2f7f7d-1520-3de5-aa19-133157eb50b4 | -7.864 | -44.5152 | 2025-10-12 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| fa77403b-2a5d-3630-99c6-7fd156e6c90c | -7.8637 | -44.5382 | 2025-10-12 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b792c788-1099-31d9-9777-64d92bb35462 | -4.271 | -46.9369 | 2025-10-12 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 18a4fecc-471a-38dd-a4ad-aa186eb7ff52 | -5.9221 | -45.434 | 2025-10-12 02:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 9f47b477-c2c5-332c-b58b-697401dabc67 | -9.0161 | -67.4275 | 2025-10-12 02:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 85abda8e-109b-3766-8435-cc21cfde2334 | -3.5153 | -45.8411 | 2025-10-12 02:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a386c1ad-8298-315c-8a80-554ea0789988 | -9.016 | -67.446 | 2025-10-12 02:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2e00f13f-4228-3a40-9b9c-1817ed88bb07 | -14.0155 | -43.4943 | 2025-10-12 02:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 314381bd-d529-3642-a432-84ff69c6b729 | -2.5423 | -47.811 | 2025-10-12 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| ba29e214-f975-3404-aea8-6a199866e4ac | -12.2051 | -64.367 | 2025-10-12 02:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 191d93ca-4276-3139-8650-21563ed80338 | -14.0351 | -43.4906 | 2025-10-12 02:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b7b938df-854d-3069-b9d0-5bb15a5d391e | -19.0319 | -57.5382 | 2025-10-12 02:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| f6382cf3-dae7-3e05-b5e1-c5dc063f58a3 | -2.5424 | -47.7893 | 2025-10-12 02:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| cb549ba5-7677-3dff-b118-b9eb4a4075e4 | -15.6825 | -46.625 | 2025-10-12 02:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 879ee2b2-f4fd-312a-b316-cd56de3bf6b9 | -9.0161 | -67.4275 | 2025-10-12 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 7120a5ac-f483-34e1-a0cf-89e1bfb9389c | -2.5424 | -47.7893 | 2025-10-12 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cc1fcd97-af32-31f9-acaa-c28fa385b87d | -19.0319 | -57.5382 | 2025-10-12 02:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| af6396c9-ebf4-373c-bd79-57df1969e02e | -12.2051 | -64.367 | 2025-10-12 02:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f256f5ff-a573-32f4-ab50-cc639057125c | -9.016 | -67.446 | 2025-10-12 02:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 79e5dffa-f546-34a2-a964-80e31672598f | -14.0155 | -43.4943 | 2025-10-12 02:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 802aab7a-b0dd-33bb-935e-fd55626160f8 | -7.864 | -44.5152 | 2025-10-12 02:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 358ff8a4-7afc-3dac-b06b-16436ed534b7 | -2.5423 | -47.811 | 2025-10-12 02:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 34edf9dc-b41d-3014-a1fc-0d1d1b409a7f | -5.4721 | -43.4045 | 2025-10-12 02:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 6ef1f334-c819-3ca2-842f-de74d20819f7 | -12.2051 | -64.367 | 2025-10-12 02:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| aac12e9d-0efd-369a-8807-17dadfd985f5 | -5.4911 | -43.3798 | 2025-10-12 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b28cc512-a1c8-33f7-9762-708e9748d18b | -4.271 | -46.9369 | 2025-10-12 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c6ff2958-29a4-3778-9d4f-508dd9f73434 | -9.016 | -67.446 | 2025-10-12 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| edb481dc-fedd-3261-adc9-52fcecafaf5a | -19.0319 | -57.5382 | 2025-10-12 02:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 53.2 |
| a29afae8-7156-333b-ae77-6e45c9bc6ada | -7.864 | -44.5152 | 2025-10-12 02:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 1c1fe842-e4db-3374-9cf0-630ff7cc9be8 | -14.0155 | -43.4943 | 2025-10-12 02:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 63bbf3d0-c2b7-3816-bde3-3d16e52f0b4c | -3.5152 | -45.8634 | 2025-10-12 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8167ffbf-f86f-3243-8020-3ba5970589fa | -5.4723 | -43.3812 | 2025-10-12 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 01bacd91-adf5-3dc6-87f3-b9b36163690f | -3.5153 | -45.8411 | 2025-10-12 02:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f79da22d-7303-382b-a004-83d4224ac202 | -2.5424 | -47.7893 | 2025-10-12 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| abfa9121-bbb0-35d4-bc38-e24b26138535 | -2.5423 | -47.811 | 2025-10-12 02:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 72d12ad8-021f-3d15-b9a7-939dd82932ac | -5.4909 | -43.4032 | 2025-10-12 02:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| a5c523bf-bc61-32b3-88db-0a99ab250340 | -3.5152 | -45.8634 | 2025-10-12 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| cb527902-6e87-3999-9e50-6353066c8f44 | -15.6825 | -46.625 | 2025-10-12 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 75.7 |
| af5c12e0-85ba-34d0-b3c7-06c27ae94094 | -7.864 | -44.5152 | 2025-10-12 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 8723f953-14f9-35e2-a17a-23c85713373d | -12.2051 | -64.367 | 2025-10-12 02:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0eeb38ab-c6c2-32b5-be28-e79ebd8056ce | -14.0155 | -43.4943 | 2025-10-12 02:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1b0d217f-8ccf-3148-8cb6-29a818092f7e | -19.0319 | -57.5382 | 2025-10-12 02:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| df7edda3-4edf-3703-b4bf-33c358c7623b | -14.9572 | -46.7327 | 2025-10-12 02:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 2f73505c-7eb4-389e-aa7a-cdd077430bf9 | -2.5423 | -47.811 | 2025-10-12 02:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| eab52918-11a6-37bc-873e-5769c439ddba | -7.8637 | -44.5382 | 2025-10-12 02:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 39d1db9b-fbe7-3f07-98d1-cc66cec6fc97 | -4.271 | -46.9369 | 2025-10-12 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 42d3547e-e1e1-3c93-af7b-6ef4e5ba6079 | -3.5153 | -45.8411 | 2025-10-12 02:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 965dbba5-957e-3a03-b8f9-2f855ff92d3a | -17.2504 | -52.2658 | 2025-10-12 02:40:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 75df2bd5-0a95-396c-90d2-2f8161cf1669 | -2.5423 | -47.811 | 2025-10-12 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a8ec84a0-2a81-39e6-a90a-abca76e44beb | -4.271 | -46.9369 | 2025-10-12 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b5da8dd8-3066-32de-92e9-f6c1f362fd40 | -14.0155 | -43.4943 | 2025-10-12 02:40:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| ff5da3d5-5d4d-3c80-bfce-867957703011 | -14.9572 | -46.7327 | 2025-10-12 02:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f42f33d8-f676-3f30-bf04-52f7fe00c11e | -19.0319 | -57.5382 | 2025-10-12 02:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 03331325-620a-362b-b7e5-54413ecf533c | -3.5153 | -45.8411 | 2025-10-12 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 88bf6448-505c-3f61-affa-667521bf53c5 | -17.2701 | -52.2627 | 2025-10-12 02:40:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1bb1e3c1-2824-3b02-8b2c-9b81e7efd05d | -12.2051 | -64.367 | 2025-10-12 02:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |


[Clique aqui para ver as próximas entradas](README9.md)
