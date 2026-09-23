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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d6f2d37-8e3a-392e-b2bc-dc910a294ca5 | -5.4054 | -60.196701 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f4c8fe7-3f8c-35fd-9c6b-d6e29a99f585 | -2.8548 | -57.785198 | 2026-09-23 00:58:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdcbb73f-38d4-3356-90df-23c06333046e | -8.5866 | -54.631599 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4dc03f-aa63-36cf-afde-36f2cff5e760 | -11.6678 | -43.473499 | 2026-09-23 00:58:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d10b7baf-1e88-3372-bbe3-4979a2c6a7d0 | -8.4951 | -57.612801 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7ab228-2a7d-3b32-b4e3-d7a0550b1347 | -13.4451 | -46.242001 | 2026-09-23 00:58:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c1612fa-19f6-3bf9-9799-e177d97b9015 | -3.3326 | -59.853901 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 718f5be1-0f60-3b20-9457-b17a6c8318de | -5.8537 | -52.0191 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22974430-99e8-3ba4-98b0-8dcec2f2be9e | -4.5131 | -54.9776 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aea4b52-7a6e-38f8-b721-5c528f204f57 | -6.3753 | -55.282299 | 2026-09-23 00:58:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18d6bd08-8d72-3ed8-844e-22c3c17fc7bf | -6.296 | -57.7314 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36159306-9d69-3ee8-8068-c8b55d66f117 | -3.5849 | -59.059898 | 2026-09-23 00:58:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 447c33dd-06ff-382e-91bb-d0da1bb30d44 | -12.7776 | -50.8941 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0087f64-ae52-3fd9-8fd7-8b41a908d815 | -3.2205 | -46.945801 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0299d0c2-03e5-3c6a-b49f-78b0970ae04a | -10.9083 | -51.515499 | 2026-09-23 00:58:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1a037e9-ad1c-3c39-a354-2e9617fe5161 | -6.5966 | -59.942501 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5cbb6e3-5024-3153-b0a0-047b3d56892c | -7.0313 | -44.638599 | 2026-09-23 00:58:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d009ed1-c75a-38a7-9fb4-3ca2d0d3064f | -9.583 | -48.450199 | 2026-09-23 00:58:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 147ba37c-2907-35cf-ba2c-10a65359f5e5 | -6.0953 | -57.660099 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e9b13f-f665-398b-99a2-edfc924f5b0a | -7.3983 | -55.2076 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a297299-09c7-3c6d-aa21-507602bd4479 | -11.6995 | -50.9203 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cc13e13-b544-38b4-a1c5-99c38c734bf9 | -6.7221 | -44.145699 | 2026-09-23 00:58:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9762f3ef-3c95-3ce0-9094-c5f00b83704e | -8.8313 | -50.493401 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9537f4e-ca52-397d-978b-973a9beb82a3 | -3.0319 | -54.408901 | 2026-09-23 00:58:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48d405f3-3a12-3fb6-ae20-9c59973c342c | -3.2368 | -53.9543 | 2026-09-23 00:58:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 180c8357-4115-3714-8c3a-8b9d4bec1700 | -5.776 | -47.137199 | 2026-09-23 00:58:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4bbf5db-9ada-3f90-b30c-513dcbf79a90 | -6.4474 | -59.960899 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 083bb7a6-1e1b-33d4-b388-561dc4bca392 | -6.4542 | -54.994202 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab4cdd9b-c15c-3980-b5ca-7a5d7ccaa137 | -11.6816 | -50.932201 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 372dfcb6-e9d0-39fb-a8a2-1d8a017127f8 | -6.3226 | -43.905499 | 2026-09-23 00:58:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebca9de5-0057-3aca-a753-1e8f69ea4337 | -13.8632 | -48.573601 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c42a9b9-6970-3d3c-a2b4-f7f2c41c5193 | -5.8554 | -52.026402 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00dd952-9d8a-37d6-9729-3ce96476d040 | -12.4813 | -46.9846 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e722fa59-8236-3df8-b022-f310c1a479d6 | -10.7169 | -48.694 | 2026-09-23 00:58:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3854e83b-932b-3f9c-80be-8276f3de4624 | -13.8534 | -48.576099 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f3f3dfd2-7c1a-36ad-8394-c98a85b2f5d7 | -4.3278 | -55.430302 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eec1d8d-c244-3eb9-b688-1cb8d39380d1 | -7.4372 | -49.8395 | 2026-09-23 00:58:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 169a66cb-a940-3177-8ccc-7ba751e5b265 | -13.8652 | -48.5821 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 43dbee77-30cf-3e0a-88d3-cb05d0604580 | -11.3015 | -51.340801 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23875d45-7bab-3ed9-99b0-9ab3fee0d268 | -8.258 | -54.7728 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b61012a7-f41a-3d5f-a5de-5e38f51d87d0 | -5.8117 | -47.751499 | 2026-09-23 00:58:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49457990-09da-3a6a-bd60-f297c8488b17 | -6.3337 | -43.9492 | 2026-09-23 00:58:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72890adf-8f1c-3e23-b770-a850ef963992 | -5.8902 | -52.0872 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f10293d2-c85f-3a6e-b6c2-9eedbb5c8d23 | -8.7826 | -45.623901 | 2026-09-23 00:58:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c898b8c0-2ad2-3b41-a300-ae9a4f22ead4 | -10.3242 | -50.516201 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1b12907-1b19-3ade-9bf5-3cebbe9990b9 | -6.4627 | -59.984402 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd99e2a1-3844-362f-a848-c4d14e21abcd | -8.276 | -54.761299 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a80c8036-86a9-3d03-b4b3-a21d7bbfd940 | -5.9798 | -57.694801 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 535751eb-fbc5-33ed-b057-a41e1448f4ea | -1.3246 | -54.655201 | 2026-09-23 00:58:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c10c2c99-1e31-3ef0-9657-84c75d98bc68 | -11.0953 | -48.334599 | 2026-09-23 00:58:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7417ed15-7782-3b7a-a7e5-df0207c00bdd | -3.583 | -50.032299 | 2026-09-23 00:58:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38689b70-a3d2-3434-8cc8-80f5a7c56567 | -3.1042 | -60.707401 | 2026-09-23 00:58:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61ea6f78-f01c-3c93-a6bc-b44e853255de | -5.8639 | -52.062698 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e435f1e3-7e31-3edd-95b2-8e6c6e9dafac | 1.5653 | -55.8591 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a98bef6-67a4-390a-a9b2-b7821dda7024 | -4.0014 | -52.0854 | 2026-09-23 00:58:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9818339c-421a-33fc-aa73-893952e327d2 | -12.7955 | -50.882198 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4cf39af-f54a-3410-be4e-7e9992ea1255 | -3.0097 | -54.177601 | 2026-09-23 00:58:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31bcf53c-c4d8-3ce6-adeb-6316609de135 | -9.8591 | -48.310101 | 2026-09-23 00:58:00 | METOP-C | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a73a118f-517a-30b6-982e-4712dff512bb | -10.4534 | -51.290001 | 2026-09-23 00:58:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 638c4adf-faa3-39cc-89bd-1b52bf1f71f6 | -5.7967 | -49.148499 | 2026-09-23 00:58:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbd985d0-51ac-36ef-8de9-a458063ff13d | -6.2862 | -57.733601 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83d832e9-b2bb-3448-adc1-340228c0d9a9 | 1.5602 | -55.836498 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c802b11-27a0-3bdd-aac6-b4c8f568c060 | -9.5094 | -59.7328 | 2026-09-23 00:58:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8472e4d3-2e0b-3479-9fc6-3b2d1f8b5f50 | -11.3519 | -43.372002 | 2026-09-23 00:58:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e4c9f6c-cb6d-3feb-9e91-b26f55f0fa98 | -3.8198 | -58.871799 | 2026-09-23 00:58:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac74d6c5-7939-3b98-a536-f0aaeee605b4 | -11.8807 | -45.784199 | 2026-09-23 00:58:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 42c24bae-594d-337c-975d-7b333682b0c9 | -11.7012 | -50.927502 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3d2b5a6-d87b-387d-8631-2ece039fa362 | -3.2814 | -57.851398 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6cc8c34-fcb1-3be2-b693-bd9591f091c2 | -11.7751 | -50.979099 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8522314-69d6-3c18-ba43-57c988915d34 | -12.4786 | -46.973598 | 2026-09-23 00:58:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f77f27d1-74b4-393c-902e-dc5ea6e2cace | -6.4437 | -48.4482 | 2026-09-23 00:58:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 039640f1-98eb-3d12-ab63-da1f810d0686 | -12.7513 | -50.8699 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70a0442d-5991-38d6-907e-b01ab971b857 | -6.6762 | -58.5728 | 2026-09-23 00:58:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b738956-728d-319f-885e-1d5f831a3286 | -11.8672 | -45.730801 | 2026-09-23 00:58:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce180168-bbd1-3145-a438-d433e808cb19 | -11.4707 | -47.332401 | 2026-09-23 00:58:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e21eaf6-35f3-3fcf-b170-1bc927987ec3 | -6.7333 | -55.089401 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 375d3caa-b969-3bdc-99b3-95f45305e5a1 | -8.456 | -48.702599 | 2026-09-23 00:58:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d5a9f4af-1497-3276-9ddd-778c0e259279 | -8.2744 | -54.754101 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 780e43e2-fca8-372f-9c46-3859fb47b58e | -5.9764 | -57.771999 | 2026-09-23 00:58:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6827c2c2-a802-382f-bee9-897bed05cf1c | -10.9106 | -53.930801 | 2026-09-23 00:58:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 352dc034-acaf-3ee3-ad97-114df945e089 | -4.4423 | -55.0737 | 2026-09-23 00:58:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b891a46-6202-3542-a3fd-7d5d58984a47 | -12.7709 | -50.8652 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b0c642b-51f5-3673-a6f0-34da07de59ab | -12.7432 | -50.879398 | 2026-09-23 00:58:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2270e99b-6795-3819-a211-b80949820ec7 | -3.4637 | -59.5247 | 2026-09-23 00:58:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3c43c56-e301-34e4-abd0-83f73059a72b | -13.8513 | -48.567501 | 2026-09-23 00:58:00 | METOP-C | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e176a486-4b5f-38ff-85e4-baf45d00ef50 | -8.4474 | -55.021 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9bf93ad-821a-3630-8b56-82dbd6418027 | -3.4485 | -50.6012 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9ba155d-b9fc-3b4f-9344-cb144c42476f | -3.2169 | -46.930599 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f7e07c-b144-38ff-94a7-c4be13142501 | -4.0445 | -56.314301 | 2026-09-23 00:58:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2981dcd2-abea-3def-aaae-8b5c20b89370 | 1.5685 | -55.845501 | 2026-09-23 00:58:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd868140-6092-37e9-a5fa-b0b17f06ec73 | -11.6752 | -50.9491 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d577b1b-a465-360c-b26b-1a4a7a7148f3 | -5.7499 | -51.927399 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e9cfeb-beca-3d91-b788-ac276c04c634 | -8.5932 | -54.615101 | 2026-09-23 00:58:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f09aea2-4b59-39ea-a0bc-5e89e0bba7dc | -3.2266 | -46.928398 | 2026-09-23 00:58:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd7a089-fbf0-3222-a7f3-da4fc760bc93 | -2.7403 | -51.542198 | 2026-09-23 00:58:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5667715-5692-32b9-8928-e269b0d1ad4b | -6.605 | -43.763901 | 2026-09-23 00:58:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 14fa0c67-17a5-37b2-8b8f-3179b5f0b50f | -6.4572 | -59.958801 | 2026-09-23 00:58:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af29e668-d2b8-3760-861e-29556aee70f4 | -5.8085 | -52.090698 | 2026-09-23 00:58:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd144cc-79a0-34d8-bd1c-e50586a3e3b1 | -5.7825 | -47.164001 | 2026-09-23 00:58:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55380a66-0ad3-3c7d-8a62-8b9dfaa46c4e | -8.3558 | -50.842499 | 2026-09-23 00:58:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README25.md)
