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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9c24c9d-a2c1-3740-9f4c-5033893def84 | -4.55999 | -48.00365 | 2024-11-17 05:22:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a60dcddd-26c1-3ee4-9503-0af7f97e9aa2 | 0.40723 | -50.86631 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a369d1c1-32d3-36ab-85e5-4833bee50804 | 1.5774 | -55.87864 | 2024-11-17 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b88ea02e-be3e-330d-b783-f33eb1db80c5 | 0.61209 | -51.77151 | 2024-11-17 05:22:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 88e9c535-9166-35b6-ae26-9919fa07122d | -0.95154 | -51.72766 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f39fdd27-5267-3c2e-aade-63f5b5fb5025 | -0.32303 | -48.6938 | 2024-11-17 05:22:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20013b99-8dde-3574-a8b0-41e2ed903339 | -1.83065 | -46.59712 | 2024-11-17 05:22:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01ed7e0e-ed75-3614-8ace-12f22542f775 | -3.71556 | -51.842 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9ee7c61-f1dc-3812-957b-2a81be9a2efb | -0.09861 | -51.43826 | 2024-11-17 05:22:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47ce60bb-438e-38a1-bbd8-a33f9ef8ac6b | -3.97858 | -50.93108 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 575c3c75-9508-3c3c-9442-ed910180fe7a | 4.08242 | -60.24387 | 2024-11-17 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4d39e32-ab4b-3f1e-a0f5-41efbe83b877 | -3.79744 | -51.3759 | 2024-11-17 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a424d04-3fb1-3775-9b0e-431e76f67711 | -3.26262 | -54.53221 | 2024-11-17 05:22:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6af7bca-9a45-3ca7-8327-d380d0a8ea8d | 0.52783 | -50.05664 | 2024-11-17 05:22:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e91a47-d34c-31a0-86f3-90bad45ee4cf | -0.82821 | -52.29463 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2388968a-b91a-365a-a4d5-e133d476fac3 | -3.86985 | -51.17062 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9d4782-13aa-353c-8c18-81816a01f1d2 | -3.39347 | -53.26993 | 2024-11-17 05:22:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfd22bc7-034f-3b10-bc6e-3469183dcfe4 | -0.04697 | -53.24994 | 2024-11-17 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 015f2130-c757-30ac-a933-a0656ad83e29 | -1.23413 | -47.35569 | 2024-11-17 05:22:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 03a8fd0e-c2e3-3b3b-9c36-8481092e9fb1 | 0.40263 | -50.87006 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 77a942a7-5d69-36c8-8cfe-7941f6ec1ffc | -3.79787 | -51.37292 | 2024-11-17 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b58ff18a-d28a-3c87-9adc-0e468122133c | 0.61765 | -51.77589 | 2024-11-17 05:22:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 740c9378-1925-3605-b5b9-715a8c81ff43 | -0.9019 | -51.94809 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fce9951-6f0b-39f8-bd70-542a3c2d8ee5 | 4.0796 | -60.2481 | 2024-11-17 05:22:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9bcbb80-d005-3c65-be26-3ae2b2c6cbc5 | -0.83527 | -52.3412 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d8a8532-21c5-39ca-a9fe-115fb3bbc8af | -0.95454 | -51.72858 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ceb6f7a0-3091-3c30-9c74-9d82281153ab | 0.40171 | -50.86415 | 2024-11-17 05:22:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1d38021-6cd6-37e3-966b-2c1a2ada243d | 0.51117 | -50.73983 | 2024-11-17 05:22:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67412bb8-58f5-34a9-a33a-ccfff4aa1418 | -4.23399 | -50.67877 | 2024-11-17 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 453b7107-a457-3182-a6b2-7615b5bf9465 | -0.88576 | -52.77714 | 2024-11-17 05:22:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a52ef03f-b439-3a66-bd88-2f1f69432b8e | -4.04002 | -50.88763 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 17cd6a71-0290-337f-a66a-72fd1467c625 | -4.72976 | -46.84211 | 2024-11-17 05:22:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a8f7e02-58a0-31ab-8e1e-15d362c88649 | -3.71581 | -51.84535 | 2024-11-17 05:22:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208b824c-012b-37da-ba46-ec731c1c2e92 | -1.23327 | -47.36132 | 2024-11-17 05:22:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 346ac12c-b191-334b-a6df-70c8568be0ba | -0.90921 | -51.7431 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac63df29-fa57-3658-b124-bf3afec23fb0 | 1.10844 | -59.19036 | 2024-11-17 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63328d4a-71bf-3535-9148-8071a6dfb1c4 | 0.00027 | -51.22035 | 2024-11-17 05:22:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69bee9dd-6746-3afa-8613-68c9c70a9acf | -4.63778 | -50.41819 | 2024-11-17 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2d6ab34-3281-3a1a-8519-d2a86ecb6a05 | -1.01834 | -52.27617 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9dc4169-f10d-3e1e-b96b-343c311f69b6 | -3.70115 | -51.0791 | 2024-11-17 05:22:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548f8da0-9228-3865-9294-c58ef16e7be3 | -0.90685 | -51.72618 | 2024-11-17 05:22:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| db72ad86-0e79-3716-a25c-a98133028f48 | -2.32961 | -53.57025 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bce90161-70d6-30c2-aa9d-688dc4092032 | -3.1166 | -51.32506 | 2024-11-17 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7070930-6cb7-3966-81df-166ce8f0495a | -1.40051 | -51.08289 | 2024-11-17 05:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac8ee2c3-5d35-375f-9e6b-189e95cf2baf | -1.6338 | -53.28711 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0f9e7c58-da4a-3499-836a-324917974a46 | -12.55737 | -57.81923 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 107f2adc-7abb-3d32-89ce-cbdac2a32c30 | -10.99766 | -59.09101 | 2024-11-17 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 262859f9-cc10-3545-813c-1c16a463c98b | -1.2127 | -51.77742 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 414f5a71-8703-3227-ab59-4c88a74dddd6 | -2.80835 | -52.91804 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9531f835-d02f-3941-8c9c-e0c1dfa1bc4c | -1.29591 | -51.74114 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 82c0b7f5-46fe-3efd-acf6-6f9ccb17c8b6 | -2.73613 | -54.11609 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6526ec84-2125-31d8-bc33-0ed814571a23 | -2.33335 | -53.57519 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 011f383f-dcce-3bd4-84df-63121dfa61fc | -1.29674 | -51.73565 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 395a189b-d8ed-3156-bc66-3a9c7fddbdb6 | -3.92245 | -46.52436 | 2024-11-17 05:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 610a8419-68d5-3cdc-99b2-c90ff0002c16 | -3.58442 | -50.5308 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec0e3565-ee75-37e5-90ca-95f8756e52e5 | -1.2972 | -51.96109 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6e11f552-ffc7-39f2-b705-245e00128142 | -3.03356 | -54.09828 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de503745-7c8d-3a8a-be2a-2ac930f23bf2 | -3.53738 | -50.24071 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2fc3323-57ed-37c9-b62c-7083251eb2a6 | -3.25001 | -51.52252 | 2024-11-17 05:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b55adee-8ffa-3122-98f0-78ec56abc7e6 | -1.53024 | -53.5571 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2126f3b3-5c18-3f8a-aa07-f20ba92d5380 | -3.10983 | -53.74281 | 2024-11-17 05:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75c9c975-7d43-3311-a21e-e3ee2535b784 | -2.41616 | -54.62342 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 13d6ca63-820a-3354-89f7-e91911271b46 | -2.34793 | -47.46895 | 2024-11-17 05:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21c6e6d8-c761-3ff7-ad3c-aee6224c9b8c | -3.52616 | -50.23903 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a710ec1-c226-3a0d-a3e3-8b500fc32f0c | -12.39849 | -57.52398 | 2024-11-17 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d1b36b03-cab1-36ae-8d46-3b368eb4e7ca | -2.9512 | -53.72068 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aac87b17-5860-37a4-9416-c83c42b0f8ed | -2.62197 | -54.15712 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb21b32-fb1b-38d1-bc4f-dac85ebed304 | -1.63956 | -52.66717 | 2024-11-17 05:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 78a681f6-bd2d-37c5-850b-1d600b68895a | -1.37818 | -51.09171 | 2024-11-17 05:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d0efae1-05eb-3c65-ab71-1ed08e3e32b2 | -2.96261 | -54.16464 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4690b978-b09e-3dcb-90be-9446add7e535 | -3.91921 | -46.52513 | 2024-11-17 05:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5deb4326-decb-3826-8e35-1aca32fb6be5 | -1.19836 | -52.03032 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1e1a0e2-35c1-38db-9f35-2b9387e40be6 | -3.33191 | -52.77199 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccc59d94-a044-33ba-852e-06b6314d890a | -2.55963 | -53.9945 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d63749ca-ac98-385f-836a-ecd777dcd0d3 | -1.52811 | -53.55892 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b96c685b-d044-3273-8d7e-17f6dad82e4c | -2.15693 | -50.70286 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c71e00e7-ea98-3230-8700-665a08d7d987 | -3.52875 | -50.24866 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4d24b76-3429-3c20-b007-2e6d8cbcb2b3 | -3.59013 | -50.52948 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77ccb76b-e9aa-3586-a63a-b505cc1a1425 | -2.23368 | -53.60847 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0e54228e-f5cd-3d8d-8e15-c8b203f83ad3 | -1.79675 | -48.4429 | 2024-11-17 05:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f1ee582-3161-36c8-b0b7-eb5f6a31ae25 | -2.86421 | -46.72346 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 783aba55-2cf7-3226-87c2-65be1b2a3cee | -2.26113 | -53.79008 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a928abd-9f76-36f5-b429-1d05083c7cb3 | -1.62871 | -53.29084 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4808d525-21f5-3d6e-b68c-5f74471f8ffa | -3.53515 | -50.25559 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15298578-96d6-31ee-a21a-99afd434c3e2 | -1.13805 | -51.69152 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 926fb256-c4b5-3633-85c8-4099dd30b04f | -1.95098 | -53.33391 | 2024-11-17 05:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e9cc9b-1d21-3648-ae0e-faa3b4ad00f5 | -2.69937 | -49.28771 | 2024-11-17 05:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c653950c-6f3b-3f15-8ce7-a84fa6779184 | -2.86494 | -48.73004 | 2024-11-17 05:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee336941-b70a-37ae-bf0d-13c0c1b82360 | -1.29318 | -51.95511 | 2024-11-17 05:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf6de267-8f9c-3803-b5e1-68b2477cb24b | -3.02502 | -54.09699 | 2024-11-17 05:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b043323a-c911-3f1c-ac59-01db3c2a41e5 | -2.86417 | -46.7219 | 2024-11-17 05:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| df7c02d2-c687-3ab7-b7e1-0756f41048e1 | -1.40005 | -51.08591 | 2024-11-17 05:25:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a97f736-4c57-3807-9ccf-9961d0cc3c87 | -1.20865 | -51.77124 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2f0ba2b-de0c-3d68-b2f9-ce7f0b894c1e | -2.14871 | -46.92807 | 2024-11-17 05:25:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 878c7731-c518-3c0e-afd9-dcae02863d26 | -1.20377 | -51.7705 | 2024-11-17 05:25:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2a736be-660d-39c6-a5ff-25077a073497 | -3.56129 | -50.26138 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5ac16e14-8167-3fa5-90dc-ab19ae36ad8e | -3.58543 | -50.52367 | 2024-11-17 05:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875febc7-0416-3628-a4d3-6258eacda671 | -12.55201 | -57.7734 | 2024-11-17 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af069811-4e20-30ad-99af-2bdc2be4d72a | -2.2214 | -50.51413 | 2024-11-17 05:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b025fdc5-37ee-38cf-9be7-27d3b526787e | -2.80078 | -52.99607 | 2024-11-17 05:25:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README62.md)
