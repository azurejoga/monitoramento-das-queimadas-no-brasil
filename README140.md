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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76c2ddc0-e17d-3d38-958c-fb51adcffc7f | -8.6114 | -55.2376 | 2026-09-20 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 79d29ef0-9bf2-31e2-a11d-ba926a728094 | -6.4587 | -58.1373 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 8dee905b-601a-33f0-8df2-56cd9f9bbc31 | -11.4732 | -45.3635 | 2026-09-20 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 0c092648-7f2e-3901-8d98-f97de45b54cf | -11.4537 | -45.3892 | 2026-09-20 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 3a2b4490-7457-3744-9197-4106feb9c382 | -11.1222 | -49.4818 | 2026-09-20 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 28541e0a-7efc-3227-8a4d-c818133c0bc1 | -8.3581 | -47.2378 | 2026-09-20 15:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3ab49db7-2efe-38c9-bb58-8ad6693d2bab | -10.8364 | -50.9479 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 232.6 |
| a778558d-ae56-3b2b-936f-7e3e17cb11c3 | -10.8732 | -53.9874 | 2026-09-20 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| b0a218c7-c1a4-3413-8f79-e7a14f311802 | -11.0353 | -47.6756 | 2026-09-20 15:40:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 21edac48-fe82-3b3e-a306-85b8f3d1d9ca | -11.4541 | -45.3662 | 2026-09-20 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 355b0aab-5de1-39b1-b9fd-4b6537d18964 | -11.0614 | -49.7477 | 2026-09-20 15:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 235.8 |
| d93ef1b0-e077-3a6a-adf5-1cbe66c99cf6 | -6.5829 | -58.9851 | 2026-09-20 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3732f442-2730-379b-8833-2bd66e435591 | -2.9997 | -60.8047 | 2026-09-20 15:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fdd31e4a-b3bc-3226-b25d-7c83deb850e8 | -10.8367 | -50.9266 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 200.5 |
| ccb68768-5070-3921-80ff-2a9dedbd0764 | -7.2519 | -55.5994 | 2026-09-20 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| cd5c9c8e-4604-3e8a-acb6-5069225b2ed8 | -3.6946 | -60.5835 | 2026-09-20 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 336.5 |
| edeaa3b4-ecf1-30f6-9447-03154085f3ac | -9.8136 | -48.3218 | 2026-09-20 15:40:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 35fc3157-3c62-3bb3-89f8-49aed8fcde15 | -10.41 | -48.933 | 2026-09-20 15:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cb1e39b1-7d8c-34eb-9fcc-74033df5fd1c | -11.0065 | -48.3187 | 2026-09-20 15:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| ca28f91b-817c-3ff8-99aa-867b49fae54d | -1.7316 | -54.9319 | 2026-09-20 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3cc734c6-b326-30ed-8b7a-1a3946cb91e3 | -2.9326 | -58.3397 | 2026-09-20 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 25aea4bc-dc76-3d3f-9ad9-6cd18e49a665 | -3.5894 | -59.0581 | 2026-09-20 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0e06352b-51d3-3eb6-90ee-10710eb099b5 | -10.9301 | -53.9618 | 2026-09-20 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 72db5063-2cee-3085-b402-b09a30d2eb4e | -10.7423 | -50.9152 | 2026-09-20 15:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0534d5f5-2890-3b4d-b8af-2dad29b825a5 | -9.6668 | -54.3129 | 2026-09-20 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e6c1dc6e-f6e0-3c4b-a73f-ddb17243efcb | -2.8962 | -58.2825 | 2026-09-20 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 334db9bc-ae93-3907-ba61-f424dacec9a6 | -10.8735 | -53.9668 | 2026-09-20 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| f79ff979-3f1e-304f-9544-847530425c33 | -6.6217 | -55.6917 | 2026-09-20 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b3a967b5-9eeb-3600-958a-4ff373976b35 | -10.7842 | -50.6133 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e2cfe65b-71bf-311e-9fc6-ae401ed28523 | -10.8665 | -56.2377 | 2026-09-20 15:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ce294e90-455e-384d-bc0b-01251e403d2d | -11.4549 | -45.3202 | 2026-09-20 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| db04374c-a589-3eb5-9770-b0eba744b9d0 | -10.279 | -50.2391 | 2026-09-20 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 28fdb2e0-3523-3cc4-b82d-f9012e1840f4 | -11.0259 | -48.2944 | 2026-09-20 15:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f431578d-9ec6-3438-ad9a-7b0dfb532ba8 | -10.2787 | -50.2605 | 2026-09-20 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 12c47eba-6b22-3d02-a03d-46ae44605c9e | -3.4429 | -59.0804 | 2026-09-20 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 88a4b9ca-c492-39bc-84bf-e2ee4031eea2 | -6.4942 | -58.369 | 2026-09-20 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d7195623-1a47-3cf2-a3dc-5be6317b7bb1 | -2.8974 | -57.7987 | 2026-09-20 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 7210d0bc-daaa-39b9-8edf-84675ed58703 | -6.1981 | -55.4534 | 2026-09-20 15:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b1618632-e7c0-3488-afe3-293363aa7044 | -10.8177 | -50.9286 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| c80725c9-fc24-30b9-b496-c41ef07c0282 | -3.3367 | -57.8479 | 2026-09-20 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0185f7b5-e254-3e4b-b2a0-04080780c584 | 2.2187 | -50.8977 | 2026-09-20 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1866d229-adce-37e8-a710-d5ce0f25a715 | -2.8962 | -58.2825 | 2026-09-20 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| f51df100-7b41-3f79-8cae-f9dc58fa257c | -2.8975 | -57.7793 | 2026-09-20 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 077567cf-030e-3ca2-8257-6c923aeaeccb | -2.9709 | -57.7197 | 2026-09-20 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9599a646-0edf-3813-a485-0596ae64f51d | -3.1079 | -61.408 | 2026-09-20 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 66159f9f-8c85-34c7-abc4-554d0121e2ca | -6.1109 | -57.684 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 6f54e478-4509-3431-b714-cd0e4331137c | -6.8031 | -59.1886 | 2026-09-20 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e88c18ee-f248-3392-ab8d-d20d8fd702e6 | -3.2817 | -57.8685 | 2026-09-20 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 34232f39-8bbd-35b1-8d0a-fe7fcf43c7d2 | -10.2793 | -50.2177 | 2026-09-20 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| cfbd76b7-7857-3cf5-a54a-9295ff487160 | -3.331 | -59.8292 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bd63deb7-eaff-3328-aabd-241be5b506e0 | 2.1082 | -50.8792 | 2026-09-20 15:50:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 80d6bfaa-d5ff-3061-a53b-21b373c5adac | -3.2955 | -59.4476 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d1fa5cab-bc63-3c12-baa6-b5dfbefdf7f0 | -2.8009 | -59.8957 | 2026-09-20 15:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| bdf1d816-16cf-3931-b574-164b9abcbf65 | -5.7431 | -57.5814 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 665dd579-9c34-3128-968d-da3c9209f7f4 | -1.5858 | -54.4552 | 2026-09-20 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9e8d7fa6-1a14-3470-b96a-8752b443a302 | -8.1686 | -54.7634 | 2026-09-20 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 267.8 |
| 896fb46f-d1ac-34a0-807f-2acdcaed24db | -3.7347 | -59.4194 | 2026-09-20 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 39b302f1-d62a-3a99-b563-abde7ae02033 | -3.3358 | -58.1384 | 2026-09-20 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 110c2aec-c33e-3839-9500-d6e29d0b6599 | -3.3494 | -59.7906 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 90c0d2a2-535b-36a6-923b-f19fa2aa30fe | -6.0928 | -57.6262 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 9f45318d-f645-376f-8eba-eed1c9c1e4ab | -10.7609 | -50.9345 | 2026-09-20 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 85fbc0e4-edd1-3fe7-9ca3-06487f70e6e3 | -3.5356 | -58.6939 | 2026-09-20 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0e0800ba-8f4d-36fc-9fe7-d608cadab70c | -2.9142 | -58.3787 | 2026-09-20 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 570af938-be7d-315c-be2c-c0ea720d1550 | -9.7504 | -46.0637 | 2026-09-20 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 35b8ecee-4547-3a60-955c-bd302610004a | -6.4587 | -58.1373 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 926d11ab-15ad-3850-8b4e-f90a3b9978c0 | -3.2372 | -60.8007 | 2026-09-20 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4ca25e89-9817-374b-897c-fc17e7067942 | -11.0614 | -49.7477 | 2026-09-20 15:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 3aeb4f25-495d-3f76-ad38-57ef16c4a34d | -6.1981 | -55.4534 | 2026-09-20 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 291387a7-12a8-3b03-8222-293a719f3f2f | -3.5893 | -59.0773 | 2026-09-20 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e6e121ae-8b9b-3bf9-9410-ec9ec69aef50 | -9.2865 | -48.2453 | 2026-09-20 15:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2e624577-91b6-30b8-b156-8ff7d9121e64 | -2.7713 | -57.0229 | 2026-09-20 15:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2b1c7f43-ed44-3b4e-94cc-c1f33d18c7b0 | -11.1222 | -49.4818 | 2026-09-20 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| f61d4488-0a92-3af7-96d1-f6b935e2aaec | -5.9815 | -57.7672 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 68997808-a855-3337-9d58-2475e33e2a5f | -6.8032 | -59.1693 | 2026-09-20 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 495f96f6-e7f5-3152-96b9-692887ba63d9 | -2.8779 | -58.2828 | 2026-09-20 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 12506714-4351-3012-ac6a-a1cb8fe92f4c | -2.9143 | -58.3401 | 2026-09-20 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 183.5 |
| 0e405724-cb89-3eb3-9ec7-7c39e16f3528 | -6.0925 | -57.6847 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6c5b79e8-222f-32f2-b7ac-48b2770a5e82 | -6.1291 | -57.7418 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 351ae34f-cd8e-3686-b50b-7b79c25105d9 | -9.6665 | -54.3332 | 2026-09-20 15:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 48ad895b-f4b2-335d-b150-b78c2c8d3cee | 2.2003 | -50.8773 | 2026-09-20 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 241bcc05-9598-390c-addb-c56e296d2d5c | -11.4541 | -45.3662 | 2026-09-20 15:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 291d0792-2ded-33bc-989b-ad5d9373ec48 | -9.8136 | -48.3218 | 2026-09-20 15:50:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| aa8e1c7d-659e-35fd-8852-110cd93135e5 | -10.2787 | -50.2605 | 2026-09-20 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| af1f760e-099e-36ba-af61-3571f3eb923b | -9.6668 | -54.3129 | 2026-09-20 15:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 654dded8-8d1e-3531-89e2-c8452b4af559 | -10.2748 | -50.5592 | 2026-09-20 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ca3336ae-ff4a-3623-a479-5043c00db748 | -9.2682 | -48.2034 | 2026-09-20 15:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| af2c7fc0-b5cc-328a-ae81-e9962041cd7d | -10.9665 | -49.7583 | 2026-09-20 15:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d2e322e2-e911-330f-87b1-d9dd13f293ea | -7.2519 | -55.5994 | 2026-09-20 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 637eeca9-7ac4-36a2-b90b-71ccec750cf9 | -11.3612 | -51.3374 | 2026-09-20 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 705f1355-024b-337f-84ff-3555f528d2a9 | -3.6449 | -58.8647 | 2026-09-20 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 45f26cfe-f7f6-3aaf-ba73-d4fe9846a367 | -6.3843 | -55.2451 | 2026-09-20 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 64b355c9-9cfa-3ee8-97a1-e71e18453ed9 | -6.1412 | -55.6947 | 2026-09-20 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4cb1224b-4384-3768-a8ef-5b12f85728da | -3.3321 | -59.4469 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 3fbb2629-b18e-3deb-aa4e-57eefe483a90 | -6.1477 | -57.702 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0169a107-f9b0-3061-a579-6fa1c9974a43 | -9.0353 | -48.7704 | 2026-09-20 15:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 98.0 |
| bfc7b97b-4127-3093-a8fe-b0c1c9554156 | -3.2775 | -59.3522 | 2026-09-20 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| cc5584d0-a20a-3c19-a500-de3d987e126c | -10.7466 | -50.5959 | 2026-09-20 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 6baf6b0a-66db-3fd6-a4a0-da27ac32a18b | -5.9814 | -57.7867 | 2026-09-20 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7c361428-4628-352b-95b0-9d61b4aaeeb4 | -6.3195 | -60.0147 | 2026-09-20 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5b77e8ba-066e-3f4a-ad7f-a62935778e54 | -6.8411 | -58.9939 | 2026-09-20 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |


[Clique aqui para ver as próximas entradas](README141.md)
