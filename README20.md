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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb621fc-e5b0-3b93-b058-b48916b0526d | -2.78385 | -51.75097 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2245e2da-ea4c-3330-8e36-62ae040acd96 | -2.7294 | -54.13767 | 2024-11-12 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d18214ac-8ae5-31e5-91ff-e26e0a3e6100 | -2.03663 | -56.65616 | 2024-11-12 05:18:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ab9c872-75cf-32e5-8914-5ab0f9891cf6 | -4.25064 | -50.25286 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46079b75-2bf3-3a28-bed3-2bb470cc096a | -3.89617 | -55.73384 | 2024-11-12 05:18:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58669344-cd4c-3334-b40e-7917776d0892 | -3.92589 | -49.92201 | 2024-11-12 05:18:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1eba4a5-b938-3973-a6b1-581810880834 | -3.08175 | -49.19895 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8a09310-0134-3048-b8cd-064f02fec26b | -3.08125 | -49.20234 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f305846f-057f-3e34-a200-7ca466030471 | -4.4222 | -49.72194 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 701684a3-6d6f-3864-8777-56ece0230252 | -3.09945 | -54.30334 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 22486cfc-3644-3639-8bd4-39a785d0bf34 | -2.59665 | -54.24772 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d8d4043-f559-3978-a3ba-65317499560e | -3.0985 | -54.28698 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 406970ca-0882-37da-8457-18b682c96858 | -2.62889 | -54.29033 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 877b5aa4-9452-3fea-8e39-ee35ddecabfa | -2.60015 | -51.71777 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6192d42e-b2d7-3026-9de1-ba826fd81e91 | -3.06914 | -54.57604 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dbd9d81-d5f9-3d3a-b5d6-6ac92974e4b0 | -3.07004 | -49.20404 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51120255-9381-31dc-8b16-ae745b55997b | -3.70179 | -54.3963 | 2024-11-12 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c819ad8b-2063-39bb-acdb-0adaa7fbd6b3 | -2.71508 | -57.34698 | 2024-11-12 05:18:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1728032-d247-30e8-901b-436c62b0f8e2 | -3.06168 | -54.57485 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56fc3a3c-0476-3e0e-b90e-b28cdb021db2 | -3.9536 | -48.12685 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 519ad8a7-b9cb-3eb2-a782-8c00d02c8791 | -3.68038 | -49.95159 | 2024-11-12 05:18:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef113a3d-9a2e-3e67-925a-917d2bf6be15 | -2.73322 | -54.13826 | 2024-11-12 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad321c6f-7250-37e3-a6e6-44b1c1f2a5c7 | -3.07539 | -49.2049 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8762bbe-7353-3a2a-a32e-3b951c3abddc | -3.28722 | -50.05508 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef9d3d1d-0401-3049-951c-8250af21c130 | -2.9877 | -49.54309 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 53c7165d-1ccd-3ff6-aa95-80f975d6363b | -3.09944 | -54.30608 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 44a1239e-c31e-3784-be87-f029901ea89c | -4.42168 | -49.72127 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 61c82c1c-9a67-3ede-8e9b-5c405ea13d0b | -3.34648 | -54.18858 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 424ceebb-df2a-3920-9932-101892cc6608 | -2.62651 | -54.28057 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 32cc1e7e-ad3a-3e50-a4b2-35fc797e09bb | -4.01964 | -49.00428 | 2024-11-12 05:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69c4ded0-33f4-32d7-a488-85ee34bc87f3 | -3.34525 | -54.18633 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e02198bc-3268-3e22-9a46-e42524a77b75 | -3.07439 | -49.21163 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbf74c35-cbfc-36a1-a18a-72907d04542e | -3.9535 | -48.16915 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a5a15fa-56b9-360a-88e9-d14d7a16b62a | -2.7195 | -57.3405 | 2024-11-12 05:18:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b38f7029-63c3-3a1b-b4a7-eee450143b4e | -3.52268 | -49.95431 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c8d0851-b8d2-3172-a356-354903583194 | -3.10611 | -54.28814 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9bf2a0f-44e8-333f-9675-473a71905718 | -3.05157 | -50.33327 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f5072cc-949f-3cc2-a057-43ed0679d6b7 | -4.17239 | -55.65768 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af71c1a8-8d2d-3297-82a4-021d5a03b0ec | -4.09242 | -47.71093 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69e2ec06-918b-3543-948a-ef9d253bc67a | -3.53133 | -54.08966 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7c507c2-b813-3938-86c3-ca3e548b357b | -4.05797 | -55.78967 | 2024-11-12 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89a8228a-5402-3130-b545-07867d464ba7 | -3.10015 | -54.30147 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 1e8832a1-d0a9-34da-a9d0-c99769ee26dc | -2.85055 | -54.1577 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f232f9ab-23c6-3726-958c-668ef4f10486 | -3.38838 | -50.13238 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab0de2a6-6712-37a0-989f-75bc5d77e802 | -2.7287 | -54.14237 | 2024-11-12 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53ddfc05-2f20-3032-bc74-c3f9bd71942b | -3.78785 | -50.09472 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4f716f5f-4277-3e50-adf9-98144d046ecd | -3.10159 | -54.29221 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ba31139-a8fe-39f8-8742-f8373f6a4408 | -3.9517 | -48.18179 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f543eda-4d4d-3108-9ded-acfffe3bb436 | -3.84676 | -50.21621 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87f7228f-e177-3911-9116-cbdf98a28f2f | -3.10231 | -54.28756 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e93096ef-5251-31ec-8b9f-2898421624ea | -3.43938 | -50.30661 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b5afaeb-e3f1-3008-a1b0-9cd8ca196549 | -3.10393 | -54.29928 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b9384bdc-ea22-34af-835d-26cb1083e7ab | -3.74316 | -50.18821 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2981e845-7383-3c5e-aa70-ad24830327ff | -3.10082 | -54.29406 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4bf93a8-ebf3-355a-a291-9594ae6a848e | -3.34573 | -54.19341 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28abb673-4e2a-3e40-8569-03ea46ab577d | -3.43854 | -50.31229 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5ee5c08f-89ee-3785-a0b8-4ada2b84d448 | -3.34231 | -54.64389 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b75f00a7-d11d-37e7-96fd-727afaa6c303 | -3.84633 | -50.2192 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4333760e-37df-3305-bbd0-5249e2a060a9 | -2.78832 | -51.75167 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 90bbbc4b-d520-3f29-b762-f5a3972eb480 | -3.06954 | -49.20742 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cbcccee-3bd3-36a7-b983-f0eb6e2e76e5 | -3.38882 | -50.12942 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 873c7bf8-8f19-3ecd-8474-cdf1cbb903a8 | -3.10539 | -54.29279 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3fd5095-c363-33fa-862f-233134532542 | -3.08024 | -49.2091 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00891794-ab24-3a9d-9023-85977d66a394 | -3.07589 | -49.20151 | 2024-11-12 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60ed49f7-eb01-3016-be70-7da081c7889a | -3.95228 | -48.17769 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10a9b168-bf8b-34c1-91c6-daf1de669fd2 | -3.09876 | -54.30795 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 74d43e05-32a9-34b5-af4a-a603527b8c98 | -3.99739 | -49.27769 | 2024-11-12 05:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2e751d1-0d92-38cf-8dde-259ba89935ee | -4.11612 | -50.23447 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40f106ab-b9eb-3b49-9ac4-8fde245f0d55 | -3.57311 | -53.78704 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c7ac064-9f41-3d28-9cc1-de911fa8e9eb | -4.42269 | -49.71866 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e179db97-9edf-3ec2-990a-e7e746319a75 | -3.09635 | -54.30091 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18157a80-e379-3b64-ac2b-165ff60dc20f | -4.33932 | -55.4455 | 2024-11-12 05:18:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd197ba5-112c-3a3b-9f0b-bc26bc3cfe0e | -3.94474 | -48.14731 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa76e640-65ca-36a9-b0d7-2ea0622f8183 | -4.25022 | -50.25581 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f71890c1-dfeb-37f8-a3c3-6d976e6e1ffb | -2.62581 | -54.28515 | 2024-11-12 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67dcf96c-111c-3112-bcd1-2ba44d807098 | -3.65891 | -54.65355 | 2024-11-12 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 480c897a-a78c-37fb-9d69-5015eb2f08ba | -3.43481 | -50.30295 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7e6fe15-35df-3e59-8bd2-bb3df5ddef19 | -3.34333 | -53.21004 | 2024-11-12 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b39efc63-4347-309b-9bae-dff4c78be870 | -3.10013 | -54.29871 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6eff649d-d851-370a-9439-36822198ccde | -3.95419 | -48.12276 | 2024-11-12 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dfc6737-73d7-3083-97d4-07a0c3954fc3 | -3.40428 | -50.37229 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84985231-d22f-3828-9800-9f53381cc7be | -3.57388 | -53.7819 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f6749da-f67e-370d-a09f-32887c0c259f | -4.7391 | -49.53079 | 2024-11-12 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b204c1a8-5589-3f35-8931-5ab7d34adda8 | -3.10467 | -54.29743 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9135ad87-5dc0-3e1b-af1f-5df806269931 | -3.36031 | -53.40517 | 2024-11-12 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e20f9da4-db3b-3c43-ad0d-a48d06e20a25 | -3.06644 | -54.5778 | 2024-11-12 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0b082ab-1356-301d-84eb-dff02bef086a | -3.51665 | -49.95958 | 2024-11-12 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 473c7b44-3ac2-304b-a99f-751154c5175b | -3.05814 | -50.32286 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99063a34-f68b-317f-b7f3-cc3dc6b57d96 | -4.03775 | -53.74255 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc156c59-d2ff-366a-a95e-264f0f8bdd3b | -3.71363 | -53.40737 | 2024-11-12 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2335edd-3d98-31c8-9476-14d2e2c375fe | -2.78765 | -51.75612 | 2024-11-12 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb1489f2-8694-3b69-8942-26018824a0ba | -3.1096 | -54.3066 | 2024-11-12 05:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 3f4f31d4-d835-3f1f-bcef-a5d63e0aebcd | -3.9482 | -48.194 | 2024-11-12 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 57db8eaa-d977-3d30-8a94-739927dd3699 | -2.1087 | -50.6916 | 2024-11-12 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| cc68f250-84e3-3ec0-85b7-2ecd30af3400 | -3.0504 | -50.3332 | 2024-11-12 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| f6ee38f0-856b-3880-aa5c-58a0d1a63d8c | -2.7588 | -49.3285 | 2024-11-12 05:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6f53d14b-5951-3e32-b0bf-0ee8e7eb93d9 | -3.0913 | -54.307 | 2024-11-12 05:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 5bb47101-a307-3b48-b3cd-f7d77c8f5243 | -3.9483 | -48.1724 | 2024-11-12 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8f02c149-8468-3e14-aed1-809a97cec5a1 | -2.1271 | -50.7121 | 2024-11-12 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f03acd44-88d0-3bba-a261-e28c7ddbb4be | -3.9669 | -48.1716 | 2024-11-12 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |


[Clique aqui para ver as próximas entradas](README21.md)
