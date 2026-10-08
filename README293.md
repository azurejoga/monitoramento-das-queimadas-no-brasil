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

## Dados Diários - Página 293

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6eec6291-bdf7-3dd5-a0c6-8be182300d83 | -5.13284 | -46.0262 | 2026-10-08 16:20:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b9d104e6-5dd3-38ee-a646-bbbc631614eb | -5.94393 | -45.69211 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38188ded-0bb7-313e-b99d-ca5e9fd81a79 | -6.33219 | -44.43645 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 522aaf48-a599-34fe-b866-7067fb692f05 | -6.16802 | -52.65977 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 4ef43796-42a5-3bbf-b8f4-d73700303e81 | -4.38057 | -43.36628 | 2026-10-08 16:20:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2d0a499b-3949-3b71-b3aa-6f46fe6b6bd8 | -3.93087 | -38.62756 | 2026-10-08 16:20:00 | NPP-375 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1e5bf93c-9bcd-3cdd-adfe-76d46dbec4ee | -6.58765 | -41.54992 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 737fcd1a-e45e-30da-949e-3ec39b88b334 | -7.04785 | -45.43414 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ee0f1507-5621-3c8c-8ea0-b81575151ba3 | -7.29044 | -46.15838 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb277447-b7c8-34be-a56a-81fef906a65d | -7.76011 | -43.83461 | 2026-10-08 16:20:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eec70d00-8146-3558-bdef-00f69be60ecc | -7.63599 | -44.38209 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8351e6cb-6ab6-3ccf-88c5-c065aa6daf62 | -3.7897 | -41.67763 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| e0aeb4cb-0b75-3b20-9231-8ad215e02b23 | -3.90283 | -44.13753 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c39bad8e-86ca-3dde-974b-fe5d3be73760 | -4.0856 | -44.12907 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 676ab87e-93dc-3fd9-a206-acbcd10a0e30 | -5.70545 | -53.46582 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 1721a423-2ae2-36de-9758-0e5c6eb41f42 | -6.18522 | -44.11096 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 760b5a10-1b41-3ba1-b1d6-68054ebbc334 | -6.05131 | -42.59179 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 532fd578-5528-3c0a-8c9b-eef9585f4096 | -5.78432 | -45.38335 | 2026-10-08 16:20:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f7ba91cb-2e55-306d-98a1-7ab5ff5c7c3e | -6.05556 | -42.59543 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 49f9dccd-2c37-3d31-8891-92d678c24b16 | -8.18929 | -46.36794 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 16e78c55-a7e2-3491-9b87-6f1d80eceb8b | -7.03709 | -45.45295 | 2026-10-08 16:20:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 19c51b0a-c719-37dd-a617-dfbfa6d01950 | -3.09117 | -53.95605 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f4848e87-f721-387f-8892-927c5856054c | -6.13012 | -53.0625 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2616c432-51c4-33a5-8973-e5ca60f1c612 | -6.49423 | -39.95297 | 2026-10-08 16:20:00 | NPP-375 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c5407836-0f38-3638-a880-6f189c1397c4 | -3.671 | -44.81318 | 2026-10-08 16:20:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac375ee4-f0ff-31c9-a11f-3cc35195feb6 | -6.15244 | -51.70087 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7bea57e-bf46-347a-8c8e-100d23f4b3d0 | -5.76465 | -42.06419 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 829ec70f-2ac3-3653-8969-09d5f46f203a | -5.51315 | -37.49135 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 2b2b0ebc-8bcc-3187-ac2b-68ad1e4683be | -7.61127 | -44.81065 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b659537d-3e04-3a83-8043-f262b97ffe77 | -2.7536 | -54.1161 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1a614c89-3bdf-3126-9510-e54bd03194fb | -1.63761 | -47.3654 | 2026-10-08 16:20:00 | NPP-375 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 39062d8e-dc4b-3eca-973c-3220c18d052a | -7.22089 | -44.28508 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c347ca62-192d-3435-92c9-3fe76f107b8f | -1.22941 | -49.33587 | 2026-10-08 16:20:00 | NPP-375 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 76e4532a-23c9-348b-b079-54476aa82ca7 | -6.32765 | -46.55806 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5cecebc9-0c7c-3a79-ac90-3c32eef06782 | -5.21361 | -44.63092 | 2026-10-08 16:20:00 | NPP-375 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7791e211-ca7d-3188-8dab-424840587ee2 | -2.98964 | -54.09118 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 795591c7-764d-376b-8b42-116ff1b0fe62 | -4.74954 | -40.50548 | 2026-10-08 16:20:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 21be154a-e428-37a4-a5b5-3e5b5d534199 | -7.1898 | -52.61499 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 867d1c60-a490-342a-b579-a1794744f901 | -6.3217 | -43.49082 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f07be6bc-fb93-3c7c-bcf2-88c551ebf48b | -5.29411 | -42.7569 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fe5e17c5-2f33-360c-ac42-63ed79780a2a | -6.85159 | -41.74952 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 8c1c6e86-a007-38bb-b8e1-d211efa6bb35 | -2.73798 | -54.11068 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a65f029e-b84e-363f-898e-25ae8a0d120a | -7.57739 | -46.20379 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 49b62f06-521e-3efc-93fb-b297f8e40141 | -6.97252 | -47.67157 | 2026-10-08 16:20:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| a4a6ff6d-5abd-35ee-99cf-31fee0e2ba41 | -5.84781 | -42.67517 | 2026-10-08 16:20:00 | NPP-375 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 3ded5a15-9820-38ce-a83e-231a9e35fded | -5.27873 | -47.91318 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 68d8fbd3-dcf4-3177-8b8b-7e581fa0b5f6 | -7.31646 | -43.99884 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c2ffb4e-bae6-3e44-8878-642cc07c3486 | -6.63767 | -44.88546 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5351ae20-1a6f-31b7-bd30-869d87f1abee | -7.19146 | -44.31183 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7d0c6bbf-bda7-361f-9392-8a98f7da36e7 | -7.84382 | -45.50602 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5da32d51-98b3-3744-a668-c1d4a0526ebe | -3.89312 | -41.60241 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 59cceeba-4c6f-3fff-82fb-76f094613331 | -2.84637 | -54.12628 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 003863c5-6017-38d4-9c26-daf5361ee945 | -5.39206 | -45.64595 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f10ad4f-e52f-32c1-af2d-8774a3d372ce | -6.78763 | -45.0604 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 29424ceb-abe9-36f4-8fd9-d6bfe9e443f0 | -4.5108 | -43.79555 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c04ab1a7-395b-3fb9-b830-26184e5e28e9 | -7.7075 | -45.45658 | 2026-10-08 16:20:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 11eb9b2b-faa2-389c-ace3-c3c8b2908ec5 | -6.83697 | -39.55981 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cffc31eb-42d0-3e64-82de-45d29527dd67 | -3.34409 | -42.49241 | 2026-10-08 16:20:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| e3081560-f9bb-34d4-af15-49503d3b9098 | -7.53984 | -42.09136 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| caa1acf1-a5b1-3c14-a079-8a2a151b3740 | -5.9848 | -40.92469 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d1df0ccf-1926-3e30-832b-2953cdafde2a | -6.1078 | -38.16851 | 2026-10-08 16:20:00 | NPP-375 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 391affda-a0eb-35c8-ba65-793e3f899afe | -5.47915 | -45.63399 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d9fdf5fc-a908-364e-8efa-ca709c6398d1 | -6.19377 | -45.40954 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e33457c-d631-33bc-9540-45bfb77b3d6c | -6.15347 | -39.42331 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c7a1c08b-6553-3042-9609-1e75d7c7fcd7 | -6.15437 | -47.93092 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 862abf2b-67b2-32c6-828e-fd466061753a | -4.36358 | -40.409 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a7bb23ca-955b-3017-a6c2-f004157629fc | -5.17586 | -42.6847 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9e38f4ce-0b54-3f3a-b1ca-a5047047f29a | -6.38866 | -42.53518 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6e6559ca-c466-3460-963f-427b63bcd57c | -6.23893 | -52.67463 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f1529916-f3c6-3ce8-b77a-1a74e4b25ab5 | -4.7462 | -40.50597 | 2026-10-08 16:20:00 | NPP-375 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| d4eed943-478d-39bb-b2d2-04b127747658 | -4.31949 | -41.23621 | 2026-10-08 16:20:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 83a9c549-ef85-3bc5-95e7-cc4a35ef8440 | -4.36744 | -40.41198 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d67834fb-6b7d-3db4-9610-a5361626db34 | -7.53685 | -42.09602 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 77207600-f898-3e54-a965-0478362acb89 | -7.59817 | -42.38338 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 9f1a8ca4-36fa-3a49-a107-fa65038f7419 | -5.69739 | -53.46658 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b6bbbc4c-4744-3c41-8814-aa16e2175c6b | -7.04386 | -43.82156 | 2026-10-08 16:20:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87ddfe54-2619-3656-8222-8e58220894a5 | -1.39969 | -48.94087 | 2026-10-08 16:20:00 | NPP-375 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcce3055-be1e-329d-be31-bee25df92783 | -8.35232 | -47.66896 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b936ed3e-dcd6-3026-849a-8de33ed17396 | -5.51138 | -42.84362 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| a49d3603-35cb-3d46-8780-4c4f8bafad87 | -6.22952 | -44.97721 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93e5d82d-a7ec-3826-9cf8-78671f989c7e | -6.32625 | -46.54822 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 706c5a40-1327-3d91-ad60-4eaec9cf89ba | -6.22147 | -44.83516 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8cb3bbe-8e70-3967-8be6-ca0824a31503 | -4.20342 | -41.7626 | 2026-10-08 16:20:00 | NPP-375 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8924f839-b208-342b-8088-dc98a74a50b1 | -6.85452 | -41.7451 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| bfe63478-2ee5-3f1f-89c9-f902a2804dc7 | -5.44167 | -45.68179 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0435ab39-e31c-3611-bfa2-07de63f26c89 | -7.05354 | -44.33438 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b8acade-96ac-3541-a20a-539e379d61f6 | -7.35504 | -43.18809 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2671a094-7bc3-35f8-97f3-be0b0ae42930 | -5.24702 | -37.57938 | 2026-10-08 16:20:00 | NPP-375 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 14.4 |
| be0e9b86-85d7-370a-80d4-84b75159d60e | -7.85993 | -44.22094 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 46201caf-dbdd-3370-8f25-e2a21cae9ce7 | -6.07581 | -43.8791 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9214e752-426d-3e13-8d08-cf1bca37f807 | -3.50321 | -44.27102 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b7599daa-2577-3f58-9ab2-6fe91235e0b7 | -3.7812 | -41.66767 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 29ae1d3a-417a-36a4-baa5-20a06d262253 | -5.75524 | -42.07367 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| e2d27487-d557-3727-984f-af0535a54756 | -8.56292 | -50.1897 | 2026-10-08 16:20:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| f2249b6c-4fe3-3e05-8926-8453b41448c3 | -4.15708 | -43.19527 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4a303a69-e162-31d1-a70e-da4c6e498d14 | -6.1515 | -52.64194 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 0562fca9-7ed1-32c4-84a8-5b332cc3c454 | -2.49397 | -49.10596 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8c8a17ee-a82e-362b-8fe2-ff943e5267c8 | -7.07052 | -45.37123 | 2026-10-08 16:20:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a5d869f9-1da3-35a8-a676-999d1c8f3bea | -5.1687 | -42.89008 | 2026-10-08 16:20:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 70bc0994-c394-30e6-adc9-fe74464078fb | -6.81539 | -45.0491 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |


[Clique aqui para ver as próximas entradas](README294.md)
