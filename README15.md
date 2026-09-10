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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b30d360-48ff-3a95-babc-eeb1e21b742a | -7.09966 | -42.13576 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 63f44947-964c-3211-ad08-e73f433f9800 | -6.36005 | -43.36543 | 2026-09-10 04:06:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b07983f2-c632-308d-a1d9-f81de8d86a33 | -5.68658 | -43.39217 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| eda9a69a-06f1-3c69-a9bb-57b534a86997 | -5.4149 | -41.84238 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d68f4353-92d0-3b14-8cf3-a0b0756af9af | -7.05243 | -42.7135 | 2026-09-10 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4e47fef7-eed6-3428-a4f5-2bd09e694a9c | -7.10122 | -42.13794 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8aecc97e-815d-3866-85db-a52d31e2c7b9 | -6.76436 | -44.56584 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86e4146a-ceb1-3846-ab45-744f9e065d18 | -2.93869 | -50.47009 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c46f726-c510-3fc6-9312-fdc1f393c4bf | -5.48246 | -45.12662 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82a4fd8a-2b02-36bb-a140-3ca0cdeb94e5 | -6.17611 | -43.01951 | 2026-09-10 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8746692c-2645-32ef-9fb3-737a6df9d706 | -4.0005 | -51.02562 | 2026-09-10 04:06:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1d79259-d2cc-3154-8bb6-7154a705e18e | -5.80504 | -43.79992 | 2026-09-10 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 821fc6d0-097b-3c15-b330-7f4dfa40e7db | -6.27725 | -41.69833 | 2026-09-10 04:06:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 494c2783-5bb8-350d-9c82-100b77a22019 | -5.77152 | -45.08081 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 80b51095-aeea-333e-ae4d-2c86f2879fb0 | -4.00214 | -38.43171 | 2026-09-10 04:06:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bb71eb6-bfcd-3907-86fd-986e74c57379 | -2.94079 | -50.4579 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c61e16a-960c-38e1-bca1-742296faa100 | -3.26326 | -50.08091 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97b3d516-2b54-39f6-aeab-2a62181674ea | -5.77072 | -45.08545 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c76a5296-4134-3bd1-b482-89322b83c216 | -3.24814 | -47.24471 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d45f40a5-b46f-3a85-aa76-b6f35c803bba | -6.35982 | -43.36573 | 2026-09-10 04:06:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 83117783-d535-3c62-9f49-c8d8fe52b751 | -5.65398 | -44.30042 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0cbf03b3-84eb-39d5-b7a7-d8783add4359 | -5.39339 | -44.16237 | 2026-09-10 04:06:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f40bccf-b413-32fb-87c4-b34432136ced | -5.10784 | -46.9455 | 2026-09-10 04:06:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5045dbf-fc32-3e84-b5fa-42fa36e118e9 | -6.76364 | -44.57007 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee544f52-b694-3ea1-b568-b2cde0d0c6c3 | -6.16226 | -44.63897 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 78bf146e-a9f5-36c2-b4fb-72d6d4b531fd | -6.16152 | -44.64324 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9344e353-921a-37a1-8208-f3f08359cbc9 | -3.55073 | -48.18408 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4a922ab-0610-31f7-bb65-a684f926ba23 | -4.36315 | -47.77876 | 2026-09-10 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2ae3529c-eb45-3e15-aaf2-5003f00df14a | -6.51212 | -43.96235 | 2026-09-10 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e486ec99-9240-3ef0-83bf-6e5b55b7033c | -7.10707 | -42.1254 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 79bccb5a-14c1-3e23-946d-7fc3ab9e4810 | -5.76773 | -45.07553 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| f949c90b-25b0-315c-a9e7-054432639948 | -7.10484 | -42.12762 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59c7b1dc-0ac6-3eda-afd7-5b5f0aac4623 | -7.15121 | -39.41387 | 2026-09-10 04:06:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bcb96882-2850-3e9c-8172-61d22e4a1e69 | -5.60468 | -44.85059 | 2026-09-10 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51bc8aff-c497-335f-8fa4-70c39f1fd963 | -6.09364 | -44.13893 | 2026-09-10 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30fe6d8e-a6df-348b-af37-f90e76a41761 | -7.12999 | -42.11384 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| abcaeffd-5de3-390a-8926-afdbab0cc272 | -3.5456 | -48.17897 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1639754d-fccf-36b3-a3c2-fd083e46c877 | -5.10279 | -46.94814 | 2026-09-10 04:06:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53843b68-45c0-38eb-89ef-e5be342aed1b | -7.54027 | -38.43909 | 2026-09-10 04:06:00 | NPP-375D | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1ecf6df-034a-3ea3-b883-fa01e1237928 | -7.05086 | -42.7228 | 2026-09-10 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1a4beecf-aaac-3c67-9dd8-bb1419ec398a | -5.63901 | -44.22317 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b783837b-b3d7-3aad-9782-baa04b8c2ee6 | -4.1509 | -43.1014 | 2026-09-10 04:06:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a881af-ee62-3923-8f4c-52b558d41ccd | -5.55478 | -43.43278 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4026e53-fe37-37ed-b34a-2305ff50e464 | -1.47087 | -47.27332 | 2026-09-10 04:06:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6fbb47b-df7a-3a74-9d73-d8fc31ddf7c3 | -2.93762 | -50.4763 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 267cb183-4263-3a22-b1a5-8fa57376bf6a | -2.94222 | -50.49007 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 45979510-06d1-3409-a69d-5cc2d39de373 | -3.973 | -41.522 | 2026-09-10 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 983a5c28-eff7-37dc-bfdc-c8a8de8bdeee | -2.94333 | -50.48367 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05f28233-5ab7-3e07-82bc-779ed4956459 | -7.10635 | -42.12978 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26e2a860-ef34-30dd-b7a8-b2b16942f18f | -2.9365 | -50.48277 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b8bf7bc-7695-379f-9af3-5100e32b24c9 | -5.65832 | -44.2942 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6fb29d4-ac23-3c5a-882f-7a1d95cdea31 | -1.09983 | -48.05447 | 2026-09-10 04:06:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c2c4be-a40c-392f-bf3a-dce6448396c5 | -5.68192 | -43.39503 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81760fd7-2aae-3744-bf63-e5b41daaf043 | -6.17179 | -44.63619 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e91bca62-2fbf-36e9-b4f0-889796ed495c | -4.86177 | -47.40744 | 2026-09-10 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01b140e9-15a2-366e-9103-e563d8c3befe | -5.75211 | -43.27063 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 402f35f0-dc3f-3e75-9314-ee885883e095 | -7.11298 | -42.14706 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 599c22dc-4e8c-3647-a305-65569756b31d | -7.11816 | -42.11634 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1ef13429-b1ae-3419-9e6b-ac94a84cdf47 | -5.38592 | -46.29888 | 2026-09-10 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8f86e5b-f6bb-33aa-9fc0-310ee289bbfc | -3.55214 | -48.17582 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7f9fe26-8d5b-3871-a96a-dc36b93ac7e3 | -6.27047 | -46.3674 | 2026-09-10 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab2460f8-62e2-36d0-9b6c-58c1e32b004f | -5.76074 | -45.08878 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| f2276e58-4323-3148-b887-1fdb0c0fbea5 | -5.76693 | -45.08015 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 269b35ed-2c19-383d-abec-922d84bcdd1e | -7.12186 | -42.11696 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 569dae19-7015-3a10-aed2-9db9cbb7f6e9 | -6.09857 | -44.13564 | 2026-09-10 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8404ddcb-9ce7-37bc-9a69-28da58af5643 | -3.26475 | -50.08687 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20a54010-8ce2-32ab-902f-67eb9efdd519 | -6.42726 | -43.06797 | 2026-09-10 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15f9b47f-9437-3f9b-9b24-feb3070f6a19 | -5.92566 | -44.94607 | 2026-09-10 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c082af8-e111-3119-8156-cace8d01b3aa | -5.65901 | -44.29717 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 38da5249-4237-3fd0-93f7-2786f7d92b7b | -6.82384 | -43.04963 | 2026-09-10 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d72aca7-d0e4-34d9-be4c-da6e461e5a6b | -6.10283 | -44.13633 | 2026-09-10 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69b625a1-242b-30ce-99b9-f38cdb579160 | -3.55145 | -48.17986 | 2026-09-10 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa5c97c3-70ca-334f-a353-8087da657dff | -6.32961 | -43.81518 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f27916b-0e54-3329-a2ca-2b313431f032 | -6.7149 | -45.45742 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a22805ba-220b-3153-a8b2-44873156fee0 | -6.72278 | -44.04521 | 2026-09-10 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2041d40a-365a-3c4f-8119-8e2566bd8fe0 | -2.94439 | -50.47747 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 322b81c8-f24f-326e-b8a5-975198653a66 | -5.11735 | -46.00986 | 2026-09-10 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35cded0f-97ee-3eaf-b6c4-5a8c58293f41 | -3.26883 | -50.08775 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d58c9591-1871-3ee6-8f53-58f55084f6f3 | -2.93975 | -50.46397 | 2026-09-10 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 451ff2ec-2683-3286-9641-3f272b374b3a | -7.11149 | -42.12162 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c0d2eab-bdcb-335d-a7f3-4c4e17ca00cf | -3.67532 | -38.84374 | 2026-09-10 04:06:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5b261a3a-5e1e-30b6-b55a-803e33729d7d | -5.65764 | -44.29827 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b829c16-6ad6-3a0f-8245-d3d2bd71c8b3 | -5.32581 | -47.47297 | 2026-09-10 04:06:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2535d45-8b93-37a3-8443-197f35c4d8ab | -6.75389 | -45.47933 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 20478d1b-017b-3450-adc3-c41593dda83e | -7.04781 | -42.71752 | 2026-09-10 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e0c7ad8-b6f0-31f3-9e93-aba461398204 | -6.23141 | -42.85502 | 2026-09-10 04:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85283dd4-47e5-383c-b337-5dc4eef09f17 | -6.09431 | -44.13496 | 2026-09-10 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 250a89b9-552e-33fe-91cd-7cc2e9bdc8e7 | -5.77231 | -45.07623 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 686d018a-f465-33a8-9ac7-88265af1e29f | -6.72343 | -44.04142 | 2026-09-10 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd179125-b4fd-38a6-9a0f-50c838bf337e | -5.75271 | -43.26707 | 2026-09-10 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e7f08b8-19f1-3c6e-a277-9c81c7a9e0fc | -5.41709 | -41.83699 | 2026-09-10 04:06:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 286088ed-55d8-3ca7-b016-ac2567e545fe | -4.8672 | -47.40837 | 2026-09-10 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b5b13f3-61d2-3dab-b339-77107970e2f5 | -5.60543 | -44.84617 | 2026-09-10 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e7c8af9-84a6-307a-ad52-8bf626c831b2 | -4.49529 | -42.55278 | 2026-09-10 04:06:00 | NPP-375D | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74c6249f-72d9-3202-97a7-9a5f2e4830cc | -5.66264 | -44.29502 | 2026-09-10 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 964e8886-8fe3-354d-ba6c-40d1581a634c | -5.1183 | -46.00424 | 2026-09-10 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c8d74674-a85a-3ee1-bbd7-767ff1753b2e | -5.76316 | -45.07482 | 2026-09-10 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| ad20276d-89bf-3ec7-9a61-80ae4b4a34f1 | -5.37695 | -46.29124 | 2026-09-10 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ac43daf-1ba9-38f5-94ba-99a9b8cbafb5 | -6.16591 | -44.64402 | 2026-09-10 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8b881bed-ef67-3150-b3ea-66571d3270b5 | -7.11299 | -42.12447 | 2026-09-10 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
