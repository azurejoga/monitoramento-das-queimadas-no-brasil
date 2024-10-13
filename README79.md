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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fccb1ba-91b2-33be-bd0f-05254c252a07 | -0.43486 | -52.04351 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f78c12a1-219a-3d86-acbf-28f41da5134d | -0.43197 | -52.03916 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f59cd703-09fd-326a-b386-6b6a32cc468d | -0.42779 | -52.0659 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac0c151f-71a2-321b-be47-d8960ee22699 | -0.42719 | -52.0697 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f055394-5114-352f-88c7-b14bed22e8d0 | -0.42431 | -52.06537 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 624f93a3-a8c0-3880-888f-af4d64e5a4be | -0.42372 | -52.06917 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4df01f5-c2ae-36e9-84e7-72d3a53444f3 | -0.42083 | -52.06484 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed852ca9-919b-3751-b6a5-3827c4051433 | -0.42024 | -52.06864 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be3d4758-244c-3d91-a6a3-d95bf6645901 | -0.37135 | -52.03 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e732e38-0196-3ae5-9d92-7dbb503e394d | -0.12592 | -51.57772 | 2024-10-13 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 23b04b5e-df28-3315-a8d0-706306276a33 | -2.00726 | -53.30126 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c61eee-3e82-3b34-be6f-34eb831e49b5 | -1.74383 | -52.2482 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d03bc1de-732b-39f9-ad05-88d4f8615f09 | -1.71411 | -52.50408 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a83c59f3-bf0f-3b2e-be01-5d2a41d970b4 | -1.66835 | -52.03934 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25232115-34e5-3bd6-9a2f-3cf3028862eb | -1.66415 | -52.13429 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd1e25ca-de3a-386b-8be3-7c5128eb5a06 | -1.66064 | -52.13375 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3387031-3268-395c-a4bd-098ed661862d | -1.66003 | -52.13762 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0317ffea-8015-34c1-af41-509f5c08a0ad | -1.65653 | -52.13705 | 2024-10-13 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc3a04e1-04a7-3f30-a049-0a27be2382bb | -1.59288 | -53.34376 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0f37544-511d-380d-abe0-98157c62d81d | -1.43782 | -52.86036 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82674c87-7765-3e1b-bffd-098d7490bd3d | -1.43724 | -52.86401 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d310771f-548b-334c-bfdb-6f566f412dce | -1.43667 | -52.86765 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f166e7e-d8a5-34ed-a966-25da538f567a | -1.43441 | -52.85982 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c65351c-b110-345a-85ff-0cc65f9a7939 | -1.43384 | -52.86347 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c30a635-d1e4-3c44-b485-9384c58b7d23 | -1.43326 | -52.86712 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76031d48-ec58-33b9-a4eb-792019e0a96e | -1.37306 | -53.00634 | 2024-10-13 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81b4729c-4ed4-33fa-a2fd-3fd950534e3b | -0.83868 | -52.36264 | 2024-10-13 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7d4d090-cc37-3c49-a938-3a03bc89de71 | -3.42917 | -52.77363 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 174ebefc-34a8-393e-a0d7-e85252dc04b2 | -3.23407 | -52.8878 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dac68a2-6a55-3505-a2b6-15e886a67352 | -3.23062 | -52.88725 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc0a0feb-3803-3728-8660-d776cafcb893 | -3.17766 | -53.16034 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e9bcdd8-33e1-3dc6-826c-4d9bf49e8d70 | -3.10658 | -53.03614 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbe417b4-a9d6-35c2-970d-f5ca70c19cea | -3.10485 | -53.04727 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4a0f2be-7f40-363a-ab5a-51ea45945750 | -3.10316 | -53.0356 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4aa401aa-a011-32f3-9c7d-d6cebc648d94 | -3.10258 | -53.03931 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 49a3ca8b-19e8-39fb-a94c-56a20e47066f | -3.102 | -53.04302 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 61fddccb-a099-3788-9b66-7420e8081fe1 | -3.10142 | -53.04672 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 2566fa13-42a6-3744-aeae-b6ac9017670b | -3.10085 | -53.0504 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e0ae1b2e-ef2a-302e-a985-2d3e8111406a | -3.1003 | -53.03135 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7f15d0f6-74d3-3df0-b2e9-5be2b297533f | -3.09973 | -53.03506 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 941cf741-af52-3bed-96a0-47b53fe308d0 | -3.09915 | -53.03877 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 153d85f2-1b89-3221-9a50-22d4e1b01b54 | -3.09857 | -53.04247 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e5793ca5-48a3-31d0-8b65-bd6e381eb89b | -3.098 | -53.04617 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 1daf7d42-ba34-3247-819d-cb5e27087bd3 | -3.09743 | -53.04985 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 72e173ca-a18f-3455-b25f-f309c1fc8031 | -3.0963 | -53.03453 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f038021b-1ac5-3f58-84f0-f69dc1534a5e | -3.09572 | -53.03823 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f19255c4-855e-37d9-8459-9cd3eff97b76 | -3.09515 | -53.04192 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1639a45d-8507-31c4-852e-20dc52ffdcc2 | -3.09458 | -53.04561 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 01991004-1ac8-37b1-a34f-50945bc59bef | -3.09287 | -53.03399 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 98fdc516-9590-3697-8f91-b0b725a1d61f | -3.0923 | -53.03769 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d2c3e6cd-3ab0-3eee-991c-cb14fbbb6de4 | -3.09172 | -53.04138 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 20fc3d2f-8d86-3c69-b3f8-67669b8d9841 | -3.08944 | -53.03344 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f438ad60-fa6a-341f-a58b-b4657eaf70c6 | -3.08887 | -53.03715 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9f3ef70-5675-3842-ab36-bfe13190f561 | -3.0883 | -53.04083 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e46a87c-deb0-322e-85a5-c236f9df33ea | -2.98707 | -52.90412 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8fac826-10b8-3a4f-b688-0ad1cd68efb5 | -2.9865 | -52.90786 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af29c5ab-a393-38f6-aec6-7f7357608065 | -2.98363 | -52.90358 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38af1497-380e-3e44-b522-133a836e5e3e | -2.98305 | -52.90732 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53f0cb07-a16c-39af-bafa-a54b02cb14dc | -2.97331 | -52.90198 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 527b6b9e-0d20-3b9c-aea6-28dd8a495e3d | -2.96928 | -52.90522 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 845009ca-4adb-30f8-91fe-7e7754c90ffd | -2.96584 | -52.9047 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf84c0fc-aa75-3741-9bc8-5c7b29e73ecc | -2.96526 | -52.90846 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8d99741-1d08-3326-b9ac-5d22f8d4ea0d | -2.9624 | -52.90418 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c63b036-f232-38fb-aa50-7dbb45ce31b7 | -2.95499 | -53.04347 | 2024-10-13 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a32601d-3e87-3e68-ad1d-94f648c1c1b0 | -2.67527 | -53.3407 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 621ff677-7e47-3d1a-a43c-27074f48a726 | -2.67471 | -53.34431 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 158ad942-cfc6-31ae-9ba8-2358a258575c | -2.67416 | -53.34791 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aaa0d48-8139-3366-b9f0-c18ad246a858 | -2.67133 | -53.34378 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8fc78a14-c41b-3543-959e-eb880ff076c1 | -2.67089 | -53.34422 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d35a8397-07f1-3c9d-bc08-6b2661aa0b1f | -2.67077 | -53.34739 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cde441e3-e4ac-3821-afa9-671d35b03465 | -2.67032 | -53.34782 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 453927d4-928f-395a-8ca1-b69a4797b311 | -2.67021 | -53.35099 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0428898-b519-3db2-9461-59282678b291 | -2.66976 | -53.35142 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea6dd423-885f-3665-abdb-36a8d730eff9 | -2.66751 | -53.3437 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2b54647-a6d0-3790-a9e2-c38aff1c404c | -2.66694 | -53.3473 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81b55ba4-ca17-3e6f-aa2e-48d6166c1004 | -2.66637 | -53.35089 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0156b360-87d7-3d85-857c-f8a1062acb4e | -2.66355 | -53.34678 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96333f28-d2d3-3ea6-a10e-ec7f0eaed044 | -2.66298 | -53.35037 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94e70a9c-f37e-3584-8a68-fb1f4df67a3c | -2.66242 | -53.35397 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 889abf55-2cf4-3e6c-a4bb-49c5c1972350 | -2.66016 | -53.34625 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 760c36f7-cd93-3c11-8f6c-173276269501 | -2.6596 | -53.34985 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ebfc3fc-2725-3bf5-b972-079466010c7f | -2.65903 | -53.35345 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937d9da0-661f-3ee2-9fbb-c03930fc6af8 | -2.65621 | -53.34933 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d03fcf70-7f8a-384f-be70-b675244f9134 | -2.65565 | -53.35293 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a4ef32-90b8-3ebf-afd3-0075e2f69f6b | -2.65283 | -53.3488 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2deb906c-ff7c-3aee-b1cb-9427cc9b442c | -2.25972 | -53.4752 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d31dbfd-635f-38d9-a254-b36d21a0e470 | -2.25916 | -53.47876 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b049e56-4cec-369d-a075-7f8cf42f519e | -2.2569 | -53.47111 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 181e8152-675a-33a7-aab4-45b0cb7d84e5 | -2.25524 | -53.4818 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4b06409-1879-315c-81c8-f1661f939aba | -2.25468 | -53.48536 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c501af6-c952-3eb2-b778-536651363baf | -2.25131 | -53.48484 | 2024-10-13 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4320d7be-6665-30f2-ade8-e699d4a8ff89 | -3.81042 | -52.40134 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b595983-3f94-35f4-9fbd-f733374340a1 | -3.80687 | -52.40086 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b9d5aff-f9aa-361d-b16c-a98e3851c8f6 | -3.78628 | -52.35008 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5baf5cf7-7d05-3d6b-9f31-ac7148f47507 | -3.77717 | -52.38521 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| adcd06e5-515d-3660-8189-9df2dda34f6f | -3.77655 | -52.38919 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06da9cc4-5040-386f-bbfe-22002c424244 | -3.75699 | -52.30465 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b587ce54-8894-341b-96a0-572655ada347 | -3.74093 | -52.43207 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a143075a-29ac-3381-8c4c-c5e4c5120dab | -3.7374 | -52.43152 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 44263dd4-7f56-3b67-9ed6-9a53c20a85a7 | -3.73321 | -52.31738 | 2024-10-13 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README80.md)
