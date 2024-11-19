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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91e27dc0-1aae-3535-a8b8-33f1a4d86db6 | -4.56328 | -48.01589 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eda04d29-786b-3b3c-b261-fc2f3b7dd31c | -1.202 | -51.7645 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b98626b2-8ec3-3a4b-9a12-78bf9e4a072f | -1.26745 | -52.12812 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bcfee69-f015-3360-adb0-24f510cfc503 | -3.57803 | -50.15821 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c1ff713-696d-32e4-ad15-55ce15298f66 | -4.11459 | -51.04887 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfac2fc2-8649-3c36-902f-e4ffa2d0ccc1 | -2.69175 | -51.80231 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bf5f5b4-becf-3707-ab15-ec33f54783db | -4.54328 | -48.00647 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4045f848-ddbe-3fc2-8028-31f85a4d6294 | -4.39629 | -47.77531 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3238a88a-cd87-3735-96e8-3f2284cbb002 | -2.32434 | -45.65161 | 2024-11-19 05:08:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 414f31e3-af71-36d3-9a17-d7196caf3d33 | -5.97795 | -45.36788 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b7b17e96-e119-3869-b19e-6d032bec34e0 | -1.54261 | -51.11117 | 2024-11-19 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2281a56-20ee-3a94-accb-693d6162dbfe | -3.36542 | -50.82113 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88d0c213-1400-31b7-bfd9-9b6e3cd7593e | -3.66033 | -50.44463 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5034b5e8-6332-36ad-88d0-89cf1d8b891c | -4.55805 | -48.01529 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 4fc2e7c5-dded-3824-b496-03c4df70ea35 | -2.95917 | -51.41549 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d20cfb57-843c-3d33-b8bd-e68a16ff3aad | -0.8262 | -52.86289 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab649b65-b5a8-3660-a235-28aa001e6346 | -3.66534 | -50.44112 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4660e0c1-1acf-372b-8d52-fd470eb11f53 | -0.11945 | -51.42689 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf4e15e5-4e59-3223-887c-acef9100c2ca | -2.65734 | -48.48356 | 2024-11-19 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1bbf5561-9662-34fa-ab7f-851a48b1be1d | -4.99132 | -44.33711 | 2024-11-19 05:08:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15fdeebc-e12f-3193-967f-f0700eafa409 | -2.61674 | -54.53923 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 759f49f2-48fb-3c14-a22f-6fc2c825fcda | -2.99862 | -51.45852 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c47fb2c3-4f3e-3e2b-8a0c-3e8a0ab0b095 | -1.63363 | -52.58313 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 908176c2-1797-3678-801a-b3f3acc7bfb5 | -1.05005 | -51.74395 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f4470aa-ef73-3559-9589-fad6e76951d3 | -2.66388 | -51.72116 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f019710a-db38-3561-bed3-a8e51e96a4ff | -1.86379 | -53.19799 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ab4f370-8b35-30f8-b52d-00cb57edcd48 | -1.39186 | -52.42128 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 029c1288-2a4b-3065-9b97-7f8a504fbdcf | -5.98501 | -45.36373 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a56b432f-173e-3dac-99ba-121f2ff87dbd | -1.43544 | -53.38451 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a718de-3238-39d6-8904-f1b36e2a3f0f | -2.25331 | -50.57033 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d931a08a-a95f-3de7-a6a4-fea67053cd3b | -3.90152 | -52.40596 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1508c98f-1379-3d99-9d6a-90003833a15c | -4.39089 | -47.76431 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d92b1df4-6098-3911-bac5-130ace9261d3 | -2.19979 | -53.66077 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5dc4826-1959-362f-9420-3a012f35cf83 | -3.9832 | -49.92204 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34ab9dcb-10b6-37cb-90e7-6aa67e32a024 | -1.95305 | -53.004 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 921c544a-37fe-3a98-be09-10771eb5e2ec | -1.66024 | -52.53346 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff874457-8b67-3f25-8f91-0521e8c917b5 | -4.54617 | -48.02324 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af795c82-0f96-3160-a35f-d2fffa18f729 | -0.93037 | -51.63889 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a76a5b36-500c-3a6c-a04b-14bf7cbc749a | -3.06059 | -54.40355 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ecb953d-72d6-3215-999c-cfc053cccfe1 | -1.27558 | -52.75768 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60850f72-0245-34b6-b0d3-f632d79f3d8d | -4.56329 | -48.01606 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02edd6fa-2a28-3847-ab4c-b03fd5f0c666 | -4.54376 | -48.00326 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9ca1f15-f848-3037-af80-adf1582e030e | -1.20235 | -51.77151 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0a57344-7f49-305f-8075-9361b48538f2 | -1.621 | -52.48453 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a6cc18-3b41-3c6f-8bc6-717cdb4947ac | -2.61175 | -54.05053 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a5d7906-514c-3476-992f-ffa3baa61c30 | -3.04237 | -49.47171 | 2024-11-19 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d8a075e-86c4-32ad-8a40-8acee71c6d75 | -1.70458 | -52.14386 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c20aa211-6941-3df5-b5e4-50d3c0a11138 | -1.5856 | -53.80903 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e2950a-b9ce-3b10-87dc-2e1a056d3926 | -4.10616 | -51.04753 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ae6929b-f778-376e-97d1-aa81b19a47c0 | -1.14597 | -51.69189 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35692303-01df-3d2f-ae86-947a50ee2544 | -4.11096 | -51.04436 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9e62377-1bf8-3bb8-b62b-52e8613b0ded | -4.55421 | -48.00504 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e4d075b-9f4d-3180-bb7b-384a5312bc80 | -4.54898 | -48.00417 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65786c6e-fa98-3752-8ce8-dbd8be6bf590 | -0.9564 | -51.7264 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71b5b18f-647b-337a-85ca-5a020e9d2a26 | -4.06027 | -54.05138 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbf5dabb-2c23-3177-8f5b-5eacc4bd754e | -1.92432 | -54.05782 | 2024-11-19 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0df93fd9-6a30-3f82-a959-6abc49125ff8 | -1.78871 | -53.59254 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1bba6b-4521-3719-9182-1ed8436816f0 | -3.08874 | -54.6664 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb08f363-5526-36d7-8e41-903e242186a1 | -1.33173 | -51.86169 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d30d238b-011e-3157-abff-1cbdb7d8bf45 | -1.15692 | -46.75076 | 2024-11-19 05:08:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 49b8b33c-77dc-3209-81b7-2095bae6296d | -1.5868 | -53.80133 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2270571d-36f9-3a59-bf9a-f2362c97522a | -2.72245 | -51.81213 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c75939fb-de9e-3901-81c8-2c31552fd65c | -3.14136 | -52.98056 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3b25f58-4efe-3d3f-aa18-5bcf01df0bb6 | -3.06345 | -54.40786 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf673a2e-bc34-35df-b829-8f5f4c7e483e | -3.47958 | -53.87028 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1a2788c-8c47-3a1c-b883-d4383e022eb8 | -2.86556 | -51.78598 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc96c6fe-3400-3793-b076-336307ebf78f | -3.31308 | -54.08286 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e48aad8-3476-303c-87c6-aa7201536a28 | -1.98426 | -53.13913 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6133560f-34c7-39aa-8a8d-2d4e44350dfc | 0.61392 | -51.77394 | 2024-11-19 05:08:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9444a58a-da96-30b1-b2f3-ceb9fe261b9b | -3.13766 | -52.98002 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ba71c84-48cd-3746-8ba2-131ebeab5726 | -2.00414 | -44.79521 | 2024-11-19 05:08:00 | NPP-375D | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| abf90574-9910-305c-b558-c2c72f765efe | -1.20358 | -51.77945 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e16701cb-04e1-3316-92df-728c2f42fe3c | -4.57901 | -48.01844 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4cf6122d-3d4c-31cd-a40c-2900d493f4d9 | -2.71531 | -54.59866 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d995a6d-3442-32f8-806f-822236de1226 | -3.66696 | -54.65483 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f3cb49f-ab6f-3ee3-998f-f0b7112f90d1 | -2.85816 | -51.58554 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3b5f783-2d70-36ab-88ca-064c6df611af | -4.39625 | -47.76488 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ee76388-1168-3a2d-a8e3-fbab1e033607 | 1.18559 | -60.22135 | 2024-11-19 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a758a566-7f0c-366a-9d9d-74e36066211a | -4.39043 | -47.76757 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 812df539-096d-337c-96ef-5a61d2387ad9 | -0.27359 | -51.54436 | 2024-11-19 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6939e2c9-2951-3139-a9cd-2a7c791ec8f9 | -2.19854 | -53.66865 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a785a2ab-414a-34d1-a604-bd613c83e199 | -1.41959 | -52.43898 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f66bea00-7d3c-3b5a-8f61-c60f42a435a0 | -3.33304 | -54.07 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 179c0048-dade-33c7-8d0e-a4fd13e69779 | -1.62763 | -52.62232 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6669901-c4b7-36af-be42-be7605b6a4e2 | -1.92409 | -53.35281 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 638f643b-db47-3f65-bacb-c24e5a7d7d3d | -1.20308 | -51.76671 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fc9f41a-6cf3-3ad7-88e6-10bd6daed537 | -1.57458 | -55.17663 | 2024-11-19 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63cc1c83-f40c-3ce3-8bc7-9f32a31a06b1 | -3.98843 | -49.91817 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ebcb2e8-796d-3c41-b37e-8265a9fbbf7e | -2.373 | -53.68185 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 820a96ef-c292-3d55-a313-752a79191d67 | -3.89531 | -50.07399 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6192e5c3-ae2b-34c4-ae9f-366281935f95 | -4.38951 | -47.7741 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 927705f4-6c23-3fef-8062-93c1bf51d96f | -2.89583 | -54.00594 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6e86d4c-b9c4-3c76-933e-25173fc09726 | -2.23567 | -53.66188 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acf24f81-cb17-33fc-bae9-c6eb2418a794 | -2.10833 | -48.1047 | 2024-11-19 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93714a3f-a4cd-3544-831f-e84d33fa068d | -2.64747 | -48.48213 | 2024-11-19 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2890e879-c845-3cb9-9262-43a3635b6f5f | -3.74302 | -54.4505 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc3c6018-c7be-3836-8e6f-da8570d2f214 | -2.64254 | -48.48138 | 2024-11-19 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1c7f248-da89-3ef5-ac15-34e2196f1a2c | -0.91845 | -52.53912 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c9bbf8b-826d-3995-a545-0e6dc4f515d2 | -1.67981 | -52.55443 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7502ed7d-0d2c-3429-91df-e2ea5cef6eb0 | -2.59303 | -51.71896 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README42.md)
