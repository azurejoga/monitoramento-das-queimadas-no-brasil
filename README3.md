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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884a08f1-f7cf-3cf0-8267-26d80fe318fb | -20.091 | -44.143398 | 2025-09-04 00:08:00 | METOP-C | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4f092ea9-de27-3d55-89d0-9954b938b331 | -7.711 | -50.310501 | 2025-09-04 00:08:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f7df54-3910-346d-bd85-565fc7447d81 | -6.2245 | -43.552601 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 614b349b-1ade-34d1-82a2-44ab62c0817b | -22.903099 | -42.422901 | 2025-09-04 00:08:00 | METOP-C | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd10b021-37fe-30c3-9003-d4eca54d3952 | -6.1993 | -43.346199 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20b7d460-f688-31d7-9fbd-1694541abfd4 | -4.956 | -42.066399 | 2025-09-04 00:08:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 01e3b669-a919-3d93-b945-6e1d680fa663 | -6.2265 | -43.561501 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3b8d1d8-d189-3491-b7de-10782e09fe20 | -6.2222 | -42.434601 | 2025-09-04 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cdf386de-7b09-390e-bdf7-923ed4f4b0fa | -5.6832 | -45.932899 | 2025-09-04 00:08:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 927e1fe3-895a-362d-a4cf-41a115b5143c | -6.2638 | -43.590801 | 2025-09-04 00:08:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a24f9db1-df2e-37b5-bd6e-9de27b43ec02 | -5.8891 | -43.0144 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e40304d8-e65e-32c0-bce7-b66d1e82bd26 | -5.7391 | -45.534901 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 750ae6e6-f573-3036-a824-c1af811c388c | -5.687 | -45.390701 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2b50e8d-4abc-39a8-a91f-90aa418c85a2 | -6.4052 | -43.2561 | 2025-09-04 00:08:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19625361-10f0-3e10-8409-b2a4d05bdfc3 | -6.2872 | -43.510899 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b78ba30c-4e4b-3501-bfcf-5a2a4b8a30de | -6.2599 | -43.572899 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c78b4295-478a-3657-8bc8-b541cee21018 | -6.2774 | -43.5131 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b62b5e0-0fa1-3440-80f7-1216e5f99bc0 | -6.2853 | -43.502102 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97d7491c-d16a-309d-850c-84d4a6e4e513 | -6.1622 | -43.3181 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc792f86-2010-3ac7-ab6b-3a918001293f | -5.693 | -45.930801 | 2025-09-04 00:08:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb28b2b-7e14-38cb-aa79-d9f9f2a7c2e4 | -5.8985 | -43.240898 | 2025-09-04 00:08:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 4b812b4c-beda-3f70-915e-746282b213da | -7.7013 | -50.312401 | 2025-09-04 00:08:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef4c164-3c42-3b8a-8a82-29126634e062 | -6.1974 | -43.337601 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb2e4f78-e9ad-3a51-a212-e6e054438feb | -6.5868 | -44.310902 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1042ceb8-faa0-3aa5-af87-528ad086d1b1 | -5.8873 | -43.0061 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6de388a-8107-330c-bccc-f1b018b44b78 | -6.2854 | -43.595501 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3a26ceb-8e84-3968-9fdb-e9cb1f2c7bbc | -5.6643 | -43.665001 | 2025-09-04 00:08:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a42a6fb1-df4c-3960-a2a8-aaf17358829a | -6.2398 | -42.605202 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6891d8fb-5f78-3663-a3c5-6937bcdc5f84 | -6.2505 | -42.653301 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8f095baa-c7d8-3a42-b8cf-e41d275487b1 | -6.2583 | -43.288101 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0a912c6-4e9f-3a7e-9f4d-888de0f8c089 | -5.5975 | -45.0308 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7801c01-6047-3382-a80f-76b088bf83bc | -5.6049 | -45.018101 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9e8a3d6-9158-32af-b967-0e20f064f27f | -4.898 | -41.7644 | 2025-09-04 00:08:00 | METOP-C | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| abb31612-3a3f-3b17-8e75-5c5ef4008ba1 | -6.247 | -42.637199 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61ca0ff0-f606-364a-bae5-31a3360e664b | -6.2932 | -43.5844 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a410437-21a0-38bf-bb0a-369bbd7aa334 | -6.5408 | -43.915401 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73784898-f48e-3fd5-8f7f-efef653b47e6 | -17.8783 | -42.645901 | 2025-09-04 00:08:00 | METOP-C | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 412f5882-2a8c-349a-9d7c-666fc371458b | -6.2441 | -43.548302 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff0a83d6-e202-3e22-9ec3-138a17ac3abe | -6.2478 | -42.5951 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a68179b-b04f-33e6-a550-939cdd36f912 | -6.172 | -43.315899 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a22f2871-bd86-3287-82b2-62b7d9c61317 | -7.7056 | -50.284 | 2025-09-04 00:08:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085211cf-aa39-3a58-b0e2-e06e8c2e08b6 | -6.594 | -44.063499 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 295b4b32-0f3e-33ae-aee5-6caf981d5643 | -6.5966 | -44.308701 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2380920b-89bb-35c7-819d-181daa0a2d5f | -6.2504 | -43.298801 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f52f255c-7dc9-388f-aefa-b868b2cd23b3 | -6.4905 | -44.1059 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13387863-8104-3c10-b8d4-ae294edc640e | -6.2585 | -42.643101 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 17baa2b3-07d2-3b6c-a4b5-664a35ac2b5a | -17.169701 | -46.2649 | 2025-09-04 00:08:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0867f5ff-cc33-3b9f-8a75-f36a99fb31f0 | -16.2999 | -45.6908 | 2025-09-04 00:08:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7aeb1746-6964-3c32-9bf9-e547196b3279 | -6.2523 | -43.3074 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff496e24-e5c1-3783-be83-c7d9f76e9c76 | -6.2952 | -43.593399 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 007e79e0-a2c3-3596-88a6-b8a9701f983a | -6.2142 | -42.4445 | 2025-09-04 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1aa3d51-fff7-3b6e-89ad-75d99867e87e | -6.2336 | -42.623299 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f5eebff-e0c7-3624-8598-156451c7cce0 | -6.1701 | -43.307301 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b31763e0-ad87-3e95-a7f4-22b4dbf831f4 | -5.8327 | -42.992199 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9da1cd1-073e-3028-af6e-9c615e026edf | -16.312799 | -45.7062 | 2025-09-04 00:08:00 | METOP-C | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cca9ef11-6f53-3aa2-970b-c0aca5ae9d14 | -6.1206 | -42.946499 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8337a73e-8c95-3fd2-bc9a-7128e5ee5475 | -6.2485 | -43.290199 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d40f868-5fb7-30c1-a9ca-c09c239525a8 | -23.299101 | -46.156898 | 2025-09-04 00:08:00 | METOP-C | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee6467aa-bf50-3d3d-9a1e-cbd1e3c42bf6 | -22.9007 | -42.4095 | 2025-09-04 00:08:00 | METOP-C | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da77b47e-6d32-3b8c-b97b-739b24c0ab77 | -6.2089 | -43.389702 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae4e1aaa-81ed-35f9-84c6-21df88c2d136 | -6.8322 | -46.3787 | 2025-09-04 00:08:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f10ce3ba-8e18-335b-b0f7-05f4b84dd16f | -6.2618 | -43.581799 | 2025-09-04 00:08:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf53f136-d2d7-392b-8024-e44868c75839 | -5.6859 | -45.945099 | 2025-09-04 00:08:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65314d8a-164d-3c52-b0f8-c61500c8131e | -4.8964 | -41.757198 | 2025-09-04 00:08:00 | METOP-C | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0e809946-0355-3ca3-97ff-da6a49366835 | -6.264 | -43.313999 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| febcaa17-ef92-3657-94a8-07bead67468a | -6.2324 | -43.5415 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51ca23c3-d4ac-3758-9fd0-05b2626f5f77 | -6.1603 | -43.309399 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| b278ea11-8e27-3adb-83e2-20a97592e5f5 | -6.1524 | -43.320202 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| a027e6bc-13ef-3300-bc83-ffb7dcc6ad05 | -6.2434 | -42.621201 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8db6f867-aacd-3029-bc0a-cd9214051ce9 | -6.224 | -42.442402 | 2025-09-04 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70598a5f-3763-36fb-a91f-fd7600d98cd0 | -4.5545 | -40.346298 | 2025-09-04 00:08:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c1fdcfd1-65f2-347e-a99f-3f795c8a6f06 | -6.4072 | -43.264702 | 2025-09-04 00:08:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6af818b3-444b-33be-8934-470e2ac11a43 | -5.8808 | -43.253601 | 2025-09-04 00:08:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a07f9c1-219e-34b1-bb0f-bca1c0a4ad75 | -3.4844 | -40.6716 | 2025-09-04 00:08:00 | METOP-C | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fff44b9d-aa61-34bf-8b63-b05befa9ed67 | -6.1225 | -42.9547 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3a77244-2b19-31cf-969c-022324b24aff | -6.232 | -42.4324 | 2025-09-04 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6fa2674-c3ed-3dfe-bf2b-0345f2f33ebb | -6.2487 | -42.645199 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 424cba0b-7311-3b47-b9c7-3928d8a82674 | -5.4841 | -45.2136 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4fbc521-75ce-3dc5-89c0-31fa1da5e215 | -4.5643 | -40.344101 | 2025-09-04 00:08:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6b61c0f5-15b9-3061-b235-2272ca6ea277 | -23.302799 | -46.180698 | 2025-09-04 00:08:00 | METOP-C | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3adbe047-ce46-3573-a617-1eebd82aaf35 | -4.9624 | -42.0494 | 2025-09-04 00:08:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8e57050-86b8-33f0-867e-e2218f42c318 | -17.875999 | -42.6343 | 2025-09-04 00:08:00 | METOP-C | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 02ea9544-2354-338a-ae87-4f32542b1e00 | -6.2168 | -43.378899 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc324ea6-f2e1-318e-81e1-66340350675f | -6.2266 | -43.376701 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb4a6cec-5052-3da2-a23c-3155ddc8d338 | -6.1739 | -43.324501 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcf27e0e-2b01-34ae-8f89-442c9d99c914 | -6.2205 | -42.426701 | 2025-09-04 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71aa634f-cc37-34d4-90e5-810330ee4bad | -5.8854 | -42.997898 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb829efa-378a-3f8b-849c-5198d9557482 | -16.303101 | -45.708 | 2025-09-04 00:08:00 | METOP-C | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03ac8336-8f3f-33be-b3ff-52befd4eb769 | -6.8725 | -45.1964 | 2025-09-04 00:08:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99b36023-4032-3c98-b353-0e5b21a14377 | -6.136 | -42.9692 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2cbe136c-d35e-3946-8eef-41dbc8ac464f | -6.87 | -45.185001 | 2025-09-04 00:08:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5fefae47-5ce6-3c1f-ac83-36eae29b78dd | -4.5659 | -40.350899 | 2025-09-04 00:08:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4da87d31-9a14-3453-86fa-18ea29c1c29f | -5.4865 | -45.224499 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c659c0f3-b49d-33ad-beef-d1a2f1c793a0 | -6.4884 | -44.096298 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42a9e292-1b2a-370e-b73c-1fa76bfc43a6 | -5.8836 | -42.989601 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d8e78233-8e23-34d6-a57a-be0f3a2f00fe | -6.1341 | -42.960899 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8a70e9bb-7bc0-3f56-80da-81f7ee6a20b1 | -6.0822 | -43.2813 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 59ebc2b6-6720-3759-8639-d26652e52a29 | -5.5952 | -45.020199 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88cb5423-cf55-35d7-b8a2-0ad2d4442eaa | -6.2324 | -43.402901 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faf630d4-41f1-3152-804d-536870772c43 | -6.2416 | -42.613201 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
