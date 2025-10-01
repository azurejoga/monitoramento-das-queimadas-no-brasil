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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2fd5cd2-12a2-383f-865a-4b29c0d233a1 | -7.48085 | -46.47181 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a1770be3-c816-3b13-bf52-e841040dd3bb | -8.75501 | -45.92849 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 928856a8-0f9b-3f21-949c-7661a470f83f | -5.52167 | -42.71869 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 72ccfaca-5ce5-30a3-8815-5477c306e26c | -7.62857 | -45.45195 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 798f953d-6196-3211-b9ea-4f7c0137463e | -5.32328 | -42.7747 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 220f98aa-ffc1-3b45-990f-d29b16129098 | -8.58314 | -44.74533 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cf3cb482-0011-37d6-a947-05bd754f2aec | -7.47906 | -47.27674 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0741b46b-9ac6-3948-beba-1d9dafa3d517 | -5.64704 | -43.91396 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c18a04d9-9e53-38bd-9cf5-60bdc01d6f7b | -7.16321 | -50.54242 | 2025-10-01 04:19:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d44f10c0-d790-3f4c-a4a9-f85737cbfa84 | -8.22212 | -45.78947 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4317526e-e3ed-318f-9c7f-b5b20c7778f4 | -4.96258 | -42.03654 | 2025-10-01 04:19:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f80edac5-e816-3a98-876e-cca06827c325 | -6.87817 | -44.52939 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bca2d68e-41b6-385d-b831-9b93827399b7 | -5.68246 | -42.62959 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a79b6659-9d93-3cb0-a01d-589a32a8fe6b | -9.92478 | -43.68224 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29ff681f-e95a-3a4b-8280-a37c4682545c | -5.65035 | -43.91446 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80eb711a-bc90-39ac-9499-92dab5d9eecd | -5.69842 | -42.61679 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 08a707d8-828c-36fb-8b7f-a5cb0ae44752 | -5.90634 | -43.93001 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aa0c260-c08f-33b5-9dc8-ab98294791b8 | -6.09176 | -42.66051 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb48192d-fbd6-3f19-b498-f41e45ff04b7 | -7.12724 | -45.54588 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69ede0d-56f4-3c1f-aa7e-663b1ca30ebe | -3.86053 | -40.43494 | 2025-10-01 04:19:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 06f99826-5226-37fc-a9cf-a0767e6cfa1b | -5.71065 | -42.83755 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d31505f8-f82c-3c0a-8c6a-fd683cb5ae54 | -6.30755 | -43.4707 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ddbb83d-f969-320d-84c2-9dbd02431dcf | -3.51986 | -49.44581 | 2025-10-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2a20d375-cf00-3e84-93fa-c9f47cc26cc1 | -8.55732 | -44.75912 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcbfdd5b-04f5-392c-b1b6-4c6861ef6026 | -5.07081 | -42.63979 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 18c3fb17-80a5-30f1-a9eb-bc7b51b3c79d | -9.92869 | -43.65613 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1f47669-2003-32be-ae98-6be3b933b106 | -5.70232 | -42.66311 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 51abc23f-54a9-3919-97c3-73069f20aea0 | -3.75316 | -41.03393 | 2025-10-01 04:19:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff913aa7-de06-36cb-8d4b-d67d13cfaa6d | -5.22114 | -44.83122 | 2025-10-01 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 480f3dd4-be88-3a87-8bf9-d59b79708651 | -4.12262 | -43.32358 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f21aa47b-5f39-3ddc-9e9c-19c8748d97e4 | -3.35293 | -43.19718 | 2025-10-01 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72123cb4-919a-3670-bb21-fe50ec01148f | -6.03816 | -51.89583 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7756a45-d3af-3942-8e38-a4f65c627a9a | -5.83008 | -43.93874 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c752412b-61ff-3c8c-9b4c-44410146d3b0 | -7.45487 | -47.2729 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2cac8c8b-ffc4-3892-8720-9dbc499171ce | -7.053 | -43.23806 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 967a4253-4890-32f1-b1a5-69a86e94a08b | -3.10158 | -47.01195 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16a24d14-db0c-337a-8619-1ce27ab70327 | -5.99358 | -43.4334 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10e62a89-9b64-357d-9398-6dd1bb83b338 | -8.97451 | -50.2683 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b96551b8-5cc3-3d8d-9ccf-9c28943da04a | -3.36245 | -43.37622 | 2025-10-01 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c519e2e9-da0f-3b54-8743-2d704024cdf9 | -3.87827 | -42.52279 | 2025-10-01 04:19:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 250f598d-92c0-3411-bf9f-be4a67430676 | -9.2595 | -45.68475 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5ae6411-2127-3633-b321-57584d2b9a32 | -5.94456 | -45.85687 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92e20be-1d06-326d-8278-02095dc56bcb | -6.18584 | -43.90577 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23a5ba2e-4539-3556-a3a8-6c51212b6e88 | -3.4965 | -52.46254 | 2025-10-01 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b25406f-3a67-3463-9755-b3221a0f6766 | -6.36329 | -44.57832 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43ed68b8-f993-367e-a0f3-8284227ad5d3 | -3.05116 | -51.10095 | 2025-10-01 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 376513f8-191b-3721-9d1a-f5de4a3da15e | -2.55188 | -48.40276 | 2025-10-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be119c05-eee6-3926-8ac7-5bf25ba88f95 | -9.31781 | -45.72669 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a07eaa85-f01f-32aa-bae5-2c7fc2b22d2a | -6.00283 | -43.79126 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9975a9b5-004f-38e6-a6b6-aef4fb1a2b34 | -8.57793 | -44.66971 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee848c17-efdd-36df-b311-2ccdb3ea8653 | -9.45001 | -47.92167 | 2025-10-01 04:19:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8efa0af-32cf-3755-bffb-f4baf31385cf | -8.58152 | -44.75575 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb22e552-826b-3846-969a-4095ea9d329a | -7.49161 | -45.43689 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21b7f6b2-a52b-31df-8dd4-95495287d499 | -9.89353 | -45.94099 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36e27ad9-857b-3de4-b7ce-98afe8ea5ceb | -9.93607 | -43.65345 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ae862a4-2197-35df-b515-ef6c96f4ca0d | -7.12779 | -45.54241 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00ee5dbc-dd10-3e83-adae-d8dced4e15db | -5.91344 | -43.90613 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5dbcf5c-2d73-3af2-9ad4-8168063aa452 | -5.50868 | -42.75816 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2f11670-bac8-3dd2-9eff-b98671839e00 | -7.82049 | -45.11732 | 2025-10-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a7faa61-602a-305e-b380-d7c3cefc7013 | -5.50924 | -42.75451 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d4aab9b6-93d2-34f0-9909-226dc4311c73 | -5.8332 | -43.87518 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9c5e56d-6ade-3f4f-bcb6-5ba31bb840e3 | -5.39181 | -43.5851 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e83365f1-df7b-3d61-b90e-b697d9455bac | -6.05539 | -43.6054 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52a5595e-ff66-39d0-b8c2-3e042aa50a42 | -8.94932 | -50.34303 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e63ffd7-2467-36db-a957-a0f02bbd43b1 | -6.08092 | -42.6627 | 2025-10-01 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4716c253-3626-36fe-b257-5fda016e4cee | -5.71469 | -42.87928 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 42ac4663-2b09-396f-a77c-03e8f0c44b83 | -8.64313 | -43.98309 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfc1618e-1bc9-3383-b925-8a37cf7ec6f5 | -6.07124 | -42.68029 | 2025-10-01 04:19:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f24316ea-fe2b-3f7b-9944-8a1909429f61 | -5.7067 | -42.84068 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a3d973a9-916e-377f-90b6-cdac22943101 | -9.94176 | -43.66197 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69a8e95e-85be-3b8e-80c2-39163d4d7c6b | -5.90362 | -43.4444 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1da9adf-0b47-379c-930f-b5abd6aeaad1 | -6.14089 | -44.73743 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 246dea63-fa12-3346-ae6b-dbbb3135621f | -7.47306 | -46.45578 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825292ce-b4df-308f-9725-d1c34ae604fe | -5.41033 | -41.326 | 2025-10-01 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2bcc88f6-d7e3-3988-9cb0-807935906d9f | -9.9259 | -43.67479 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77201a48-61ef-3064-b509-ea50f17e3551 | -7.76637 | -45.76587 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 080d8985-35a4-36da-8991-81f9331590ea | -5.83278 | -43.9214 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80234e2b-e37c-325e-a013-be97bf9ead8b | -3.46728 | -50.09468 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0118a868-e0bf-39be-8e66-4a28a68701d0 | -6.36508 | -43.95491 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e3367a13-6e3d-3401-8a48-765967e92631 | -5.72542 | -42.87714 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ae040e4e-ed6c-3be9-a2ba-f3079096f5e3 | -5.64327 | -43.93826 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a38a60a-a878-3eb9-8353-5594455751b3 | -5.88334 | -43.68335 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6bdf60c-e8b8-3d53-a94c-27e1f81a327d | -5.82695 | -42.78761 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7b9616ae-9d06-328e-a290-f32e2d3c3e00 | -5.64534 | -43.90302 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 655f0806-2d0a-37a8-ad59-800912a78139 | -2.27118 | -47.85206 | 2025-10-01 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 038c3de2-3f96-3603-9510-5ae0ef62fbb0 | -8.54771 | -44.64348 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8683fb8c-0a4b-3212-b1f8-3f08d31bb74b | -5.90696 | -43.44492 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d6dfc6b-8bc4-32bc-a716-b5eb870b06c7 | -8.55171 | -44.72976 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b701d73-1be8-3ccb-824a-19a7d56b9d5f | -5.49678 | -42.74503 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 301c936f-afcb-3eac-b06f-2239aef6b668 | -9.94105 | -43.59684 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1254fd9-b682-3ae5-96ae-f9bb21ba6a01 | -5.89269 | -45.88153 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b954597-437e-37b9-bebd-23dafe87f9cb | -5.76439 | -42.91674 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3e854e3a-cc54-35e0-9d03-7e88e9a33708 | -5.35952 | -42.81783 | 2025-10-01 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a460b9ef-f019-3d92-b492-2b76b91e2af5 | -3.92074 | -42.26706 | 2025-10-01 04:19:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06178d78-1aa9-314a-af43-fde5ce540775 | -7.20872 | -45.48047 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0207f6c-a454-3eba-a496-4c85797e3ce3 | -5.2864 | -48.12447 | 2025-10-01 04:19:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 495fdf98-bb90-3c42-801f-54edc1f5b86d | -3.60983 | -41.37532 | 2025-10-01 04:19:00 | NOAA-21 | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a02894df-3cba-3e50-89b1-669dd775de57 | -6.09572 | -42.4728 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15228fe4-51a6-3530-8a18-c6ec612d3d15 | -5.94061 | -45.90359 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b68823b-7592-3de7-94b3-b96d32862edd | -6.72062 | -44.60365 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
