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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec1e7713-4f0d-3af5-96ec-71977e943a2d | -1.19806 | -51.9732 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c400be9-a032-3520-9bfb-8ecc7abd4680 | -3.10605 | -53.99416 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04035504-dabe-3ec1-93a6-e47ae1675dc8 | -4.19534 | -53.49634 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 673c65b6-6741-32a9-8a45-4fafbd8f7597 | -2.57894 | -46.54545 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b8fd310-8615-3101-8126-bcbc0411116a | -4.06256 | -46.41544 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633a6623-fc90-3ff9-92c4-9a84f4926583 | -2.82239 | -54.09113 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5b312c9-aaa6-3e7c-9e07-323d4e83c898 | -2.60818 | -48.22162 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 057fe795-a093-3e6a-9703-e9f4c1ffc1a8 | -2.83955 | -54.01323 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe761487-3d07-36e6-9578-5ca1c7692b67 | -3.21676 | -54.24256 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60965924-0650-31e7-a495-46cbf9e59d91 | -3.32844 | -53.2666 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c3fd673-87f1-3dec-a176-917c74ad04db | -4.70781 | -44.25441 | 2024-11-22 04:36:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 665c4789-7b2e-3ace-a3b1-42bea6e90b28 | -4.01305 | -49.91541 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 793aacda-dbf9-3726-8b03-54395e02117d | -1.49142 | -51.13542 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12b66188-7ed6-32de-8f56-d8ab8372075f | -2.08306 | -46.28771 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f77c1d5-b950-3fb0-821a-694bbd35be60 | -2.7308 | -48.65281 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 053e27ce-5699-34dc-9395-b6f276690877 | -2.49979 | -48.99672 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6119c8a-2b5f-3c10-ad9c-0a408bb47922 | -1.28794 | -52.24176 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410ed1c7-aca2-31e5-a3da-a57152d94082 | -4.07042 | -48.96844 | 2024-11-22 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4ccb426-df2f-3083-84b4-4e2ef9776199 | -3.26387 | -50.66275 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d106d7ac-cba0-3cb8-8ff8-acb46940b187 | -2.65668 | -46.13962 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 105d91ba-534b-3cf2-bf5a-f142e2d43c79 | -3.52927 | -50.75692 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1f2081b-58e4-35ed-827b-fa38ddd8d835 | -4.08974 | -54.0473 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28a53f4b-7af7-3adb-9a2d-184687ba92c1 | -2.16721 | -50.12861 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e05744-6a5d-32f2-9241-cc9c3674c3f8 | -1.13164 | -54.17544 | 2024-11-22 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32c787d6-9bb6-37a0-81a4-07d751a8214c | -4.56002 | -48.53369 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d89527c4-5ef2-37cc-a13a-9ba21337043b | -2.6044 | -48.24569 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 616cdf9c-fe64-355e-8860-6ac5cf017f1d | -2.72702 | -46.08632 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb7b813d-0bf9-3ffc-a21e-3efd04c86f01 | -3.61105 | -51.31458 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd211e38-106e-36ed-af9e-5c8c805781eb | -4.40969 | -45.84898 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 919dcc9e-f8ec-306a-acf4-e3b94d98eb71 | -1.64222 | -47.3618 | 2024-11-22 04:36:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d00cd6c-e651-3274-9cbe-44fb9c18d5e3 | -1.83724 | -52.17902 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44dc5e3e-6634-3285-a118-65ff1e7ce023 | -1.80166 | -48.46861 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 646e1b9c-9d93-3086-a9f6-771a2e2d1681 | -1.07312 | -53.36481 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b88cb252-7d62-33cd-8c6d-7290da5a0800 | -5.23999 | -42.64173 | 2024-11-22 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94e9bbf2-7050-3cc1-bea9-688e0766dc96 | -2.40822 | -48.60902 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fe186c4-b52f-3758-b9df-2aecea89a12a | -2.15419 | -50.49621 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90177422-7650-3375-b255-996db113a19f | -3.6629 | -51.57788 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37939741-faf3-33ce-9c06-902afe88e976 | -3.27314 | -50.62574 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8ce5f82-b4d8-3d51-8877-dee5c092f754 | -4.06723 | -46.84399 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3bf21737-3c1c-3077-aa5e-4ac5b40aa86b | -2.14682 | -50.6995 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcfd7a99-8ce2-323e-a49e-56926ba9f6e2 | -3.29378 | -54.72733 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cc88d02a-f690-310e-817f-a9372956685a | -3.52927 | -51.10435 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abc31ba9-8676-3e0e-a864-1900f8e7f38d | -2.66411 | -46.1604 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e44004-203b-32c7-ace7-4e3a062c922b | -2.35947 | -53.68595 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64c33bed-f64a-3209-8cf3-e3d2ecac909e | -1.26728 | -51.62643 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ed3ae3-5b85-3b86-ad1a-3be02d3c2236 | -2.26624 | -50.45228 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad3be33b-6a2b-338a-a734-1cfb0ee92985 | -2.66625 | -47.0 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5707cc1-d0dc-307d-87aa-e82f896fee28 | -0.881 | -51.72583 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3571d826-52cc-3319-8c56-fbaee5f98123 | -3.12677 | -45.91177 | 2024-11-22 04:36:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fd601b8-2ef4-34f0-aad2-1ff953118d05 | -3.22253 | -53.84128 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b2fbcb7-7c44-322c-96d5-4c72414c7f56 | -2.66791 | -46.23865 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf760d2e-c139-355e-af88-d0d233aec02a | -3.66277 | -51.57714 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b677eb3b-1758-37ba-b0c3-12886e262d80 | -2.18686 | -46.56533 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6991adf4-be57-302a-8d39-1963f946f183 | -1.12758 | -51.68175 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2980a1e8-ac12-3890-9d66-4612627b1ff2 | -1.04234 | -51.81498 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 706877b3-8832-363e-a91b-f54fd176b970 | -3.57906 | -54.68395 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0703be67-57ef-3c71-b40d-39ea382fdacf | -2.57727 | -48.20272 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 132cad99-e70f-3a8d-be1c-3217918d11d9 | -2.64443 | -46.57399 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58e68128-0a6c-307e-86e5-2c11520e5c5b | -3.67455 | -52.37683 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8024018a-00d4-35f7-b2ed-5ef792f3e1fb | -2.90851 | -48.32197 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376105b1-b4d7-37c8-b45b-b9017cdb3433 | -1.22257 | -51.74358 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52e1a171-249e-3abe-9587-ca912e01abff | -2.45872 | -49.14954 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e968c5a-bac1-3a2f-a64b-b736dd522f48 | -2.70031 | -51.86789 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1abd003f-8b04-3b11-ba9d-2c02c85710b2 | -2.65874 | -46.54959 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f53e52b7-d8a1-3e43-b237-7aab1f868e4d | -3.28701 | -53.855 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5a043975-d41b-3ca6-a60f-55ed45511af9 | -1.87602 | -48.94468 | 2024-11-22 04:36:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 893485b7-e991-3ddc-ab4f-02ef5f9f14ec | -0.26276 | -51.56408 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 897819a5-3bcc-3272-a847-92f4a7de0d74 | -1.58828 | -53.81374 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4177651f-b52a-32d1-aec0-e6553c2278b9 | -1.78121 | -53.60225 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 602fa622-c1d6-3294-92df-0103ea537329 | -2.19492 | -50.30524 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e628f71-16c9-376b-8543-cb1886aa38ad | -3.28644 | -53.85859 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3fea4fb6-8836-3e1a-a106-9d236a2b351d | -0.30726 | -51.54449 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1236d8de-f643-3a11-85ba-b7dc8692eed4 | -3.2251 | -54.24396 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5b22108d-2d82-33e1-9aa2-9133632ae0e0 | -1.38764 | -52.34538 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8fbb995e-3940-3281-9837-72c14736b0f0 | -2.68142 | -49.20247 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4576274b-7c07-35ae-8fa3-1a7902a2e8a6 | -1.88013 | -47.88266 | 2024-11-22 04:36:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d240f2e3-d519-302a-a0a2-af216f9def52 | -3.65163 | -42.2606 | 2024-11-22 04:36:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| abb9ab1a-0455-33c8-a3dc-0a2ece8d721a | -1.11273 | -53.40292 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b9cf403-bb01-32d8-8ce0-44a693a3b458 | -1.61553 | -52.47253 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dbd34d0-be71-38d3-a1c9-ce3b68d953c0 | -2.03082 | -51.18281 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01eae737-3bd3-3d37-a740-4dfcfec01089 | -2.45717 | -53.70124 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc90d84f-5785-3886-9a92-54beb75111fd | -1.6406 | -52.61208 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 574c4c2a-084b-3158-8efe-f58dfd5a9d45 | -3.28351 | -53.85077 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50417e51-3474-309c-b04a-839955b8c6c4 | -1.20883 | -51.75914 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3882de83-3ffc-3993-9033-3ff52fc225e9 | -3.83432 | -51.70626 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e9428b4-a82f-3470-ad5f-d32a090ec43e | -2.31887 | -54.75747 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87a718fe-4043-3d7f-a0c7-30c2a91dc19b | -6.38103 | -47.1461 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf71f991-4247-3cac-89f7-a23719970ba3 | -4.68839 | -40.69328 | 2024-11-22 04:36:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 209047a6-b5f3-3443-936b-5ae33044c0ac | -0.93882 | -47.55851 | 2024-11-22 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 66f15511-8c3d-363b-bec9-237ae5df6a09 | -3.20177 | -54.25591 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d3e275c-9d9a-3f95-a9b2-5ebcbb0c25ac | -2.65932 | -46.54588 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ebf0b8b-2e2e-3b7f-ba88-1633ce3af782 | -4.99964 | -50.50701 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc58718a-d62f-39e9-9188-a6f0837328dc | -3.28345 | -53.82511 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b849ab1-2c67-3303-a00d-32d2ee5a261e | -2.87622 | -54.87844 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d46fb6a-cacb-35fc-85cc-d1568a7b51a7 | -2.43104 | -46.52665 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47564c49-cf2d-3755-b79b-8bdb5c1f575b | -2.58464 | -46.55391 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 335c62e3-3d8f-3030-8014-68eb78c4a10a | -1.12145 | -53.40065 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 02d087d5-5291-38bc-9794-baae44225884 | -3.93784 | -47.02098 | 2024-11-22 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de6450ef-6410-3fd2-9509-62023daa023c | -5.95898 | -48.0593 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5d32a6d-21c0-39b8-b064-78d9a94c397a | -3.20719 | -54.24881 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README39.md)
