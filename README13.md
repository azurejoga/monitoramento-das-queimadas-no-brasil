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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14c232b9-7f39-3ecf-a657-20f949f809aa | -4.59195 | -44.31736 | 2025-11-15 03:34:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4d2e33ff-8540-3c82-8dec-9379859933e2 | -4.39926 | -44.07983 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec9b63ef-8aed-31aa-b389-0a0cb75b5a31 | -5.04081 | -43.60988 | 2025-11-15 03:34:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 91f094d1-ce0f-369a-88d4-5cfd55d207d9 | -4.42229 | -43.35307 | 2025-11-15 03:34:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 510b446c-5b2e-3799-91d0-022e9929d1db | -3.99858 | -44.17398 | 2025-11-15 03:34:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85846801-5db7-363d-870d-2b3044e9effc | -7.76559 | -45.16014 | 2025-11-15 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c40a7305-c739-3664-a14a-0e880e128037 | -7.5382 | -45.8598 | 2025-11-15 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a3a052b-8e9f-33e0-8197-335501d8e793 | -10.7018 | -44.49173 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91cf2d4f-0385-3cfd-99f4-7dded965fbd6 | -6.38863 | -40.18296 | 2025-11-15 03:36:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ab7efa7b-b3fa-33ff-8455-ad94fbeaed40 | -10.62774 | -44.58456 | 2025-11-15 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5a88b71-7b25-38bd-8cc8-e7ed862efd16 | -5.2352 | -44.35577 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| ec31b85c-9ad0-3a89-880f-7b7ea710f20c | -7.45681 | -42.56537 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8136ce75-e82b-38f1-b73f-3bde6cf2decc | -10.69185 | -44.51319 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 61168171-fbb8-3236-b111-7386516d3b08 | -7.69685 | -47.19086 | 2025-11-15 03:36:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88e8667b-2cad-3f20-9d75-9ef6dd384c34 | -5.42606 | -43.2603 | 2025-11-15 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f508980-f081-379e-89bb-3f99ccc7ea61 | -10.69815 | -44.51051 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4526b10a-1671-3226-9232-71a3adc2c2b6 | -6.6519 | -43.51358 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5584666-cb5f-321e-bbdf-6b140c1c1ba3 | -8.86092 | -40.38704 | 2025-11-15 03:36:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d5595d47-462c-302a-913e-964077431457 | -6.73439 | -42.95773 | 2025-11-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 87851673-7d67-388d-b412-39000434b9b6 | -10.10744 | -40.89437 | 2025-11-15 03:36:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d5b2c434-d1e7-39b6-b231-c9165b8b10bc | -7.10959 | -39.07792 | 2025-11-15 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c46c28f0-5aaa-3dd3-a169-b2d416a2f113 | -9.8514 | -44.1754 | 2025-11-15 03:36:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ce2d7a5-8179-364f-ba9b-7f47a7261661 | -9.00324 | -44.18148 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f7efc3de-c1f2-3b66-87b2-623b1e4aa70f | -9.44497 | -44.8692 | 2025-11-15 03:36:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d65d7b1c-ef2e-3ebf-9330-573d1ab6d784 | -8.32072 | -45.40579 | 2025-11-15 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe097162-79ce-3b6f-bec4-bb15fc26603a | -6.37461 | -39.30513 | 2025-11-15 03:36:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f01f5044-0fb6-33ae-bdc8-08c18112818a | -10.11111 | -40.89947 | 2025-11-15 03:36:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 80a7266a-a8cb-3979-b1d8-e819de196089 | -10.42533 | -44.95374 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fae8cf3-0076-3a99-a5a3-3528f9155b10 | -10.70295 | -44.51554 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d6d82d8-67ca-3284-a9f9-3d70a8c81372 | -10.70108 | -44.4954 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d50c7667-6448-37be-b656-28334d8b42f2 | -9.8576 | -44.17287 | 2025-11-15 03:36:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f02a870-3947-3d86-9d05-df1fa1251bd9 | -5.63057 | -43.92537 | 2025-11-15 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 928d9b5c-88bd-3151-80a1-eb9b206d47a2 | -7.42401 | -45.22922 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d90aa82f-43d4-360c-aa7f-f84c571759d5 | -7.42312 | -45.23417 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5bcd000-6c8e-3d49-b26e-20be8853b63e | -9.66371 | -43.90018 | 2025-11-15 03:36:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 30df13b7-6c2c-3f5c-9a2b-6ee4a252f67f | -9.7527 | -43.97345 | 2025-11-15 03:36:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61730648-0b85-317e-9ab2-7c4797c14742 | -9.01386 | -44.17458 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ecb5b37-1d84-3e03-97cf-839fcbc776a4 | -5.63142 | -43.925 | 2025-11-15 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57fcf07b-d21a-350f-bb76-cca001889ead | -11.47548 | -41.98929 | 2025-11-15 03:36:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 82f019bf-e2df-3be2-a8a7-f2e69673d1ba | -7.76385 | -45.16771 | 2025-11-15 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 701213ad-7abd-340f-8c02-f398dadceb95 | -7.10416 | -39.08481 | 2025-11-15 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 49b9e506-7836-3bb2-8713-5547c228363f | -6.01625 | -41.96342 | 2025-11-15 03:36:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 065fa99a-5e87-3b5e-b6e0-134a86dff5b4 | -5.3297 | -43.03841 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ba69f86-e5a8-31d4-8d1c-33aefc60aad5 | -5.62982 | -43.92955 | 2025-11-15 03:36:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80bdb441-cc27-31cc-bea3-69be6474bf08 | -9.01031 | -44.17461 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1712b15-f6ba-30f7-b9dd-1dbe09cbef41 | -6.2834 | -41.75978 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 61312a7f-4d5f-3b42-8147-e3d1e95d1f3b | -9.14104 | -47.76102 | 2025-11-15 03:36:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2bef2ec-e09a-36d1-a06e-829849169cf4 | -7.25882 | -40.17463 | 2025-11-15 03:36:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3aafd4da-dd5d-3b80-a095-25be047d709b | -5.32897 | -43.03811 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b70b5d30-04de-30a1-a4cb-35e5909c7394 | -6.73255 | -42.96825 | 2025-11-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce2a7ebf-b59f-38ce-9dde-83d59e8c7447 | -6.30179 | -41.82875 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5c8ab9b1-afa7-34c2-b74c-9893b20189b7 | -9.96535 | -44.94221 | 2025-11-15 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f99b1625-a63d-3898-ad6c-d029364cca0b | -7.33298 | -40.37228 | 2025-11-15 03:36:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0fec956b-0a94-38e5-9286-2d2902949e5b | -5.16646 | -44.85443 | 2025-11-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2b93efc-d53d-3afd-a7a4-cf1227a4f974 | -5.66051 | -41.08813 | 2025-11-15 03:36:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e4fa0831-db20-3770-8b4f-7190ef5d5165 | -5.22917 | -44.35459 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 5d92df87-4667-3a1d-85e0-99a8d01727f2 | -10.62697 | -44.58863 | 2025-11-15 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 095a7847-942a-3ed0-9eda-36dcf3e21127 | -9.5224 | -47.27119 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6072b4ce-a4a8-312f-8ad3-d441da9937f8 | -6.481 | -43.95316 | 2025-11-15 03:36:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef6ebd8b-b283-3681-bb44-f6cbb920d123 | -9.49316 | -47.27808 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4942fef3-bd71-3bd1-bd0f-fdd0c754ed94 | -9.52486 | -47.27227 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 917465d0-ed4c-3675-9d38-8ef0c228ce0e | -8.33188 | -45.41402 | 2025-11-15 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 742ec3a2-60af-345b-9278-6a8d95ff2544 | -10.10298 | -47.52048 | 2025-11-15 03:36:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f11ee581-c582-3b92-b91d-32229152dba4 | -7.29246 | -45.11724 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 879cf1ab-50a1-3131-a61a-57c12bd72772 | -7.29421 | -45.10769 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5c2d4c67-4692-3266-8930-f8d91bbe35e9 | -5.85116 | -44.38883 | 2025-11-15 03:36:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e01cfa58-0ca6-3efb-ab32-b4805723189a | -5.23054 | -44.35524 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a6fc035d-ac8e-3841-ab5a-4017db1af9f6 | -10.7037 | -44.5117 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef0f3bc3-e4a8-3d34-86fd-1b0a05e3aa7d | -8.10761 | -40.88079 | 2025-11-15 03:36:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8018af63-0436-3e0a-9d69-3f8a7f3d4af1 | -5.16732 | -44.84962 | 2025-11-15 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e438a939-47f2-3e17-a479-04ec82f2cd85 | -9.85692 | -44.17653 | 2025-11-15 03:36:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52a64f60-eb60-3e64-8e05-6d99054ee80b | -8.74827 | -44.23454 | 2025-11-15 03:36:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4bcd4160-2740-39b9-a043-6b4ad8d05be9 | -9.48881 | -47.27784 | 2025-11-15 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3fc2406-3713-3be7-8824-0f28b63884c5 | -6.29809 | -41.82502 | 2025-11-15 03:36:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 486adf1e-6e91-3a3b-80c6-46511b8149d3 | -9.80857 | -42.20966 | 2025-11-15 03:36:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ba9ebfb2-3539-3ae0-93fd-bc229b2a1abf | -5.05264 | -44.68245 | 2025-11-15 03:36:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 740e0a5b-7e8f-3aff-bd87-57a5505a4f9c | -5.23823 | -44.34713 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 3b319ad9-51ca-3ee0-bc90-6ac544872ea9 | -5.5426 | -42.69654 | 2025-11-15 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d603ac1-ab97-3ca5-b260-99a4c718db5a | -7.22449 | -39.95491 | 2025-11-15 03:36:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73b7494c-306a-3d59-9ae6-db23c92ae9e3 | -6.93127 | -39.60795 | 2025-11-15 03:36:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1fb709e2-5811-3467-9887-5e1997ecc82d | -7.38775 | -43.31339 | 2025-11-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7c4b23b-6ef1-32a0-a766-49ce3e7ca413 | -7.53686 | -41.17368 | 2025-11-15 03:36:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| a77dfadf-8f97-365d-9ae8-51bc7d316035 | -5.3888 | -44.84663 | 2025-11-15 03:36:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fff02f6-64a4-3512-9085-51a23912fd90 | -7.35397 | -43.344 | 2025-11-15 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50fe3f0f-b978-3117-b701-1bd64d07c816 | -7.462 | -42.56633 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3675a91-5832-35e1-ae8a-502f8891f2d7 | -10.45031 | -45.07341 | 2025-11-15 03:36:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61522804-d308-310a-b91c-f63ae6ad6afd | -7.40185 | -41.00895 | 2025-11-15 03:36:00 | NOAA-21 | BELÉM DO PIAUÍ | PIAUÍ | Brasil | 2201572 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e6db394e-51a8-3512-8d97-42b1eef7f7f3 | -5.23679 | -44.3465 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| d7251fbb-6bed-3341-8f1c-4776260c585a | -9.01948 | -44.17558 | 2025-11-15 03:36:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7287482a-a0c9-3486-a4cd-c9acd14f6ebd | -5.33525 | -43.03936 | 2025-11-15 03:36:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3e358c07-7e50-3a19-a1f8-37b68318392c | -8.32776 | -45.40208 | 2025-11-15 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 235c12cb-f1cf-30be-8762-2187a1d9c657 | -5.23218 | -44.34609 | 2025-11-15 03:36:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4760e10b-d7ab-3a33-9a13-26b189168dac | -7.45736 | -42.56226 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6a2723c7-2c6f-374e-93f7-54b25f02d27e | -7.42868 | -45.23303 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| beac60a7-272e-3853-91dd-9427a875107f | -8.10816 | -40.87724 | 2025-11-15 03:36:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c2268385-e4ab-311b-989c-342907a33e16 | -10.69962 | -44.50292 | 2025-11-15 03:36:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54fad444-a506-3559-99e1-3b047dc48aeb | -7.4296 | -45.22813 | 2025-11-15 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a007999-6848-350f-9dbd-72d5db8a55cc | -6.73194 | -42.97177 | 2025-11-15 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c6d5dcd-3e57-365b-9cd4-9d951092fa4e | -5.52392 | -41.77398 | 2025-11-15 03:36:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fcaf7a79-94fb-38a7-a613-1f362d8fa600 | -7.65252 | -41.30045 | 2025-11-15 03:36:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README14.md)
