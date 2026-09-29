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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58b37642-4cdc-3bd4-b95e-08ce04696c58 | -7.99087 | -43.25771 | 2026-09-29 05:10:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 42b719b5-7f9f-3bef-bd89-d3aea6d6715f | -7.83917 | -45.8235 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eff3b7cc-9390-362e-adbd-fd0e9d2bde2b | -6.31835 | -52.62545 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 047b05e8-b6a9-3f7b-ac9a-789bdb197b07 | -6.76822 | -47.16311 | 2026-09-29 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af63118d-e22b-3b68-94ab-e527cedbefa9 | -8.23752 | -45.44541 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b7ca3e71-7902-31a5-a400-f51d8ebf03db | -5.73233 | -45.18077 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1feab9b2-6dba-34ac-891b-372db2f34aed | -6.32158 | -52.62749 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 68c07d4e-cf26-3ffe-8ea5-2a5d2bc60a27 | -5.97644 | -53.52903 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c77421e2-be49-3e26-a69f-82c3dee8ff68 | -2.9067 | -54.0976 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6a63ec7-27a5-30c7-9c9d-1ad97bf4942b | -6.14127 | -44.14029 | 2026-09-29 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2aa1ab-1d38-3ca1-b6c2-043d9bd86e5d | -6.68009 | -55.10962 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e13a921-8292-3d56-97f6-e8029b541859 | -5.43938 | -47.27484 | 2026-09-29 05:10:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc7acfe1-bed2-39a9-8a7e-eb85747d852d | -4.82002 | -45.63486 | 2026-09-29 05:10:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7acf3bda-0265-3194-b8fb-1f45a02580de | -7.2454 | -43.36554 | 2026-09-29 05:10:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 138bf897-b856-3b09-837f-a222dd397928 | -5.7335 | -45.17245 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e85c64d8-6b33-33ba-bd32-33d894cf262b | -6.29485 | -43.65265 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5d5eb6cb-38e5-3d49-b8cf-5d14bfc01970 | -3.70284 | -54.21429 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d6e7f25-4509-350a-9e11-eb872ebc30e3 | -3.04733 | -46.92538 | 2026-09-29 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74c38732-b451-3e03-9d50-4661bc592620 | -7.84021 | -45.81557 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 8b4b2f7c-06e6-38ed-bded-fc04f23b0a3e | -6.30402 | -56.02914 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c8510aa3-6bc4-34fc-8bc1-a5d84dad242d | -6.2902 | -43.64537 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 6d3b4405-12be-36e7-b2c4-e80a23290827 | -7.8346 | -45.81521 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 096540f9-e2db-3828-9d00-12d683f64526 | -5.87362 | -43.59428 | 2026-09-29 05:10:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e7bbaf4-ffcf-33af-9995-0cb4860173be | -6.15071 | -52.91053 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b382385a-f908-3d27-80d0-11cc07153d3a | -7.84549 | -45.82056 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4fad9c0b-bafc-331c-8163-15caa2d2e839 | -5.80544 | -57.72436 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41e2cae2-8baa-3508-932d-d422ab612fa1 | -4.29295 | -49.09006 | 2026-09-29 05:10:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba9d38cb-022f-3ef1-9328-16efcde8ff96 | -3.15171 | -54.0962 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bccdb467-74f2-3afe-9684-3b34091ac59c | -7.82754 | -45.82167 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5cc9f7d8-1aa4-3e0b-8b2b-1680686f22a8 | -4.50068 | -49.6432 | 2026-09-29 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fcd345d-c959-3124-8d6e-3a0374a562bb | -3.02053 | -53.8689 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2f2c4d6-5acb-3b8b-8ee6-7c0677d6650f | -5.73615 | -45.0235 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21bf9beb-dc7e-381d-8998-53edc7386d87 | -5.48457 | -45.12769 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f740755-6acc-3d3b-b553-9a970b74caab | -6.28366 | -43.64441 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| d39f30c0-dbc3-3fe3-bc4c-e786bf333204 | -7.3896 | -46.42806 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e15c5431-4259-3277-b31c-647967605166 | -3.14781 | -54.09922 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ca4c1a-bcb7-3569-82ef-4f0f0105ed24 | -7.83405 | -45.81921 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 26f7cd8e-116d-3e21-8140-af37b414ccb6 | -6.99976 | -45.34256 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7031d666-617c-3a6b-a4c3-7cdbc428a978 | -3.02109 | -53.86532 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f0a7a5c8-4b6d-3c99-a3fc-7bb9e83da29e | -7.84512 | -45.82504 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8d51b762-36c3-3cac-85be-1403bf568c7a | -5.72213 | -53.46034 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4148fc0f-64e2-3add-a345-e4d207c28d0d | -6.31495 | -52.62215 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4d986634-e09c-30be-912e-0f4065dc2080 | -3.15339 | -54.08558 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c2a3524-3ec6-3a7a-96ae-3a980f26e0a1 | -6.29558 | -43.64711 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a099ba25-574b-3787-9b2e-a4be624a8467 | -5.36484 | -46.22764 | 2026-09-29 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa579388-08ef-3abe-b82f-75ef3bc4520a | -6.15492 | -52.90702 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6ec493d-d890-36c7-9f3a-4043942b3506 | -3.01287 | -54.22235 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbffa548-aa74-36b9-a60a-ff5d52d9bfde | -2.97721 | -54.14484 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 340a42bb-7604-3b3c-8080-aead7b403049 | -5.73999 | -45.16912 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f271fea-1cd7-3e76-ac03-9fd6eeeaac19 | -3.1439 | -54.08052 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 371a2e44-db3a-32a1-a5f1-6066447c3695 | -6.72436 | -45.62376 | 2026-09-29 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a3196ee-bc2c-3bea-ba7e-6f2e9739441e | -7.38754 | -47.01649 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09c91c9e-bf4f-3202-96fc-02a3036a11f2 | -6.14713 | -52.90998 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64593713-ce8f-3efb-a690-2eae8b4d687f | -6.51998 | -54.95829 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 598e5d64-052c-3aed-a8f0-e2d9ffd3e794 | -6.31728 | -52.63119 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c94e5c56-36af-32fd-8fa5-ef7480daee16 | -7.84566 | -45.82109 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c84c3316-7311-3185-8845-08b5f5591b43 | -6.31429 | -52.62641 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ab0c231-7d43-3947-88b0-5e249361a001 | -5.30615 | -55.83185 | 2026-09-29 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f5a29ec-4752-38f8-b72c-1ff29aa50a2f | -3.85098 | -52.20758 | 2026-09-29 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 813e4bb8-99e1-34d2-a962-2d089dc9a745 | -2.89779 | -54.11065 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d30cc93b-125f-3768-9ce0-3f02ef3558f3 | -4.36013 | -47.77325 | 2026-09-29 05:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9338b2b4-bfd8-30ec-89dd-df3f3eaff3de | -6.32051 | -43.60984 | 2026-09-29 05:10:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89b8c0e0-6ad2-3150-b79b-25f59e52263c | -6.66898 | -55.11509 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 292b645b-a7e9-3ca6-898c-481019162f07 | -6.30795 | -43.61354 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 81179bfc-0272-3516-afc2-5d04072fbd0b | -7.6101 | -46.45969 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a7d692ad-e2d8-3e09-bd98-de1011026245 | -4.82514 | -45.63937 | 2026-09-29 05:10:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a56d1ab-f451-32e0-958d-ac8eb8eab326 | -3.01176 | -54.22937 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ff84365-8e9d-3266-816d-3002a6d5ef98 | -3.82623 | -55.90839 | 2026-09-29 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 08dfc43c-ea94-3c4d-bb84-dd68da3e172a | -3.15841 | -54.09723 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8036f80-6c91-3922-b727-379a8b2ed6a5 | -7.43364 | -46.88096 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68d06e06-9891-31a6-b6aa-6fe451336b45 | -6.38372 | -55.13498 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26ecc034-5f67-3121-9295-f35ecf676397 | -6.16727 | -57.69865 | 2026-09-29 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba455b4-1440-397f-ad39-8507ae3834ea | -1.34622 | -55.47764 | 2026-09-29 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e84c5eef-5ddb-3ed8-a562-15006c61f267 | -1.05533 | -53.58315 | 2026-09-29 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b11a2699-3693-3bcb-91f0-a92db71d314f | -2.9112 | -54.19902 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6e68eef-13f6-35d4-babb-a210e907a881 | -8.21542 | -45.45679 | 2026-09-29 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45e3ca86-576c-3808-82a1-ec56f22624c0 | -3.14446 | -54.07699 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ab07ddc-94cb-3474-9358-352f1f9c8057 | -4.45612 | -47.91908 | 2026-09-29 05:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdf3eccd-5ccd-3bd6-8752-0e1bf1a10608 | -6.29097 | -43.63979 | 2026-09-29 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f1058a25-e07d-314b-b021-c009c8ac7bff | -3.71402 | -54.23049 | 2026-09-29 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 433b8df9-1f5a-3488-8cb1-938bd1d0dc55 | -7.27782 | -46.79625 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d67d9e78-d365-353a-8b2f-d4f6c828f773 | -5.74473 | -45.17822 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9ba7776-f9fb-3e27-95e7-0d5ba7048a4a | -6.29962 | -56.03553 | 2026-09-29 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f586e37b-e694-369d-b26f-7971c5a93437 | -3.15116 | -54.078 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dc4cd48-70dc-3755-a23b-63471f7e9fe6 | -3.42123 | -48.33616 | 2026-09-29 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb6e037-15c0-346f-936d-fd6638683edd | -6.13875 | -53.05843 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8b3d2cc-3321-3292-9187-bfc3a85dd888 | -3.85983 | -52.00596 | 2026-09-29 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9096738-b183-385f-98b1-a976fd58f83a | -7.52077 | -46.61628 | 2026-09-29 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc6eef3-25b8-39c6-b8f6-ed9c2d734cc0 | -3.71458 | -54.22696 | 2026-09-29 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 49a1800b-fad4-3d16-9cff-e20db87e6368 | -3.70619 | -54.21483 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4a040bd-1cf1-3073-857c-a2ecd681a2b6 | -6.75057 | -55.09209 | 2026-09-29 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3917e094-48cd-32d1-ac54-125d2dac4ccd | -5.73882 | -45.1774 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 839baf56-8910-3cc9-9b36-932f5bb45c7d | -5.7349 | -45.03243 | 2026-09-29 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2abaa3d6-9920-3002-a20a-945b82154e3f | -3.01454 | -54.21183 | 2026-09-29 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb2e51da-f0fb-3ac8-8b94-000b9ab5d3f7 | -7.47416 | -45.8117 | 2026-09-29 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56adfd6e-ca28-3b14-8ca1-4ea907c756d2 | -2.89554 | -54.08144 | 2026-09-29 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed28a297-73fa-3056-a811-e1c953087abc | -6.37902 | -45.81087 | 2026-09-29 05:10:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8626632c-8887-3eec-9ed2-31e35ce47ad9 | -6.31772 | -52.6297 | 2026-09-29 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f258bcf-fe4d-3f64-9edd-37f649758e3f | -7.82769 | -45.82224 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6fc07619-3f53-318f-9150-cdaf1206d6d3 | -7.83986 | -45.82012 | 2026-09-29 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README56.md)
