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
| 72246756-775a-3f96-a0b4-96d0149b15a9 | -6.14273 | -43.82228 | 2025-07-27 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fe28206-d53c-313e-bace-f589c75cd5d7 | -6.05448 | -42.92839 | 2025-07-27 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0205de7d-a2df-33dd-89e3-805ee6b41644 | -3.74505 | -49.04899 | 2025-07-27 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 491680f7-14b7-35c4-a489-ca7575e94c57 | -5.9678 | -44.15966 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e449ee8a-0c86-3a14-89e4-fe7aea168702 | -4.95788 | -43.7286 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 08587615-d521-378f-8140-2c06c55d5473 | -3.40357 | -47.50528 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1706f04e-fc6c-3a93-902a-af6cd25b5a2a | -3.39613 | -47.49487 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6de1d0d-71af-3ab1-82db-fae795d19e53 | -5.78222 | -43.60304 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 33612dd3-30b2-34df-8741-a5d8fa527a68 | -6.99956 | -42.34596 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b4a1c8ae-e0e9-3a9d-bcfc-aeb4e7b9474d | -6.86348 | -43.68486 | 2025-07-27 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8aa560c4-94f8-3dbe-9211-33609ac36a21 | -3.39912 | -47.5045 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22288fdf-da1c-36ee-affb-8b4aed142918 | -6.34005 | -41.8112 | 2025-07-27 04:06:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9f79ca3c-58d2-3920-b523-8f05d2dee1c8 | -2.74252 | -48.67946 | 2025-07-27 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6efa3e0-84a3-34c7-980f-cc78b16b81a3 | -6.13989 | -43.81793 | 2025-07-27 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d21489c5-61a7-3631-84f6-b863f926b0fd | -6.55589 | -41.49907 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5e39a652-4aa7-3c20-8a24-735b475162b0 | -6.22712 | -44.527 | 2025-07-27 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b5a58d4-ecb6-31bc-8324-7fc0e2c32437 | -2.95353 | -40.12251 | 2025-07-27 04:06:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f23c1a6-eecd-364e-be67-eead07198eb1 | -4.13736 | -47.64931 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77db4042-4a3c-37d3-80d4-dac1a98e863a | -3.56976 | -49.50234 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7de1ebeb-52e8-3212-ac77-e14f9981c37f | -6.55049 | -46.96043 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9979b5b-da17-34fd-b21a-3d6db7c5d078 | -3.11557 | -48.96288 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5cb72118-e8b5-3c8c-849a-d9d0d64bdde6 | -5.78725 | -40.94201 | 2025-07-27 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 05aeef82-ba33-3968-aac2-a364193eb3c3 | -6.41797 | -41.14391 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28fb370f-a8bd-31f3-a206-e9db5447357d | -6.2422 | -44.05358 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4576b8d-28ba-3ff0-a20c-9e3132e8a732 | -6.55534 | -41.50252 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c5357180-4c48-3771-ab38-e9545413011c | -6.89094 | -44.80889 | 2025-07-27 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c82b30e-a6ed-3438-952f-5d117917bb68 | -6.02046 | -44.03563 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97114ca6-5e30-3fc6-851d-74d61c3d38f6 | -4.49612 | -42.93876 | 2025-07-27 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b1a49f-8b77-3e63-a158-792b6b1e3474 | -3.13301 | -47.01218 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f438012f-3f3b-3f24-8dbe-180594ccef0e | -3.12868 | -47.01148 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cbdabff-3efb-3723-965e-d8f755be3ce7 | -5.68111 | -43.66492 | 2025-07-27 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60723ba3-b9b1-320c-8c74-093eb5a4fc2a | -5.1843 | -44.9581 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 28902561-c062-3ea5-91c5-d185188dee40 | -7.00011 | -42.34249 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84e526a0-0da7-397d-8d69-b35af501770e | -3.56026 | -47.37567 | 2025-07-27 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 901dbcc7-6fb8-3864-97fd-9a5ac12e03f3 | -4.4967 | -42.9351 | 2025-07-27 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f9d27f2-6668-3cb3-b5ed-955bae3aa50d | -5.48144 | -41.78437 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c3c748f-214d-3082-b3d1-744d3f510ac6 | -6.66994 | -43.96721 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f8c2f1-a858-385c-b2e4-8b11d6ab8490 | -6.63411 | -43.03883 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 129b9993-d1b2-3e70-911d-f1397133daca | -4.0568 | -42.53271 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d38f2a45-71ef-324c-acbb-3becb4de36ae | -4.10379 | -47.93521 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51766440-7b11-39c4-9a01-2e3944a51ebf | -6.88738 | -44.80819 | 2025-07-27 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 837fc226-59a8-3fe8-9933-10bc481d3218 | -6.63747 | -43.03937 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6a9fcba-0033-3f49-98fa-5917d8444206 | -6.55204 | -41.502 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e28c9578-e4f4-3402-832b-7a32b4ebebc9 | -4.09789 | -48.20039 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be00d6c6-e65b-3774-bba2-dff8d642e23d | -7.12991 | -44.29688 | 2025-07-27 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9ff1fe0-811a-3a26-b56f-d434787834e8 | -4.0669 | -42.5343 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 141e53e0-38f3-385c-acfe-daf1a3e7b8ac | -5.68267 | -42.4009 | 2025-07-27 04:06:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| df96438f-88ee-3b39-979a-ad97da1a0f46 | -4.5837 | -44.6383 | 2025-07-27 04:06:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 630d2e6d-cf44-3669-9002-35815260f2ba | -6.89197 | -43.10968 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a0bc344-4e5b-3cf4-a5b1-6924295a7f2f | -5.65362 | -42.58397 | 2025-07-27 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 26ade3a6-e212-3313-b55f-30b839ad86cc | -3.11726 | -48.95938 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d7c47ce-622c-3d93-8ebf-ad28243400fe | -6.55978 | -41.51736 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c347089a-a7ea-3293-a5b5-6e79691f5695 | -6.42074 | -41.14789 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b0aa974a-69c5-3745-a632-c361de853ae4 | -6.56417 | -41.51098 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e76c4a20-a0a0-3e02-88f1-6dd1248b1a37 | -2.90291 | -48.24976 | 2025-07-27 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9fa9f19-6610-37d9-b693-2adc5b06ddb0 | -6.05857 | -42.93654 | 2025-07-27 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2cb4b7d4-de8f-3c5f-a247-acbf5b42d6f0 | -3.42118 | -49.47778 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec4ee9d6-67ba-3cb4-957c-52d1b71c0356 | -6.54819 | -41.50493 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 738ea177-e0b7-30d7-9014-756f27bbfbe6 | -6.99424 | -43.33249 | 2025-07-27 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d19123b1-3ac0-39f4-9ea8-5ab6f938789f | -6.64025 | -43.0435 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df713cff-176e-34a7-9d73-0ff3c269cf4d | -3.12435 | -47.01078 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 194ba840-2939-386d-9e37-0d60939503bf | -6.56032 | -41.51391 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a1716517-a2e7-3b18-8753-8b8e1df5a24c | -7.00619 | -42.34702 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6e7eb38-860a-3c01-9502-75e89aedad1a | -6.41743 | -41.14737 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c5a47ec2-14bb-3043-b614-07199075b281 | -6.64083 | -43.03991 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c8d1e13-b5d8-307d-90eb-09cdb1424ebc | -3.06717 | -49.50425 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ede3576-0ecf-3f5d-8c32-ecc75c604acc | -6.89676 | -43.11361 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5c250a5-bd4a-3f71-bc26-e2e4ee836aaa | -4.03606 | -42.52231 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9deb842d-0f6f-3ef7-9755-d68a5e7ba1a6 | -7.28345 | -43.08014 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1762792a-e38c-3649-aa87-5bfcad5b8003 | -3.3648 | -49.16755 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b07a15cc-072c-304e-8bd7-16cde67473ea | -3.39094 | -47.49857 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b31a7fc1-c4d6-3bb3-bb9f-efd93ceca61c | -4.04615 | -42.5239 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a03b54de-8c22-3fe5-b3ad-e8ccd92cd099 | -7.18143 | -43.95411 | 2025-07-27 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95fdbc4c-b08f-3354-a2b3-975a84960828 | -7.00233 | -42.34997 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3408b477-a756-32d7-b867-dcc4fe4826d1 | -7.42786 | -44.71615 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4be01c9b-11e9-3230-bc96-b3f863144d01 | -13.09338 | -47.32952 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10b50821-03d2-3c13-a85f-1fa1aa5cc371 | -13.71691 | -45.67646 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dd09a79-1789-3c98-ac88-0a71da496e80 | -11.30117 | -55.12372 | 2025-07-27 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b62f7e6f-b865-3106-a045-ba3abf5ed7f6 | -7.74745 | -51.12903 | 2025-07-27 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dd3a20e-84b1-3ab4-b1e9-85d5d2db2a16 | -7.74813 | -51.12526 | 2025-07-27 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2048533a-df7a-36cc-b03a-7b73cae76437 | -7.2241 | -45.38065 | 2025-07-27 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64bf1487-6e07-39fe-aaf9-acbe54a80890 | -9.1305 | -45.86732 | 2025-07-27 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04d634ca-98eb-3a76-bd4b-de4cdee38ee1 | -11.59631 | -43.20589 | 2025-07-27 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed10db4e-0578-3f68-b75b-2d28e39b6259 | -13.09986 | -47.35966 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 819030c0-e82e-3293-88b1-fc19eda385c5 | -10.84985 | -46.68248 | 2025-07-27 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2aaa68b9-a53d-3314-a23a-9d3668526da6 | -12.68288 | -46.98648 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c12a3a6c-c5ec-3411-ba85-7ea8c96656d6 | -14.21706 | -43.9467 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95203bf9-0b49-3546-83dd-f894c44906c6 | -9.03283 | -45.39817 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 476038e1-5251-3c0c-95ec-f6b9ef2bb634 | -8.17143 | -43.20374 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 80883e90-150e-3a00-98ef-c24ed9beb16b | -13.08956 | -47.32907 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a772e374-0357-3fc3-add2-04241a1df2df | -8.00839 | -48.17245 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4ea86b3-83e3-3786-bfcf-bc0a323a80ff | -7.75208 | -51.13374 | 2025-07-27 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| decba871-beaa-308b-8851-2e1bda8678b5 | -13.53433 | -45.52981 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e40fb82-a89c-3890-89f4-ed3eb6e67a4b | -13.7154 | -45.66413 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72f66e20-1016-3992-9935-492f5142edd9 | -7.964 | -46.0425 | 2025-07-27 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b727792-1d36-31af-89a7-987bac1095cf | -13.14027 | -47.32916 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c4b0bf1-f6ee-31e3-9200-538e1f073be4 | -11.29474 | -55.12252 | 2025-07-27 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb811fb0-9f2b-3b10-ae62-2757599d93cf | -7.5084 | -44.4234 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 361bae8f-6617-3dcc-8515-5965809c8a79 | -13.13573 | -47.33284 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1715c8bb-c3de-3832-a7b9-0c7ec6e953c6 | -8.30432 | -45.01009 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README10.md)
