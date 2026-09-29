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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba20f629-8fb3-348d-9bbf-d9c7101e52d5 | -12.6078 | -47.2653 | 2026-09-29 18:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 081ff04c-eb75-3fef-beef-2f28f1972720 | -15.1852 | -46.1179 | 2026-09-29 18:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 141.6 |
| eb9f8885-2969-30ce-972c-2eb1bd8a8506 | -11.4119 | -43.415 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.4 |
| b03122eb-a921-3b49-890a-ef6a7fce7829 | -11.6404 | -43.4981 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 888720ac-70d9-32a7-a18b-4759e6c5f74f | -11.6212 | -43.5011 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| b3ea2367-7b86-3673-bec8-e7e67f21dfcd | -8.6451 | -45.3489 | 2026-09-29 18:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 7e4571b5-2727-3465-bb42-d334feb61e1c | -10.7056 | -50.8341 | 2026-09-29 18:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 192.8 |
| e8339d14-98a7-35c0-9500-b7dc4e2c47fe | -11.7178 | -43.4623 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 5e73b0c1-8599-3564-b846-34402d3b5721 | -11.1273 | -43.2687 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 152.9 |
| b3a307d1-6633-3c0c-a441-62effa8b6d19 | -10.2254 | -50.0093 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 45db94b4-1c00-3e6d-af30-2207256d70e4 | -13.3835 | -44.0132 | 2026-09-29 18:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 31bf3f10-7fdb-3168-85e7-c90bf3383ca4 | -11.4004 | -47.452 | 2026-09-29 18:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 8e6a6334-51e6-3bad-b49d-f4913ccb13ad | -11.8167 | -43.3044 | 2026-09-29 18:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 526.1 |
| d778b841-e6f3-3888-b903-58e99442e28c | -11.6941 | -50.6202 | 2026-09-29 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 455f5d81-e5bc-383a-8523-870777821976 | -11.4425 | -44.9303 | 2026-09-29 18:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| f4f37a2f-43ff-39f6-87ca-48d0dafc7e50 | -7.8613 | -71.7654 | 2026-09-29 18:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 101.7 |
| fcd2dd36-f987-3fa2-9ed3-953ab457d1a6 | -9.9595 | -50.1431 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 05d68763-ed01-33e2-a731-ad36d8efd0c9 | -15.454 | -41.4403 | 2026-09-29 18:10:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 97.7 |
| fe98a3e8-0121-34a5-9d05-03b74438c7a1 | -10.6505 | -50.7123 | 2026-09-29 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 3d2cdfcc-6ad6-3617-959c-a168df3f288e | -1.0238 | -49.2348 | 2026-09-29 18:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e6cda512-9c62-3def-9061-b80ad2baf7be | -10.9154 | -50.7059 | 2026-09-29 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 608d20ac-aca1-3e34-a144-205c75f4e394 | -12.4346 | -44.1733 | 2026-09-29 18:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 1560630a-b417-33ac-843d-abe31f2a9291 | -12.0618 | -50.2127 | 2026-09-29 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| cb4ac2b4-a7c2-3ca2-b853-e4a3591c16ce | -11.81 | -50.4999 | 2026-09-29 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 7a6b8b79-4c46-3dc8-8f25-e1515963be66 | -9.4531 | -41.833 | 2026-09-29 18:10:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 89.4 |
| b218e653-519c-3d14-b1c6-8249bd3a09f2 | -10.2065 | -50.0113 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 575b0a60-ce15-360a-bec0-e0b00b688aad | -11.699 | -43.4416 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 32697bc0-f0d5-3162-bdc3-ee1f80ae968e | -11.5818 | -50.5047 | 2026-09-29 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a9be0360-fa86-35cb-a2f5-992c22cef5c5 | -11.8989 | -50.9169 | 2026-09-29 18:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 3bab3a72-a248-3c1a-8568-3d846bc330f5 | -9.9956 | -50.2675 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| ce6173e1-a5cf-3e3d-ba53-1d34757f6aac | -11.2566 | -43.5331 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 54c54e4c-2b7b-337d-b715-2a67e31ff1bf | -11.3922 | -43.4417 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 98b602bd-37e3-3b20-acac-ca36aa446239 | -15.4533 | -41.4653 | 2026-09-29 18:10:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.5 |
| 5c023cc7-b44f-3310-89fa-a9153622b25f | -10.9538 | -50.6592 | 2026-09-29 18:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 09442b1d-db99-312b-b292-00b21f1c32b0 | -9.4535 | -41.8088 | 2026-09-29 18:10:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 96.9 |
| ccc48c77-a92a-3d4e-9ad4-92919d6e0338 | -11.5628 | -50.5069 | 2026-09-29 18:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 2e0860a2-0760-3e7f-9ac7-00b1c5382a87 | -0.4889 | -49.1327 | 2026-09-29 18:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 73c08506-f9bb-331c-9d7e-05cf240d73de | -0.5073 | -49.1326 | 2026-09-29 18:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4022565b-1766-367c-a044-d46e34517655 | -10.1878 | -49.9918 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d616899b-893d-3a43-af2f-4111f2e3c19f | -11.0241 | -49.7088 | 2026-09-29 18:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| c464ca1e-f892-38c0-9710-a5cf80ace0ff | -9.0969 | -49.9049 | 2026-09-29 18:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 045fb572-e252-3e4f-a2f9-9f928842b431 | -11.4495 | -43.4566 | 2026-09-29 18:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| cdedb0d0-5338-34e5-8e6e-0dd2eb7e7fa1 | -10.207 | -49.9684 | 2026-09-29 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 01493a61-dc7b-3fd9-95b4-3869beac4bfe | -10.8851 | -50.1539 | 2026-09-29 18:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 159.0 |
| a35b8684-c7e9-3b99-8524-71070dec7036 | -11.42 | -43.48 | 2026-09-29 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b5e536e-2bf7-38b1-aaa7-87ac58a30ce0 | -11.15 | -44.75 | 2026-09-29 18:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 487768f5-d38b-3c74-87d3-a593c2a5e1ac | -12.78 | -50.68 | 2026-09-29 18:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a5edb6fb-6435-37cb-9a2e-72c13ca572c5 | -11.42 | -43.43 | 2026-09-29 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8c42a44-4079-3b88-8faf-d0b3ca3ff07e | -19.45 | -47.95 | 2026-09-29 18:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c1222fc-f1ae-3b0f-bf1e-579d0943e162 | -5.52 | -39.84 | 2026-09-29 18:15:00 | MSG-03 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2b137133-bc55-3ef0-9d06-4ea4906a57b3 | -3.41 | -50.94 | 2026-09-29 18:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fa2fc08-adab-33d6-a7ea-99cfc4427df3 | -19.45 | -47.9 | 2026-09-29 18:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7f687675-f900-3945-bdcf-797febf84e5f | -12.78 | -50.62 | 2026-09-29 18:15:00 | MSG-03 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc43ff62-242f-3f09-b13f-58e74404dde7 | -15.22 | -41.43 | 2026-09-29 18:15:00 | MSG-03 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 59609f74-6855-3be9-b621-182a9cd01f68 | -11.16 | -44.8 | 2026-09-29 18:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f64593d5-01f0-30a4-ba98-d6aaae04e9d9 | -19.48 | -47.97 | 2026-09-29 18:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 30dc665b-5f91-3b33-ac49-00b920b05dd3 | -11.19 | -44.8 | 2026-09-29 18:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b4f9aeb-4828-3f92-9741-9f3ae5552102 | -11.13 | -45.93 | 2026-09-29 18:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c637026f-6758-3f18-ae39-572ccc3d5ba1 | -11.45 | -43.44 | 2026-09-29 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2b53dba-bdb2-3c00-9e84-bb1d3dde7dfb | -3.38 | -50.93 | 2026-09-29 18:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c82717ea-709a-32a4-8903-bc80ef50f425 | -14.12 | -46.32 | 2026-09-29 18:15:00 | MSG-03 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f89c358-64f5-3f4c-8e9c-98f35a79137f | -11.45 | -43.49 | 2026-09-29 18:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff4842b3-e9bf-35aa-87e1-e5a2f97d8c4a | -11.18 | -44.76 | 2026-09-29 18:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 778724f4-7d01-39bb-bd76-3cca19c2f399 | -19.48 | -47.91 | 2026-09-29 18:15:00 | MSG-03 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4986885-639b-3eaa-850b-2758c7c35b17 | -13.38 | -46.83 | 2026-09-29 18:15:00 | MSG-03 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3b663744-b525-3fac-acaa-3bebdfeb5156 | -8.9633 | -44.1655 | 2026-09-29 18:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 87060980-8595-32b4-9f62-4c99a2cf89f1 | -13.3646 | -43.9929 | 2026-09-29 18:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 467a06d9-08f5-3127-91b1-719bd32cd574 | -12.4351 | -44.1497 | 2026-09-29 18:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 759415f1-a9b8-3725-9084-00a4b34507a0 | -10.9154 | -50.7059 | 2026-09-29 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| f5e49afd-ce1b-35b5-bb6e-95aef9b89d68 | -11.1815 | -50.6347 | 2026-09-29 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 13ee96af-4c55-3948-b089-f665b1f571e0 | -11.6404 | -43.4981 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 12a1da30-369e-3ec1-811a-2921706a8eae | -8.9823 | -44.1633 | 2026-09-29 18:20:00 | GOES-19 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d9b0bce7-ed29-345c-a5cc-850176df72ea | -10.934 | -50.7252 | 2026-09-29 18:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 1c374339-e870-3260-a254-63f54bd15153 | -11.2758 | -43.5303 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 76b9537b-9ffb-38f7-b08f-370c3513d017 | -10.8851 | -50.1539 | 2026-09-29 18:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 265.0 |
| 14633608-a05c-3d29-8e09-a481334ea596 | -11.7178 | -43.4623 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| f6ea78d0-580c-3f69-93ef-c9de13e43b98 | -0.4889 | -49.1327 | 2026-09-29 18:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| a40bd1b8-0367-35a4-87ff-4269b12d47cb | -9.0652 | -45.0062 | 2026-09-29 18:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 02cbad9d-0ec7-322c-bc0a-9bfea5c0b6fe | -11.7135 | -50.5966 | 2026-09-29 18:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| d28cd9f7-f572-3238-924f-5e2aa5de57f3 | -10.1051 | -43.9306 | 2026-09-29 18:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 9b188693-6f6d-3e23-b14d-4bf4cd2dd26a | -7.8047 | -73.006 | 2026-09-29 18:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 215.8 |
| eaa48aab-482b-37cc-81af-3be21b9cf2c2 | -15.1986 | -41.4228 | 2026-09-29 18:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 147.5 |
| 1d027777-94c3-3fb9-8b16-d3cb7442437f | -11.449 | -43.4803 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c4b0bc0f-4e5f-3200-b591-f6d3d27e03c1 | -10.1878 | -49.9918 | 2026-09-29 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| a06f9176-987f-3fb9-ba32-ca5b1d9bf90a | -11.6986 | -43.4654 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| f689cb98-4025-363d-aeda-01f0bae74de4 | -1.4303 | -48.9102 | 2026-09-29 18:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 7f22e572-54ac-3a6f-a0fe-13baf3514137 | -10.9066 | -43.8669 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| e67c5f75-4032-3a6b-acaf-3cee77f67dac | -11.4311 | -43.4121 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| f4bf474d-68cf-3471-a924-9cf941731816 | -11.8132 | -49.0519 | 2026-09-29 18:20:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 7fc057ac-f9eb-337e-81bb-f1ed24120b16 | -11.2566 | -43.5331 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| d0092d56-562d-3134-8c23-0259af9e41ef | -8.8548 | -49.7345 | 2026-09-29 18:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| ed22ebed-5542-3e4a-ad34-4f398179777f | -8.3759 | -72.6192 | 2026-09-29 18:20:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 124.5 |
| aa789eb9-6d0f-3b72-b07e-0bace93f0147 | -11.4495 | -43.4566 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 0b32cb0a-f1ea-3a58-8af5-c40e0921d793 | -10.207 | -49.9684 | 2026-09-29 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5c97c93b-6c67-3650-aa7a-569f02ca6e0a | -10.7056 | -50.8341 | 2026-09-29 18:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 1e7c3f88-3922-3e75-b073-3cfab263fc9d | -9.9595 | -50.1431 | 2026-09-29 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| fb2a2c1e-bd3b-3378-9401-d04155aa324e | -11.6596 | -43.4951 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 609a8218-fa89-3760-a524-c93e17c65000 | -11.1273 | -43.2687 | 2026-09-29 18:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 175.7 |
| 101c01bc-5964-341e-b136-a365c9283078 | -10.2067 | -49.9898 | 2026-09-29 18:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 05a8533b-ef85-3d90-a0e2-3457d8f716ce | -11.8167 | -43.3044 | 2026-09-29 18:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 306.4 |


[Clique aqui para ver as próximas entradas](README100.md)
