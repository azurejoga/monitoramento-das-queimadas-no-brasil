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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6c14c8f-ff42-358a-9c8e-18f531f1b24d | -3.24606 | -53.64324 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a788c3e-49af-3961-af10-43651adb14e0 | -3.26209 | -53.63702 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2e08fa23-ff89-31ed-baaf-1c494fe5bcd1 | -1.4578 | -51.49889 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8dd44a40-dc8e-389a-9dd5-59e9e65152f7 | -3.03337 | -51.53986 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b108dd7e-689e-304c-a920-9cda4b609781 | -4.47256 | -50.76501 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04313e8b-ac76-385d-b4c5-aa8e1302d180 | -4.01899 | -51.02372 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b890d2f5-70b3-3ec2-bbf1-efa14a4de551 | -2.98098 | -53.8995 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 447f0c7c-e0c3-363c-85e1-cad2eeafb6fd | -2.8461 | -54.04014 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa9a9cce-64ed-3c1a-8cd6-bf8db7c47e28 | -2.77651 | -50.29676 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2e00cd4-cd26-36a0-8f19-e79591c3471f | -3.59756 | -50.37289 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 459f0c19-7755-364c-988c-08c1374df31a | -3.46773 | -50.27074 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6734e895-b556-3a13-b553-c50749c38626 | -3.19231 | -54.33205 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2305171-a0b9-38f6-b14b-23a5fd0708d1 | -3.58022 | -54.52237 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86df2e11-dcfb-3432-9864-d0cadaa7e8c6 | -4.18014 | -49.95737 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8c33271-f77a-30b2-a6e2-93befaca3634 | -2.87016 | -54.03465 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b5fcb9f-87ea-3c02-817c-7e41671ca735 | -4.20052 | -50.69024 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e43797a3-eb75-3f8e-933f-9824f91099d4 | -4.41237 | -50.8229 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9122c0c-6678-39c8-9774-ed4c031b2f3f | -2.29887 | -50.68608 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8192b8c-dc00-331c-b2a5-19c77e761032 | -2.45358 | -53.62594 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ad348d4-f74f-361b-85ac-206b5e3b8f86 | -4.11289 | -48.53234 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 790b9814-ed15-3c93-9f50-44ab3112b8ed | -4.00006 | -49.98226 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88268dbf-079c-31c7-8ec4-8d7ba5cc19ec | -4.48697 | -48.48537 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f4e1bdc-ae6c-36c3-b244-045fb5e32746 | -4.1712 | -48.63231 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd07958a-c68e-3207-98a5-0e99fc017b78 | -3.02304 | -52.35303 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dee732b-09cd-3aa3-9fc4-0ba5d2fa69eb | -3.11933 | -53.10687 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fcb87a8-4f4a-3e08-bee4-8e9506515f7b | -3.94402 | -49.75652 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a896f072-ae47-33b9-97b1-70d49dd2e090 | -2.83024 | -52.58975 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 497575a6-39b9-3f27-8f53-ef1b6a0fc3de | -2.47496 | -50.36609 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8b4b69a-c75d-338c-8513-d4e9f9e4e04a | -2.99069 | -53.27967 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51bd0868-5817-30bd-9876-6dd0633d07c7 | -3.51308 | -62.76001 | 2024-12-01 04:44:00 | NPP-375D | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d8e8788-65c3-3ee4-9b69-e85f2b5110eb | -1.07383 | -53.63133 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d56ed94f-6040-3494-8efc-2ec97b6b3046 | -2.11946 | -50.34254 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ef4ebfc-bf9b-39e9-a7ab-1beb21df1d91 | -3.49508 | -53.82833 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d88105-5722-337e-9746-e5c3d35ddaee | -3.4803 | -53.81389 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4b877db-fd7f-3b33-8b06-31c6efeffab2 | -2.77725 | -55.34254 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ac7b35f-dd4a-3592-93ac-9093d9abce43 | -3.26425 | -46.44871 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc4f8162-393a-3443-9ac0-f82a4cf417b2 | -2.65803 | -51.68404 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83d4e403-a444-38f7-9856-b266e3f3ffd3 | -3.22186 | -50.58604 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1e01ba-9a60-3452-a4b6-28a83c93e966 | -3.06444 | -53.26536 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00051f1e-2c79-3d3d-b303-f0eda1be246f | -3.2521 | -53.86625 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcab1706-364e-34be-97d3-a451b642cc45 | -1.83563 | -46.2315 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffef851f-b74d-3bb1-8210-967e20faf0e1 | -1.6974 | -52.63749 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01f457ae-56f1-32d3-917f-41016c319dc9 | -2.63583 | -46.1962 | 2024-12-01 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff60551-ce77-3725-a010-208fd0fcf746 | -3.78986 | -52.4054 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7fa0a88-eb92-3b93-aa73-2f43b37d1172 | -1.69659 | -52.45953 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20b23005-fe52-349a-bbc8-2e06611e6545 | -1.81633 | -50.80346 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed42f5a8-6380-3e6d-bc0d-c2772a6e33c1 | -3.27061 | -50.21184 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0fa1024-bf5d-3d53-aa79-dc8c6c0cd145 | -1.58692 | -52.26423 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 68581024-ec42-3941-8188-e37e6f4a9167 | -1.23713 | -51.61514 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f21a63e1-a20a-316d-be22-10e08911fccc | -2.64492 | -49.90856 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1449adaa-dcb1-30da-a9e4-bfc6690999c6 | -0.99501 | -51.71099 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcb6ef93-7d32-3cdb-93ad-28d31ef00683 | -2.47218 | -50.36212 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20013cb4-37a9-3529-abb3-ac91ca4b5546 | -2.83104 | -54.03773 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea79a43f-07b5-3dda-acd9-17a4e9b49ebd | -2.6004 | -54.2226 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39d32f3e-336e-3e4d-8cc6-39f512ee35a8 | -4.40911 | -50.69799 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be2c0001-8d72-3561-b26f-ba67efe62a06 | -5.48425 | -46.34498 | 2024-12-01 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e500f24-9584-3e0a-a283-e14da8a5cbe3 | -1.6282 | -52.36577 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 481f76fc-98ac-3d7a-8b6b-ddea704b560f | -2.69037 | -46.86528 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 753a58a3-99f0-36e2-a15d-3e690aad3104 | -2.46227 | -50.38179 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c2c5b63-7322-3747-9a22-93512a356d25 | -4.17235 | -48.62492 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e074248-c2a7-38d8-884c-a56a8a5e4708 | -2.18571 | -50.28923 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3140058b-b797-3f4d-b141-86aa914c8da4 | -3.90234 | -46.66224 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14c2bbec-10f5-3bd3-97a3-2d405869065c | -2.48596 | -54.0243 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8e5fdb2-2040-3077-8771-e0b6de032795 | -3.85556 | -46.53757 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7884aee-cd9e-367d-80ed-fc3fa2fd1784 | -2.65325 | -51.75764 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50f3fbed-c11d-3885-b2a3-ca424de67482 | -3.69689 | -50.16904 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 721d22f1-e0cb-3bb5-9156-3651a52b4727 | -3.251 | -53.92774 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a28651ee-8f44-301b-bbf1-3645942ffca3 | -0.18871 | -60.6754 | 2024-12-01 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7136160-97ba-36f1-a5d4-d3548b933d18 | -3.79089 | -51.1841 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e3895c5-6596-3be7-8ee2-48a2e3cf5cc4 | -1.19915 | -51.74553 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dea3085-95d5-3e88-bf98-59fb2bc64636 | -3.14958 | -53.82992 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34a29671-c3e9-36d2-9ba6-aa513ef1fe6a | -2.19331 | -53.77847 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c84ff1c-9398-309d-b4db-66468bfb0ea7 | -4.55821 | -45.72705 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 27.8 |
| ea979116-ee60-34b8-bcf9-e5907611c0ff | -2.25592 | -51.08784 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a602f133-2591-30da-8cd8-794c4fa053a4 | -2.8661 | -53.98775 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da134823-1347-3351-8226-0199f7ab2eb9 | -2.32265 | -50.64354 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d8a5c2f-3129-32aa-b435-7eeed80a072b | -2.99454 | -51.05975 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83be74e4-488f-3072-a2ee-5ed9a3a319a8 | -2.89006 | -53.98233 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d52fa37-1921-3996-8b3e-c20815ae4df1 | -3.21373 | -54.08437 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce87ede5-dd95-3515-9c1f-d4cafd783690 | -1.30932 | -51.7317 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c79403e6-c9e1-3ceb-bf89-f4ef0a03e019 | -3.55061 | -50.19591 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3905d393-192c-3a0c-93da-e10256436aa2 | -3.46619 | -53.87905 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0c4e5e23-ef47-3802-ad7f-0b2fc154b157 | -2.44618 | -53.62479 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a8dc1747-01d3-3e51-b08e-3afba2a6c6db | -2.94048 | -54.42014 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5260643-38a1-3e3b-aa91-88522b5bb533 | -1.95102 | -53.34305 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9fdd71d6-c353-3e4e-bf26-bd604814892a | -4.00772 | -49.95504 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dd716a6-ad1b-3d78-8dc0-017940eb1556 | -5.33034 | -45.44204 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee3ed7e1-dcbf-39f1-b034-6e7ec2a77dee | -2.46738 | -50.22004 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53c3a17a-f32d-3693-a53e-3d55522e90ae | -2.62549 | -54.2127 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c1681fd-0dab-3224-9a23-f7c82ea86ef0 | -3.06502 | -53.81181 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b129786-4545-35e1-8305-6e62004a2049 | -3.12752 | -54.52789 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9d32984f-b7d1-32a2-8bd2-d5a9b18444fd | -2.29892 | -51.98511 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c6cb486-5186-3c69-b77b-58dc1654821b | -1.71701 | -52.77944 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff748b60-3a9a-39df-adec-4b600750fdca | -2.62107 | -51.76029 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| deacdea2-2d28-3b4b-8cfe-13b26dd90778 | -3.35066 | -49.91665 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c85cc2e8-c395-34c9-9fcd-232584025a9e | -3.15495 | -50.62164 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f6d1fc7-b697-3c8c-ba6e-9da37dd1002f | -4.05654 | -50.95492 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b54b6831-27cf-3f07-a09f-e35fea41638c | -2.90181 | -51.57838 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 638c793c-943c-38db-a90a-a0a0fed80c83 | -2.94824 | -45.71215 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3421776-cca9-3d08-bde9-cad2c5fd28f7 | -3.32726 | -50.2172 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README47.md)
