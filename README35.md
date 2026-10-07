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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e51f1c8f-872b-3d05-86b9-147dcd2420e3 | -3.1115 | -53.7637 | 2026-10-07 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a2b778ba-58d4-350d-be49-204002604266 | -3.0 | -54.1287 | 2026-10-07 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3716bac4-a85d-350a-896d-0e678a859802 | -3.0191 | -53.9071 | 2026-10-07 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 2fc399fb-e6fd-3c51-9f0b-25502b213f01 | -3.0731 | -54.2473 | 2026-10-07 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f0e724f1-4679-3039-b9ae-4cffcab47a89 | -5.7187 | -45.1773 | 2026-10-07 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 17c97a88-92c2-33d7-a1b7-b4ccdc1dc358 | -3.1114 | -53.7839 | 2026-10-07 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7ba301ca-098b-3687-9bcb-1188fca41951 | -2.7797 | -54.0736 | 2026-10-07 04:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 463a3f24-c8f0-3519-97c5-805b7ed8e551 | -2.7796 | -54.1138 | 2026-10-07 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| bc182110-ba5b-31de-a5ac-57f86ab22f56 | -3.073 | -54.2674 | 2026-10-07 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 90d89a39-3863-352c-aa15-5cddeca55e25 | -3.531 | -54.6557 | 2026-10-07 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 2bddc50b-00c1-3848-ac6a-7ad0c20c0998 | -5.7189 | -45.1547 | 2026-10-07 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 924ab09b-d242-3e0b-93d8-a00ef8153afc | -8.7228 | -45.1812 | 2026-10-07 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7c107d91-26bd-31b6-bd1f-47443db86c3f | -2.7613 | -54.0941 | 2026-10-07 04:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 264.6 |
| 93e303e3-8722-35ab-9b7f-0cc86fd5b38a | -3.5127 | -54.6562 | 2026-10-07 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 97574532-35ff-3870-a70c-900aeec30f8a | -3.1787 | -50.5597 | 2026-10-07 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7a528964-f97f-3c65-9987-593163c1b1b7 | -3.8567 | -55.9769 | 2026-10-07 04:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b0433ca1-fbef-3893-9f4d-ee960d0af10a | -15.2517 | -43.2501 | 2026-10-07 04:00:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 4c552649-b409-3a62-b123-bc3833230b9b | -2.7613 | -54.074 | 2026-10-07 04:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 00d8c5da-7454-34dd-8da4-a119b5211744 | -3.0374 | -53.9268 | 2026-10-07 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e4f9ef2e-1ed8-3f59-a5cb-adbb1a783a56 | -2.7612 | -54.1142 | 2026-10-07 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 504bfa77-1a39-3470-a416-9240215260f6 | -3.5311 | -54.6357 | 2026-10-07 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b0f049d7-e4c1-3137-920e-8df1cd56bf80 | -4.47734 | -38.17646 | 2026-10-07 04:00:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83d01eef-cf86-3283-bb8d-13c0a0873c29 | -5.72423 | -41.66122 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3571f33-0fdb-3e03-a64e-44f21df9dd86 | -5.97048 | -40.94759 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de3d44ad-cda3-3ba3-b5c8-380549a9072a | -5.01639 | -45.52917 | 2026-10-07 04:00:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa5a2f07-1e6d-341f-8758-6a7183dcc58c | -4.91555 | -42.75235 | 2026-10-07 04:00:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3fe9ac02-d66a-32ff-a71d-360fac938bfd | -2.18007 | -48.14027 | 2026-10-07 04:00:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57892e7f-d4d8-38f9-8c56-ef21d0ab0cc7 | -5.69072 | -40.89371 | 2026-10-07 04:00:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ee57b9b1-75d2-3929-9a70-17186b71a5c5 | -3.47219 | -50.08817 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 00fce747-7e48-3935-a06f-dd254f3435cc | -3.41172 | -39.28355 | 2026-10-07 04:00:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4c0d1030-c4f3-36df-a461-37502742fc30 | -7.41281 | -39.00717 | 2026-10-07 04:00:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e869e844-dc1b-3003-b2ba-86def1a7e76c | -4.45254 | -47.91936 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6d2a24c6-2491-39f6-a715-d8b3a7ba9309 | -5.41117 | -39.1086 | 2026-10-07 04:00:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84fbdf0a-0e4d-368d-9106-207cd3d06cdc | -6.62029 | -37.88332 | 2026-10-07 04:00:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 47ae59b9-5274-3b55-a3d7-d90deb345558 | -5.72549 | -45.15554 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b128f635-13d4-3ca7-a3ff-0fbd23bc4b44 | -5.11231 | -45.88577 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54ae73c3-05a1-3284-9b37-3e805ef459b3 | -5.97213 | -40.93781 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| f40b61c8-9c12-3e23-9859-1bab54943b4e | -5.97536 | -40.91865 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 42aeadc1-d0f6-30b5-82b7-338ac773aed6 | -6.89036 | -42.2195 | 2026-10-07 04:00:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fb7c72c8-ca14-34c9-8839-bf1ee0b9fdeb | -3.28259 | -50.13961 | 2026-10-07 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7bb14dd6-ad39-394b-a17d-521e90b6c2da | -4.32228 | -43.81469 | 2026-10-07 04:00:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97600aa4-42f6-3431-a08e-9aeded4bcbf5 | -4.45164 | -47.92437 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dab9874a-dca0-3c24-a96b-08c7331ab523 | -2.17347 | -48.13907 | 2026-10-07 04:00:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1af525c-3ad7-3845-8bef-5fab0d6dfd1c | -5.7438 | -43.28166 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6bcf5e58-8c63-3439-9306-b09a1df04ef4 | -4.51581 | -42.89264 | 2026-10-07 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 00de77bc-f6f6-3363-abcc-ba50e6e7dee0 | -5.72538 | -41.66106 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a0dd52c-e52d-3a2c-b87f-b03e6c23cedd | -6.37259 | -42.91371 | 2026-10-07 04:00:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 03faf15b-42e0-3261-bb3c-9872081cb3cc | -5.77667 | -41.92715 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f49eaf91-27f1-3e62-bd39-ece65b42a145 | -4.25071 | -46.37648 | 2026-10-07 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8b29a72-0e24-3449-be64-910d9f02605f | -5.74083 | -43.27159 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b13e82e4-f0f6-3b76-9773-0687413165d9 | -5.72395 | -41.68732 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce0a1307-204c-38d6-ba89-502eec7f2cfe | -3.77998 | -41.60309 | 2026-10-07 04:00:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 016e199c-0494-3fc0-a0e1-f3aa95df5918 | -5.11258 | -45.8858 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5531c1ef-37d6-3eb3-8f36-c2537ddabf46 | -6.02733 | -42.26522 | 2026-10-07 04:00:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7efc3fff-a57c-339b-a73c-4d81f1746186 | -5.97376 | -40.92815 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 0638a545-5ecf-3f62-b4dd-4156ac99409a | -5.71923 | -45.16095 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1ee412cc-63ca-3800-a258-e231e16f9170 | -6.2297 | -41.99059 | 2026-10-07 04:00:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 5649e27b-e120-3a5f-b21c-6a84fd69413a | -2.96279 | -40.39297 | 2026-10-07 04:00:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 8deded1f-64b0-3b3c-9414-f82bc9a43fdc | -5.72479 | -41.6647 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29296eca-e9f2-3262-b09f-a1b6cc1680ae | -5.72458 | -41.6837 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e176bf0e-5281-35c8-ab67-281b9728f88a | -3.3015 | -42.27887 | 2026-10-07 04:00:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b558e796-8747-34dc-8467-3519291e99e8 | -5.74615 | -43.26779 | 2026-10-07 04:00:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 645eb286-565c-3be4-bed4-3e9fa2f7feba | -4.84149 | -45.984 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea3b85ba-348c-35f0-8abe-bba15362fdd4 | -6.91936 | -41.23517 | 2026-10-07 04:00:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e3fcf56b-9fff-37ca-b9ee-c99a5ad0d107 | -4.45586 | -47.92472 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 34e4c2fb-fa32-34d3-97cc-aba5cb5b3b6d | -3.54594 | -50.09417 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c57d6598-2bc2-3359-9480-bbb17b3a3454 | -5.97907 | -40.94395 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c76f1f3b-d366-30a7-b6c2-39fe5fd59e2f | -6.60173 | -37.89128 | 2026-10-07 04:00:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d9724441-ad15-399c-9c82-52e9f051affb | -2.96199 | -40.39789 | 2026-10-07 04:00:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c18222b1-6b56-319f-bb78-27c3b34be02d | -5.72901 | -45.16593 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8217a360-e940-3962-8752-17c09535b1d2 | -3.47343 | -50.08113 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 04e40e1b-0c01-368f-b684-b997d0fef443 | -5.97699 | -40.90904 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c75e6a68-d4c7-3db0-9bd1-bc7e3b6f8a1e | -3.36615 | -43.39528 | 2026-10-07 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 496a1970-bc9e-32a8-a78e-6125a900d59d | -6.83067 | -39.54493 | 2026-10-07 04:00:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 83063c95-cdc9-3302-bf44-88befa390a91 | -3.53869 | -50.09284 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39e7b86f-b999-3e80-818f-eeb8a9bfec3d | -4.45883 | -47.92049 | 2026-10-07 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8897c2e0-3dbb-334c-bbb7-99eddaff3981 | -3.48673 | -50.09059 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 595382ad-1401-32b1-8aaf-f0151ed03135 | -3.27389 | -50.14255 | 2026-10-07 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 13146188-e2ab-3d51-a7eb-bf00ea95d119 | -5.72329 | -45.16819 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4c820b97-52aa-3d9f-acc9-5f19500885b5 | -5.04803 | -44.75237 | 2026-10-07 04:00:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf173585-cec0-3669-a738-b8e1a399ad61 | -5.73001 | -41.72573 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 503798ab-6df4-36ea-a88c-19044f038451 | -5.72529 | -41.68723 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 145e20bc-b3bc-33a6-bfe0-2cceeea62ee9 | -5.97352 | -40.95317 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5242f72c-1a23-3057-a888-4820d82a71e5 | -4.09985 | -42.5 | 2026-10-07 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bd54165-dafe-3e07-add7-2e937b20d131 | -4.84037 | -45.79476 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19c9877b-56f1-37d5-b639-b0e2b8bc0655 | -4.32034 | -42.99862 | 2026-10-07 04:00:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed0ddc65-09cd-3b8e-881c-74d994510ffc | -4.25647 | -46.37735 | 2026-10-07 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32bb45db-8326-3a66-85e8-ce7eac973b16 | -5.72494 | -45.15871 | 2026-10-07 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 11fb90e9-31d4-3f12-b833-5255125dc83a | -6.5844 | -41.59114 | 2026-10-07 04:00:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| af48837f-9c1c-3986-a1cb-0a336ccb04d0 | -3.53999 | -50.09196 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92cbc5cc-db22-3d56-abbe-1530031d45dc | -4.24486 | -42.66145 | 2026-10-07 04:00:00 | NPP-375D | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4703fe9b-317a-33e9-8e54-9d73adcdce38 | -4.85679 | -44.37432 | 2026-10-07 04:00:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b4b1302-97d1-3b3f-ad40-c937e47722cd | -3.35664 | -43.39362 | 2026-10-07 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9582b027-5776-324d-9ba1-18d91f1f0f94 | -4.75364 | -43.26379 | 2026-10-07 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1a0d4a-d5bd-3246-8b4f-9b31dfbe6bfc | -4.25001 | -46.38061 | 2026-10-07 04:00:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f24661f-6c9a-3808-b719-fecd7579e79b | -5.72061 | -41.69019 | 2026-10-07 04:00:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4795a4b-ae41-3356-89ea-269faea7bf39 | -4.83978 | -45.79815 | 2026-10-07 04:00:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 825ec446-cdb2-3e2b-addd-8fd1d85b8894 | -6.6175 | -37.87923 | 2026-10-07 04:00:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b15fd8d1-178c-3d26-843d-735d6466dba8 | -5.97764 | -40.92878 | 2026-10-07 04:00:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| adcdc678-e41c-33a6-b639-09ea2f552dcd | -3.49253 | -50.10606 | 2026-10-07 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README36.md)
