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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79d5ab21-8b1a-3d3f-b47a-1271f68f7cc3 | -5.51482 | -43.8769 | 2025-09-30 00:35:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 05261ca2-d593-378c-9d92-98da6c76fbf8 | -6.20985 | -44.2191 | 2025-09-30 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e1930c59-732a-37ea-bea5-2cd13b9cd8f2 | -3.80909 | -47.56566 | 2025-09-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e2ef30d4-5ef8-35c6-b584-4c182d9d9517 | -3.27762 | -50.03161 | 2025-09-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8957ec0f-c709-3b57-a627-9fd7c82119aa | -7.36978 | -47.05086 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 13473f01-dd87-396b-a16b-635b575112a4 | -3.38173 | -52.71529 | 2025-09-30 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 82b10c36-a9c6-3fac-a61f-4b90ca8d3a2a | -7.12109 | -45.53931 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e7fe52bc-5ee9-343a-bf55-de34e44ad0a4 | -7.36839 | -47.04111 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f8152da5-3808-3b10-8b32-0de5faf90509 | -6.82015 | -48.70717 | 2025-09-30 00:35:00 | TERRA_M-M | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7c0b73f4-a42c-30a8-9867-d0afdaf1db32 | -3.25453 | -50.12426 | 2025-09-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 4ab475ed-186f-3100-9bc6-a795326c1c99 | -6.29013 | -43.92232 | 2025-09-30 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| d22e48be-919d-3df0-b66d-e369db768c56 | -6.29416 | -43.92729 | 2025-09-30 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5b3153ca-fd95-3c97-b557-f26812e01691 | -2.73925 | -48.6762 | 2025-09-30 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f4b41bd-6986-332f-8ffa-97518673b829 | -5.24391 | -43.74635 | 2025-09-30 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4c69a5b1-3597-340a-a994-97b3aa81f78a | -7.8023 | -48.02546 | 2025-09-30 00:35:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c55e5eca-9806-389b-8448-3212bbbd28e4 | -4.90264 | -43.47055 | 2025-09-30 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f23c451b-555e-3386-89bb-27849efbfb48 | -4.871 | -45.05434 | 2025-09-30 00:35:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 658fa34a-46bc-38db-8311-aaa17ec76ead | -4.07003 | -48.03864 | 2025-09-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6c7f9923-e8f3-3bba-814d-ce6b552e4a75 | -6.43627 | -43.08704 | 2025-09-30 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| f3baa791-b5ad-3655-af60-5466a1fd8689 | -3.05775 | -48.70895 | 2025-09-30 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7008d6b2-d700-3ca2-bd5d-1502fa93d36b | -5.48384 | -48.6545 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8fb4f120-ad8e-3d2d-9e48-baa6a8aeb3f3 | -3.25332 | -50.11548 | 2025-09-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| dbd7020e-2aff-3c0f-b3ce-def39fe9000e | -2.66299 | -47.86969 | 2025-09-30 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 918e5496-5cae-37b4-aed5-cabb6977fcd9 | -3.8105 | -47.57558 | 2025-09-30 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 0bfdd7ab-1682-3ebb-b137-dc0f0432363f | -6.55303 | -47.27466 | 2025-09-30 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ff91b60-795a-3589-a3b3-97b99c21198b | -4.35294 | -45.59119 | 2025-09-30 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 1d677cde-b2ec-3f88-b111-c2ab382c3dba | -4.25401 | -48.56161 | 2025-09-30 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d2f671e5-8c25-30c9-af92-2129dcd17de1 | -3.47465 | -51.59315 | 2025-09-30 00:35:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6e6ba1cd-e4a6-3a0a-8aff-34b6078ba48c | -5.23629 | -43.69443 | 2025-09-30 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 5705d3be-9b92-3c69-b4c9-05cbdfb12bb6 | -7.12592 | -45.50177 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed017ad3-8da6-3f1e-b42f-bc40883c053c | -7.56539 | -49.84029 | 2025-09-30 00:35:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2a5143c-8747-36d3-b050-716a7d78d690 | -4.3548 | -45.60388 | 2025-09-30 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5691bc9f-7e6e-3271-bfb9-71344bd785f2 | -7.30405 | -47.30236 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c9b7d70a-7064-33f9-bbd3-76669eea3da8 | -7.04477 | -46.4092 | 2025-09-30 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62d5f9e6-e5f5-304d-a9e8-cbfdf22ed010 | -4.57625 | -47.70626 | 2025-09-30 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44571edb-07e0-3272-963e-0a85a66955c3 | -7.65725 | -49.57378 | 2025-09-30 00:35:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| eddda396-25f4-3866-a383-b7db38bd5076 | -5.09815 | -47.48551 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5ed1d40a-50a0-31d2-852a-654908cc6353 | -5.96557 | -44.11576 | 2025-09-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| aa5dcc02-10fc-32a6-9820-ade86ff6037e | -6.02482 | -44.75857 | 2025-09-30 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9c3fd687-ef06-37b0-8fae-31f2065a3de8 | -7.2367 | -46.76385 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| eb89d880-6ff5-31cd-84ef-03ad7ea3cb69 | -7.05799 | -45.18578 | 2025-09-30 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c87cc5ff-c220-34b5-a008-3ed14f04077d | -6.88856 | -44.52333 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4967c064-407d-3c03-ae61-c9f1a941d79e | -4.87038 | -48.88459 | 2025-09-30 00:35:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 2ff461d1-374b-34bb-9f72-dd4112b0999e | -6.3741 | -45.61627 | 2025-09-30 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 868cbff6-08a7-3739-99c6-0a052d6a43aa | -5.77642 | -48.4972 | 2025-09-30 00:35:00 | TERRA_M-M | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 03e930e9-8e55-3119-8e22-09e8d25d0ebf | -5.74142 | -42.68042 | 2025-09-30 00:35:00 | TERRA_M-M | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| fe8c138e-43ce-3024-a048-cd5c66c14ad4 | -4.95922 | -47.60706 | 2025-09-30 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 3bc956e6-9ffa-3281-96e0-171a88cfaadf | -6.29252 | -43.45994 | 2025-09-30 00:35:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 40d46455-1e57-3562-82d3-b899e093b142 | -4.95784 | -47.59728 | 2025-09-30 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57ef7b16-2192-34fb-927c-a61141fb233f | -7.05988 | -45.19839 | 2025-09-30 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 3179e8b5-6f51-3f52-92a3-7a99a9b83be4 | -3.85883 | -48.96827 | 2025-09-30 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fcc8206c-5d65-3b7a-8a09-97fe8b9be311 | -6.43141 | -43.07557 | 2025-09-30 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e62ea7ae-d0c1-3f21-981f-7097ed8ebfe9 | -7.11309 | -47.77847 | 2025-09-30 00:35:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0736b910-e365-37eb-9293-1c496a8dcc6d | -7.61318 | -47.3356 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 256d58ee-920c-30ae-a289-144446898a05 | -4.68013 | -50.50306 | 2025-09-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4bcb95e-955a-3b55-a031-422b72fc8a7f | -5.74685 | -44.74694 | 2025-09-30 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7a99ad37-88be-3cda-9a2a-e9a6b0aaf6df | -7.0173 | -44.46812 | 2025-09-30 00:35:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e42c102a-8561-3b87-be9a-badffdb10eb9 | -6.20771 | -44.2047 | 2025-09-30 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9c1ceb4a-0ff2-307d-b7f3-a5965acbcc65 | -5.51733 | -43.89377 | 2025-09-30 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 900b71dd-32bb-384e-b066-265444f91ac0 | -5.53294 | -46.38302 | 2025-09-30 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1825df11-5ab1-338c-bb2b-93fb3c2328eb | -4.72701 | -46.47704 | 2025-09-30 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| b367b7e8-d614-3967-be14-7931905130a4 | -4.5264 | -50.52747 | 2025-09-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b607b875-81cc-33e0-9ce7-12d061e8e4e2 | -5.86537 | -45.7765 | 2025-09-30 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cde356e0-6bfa-3c9b-bbfa-5e019576abb2 | -3.25428 | -49.13298 | 2025-09-30 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6f57b291-42d8-3b00-aaba-d44c62e65181 | -4.66473 | -46.46348 | 2025-09-30 00:35:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1af40a82-a69f-31cb-8b24-d2e441d0c181 | -5.67127 | -45.3034 | 2025-09-30 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8046cefb-e80b-3ae3-adef-8075ff11db2d | -5.90627 | -43.70712 | 2025-09-30 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5177ceeb-bb47-35d0-966a-9583cefba63e | -3.27884 | -50.04037 | 2025-09-30 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 47c1c6a0-4dd2-3a3f-8d74-1123bffd406b | -4.35104 | -45.57824 | 2025-09-30 00:35:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 0699ff63-e34f-338a-87be-0aa474586ef5 | -2.55988 | -47.65602 | 2025-09-30 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5bf4e7c8-1f84-3baf-86ab-b1ff0cfca757 | -4.51529 | -50.44661 | 2025-09-30 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ac7e853-1c7e-3e86-9efb-fc2093a91804 | -7.47386 | -47.26505 | 2025-09-30 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f4b82112-be5b-3e40-93b5-2ee5e30a6915 | -1.29077 | -54.17923 | 2025-09-30 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 7be2efa6-32bf-38eb-bb42-47e9249a6363 | -0.10397 | -51.27942 | 2025-09-30 00:35:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 049be196-f281-3a73-9511-92d104cf460e | -1.29247 | -54.19188 | 2025-09-30 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 3f489e8f-a158-3eb2-b37f-89aa3731375a | -1.28529 | -54.18536 | 2025-09-30 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| bd3839e6-62b8-32e3-a33f-e2d9a59fa012 | -0.0951 | -51.28065 | 2025-09-30 00:35:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 04228f97-576d-3c86-9258-0b77f0dc4422 | -0.10274 | -51.27052 | 2025-09-30 00:35:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2aecf4a2-eb9e-394c-ab0b-d9d74ebd7255 | -1.29586 | -54.18429 | 2025-09-30 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 6ad41aba-597a-3901-8626-d3256f11b0bd | -1.29402 | -54.17134 | 2025-09-30 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5a1aa720-c091-3a8b-b536-8da31b005096 | -5.5243 | -43.8647 | 2025-09-30 00:40:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5559a340-cb43-3075-a8eb-8774c4113b0c | -10.6317 | -53.7011 | 2025-09-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 828f8afe-baf7-3476-b39f-1e925fe8e1bb | -11.7519 | -44.7461 | 2025-09-30 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| f99d3717-46b7-360c-b7e8-a591b8974e11 | -10.2041 | -44.8915 | 2025-09-30 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 257.7 |
| 3979d774-787a-3015-a2b2-e977cfd2ddc3 | -10.1851 | -44.8939 | 2025-09-30 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 304.6 |
| 5906b4ce-a404-3c34-adc9-cef0f7701517 | -11.7524 | -44.7228 | 2025-09-30 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 23603fc4-1428-3ff7-b6f8-540c10e887be | -8.672 | -47.7144 | 2025-09-30 00:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 8e2fbd82-3ca8-37da-8530-372d89534687 | -4.354 | -45.5773 | 2025-09-30 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 295c127a-8fec-3164-a3a5-5f6c1934426c | -5.5241 | -43.8878 | 2025-09-30 00:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 81b35e27-eff1-3674-b9cc-8f880f2e6e5c | -11.8868 | -48.0323 | 2025-09-30 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ba45b668-96c0-3953-a6b3-77e26a905bf7 | -12.8429 | -47.0063 | 2025-09-30 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fc709197-1fa6-3771-b1f3-298b021fa63a | -10.2045 | -44.8684 | 2025-09-30 00:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 246ebacb-78d7-3adc-87d8-2efcfa059c82 | -20.05 | -41.2992 | 2025-09-30 00:40:00 | GOES-19 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 7b83ac40-5751-366f-9a7c-44c0b9f3db6e | -1.2928 | -54.1784 | 2025-09-30 00:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4dfd1797-e22a-34b4-bf60-305a354edb80 | -11.2138 | -47.2086 | 2025-09-30 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 73497e6b-9392-36f8-8a83-93f5a795fd30 | -4.3538 | -45.5997 | 2025-09-30 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 91f7a092-0d87-375b-bd53-5569e30de4d8 | -11.1546 | -54.126 | 2025-09-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.1 |
| 29e8fd97-b6d1-30b9-b59b-648cfb78d766 | -11.1735 | -54.1242 | 2025-09-30 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 778d9ffc-e571-37ac-86dd-b5d73b866209 | -3.1013 | -47.0082 | 2025-09-30 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 89afeffd-9483-3ce3-bca5-df5b56fff83f | -12.8638 | -46.913 | 2025-09-30 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |


[Clique aqui para ver as próximas entradas](README11.md)
