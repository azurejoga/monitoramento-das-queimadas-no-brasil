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
| a75c9684-e532-3967-9ec6-2a22488ebdae | -7.10401 | -47.95295 | 2025-10-26 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 05257980-f0b2-35be-869e-f7ff16bf170f | -3.85813 | -40.73657 | 2025-10-26 04:00:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa535ed0-d67f-3ca1-a6e4-e8c4515d9bef | -2.97741 | -49.11912 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20344f91-aade-34bf-8dcf-f384a3ce43b2 | -6.10469 | -43.70189 | 2025-10-26 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 23861416-e8ff-3f61-8bca-c977a22dae14 | -6.60197 | -42.6731 | 2025-10-26 04:00:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2961cd7e-fa23-31b7-ad12-203e12e427cc | -7.8488 | -45.37101 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ef00806-d244-3407-91bb-7da0162c25e4 | -3.23802 | -50.64674 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e61907ef-6e5f-33cd-bcfb-21c184e1720a | -4.63493 | -42.51184 | 2025-10-26 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90ff22a2-08c3-314f-9732-65d7ee68d79e | -7.77968 | -45.38606 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4d5e474f-5b2a-3737-bed1-e6698833b7ec | -3.10473 | -49.45695 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 886c30be-afd1-3893-8ee8-9d07bf6b1047 | -6.13105 | -41.72301 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1e7c15d-7b4a-3133-a66b-262103864402 | -6.92141 | -44.88386 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51d83977-6a0f-3766-a18b-3f9396de45c0 | -7.15106 | -44.13471 | 2025-10-26 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1518b136-4ccc-33ac-9a2e-edc16dd4e9d9 | -7.02509 | -46.0796 | 2025-10-26 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a524abd-9e8e-3e48-97b6-70fdba5e4efd | -6.11093 | -41.73895 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3a2acfb8-fc98-3565-a2c5-30cc6443adc6 | -5.10428 | -43.19862 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 93396577-dfe1-37c3-accc-26fc3710bb0e | -7.4043 | -45.75805 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e82d390-7e38-3ef2-8758-034104c1983c | -6.20216 | -41.52209 | 2025-10-26 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc5494f3-8d75-3ec2-921f-e13f3e603333 | -6.13809 | -41.80877 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d7c5107f-af4e-33ca-8ad9-3b86acbb6304 | -6.39545 | -42.62838 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c39603ad-9746-36f6-a21c-b094725774a7 | -6.70179 | -42.05574 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e787904-daa0-3d91-a79d-7f847ad8dd16 | -6.78138 | -45.41313 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81920f2e-da58-3adc-8ad3-ca3777fffa99 | -6.12421 | -41.72181 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f54790e-837c-391d-b0c3-14bc44181454 | -4.71163 | -46.42981 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0f4d1b48-560f-3f85-ba86-61d85a3d6b1d | -5.09987 | -43.20236 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 403c7446-041d-3aa8-989e-f368cc9a8ecf | -3.75847 | -47.57234 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6aeb74a9-f686-337f-9cb1-3ac62ba46dac | -7.94186 | -47.19594 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 302def15-1653-3e41-a470-a7de38fee168 | -2.97506 | -49.11882 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5964e393-01f5-3a83-9f9a-0407afe88792 | -3.90932 | -39.36568 | 2025-10-26 04:00:00 | NOAA-20 | APUIARÉS | CEARÁ | Brasil | 2300903 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b3feff6-c08f-34c3-a419-c9b32ff1c6bf | -3.76756 | -47.57998 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0c1e1a-e49f-36f2-9fd5-a426ee58e3e6 | -5.50217 | -49.57709 | 2025-10-26 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e01cb52c-a157-3800-8fc0-09903da3ce23 | -7.69474 | -42.18188 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a8106398-0b29-3101-971a-54e627ed7e43 | -4.88878 | -43.23542 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9821c523-0bd6-377c-8de5-20072a766a2d | -5.46706 | -40.87587 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b46191c8-60fb-3098-bb67-4f3104f0229b | -5.86734 | -48.25971 | 2025-10-26 04:00:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36352446-38fe-380f-8422-e34444521412 | -4.80456 | -43.30473 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 195cd3e6-25f9-375b-8551-8f60bcceb214 | -7.69127 | -42.18583 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8df79db7-935d-3eb5-bd08-5b2bf71b87a2 | -6.06404 | -42.15247 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4dcef96b-c00e-352c-bdf0-50cf58a731cc | -5.60473 | -46.26304 | 2025-10-26 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef4ac1b9-dfdc-3744-a66c-fe8f6667be4f | -4.89336 | -43.25453 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 16260ef1-5686-39fe-afa7-8c7cbf9c7b8e | -7.00671 | -40.93974 | 2025-10-26 04:00:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12afe9a9-51f2-3ba2-bcbd-72f35dc2ae9f | -8.33194 | -49.3139 | 2025-10-26 04:00:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 337f6525-81e9-38db-9e3f-5f6e96f20948 | -6.62667 | -44.63689 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7d8a2b6-283e-3ba4-a423-da8a129b85ac | -4.39967 | -44.27273 | 2025-10-26 04:00:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10eb1e8b-de1f-3a27-af76-05b1d0045c98 | -7.64842 | -42.1671 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7c5ddbe5-9d60-3e93-b6a4-5c79d39c482f | -6.03366 | -39.61649 | 2025-10-26 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| de625a5d-127f-3ff7-93ca-b8f13941c848 | -7.76735 | -42.92798 | 2025-10-26 04:00:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 249082d2-673d-33c8-9ce2-8bfe6ffb835d | -3.0942 | -49.44736 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f8a3f56-c39c-3556-9c8a-4b5b81642e55 | -6.70362 | -42.0444 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8ff39511-8a34-396d-abce-429ea2f6863b | -6.21076 | -42.53841 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7faa8004-ff38-3b59-a408-d150d8035b16 | -6.11033 | -41.74271 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cbc8c62c-ad80-3c88-8058-e101f00a7159 | -6.44989 | -42.33593 | 2025-10-26 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71535434-2782-3ad4-8b32-a75c34dc4dbc | -4.34268 | -38.77004 | 2025-10-26 04:00:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 687fa064-e77a-30a5-bd1c-03b887c61961 | -3.1024 | -49.46971 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66454851-9f6d-329e-8c40-e5ffab927998 | -6.78972 | -45.41431 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 59d8f1c5-5ae5-3abd-8c75-161202525d43 | -6.49338 | -42.91058 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 53d1fd09-f52a-32ea-a573-0b685439101d | -5.44863 | -40.88363 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0830cf69-52ad-34a1-9b68-d6e461ec0801 | -4.89106 | -43.24501 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5aaebce0-1b0b-3d9f-b985-b99c42783eff | -8.13942 | -39.85788 | 2025-10-26 04:00:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b819821e-c5a5-37be-b656-151284da60f2 | -7.15181 | -44.13009 | 2025-10-26 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a921e68-eb10-31a5-8f5a-a018bf065a10 | -5.65389 | -48.46362 | 2025-10-26 04:00:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3acc4ccf-5aab-38f3-8faf-f8cb541bf6ca | -9.31304 | -43.09649 | 2025-10-26 04:00:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e0eb3dd-cf4f-3aa7-a5e4-8bd815db0b6c | -5.81898 | -40.82185 | 2025-10-26 04:00:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cdc840b2-e680-3b2a-870c-4f7df526274e | -8.15924 | -41.10576 | 2025-10-26 04:00:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 433f66fc-2730-36e4-87b2-ace363be30f1 | -6.79868 | -45.41173 | 2025-10-26 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fae4f3f-be68-395e-8e31-5deb785d4340 | -8.15704 | -47.0431 | 2025-10-26 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80512b55-8638-3669-82c6-f82cfec31194 | -3.23715 | -50.65173 | 2025-10-26 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7604191-b296-367c-af1b-f64b93cc7b74 | -7.38807 | -43.94245 | 2025-10-26 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec89d75a-11db-3b75-9658-6d059b88df02 | -4.02256 | -45.9973 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1f9a721-7b08-3845-976f-d746deae829f | -4.82472 | -50.69117 | 2025-10-26 04:00:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 971b4b8b-2c2b-3281-8a59-953e6f738186 | -6.87236 | -41.34919 | 2025-10-26 04:00:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51b62d57-aba7-3be8-8063-a1222a271fe5 | -6.4456 | -45.7351 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96bff2e9-14b6-3a9e-a278-24d55349f124 | -5.70592 | -41.83422 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3a0fcfeb-9af0-3fdc-b180-32b90f0b22b4 | -7.84465 | -46.44073 | 2025-10-26 04:00:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cbfa8f0-91ba-320d-8000-2d205f6d5e67 | -3.10581 | -49.44913 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab8a7d71-36d9-37d4-a78e-7119159fe44c | -6.26902 | -44.39003 | 2025-10-26 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a86c03e-71df-377a-9ee8-677ba4ab27cc | -4.89323 | -43.23155 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 64c2eaee-7565-3033-9e71-68bfd6e5571a | -7.24156 | -39.32446 | 2025-10-26 04:00:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 48a7c68d-0e27-396a-9a01-f50f4d30cca9 | -7.10984 | -47.94854 | 2025-10-26 04:00:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3de8579a-41ad-3a92-9a4b-858d4ce46bb3 | -2.98241 | -49.12403 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f1489df-5cb3-35b4-a95f-aa6af073479d | -3.76302 | -47.57613 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 628b4261-20ee-3161-89e2-c33b2737023f | -2.91848 | -52.71822 | 2025-10-26 04:00:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d19aec84-299e-3f61-83ec-92c0ac9c3fc0 | -5.41514 | -46.33484 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f661f891-657e-3b01-a799-dfac1f5f80cf | -3.8587 | -40.73299 | 2025-10-26 04:00:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3a35996c-2e9c-3f9c-aaab-2a763d7af1cf | -3.10514 | -49.45316 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31b53eaa-724f-30ef-93bd-9e3f02814153 | -6.47427 | -47.55666 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 81461c46-3901-3335-880c-c14ee1c95eb9 | -4.60208 | -48.78808 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 728fefe5-882c-3adb-b9e5-fc8dcbe2aeac | -4.88662 | -43.24885 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8985b57f-d750-3e22-8675-8218c3bb8650 | -4.48533 | -48.67783 | 2025-10-26 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9d29443-c539-332d-ab76-2677a1adf467 | -5.0289 | -41.20571 | 2025-10-26 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 216e977f-05d1-3420-a92b-453587ed2ff5 | -5.42903 | -40.87714 | 2025-10-26 04:00:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1f7f62cf-be6e-39d1-bf12-7e729edeb12c | -4.71177 | -46.43204 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 53754f25-dc1f-3aed-8d47-c63dfbef8f5c | -3.96267 | -45.41396 | 2025-10-26 04:00:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d2bfabe0-df4b-3c7b-988f-6e3a95a0294f | -3.71508 | -49.30583 | 2025-10-26 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6800b3b-5f50-3d7d-9ea4-7cb97547007a | -7.85286 | -45.37176 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f926829d-ad3e-317a-879a-4a33c39d7b54 | -6.2185 | -42.53544 | 2025-10-26 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9255f2e4-11ee-3239-926e-e9ec8b1c2d9f | -3.62589 | -42.37539 | 2025-10-26 04:00:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b802db6d-00ef-3cd5-ae24-9d3bf98d1a11 | -4.03292 | -46.07365 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75f6103b-3a9f-3eaf-b3c6-64037f01d249 | -3.76405 | -47.57856 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fe65f1a-d890-3d91-9898-6e7f162795ce | -3.10257 | -49.46939 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
