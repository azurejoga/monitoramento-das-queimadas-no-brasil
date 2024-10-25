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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd8e691-274d-332a-96e0-a3fa2a7210fe | -1.57821 | -53.31592 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc56713d-b8f1-353a-9a67-15ffb62fb392 | -1.53286 | -51.9213 | 2024-10-25 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62bb65c5-6099-31b1-be4d-0279fb4b29d0 | -1.44832 | -52.28414 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb8dadf3-b563-3e6f-95bf-1fb7900cfa61 | -1.44049 | -52.23546 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec7b3f50-de3c-3858-bd43-ebbad6079e2f | -1.43669 | -52.23486 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5254bb18-5c1f-3042-9549-4bf6fac80b9e | -1.43595 | -52.23948 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 590e67c5-3b71-3082-85e6-c3fedcf4f553 | -1.43382 | -52.728 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 948e0aea-275f-337e-9f9d-be23d416a8b2 | -1.43377 | -52.72467 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6591ef00-5545-3205-b2e6-e7d514953a6a | -1.43296 | -52.72964 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be8ab39b-f1ab-3874-a8c7-1f96dfc30aec | -1.10641 | -52.24634 | 2024-10-25 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14d20582-16f4-36b3-9985-f7128c898046 | -1.35489 | -54.64857 | 2024-10-25 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e812bb12-9ef5-35c8-9489-e6335730f6f0 | -1.35305 | -54.64598 | 2024-10-25 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a82d441-4d6e-378a-9460-487171b1acf4 | -1.35044 | -54.64779 | 2024-10-25 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63526e02-0e6f-3383-bb0c-3af3826b4480 | -1.21509 | -54.19777 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bad59b3f-bd68-3106-aa8d-9971aabea770 | -1.18646 | -54.11932 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c51f5e9c-9cad-3bfb-8010-cba4d3d61486 | -1.186 | -53.90135 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4095195-027e-3aee-84c7-b4a2ca8bb50b | -1.1858 | -54.12355 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a70cd372-33b6-3676-9156-742b383909de | -1.18527 | -53.66497 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 09888894-adda-3f79-8bb5-ff87a215033c | -1.18467 | -53.66867 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 6db358b8-c7fc-3e81-afa0-659df5bd82e5 | -1.18419 | -53.66542 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a5ddc69a-761f-3e15-9c66-d01e1cd7fed4 | -1.18406 | -53.67242 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 6e1eebd1-f499-31be-8290-c6131b88a56c | -1.18361 | -53.66915 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| b3f0a9ca-b915-3f78-b053-2a1df09005e7 | -1.18303 | -53.67293 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 2cbd52b7-a8d0-3a09-8fe3-1c0699eb12bf | -1.18108 | -53.66442 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 168ba239-cdcd-374b-8119-a7583f17c69c | -1.18058 | -53.66112 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 078c4b7d-b366-39f6-9940-30a900edabd0 | -1.18046 | -53.66819 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| cea65c1d-0ab9-39f8-876e-3cf7a703a046 | -1.18 | -53.66488 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| b9081529-b81d-3d39-9bb8-896c090d8491 | -1.17984 | -53.67199 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7b6d9234-da76-3dc4-be63-a4a73c89230d | -1.17941 | -53.66867 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 89294509-9058-3733-83f1-20d315790791 | -1.17882 | -53.67248 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| a41445b1-6f69-3af0-88ce-1b1efdfeb3cb | -1.17688 | -53.66389 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| af320884-8dc9-30dd-8245-e5e838498d14 | -1.17626 | -53.66769 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5bcfc4b4-e336-370f-a330-09bbc8041ef4 | -1.1758 | -53.66436 | 2024-10-25 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84163581-46e0-3c72-a2ba-9ba3bb4a6aa3 | -1.16375 | -54.09551 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cda2a38f-160e-3aa2-87cf-862cf26edcb9 | -1.16315 | -54.09929 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fbce15d-49c5-31db-b8d5-381ae604d66d | -1.14092 | -54.10028 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb90f3cd-eca5-30b1-9421-cfe4d0940939 | -1.14027 | -54.10431 | 2024-10-25 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2974e340-b3e3-3099-bb83-701e0f40dace | -1.12222 | -53.43917 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39e6083e-2791-3d12-b2b2-44edf62f682d | -1.11114 | -53.4157 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8c9bc2c-4812-37ab-8fa1-f54c8b8521b8 | -1.10873 | -53.41828 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fbbd253-4399-3e0c-ade5-afd78c00dd11 | -1.10647 | -53.41862 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50001839-f75b-30ca-b0f7-cb93a1749cf6 | -1.07373 | -53.65673 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dcb6f379-2c31-3ead-8187-a96f5440be8b | -1.07371 | -53.65948 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13a33b7c-f64b-31bd-941d-98f10d265a27 | -1.07316 | -53.6604 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cdb1ad62-bc7d-3bb8-ae49-ea2b690a3789 | -1.0731 | -53.6632 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2b38127-ec43-3575-8cd8-fc6184e16209 | -1.07257 | -53.66417 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f3baa538-af2c-396b-a583-e6503d628b6a | -1.07246 | -53.66714 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 88e2a5c1-6f0c-3cdc-a6a4-94316cc726a3 | -1.07196 | -53.66814 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd8d3922-3231-3c00-98e9-4a75c4fb1c74 | -1.07182 | -53.67107 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9355d96-591e-3aca-b592-28bb05ba8ecd | -1.07136 | -53.67204 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 172f7b07-d435-3e57-b49d-85581f00667d | -1.06951 | -53.65892 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c28be84-4e24-3c61-af49-6894a916a835 | -1.06897 | -53.65981 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e18e6a6f-97c8-34be-bc11-9c135d70ecf6 | -1.06891 | -53.66259 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c6cadc9-6585-384e-8a36-601b48c4c480 | -1.06839 | -53.66354 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 985fc7f2-ae30-32f1-a189-d63460ddd30e | -1.06828 | -53.66646 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca517ad1-0244-3ae5-8646-344bb205265c | -1.06778 | -53.66745 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 200890f9-697a-3d35-a5a3-3639607a0bf2 | -1.06359 | -53.66679 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae57df91-d8fa-342e-a47c-c028ee84174f | -0.87469 | -53.68848 | 2024-10-25 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59de5ad7-9fe5-3e1f-ba73-77c791010613 | 1.57431 | -55.65693 | 2024-10-25 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e398e85-c680-3736-bd8e-2e1083a9213b | 1.56342 | -55.65277 | 2024-10-25 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1d35fc4-1393-3691-93c5-167ca3ce561e | -1.28601 | -55.71854 | 2024-10-25 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ee89407-8230-3552-b440-548f96838034 | -1.28519 | -55.72377 | 2024-10-25 04:36:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b76a119a-d8f9-3912-8920-6e5f08974f3c | -13.4959 | -61.6203 | 2024-10-25 04:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2436ee61-b5c5-38c8-ae96-d67aa6873dd7 | -15.6788 | -55.972 | 2024-10-25 04:36:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 88eea0eb-143d-3ed1-908b-d62f6b839965 | -15.6591 | -55.9948 | 2024-10-25 04:36:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 039eb251-eb72-3af6-b2bc-a0d1b65ea465 | -15.6594 | -55.9742 | 2024-10-25 04:36:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e5f9d2ad-8d5a-367b-8e6f-28b2e9650acf | -16.94 | -57.5268 | 2024-10-25 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| d7c39334-cb2a-3933-a233-cbc917245eba | -16.9596 | -57.5245 | 2024-10-25 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| a06e5461-8e74-38c5-a993-43c1256ec60e | -16.9792 | -57.5223 | 2024-10-25 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| 9a4409d1-f279-3865-8935-08a0fe752f14 | -17.0381 | -57.5155 | 2024-10-25 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 0f4f46f2-d518-3ae9-b4d2-4239acdffe98 | -17.059 | -57.4312 | 2024-10-25 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| d3aab113-3004-3d64-ba19-e776f5322e0d | -17.2537 | -57.5108 | 2024-10-25 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| fd0fb96a-9bbe-32e5-9f28-39b89cb39cda | -17.7671 | -57.3673 | 2024-10-25 04:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| d0e011e6-a29b-3057-b075-caddfb9523fb | -18.3199 | -56.2404 | 2024-10-25 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 87b992de-ce61-3072-91d1-f4286504e7f0 | -18.3203 | -56.2195 | 2024-10-25 04:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 31c6753f-54c5-3a3e-a8cd-01425d74d851 | -9.35274 | -43.36767 | 2024-10-25 04:38:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 655245a1-9b66-398e-9a2f-7c4b16e063c8 | -8.77337 | -44.7042 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 344fa480-68c6-3274-9f8d-438f09fdd8fc | -5.17533 | -37.98618 | 2024-10-25 04:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9ab6a8be-edd9-3c00-999b-c59e35852684 | -5.15374 | -37.73941 | 2024-10-25 04:38:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0a94a08b-2e9e-3785-aff1-8ff42cf77f39 | -5.14755 | -37.73853 | 2024-10-25 04:38:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f3e5df6a-24b9-33a1-8960-ba0ef142060d | -5.14688 | -37.74335 | 2024-10-25 04:38:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94467463-d281-3d7e-9bcf-5c4d42fec7b4 | -3.89588 | -41.03733 | 2024-10-25 04:38:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 583dc2f4-63fa-3694-9fa3-0c894b2f089e | -3.89414 | -41.03477 | 2024-10-25 04:38:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 57cf0432-1009-3319-8815-791115cceb2b | -3.89334 | -41.04008 | 2024-10-25 04:38:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a7c39232-d4f6-3fef-8e05-a0c4cf2ccc0f | -3.89102 | -41.03652 | 2024-10-25 04:38:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4a73fcea-9815-3843-94d6-01ace8e695a6 | -7.09775 | -41.13946 | 2024-10-25 04:38:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17887806-bd8b-3d1b-b8c7-ece0e196d24a | -7.09735 | -41.14243 | 2024-10-25 04:38:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 08f72df5-84fc-36cf-8e8c-acf3f205b792 | -7.09514 | -41.13876 | 2024-10-25 04:38:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8b2deaeb-6360-3f20-b1f5-854dbebc2266 | -7.09472 | -41.14173 | 2024-10-25 04:38:00 | NPP-375D | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72ed2aa8-d7f7-38e2-92db-3abe9df86aa0 | -7.00007 | -41.30123 | 2024-10-25 04:38:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9dfb7aeb-6197-38ca-ae46-37c6280323b8 | -4.91819 | -41.97228 | 2024-10-25 04:38:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edc4a049-c564-3365-b414-1ceaa67b4232 | -3.81215 | -42.63089 | 2024-10-25 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02ed72a5-8767-3a56-adc7-6c6909535045 | -6.0673 | -42.69383 | 2024-10-25 04:38:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6437fe6c-c50e-30bd-8a6e-14848015d6e4 | -5.8187 | -42.73884 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7a8bda11-0510-3468-a69c-2708cf0a21e9 | -5.69264 | -43.17677 | 2024-10-25 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e70a27a5-f550-3acc-ba7c-c0675effcccb | -5.69203 | -43.18088 | 2024-10-25 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5004ff33-ecde-3926-bccb-1e40e0a648e5 | -5.52767 | -42.2346 | 2024-10-25 04:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 7c87d2fc-5ff0-3da4-b327-89bf199d952f | -7.79635 | -43.16651 | 2024-10-25 04:38:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e7e27691-3ab1-3669-8d9f-cf1f2ec5efad | -7.49438 | -42.91903 | 2024-10-25 04:38:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8872d57e-409b-387f-ad42-2827445a186b | -7.27467 | -43.63634 | 2024-10-25 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
