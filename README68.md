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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02da0478-9f7d-3396-9e5a-caa5afb4573e | -11.211 | -47.3872 | 2025-09-17 14:20:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c6786b23-b69e-3942-afbd-196b3d510f28 | -9.4935 | -48.2679 | 2025-09-17 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| f5e80911-5f15-3bce-b375-4885a9c5f258 | -12.729 | -48.0068 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 8c125103-8ecf-3810-87ee-35efb826579a | -7.6386 | -44.4686 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a0043cea-def5-3f52-a14f-b11d8432748b | -5.786 | -43.9147 | 2025-09-17 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 4f73bb4f-6260-3921-97a8-03ebbdcc5063 | -6.8734 | -43.9636 | 2025-09-17 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e9bba528-18a6-3fac-8c9b-d542154b3ac1 | -12.907 | -42.7378 | 2025-09-17 14:20:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 93.8 |
| faec25ef-f63a-3dcd-971c-234b60ed929d | -5.7867 | -45.9603 | 2025-09-17 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e235e2d8-c78b-32cb-8d53-b9e6cace5845 | -8.6696 | -46.3842 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 9fc7a029-e9f5-322e-afd5-8ddc1cbb98f0 | -8.631 | -46.4553 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a96ea1ed-9cf8-3cb3-9460-816e83f7320f | -8.8958 | -47.8683 | 2025-09-17 14:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| dca96f88-7814-378f-8e68-673d6615aaea | -15.0549 | -42.4653 | 2025-09-17 14:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 5f42c785-3e20-3079-ac09-46d3ef2ce387 | -9.4747 | -48.2698 | 2025-09-17 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4be607e7-e29f-3599-aba2-21dc8e9a6771 | -12.124 | -47.5566 | 2025-09-17 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 51e00911-8ee3-33e1-b149-1bf990e5f22f | -6.1252 | -47.8355 | 2025-09-17 14:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 0d626f91-d6e3-38a5-9b54-42827894cf92 | -5.7858 | -43.9378 | 2025-09-17 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 8a4518de-3628-35c3-a20e-5fd1eab8a9a8 | -8.5611 | -47.5492 | 2025-09-17 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 9e78b5ca-ba6f-3669-92fa-8b94663e5146 | -8.0597 | -45.4544 | 2025-09-17 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| bdeeeff0-88e5-3de4-9740-b2c3a63b8257 | -13.9683 | -44.7802 | 2025-09-17 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.3 |
| f555d532-9aa2-3446-a5b2-94a526b4b43f | -12.7145 | -47.7419 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f322cbac-07c0-3a00-9767-b63590e0118b | -12.7482 | -48.0041 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 288.5 |
| c52c928d-ff45-3175-b3f5-13c746ff14f3 | -10.6401 | -48.7332 | 2025-09-17 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 271b76ec-acfa-3f83-8e8a-80e897edc831 | -8.9399 | -44.492 | 2025-09-17 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 33b786e6-f3a1-3583-aae6-bf526265e3c1 | -7.5996 | -44.5872 | 2025-09-17 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 239.0 |
| bb775978-b3b5-323f-9bec-7bd4f32717a9 | -8.1569 | -46.7693 | 2025-09-17 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 3d97e9a3-6717-3f93-b1ee-81f7102d3313 | -8.9449 | -45.521 | 2025-09-17 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 3dd0b916-1e8c-381a-873c-bb35e2739aad | -3.8463 | -40.3607 | 2025-09-17 14:20:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 104.8 |
| f740c41f-36d0-3380-a930-4379544c4d0f | -9.7319 | -47.3847 | 2025-09-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ad90a96b-00d1-3268-a801-175f94b98720 | -12.6949 | -47.7669 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| ad9bb3bd-21ef-3cba-adc5-7ced19041444 | -8.4279 | -47.6937 | 2025-09-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6adea546-3244-336a-ae7f-3f8f2971a853 | -13.9648 | -44.9445 | 2025-09-17 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| ad5bada7-1858-3499-ad53-758ba3e0c67e | -12.7478 | -48.0263 | 2025-09-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 590d955a-a654-3f39-ab76-59a557daea3b | -8.6499 | -46.4534 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7003d7d6-7acb-3c78-984b-fb668c99fb8d | -8.6885 | -46.3823 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 444.3 |
| 05282853-5c2c-393a-b440-807162e42de9 | -6.1739 | -44.5058 | 2025-09-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ac36d29a-e3ca-3f87-bee8-a9c58be0047a | -3.8042 | -44.1072 | 2025-09-17 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 374.0 |
| 6e6059f2-958e-3816-bb59-3c1519075a1f | -6.2055 | -45.1187 | 2025-09-17 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6b19aa01-ae3c-3d0b-9f66-3a7567f46b0e | -8.9359 | -46.1995 | 2025-09-17 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 192.6 |
| f9378979-5940-3a68-beec-74d774559139 | -7.897 | -48.1787 | 2025-09-17 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 26247ab5-42e1-3395-8147-d34a4ed304b9 | -11.3636 | -47.3677 | 2025-09-17 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d136241c-dd0f-371d-a20e-f514405cb3d2 | -9.1236 | -44.8849 | 2025-09-17 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 124.6 |
| fb259a6f-70fc-3b04-9817-de44f3189226 | -8.6502 | -46.431 | 2025-09-17 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 0670ed1c-7822-3265-827a-b6627aa0838b | -3.8042 | -44.1072 | 2025-09-17 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 275.8 |
| e936f8de-f126-3c8e-abbe-fe0438351e3f | -7.5415 | -44.7303 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 9bb4d023-ca8b-3263-91b4-d3e63354e487 | -8.631 | -46.4553 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 34161e1a-6719-3169-9ea5-6432c4b9c1cf | -12.6729 | -45.8052 | 2025-09-17 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2686775f-270d-345a-8ccf-9a2f43b2467e | -9.4747 | -48.2698 | 2025-09-17 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 35921a89-6b77-306c-9164-85f12d9bbdb7 | -14.7911 | -60.2289 | 2025-09-17 14:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c294f404-0f43-3027-ae9c-e952a9f592fb | -5.943 | -45.1838 | 2025-09-17 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 5d132a46-37db-307c-a5c4-76724bf987dd | -8.6696 | -46.3842 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| a38fe2d4-7a38-3a60-82b9-013efeae53dd | -8.1569 | -46.7693 | 2025-09-17 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c238360b-eb5e-334f-857b-f95e280337a4 | -3.8228 | -44.1063 | 2025-09-17 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 8b8095e0-3708-3d22-8ddb-3a03deb5bce5 | -11.1681 | -45.3373 | 2025-09-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8017384e-8ac3-34fc-b063-faf89694648e | -12.7106 | -47.9649 | 2025-09-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| c0e217c0-4c80-36c4-bc8d-846ffb201736 | -6.2055 | -45.1187 | 2025-09-17 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c0b70f23-4c3e-3c1a-9b7d-77a91190369d | -5.7871 | -45.9155 | 2025-09-17 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 3f6b4789-66a3-3e81-9a4c-5eeb0a9c22ac | -11.211 | -47.3872 | 2025-09-17 14:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| da750d20-17ee-3d6e-89fc-0469329d3eb2 | -3.8463 | -40.3607 | 2025-09-17 14:30:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 105.4 |
| ba9f04f7-c781-38d5-836c-86f7a2e5c33c | -7.2581 | -46.6052 | 2025-09-17 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d82deed3-406f-385d-8bd9-1c3cc3bbd876 | -7.5227 | -44.7321 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 146.2 |
| f7c58f4a-3912-35c1-869f-dab6ffa8d619 | -7.5998 | -44.5642 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| d278bec1-c827-3e51-84ec-b44b522009b8 | -11.6434 | -46.591 | 2025-09-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e1cfc968-2b42-31e8-a1a1-22b1b0d3747d | -8.8987 | -46.1585 | 2025-09-17 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2957e035-350a-3f7b-8367-ac7e265d5649 | -8.5421 | -47.573 | 2025-09-17 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 41083a4d-4069-334d-96f3-e5602ac9342a | -3.8002 | -41.6947 | 2025-09-17 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 216.7 |
| 09a155ef-451e-3579-9cc4-6ad50684cc39 | -8.5611 | -47.5492 | 2025-09-17 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 41985c55-758a-39d3-8fe4-87f2ecf08069 | -8.899 | -46.136 | 2025-09-17 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 9416d63e-838e-3403-9f0b-df913716cc88 | -8.6499 | -46.4534 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.8 |
| a3286d86-fc95-3fc0-95c7-c1b218a6ebef | -6.1252 | -47.8355 | 2025-09-17 14:30:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 70ccced8-2639-3e01-8894-d47ed517c46b | -12.907 | -42.7378 | 2025-09-17 14:30:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 23b0b7b8-1fb6-35e2-81aa-7224f4d07487 | -8.6502 | -46.431 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| e147dd43-e94b-3faf-90a7-2315faf72b9c | -8.5797 | -47.5694 | 2025-09-17 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 34106771-b56a-32ed-b984-020a20443e77 | -7.5269 | -44.3644 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ef8c9176-7867-33c7-8981-8be8262eff80 | -9.7514 | -47.3382 | 2025-09-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 83d20354-30ea-3f89-8706-b6a4d532f5e8 | -8.4279 | -47.6937 | 2025-09-17 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 85c26c82-b787-3f1e-99a6-92bbbcab6865 | -9.4935 | -48.2679 | 2025-09-17 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 7a6738c6-c393-346f-b249-6d25161bd23e | -15.8417 | -59.4799 | 2025-09-17 14:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 50965b5b-3488-39fc-b17b-776cb8b97c9b | -7.8259 | -46.153 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| f970e134-b28d-3c24-8513-be4f03538294 | -9.0851 | -44.9352 | 2025-09-17 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| c82b9fae-25eb-3b26-a628-eb36633cf0f7 | -11.1299 | -45.3426 | 2025-09-17 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7a6d3da3-59e9-3788-86aa-e0bfedf1f78d | -8.9399 | -44.492 | 2025-09-17 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 3486e692-3fe3-32a8-963f-04e4ec0872b8 | -9.0661 | -44.9374 | 2025-09-17 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 2e921db5-b9c5-3a19-8512-5b41704e22c6 | -10.9643 | -47.3514 | 2025-09-17 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 6db8245c-2802-3cd3-b4c9-06d82f6b8355 | -11.3636 | -47.3677 | 2025-09-17 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 48752893-7ff1-3ff8-99cb-28d538e596c4 | -10.6401 | -48.7332 | 2025-09-17 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| adef4de8-0c01-32c2-9953-2f586e57c957 | -5.786 | -43.9147 | 2025-09-17 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 211.9 |
| e00d4fd5-ccce-3e26-93df-7e57aa4bab63 | -4.6586 | -37.4564 | 2025-09-17 14:30:00 | GOES-19 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 83.6 |
| 3a397185-caa6-3ca0-8182-accb45cfa7ab | -7.581 | -44.566 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 130ecab4-4f1e-3f97-857d-365ce3aa86cf | -8.6702 | -46.3394 | 2025-09-17 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| facd9601-1d07-3afd-b076-69a3c366c53a | -5.7858 | -43.9378 | 2025-09-17 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 150.4 |
| fedb4ce9-3189-3dab-bc33-4edf4d94c5a6 | -7.6574 | -44.4667 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 192.7 |
| 938d6484-567d-38f4-8bde-6e8e35eeeb69 | -9.7445 | -47.8468 | 2025-09-17 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 6756203f-640f-3d8f-ab54-8cbaf15a2300 | -7.5272 | -44.3413 | 2025-09-17 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 9439924e-8cb1-3fa6-bb7a-2defc7bffe70 | -12.7478 | -48.0263 | 2025-09-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 5c3e3562-7ecb-3f15-bc35-521a5396b848 | -6.4804 | -45.7296 | 2025-09-17 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 45fd6667-d552-30c2-80b4-d01c7c69098d | -11.6438 | -46.5684 | 2025-09-17 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 62328fd5-612a-3723-85ee-108ae9113fbd | -8.9449 | -45.521 | 2025-09-17 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ae78d115-0fdb-349d-a3e6-a357cb23ad3a | -8.0005 | -45.6864 | 2025-09-17 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| d97b916e-762a-367e-af63-fa1939676207 | -9.1236 | -44.8849 | 2025-09-17 14:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| a5c5c07f-2db9-3a32-8ea5-65a2de4c6b8d | -12.7102 | -47.9872 | 2025-09-17 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |


[Clique aqui para ver as próximas entradas](README69.md)
