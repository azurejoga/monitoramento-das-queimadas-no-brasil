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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cec3d724-d1dd-3bac-9dbc-1cf39fbe5c9a | -3.72307 | -41.6951 | 2024-11-06 00:17:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 044415cb-ca75-33c1-a6b7-7bdd9e66300c | -6.75709 | -35.25255 | 2024-11-06 00:17:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 10.8 |
| bf7d7a0c-dbcb-3671-ad52-b71bec5ec921 | -5.02727 | -43.60091 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 04d5380d-1b4c-3e05-8fd5-1d4caf120fba | -4.1311 | -43.57902 | 2024-11-06 00:17:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d669bfa0-547e-3931-907b-a5c541c23d34 | -6.11073 | -43.99211 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 92a3cc86-d5dd-3935-b458-200d4fabbdff | -6.50383 | -47.47235 | 2024-11-06 00:17:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| ccccb85d-0b34-37e2-b313-267460b0bd48 | -6.6723 | -37.4604 | 2024-11-06 00:17:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 9234eea0-d381-3c3d-ad1f-ff6b7fd990f6 | -3.71359 | -41.69638 | 2024-11-06 00:17:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| 52b099cc-0372-3a1f-b4c0-e58620ec4912 | -2.266 | -46.46545 | 2024-11-06 00:17:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| df3d9e75-b000-30bd-a2e2-5af289194da0 | -5.67192 | -45.95878 | 2024-11-06 00:17:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7a1402c8-b36b-3c9f-a450-7e6f3a3d3707 | -8.50746 | -42.09277 | 2024-11-06 00:17:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| dbf4ca7e-0241-3908-a94d-f234e6f462bf | -2.24229 | -46.49066 | 2024-11-06 00:17:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c45a32c7-9e7e-3d55-9df4-be8a61c38c49 | -6.49791 | -39.97583 | 2024-11-06 00:17:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1fb28f66-aa40-3474-ad46-2678f3842129 | -6.51324 | -44.69709 | 2024-11-06 00:17:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 81145d6c-44da-3359-9afe-31a1ad6a3f20 | -7.01616 | -39.99555 | 2024-11-06 00:17:00 | TERRA_M-M | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| de4c05db-4b95-3b20-87d5-8fae2a748f73 | -3.72167 | -41.68486 | 2024-11-06 00:17:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 93f915fd-8206-3827-b4df-e64ca60a73e5 | -5.65766 | -39.75927 | 2024-11-06 00:17:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e3d3b98e-09b3-384f-9ace-bf6620d3339b | -5.79236 | -36.58313 | 2024-11-06 00:17:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 3bc23f03-7ac1-33b4-98d5-a8e58aa326cb | -4.09819 | -44.27523 | 2024-11-06 00:17:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 3c6beb28-8a8b-30c9-ae17-d6a5fe0b9e62 | -6.48765 | -39.96788 | 2024-11-06 00:17:00 | TERRA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 85f79017-76b0-3da6-b7d9-4a7103f858e5 | -6.10663 | -43.9603 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4cafc81c-4ce3-3d5e-a2b2-e5cd4bb48244 | -6.52135 | -34.97719 | 2024-11-06 00:17:00 | TERRA_M-M | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| fd601e66-56bd-32f7-9fb2-ce82321c9ef2 | -6.7845 | -37.53505 | 2024-11-06 00:17:00 | TERRA_M-M | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| fc218463-4d38-335d-a3b3-aa1a9ec6bc31 | -6.85491 | -38.89563 | 2024-11-06 00:17:00 | TERRA_M-M | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6fd4a162-24f7-3cc5-b7ef-5b3359d1c376 | -6.49206 | -47.50389 | 2024-11-06 00:17:00 | TERRA_M-M | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 395.1 |
| bed3f047-365f-343a-8cc6-65b9afab23b3 | -7.79093 | -40.27369 | 2024-11-06 00:17:00 | TERRA_M-M | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c1e434ea-cfea-3280-b946-269a5b729e5d | -6.13183 | -43.97293 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 7fe736a6-58f1-3d95-a3d0-ea96d9e4c5e3 | -7.48466 | -34.83279 | 2024-11-06 00:17:00 | TERRA_M-M | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 88fd0bd4-3f62-31a0-85fe-7345175829ba | -5.63214 | -44.17327 | 2024-11-06 00:17:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3d0fc773-ce41-3489-8153-4bb38713d17f | -6.13744 | -42.54421 | 2024-11-06 00:17:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| e8414d9f-bec2-35c9-8d3b-ae8c3736daf9 | -8.49879 | -42.10704 | 2024-11-06 00:17:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5aae8145-ec69-34e1-b10e-70f17b8bc880 | -3.83827 | -44.13747 | 2024-11-06 00:17:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d9a1676f-cb10-30f4-b866-37d6f25a0b82 | -6.5232 | -34.98953 | 2024-11-06 00:17:00 | TERRA_M-M | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 28.1 |
| 59c5fe47-9461-3229-bffc-0dd1ff271664 | -7.52412 | -40.14625 | 2024-11-06 00:17:00 | TERRA_M-M | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 717ed1f2-2d26-34b7-be59-311880a493df | -5.47878 | -43.194 | 2024-11-06 00:17:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 95c97703-e92b-3c38-a291-09658cafa166 | -7.05036 | -35.22652 | 2024-11-06 00:17:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| dbd3727c-1b3b-37a2-9a66-998ec013b9ea | -6.14342 | -43.97145 | 2024-11-06 00:17:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 88a40fa0-67ea-3261-abd5-7c481b76b358 | -7.50181 | -43.84927 | 2024-11-06 00:17:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| eed26f77-4cfa-353d-8782-19f4cebc649c | -5.98772 | -45.3747 | 2024-11-06 00:17:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 7f3d0388-81b3-30a1-9cb4-b923762b805d | -6.75018 | -39.26081 | 2024-11-06 00:17:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8274f14c-3918-39fa-abd3-dc17f414c55c | -5.32311 | -43.07849 | 2024-11-06 00:17:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 691eeaaf-5138-3b56-90c4-00066f21fbf3 | -5.7938 | -36.59327 | 2024-11-06 00:17:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8ff4fc7d-1159-3b6b-b128-51f94e1a755a | -6.28468 | -43.38507 | 2024-11-06 00:17:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 38b9f3a5-73c7-3c07-9eb7-96264e9ada98 | -5.93436 | -43.77621 | 2024-11-06 00:17:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 24ad93c8-5959-3e6b-9828-e56612707cf9 | 3.6184 | -51.3162 | 2024-11-06 00:20:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 91.8 |
| eda4e729-8622-36b2-b587-0503d200b2d8 | -3.0023 | -53.4434 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 1fdf6b0a-4b43-3130-a83f-33cdd5fccbd6 | -6.1416 | -43.9563 | 2024-11-06 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7e1df5c5-2261-3770-9629-749e59cf1e17 | -2.6131 | -54.5381 | 2024-11-06 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d9985760-653f-3d1e-82ef-af93fa3ee50b | -3.7255 | -41.6748 | 2024-11-06 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 08199628-d2c1-30c7-9e9d-0000b7c55608 | -3.5304 | -50.3597 | 2024-11-06 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 228e4288-21f8-3a06-a72c-d0f48e8029ab | -2.8064 | -51.5061 | 2024-11-06 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| ce38e84f-9b19-3b36-8a1f-f6b34b86c313 | -3.9669 | -48.1716 | 2024-11-06 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9e849056-9d29-3c75-9195-d036e6159af6 | -3.7254 | -41.6987 | 2024-11-06 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 6182f3d4-0a66-36f1-af73-fa5e80bf0377 | -6.4909 | -44.6633 | 2024-11-06 00:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e5cd2b23-00ee-3409-b669-dfe1ef5e0c9f | -2.658 | -51.8194 | 2024-11-06 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ab0d67d4-e569-3494-b641-c647ea37cfb8 | -6.1039 | -43.9824 | 2024-11-06 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 439e7313-77e4-359c-a6ee-a38b0810d603 | -2.2691 | -46.4614 | 2024-11-06 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a8410e0c-6691-3379-a369-241fd355e6c7 | -5.5632 | -43.6998 | 2024-11-06 00:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| b4417cb4-6e81-3f75-9c6f-91bc51d4fdc1 | -1.2922 | -54.5585 | 2024-11-06 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 568ae6f1-0354-3f9e-afe2-4413ac5210af | -6.5096 | -44.6618 | 2024-11-06 00:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d559372c-9861-379b-a2c5-71310877b092 | -2.8065 | -51.4855 | 2024-11-06 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| dfa62640-f70f-3e36-9819-bd4e1cfc186e | -2.2505 | -46.484 | 2024-11-06 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| afb4f794-35a7-3ed4-ad40-fa9615c46039 | -6.5014 | -47.4813 | 2024-11-06 00:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 435.3 |
| c5aa9e4a-369a-35f7-94c7-b9625bc7a6a2 | -2.8661 | -45.6201 | 2024-11-06 00:20:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ffdd4515-c4aa-324c-b4dd-33a64e21248f | -2.6764 | -51.8189 | 2024-11-06 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| a4a5e0c4-9cc1-371b-bedb-1f831ddf26ef | -4.0667 | -46.9246 | 2024-11-06 00:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 52.8 |
| b1fefd16-1d57-3cdf-97be-8d6390810cae | -4.1246 | -43.5833 | 2024-11-06 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e95b8708-ba20-3924-8683-a7584aaeeead | -3.1802 | -50.2032 | 2024-11-06 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4a85edd7-5356-390e-8295-a67182e7579d | -6.1041 | -43.9593 | 2024-11-06 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b2dde045-fee3-3f19-b3cf-3a50d402308b | -1.2739 | -54.5587 | 2024-11-06 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 637df1c1-d393-3e01-8d3b-7dc23ac208c9 | -3.1617 | -50.2038 | 2024-11-06 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4b0429dc-9959-3ff0-a7b2-7157e8de4032 | -0.8355 | -52.8503 | 2024-11-06 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9316ecf6-7c46-3cfe-98b7-eca8c0286f6d | -3.6788 | -50.2284 | 2024-11-06 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| ba660969-6520-32c7-8ab3-a4dee902ff0e | -3.967 | -48.15 | 2024-11-06 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f41e26a1-fb4c-38b6-85ca-914a021402ea | -3.1393 | -51.2069 | 2024-11-06 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 0b036303-3529-340d-a250-97f835172c9f | -3.7564 | -45.9422 | 2024-11-06 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 864c5872-0c68-3130-ab93-609b42190a35 | -3.1616 | -50.2248 | 2024-11-06 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 683fdded-22ec-3dee-84b1-05ceeb066b9a | -0.8539 | -52.8298 | 2024-11-06 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 164.2 |
| 00daa1ad-ae6a-3da2-9f97-81be3d538e3a | -3.2054 | -53.2153 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d173e635-a419-343c-b4f3-0e96a4a88cf9 | -6.4906 | -44.6862 | 2024-11-06 00:20:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8f16a03a-a88b-3cbe-bbd2-fca494ecdebd | -2.1746 | -53.7036 | 2024-11-06 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d111729c-a92e-3564-b5eb-9a9dcbeca91f | -3.0023 | -53.4232 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3504520b-a644-3fb0-9e08-195469217d0a | -6.1414 | -43.9794 | 2024-11-06 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 12b1bad6-ee7d-34d2-8981-4f273c061a10 | -2.6764 | -51.8395 | 2024-11-06 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2764d50f-5a74-31a9-9bf7-8db96fe4ff2a | -4.1432 | -43.5822 | 2024-11-06 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0d3f4a67-3be7-3f80-89ca-92dda5eafbc5 | -3.0607 | -52.5066 | 2024-11-06 00:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5e0c2422-4ef8-3065-8be4-9ebc0825beeb | -3.5305 | -50.3387 | 2024-11-06 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5bd00a2b-99af-345f-8999-0dbe531ca5ad | -6.5016 | -47.4594 | 2024-11-06 00:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| aedab309-3b58-398d-813b-8fa8c503276c | -3.7068 | -41.6758 | 2024-11-06 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 8668ad94-b9d6-3b44-9f44-eba2ea462e2b | -2.3999 | -46.1699 | 2024-11-06 00:20:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 36.9 |
| ca0270d9-affc-35ea-a4e6-32a3c135bfcb | -0.8355 | -52.8299 | 2024-11-06 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3b886c66-90fd-361a-bc8b-e67b74fdaf6e | -3.2231 | -53.3972 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| fff6013a-4320-33bf-94e1-ada6d524d6b0 | -3.2415 | -53.3967 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| aec544b4-6eea-33b4-8cbc-02eac699b411 | -3.0207 | -53.443 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 368327ad-d87b-3124-af9e-cca3c009bdcf | -3.0214 | -53.2404 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 2464ea98-443f-3a03-96b5-2a7caa6c7e17 | -3.5446 | -47.3855 | 2024-11-06 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ebbdfd48-360c-3f21-9793-2f9f151a2a17 | -6.5012 | -47.5033 | 2024-11-06 00:20:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 290.7 |
| 3f9b0342-7291-3f29-88bd-dc289f754f98 | -3.0397 | -53.2603 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 9e67259b-fa5c-3fc4-9fc9-2322335fe63f | -3.7066 | -41.6997 | 2024-11-06 00:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| a17a7e88-764b-3aca-ba3a-04b1e680709c | -3.0396 | -53.2805 | 2024-11-06 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |


[Clique aqui para ver as próximas entradas](README5.md)
