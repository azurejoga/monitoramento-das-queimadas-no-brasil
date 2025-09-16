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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2df00a5b-67e2-3fbb-a4e3-e07bb930dcd7 | -7.71662 | -45.30115 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ccc98bf-4c44-3f88-980c-0a7bd40e2f94 | -11.35316 | -47.34697 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b51a115-42c4-3850-9750-e9539a88867d | -8.62433 | -45.72045 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84894993-e41d-3b5c-8685-a85d580eef93 | -11.42536 | -46.93199 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c560ef3a-39ef-3442-a004-73a8ff492923 | -10.65183 | -46.46129 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e395a87e-e7c8-3147-a0fe-6879f58305e2 | -7.08451 | -44.55505 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d302e99e-0557-3cf2-a99d-acfd4f1c2d5e | -7.45848 | -46.14809 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0664cb6c-5a63-3507-b7d2-3f342d73ae55 | -8.36511 | -37.60635 | 2025-09-16 04:02:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52095f04-795a-38be-8964-a3754c66a977 | -6.45051 | -43.60397 | 2025-09-16 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d8a517c8-d65f-34bd-b523-1b19d078f178 | -11.50041 | -43.70685 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e16acf21-a50d-3cfb-ad9b-f340a1716ce9 | -6.40682 | -42.65603 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5250643d-1ec0-3073-8070-90de3d2d529d | -7.69339 | -44.66418 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c3720301-7ab5-32bf-9040-f41843c9aa28 | -6.12366 | -42.94382 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ae6d1873-27c3-3c6b-afc0-fd893285419d | -9.05768 | -44.84822 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0b2a11e-eccd-3d29-bb23-4d1f55dacafd | -7.20664 | -39.9658 | 2025-09-16 04:02:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39b4b717-937e-36c3-9095-7b9418ea7e6c | -5.87252 | -45.86227 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a46bf96-c4f6-3871-9fd3-adeab71b1834 | -9.7377 | -48.12313 | 2025-09-16 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2fc2ceb4-4f93-32b3-9c98-0661bfd87d19 | -5.89208 | -45.74718 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aa81f22-bd9d-3740-b59b-b585849383bd | -8.58337 | -46.3589 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fc037df-b5eb-3a4e-908a-dc3397b624b8 | -10.72042 | -46.50458 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6fe3d37b-e6f9-38b6-b33d-7f31674c843c | -5.63145 | -45.33478 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28e0c06b-ded2-3ea1-a6c7-3dc6765e02c6 | -5.89988 | -45.75243 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f59eaed-9bcd-3327-ade8-dcda32ad793a | -11.72154 | -46.47713 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9654e791-9387-34c5-ba6e-a0e2d991acce | -8.89747 | -46.15339 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9feafd06-8aa3-33a1-963f-ddee7be421c6 | -5.80274 | -44.86647 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aca784c5-a0ad-3dfe-916c-4a11660841de | -11.27923 | -50.80242 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b83528fc-c6b0-3fd5-98e9-03f30c95875b | -11.50065 | -43.72712 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 527ab013-6819-3458-b0a6-e76c6178d9a3 | -11.7096 | -46.87909 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 11bdce78-b46a-3d99-89f2-89e037485e6c | -10.78223 | -49.14284 | 2025-09-16 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4179591-78ab-3f06-920f-39443bd3bdab | -5.93681 | -45.71344 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 177aa4b8-71f3-3379-aa9f-02c4d242e392 | -6.65059 | -44.71429 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df4cc084-9d45-364d-b325-9c1051c2e036 | -8.97795 | -45.04263 | 2025-09-16 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95be364f-bf86-3fe1-a0d9-be09ec113601 | -10.14552 | -46.14774 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5604960-3687-321e-9dc5-1849c848ac47 | -5.92147 | -45.72738 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d26c8f9-1d24-3f6d-a6ec-fca9e1f59f0f | -12.35058 | -38.1973 | 2025-09-16 04:02:00 | NOAA-21 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 918ce15f-287c-3f6d-a20d-11ca1628bb62 | -10.6505 | -46.46881 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3f66dae-b4e2-32e9-ac3d-57d56f3d4dcf | -11.11551 | -45.35223 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e5508ced-9333-3514-b0cf-e2a8f7a8d158 | -7.73318 | -45.30022 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f08e9833-0913-3dc2-be9e-e6d1327da2f3 | -4.81084 | -47.34237 | 2025-09-16 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33e46e2f-95ba-3504-a337-9cb95274abf0 | -7.27478 | -46.60835 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2497776-1313-3a4a-8d50-b40c678d2504 | -11.12372 | -45.12225 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70df1e7c-e0c8-31a8-bad3-e050e9cde97b | -8.2013 | -45.55243 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4a56002-81f6-3a32-9283-346083e3378e | -9.14566 | -46.94715 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb31101f-9d07-3a0f-83e5-7e681aecd641 | -10.71692 | -44.75865 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 33627e65-f873-3570-898a-1b793031838e | -9.5388 | -46.29391 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42ee53d1-0f1f-36f4-8b1e-001a336a8a17 | -10.72242 | -46.49296 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0958a0bf-8021-3614-9a46-b0215c642cca | -11.42889 | -46.93642 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a182f085-31bc-3d41-9f32-4aa2b5327b11 | -11.50284 | -43.73559 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e4b0341-26e3-38ed-9a05-52294a09c12e | -6.16204 | -43.66799 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4154b1f8-4d42-3ac5-82a7-ab643be9cb1a | -8.6668 | -46.38022 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4ac56152-06ca-3831-8129-9ae9058ae66f | -11.4418 | -46.94268 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f301d1e-3808-376b-b337-1cd394f14ca0 | -5.79006 | -43.94645 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3e4fa19a-c7b6-3b22-a2b7-c7c4876d7bb3 | -7.68619 | -46.29206 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfbabb5f-6af9-36b9-b27f-a6c749c0b300 | -10.71957 | -44.75725 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71332647-fb80-39f8-979c-2eeadee85709 | -8.58271 | -46.36285 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765271d8-310a-3bf5-a4c1-3fc754ddc44e | -7.13566 | -47.97336 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8a04def1-f93e-342a-91a4-eb0884473513 | -9.06293 | -47.02811 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5d4b030f-566e-330c-9aa5-7c75c652cdb3 | -9.97879 | -48.36898 | 2025-09-16 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d59a9cb-5667-3616-bfab-977b7411867e | -5.98308 | -45.85061 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861bb444-32bc-3b44-b1cd-0a7bfba32e1f | -7.01045 | -44.53599 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d557349-8981-3952-b179-f5a7ff7e8412 | -6.46082 | -46.01 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1a53d80-44d9-3d27-8f14-dc8fd7ccf6e4 | -9.09798 | -46.93032 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90031bcc-2d24-30c1-ae25-12ff24795da6 | -8.63458 | -45.68498 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 914839e6-1d09-30f4-bc03-842819ed71ec | -5.54356 | -46.41029 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d81643-b192-3d2c-a0f0-02ccc2c27fc4 | -6.98729 | -44.77291 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26fd6330-20a3-323c-9d02-e0fcc9e355bd | -10.79238 | -50.66138 | 2025-09-16 04:02:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99b143d1-4a58-3a7e-8e0a-0a5562c8ea1a | -11.59736 | -46.97143 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81fd8535-bfc2-35a5-b9f4-d2aab1c420ab | -6.2484 | -43.46212 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15acf5de-93fb-3a2d-945d-ff993b6efc9c | -7.05876 | -44.17274 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8d7c6ad-aae1-3a06-b430-a3dd085b1540 | -6.28967 | -42.38676 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab8d393d-b350-380b-9a80-184b7d63b991 | -5.06 | -44.32154 | 2025-09-16 04:02:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09d4fdc4-b70f-348f-8378-24d62cf4b677 | -5.95391 | -42.80602 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2989e40f-86c8-301b-8379-0fc55b5e08f9 | -10.43541 | -45.143 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bace9153-30fe-3a45-b19a-60731d074ac8 | -11.12737 | -45.30551 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3f13f8a-2391-35a3-9dc4-180cc385712f | -11.29716 | -43.18786 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e88e213c-708c-3b2c-8bf7-aff3a5cef489 | -8.60445 | -45.73917 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f29fc70c-e093-334d-a176-d61d3dbbc347 | -7.26983 | -46.58494 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e791e44-b188-3af9-9c21-0634b7d54a15 | -6.46961 | -46.03639 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ab29b5-efd4-33ea-8a8d-e2853a88e41b | -5.59929 | -45.36063 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 801a6f86-3786-3824-8a62-dfc334a045e4 | -10.71088 | -46.51077 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| efb13763-4a2c-3a30-9756-618ce9114fd0 | -4.91792 | -48.26066 | 2025-09-16 04:02:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4248eabe-d843-3235-a2f2-b339c6a89e8c | -8.1716 | -46.76151 | 2025-09-16 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 967fa998-eb9b-3123-9690-baa1c6357e25 | -8.98045 | -46.25312 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 18282c8f-2e3a-36f6-95ed-709dd7ae3fa9 | -6.43057 | -43.31141 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8b24d06-f8cc-3b1a-ae68-228b2181ae15 | -8.61624 | -46.3963 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87162a98-8b61-398f-8a50-69ea202dce32 | -7.46338 | -46.14492 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 061350ad-829c-3fb2-b5bd-9a19bec5808b | -7.00024 | -44.57386 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 203b8e45-e551-3141-8e2a-5c0cbce511e4 | -6.18211 | -45.11665 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 173fc6d2-ebc6-3356-88e6-26e56ccd665d | -11.1245 | -45.11773 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87c3f336-6305-360e-adef-4e08b2cc8f6f | -5.00703 | -47.64307 | 2025-09-16 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3f33de3-ba46-32b7-925c-88c4585abf91 | -5.22791 | -43.69788 | 2025-09-16 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f127d304-d4b4-33e4-92fc-da933425fcac | -8.9321 | -45.50547 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7254a66-55c5-30de-b93c-c60b0ead8ad9 | -11.13018 | -45.33496 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72845508-a809-3936-9d3a-9ca805110a8d | -10.71827 | -46.49249 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7a7a0cd3-c012-30b6-8798-6d9a00590ab9 | -9.08881 | -44.84631 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e02fea66-5f06-30a2-8eaa-e70da200ac38 | -8.62495 | -45.71687 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c89c7eab-59b3-341f-9c4b-2ae101e504c1 | -10.47085 | -45.16158 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f73a40d-e950-3158-a703-be3fd2f262a8 | -7.01509 | -44.53182 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ca3df1a-b044-36d2-a542-76814abe86ba | -5.7606 | -43.93708 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21fbd3c9-217d-3d0b-8006-c63e1c442605 | -6.82539 | -47.85738 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
