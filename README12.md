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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b0cebaf-cf94-3409-94f8-0f80635f741b | -19.02377 | -42.03634 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cfcc5e0e-f6f7-3d65-a487-3989e281507d | -20.12186 | -42.40135 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 94d0b8e8-521e-3042-83d3-d755dc1d3900 | -19.02442 | -42.03325 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 577d94f0-ef03-3612-979d-5aa38d03a087 | -19.83476 | -42.8863 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3145cc05-22c0-38dc-abcd-286e50947dc4 | -15.14674 | -46.62507 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 79ab69f4-3842-3e9e-a9d6-4ed17f2783b2 | -14.76132 | -44.96199 | 2025-10-28 03:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b527cfca-a261-38fa-acf6-1f8d191655e3 | -14.7601 | -44.96761 | 2025-10-28 03:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9ac21db-5169-338c-90a7-45fbd42653c4 | -18.73847 | -43.70861 | 2025-10-28 03:25:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 314e69b3-854a-36a5-af79-3f36acfa53c7 | -18.1423 | -44.17163 | 2025-10-28 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb177520-efd4-3719-9ad8-f426b959a74f | -18.14276 | -44.17253 | 2025-10-28 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37f61432-deaa-3ec2-ba51-98298bd47dfb | -15.14107 | -46.59883 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3daba84-9a8f-321d-8255-b3352779719d | -19.82895 | -42.88814 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5c4b2587-9929-3663-8ef3-e9ab6b9293a7 | -15.15475 | -46.58976 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 8e93f0ac-3a4a-3e87-99c8-4c64c429aa7a | -20.13922 | -42.41859 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bb968f6e-dea5-38c9-b7b1-429f476eb4e9 | -15.15131 | -46.60496 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 90bdc64f-f748-3d6e-974b-140db4916b32 | -18.15068 | -42.45152 | 2025-10-28 03:25:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 359936fd-eb77-3690-b239-e4c3332b5a55 | -19.02465 | -42.03488 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ca1f4aab-9f07-38e0-8e0a-652cad0f1a57 | -16.04738 | -43.53747 | 2025-10-28 03:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1000a44-e26f-39da-9a4d-1e6cdf0c7f36 | -20.14555 | -42.40844 | 2025-10-28 03:25:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba5b7ecf-c99e-3692-a640-0d83782fea1b | -16.14863 | -45.10412 | 2025-10-28 03:25:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcbf1099-184b-30af-9840-8b868157870d | -20.12256 | -42.39798 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| d0e9e69a-4c4d-3b21-8be8-e61c6570d5aa | -15.14969 | -46.61208 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9cbb631f-b9dc-3874-a677-94e2ddd583a2 | -18.05604 | -45.10091 | 2025-10-28 03:25:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1de4dd43-fcbd-3e86-8cf3-598a11e1baa1 | -18.60612 | -44.26135 | 2025-10-28 03:25:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4150cae-c158-36e7-893a-86d42f35361f | -19.02941 | -42.03436 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3103869a-45f5-3eda-86ca-a332fc626d1a | -19.01966 | -42.03377 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8ef64db0-3b30-35f7-afae-eeb983083a06 | -16.82323 | -43.113 | 2025-10-28 03:25:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb20ab56-e896-3c83-b16f-fd5c14d27251 | -19.02528 | -42.03177 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e7a44b63-5f2b-3459-9021-17f52c8d2919 | -15.15302 | -46.5974 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 60b78ba5-8a0e-38df-989c-63e08933df5e | -15.19736 | -43.78299 | 2025-10-28 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d85b31b3-1782-3f12-942e-b43f3557af9c | -15.57584 | -43.20243 | 2025-10-28 03:25:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2e84ee57-f13b-3b3e-8b6e-5c9084e7f076 | -17.62489 | -44.00042 | 2025-10-28 03:25:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39f067d7-3112-3de1-bcb4-7fdd3c6af9df | -18.5311 | -43.47314 | 2025-10-28 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 91831261-3d20-392e-9c80-a23248b85882 | -16.70506 | -42.88289 | 2025-10-28 03:25:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c48be1b3-cc1b-3716-92b5-39e4cc5abf29 | -18.73763 | -43.7125 | 2025-10-28 03:25:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 697130b4-f6c6-3b53-9786-b63132eafb2e | -16.70578 | -42.87948 | 2025-10-28 03:25:00 | NOAA-20 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffd2388f-1d55-34f1-b970-e575cc82b421 | -14.94041 | -43.4435 | 2025-10-28 03:25:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 018c9052-5bc1-3c22-89e7-c5787741dc41 | -15.13817 | -46.63026 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccccc5aa-2cff-39c6-9e14-2a5c38e2296d | -20.1269 | -42.40226 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 79b0ee10-2b6e-3922-8107-8f4446906912 | -19.02875 | -42.03751 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 32a0ecf0-4431-3d34-8f4d-1ae69ce2140a | -19.83571 | -42.88304 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f16b78ce-3d60-348b-a7a0-419f37f4d517 | -14.81115 | -46.71456 | 2025-10-28 03:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36e16e4e-a030-3003-af8b-c5ba69c034a8 | -19.82965 | -42.8848 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7c8d8a9d-34d8-3aa7-90ac-5fcf170cc361 | -3.0344 | -45.3672 | 2025-10-28 03:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 03502436-f9ee-3784-8b64-a5d0b2e530bb | -11.2794 | -45.5281 | 2025-10-28 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 219c3652-cb18-3431-9d8e-932b375a6fcf | -3.0158 | -45.3679 | 2025-10-28 03:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6f757645-fb98-30f5-ab5a-d614bce813ae | -7.9461 | -45.5108 | 2025-10-28 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6f8d4142-befc-3141-a3f8-e2f3fde40f35 | -7.4541 | -49.4018 | 2025-10-28 03:30:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 4ec74a6c-8199-3fa8-81eb-80b4293f640c | -11.299 | -45.5025 | 2025-10-28 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b032202d-b47f-32c6-bc66-39591fe87295 | -11.2798 | -45.5052 | 2025-10-28 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| d460a26a-b7e1-377b-98ed-f25ab00b666b | -7.9693 | -46.7423 | 2025-10-28 03:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 2ee4ceaa-bec8-3d31-8259-a2cb200b68d5 | -4.4632 | -43.2386 | 2025-10-28 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 31cb3479-5350-3c70-b0a2-baf856731fda | -15.155 | -46.6062 | 2025-10-28 03:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 161.2 |
| f226a511-9304-3a97-a9c3-6aac68c3b661 | -15.1359 | -46.5867 | 2025-10-28 03:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 92a6afb9-b8bb-367f-b569-a1e88f775192 | -15.156 | -46.5602 | 2025-10-28 03:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 842d77fe-c0e9-38c9-b832-7848df139761 | -15.1555 | -46.5832 | 2025-10-28 03:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 697.3 |
| 9a8c1e81-7d30-3c27-b525-0b717694c68c | -15.1751 | -46.5797 | 2025-10-28 03:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 459981f0-287f-38dd-af07-058ceaaa4245 | -3.0158 | -45.3679 | 2025-10-28 03:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 4bd9e316-f0bb-32e4-bac9-55e4b3ac31c3 | -7.9461 | -45.5108 | 2025-10-28 03:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 0441494e-15bd-3a43-b574-cb5e208cd0b1 | -15.1751 | -46.5797 | 2025-10-28 03:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| aea13d56-285a-3304-b57f-73d73ca2daf6 | -7.8035 | -46.4681 | 2025-10-28 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| de37aab4-084e-38fd-91c2-305493b94db7 | -3.0344 | -45.3672 | 2025-10-28 03:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 33ed993a-ec2c-3d48-b188-3ac4bb940b76 | -15.155 | -46.6062 | 2025-10-28 03:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0666b192-256e-3c3c-9412-ff0466dcb2ff | -11.2798 | -45.5052 | 2025-10-28 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| ce937214-e8e3-3d5a-b73b-1ee34a4eea43 | -15.1555 | -46.5832 | 2025-10-28 03:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 245.7 |
| c133fcd4-0904-3f86-b2d1-99831dea5eac | -7.4541 | -49.4018 | 2025-10-28 03:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8b4e8673-2656-3c16-8d28-3c071530fadd | -11.299 | -45.5025 | 2025-10-28 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 5720e376-c1ef-3fdc-ba6a-c90b07e7fc96 | -7.8223 | -46.4664 | 2025-10-28 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 179527ad-734a-3f1b-8313-cb39f571d9d4 | -7.9693 | -46.7423 | 2025-10-28 03:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4cb9620a-3329-3826-8cad-f904d24f665f | -4.4632 | -43.2386 | 2025-10-28 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ad8f3339-bec2-3993-b66e-dcf75e0441a0 | -7.9691 | -46.7646 | 2025-10-28 03:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a929ab98-22a3-3d49-941a-8e6f7543a3e7 | -15.156 | -46.5602 | 2025-10-28 03:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4eec65bd-3daa-3e0f-937d-cc55aff39e8e | -3.0157 | -45.3903 | 2025-10-28 03:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fb17a1b4-b4a1-3a4b-b01b-92b289e22ed1 | -7.9693 | -46.7423 | 2025-10-28 03:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| f138d48b-eb50-38b4-a702-98ac4322c610 | -10.5872 | -49.7998 | 2025-10-28 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 09fd3826-79fb-3fab-92d2-d8f397ce0f29 | -3.0158 | -45.3679 | 2025-10-28 03:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 2c21c624-1f8b-3a25-a70e-576dbd43effe | -7.9691 | -46.7646 | 2025-10-28 03:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 72d1fb6a-1ffd-372d-8777-51cd7cebbd2b | -3.0344 | -45.3672 | 2025-10-28 03:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 33156ebd-7dcd-3302-b3a3-46b7bf5d773b | -13.6319 | -47.0438 | 2025-10-28 03:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8a71a1f2-88e2-325f-904a-a9a4bcfa6551 | -9.5676 | -46.9587 | 2025-10-28 03:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| f333a325-fc33-3124-8ea3-0aa574738984 | -13.6324 | -47.0211 | 2025-10-28 03:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 4dd85a1a-cc06-3e62-8b70-e7dfb6c50875 | -11.2798 | -45.5052 | 2025-10-28 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 687a1bb1-0e90-32ce-8cc1-3ad4c414b3aa | -15.1555 | -46.5832 | 2025-10-28 03:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 0a692de5-a2da-33ca-be33-3ae85d3bdf93 | -7.4541 | -49.4018 | 2025-10-28 03:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 21e15438-8728-3035-964e-9fe1a8a88475 | -7.822 | -46.4887 | 2025-10-28 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 31fed662-b630-327b-a156-8f72a40ffda4 | -7.8032 | -46.4904 | 2025-10-28 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a1e0145c-319c-360e-b3e3-3e4ae4f36669 | -9.5673 | -46.981 | 2025-10-28 03:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ed6a8033-1a15-34ca-8d14-5c0bda99d167 | -4.4632 | -43.2386 | 2025-10-28 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7f5f4011-f99a-3bd4-87d6-a761e1287174 | -3.0157 | -45.3903 | 2025-10-28 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 78d67d19-7ab6-318f-a84f-a996b2bf548c | -11.2798 | -45.5052 | 2025-10-28 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| b493985c-8e6f-3d32-b339-ca261d90f37e | -3.0158 | -45.3679 | 2025-10-28 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 143.1 |
| cd900ff6-2802-391d-85be-8c7b1f242906 | -10.5872 | -49.7998 | 2025-10-28 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e40cb608-6b9c-3d77-accf-7b2a0af35bcd | -11.299 | -45.5025 | 2025-10-28 04:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| e4d82465-5ac0-3090-b2c4-882a958cceab | -13.6324 | -47.0211 | 2025-10-28 04:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a56d22f4-4934-31bf-878a-ebc5097ef20a | -10.5875 | -49.7782 | 2025-10-28 04:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f56bca1d-0864-31a9-ae0f-cde56ca2a800 | -7.9882 | -46.7406 | 2025-10-28 04:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 422f580e-b413-358a-8bb4-0403cceb04ee | -7.4541 | -49.4018 | 2025-10-28 04:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| ca89fd45-f0a7-3c51-8215-eac4ba32ead6 | -15.1555 | -46.5832 | 2025-10-28 04:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ccedf80a-17fa-3928-9a93-2305f0a8a06e | -3.0344 | -45.3672 | 2025-10-28 04:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 115.7 |
| b01f282a-6ec1-35e9-9d31-183268bf0d65 | -13.6319 | -47.0438 | 2025-10-28 04:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |


[Clique aqui para ver as próximas entradas](README13.md)
