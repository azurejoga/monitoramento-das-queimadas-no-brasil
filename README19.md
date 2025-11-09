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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a1a6a51-4ed6-3306-b172-5d6d14891b39 | -9.09396 | -44.3228 | 2025-11-09 04:18:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 231497ac-9ab6-3a57-9e9f-cec6827b4caf | -8.89857 | -47.90428 | 2025-11-09 04:18:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a971eb44-1739-3ec3-873b-6935fc1d993c | -7.43029 | -45.75515 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83d44f72-cb49-3fad-8b2f-89ebc85cd007 | -9.37815 | -47.07903 | 2025-11-09 04:18:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1ea3e565-6107-3327-ba6e-7e9c13474284 | -12.10981 | -43.6459 | 2025-11-09 04:18:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bcefa6d-b199-3b57-8341-e5a65cd9e701 | -7.23458 | -46.7845 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17de7b3a-ea17-38e1-998c-4815b0813e5f | -6.85641 | -40.15419 | 2025-11-09 04:18:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d2dd25ef-2298-3166-9cfa-1d737fd9c707 | -6.02082 | -43.76931 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cefa45f-b49e-3e80-9f24-b6f323341a27 | -8.4868 | -40.52464 | 2025-11-09 04:18:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cd233657-b502-33c5-8383-0ff5e4202735 | -10.07378 | -45.59627 | 2025-11-09 04:18:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dd3451a-bff9-3025-bd81-a8a41a425423 | -9.05514 | -48.83678 | 2025-11-09 04:18:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c42917-3da1-342a-9c65-6dd8302100e6 | -7.03543 | -44.28488 | 2025-11-09 04:18:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 728cfc13-ee98-3a7a-9daa-638e81e16f24 | -4.99535 | -49.65392 | 2025-11-09 04:18:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b447a71f-b9da-3529-be47-546ee464ff91 | -7.09727 | -45.22604 | 2025-11-09 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee31e622-de7d-30eb-8882-4f1f5d4d92fa | -10.76671 | -48.84046 | 2025-11-09 04:18:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc99cf9c-5c08-3c57-9dab-c935c0685335 | -5.22873 | -49.57819 | 2025-11-09 04:18:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de11e73d-a8e9-3d40-9f4d-6c6b5b14ce40 | -6.22523 | -47.01492 | 2025-11-09 04:18:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a6c74de-7694-3517-b09b-25d0f728f525 | -5.89536 | -43.96189 | 2025-11-09 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53593ff5-dc5a-30a9-a0d5-9b57269380d7 | -6.74462 | -44.29664 | 2025-11-09 04:18:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb95082b-e3b4-300a-a508-dac775fba0f0 | -6.87958 | -47.24226 | 2025-11-09 04:18:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90d13700-63f3-3420-9477-502406b3fb0f | -12.10925 | -43.64947 | 2025-11-09 04:18:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49f5b11b-7f7e-3216-9d27-ace386b9248a | -8.19043 | -46.20471 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4302d296-a4f0-34a3-ab21-e5b683e57c2e | -11.91698 | -44.18515 | 2025-11-09 04:18:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b3699d3-8443-30dc-8742-1dfb6b3c34ca | -6.41443 | -43.76017 | 2025-11-09 04:18:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35b8e65d-ad0a-32ae-b614-25d988e03c2c | -11.73682 | -43.84476 | 2025-11-09 04:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 85c03cb4-5ef4-301d-98e1-607ccad5cf16 | -11.01783 | -49.35146 | 2025-11-09 04:18:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36cf2561-e575-322d-b204-d472297c90e2 | -6.22069 | -47.01891 | 2025-11-09 04:18:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78154bb2-23ca-3c6d-bff7-40a3b81f6428 | -5.20985 | -48.68483 | 2025-11-09 04:18:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbbac06b-0b66-3535-a804-e974d3242220 | -7.40143 | -40.0697 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38239c43-0c94-3be4-a1f1-7ad2f5d3a485 | -8.4904 | -40.52522 | 2025-11-09 04:18:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8fe8d097-dd55-3093-8b96-89f67e6c4f95 | -6.3302 | -44.26352 | 2025-11-09 04:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73cb9e43-ca54-36b5-9d35-6e8f3390ffdc | -7.55098 | -45.85391 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a92eee17-42e2-301b-8b2e-b3b115bff1df | -9.67717 | -44.56853 | 2025-11-09 04:18:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f569db8e-c1d6-3fa6-b3ab-397d31c13542 | -5.6039 | -46.96244 | 2025-11-09 04:18:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f239c0e-92c8-378a-ae82-dee56df0e4aa | -10.17198 | -49.31277 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75c9aa39-60c7-3d6a-83f9-9b5eb3786c08 | -6.12012 | -43.75982 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e1b1e89-28a5-3212-b00e-88bb9935b0c9 | -5.9994 | -44.03274 | 2025-11-09 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ce74fd7-4717-36c2-8afd-cbb0663d0b35 | -8.0183 | -38.5495 | 2025-11-09 04:18:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d7228b6-9e38-3ab9-aaf7-837686cdceb0 | -6.32206 | -46.20767 | 2025-11-09 04:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7d896f1-33ce-3fe0-9cf3-d6769fd76acb | -5.40222 | -47.26013 | 2025-11-09 04:18:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0a19948-8b83-3a98-84b5-9e2497a48828 | -7.03862 | -46.98177 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daaa2593-ea04-37d2-87f8-010ad1a0e9dc | -7.84872 | -38.43488 | 2025-11-09 04:18:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c8ff884d-6cc5-3f4e-a2c7-f6bd0e8e5bca | -6.85953 | -44.83543 | 2025-11-09 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf9d08c9-44b0-33d4-92cf-cbbb86d64303 | -9.95691 | -48.58615 | 2025-11-09 04:18:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df7daf13-97d4-3d22-8d79-0bc0fe66635b | -7.17333 | -44.94962 | 2025-11-09 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1fed5a7-4e94-32ec-be92-5c59a60d0ac6 | -9.81182 | -46.49007 | 2025-11-09 04:18:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3068af-a832-322d-88c7-bd4aafea7841 | -6.88208 | -49.25172 | 2025-11-09 04:18:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13db768f-2596-3ccd-86f8-399c1d150480 | -7.00156 | -42.78852 | 2025-11-09 04:18:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0134ce90-f46f-3c47-b2d9-37dcf0733270 | -7.17615 | -44.95385 | 2025-11-09 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cba8964-d0fd-337e-acfe-e9f37060c572 | -5.73131 | -46.4641 | 2025-11-09 04:18:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db740fe9-389c-387a-b602-7ddffa410cb1 | -10.33707 | -49.62613 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0fe3fd0-9063-3ffb-8628-692231756ddd | -10.4176 | -48.80596 | 2025-11-09 04:18:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a4d167c4-05de-38c9-8067-48b360d50ac0 | -6.71585 | -39.99826 | 2025-11-09 04:18:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b0099f3b-899b-35ff-8bf7-87188eb79f22 | -6.22145 | -47.01432 | 2025-11-09 04:18:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb235cdf-d22a-38d6-8ad3-e040a13cf23e | -6.79494 | -39.42371 | 2025-11-09 04:18:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e89d661c-43f3-3db5-817f-a2284befefb9 | -5.65211 | -45.98817 | 2025-11-09 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3bdbcd5-5f6c-3cfe-8295-f85455f684fc | -7.36425 | -46.83613 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2c1adcc-2548-34f7-9a27-7c5aae3ad381 | -9.9494 | -49.19843 | 2025-11-09 04:18:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6bc2881-0f7b-309b-97ae-ee8b875f16ae | -11.39832 | -47.63966 | 2025-11-09 04:18:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85307171-b1d1-399a-94ce-c2f0bee0bcae | -8.82045 | -50.05045 | 2025-11-09 04:18:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27344727-bce6-304a-89ab-68f3a130fbb5 | -10.34124 | -49.6269 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed39888f-c576-3618-a39c-2f79fbab7cb6 | -7.56473 | -45.88019 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 60d695ab-cd9b-387d-950c-d116ce3b44eb | -7.7088 | -46.01508 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb954665-9719-3c43-9a5c-d9776b23332f | -5.72763 | -46.4635 | 2025-11-09 04:18:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd56f40a-0e4c-36aa-8def-7dd7a3befc10 | -7.84468 | -38.43427 | 2025-11-09 04:18:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f03ef72-0eea-36a8-b641-43fbdc492d1c | -7.40177 | -40.06806 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cd579c3-f1ad-3ba2-b77e-0dedc2f34400 | -11.73294 | -43.84776 | 2025-11-09 04:18:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0733e4e3-b4ee-3564-ad1e-4a9501b602b0 | -11.0172 | -49.35505 | 2025-11-09 04:18:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6055dd2-ccd9-3a7b-85e8-afadcd55b25a | -5.43329 | -47.5626 | 2025-11-09 04:18:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75c24ee7-d963-34c5-a62d-2a6e015df145 | -7.17198 | -41.73494 | 2025-11-09 04:18:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6c21892-6498-335a-b8af-f225906886c0 | -6.03262 | -46.56187 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7717ea5-f0b7-3601-92ff-8db6e247a076 | -6.99545 | -42.78399 | 2025-11-09 04:18:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 39ed8165-a069-32e2-96a7-e9b956bc6c06 | -7.56122 | -45.87961 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a2058f36-d7e1-38d4-a64d-db696c8241be | -11.91753 | -44.18163 | 2025-11-09 04:18:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 319c3204-680e-39d1-a5e2-e76689aee51a | -8.82519 | -40.6223 | 2025-11-09 04:18:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b20e1a9-c250-3766-a3f4-65e8aa8f8ae9 | -6.02026 | -43.77281 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17fa58cb-51c5-316b-96f9-7810a1ae2717 | -5.8948 | -43.96543 | 2025-11-09 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29d0b980-bd69-32db-b169-9e3beec58645 | -7.94931 | -46.8462 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b49962dd-67cf-38de-926a-a04d9bbcaf99 | -10.34056 | -49.63072 | 2025-11-09 04:18:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| dc2ff8ee-1a43-3eeb-9df7-5d4299b7ba62 | -7.49515 | -46.61004 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8956adf-45d5-3e54-b5ca-93f686e299af | -8.04603 | -39.688 | 2025-11-09 04:18:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6279b79-122d-3c67-b786-ed18fee82901 | -8.98192 | -40.54878 | 2025-11-09 04:18:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db472d46-ae55-3892-a261-6037beb7a93f | -7.49586 | -46.6058 | 2025-11-09 04:18:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b87edb0-c514-3cf4-a32b-586850965e06 | -6.94684 | -39.31155 | 2025-11-09 04:18:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 033cb984-6fcd-31f7-b32b-64b982072b26 | -6.88775 | -49.24431 | 2025-11-09 04:18:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1648682-6373-3b5e-88d2-f59093656122 | -5.40268 | -47.26229 | 2025-11-09 04:18:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23a8419a-d40a-333a-a584-48756d379658 | -9.47445 | -48.74216 | 2025-11-09 04:18:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33644f59-55e9-3f07-ad54-521932f432a8 | -6.01637 | -43.77578 | 2025-11-09 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b07f7b68-3ac8-304e-ba66-e5cb212b9706 | -6.70399 | -39.6772 | 2025-11-09 04:18:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cd2661c-2b42-3169-a17e-d13961304784 | -7.5615 | -45.85561 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6847edcd-d532-3c7f-ad21-4f4dbb0bd948 | -7.95296 | -46.84682 | 2025-11-09 04:18:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbbe6f95-b3aa-392c-8863-5988a0c7a29f | -7.55736 | -45.85895 | 2025-11-09 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb7699a4-2d66-31ee-897b-8ae18887a567 | -6.00275 | -44.03328 | 2025-11-09 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60aa1944-8485-3cee-b15d-c9974c854214 | -6.54884 | -44.46648 | 2025-11-09 04:18:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cccda2d8-bde3-34c5-95fa-8a77a8ad0263 | -7.03487 | -44.28841 | 2025-11-09 04:18:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa70c523-d5ad-3364-a1c1-04add8f3d136 | -7.92108 | -43.30838 | 2025-11-09 04:18:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f63156b5-2d5a-39ff-987b-2fdbfe419d17 | -8.44774 | -48.10237 | 2025-11-09 04:18:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9b9e99d-603c-3cee-82c1-5bd888ed0038 | -6.68609 | -46.66664 | 2025-11-09 04:18:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba54bc88-7f46-3310-9741-d3f524507d89 | -7.41271 | -40.06971 | 2025-11-09 04:18:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec34eb30-7168-35aa-b24b-92b2e9ef61e3 | -6.55261 | -43.21218 | 2025-11-09 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
