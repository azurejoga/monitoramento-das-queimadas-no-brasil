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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9384e454-f094-347d-a925-27313ed07f66 | -7.80532 | -38.73481 | 2024-12-03 04:08:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c39e82de-ef32-3983-8779-f355c862cf2f | -6.77725 | -46.27172 | 2024-12-03 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10cda054-bc1c-3d64-bf9b-65e540f18283 | -7.78896 | -45.28858 | 2024-12-03 04:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b379c4d0-6b78-3aa2-b0ef-19362ac4df94 | -9.81441 | -44.70898 | 2024-12-03 04:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d30af12e-a1a3-3c72-8728-a69637f7df2f | -6.81658 | -46.77047 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec92cf60-3d87-3eda-9cf3-11d26052368c | -12.50238 | -46.35179 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 133b5fb5-873e-37d3-bd2f-33387c9fbfdb | -9.1609 | -43.11737 | 2024-12-03 04:08:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 62e3a574-f342-3157-b25f-8c943c7e56fc | -7.48556 | -47.48568 | 2024-12-03 04:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b27c588-018b-3b53-ad4d-aee40081ca34 | -6.99208 | -43.5245 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6f529a47-466e-326e-a771-0ba014f1fbd2 | -8.13961 | -44.46457 | 2024-12-03 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb7bd56b-b991-30bf-81e2-ddd43ff33ae9 | -9.44525 | -43.21048 | 2024-12-03 04:08:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 15deed43-b3b1-3887-9c01-b3b9663a896a | -12.49974 | -46.3534 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70e7f420-04b9-312e-910e-c68c9287fc11 | -10.65362 | -44.48664 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbfe97c2-8805-3e9e-925e-3c6ae4dc0973 | -6.82066 | -46.77114 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd59b4f8-1414-3d19-9b49-4556a0a87269 | -6.76264 | -43.81401 | 2024-12-03 04:08:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86d8c663-41f9-306a-853f-13d3ee58d174 | -7.48133 | -47.48494 | 2024-12-03 04:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c039d1f8-4108-3bf7-bc07-a0554719c5aa | -10.65237 | -44.49421 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ad0c9546-2cbf-3177-9e4e-9e050d719c70 | -13.93146 | -43.51389 | 2024-12-03 04:08:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3faf3fd3-a09e-30d0-acdd-21e7f161d009 | -13.24205 | -39.97948 | 2024-12-03 04:08:00 | NPP-375D | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 89414151-8d18-3ecb-9508-e2362da0ca11 | -6.66563 | -46.55751 | 2024-12-03 04:08:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3661b6c-d60e-3d34-9c1d-df97981f3b40 | -6.97895 | -43.51852 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 14606144-c2e9-3936-8855-b4d17530a457 | -7.83709 | -47.02915 | 2024-12-03 04:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59c4e6a6-a488-3976-9716-8418893b5500 | -10.66333 | -44.49216 | 2024-12-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce15f8c7-c0aa-3160-999b-a1d5a93b4bd4 | -9.70273 | -42.88877 | 2024-12-03 04:08:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eb82f07b-856e-371f-ac4b-e70e73ac2a84 | -11.63549 | -41.4284 | 2024-12-03 04:08:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3d4bc608-7d9b-329c-a0ea-26eab782e3b6 | -12.49607 | -46.35277 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 699e74f7-a605-3230-aa7c-bffe694a1911 | -6.75246 | -46.83511 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb8d2f98-6762-3d8f-b307-c0c0c482638d | -7.56615 | -45.72818 | 2024-12-03 04:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 996f0628-d8fb-3fd9-80c2-24c97f9e0afd | -9.44707 | -43.2106 | 2024-12-03 04:08:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ee526f0-b361-37e9-b55e-cd432e60b5e9 | -8.7406 | -47.02901 | 2024-12-03 04:08:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42846ce0-f9ca-338b-9704-dd626b530f82 | -8.13128 | -44.47128 | 2024-12-03 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c7c7efe-5988-356f-9dba-73b215037139 | -6.67908 | -46.37986 | 2024-12-03 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee22e006-2168-3656-b1e5-c97b93375c64 | -6.6822 | -46.38566 | 2024-12-03 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 930f59e2-0cc1-3aeb-b63f-e3911593bb89 | -8.13833 | -44.47246 | 2024-12-03 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d56c5e65-c16d-329d-b153-fbddc77f2d28 | -7.80593 | -38.73069 | 2024-12-03 04:08:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30fffc35-409b-3b98-89f1-6a3c7ba23663 | -12.49871 | -46.35116 | 2024-12-03 04:08:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e26208fa-6529-3af8-9988-b15778248b54 | -6.81595 | -46.77414 | 2024-12-03 04:08:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 762f9e14-ccaf-3d95-9507-8df4ca7593fc | -14.15479 | -43.72181 | 2024-12-03 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bca8602c-4eb7-3047-929e-9df2c47b2376 | -12.21132 | -44.32714 | 2024-12-03 04:08:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7251f08b-831d-3056-abcd-4733216aebe5 | -7.62251 | -47.84289 | 2024-12-03 04:08:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c76105e7-6cfa-35e0-a7c5-1326cd8583da | -6.98521 | -43.52339 | 2024-12-03 04:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 59a94fc4-e2a3-3b5d-bc9f-d7de15da7173 | -8.1348 | -44.47187 | 2024-12-03 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fa4f5690-6bf1-3aca-a520-54b284ccf4d4 | -7.56538 | -45.7328 | 2024-12-03 04:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 53489552-bb0a-33e6-8798-804510f0b845 | -7.80171 | -38.73428 | 2024-12-03 04:08:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 560a8d0d-94d0-340d-9f98-de559b59d78a | -6.68308 | -46.3805 | 2024-12-03 04:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c9edf1a-7251-37d9-91d9-48324a77504c | -5.118 | -43.2198 | 2024-12-03 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 86c7872a-fa14-37e2-8ade-3c5c12410742 | -2.8196 | -53.0629 | 2024-12-03 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b90bf055-96bc-3bda-a4f2-e1a97f896ba2 | -5.1181 | -43.1964 | 2024-12-03 04:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| cea67099-1c82-33e9-b9b7-e369758ba1cf | -4.1914 | -51.1914 | 2024-12-03 04:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 961f6ce3-a436-3ee2-8345-dcb12c38c9e4 | -2.8197 | -53.0425 | 2024-12-03 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d7b47869-a13f-3aa9-948a-5030b007853f | -3.347 | -46.0486 | 2024-12-03 04:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 5223daf8-6071-30a6-a6a5-4f6bc99dba42 | -1.0735 | -53.4562 | 2024-12-03 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 714d76f6-6fb6-32d5-9db1-76a7db586742 | -5.8009 | -46.4941 | 2024-12-03 04:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 1fe63ee6-2b69-32ee-bdad-084cf1c22239 | -1.0736 | -53.436 | 2024-12-03 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9dcad97c-098e-3f51-9065-e0ae1ac89595 | 2.7267 | -60.3916 | 2024-12-03 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 399c18e6-8a80-3c30-b7b0-4522578f3de7 | -5.801 | -46.4719 | 2024-12-03 04:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 216.2 |
| 06018e95-6cd7-38c3-b639-eaa7d8c51ccd | -3.076 | -53.3808 | 2024-12-03 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 619c1aea-b1ec-3a8e-bb75-781cf9c1c4a5 | -1.0919 | -53.4561 | 2024-12-03 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| e99ddd5f-d198-3f6a-a205-215112e79167 | -5.8195 | -46.4929 | 2024-12-03 04:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2e800ff7-3238-3fac-9b44-3a6ef4dc9fd4 | -3.183 | -54.3448 | 2024-12-03 04:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 18485130-c148-31af-8785-ab576622c411 | -6.9911 | -43.5116 | 2024-12-03 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 20fc4359-c706-31e6-ae94-71fd4da5cd09 | -4.1915 | -51.1706 | 2024-12-03 04:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| dabdef7e-e7f6-3c83-8bbd-059322b337a5 | -3.0944 | -53.3804 | 2024-12-03 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| e288f40c-edaa-3d35-b804-24469a34e553 | -5.8197 | -46.4706 | 2024-12-03 04:10:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| f966f06d-1612-3421-aa9c-321f7758e6f3 | -19.7188 | -40.35234 | 2024-12-03 04:10:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 72aa8311-8e53-30a4-88fa-42af1d30f240 | -16.67981 | -43.88493 | 2024-12-03 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f81d2ab1-e9de-399f-b693-6bcfb4a7b601 | -15.60672 | -39.32576 | 2024-12-03 04:10:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f690901-7085-3495-9d64-5d83949ad08b | -27.85684 | -54.44801 | 2024-12-03 04:14:00 | NPP-375D | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 3a88485b-7707-30c3-980c-67fdb39cff7e | -27.85798 | -54.44276 | 2024-12-03 04:14:00 | NPP-375D | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| a0b62f4a-6fa9-3289-b333-60df1391fc3e | -1.0735 | -53.4562 | 2024-12-03 04:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 370c5592-bd96-3eb6-a224-2f52e379ec5a | 2.7267 | -60.3916 | 2024-12-03 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 8e8bf8c9-34df-3c73-8001-4670e1444c58 | -3.347 | -46.0486 | 2024-12-03 04:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| eb729f63-ad84-3d94-96f9-e645e7c4f419 | -5.118 | -43.2198 | 2024-12-03 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| f0bd10ec-33b3-3b00-a2e8-78fdbac30a7d | -5.1181 | -43.1964 | 2024-12-03 04:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 38a8e248-8fcc-3691-b403-7fa98f1d68c0 | -4.1914 | -51.1914 | 2024-12-03 04:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| e7be7eed-c61c-3aa7-bd72-381e0e649e8b | -2.8485 | -45.3963 | 2024-12-03 04:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 83302315-8a6e-3a90-a337-ccb62cc73a87 | -6.1229 | -43.9578 | 2024-12-03 04:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8068eede-6bae-34a3-b262-9f6dc2ee1077 | -3.076 | -53.3808 | 2024-12-03 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 28758162-5e60-3df4-9a7d-65db9a18934e | -5.8197 | -46.4706 | 2024-12-03 04:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 145.2 |
| f9d8d229-b93b-341d-8c61-c7d967c27850 | -6.9723 | -43.5133 | 2024-12-03 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 52.0 |
| dbe71991-5aea-3d49-b9ec-c68f8a092b4f | -3.0944 | -53.3804 | 2024-12-03 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 32e8bd57-9d65-38e7-8e58-94cd3b0fe12c | -2.8196 | -53.0629 | 2024-12-03 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3810ff4e-b1da-3798-bac6-ad5c54ec9399 | -2.8197 | -53.0425 | 2024-12-03 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5e761b45-4a63-3c09-bed9-8f7a709aa5fb | -5.801 | -46.4719 | 2024-12-03 04:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 335ef32f-6074-3cef-9871-581c9c024890 | -5.8009 | -46.4941 | 2024-12-03 04:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 4fe95e60-309c-3ac5-8502-d6f7a6b0f351 | -1.0919 | -53.4561 | 2024-12-03 04:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| b0d7a96c-ecc6-369f-9a68-798bc0da2382 | -1.0919 | -53.4359 | 2024-12-03 04:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 6d22b3d0-68f9-3498-99d1-4a8e2f6c9c6c | -5.8195 | -46.4929 | 2024-12-03 04:20:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| b714cf30-54b9-36ef-ab70-e206eae9e256 | -2.16802 | -46.65028 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90278f9b-cbe2-37e6-b965-be0da913e78f | -2.2366 | -46.38614 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fb5075-8a94-327d-8927-9034730271bd | -1.07211 | -53.45912 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b1fb001c-369d-3f9d-a7cc-2205724f1f0d | -1.53672 | -45.84492 | 2024-12-03 04:27:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a033809f-ac79-3347-9905-d4b00900c67c | -1.08275 | -53.45146 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3ded3fbe-11ba-392d-9048-32ebcf77fd2c | -1.72234 | -46.22091 | 2024-12-03 04:27:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed0562b7-bbbc-3613-b3a6-a14e497fbe43 | -1.0774 | -53.45546 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1d624e9f-fd80-31f0-a5ac-cf6f534dfcbe | -0.84411 | -48.72099 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4031f37-c1dd-327d-9db3-dfdec8957a45 | -1.54598 | -45.78573 | 2024-12-03 04:27:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce340146-bf7d-30b4-88ba-5cfce4cde317 | -1.61647 | -45.92165 | 2024-12-03 04:27:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b411be02-2488-37ce-a2f1-961c8c43a7bc | -1.91037 | -46.29993 | 2024-12-03 04:27:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02eac099-19de-32b1-8a4d-ec823714c1fc | -0.85589 | -52.70852 | 2024-12-03 04:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |


[Clique aqui para ver as próximas entradas](README33.md)
