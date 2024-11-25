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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 741911f0-8e1a-3a57-9342-98ba834fe75d | -1.82718 | -51.20965 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5022ab1-d16a-3a4e-b46c-75f33f4bb364 | -1.71984 | -52.70225 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57c976f2-aac7-3e33-8959-fe0dc9602b85 | -4.70998 | -45.72354 | 2024-11-25 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee8da872-ffa2-379d-90ce-07a7f8c5b26e | -2.5708 | -54.06426 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e0a7723-2613-335b-ab81-226fe0768491 | -1.48511 | -52.51676 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e355d94-a2d7-3bda-9a2a-39f075e76842 | -3.71134 | -51.79769 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eac7eeef-adba-3a8b-8954-b4f53d7b3347 | -3.62051 | -52.20459 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8be687f-1ec9-34c1-9bdc-3b325f96b487 | -2.14063 | -51.017 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b43d9d7c-0d24-3cfb-97a7-3c5e68ac6c03 | -2.16558 | -53.26599 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a2a2eb3-051e-30b4-b2bd-755d695ac9cc | -5.00179 | -49.97241 | 2024-11-25 04:55:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8153ef35-1342-32bf-9fe0-529c077b9a95 | -3.05122 | -54.02506 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bd03436-cde9-3521-b024-bc76903eec0a | -3.51118 | -53.81285 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b5c0a8b-d096-31a1-9354-83d9c4bd7edb | -1.11653 | -52.10736 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0cfe1c-050b-31c7-b706-24f02c2adac0 | -1.39665 | -53.61641 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a960798c-3927-32e4-a51b-e036f70e26b2 | -0.82021 | -51.49113 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c8891f1-90d1-34af-b061-d83db5972520 | -3.42186 | -53.28587 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2749e74-1d91-3a3c-96e5-b4b150e29250 | -2.88257 | -51.58359 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c82dabb-502f-3869-8682-ddd9024608f8 | -2.33463 | -53.86977 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 336b39dd-97d8-3dac-b029-b48dcda57215 | -2.35926 | -53.71357 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b887aaf6-e501-344b-af75-1da4ab6e544e | -2.80493 | -54.01826 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fc32929-c40a-37d5-a823-14a18b3ae02f | -2.92431 | -53.07027 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f95d60fb-531f-38cf-8b4d-1422efddd0a8 | -0.75258 | -51.73517 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60fca862-931e-3d89-a456-8995368b10ec | -4.15195 | -54.23696 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 108e5dd5-71dc-38d6-9a6b-7fb1a5da6dcd | -1.91644 | -53.34316 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445bcd85-24ee-3089-8cb9-0661bef420ff | -1.10285 | -53.61272 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c48ed0de-4c1f-3d97-bc5d-f6caa3eeb6c9 | -3.93821 | -47.98502 | 2024-11-25 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21abbb98-ff62-33b1-8013-7a3b79eadda1 | -1.76024 | -52.70498 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e0acb0e1-e9f4-32d3-9cbf-e62335d3259c | -3.61604 | -54.21694 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b26307d2-b1fd-3aa5-9676-37b8b013b5af | -3.05141 | -52.75703 | 2024-11-25 04:55:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75ad114c-55a6-3805-b926-743bfd7b6ed5 | -3.42587 | -54.59101 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09d3b73e-2b59-36d4-b118-e7c9b3a83b3f | -3.24406 | -53.27233 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82f8cbfc-e28f-31c3-9e32-36ba1775b8e9 | -1.0698 | -53.17891 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37d817c8-ef33-3f64-b0be-7291304a4287 | -2.01493 | -51.17434 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 496e2f01-c452-32a9-8572-e239f7b5a968 | -0.91066 | -51.64752 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49589cc2-9573-39dc-951a-1c71ec211193 | -5.13531 | -46.19112 | 2024-11-25 04:55:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 655b9147-0de7-363c-8b2a-3ffd32eabbe6 | 0.61481 | -51.77394 | 2024-11-25 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aaa5417-60f5-337e-b7fa-4d8bde5ded22 | -3.945 | -46.5126 | 2024-11-25 04:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a3fc7ce-021f-3b9b-aea9-7d451d7c6d0e | -0.81642 | -51.60358 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bb0a43f-33a2-3907-b544-a999176196c7 | -4.84807 | -50.80628 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd03e767-15b1-3a2c-9e20-a579cda778e0 | -0.8923 | -51.72081 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 496b4f82-26a1-3c2f-83db-9970434b8f72 | -1.26602 | -51.62903 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f66f157-dc82-353d-8c14-8df98af3dd16 | -2.02691 | -51.18758 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2c338bf-56b0-380b-88e5-f08c1dfc2aca | -2.66524 | -46.60423 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42d5ee8d-6380-367b-bd53-b7eb882d6443 | -3.81334 | -51.99597 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6dddfef-efbc-3761-bae0-ac40b3af289d | -0.92241 | -51.63845 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50a442cf-daa0-3e32-aa0e-eda0ebf8001d | -4.25536 | -48.66972 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e36b4bcc-9532-3806-ac89-ea3735883ea4 | -3.52725 | -53.81893 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a61d049e-ae11-3562-9cea-be785252ec1b | -2.79414 | -51.6817 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02b5a873-4f94-3af9-aa74-6e21b4377e23 | -3.51396 | -53.81684 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05ef7796-b092-3a96-9821-3a66c912ac70 | -0.34581 | -51.54575 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e95ba00-aa19-3ffe-8346-186603afe295 | -1.22855 | -51.73604 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3e6552c-bfe0-32b4-8305-f766caabb255 | -1.73929 | -52.73001 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 17e5c028-672e-3db2-9d54-a616819946e5 | -2.97876 | -52.91602 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3ac91e9-f845-37bc-ae65-d4e3cd364a92 | -0.32007 | -51.59972 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddefade3-e57f-3cd9-8108-81039ee6e4cb | -3.7875 | -54.65128 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccc63fbb-b670-367e-aee2-939b1f7a2a21 | -3.95912 | -52.22761 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8266e8f2-cb1d-37ca-a16c-38cfc0dccfe4 | -0.36045 | -51.40978 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee9ea50-f0c6-3ef4-a310-7e660a2d37e1 | -1.28571 | -51.7449 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0030c2dd-3aac-32b5-878f-478dc6c6bc7d | -1.72302 | -52.48669 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 501f6dc4-8087-3025-82b9-a85fead34060 | -1.35165 | -54.63255 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 28908938-099d-378a-a722-88c8961244b6 | -2.16504 | -53.26944 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8987f48-a15e-3d9f-ae42-be3eb8cd2fd8 | -2.79158 | -53.01087 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9eff44-5687-3c96-8fca-ffd658b136bb | -0.80746 | -51.61673 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71130310-df58-3929-83eb-091a4a7f6bbd | -3.26562 | -53.82369 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8f5b1bd-0614-3031-b4e6-4ed24fb2ee81 | -0.04962 | -51.74536 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8875aa29-8401-3444-b1d5-24906c98d914 | -3.25068 | -54.24197 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a7f381a-2250-32e4-bce3-8b5fe989fd32 | -1.19334 | -53.89173 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1655ec50-db7f-30a3-94a6-6bbffae58732 | -1.07563 | -53.37416 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 965fb90d-f629-3ff9-9cd4-f25480240d56 | -0.92705 | -52.64542 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd17482b-7a22-330b-9b89-bc47e680590d | -3.24342 | -54.22292 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1bc37bd-5538-37af-adaa-e42f85803f4a | -4.37509 | -48.50684 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2d1352c-fa44-3ee6-8501-2eb3ea456457 | -2.61611 | -54.25454 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10f5c6c2-5d15-335b-a894-5f4e7e0b33ab | -1.95676 | -53.32471 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 974d14b6-56fc-3c4c-a4c3-bfc9a6fb8159 | -0.82133 | -51.48399 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f3342d0-d90a-36db-b91d-86d77d170cd9 | -0.94821 | -51.64972 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 578e0a1c-2c46-3523-8469-16d412a54341 | -4.30367 | -46.57296 | 2024-11-25 04:55:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e494a0a-b174-3ee4-8905-1bcfafd9b2db | 1.38244 | -55.8982 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9629d80a-2ab5-3484-b5f4-9b207399cb44 | -3.10624 | -54.97879 | 2024-11-25 04:55:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00fb5ff-cf85-3f30-9417-da0d53c9deca | -1.98108 | -46.42746 | 2024-11-25 04:55:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a27ebf73-ccbc-3cb3-9a4b-fdc11a5bfa3c | 1.84953 | -55.90072 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d4720744-5cff-3fdc-a7ba-be0448f12cf9 | -1.48843 | -52.51728 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9649a160-0075-3608-8bb6-c4d576085902 | -3.54091 | -50.45616 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63b59907-e74e-3b94-8c37-1f4d025753c3 | -3.43375 | -53.87464 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c49f6a1d-f409-38a9-90b0-0c543c801af4 | -1.64117 | -52.70709 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae318fa8-9434-3dc8-95bf-b06d168432b0 | -1.19332 | -51.76321 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d81754f8-dedd-3d18-ae24-502fd5d3b51a | -0.21438 | -51.18929 | 2024-11-25 04:55:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d487e79-c8b2-3c9a-96c9-0132a68f5f68 | 1.41376 | -55.89072 | 2024-11-25 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cd2754b-d7a0-353c-8098-933f2ce7ed00 | -3.79036 | -49.85217 | 2024-11-25 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd26b1df-086d-3ece-9af5-d935a10ba84e | -2.9991 | -53.73259 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad082058-3491-3f1f-b124-7f1dd08e79ee | -1.2034 | -51.76478 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21526f3b-aea4-3e96-9204-a559811e0c91 | -0.80799 | -51.59136 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45a76fc3-812b-330b-8cb2-5b0da91cbaca | -0.27647 | -51.61463 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 985181d2-c8df-3e23-8f43-f6ac4b9eb30c | -2.31471 | -53.60732 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f676487-8399-3afa-8040-cbc565b8945a | -1.60205 | -52.26839 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4340dbc-4af4-393e-a2e6-4a7f851b3858 | -2.32463 | -53.86822 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1ff429d-be90-3074-81bd-0e301b9247f1 | -2.56189 | -54.05571 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b7042a8-7c4b-3df8-b1b4-cb66ae9e0ecd | -0.91457 | -51.6445 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b398c78a-169d-3bdf-b19b-2456b80131d2 | -3.51673 | -53.82082 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e517ec86-6f73-38f1-ad62-8a0a84cdd912 | -0.39732 | -51.44811 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5b235a7-7787-372c-aca8-fe7e349a5740 | -3.11118 | -54.00574 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README37.md)
