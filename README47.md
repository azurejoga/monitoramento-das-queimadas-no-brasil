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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55caceaa-faf9-3079-a0d2-b426a29e6264 | -14.9895 | -44.4022 | 2025-09-22 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 9c08a75b-51b3-3934-9fe6-c5f01371986b | -14.8484 | -45.4613 | 2025-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 292.8 |
| a9e2c140-64f7-397c-bd9a-6d5d43637ae6 | -11.215 | -49.6224 | 2025-09-22 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 876b1f06-6464-3dd1-916b-c786f4393a08 | -8.5185 | -44.9291 | 2025-09-22 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 27e20a1a-06a4-3766-ad69-01be77920e4a | -14.99 | -44.3784 | 2025-09-22 13:50:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a2d50233-18f2-3b79-a4d1-15ca332b003e | -10.2617 | -46.0929 | 2025-09-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| cf1d71e2-1751-3cbb-a013-34969a5ecf0d | -14.4721 | -44.8532 | 2025-09-22 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| a6fdb295-7d73-30b8-bded-8918c831a34d | -12.1348 | -44.7809 | 2025-09-22 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 235d0394-399c-381c-8263-1ea752e66a3a | -12.4186 | -45.0153 | 2025-09-22 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 6025ef43-0ca9-388a-9004-c8cfcdcaac02 | -11.6446 | -44.32 | 2025-09-22 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 24107e46-ab25-3a63-bcb2-9dcd3e49db20 | -12.3399 | -44.0946 | 2025-09-22 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0531f145-b40e-3523-b231-27eb4c1d826f | -14.8361 | -45.137 | 2025-09-22 13:50:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| dead4456-0195-3f57-880d-cdd8705443ec | -12.0771 | -44.7898 | 2025-09-22 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 39c98613-1bea-3f28-ac6b-260e0d17ee9e | -12.0963 | -44.7868 | 2025-09-22 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1df06549-cb31-3427-96dd-12e01707d3af | -10.2621 | -46.0703 | 2025-09-22 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ac770f92-da01-35e5-aba0-cfd0b8737b29 | -14.9699 | -44.406 | 2025-09-22 13:50:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 131.2 |
| af773488-e1f2-3180-93f3-9e0a2ed59734 | -11.2153 | -49.6008 | 2025-09-22 13:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 7d2de6df-add9-3e9f-9e05-3f3c4b95a78a | -10.0371 | -47.1952 | 2025-09-22 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d3d304a9-bd6a-3ac3-824f-3cc590003b96 | -9.1937 | -45.2886 | 2025-09-22 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6c182616-7a97-3f79-bbc3-8e7595bf8ed2 | -14.4726 | -44.8296 | 2025-09-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 72eff37e-991e-3f32-8c4c-1ae76df6e4d8 | -11.4674 | -43.5248 | 2025-09-22 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1857f843-b3f1-3066-8c33-0297a11e59ae | -12.1156 | -44.7839 | 2025-09-22 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5ea7197e-66c9-323c-8786-38da3a4c6d77 | -5.5959 | -42.1478 | 2025-09-22 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 626d3840-0177-315d-b1c8-220baeca3657 | -14.8484 | -45.4613 | 2025-09-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 5a26e477-bcd3-3822-8549-fad2e748202a | -12.0771 | -44.7898 | 2025-09-22 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 9cbab055-df5b-3261-988d-80a592270ce4 | -10.3382 | -46.0609 | 2025-09-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0ab0a06a-3b38-3de5-bf32-052bae8e4b6d | -11.6247 | -52.8624 | 2025-09-22 14:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 1be26253-3866-38ca-82fb-f010ee06a8b8 | -14.4721 | -44.8532 | 2025-09-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| aff5a007-6f18-38ec-bf8a-7450b99500eb | -11.7687 | -44.8826 | 2025-09-22 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8ebff15a-101e-3d0b-8052-7f3223b441c0 | -11.435 | -50.1571 | 2025-09-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 3fd833e9-960e-3ff8-b218-5c025a8f462f | -14.989 | -44.4259 | 2025-09-22 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 08a4f04f-d01b-36ed-9218-43d50a73a92b | -5.5585 | -42.1269 | 2025-09-22 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 8187ac95-ad25-3603-b140-16697c6b8d9c | -11.604 | -50.288 | 2025-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| dc2c7359-d2f5-3883-81e9-8f49cb5d16ce | -12.6663 | -45.1385 | 2025-09-22 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 38a1afee-3670-30d6-8fca-7a85e27d796c | -8.5377 | -44.9041 | 2025-09-22 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 410e9f09-8d42-310d-ba7c-8dd16124a0f9 | -18.5983 | -45.0287 | 2025-09-22 14:00:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 78497647-8c64-3069-ba30-2fc2179a55c4 | -12.647 | -45.1415 | 2025-09-22 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 95f5519c-ecfb-3bd4-a090-e0d93972ad01 | -10.3572 | -46.0585 | 2025-09-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 37ff7dfb-5bc9-352f-8273-e0a9fcad4d59 | -7.5272 | -44.3413 | 2025-09-22 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d92a2e30-badd-36df-8638-7d97999c9045 | -11.467 | -43.5485 | 2025-09-22 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 705c459b-aca1-3789-bc57-ac7a75f29dfa | -12.4545 | -45.1486 | 2025-09-22 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0e2ff683-40b4-3b30-a9ae-f42cc5df9a3d | -14.9895 | -44.4022 | 2025-09-22 14:00:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 248.5 |
| f2535ef8-4d92-3df2-9df3-ea586f721df6 | -12.0767 | -44.8131 | 2025-09-22 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b201da61-d92f-325e-96e2-ef81aaf5b002 | -11.4862 | -43.5456 | 2025-09-22 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d6fe332e-d193-3e30-beb1-5b3edcc29730 | -10.3378 | -46.0835 | 2025-09-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 68de87ad-03f9-325f-884f-baa81ef06bf2 | -11.9301 | -43.405 | 2025-09-22 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.0 |
| c6b96d60-3e93-3497-b2bd-54e06ce77bda | -14.2613 | -44.7041 | 2025-09-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 265.4 |
| 0878b404-9a19-3a73-b5c1-1c2d9f72b092 | -12.6474 | -45.1183 | 2025-09-22 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| cce5cb94-9842-3328-9442-8f50e1116d4c | -11.6446 | -44.32 | 2025-09-22 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| b481b24f-9a30-3970-8487-28fbf0c2b65c | -11.585 | -50.2902 | 2025-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| fce45059-cce7-322d-a16c-a183d572179f | -11.9296 | -43.4288 | 2025-09-22 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| a1ddec78-dcc7-3fea-8fde-718edb7fa7d4 | -5.3711 | -42.0937 | 2025-09-22 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 4224d518-083c-350b-b3c4-2aecef1c45cf | -12.0963 | -44.7868 | 2025-09-22 14:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 9fd700ab-cf92-3275-8fac-1253d1d57dbb | -8.5374 | -44.927 | 2025-09-22 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 6e5863ba-b16c-3545-9c93-1c8d9761600a | -11.6442 | -44.3434 | 2025-09-22 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 241.9 |
| cf17f3ef-ce52-3dcf-80c5-3cb72376e6c6 | -12.1348 | -44.7809 | 2025-09-22 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 98594cd0-b715-319b-92a0-96ebac8506c3 | -5.5773 | -42.1255 | 2025-09-22 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 96d06d40-9f16-3fad-a4d2-064d5df55763 | -14.4917 | -44.8496 | 2025-09-22 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 4f7bf18b-4120-3f5c-9ce7-d322cc0f3b92 | -14.8361 | -45.137 | 2025-09-22 14:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6cc97ddd-749e-32f7-b25f-aff9162ab842 | -14.9699 | -44.406 | 2025-09-22 14:00:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 07c23ab1-8b53-333c-b633-1d7eac0d9810 | -12.3592 | -44.0915 | 2025-09-22 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4d8f259f-725b-35f5-a903-7862a8baee6c | -5.5583 | -42.1507 | 2025-09-22 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 4e8e2308-5b96-3b42-bc4f-bb3a5ca743b2 | -14.4259 | -60.2984 | 2025-09-22 14:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 9e58344a-0457-31a7-9171-4f12e161e2c7 | -11.4482 | -43.5277 | 2025-09-22 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e694add4-b4cc-34b6-9677-e49ff56382a7 | -12.0963 | -44.7868 | 2025-09-22 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 237fb72d-98eb-3cf3-aeac-9f1cf77d46be | -8.9911 | -46.3059 | 2025-09-22 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| a2a26be3-d056-33ea-999f-e868fa3afb53 | -14.4726 | -44.8296 | 2025-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 57f02d58-e6e2-3cab-b873-2015bc38ea5d | -10.3565 | -46.1038 | 2025-09-22 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 97b41e96-2b27-37b0-9a4c-9a403fcb5abb | -4.1382 | -41.5557 | 2025-09-22 14:10:00 | GOES-19 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| ea32c09c-35a1-3808-8172-c16467aeec25 | -5.5395 | -42.1522 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a6783479-e03c-35b5-94de-c1222955c9f9 | -14.8484 | -45.4613 | 2025-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 2eb7763e-b229-3e4f-a4b2-a2b695125240 | -12.647 | -45.1415 | 2025-09-22 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| ebecc128-4aad-3408-9a90-c33390ccfd40 | -14.4721 | -44.8532 | 2025-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 2469bec5-3a3c-35bc-a67a-aaeee3db8a53 | -5.5773 | -42.1255 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| bd7c96fe-1e6a-3730-834c-5e5cd979f5ad | -14.9699 | -44.406 | 2025-09-22 14:10:00 | GOES-19 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 255.1 |
| 58b16d48-b64a-32b1-a6fd-74f559752f14 | -5.5583 | -42.1507 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 1e1f446f-0c16-3cbd-9568-f757f157a35d | -12.6474 | -45.1183 | 2025-09-22 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 0ed7ad07-5d1c-3c42-85da-f7e89db9ded2 | -11.6436 | -52.8605 | 2025-09-22 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 150.5 |
| d9a6469e-3e20-3543-a686-474d2ab9a4bb | -11.4482 | -43.5277 | 2025-09-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f5f15eb0-f502-3d8e-85ba-82bf0e8fe989 | -5.5771 | -42.1493 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| f3559254-f43e-3879-a31f-21ca5e810c3b | -8.9402 | -44.4688 | 2025-09-22 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 91de745b-a063-3224-963e-f38947e68818 | -11.9301 | -43.405 | 2025-09-22 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 4c8c592e-1020-3ffc-b15e-9ccc4ee2fade | -12.3592 | -44.0915 | 2025-09-22 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b568ce07-7c89-3075-8289-fa4560cf8969 | -11.435 | -50.1571 | 2025-09-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 31b13700-4e7e-35a1-a296-6c7017d657a2 | -7.5084 | -44.3431 | 2025-09-22 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c7c0d50b-106d-3d5d-abc9-ffa60effed08 | -14.989 | -44.4259 | 2025-09-22 14:10:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5176c585-f344-39e7-b4dd-bf12d67310aa | -18.5983 | -45.0287 | 2025-09-22 14:10:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 246.6 |
| 472e3455-dc01-3a73-90b2-e9758f9e9ecc | -11.467 | -43.5485 | 2025-09-22 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 5360b722-d42d-3cce-8cfb-f2b9d9d95051 | -11.9296 | -43.4288 | 2025-09-22 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 3e4ca024-b7f3-39eb-9d8a-73913d5924cd | -14.8675 | -45.481 | 2025-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 6b6cd452-27ab-3b7e-a9c3-628d14f74710 | -12.6088 | -45.1244 | 2025-09-22 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| eeba7b8a-48e4-37d3-bb6d-311503dd70e1 | -12.0771 | -44.7898 | 2025-09-22 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 379fa724-2d7f-35ff-bd02-27fdb90d073f | -5.5959 | -42.1478 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| b4192eb3-9aea-3f15-a387-859518af02d7 | -5.3711 | -42.0937 | 2025-09-22 14:10:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 100.6 |
| dc68a158-3398-3ebc-8591-e7e38c2597f8 | -12.7722 | -47.7337 | 2025-09-22 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 02690ef9-1202-3fa6-9581-ec643b3fbc7d | -4.8638 | -42.2252 | 2025-09-22 14:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| d2a6aae7-5201-366e-b026-2166ea0f1e0f | -11.4731 | -51.4734 | 2025-09-22 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 7b12f29f-f903-3582-90e3-c92f9d2246a8 | -11.6247 | -52.8624 | 2025-09-22 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| a20aecc0-a532-3a22-9998-34e38af224cd | -11.6249 | -52.8416 | 2025-09-22 14:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| f724bcad-6435-301b-8adc-ef32e5aac2cd | -12.0767 | -44.8131 | 2025-09-22 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |


[Clique aqui para ver as próximas entradas](README48.md)
