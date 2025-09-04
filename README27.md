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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 699ca79a-4c03-3db2-94c2-2245d0178f22 | -5.70226 | -45.15935 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e71d9a6-4ec6-3f4c-b57a-4ba3c0bde83f | -7.04721 | -42.37712 | 2025-09-04 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8038dabe-05ed-35b8-be53-277a888e0eb8 | -5.71426 | -45.25857 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e95e898c-0d5c-3fb6-a867-216c747e667b | -7.63877 | -46.5548 | 2025-09-04 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5f612eb-452e-3923-a5f8-10548e1fda4d | -6.59801 | -44.06526 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b9cb04a-f8c8-3f01-9ff4-b97ebac71d70 | -6.92639 | -45.55462 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a73835d-8301-3eeb-88b3-1df51923c2ea | -6.30329 | -43.58955 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5d47896-1fff-34d8-a976-edc399bf81d7 | -6.24069 | -42.61531 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 63755418-9bc3-384e-867f-349431478b90 | -6.26551 | -43.57571 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbc2b62b-f5b9-3b54-90a3-5eefb3922ac0 | -6.48259 | -45.39249 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a841c39-3b30-3bc7-aaa7-f4c2725f71a4 | -7.26257 | -41.89829 | 2025-09-04 04:25:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eaec2349-2174-3a3b-8103-744c6328a45f | -5.31032 | -55.86018 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7a41a52-f9b9-35fc-b8e6-6b2adb261038 | -5.31095 | -55.85804 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c0a5d18-70c4-3aef-a9a4-56622b8d22bf | -6.29142 | -43.59619 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a2128a8-7291-384c-890e-a9df6e974e2d | -3.17124 | -48.80377 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce549389-9301-309c-a2c3-8000c817eef8 | -4.18244 | -48.58401 | 2025-09-04 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c903bbe2-9913-36a5-9fc5-07d8710b9cac | -6.85284 | -44.26347 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0efed716-7c0a-3cea-81ce-eadd6455a345 | -6.74711 | -45.9244 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08f5cf0d-1b1e-3e7f-885c-5ff85261bfdf | -4.99701 | -56.26339 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bb55b5e4-3588-3d36-93dd-0aee483260d8 | -6.07742 | -43.28297 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 22abdd35-b380-3ed6-88cd-1a8a40635222 | -5.68898 | -45.17897 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac20cf9-f2f1-345c-8ec0-a1431048d4fe | -5.69864 | -45.40334 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68faf03e-6938-373e-b960-c30c4c37cab4 | -5.67163 | -43.66887 | 2025-09-04 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d54da7e-258f-375b-82f4-640c1550c120 | -6.54558 | -42.94987 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3def04bd-2cdf-3102-8197-e85465ec177f | -4.89467 | -44.952 | 2025-09-04 04:25:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35c8c3b8-c88a-36e7-a001-257d4450cb9e | -6.78448 | -43.10572 | 2025-09-04 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0fb294e-15b5-346f-a0d2-941d758e514c | -5.38224 | -45.95072 | 2025-09-04 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6223501a-4f31-3c01-bab4-257c0fd0629a | -6.23701 | -42.43489 | 2025-09-04 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f2609909-3c16-3cea-8b32-122a0de110bb | -6.73676 | -42.25216 | 2025-09-04 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| febfeb68-9b42-3e51-9fe9-5e53f53c70d9 | -6.32179 | -45.68284 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 109041db-981d-3cf2-9ef1-4a8476f5772e | -7.60306 | -46.21556 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e8b9da5-9823-3101-aebb-886e3373ee8d | -6.87849 | -45.55827 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 56b1450c-2bf3-3830-bb14-4dec111ce3e5 | -6.32511 | -45.68337 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 09153677-8118-3dbf-aa84-027729fc1c16 | -3.38221 | -47.61263 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 826d49d2-8ef7-3153-9196-0dd564e4aabc | -8.00821 | -44.78139 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3d2229d-35a2-3dc4-9b12-a7f5eeb2746a | -5.69641 | -45.94365 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32906a5d-1bba-323a-8b55-7e26ef7fc3e7 | -5.8923 | -42.99276 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4632cb85-3192-315a-8711-f28d7a5a937c | -4.69036 | -48.60908 | 2025-09-04 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22afe528-54cb-34d1-83e1-a3370e3ed824 | -2.93554 | -48.82447 | 2025-09-04 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0d70384-04d0-3d60-b7be-67ff545978cb | -5.80265 | -45.41273 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbdb9902-b47d-36a9-8b5a-0d1957c9993d | -7.93347 | -44.94989 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30d6ed00-bb03-3817-bef2-211e8c9cc6f7 | -5.60809 | -42.88929 | 2025-09-04 04:25:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 08674415-519e-37a1-9688-bd489c729f32 | -6.25739 | -43.29609 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 190cb51f-a924-3289-8bc0-78395800cd19 | -6.9653 | -44.33108 | 2025-09-04 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e838eba3-c173-31c2-b835-dfbe5bc2c4db | -6.34276 | -45.67906 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1bfaaf0-9f48-302f-9d45-b26e03d41ad6 | -6.02449 | -46.6734 | 2025-09-04 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f283fd5-875e-397b-a02f-e92f3da32f9b | -6.33945 | -45.67852 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d686df7f-e4ec-33d7-b8f5-e7ded105186b | -5.70001 | -45.15176 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4dc473dd-0810-34e4-8330-a407054afc49 | -5.91104 | -45.9417 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 895cdc80-9b7b-3bd8-afaa-007db739714e | -6.71067 | -44.18014 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed26a04d-3c47-30b6-bb07-6f37366fe502 | -2.21833 | -48.22855 | 2025-09-04 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6fb14c9-4f58-3ae7-9d34-8b0240dbd430 | -6.84062 | -46.39265 | 2025-09-04 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 864d62ec-f931-3b93-ac57-348c72f9e7ef | -5.9804 | -44.12019 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46e42359-dae0-3696-a543-5871fa7f424a | -6.37508 | -43.01546 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6a6b9d2-76ac-347b-b7a7-3b1210d7f83e | -6.29557 | -43.59268 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba6f82e6-d669-38ab-8f04-990342926e8e | -8.00558 | -44.04027 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba37e23-5b56-34d1-8196-f7d9812e1af5 | -6.2509 | -42.6486 | 2025-09-04 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e8ea13a-d7a6-3276-9f81-475aa4a6d84d | -5.48556 | -45.21988 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8adc15-ad89-33d0-995c-dfd16b6bcf19 | -6.54254 | -42.94708 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 575d9c13-2af9-3656-826d-2801f96253b9 | -6.29419 | -43.50551 | 2025-09-04 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 922379d9-081f-3f62-94cd-d7385162e19c | -7.93743 | -44.94675 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e31a006d-f76c-36d0-9f1b-e832a2157042 | -6.88769 | -44.88256 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11a98730-0d51-3c5a-bf6c-05c1573aa623 | -5.8688 | -46.12588 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3032cd2-571e-3509-8675-84d4b58520ce | -5.85764 | -45.64976 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b83ab415-9ae0-3bce-b186-ef111bb8b1b4 | -8.03402 | -44.1414 | 2025-09-04 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c675c4bd-daa0-3d59-9db7-f7efa59e0def | -6.32202 | -43.77882 | 2025-09-04 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44521027-2182-37da-9387-7627341e3608 | -3.25854 | -46.92959 | 2025-09-04 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0279c32-59c6-395b-827e-5196680c9c00 | -7.94083 | -44.94726 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d82e0645-fe40-3078-8934-1862535e1a6e | -6.22885 | -43.55483 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a522d5f2-7b03-30fb-8cbb-51fefec414cc | -7.93854 | -44.93942 | 2025-09-04 04:25:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47363488-97a0-34bc-89db-b40c16c54188 | -6.21426 | -41.80027 | 2025-09-04 04:25:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4d62e5ef-efff-3e1d-a8fd-28da65ab7d48 | -6.78506 | -44.45466 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a18b92c-c14e-3ab6-9623-8d0f958e7686 | -6.69312 | -48.4143 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f887ca4-51c1-3631-a994-6d7b018eddff | -5.69586 | -45.39935 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3176a707-1cd7-36b0-bdd1-71294401d70a | -5.86492 | -43.02056 | 2025-09-04 04:25:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc378002-505c-381d-a180-07c3f5b60178 | -6.23365 | -43.54612 | 2025-09-04 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91ea918d-7afe-36f5-a731-472034f3b630 | -6.18909 | -43.98962 | 2025-09-04 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39d5b1dc-9f22-3207-9f40-078cf7226888 | -5.87648 | -46.12001 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38939fb8-e197-3412-884e-a2c874c3b838 | -5.92693 | -45.5536 | 2025-09-04 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e40e5657-b190-3675-ae14-d0bf72d90998 | -6.27399 | -43.32223 | 2025-09-04 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49b83b20-554e-384c-893b-396a8bb8bb06 | -6.78843 | -44.08927 | 2025-09-04 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| facccafc-9d63-3d43-b7f2-ea80f214465d | -5.70197 | -45.40386 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b79f04e-aa24-3ac6-bbcc-281d37310442 | -4.27741 | -48.19067 | 2025-09-04 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03adb83f-ecf1-3f5b-95ed-54a250d41338 | -6.96305 | -45.56026 | 2025-09-04 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c6a9656-7d1a-3a7f-be8f-3645f11e7c42 | -5.49557 | -45.63932 | 2025-09-04 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34b5efc3-39ba-3b5f-8d67-99dadd58950f | -6.26078 | -43.58308 | 2025-09-04 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2787115d-5c5c-3327-8001-281f6deec7d2 | -6.79025 | -44.48995 | 2025-09-04 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0a7b4a6-9fc8-321c-b933-dd1e6ee2e29a | -7.4578 | -42.01856 | 2025-09-04 04:25:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0b5bc73-caf7-3c21-b45d-22de240ee571 | -5.30202 | -55.97575 | 2025-09-04 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8689de8b-cb96-32a4-8071-3809980a7abc | -6.99853 | -46.60191 | 2025-09-04 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67431723-df28-30bb-93cd-8a900f8bb2b3 | -6.2759 | -45.67215 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59753bf7-5bbc-3ede-91a3-22cd7fee06f0 | -4.97648 | -45.12657 | 2025-09-04 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09677a68-272c-354f-a223-2b50bfbfb241 | -6.5411 | -43.1077 | 2025-09-04 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fb0e79b-f65c-356d-a773-3be366544993 | -6.05121 | -45.035 | 2025-09-04 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bbc3a6e-e93d-3d6c-bcb4-9b5384564927 | -8.01506 | -44.78243 | 2025-09-04 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75dbed6a-4eac-326a-9108-f9e1f36c4b24 | -7.81385 | -46.08438 | 2025-09-04 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7bfa8aa-b89b-312c-ac1c-40d8e05f7593 | -6.07207 | -44.69506 | 2025-09-04 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab93b9a6-d7fd-36a4-9f55-c7803f6398ce | -6.6891 | -48.4175 | 2025-09-04 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0dd41f0-5749-3ff1-9f05-e5e4d0451f5a | -5.7056 | -45.15987 | 2025-09-04 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef3df571-bb0f-36c6-9bf2-91755ad2faea | -6.49456 | -44.10145 | 2025-09-04 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README28.md)
