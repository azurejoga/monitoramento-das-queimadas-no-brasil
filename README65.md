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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06773552-5b81-33a0-b85c-90d8d58cbaf4 | -3.36101 | -50.05653 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f522644a-db7e-384b-89e2-638d1f0fb45e | -3.90706 | -49.74226 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0f764019-b4d7-30bb-aa8f-ff3501af0644 | -4.0851 | -48.31848 | 2024-12-02 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3207af00-1759-37a4-84eb-d5e0219a2ab7 | -1.20077 | -53.87395 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e1826de-c259-353e-8813-eb156040bf10 | -4.3297 | -45.92212 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1da9911-7476-3d45-b1c0-3fe65ce1d50e | -2.45575 | -53.7129 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02fad3ad-4d32-30a1-b36e-560521dca8e9 | -3.29526 | -53.83748 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46d0ba79-29ff-3f68-ae55-6df3349fb7cb | -3.97871 | -46.75213 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b66c31b-c722-3ad5-bb5f-df0eef26477d | -1.09162 | -53.6054 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36ca3cc4-2d0a-30c5-b487-ef2623bc1671 | -1.35118 | -51.38329 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e5aada6-e5f8-3597-86c2-9201a25a80ee | -2.74657 | -54.08692 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b0d29f8-4f9c-38c1-99be-df4bc0cfb009 | -0.96196 | -53.20685 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1dcaa3ce-cf72-34c8-9308-65fdc9004f1d | -2.83274 | -51.83414 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4ff8c04-fbdb-3f93-8bf7-652f51e0079d | -2.87045 | -53.92645 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e299360e-db0a-3700-935f-ebd695b5acec | -3.67946 | -50.10442 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17bedcdf-f0d6-30c3-b998-6bcc0121735c | -2.82229 | -51.83604 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f2387c-b5fd-3b6f-814b-de2b5b0803c9 | -3.74693 | -52.26303 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 470f3345-71e7-3903-bb7a-8f601c87e4a3 | -2.7818 | -55.35888 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97065258-1596-3c58-b0d9-e49e24b20ec4 | -4.4166 | -50.29806 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a605669-d40f-32f4-aad8-aebbd68daf40 | -2.6085 | -51.81281 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7623696-08c9-3f32-8a45-626257d31d65 | -3.33637 | -53.37826 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3b8e5d2-408e-3ac6-b108-3e1c221b0772 | -1.9534 | -53.34414 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc6e6d10-5f2e-3268-bbe0-ef756e9c5f51 | -2.81015 | -54.04588 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb697386-d8f2-30c1-8074-78d1809f3105 | -2.82391 | -54.07163 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58284285-721b-3bf3-ae0f-798de99049f8 | -2.35003 | -54.36859 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bd5384b9-6bbf-3de0-b087-05fe60e020e1 | -4.25752 | -50.84842 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b3dcadd6-e669-3ac6-a362-fca8f64aa120 | -2.25748 | -51.25815 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65e60ee0-93a1-31eb-9e29-23ae5f8979c9 | 1.15822 | -56.01074 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c028c81b-3180-376c-86ea-3f077fc70cfe | -3.69908 | -47.12508 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2da45449-621f-3dfd-9818-5dc1959d1d73 | -2.99016 | -51.32981 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfef9942-1335-37df-b4a6-f8ee32234dd7 | -3.69348 | -53.42346 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eda84312-f311-35bf-ae00-48ccde0191f2 | -1.20017 | -53.87782 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0945120-c3c5-335b-9764-8f7f2029582e | -2.80486 | -54.05681 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3373d11-5524-36ed-b6fe-cf829d54411c | -4.05732 | -48.9611 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 48e44d2f-b22c-3605-a27f-ca5eff42af54 | -3.94685 | -53.51042 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 567af94f-1697-3fa3-b17e-a0e586819784 | -3.11212 | -54.04078 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 994d22b5-bc76-3602-84f8-9062c45b1673 | -1.23357 | -51.61127 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3071a78e-faa7-31fe-ac23-aca61268e6c3 | -2.98032 | -53.89672 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 951dab87-7437-382a-95e1-a0e0498ba316 | -3.86285 | -52.39061 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6a32095-a43a-3388-862d-65e9eb394176 | -2.47426 | -46.57496 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39bf1a2b-8e98-3540-9825-9a9b7138779d | -2.4428 | -53.61948 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 911d5828-a6ee-3aca-94cb-a35757d99b64 | -2.65115 | -46.77644 | 2024-12-02 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7165fe9d-6082-34cf-9b0d-a205c9d6018e | -3.48136 | -53.81284 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5858ca2f-2847-3c91-a1fa-79a06f0f6d3b | -3.3559 | -49.56767 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8041c3b4-be81-378d-80a7-d1f639ba6947 | -3.25835 | -46.45085 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48184e13-51af-3877-9b70-ba1c8f0f8f50 | -1.26866 | -55.70255 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74b9edf3-cccd-35fc-9e4c-6d9b3c06dde8 | -2.41184 | -53.86099 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ec912d8-e710-398d-a748-709c7c374c75 | -3.02784 | -54.18843 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d6a30e-1718-3d1c-b053-0778541be244 | -2.77399 | -48.579 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a279ad2e-bf46-3f14-b462-6e778d7727dd | -4.30741 | -48.23038 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 809572d6-4e3f-360b-8b03-a710680febe7 | -1.49712 | -51.94522 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8ae0e22-9c16-369f-945a-067ea45a7a94 | -1.00533 | -51.72317 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 560798a9-9c07-32d1-8698-965fad1f78b5 | -3.78605 | -52.40387 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f71a968-0d43-3978-9bea-1bffd08ccf9e | -1.18445 | -51.77273 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd660c5c-2fb9-314d-9bf1-c12842414124 | -3.11086 | -53.80528 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eac8f98-67ed-3895-84b4-505428593685 | -3.47793 | -53.81231 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f21a2cda-504c-341b-93bf-6f5c39d68e0b | -2.83594 | -54.09674 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca48fbf8-53fd-333b-9625-fcbc083a8728 | -3.26197 | -53.62741 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d2e68e71-c809-3f29-8d89-ca661654f686 | -3.40066 | -50.22673 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70a0fa7a-41d7-35a0-972b-8b47d90f17f2 | -3.48761 | -53.81767 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b449959e-3323-38f6-bdaf-db123e76f323 | -2.02933 | -52.08149 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4306a39d-367d-3014-97ee-67d28f049be5 | -1.9577 | -46.44284 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a7b10d7-6850-3290-a8e9-527e8a0f34c4 | -3.90297 | -51.05303 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b54c9646-969e-3bbb-9957-3250ee2ac017 | 1.21322 | -56.01683 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38cda6b2-d41d-38e0-81b3-3aeea89ad167 | -2.44763 | -54.00721 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 11cf9d11-078d-3e6d-9f6c-305ea5282fbe | -3.55491 | -46.0228 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66fd18a6-5f55-3ae7-b4d1-8b2d17d7202d | -1.23699 | -52.5364 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2efa3044-48a2-3ab4-812e-390fcbcea063 | -0.61816 | -51.70187 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dfe057f-eca8-3370-a9f2-db8be788baba | -1.59093 | -51.26287 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cd33651-b7a6-3962-8894-cd4ad4d52002 | -2.86378 | -54.03441 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e4abe3d-b2dd-30a2-9ff6-550637f3103f | -2.69264 | -51.88235 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1901fa00-5151-364a-b2ea-0b715e91f570 | -3.49499 | -50.31901 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13f05b37-c96f-30b0-872c-122139be3a0e | -2.35959 | -53.65601 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02455668-233b-3a06-9c46-fbe4e822663d | -3.26212 | -50.57219 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 115790cb-256b-3dc6-9e3a-d7c06f008431 | -2.15832 | -50.65742 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 503830f1-e5f4-36f8-9a25-f30a5b3e62d9 | -2.37946 | -53.68594 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08f663de-fb4d-3d2f-8796-3c34b726bbc9 | -2.86847 | -54.02732 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4658b78-cb46-327b-91da-7fa280cd4510 | -1.45582 | -52.61418 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0d46947-01ae-3e6f-9d26-2c136923469c | -4.24906 | -49.19057 | 2024-12-02 04:48:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 842d44de-2767-3a8a-a31d-5836bbd93acc | -3.09868 | -53.75052 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c38abd33-f242-3da0-b34c-010ad5d06049 | -1.65459 | -52.75366 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d90de516-d3c8-38fc-866d-06a07cfb5a4f | -2.48364 | -46.573 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022605e4-0cfd-37b0-b8e8-1009fe6cdd79 | -1.6208 | -53.89748 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9233060f-2fd4-3d5a-b2a9-b143d172343f | -3.74531 | -52.27337 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80ac6645-6075-346b-bc7a-3e8bf76e826c | -4.01518 | -47.0053 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c764d20c-f16f-3525-aa08-a2aed6d7e59b | -2.59121 | -53.9888 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afa9bd58-aaee-3a89-a912-6dbdd7275f28 | -3.53459 | -50.17672 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ffedccb0-c94f-38eb-b0ec-06062548459e | -2.58244 | -53.99918 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8bc87c30-575a-3528-8d5c-70d08bc6fdf3 | -1.8854 | -53.28837 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d10908e-bb4d-34b4-ac32-06b6bcb4f43d | -2.84448 | -48.09846 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f10372f-e4f2-3536-8244-199da9a3b928 | -1.09196 | -53.64804 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9765de5-e372-362a-94ce-e68c87e93bfc | -1.72936 | -52.49765 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60030d1c-637a-38e9-942c-0df0d8ae956c | -3.26745 | -50.05006 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d18b1e53-393b-3f3a-8936-a1108c24206c | -4.61694 | -48.02484 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cd0ed82-504f-3175-929a-f10a81beb7e9 | -1.25772 | -51.58689 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff3665f0-a48a-39ab-b3a7-566a11d9a3c0 | -3.0319 | -51.54122 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b0029df-6a4b-3bbe-9d89-5d397e4c38b7 | -1.69986 | -52.4679 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71bc6589-c0e2-37df-bdc7-5eabca72c219 | -2.79964 | -53.11802 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2207924-fdac-3865-91a9-c73284976c43 | -2.52921 | -54.04227 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2291ff57-c262-34d9-92e1-f359cfb9dc74 | 1.13685 | -55.98103 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README66.md)
