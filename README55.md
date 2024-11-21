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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7e5e335-b628-350f-b5dd-3167be20e572 | -1.4782 | -51.13471 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5950a6b-37e3-325b-96e1-e72a19e2cfb0 | -2.18191 | -50.57763 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db180940-d082-364a-8d10-4aa10a5badc6 | -1.29288 | -52.22346 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a48014f8-99e3-3afb-9c59-3bc1715f7473 | -3.12168 | -45.44736 | 2024-11-21 04:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e38a8713-0c9c-3eaa-953a-34e1954c45f6 | -1.33395 | -51.40451 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b49c52d-c0a1-3de7-868b-1012417af503 | -1.40719 | -54.26226 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9105465-aec8-325e-a092-2b3ae52d65f4 | -1.39226 | -52.43437 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2d6b02b-987b-350b-9e9f-130711cb5014 | -1.70044 | -50.20756 | 2024-11-21 04:53:00 | NOAA-20 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32c98290-ad2a-3f39-b2c3-868c1fa02711 | -1.68045 | -50.71056 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdd07b57-000b-3425-a9c3-8bc5cdc46ba8 | 0.90488 | -50.24108 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb9bac1c-5ff9-3303-8854-f826a02399c5 | -1.46269 | -55.45216 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8db7ca0-afe4-379c-a67c-19b70052cad6 | -1.42621 | -54.29409 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2eb948a-458e-3d09-8345-5283e6d4a075 | -0.97805 | -51.71609 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0b62654-9dc6-3623-aeb6-70dcb0baef0e | -2.24737 | -46.8243 | 2024-11-21 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bbac4dc-9e94-3ca2-be45-0658da4746a6 | -0.85485 | -52.59057 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df3fa53e-95a6-3f03-9fab-7d30db6949ff | -0.92039 | -51.65259 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9af24d2-80b1-33ba-8978-44af4a6bb5e1 | -2.09076 | -46.32162 | 2024-11-21 04:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71c40c75-9e60-3830-bf35-a258c7d32223 | -0.92877 | -51.64299 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d06ce7b-e410-37cc-8708-37f80cab2a62 | -0.86495 | -51.85344 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e054cc6d-dd04-3a9f-9d29-5785a1355bb7 | -1.01649 | -48.07323 | 2024-11-21 04:53:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a95d3792-359e-3daa-bee6-b50834a44ac2 | -2.20208 | -53.65966 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 121f5b63-9529-39dd-adfa-473231787cf3 | -1.62284 | -52.48051 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3072ac4f-957b-3d6c-990b-71851f6fd452 | -1.68331 | -55.02686 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20e23140-5268-3e3a-bc6a-636c3630e294 | -1.45805 | -51.99561 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2d6c167-c153-31f5-89da-431f5b1bdd3f | -0.93384 | -51.71989 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fe00e9a-92bf-3568-ac56-f3e4de1f8a89 | 0.03217 | -51.22551 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d92091-76e9-300b-b7e9-3bb257646adc | -1.61278 | -52.60973 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2297b295-fa35-371d-bedb-5016512dbc25 | -0.91716 | -51.78233 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad4ac477-85ad-3f55-8713-48db441ff801 | -1.33888 | -52.92631 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 214c13a8-d0ee-3aa5-a633-8db1aeff4173 | -1.14045 | -51.67941 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bba18eef-3bb5-3048-995c-ec145fa92bfe | -2.57574 | -49.09108 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e57f5bdb-a2aa-3a42-90d6-5bad10a4a347 | -2.25007 | -53.67771 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afdd8be5-a4f0-39e8-84ed-abd024cb5aef | -2.35677 | -49.00443 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50419ee-bcfd-337c-b245-d564f40e7326 | -2.26302 | -50.80064 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e4d60d8-0151-3203-9045-e79d3683ffd0 | -1.49566 | -51.99059 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4acda20-5a73-32a7-8018-e21da1cdb163 | -1.76768 | -52.70467 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9dbf9e4-a58f-37bf-8487-e6a7365c6fda | -0.92933 | -51.63945 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52a276d6-6428-3992-8a17-991263b13962 | -1.65009 | -55.25853 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 463d603d-6a6a-36e9-8ab6-e54547f95d0b | -1.74642 | -52.06128 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e22e36ae-18fe-3ebd-b680-ef5e14e63ada | -2.38692 | -48.92339 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bcf7def0-85a3-369d-9f26-1f3aa9687fd3 | -1.68614 | -55.03108 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0552043-7198-39a8-8a0c-ddbe4df9d15b | -1.18677 | -53.71982 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| da15cb69-8744-3fa8-896b-dbca841f0eee | -1.44617 | -54.509 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b239299e-46ee-3525-9e75-f20d4fa77f3c | -2.94187 | -48.33037 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96a9ca55-bfeb-3c8c-9f3d-a988b87a6118 | -1.62217 | -52.61471 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 673d177f-cda8-34a9-8f8a-ac118f296d1a | -1.19607 | -53.68204 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bbdc9331-b25f-3d75-9227-f2ed701f91b8 | -1.4742 | -52.51777 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd421618-530a-3881-8d4c-50c9fb85c79c | -2.24361 | -46.81929 | 2024-11-21 04:53:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1469593d-e277-3a1d-bcdf-fd337d9726a5 | -2.3617 | -49.07276 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 656e407c-3a03-3828-87d9-d91f7bcfaa8b | 0.18264 | -51.21697 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13854c6d-12ee-3bb3-b6e1-a91c57c2338e | -2.93898 | -48.07177 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 125a968a-6418-3c25-9dd9-17125d1e722c | -2.24426 | -49.20238 | 2024-11-21 04:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05fd8b9c-650b-3214-97c9-b6650d038725 | 1.36162 | -56.02739 | 2024-11-21 04:53:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8b375fc-59a7-3311-a9b1-93aca73ce915 | -1.19009 | -53.72034 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c2c98cf4-3dc8-395b-bce9-e7d3326ab99d | -2.26853 | -48.99096 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eca87685-534c-3495-87ad-425b606ca003 | -1.61219 | -55.40777 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66913331-4103-3dc0-b920-57ac5d128297 | -1.1189 | -53.39418 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5fdb5c0-31a6-3232-b965-f4ab41d5a3eb | -1.63757 | -52.60298 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 439ee521-ef88-311c-b645-4c78ec1b0c12 | -1.7353 | -52.39193 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 246c73fd-30b3-32fe-a976-f116e5da3616 | -0.88197 | -51.72272 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7c6ff27-8e59-3c03-80f2-a3e75c35ad9c | -2.02807 | -51.18335 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ca6c9ae-283c-3853-8f94-02dafc8d02a6 | -1.31759 | -55.45763 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a6e4f1e-732e-3a1d-b6f7-b0171aa0750b | -2.83704 | -46.68125 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c27a16-07be-329a-ba08-2c27436390fc | -1.44642 | -53.3862 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b165f33-7594-3590-8676-e6bd2931f1b2 | -2.92951 | -49.1249 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 738fbbb4-3369-39a5-961e-139374a71c18 | -2.61433 | -50.54301 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dbb3e94-8fb1-3381-81d2-a2cd04c62510 | 0.4553 | -50.78971 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2b9c4d7-052c-3f12-9e41-845fe145ca73 | -1.42459 | -46.01434 | 2024-11-21 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c677b30-d24a-39f3-ab10-fa865ab94bdd | -1.23563 | -51.78803 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ffc0bf5-963c-3693-875f-a65cd23db240 | -2.93273 | -48.33617 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a290e850-3938-3c72-beb2-fb207d15040a | -0.96007 | -51.72756 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bec3d3a-9545-3230-839e-bf7dec978587 | 0.45189 | -50.79024 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d581d60c-b9b2-348a-b53c-5d8024445571 | -2.02258 | -47.00026 | 2024-11-21 04:53:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 912f3ae5-81ec-3102-9ff2-e040d80a5003 | -1.42644 | -52.41133 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 424e0b9c-e3fa-37b4-b01d-c12fad2bee4d | -0.94666 | -51.63849 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b72d347-3eea-341e-afab-261c97409e81 | 0.13968 | -51.09851 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cdf858c-1bca-3d4a-8cf5-1e240da85086 | -2.38491 | -48.92578 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73b6f0eb-3d35-3d96-a0be-3233921b6f75 | -0.97983 | -51.77061 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44a83126-f5ca-304a-b24d-680102d240e1 | -2.62761 | -47.96614 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43c0c128-4b19-36a1-8923-4465ddc490e0 | -2.11536 | -50.16667 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78c5e5cc-51c2-3844-976f-12cec121dfa0 | -1.98473 | -53.13998 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1166c9cc-e389-37a7-bdab-d5c58b2f2a90 | -2.01843 | -52.0137 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26230092-b160-300f-85cc-72981a2dd9a6 | -0.96036 | -51.78564 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa1d560b-33a0-334e-8129-b46526f86703 | -2.20427 | -50.73274 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66f98760-6e93-3860-a1a2-2531751103ca | -0.42163 | -51.56509 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0fe4a57f-3953-30f5-b311-3e6af62f9ee2 | -1.1371 | -51.67889 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7036b031-8a7d-3de5-a135-335cfaf0ae99 | -1.79326 | -48.45133 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01f593f1-0a95-3082-bd5a-9e7251ec16e9 | -2.84883 | -46.67679 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18632b4d-b6c1-3266-8a64-acca82066371 | -1.14131 | -53.40512 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab64534-bd89-31ed-810f-69d32126dcd6 | -1.67986 | -50.71439 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f2ace79-c042-3b1b-b944-6f3fecc95bb0 | -2.19931 | -53.6557 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 80208d50-f3cf-3ce4-b330-4c492392adff | -2.20956 | -49.87012 | 2024-11-21 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a546d609-9408-31ee-bf4f-ce442f97909d | -1.61676 | -52.47602 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e9c9cd-3e7d-3ac1-9c26-d378e6c21413 | -1.38414 | -51.55577 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846ad235-38d7-3868-869f-ef642d736709 | -1.75987 | -52.6682 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede1a9cf-2a44-310c-ba7d-94ea090bdf4a | -2.38938 | -50.3345 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a43c8fd5-abd0-3764-bfe5-75b2a5bc793e | -2.20725 | -53.75582 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9667fc48-3874-30db-8847-5d982d3de38e | -1.14549 | -51.69109 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d9c1224f-1909-39cc-a6d8-e2227be18a48 | -1.25272 | -53.36616 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e81b76b-df0f-31fd-8eba-2ae8517a9566 | -2.53389 | -45.44192 | 2024-11-21 04:53:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README56.md)
