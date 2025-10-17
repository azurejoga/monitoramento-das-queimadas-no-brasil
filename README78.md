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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db2d083a-c33b-38a0-b0e6-9a93c810caef | -5.51461 | -44.9849 | 2025-10-17 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d13487-cbca-3825-86a2-91f43ada7464 | -6.94416 | -47.72713 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1edd9742-3731-39e6-bc5d-bed9b6298071 | -6.59111 | -44.37315 | 2025-10-17 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29a73e66-74e1-3984-9350-81af71ac3f8d | -3.68185 | -47.63328 | 2025-10-17 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69917fb6-d5a9-3298-9608-349324bd76f9 | -4.25385 | -48.54968 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 676a706b-15a4-3119-94bf-2aab1d0fae83 | -2.87131 | -50.73235 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d20b115-9f52-392e-899b-227dc30bb260 | -5.90337 | -44.75069 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4adf326f-42d7-3913-a3ed-4fe01a02700c | -2.87852 | -50.72993 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b05bf492-97f8-3d4e-af3b-a5a57e6dd70f | -6.54338 | -43.916 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78e92ccc-18a0-3d46-b73e-8c121a2426f3 | -4.46523 | -48.27356 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c5cd2e6-2e2e-327e-bc89-e2779a68ccaf | -5.63473 | -50.03077 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0444eef0-703e-316f-8533-43fefb979a2b | -7.18282 | -42.36025 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee259e2f-7f5c-3f41-9031-52b4ffccfe81 | -5.90548 | -44.74 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2a7183e-9acb-308b-94e3-1591f99bed03 | -5.33516 | -44.47475 | 2025-10-17 04:49:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 677537c7-3e7b-3dca-8983-9af3b5167911 | -5.45833 | -44.64456 | 2025-10-17 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58de6b2d-ff6c-3b29-bf83-2b5e5463de87 | -8.25422 | -44.02352 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de227416-24cc-34c0-8be9-624cf03df89c | -7.74312 | -42.50452 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 416b72bc-3726-36ff-a8d3-79e912c1dbb5 | -4.40915 | -48.94481 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db13c0ce-e417-3709-90af-ed104bc37298 | -8.29321 | -43.39231 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c722d24-9cd2-358f-9118-322698737aca | -3.35228 | -49.94032 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5821d46-114d-391a-86c1-220cd0a9ca76 | -5.91128 | -43.94412 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 224874f2-0441-368f-8124-556880a1e92c | -8.30585 | -43.4114 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3501c78-4053-3859-a859-8e58cc6a5a48 | -6.96961 | -42.20649 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ceaa4fb7-838a-3335-b162-2d11e5c93c65 | -5.73809 | -44.98741 | 2025-10-17 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 723911cc-42df-3aae-afdb-022e3ecb54ab | -5.71705 | -44.52057 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9699944d-0504-3ffd-9ada-835f58073a59 | -5.76965 | -46.76149 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b393a78-fcb9-3765-8fa1-02b2f3807e81 | -5.20279 | -43.75042 | 2025-10-17 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbdacc07-bc30-37b1-a706-c444da4342e9 | -5.24763 | -50.96135 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75248358-d449-3224-bf15-2f3027601d44 | -6.3828 | -41.47298 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 262f3830-8be2-34ff-bd26-06d094e83bfd | -6.74506 | -44.37235 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff6324a3-84f5-3ca3-9829-0cbf7dcbf5b0 | -7.53139 | -44.2805 | 2025-10-17 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b558bea-2e67-3760-82c5-4481a9107508 | -7.17165 | -42.51807 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d11a98f-16d4-32d6-a2b5-18996596bca7 | -5.8839 | -43.91438 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c62da02-710e-3c1f-98c0-52572902ebaf | -8.30681 | -43.44095 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5c362c2-f131-3adc-9ccc-e161b84db5b6 | -3.24481 | -45.97593 | 2025-10-17 04:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 9be6d868-67c7-32ca-98bf-ff31c33411bf | -4.22137 | -48.35982 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25f57d96-f8aa-3200-b4a0-cb2dacd2a0f6 | -8.23986 | -44.02163 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88096c0e-79d8-3804-aa66-bd4f32fcf5fd | -6.21557 | -41.54822 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ffdec8c3-fcd3-3b3a-9a1f-110b27c7a168 | -5.86933 | -43.91658 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 655dee85-0533-314f-b576-4ed171a824a7 | -5.81494 | -42.33568 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7325c3b-6ba2-31bf-8258-8230b184d8b0 | -3.32113 | -42.79783 | 2025-10-17 04:49:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0b8c5b5-a488-3dee-9434-6f6ca28152ce | -7.27957 | -42.31791 | 2025-10-17 04:49:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9e8aff57-7924-39cb-b2f1-f07286495980 | -6.20868 | -41.76651 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c1e41a9e-64e4-3559-86bf-a092e31ee52c | -2.87241 | -50.72542 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9b905db-f758-3041-bbb0-55f87e15fb1c | -5.87926 | -43.91363 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce07ea0b-dffa-34ac-9880-a30e6395731a | -7.66575 | -42.56721 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5cfe270a-90ad-31ef-a67d-ff84a95f5ec7 | -4.26355 | -49.69572 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6745e44a-4931-3d0a-9923-8ece7905ba4b | -7.27279 | -42.93933 | 2025-10-17 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c1532012-ec44-31c2-8eb0-a1c0b36aaa95 | -2.86798 | -50.73183 | 2025-10-17 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fb7412a-ad54-3862-8b3c-e68719568ede | -5.88829 | -43.88456 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bcac137-0f94-3d20-8415-972486bab84d | -8.22364 | -43.99831 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d7c0078-73a0-308b-9c98-dc2f085c7c7e | -4.31138 | -48.08135 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad17fd8-f6c8-3c03-936c-50c5256ae5fd | -5.82845 | -42.24346 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd9f2d23-b834-39fa-9a02-7e9c394c97c3 | -7.36452 | -46.54754 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41f351f1-998f-3bef-9224-3ac9ae900c84 | -8.27289 | -43.35456 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 77d6ce3e-8f3d-3646-8866-cd7d9879b3cf | -5.87934 | -43.84809 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f33f670e-987f-3ca2-9825-6607ffd8b92a | -7.35892 | -41.90795 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6981730c-6319-3482-af52-84b9bb98a25d | -7.18101 | -42.37309 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a23e93eb-24e2-3395-9f44-944876f3af05 | -5.3129 | -42.94677 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee338fb3-cdfd-30a9-8c27-8c779104226f | -8.22371 | -43.31127 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a3bbab9-2bb6-3b7e-93d1-73f07114ec61 | -7.27827 | -42.93717 | 2025-10-17 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 83fb39b8-3453-31b4-8778-ee17f7fc4c49 | -5.74619 | -47.47612 | 2025-10-17 04:49:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67c28167-1728-3033-b82b-2841448ecac4 | -4.41143 | -48.95265 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ce3800-2404-358e-9649-e93069c58f84 | -6.89205 | -43.98962 | 2025-10-17 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7f602e3-ac63-3ad3-ab86-b4e7fd4cb939 | -2.73673 | -48.30793 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ec2f2b6-31fc-3724-8a80-d7e1e085e175 | -5.83457 | -42.23807 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8629e804-e8ec-38be-b381-dc2c97b90baa | -2.7141 | -49.4122 | 2025-10-17 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 72a940fd-743f-3a00-ab59-ba6dd2c6cfc3 | -5.86484 | -47.58063 | 2025-10-17 04:49:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fc41792-3180-3fce-bc47-cf828f41476f | -5.89005 | -43.90487 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9ff91558-62c2-3b3b-b409-888d17a2ba72 | -5.79302 | -42.49841 | 2025-10-17 04:49:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6f4a901f-8508-3c69-8a83-887372876ff1 | -5.45979 | -42.95158 | 2025-10-17 04:49:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a42b0aa-3c27-3339-9c89-a522df456202 | -7.8304 | -44.13694 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e3bf1883-9647-368f-8e02-812dddd90ee4 | -3.47716 | -50.02356 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26e1bda4-2091-3082-baa1-d85f05ae1eae | -6.53535 | -55.04763 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e09e1374-5e96-34c0-b910-4f056c657911 | -5.53299 | -44.08126 | 2025-10-17 04:49:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9bb541e-daf5-37b9-a9f0-f540d29de7b8 | -6.58543 | -48.77315 | 2025-10-17 04:49:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b34408fd-0f1a-32f8-898a-26277527752d | -4.40571 | -43.40224 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2887cb5-476f-3951-ba44-630a1d39a956 | -2.74706 | -48.30951 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c148c54-b3d7-3f7e-8136-70ba52da4427 | -4.44289 | -49.6914 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6283b512-a227-37f5-9913-fe0314929998 | -1.49863 | -47.81186 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4f1185e-80df-3d37-8e5c-6de882e5076c | -7.66704 | -42.59637 | 2025-10-17 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ebeae0ef-83d6-32ac-8c02-da5729edc168 | -8.2203 | -43.98726 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aea85b1e-c7dc-3718-aa06-59430f9414fe | -5.4809 | -48.6502 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65142d9a-47ca-3ba8-a7f2-a5966e2980d2 | -6.5481 | -43.91652 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d48547ee-07a1-398d-8427-0e56c1430ff9 | -4.92298 | -46.73074 | 2025-10-17 04:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2f5089f-5ed0-3a59-afce-e7a1b71f63da | -5.58363 | -44.40059 | 2025-10-17 04:49:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6aca3a9-6f1e-302e-b74d-41e2f54cf3fb | -2.74361 | -48.30898 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c350248-e7ad-3642-a041-679350da912e | -6.60428 | -42.06974 | 2025-10-17 04:49:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c6c826e-4cb0-3341-809a-3ec1af8385a1 | -2.57797 | -48.40454 | 2025-10-17 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d490243-3a01-324d-bcd2-c149a7b3a5d4 | -4.55303 | -46.62475 | 2025-10-17 04:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79524f80-b6f7-3820-8739-4f387ea82c65 | -6.19049 | -52.7361 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5ccd103-34c6-3caf-b365-ba8c0637d3c7 | -7.17208 | -42.51144 | 2025-10-17 04:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5a74ed14-7475-3a18-854a-04e374192d1d | -3.84348 | -47.06359 | 2025-10-17 04:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208ba5e9-4bad-3296-b1ea-943f2eb98fe6 | -7.15965 | -46.53069 | 2025-10-17 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af412a13-726a-33ce-b85a-0fb576356e30 | -6.20411 | -41.74578 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 84275208-d53e-30c3-afe6-81d79dfc5cfc | -4.86853 | -45.78262 | 2025-10-17 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b080fad-3ce2-3669-9bfe-5b9694c26579 | -6.54269 | -43.92094 | 2025-10-17 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f04d1c9-56eb-3e12-aeae-1b042f8f256d | -6.99384 | -39.23239 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 569ad3c1-0e11-369b-afbf-9628e17dadda | -3.6467 | -53.49488 | 2025-10-17 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42eb2105-09c6-371a-8b8e-f54998bc30f2 | -6.31334 | -40.93862 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
