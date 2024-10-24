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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ed3d6a1-4a03-3ee3-a723-f8973abc6f92 | -2.40302 | -50.41175 | 2024-10-24 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68a2941b-34c7-3c83-b1ab-d197b2378c7e | -2.38925 | -50.3096 | 2024-10-24 04:32:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 561a67d3-215d-30fa-a47f-97b759ff1be9 | -3.51431 | -50.4781 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcf64148-4c48-3185-9ff2-ffe9cbdf1aef | -3.51074 | -50.28247 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0f92adb2-cf46-3333-89e3-6d013b8ae2f2 | -3.51068 | -50.47757 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03f40472-e05d-39c0-b948-25259e649f63 | -3.51 | -50.48175 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f71faf0-3860-3724-858a-91a477fcf82c | -3.50934 | -50.28101 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e98248f7-4e0b-305a-a16f-8f7686ee0515 | -3.50867 | -50.28511 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2caf9cef-7d05-310e-9af2-404f7c4905d0 | -3.50801 | -50.2892 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| feb039c4-9015-3036-afc2-1e102138218c | -3.50714 | -50.28192 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 2e3fbace-04ec-3e87-902d-3017a80d593a | -3.50649 | -50.28602 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 90d983ba-e59a-3d88-9c99-804ff7de0d67 | -3.50585 | -50.29012 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16546bd4-57f1-3d7c-93b7-0aedf14f2a40 | -3.5018 | -50.53236 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2d9b728-7972-3894-9b54-f8736d760292 | -3.4839 | -50.48203 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 363348e8-4266-3f88-9802-8a5fb2bbcc89 | -3.48282 | -50.4833 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb181f6c-4efd-36d8-9877-29a64cde16c1 | -3.46912 | -50.08372 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cbd3052a-42f4-3fc5-a340-76296f9f03c5 | -3.46847 | -50.08773 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cb218500-1879-35a4-a42a-de643911035d | -3.46556 | -50.08318 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a614004e-3466-31e9-8201-3fe84f8847a1 | -3.44842 | -50.07634 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35466fec-bb71-311b-b5b4-293b2be529ad | -3.44706 | -50.40431 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38cb3c1d-4c56-32a7-b668-933aa55dbb35 | -3.44639 | -50.40849 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe9e8ec4-db19-392b-be72-57d83a0b4615 | -3.44572 | -50.41269 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a4f4185-f5e6-3c59-930d-4bc80d209d04 | -3.4421 | -50.41215 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 201fc5bf-2320-3318-bce2-63986169e833 | -3.43633 | -50.35574 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ac7e822-1114-3e68-a39f-8b3667af10f3 | -3.43566 | -50.35993 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05713147-798b-3bc9-a7a7-ab677687b10f | -3.43272 | -50.35519 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb9c2ea9-c342-300f-9eb0-d4a03d6fdbb0 | -3.43078 | -50.25301 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db6577c9-b200-3d83-9f83-892facacc727 | -3.42719 | -50.25245 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81fb904e-af9c-3d45-b47e-3bf813dc8522 | -3.42577 | -50.37537 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db20bc3e-b4fa-399d-a632-3f8d5bab28ef | -3.4208 | -50.38316 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 420f4282-9545-3ff2-be02-5a87e78f2fdf | -3.41719 | -50.3826 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65248a6b-e0e6-3972-9bd8-d0b936fb7ef2 | -3.40588 | -50.3382 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a1c9237-ea91-38fb-bee3-f0c3d1c9a83d | -3.40436 | -49.53074 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 189ad7ff-5f33-34b4-8d3f-2ff7aee78768 | -3.40227 | -50.33762 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b22967f-f8bc-36c0-ba7e-f9ac9d278ef5 | -3.39867 | -50.33704 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22a7903c-9f60-3616-bc0b-f99e0b5faa18 | -3.38936 | -49.85856 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 567bd3c5-8a01-3ad7-abc6-0b6fab54a8eb | -3.35282 | -50.15314 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecc7896f-93c1-320f-898d-3fceac065621 | -3.35156 | -50.32163 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 309fba0d-484c-3505-83ac-9c7d12b8aec3 | -3.34925 | -50.15259 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee7c1908-66e3-3991-8c66-dd356a0467ac | -3.34859 | -50.15667 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b25cb353-783c-342b-ab87-0a8377b7c8f2 | -3.34795 | -50.32108 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3a108b55-91a4-3061-a327-436b07c503e9 | -3.30371 | -49.55839 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1995cc94-901c-3d06-843d-7e1b64b24249 | -3.30252 | -49.55471 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cd946e8-c7ee-3752-8d82-6b32cb8c124f | -3.30191 | -49.55857 | 2024-10-24 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6864844a-88c8-3e90-9ff9-422a1c897feb | -4.85122 | -50.67714 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffbf5047-2b35-34ba-a7b9-98b2e82523a3 | -4.84761 | -50.67657 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fc4f95f-5f3f-3e9a-9158-7f59c4446c55 | -4.84694 | -50.68076 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92083b8d-6c9e-3cad-ab95-c41663ba0fc5 | -4.8212 | -50.88873 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85206c96-04f2-348e-9b68-9872ea663877 | -4.81755 | -50.88815 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96f3b586-21b0-3338-933a-9a6a6fe425e5 | -4.73953 | -50.69491 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0266849e-8f2d-3c2f-80f4-72a26953e398 | -4.73658 | -50.69018 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d9842d5c-3278-35a9-bccf-b0a0c9d35cc3 | -4.73592 | -50.69431 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c776e7ab-85cb-3a1c-8ed1-c9bca8b580b8 | -4.72301 | -50.82193 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ad6e649-96ac-3731-b2d5-1ec83e76f689 | -4.71975 | -50.86801 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e41dc307-db3f-3da1-b783-c0ebb4f30819 | -4.64619 | -50.76639 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca65837a-fde4-34f5-bfa5-3ac40bd6f84e | -4.64255 | -50.76583 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2937edf8-88e5-35b5-ad52-a8d564d69415 | -4.6236 | -50.53214 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 312e9c44-ee39-32fb-ae4f-cb59f542bcb6 | -4.62293 | -50.53627 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34b0be0d-42ba-3d0e-b302-e4aa402cc44e | -4.62001 | -50.53155 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67e1c058-2c83-3dd1-95ae-23ce451108ae | -4.61891 | -50.79295 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f676dc7-32e2-3c48-ae8d-10929caa7820 | -4.55319 | -50.42962 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb819725-407a-3561-9b91-3e67d7c7c994 | -4.51583 | -50.82914 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95d629a3-3b24-320b-bb93-8c1b00dc9756 | -4.51534 | -50.83054 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 649a357c-f4d0-3785-aaec-d2b71a5ce6d0 | -4.49366 | -50.34494 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3ce76f4-9f9b-3f5d-a8a7-7738aaf8416e | -4.42162 | -50.78503 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3643861-10c2-330c-b81f-c4c43a85a1dc | -4.41027 | -50.83132 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 269e5d36-6d1b-3ea6-ae35-7442ce810f3a | -4.40732 | -50.82648 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fc797f8-bbfd-30c6-a087-60d556928c94 | -4.40709 | -50.82793 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ffd03e2f-7139-3c32-b0fb-c7d6810aa672 | -4.40662 | -50.83075 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2bbcf0-035e-33be-b005-b58359d08c06 | -4.36665 | -50.79958 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7789dced-41ce-37c6-ab60-2bf1dc0fffb5 | -4.36528 | -50.80812 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6aa80b70-47aa-311f-b908-7c4712ff6246 | -4.23209 | -50.63561 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a83cff70-3f55-3cab-9819-b2e0fbe6f479 | -4.2314 | -50.63984 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3780c21f-a876-3541-a459-d096cb948306 | -4.99977 | -49.78837 | 2024-10-24 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d2584f5-e624-39f8-a292-a3b94c85552c | -4.94789 | -49.64831 | 2024-10-24 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ef782cb-b664-3bee-8914-70f10f21e677 | -4.54393 | -49.60514 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efc3a5f7-ead0-3f9b-b0ea-5c93f776e6dd | -4.44813 | -49.65588 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5ad7627-a130-3cf7-9b9f-70f85d096d10 | -4.42434 | -49.80511 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71402d29-b20e-3b26-9161-4a5e6d1f88bd | -4.39288 | -49.75679 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e58c23e8-018c-385b-a155-db6512358977 | -4.39226 | -49.76063 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9e2b402-772a-3206-9cda-daec45646dee | -4.38941 | -49.75623 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8290643d-0173-3fe6-87bf-ea484ed27618 | -4.38879 | -49.76009 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07574ec6-0fe6-3b90-9d90-60a03133c75e | -4.38531 | -49.75955 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ced70884-9b69-36a6-876e-4af2902e86b1 | -4.3773 | -49.41737 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7ad44aa-e5d4-3745-bf8e-0be49e2544bd | -4.17006 | -49.26303 | 2024-10-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1e64b24-43ce-33ae-b247-818141fdfd6b | -4.07137 | -50.03926 | 2024-10-24 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07fc8307-a3c1-3b6d-96bf-cb7c6f70d74c | -4.06784 | -50.03868 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b095ba06-3584-33ee-acc7-d2ba6b2221da | -3.72423 | -49.67379 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ade6b5fb-e9ef-3790-a11f-fd7c441be583 | -3.66328 | -50.11644 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b9d4440-0dea-3188-ad5a-4eb06fe5b8be | -3.66264 | -50.12044 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 129655df-e2a7-335b-85c7-458956254c9d | -3.66199 | -50.12445 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dd7898a8-1373-3dd4-8a3f-3bdfd84e95c7 | -3.65972 | -50.1159 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38c5dc72-612e-35c5-9da0-86b14a46f037 | -3.65908 | -50.11989 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cd46ed58-f637-34cb-843e-baf5c456a45d | -3.65616 | -50.11536 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7ffbf1c-6e7a-3865-8d4e-9698ba0fc13f | -3.63696 | -50.12552 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c404883c-4262-373f-856a-fc456b657309 | -3.57851 | -50.56621 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73e3dce2-1838-31c8-87f0-45f60ddac1e3 | -3.57843 | -50.56932 | 2024-10-24 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b9a46e6-ec26-3e74-ac12-6cae8cd5c56b | -3.9382 | -49.39536 | 2024-10-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c94155c-8166-3ba2-b7d4-927ed24c3612 | -3.931 | -49.44057 | 2024-10-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80d5fe10-3594-33b0-a6b1-91db6e43590d | -3.90913 | -49.87721 | 2024-10-24 04:32:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README35.md)
