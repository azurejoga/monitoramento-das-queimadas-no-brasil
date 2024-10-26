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
| 51d60cfb-3bf1-304b-8c62-88c841fbd942 | -9.49129 | -47.81678 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4f3c8c6-9790-3d74-bd48-e657aac5b8fd | -9.46019 | -47.69925 | 2024-10-26 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2691098b-4cee-39c3-89f1-daa76f5bb7ee | -10.05826 | -48.05806 | 2024-10-26 04:19:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98acbe9c-c0a7-300a-a767-7554cde566f9 | -10.05473 | -48.05744 | 2024-10-26 04:19:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79cc43eb-785b-3b84-ac25-1267f828952b | -10.19798 | -47.62665 | 2024-10-26 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcc24bf3-20b8-336c-b433-b65c44317760 | -10.19452 | -47.62606 | 2024-10-26 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b20009ca-72b5-389b-b509-c49434f32109 | -10.19389 | -47.62989 | 2024-10-26 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acbfc93f-cea3-33c3-8723-a08f1b78ad98 | -10.19262 | -47.6376 | 2024-10-26 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d61380f-7722-3b8c-9896-f1b7d243dc9d | -10.19106 | -47.62549 | 2024-10-26 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 052f29cb-a561-3a35-9d4a-a2ca78cf4592 | -10.19042 | -47.62932 | 2024-10-26 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a843feff-c1b9-330e-a14d-632aef69af51 | -10.63968 | -47.96782 | 2024-10-26 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20a62beb-fd14-3208-b453-c025a955c913 | -10.63905 | -47.97166 | 2024-10-26 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94a9686d-c7c9-3431-ac13-1f586eb2e3cb | -10.57543 | -48.09564 | 2024-10-26 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d3258fde-bd1c-3639-944a-505ff38b251e | -10.57193 | -48.09497 | 2024-10-26 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c9a041e-7a75-3d01-8e9e-06ca18161294 | -10.55753 | -47.98643 | 2024-10-26 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf59700-5f1b-308f-a175-95e377728c08 | -10.54915 | -48.60928 | 2024-10-26 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6608507-fbf3-355a-b0e3-608eb01f798f | -10.54636 | -48.61144 | 2024-10-26 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83915dd7-3684-3f32-81a7-825f476edd7e | -10.35046 | -48.05818 | 2024-10-26 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54be96f9-be43-33a1-afe1-89204988ceff | -10.31085 | -47.79543 | 2024-10-26 04:19:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b354b39-2fa6-371f-aa0f-f13c5773b748 | -10.30737 | -47.79486 | 2024-10-26 04:19:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55734efa-b87a-3d53-84c5-e11624abf79c | -10.30673 | -47.79873 | 2024-10-26 04:19:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aea243e3-e551-336e-ad0e-6892385b4168 | -10.28997 | -48.89133 | 2024-10-26 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7988bcf-d64d-37b8-8703-d9b5adeef0a6 | -10.28942 | -48.89024 | 2024-10-26 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0010773-ea48-348e-a31e-f66630ccb318 | -10.28926 | -48.89566 | 2024-10-26 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01e2b9f0-d2a6-341c-b295-b7f344ac89d9 | -10.28868 | -48.89455 | 2024-10-26 04:19:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbf20176-82aa-3fbc-b876-fa8e2ff064b4 | -10.27775 | -47.97469 | 2024-10-26 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8571eb0a-84ab-3204-80d0-dfa3ec1b550f | -11.96078 | -48.73293 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eed6de1-abb3-3e3f-8bf6-2ebd611cc22a | -11.95721 | -48.73232 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52269b13-7aea-358c-bc59-c0e808b93d0d | -11.75913 | -48.36467 | 2024-10-26 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2373570a-ae04-3e94-a583-18705d7f1529 | -11.60425 | -48.60008 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ec170f7-3a58-38e5-8f0e-49fa79400df6 | -11.60357 | -48.60418 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3869367f-0f9d-38f8-a69d-8dde55aff3de | -11.59546 | -48.47757 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b190cdb8-ce62-358f-b354-430101c3ec58 | -11.59259 | -48.47295 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86fb1200-9609-3264-94cf-324e0165d0f1 | -11.59192 | -48.47697 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20078ddd-eeb5-3b3e-b1b7-9c0552c9133b | -11.43919 | -48.48124 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46f77801-1fd1-32fe-bfb4-a9aac4afb8fb | -11.43624 | -48.48188 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6e235c6-8863-3e76-8922-cfb9cc28829e | -11.43564 | -48.48064 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7426c60f-079b-325b-98f3-119d51b121aa | -11.28569 | -48.62917 | 2024-10-26 04:19:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c141108-29fa-311a-8e8a-0a2675b28d69 | -1.01871 | -48.07235 | 2024-10-26 04:19:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d243d705-8502-3bd9-b9c8-24f6a671e3f0 | -11.28211 | -48.6286 | 2024-10-26 04:19:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 469f1fab-c3d5-3f6e-a037-75376bc7cde0 | -11.04572 | -48.52715 | 2024-10-26 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9055eb01-f173-3b89-8253-fc0cecbae7b8 | -11.04216 | -48.52653 | 2024-10-26 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fce7366-e2d4-3ce3-98d5-eda5f23ec16f | -11.01864 | -48.27786 | 2024-10-26 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4211ba78-8e95-3105-aed7-9602924c1fb1 | -10.87177 | -48.80636 | 2024-10-26 04:19:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20ad2e1d-d7e7-3ef7-a744-e605e17c4ea4 | -12.86672 | -49.56401 | 2024-10-26 04:19:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec45fb91-4d38-3298-825e-d39f0eaeb905 | -12.81478 | -48.18826 | 2024-10-26 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8121ecfc-9563-3157-bc48-1cb19d34ae98 | -12.81414 | -48.6023 | 2024-10-26 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03fd8f0e-2f09-3939-8e68-e61d7d9b8dab | -12.72117 | -48.52991 | 2024-10-26 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88382149-3cc5-3444-ad41-fba068712b07 | -12.59783 | -48.76893 | 2024-10-26 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cbbc7b81-42bb-3e77-bedb-8b1af7165b00 | -12.59715 | -48.77301 | 2024-10-26 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 37300a9f-84e8-30aa-9811-3fbf520bbddf | -12.59429 | -48.76831 | 2024-10-26 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9e820536-b74a-3070-95de-485d2057ed33 | -12.5936 | -48.77237 | 2024-10-26 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 80f37377-fe19-3470-99da-ca4bdc2eb06d | -12.59075 | -48.76767 | 2024-10-26 04:19:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 16814e4e-129e-36db-b531-93bcc6f1d975 | -12.38221 | -48.59406 | 2024-10-26 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb525bad-8562-36da-854c-60bc318b349a | -1.02136 | -48.06908 | 2024-10-26 04:19:00 | NPP-375D | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b3fc2b58-376b-3ad2-8f79-324d7ffd03e2 | -1.02054 | -48.07414 | 2024-10-26 04:19:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ccd1d7ad-f028-3daa-8992-e42e58275bf8 | -1.53333 | -47.28897 | 2024-10-26 04:19:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b845093-c29e-3215-bb0a-b8922348ecc0 | -1.53262 | -47.29349 | 2024-10-26 04:19:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0adc6871-31dc-372b-a176-0d7d656399b0 | -1.53177 | -47.20173 | 2024-10-26 04:19:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e1affbb1-aff0-399f-a05a-c326c0c6f68a | -1.53106 | -47.20618 | 2024-10-26 04:19:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0670549a-3492-3c86-bd0e-f6f65257d406 | -1.05388 | -47.63975 | 2024-10-26 04:19:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8305e7c-5de7-399d-8180-f0311a87e43d | -5.71181 | -49.29959 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4499e589-33d7-37d3-9314-22230827d409 | -5.66027 | -49.10497 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6cbe147a-5a9a-33a3-ba0c-1cf14a36c3c3 | -5.51384 | -49.28915 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e368778f-a93f-3f2a-9090-d2e6992bfd46 | -5.4951 | -49.50344 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c484ee59-2d6b-36d5-82ad-62116031da2a | -5.49451 | -49.50703 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb01a705-eaff-3ab3-8268-918a2a022e79 | -5.49379 | -48.94974 | 2024-10-26 04:19:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cad3ff94-e4d8-3daf-a972-2a3be9200fef | -5.30112 | -49.49692 | 2024-10-26 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3b28906-5d78-385b-9e8a-94b6f20e1c09 | -6.40663 | -48.34846 | 2024-10-26 04:19:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aaba585-4509-367c-a535-8a37a672430c | -5.51054 | -48.08611 | 2024-10-26 04:19:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ec111b3-4202-3161-a89b-08894fdf37a2 | -7.8768 | -49.60404 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 946324dd-a483-3551-87ec-c96bae805413 | -7.81035 | -48.62508 | 2024-10-26 04:19:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b05c8cf7-f3ea-3629-a8c9-169b1efaaee7 | -7.80971 | -49.25856 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec4c34b-7873-323b-8f2b-a98b29377837 | -7.72578 | -49.54372 | 2024-10-26 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efff6799-9ebd-3bbf-81d8-570b80e277be | -7.69854 | -48.52979 | 2024-10-26 04:19:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11bd1acb-b504-3e8d-bf70-2c68498d6431 | -7.29672 | -49.28651 | 2024-10-26 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d10040f0-c87d-3c26-b24c-890745143d09 | -7.29585 | -49.28896 | 2024-10-26 04:19:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d14e7a99-c682-3998-b4c7-9d1bedcd9394 | -7.13944 | -49.51094 | 2024-10-26 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09758cf3-1a47-3ab2-be41-f225caa93d4d | -7.13453 | -49.27213 | 2024-10-26 04:19:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11ae0928-38fc-3baa-9d8a-0d9465fe603f | -7.12091 | -49.13881 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2bdbb7fe-4ee5-3114-ae24-252fe6d8af51 | -7.11704 | -49.13814 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6165f20c-49f5-3f90-a385-97ed59a11077 | -7.1032 | -49.12575 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a7e1981b-293d-39d2-85f2-6500ee42d4f1 | -7.10234 | -49.12876 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efc5174a-33fd-3ec9-a999-7f4b676bead6 | -7.09994 | -49.14342 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 106e9daa-e898-32e1-9c22-dc1e8cdbf00d | -7.09987 | -49.14526 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e8d1025-ca1a-3877-a908-ea6a8978f9f8 | -7.09607 | -49.14273 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dcaa82e-3e61-3241-90f2-4e9fcf923a58 | -7.096 | -49.14458 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7141f0f-69f4-3e1f-b8d4-da196671e339 | -7.09299 | -49.13719 | 2024-10-26 04:19:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98863911-e0c5-39e4-a023-60a4d8105c24 | -7.03191 | -49.28851 | 2024-10-26 04:19:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fca685b3-dbda-3b5b-b18f-1f97039570d5 | -6.75792 | -48.76975 | 2024-10-26 04:19:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77d71466-95b6-39b0-88c7-6945e83cbad6 | -6.68816 | -48.7515 | 2024-10-26 04:19:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c91bd9c8-9375-3e94-887d-450d8c2212e7 | -6.68435 | -48.75085 | 2024-10-26 04:19:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39233184-f1b2-351d-ad13-0a74e36a89e7 | -8.18579 | -49.50251 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e9db645e-5f61-3034-b207-2ac400cc861f | -8.14124 | -50.08752 | 2024-10-26 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dc437e8-9771-3c44-a467-f2a7b877edb6 | -8.0627 | -49.37827 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a78988a-2545-3949-98eb-a64f73615ce5 | -7.99033 | -49.69294 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8e6fae1-0e13-39fe-9252-4e195c83bd69 | -7.98844 | -49.69446 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ce62f5ff-9aa2-33a7-a76c-4edad54c5681 | -7.98636 | -49.69227 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e18728cf-a820-337a-ae80-e093a2aed1a2 | -7.98552 | -49.6974 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cd86c4f-5a90-3c62-b36d-52432304518d | -7.98447 | -49.69382 | 2024-10-26 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README54.md)
