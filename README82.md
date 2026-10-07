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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adf42440-2ea2-387a-92c8-8133451bada7 | -3.05868 | -54.21489 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7896d865-2c72-3681-9e9b-6cb4878e1cfb | -3.22544 | -53.88295 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44db3804-4ae9-3242-ba5d-1ca39fb08bed | -3.0199 | -54.13713 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ff7d2ff-4ee2-36fd-8c06-44f2cfc7b28b | -3.18017 | -50.573 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4d110f44-f076-3c13-bff2-212183253d45 | -2.98712 | -54.12848 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc240ec9-9466-3222-bca1-7e44afbbb893 | -3.27014 | -50.40501 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e588d1b-5609-32ef-9acd-958e79a18cfe | -3.48493 | -55.43318 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57dd5f4f-f820-38c8-bc86-9792162456f1 | -3.72966 | -51.20895 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 732f243e-7f6a-3ceb-aab3-b33a90170ae4 | -3.21483 | -53.88492 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e97cb2e-6eda-397d-a7e0-f59bb9297fd5 | -8.71443 | -45.20567 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5c2fd7af-9a95-362d-a240-c7b1bd05bdf2 | -2.76291 | -54.10447 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0abc5a45-c6c7-325c-9e4e-33f678b52fc2 | -2.99262 | -54.11495 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 284ad792-e27c-350f-a73b-fa8d3100ee39 | -3.03648 | -53.89746 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6c6b17e-e265-38e0-9702-43696959c134 | -2.99681 | -54.04354 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17c7e20c-a4d2-3b19-944b-4177cb7f4ca7 | -2.99065 | -51.04667 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d6a9dcf6-0977-3d23-9058-8d63af7a7539 | -5.482 | -44.25578 | 2026-10-07 05:04:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 252d26da-1a32-3af4-8a74-0a5a39d6bb2c | -2.89226 | -54.08175 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ae0ba7-48a7-33b8-9105-910aa6570a97 | -3.61794 | -55.27824 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 745f2fd2-fca3-398a-b83d-511b1328b4eb | -2.97843 | -54.77742 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aeaa58f8-c178-3eb7-ab45-ff6992149e59 | -3.65422 | -55.50577 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce6b1bd5-4ae7-3260-b087-0155844bc12b | -3.27894 | -54.06915 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7764a0d2-d61a-3ae2-af38-140ded8cad32 | -3.74312 | -51.21778 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d44c799-4328-3849-99b5-366c3c0eb588 | -6.20686 | -52.68966 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81502357-6717-3bf8-b754-6b4ea3397ba3 | -3.98497 | -56.21791 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6c394fe-d73d-3e7c-9fc1-7f754ef23ccb | -3.49186 | -54.6246 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0ecec26-5284-35dd-8c2e-a0ab890d3bdf | -2.93464 | -54.13858 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4427211-5dbc-3ca7-86e9-486c6f42c90d | -6.15005 | -51.73143 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a427451b-9dc6-35ea-ae6c-9b6ce6a2fc11 | -7.72086 | -45.44149 | 2026-10-07 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 024fadd0-b89e-3a45-b43f-6c602c783034 | -3.95599 | -56.05374 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57780bf4-458d-3046-87e8-1e6412b9b170 | -3.53543 | -54.65248 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1444da29-4309-336b-a604-bc448eaea75c | -3.09219 | -54.28449 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 089f4dea-2616-3b36-9370-857f5eedafc3 | -3.04154 | -53.90915 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a2efef0-d1ed-3457-9199-c5fc2eff139e | -3.52064 | -54.32964 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d2c305d-37b0-35bb-876e-f53a6ab587d1 | -1.56767 | -47.73594 | 2026-10-07 05:04:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb87e847-7cbe-371f-8f6a-7ae81c58a897 | -3.52004 | -54.63961 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b61e896f-392a-34e2-979d-a5c6bb0b7ff5 | -2.90016 | -54.11892 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4101e880-8a3e-3277-b56d-1672d6f45a7d | -1.61512 | -55.11845 | 2026-10-07 05:04:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a38d8bd6-eb14-34a7-be88-4ac6bc0047a3 | -3.008 | -54.23573 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cee06ad2-376d-32ce-bbe0-afd5ca56f15f | -2.84053 | -54.06611 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 307224cd-c3c8-33bc-96a0-1d90c0255088 | -2.96694 | -54.0822 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 451883fe-ccf8-3e51-b950-510e6c37faef | -4.02638 | -54.88435 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57e57ed5-1384-3531-ae5a-3bd8d9caaa57 | -2.99759 | -54.10491 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2888d588-909e-3f85-b245-51b827c2e764 | -3.04841 | -54.21688 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcaf1582-84f2-325c-ad34-8054dcfe1387 | -3.47524 | -59.46635 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b05db9b-78a7-3f49-a9b9-b20b118e890b | -1.10864 | -54.15418 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0ef46bf-f88d-33bd-9fd0-6d5590e7419a | -3.0703 | -51.20898 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9482e123-3de3-3825-b2fb-3f1f3f72490a | -4.24924 | -51.04917 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e360b25-6898-308b-bd90-a7f44ee59227 | -2.89643 | -54.16498 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c119c07e-a1f8-39e9-8acb-276a7a4cc658 | -3.49973 | -53.43881 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6a1d4ea-5f3c-3340-8ec7-36d656fe6776 | -3.07927 | -54.23598 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baa0f862-d35a-32fa-a9e3-4cc7fc0b920b | -3.33207 | -53.39104 | 2026-10-07 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 868481e5-c7d4-34a0-b5d4-5bcaa43d7ae8 | -2.93579 | -54.15311 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fce9baff-f9af-3997-a559-9fe05eeb22e1 | -4.3276 | -55.90048 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98371fa6-f70c-3c8b-8bf0-9d46cc564e0c | -3.10056 | -53.75023 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9190d7d-f77d-3510-a825-390d7a1b72be | -3.21537 | -53.88139 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 706cdabf-4571-3a2d-bd35-d73c0d8bd80d | -2.80574 | -54.13619 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7cf5a1e-c6c4-3058-b52d-5eb39113819a | -4.45312 | -54.96226 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e8c75ac-071a-375b-a1d0-0b87fb80cb12 | -2.57329 | -50.68112 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df871bbe-fc7b-39a5-9a39-cc6bfe1262bc | -3.28673 | -54.06312 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c75beb7-f129-397f-bdca-c918ca23fa0a | -2.7657 | -54.10849 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 881e5712-3994-3a49-a02e-1bda3b83d4c4 | -3.66043 | -60.62309 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65d4a436-18af-3d14-a7c5-134751824e48 | -6.00788 | -53.50565 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e32a24ee-699b-3000-b90f-90645fd092f7 | -3.28952 | -54.06716 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b36f455a-4fb3-3c7e-b329-5c41187e03f7 | -3.02692 | -57.47885 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06e7eb56-02ac-32a2-adec-79682b6d9879 | -3.09507 | -54.1558 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55190ff5-0164-3f84-adcd-690364da69b3 | -2.87305 | -54.13986 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76d97661-9038-3bf7-bbe1-2936a253292c | -4.11436 | -50.8244 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95e49c8e-2bb2-3bc0-9cc0-c110e326e711 | -3.04594 | -53.8807 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c5977c0-bab9-3507-9156-9e176c446a45 | -3.17218 | -58.64181 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f3a300b-960d-3d2c-b849-b99c8c0a2ee0 | -3.57571 | -54.65512 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 28fae54e-35bb-33c9-a341-7e79436945b9 | -2.80741 | -52.08507 | 2026-10-07 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 540c5a59-45fe-32aa-a50a-e3dec1efe33a | -3.66791 | -60.62772 | 2026-10-07 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bba5606e-efce-3077-9875-bd000f10c268 | -3.04159 | -53.93098 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb1a54f8-6c34-3be9-b4ef-d51a94dba36e | -3.0756 | -54.14926 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5415908d-8f29-3056-af2c-39a2bb6485ec | -3.01936 | -54.14062 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d919e34a-85c5-3aad-8186-e3e8e89e1c50 | -3.08717 | -54.27298 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c71c68bb-cd32-300a-bf10-706949190ece | -4.18915 | -51.13412 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b015db10-f3b4-3faf-a8cd-0e5aea1fec66 | -2.48747 | -58.06571 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b465dd-d505-3f67-96b8-72829f2fbb4c | -3.11791 | -53.70514 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3143089e-af66-3589-b270-b173938dcae2 | -7.27762 | -46.15693 | 2026-10-07 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 0fe8b51f-f9b5-3e99-81b3-f64f390d8e5b | -5.82706 | -52.00089 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c161464a-3aed-35fd-b3d4-6c9a80bdf7b4 | -2.42798 | -56.53244 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2bb6119-579b-3611-b75c-a456364c835b | -3.27941 | -54.02218 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5aa6987-0364-3ec8-aff5-49096c1c9f08 | -3.12747 | -53.71028 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 506f276c-7038-3e3f-838e-4b4a44d623a3 | -2.93628 | -54.12806 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 659d2b03-345f-3081-a6cb-366b71b9f2d6 | -2.92204 | -54.19758 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dd8a253-0fa2-3fee-a606-f2f8dbdef18c | -2.84012 | -54.22073 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051064fa-8f1d-349f-b8ed-5f9c004feab9 | -2.87329 | -54.20442 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46ed0d7f-0859-3212-9508-eb1e21a12451 | -2.96919 | -54.08975 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 379b5728-a723-33c3-afe1-98f71b7534fc | -3.12803 | -53.70669 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d67b4e1-30c2-3579-a5c3-62de5912ab45 | -2.10419 | -52.05976 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4182fdb-8ab0-33bb-aa9d-cf01ab659560 | -2.99347 | -54.04302 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7e8779-ee0b-3ef1-82ed-e1dcca75a771 | -3.51349 | -54.65987 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 542e24ac-65b2-3734-9872-af633f9f8f9a | -3.50965 | -54.66281 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a965a3a-0d36-3e14-840e-b6d450cd4f7f | -3.85137 | -55.98369 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d7b91984-bc0d-305b-aaef-8708cb9ec36b | -3.7954 | -58.35165 | 2026-10-07 05:04:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9f29677-2ae3-3578-a948-05b4aed5b2c0 | -3.75935 | -61.17347 | 2026-10-07 05:04:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce9be883-54a2-38a1-a0a0-8788c978226c | -3.54431 | -59.49426 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf6d76eb-05dd-3188-b75f-321ae643d18f | -3.08601 | -54.25849 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ce6a649-0a7a-3c3b-84b5-41bd6329956f | -3.85035 | -55.8388 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README83.md)
