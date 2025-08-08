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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 850075f7-0ab7-30af-8fde-3986d811c01a | -9.93433 | -60.50045 | 2025-08-08 06:27:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| afa3e831-e6d3-3c18-a06d-7004d05817a3 | -7.07056 | -59.14852 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 6357aa7d-838c-3604-9b0c-0ace4cf911ec | -7.04799 | -59.17541 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 234.9 |
| c8b760b2-289c-3dc0-95ee-86e9d7ddb7c5 | -8.92201 | -60.74697 | 2025-08-08 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a0781560-b45d-36bc-b16a-7e543aabcabb | -12.55079 | -47.13005 | 2025-08-08 06:27:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| ca3cc06d-9faf-3aaf-8e20-daee140b8fad | -7.07223 | -59.15429 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 3c2242f9-6f1c-39c7-8cf2-15bd8c9db6ea | -9.70823 | -61.30067 | 2025-08-08 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 2122b7bd-b7f4-3ea7-a31e-d6a62cde1455 | -7.06199 | -59.15284 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 73f7b6a6-3645-3199-9d70-154d9da35c6a | -7.06011 | -59.16491 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.8 |
| bb27b7c7-5038-3097-815e-de11f180b07f | -7.03584 | -59.18597 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a0360879-2203-3927-b62d-28f43db1ad45 | -8.9244 | -60.73212 | 2025-08-08 06:27:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7892b63b-fa02-3397-bf2a-78372275d93d | -7.04987 | -59.16336 | 2025-08-08 06:27:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 1da04073-bf1b-30e8-8418-3e08e5a072bc | -16.35458 | -53.34063 | 2025-08-08 06:29:00 | AQUA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 5a99fbd0-1b3f-33b4-b34e-d3f3fac881fb | -16.35633 | -53.32696 | 2025-08-08 06:29:00 | AQUA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 54cdca9b-b33e-32b7-95b1-5cef1c31e555 | -7.0615 | -59.1779 | 2025-08-08 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 1fc66a60-d1b3-3dd9-90f5-fdb8c34ea9d6 | -7.0616 | -59.1586 | 2025-08-08 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f304a98e-6b00-3c08-81ff-8fd22136513f | -7.043 | -59.1787 | 2025-08-08 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 3b1e2fbb-ac9c-3f76-92df-f204a1dac7b1 | -7.2415 | -44.6667 | 2025-08-08 06:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1e88da78-5d69-34d0-bd2d-7116aec3ba68 | -7.2412 | -44.6897 | 2025-08-08 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 45fe3fcb-0fcb-3417-9691-8290ac1adb3a | -7.26 | -44.6879 | 2025-08-08 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 002fae64-621c-349c-8d3f-21316461e72b | -7.0801 | -59.1578 | 2025-08-08 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 2db5ee3c-54d1-39d3-b2e7-a19e38d9a7ab | -7.0429 | -59.198 | 2025-08-08 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c59af810-2dc8-3331-a2b0-9cc4b279cecf | -7.043 | -59.1787 | 2025-08-08 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7ab24d40-1176-3347-83f2-a9239ed263f2 | -7.0615 | -59.1779 | 2025-08-08 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| de17435c-2a64-3e03-b848-cfb690b449fc | -7.2603 | -44.665 | 2025-08-08 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 453.1 |
| a40a959e-7a53-3b64-8f14-1608222abbb3 | -7.0616 | -59.1586 | 2025-08-08 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cc1eaae2-6783-3dbc-9e50-c21fb1c62370 | -7.2605 | -44.6421 | 2025-08-08 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 5d3c2119-71a3-36ee-b387-4f066023281c | -7.2415 | -44.6667 | 2025-08-08 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 0296b70e-3ae0-342c-9c90-aa2124d74456 | -7.2417 | -44.6438 | 2025-08-08 06:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 78d29edc-7272-3794-8407-409db8f8886a | -8.9213 | -60.7489 | 2025-08-08 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 45095c70-76f6-32d4-bab4-379a7c73080d | -7.2603 | -44.665 | 2025-08-08 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 06e4ac70-7a35-3414-a441-b223df0ceb55 | -16.3466 | -53.3405 | 2025-08-08 07:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b4c4de9c-c909-325c-821e-e4919d625a06 | -7.2415 | -44.6667 | 2025-08-08 07:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 4d767a3b-840a-3bb1-96c4-bb1ef04568d2 | -16.3662 | -53.3377 | 2025-08-08 07:00:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| bf7634e2-391b-30dc-acc7-239674731034 | -7.2415 | -44.6667 | 2025-08-08 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 2e3d4dd3-a843-3712-8411-4c0c5f43275a | -7.2603 | -44.665 | 2025-08-08 07:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| d22c134b-43e6-3c4e-8022-81cf74697ba2 | -16.3466 | -53.3405 | 2025-08-08 07:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 3768df5a-6963-30c9-8e56-5606fd2e6003 | -16.3662 | -53.3377 | 2025-08-08 07:10:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 43c643f0-82e8-3184-b9ef-f51ad45a52d1 | -7.0801 | -59.1578 | 2025-08-08 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 831b82c6-53a2-3509-91ee-262c264ac872 | -7.0615 | -59.1779 | 2025-08-08 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| ad5f0af4-48d3-3030-942b-0dcf488a54e5 | -7.043 | -59.1787 | 2025-08-08 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 6bba6fab-d9a7-3951-a0be-f8f958264873 | -7.0429 | -59.198 | 2025-08-08 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f48d083a-1ceb-3ab0-949f-dce48256226a | -7.0432 | -59.1594 | 2025-08-08 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 82cd9069-f0e2-3655-8886-ba59a27bad2c | -7.0616 | -59.1586 | 2025-08-08 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d1e62128-52aa-3cdc-ad6a-4ef76532362c | -7.0801 | -59.1578 | 2025-08-08 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| fb36ad12-9160-30b6-ae4b-b9db44a63cd4 | -7.08 | -59.1771 | 2025-08-08 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| bcbb98e2-5883-3761-8a91-56938f1c3ed9 | -7.0616 | -59.1586 | 2025-08-08 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 6b3690f4-3f97-3298-bd11-1af94d0fe469 | -7.0615 | -59.1779 | 2025-08-08 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 61c45d6c-32e4-3ac5-b81e-0655960faada | -7.0432 | -59.1594 | 2025-08-08 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2ecc0d4b-d4d6-3132-81ea-e2493279e25a | -7.043 | -59.1787 | 2025-08-08 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3b73a6a2-9561-3426-a442-2a790449fb99 | -7.0802 | -59.1385 | 2025-08-08 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b80d1279-1757-3f35-a22b-b692c9270811 | -7.0616 | -59.1586 | 2025-08-08 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 1db9c8c8-364f-32aa-a79b-627a7f77a99c | -7.0615 | -59.1779 | 2025-08-08 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| e5339c29-9273-39eb-9bd8-0726bc600f01 | -7.08 | -59.1771 | 2025-08-08 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7c253f89-b5e6-3b99-a9cb-5d3b5452eb05 | -7.0614 | -59.1972 | 2025-08-08 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5a203c71-8baa-3ba6-b181-9979c0d896f3 | -7.0801 | -59.1578 | 2025-08-08 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 82da8392-5f89-305d-bdb6-576ee95e6160 | -7.0615 | -59.1779 | 2025-08-08 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 47ebda28-7425-3f5e-a514-798d3d31fa2c | -7.0801 | -59.1578 | 2025-08-08 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| c52ff1b7-5ce2-3107-8c7f-72f98bd265c1 | -7.08 | -59.1771 | 2025-08-08 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e23dfc76-c67d-34b7-a83f-9555158b46db | -7.0617 | -59.1392 | 2025-08-08 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 3491599e-cb0f-3c01-b19e-c90257cc03b1 | -7.0616 | -59.1586 | 2025-08-08 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 199.2 |
| d8cdf99d-7ba8-33a9-b53d-77dacf6a9936 | -7.0802 | -59.1385 | 2025-08-08 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 96f04831-3b22-313b-bcbc-ab52b9e0afbb | -7.0802 | -59.1385 | 2025-08-08 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4877bfbd-ae83-3e93-b976-8fcd2aacd1ac | -7.0801 | -59.1578 | 2025-08-08 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 228.2 |
| 34ff517b-758b-3a5d-88cb-2e8e1a3a7854 | -7.0615 | -59.1779 | 2025-08-08 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 51006686-dac0-3895-93d5-9e20f72b1273 | -7.0616 | -59.1586 | 2025-08-08 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 268.9 |
| 3029cbb8-6f71-3069-aa91-9c1c7f619135 | -7.08 | -59.1771 | 2025-08-08 09:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 73db19b2-e071-3009-8c39-5b57d2e207fd | -11.089 | -50.474 | 2025-08-08 09:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| cfca5221-1071-355d-b6ff-952d17654de5 | -11.089 | -50.474 | 2025-08-08 09:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5dc06733-6f0a-3827-bd1d-5412f8988b9e | -7.26 | -44.6879 | 2025-08-08 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 5c0e8739-dc81-38f0-af7d-f66d62d1d778 | -7.0616 | -59.1586 | 2025-08-08 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 226.0 |
| c103385d-5bd7-3602-94be-f01ebffaea75 | -7.0614 | -59.1972 | 2025-08-08 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 332.9 |
| b0f5882d-2b8e-3d00-96b0-6d64e44eb8cb | -7.0615 | -59.1779 | 2025-08-08 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 403.9 |
| 695bdc3d-c07d-36f4-9484-21bfc121c8af | -7.2603 | -44.665 | 2025-08-08 10:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 558.2 |
| c03f3544-4f2e-384f-92db-2b68794ec980 | -7.0429 | -59.198 | 2025-08-08 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 323.6 |
| 80320584-d1e6-34b1-af2a-be0694996970 | -7.043 | -59.1787 | 2025-08-08 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 362.5 |
| a7d4a2b1-daf7-386d-a678-c887e2066ecc | -7.0801 | -59.1578 | 2025-08-08 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 8e2be657-d206-3b5e-b5c5-7607a6907d0d | -7.0429 | -59.198 | 2025-08-08 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.2 |
| dffa95cb-b94f-3cb8-9b0d-d9a99c2fd5e4 | -7.0615 | -59.1779 | 2025-08-08 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 356.8 |
| 2524d448-f35a-3cf8-ab6b-565c82db1f55 | -7.0801 | -59.1578 | 2025-08-08 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 200.8 |
| cd6afdc3-27d1-330f-b4e4-ad4f27fee91d | -7.2415 | -44.6667 | 2025-08-08 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 369efd65-c103-35a1-bc98-c5f1f9888073 | -7.0614 | -59.1972 | 2025-08-08 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 253.6 |
| 7f13befe-3e48-339f-9465-1a741eeb93e1 | -7.043 | -59.1787 | 2025-08-08 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 207.0 |
| 7ba5fdbd-f4aa-3394-b5cb-85542bb48d2e | -7.0616 | -59.1586 | 2025-08-08 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 223.6 |
| f9359060-fd9a-307c-a205-4e4b1ea08d96 | -7.2603 | -44.665 | 2025-08-08 10:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 388.1 |
| 0f60a6ef-229d-3bd0-b6a9-3766d83b9fae | -7.0614 | -59.1972 | 2025-08-08 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 219.7 |
| a1f68fda-fbe3-307c-be25-93e17b4205a1 | -7.0616 | -59.1586 | 2025-08-08 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 234.1 |
| 488524a3-e061-3e8b-b195-54ec404f4c9e | -7.0801 | -59.1578 | 2025-08-08 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 204ea2fb-6998-36ba-9e55-3dcc4e31f106 | -7.0615 | -59.1779 | 2025-08-08 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 347.3 |
| b29382ca-9b61-33c4-8dd6-b0867c31c5d6 | -7.043 | -59.1787 | 2025-08-08 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 260.4 |
| fee4fb1c-fb87-3250-b709-8c61068d65fc | -7.0429 | -59.198 | 2025-08-08 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.4 |
| dd315ea8-0b21-3c3e-ab19-517320fef84e | -7.2603 | -44.665 | 2025-08-08 10:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 70926f78-ce19-3e87-9e3f-717a50db1ad7 | -7.0615 | -59.1779 | 2025-08-08 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 442.4 |
| 569943ef-15d1-3e0f-8054-2739d79577cd | -7.0801 | -59.1578 | 2025-08-08 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 217.6 |
| 85a76dcb-220d-3adc-8ac2-b71cae3f3158 | -7.0614 | -59.1972 | 2025-08-08 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 323.6 |
| 96d9af17-0e9d-3ddf-bd80-e9c7ff351698 | -7.08 | -59.1771 | 2025-08-08 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| f7cdc568-3916-3690-9c2e-92b508801235 | -7.0616 | -59.1586 | 2025-08-08 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 279.4 |
| 734c04ed-d879-3b7f-b6fb-9c17079a8591 | -7.0616 | -59.1586 | 2025-08-08 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 338.1 |
| c25bfdef-f53d-3465-b860-74ff092df9e8 | -7.0614 | -59.1972 | 2025-08-08 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 313.7 |
| c6eba124-a713-3b07-95e3-ba1d4e3eb797 | -7.08 | -59.1771 | 2025-08-08 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |


[Clique aqui para ver as próximas entradas](README27.md)
