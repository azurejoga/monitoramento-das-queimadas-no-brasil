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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fe1dd7c-1c4a-36e1-8a73-eecebe511a38 | -4.6976 | -41.96351 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c4825fa-9eb3-3bd7-ab00-7d2232ddf51a | -7.06343 | -44.35794 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac2851b2-9724-3aae-ac41-860a52f27639 | -6.41368 | -43.36149 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8235937-7201-38da-819f-1d65a162be15 | -5.66567 | -46.24076 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac7b7d9b-48d8-3095-af8d-a3decb5ffa1e | -6.45568 | -43.31079 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf4df68a-45b3-3dca-b5e5-3e79403a009f | -5.42737 | -43.19725 | 2025-09-18 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6a97f62-05b5-3297-8365-31a479b3479c | -5.52836 | -42.16833 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6115afa5-fd8f-377f-b374-0559ecbc7d37 | -6.54593 | -43.59896 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74e34acd-d9ae-3349-b794-86163ea87cdf | -6.43306 | -44.37079 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac0bb62d-a4bb-366d-a9b5-77a40b98ea3a | -5.85761 | -45.89063 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da078b3a-4585-373f-85ed-369387953b11 | -2.91902 | -48.31428 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d78262a6-2f18-3aa3-b645-101c1e750d04 | -6.49841 | -46.00485 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 986e9906-c402-3ce7-a9b3-5b115c58d19e | -6.40873 | -43.37136 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47cbecde-c140-380e-b19d-8a0abb18a7a2 | -3.85174 | -40.34627 | 2025-09-18 04:12:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1e074671-bc75-3d76-bc8e-875e41575871 | -4.6952 | -41.95959 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 514e76ef-2aa9-398e-bb36-fb182613d883 | -5.80803 | -45.92443 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dfd30cb-32a2-3b82-899d-28d2d4cef150 | -6.32059 | -42.39919 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ff395889-9fec-3307-b8d1-46240d352d35 | -3.45345 | -44.14349 | 2025-09-18 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df0427dd-6b3b-3103-943e-4b9f4d996cae | -5.68679 | -47.44477 | 2025-09-18 04:12:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d9aa344-0b0d-31a2-9ec5-c5662bba9262 | -6.47484 | -45.72683 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aca3df22-294b-3f47-bdd5-fe5329890057 | -7.00179 | -44.61202 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06e03990-e384-31c3-83bf-a3f4395a41fe | -4.3406 | -40.73626 | 2025-09-18 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a83c13d-d34d-33c1-9bc6-50807778c37c | -6.53647 | -43.93723 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d549576-9330-35f7-9a61-09eaa44272ed | -5.74006 | -42.57109 | 2025-09-18 04:12:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8159820e-6972-3506-a1da-211e8571ac00 | -5.44817 | -46.68325 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4105d61-1d85-3f53-b23c-66f58c175854 | -6.16379 | -43.09488 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70474de0-99e1-3229-af25-aa1c89e48aa8 | -5.95637 | -43.80173 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55f1491e-97d3-3c0a-89ec-6b26098e8d11 | -5.53927 | -42.20517 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b4ce0745-63a5-3d60-8856-5eb858bc5ab5 | -6.72662 | -44.15194 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 42062650-95f2-327b-bec7-4dfe8ed7c38b | -6.42635 | -43.34575 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6ed092d-4bf2-3c15-9881-77abf327ff6f | -3.7427 | -49.04895 | 2025-09-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27efe10f-9ab4-3c09-ac49-f629ae71b99a | -4.91555 | -47.86079 | 2025-09-18 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9be693a6-2677-38e2-a281-2c8e1c948ee3 | -6.28459 | -43.0821 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 411865e7-9442-3a9d-978f-674fc1cde6b2 | -3.97199 | -44.45415 | 2025-09-18 04:12:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49470e9b-92f4-3630-b2e5-d67960680972 | -6.87526 | -44.17531 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27c1668a-7d30-300e-9035-62489faad95b | -4.61167 | -46.34315 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0ca7176-c2a0-36cf-a3ce-135d9440eb8c | -4.69652 | -41.97048 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd8a3461-b847-357c-9f79-c9f3defbb07a | -6.31727 | -42.39865 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef173015-1a02-3a4a-a4d9-e64c0a533d2e | -5.82437 | -45.91444 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57440ae6-8ebb-374b-b1c7-cb3b0a21e54a | -5.32956 | -44.99426 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b66bda7-5aec-36ba-82e9-4c6d9e8ae3ea | -3.30195 | -48.70969 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8aa54ba-28cf-3ba1-bae3-5072de43f8a7 | -6.39049 | -43.33653 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb2846fe-85fd-3c58-bbf7-1c1bae2f1cb3 | -4.69242 | -41.95559 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 046e148b-36fc-307f-9dd5-7e973b649ace | -5.53697 | -42.17626 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88264bd4-4b94-3209-afd5-c9f96df45e60 | -4.71703 | -46.12993 | 2025-09-18 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a3855500-76a4-3dba-8401-7131ce4592bc | -5.95298 | -47.01179 | 2025-09-18 04:12:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 609e8ad4-4ea2-339f-bcde-1e82138d2ee7 | -6.57929 | -43.04332 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89935cfe-517c-378a-8360-8a0f2e98dae4 | -6.11784 | -43.38526 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19e65b58-b386-3c07-a720-7c2e43e4d9bf | -2.64171 | -48.04459 | 2025-09-18 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac022176-d7eb-3c41-8951-66b816cbd8ae | -3.835 | -40.36292 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a51a8ad-0163-3b88-8fe5-304e7aba1e20 | -5.79844 | -44.87132 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bd8ac07-779f-3b2c-aa3b-e7cfdde654a0 | -6.61109 | -43.57376 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64a0cd6f-c817-37bb-ae55-70f4fbcc8614 | -6.98275 | -44.4398 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f407a50-a9df-30d4-bf64-8fbd80ad52b6 | -2.1719 | -48.42357 | 2025-09-18 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbca6a50-2747-36b5-a6a1-cc96b29d63c7 | -6.50064 | -46.01364 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7344bd82-4ec3-3ae3-bc86-64eb73cfaf13 | -5.67599 | -45.04441 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d787f77-656f-3fe7-ae37-b5e4a504e691 | -6.43045 | -43.53409 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 358e3e3d-ec82-37c0-b237-21b89fcc20f8 | -5.63755 | -43.88482 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e26bf99-c74a-38cf-b769-3fab5e008e82 | -5.85902 | -43.17413 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 98d87b1b-9bc0-35fb-8166-cf5a8074940a | -6.55366 | -43.59307 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 978614da-a2bc-3d1d-9322-10322dc0f678 | -5.36845 | -43.01158 | 2025-09-18 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 263cf288-4796-3c78-a475-b79712e13b99 | -6.59052 | -41.38352 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8c9a8b45-4a0c-3540-87d7-2414c6493a46 | -5.81089 | -44.72914 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07514f01-796a-3924-9826-8ba472081ab6 | -6.98789 | -44.76197 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1901504-5d0c-3c3b-a8b5-6c3fea32f11a | -4.88111 | -48.2639 | 2025-09-18 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 654f65bb-6a80-3591-a35f-880cd6119e18 | -5.80484 | -45.90842 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd934f1d-d7f8-31ca-85f7-dfc4873f258f | -6.14245 | -44.49413 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c483178-973e-3f7d-a660-960f1c6f886a | -5.88982 | -45.64836 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ececd686-27e6-3e0b-9b1e-2f46b37f9b7c | -6.53315 | -43.93667 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672591b7-c9cc-344c-8277-434952effef2 | -5.62 | -42.90248 | 2025-09-18 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0961e881-b67c-35ed-94eb-2331899443bc | -6.3995 | -43.72865 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c2a902e-68de-318d-a3d9-0e94c4257e75 | -6.0352 | -43.13445 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 922f65bc-b68a-323f-af64-43af3642ff43 | -5.76084 | -46.25425 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b62d6f4a-3cff-3cc3-aa7e-e15fb5b612fe | -3.813 | -47.0573 | 2025-09-18 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7776d3b3-8dc1-3e4c-b5b2-5c73e2f52d0d | -6.60776 | -45.64238 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf7ec952-9f5d-38c0-ad12-d30cb188becd | -6.19079 | -45.11248 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3507a6e8-8229-3c5f-915f-142d8385513f | -5.78421 | -45.96835 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cfec96c-7ba4-36de-9fbf-9f2873846775 | -3.15524 | -43.25923 | 2025-09-18 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a980b05-4c33-3ba9-8457-d997158b3de0 | -3.88678 | -47.59777 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34cd6f26-fc75-332b-ac02-94930cd8a09c | -3.26503 | -43.05795 | 2025-09-18 04:12:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9059c5da-3c7d-38a2-a932-2a54537465f5 | -5.66646 | -43.91832 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02046d5d-0069-36eb-ac57-e570c9ba7c0e | -7.06587 | -44.60027 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 100a24ef-d055-3eb6-a4f2-c1b2e7ac4844 | -5.81296 | -45.91681 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 202bcc82-2fd3-3351-922e-6342bc2bcfa3 | -6.16413 | -44.49765 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c46d412b-9bc1-34af-9fce-47b2b04a50c0 | -6.41754 | -43.35855 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 302f68d3-2ecf-3db0-b9f7-92f9eece7c20 | -6.49775 | -46.00891 | 2025-09-18 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4a2d44b-3b88-331f-a9e3-ab2970b118e7 | -4.69814 | -41.96004 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82133eed-c0cd-3bde-9f98-81f4096aca99 | -7.0358 | -44.1718 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61f8c91e-aaa6-3465-bb9a-e5a974fbd049 | -7.00114 | -44.89518 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fe378cc-f3e8-33d2-aa54-342fd47c6e6f | -6.75137 | -46.01047 | 2025-09-18 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aa2252d-ff27-3554-bce5-065f547b7e8b | -5.81148 | -44.72549 | 2025-09-18 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b24766-a11c-3113-9d30-cbede04704d3 | -6.16192 | -44.48989 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 709c02c1-74c8-3b6c-81d8-a1bf51567874 | -4.0985 | -40.4906 | 2025-09-18 04:12:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 46bc8240-6af9-39a9-bda6-1fa6b7f02dc0 | -5.56919 | -45.61533 | 2025-09-18 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe307d9-bb53-3502-84a3-b9f7cd62d3c6 | -4.80798 | -42.73211 | 2025-09-18 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c6f8fb1-e1c1-3219-843e-0fd8aeeb0166 | -6.20828 | -44.28769 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93ee1036-00d1-363d-83f3-ce735e46df04 | -2.91708 | -48.31212 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f1ab1d8-7a38-3a67-adf6-cc29b54502b6 | -6.32854 | -44.04438 | 2025-09-18 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1474408-1cc2-3838-9392-eab03cb135a4 | -5.63699 | -43.88835 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 662cf62c-de79-3825-84d9-713bed0ebcc0 | -6.76951 | -41.60789 | 2025-09-18 04:12:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
