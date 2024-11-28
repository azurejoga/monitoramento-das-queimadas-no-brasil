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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f37c73a-7848-3088-a9ac-0e79d312292b | -1.697 | -52.446999 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed0d70d-6c42-373f-b79c-1fd0581e0544 | -1.3222 | -51.7477 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4818c41-db2b-3a68-b9fd-e99facb8ce8a | -1.3109 | -51.9249 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5719ad5e-fe1b-35a8-a215-7fd36f326cb6 | -1.1108 | -54.141998 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 278c0436-efaa-359a-90d0-649c6aa2f598 | -1.0809 | -53.369499 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e73c4b7a-b572-33f6-9149-549a0b1f2f06 | -1.6021 | -52.255299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b091a7b-5add-3a35-a0af-14247dd73389 | -0.2745 | -51.624699 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 880b05b5-3ac6-3859-894b-fafaae467131 | -1.0734 | -53.199501 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f455016-07c5-38a2-8a82-1731847cb80f | 1.2507 | -55.914398 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98755088-e2b0-39ff-9cb2-813fe1221e0b | -5.2227 | -44.9174 | 2024-11-28 00:41:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38ddbf61-85f6-301f-9195-314fe0556b6e | -1.3305 | -51.920502 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06e0c947-4848-3fa6-8059-04ca7bc27087 | -1.6373 | -52.3652 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6276ff6-bff2-3ebb-b541-0fd3ce7b5a78 | -1.6515 | -52.427898 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 944fcf08-5feb-3fa6-8ec0-8ff44ec38f67 | -1.6884 | -52.5 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d4f04cb-0df7-39e0-bbfa-0d83afc42117 | -1.1134 | -53.605 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c11c8e9-551e-3a95-a50d-4040b8a8757f | -1.6463 | -53.865898 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5010be3-289d-3676-91b6-7107a1d9be00 | -0.2843 | -51.622501 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 811373a6-4750-3695-acab-28ec626c0d57 | -1.2406 | -51.796398 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e6690ed-071d-350b-ac90-570101e644e9 | -1.2909 | -51.654999 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc0a3d47-f81b-3c82-a3b9-c9ecce87501e | -1.7067 | -52.626801 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73f04346-8416-397c-9a6c-29937c34658d | -1.1785 | -51.931599 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66d95b4c-c3a8-39a5-aac6-ea382fd1a02a | -0.5925 | -51.709999 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 86395ec9-f5bf-3dcc-8db3-e16cdc559b6f | -1.6485 | -52.733799 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60ee0172-ea17-3156-b66f-b54a7965aef4 | -1.0876 | -53.353699 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad7270e3-32e9-3a1d-b82d-a3fc1774e505 | -1.6249 | -52.264999 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a83525d3-bf09-337e-aa19-47e4b0140178 | -1.118 | -53.396999 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ab37ed5-7fbd-3fe9-9744-b6dc92478fb3 | -1.6688 | -52.504398 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ae1d49-3104-32c2-8091-9bba36afaa6c | -5.984 | -45.348598 | 2024-11-28 00:41:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02a32f80-b920-3616-a90e-f5dc7dc31e20 | -1.6707 | -52.467499 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 819a482b-153a-3198-96fa-0ceb422a762a | -1.6364 | -53.868099 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e8908e-ae4d-3326-a06c-4da018f6521f | 0.9692 | -50.126301 | 2024-11-28 00:41:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb07365-aaf1-3c73-8a7e-921087603b1d | -1.479 | -52.348999 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daf4f01e-eed3-33d7-ba40-3942d96b77b0 | -7.6985 | -42.987999 | 2024-11-28 00:41:00 | METOP-B | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d427e331-2cf6-32ba-8566-41068088355c | -1.0824 | -53.376301 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cb96d32-847f-3ca2-8240-9f7ca355675b | -1.0507 | -51.731499 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 5065e8f0-5447-3654-ac12-849926d03fac | -0.9984 | -51.727798 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 345c5420-cf64-3f36-b609-640e5dee2b96 | -1.1914 | -51.761501 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0be480ee-9d2f-311b-9b3e-a050912d78b7 | -0.2784 | -51.505402 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a206be3f-5770-39f6-91ec-b0ab0d3ff2ec | -1.2516 | -51.6175 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ba5c6cd-4479-386e-84ac-14c335620c97 | -5.8284 | -44.109501 | 2024-11-28 00:41:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f406ed7-a675-3a3d-848e-97b5f3d4d052 | -1.6852 | -52.486099 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eefec16a-2edf-3cc1-b233-e71ccb9bc001 | -2.0451 | -54.676701 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a06ad375-c128-399a-bcb8-3abee7d5d73f | -6.8356 | -44.406601 | 2024-11-28 00:41:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da53283c-840c-32f8-9166-630d1cbb1f17 | -1.6053 | -52.269299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519727c0-e425-3e93-8fa3-57b0e548d45c | -1.7937 | -52.737701 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d326b130-c23e-30a0-acc4-c9e009a6e866 | -6.8219 | -44.392601 | 2024-11-28 00:41:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8adabca6-f610-3417-93b3-6d2b2d0a82b5 | -0.9605 | -51.651402 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa4c03fe-a1f8-35b8-ae56-a19a339667a6 | -6.5859 | -44.183701 | 2024-11-28 00:41:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bdf8439-56da-375f-83f4-4e5be5173850 | -1.2977 | -51.730202 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 016a7859-97d4-3bb6-b6f3-8352666be131 | -8.1257 | -47.983501 | 2024-11-28 00:41:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f62cbc68-e10d-3729-9e2b-faae0ddc3767 | -2.1503 | -54.824001 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 869ad681-f762-3b5b-90c0-0435dcc753bd | -1.3189 | -51.7332 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2891ab6-2ac2-3d75-8a58-35edfb340920 | -1.6438 | -52.7131 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e0982f-c57c-3597-81e3-a4565a23ed3c | -1.3321 | -51.9277 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a6c48c-17ed-3ea2-b72b-6d405212bc83 | -1.2176 | -51.740398 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba2e1410-921e-38a3-80d9-1b3e2fd40829 | -9.1774 | -44.719398 | 2024-11-28 00:41:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ac8d363d-abad-3e10-ab25-495f268677ad | -1.638 | -53.874901 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5c64fb2-0ae0-348e-aaee-3c7d28f043fb | -1.1714 | -53.542301 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d04ee82-06e7-3080-a898-0124dd0d3742 | -1.3962 | -54.9977 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6932d504-ff62-31c0-899c-14ebcad54092 | -1.3075 | -51.728001 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 771c9d2b-a13f-3379-b5a7-0f982df66992 | -2.1519 | -54.8311 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62133cc3-9c99-3fcd-af8c-7ac8b4ddee77 | -1.2078 | -51.742599 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf88a98b-2dfc-3e66-a4dd-103f35b3b7df | -1.7229 | -52.470501 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6236a0-4782-342a-bae2-9f10dfdbe442 | -1.5948 | -53.82 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ba02e6e-f1fa-3349-9616-cdf2d3802f89 | -1.6919 | -52.470001 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c16fa9e-fe13-3dec-a9d5-470ae830e1d0 | -1.388 | -55.007 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0363c5b-dcd0-3d5b-ba84-174078b919e4 | -1.345 | -51.666 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 881128b1-83d1-308d-969b-dee3df27b9f0 | -1.1711 | -53.677898 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9632b774-e49e-3ffa-a793-a22e731e4ae3 | -1.6267 | -52.455299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc96495-5db6-3575-83df-359688647a5d | -1.5939 | -52.2645 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 309efc44-fe57-3804-9424-a0e530bf545b | -1.0719 | -52.417301 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23b7ad4f-0a30-3e98-9de7-35dbce022005 | -1.6349 | -53.861198 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3aeccc-cbd4-358e-a821-f3b364910533 | -1.3338 | -51.934799 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75e7af24-e121-3b80-abb7-f5ecfa435f5a | -1.5869 | -52.006199 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2923e90-a66e-3d88-8518-42eefd5a65e2 | 1.8896 | -55.732399 | 2024-11-28 00:41:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6050b6f-cd15-3084-834d-efbf9083d35f | -1.4395 | -55.236 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50791394-e5eb-38e7-82cf-162c1560757e | -1.5278 | -54.4832 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdbdc905-1222-3cce-98a8-058d508ca045 | -1.6966 | -52.490898 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24a4f35d-d36d-3296-927a-d66388b120c3 | -1.2825 | -52.163399 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60fa6c18-2c58-3297-b9e8-d18851913c50 | -1.653 | -52.434898 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6aec49db-be6b-3e05-9a78-eac6a99bd588 | -1.2532 | -51.624901 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b30dd0f1-6c9b-341b-8c1b-a664420b008b | -1.6763 | -52.720402 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd75a83d-38de-3cca-ab6d-d365b67e5c59 | -1.8019 | -52.7286 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca66d8e-c002-39bf-8300-dd1d4b9cd386 | -1.5046 | -52.598999 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c136c7c-1e75-3da9-9cde-8baa937648c0 | -0.9571 | -51.6367 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0f3aec9-7af3-35fb-9cf3-ad881fd23920 | -1.1931 | -51.768799 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ecfe3b-4d8a-3eb1-a6c0-6ec15479d3d1 | -0.995 | -51.7132 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bfe9e518-2814-34cb-8830-5776c4c8745a | -1.0922 | -53.3741 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62a21244-8b26-3734-95b7-43e20d42f865 | -1.6299 | -52.4692 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| defef411-f391-3902-9390-bb2f5f6fab9a | -0.8822 | -51.715199 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3730abda-caa5-3cc6-86d5-114a0d121e9e | -1.7261 | -52.484402 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 996ede0e-aa85-3845-87c2-598eb31a2bab | -1.5809 | -52.252602 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0d814b-dd04-39cc-abb7-4bdb7ac163a7 | -1.3329 | -51.9257 | 2024-11-28 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 264ec80c-8a9f-3140-a744-c51f4999964b | -6.0862 | -48.0339 | 2024-11-28 00:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 197.4 |
| bbbd4a44-0efd-3947-81f8-d37afc89c32c | -1.5898 | -52.2505 | 2024-11-28 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| f4e1993a-f5ff-3d01-92bb-2dcf74be05f7 | -1.5897 | -52.271 | 2024-11-28 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 6b3557c0-5afa-3992-8907-f09b80e92b5a | -1.5714 | -52.2508 | 2024-11-28 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2e3f949d-6fcc-3733-b221-873b191a342e | -3.9674 | -48.0851 | 2024-11-28 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 23f56872-4ebf-3b30-9323-a3a710353a1b | -1.3145 | -51.9465 | 2024-11-28 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c62ec351-536f-3c2d-bd2c-a60a6816422b | -4.7722 | -44.4205 | 2024-11-28 00:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 451.1 |


[Clique aqui para ver as próximas entradas](README19.md)
