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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a84fd9c-8005-3c4f-bacc-4f88c8a20435 | -5.8682 | -48.26132 | 2025-10-26 04:49:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b82554e0-4399-3269-b569-228477d4a438 | -4.89378 | -43.2481 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf729914-8884-3860-861d-d9264cc98184 | -4.7847 | -42.76872 | 2025-10-26 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| fdfbbfff-497a-37a0-b9d9-1c06474d3970 | -6.39384 | -45.7706 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a7e1a65-83cd-3b7a-9dcc-6d1b6fcbcdc4 | -5.89964 | -49.48602 | 2025-10-26 04:49:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a871ad8-f5a1-34d9-8c60-fcd6cad30423 | -3.12076 | -49.10501 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bd48df2-33b6-372e-a72c-007428492390 | -4.54797 | -46.55602 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38c717fd-2d1c-3cff-a616-4434f581d431 | -6.21999 | -42.53665 | 2025-10-26 04:49:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a72506a1-f185-3464-9eb8-21afc6bc2eda | -2.81288 | -49.14828 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5943e380-bf23-3bbe-97f8-bd5f46f4b9ce | -7.349 | -42.44485 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3f2c0396-cbf8-3d1b-a8a9-33a9a30cc304 | -3.10244 | -50.20297 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd272b2-f05b-342c-8cc2-f1ab0ab2f532 | -5.10705 | -43.1788 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9eac634e-3219-3f3e-9696-f68988d35211 | -4.8311 | -50.92887 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c54fe2f-e331-3b12-9c93-42fc4590fe74 | -4.94204 | -48.59201 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d56df26-9773-3261-9b44-ebeb88fa66b7 | -5.10527 | -43.19167 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca87c403-1b40-3530-9d6f-4ce1ca69ebd8 | -6.59953 | -42.05975 | 2025-10-26 04:49:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40eb698e-17cd-3367-8660-71b2be5379ae | -4.35927 | -50.33115 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09d01b8f-acc0-3ea1-9f4f-6e5513bd9efb | -4.70921 | -55.99022 | 2025-10-26 04:49:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e5128d5-3027-3acc-87fb-7e28ab06e7b3 | -3.68828 | -51.97061 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6618c528-63af-3f5d-b28f-30dfde45cf6d | -4.60259 | -49.58722 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d74fc28a-ddab-3b0c-89dd-bf66320abd8f | -6.26889 | -44.39327 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 517b7b4b-313f-38ac-9f9d-eeee9aaf0820 | -4.33919 | -49.89237 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05be4795-2e97-3776-be81-99b986ba8811 | -3.79386 | -52.01885 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b102719-21e6-3f62-accc-795f9836091c | -2.79499 | -48.89153 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf9672d0-f2cf-365d-8202-652cf2893c0c | -3.39274 | -52.44506 | 2025-10-26 04:49:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1742da9-c8d2-3ba0-addf-ca42fd58735b | -5.65653 | -48.46277 | 2025-10-26 04:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd6f04d0-9ae1-3135-9084-e73bc68e84c0 | -5.70718 | -49.27492 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65c21b3d-0c91-39c0-a0d9-c6ddb06a87d6 | -3.31174 | -50.11314 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7dd05486-58c3-3b18-9416-c53f90a045a0 | -5.54669 | -46.35024 | 2025-10-26 04:49:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c82faedd-98ea-353d-b8a0-8babe630eaff | -4.91584 | -48.56576 | 2025-10-26 04:49:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd46fd65-eb30-3873-b79b-a3b317a72dec | -4.60552 | -50.80322 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eec2666f-2745-36ce-96ad-7faf2f95e681 | -6.84306 | -44.00877 | 2025-10-26 04:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b85613c-1d60-3b73-8ea7-39d36c7fee5b | -3.75948 | -47.57035 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5fb30ee-a800-35c7-972b-fe1ad9bb291c | -3.83472 | -51.40609 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb48066c-e165-358a-934e-93598f0d9d2c | -4.78372 | -42.77566 | 2025-10-26 04:49:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d882dde2-c1d3-3adf-9b7a-4fa367c282d3 | -4.44305 | -49.69848 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb4c7087-9466-3a14-9b79-49fab23e0d9d | -4.89949 | -43.24562 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47a8c0e7-5c59-3f64-baf0-351baa6b95b3 | -4.26996 | -50.50637 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75f1d31f-0d04-3b87-87a4-73a9c45f7840 | -5.89205 | -49.65395 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85af41b2-c634-3e63-871e-1e178ebe09fc | -4.88853 | -43.24731 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1d6b88c-e2fc-3cb4-838b-8cbb91b02f3d | -3.78689 | -43.41041 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5643a4b2-30eb-3bfa-8bb2-aab69a48e1be | -5.70655 | -49.27903 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0abd522b-5072-3b5b-a4c1-5800d77aab6f | -4.09666 | -51.05656 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dad38aa0-220a-3276-a77a-8ef24c896115 | -6.14207 | -41.80825 | 2025-10-26 04:49:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d91287b7-699e-37e4-9ed9-8ae55844f3e9 | -6.39773 | -45.77565 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a940ae-b4e6-3e7e-9218-e9c5eef0bc8d | 1.62224 | -55.7393 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65472cf2-3a98-3100-9953-3a044cd51dcf | -6.66651 | -45.93712 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6d08a08-c022-320a-87e4-9ff2ccdc87c8 | -6.21391 | -42.53922 | 2025-10-26 04:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 309b8fbf-48a0-36b2-985b-8ea368e18f54 | -2.32099 | -48.58079 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a3304cc4-32e2-34f0-8457-68bad0971789 | -4.89276 | -43.25394 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 246ba9ac-116c-3f00-8b33-d72a31008d86 | -4.48369 | -48.67527 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 30a3051e-3507-3f16-9daf-8288f65515eb | -3.75944 | -52.25957 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78418887-e1e7-3f20-8f8e-78003038f2f5 | -4.89373 | -43.24738 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ded9818a-5391-35a2-89ec-f0303734a7d6 | -6.53271 | -43.57101 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c94717da-800e-352d-a9e2-411cc7920944 | -3.73448 | -42.2999 | 2025-10-26 04:49:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dfa4987f-8387-338e-b5b7-d46c171e0eca | -6.20782 | -42.54182 | 2025-10-26 04:49:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d449b6fe-f1a4-36da-b8dc-8c887bdcf6c4 | -4.31298 | -50.33891 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e2c7d9d-8e58-359d-8a6a-8a16eedcde31 | -6.55251 | -43.23238 | 2025-10-26 04:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e418256d-40dc-397b-97d4-cfdd163f097c | -2.91816 | -52.71579 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a3426a7-cd25-3eef-9904-c246cd293d57 | -2.47822 | -52.15963 | 2025-10-26 04:49:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9dc3b39-81d1-3292-9844-793cd3f6730c | -4.35588 | -50.33064 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d3a90cd-2795-3e0c-a001-66a3d3ce59a6 | -2.26513 | -47.85461 | 2025-10-26 04:49:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec9c9e45-7038-3aaf-a388-8389f089d583 | -4.16028 | -47.65952 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0e87d38-94ce-3fef-8b93-8d651ab87a6e | -3.5481 | -54.6934 | 2025-10-26 04:49:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a09dad-cdc9-304b-af39-d443d72fb99c | -2.90273 | -53.13617 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6a75926-ceb1-375d-af3c-c517982083b5 | -4.09774 | -51.04958 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 350bd731-e843-302f-92c9-bcb68285b1af | -3.09634 | -49.4459 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d3d0512d-9b23-3528-858d-7c53135595ab | -2.90385 | -48.98446 | 2025-10-26 04:49:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a04acfb-1853-3441-9951-94dc59ca80f5 | -7.36152 | -42.4386 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4d4ca9b2-7e76-3e3e-b649-ece307bfe4ef | 1.4317 | -50.89163 | 2025-10-26 04:49:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de446b9e-c851-3dd6-a674-73f24516349f | -3.8327 | -50.19533 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cad842c-b346-3270-92db-bffbe5012dec | -6.09434 | -47.05233 | 2025-10-26 04:49:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d044d0d1-0129-3c37-8303-ff9e01d9aa2d | -2.31805 | -48.57618 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 60ef744a-94d7-3201-ab04-2d2c427ef2bd | -4.9061 | -43.23676 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddc3ecce-75ca-35f7-a760-1c69bc82dbe9 | -3.29012 | -51.60198 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31778006-5c86-393c-92d0-c5ae62ea3991 | -3.80146 | -51.99192 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ec6f096-d4aa-30fa-9936-3ce6253af88d | -3.48254 | -49.89811 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b9bb45-36e3-3176-91a6-467cdda3218a | -3.12488 | -49.10164 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65780cc9-7318-30fc-a06e-c0cdc88fa68b | -3.78881 | -43.4112 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7441b59-bc75-3c6d-92c2-e780336d6f45 | -3.37091 | -52.80096 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76a8b782-658f-31c2-8179-6818d61970ac | -4.43835 | -49.729 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb2dbf12-18fe-34dd-85a2-cb3aa3505023 | -4.02717 | -46.06852 | 2025-10-26 04:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e928c615-acef-3418-a001-a4cb90c0a764 | -4.29306 | -48.06577 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c922b7a7-8342-39c5-b085-b7da660622f8 | -3.7622 | -52.26352 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 627e878a-2cf3-3105-a9f9-e203e3fe04d7 | -2.65905 | -54.76384 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efb5bcb2-20e0-3097-a21a-dc8f098c01d5 | -4.1557 | -47.66383 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f9881a7-a7d4-3af8-9d7a-2b49b0aad36d | -3.45727 | -49.69634 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a85acd96-da24-3117-9cf6-8b5906f99eb5 | -6.7376 | -44.14787 | 2025-10-26 04:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 427f0218-1d2f-3748-98d4-0d31c43e436e | -4.05737 | -43.08968 | 2025-10-26 04:49:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cba8abf-4664-3d58-852f-2859a7a10784 | -5.88761 | -48.59965 | 2025-10-26 04:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a5cbaf2-16ff-3a11-b9cb-e8fee57bd038 | -2.41163 | -48.21132 | 2025-10-26 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60417ad7-edcc-3a31-b7dc-8cc8114a607b | -2.94997 | -49.34533 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd187446-4641-3527-bdc2-19d3e98323cf | -6.09846 | -47.05292 | 2025-10-26 04:49:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95047c2e-5381-3395-9477-422e73bd8235 | -5.11014 | -43.19995 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9a028c0-388e-3aeb-9568-ee053ad1aa03 | -1.89128 | -54.6175 | 2025-10-26 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbf1e41b-4992-3be9-83cf-c0846754e55b | -3.73486 | -42.29983 | 2025-10-26 04:49:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42087eea-8ab7-3d5c-a99d-ff59297e8a42 | 1.53729 | -56.00224 | 2025-10-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f75ddbc8-1e14-3d7c-bac0-0fe33a806f28 | -6.71372 | -42.04737 | 2025-10-26 04:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6ef284e7-a888-35f9-b4d4-fa58368fe388 | -2.06894 | -56.86932 | 2025-10-26 04:49:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 694c714e-90bb-335c-b8d1-9f8da1952ef8 | -3.14004 | -50.1608 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README33.md)
