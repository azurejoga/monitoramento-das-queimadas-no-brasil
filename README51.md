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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c759318a-a6bf-30e0-8716-4503391a081f | -2.58773 | -51.72153 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d6294d0-78e4-3bdc-9a37-099c88997c47 | -3.70744 | -51.79821 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b120497f-44f7-3b23-a2eb-dd32e9ea8ece | -2.17859 | -53.77254 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18e21631-e339-3160-b4dc-f22d7f009f58 | -3.2837 | -53.01538 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c49b771-4e0f-3065-9cad-6867d628e772 | -1.88786 | -53.32162 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 407d7861-1b5b-37b4-828d-37b93029e7de | -0.94874 | -51.7188 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 796bb161-a7e3-3c46-99f0-13922b8681cc | -4.41238 | -49.70942 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 405a81f9-b4d9-3912-a8c3-5992288b9e91 | -1.6005 | -52.58059 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3860bbde-1104-32d3-aee9-c26aaffcd622 | -2.16046 | -53.77776 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ccac81e-7083-3ce9-857d-5847acf27454 | -3.5154 | -53.82674 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6ca423a7-12ac-319a-961f-b9d42ba4e9ac | -1.08319 | -53.64031 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f6ca210-e5c0-35a3-8c53-d5bee45d7fc6 | -1.73554 | -52.73479 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3e2b29b-faef-381c-b20e-5953ec10b336 | -2.20705 | -53.67196 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f38b6424-26f1-3a60-b875-f28d6d8b2bed | -3.62041 | -55.30437 | 2024-11-25 05:20:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7e52a5ab-7460-3b25-917d-fffc8b4d104d | -1.04802 | -51.7411 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb10d50e-3700-360a-babf-36d076d3b795 | -2.17435 | -53.77189 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b65ceaf5-55c8-30e2-b21a-8b187afe881d | -0.35618 | -51.97563 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 963389f1-13d6-3cda-83fb-2e24c680d6db | 1.71115 | -55.81967 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c6135f7-d257-306a-9586-67290517b1c9 | -1.1077 | -53.39304 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c071d59-4c7b-39b0-b021-74e002d09abe | -1.7224 | -53.25295 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a155aa60-a155-3c99-8365-0d11e239396d | -3.94393 | -47.98843 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6c07aac9-f38b-32e6-8856-2f0bf970e332 | -3.62267 | -51.36959 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1437abe-0413-352f-bca8-bf8c2decb82d | -3.62905 | -54.73896 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9b625d3-5a80-3dcd-a874-723fe3670407 | -3.26868 | -52.96065 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfc30ff0-3c26-3fd2-a5cf-d4a4b056261c | -3.49334 | -54.02377 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ca1d34-65be-37f6-a781-f7cf0a503dd2 | -2.92402 | -53.07003 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b28b68f-e22d-3075-b345-ca3a1e2f8178 | -2.17799 | -53.77648 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6222e294-0306-38c9-b93f-bccbc932cb06 | -4.53876 | -47.66359 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 056a151f-d68f-3f9a-9b32-e821e4419d77 | -0.94651 | -51.63472 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58c949f5-be8f-3569-afd5-1918ae11ccee | -0.96822 | -51.7182 | 2024-11-25 05:20:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91656185-8120-3c2d-abb7-e69d990dcb52 | -3.49778 | -50.46212 | 2024-11-25 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c54ff80a-c501-3ca4-848c-a5b137afe3e6 | -3.2543 | -54.22866 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 795be02d-178f-3a83-a023-b5562cf6cb2c | -0.75435 | -51.73925 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a40d039b-9cab-38ba-85dd-2f47b4eb460e | -3.55156 | -53.53271 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8fbb5ec-14da-36e1-8bed-f101651df9e1 | -1.72227 | -52.76056 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce164560-e913-3fdd-92a8-ca46b7b44a01 | -3.13386 | -52.98512 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7870974-4f9d-31fd-8fb5-8600a3779c26 | -3.00262 | -51.54914 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 397404eb-40fc-360a-9fe4-9a80514fe687 | -3.49873 | -53.82051 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aee7f95-7e73-3c35-9cd0-e36155a2cf30 | -3.08361 | -53.26255 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dee1759c-a2a5-3dc7-b604-13afd3f56d6a | -3.71499 | -51.78193 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d88d8358-d573-3d73-8e0f-ed8486d423e0 | 1.36784 | -55.91566 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fabd20d-6f52-3a1a-8ed8-b272593b2e03 | -3.04852 | -51.44633 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e0e1a4d-3078-3ef9-a347-6b2dcdd45495 | -2.82085 | -54.7148 | 2024-11-25 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d68159d1-f857-320c-b10b-0731e8d45232 | -1.63964 | -53.87357 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42efea88-9bf4-3b4e-b89e-499387065a40 | -2.35539 | -53.71613 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ce8a34c-64d2-3852-9651-420e8894a511 | -2.86908 | -55.18055 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8c070f3-23af-3909-8153-0586ba85e6ab | -1.56554 | -52.00827 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14c40e35-f339-353f-b967-71c5c7b15e19 | -1.35721 | -54.65533 | 2024-11-25 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cbbd177-c821-3ad7-9cb8-034506fe6560 | 0.0548 | -51.13943 | 2024-11-25 05:20:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dfd1634-9e9b-3b88-9cc8-398b2ca39541 | -3.94124 | -47.99552 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ed51b3c6-f106-3548-959a-6d44e8910d60 | -4.2641 | -48.69601 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87714b1c-ee01-3f2f-a43d-3527865275e9 | -1.26099 | -51.75747 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4390d719-fde8-3430-8717-3c597d596b9c | -2.95301 | -59.16065 | 2024-11-25 05:20:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a2c1bfc3-14df-3d27-a954-2dd13c785465 | -1.24797 | -51.74779 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e90066f2-3823-35a8-b618-70935aba23d2 | -1.46286 | -52.68326 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31bd02a6-9559-394c-8f1b-724009153652 | -3.65114 | -51.38891 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bccd2f87-5e11-3b76-a72d-ba72fbed44c7 | 1.38302 | -55.89693 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d1912c4-a5f6-36c4-914a-d5a3f21b83b9 | -4.22789 | -53.49434 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 031eeb33-d228-3f66-a68e-2f40e4af7b53 | -3.2531 | -54.23636 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 807ee5d2-ccd4-3968-88a3-d3a5214622f8 | -0.34795 | -51.54764 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5915076-006f-38dc-bd4a-78d854657726 | -2.81957 | -54.10373 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebe292a9-2103-346e-882f-2320e069669b | -1.51794 | -52.62644 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 838a73f6-1c14-325c-8865-588cb1bf3707 | -3.47486 | -51.99542 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e827dbb9-f784-3c73-93a4-3cd21f9004d9 | -3.64603 | -51.38818 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19154ac9-dbc8-316c-af37-be13d65ab89a | -3.87556 | -52.20821 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b34b8f25-064d-3fb2-8d4b-5807c08e56ed | -4.25382 | -48.72341 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 70d7f900-fa71-31c9-86f2-ab177d8cffae | -1.6105 | -52.36041 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 313269c4-80a2-346e-baa1-bc54e705a2ae | -1.15408 | -53.40457 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 439a80a7-4ee5-3212-8554-e06ce09a1a1d | -1.23438 | -51.74042 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3095eab-7855-32f7-84ec-6a6b412faa92 | -2.80632 | -53.01358 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbb440e2-a480-363a-864f-0262b74adf63 | -1.61659 | -52.59722 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51144f2f-f7f9-3d3b-9e93-2343d3b26407 | -3.02692 | -54.05035 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b64a0471-b1b2-394c-8549-ed3b69ebeb92 | -2.82375 | -54.10435 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c3ce46-5124-302f-b3e0-7d7ea2bc1454 | -1.67606 | -53.2 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f08a2862-c34d-384b-bde0-488bbd3c42be | -3.24894 | -54.2357 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61ac56b3-ed2b-3e6c-8f5b-5b254924228e | -1.95812 | -53.32799 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31cb8dc5-c1ee-3661-8acd-1ca086f409db | -2.64785 | -51.76972 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 624e14bd-fb7e-3f81-8765-ccba677b80e1 | -3.94836 | -47.99153 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b537689-6b60-3c6e-a521-f6d9118b826d | -3.24481 | -53.27224 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55bf3662-1d4f-3022-aded-860bf5adaa43 | -1.20395 | -51.74641 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9577ecce-a076-3b29-a145-4f7ed26d1216 | -0.23976 | -51.61393 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83845005-2c15-3428-90b3-3af0ef16cd00 | 1.71534 | -55.82313 | 2024-11-25 05:20:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11d75842-feae-32d9-a0c4-110002e04657 | -1.99015 | -53.29433 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5c6feca-81df-3eb3-a7bf-4f1b40f0abc2 | -2.7965 | -53.00449 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4e9beb9-985a-32b1-b470-37ee00281996 | -2.82016 | -54.09992 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd5bb36a-4383-36dc-979a-be3c9ea06d46 | -1.77115 | -52.72447 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 628bbbe3-6132-322a-8aac-7e016c721556 | -2.86218 | -53.96801 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f00fe2b5-0afb-3e1b-9443-b3c0e1c4b383 | -4.19972 | -50.24053 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4302db24-820a-3dc1-a892-6715e5201795 | -2.17316 | -53.77974 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c48e2a-a371-395f-a5b6-19f47e60a1d9 | -0.35283 | -51.97754 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fbbd2c3-686f-3ae2-af48-3398bfce1667 | -3.27239 | -50.55956 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 510be443-98f6-307a-a957-e6b81ae28491 | -0.33915 | -51.54094 | 2024-11-25 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f48d719-ddc0-3c4c-b7a1-92ce01b9f3be | -2.85496 | -53.9589 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ab64b36-bd27-3219-bd93-53e890143c76 | -1.64382 | -53.87413 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf93d76f-ecf5-367e-b678-f434deb550c3 | -3.05899 | -53.22451 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b0eec2f9-bb7a-316e-b58c-e4d19f282219 | -1.73535 | -52.79478 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5043949-31b6-3f09-966e-1c35dda7de6c | -4.15279 | -54.23848 | 2024-11-25 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26dd2afb-2483-36b3-9948-3354813399f0 | -3.22189 | -53.93287 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e28cab5-7abe-338b-bf6e-59d7d4212911 | -3.71001 | -51.78125 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 837cce04-8a6e-3abd-aa2f-13cca51525a8 | -1.38568 | -52.32737 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README52.md)
