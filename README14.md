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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 422b2d2a-1349-34c9-b597-c710c896d0b3 | -6.10039 | -40.88394 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4e598d94-94ac-3f1c-8f78-e2cbbff701f3 | -4.37002 | -43.38395 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2d65808d-372d-3122-9804-b9f2f7a6ee33 | -5.87606 | -43.88862 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ced0762c-035a-38cc-bd03-5c816951296d | -6.56677 | -42.96379 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c3fbee4-9fde-3624-a1b6-638349768461 | -4.56521 | -44.00923 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53b12778-fe35-37e2-b2a8-cb8c04f21453 | -4.6712 | -44.10029 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 0abeb992-cd6f-3ffb-b484-4d8dba13d818 | -4.65807 | -44.09057 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6248fc48-655c-3501-af7e-605dd4f2c8b6 | -7.07748 | -41.9454 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c73dd10-2570-3e7d-9035-c66a35dd0cd8 | -7.16218 | -42.51888 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5f86d0bb-dfa3-3f57-b4b0-6a5f6cb71a83 | -5.54337 | -41.32034 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1169d232-bfae-3247-9f9f-842576aa3784 | -7.08362 | -41.94648 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24c3abaf-1d54-3ee4-b2c8-832c90cb0417 | -6.04207 | -41.93824 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c5a9440-bb49-35e7-aec0-a55556d0f919 | -4.67119 | -44.09383 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d7ee2d66-ee12-3c12-a674-4e9397cdd9d2 | -7.16502 | -42.50328 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7624140d-457e-327a-ba1e-5bd3eabe55a1 | -4.37458 | -43.39853 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 88e84122-9b93-3300-ad19-69a29df6a947 | -6.38359 | -41.47663 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3bc58275-eda1-3f7b-9a49-4157f1f3f6ce | -5.87077 | -43.8906 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6004087-f075-32ad-9a68-3f617c1cd27a | -5.87378 | -43.86208 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c449b5c-986a-3bb3-b6db-f147208ee6e7 | -4.65539 | -44.10517 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b0891b2b-8515-3255-a183-e27c3671cf9f | -6.15638 | -40.90208 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a9ef4980-3c17-390d-8ef9-867505224373 | -5.87501 | -43.89426 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 651c02c2-ec1d-3618-9ff9-1e5f206948d1 | -6.52222 | -42.19546 | 2025-10-16 03:25:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bf8d0d49-4afd-3cc2-ba06-e1a974b87897 | -5.24907 | -41.029 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| adce53e1-47f1-3e67-b97c-1b516a5d58f9 | -4.66396 | -44.09913 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| f081bedd-6c40-3586-90b2-f491d2cda0db | -7.16314 | -42.51358 | 2025-10-16 03:25:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 918885e9-e3b0-3bc7-8f01-2b42469afd9c | -5.47595 | -42.93991 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3afe1df2-e533-3ffd-b953-65556004ac46 | -5.40419 | -41.15139 | 2025-10-16 03:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dba22c99-7c1e-3432-aeaa-05bc6afe8e0f | -6.16147 | -40.90712 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 0e1d1ad3-be78-398c-9752-f110f29a420e | -5.47084 | -42.94461 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| aa011ab7-a776-3b6d-880b-2a8a54514097 | -5.87185 | -43.88461 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7730df7b-1804-306b-ab28-819fde3fc8a3 | -5.40403 | -40.91441 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd4dccec-05ba-39a2-94c0-118652e24ce3 | -5.00279 | -37.96542 | 2025-10-16 03:25:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e5e5037c-bfa6-365d-b115-9c28fb64f80f | -4.39782 | -43.38918 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7cf4ea1-52ae-33b6-8655-9fcb91a15840 | -4.36185 | -43.38937 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 10175971-02cc-3ac0-9cc3-587fa850cb7b | -5.8555 | -42.88932 | 2025-10-16 03:25:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f8514c27-1534-3a1f-8caf-3be4eb1c7649 | -5.42002 | -40.97971 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b17d345-3478-36fa-a6fc-11570f4e0035 | -6.36908 | -41.48779 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 467e2a6c-b170-3bd4-9b25-a85ed1f66d59 | -4.35557 | -43.3972 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 417c29f8-d2ce-3461-a877-38db1e410899 | -5.87502 | -43.85546 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dcceded-eb10-35f3-a0dc-7e8e2324d862 | -4.67255 | -44.09287 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4ea3a55f-23bb-341c-98bf-b0b7f018f8bd | -6.42911 | -41.88462 | 2025-10-16 03:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 699d33c7-489f-33b3-80ee-23d7355b5b56 | -4.65271 | -44.11981 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ab10353a-239e-3c92-b5be-88c2bdcb97f1 | -5.42514 | -40.98544 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 208649d8-45f4-3fc4-a88d-d3616e5a8b33 | -7.259 | -41.74478 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 35d025f9-7d93-3095-87d1-f03d4557ac2d | -4.39432 | -43.40876 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58adbceb-78e1-3cea-b528-40bd6757cfe3 | -7.10474 | -42.03852 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a75a68a4-38f9-384b-a136-eeee634e693e | -4.35673 | -43.39051 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 637d5e1f-6abf-38db-b556-69eca5fe9717 | -6.13938 | -41.77781 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf0d1c2c-13ed-30f5-97e2-6d7e9083fd00 | -5.88651 | -43.87143 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b5d55042-6e5e-35d4-8fdc-d9d063d62b69 | -6.13855 | -41.78233 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 062a3838-b1f5-370f-91e9-4de651fefcd4 | -4.66987 | -44.10131 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 32c0b835-affa-33ec-b0d4-31644dce20f6 | -4.66647 | -44.07837 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c2578d4-16f1-32a8-aa10-74ca7bb22312 | -4.6567 | -44.09155 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0ef0dd00-ce98-39e3-b0dd-c200d6e4c5af | -6.15076 | -41.78514 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4ba272cc-67d9-3304-a71c-f4a1e241e9b9 | -5.44168 | -44.27201 | 2025-10-16 03:25:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f700495f-66ad-3a83-ac75-1f1b7fea8960 | -7.30034 | -41.86442 | 2025-10-16 03:25:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f36a54e-fd84-3a9a-8b4e-c15c32f0c1c6 | -7.11095 | -42.03942 | 2025-10-16 03:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd7e97d8-06d4-32b7-bde6-f2a346cfdfae | -6.45107 | -43.38595 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85d7060e-4149-3fb6-a082-360b57e31ddf | -4.38625 | -43.41369 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26048000-74e0-3298-87e1-2b245cde6cc1 | -6.16069 | -40.91137 | 2025-10-16 03:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 055c5375-560a-3256-accd-a8215d2682ed | -4.66138 | -44.10721 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c8ae2cfa-eddd-34a0-b10e-e7d02984dc6d | -4.65855 | -44.1287 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d22ddaba-ea3f-3829-84b0-037d9d9da97f | -5.54264 | -41.3245 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1c761c9-8cef-3c62-bbf4-2ec2ce4bf017 | -4.3794 | -43.37172 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfb47683-d116-33be-9d4f-bb7703428c9a | -5.60248 | -44.25889 | 2025-10-16 03:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b932dd76-e3eb-3075-9784-e61f68f3ffb4 | -6.56709 | -42.97533 | 2025-10-16 03:25:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f9be484-5734-3227-b4b4-7f3d2a570978 | -5.79429 | -35.59925 | 2025-10-16 03:25:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 797020a1-b1af-3394-94f6-3dfab555f9d9 | -6.38277 | -41.48107 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| df071182-5001-3449-a490-00211cde1d57 | -6.14028 | -41.78204 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 708e66f9-1aa6-3387-a92d-786b5d1977e4 | -6.06339 | -41.89128 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78c220d3-c97d-34a8-9595-b9c5c96d4403 | -6.01199 | -35.3199 | 2025-10-16 03:25:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa2f14ae-29c7-3859-8aaf-eeccba1f0623 | -5.86403 | -43.8478 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c1682542-4660-36c9-b32c-379c56674797 | -4.92405 | -41.55254 | 2025-10-16 03:25:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 01e4690a-877e-3c25-aef3-e3ae0b68e804 | -5.06714 | -40.47346 | 2025-10-16 03:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ddc026a-edf0-3139-ad54-21d22b8ec57e | -6.06784 | -41.90219 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ce0f8f4b-a0d9-31c0-9c12-2827937da6ab | -4.67243 | -44.08676 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 442ddd09-f37f-3086-9b6a-368e456fb817 | -6.37594 | -41.48434 | 2025-10-16 03:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d9dff753-3678-3987-934f-dcbe9937ee7a | -7.29546 | -41.95805 | 2025-10-16 03:25:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 784ce248-e834-3c3c-bbff-4a7a4150ae9f | -6.13818 | -41.75793 | 2025-10-16 03:25:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 382cc42e-625d-3945-aa39-37db5e0d6618 | -7.39878 | -39.69685 | 2025-10-16 03:25:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 17.5 |
| bb914197-0dd0-34ad-a1d4-64bd9ec562a2 | -5.44009 | -44.27405 | 2025-10-16 03:25:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4daf5b17-f282-33cf-81b9-711aebe47212 | -7.32445 | -39.26579 | 2025-10-16 03:25:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b4c73c90-335b-30bc-a7f3-690a4e826d6b | -4.64159 | -43.13321 | 2025-10-16 03:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e153b71a-c758-398d-ae4a-f5345b1c2295 | -7.46574 | -41.51817 | 2025-10-16 03:25:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| b01c763a-bbe6-36d1-97fb-7e741e894686 | -4.38973 | -43.39425 | 2025-10-16 03:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| eb6939ef-f411-3cdd-91c5-44dde1824258 | -5.47806 | -42.92814 | 2025-10-16 03:25:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 555943c9-705c-37d9-b7f9-4b710ecb4944 | -4.66524 | -44.08533 | 2025-10-16 03:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ab8d563-f59c-3e01-aed0-c19d5a395201 | -5.86219 | -43.88529 | 2025-10-16 03:25:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 247c86bb-c84b-34d3-be8e-4d09cd933d4c | -5.42589 | -40.98107 | 2025-10-16 03:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 643e42db-4eb5-31d9-99a4-ceb0a620e9e4 | -6.04122 | -41.94296 | 2025-10-16 03:25:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0b28168d-25bf-37b7-873c-d7ab639bcee0 | -6.42118 | -39.60173 | 2025-10-16 03:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb3a1540-7404-3000-a5ed-2ac23bf681fe | -9.6882 | -44.53116 | 2025-10-16 03:28:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6bbf46d-8b37-37fa-8091-8f914bb183ad | -13.04413 | -43.03163 | 2025-10-16 03:28:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6459ee1-6e17-3fbc-b795-a49939242a4a | -12.65152 | -41.24815 | 2025-10-16 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ace3c425-9a8a-3159-845a-02bb84e1c1fa | -8.45742 | -44.17994 | 2025-10-16 03:28:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 269e71df-317f-3a48-bfce-3a88dcc12d15 | -12.22456 | -43.30359 | 2025-10-16 03:28:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 731f54e9-1b3f-3cdc-b3fb-70ea9383a080 | -9.15069 | -41.06113 | 2025-10-16 03:28:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 5f878063-6990-3946-9bf1-a4479553b6c2 | -7.6627 | -42.38575 | 2025-10-16 03:28:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c50ca9a8-130c-3e53-98f6-2bb9a852a996 | -8.2374 | -44.03249 | 2025-10-16 03:28:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d26ba23-cf3a-3c69-9aea-1df8ed2fb2d7 | -13.90449 | -45.57868 | 2025-10-16 03:28:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README15.md)
