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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ef4d456-5ee4-3e4a-9fe9-bb45d01b5bde | -7.5632 | -45.2714 | 2024-10-10 00:20:15 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47af2fe6-f019-3ae6-9e0e-a0365eba971d | -7.5652 | -45.280701 | 2024-10-10 00:20:15 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 609ece2d-716e-3162-b756-fb3ea3e849b3 | -7.5534 | -45.273602 | 2024-10-10 00:20:15 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce2cbd5-55d5-3295-9034-d436e51a9bf5 | -7.5554 | -45.282799 | 2024-10-10 00:20:15 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b176596d-00e8-3e30-b57d-16141029dd1a | -8.3252 | -49.551899 | 2024-10-10 00:20:17 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 527b5f3a-3d8b-3b9c-a0f0-ffe18d35161d | -8.3289 | -49.570099 | 2024-10-10 00:20:17 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cd9ca48-9adf-3498-b097-62cb73f5a6a6 | -6.2997 | -40.483501 | 2024-10-10 00:20:18 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 59e7fddd-3c31-3b24-8209-691e22b45700 | -7.8782 | -47.7211 | 2024-10-10 00:20:18 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98cfe8c6-9cb2-3304-96ff-13d0580ba3f8 | -6.5971 | -42.097198 | 2024-10-10 00:20:19 | METOP-C | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9ae32c54-98cf-3acb-a4bb-55aa60dbfa1d | -6.5987 | -42.104099 | 2024-10-10 00:20:19 | METOP-C | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e53e5c4-b44e-378a-94f3-396e72bc71c0 | -7.2409 | -44.972301 | 2024-10-10 00:20:19 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce7d31ec-ad43-3706-8b1c-e85318174c4a | -7.2311 | -44.974499 | 2024-10-10 00:20:19 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a000b356-36e7-3447-a0e8-972e3f5cc1e0 | -7.233 | -44.983299 | 2024-10-10 00:20:19 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ca830508-086e-3543-b49a-4f4eec6e42dc | -7.235 | -44.9921 | 2024-10-10 00:20:19 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3c1ec3-51b2-3959-bfb4-a92974725411 | -7.2233 | -44.985401 | 2024-10-10 00:20:19 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94d41eee-ad35-3bbe-9676-ed12ca1e2d2f | -7.2253 | -44.994202 | 2024-10-10 00:20:19 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a966723c-885a-3a86-8755-df386a114d1e | -7.3531 | -45.622898 | 2024-10-10 00:20:19 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08ff508e-1ba6-3642-8527-3dcbc8ec27b8 | -7.3552 | -45.632599 | 2024-10-10 00:20:19 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f77b6b0f-0fcf-3a45-aca3-7255b8d2ab43 | -5.8524 | -39.2234 | 2024-10-10 00:20:20 | METOP-C | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bec35362-9a90-3759-9505-8d21b1afc8b5 | -5.8426 | -39.225601 | 2024-10-10 00:20:20 | METOP-C | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2e4b5549-b48b-37cb-82f2-6830b16c2199 | -6.5222 | -42.0849 | 2024-10-10 00:20:20 | METOP-C | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8553d5b8-045a-320f-b08e-bef5f0e46b4a | -8.2515 | -49.9771 | 2024-10-10 00:20:20 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1adaf836-5252-3f04-a92e-1ccbe253e665 | -5.7478 | -39.085201 | 2024-10-10 00:20:21 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 34a07c32-644d-35fe-9815-223f2ff25c2a | -7.5179 | -46.803699 | 2024-10-10 00:20:21 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de047342-d934-3823-b546-87dad15cca73 | -7.5204 | -46.815201 | 2024-10-10 00:20:21 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9da7eef-feee-3c0b-b8d4-2de81167788d | -7.0486 | -44.705601 | 2024-10-10 00:20:21 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e91e94cd-d8ae-3c5b-b732-de9e0d73056c | -7.5056 | -46.794399 | 2024-10-10 00:20:21 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8112a0d3-8f1b-3e35-947b-ad6a4c242edc | -7.5081 | -46.805801 | 2024-10-10 00:20:21 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 621d434f-a694-31ff-80a6-f3dc642b26a8 | -7.5106 | -46.817299 | 2024-10-10 00:20:21 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7822ff8a-a987-33a8-830e-455f6306fcd4 | -7.513 | -46.828701 | 2024-10-10 00:20:21 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 176ff187-2b4f-30cb-9efb-1a8bd443dae2 | -7.0369 | -44.699402 | 2024-10-10 00:20:21 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2f4e33b-d95c-3a08-98b1-4239ca616cf3 | -7.0388 | -44.707802 | 2024-10-10 00:20:21 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 780ee48f-314d-3fb3-a0af-7c41a4035847 | -7.0215 | -44.675999 | 2024-10-10 00:20:21 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12a609fe-0044-39f8-a2e4-6d18aa552acd | -7.0233 | -44.684502 | 2024-10-10 00:20:21 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5f38602-c131-330a-a999-245ca146d7af | -6.864 | -44.060001 | 2024-10-10 00:20:22 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 319bc3ae-3534-313f-8ae1-a4a2a441cdf3 | -6.8658 | -44.067902 | 2024-10-10 00:20:22 | METOP-C | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7611f726-36e5-39ec-8995-ba1b8d6c9bb3 | -6.8647 | -44.2015 | 2024-10-10 00:20:22 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 299f9a98-af9c-3b16-9522-a26cb7b49ab0 | -7.3227 | -46.140499 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35358c0b-18b4-37f6-8cc6-1023e15738d2 | -7.325 | -46.150799 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b0fbb80-95ec-31c3-80ec-3ca8ff9bb87d | -7.313 | -46.142601 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78d3d97e-8bd6-3b78-b5e1-50fb42909cc7 | -7.3152 | -46.152901 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0d6c92-cb24-33a3-b350-1c0d84a5b8f9 | -7.3175 | -46.1633 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 149652cb-e91c-3d8f-bce2-ccc058ebe847 | -7.3032 | -46.144699 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 856df0ce-e435-3def-9b8c-06fe49cc3f94 | -7.3054 | -46.154999 | 2024-10-10 00:20:22 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f1f7b1d-be51-34d5-b07b-9bcb9dfa89bb | -7.0548 | -45.058998 | 2024-10-10 00:20:22 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a3b3b5ed-f004-3bf1-9ccc-4a2b59eeaf24 | -6.6491 | -43.558601 | 2024-10-10 00:20:23 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91264478-7512-3adc-b142-c4744e314bcf | -6.6508 | -43.566101 | 2024-10-10 00:20:23 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d07199a7-b986-328b-ac50-acb17d3c9727 | -6.6525 | -43.5737 | 2024-10-10 00:20:23 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 245ad7db-b7c0-369f-b4cd-733483275b23 | -7.3711 | -46.692699 | 2024-10-10 00:20:23 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 581e5a9d-901a-3759-a7f6-b2dc7dcca682 | -7.9924 | -49.657799 | 2024-10-10 00:20:23 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc91236b-1e96-33f6-926c-3bcf710058e9 | -7.9962 | -49.676102 | 2024-10-10 00:20:23 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfda922-8eb1-39d6-abbe-0dbe0f659ad2 | -7.4209 | -47.2062 | 2024-10-10 00:20:24 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5e5ee8d-4f77-305c-be42-32611462f7b2 | -6.3515 | -42.422001 | 2024-10-10 00:20:24 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1dbdfba-d8c3-3dda-938b-61cbc0bf1bdd | -6.5496 | -43.1619 | 2024-10-10 00:20:24 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c025c58-3a39-3df9-8be5-c3dc1ac71c54 | -6.5513 | -43.169201 | 2024-10-10 00:20:24 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8fc1e93-f689-33b8-be17-771476152d88 | -6.5801 | -43.5266 | 2024-10-10 00:20:24 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5a1a9d5-9f42-3183-87e2-fd4c9ae14a64 | -6.5818 | -43.5341 | 2024-10-10 00:20:24 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4678626-c7ee-3611-a3b2-595f876edfed | -6.8755 | -44.619598 | 2024-10-10 00:20:24 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a2fd979-d583-3323-bbb1-c863967cca81 | -6.8638 | -44.6134 | 2024-10-10 00:20:24 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 410dfd34-ae4f-313c-ae60-f8f163f9bf07 | -6.8657 | -44.621799 | 2024-10-10 00:20:24 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0a0601a-1451-3e62-bbc3-5b56314cca53 | -6.8675 | -44.630199 | 2024-10-10 00:20:24 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a403d5b-e012-397a-90ab-fe7d0f4e4284 | -6.9725 | -45.104698 | 2024-10-10 00:20:24 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08df5d0c-d8bb-32a0-ab4d-4744a709470f | -6.9199 | -45.238201 | 2024-10-10 00:20:25 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eff2023d-9903-3f86-a0bb-105d94def985 | -6.9219 | -45.2472 | 2024-10-10 00:20:25 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6e992ba-2496-3168-9e3c-f585c670306c | -6.7407 | -44.475101 | 2024-10-10 00:20:25 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5bedb78e-34ac-36a4-92d0-d42674f4a61f | -6.9101 | -45.240299 | 2024-10-10 00:20:25 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d79b66ed-841b-3706-af98-be7b6ea6a27a | -6.9402 | -45.377102 | 2024-10-10 00:20:25 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29e147b5-76f2-3be3-aae9-27d41958c60a | -6.9467 | -45.453098 | 2024-10-10 00:20:25 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8158a55e-e34a-3857-9d79-8cf7c0330607 | -6.9488 | -45.462399 | 2024-10-10 00:20:25 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72c99c41-b1be-31a5-9b2d-adce593787bc | -5.5237 | -39.450802 | 2024-10-10 00:20:26 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7b4df8c0-c22e-30b1-8b51-b2cec89bc0b8 | -5.5255 | -39.458302 | 2024-10-10 00:20:26 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 84dae5b8-0239-32b5-ab18-409868a3dfab | -6.5709 | -43.806499 | 2024-10-10 00:20:26 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 124d4030-af0a-3caf-9bfb-15b0577894a4 | -6.5726 | -43.814098 | 2024-10-10 00:20:26 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f36711a-aa08-3e17-9378-e3e22fe73f07 | -6.5444 | -43.780201 | 2024-10-10 00:20:26 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 617451b7-89a3-3021-a177-a130b50bd6b3 | -6.3751 | -42.9356 | 2024-10-10 00:20:26 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 3c94698c-5672-3176-bb85-ded781739679 | -6.4175 | -43.352402 | 2024-10-10 00:20:26 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92c1d0bf-817d-3019-8b3d-8eb58baaed1b | -6.5346 | -43.782398 | 2024-10-10 00:20:26 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74a70855-a500-3cc3-9479-3e00d8240496 | -6.9369 | -45.4552 | 2024-10-10 00:20:26 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d24016c4-dd4c-326e-8bb3-d7ff22aae9a6 | -6.939 | -45.4645 | 2024-10-10 00:20:26 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43aef687-b951-3283-bdd9-e9c54844839e | -6.8887 | -45.282902 | 2024-10-10 00:20:26 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aea1ac16-f690-3327-b610-dd36f61f7be6 | -6.8907 | -45.292 | 2024-10-10 00:20:26 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b52e1635-f3c4-3415-a139-8939b257d6ab | -6.8927 | -45.301102 | 2024-10-10 00:20:26 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87d72267-9962-32e6-9c70-9a5aa3f59773 | -6.8789 | -45.285 | 2024-10-10 00:20:26 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec6579e2-0686-3119-9bde-c10919fc3ad2 | -6.8809 | -45.294102 | 2024-10-10 00:20:26 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 27d744a8-98c9-3fca-b20a-12edbb7f6771 | -6.8829 | -45.3032 | 2024-10-10 00:20:26 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 898cf83c-bda0-3cf4-a034-f8c570152537 | -6.4044 | -43.339901 | 2024-10-10 00:20:27 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f477ff6-f36b-32d3-a15e-f4ceae43dcc9 | -6.4061 | -43.347198 | 2024-10-10 00:20:27 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cb975f5-03c0-36f3-97ce-3ec304c65fcd | -6.3946 | -43.341999 | 2024-10-10 00:20:27 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b208128-c597-3196-9532-bb578c895f81 | -6.1877 | -42.5172 | 2024-10-10 00:20:27 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffaee980-74d9-3999-9b17-e28cf6fd0e44 | -6.1893 | -42.5242 | 2024-10-10 00:20:27 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1385e6a8-0dd0-3fa5-af41-1048d96f6ad4 | -6.1795 | -42.526402 | 2024-10-10 00:20:27 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d3733a5-6892-3145-9ac4-5cca56513dcf | -6.181 | -42.533401 | 2024-10-10 00:20:27 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0359584a-21bf-38e6-acac-a428e3893193 | -6.886 | -45.643398 | 2024-10-10 00:20:27 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f7edb19-f2b0-33f9-aca0-227968bcc419 | -6.8881 | -45.652901 | 2024-10-10 00:20:27 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c94b2952-c09b-3141-9b09-9570caf27c72 | -6.9044 | -46.006901 | 2024-10-10 00:20:28 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4beabb3-7090-3641-a4e6-37f05659284c | -6.3629 | -43.796101 | 2024-10-10 00:20:29 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2ff4047-c294-3523-9246-a5e4e4f232d7 | -7.5291 | -49.3843 | 2024-10-10 00:20:30 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c65a82b-cd71-354f-bfce-71effe7317e4 | -6.1986 | -43.431702 | 2024-10-10 00:20:30 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8bde549-2a8b-3c9f-81f7-525696bba79c | -5.9484 | -42.235001 | 2024-10-10 00:20:30 | METOP-C | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 750803de-4858-304b-a49b-71f83112e895 | -5.9499 | -42.241901 | 2024-10-10 00:20:30 | METOP-C | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README10.md)
