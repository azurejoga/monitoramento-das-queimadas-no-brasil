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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edc3c09d-4194-3e68-923d-4ac370fdaaff | -3.0158 | -45.3679 | 2025-10-16 04:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 6b7d1815-9ce4-3d69-afea-a7c118417880 | -4.6626 | -44.0832 | 2025-10-16 04:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 272.2 |
| 8fdae8d7-5755-3a54-bdb7-debb81da8e61 | -4.3687 | -43.3838 | 2025-10-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 383.2 |
| 430f16d4-1b1c-35ff-bc3e-695d9a814ee2 | -4.1161 | -48.0136 | 2025-10-16 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| d48f0ead-5e36-3804-8a1f-4e45ebaf060c | -5.8799 | -43.8844 | 2025-10-16 04:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 61e1665b-91e2-3bcb-aafb-5218d9fff2c1 | -4.0976 | -48.0144 | 2025-10-16 04:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 8c00ff82-80fa-39c1-8e85-891fbb600983 | -4.3872 | -43.406 | 2025-10-16 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 345.2 |
| 18b5dc73-7aa4-3055-93fb-fcbcf9c89263 | -8.4717 | -44.1746 | 2025-10-16 04:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1bbee7b0-36b8-3838-b228-4e49e8f18479 | -5.4762 | -42.9367 | 2025-10-16 04:30:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| f07cd06c-365a-3036-be40-4fb7d324d90c | -4.116 | -48.0352 | 2025-10-16 04:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8afa465b-c063-33ec-a778-7efe9d9f1619 | -4.3685 | -43.4071 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 4d01e1f5-250e-37ef-b80d-dea07dc42151 | -4.6811 | -44.105 | 2025-10-16 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 153d003d-d61b-3001-bbd3-f685ee5cb100 | -6.1723 | -40.8954 | 2025-10-16 04:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 6dd7d5ae-6d3d-396a-b63d-f3d499ab6704 | -4.1161 | -48.0136 | 2025-10-16 04:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 75ffa96d-ccc9-3f3b-81ef-23e84891ef5e | -4.3874 | -43.3827 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 483.0 |
| 0fe5c2a5-1df7-336a-8d26-d698a17aaf82 | -4.3872 | -43.406 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 77421b4f-45e1-31a5-b3cd-a390ba2b7ca9 | -11.4368 | -44.1641 | 2025-10-16 04:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c1e1d7fd-2826-3cc3-9b94-ffeaf5d3cf50 | -6.1534 | -40.8971 | 2025-10-16 04:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 986617f5-91ac-38b5-8c58-5927aab4bdbf | -8.4528 | -44.1767 | 2025-10-16 04:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6ecdc328-99a3-3a89-9d25-bd1a68e10ef5 | -4.3687 | -43.3838 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 353.6 |
| 9c2160a6-861a-3826-8e6b-caf786fa94d6 | -4.4061 | -43.3816 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 17793224-f727-3a2f-8b10-defcf7e42dcf | -8.4717 | -44.1746 | 2025-10-16 04:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3b7118c9-74bf-39e6-bd23-e5eefeb7b123 | -5.6821 | -45.0893 | 2025-10-16 04:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 04359ede-9be6-3480-8ec6-4e4ea017af55 | -4.0974 | -48.0361 | 2025-10-16 04:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 09cf6d2d-eccc-37de-8b67-bc30dfcb1513 | -4.3689 | -43.3606 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c6e528e0-b4f1-36d8-b8f2-78acf457ead9 | -4.6813 | -44.082 | 2025-10-16 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 22f6c672-3dda-3fba-93b3-ab10a331d016 | -3.0157 | -45.3903 | 2025-10-16 04:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 22f9b28e-1546-363d-a0e0-b45e29c0fde3 | -4.35 | -43.3849 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 01f8777a-4a0f-31cf-86d2-321c4e411f90 | -3.0158 | -45.3679 | 2025-10-16 04:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 8862b110-dd07-391d-aa66-46565f676dd7 | -4.0976 | -48.0144 | 2025-10-16 04:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 5fa1ac9c-63d8-3d3d-86bb-c205410d51bf | -4.4059 | -43.4049 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a1ae7bf6-8e38-33ca-9375-9b4be987e133 | -4.6626 | -44.0832 | 2025-10-16 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 416.0 |
| bea322a8-3d35-3e9d-8d84-d8a8c067f931 | -4.6624 | -44.1062 | 2025-10-16 04:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 529.8 |
| ba924795-361d-39ae-a282-1c2d8033e894 | -7.3955 | -39.6845 | 2025-10-16 04:30:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 68270b32-1de9-3298-88d8-bbccd96e1704 | -4.3876 | -43.3595 | 2025-10-16 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a61e9b0d-7f8c-3758-9ff4-e4d827808752 | -11.4372 | -44.1407 | 2025-10-16 04:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 05f66d3c-5ed6-309a-8bdf-87ea2b866fff | 1.8023 | -55.88654 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fc2e94f-b4fa-35e9-addb-9f779b588150 | 1.82625 | -55.74078 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a25853-2ba5-3398-8a84-b0c52358ec05 | 1.22392 | -51.0335 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7a871c95-41c5-3942-83be-5c7c7234c341 | 1.8117 | -55.74597 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 166a4fba-bd8e-3960-ae33-82827e61cf97 | 1.81143 | -55.88207 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e67d31dd-6615-3c4b-a505-d6b83c6af922 | 1.82385 | -55.7588 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b959d8d5-08f9-3683-bb86-403b0d5ce173 | 0.99198 | -51.08408 | 2025-10-16 04:36:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73ab4f14-a889-3336-bee5-2937ab6092ab | 1.82298 | -55.75302 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3110faa9-7778-3fb2-9168-45ae69675436 | 1.0646 | -51.01769 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| de813091-8a2f-398d-82fe-a5a0aff66ffc | 1.79934 | -55.73598 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e0d4c02-5fb2-38da-9ef6-9011187cddf1 | 1.83492 | -55.7306 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c30929ee-ebd0-348e-9609-54d1bf030e2e | 1.05806 | -51.12595 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eaf72f7-2ed2-32ba-9394-46cd544a64a0 | 1.05734 | -51.02684 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f880361-676f-3b22-b09f-7b2568f4ec9e | 1.83297 | -55.75148 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5640c471-10ac-34bb-98f6-4337ee7fbb20 | 1.80688 | -55.88279 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1af1056-c20d-3930-ba5b-f90341c897ac | 1.86199 | -55.67416 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7f496bc3-3d4f-3389-ac5c-c59f59d17a01 | 1.0478 | -51.03691 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bab764ac-346a-323c-9eb0-ea8970842958 | 1.06688 | -51.01678 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc6224de-e755-334f-9869-8d176100d3fa | 1.82168 | -55.74442 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fb26f59-401d-3840-93b7-0ad2b82b84c1 | 1.86696 | -55.67339 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9007bd52-e62c-3019-828b-97c81396387b | 1.83449 | -55.72774 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 036a0542-8d22-399a-a434-f4ed9c2d2994 | 1.05509 | -51.13074 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10f98fe4-a54c-323a-b716-69434a8f9ec5 | 1.06622 | -51.01259 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8109325-495c-3d7e-af03-c30554e6414e | 1.04483 | -51.04167 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cbae0bff-0356-3135-b951-e75260910131 | 1.06758 | -51.01293 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7a468b18-63c1-30ef-8240-13f3b584695a | 1.78617 | -55.7498 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b00b50e5-d797-3315-91bc-e80aeab28f76 | 1.75791 | -55.76545 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f4d91e5-1d63-3ca8-bdd8-33a85259f425 | 1.05076 | -51.03216 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa0fcb7f-d866-3d04-b98b-40ac89836772 | 1.81188 | -55.88179 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| feefdeb8-9b58-314e-bdf6-917aa74f31f3 | 1.82993 | -55.73138 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb5034e7-6bd7-33df-ba61-a08ace7d5d2b | 1.81755 | -55.75092 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dac9687-9760-323a-a03a-17d123b56c78 | 1.73819 | -55.80396 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3a2b8dd-b68c-3442-b66f-271967dd50a9 | 1.05438 | -51.0316 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 14de9b75-3887-3b02-8d2b-c21376bb1625 | 1.81603 | -55.94152 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf2a409e-3feb-3932-bed4-63903e5a30b8 | 1.83037 | -55.73426 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66cf9024-78af-399e-8d18-4254dabb718b | 1.23052 | -51.02814 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a667abd-d5e5-34d4-aaf5-d1b7454b5ceb | 1.06237 | -51.12965 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c10d3ca1-173f-311c-ad06-d1d424126df1 | 1.80553 | -55.87411 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 741d43a2-eb7c-3fd3-8702-c5bd783173e1 | 1.89527 | -55.89023 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a92d717-f544-32c2-8252-e4cdfc5f2f4d | 1.06097 | -51.02628 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ad4224f-a3f0-3052-9ec7-06e129726382 | 1.84599 | -55.70269 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 120529c8-ddd1-397a-87b3-a5120597f185 | 1.82711 | -55.74649 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2407f3b-6c87-3b63-87b0-9ce635887995 | 1.75013 | -55.78146 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9537a749-f4a8-3948-9ef2-ab0e594bee29 | 1.06326 | -51.01734 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4e664d1f-49d8-36b7-bb3c-23860ea294c1 | 1.83861 | -55.72124 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2ecf80f-d24a-37a7-a670-270ed7a196f1 | 1.83405 | -55.72487 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 571a5f7f-75e4-3fe8-90b7-d7edb002aaae | 1.80598 | -55.877 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03e2b357-0056-3244-9571-a73b73fca143 | 1.81798 | -55.7538 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afea31ed-59e3-395c-966a-f8feafd5cc93 | 1.82841 | -55.75516 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffaf6c88-1b6d-30ea-942e-7c01e1d7e0a5 | 1.74688 | -55.79373 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b524e460-d351-3c6b-bf2c-18866c9ab180 | 1.8948 | -55.8872 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc871362-965f-3d1b-bc6b-0559c39cafdd | 0.9986 | -51.07876 | 2025-10-16 04:36:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a90ea813-62fb-328d-b487-c79f9877fc3b | 1.05801 | -51.03105 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e684e586-5158-3345-8aa7-ed508e44d873 | 1.82798 | -55.75227 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c268ea3f-6b5d-366a-abac-cc322df05ae0 | 1.81051 | -55.93935 | 2025-10-16 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c24664f-a953-39a0-b93e-c91cb5fdd690 | 1.82341 | -55.75591 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 882fccbc-131e-3a76-a457-d60847889a31 | 1.04846 | -51.04112 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78cd5c0a-e4e2-32f8-b886-bdfdc2608c5b | 1.8308 | -55.73714 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f67cbc22-edd0-3417-88b1-32116d2c5343 | 1.22326 | -51.02926 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89ea1322-a0d0-358c-a264-be3e4e0c4caf | 1.82255 | -55.75014 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 600b3256-e373-3ca8-9030-6f0c1bee1697 | 1.8356 | -55.76886 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd594837-ad5e-38f5-8e94-8b658db1282f | 1.05142 | -51.03635 | 2025-10-16 04:36:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2dfa4af0-032e-3a1f-b034-7b6a61f6c086 | 1.75835 | -55.76832 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93f3b25b-f8d9-3957-a9a6-a52548b53b98 | 1.7432 | -55.80318 | 2025-10-16 04:36:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README42.md)
