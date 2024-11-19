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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9caa946f-9972-361a-98bb-8075fc540e0e | -2.25909 | -48.41576 | 2024-11-19 05:40:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cff9dd4-66fb-3c81-96ec-0dadb9c5c394 | -4.57947 | -48.01385 | 2024-11-19 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6719b6ea-28f9-3467-b46a-fdaedab18866 | -3.36136 | -54.09783 | 2024-11-19 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f3c26d8-3a16-38db-a330-9ad5a1367568 | -2.3549 | -49.01248 | 2024-11-19 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 65ff187b-0d2f-3452-b07e-aef0685bbb7f | -5.97683 | -45.35841 | 2024-11-19 05:40:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d16c851d-2fd4-338d-8249-a3a7ac3cba89 | -3.43466 | -50.29652 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 579adb0d-e3ae-3c61-80f6-4ebc7fee8054 | -4.55049 | -48.01944 | 2024-11-19 05:40:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 480adb3a-07c7-364c-8442-41b76c4661a5 | -1.37635 | -52.07719 | 2024-11-19 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d96ac641-63d2-3547-a765-3a772089d95b | -2.65996 | -51.7085 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 50bc9504-e98c-3e80-bf14-7c064f786c08 | -3.56662 | -51.43819 | 2024-11-19 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f32d270f-f830-3150-96d1-6331517bc2e1 | -2.77453 | -52.59064 | 2024-11-19 05:40:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4520074f-e666-3308-9cc0-ac18cc1d34fc | -3.57221 | -50.24715 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1998ead-037c-3b8d-84f3-0a5017d6440f | -3.31555 | -54.17243 | 2024-11-19 05:40:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 67d2f8f4-24d1-3895-b278-89e8731df12a | -1.13871 | -51.68168 | 2024-11-19 05:40:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4d0eb6ee-b2fd-3720-b8c0-b0c531a72480 | -1.39506 | -52.42297 | 2024-11-19 05:40:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d3eb15d2-27c8-3c88-b911-c0af4c993103 | -1.63489 | -52.66959 | 2024-11-19 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c81f2581-94c8-35d9-8e52-889b20e98db8 | -2.49061 | -49.02084 | 2024-11-19 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f9203ded-a4e3-3b94-98bd-c277afd0d8fd | -3.19703 | -52.43731 | 2024-11-19 05:40:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e1d2c087-a18b-3ca7-8672-9828d35a8f8a | -2.35359 | -49.02127 | 2024-11-19 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e495070d-0044-3fe5-886e-d549829fd6d5 | -3.57086 | -50.25609 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ee5d469e-46af-3a2a-929f-3e1f07143813 | -1.62181 | -52.61886 | 2024-11-19 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0429a6b8-ee4b-3ae0-8af3-847ae41e3ff6 | -2.66791 | -51.7201 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 21e92bb4-1346-3795-9afb-392bb80eb676 | -2.59052 | -51.71908 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cde19728-009c-3262-9421-82e9c4d21f0a | -3.33211 | -50.4926 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9cf87dc9-89d2-3530-a5ec-5e43ae2b7395 | -2.26042 | -48.4068 | 2024-11-19 05:40:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b927f06-fd86-3b38-832d-08dd1836df15 | -1.92931 | -54.05131 | 2024-11-19 05:40:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 939fb4bd-e175-3f73-921d-d4eefcb107e5 | -2.21364 | -48.40336 | 2024-11-19 05:40:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee981386-9cd4-380e-84a7-3231eab683fa | -2.48929 | -49.02964 | 2024-11-19 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 47b0d37d-9b74-336b-affa-3721ec9ea22c | -4.06193 | -50.00544 | 2024-11-19 05:40:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43fe6d3c-0c1a-3257-8a47-af08ab3c94db | -3.66341 | -50.43991 | 2024-11-19 05:40:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 488179b8-01e2-3ef8-b7bb-88b38d8ca015 | -2.65843 | -51.71869 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6b17b0d2-b2c8-3eff-9d0d-f5246a402642 | -5.988 | -45.36002 | 2024-11-19 05:40:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 06daed57-1416-3748-ac7c-7362c257e622 | -4.20397 | -46.59787 | 2024-11-19 05:40:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 172785b0-9988-3f79-ae03-2a689d64162f | -1.5882 | -53.79447 | 2024-11-19 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 59d62230-e974-34c3-84a5-48d067058f94 | -3.25565 | -50.39193 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5ab80a52-9265-34bd-82d7-6cc163f7a9a3 | -2.28284 | -53.63258 | 2024-11-19 05:40:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 812af5c0-6f5f-3911-80df-adb4c72ca68b | -2.6553 | -48.47964 | 2024-11-19 05:40:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2002f0c2-b65d-33e1-97b6-e4035939eac0 | -3.48314 | -48.2476 | 2024-11-19 05:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 742071ab-9f94-39d9-950e-c08896ffeb24 | -3.55171 | -51.53555 | 2024-11-19 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 433e965c-5330-3a82-aaa6-51556ac29131 | -2.77281 | -52.60192 | 2024-11-19 05:40:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 33d9e349-b79c-3343-a90c-c3f1f7d92da1 | -10.99653 | -49.02195 | 2024-11-19 05:40:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ffe01c0c-feca-36bb-8565-6f256bd9485f | -4.9956 | -44.33534 | 2024-11-19 05:40:00 | AQUA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6e807f02-8f85-39ca-8cc7-7ff9e464c1a9 | -2.25703 | -50.45525 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4a6556c-6cfb-3e36-950c-2cc1df65d3a2 | -3.5532 | -51.5258 | 2024-11-19 05:40:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4c8bc865-cb97-3e60-a3ce-7d88f15abe2a | -2.78496 | -51.71864 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 15daa6aa-ab2f-3f9b-9c4f-1a990b605bf4 | -3.99122 | -49.91732 | 2024-11-19 05:40:00 | AQUA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8c18c471-53dd-3f49-abc8-1a33a4643f14 | -2.92969 | -49.11537 | 2024-11-19 05:40:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 18c452ed-6d92-3427-9254-abb27f5d270b | -2.58103 | -51.71767 | 2024-11-19 05:40:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d91b5010-358f-38a9-9427-e05c4e239160 | -1.70572 | -52.13932 | 2024-11-19 05:40:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 58c509da-6329-3bf0-8b62-5a16dc229f40 | -23.96631 | -54.14571 | 2024-11-19 05:44:00 | AQUA_M-M | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a4bfac39-9526-36c3-83e2-9f412980b3f0 | -22.30826 | -49.76413 | 2024-11-19 05:44:00 | AQUA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 32bfe87e-edaa-3a9c-88a3-e82c166a6c3e | -4.58 | -48.0132 | 2024-11-19 05:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e714c7e6-dce3-3a55-ad49-62b39195f8d3 | -4.5429 | -48.0151 | 2024-11-19 05:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 7c10977a-ef19-32be-980a-9d62169d219a | -4.5614 | -48.0141 | 2024-11-19 05:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 1b65cedf-a6b2-3e5f-bad7-392e2904821f | -4.5429 | -48.0151 | 2024-11-19 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| cbae3f44-3cfe-391e-953f-8599696a969b | -4.5614 | -48.0141 | 2024-11-19 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 7f611560-7c30-368b-a0ac-8c888261bb45 | -2.5514 | -45.3612 | 2024-11-19 06:00:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 4561cb8c-06b9-3fb2-9cb1-6891e57789a1 | -4.5616 | -47.9925 | 2024-11-19 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 58c6bd8d-fdf6-35bd-a06e-ee0a0c89f57e | -4.5614 | -48.0141 | 2024-11-19 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 6f5c25d6-4ae0-3bd3-ad64-997f1b1b2d7b | -5.9788 | -45.3621 | 2024-11-19 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 60d180bc-a6d1-3176-8a37-fac8f35c1500 | -4.5616 | -47.9925 | 2024-11-19 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6e144a2c-96da-3620-9e8e-de1d5331aa47 | -4.543 | -47.9934 | 2024-11-19 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| afb3d00b-f6fa-3d28-8097-57fdfcaa19a6 | -4.5429 | -48.0151 | 2024-11-19 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| c8b5678c-8292-328d-a615-9d2ce5c9392c | -4.5614 | -48.0141 | 2024-11-19 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 05dc9b85-ef51-3bd6-a3fc-5eb275c77bb3 | -4.5429 | -48.0151 | 2024-11-19 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 89af5b9c-16f4-3371-a7e7-13ed4fae3987 | -4.5614 | -48.0141 | 2024-11-19 06:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 039585da-45f6-3a25-a989-44d40bf945e1 | -5.9788 | -45.3621 | 2024-11-19 06:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 8f74d693-a6e3-35cb-a0e1-290b4817f32b | -4.5429 | -48.0151 | 2024-11-19 06:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 243f309b-c6c6-30cf-8c6d-8b55515aaed8 | -3.5382 | -45.031 | 2024-11-19 06:30:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d7401b85-63ab-3300-a168-e4e7fed9c976 | -4.5614 | -48.0141 | 2024-11-19 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| b8895425-6a9c-3a28-909c-39cbdfdd82f9 | -4.5616 | -47.9925 | 2024-11-19 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 754b75ee-74bc-3bec-b36b-ebc9b1cfc1b6 | -4.5613 | -48.0358 | 2024-11-19 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 387ad120-f3b7-3e8c-808a-c9b017b427c3 | -4.5429 | -48.0151 | 2024-11-19 06:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9e4518e0-a08b-3957-944c-0ee0f1974a12 | -3.9102 | -45.0816 | 2024-11-19 06:40:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 66fa5942-82db-33b5-aa3c-3286fdfcda3a | -4.5616 | -47.9925 | 2024-11-19 06:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b7e93b35-f676-3a97-a7c7-79736f85151c | -3.9102 | -45.0816 | 2024-11-19 06:50:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| dc6612d1-a602-32bc-97ae-03fb94ddbe53 | -4.5429 | -48.0151 | 2024-11-19 06:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 59622e6c-da04-3585-a93a-6ab9b24584b4 | -4.5614 | -48.0141 | 2024-11-19 06:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 34e68ee0-0662-3277-be19-39c3882f97b4 | -3.9102 | -45.0816 | 2024-11-19 07:00:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| eeb32974-343a-3318-b53a-0d8e711bb35f | -3.5361 | -45.4144 | 2024-11-19 07:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e00c0913-6417-3ced-8981-11576646b83b | -4.5429 | -48.0151 | 2024-11-19 07:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| eb343ff2-e399-3476-bc08-8b00e5980fe2 | -3.5547 | -45.4136 | 2024-11-19 07:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f4a8a21c-aa89-32f4-9113-86defd465ec0 | -3.5361 | -45.4144 | 2024-11-19 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1d8a28cb-bcd6-3a14-a869-6ed2e8a33953 | -3.8916 | -45.0825 | 2024-11-19 07:10:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 5925d6c1-b169-3995-9b0e-36bc902752d0 | -3.5547 | -45.4136 | 2024-11-19 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 502b3162-eaa7-352c-8f22-ada930b1fb0e | -3.9102 | -45.0816 | 2024-11-19 07:10:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 155b4a93-86a8-31a8-a44f-dc58649b569c | -3.1838 | -45.2264 | 2024-11-19 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| af39d0ae-5eb5-3eee-8e2c-7e03049fb8e4 | -3.9102 | -45.0816 | 2024-11-19 07:20:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 9ddb6858-1d55-329e-b08d-7554609d3ac4 | -4.5429 | -48.0151 | 2024-11-19 07:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 74403080-b511-3247-80f0-e8cf48ab2815 | -4.5614 | -48.0141 | 2024-11-19 07:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a721064d-4152-3408-a976-e66bb143afe1 | -3.1838 | -45.2264 | 2024-11-19 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| c3889728-1ded-3166-a3f5-29fbbce74de6 | -3.9102 | -45.0816 | 2024-11-19 07:30:00 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| a76b332f-6c6e-35d3-8518-4420b8f48108 | -23.95 | -54.1191 | 2024-11-19 07:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 37c17e67-daa4-35cf-a5a4-e14d2ecd62dc | -23.9706 | -54.1372 | 2024-11-19 07:40:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 2aaa89fa-66db-325f-9ea5-cca2cefbd01d | -3.1838 | -45.2264 | 2024-11-19 07:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 665b3dc0-46f7-355c-940b-9ed19205e484 | -3.2024 | -45.2256 | 2024-11-19 07:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1c81e924-9a0d-3d22-89e8-2aa93fe005a8 | -3.2024 | -45.2256 | 2024-11-19 07:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 6dad9e0f-42c5-3edf-84db-12d53edd8046 | -23.9706 | -54.1372 | 2024-11-19 07:50:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 98.0 |
| d79830b5-d46b-316d-91ba-c1b8eecac728 | -6.9236 | -42.8144 | 2024-11-19 12:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 5924a27e-8c92-33af-ac89-429d4720aec9 | -3.9298 | -41.9263 | 2024-11-19 12:40:00 | GOES-16 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |


[Clique aqui para ver as próximas entradas](README50.md)
