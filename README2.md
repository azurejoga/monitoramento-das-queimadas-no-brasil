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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 062c7703-f687-3b9d-9c50-69b97f39e178 | -14.44689 | -47.77811 | 2025-10-27 00:11:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d1a55f89-0839-39c5-bdfe-897560d8a215 | -11.70811 | -44.43657 | 2025-10-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e5b15999-8b64-3d6d-bc16-974fea6b86fb | -12.50558 | -44.34086 | 2025-10-27 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 599719bf-f6b6-37e3-a390-9541e92c0e02 | -13.2355 | -47.99095 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d7154ae9-3d26-33fe-90d5-2eddb3cc9330 | -12.28772 | -43.75255 | 2025-10-27 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3544bc78-e069-3f91-a9d9-cbaaa1e1d5b6 | -17.9973 | -48.17952 | 2025-10-27 00:11:00 | TERRA_M-M | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 29.9 |
| caffda86-0455-325f-967c-68ea35a757d6 | -14.03411 | -48.74242 | 2025-10-27 00:11:00 | TERRA_M-M | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| a8b9062f-c3c0-391c-a950-f62cf92ff83a | -13.64844 | -47.62511 | 2025-10-27 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 92ee8be1-8e3a-3114-9756-6bf9c4dff494 | -13.65787 | -43.73653 | 2025-10-27 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e1b2071-e1c8-3917-b753-3a384cbd0856 | -15.97137 | -43.0198 | 2025-10-27 00:11:00 | TERRA_M-M | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9fbf66eb-95d8-3d1c-8d30-44cf2889ae59 | -13.77846 | -44.09007 | 2025-10-27 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b0270c9-aa61-30ae-a0a6-799ca5c73641 | -16.14548 | -45.0949 | 2025-10-27 00:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 78b81f65-0c3b-3ba5-8a99-c4d864b78463 | -13.54428 | -44.32378 | 2025-10-27 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 33cb887a-7ae5-313e-b794-e74dedf9a500 | -12.28123 | -43.83599 | 2025-10-27 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| de07b683-eabb-35fd-bae0-97a8f7932a8a | -17.99928 | -48.1974 | 2025-10-27 00:11:00 | TERRA_M-M | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e87e095f-b111-38b3-8de4-a9c5a5d50e18 | -13.26641 | -47.97229 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6aab4405-6ae7-31ed-b906-45f085c41f86 | -16.1468 | -45.10527 | 2025-10-27 00:11:00 | TERRA_M-M | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 72ce3b98-81a5-35c8-a905-5324df1b3950 | -13.88924 | -48.4847 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c3345d33-ada3-3dd7-93d4-86aa2aac4bb7 | -15.96254 | -43.02113 | 2025-10-27 00:11:00 | TERRA_M-M | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93099ddd-3890-3b35-aafb-bd3d67c3f7ec | -13.04663 | -46.64193 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7a9cabc-58f8-3f8e-946c-9912e584f52d | -16.19372 | -45.09869 | 2025-10-27 00:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5ff7886-173d-3f9f-a9a8-44a6533fc178 | -15.30661 | -42.87418 | 2025-10-27 00:11:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1f44872-e43d-3a7f-a642-5958d67c2c49 | -13.08609 | -44.54831 | 2025-10-27 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9144fd78-d006-3384-a41b-4bb3e386921d | -17.63405 | -42.19827 | 2025-10-27 00:11:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 507651d7-3929-37cc-af04-5ca9a377734d | -13.05652 | -46.64064 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7181099-d5da-3f43-aee7-052f06f3dab8 | -12.05238 | -46.38218 | 2025-10-27 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 661f82ba-ec2a-3cff-a0df-6cc8553db29b | -17.08146 | -43.19195 | 2025-10-27 00:11:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ea7fbfb-3d8d-3224-9671-ecfb87913899 | -12.51321 | -44.33047 | 2025-10-27 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| fdac1a51-db0b-317a-9291-70b022260747 | -18.20049 | -42.16738 | 2025-10-27 00:11:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| db0d65ca-11d2-3682-8e9b-3d22a6199221 | -11.97765 | -44.30885 | 2025-10-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 90413cb1-1328-3556-a8f2-68a88ce3fe55 | -14.98441 | -43.54841 | 2025-10-27 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6363c178-0829-3f12-be5f-7b56312a40f2 | -13.25551 | -47.97364 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c0aa35b1-73ac-32d0-8bcf-7040b5c12ffa | -13.24479 | -47.07785 | 2025-10-27 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3379dbd6-8bf1-36f6-9ac1-1055d162c1de | -14.02501 | -43.26986 | 2025-10-27 00:11:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 11e280f5-c41b-3526-8bab-436261efaf3b | -17.32796 | -43.65829 | 2025-10-27 00:11:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 846ea4a6-1946-3fba-a99a-35d7bbea0e3e | -12.51445 | -44.33957 | 2025-10-27 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef93d02c-87d2-3327-ab69-1cba0d9cf65a | -11.91984 | -43.82171 | 2025-10-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| fc52c81d-44dc-3c16-9023-6959f3eaf756 | -13.90085 | -48.48462 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7e560352-0401-3f0e-be38-04c3763caca9 | -14.54919 | -46.18607 | 2025-10-27 00:11:00 | TERRA_M-M | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d64ae479-31ff-3a83-88b0-238bd26bfe2a | -15.58383 | -43.15513 | 2025-10-27 00:11:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 2da906c9-9945-33b6-9d2b-91ec03285280 | -14.49352 | -47.88923 | 2025-10-27 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b7092ea7-c520-31c7-8251-288fcfe9ea3f | -12.27999 | -43.827 | 2025-10-27 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1d353591-8cc8-33fd-a761-d9c5c8f64111 | -13.12786 | -44.64982 | 2025-10-27 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 157318f2-9495-3ece-a1f6-2f254823f2fb | -12.29021 | -43.77051 | 2025-10-27 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 211f90ae-2d08-3ab2-a575-9d3868c48f4b | -12.04419 | -46.39417 | 2025-10-27 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 7ebd8e56-f763-3e05-95c1-0f711b6e3f81 | -13.94482 | -43.8148 | 2025-10-27 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd98ecf6-5f5d-3cfd-a4fc-13d8eb8907f1 | -13.48034 | -43.71928 | 2025-10-27 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21d3f96f-98a4-3f47-a073-1d77fa4bb834 | -17.32671 | -43.64888 | 2025-10-27 00:11:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 626ad049-e6a3-301f-be98-b077c1bfe3c3 | -11.91225 | -43.83197 | 2025-10-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 861ee1e8-f96e-332f-8cc2-9583da2debc9 | -13.96378 | -43.82131 | 2025-10-27 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1f0c7bb0-a3a3-357f-8e54-a2fa19a93c9a | -14.25989 | -48.13561 | 2025-10-27 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 28d6b92d-95e1-33d6-80a6-f07cdfb2e7ac | -15.56746 | -43.03657 | 2025-10-27 00:11:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7d456827-7490-3c4c-9893-a1dcb84d1868 | -13.00937 | -48.67669 | 2025-10-27 00:11:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d993ebed-1c3c-3ca8-899e-498c90dd23ed | -17.43456 | -46.86928 | 2025-10-27 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9969fcc9-8268-3e94-a671-1dfd245983f9 | -12.0886 | -46.40464 | 2025-10-27 00:11:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1758daef-d411-3abb-98b4-993189c59f2c | -18.30832 | -42.13822 | 2025-10-27 00:11:00 | TERRA_M-M | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 40ba5b90-5954-3a8b-a6a4-4619da88a7c5 | -14.09932 | -46.99341 | 2025-10-27 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 11fa493b-1444-3226-b1be-16b84f49e717 | -13.0352 | -42.32353 | 2025-10-27 00:11:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 955bb178-674b-36b0-be60-0badce65db81 | -12.06177 | -43.98742 | 2025-10-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8a9ce45d-f5ab-34a2-a07e-dd9d4b48d3c3 | -18.55761 | -44.42069 | 2025-10-27 00:11:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 76756503-a197-3941-8dbb-08c7313f9be7 | -13.54081 | -47.15843 | 2025-10-27 00:11:00 | TERRA_M-M | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bc0241a6-cbdb-3266-8ae8-748f14ae60ce | -17.319 | -43.65966 | 2025-10-27 00:11:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7ddb12f0-2949-3f5d-84b2-4e9c51868b20 | -17.32042 | -43.60152 | 2025-10-27 00:11:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 86bb4634-e563-35ef-a545-fbd50e8bc1e0 | -12.28897 | -43.76153 | 2025-10-27 00:11:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d053dbea-255c-3a23-8fa7-a65475ebbfb0 | -15.11166 | -43.26595 | 2025-10-27 00:11:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 9e588149-7c04-3411-8078-eea77fcee6cf | -17.31775 | -43.65023 | 2025-10-27 00:11:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 76906ae1-b6e5-3040-b6db-e84467d72648 | -12.2789 | -43.75384 | 2025-10-27 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 229.8 |
| 37ef8b27-4f67-3bde-9e1b-2288910e40a3 | -12.97652 | -48.39935 | 2025-10-27 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a343b7d0-e47e-34c0-8bca-349770a00dee | -15.32356 | -43.80183 | 2025-10-27 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aa14b1fe-e175-3598-80b9-0e600beece37 | -15.5462 | -44.02243 | 2025-10-27 00:11:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a235e375-ea89-3ae6-9d44-f18e30a10612 | -11.70935 | -44.44562 | 2025-10-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 8b0fe58c-339a-3a02-ab34-f5d28b18397a | -13.1291 | -44.65917 | 2025-10-27 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5c42d5b-f124-3f6c-9092-257a60f38826 | -13.89118 | -48.50153 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 488c45c3-8ef9-33cd-b13a-d9eadd2f5c30 | -11.43777 | -44.67889 | 2025-10-27 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fcfe068e-f65a-33f1-becd-3a9eb947e9f8 | -16.85942 | -41.93185 | 2025-10-27 00:11:00 | TERRA_M-M | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| abd2e61b-aac1-3e44-9c5d-a7e5bbf72ff0 | -17.40166 | -45.52335 | 2025-10-27 00:11:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e25d02cf-2628-3a2f-8cdb-561c18b3e6d4 | -11.92108 | -43.83068 | 2025-10-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c4be7358-a8f2-386e-bd98-d6f50a053dda | -15.55862 | -43.0379 | 2025-10-27 00:11:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0f950803-2c3c-39ac-ab4a-64307544c540 | -16.19238 | -45.08832 | 2025-10-27 00:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 44607689-afa6-3c80-8d24-1d9d783419ac | -12.8708 | -48.65783 | 2025-10-27 00:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| d267614c-56a0-380c-b90c-7124d46d1742 | -13.65287 | -44.31116 | 2025-10-27 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1693af40-4769-3899-98e1-9ee373d962ba | -11.4552 | -43.72829 | 2025-10-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a572f36-3c8b-3be5-85a3-2d362bcbaf52 | -13.65163 | -44.30199 | 2025-10-27 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ee732f0-2177-3ce1-9616-803b0db52daf | -12.53241 | -47.57917 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 33f02dcc-9e56-3219-a3fc-d570455c95d9 | -11.45395 | -43.71933 | 2025-10-27 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 46586317-0f27-33d8-8460-5ddae444d0db | -13.96254 | -43.81221 | 2025-10-27 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b619a090-6473-3027-9181-d9dbc8f06378 | -12.50433 | -44.33176 | 2025-10-27 00:11:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.5 |
| def5457e-19a9-3c09-8f5e-796364741dc2 | -12.52919 | -47.55338 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 2a62ac86-470c-3405-989d-5a5baaa39a8f | -12.32555 | -47.47526 | 2025-10-27 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8ae91701-06dd-3162-9ebb-963286472f98 | -13.76392 | -43.64063 | 2025-10-27 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| ad8e249f-3a51-364e-b0ca-2f4a0c927cda | -14.21586 | -44.39259 | 2025-10-27 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da5ec000-524a-300a-b851-717623a15a5d | -17.58142 | -45.02811 | 2025-10-27 00:11:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 20d35e94-9e3e-3833-b59d-c1a9b9cb5d33 | -14.63661 | -48.42513 | 2025-10-27 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e8ce3fe0-bcb1-3f10-b7ed-aa7b7caa64c7 | -12.28014 | -43.76282 | 2025-10-27 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 228.3 |
| b4b8e846-de19-31e0-8024-2d976bfb9175 | -13.55468 | -44.26593 | 2025-10-27 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4ed51749-2e66-3153-b216-4630d3fdb368 | -13.08484 | -44.53906 | 2025-10-27 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 754533bc-1635-3765-a043-3cb06428e8e0 | -14.63471 | -48.40886 | 2025-10-27 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| ff6a6082-e550-3211-bf85-f4647b945d2f | -13.89898 | -48.46852 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| af475692-d252-3ba2-b29b-e56c21ae3b41 | -11.91101 | -43.82301 | 2025-10-27 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| d2f19e92-2d6d-3b5b-94fc-c9f4071f6ca2 | -12.52034 | -47.56763 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README3.md)
