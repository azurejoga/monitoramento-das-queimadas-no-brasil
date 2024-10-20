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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee7fc468-4a96-3c44-88a2-dbb6e82d6d69 | -7.21147 | -47.33648 | 2024-10-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 729ef088-3a0f-3e79-89c3-ddd65ab99016 | -7.05575 | -46.82779 | 2024-10-20 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 712ed0fb-0976-3dd9-ae15-28a7c8b0b64f | -7.05514 | -46.83139 | 2024-10-20 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c18ab433-0f4c-32bb-b617-6b9f42fbb53f | -6.93359 | -47.20333 | 2024-10-20 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3aff726f-8ebc-37ab-a62c-e95bce3b309a | -6.62966 | -47.35599 | 2024-10-20 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dbbcc2c0-76ab-37c6-a1a3-cf55a49ac55f | -6.62959 | -47.35662 | 2024-10-20 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fc5a7efd-c5a0-3c03-be4a-79d8f370923a | -8.56002 | -47.81483 | 2024-10-20 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a899170-7f7d-3205-84fa-5fb4c522b5f2 | -1.97596 | -48.68348 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a031deee-943a-3d93-8aed-443971f4f280 | -1.97549 | -48.6863 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 445050c6-3a28-31c5-bbcf-c33c4260209b | -1.97529 | -48.68472 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6567754c-5c87-3c54-b6ef-6d1bca44008f | -1.97484 | -48.68758 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 093fb456-02b5-3bf7-9a79-7af1f96b5f4e | -1.82582 | -47.22593 | 2024-10-20 04:08:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80cb3b19-83d3-31e4-bf69-04172ba4e1c1 | -3.25812 | -47.97297 | 2024-10-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a41f12a2-864f-36fa-b0c0-944e6321a5b6 | -3.21726 | -48.61292 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c3dacedc-209c-3aeb-b6bf-476ff6c98e47 | -3.21239 | -48.61216 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b9c1529-080a-3d99-9527-987eb7c2d128 | -3.20661 | -48.61679 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c28d114-9ac8-30a5-a365-0e0dda0dc933 | -3.16386 | -48.37223 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 267fefdf-ab8b-3092-b2f2-37e85bddd19c | -3.05113 | -48.01835 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b54e35e0-e400-3dd2-b8e7-b7299c2e2dec | -3.04921 | -48.01553 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c03edeb-cdb4-3c2d-921e-fc495c3bcec5 | -3.0484 | -48.02057 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b12d6d7-3849-32f7-8929-0a6b6c711978 | -3.04644 | -48.0176 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7471da4b-6ce1-382f-b077-2a69e8a9a4f7 | -2.97875 | -47.91845 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e4467340-7b9e-3746-ab25-a4b078bba180 | -2.9741 | -47.91768 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9669e21-7f65-35b6-8616-4ea5798ceb92 | -2.51782 | -47.4882 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 512ea5e4-f1fa-3930-b0d2-52ee1ae8522a | -2.51329 | -47.48732 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 0cfaae42-7eb4-3b72-9e59-3a3e1c8a87e4 | -2.44075 | -48.5036 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a130b8aa-427e-3ba1-aa19-40aca275d60b | -2.43596 | -48.48785 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7b239630-96ce-3259-bada-c74efc05bd2a | -2.43357 | -48.48563 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 98e0086c-b791-3c9e-82b8-a7faccd26920 | -2.43107 | -48.48706 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51cc2d42-68e8-3980-a0cf-b1cf6ac1083b | -2.42138 | -48.88277 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e0b1b4e-37b4-3232-92ab-27b448013e65 | -2.41927 | -48.44983 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8029c1f-a792-32f6-9288-57734bd7fde0 | -2.41635 | -48.88196 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| daab6ed7-7236-3d75-8219-9cc61662ebc7 | -2.36658 | -48.29102 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3292e9d-14d5-3355-a9e7-6af8e72a78c0 | -2.36528 | -48.2928 | 2024-10-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af6e6c26-9876-332d-90b7-7ea7c546125c | -2.34628 | -48.80711 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7619635-2c5e-3a2d-8265-d9591ce5fa4f | -2.30559 | -48.58986 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4bf4c16-8687-34b8-992d-5fbb6379215c | -2.30519 | -48.58224 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 787f1dc0-63d2-3540-9246-823c01cbac59 | -2.30463 | -48.59557 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8f1e537-e627-3409-a180-add01b752d7d | -2.30429 | -48.58787 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ad2104bd-2770-3473-9d33-cafaee3c9df4 | -2.30338 | -48.59359 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 316e0098-1bab-3999-879d-079f5031bf0f | -2.30254 | -48.57785 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 762c3176-f27f-34b8-8fe4-187b47780c7d | -2.3016 | -48.58347 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f22ca38d-ee36-3a48-b94e-c3935fb28f8f | -2.30065 | -48.58908 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7b61c08c-fd1d-3a07-b367-baf86af20191 | -2.30025 | -48.5815 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 99e24e23-0697-3bcf-94f5-0847c363a2d7 | -2.29936 | -48.58709 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 13454eb5-506e-3c66-bfcc-057e397b8af9 | -2.29844 | -48.59281 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3759c187-23ec-3fd0-bd23-6d6c00118732 | -2.29666 | -48.58272 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 0fea1b6f-52ff-3269-8ef0-6d7cbf948d6b | -2.29571 | -48.58834 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cf7399b5-416b-3284-ba99-faa1a33e4fc9 | -2.29476 | -48.59397 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4f6cad77-06ee-3627-b95b-93cf9ae69315 | -2.29351 | -48.59199 | 2024-10-20 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7bede097-8101-3172-9f15-b36d58a8c6e0 | -3.48555 | -48.24191 | 2024-10-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f98c01d6-b337-3cd0-83e5-73dc7aa3e620 | -3.4638 | -47.66572 | 2024-10-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26039532-28b8-3238-b509-9c5e86cdb899 | -3.46303 | -47.67032 | 2024-10-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 593fa044-4741-3ee3-89da-ac7d0ab6f66c | -3.42861 | -48.82506 | 2024-10-20 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd272617-28eb-3596-ad59-9b2a5c94dd18 | -2.80352 | -48.68288 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd6c3e7e-313b-30bc-9349-d82f3704228f | -2.79859 | -48.68211 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 758a75e7-1d88-3815-ac30-06eb7657f9f9 | -2.79768 | -48.68767 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e5b4e3f9-ea0e-328e-9e1c-b5a5122194b6 | -2.79457 | -48.67576 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| beb32766-c608-3371-9bc6-ab374891ac17 | -2.79366 | -48.68132 | 2024-10-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 4ce85996-a3fd-31a3-b28a-1b052e29080d | -2.18339 | -48.73542 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8243e669-9425-30f3-b95e-b1119bc32fe1 | -2.18297 | -48.73558 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d133961c-a5f2-3eff-8d11-903b4b63043c | -2.18291 | -48.7383 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f307d254-7e56-3097-bab5-f8cade4c9582 | -2.16377 | -48.79127 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b70d16fb-3841-36ad-9d48-912a6924e617 | -4.89663 | -48.28407 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 80d88fe9-4082-30c5-b4fc-6ae25e77297f | -4.87491 | -48.21627 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 7119d4e5-0805-304c-bc5c-1c6b290198c5 | -4.87137 | -48.21214 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 73dda724-62a4-3c19-bb87-de27835ec9a8 | -4.87115 | -48.21054 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| dc08f25e-09a1-3054-a2ff-c75985b801df | -4.87056 | -48.2171 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 50aba439-0b58-3770-9b54-75133b255c3a | -4.8703 | -48.21549 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a06435cb-b47c-3ef7-9807-c70575ba099c | -4.83292 | -48.54639 | 2024-10-20 04:08:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d085c44-185c-3e5b-aea9-1907a00ce165 | -4.82822 | -48.54546 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b3cdaf2-c270-3f0d-be3e-b2e56e4d1ac9 | -4.57867 | -48.01725 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08158b91-d800-3bad-bac9-5059baa74e28 | -4.57823 | -48.01802 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 42d2bb01-867b-355e-a17a-1783f5d69b97 | -4.57787 | -48.02195 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b40ef30d-b6a8-36ee-bf92-f1820daf6147 | -4.5741 | -48.01651 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 86fdf7c9-4586-3542-8de7-771901d7dd72 | -4.57366 | -48.01728 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f977d3ce-1d9c-3262-8227-e101d7fa36b7 | -4.5733 | -48.02121 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0b46262c-209c-3f33-b737-9f993b90454d | -4.57289 | -48.02201 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| df5e1eab-2f5b-3138-a2ce-b54f9e5cad8d | -4.56872 | -48.02049 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d8935bc7-484f-3dec-8599-9d78809bb2bf | -4.56832 | -48.02129 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 651cc865-8fd8-3a05-ab8d-2da970b7157d | -3.96761 | -47.95024 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bce48afd-b119-3dd9-a741-c9bc6aa7cab8 | -3.963 | -47.94956 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a86be28-716d-30af-b65e-533337dd9908 | -3.96222 | -47.95422 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 481acdd1-6ac2-3f2e-bf57-a119d9dd0d36 | -3.95761 | -47.95358 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49f4f052-e5e7-3eca-9f30-3caf3c6e314c | -3.92794 | -48.36129 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7de5687e-a989-38f7-a7b3-179284907b5a | -3.91246 | -48.33753 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf7702bb-d26f-35e7-aadf-9c7ad3998867 | -3.90854 | -48.33197 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3538caa2-426e-3753-997a-697fddf9e179 | -3.90773 | -48.33681 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fb2a27a4-681c-3fe2-8d91-bf87476f4772 | -3.90381 | -48.33125 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c66dc09a-d958-3bac-a9d6-0676b839d0c6 | -3.89909 | -48.33047 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ebaef4e-4d38-3735-8d84-e35587c7703f | -3.87551 | -49.08269 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 523b3a04-bbbf-34f0-aee5-c3529dbbcdce | -3.87052 | -49.08194 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06c05420-b095-3f1c-bdf9-93b4509348c2 | -3.8381 | -48.96378 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 8aaced4d-d258-351b-9d84-840b66aa2f8d | -3.8372 | -48.9692 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 460d913d-1157-3f1d-be89-70fbde381ff1 | -3.83711 | -48.87836 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9d7ddf47-661b-3972-8873-fd614629b182 | -3.83618 | -48.8839 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5b440483-2697-319f-ac72-92416018d47f | -3.83526 | -48.88947 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b3c410a-58ef-3a75-8db4-3c841b75347c | -3.83315 | -48.96301 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 09378f08-4e2b-3bdd-b789-12f50ee454b6 | -3.8322 | -48.87753 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c25a216b-2817-3788-8ee1-94f6e45b5329 | -3.83128 | -48.88303 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |


[Clique aqui para ver as próximas entradas](README21.md)
