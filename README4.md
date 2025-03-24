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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d390854f-df5f-3a6f-a0b7-74ed6a98e7a6 | 1.29881 | -59.99948 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fcbe86b-6752-3596-8038-c442a4fde422 | 4.09706 | -61.53127 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 723b7303-f80f-360a-ab7f-16ad1639fd82 | 4.09317 | -61.55022 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6df865d-a447-3cee-b384-8b89626fecff | 4.09487 | -61.56091 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92408509-43d0-35bd-bb51-904980537d93 | 2.08966 | -60.21767 | 2025-03-24 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b890c9df-d06e-3922-bb0a-229ababfec69 | 4.09151 | -61.56144 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6a10e8e-9356-3b43-8a5e-a7e9c3e71b47 | 2.14395 | -60.58868 | 2025-03-24 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bfcfef3-6634-3c9b-935e-6a4cbc8b1f7e | 2.31645 | -61.24368 | 2025-03-24 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ea50ecc-98d7-3e2a-a463-070622921172 | 4.08201 | -61.5666 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 989cbaad-d5d5-335b-9849-f1c1502b4b3d | 1.52991 | -60.11265 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49e842ed-afc7-3fdc-acbc-7c7ee3a0bc6d | 1.29212 | -60.00504 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53248e09-71ee-32d3-bb6b-bedc37d553c9 | 3.31346 | -60.09847 | 2025-03-24 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d4ac14b-75c2-3be8-bb71-c8becc5964d8 | 3.87427 | -61.84264 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1362f5f-9c4d-3a6b-9fa2-31964834feff | 3.04438 | -60.15841 | 2025-03-24 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89aa76cc-3581-3e70-8848-339755c03aaf | 2.39755 | -60.4039 | 2025-03-24 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2c0e6cb-e536-3cf6-a324-6d5245fb64bc | 3.31573 | -60.08972 | 2025-03-24 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36074758-19af-3ef6-bf2d-fde9c4cf84c2 | 4.07586 | -61.57122 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 981b9052-af41-3663-89fb-dc9db7d52209 | 2.32639 | -61.28435 | 2025-03-24 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2fdf0ec-3462-3553-8b44-b482369e59c5 | 4.05398 | -61.55596 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c0f87df-0861-33ff-86f7-5a7ae5ad6dd0 | 1.2958 | -60.00444 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cb50756-a9cc-3b7f-90e7-45fb48ac4ae2 | 1.53355 | -60.11193 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69d78733-102e-39d9-b733-78795ba98622 | 4.08703 | -61.55485 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed9e317e-d7ed-3343-b5e9-fbb1ecf38c87 | 0.77671 | -60.58922 | 2025-03-24 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c10c978-dba5-33ac-ad4b-349e73d4794e | 3.31215 | -60.09031 | 2025-03-24 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47f3567f-6a24-37ef-8ef6-1d9f0fea698e | 0.78325 | -60.58397 | 2025-03-24 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45af7b31-5d82-377b-ac67-d3d64dfa4629 | 4.05342 | -61.57435 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4547b56-cbef-3517-96eb-692aee64c0e5 | 2.09031 | -60.22189 | 2025-03-24 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fe2df6b-b3b3-3fae-9cea-2c7f90925de8 | 4.08982 | -61.55075 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 373fa678-6263-3299-9288-cb00bd6a7062 | 0.78031 | -60.58866 | 2025-03-24 05:40:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 714fb817-5c3f-3cdb-b8c9-d60d58bc9eea | 4.0937 | -61.5318 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9261ea00-aa3f-31b6-8123-3ef71b32da13 | 2.25191 | -60.28822 | 2025-03-24 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2c8ad5d-9170-3771-97cc-4e8b28453b10 | 1.53289 | -60.10773 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4a389ed-59a7-35d0-a56d-381569c042e0 | 1.90471 | -61.1 | 2025-03-24 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0097660-7082-3168-a3ce-e4cd75233b22 | 4.07865 | -61.56713 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19d5b802-0222-3ea4-aece-aed0ecf8ddc1 | 4.0848 | -61.56251 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bc7afb8-8d1a-30bf-ae6c-1de860069ef2 | 4.08759 | -61.55841 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8343896-a63a-322a-94fb-059fbd546858 | 4.09374 | -61.55378 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d355a08e-bf30-3175-bda1-1fbb470133de | 4.04726 | -61.57898 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 296ce769-607d-304e-804d-e8c7f991c5f6 | 4.06014 | -61.5733 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd76aefd-fc5f-3499-a3bc-5dbfc00fcdba | 2.39463 | -60.4085 | 2025-03-24 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a684c3a-4e4e-3075-8e25-a78cde461604 | 4.08367 | -61.55538 | 2025-03-24 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 352ab34a-4cb1-3cb4-980e-29901c87397c | 2.39819 | -60.40792 | 2025-03-24 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de348459-9dbf-30dc-aa76-9b74fdc8eeb8 | -3.11618 | -59.92904 | 2025-03-24 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b815ac8-c157-3315-ad5a-b06bc4c65481 | 3.31215 | -60.09737 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60ef09d3-059c-364b-a401-5bf9885fcd78 | 2.14479 | -60.58754 | 2025-03-24 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35c82ea4-d7ef-3817-b246-0c3d2a67233d | 4.08415 | -61.55518 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bac317b0-b2de-37f8-8761-4d5ba6bb1a8a | 4.68837 | -60.88512 | 2025-03-24 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37efb668-cccb-3019-8c6f-e2a5e5faabb9 | 2.09202 | -60.22678 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a93e6720-253f-3d44-b516-5180a3e6c2da | 4.07628 | -61.56711 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 300af60f-bd74-3cff-8035-815cbb7b617a | 4.08502 | -61.56034 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23b98a0e-de28-38d6-979d-2720284cf8ed | 2.39813 | -60.40618 | 2025-03-24 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2c96867-8e85-34ad-a36e-8f91fa3c0f63 | 3.31272 | -60.10077 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4875a87-a308-3bc3-b78c-051efca5d3fc | 2.82667 | -60.43592 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4d641b8-d2d3-351d-8683-05280ba88d44 | 2.39867 | -60.40948 | 2025-03-24 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69a25fe9-d8dc-3dff-a5b2-e0ef424eeb1c | 2.09246 | -60.22573 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5c7f12c-f200-3b33-9edc-39a1f3839e34 | 4.07146 | -61.56784 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75401ba1-3388-3eb9-8ba7-0a4dfdbe076f | 0.82482 | -59.9496 | 2025-03-24 06:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65726da8-b994-34b8-a055-dd901d7e6911 | 0.82422 | -59.94588 | 2025-03-24 06:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99b7e019-b7af-31ec-bb5d-be061b99a3cb | 1.53258 | -60.11198 | 2025-03-24 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98df2dc2-129b-3548-8aed-d7ce504bfc1e | 4.08589 | -61.56551 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8c4d01d6-25d1-3027-bf1a-46e94c40f47d | 4.05937 | -61.57633 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ee29b79-4afc-3f26-a8d0-dba7a617390e | 2.14532 | -60.59079 | 2025-03-24 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ccaa4ce-dfe8-3bd4-936a-1e99e17fc4ba | 4.08809 | -61.54918 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fcb9c7e-4b0a-349d-9df4-2af89581f880 | 1.2957 | -60.00414 | 2025-03-24 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5995336-a9e6-3acc-af4e-57d1d170e98f | 4.08022 | -61.56118 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d3f9111d-5b87-3d0a-a0d1-88271bb7dd2a | 1.29633 | -60.00808 | 2025-03-24 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a304844f-64e0-3e69-9127-c0ef71190747 | 2.09088 | -60.21971 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2090c3b-f385-3533-8a29-fff204dc1167 | 4.08895 | -61.55433 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4184d603-0880-32b7-b08d-e43a74de52f5 | 4.08109 | -61.56634 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa7d6f1b-71e8-3252-8432-f0cec082464f | 4.09288 | -61.54827 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f118732a-3e85-369f-b19b-4d729e491985 | 0.82987 | -59.94497 | 2025-03-24 06:03:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd161d17-0070-3820-bd60-4a8985b1fe83 | 2.09126 | -60.21862 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0df1ac31-8f66-3993-bb6f-50e3d148830b | 1.38554 | -60.80266 | 2025-03-24 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd6799a4-0884-3fc6-b535-cb3b9e7ae136 | 2.22395 | -61.67202 | 2025-03-24 06:03:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| face07cb-b017-36a8-b451-93a6b318d1e1 | 2.82613 | -60.43265 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ef736a3-e22c-33ef-a67a-6c1db1182c6b | 4.07716 | -61.57229 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93db7036-40a9-31fb-92c5-fee403c5ca92 | 4.09461 | -61.55863 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5feaa63-624a-3f67-99b5-37973bb5cdbc | 1.38025 | -60.80349 | 2025-03-24 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 917c385b-6451-3491-9889-f6704561b19e | 3.31639 | -60.08968 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b815abc-f6d4-391e-b04e-ef0791a80242 | 4.07541 | -61.56194 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d50af51c-cbf2-3fbb-912d-c6cb4ccd3f3e | 3.31159 | -60.09401 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758c7b6a-3010-33d6-a037-f215a18e4fc5 | 2.58482 | -60.27181 | 2025-03-24 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d9dcc36-8edf-3866-9b21-68f722e9d071 | 3.31103 | -60.09067 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c00d386-5032-330b-9ab9-1f0321acdf84 | 4.08982 | -61.5595 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4ad6191-fab6-32a3-a398-b57737674c1a | 4.68821 | -60.88245 | 2025-03-24 06:03:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd168d53-9f2e-3a93-b999-f489e8e27355 | 2.09146 | -60.22328 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc7179c2-f4f4-377a-aba7-6a4a81ae6336 | 2.09187 | -60.22223 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dde016a4-0b97-3fba-83d0-dd8f3775e536 | 1.37972 | -60.80026 | 2025-03-24 06:03:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cea0588-07cf-3010-8e25-8fabd0757a84 | 2.57945 | -60.27276 | 2025-03-24 06:03:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb68da24-fee5-39c7-9229-291c57a6db77 | 2.08539 | -60.22029 | 2025-03-24 06:03:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 253cf871-bd89-3b3b-ab4a-1cd97e95ca5d | 4.09374 | -61.55344 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fabee523-5b0e-3772-8ea9-b1b9260b4ed7 | 4.08196 | -61.57151 | 2025-03-24 06:03:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |


