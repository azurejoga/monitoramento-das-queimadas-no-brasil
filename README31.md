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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0557b3d-372d-3b6a-930b-4f61a244a2fa | -3.07028 | -49.53619 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f9a1af41-4d7e-3667-b730-a7dfae572165 | -3.01428 | -53.89148 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e769391-84b8-3608-8ac8-dcdcf62c1925 | -3.07794 | -49.54122 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 49549a96-b96f-3baa-af9b-ef8fb3737d98 | -2.80521 | -54.12336 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e6e5c214-f54b-361f-9199-59686ff1fe8a | -6.07682 | -53.47033 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f6e36c32-a40e-3e51-a8f3-601a95dcfe23 | -6.57543 | -44.14712 | 2026-10-04 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8751be1a-99e6-3509-9a7c-edd8a702e538 | -2.90395 | -54.14086 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f659d4f-51ae-3378-a4c2-f3addb73f0d4 | -3.47577 | -50.09504 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96002f9d-1335-31c5-8975-7decc3f9d9a8 | -3.13499 | -53.74252 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ac7d298-992b-30a1-b2fd-a4a2a50a1aca | -2.79081 | -54.10537 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d7c8b6c-32f7-33d6-90ed-925d49a69e30 | -2.81665 | -54.08963 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a86a84c-2bb2-360f-b3d9-760ea901aee3 | -2.25659 | -51.93602 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a777be23-6cb8-372e-87b9-544aab2ff180 | -3.09447 | -51.10159 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b09b673-c073-3e23-8602-fcc60e6fc3ec | -2.80149 | -54.11092 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4dba3d5d-f9f8-3534-90b6-d1285bc7fb7d | -3.10404 | -50.29672 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87f73795-d62e-31cd-addf-37107bbec3ff | -2.81215 | -54.11659 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0bcb71d-c87b-3a71-aaf2-f1d66dbb3527 | -3.81889 | -52.04997 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dbde398-fe2e-3e73-b58e-c910149d1ccc | -4.15863 | -47.53789 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6657bf4-c04f-30ee-9ae1-f6a57cddb0ef | -3.87076 | -55.80402 | 2026-10-04 04:19:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 9b420154-0e45-3765-acf1-dffca9695e35 | -3.46726 | -50.0937 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 79c98f68-1516-3e43-8659-5fd0fc3ca2ed | -6.2081 | -43.61497 | 2026-10-04 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5359fd2b-464f-3009-b2ee-040918c0adb7 | -3.77421 | -51.40489 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| eabfa4a1-7e64-3807-856c-8efbba624083 | -3.08554 | -49.53837 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c814a8a-e0a6-3e1a-970f-531c949f0a8b | -4.26851 | -50.74509 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fef42939-2d65-32fb-af81-e2efaa10e80d | -4.27187 | -49.97726 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68109fb6-ab14-3c8e-ac77-5acf826bcd9f | -3.1895 | -54.10036 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 310f8e7a-f55f-35f5-bb8d-f46abc600ff5 | -3.1344 | -53.74611 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6993a4ab-c804-3c40-9260-8e2b7f5aed03 | -1.7016 | -50.03261 | 2026-10-04 04:19:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cf9180a-59c9-3b47-88af-909649014337 | -5.12544 | -42.40512 | 2026-10-04 04:19:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0322a4b2-07e6-326a-9656-2e642fabdaa1 | -6.00279 | -53.53026 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c38d4343-1b9e-3712-839e-7c48d223e34b | -5.55155 | -44.21095 | 2026-10-04 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcf7836b-f6d9-37a6-a24b-d611ff45d3ef | -3.08264 | -49.53818 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77df3f08-8383-3aa7-b282-b635366e43cb | -6.21205 | -52.79848 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6675ece0-f565-3e54-a619-67951c60ca64 | -4.29263 | -50.27516 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e23d2b7a-eb12-3833-89a6-3ad0447dd9f8 | -3.11304 | -53.73893 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d9a33ed3-08b6-3112-b3ab-9407e1b76d25 | -4.9669 | -47.97588 | 2026-10-04 04:19:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03a8e061-5632-3523-a902-d9e5c0e5e266 | -3.9239 | -40.74344 | 2026-10-04 04:19:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0c8c8a83-5bc1-3651-9f5f-c62b4f38c109 | -3.23754 | -43.14299 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0730b79c-c278-3212-9a6b-8e6bde263a22 | -5.26764 | -43.62885 | 2026-10-04 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bb214d7-1a00-34a5-bda2-744c317f2eb5 | -5.63356 | -50.02857 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74b73235-4b75-3ee8-9184-be83d2e29dfb | -4.2763 | -50.26847 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d9e3556-4577-3c1a-b1c8-37dc0654e0e2 | -3.04458 | -54.22215 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ebf25972-1189-31ce-9b1b-d3ae30ef3867 | -4.2861 | -50.26196 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1707a0f1-24e2-307a-865c-0685f81665bc | -3.51098 | -54.61293 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2c09d903-a116-3fd4-b1d5-3fd4e067ddb5 | -4.81452 | -49.28788 | 2026-10-04 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c25c35e-9c8f-303f-b896-bc94301d6d20 | -6.00009 | -53.63649 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1628f96d-1cc1-3529-8c09-cbd46d10b881 | -5.58477 | -49.01505 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cb2d907-0d99-357a-9b2e-5f2d35d4cff5 | -2.61418 | -51.21513 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78e013c2-8300-34be-9fb9-04f66970acd8 | -1.86758 | -50.62566 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc501bc4-b04b-3d03-93be-529e1f559f93 | -4.4704 | -50.96965 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 201bd53c-0efa-38c0-893c-b3a92deb85ff | -3.10472 | -50.29258 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8fc8799-30f6-3dfa-8669-e6c9dfd6d0cd | -3.05915 | -54.16906 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e995f2d-0baa-3ec4-a693-c73d35b9429b | -4.98178 | -46.04141 | 2026-10-04 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bfc078cf-2b21-3e8a-b44f-155a2b2f354d | -2.82037 | -54.10209 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d099164e-b1db-3d56-844f-5c8d990df5d6 | -5.36566 | -44.94726 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43009cac-6ff6-3efe-9327-887d3e6bbc4a | -3.22201 | -54.3086 | 2026-10-04 04:19:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37f55e62-932d-33ad-8416-300dc0a05d08 | -4.53086 | -49.69466 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| faf5eeea-80d5-3de0-ae8d-ea0f169b4b6e | -2.816 | -54.09349 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5638e800-dcda-32c1-a5b4-54cb4bc87fd2 | -2.8967 | -54.08066 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3c86434-6fd0-3aa2-9c33-dabed91a6f58 | -3.05477 | -54.16043 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7d053c8-44c7-3fb6-8c58-46d4e3c20614 | -6.62569 | -41.77159 | 2026-10-04 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aa63d17a-446f-3b52-829b-b7b19d0289b8 | -3.27274 | -43.37698 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1350d31b-1bfa-3e63-8342-2685e76210bf | -4.25978 | -46.36169 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 250a1916-3b35-3bfa-a6be-18f719f613b5 | -3.12891 | -53.74521 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fc202a7-47dd-3cfc-86b8-a7e6cc036973 | -2.94668 | -54.12818 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9766ac60-81d6-3d09-a3ac-561aab1c2596 | -2.56342 | -48.2483 | 2026-10-04 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3152a14f-0874-35f5-8808-3c4ec49940c4 | -3.12158 | -51.59592 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5e79452-6419-39bc-b299-fdb04a22f2db | -3.07615 | -49.52577 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c88339f3-8741-3b11-a880-3d7b7aecabfa | -3.74807 | -47.15101 | 2026-10-04 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1112e4d4-381c-305d-9cd1-af298dc537f0 | -2.81022 | -54.12816 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f6e81a20-7d3e-3a78-9887-273c5ffdddd5 | -3.16963 | -54.08105 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c517f31-594f-37ad-a820-34d3f10709a4 | -6.57489 | -44.15061 | 2026-10-04 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2f1d4f0-b4bf-392c-abff-4447e62922ff | -3.18138 | -54.07964 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d796ab29-bf34-311c-b7cc-054c96b71e32 | -2.82087 | -54.13398 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 095d0964-42c5-3527-b305-66ac8aa6cd36 | -1.62748 | -55.01611 | 2026-10-04 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1039d5b7-3d99-3d53-91c4-8045e5d1ce01 | -1.46368 | -49.46927 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d5e1c5c-c69c-3f82-b145-9fe71d3d6152 | -6.08093 | -53.47717 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbd1e473-714b-3961-98ba-937e77d33354 | -5.85968 | -55.70798 | 2026-10-04 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebea7fc9-3689-389b-96a7-d1155bc5f1aa | -6.21109 | -52.80413 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e22ad68d-4e5b-3e47-8bbf-55d3176b72e3 | -3.28431 | -53.83461 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94337e67-38bb-3f0c-b90d-4dbe2b78fd6e | -5.74149 | -45.15138 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| feb26219-f908-3eb5-a8c3-22cb8c07238f | -3.0744 | -49.53683 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fa35749-e8de-3cc9-aa3d-4ed762cbeabc | -2.79146 | -54.10151 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57185ea5-f4de-3daf-8c32-16fef02c5262 | -3.08143 | -49.53768 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78db7c70-aa1b-34bf-82f7-4bbd5d6f090d | -7.27807 | -49.25751 | 2026-10-04 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a58edeb9-1cb3-35fe-a42f-0dd860b11f9f | -3.08021 | -49.54507 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5217ded-03c6-3b95-b774-75a28aaf3c90 | -3.12031 | -53.72904 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 6f7d5b0b-362a-334d-91ad-f746f8113c92 | -2.11263 | -48.99791 | 2026-10-04 04:19:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d1373a7-a6db-32fa-87ef-bc20af172945 | -4.27762 | -50.26057 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54adfd74-ecf4-32d7-8b3c-e20f96df4d0f | -3.18818 | -54.09742 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0767e41-758a-3be5-9cf4-c4a3be09a756 | -2.59356 | -51.85425 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| aa9fb0d9-7f9c-3a25-993a-eb345648c398 | -6.20621 | -52.80322 | 2026-10-04 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce2dbb24-8a13-3d59-96ea-18a70aac7f39 | -2.88764 | -54.13426 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6aba6f7-a0fa-3bdf-96f9-fd1af09d3446 | -4.204 | -53.46389 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e71ab4b7-a8a0-329d-9396-4bfc893a1d6f | -6.61675 | -41.5555 | 2026-10-04 04:19:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59cff51f-f756-3b19-9d14-f46d846ed56d | -4.25782 | -50.78297 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7eeedda-50bc-3fe4-87ef-fbe6ca49980d | -1.90509 | -47.01609 | 2026-10-04 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f55451d0-a240-3d89-9c82-8c73d2a242a3 | -3.07204 | -49.5251 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40413687-f675-3b12-abc1-a1a38ba0c603 | -7.12564 | -46.62786 | 2026-10-04 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a113c1f7-4792-32fb-8c0b-0538d232245b | -3.27552 | -43.38096 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README32.md)
