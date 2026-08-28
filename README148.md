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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 456168a7-5c36-39fe-b8fd-165f9ae80a6d | -9.27432 | -71.90825 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e4e0cb7f-ff06-3aab-b03a-26c6f3a68946 | -7.62853 | -61.34541 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 59866b51-3a06-3b55-a50d-cbd4d43ff112 | -7.35398 | -55.16749 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 39054363-02ee-3918-9879-662f52c01a09 | -6.67248 | -59.07461 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ef115e6-10a9-3d7d-b25e-10694e6ca4e1 | -7.44342 | -65.42375 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 381b7a4b-506d-3fe7-ba95-70de4c418060 | -6.93911 | -57.35484 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eb3c208d-225f-33c2-87c6-94503edec004 | -7.74886 | -61.06266 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8321bc4d-d7e1-3fb2-a806-53e01f33ee9e | -8.34686 | -70.85131 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 33c3dc38-a20c-3166-80f3-ae75d3acb8e8 | -8.22182 | -70.50603 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 31.7 |
| c43dd7c8-44dc-3f97-9d6d-17d44f50ce82 | -6.72064 | -56.33926 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ca318d27-98c1-3ab6-b86c-5d13482c2e26 | -6.03149 | -57.81593 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4567ba83-028b-350d-9f14-2aac686a1831 | -8.35711 | -70.74523 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 85.3 |
| dce06949-5795-328d-821d-1f6d46b3a6fd | -6.4472 | -64.49185 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c220c301-983b-3f8d-886b-0b9e23eb4c57 | -8.16117 | -70.63776 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 11.5 |
| eb8ff10b-bea3-33f8-b721-64e9082893ae | -7.59497 | -61.33174 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 64665047-2872-3a62-96e5-5fe1a58a0287 | -1.86477 | -56.23684 | 2026-08-28 17:47:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75c236c2-664f-3ca8-8287-8b7e7efa40a5 | -8.35101 | -70.84523 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 37.3 |
| af55c66b-0970-365b-a9d9-b10ea0b95427 | -9.35602 | -70.49204 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f883ccfe-2e28-3b0b-a049-b0b1bc1b6791 | -8.33874 | -70.28963 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 69508b5a-8bde-38cf-a9cc-10740002c56b | -6.81347 | -59.70961 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8747d026-6a92-391d-be35-ea0c3f222422 | -6.11166 | -57.82685 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66d249f1-793b-38ea-9cc0-4539d6933ff4 | -7.22234 | -73.10538 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce1d79b8-3794-3512-a4f7-4452eb5402a7 | -7.22844 | -72.43251 | 2026-08-28 17:47:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 46156023-8980-36d9-8007-976aff84a166 | -8.63843 | -66.53273 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d634fe3f-c6a7-39ea-b3ff-67283d3d0f15 | -9.20864 | -65.79404 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 59ed1578-14be-3d9b-b153-258e84ec8872 | -6.15345 | -56.10719 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 15800349-9ccb-3fd5-af02-523339180fba | -8.91877 | -68.85558 | 2026-08-28 17:47:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 0a5fb3e7-a05a-3347-a7ce-d03730bf7ab5 | -6.02445 | -58.05568 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35e41dbb-a3f1-3098-b0fc-cabba8421b4f | -7.78461 | -61.11091 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 660b3e1e-0d34-3d45-8d8e-8fbf9515e61c | -3.7121 | -57.22777 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a9d06560-5038-3257-bfca-c1e69e702c65 | -6.23749 | -55.46948 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9c33375d-72e7-3846-8bef-4c3cc96a913d | -6.18612 | -57.75519 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89742b66-0538-3f05-a9e5-b2ab5a928d16 | -6.65337 | -58.49479 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 366945b7-8727-31a2-b881-28a69954e069 | -9.29524 | -71.90221 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e9e9050-1011-3cbe-91e8-125427f776dc | -5.91067 | -61.38766 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e842c0a6-040b-364a-ac8b-ab10a8b3c634 | -8.20572 | -70.49941 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 104af558-3d99-3426-b94e-811711dbf66b | -8.79164 | -62.48162 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09e137a4-9a2c-32ca-b67e-1989933ca660 | -6.93615 | -58.94776 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1244bb5c-e614-39f8-a289-ba66e1efa30a | -8.87878 | -66.89767 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0226a0d5-d32d-33b3-bccf-f86ffc6c4968 | -8.79389 | -62.47413 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4adeb82c-8ef4-36e5-9c67-694ae833f01c | -7.57784 | -61.31166 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a104f227-4d3f-3264-ab5f-4f54b81c1294 | -5.88123 | -57.77219 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| b1517e7b-72eb-3afc-a02e-1ca27dab5b50 | -8.86216 | -70.66121 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8131e6f3-191b-38a2-86a8-55f466290fbf | -7.55902 | -61.3032 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 50be7042-ec7a-3638-becf-d79e5a9806ce | -3.63949 | -60.56178 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4c72c3f-e4d3-3fd6-adf6-79ed26ee3a7c | -8.68677 | -70.9864 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 01b9295b-7d46-337d-86b4-aa9d03ca8052 | -8.57253 | -64.17004 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1671bc49-1ef5-357a-89ea-00954b936fb0 | -7.48176 | -61.41443 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6a7d967e-7f11-3307-a4ea-ec88c79d81ba | -7.60179 | -61.33067 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8efdf0af-366f-3a6c-a293-2a5e0974036c | -3.2466 | -58.00807 | 2026-08-28 17:47:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| a2217fe9-2365-3c98-8fe7-a62b5f28f8a2 | -8.36272 | -70.75001 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 43.7 |
| af7e666b-096f-3eca-a530-bafa0b42d895 | -8.78512 | -62.4612 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.6 |
| b75476e1-87d0-31d4-9aa9-068b329182a3 | -6.21719 | -53.48153 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aec7a191-a83c-32ec-908e-bd4119222ef7 | -8.91304 | -70.87601 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1fc65aaf-669d-389f-9879-4fba5c60ca65 | -6.64752 | -58.49812 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0fbad7ba-0659-3fe8-a7d5-406ed38096a4 | -6.80326 | -58.74332 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0facf5f7-ee27-3ea1-8251-7535f81cf755 | -9.04919 | -68.12262 | 2026-08-28 17:47:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 2a7327e4-9d4a-3e71-973a-86ebe9ac3dfb | -9.38142 | -72.71788 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f90fbac-90dc-3717-bd2c-658c4e44bf9b | -6.16532 | -57.78653 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| d46e7981-93ed-36d4-be99-e962c422fca3 | -6.6515 | -58.49747 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 342ffc5c-75e6-3cd9-9320-e5fa4761d852 | -4.29807 | -59.47469 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7c187275-8636-3db7-9e9c-e6a061e39aa3 | -6.59744 | -55.43084 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 78fdceab-b084-3319-a4d5-65dad2e21d74 | -8.72124 | -71.00967 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8b1c68da-ce79-30dd-9a29-da543fc2d319 | -6.15885 | -57.79964 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 450d05d1-0164-3829-82fd-f579aa108233 | -7.58989 | -61.34388 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 5a59f7e6-b284-3c38-9b79-b9a5db0cfe6f | -3.40558 | -61.32525 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c04690dd-1a8f-3e9c-b988-fa6eca4fa7c1 | -8.27425 | -70.77998 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e18accad-26c1-339d-b85f-fc010bb83e2f | -3.40866 | -61.34573 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bb3f0d32-00fd-3d56-aa49-93509608bdfe | -7.64534 | -72.43708 | 2026-08-28 17:47:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| d841fc2b-ad37-39d9-b876-5cd82bab5c22 | -8.46821 | -70.80953 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4be1fddb-cbc7-3695-95ee-135ed9d4c2be | -8.6838 | -62.95135 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 58c49e76-90aa-31dd-bb04-384e8e139e29 | -7.58757 | -61.3291 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05cf86cb-9bc0-3a40-9b02-156468bc0c58 | -8.43375 | -71.15239 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c3ff179b-2f8e-3f91-9682-badd26f3b2b9 | -8.56953 | -66.95005 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 978f435b-49bf-37c3-921b-ea710ba4bf9c | -7.49405 | -55.27914 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b88941aa-426a-3940-8809-ea5ae0ec153f | -7.58524 | -61.31432 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 293d6ef8-02e6-3a57-8a1a-113a486e30a6 | -8.60534 | -70.21288 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c3573b79-9e5b-354b-bed7-24cdb7d4e394 | -8.83097 | -62.31723 | 2026-08-28 17:47:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b32274d4-25de-3862-b374-9c9f3622fbb1 | -8.50463 | -71.45567 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8fb153e0-06de-3335-9607-359b597f6469 | -7.47488 | -61.39285 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 6970f520-ea24-3cc8-82a1-fa69fb6c1a9c | -6.12007 | -57.82562 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb14691f-1e0e-3b32-8a08-da76c3aef4aa | -7.52933 | -61.36162 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6db8a3a4-1ae3-353f-bcb8-7bb3b39d82a8 | -7.76711 | -73.32742 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e861742-593f-3275-bf62-288cf189bd35 | -6.22401 | -52.97013 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1104e654-7e58-3de1-9ec1-5e4e718e1d1c | -3.6294 | -60.54567 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3f15e31d-0613-3e46-8110-b5c0d9ec7f65 | -7.78862 | -61.11412 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a595065-05de-36ff-9571-16cc85c70cae | -8.56641 | -69.65704 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 58776767-b5bc-361a-accc-10c417f1d039 | -7.4772 | -61.4076 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3dd9d442-122b-37ea-9df3-8c5784bc1ed7 | -8.43123 | -70.72071 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b21e0458-b8d3-3559-9168-47c086d4045b | -7.01235 | -59.57161 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 19f9c655-a780-37b7-9dea-6615bb43c54e | -8.88012 | -66.90695 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e5205351-cd5b-35e2-aeac-6ccff677ad79 | -4.14238 | -60.76084 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fd709d81-1c98-321c-8d2c-5e5bf8ca91c7 | -8.38189 | -70.85226 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 36.9 |
| dbea5b31-adff-3d88-a7e9-170b4c4ba212 | -9.42976 | -70.57761 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e3255422-5cb6-3bd4-8d2d-bfe8cc6e5338 | -8.67996 | -62.94838 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84148f03-db65-3e97-8d2c-60c50a8525de | -6.76682 | -59.46548 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6b7d705c-87fa-370f-b6dc-e8a0f0fadb81 | -8.89517 | -71.53124 | 2026-08-28 17:47:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 976a3c91-28a4-35f1-af77-2ca69330401d | -6.75191 | -58.72399 | 2026-08-28 17:47:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7214fbdd-6a26-3bc4-a937-c26f337eaa4e | -8.59994 | -70.2085 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 61c13934-1147-3c97-97fc-850c84222ecd | -7.73857 | -64.67494 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README149.md)
