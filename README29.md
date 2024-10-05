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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbe47fc5-78c2-38a4-829f-9bad8afa321e | -7.45297 | -64.44485 | 2024-10-05 01:52:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 953c1e2f-cc4e-3aa2-a616-f27a13566fb5 | -2.8829 | -50.7147 | 2024-10-05 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 89e6b8cb-0756-33dd-b9be-600406113067 | -2.9014 | -50.7142 | 2024-10-05 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 62d10d0c-43d2-3937-8978-18bd033ec2a6 | -3.1432 | -50.2254 | 2024-10-05 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 03128336-1b39-395c-8bec-89326a10592c | -3.2349 | -50.3695 | 2024-10-05 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 5d315c6e-be15-3e83-bf30-473a3ca6b223 | -3.2534 | -50.3689 | 2024-10-05 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| ab411a5c-d8b5-35bb-90f6-1ecec2bf2674 | -3.2899 | -50.4725 | 2024-10-05 01:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| f50b7350-9514-3879-b070-d69c1d52239d | -3.2899 | -50.4516 | 2024-10-05 01:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2589c68f-423e-386d-8c3f-d2ec90e8ce4b | -3.3083 | -50.4719 | 2024-10-05 01:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 73f4108b-2a41-3e45-84b3-186e3bdc20fb | -3.3084 | -50.451 | 2024-10-05 01:55:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 3d5d6315-d428-3ec2-9ed1-4826cd3eb9fa | -3.618 | -47.5352 | 2024-10-05 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 544c4e86-5abd-3dbd-87c2-116bba8aafaa | -3.6181 | -47.5134 | 2024-10-05 01:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8d85f6da-f6cc-3c0c-a61d-8e44356125bc | -4.0148 | -43.2408 | 2024-10-05 01:55:29 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 06218442-0ca6-3e60-a5cd-62536bfeff55 | -4.0794 | -47.9502 | 2024-10-05 01:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 0cfcabde-cf8a-36cf-b34f-0a41da6bbe2f | -4.9451 | -43.7888 | 2024-10-05 01:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 0f407ba5-5bc6-3355-83b8-c936cfd46dee | -5.8214 | -44.1426 | 2024-10-05 01:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a5b9fcd7-94cd-30d9-8968-9904b05a09c4 | -5.8216 | -44.1196 | 2024-10-05 01:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| c655b532-c502-30e2-942d-79aa863cfb9b | -7.5193 | -63.2558 | 2024-10-05 01:55:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 5d7e8196-db67-3492-ba9f-e61b2a2fa1b9 | -7.7362 | -49.2297 | 2024-10-05 01:55:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cbf8550e-2bea-3a3c-a518-ce239c8922d7 | -7.7364 | -49.2082 | 2024-10-05 01:55:50 | GOES-16 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 66.6 |
| afa1fdb1-b98f-3c68-9443-9509f84bf76d | -8.7652 | -44.8335 | 2024-10-05 01:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1b8b7918-8161-39c8-bc9a-ef666ca4648e | -8.7655 | -44.8106 | 2024-10-05 01:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 5199099c-c325-3d26-9755-c2fda9680c19 | -8.7841 | -44.8315 | 2024-10-05 01:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 54caa575-96fd-3a73-ab87-f0a1d734b7ea | -8.7844 | -44.8085 | 2024-10-05 01:55:55 | GOES-16 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 9ae02f53-2913-3d5b-b370-7952ce25efb4 | -8.7772 | -49.955 | 2024-10-05 01:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6b4b6e26-0ee6-3ec0-acd1-142964ae20b6 | -8.7957 | -49.9747 | 2024-10-05 01:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 988903d7-eee9-3f8e-9649-6cbe933511ca | -8.7959 | -49.9533 | 2024-10-05 01:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 82872fa1-c5f8-3dd3-a7a6-3d413e2cb188 | -10.3129 | -50.5341 | 2024-10-05 01:56:04 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8e007b4d-532e-349b-85f5-538663498d33 | -10.4424 | -50.7336 | 2024-10-05 01:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 41408abd-c550-3b44-8d0a-1549b297ea71 | -10.918 | -46.6642 | 2024-10-05 01:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 3cbc52f4-a7be-3c07-89ab-70fd74ec108c | -11.0966 | -54.2336 | 2024-10-05 01:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 482a267f-18a0-3f94-aa44-475491a5f729 | -11.1155 | -54.2319 | 2024-10-05 01:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 4deea981-daab-36e2-9d2b-c584125e90f5 | -13.1543 | -51.1931 | 2024-10-05 01:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 8b2d0f46-d1b1-3709-9940-1d4d5d178957 | -15.5597 | -57.4553 | 2024-10-05 01:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8c705efd-5802-3318-808f-22fed58c453f | -15.5788 | -57.4735 | 2024-10-05 01:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d743aaf1-fe60-38f6-9710-be11e65a91d2 | -15.5791 | -57.4532 | 2024-10-05 01:56:34 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| f1d98061-8a3e-3be9-a8ae-527277518db3 | -15.7151 | -57.4184 | 2024-10-05 01:56:35 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| f9e1bbd1-23d7-3867-881e-28eb447b73fc | -16.6598 | -55.5219 | 2024-10-05 01:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 1f0ec157-b201-32de-92fd-ce04c8701ce6 | -16.6871 | -57.4536 | 2024-10-05 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| 8217f53e-4368-3ebc-ad13-64010d284790 | -16.7647 | -57.4856 | 2024-10-05 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.8 |
| 5ab57730-1ef9-3b89-869f-feebe3d50875 | -16.765 | -57.4652 | 2024-10-05 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.4 |
| 0a99b593-7753-3fb8-9b75-9531ed1cba57 | -16.7843 | -57.4834 | 2024-10-05 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.8 |
| fae094b7-b2ea-312d-8162-292d101c6009 | -17.0888 | -56.7915 | 2024-10-05 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| 61caf670-5368-3fb1-8c1d-2b2bb7a09543 | -17.0892 | -56.7709 | 2024-10-05 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.3 |
| 683b01f0-0980-32cf-bb83-3c4dac156c66 | -17.1178 | -57.4244 | 2024-10-05 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 154.1 |
| 05de9218-09eb-373d-8bc0-dfb6a639a4a6 | -17.1182 | -57.4039 | 2024-10-05 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 210.7 |
| 1bc54132-b5ae-3d13-9bdd-ae8cc49be63a | -17.1185 | -57.3834 | 2024-10-05 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 231dbeac-be4c-32ef-a917-70af2d1c1233 | -17.1375 | -57.4221 | 2024-10-05 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 148.0 |
| 6311a98b-8c09-370c-8cc9-f4e15a1ada5a | -17.1378 | -57.4016 | 2024-10-05 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 203.1 |
| 597c0450-6d0c-38aa-a22e-dcd827be1968 | -17.1381 | -57.381 | 2024-10-05 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| e8f7f961-fb7a-3bee-b31a-be6daad28260 | -18.6582 | -57.2967 | 2024-10-05 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 691656db-0265-3911-89c2-a411a42d0dc3 | -18.6586 | -57.2759 | 2024-10-05 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.2 |
| 85ae00bc-0585-34b9-8895-f2fdf60d3336 | -18.6782 | -57.2941 | 2024-10-05 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 07b58255-53e7-3055-ab76-d4094258d85f | -18.6785 | -57.2734 | 2024-10-05 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 189.1 |
| b24e6cce-b8b8-3c27-8e1a-9a1eef1bf2d8 | -18.6981 | -57.2915 | 2024-10-05 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 1bf6ae29-90c8-35e5-a879-713122dc0868 | -20.7895 | -47.77 | 2024-10-05 01:57:01 | GOES-16 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 364471d5-97ae-3d6c-a7f3-19905d415fb1 | -20.7901 | -47.7465 | 2024-10-05 01:57:01 | GOES-16 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c1ef0ab9-18c5-3519-87fb-99f101591fa7 | -21.5203 | -48.7377 | 2024-10-05 01:57:05 | GOES-16 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 55324d69-0a9c-30d1-814b-cf93ed47b33d | -18.775299 | -52.6161 | 2024-10-05 02:00:48 | METOP-C | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6a854ba7-c997-3fa7-8471-6216f4d3aa31 | -19.653099 | -56.446602 | 2024-10-05 02:00:51 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2002f442-99d1-368f-abbf-e541c6c905bd | -19.657499 | -56.4631 | 2024-10-05 02:00:51 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e9924094-9366-39f0-9391-16d1571928be | -18.49 | -52.7421 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c978d81a-befe-3680-a8c2-9e70ad188f34 | -18.4988 | -52.7719 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 55b9f4c4-48d2-3bd9-94c8-c0d4f6731924 | -18.480499 | -52.745201 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e901a0c2-fb85-36ec-af88-0212890adb64 | -18.4893 | -52.775002 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 069d5d97-dc42-3f71-927f-c54096979c68 | -18.497999 | -52.8046 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 97defeef-0736-3875-81dd-f308422ef4db | -18.4711 | -52.748299 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 732f9cb9-2637-303c-bee0-fb2d579c7650 | -18.479799 | -52.778099 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab3b543-6759-3eeb-b781-f7a15374e5f6 | -18.488501 | -52.807701 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b87a7473-cb96-3c55-ac79-66dc1eebf6c0 | -18.4972 | -52.837101 | 2024-10-05 02:00:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 688ee160-528b-3d95-a486-617b5f6f84c6 | -18.470301 | -52.7812 | 2024-10-05 02:00:54 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6290e72c-9d88-3729-b80f-3cccca652a0b | -18.479 | -52.810799 | 2024-10-05 02:00:54 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 67e35541-3e96-301a-85e3-b383c0b674c4 | -18.4877 | -52.840199 | 2024-10-05 02:00:54 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3a8ee46f-bfc6-3ece-b0e7-833d25cd684a | -18.874399 | -54.5392 | 2024-10-05 02:00:55 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bf99e45f-f66a-3278-8c35-3ace3955c1d3 | -18.8584 | -54.519501 | 2024-10-05 02:00:55 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3ceb2e-27f5-307b-8fdb-e33ac18e32bc | -18.864799 | -54.542099 | 2024-10-05 02:00:55 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 854beecd-0b21-3b12-9351-5d35fa320b69 | -18.8489 | -54.522499 | 2024-10-05 02:00:56 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 05cbcbdc-4870-3d20-b4b5-087c419659a0 | -18.690599 | -57.2789 | 2024-10-05 02:01:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8240743b-1353-3ba1-ade7-b51f7d79e0cf | -18.694599 | -57.293999 | 2024-10-05 02:01:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bda5b65f-9578-3f36-8e7e-f0a8de5df100 | -18.677 | -57.266499 | 2024-10-05 02:01:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f695e408-75ec-3934-b8cc-368eca8ff789 | -18.681 | -57.2817 | 2024-10-05 02:01:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9855a8c2-bb82-33fb-8096-0203f73eda8a | -18.684999 | -57.296902 | 2024-10-05 02:01:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4d0a6764-3035-3791-91aa-e559a0bab483 | -18.667299 | -57.269299 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea99bc45-f0b4-3da8-87fc-54375f016ba6 | -18.671301 | -57.2845 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3fb4d6c8-831c-3294-b059-8f3fe7e7b347 | -18.675301 | -57.299702 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5d5c64d9-f030-3b21-9d95-c030eadc7efc | -18.6577 | -57.272202 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8450d2fc-dec0-3cfa-953d-91d06801ce13 | -18.661699 | -57.287399 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 628b0c86-9863-3df2-ad47-73a5c1e545ca | -18.665701 | -57.302601 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1be57a61-4910-306e-8fd2-af96080dee7f | -18.648001 | -57.275002 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 365e4073-841e-3785-b67e-8648a328d6e8 | -18.652 | -57.290199 | 2024-10-05 02:01:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a7575208-b85b-34c9-8161-1dd844a27c35 | -16.910801 | -55.809399 | 2024-10-05 02:01:32 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b78410f-b9c8-37eb-a076-0ac5a7c2f333 | -16.916401 | -55.829601 | 2024-10-05 02:01:32 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3071e56d-4890-3761-91d0-4b3978e84083 | -17.112801 | -56.741901 | 2024-10-05 02:01:33 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 643c2f0f-ac95-3018-8391-b7d890304bec | -17.1175 | -56.7593 | 2024-10-05 02:01:33 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b68fb203-90c8-39f3-b7c3-35769d3091e9 | -17.107901 | -56.7621 | 2024-10-05 02:01:33 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc854b52-27ed-3ce0-8900-94867b4d2e03 | -17.112499 | -56.779499 | 2024-10-05 02:01:33 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06d8e311-bc39-3f28-ac57-0a76b7065e06 | -17.1029 | -56.782299 | 2024-10-05 02:01:34 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6ff8307d-8937-311a-838a-b5f1a48ecdf4 | -17.1075 | -56.799599 | 2024-10-05 02:01:34 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| df1c3307-bba5-388f-b5fa-77ef1a194e1d | -17.0933 | -56.785099 | 2024-10-05 02:01:34 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2147c92-071a-3513-9d93-4ad8f96cd7cd | -17.074301 | -56.753201 | 2024-10-05 02:01:34 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README30.md)
