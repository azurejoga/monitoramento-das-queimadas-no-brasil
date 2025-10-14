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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edcf318f-aa43-3498-b2c1-c2b6a90ab859 | -5.90344 | -42.83697 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9cddc62f-3968-3dfa-8997-d5211af6d1a3 | -3.13888 | -50.21106 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef565f18-74b0-3f0b-83a3-32be00833bc0 | -7.67036 | -42.38162 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 69dff424-9bda-35b5-8698-65cc9258746b | -6.53463 | -41.62411 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8564ff09-7738-3fa5-a975-e884895bb36a | -8.2391 | -43.34222 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe050489-073c-3c13-945d-1ccd3881cc5f | -6.15412 | -41.7725 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c34a8679-8232-36ff-89f1-ad90c376410a | -5.4569 | -37.7229 | 2025-10-14 04:04:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 667afe5d-88d3-352d-97e2-86fb6931dbf6 | -3.97503 | -42.11929 | 2025-10-14 04:04:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9024437c-2bd6-3701-b2e4-69bf3c5389e0 | -6.90028 | -45.66278 | 2025-10-14 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62674bc0-a545-38b4-ad1c-7f576eae7f73 | -3.16191 | -48.60566 | 2025-10-14 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3c1dda7-9a85-3010-9b4c-cb9bea3eccee | -8.50371 | -37.94022 | 2025-10-14 04:04:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6cb2af4a-919e-3065-90da-e7eb84dee309 | -4.50935 | -42.071 | 2025-10-14 04:04:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 582f7345-09ce-355b-b46e-b0019b225fda | -6.23838 | -41.55566 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db83815e-b29d-3e4f-86c0-91187fab9377 | -8.4366 | -46.18528 | 2025-10-14 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98ac93db-1172-3962-babe-9a4953fb385b | -3.04177 | -40.11487 | 2025-10-14 04:04:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 4de103d4-8799-3d48-8da7-a531a69dedca | -6.98862 | -47.08681 | 2025-10-14 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa5ca50d-cf8d-35e5-8aac-c2f477509f13 | -8.24962 | -43.39034 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a350fe8f-23ef-354b-a04f-fcb0cbd8a7aa | -7.64357 | -42.56987 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7eb08c02-bf64-3821-9e68-2d307eaed3ff | -5.57634 | -41.10888 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 179578cd-2d9f-3973-8083-1171b47b990f | -4.91285 | -41.54383 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9264408-7851-345b-8a0a-c96c0f160c99 | -6.57843 | -43.91772 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d922fbaa-8f6e-3fae-aa4a-b1306d064410 | -5.94148 | -43.73003 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbb96df7-f1a3-3df7-bbcf-e87b6b62a5c2 | -4.29988 | -50.4026 | 2025-10-14 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce2d038c-e0fb-3d87-a044-5f2fb6191dbb | -7.51932 | -42.69269 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cd3d8075-a0fd-3ac5-a636-2530415ffd8a | -3.29436 | -43.50051 | 2025-10-14 04:04:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58c050a0-80cd-3a57-8efb-7a9b22c3836b | -5.25162 | -42.00733 | 2025-10-14 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2ce2371-85f7-33db-aa13-32171be45893 | -9.53006 | -41.683 | 2025-10-14 04:04:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c0c868b-9e6f-3754-a38a-ec1da084ddbf | -4.2366 | -48.68465 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08949c1b-4e45-3590-856c-7dd0c8d32f5c | -8.43175 | -46.1882 | 2025-10-14 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 635d2654-3fdf-32a5-822d-6b9db8b3fa52 | -5.26445 | -41.00801 | 2025-10-14 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b685464-d2d0-3337-a190-0297a5f1476c | -5.60525 | -41.19432 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0730d1ad-fbfd-3cc0-a086-903030cca972 | -7.94642 | -44.10981 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdf93565-e3b6-3d23-8b4d-2270ce8b4239 | -5.256 | -43.21593 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18a07783-5640-32b5-a855-7cd04d311d88 | -7.75202 | -44.73093 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d33c6f3-904f-31eb-bada-bb3ee3953ee0 | -6.16883 | -41.72548 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 00fb8c57-a0c7-3856-9671-ecfa051ce598 | -7.95086 | -44.12906 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6e6f4a14-ba85-32d6-b913-3555b0cf5a85 | -5.54109 | -41.32938 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99dc18d7-9ba6-3c86-9ade-9643ae3c2ec1 | -6.14277 | -41.75956 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fa0f2947-26b9-354a-ac98-c956e9f5f05c | -6.24952 | -42.91093 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ad353c7-3b7d-33ce-ae41-ab9ac4e5dc84 | -5.5473 | -46.38194 | 2025-10-14 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bd01e9b-2e0e-3275-9e0e-01d65d084eec | -6.37704 | -47.25977 | 2025-10-14 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83dbedc4-5415-310f-9137-139d256caaf0 | -7.68135 | -42.37951 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 676d6550-a978-365f-b108-2f826cb47498 | -4.67024 | -43.12032 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f59cc2cd-cb50-31e8-90f5-f91150dcc428 | -7.09148 | -41.96305 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| de2dd0f3-aa43-3571-8a3f-980e194d30aa | -5.41966 | -40.98114 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dfc8af75-f9e1-3b5c-a682-63074e8f06b1 | -5.73609 | -40.76607 | 2025-10-14 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9d517fd0-286a-399b-9d48-e838325b51a8 | -3.43921 | -50.25181 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a41c9720-7209-3ba5-9b43-6899ad821217 | -5.59794 | -44.89785 | 2025-10-14 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 144fc1a1-3c73-317a-a68a-1e34e366702d | -7.9021 | -45.00093 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb0d6ddd-e089-36e8-948b-fe2b0d81106c | -3.75002 | -41.67811 | 2025-10-14 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b4860da8-5d41-332e-8c8e-7b73e52ef0e2 | -5.56493 | -41.311 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ee3bd01-755b-3000-8764-804b6636fa66 | -6.45651 | -44.5757 | 2025-10-14 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58a73f14-f598-3ed7-b9a5-ebe910729fdf | -7.49136 | -42.148 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 352172b8-6044-3a49-b7d9-164739057198 | -8.25141 | -43.35695 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e41687c-961c-3d4b-8747-fad7a494b1b1 | -5.22606 | -50.95455 | 2025-10-14 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1b2b61b-a4b9-32dd-9c9a-66a89d2a133d | -0.89726 | -47.54958 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b2767f5-a620-3c42-b162-9ec04b816259 | -6.18395 | -41.76214 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4932fbff-1a79-3972-968e-297377dfd2e4 | -4.66141 | -43.12782 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f1aca5b5-bbae-3e2e-a34b-be772b876496 | -6.21314 | -42.48968 | 2025-10-14 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e184af7a-677f-397e-a104-b459abb469fd | -5.30974 | -42.90535 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89b8b868-7f11-36d0-9077-b6e10720e19c | -4.87621 | -45.61054 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eded5beb-1955-3aa0-a811-aa3fb2154e5f | -6.17101 | -44.2888 | 2025-10-14 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef949a52-e6f8-3f06-8d99-060fe0389e75 | -7.75321 | -45.73071 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 05c96377-7b77-358e-a89c-7a921ecfd369 | -7.65202 | -42.56631 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cfd36a5a-ee1a-3281-a441-1a7059105739 | -7.84268 | -41.76545 | 2025-10-14 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ce089f47-a201-3738-8f7d-babac4282682 | -5.49694 | -43.06292 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c3841700-06e5-30b8-9778-67c8098418b7 | -7.67728 | -42.38274 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2144a90f-9307-3138-929c-9469a00b1f15 | -5.8624 | -43.85753 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55eda424-7a5f-3ea4-bdbe-6644cedeb3bc | -5.88832 | -42.90636 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aa3eb3fd-1d1e-3687-a8db-aa98c800db2c | -5.79531 | -43.89204 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 878e8db4-5a27-3eca-b11e-ba5024b4f378 | -5.97485 | -44.93011 | 2025-10-14 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84122d66-d071-3016-aae2-582dc7c88310 | -5.63279 | -42.68755 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bdaa57d5-aaf7-3c3b-9ff4-f4ebaf1a9b70 | -7.63945 | -42.5732 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d67a9ee9-3c68-3898-8c15-9400807f39fa | -7.93367 | -44.11687 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b5d5c17f-2ced-3683-9ef9-e2ce839f8566 | -7.08588 | -43.701 | 2025-10-14 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c349a527-37ac-3f4d-8e4d-37dfd05d0e22 | -4.17068 | -38.12139 | 2025-10-14 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 34cd7ba7-d45b-3fb8-a528-34ac378b90a5 | -6.86692 | -43.85567 | 2025-10-14 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96064b1e-d2f7-334d-9904-d33ea61dfc88 | -3.37811 | -50.28267 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 279f7968-769f-36a2-b6c8-0ed42f0b3798 | -6.17568 | -41.72657 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 23abc0b7-a203-3a57-b577-5f4c10d84b7c | -7.75157 | -45.71513 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c13c5e6-d065-377d-86e6-43d49692e38f | -6.38911 | -41.48558 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9b847e63-e87f-3e42-a215-dc21baae6cb4 | -3.43436 | -50.25327 | 2025-10-14 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1dd5ca16-fd6f-3028-91e1-6842a3762252 | -0.89671 | -47.55124 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 16711425-4abe-3696-994e-fb920bfee452 | -5.61678 | -42.71822 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3d1ba05e-f1fd-334e-84be-8894bad58af3 | -6.99128 | -38.4471 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 745b7cf1-539a-3b15-be8d-61c5a2893304 | -5.31201 | -45.52975 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbea4ae3-a5f1-397f-a0d9-9f91a2d92852 | -2.4349 | -49.37304 | 2025-10-14 04:04:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d45dbc24-b91e-3ad8-860c-fa7db82ce3aa | -4.6163 | -43.61464 | 2025-10-14 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44427c6c-15f9-3d43-8183-6b833c9ba05f | -3.05638 | -40.81508 | 2025-10-14 04:04:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c96317c4-ffae-3e0c-aef8-8ebe1540156b | -0.90196 | -47.55209 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2f45ce8-26cc-3c4c-ad22-5544209b86dc | -7.67382 | -42.38218 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be53b81a-5165-3a66-b182-c5b9860fbdc4 | -4.69242 | -43.12397 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9eb6181-67db-3b1b-ac24-36983afdc224 | -7.52569 | -42.69773 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 26063660-4ea0-3339-ab8e-b3f497502499 | -7.42377 | -45.4105 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17b557bf-308d-3380-b744-5a1f0020d1a3 | -8.03424 | -44.4825 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c138cd35-bd75-323e-b2bf-8474b12fe186 | -7.44967 | -38.97324 | 2025-10-14 04:04:00 | NPP-375D | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5975651a-0ced-3f83-bf2c-025ae10c7e95 | -3.15564 | -42.88726 | 2025-10-14 04:04:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9f30e1c-0c01-31e3-85e7-000b076f3d16 | -5.22526 | -50.95915 | 2025-10-14 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39230a0-abae-307d-ac4b-82f43be5b594 | -4.1293 | -42.2165 | 2025-10-14 04:04:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd7ace6f-0e5f-343e-b7ea-4be6ffd8e642 | -7.53559 | -45.81717 | 2025-10-14 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README17.md)
