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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d19b61c-2273-3b16-a81c-1a5978386ccf | -4.95641 | -45.62273 | 2024-11-22 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6e6872c-a070-371b-b11a-9c8cbaa7d1c5 | -4.52104 | -46.46634 | 2024-11-22 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee71116d-6b99-35f8-9ab4-5526ba716081 | -5.95674 | -48.05166 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4c07496-f826-3c3f-a5c8-7b4a6aa87a1f | -3.64164 | -54.32109 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d3ac15e5-5470-3c36-97ce-d692ae204f3e | -4.48211 | -48.12056 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0d932e8-6748-366a-a612-e072d62288b4 | -3.10986 | -54.28836 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5ada360-f6d0-3fa2-b5f0-e158888be10b | -3.51703 | -53.79735 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64aa076e-42c8-3560-9ffe-52e4ce9039d7 | -3.85363 | -46.66229 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a019d496-5d75-3a31-834d-ac08913f0df8 | -2.15324 | -50.45787 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc07a925-aaab-3baf-a5b5-e165db69e474 | -1.82832 | -50.99922 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b40dd61-ec6e-3791-875a-ac4fc837a130 | -4.70335 | -45.81388 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afafbe21-2c4f-3816-9017-9862994d1b8c | -2.0059 | -54.52032 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 76be5b4e-4566-3908-bc6d-479d83ad9d4e | -4.66474 | -46.53926 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50d17482-94c2-3630-8104-6deee7300aa5 | -1.2119 | -51.96928 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b381e18-f372-30c6-96b5-3bcfff403f0c | -2.75367 | -48.57197 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0fd9cb5c-36b4-3469-9602-0163531e68b7 | -2.10083 | -50.58768 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a42efae-77b1-3d92-8f70-418f2eed2a50 | -3.88121 | -46.66658 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd628170-2f56-3b8c-b8d3-5b0cd8520c1e | -2.97519 | -51.43805 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61dcd8e7-a8fc-3dcd-a7ce-38a1fc5cfbce | -1.24724 | -51.75059 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51f50f4d-bdbd-3f04-a02a-9cfdfa3cf9fc | -3.23407 | -54.24138 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 1433fc12-037c-389a-b537-e3c78bc4e301 | -3.56988 | -54.68648 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a96732e8-2571-3803-b163-9a920bee2a18 | -1.12756 | -48.3449 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49e6a75f-586e-3078-af1c-ab5321635d09 | -3.46973 | -45.91492 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87bc2fe0-6f03-32b0-ac04-f9ce8670ea8f | -1.70246 | -46.7018 | 2024-11-22 04:36:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 227292a1-d5d3-3c51-92de-096dcd8da5e8 | -3.22874 | -54.25621 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 1df63e15-24b3-3975-bf5e-560d87318bb7 | -2.95357 | -51.41423 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd860090-749d-3b94-ade2-f442c957f883 | -3.64897 | -51.14622 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f7e2308-fdfa-3777-a3d5-475bff663f31 | -2.83446 | -46.68162 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3284836c-d846-38ee-bcb0-f5d6b294996f | -1.11853 | -53.39284 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2aacd519-f9e9-3573-a9dc-16c077a6582a | -5.57687 | -46.13797 | 2024-11-22 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e49b0e5-2a61-3a98-a135-3707be7169c3 | -3.23101 | -54.26065 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 1d54d227-92d2-3240-bba3-171a2ff219ae | -2.12034 | -47.67165 | 2024-11-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbe2b526-6751-340c-bb5d-7873b6a76208 | -5.96174 | -48.05628 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56d157e6-744e-370c-963d-a232fca9ff6f | -2.64843 | -46.5708 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f80f5e2d-9394-3fd3-ac92-977b84c5a722 | -1.14787 | -53.65924 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97833bb2-3d9a-3b83-9a81-55363b89e1ac | -3.10484 | -54.00163 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e728f56-3691-300f-a809-fa98d036ffbe | -3.18645 | -49.05882 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dad9192-239e-3f72-b5d1-28f159bb202b | -3.32418 | -54.08995 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4fd74caa-3d08-360b-8a4c-f08383af827d | -4.00915 | -49.91839 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2142144b-1b77-3104-888a-9076c94bcb14 | -1.63675 | -52.61147 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 38befc86-6135-3076-8362-e42e38b9c1f1 | -2.70211 | -46.2243 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd7d9944-3427-3bf0-b336-44902358f731 | -3.76015 | -46.12039 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 981ecf3b-77ec-3db9-adeb-4ce9b997a7d8 | -1.18693 | -53.72094 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cb78ce9-4405-39c4-8374-0bebe5a2e3c3 | -0.77315 | -51.76919 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 156c4af0-0007-35e2-aec6-53f709a88f8b | -3.09667 | -54.29015 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28ace121-95c7-36fb-be0f-fa1d551ca3f5 | -1.47524 | -51.10008 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 396dd2b8-0137-35d5-8964-964b8717b923 | -2.70086 | -46.25536 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02b8677c-a47b-335b-a7d8-edf4a7752d0f | -2.45778 | -48.81024 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a947d9fa-772e-3afb-98b0-243997fd20f2 | -2.81 | -54.0237 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad1de71-ef85-32a2-8172-bea8eb432b9d | -3.29107 | -53.85565 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 678f98b7-b654-39d9-b44d-8f56a8887172 | -2.34609 | -50.37 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15c13386-d085-3c0c-90bb-66db0770d159 | -2.04744 | -49.7315 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ce618ff-668a-30c1-9ccf-34676044f82d | -2.63016 | -46.21799 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06d620ec-6d1e-34c4-b26a-737834c5d384 | -2.25795 | -48.69827 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 992021a9-43ac-39b4-bdd4-58f96243e052 | -3.29463 | -53.86014 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98318e59-4a67-305d-8e52-6802b34dadcd | -2.57377 | -46.55606 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 006a9863-7ca1-3431-89c1-9142097baabf | -2.02728 | -51.18225 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3c0a8b6-2774-32e6-aef8-7291b191b90f | -1.44417 | -53.39054 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2bbffea-4df9-3633-9f24-385859b15889 | -2.65162 | -48.78812 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b05b3b07-c186-361c-8a9d-e9575c88f3e8 | -3.23763 | -54.24593 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 69717134-81fc-36ad-a18d-3c1d8a2fa424 | -3.18401 | -46.50525 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb4a26e-8728-3732-9770-95b8e73766be | -4.20819 | -50.6987 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bfc064e-a433-34f9-8fb8-37ead79dcb61 | -3.20637 | -46.54333 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71a38f24-c499-3aa2-b184-ddaa941dc0c2 | -2.58063 | -46.5571 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b26a779a-6c3d-3600-a9c1-7f27cce70ee3 | -2.21252 | -48.20909 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46fafd4a-81b6-3b80-86fd-2acbc553032d | -2.82054 | -51.79559 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e1030c2-26e9-3482-9499-6dc55c039bf4 | -1.82705 | -46.28745 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65bb4f0d-f27d-3751-a77f-9ae8b5c3391e | -3.97146 | -43.72107 | 2024-11-22 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 795b363e-5458-34ba-8c51-c7a125f7ee8e | -2.80232 | -54.01862 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08a39fb3-e9ac-3aae-ad91-c963a33bc459 | -2.7545 | -46.07074 | 2024-11-22 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a0c1f2-1812-312f-9626-192dbd938698 | -5.96119 | -48.05984 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b230ec83-6b65-3822-a9fd-22413d2257f0 | -1.20496 | -53.68799 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 24cc9583-66d2-3674-bfc3-e1a629fb3f1c | -1.11446 | -53.3922 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d91ae04f-4ca5-3790-a26c-352713c45b84 | -4.10582 | -46.91013 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cb0bbe6-1344-3ef1-8093-6b8cc6f1e457 | -3.27653 | -53.84233 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e208ff7-2fcf-30c0-acde-0f748410af19 | -4.44326 | -48.45589 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 317134f3-2f53-3068-bfe1-e1365078bb55 | -2.53423 | -46.22705 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 920083fb-cd07-36f2-98cf-aec23863d29c | -3.80378 | -51.99125 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5153de52-5342-3a7d-a511-29ba66e44a4f | -1.48303 | -47.23002 | 2024-11-22 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64f8670f-3b8e-395b-8120-5b01eaeced6e | -2.39621 | -46.79593 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c733544-3a64-32f9-8081-8484867eb428 | -3.50871 | -51.01984 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4b6946f-b5ce-33d5-97d1-35b6647e4b27 | -1.12494 | -53.4049 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78666e22-7577-35da-b66a-128fb0eeb2b9 | -2.28279 | -47.91315 | 2024-11-22 04:36:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 800d91d6-1c5c-39ea-8219-1ce25aca40e8 | -1.75775 | -52.66899 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51738b98-e5f9-34de-8796-cecc98cf0470 | -4.57848 | -48.0238 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7e3443a-cf9b-31c3-8077-43de359dbeec | -3.95859 | -51.13904 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8b338d6-4923-329b-bf8c-d9d41a8ae854 | -5.51097 | -45.48738 | 2024-11-22 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| addda804-0e3c-3773-a52e-b61461752752 | -2.17897 | -52.12761 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c10a5d5a-c33f-3369-b417-c9fd3dba3b58 | -1.19767 | -54.0341 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75e79dd2-2259-3c9a-8fe9-7234a2a25b10 | -3.20304 | -54.24802 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 18dc853d-a978-3bb4-895a-d8a39b7a0b84 | -3.14515 | -53.13241 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba5b86a6-d73c-34d0-be15-ce37079d5d0a | -1.33227 | -51.85741 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edffc815-b3ae-3674-b536-673ae9e1e244 | -3.23773 | -54.25374 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a742eee3-27e9-30c5-93b8-0779424adb8c | -1.49719 | -49.68599 | 2024-11-22 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b499cf9e-d1c9-3193-8629-715c323b8790 | -3.59207 | -43.64298 | 2024-11-22 04:36:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99b93b87-9676-3750-91f7-f0f6019897c1 | -2.00476 | -54.51849 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fcecc4e2-109d-32a0-86a1-818a63fb9d93 | -2.44586 | -46.54411 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbf33a5c-a3cf-3684-b79e-26eaa3661006 | -1.85424 | -52.06109 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12dd990b-7dd3-3c95-b240-c535f46aec7b | -3.58855 | -43.63887 | 2024-11-22 04:36:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6254ae0-de09-399d-ab54-13f47fdb7806 | -2.08365 | -46.28395 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
