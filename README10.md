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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac43232a-d333-365b-ac70-57d1e8e81145 | -7.3382 | -44.20959 | 2025-07-17 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd0f4b0a-1250-3ea1-b587-cd756941d79e | -9.30675 | -44.84846 | 2025-07-17 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18dcf746-4a9c-39be-b394-89dfc2777d11 | -8.1109 | -43.15079 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 71996738-f35c-37bb-a3d6-ff5ca02e8eb2 | -4.80555 | -43.23327 | 2025-07-17 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4499af5e-fc2a-36d8-9888-597295ca00a5 | -8.10083 | -43.15285 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 7fa470d3-edb2-3d95-bcc5-c8d5377ede6d | -7.14979 | -46.09373 | 2025-07-17 03:32:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be4290c3-9fc2-323b-ae63-af785d0840d8 | -6.73425 | -44.33346 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c06a0cd1-5a46-3fc1-8bca-3bd134fbccfd | -8.87587 | -44.79772 | 2025-07-17 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93e3ac80-4d7d-336d-b9cc-6d0f02e34fff | -6.72776 | -44.33223 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3182f7e9-58e8-33ac-9953-ed45be819283 | -6.82399 | -43.78719 | 2025-07-17 03:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be222a9e-7bd2-3f7c-ac79-b2063603f0f5 | -5.66722 | -43.72441 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 48c8917e-7f62-3e66-ab62-b8496c919f14 | -5.51535 | -41.32712 | 2025-07-17 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d29e15de-32df-33b8-b43d-28cdeae4866b | -6.87389 | -41.72651 | 2025-07-17 03:32:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0e208b53-bfc4-3fe8-a245-2b0a3cfab8ce | -7.21713 | -35.77714 | 2025-07-17 03:32:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 134660c2-5ac9-396d-a953-c536b31a869f | -6.71696 | -44.32415 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| caaf0d57-1eef-3a65-b33e-0bf568c22c40 | -4.80641 | -43.2283 | 2025-07-17 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60f12263-8023-39dd-bb24-dd5a432db717 | -7.21164 | -45.33264 | 2025-07-17 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75b17114-987d-3832-a66e-38f297f2a97d | -8.38175 | -36.17316 | 2025-07-17 03:32:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4d3e9d25-fb6c-3097-8695-19a78660e79f | -7.05919 | -43.51307 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdde1004-e06e-31d1-a184-0e3d30f11bac | -5.79326 | -45.10865 | 2025-07-17 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 142ffb94-e946-31e8-a3d4-397134aa2520 | -7.05835 | -43.51771 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 870ef32d-8868-3620-a189-e27fca1f3634 | -5.65792 | -43.7296 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| c4cca473-10fa-3570-9152-c56ca2ffce57 | -4.80727 | -43.22329 | 2025-07-17 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21e273b6-0bf9-3117-9c76-e852254220a2 | -6.37789 | -44.7493 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 587f1e22-a94f-3516-a387-b3604de7c4c7 | -6.70399 | -44.32166 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0135e884-7f6f-3964-ab04-9cac99fcdcb7 | -5.79444 | -45.10223 | 2025-07-17 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 100c4ed6-5470-36eb-a0a1-6e23ed05446c | -5.52965 | -43.89132 | 2025-07-17 03:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1642f8c4-efea-3e8b-a4aa-235063cc15dd | -7.23001 | -43.50509 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af62d1b3-379e-39cf-9b92-2c056e991c1d | -7.19384 | -43.12294 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5f278df3-b641-386d-a79c-bbbf027ab762 | -6.8144 | -43.78946 | 2025-07-17 03:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba6ebe0b-e976-39d6-bc32-8cb183307ad0 | -8.87699 | -44.79203 | 2025-07-17 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f1f2f1b-2838-30ce-86cf-61a42a0410ee | -7.18785 | -43.12185 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1634f01a-d71c-3a80-95b4-df647fbb2fa7 | -10.96608 | -46.47792 | 2025-07-17 03:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1c24c96-5b62-365a-ba52-8e5b6157aad0 | -6.85439 | -44.77351 | 2025-07-17 03:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c82b7d7a-184a-3808-b572-df5d047a65ad | -7.89238 | -44.49351 | 2025-07-17 03:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54ec8e45-c3b0-3358-9fa5-e7ea07504c77 | -9.48976 | -40.39784 | 2025-07-17 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b3430e67-f9d9-3b91-81b1-451c970c3943 | -6.46498 | -45.34483 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 951230ed-3ff0-3635-b86c-83be285971b2 | -8.88238 | -44.79863 | 2025-07-17 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d9adb2f-8d39-3f0f-b212-bd71a6722a15 | -6.87307 | -41.72972 | 2025-07-17 03:32:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2013e04a-1645-3ffd-a2b4-2e618989ab71 | -5.78879 | -45.09422 | 2025-07-17 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| def69b6e-6c7d-3f91-8214-3fb7c178a680 | -5.66707 | -43.71507 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 970001a2-75f3-3bc9-8711-96687005aec1 | -5.65984 | -43.72874 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 04a4da9d-cc25-300c-8b45-b63327433f6c | -4.59863 | -43.32309 | 2025-07-17 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8cfff3da-6c22-3d74-85dc-df6501b73c1f | -6.8513 | -44.76917 | 2025-07-17 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2347ae71-cfb8-3559-946c-ae7fca4b0df0 | -6.70829 | -44.32858 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3cc36281-987d-3545-b098-32563d2205fa | -6.72023 | -44.33648 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4f8e1786-6c76-3fe9-8a08-adf4d1785ea1 | -6.84458 | -44.76828 | 2025-07-17 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8889b82b-37cc-371e-8ec4-ee60b782c409 | -6.9973 | -43.74517 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b3e41df-6ec3-399d-8889-8c6e140b92fd | -5.66271 | -43.7132 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 1b55dd20-dfd7-3535-9926-5d67053e51fc | -8.11763 | -43.1476 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 792bdf47-5bfa-30b7-8aaf-c403b9fd74dd | -5.66528 | -43.72519 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 4ba9378f-26eb-375c-904b-6ce0c7e0e7f3 | -8.87595 | -44.79682 | 2025-07-17 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1deef578-e120-3087-96e5-ab03234203b8 | -5.51474 | -41.33063 | 2025-07-17 03:32:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f9c91f8-a036-3ef9-9a17-e5b60fa62156 | -8.11422 | -43.14647 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 542d1c1c-bde5-3752-b414-67e2b610cec6 | -6.45896 | -45.34362 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2ed5f9da-3092-3b9f-88f7-fcc98a08a567 | -6.45773 | -45.35036 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| c30da641-0613-30a7-a718-2fc23aaf7298 | -5.93284 | -43.37177 | 2025-07-17 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ae4875c5-e667-3bcf-a0f1-bc2cec47136f | -6.97289 | -42.81115 | 2025-07-17 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c6265c96-93bd-3e3b-a0f2-a77599055855 | -6.72898 | -44.33189 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4369902e-e209-3035-9769-c9d8ddc91abc | -6.8477 | -44.77249 | 2025-07-17 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a551cf75-a2f4-3665-b9c6-1b77c94726d9 | -8.38154 | -36.17007 | 2025-07-17 03:32:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 294be63b-c934-3c65-a744-bd900a7f9190 | -6.73324 | -44.33881 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05a1b5a9-e8e8-3ec5-8284-4323fce8424f | -7.04967 | -43.53031 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d7d25b-128c-3fae-9fcb-4082de6854f7 | -6.82786 | -43.78679 | 2025-07-17 03:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f97c81e0-7033-33c8-b25e-45296e543885 | -6.728 | -44.33728 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1da58e9b-03cf-392e-aa31-ae7274630f1b | -7.20487 | -45.33103 | 2025-07-17 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcd7d58e-ff63-3c85-aa51-e401895fdd08 | -11.66405 | -43.76812 | 2025-07-17 03:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1327c787-abff-36f0-b0d1-42c6600037b0 | -9.49122 | -40.39634 | 2025-07-17 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 56a50cfa-f805-3a22-a7ca-e43c1d514f04 | -8.11343 | -43.15078 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 91dc74f0-7427-3cc6-b699-eb3af016fb27 | -6.99641 | -43.75002 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d866d53a-6daf-354d-8f37-e23f6b389b6c | -9.30713 | -44.85013 | 2025-07-17 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc05c3fc-0775-3256-8de8-d66dc93b1dbb | -8.09493 | -43.15171 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 507dafd4-770c-3c4f-8370-d1695b2eb72f | -5.65435 | -43.71269 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee9e115c-db24-3344-b623-b07060ec22b7 | -8.12012 | -43.14759 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37bb1be8-f5c2-35f6-8106-04b3611022f1 | -5.66816 | -43.71927 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 0ac04667-a29f-3da3-99ec-d6453629400a | -6.70932 | -44.3232 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| add07c00-6c0f-330e-b61d-ddd5a2941aaf | -7.05581 | -43.53154 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f44ea79-5f96-3936-89e1-ae7052373b18 | -11.67045 | -43.76662 | 2025-07-17 03:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa37b1b9-ac33-36b0-b333-1f501a343e63 | -6.73449 | -44.33849 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d58092e-5d63-3866-ae98-a9646fe99012 | -12.47611 | -46.92482 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b758de77-fa75-34ff-8d42-23916196c891 | -12.70002 | -46.81091 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2049421-0ac6-38ae-b650-c5078eb69e8b | -12.49637 | -46.92979 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56da304b-8c3a-3c23-837d-f1e478761700 | -12.02778 | -47.77882 | 2025-07-17 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 826ac054-c97f-3cf3-a1d8-ce864429ed56 | -12.027 | -47.78074 | 2025-07-17 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 90cfe268-2909-33c5-a0a4-dd38e3f91277 | -13.00309 | -44.87376 | 2025-07-17 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 06b9ce21-35ac-34f1-8ccf-ce2985b7688d | -12.47206 | -44.50232 | 2025-07-17 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a904283-3a9d-3f5b-9e3d-f787b63e99f3 | -12.47801 | -44.50355 | 2025-07-17 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dafd0254-93d5-3710-9599-b1f8fa0abd19 | -12.03426 | -47.78216 | 2025-07-17 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b659645-fd1b-3b92-91dc-17aef1a8f8ca | -12.71493 | -46.80751 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2cae85f-87df-35a3-86ed-d55f5d291398 | -12.49115 | -46.92141 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 231740d9-5400-3a57-ad2d-364f2b123b5f | -12.99806 | -44.8676 | 2025-07-17 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c58eee7-bbdd-32ee-8abb-c9f3fb7d724d | -18.84986 | -45.20953 | 2025-07-17 03:34:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ada5cba9-f599-3550-a466-62b0026543c1 | -15.93204 | -43.52344 | 2025-07-17 03:34:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a43ecb6-bd88-3c7f-9257-39247f82af2e | -12.70681 | -46.81239 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 567391bc-0d82-3155-a617-d281e6f2486a | -12.19615 | -43.46795 | 2025-07-17 03:34:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e6deb50-7de0-364b-866a-86f3d5ee0a92 | -12.02627 | -47.78573 | 2025-07-17 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 65d0ea43-927e-319f-aeba-fc9ac522c2cd | -17.0453 | -43.77626 | 2025-07-17 03:34:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84759e00-2d01-35fd-a211-6ff6d1bdb02d | -12.47892 | -44.49913 | 2025-07-17 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6da77d28-9ed1-3af4-b655-6358b540de25 | -12.7136 | -46.81379 | 2025-07-17 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40311367-9dec-34f5-b4fd-6c04d533bbd3 | -14.52088 | -47.67664 | 2025-07-17 03:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README11.md)
