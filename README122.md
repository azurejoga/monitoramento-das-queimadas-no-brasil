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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ab9459b-52d2-3357-b3b2-13380934ef50 | -17.5795 | -44.9765 | 2026-09-20 13:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 6ea8fef6-2423-3861-b965-472cc5dd7cd2 | -10.3914 | -48.9133 | 2026-09-20 13:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| feb1aaee-963e-3b9e-9761-4a1357d9fcec | -9.26 | -45.9616 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 2a016cdb-052f-382d-97ec-1a6eb4d5c720 | -9.5539 | -46.5807 | 2026-09-20 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0d37c20b-e914-343c-87d7-dfa013ad20bb | -11.0256 | -48.3164 | 2026-09-20 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3c7a9137-0b68-356f-81c1-5c1869c0eb75 | -12.9084 | -51.01 | 2026-09-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 7ea6c3da-1020-3800-bf02-13f5f7785030 | -12.0069 | -50.0686 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| f392a2f7-de7a-3ffb-af87-e1e0d2df23f9 | -7.3259 | -55.6153 | 2026-09-20 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 43801636-7864-3ead-9e2a-80e1747dd792 | -10.7708 | -46.3453 | 2026-09-20 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.2 |
| c2d94307-8ae4-3638-964b-fee3e0c04c44 | -9.2374 | -46.2344 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 2fd963f4-bd32-38cf-a62b-4d7707901476 | -11.4905 | -47.7736 | 2026-09-20 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 67d70e56-b6b7-3cfd-8326-e7c8da08a34a | -10.8367 | -50.9266 | 2026-09-20 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 334e5295-b587-36ab-97fe-4fda69411427 | -10.7708 | -46.3453 | 2026-09-20 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| f78e917f-6914-33de-8333-f44708976870 | -8.9752 | -44.6722 | 2026-09-20 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 24c09c8a-2cb7-35c8-a94f-2dffdd9ba008 | -8.0689 | -46.2645 | 2026-09-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8086f819-aa8e-3eb8-aa53-24ae63f4bc7c | -8.2499 | -61.3724 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 9c246ff6-5b6d-317f-a3aa-d6c90888ab2e | -3.3493 | -59.8288 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9ffe5422-277b-3780-b5f4-303f20826b24 | -12.2344 | -50.1488 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 285.9 |
| 2bfd4ca1-94c3-39e9-b5db-e9148a0f3241 | -11.3813 | -44.0554 | 2026-09-20 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 90b411c3-f1d7-3e7b-b4d0-05a93e47ddd8 | -10.6694 | -50.7103 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5b019b6b-82d3-3203-a366-ca1c85500151 | -10.4673 | -45.0873 | 2026-09-20 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| eb097590-486e-3f76-aa79-8efa48c6444e | -12.1524 | -47.0158 | 2026-09-20 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| dcc16238-2c5b-3623-8cd5-6b38408a2297 | -8.8636 | -45.9596 | 2026-09-20 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6d710253-42a2-3213-904b-9b2db25bad99 | -11.0259 | -48.2944 | 2026-09-20 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3bbf2569-5618-31f5-a72b-a5576af022d5 | -11.3787 | -51.4412 | 2026-09-20 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 1f9777a2-d9a1-3d14-abdb-8a42a13b6825 | -10.6703 | -50.6465 | 2026-09-20 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| e2ebe94c-48ae-3a0f-8296-5d541858a30b | -3.3367 | -57.8673 | 2026-09-20 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 78e2c621-1459-3d48-bc8d-9cad3f289459 | -11.0506 | -54.9309 | 2026-09-20 14:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 228.5 |
| d2b5680a-0997-330a-aeaa-5cf608ebfb12 | -7.6314 | -46.7507 | 2026-09-20 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| f7290fb4-ce9a-35db-a8f1-d003dd6fe365 | -14.6861 | -46.6657 | 2026-09-20 14:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b10bd93c-dfc3-3508-b57d-a00fd85cedcf | -10.8735 | -53.9668 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d1e7f1ea-6691-36cc-9025-a90007cf11df | -11.3603 | -51.4009 | 2026-09-20 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| de1644e8-31f0-3bdf-8c3f-ba5ed772a7b3 | -11.4905 | -47.7736 | 2026-09-20 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1d0b05d7-ada0-335a-88de-f04a90954853 | -8.05 | -46.2663 | 2026-09-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2bd9068a-ce00-3016-87e5-b3920ce9eba0 | -10.67 | -50.6678 | 2026-09-20 14:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| eeadfb5d-de09-397c-8fdc-51f0b23a20a9 | -7.0455 | -43.6928 | 2026-09-20 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e6949404-85b3-3001-863f-25329de902ce | -3.6946 | -60.6025 | 2026-09-20 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 6310aa04-35e5-3037-a6a0-b3437651d80b | -10.2787 | -50.2605 | 2026-09-20 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| f925372d-0834-3236-83f5-7377e513ad88 | -12.8701 | -51.0148 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 73c62798-b5d7-396d-b78d-2679e3131c1b | -2.8974 | -57.7987 | 2026-09-20 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a2944baa-464e-3dcc-8856-dd3b7056276d | -9.2606 | -45.9164 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 796808a9-0442-3eae-83d0-28b49fa870c5 | -12.8896 | -50.991 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 7a26c386-3ccb-3bed-bd23-027e7f1887df | -5.8411 | -53.5002 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 37e9ef94-6c79-3e9f-96e2-564b1bc74c10 | -12.6423 | -50.9144 | 2026-09-20 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 0c49ff13-db59-3232-ac60-ad926a41ae49 | -10.41 | -48.933 | 2026-09-20 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f88d6c0f-73b4-30f1-93ea-5ca66645e4be | -6.3199 | -59.9381 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 1592be62-8549-3f29-b6b0-5c476d8fa4af | -11.0596 | -54.1755 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8c061d0d-244f-3a25-a05b-9cb2ec63d537 | -3.3 | -57.8681 | 2026-09-20 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 5c74beae-a36a-3bdc-9174-9d535253063e | -7.9639 | -44.0435 | 2026-09-20 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7704d3f2-0660-3f1b-b03b-dc41e782e2e3 | -9.2414 | -45.9411 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 39637a91-3c4f-37e2-8926-612190c6d8ed | -7.2519 | -55.5994 | 2026-09-20 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| ff813800-dbe3-3684-bff5-6aa792f09be3 | -10.9112 | -53.9635 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 896962b7-2dc2-382b-abbe-cbe023b373ae | -3.6946 | -60.5835 | 2026-09-20 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 176.6 |
| 290ff237-3533-35ad-b445-592419c79b54 | -2.8009 | -59.8957 | 2026-09-20 14:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| db44bec3-68ce-3977-813b-46c05cf69b17 | -7.4288 | -44.718 | 2026-09-20 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0f446e9b-d4ed-3030-8edc-a7c15f7dc990 | -11.9352 | -49.7752 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| dd5f0fbf-70f1-3656-849b-2fb3535c51eb | -6.3382 | -59.9566 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 6784562e-0afb-379e-824e-e64ae06d1ac9 | -8.845 | -45.9391 | 2026-09-20 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.7 |
| f94c2bd3-0df8-380d-b528-ece82d2059a8 | -7.0286 | -45.2554 | 2026-09-20 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7f250b13-ab93-396a-b473-987848bf3e68 | -11.875 | -49.9767 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| d173da1c-5b27-3579-a63a-377544551bf9 | -12.027 | -50.0015 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 357ee9f4-19f8-3963-bc47-9efe2abdb844 | -7.5704 | -57.6766 | 2026-09-20 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f07cbe5d-9579-326a-8335-9a862788fae4 | -12.1328 | -47.041 | 2026-09-20 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| d5aa0da9-b81f-31d6-9e21-cb03f49d971e | -11.379 | -51.42 | 2026-09-20 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| fa800927-9cb5-30b8-8679-82b5eb647372 | -13.5907 | -51.4794 | 2026-09-20 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 199.5 |
| c8ea434b-8008-3575-b10b-a62a25f41e51 | -10.9694 | -57.1881 | 2026-09-20 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 34115e5d-f4f0-328a-abc3-ff9c74b13f62 | -8.1874 | -54.742 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9822c3ab-2bdd-3f9b-9a08-862e290603f5 | -12.8053 | -54.0669 | 2026-09-20 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 41b58e5c-5832-3b9a-b5a2-ec02d4bb5203 | -5.8408 | -53.5408 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b6435da4-c8cb-319d-9878-59f10a1ccdec | -10.3917 | -48.8915 | 2026-09-20 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 9a9a37bc-1faa-3cfb-b396-07732acc6806 | -11.6624 | -50.1954 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 208716a2-e437-3356-a93c-3d147c4b82b7 | -12.7616 | -46.2029 | 2026-09-20 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d2c7b6cd-f485-30ae-9f80-de32af94f82b | -8.1688 | -54.7432 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 5835d8fe-d1a2-36e6-be52-23fc9c07b962 | -12.5081 | -50.952 | 2026-09-20 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| e741d74c-3cfe-33a1-a2f1-41e9e62c47ba | -15.866 | -49.9177 | 2026-09-20 14:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| eb447b78-4a5e-3282-b742-41da9384a176 | -6.6098 | -45.8991 | 2026-09-20 14:00:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d4e1d507-44cb-32c2-904e-5709bdb61b47 | -12.9088 | -50.9886 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 93e35275-6d50-3b94-b2b8-07ae9e5bb7bb | -9.8502 | -48.4053 | 2026-09-20 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 260.4 |
| 5f120210-ee3a-3166-84fe-8778ee916d18 | -10.8757 | -57.1554 | 2026-09-20 14:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b30ecd12-5098-302f-9b94-4f94719eadfd | -12.8893 | -51.0124 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 5cb48a9e-46c2-34ed-aff7-9feb887d7935 | -7.3259 | -55.6153 | 2026-09-20 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 024feda6-4e49-3eff-912f-e1c69d7ad58a | -8.4797 | -57.6282 | 2026-09-20 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 15964c67-1d80-344e-839e-d88236c3ef6a | -8.8639 | -45.937 | 2026-09-20 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 26d1ccdb-98dc-3ddc-88e2-821072225fdb | -12.0263 | -50.0447 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5caeeb4f-d3b9-3416-a469-75ea9f3025f1 | -11.0065 | -48.3187 | 2026-09-20 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 65453c49-20db-3cfc-a85e-4d23e648debe | -9.84 | -46.4136 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 6789d4b2-743b-3828-b175-e1e66c526706 | -13.5911 | -51.458 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 9829661d-05d7-3b93-b769-ca387b6a0a90 | -11.0256 | -48.3164 | 2026-09-20 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 7623a534-f915-3e62-a042-d80bdeb65cb9 | -10.8732 | -53.9874 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 9503cb13-d8b3-3ed3-9920-bfb690b69cde | -11.6621 | -50.2169 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| f442d770-adf2-3684-9a05-bc5ea393593a | -7.693 | -44.6469 | 2026-09-20 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 815847e6-6a7b-3468-a495-c746d92e728a | -8.0706 | -55.3522 | 2026-09-20 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 3e18a2be-5c84-3a3e-a2ac-fc0fafbeea77 | -8.1872 | -54.7622 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 7669e3de-4f6d-3cbf-9924-8cf5ce0d8ac8 | -12.152 | -47.0383 | 2026-09-20 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 149.1 |
| e94e09e4-3f6a-3f5a-8e3f-ed149f81f256 | -9.2865 | -48.2453 | 2026-09-20 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 139.7 |
| a4b83102-60b2-3e94-befa-29d3b5b1e362 | -9.2868 | -48.2234 | 2026-09-20 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 190e829f-8817-3e3a-8ec5-2dc27b37433c | -2.9157 | -57.8177 | 2026-09-20 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 6af49ede-bd42-3111-b050-2a4133f6989f | -7.1203 | -42.083 | 2026-09-20 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| f35c858c-0413-36d8-828f-3a054b36a204 | -2.8791 | -57.799 | 2026-09-20 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 602c25a1-bf17-3b72-80e8-0e6674061c2d | -10.8177 | -50.9286 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |


[Clique aqui para ver as próximas entradas](README123.md)
