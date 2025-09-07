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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73d52b1e-7b68-34c2-8f9c-732c25057a6b | -6.0659 | -43.3006 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7b7153c0-97b8-3647-b1d2-35199b80ef9b | -5.84262 | -44.10068 | 2025-09-07 04:19:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b570841-cb05-3b7b-8aea-1a0bcd8dfbad | -6.19661 | -43.37928 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88f6722d-8cc9-3bb0-bef6-f4ee5f691f2f | -8.68484 | -45.31168 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ecd12c19-1c32-3ba5-8aa9-e3c2fad99a26 | -6.14942 | -44.24537 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d00480cf-de41-383f-acd3-a00cf9058dea | -10.73965 | -48.59618 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9043ba61-99db-398c-a305-3e1172595861 | -10.3529 | -46.46428 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bbb8fb23-9b9e-339d-b753-45a94ad614ee | -11.82642 | -46.76725 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dea796ea-90fb-3488-8a1d-2cbe01a021e9 | -11.32104 | -46.57079 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f326826f-e355-3fd5-83c2-4b7eff4c7739 | -7.19304 | -46.5704 | 2025-09-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe440f6d-8b79-3722-9d25-603156148e58 | -6.20127 | -53.24616 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 231eaabc-05db-3b80-9acb-2136494ee47b | -12.01602 | -47.78105 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d2f4307-60e4-314b-8fb0-a3711477d98f | -6.29759 | -44.7928 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f80e06c-9b4f-374e-81ec-f20b03bddac9 | -7.28038 | -45.17261 | 2025-09-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e905ae75-a80c-3325-9c56-2be83e2bd1f8 | -10.71836 | -48.59223 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c2917fc-2ab5-36cf-b2c2-764866db88e0 | -6.87265 | -45.55688 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14726c7a-f7d3-3815-96fa-f05767174f10 | -11.04811 | -54.17545 | 2025-09-07 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 37543aea-cacc-35fb-96c2-c337fa2561b2 | -11.90066 | -46.64454 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90b11def-6cf2-31cb-b9e4-563013860809 | -7.81742 | -45.12661 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94cb0d2f-9209-38c7-89d5-53cd8f3f217d | -6.17275 | -44.31289 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6fb9d1f-1fc5-3e95-bd6e-1984ae7a34d4 | -7.05396 | -44.34465 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcfffa7c-a5eb-3f89-bc54-d459723ee18a | -8.68925 | -45.30525 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f13cc714-aea8-349d-ae3a-be1b1be57c11 | -8.91457 | -45.81277 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45273e34-ffbf-393d-8c12-fd291151fe03 | -8.03546 | -44.03772 | 2025-09-07 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4eb321d-146d-3ab6-8404-ce7001ff4649 | -6.20416 | -45.04028 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 491670ca-72dc-38ee-aa01-8f0ae2438bbb | -10.79903 | -47.2613 | 2025-09-07 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3670a2ab-e1ae-3800-8232-8dae45a0541b | -6.19872 | -53.26095 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a549ddc-f24a-348a-8c61-623a7a144369 | -6.88309 | -45.59825 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 895086b1-f459-3fcc-8f7e-236b97194ca8 | -6.93146 | -44.32504 | 2025-09-07 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2c5708-6697-3a34-bf36-4fdb3318555f | -6.19675 | -44.18179 | 2025-09-07 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fe19d9f-7360-35f4-981f-8a2e53afbd3f | -6.21956 | -43.3205 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2879c8c2-ceff-3d59-812b-12a5cf74fcdf | -7.81687 | -45.13007 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 996515b7-d28a-35ce-a90c-0b6b2a21d2da | -11.84964 | -50.53152 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c19ec7bc-734d-3e02-a8c8-f00803728b42 | -7.74161 | -48.81759 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc471414-bae9-3e54-a413-03b821f8c32c | -6.93091 | -44.32851 | 2025-09-07 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9288a3c-b338-3b6c-9f09-318659bed227 | -7.77236 | -45.43254 | 2025-09-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c070df20-a57d-3783-961d-d64db0313af2 | -11.26228 | -46.51479 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c39ac36-38c3-357b-8a06-f2cbf3be6462 | -12.85174 | -47.99112 | 2025-09-07 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a884ceb-08d6-3967-8abf-0465f8318b25 | -8.18119 | -44.77936 | 2025-09-07 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a887723-81ee-3410-962f-dc79e52e6aab | -6.27469 | -53.4454 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36ae1e1f-ac44-3b47-8f09-5ce9dc2ff1cd | -11.3216 | -46.56726 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b712635-1124-3270-bd86-f769d6b92da8 | -6.88207 | -45.54059 | 2025-09-07 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83fc3eb8-efaf-3b9c-a53b-64c68f034076 | -11.29177 | -46.54059 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cd6f913-e66d-3fb6-821e-d01d388ba66d | -6.20077 | -53.24908 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7157c81-79af-3198-8cb5-cd92b8c3f684 | -6.23871 | -43.29775 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c534ace-9645-39b2-a67c-44e0742f45d0 | -6.52736 | -42.41755 | 2025-09-07 04:19:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da82c256-a4a3-3bf6-bc3b-baa365740dd5 | -7.76505 | -50.75647 | 2025-09-07 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e701cd97-035e-32c1-b654-7b0af8cc31c1 | -6.59712 | -43.966 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a415dac1-9b2b-3b8e-a301-37342f88fccb | -9.98848 | -51.64709 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0eaa7e9-96b2-3331-a01b-44eb2b3c2398 | -6.15442 | -44.25679 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e8cd012-1f15-3488-8efe-c33aaf10e36e | -7.68753 | -50.28818 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97625dc2-eeb4-3164-bfbd-1225164129e9 | -9.97344 | -51.65662 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69504445-cbf6-3dcf-8a44-4528cfffde68 | -10.74034 | -48.59207 | 2025-09-07 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 115c89ae-6409-3e4e-b651-55d107522f26 | -8.91844 | -45.80981 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12d01b2e-cac1-3db1-be78-5634dbf0eca8 | -6.43652 | -43.62355 | 2025-09-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a674beb6-d47b-3a75-8f3a-c195aabf07b3 | -11.58508 | -47.75619 | 2025-09-07 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e9436fa-ce1d-35ab-b5c3-556a526b1573 | -6.54218 | -44.81418 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0524d33b-96cb-3bb8-8c27-f285091d81d3 | -6.8118 | -50.85269 | 2025-09-07 04:19:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f96d0b4-6231-3333-aa13-d30246a23589 | -9.81369 | -46.01213 | 2025-09-07 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2c761da-8151-3b78-a3ff-cc719ac02454 | -10.09076 | -48.09573 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f4b8ede-9ae1-390a-ac8b-e86b120d0abd | -7.67479 | -50.26401 | 2025-09-07 04:19:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ebedeb3a-2847-3c94-bc1a-95d0a1742a62 | -5.57554 | -49.08862 | 2025-09-07 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae436300-5ba6-3b12-a87e-4447161ad32d | -6.17989 | -45.42864 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 70414ebd-34c6-36bf-bf49-e39dde5bd8fa | -11.20726 | -55.0174 | 2025-09-07 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6f595569-5aab-398b-96bb-ef1b7275829e | -9.80206 | -46.02105 | 2025-09-07 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60a60b98-cefd-367a-8027-084848eb0213 | -6.18843 | -53.25945 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea817361-c87e-3ec3-9bb6-e18bbbd18f00 | -6.66365 | -44.79824 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b1358f2-d422-3180-9806-7b2521b7b5ba | -6.32287 | -43.28888 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4541092d-317c-359a-bfc8-7e88f12be5aa | -9.97145 | -51.65783 | 2025-09-07 04:19:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83e8d488-59db-331f-aeed-f8b59d3aed5c | -8.48213 | -45.17578 | 2025-09-07 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e57c00fe-3557-3a3c-a4f1-fce530ae22e7 | -6.54221 | -44.83545 | 2025-09-07 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4765560e-d5ce-3526-a122-fefe5f756f8d | -9.68488 | -51.07935 | 2025-09-07 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ea019fe-7339-3d93-ab1b-318154298ab0 | -6.05925 | -43.34347 | 2025-09-07 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f075693-7b1c-3878-b5ae-88dfa8245c61 | -6.2804 | -53.44324 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db59bef2-90a3-3bdc-9a24-2167fe92c7b3 | -9.77875 | -46.88913 | 2025-09-07 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92a94e71-3aaa-3cea-a3fe-6d97ccf330ba | -6.78144 | -52.80598 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84fb118b-9493-3192-af22-044ef4858f42 | -5.94297 | -42.96088 | 2025-09-07 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b231e1c-1870-3300-b620-24001bc19206 | -6.2722 | -53.42892 | 2025-09-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cb43544-b326-363f-a27a-6ceab0287e09 | -9.17636 | -45.5975 | 2025-09-07 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55df1573-6578-341e-bed6-70ab0cb98829 | -5.58332 | -51.91478 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d88a2cd-a3ce-3db6-a088-24eb042b58ab | -12.60935 | -44.62707 | 2025-09-07 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1695048c-d2ba-34f2-9cda-4ed564bbca73 | -11.76215 | -47.74644 | 2025-09-07 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f3782a-f036-3cd5-b5b0-92ed37329b53 | -6.3796 | -42.60559 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6abc737b-0400-36d0-88fc-ea8d3a62bd33 | -6.16548 | -43.1796 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4a76c30a-52f7-3b4a-b3bb-fce23e68e75a | -6.20175 | -42.62538 | 2025-09-07 04:19:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b56946c-f17b-3466-8389-fb6253c7ba27 | -11.4113 | -43.6389 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 852d99ea-cd1a-33fc-b4b3-2287558dec5e | -7.25089 | -41.88829 | 2025-09-07 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59304176-9271-3cfa-8496-f004bf3bb2ca | -6.15253 | -43.17387 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4bfd2dff-2ef7-3b82-b2d1-ba45bc3fcbb7 | -10.08631 | -48.07916 | 2025-09-07 04:19:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e93d1233-cf84-32b1-ba69-59d742f661a1 | -11.41477 | -43.63942 | 2025-09-07 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6d4e5954-b198-3e95-a325-47e0937f201a | -8.02335 | -44.13752 | 2025-09-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcaea626-0d24-387e-bf7b-f2cfb4834e33 | -8.93676 | -48.6554 | 2025-09-07 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 839219dc-bef3-3771-9def-a65a9f5cac6d | -6.38848 | -43.00534 | 2025-09-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2547e516-35fa-3be0-8407-7aec5ad8915a | -6.18267 | -45.43265 | 2025-09-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5c5dc8bc-97fc-3082-afce-9c1c03fdec8c | -7.73956 | -48.81479 | 2025-09-07 04:19:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a59cff0f-cd18-3a38-ad48-45b81799b4ea | -11.97655 | -50.40364 | 2025-09-07 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e5bc65d-a65e-34a3-876a-2726ebffbd18 | -10.35788 | -46.30541 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d9918f5-bff6-3035-83c9-091d71218ffc | -6.60153 | -43.95953 | 2025-09-07 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5f02d0e-4fa3-3ea8-8ef2-d416ebaf370a | -10.34681 | -46.45966 | 2025-09-07 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f1e971c6-af53-32a6-9239-70a45d0136be | -11.827 | -46.76363 | 2025-09-07 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README54.md)
