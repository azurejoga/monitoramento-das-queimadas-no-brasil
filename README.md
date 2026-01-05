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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cccb8abe-0ccf-32a4-8bc5-ba205cb9c8ce | -22.77044 | -48.01195 | 2026-01-05 00:07:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 63cdb861-4c46-37a3-9d6e-ea3ed5983dad | -10.81981 | -37.15125 | 2026-01-05 00:09:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 9b577b90-34ab-3b9b-a134-31b60cc18a6a | -10.06484 | -36.5818 | 2026-01-05 00:09:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 15194d1c-426e-3801-9c48-34d9ea370b59 | -12.19585 | -43.9543 | 2026-01-05 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e39c72ad-a181-3e4c-b496-a47ff7251d5c | -10.06004 | -36.55363 | 2026-01-05 00:09:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| 59ef976b-a806-3558-a54e-00f047a9ec1e | -10.86872 | -37.27125 | 2026-01-05 00:09:00 | TERRA_M-M | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 33.5 |
| 87643070-a54f-34ed-97bf-57bf669fb6a2 | -10.06173 | -36.55877 | 2026-01-05 00:09:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 51.1 |
| ba339c4b-8b84-3229-96f3-04b97bb07d83 | -4.81988 | -47.33861 | 2026-01-05 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f84bdc6b-dc27-3f63-86a5-3b10a31d35e0 | -4.31351 | -48.62982 | 2026-01-05 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e1ee506c-5552-35f6-b9d2-f6900d88f21f | -2.33442 | -45.82268 | 2026-01-05 00:11:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ffc36dd-d0db-39bf-86f1-06e824ee2e20 | -3.92423 | -46.51623 | 2026-01-05 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 570f45ff-b501-3750-8f84-5f13ba90a48d | -4.73313 | -45.57033 | 2026-01-05 00:11:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b58c70b2-dbff-3b64-89fc-c857f6bec185 | -4.50192 | -48.51958 | 2026-01-05 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4ac6b26d-68a9-3ece-b7fb-536aceb09012 | -3.69612 | -47.21084 | 2026-01-05 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1cbd54d7-432f-349c-9efe-c25640cbf3db | -4.0529 | -45.72432 | 2026-01-05 00:11:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 65210396-7a66-3597-aa50-21787897932d | -2.41685 | -45.8293 | 2026-01-05 00:11:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8a1d6016-7bdb-3c01-a5c2-3157e642e3f7 | -4.41077 | -43.72845 | 2026-01-05 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 14ebfd9d-51d7-367d-9630-dac5e0f0878e | -2.33317 | -45.81372 | 2026-01-05 00:11:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4c23276e-8a9b-373f-92c4-5ac76d7b59d8 | -4.68485 | -46.42325 | 2026-01-05 00:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 39d95583-0dbe-3dd8-802f-6e6008dd2358 | -4.3462 | -44.1283 | 2026-01-05 00:11:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 78467541-9a90-31a9-aa0f-c30c067769fe | -2.76399 | -54.21481 | 2026-01-05 00:11:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| cc1682ac-3a30-3b34-8860-ea65c78202eb | -4.25983 | -48.84206 | 2026-01-05 00:11:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8d9bd4eb-3dba-373b-a832-79d80c621357 | -4.75585 | -46.59555 | 2026-01-05 00:11:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 939e3e26-08fa-3465-9cc1-755c98984db6 | -4.87522 | -48.15469 | 2026-01-05 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af83f272-c598-34f9-b91c-807ea0272e11 | -4.15946 | -43.67015 | 2026-01-05 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3e4e9a70-29db-34cd-bf86-7b6bca613566 | -2.48477 | -45.31754 | 2026-01-05 00:11:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4a333343-cc8a-382d-917b-9c396e4bd2f6 | -4.79179 | -45.20021 | 2026-01-05 00:11:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fdc6b8a3-10e2-3d83-9a8d-b7b4ecfdf1e6 | -3.69735 | -47.21975 | 2026-01-05 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0dbfa0be-bf27-3682-a4a6-7ffd010f1f5b | -2.47387 | -47.97218 | 2026-01-05 00:11:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 096efe38-2566-39f4-b546-52382cd3a1a1 | -4.73437 | -45.57924 | 2026-01-05 00:11:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 155e8723-69bb-3746-9dc7-4210ccec4124 | -4.05167 | -45.71545 | 2026-01-05 00:11:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 008f1529-c33e-3524-8fd4-e550163ed430 | -4.3448 | -44.11843 | 2026-01-05 00:11:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c475b482-f631-358f-8b2a-68ce614fd8da | -2.8119 | -53.00455 | 2026-01-05 00:11:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| a5bd0dbd-cc8f-3139-8fed-32112c6aaf72 | -2.7364 | -42.6081 | 2026-01-05 00:11:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 79a2ec13-6054-3b86-a66f-debb45dfd164 | -2.37094 | -46.49001 | 2026-01-05 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4be820b2-9f03-3038-a4d6-33a06701cb39 | -2.73454 | -42.59514 | 2026-01-05 00:11:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fd3d5252-340a-3b10-b8fa-623d4a683e44 | -2.44767 | -47.78095 | 2026-01-05 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2f3737c5-e046-376b-868c-df8f8aa5828e | -4.68364 | -46.41447 | 2026-01-05 00:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18e39486-7139-3a49-92e6-27f1735c8033 | -3.69858 | -47.22868 | 2026-01-05 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b9102f7-ccd2-30a5-9c99-8369262b6c58 | -4.19115 | -45.45634 | 2026-01-05 00:11:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f29845f7-32bd-3afc-b21f-fc599038d52e | -4.50837 | -43.69735 | 2026-01-05 00:11:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 19c34dd9-0d14-3acf-bae4-1ceec2b3b5d4 | -4.69365 | -46.42201 | 2026-01-05 00:11:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fd35fd94-5543-3a10-a9fd-071f6b2c6e84 | -2.42201 | -51.83367 | 2026-01-05 00:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 97b38d32-b7be-3189-8ad6-96521bed1a28 | -4.32477 | -45.35195 | 2026-01-05 00:11:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4100272e-e050-3b13-af5a-c0087feede05 | -2.79901 | -53.00573 | 2026-01-05 00:11:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4ebda613-73b4-3c0f-aa89-706f0ad38b0d | -3.88311 | -42.52504 | 2026-01-05 00:11:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| efe3609c-a231-3844-b387-cb8e0389bd7f | -4.6833 | -43.26006 | 2026-01-05 00:11:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b8be48cb-cd3a-3e50-9009-4828d1957c5a | -4.82114 | -47.34774 | 2026-01-05 00:11:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 74f1b958-d2ca-3bf1-ac10-55088be69c5b | -1.35384 | -49.42669 | 2026-01-05 00:13:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4d96fa93-7eae-390c-ba2e-1db577c4de6a | -1.34852 | -49.42315 | 2026-01-05 00:13:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f1d481a5-d21e-3e2c-9e4b-e26f80d68550 | -1.59621 | -46.02719 | 2026-01-05 00:13:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 590c1984-0ae6-39c3-ab5c-ad19c94f5fce | -1.34997 | -49.43348 | 2026-01-05 00:13:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c66ad1e2-86b6-3402-93a6-22614af94535 | -1.29626 | -49.32568 | 2026-01-05 00:13:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b0afad0d-8989-3a67-99f5-e6111c0c1c84 | -1.59498 | -46.01828 | 2026-01-05 00:13:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 21d4c46c-c192-37d4-9e91-d4d2c9173923 | -1.35524 | -49.43704 | 2026-01-05 00:13:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 16a529b7-9df4-32dc-a700-afac65664d56 | -1.86726 | -47.98765 | 2026-01-05 00:13:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d8a5d573-eec0-3fb0-80eb-b8efdbe73198 | -0.26361 | -48.7921 | 2026-01-05 00:13:00 | TERRA_M-M | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea056ded-70f5-382e-8b7f-de25e3856b38 | -2.76004 | -54.22214 | 2026-01-05 00:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c12dbd4a-6c17-3e43-bc68-812e8ade1802 | -1.46103 | -46.04302 | 2026-01-05 00:13:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4bb00fd2-578e-3473-b6ba-ae5e1fe963ae | -1.78202 | -47.63296 | 2026-01-05 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b885f1cc-4904-3304-8336-2a561a76882c | -2.42517 | -51.83957 | 2026-01-05 00:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 672337ae-9774-37ed-a43f-5ef5609eb013 | -1.5519 | -53.2831 | 2026-01-05 00:22:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ca43533-c9c2-3fd8-b94a-544e822afdbc | 2.5505 | -60.3237 | 2026-01-05 00:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5450039f-ea41-374c-a6fb-c37f8070be32 | -1.2542 | -54.0616 | 2026-01-05 00:22:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c005e29-144a-3900-8c41-351480b5ff42 | -1.5944 | -53.971401 | 2026-01-05 00:22:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58d5362d-45e7-397f-b4e5-b975e5a5fd71 | 2.8764 | -60.203701 | 2026-01-05 00:22:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 06d9196c-40c3-34fb-9735-bbf46200ee64 | -2.4434 | -47.763901 | 2026-01-05 00:22:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3321b1-8ff7-3253-8c39-fbe049dcbc2c | -2.4457 | -47.774101 | 2026-01-05 00:22:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126802fc-3b37-38ce-9b30-c505babceecb | 2.5407 | -60.3214 | 2026-01-05 00:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 663b3f09-7ee3-323a-87d9-b2d9a5bbc6c8 | -2.1078 | -53.462799 | 2026-01-05 00:22:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9089f7eb-5e11-3417-b939-572ae243b0d4 | -1.1887 | -54.0909 | 2026-01-05 00:22:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c3493c-4182-3db1-aa80-76e7714fb3b7 | -1.3473 | -49.396999 | 2026-01-05 00:22:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff55ac11-01f4-3372-b5ac-9820cc08e3ee | -2.4252 | -51.817902 | 2026-01-05 00:22:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c619d60-fa80-3868-a82b-a029107112e4 | -2.441 | -47.7537 | 2026-01-05 00:22:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9aaafb6a-cf60-3540-87a6-f341c28cd2c4 | 2.8862 | -60.205898 | 2026-01-05 00:22:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 024f7cd9-18f3-3254-8b48-332cf218e34a | -1.5814 | -45.994801 | 2026-01-05 00:22:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd703d6a-0718-3bf4-8813-a015033f07cf | 2.5634 | -60.3125 | 2026-01-05 00:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| df940ffa-0da7-37ab-a1dc-4c5f871d974d | -2.8045 | -52.9902 | 2026-01-05 00:22:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b457bb1c-1278-3f80-b67c-49207adba7f3 | -2.7565 | -54.191898 | 2026-01-05 00:22:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ff9d233-c7ba-3479-afeb-5385f8221eb6 | -2.803 | -52.983398 | 2026-01-05 00:22:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab8fa5a3-def3-38a7-af66-9fc98fb19c4a | 2.8733 | -60.216702 | 2026-01-05 00:22:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3b3ea930-fe4b-3919-b4c6-4064c0a2b2ed | -1.2558 | -54.0686 | 2026-01-05 00:22:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94fa2586-4103-3c35-8368-c4b3b0f8c398 | -1.3492 | -49.405499 | 2026-01-05 00:22:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b8285f4-cf53-3070-a7fc-224e3cd41d09 | -27.4044 | -50.384899 | 2026-01-05 00:22:00 | METOP-B | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4fcd8cca-3a64-3c95-b712-88bed134bd49 | -2.8014 | -52.976501 | 2026-01-05 00:22:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5c73890-016f-3be4-969a-1e040eab4471 | -2.7582 | -54.1991 | 2026-01-05 00:22:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de64aa26-3580-3c62-8bdf-1ccfc3987dd6 | -1.3512 | -49.414001 | 2026-01-05 00:22:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28458c26-eac5-3b7b-8fed-a0523045da3a | -1.359 | -49.403301 | 2026-01-05 00:22:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637250d0-c5b4-3f55-84b4-8a98cc5aff7c | 2.8831 | -60.218899 | 2026-01-05 00:22:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1f496645-b695-365a-af67-b38262fb68f8 | -2.4236 | -51.811001 | 2026-01-05 00:22:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f72bee-55aa-3146-84f4-1d49a8cea207 | 2.5536 | -60.310299 | 2026-01-05 00:22:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 086244fc-aa6e-3e94-8ec4-82987a5f4ad1 | -2.813 | -53.001099 | 2026-01-05 01:01:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c48152b-8eb1-33e1-940e-486a08d653dc | -2.4529 | -48.6222 | 2026-01-05 01:01:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d61e41e-3b0b-3522-8fab-891f0d8c70fd | -2.7625 | -54.217201 | 2026-01-05 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fc86f89-b368-3253-8be3-77b881961dce | -1.1904 | -54.1077 | 2026-01-05 01:01:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94c40ae-755b-3630-86bd-b3301a829467 | 2.8793 | -60.252399 | 2026-01-05 01:01:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e081c66a-bf48-3841-80f6-d0c3a6282e2c | -2.761 | -54.2104 | 2026-01-05 01:01:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d34748-9e8c-3cb5-867f-67a0a78752e0 | 2.5568 | -60.354401 | 2026-01-05 01:01:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b31a9705-25cd-39b1-8dbb-c96b6d68c752 | 2.5493 | -60.3423 | 2026-01-05 01:01:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7104b516-ad0e-3b59-8f34-c1fc3776f954 | 2.8816 | -60.242802 | 2026-01-05 01:01:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
