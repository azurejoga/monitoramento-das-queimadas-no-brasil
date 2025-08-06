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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ff2287e-20f7-39cd-b899-d90b7da2d01c | -7.8373 | -45.22889 | 2025-08-06 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64c9baf7-db1b-3093-87cd-93c13ac1d36f | -7.83806 | -45.22444 | 2025-08-06 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a57a72fa-d4e0-3caf-8bb9-3259f1bd961c | -7.82981 | -45.08492 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07d41772-f171-3572-8594-b27a2dca28be | -6.71939 | -43.57942 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ed4faa9e-f29a-38eb-90ee-79140cd31245 | -5.72588 | -49.10428 | 2025-08-06 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2a6da63-d168-3358-a420-473ea1db5699 | -4.0233 | -48.07015 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4abdda00-06b0-3600-8682-cc23e8843f5b | -7.37107 | -44.15611 | 2025-08-06 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c0de7ad-9ef7-3a53-9ad6-f8f97bed8a98 | -3.02197 | -46.91282 | 2025-08-06 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ee081e7-e4a4-3521-a663-7a085b041bbb | -8.01166 | -43.21879 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2e7fb60-ec69-3783-ac7f-c2bee47181d1 | -6.83035 | -43.38717 | 2025-08-06 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf83d79a-e86d-36b1-ad74-b2fb81320249 | -7.08518 | -44.36296 | 2025-08-06 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fe28a41-a2ab-3d8c-b993-637126d6344b | -7.38612 | -44.62717 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a9e15b0-1a2a-3679-9c45-a41a9b330d78 | -7.91227 | -45.5281 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9daa92be-abf6-38f4-b602-756a339748e3 | -7.50933 | -47.18792 | 2025-08-06 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb6e8954-77fa-390a-b983-1563e24399ed | -7.20822 | -41.85003 | 2025-08-06 03:55:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91831ec4-3894-38cf-a8ba-a25b39e9c98f | -8.01765 | -43.18362 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 1bdda4b5-ef7e-3bc4-bfe0-1f0f076e38c4 | -7.39904 | -44.63016 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fa4e208-4eb8-3709-9c8c-31cb5082ac0f | -6.55133 | -43.6104 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 568a3e62-73b3-30e6-972a-8f9a02a4e144 | -5.58964 | -51.12933 | 2025-08-06 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03b6cfcf-8ce4-3082-93cb-7655a3fa499f | -6.72757 | -43.58089 | 2025-08-06 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6be0a7c0-936d-32ad-9287-53bfacd42a96 | -7.67656 | -45.10577 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17566f3c-b08e-3746-9889-a894e14dfe27 | -5.59504 | -51.13309 | 2025-08-06 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4a3af17-0ece-3ec2-80fa-e88ab96f8e97 | -7.24557 | -44.60937 | 2025-08-06 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49df5380-d274-38df-bfa1-99841c5077e2 | -7.90766 | -45.52971 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91c8e3e0-8324-3c49-b4e6-98f2f950b0ec | -5.7567 | -45.10671 | 2025-08-06 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 180e5377-892e-3935-ab69-ce00df95a082 | -7.64517 | -44.58304 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08c5b2e6-7994-3e04-b96e-277f9ce918a5 | -7.08588 | -44.35889 | 2025-08-06 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec323266-9247-3388-baf9-dbc123d017b3 | -7.39473 | -44.62919 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9cb4ea42-2279-338e-92fa-802a5a4b3a94 | -7.66679 | -45.10896 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4d9b9cd-31b5-3a2b-bd98-cf1fea737a94 | -4.02467 | -48.06198 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c07baa2c-9737-32ca-ab20-27d1b74ed0ea | -6.54664 | -42.8028 | 2025-08-06 03:55:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 15971d54-b7ba-3fc9-a3e3-7dc8a8022fb8 | -7.8246 | -45.08854 | 2025-08-06 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6287bb50-3f03-395a-91f9-36170ecb88f4 | -4.82035 | -47.3223 | 2025-08-06 03:55:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cfa46e2-fba2-3336-b015-d7e90bc3a2e4 | -8.00688 | -43.22312 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 699b66e2-21b5-35b0-a7d0-a00f4e2874ba | -7.1834 | -45.4804 | 2025-08-06 03:55:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56e61fdd-229d-3b06-94c4-03713efc859e | -6.82631 | -43.38649 | 2025-08-06 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2bc29d16-a976-35b6-8709-9222953a38b0 | -7.91146 | -45.53512 | 2025-08-06 03:55:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af4727da-0d26-3a74-bf28-3c08c5c4ec24 | -8.00429 | -43.23831 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2e60cef3-d3a1-3b64-b73f-694173c4c627 | -6.95712 | -41.58334 | 2025-08-06 03:55:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bb7d91d-6da7-3a75-a845-2788293c4605 | -7.57756 | -44.8999 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f12e6b08-f39d-304e-ad4c-dd1bccd6a2ff | -6.68845 | -44.76079 | 2025-08-06 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b2d8a70-4774-3142-86d9-41caccfb135e | -7.63291 | -44.57674 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66865b21-6a91-3837-a6d6-d97a3b490a0d | -8.00342 | -43.24339 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 45b81e85-cff1-32ad-bf3d-557ea12a678d | -7.37633 | -44.25471 | 2025-08-06 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98c65fda-c62a-37a1-8eaa-ecb2e859e1c9 | -7.85837 | -43.85329 | 2025-08-06 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 691f52ff-dea7-3a15-b163-56174ce8b020 | -6.54704 | -44.01623 | 2025-08-06 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed5e479-7e82-3449-9247-593b1ca3af29 | -7.50416 | -47.18701 | 2025-08-06 03:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a17559db-6d3f-303a-90a4-f94dfc203a2e | -5.75589 | -45.11148 | 2025-08-06 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5e7c216-d74b-322e-9fe2-c5b98edcd5c4 | -5.58826 | -51.13161 | 2025-08-06 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e54b690-63b2-34ce-8dea-2c0f2c63f46d | -6.27287 | -45.27006 | 2025-08-06 03:55:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 841a6e96-bae3-3b41-80c4-76db1ddab707 | -7.98687 | -43.15533 | 2025-08-06 03:55:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 67a605f2-d983-3d12-a9f5-bde98e9a1753 | -8.00602 | -43.22819 | 2025-08-06 03:55:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 991adc51-dc43-3d69-b60f-76d73ca6bc2c | -7.51276 | -44.85895 | 2025-08-06 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53a16ba3-262c-34df-83af-8561ed9024e0 | -7.38873 | -45.98602 | 2025-08-06 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f023c78d-053b-3836-961c-66d15039988c | -4.02978 | -48.06703 | 2025-08-06 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd812eaa-093f-32f1-a42a-daa85b7504ab | -10.53094 | -42.55164 | 2025-08-06 03:57:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ec469f17-70c6-3582-8cb4-1fd7ac94f2fa | -9.7087 | -51.9514 | 2025-08-06 03:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8e48f61-c73a-3d34-b6f4-b08a6bc5ae3a | -11.48803 | -50.29199 | 2025-08-06 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58335e9f-aed9-3e4a-9547-2648ba6ce270 | -9.06892 | -45.05498 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a429c536-e885-3051-b94c-13dd2d4b47b9 | -8.5388 | -47.48127 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f8dab8b-ec7d-3ea7-81dc-bb3f05f95f95 | -12.5345 | -47.17189 | 2025-08-06 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 328fa13a-5c66-3f85-9344-21d759a3465f | -11.73609 | -47.53552 | 2025-08-06 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08898ca8-f163-3106-81f2-a7595d0cb479 | -11.50063 | -50.29013 | 2025-08-06 03:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93c62cd5-3d12-31b8-8f73-4972c8fdf0cb | -11.74077 | -45.00878 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4c1fc51-378e-3423-850e-db381dedd079 | -12.65655 | -48.11189 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c90be27-282d-3d3d-b882-47ad8385f0a8 | -8.38703 | -45.79757 | 2025-08-06 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 883da694-3fbe-3c85-8acc-1cdd3d51f3a6 | -10.48186 | -44.351 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a49a3242-e580-3b2e-bd44-b7d3645f7cd8 | -11.74351 | -44.99325 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 116fa373-0625-3797-84bd-3f40663495c2 | -10.11972 | -51.67477 | 2025-08-06 03:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a268e7d2-0b6c-37f5-9a60-5472d0839f44 | -8.24628 | -45.07019 | 2025-08-06 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2ffef85-8aca-39ba-92b2-28653edf9ff9 | -10.11858 | -51.68042 | 2025-08-06 03:57:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 588ece88-1a50-3575-a28c-ffcf217b3d58 | -8.62483 | -50.01602 | 2025-08-06 03:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0806e3d-d444-3ce5-9d8b-86a2f39c9429 | -10.47683 | -44.38039 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66b60fc2-e005-34a7-b92d-f7260771e971 | -11.75598 | -45.01962 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91cefb3c-dcb5-3ce7-a576-1a72011e684b | -12.76267 | -44.41756 | 2025-08-06 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db8c84a6-23f7-3b43-8515-7f22d3c4d44a | -8.98819 | -45.68635 | 2025-08-06 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f07e332a-438c-358c-9c2f-d88c0bcdcccc | -9.30044 | -40.24148 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b9b896b9-72cd-3961-a179-20baf53402d7 | -11.74955 | -44.95901 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5372846-2671-3ce5-bc67-e83d97eaac06 | -13.29929 | -40.36007 | 2025-08-06 03:57:00 | NPP-375D | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 738069a4-6d42-3a8d-8434-c8829262fecc | -11.90104 | -44.97876 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f56fe059-bab1-3818-89b7-3e54305f7e27 | -15.54326 | -42.65463 | 2025-08-06 03:57:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b20cd074-2c06-3a96-af38-3aba724e3958 | -12.72945 | -48.083 | 2025-08-06 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 073768d0-c5ce-3865-8af3-0845a38b7794 | -9.6247 | -40.59279 | 2025-08-06 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 95494fb6-b323-3a0a-93ff-5b0c7c0287bc | -11.64633 | -50.15909 | 2025-08-06 03:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 204729dc-60a6-3e90-b456-0b3bdb885c50 | -8.06343 | -49.71629 | 2025-08-06 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c9b798a-9e63-3284-8ddb-f74995f7bb95 | -13.93372 | -54.06607 | 2025-08-06 03:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5c2943-0a54-3ff4-bed9-2f31580fa199 | -8.25954 | -45.07241 | 2025-08-06 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d397056a-ca4f-3d58-b517-71a63e1f637b | -11.44122 | -45.13355 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 231dffd5-435a-30cf-850b-36e564eb73f8 | -11.43633 | -45.13674 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 09f95474-0304-36ef-bd53-d3c213f402bf | -8.52937 | -47.44421 | 2025-08-06 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ec92919-7935-3876-ae2f-66d4589e835f | -12.98557 | -44.89346 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 895342fa-f35a-3471-ae80-d944c1032566 | -10.43333 | -44.36552 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 233e6306-8976-33fd-9da8-f9ddb3ad53b0 | -11.76012 | -45.02042 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2478d8fd-0b17-3793-9d6c-a452e9081a92 | -11.90654 | -44.98328 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e694e8-db9b-341d-a3db-bcf8ba527b34 | -9.07399 | -45.05172 | 2025-08-06 03:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 813cd777-be08-38b8-8794-fa7c7f9ef7c3 | -10.43269 | -44.3692 | 2025-08-06 03:57:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a8ffc9a-10fa-3165-bb99-701e09b20f9a | -12.72456 | -46.39152 | 2025-08-06 03:57:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3b30efa-c00f-3f77-baba-19cff84a6880 | -11.90742 | -44.95481 | 2025-08-06 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8696e0a1-825f-30b9-86b3-69a1cd301449 | -12.99449 | -44.89217 | 2025-08-06 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afe63cba-aa92-36bf-abd7-cb2b6272be33 | -16.25537 | -39.04108 | 2025-08-06 03:57:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |


[Clique aqui para ver as próximas entradas](README10.md)
