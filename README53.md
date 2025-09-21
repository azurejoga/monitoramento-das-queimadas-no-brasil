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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d0554be-d203-35c7-8eab-3592df8e4ac4 | -12.7149 | -47.7195 | 2025-09-21 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9ab021d3-0aad-3620-8e12-b69d689f84e5 | -7.7336 | -44.3902 | 2025-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e014bd4b-1f9c-389e-94fe-bd9e079ccba7 | -12.9157 | -50.5589 | 2025-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| b4e5268c-e005-3b7b-a6a1-f6d94bd0c31f | -17.1179 | -45.9256 | 2025-09-21 13:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 94b2e5d7-a0f1-325d-9dbc-c0011e7728d7 | -23.1523 | -47.6245 | 2025-09-21 13:50:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 214.5 |
| 033b303d-3a42-32c7-9625-019488bf1303 | -12.7302 | -46.8651 | 2025-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a42d13f9-643c-3a6b-91f1-11cfd405c745 | -11.5821 | -50.4833 | 2025-09-21 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b7174771-521c-392f-9ece-952e17c7cfb1 | -6.704 | -44.0017 | 2025-09-21 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 15922adf-656e-305a-b513-dea00df428b0 | -12.711 | -46.868 | 2025-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d531a919-dd76-3cf4-b814-c2da63b14886 | -15.0508 | -55.283 | 2025-09-21 13:50:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c5f679e1-86d3-33b7-bd9b-189006c4ae4a | -10.5976 | -46.4798 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| bd7a96bf-4bcf-36b0-b0e5-dc5ae02f6e42 | -13.2421 | -51.6933 | 2025-09-21 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| bb3dd9fd-5631-3a54-82ba-fe692e94000f | -12.6921 | -46.8482 | 2025-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9d02e7ef-8c75-3b50-bafc-4c71a3ce2f2f | -12.2983 | -45.2881 | 2025-09-21 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| be6e14f1-009e-367a-ba80-d968797399c8 | -12.0767 | -44.8131 | 2025-09-21 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ca1d1328-396d-3273-b1bd-f59c05b927a6 | -12.8781 | -50.5207 | 2025-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9163d8b6-305c-3266-8c97-728424fc8a47 | -12.2794 | -45.2679 | 2025-09-21 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| d7cdd8bb-5d87-3193-891b-764e6a396bdc | -15.8829 | -47.2973 | 2025-09-21 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b3f44363-2990-34c4-ac3d-44279ae9f037 | -10.0507 | -46.2538 | 2025-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c0793d7f-6bea-325c-bb64-14913b32e11e | -10.2811 | -46.0679 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3c0b766b-6593-39f5-960b-16d1b8aa49f2 | -10.0314 | -46.2786 | 2025-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d4ba3a89-14b3-317d-b40c-84da960eab1b | -11.6438 | -46.5684 | 2025-09-21 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ac747e71-32e2-3bc0-a8ee-77c1c3346dc8 | -17.6831 | -44.0901 | 2025-09-21 13:50:00 | GOES-19 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 774ee353-5980-360c-b42b-9141565f29e2 | -12.6093 | -45.1012 | 2025-09-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 7ec07e55-ca90-3568-9d10-45db30848fdd | -12.6088 | -45.1244 | 2025-09-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 9a203f40-286d-3226-b8ad-0045820b69a3 | -9.8629 | -46.1408 | 2025-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| edc14c9b-dc10-32b4-97a8-c663ee9bc5de | -10.0317 | -46.2561 | 2025-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1ae3f37c-bfe8-3d93-901e-2fc2d615ff53 | -10.0321 | -46.2335 | 2025-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 994f5678-3a2e-3ab5-8060-4d651aa8ba2d | -14.502 | -45.2683 | 2025-09-21 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ba68e0fb-93c3-3487-82a6-7f6635f8834a | -7.5275 | -44.3182 | 2025-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cebf1d0a-7d11-3218-8a85-6c601f365be0 | -5.1004 | -43.0808 | 2025-09-21 13:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 00539f80-ba4d-3032-876f-e8aa0d5755cc | -12.7341 | -47.7168 | 2025-09-21 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 13834b68-110c-3de5-82e7-40609efe199e | -11.585 | -50.2902 | 2025-09-21 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| de2536a5-7d7a-3844-818e-c3294661a3ba | -5.5583 | -42.1507 | 2025-09-21 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 1136876b-af66-307a-b58d-1dc8610c0f5e | -14.6047 | -49.7624 | 2025-09-21 13:50:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 1ac6a3fa-1b57-3ba9-8235-41abcc48a342 | -10.2998 | -46.0882 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| d8e907d7-da40-35eb-8c71-40b137a39954 | -12.8589 | -50.5231 | 2025-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 88aa5ca0-b7ee-3c85-9936-e2385856cd3d | -14.8071 | -51.3809 | 2025-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 36480549-318b-3220-8f90-f2e4755ddf3d | -12.7341 | -47.7168 | 2025-09-21 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 934fd13d-ec7c-3a33-9144-93288c0ef098 | -23.3981 | -49.1427 | 2025-09-21 14:00:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 973e5e6c-5b14-3028-9d85-b5e90c85c4a8 | -9.0854 | -44.9123 | 2025-09-21 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| edd57ce5-e003-3a91-80b0-b967499a354a | -10.6928 | -46.4679 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0d146393-2cdb-3a55-805d-2bdd0e5b3c16 | -5.5583 | -42.1507 | 2025-09-21 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| ac8548ab-3d82-355e-9319-d30ec72f2f03 | -7.7336 | -44.3902 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 37a164a0-ac5d-3491-bc11-82a8bb420a37 | -14.502 | -45.2683 | 2025-09-21 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2ade7d2b-dbe1-3c23-aef4-68d850a0b931 | -3.8663 | -43.0854 | 2025-09-21 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| d74e6253-f2df-312b-933f-b87ff957ed50 | -12.7114 | -46.8454 | 2025-09-21 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 426.9 |
| 997262d1-8d28-3d1f-b9ad-b834c53f4de5 | -6.9308 | -43.8658 | 2025-09-21 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| e8f8346d-d685-36c7-a285-7020152aed32 | -9.8439 | -46.143 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 8441cdf9-8165-396e-a260-47e2343fcca5 | -7.5272 | -44.3413 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 983a178f-f19e-3e46-ae3e-076b9f2d5b5a | -12.2983 | -45.2881 | 2025-09-21 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 436.7 |
| 36566e03-2079-309a-8dbd-908fdcaa33f7 | -15.0508 | -55.283 | 2025-09-21 14:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 80eba09a-8cb0-3669-911c-8f9e7efce5b8 | -7.1878 | -44.4193 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a1e8d647-7524-33ef-a4de-4f9f33781004 | -6.704 | -44.0017 | 2025-09-21 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| e08f43cd-78ff-3663-84ef-5b89aa669f60 | -17.1173 | -45.9491 | 2025-09-21 14:00:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 6071ad52-8f3a-393c-ba2d-cbbc8ad27706 | -5.1004 | -43.0808 | 2025-09-21 14:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c71a73f3-75ad-3320-befe-6d4a99bcd281 | -12.0767 | -44.8131 | 2025-09-21 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 05d274bf-91b5-38c7-83ef-dff16ec4a19a | -12.2921 | -50.1201 | 2025-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b828ec31-dec9-3020-a9d5-108f038cb3c5 | -12.279 | -45.291 | 2025-09-21 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| ea191610-6efe-3081-b437-67f74fb4ccc7 | -5.3711 | -42.0937 | 2025-09-21 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| f87c9da7-667d-3921-bd09-9bb8b1fd44e0 | -10.2998 | -46.0882 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f694d4c4-16ee-37ab-98ee-5f376d6e021e | -15.0511 | -55.2624 | 2025-09-21 14:00:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 63.4 |
| a69af9a5-b1c1-39de-82e7-fec3986210b4 | -5.5771 | -42.1493 | 2025-09-21 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 2d54aac5-0914-3b41-baa2-3f75ce0b1d56 | -15.8829 | -47.2973 | 2025-09-21 14:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 2eb8e74a-e775-34d6-843d-ca43a3a4ae7f | -16.8926 | -43.8849 | 2025-09-21 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 9c85bc06-0afa-3e7c-a757-0edfde2f8ff3 | -9.0671 | -44.8685 | 2025-09-21 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c9d7cc2d-55d5-3d23-89fc-583208848898 | -14.8071 | -51.3809 | 2025-09-21 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ce83221d-e95e-3fd9-bf65-0c2b29534621 | -9.1937 | -45.2886 | 2025-09-21 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 09a32262-0e8c-332b-acaf-b22a6dc02b8f | -10.2808 | -46.0906 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| ea3f5ac0-a0d4-34ba-be22-2bd98f54380b | -10.0507 | -46.2538 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 018b7cca-606c-3671-a644-53b9ea61f140 | -14.8675 | -45.481 | 2025-09-21 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 449.2 |
| 3264d168-c9a7-38e9-8338-0170b6a6b1f0 | -5.5773 | -42.1255 | 2025-09-21 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 2578ef81-5bb5-388f-a53e-ffa8bd7a55af | -12.1156 | -44.7839 | 2025-09-21 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.5 |
| fc056650-dacd-3c4e-b050-566ba7b9effc | -12.711 | -46.868 | 2025-09-21 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 0b4fe45c-f066-3b43-915f-2b80d9a24e31 | -12.6921 | -46.8482 | 2025-09-21 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 206.7 |
| c2070134-8bf0-3e84-89a8-9d2f0f21bb11 | -17.1179 | -45.9256 | 2025-09-21 14:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5fcf7ba0-3727-31bf-9d04-24535440218d | -2.9528 | -42.8938 | 2025-09-21 14:00:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d9d30ac8-f614-33de-a5ec-7deb6b906ec5 | -12.7302 | -46.8651 | 2025-09-21 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 24a2c186-2dd2-39c7-afa9-fe1922c99e0b | -10.0317 | -46.2561 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 3fe38cc0-2316-3ed5-8c61-054f0f5392ca | -10.8805 | -46.6241 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 9670a530-807f-3745-99ab-2187b57a214a | -7.5275 | -44.3182 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1c824b4b-c78d-3784-acd5-39bb32fe514b | -10.6932 | -46.4453 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 04f30070-5e1e-3285-9773-4df071bfe69a | -9.8629 | -46.1408 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1e1c5217-1ec8-339c-8ada-a1c0d2630b37 | -12.144 | -44.2899 | 2025-09-21 14:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 58d1bed5-2c74-3f8b-93b9-b1af40306247 | -10.0314 | -46.2786 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 345bdaef-77cd-36fe-bb21-5754e9e1b474 | -12.2987 | -45.2649 | 2025-09-21 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 355.8 |
| 51938acc-f65c-3dbc-a6cf-a6ed52f42b52 | -14.8479 | -45.4846 | 2025-09-21 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 351.6 |
| 814052a3-7e0d-3bf2-a3f8-f13db31826a4 | -8.8465 | -44.4103 | 2025-09-21 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1f7dad49-c7ba-3293-8382-0b6e9d42bfad | -12.1344 | -44.8042 | 2025-09-21 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 57cccde3-8b0a-3634-83ed-0da42a0fad82 | -9.8632 | -46.1182 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8da18300-afc3-3ccd-b89c-77f9bd59ae77 | -8.6074 | -45.3529 | 2025-09-21 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| bd017a60-58d3-38fd-b93e-d669ed5a87e2 | -10.6741 | -46.4477 | 2025-09-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 6b5cf6ce-5e4e-3d35-841b-bb9cba4104fe | -16.8727 | -43.8894 | 2025-09-21 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 9d778fcc-8f48-3a6b-a5c5-3c674410dd63 | -9.184 | -44.6251 | 2025-09-21 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4f91c4ce-e9a7-3ddf-81f4-4b6f0c7eca2c | -12.3206 | -44.0977 | 2025-09-21 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a22c8d8f-95ca-3552-98b7-30bbadeec1a0 | -5.5959 | -42.1478 | 2025-09-21 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 123.6 |
| 5c75085a-e700-3ffb-b5c6-82ba8874cbd6 | -7.5821 | -44.474 | 2025-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1a868649-ba57-39ea-b382-33fc6fb7b3e6 | -9.1933 | -45.3114 | 2025-09-21 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 816f6e95-d594-38b9-9bb5-4281081ffd56 | -9.165 | -44.6273 | 2025-09-21 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 894024bb-f156-3842-9b01-a747c4bd28de | -10.0321 | -46.2335 | 2025-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |


[Clique aqui para ver as próximas entradas](README54.md)
