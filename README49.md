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
| d7cf0d9c-5c19-3357-a655-110d62e68f8c | -1.12733 | -53.40451 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e28cf945-f5ca-310f-af5e-619e39b2a581 | -0.93848 | -52.419 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3609d6c6-b818-35ce-99d4-43287aef3bfd | -2.58169 | -51.92186 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a60feca-7b10-3513-be9e-84e26f495d46 | -0.92704 | -51.7355 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 543e5fe1-a015-35d2-aa90-a102cbf7ec87 | 1.35361 | -55.96957 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d365e502-e3ad-3f0b-965b-0d5dc230dbf0 | -1.79046 | -53.64003 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c416e042-4ad6-38b1-9ec6-6683d86c5ce1 | -1.7911 | -53.63599 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bb0e0d1-8fdf-3997-986b-e95e30e9b0f1 | -3.00141 | -51.54793 | 2024-11-23 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfb6de7a-1841-39dc-a671-cf07fce2fd1c | -2.6154 | -54.25681 | 2024-11-23 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 619ddfe8-5a00-3db9-a58e-410e95808a8a | -1.96915 | -47.83477 | 2024-11-23 05:10:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6f619bd-ce6f-3a7e-86ff-583e9209dc71 | -1.607 | -52.58319 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fb18b10c-5dd4-336f-91ca-269d77c2c596 | -2.76318 | -54.04954 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e6b3ebd-77fb-344a-bc09-5203e65db10d | -1.12017 | -53.4034 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b891579-edc3-3178-9b51-fefb15ed42b1 | -0.96551 | -51.72099 | 2024-11-23 05:10:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8237da17-07a7-3aa7-8f37-b440fbf6fe3f | -1.77643 | -53.61301 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1bc83721-b25a-3b2a-934f-e26d682ca2a5 | -2.53084 | -47.52214 | 2024-11-23 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc1b899e-e919-3c14-be78-2f0dba8c8c57 | -1.29761 | -52.2777 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e88392af-e7e5-3974-b188-d8bc95990346 | -0.9164 | -51.64631 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ebdd064-4947-34c4-9b1a-a582b2e64e9b | -1.61829 | -52.58494 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea2335dd-b8f5-3aab-8f59-a167b68efc5d | -2.16637 | -54.46367 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f598271c-1a56-3a15-99bf-ed0f5d061e8e | -1.37526 | -52.8639 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ec05501-21ec-354f-9d83-360874f4e33d | -1.66917 | -52.65984 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6f91829-7c0e-34b9-99de-6f47be7a2f57 | 0.15604 | -51.23261 | 2024-11-23 05:10:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42c537e7-b89b-3c1f-8078-2e34bde79072 | -0.82649 | -52.87806 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdceb8c8-2bbd-3904-9e49-acd08230b91a | -1.62044 | -53.31399 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d1117f4-ba17-32c5-aed1-3f28a3578f07 | -1.20803 | -51.94701 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3e9f0332-698e-3c63-b65f-8569c5262958 | -1.79276 | -53.64865 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb461a79-916e-3227-9e01-538ab9583be2 | -1.38155 | -55.1817 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eebe3e89-5c08-32a0-bde0-674a8fc7cc0d | -2.38137 | -49.10001 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0fea5aa8-2eb1-3b0b-862e-3bbe09f89f5f | -2.58693 | -54.04032 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbf19cc8-3d84-31d5-ab76-80d85332c468 | -2.57501 | -51.88586 | 2024-11-23 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37ee7707-1b9f-3c26-91ac-988858e59a64 | -1.44298 | -54.49059 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f10694c-1f91-3e9c-a725-f47dc73b6a84 | -0.80926 | -51.61637 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 396159e6-cd6a-36ce-827e-ad1e8b239045 | -1.14226 | -53.40277 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9242f95f-7849-3f55-9f5b-82b901a4993f | -2.59276 | -54.04926 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70f0b7d5-6226-3f99-acd8-87244b4faa50 | -1.63886 | -52.09729 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b1066c8-5a3c-3d11-9df3-abfb8ae35971 | -2.75237 | -54.09648 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0268211c-7e2b-33ae-9e1a-fe71ca78c0be | 0.69486 | -51.43969 | 2024-11-23 05:10:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eaa20346-3025-32e0-8235-f8c92b3ea38f | -1.91612 | -53.34201 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa23bf35-9147-3643-bb8d-a87b9e7ff8c2 | -1.20098 | -54.03344 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a743a20-80e7-3452-94cd-b377953bf951 | -1.78144 | -53.65106 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43805d5a-e980-37d9-b897-88b55f7a7ec0 | -1.2429 | -51.74387 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e0963acb-7765-380b-bb55-f6dc3115014d | -1.11069 | -53.39357 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6b62b43e-d796-39a8-b87a-c0751609f9cd | -1.785 | -53.6516 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6826f4dd-d8d2-38d8-8379-69afd83a52e3 | -2.58218 | -54.04762 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 750ea345-d8c1-33a1-bccd-bb5bc6897f83 | -1.18172 | -51.96301 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d6342f7-0651-3813-be2d-2766c4de4301 | -3.07997 | -49.21227 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 900c4b66-078f-30d0-b935-4af0d3749790 | -1.87004 | -55.29676 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32c74ac3-2f31-3e1c-98b9-d1012c796c1f | -1.61076 | -52.58378 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 42d8f6f8-d3e6-32af-a7bf-96e19b5521ae | -1.89268 | -53.32552 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f7ef442-2f99-3bf3-ae73-59c210e817f6 | -2.20771 | -48.91521 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4ec643b-e95a-3b90-a66b-b63ab6c33089 | -0.1069 | -51.65916 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a2f4c40c-0467-39c6-9646-b6a70db2e2ef | -1.4128 | -55.15744 | 2024-11-23 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6cabef-8ea8-3918-94df-73dbf9330e25 | -1.05678 | -52.62918 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de07f9c5-1abe-3df3-bd74-4f36dd24131a | -1.63029 | -52.61207 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43a792ac-23fa-3b85-8b08-7f63903a6d01 | -1.13806 | -53.40622 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 704af718-c33d-38db-a8f7-87034ea7ac5a | -2.68312 | -52.07254 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| facb69bf-4a71-3612-8a33-98956eae1564 | -3.01125 | -51.01555 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6b86b84-706f-3dcf-b5aa-4e026a4c8502 | -2.38869 | -53.79969 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e316db1-dcb4-3ccc-9112-e140d7b2f764 | 1.38956 | -55.91844 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35a94143-9276-326e-a416-10604a05db81 | -0.26356 | -51.55528 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11b925d0-bb92-3b14-8da0-a8b62aefb474 | -1.19883 | -51.7715 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a5d1a53-26c9-3b42-961b-42ac7f7c59c3 | -1.72642 | -53.25975 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f08fb7ea-e5cd-3360-8c2c-db6d4e2321d1 | -2.16097 | -50.46479 | 2024-11-23 05:10:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb31078d-203b-3d18-9807-c955af275b26 | -1.2227 | -51.79736 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8bb1a68-122f-3dff-8eae-5f54d10b2fa9 | -1.74968 | -52.3896 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 613d60e8-23cd-39e9-ba60-1d8096165e3f | -1.27541 | -52.9794 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a41a27fa-fb02-34f1-953b-5e587073e8fa | 1.40832 | -55.90432 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8bc0105-48fa-387c-b393-114d6bcfc2dc | -1.99246 | -53.1389 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f03c1d34-44af-3bf6-b8e6-3414c64e601d | 0.55753 | -50.89324 | 2024-11-23 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc01e60-70ed-37c1-ac9d-7d0e8090b2ec | -0.92341 | -52.54179 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 794cdcfa-e8fe-32b9-aeaf-34eb3513ef65 | -0.24137 | -51.62112 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd773c31-f3e6-337f-a8d1-a2f40ba5bd30 | -1.63675 | -52.69635 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16df533a-88ed-35c2-b83c-871e2a68663e | -1.70779 | -46.86759 | 2024-11-23 05:10:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5ad9f47c-00bf-35e9-886d-3adf03e2cdb9 | -1.24577 | -54.02029 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c5dc6d7-3d37-3cec-b9a9-fde73ac12c8e | -1.62674 | -52.60485 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 406cc1ce-35bd-37f5-88fb-cab759da6c33 | -2.70176 | -46.27089 | 2024-11-23 05:10:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad6053a3-f7b8-3aab-a270-da01d9733753 | -0.77218 | -51.77441 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f830e6b6-aa51-34e3-88bb-17859b9fbcd3 | -2.57325 | -49.09509 | 2024-11-23 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93afc1b0-f921-3820-86c2-3b63a3be9179 | -1.06735 | -53.65142 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7b140a7-93fb-3ebc-ba0f-062ccc3e4247 | -1.45042 | -54.51066 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b29900c8-0209-3bd8-a3c1-c3ff0a28fe5e | -0.18334 | -51.60708 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f145307-f897-3707-a3af-fa4a0954e743 | -0.94879 | -51.64619 | 2024-11-23 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34f11575-26f1-3ecd-91c4-cb2bbb845ee0 | -1.78983 | -53.64407 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5afe763d-8c20-311f-8e11-9bb0c01dec58 | -1.11722 | -53.39878 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60d6b29d-0829-3ae1-abb5-351ba54dca5e | -1.06806 | -53.18066 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2664cd30-54c6-3504-9fd7-a7b696a0322d | -1.26046 | -53.3649 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 43680dfe-d865-3d4a-bb7a-7af5117a0ab7 | -2.13329 | -50.70023 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1d704ff-e4b7-362d-bc5b-8d0d188ba91d | -1.93411 | -54.06563 | 2024-11-23 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2715c045-e434-35f2-8fba-ac72c82caaee | 1.15684 | -50.69765 | 2024-11-23 05:10:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb4618b8-bc6c-37f3-a155-78374cfaf76e | -2.584 | -54.03591 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 29081d15-6af0-33b3-9513-47fa57378e8b | -1.35965 | -52.55421 | 2024-11-23 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5026c353-0286-3e03-b43b-1dc76c484a0e | -1.77055 | -53.60381 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb530b9e-3d3b-3316-8458-6c6fd1573db0 | -1.22481 | -53.68667 | 2024-11-23 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a01f713-a4cf-39e1-b582-ac01bc753af3 | -2.10531 | -46.36567 | 2024-11-23 05:10:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2150aa8-2727-335d-b60d-bf0657f87b93 | -0.26342 | -51.52951 | 2024-11-23 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec179c61-0168-398b-9765-278e6f72b260 | -2.01639 | -51.1789 | 2024-11-23 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 710eaf87-75f2-3bff-8bfb-68af7e421a7f | -2.17967 | -55.14685 | 2024-11-23 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cd6db198-b0b3-3ebe-80e3-86aad7423093 | -1.66265 | -52.67731 | 2024-11-23 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40adc625-40b9-38de-98e2-94b9003e5810 | 1.3868 | -55.92237 | 2024-11-23 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README50.md)
