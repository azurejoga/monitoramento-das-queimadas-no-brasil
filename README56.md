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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d6133c4-9c3b-3ce3-be3c-7b7ff4fb7f67 | -3.09231 | -51.32582 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73b412af-bfb3-30fb-a06d-ff9e1bdfaa43 | -2.53656 | -53.97903 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c133f5d6-86c0-3bf5-896a-2761b3fb61c2 | -1.31622 | -51.74999 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e69368e4-f143-310e-8764-30487e47d1de | -2.66084 | -51.71547 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb31baec-24a1-3c8c-81cb-ffae366bd45e | -2.78829 | -53.01093 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd4d57f5-5089-37aa-be3c-782d800e8735 | -1.73625 | -52.73025 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9d1835ae-b08f-369f-943f-61ade043a2a6 | -2.61271 | -54.25018 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8e7540f6-f0b5-3505-bb25-2444429497df | -3.25072 | -54.22423 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85ee8341-df48-346e-bbdf-9af95329bd38 | -3.50275 | -50.46611 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6c32de4-0634-3106-a4a3-c26ac5807f59 | -0.21329 | -51.18882 | 2024-11-25 05:20:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6b3bd41-e72c-3b5c-91ab-0c1bbd667107 | -2.82974 | -54.12082 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90c23651-eca4-3e86-a321-9965d5664623 | -3.06346 | -53.22515 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83d04814-2272-335a-b5bc-dfbd613c42a1 | -3.80156 | -51.17376 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e50c098-1db7-3015-a4ef-c00f2b5fbbd0 | -2.79346 | -53.0071 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c70e2ba-9ed9-333f-ba6e-04e1be19f62c | -4.20211 | -48.12539 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48d6bb1d-7319-3777-baa1-200c4f0ed2e6 | -2.33687 | -53.86858 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 41e60ce7-7f90-36a4-941f-ff7855d9ec47 | -1.68967 | -52.6107 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 308979d6-3ec8-357a-b69c-a664a774cca1 | -2.53587 | -53.97977 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f811491-ddb4-3776-b241-87ee60be95b3 | -0.9468 | -51.63852 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c58eab67-068a-3b31-81a7-36287f40371d | -2.33327 | -53.86403 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 81870db4-df82-374e-8bcb-2db0c6f1b4ed | -3.00184 | -51.55305 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0d94927-6e06-31a0-89dd-b7eb968c890d | -3.51665 | -53.81863 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 629aa4bd-34dc-345b-9652-f05a50caaf00 | -3.51233 | -53.81807 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d88bcb1-d754-32f7-affe-84369ab7b07c | -0.91545 | -51.64977 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a032d863-9112-368a-ad28-f8de7da303f7 | -1.30742 | -51.74326 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99573aa5-363e-3479-98a8-93769a2ba5d7 | -1.23102 | -51.79303 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07bbcadf-a469-3554-a589-bfa33cd22603 | -1.13369 | -53.62 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0809c098-729e-39cf-a132-a99cf865f579 | -3.00179 | -51.55485 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 937d1e03-b308-37fd-84f7-9212ec3dc956 | -2.32882 | -53.86541 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5b674e50-af9c-3b2c-a438-8ac488de56a9 | -3.24654 | -54.2236 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc564464-1f0b-36d1-8a24-92fd1bf72ead | -0.25876 | -51.6484 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d007118c-34cb-34b3-9249-9604b33ef983 | -3.08426 | -53.25818 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7528766-67e4-30b8-a7cc-7fa738ad0fb5 | -1.52361 | -52.05285 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eea7cd30-55a5-33d8-b87c-233bf0276344 | -3.50365 | -53.81716 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84a7fcf5-add2-3876-b24d-d5a206e82e67 | -1.59453 | -52.58915 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa5ca298-037c-3f85-8e3d-82a2b861af96 | -1.21997 | -51.73823 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10e5ee03-30d0-395b-99f7-60294df740ee | -4.25944 | -48.72708 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47af308b-6b48-3457-92ae-b8021c557e68 | -1.10826 | -53.39841 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 70931401-0221-3ae5-ba65-872bb7ace115 | -0.27794 | -51.61981 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e445c67-ea73-3729-8853-9c2c30d656cf | -1.77429 | -52.73426 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2f355a3d-24a5-3f4d-b5c1-d17d3138885f | -3.25422 | -54.23927 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e1bb90a-fa89-3d14-8fd4-2ca5430d2df6 | 0.71174 | -59.23837 | 2024-11-25 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e081958d-c031-33d1-8565-72727bb9bfe6 | -2.81662 | -54.12275 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c6c8fc2-5c8a-35af-b036-07eb2978f014 | -2.6457 | -51.76938 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 053d321d-1d7a-3f5a-be24-14c3fc2ebd3d | -3.54793 | -51.52537 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| daa09804-5be1-34fc-bbe9-5f60202b844d | -2.8163 | -54.71769 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23a1913a-1175-3ba1-8828-6eda90584774 | -3.70604 | -54.39323 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbd7c3c5-327f-321f-baec-2700af3c228a | -3.54881 | -51.52759 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2251b02f-3c1c-357d-803f-bff6bdcb8269 | -3.28389 | -53.84096 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 502664d1-4d8f-3dfa-aecf-f20bec522829 | -2.61215 | -54.25386 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c0fe5b2-d788-33d5-b060-3563fdf5efb3 | -2.33266 | -53.86793 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae61f935-3971-301f-9920-79861e356826 | 1.40658 | -55.88504 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f26028a1-dc90-32a6-b139-5fa796e8c9f2 | -3.24237 | -54.22297 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e739375c-67f9-3068-83bb-dfa3158c6ed1 | -2.73671 | -54.11455 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70acdfaf-aecd-3609-9d3e-4eca3b5baf0f | -3.46962 | -47.6828 | 2024-11-25 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09e54957-af4f-3f3b-bb70-992fed2e2a66 | -1.61489 | -52.57804 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 78c97ab7-b0b4-3443-b874-12533a432d03 | -4.23608 | -48.67226 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18d7ddea-414d-30db-a7db-b25f2436b923 | -3.49369 | -54.02444 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 204d76e0-7dc3-3b0b-af51-1d05d84bff0e | -0.88966 | -51.72037 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7522a09e-a0d5-3250-9bb9-597a49eb692f | -2.83127 | -54.11991 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8410ff1f-20cd-3b4b-a3f1-56ebee0aa7ac | 0.71504 | -59.23786 | 2024-11-25 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29134e86-1eb2-3079-91b4-eabc93de447b | -3.21096 | -51.42317 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6dab43d-5076-39b6-909d-0f09b0386b92 | -3.28451 | -53.83694 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f25790c-b363-3539-ae87-613bc98a92a4 | -3.25072 | -53.5914 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6f5c7d1-7a0f-310b-99de-b72bfbc620ef | -3.89457 | -52.30467 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d8d7fe0-13a8-3957-8190-dfb3511b8c98 | -1.96943 | -53.13919 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54830895-918d-3f06-8bcc-75e9d00b43fa | -4.25864 | -48.69031 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f89e6e-0cd5-35c1-bc96-d0776fd498f1 | -1.98608 | -53.29653 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 681705bf-43a1-3cec-9261-05aec3f1e7c7 | -3.23644 | -54.23373 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91f8fa59-9f11-386c-b995-a39f716c0fa5 | -3.25344 | -54.21572 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d45da8b7-af87-35b5-87f7-5961253bd43d | -1.48735 | -52.52248 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc67407b-fe95-3e12-8c2f-f076fe724dda | -0.96901 | -51.71304 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e5d7ec73-6a5e-366a-929b-0cebbf3ed829 | -1.72187 | -52.49147 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41a04b44-bd3e-3d22-ad60-123d82152940 | -1.45921 | -51.12076 | 2024-11-25 05:20:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53c490b1-1cca-34c4-9542-dd36c1812174 | -1.54899 | -52.58216 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 80323a59-2f02-315c-85ec-e7f9d6e94b4c | -3.48369 | -49.89893 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c0b5398-1a94-3e8d-b743-0da134e45ed2 | -2.66495 | -51.72173 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9f12e14-56a2-3b31-ba70-7f65b2b6464e | -3.50549 | -53.80514 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89d89488-a101-3bae-a2ab-5368ee3b3ba1 | -3.25005 | -54.23861 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 060497a2-1064-3962-a9fd-355855ba2d5e | -3.28854 | -53.66563 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4de71a32-1f9d-3ed3-bb4c-df385dc670d8 | -3.87071 | -52.20754 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e89634b-2455-3719-b0ee-261b41f8f40a | -2.79663 | -53.01683 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a2c1bb8-2918-353b-98dc-23eea487f997 | -4.25529 | -48.67011 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5354faa5-6a59-30be-9209-e91b47e6e2d2 | -3.71242 | -51.79889 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd44ee88-e1b3-39b5-b1e9-d1fe1bdcd135 | -1.3799 | -53.62274 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48a6550c-587d-3a1d-9b52-ad6f162a4dd1 | -3.2906 | -53.85436 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ed8fb19-b198-3888-a767-8c5dada05f36 | -2.91181 | -51.71119 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3523233-22ae-3af8-bf1b-f7acb2d64369 | -3.54926 | -51.52462 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41af2b01-ecbb-34b0-ae02-56a9177af7db | -1.25296 | -51.74557 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b243869e-426e-31ff-83ab-9c4bb3477627 | -3.102 | -51.50171 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28f5d8a2-f83b-3f79-b45f-518685325aac | -2.24997 | -53.6209 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56e655ac-49b4-3f8a-bc73-84a2c82f02c1 | -1.63733 | -52.10694 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4ac06e6-808b-35de-8791-ed336f265918 | -1.4295 | -51.58436 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b18eb30b-b7c0-39b0-9a08-222e373654bc | -2.85796 | -53.96737 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5bf5f5c-1205-3b7d-965f-d7ca08e2f27b | -1.34841 | -54.63348 | 2024-11-25 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1049f6b8-3c4e-311f-8d50-f2d484d99bc8 | -2.97024 | -53.85784 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8cee281-ada7-354d-a5ed-727a9cf8bd4a | -3.71091 | -52.42135 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69372996-7469-335a-90af-5761ef102258 | -1.34886 | -54.63676 | 2024-11-25 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97eeb6c4-a319-3f7e-bec0-d9168cabb3d3 | -1.60121 | -52.57596 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 396d11ba-18b1-3249-aa14-90084f82f6d3 | -1.04792 | -51.7421 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README57.md)
