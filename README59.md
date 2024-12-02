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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32551c23-78e9-3e00-ba19-e109bebd44c5 | -4.62317 | -48.03493 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68d04fad-6535-3386-b46c-7bdb0c95943d | -1.77952 | -53.71451 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56847acf-a952-3791-bce5-1e0e922580b4 | -1.53255 | -51.20062 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cd7ceb3-5c7a-32a6-ad0c-aee7cdcd1b7c | -2.89733 | -53.95783 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76c6f551-f674-3900-b869-13c5ed47989a | -3.49647 | -54.17807 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddfc3417-f63d-3374-94dd-67c33cb9b585 | -2.83656 | -54.09291 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f93a2654-fd8d-399b-8d4c-4b4c4740a3d1 | -1.99775 | -53.2869 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 759708eb-65c3-38bd-9caf-83bc086b5179 | -3.03181 | -54.04074 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e7d0c8d-e827-3dc4-8cf9-3eb5aa2132d1 | -3.10353 | -54.02781 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad694802-35fd-3bdc-aa30-3e24d088bb68 | -3.61014 | -51.42688 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3bacc3e-ddfc-3ddb-8751-df2177c247b6 | -3.39615 | -50.23345 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3615c2ba-3be7-3e5c-af8d-43c61bcc46a3 | -2.14939 | -50.62743 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c672a6c1-a00c-376c-8957-4489d1c4afc6 | -3.05783 | -53.67601 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4538e354-bb16-3b94-9d98-2f923e69f0c5 | -3.64882 | -52.66963 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 655750d5-5cea-3238-b60c-bbe157659ccd | -2.35007 | -54.36932 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fcec643f-2b75-39bf-9217-c2de26f41106 | -1.24497 | -54.55093 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc619b2-f3a5-37ed-8992-43aa57e657e2 | -3.79599 | -46.69581 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08c6e045-387b-3b67-b17a-9b69cdc3d3ff | -3.5743 | -52.28197 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 649dfc8f-6973-39d7-8edf-f514cf0c36ef | -2.19755 | -48.33721 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7761081-b244-30b4-b1cd-a2c32d3617fa | -2.60889 | -48.36406 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb2db7c6-d646-3d59-a8b0-dc733e146b60 | -2.25787 | -53.45816 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 902da8c3-b843-35ea-bbd4-ebaf0370ed2b | -1.5431 | -52.9901 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9527595a-a505-38da-bd35-bb38eaa586db | -5.58988 | -45.15163 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4acfa656-e878-32a1-885b-6592093554d7 | -3.17744 | -55.01684 | 2024-12-02 04:48:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdf9ea11-6665-3d1a-931f-7753412ee028 | -3.76623 | -50.174 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ff6b63c-f95a-330f-815d-3d9901408674 | -4.27959 | -50.68435 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 173c613b-c136-31d9-a234-b9974fbe7cdd | -3.10596 | -54.0126 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78113440-cdd4-3aee-8bc2-40be1a65b064 | 1.09654 | -56.01677 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| b838532d-0973-3612-b22f-3f1f6380f957 | -2.84924 | -54.10279 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d107929-05b8-3bdd-a9e1-c8cac0d5f8c2 | -3.1025 | -54.01206 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0b700ac-72b3-306c-b85a-52dd814f27bc | -2.74576 | -54.04749 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41ecb6f3-985b-3980-9bcb-b107c9190cdf | -2.55835 | -53.39944 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a068aeec-e211-3652-a14e-806904c38cdf | -2.84576 | -54.10223 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b9e299f-0a3c-35fa-9da2-069c9cfaaf97 | -2.19065 | -53.57281 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aae4c95-2a0d-328e-a99f-6fe91deee774 | -2.34653 | -54.36876 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d054f880-e3cf-380b-a884-9a945b3cc54d | -3.25963 | -53.6421 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 490dfa0e-4dd0-30d3-97d8-93a7fe5374d4 | -2.97258 | -53.85698 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cdd56c4-1d7f-34b2-a604-70182a37629e | -2.98498 | -53.88971 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55f2469e-ade8-3b80-bb10-48b078814d16 | -1.59201 | -51.256 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 327d1ce9-99a7-3a99-9f72-51cafe110c97 | -3.0999 | -54.05057 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6928151b-236b-3094-8ad4-1da06ad61853 | -3.02035 | -54.0233 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6482c88f-3f9a-3011-b94a-6645e61ceea2 | -2.88478 | -54.01425 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b418585b-65c9-35d2-b9a9-0ab5297490e5 | -2.26743 | -53.61909 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e636f2d4-ca82-3c2a-b7e1-b02e0d9ec0f7 | -2.9464 | -49.45317 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f412f9c-f184-3fc6-9fe8-1b15bef9b840 | -2.613 | -54.08657 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93f292d9-9cdd-34a6-bbeb-3d2a2290d221 | -3.17288 | -53.63654 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e3c3041-a8f2-37f1-8aa0-552bce4edda0 | -2.46263 | -53.71394 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8990cf53-2c40-3c95-97e0-89916a2e5fe1 | -2.89552 | -53.96919 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1294290-dd1c-33ec-b3b4-7fcb0eaa8d98 | -2.89713 | -55.22349 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43ec607f-c52c-3eba-851b-bc21848aca0d | -3.2608 | -53.63475 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b583b636-699a-3e46-9129-38ef5949296a | -3.04227 | -49.37325 | 2024-12-02 04:48:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e132863-9eab-3652-bdbf-e28bbd4d1990 | -2.89291 | -54.16503 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6fb1522-60c2-3238-a7d0-e1ce79047c4a | -3.07789 | -54.12148 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e488f7a9-edc8-38a0-ad83-97b7d2116358 | -4.26367 | -50.85297 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cad81d3d-df9a-35ae-b63c-2420e29a6e0f | 1.11061 | -55.99985 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 030cae1d-fb6c-3fcf-8fd0-050f3b7ac497 | -3.30201 | -50.11891 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33596d4b-b4e7-3ac1-bb12-ee361d98ee94 | -2.47536 | -46.5679 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb36501a-b057-3405-9fa3-cc184a7d0940 | -2.56443 | -54.22632 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 442e0ff1-dd1f-3c73-b9e5-fd4a4f431732 | -4.31646 | -48.09285 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aba2b8ce-fade-3ea0-9d3e-effdfc7de857 | -3.45153 | -54.57 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba9901ad-fb1c-3f49-8d7e-91118710a16b | -2.7662 | -54.0311 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59608dc4-213a-3993-b2c9-d8204e8f6d9a | -1.32421 | -51.74842 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 445d5b5b-5110-3607-9bfd-d20ed1a85d2e | -1.70152 | -52.43586 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c03b41b-03f3-3ea6-97c6-5c5724e96950 | -3.10129 | -54.01965 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc401c4d-5895-3754-b8dc-f84a1e782b35 | -2.81076 | -54.04205 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c4247c5-54db-3118-8ab9-7384735db82b | -3.26501 | -45.37188 | 2024-12-02 04:48:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6af401bb-1e04-3306-9105-fc4cad7a010e | -2.15617 | -49.75855 | 2024-12-02 04:48:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88903a8e-7e09-3e97-b0b2-17b422ae835f | -1.01471 | -51.72816 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 428be903-681e-389f-9c0a-e3e6dbba75a6 | -3.50639 | -53.83213 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b065145-45ce-3094-8dc8-806280393a28 | -3.2568 | -53.63789 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7528acb0-3271-3d07-97f8-b0ccdd9e830b | -3.14384 | -53.84132 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9e55451-427e-3ee6-9eb7-58aea007603c | -4.076 | -54.56257 | 2024-12-02 04:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d8648b6-2d6c-35cd-802b-b59f21cbbd0d | -1.49371 | -52.41816 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f2fb9c-c524-34a9-be16-81c73ea41f29 | -3.95811 | -46.50378 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15bb60cb-a4fa-3a54-b5fc-2626ba5ccdd3 | -1.79342 | -52.28572 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ab4a93b-5ea8-3669-a539-9a8741fbd5c9 | -3.31908 | -50.03179 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca74acfd-6f18-3717-b0b2-cf5ca55eb2f2 | -2.3459 | -54.37275 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cd0bb53c-ef4d-376e-8a40-e612330ac263 | -4.18521 | -50.68058 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41731558-8710-370e-8a43-ed7bfb3f5b8f | -2.03479 | -54.66676 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b021d879-6a25-3743-8498-ef41c9930ad6 | -2.92052 | -54.1259 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe604b8a-e3da-3ec3-925b-be7daaab9967 | -4.9127 | -41.34292 | 2024-12-02 04:48:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4ff79ec6-7c43-34d9-9f7c-5a11172ac7e2 | -3.24895 | -54.52321 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13e23b34-a983-3a25-9953-5ec1834d7064 | -3.39558 | -50.3036 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eef7fbc9-90ba-3295-a876-35f93376116d | -4.36079 | -46.27085 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62fbe5ca-64d3-3782-8042-8799411aa1ca | -2.12036 | -46.41587 | 2024-12-02 04:48:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e15b0ecd-771d-31a7-89ba-ba1b501af72c | -5.16727 | -44.80193 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ca074cb-6151-3deb-9caa-8cb4cafd34d3 | -3.7295 | -49.93833 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84ea81f7-1028-33a0-ba79-96fdc9acff81 | -2.0384 | -54.66733 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 74c5194e-312d-3f32-b07b-7254ff4e5945 | -4.12006 | -53.80967 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0101132-388e-347a-8aad-061ece8010b3 | -4.05962 | -46.82365 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fb878c2-c20c-3d27-84d9-3a7a5fa413bd | -4.27231 | -50.68687 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6903b932-1958-3b16-8df3-1cd4631b2d96 | -3.75523 | -52.27494 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f7dc58e-c7dc-34af-901d-102e7fbb1310 | -2.66748 | -48.80167 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 353fbcfc-1cc5-36b2-8d0c-40919f84bed3 | -0.57985 | -51.68492 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a9de46e6-308a-3a8e-8537-cc5823aec4e8 | -3.918 | -52.38505 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 528f468c-80e7-37da-9dfc-cd20b2095290 | -2.79218 | -51.89823 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40ad9a5a-b5f6-3c9c-9190-fb2f612ec691 | -1.07848 | -53.22438 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4375b3d4-3a5c-31d7-8250-8654591c60e9 | -3.25984 | -46.45156 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2503d5b7-14ac-3351-9262-0f3b2a7ae244 | -1.99955 | -52.09809 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c227089-dacb-3f8b-b580-31c47a2b4661 | -2.82383 | -54.19407 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README60.md)
