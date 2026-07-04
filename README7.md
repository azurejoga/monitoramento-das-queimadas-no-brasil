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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c5f3dfe-fb73-37c9-a037-8a65c7486011 | -11.42276 | -46.58061 | 2026-07-04 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56e3d22f-86cd-3cfa-bbb5-9a3378465272 | -12.75836 | -44.56372 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 139ef6be-d017-31bf-a75b-075ddcec3e29 | -12.75767 | -44.55762 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 91ec4f05-112a-331a-94dd-c6d59c85ceee | -12.73402 | -44.56338 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22277470-8a53-34f7-9c41-78051cb51e67 | -11.92339 | -43.39035 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| addb3328-453d-3c52-b648-191be3898984 | -11.92282 | -43.38773 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5dda2c0-d2d7-3a15-bdb8-0e5e94861c93 | -12.73925 | -44.53731 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4954206b-6c79-39bd-9a1d-203e2f082493 | -12.74182 | -44.52448 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3758892-47f3-3c1d-b1f3-025395cdd8ca | -12.73663 | -44.55034 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94847d3c-fc6d-3a8f-a8ff-78240b915b13 | -10.92732 | -43.05885 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fba63b62-3d5f-3bd3-8570-686393b9c2dd | -11.42147 | -46.58681 | 2026-07-04 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b362d9e-0277-3cf1-a9f8-af192f60565b | -12.74595 | -44.53427 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa081821-6211-3681-977e-5ff1177d7fec | -10.92869 | -43.05152 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| ca9ca0d8-dfda-3da7-8d71-8813799e9f9e | -10.93372 | -43.05209 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 6dadb14d-f3b3-38fa-bf0c-5284f0c1c4c5 | -12.76261 | -44.54238 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a43664d7-afcf-3b0a-a86e-2662bb606b54 | -10.93007 | -43.04417 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0ee10a97-8e30-3746-8b71-dbcdd61b2527 | -11.91731 | -43.38652 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f975b0cf-b9e0-3aca-8124-5b64262d928c | -10.92458 | -43.04302 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| f82f3a33-f2b0-33dd-8259-7c78092e15ce | -11.9186 | -43.3854 | 2026-07-04 03:42:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dd36e98-12de-3ed8-bf04-c549fed59df9 | -12.75678 | -44.54107 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 886e857e-ae9f-3890-94d1-e37bc8e5b920 | -10.92388 | -43.04671 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 61309322-f171-38db-b0d8-75efe344e06e | -12.75508 | -44.54958 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 791e63f0-8736-3279-b086-b565e272c932 | -12.75349 | -44.52702 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad94b8d8-7c1c-3cff-8191-c0ec03cadbe5 | -10.92938 | -43.04785 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 5ee64526-45f6-3795-8322-74923b0e6f17 | -10.92751 | -43.05465 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 89a8e610-5c48-31c2-9317-a2d701624ec5 | -12.7603 | -44.54487 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 933f4729-8eb4-370a-8702-41f049483041 | -12.75264 | -44.53128 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 422389da-9b2b-3466-a748-f637e5eef6f2 | -11.43863 | -46.57205 | 2026-07-04 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce0cb5d7-bd47-35bb-b60e-5e99fea76d23 | -12.73988 | -44.56457 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0757ae4e-2154-31e7-ac29-d866d2ef63d0 | -12.7475 | -44.55698 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a93541ab-b675-3ae8-bbca-ba2ff65b6149 | -12.7451 | -44.53854 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 924b0279-0c05-3266-a012-18fa286be7d8 | -10.92416 | -43.04251 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 696b14c6-51cb-3ff9-b2c3-c8b1cdd486bd | -12.75943 | -44.5491 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 45102f39-7236-31b3-932d-0af3cc83cabe | -12.73838 | -44.54163 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed0588f0-7894-3ced-a6b7-0e0123b3bf81 | -12.74337 | -44.54715 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1109485c-ba1c-30d1-aa7e-edd692e8b1b7 | -10.92319 | -43.05038 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 3bb33087-e765-3325-8542-6234fcb09d9a | -11.42042 | -46.58708 | 2026-07-04 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c336093-bd24-39c3-82b0-627d855e6455 | -12.35328 | -47.909 | 2026-07-04 03:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c7a83ef-79aa-38e7-b1c9-571c9b76e496 | -12.75435 | -44.52274 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ab8d3e2-02fc-301d-96ac-b562e4134e9b | -10.92822 | -43.05099 | 2026-07-04 03:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 68b0aaaf-bfdb-3739-a36a-259490e74fc1 | -12.75094 | -44.53979 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 3c442832-55de-369a-a0cc-4f3060d65264 | -12.76117 | -44.54066 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8f702d8c-ac1d-339f-b327-354246fc285a | -12.7468 | -44.53001 | 2026-07-04 03:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0a61ad5-4af8-3932-a871-abdeaab32051 | -18.71691 | -47.54227 | 2026-07-04 03:45:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 800a0d3c-4625-38bd-8429-165c5459a0c4 | -18.71816 | -47.5369 | 2026-07-04 03:45:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30a21606-42bd-3549-9937-37d2edc945ed | -18.51985 | -42.72742 | 2026-07-04 03:45:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9003369-56d7-3e4a-8ab0-277b36ab7771 | -20.44273 | -44.86256 | 2026-07-04 03:45:00 | NPP-375D | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce15e529-5cff-3757-91dc-e6997a7a9651 | -18.77033 | -47.62613 | 2026-07-04 03:45:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d30f6f8e-bc6f-3b19-932b-fca7682748f3 | -21.90131 | -48.49018 | 2026-07-04 03:45:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c1de38a-5304-34d1-926e-a8ce9aa9e830 | -18.51881 | -42.73265 | 2026-07-04 03:45:00 | NPP-375D | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c801c3e-0017-311a-8d94-58416a3f5096 | -21.29571 | -41.44315 | 2026-07-04 03:45:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a804a60d-c674-3e81-a633-7be19fd9ef5f | -18.77656 | -47.62784 | 2026-07-04 03:45:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb39711c-a2bb-3669-a26d-91c7ff196bf7 | -20.44619 | -43.53253 | 2026-07-04 03:45:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b25a9faf-c407-37fa-9d05-f6773dfff849 | -18.71609 | -47.53591 | 2026-07-04 03:45:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ae7250e-71f3-3aec-afac-8b40730960d6 | -18.7149 | -47.54123 | 2026-07-04 03:45:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1b10094-476e-3e21-b768-b0919ec09128 | -20.44608 | -43.52921 | 2026-07-04 03:45:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7f8094c3-dc31-3235-be47-4c90d6d43c71 | -19.69816 | -47.97042 | 2026-07-04 03:45:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a077d0e2-d024-3e90-a322-68a446bcd513 | -21.20265 | -48.60349 | 2026-07-04 03:45:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6fc484f1-3e74-3416-ac02-6efb3b07002d | -21.29488 | -41.44754 | 2026-07-04 03:45:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f1cd8390-a333-35e9-9293-1ecddf74f5de | -12.7553 | -44.5194 | 2026-07-04 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 5e224889-c2fa-350c-a54b-8c573ac6373b | -10.9209 | -43.0384 | 2026-07-04 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 026f0c32-b6d1-3731-a02d-92b5de9e58b7 | -10.9397 | -43.0593 | 2026-07-04 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 2b0456bf-62a1-32de-a818-d1c5edbf52be | -12.7548 | -44.5428 | 2026-07-04 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| da111a47-a14a-3f76-976e-988d278e3cce | -12.7741 | -44.5396 | 2026-07-04 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6f5eaeb6-18d2-361d-8c64-1c1f0adbfd29 | -13.2401 | -54.351 | 2026-07-04 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| f27cb583-f304-3356-b83a-78d5eb1df0bb | -10.9205 | -43.0622 | 2026-07-04 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 23e09be1-9a40-3ed5-93bb-96ea53942a5c | -10.9401 | -43.0355 | 2026-07-04 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 65e51cb3-4fa3-3775-a66d-12296aa9510a | -13.2592 | -54.3489 | 2026-07-04 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| a38e7afc-0a5e-3fce-b985-e4efc45e0730 | -13.2404 | -54.3303 | 2026-07-04 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c5e7704d-18cf-3ede-a7d9-b3d616bc7876 | -13.2595 | -54.3283 | 2026-07-04 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 139dcf72-4186-3ed7-8632-bb58fb229713 | -4.14567 | -48.83974 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d745b23-cfb1-3e5a-9fd7-d0c959993803 | -4.57544 | -48.0281 | 2026-07-04 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98d77ba3-849a-3b18-996b-012b079ae317 | -3.50716 | -48.03696 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb3b80eb-bf21-3218-a522-d607a141450f | -5.31603 | -43.56841 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 469d4013-96fe-3b69-8626-7bbc4f502e6d | -3.41598 | -41.7005 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b745e71b-bf35-3edf-b254-b2ea9bcdb172 | -5.79732 | -43.63255 | 2026-07-04 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a220590-81c3-343a-aa29-3d2800071955 | -3.42578 | -41.71149 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37ffaf0a-a440-3a67-b7f1-cf1ddfb74292 | -5.90598 | -43.85726 | 2026-07-04 03:57:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2395efd3-fffe-32d1-854b-fe8727cca976 | -4.1464 | -48.83543 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfdd23d9-b568-37a2-8174-55515135ee64 | -4.77019 | -46.39824 | 2026-07-04 03:57:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb1e8e13-b399-3695-805c-86de135a6372 | -6.42948 | -43.72171 | 2026-07-04 03:57:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea7f263c-9417-36f0-b4da-a0e92f9adefc | -4.38958 | -43.31927 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e86d40e0-bc17-3952-a4b7-aa1c1dd63621 | -5.14713 | -37.91315 | 2026-07-04 03:57:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1f442356-c069-30c3-a00a-225f940b447b | -3.50509 | -48.04117 | 2026-07-04 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 615a0770-26c7-3d5e-b32c-0e66ff391180 | -6.19479 | -45.75616 | 2026-07-04 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dddbedc-4a60-3dc7-9313-5822df6599f7 | -5.79262 | -45.06062 | 2026-07-04 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45cf6cf4-57bd-332d-9157-d6b9b8ca7d50 | -3.99444 | -48.39327 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff1f5ee3-f985-3c49-96cc-0ee891f1ec0d | -5.31727 | -43.56089 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 85a22362-6c05-3d9a-a844-e47050bf5725 | -4.73803 | -41.98847 | 2026-07-04 03:57:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 798d7e39-d3a8-3cae-a44c-708920b691b9 | -4.34188 | -48.95865 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 481098e4-60cb-38f6-b314-7189c323a969 | -4.39139 | -43.3082 | 2026-07-04 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca858a39-e661-35c6-b6ac-da7e51e7dd35 | -5.31788 | -43.55721 | 2026-07-04 03:57:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1a621cd5-20a1-3a73-907e-984b21767823 | -3.42052 | -41.72002 | 2026-07-04 03:57:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2a477a15-3e70-3194-9ab8-a7161994d8c6 | -4.34849 | -47.76268 | 2026-07-04 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7539bf4d-02ed-3da3-933d-5fa57f980287 | -4.57611 | -48.02419 | 2026-07-04 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6a18e02-a63b-308d-90cd-87d2292b322c | -4.85341 | -45.33221 | 2026-07-04 03:57:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23a88245-ed63-3f2f-94c3-d3e7579e87dc | -5.41854 | -45.29168 | 2026-07-04 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 258eb4cc-e773-3fed-b80a-56f497c0df78 | -6.19565 | -45.75125 | 2026-07-04 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f620093-b848-3c6b-9e79-971c01a8c353 | -4.14261 | -48.83675 | 2026-07-04 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4a4b3bba-18d4-3c8d-bf9e-68f4be0078e2 | -4.28686 | -48.35566 | 2026-07-04 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README8.md)
