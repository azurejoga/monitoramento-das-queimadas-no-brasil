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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8d097e6-8b0d-3669-beb6-97cc9e7180c3 | -21.83743 | -48.38404 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fac2a4b8-de83-3757-ac87-e8be4cd1d7ab | -21.83684 | -48.38837 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 388f72c4-46f5-30be-a912-40ef02770fe1 | -21.83623 | -48.39277 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 24.5 |
| d5dd0fd6-22d5-3b7e-b289-f5a22d019720 | -21.83563 | -48.39713 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 742f7706-0744-308e-b009-38bba0cfce5d | -21.83504 | -48.40145 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| b71a4235-296b-36d4-bd31-235154d1718d | -21.83444 | -48.3792 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91841d60-db95-3bdf-a91e-df977cea51dd | -21.83385 | -48.38352 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9125acd-ea87-36ad-88bd-2fea17f61ccd | -21.83325 | -48.38786 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5d9a3dc2-7a75-352d-b156-2380472d019f | -21.83265 | -48.39222 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 106aab35-f54b-34c8-998e-f8389cdb8950 | -21.83206 | -48.39657 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 64890170-de11-3c48-b904-79bd4c1c973e | -21.83086 | -48.37864 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d665f13-c130-3abd-9904-24f2c5a63b21 | -21.82907 | -48.39169 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 090159d9-34df-30a0-9bcb-39eb47fc3017 | -21.82848 | -48.39602 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f88d718f-9765-3861-b266-d780ab8ad098 | -21.82789 | -48.4003 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0c9b1a3a-7a2f-37c1-a8a1-8637123c36ed | -21.82788 | -48.37373 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f9b411e-d5f1-3cfc-a9e8-2281c8c974b9 | -21.8243 | -48.37318 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 15f1dab8-5d69-389a-9c97-859a17d59822 | -21.82072 | -48.37262 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baf359ff-37e5-33c8-b224-ed620e9811f3 | -21.81301 | -48.40228 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcdacf20-aa91-316f-aee3-fe018d49d69a | -21.81086 | -48.40382 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0a9f2af-1c27-3dc8-a858-88f08baf9422 | -21.81056 | -48.36661 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5a80d63-e8ab-337c-a573-016fe27b3957 | -21.8097 | -48.38614 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e9a3b7c-0fee-38a4-b4cd-9259d392c137 | -21.80943 | -48.40174 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 589433aa-1f48-3c63-86f3-4574b4f326f1 | -21.8091 | -48.39041 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24476f77-a955-35ba-99a9-0dc59d9f2cb7 | -21.80857 | -48.36823 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92dfb629-52f3-33dc-b1f2-f2d38b62c8b1 | -21.8082 | -48.38403 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7bbd8f69-ed9e-367b-9d82-0e106585a85a | -21.80761 | -48.38832 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2292d794-4bb0-395b-81b7-1fb835dc61c2 | -21.80728 | -48.40331 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d144925-9efc-33d0-ab19-70fee09a5039 | -21.80613 | -48.38558 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2d675597-fbea-3406-aaf3-ca7f7541fdfc | -21.80561 | -48.3633 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aebd0ddd-b204-3010-b42c-3deda68f6510 | -21.80552 | -48.38986 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 339bf2ce-51f2-3a7c-a47d-1e9057fa4ce1 | -21.80499 | -48.36768 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cf17725-bc1d-3667-ba89-9cb17ca706aa | -21.80437 | -48.37206 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b8960f76-e064-391d-b422-5da150287d6b | -21.80195 | -48.38928 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc968d61-b796-3312-a47a-217e56e1be05 | -21.8008 | -48.3715 | 2024-10-04 04:36:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19cf9c57-38b5-3b48-9aac-769cf389128d | -21.79958 | -48.38012 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83fb812d-8436-394e-b84b-d36039285952 | -21.79898 | -48.3844 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f07d44c6-075e-37b6-9caf-baf2cb7d3a26 | -21.79777 | -48.393 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7acec83-0e32-3884-806c-4d11c1639d57 | -21.79661 | -48.37525 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e27f96b3-ed1d-35aa-bd4c-2767dbb44ea2 | -21.79601 | -48.37954 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8710fc6-4366-3d45-ac7a-3ab7c0396233 | -21.79541 | -48.38382 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bb8efaa2-56c1-3a09-8d65-85d67bbb78a7 | -21.79481 | -48.38811 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3045b1fa-d5e5-3a47-a69e-807952238305 | -21.7942 | -48.39244 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8da924f-cc98-3c8e-be3b-3333b2bfe8bb | -21.79243 | -48.37899 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5afcc1d0-77df-37d0-aa7a-b976f83a1a16 | -21.79183 | -48.38327 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa54eb0f-7fe3-3f3a-9fd3-eb4dbab04407 | -21.79123 | -48.38755 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 969773ce-983c-381b-9ac0-0ff02f458f73 | -21.79062 | -48.39187 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f325ae01-4e5d-31e8-b0ae-3e1e181f4aec | -21.79001 | -48.39621 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e84becf1-db60-3377-9c4b-464c00e63ee4 | -21.78885 | -48.37844 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a849ff28-836f-3caf-9fbc-8bf5bcf57281 | -21.78825 | -48.38272 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16c64cf2-0eae-3a80-9562-25ecf11cefba | -21.78765 | -48.387 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0815830b-d788-3dfc-8765-ea8bdf959956 | -21.78705 | -48.39131 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40df285b-a9e1-3f56-a643-ae131b72c00a | -21.78467 | -48.38218 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f69814bd-daba-3c84-a495-c04726d9d641 | -21.78407 | -48.38646 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 127e9f8d-857c-3b35-9b56-141fecbd496e | -21.78347 | -48.39076 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7dde109e-07ce-3063-b1a1-f3374cb337c7 | -21.78287 | -48.39507 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c758d38f-5def-37cc-8589-ceb0ec185111 | -21.78169 | -48.37736 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcbdbea9-f6b2-321c-ab87-cc9ff883fc9d | -21.78109 | -48.38164 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7adc551-e575-315b-908b-4a23dfac3bed | -21.78049 | -48.38592 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bfa3b45-3c2c-31ef-a704-e0bf27ba2402 | -21.77989 | -48.39021 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ddd1e4ff-f4b3-368a-bf0a-68d6d220684d | -21.77929 | -48.3945 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 48329592-03f7-3f6f-a450-beb424f52a1b | -21.77811 | -48.3768 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e8dc565-7d77-3ca8-bba1-36fdf5e5697f | -21.77752 | -48.38108 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e43786ab-9754-331d-b312-4f07d8be77a9 | -21.77692 | -48.38536 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3a459ad-01b2-3c87-9d9c-91697a80a0cf | -21.77632 | -48.38965 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 889dd66a-85bf-3b8f-b8ca-d39d4241e31d | -21.77572 | -48.39395 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 599bfb41-7da8-3751-a3ac-146bbb44668e | -21.77334 | -48.38478 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1d5f6aa-21e8-361d-a55b-a204074e32f5 | -21.77275 | -48.38907 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 80f88e87-914f-3b76-a12b-d3df84a75f05 | -21.77214 | -48.39338 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4adc8ba4-6b08-3c38-95e1-e5373d24e8df | -21.85829 | -48.41826 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f76c5b0-aa6b-36ce-8154-2cc469aa9c3d | -21.85472 | -48.41766 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5d103a1-b6ff-3c0c-8326-a60a58ba4c48 | -21.85055 | -48.42139 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec966024-97f1-349f-b909-40f104434495 | -21.84995 | -48.42567 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 075134c9-e7bd-35b8-b147-ad0ec78ee2c8 | -21.84936 | -48.42997 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c927ee2d-2982-30ed-ad77-fea578e686a1 | -21.84816 | -48.4386 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08e24f4d-a291-3aa5-b2ed-10f96639626c | -21.84756 | -48.4429 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7e5c488-c468-340a-bbe6-8a4492003a5e | -21.84698 | -48.42081 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61825c53-8ba2-3756-bd11-d3e46114d144 | -21.84697 | -48.44721 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aab79663-ff77-3a60-974d-05bc1607fd77 | -21.84638 | -48.4251 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 700d80c9-3605-38e9-9274-cfa16cfc2ae1 | -21.84579 | -48.4294 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0222e1c6-9896-3e36-89f8-da5030ae1317 | -21.84519 | -48.43372 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cf06d67-7951-3492-a7db-d3d5642e138d | -21.84459 | -48.43805 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 945b06dc-e4f8-3b8a-82a8-cbcb9b6ec7db | -21.84399 | -48.44237 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c539c403-b6d7-399d-986d-4b66a074cbba | -21.84339 | -48.44668 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab3471eb-338c-35c2-ad9e-ad25d4c39d9b | -21.84281 | -48.42452 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d66286d-c9d6-38c3-9a7a-3c54f20e66f3 | -21.84222 | -48.42883 | 2024-10-04 04:36:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c23df57d-3192-3efe-83ca-b42b45e0a97d | -21.83981 | -48.44621 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f42200b-006f-3898-bd0c-375648e1147b | -21.83922 | -48.45047 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aad10ef4-3a2a-3649-ae07-eaa4b8286fa1 | -21.83864 | -48.42826 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21ecc46b-353d-37ff-abdc-3ef5071bec03 | -21.83507 | -48.42773 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53cef2fa-6ea1-3cae-af53-c2e211d1973c | -21.83506 | -48.4542 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81b14688-0864-3f74-a733-5bae58991989 | -21.83149 | -48.45367 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b11094e-1575-3992-a69e-87699c8c049b | -21.83089 | -48.45798 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33a965f4-c981-3387-aa7f-68b1b8744976 | -21.82732 | -48.45744 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bc9593b-f656-3a4b-a5d1-e28b6556c462 | -21.82376 | -48.45688 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d9ad3b8-0dad-3374-b992-c15eb7ff46b7 | -21.82078 | -48.45202 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30eb4a49-9fd2-3bbc-95f8-28903ef0aed0 | -21.80353 | -48.44495 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8b3a250d-c07d-36d4-9b15-9a40dc10e2a0 | -21.80179 | -48.44212 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b22df34-b25a-3db0-acfc-daba95d8f855 | -21.80119 | -48.44641 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c6e111cc-14bb-37cc-b057-728751b4a2b4 | -21.79996 | -48.44439 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 410781da-3fe9-3424-b30f-09d4a7b3642c | -21.79762 | -48.44585 | 2024-10-04 04:36:00 | NPP-375D | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README135.md)
