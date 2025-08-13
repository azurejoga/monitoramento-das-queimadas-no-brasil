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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31a00e83-3b1e-341b-9449-79eb13cb5f89 | -2.89733 | -48.25433 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fbf98675-40e1-39d1-9143-0a45560e5589 | -2.90503 | -48.24844 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07a416b1-5a02-3489-9ce1-3ada098b5a4b | -4.06937 | -47.97595 | 2025-08-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f654466a-1a05-3940-8d7e-7fef19730e19 | -4.06603 | -47.97543 | 2025-08-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 500207f3-4326-39ee-bcd0-1ecfcdeb3786 | -4.1787 | -42.44979 | 2025-08-13 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aa97b69f-bd52-3355-a588-1c55247cd4b8 | -2.90064 | -48.25484 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c0625db6-e411-38bb-b3af-f08516e59705 | -3.88754 | -42.55669 | 2025-08-13 04:38:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fc59c5ab-9741-3cb2-a6ae-0f65696706b1 | -3.58452 | -47.52649 | 2025-08-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 444ea48f-5c09-37e6-b220-fa5bfd4478b5 | -4.44434 | -47.08991 | 2025-08-13 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd6fd54b-5476-3370-9bef-4e4fd4296bc5 | -2.95636 | -51.65979 | 2025-08-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac0b0ace-c7e6-3c4d-b2ab-cb9d09f5c3ae | -2.91058 | -48.25637 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6cf33a6e-eebe-30c8-9b1e-be420481fdbc | -4.22866 | -47.21458 | 2025-08-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ba1ffe2-2bb8-39e2-9fb7-85860f6ee5ee | -4.1742 | -42.44911 | 2025-08-13 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28638a8d-c9b8-39fc-af86-9dcb13c82abf | -2.2924 | -48.57548 | 2025-08-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b574150-6524-3d38-9ed1-eb3608c4cd6a | -2.28526 | -48.5779 | 2025-08-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bfcc2a4-8a47-3554-a583-b71897a23a28 | -3.0862 | -48.85171 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b4dc077-0701-3466-918b-6108c7ea3b40 | -5.44471 | -45.10279 | 2025-08-13 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25f9f01d-dd09-3456-a188-a63240ec111e | -4.22524 | -47.21405 | 2025-08-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 531641a0-b28f-3a53-8d7b-0e16760cfa73 | -2.90834 | -48.24895 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b660c2ec-6aa3-327f-b5f0-5e44982fcc07 | -2.90225 | -48.24447 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 616c4f86-4bdc-3244-9641-c144b0aa25cc | -2.28856 | -48.57841 | 2025-08-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed6b1faa-6092-3bf7-b895-e1d6b047c364 | -3.33541 | -48.71499 | 2025-08-13 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1a1a272-5ff6-32d3-9e8e-3e6f95649592 | -4.23071 | -49.9268 | 2025-08-13 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d822a4d1-5b91-3299-8f42-f1efb0adcbcb | -2.89455 | -48.25036 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ae31eb3b-cc6d-3b00-bd1f-e2c97208c30c | -4.2216 | -49.79005 | 2025-08-13 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 460d5e70-eda3-33a3-bb1e-56a8f31eb181 | -3.3321 | -48.71448 | 2025-08-13 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe60df9a-0db9-3881-8d83-5a8c515d8258 | -4.1697 | -42.44841 | 2025-08-13 04:38:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 66d74af6-5bc2-3163-bf43-ec2116a3de7d | -2.95573 | -51.66381 | 2025-08-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87d6b8eb-3ce5-3efa-b39a-cb6ad4aef486 | -3.70958 | -48.88995 | 2025-08-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9be07f29-7575-31bf-8355-64edb2b3c137 | -2.90395 | -48.25535 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c8d377ab-f9ae-3a53-b082-46a6236d7e91 | -3.18446 | -48.81072 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c1e4189-cfd2-3da7-83f2-e61c3129a274 | -3.70753 | -49.07619 | 2025-08-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fdbc4dc-e1f2-3193-80f7-32f1026ab67d | -2.90727 | -48.25586 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ea2001db-b2eb-3237-bb9c-5333e3689b96 | -4.77198 | -45.32373 | 2025-08-13 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d800df6a-7f1d-3adf-80cf-0443af644ab9 | -3.08289 | -48.8512 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1a8b5a4-5d2e-365c-96f3-7a6eb570c5a7 | -2.89786 | -48.25087 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 79dcfdc9-c2fd-32f1-81a9-9fe0e3da5509 | -4.77264 | -45.31921 | 2025-08-13 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d94f093-3e1a-36a1-8c14-9ade04c95c76 | -2.58483 | -51.92168 | 2025-08-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f87e7a7-0f86-33f3-a0ef-b67960351aa6 | -3.18777 | -48.81123 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3bc0d23-32aa-3dfb-9567-7e05e1acee4c | -3.58397 | -47.53007 | 2025-08-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7a8a8c9-e889-370d-851d-9d753a971f74 | -3.07959 | -48.85069 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f7d341a-4f66-3451-9cc8-8a19855cff8c | -2.58844 | -51.92223 | 2025-08-13 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7264c17-5be6-3966-8647-0c6264389b34 | -2.90171 | -48.24792 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1c4e0d1-1b7d-33b1-bd4b-553339a2bd06 | -3.97176 | -47.88092 | 2025-08-13 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ce18860-268d-3d0d-a5c4-7123f1300c17 | -2.2891 | -48.57497 | 2025-08-13 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 24edf669-0bae-31a9-b909-e54a3d71bdcb | -5.44266 | -45.10432 | 2025-08-13 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef7a50bd-bea1-350f-8904-f38103abfa8a | -5.18816 | -37.66216 | 2025-08-13 04:38:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e6b225be-7439-3550-b376-3d5822a9a490 | -2.91112 | -48.25292 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5f738233-938e-36c5-bdbe-cf0e6d8e175e | -2.90888 | -48.24549 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a2a0cb-be51-3a36-beff-90140bebbea5 | -3.08235 | -48.85464 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8df22b09-78de-308a-96db-cbc8febd5cdb | -4.22467 | -47.21776 | 2025-08-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66b06e0d-c40e-3c3d-b973-8297af858409 | -3.70807 | -49.07275 | 2025-08-13 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c470274-8b72-38da-84ea-dc72a29dc487 | -4.07735 | -48.03481 | 2025-08-13 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc4d0d57-ea5d-3eeb-9126-eea5541cac8f | -2.91166 | -48.24946 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 405fd3ab-7e24-3626-a6d6-8f12fed27f48 | -2.90118 | -48.25138 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 65b29086-454e-3495-82f5-79206142cf82 | -2.90449 | -48.2519 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bff0fe20-23de-381c-a78d-870cc9ff7cd8 | -2.89894 | -48.24395 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72330e9a-0b36-3e8e-87b1-88aeb3f4fe49 | -3.08566 | -48.85514 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e40a02dd-693d-35de-aac4-63d0f5702877 | -4.22809 | -47.21828 | 2025-08-13 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43814d1e-a0bd-3501-8c15-197b69d4166a | -3.18393 | -48.81416 | 2025-08-13 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55c3f401-a26b-3244-af1d-f0d2853e022e | -2.8923 | -48.2546 | 2025-08-13 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 9b84f962-ee5e-3aa9-afc0-b2c6bc534310 | -18.5505 | -46.0369 | 2025-08-13 04:40:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 54.3 |
| fd02b8aa-1727-30b2-bb5f-912ef963a512 | -2.9108 | -48.254 | 2025-08-13 04:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1314484e-03f3-3344-ba40-ffe97f9ce2ca | -16.3153 | -52.9201 | 2025-08-13 04:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a719fb96-67a9-30bd-8e88-5938fdd1758d | -18.5499 | -46.0606 | 2025-08-13 04:40:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b4e22081-f3b3-36a7-8300-24d14ab24e7e | -12.5173 | -46.9639 | 2025-08-13 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 872318b3-92c2-3626-8cc8-fee815ecbf8b | -12.4916 | -46.96172 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3729d652-68ff-328f-bb21-c05892bf411d | -12.58191 | -46.97874 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0c22e06b-88a0-3c38-95c1-8feaa6593994 | -6.91292 | -59.12408 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 145f215c-d92f-3b7b-a7e6-3ea9335de54d | -7.09342 | -60.02155 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 766efdc8-b177-313e-9220-a72c89b376ab | -7.07701 | -44.94285 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 19298d08-40bf-3bee-b1dd-785acb513c61 | -12.51359 | -46.96985 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b24981fd-ff9c-3d81-ad1e-018a4069b118 | -7.45599 | -60.62636 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7be15191-1d60-3e35-af55-e6d1de5b9979 | -11.71796 | -50.12792 | 2025-08-13 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6be55480-00c0-3df7-b942-38a8caab25a5 | -12.5814 | -47.06422 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20bcba93-c0cf-3f06-a905-0daa048a36f7 | -9.05751 | -60.6544 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 95f9f1ed-0120-3d83-94c0-f81da34aa915 | -6.9123 | -59.12758 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 8d6c6358-34c8-3601-a580-f2e218db1273 | -6.28176 | -53.63393 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b612ebc-32d6-3af5-8920-07e9883d4fdc | -12.46894 | -46.95827 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d46bd7a-8304-39cd-a2b8-ac600b2a48b2 | -12.48782 | -46.96114 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cd1e265-db37-35ca-82fd-e50723904f54 | -12.55487 | -46.97896 | 2025-08-13 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fc9a3af-2dc3-3f8b-9e42-e04bc2f990ef | -7.09201 | -60.02939 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6e55ba59-f32e-33a6-9a47-6aec337e3f30 | -8.5732 | -54.71746 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0ae57b4-ff6d-3742-8907-bd3def700834 | -7.07854 | -44.94176 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d24f745c-aa2d-3400-8dae-68d07bddf9cc | -7.06085 | -44.35926 | 2025-08-13 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a2bdb1-2cdd-3164-b0cc-623476b43c13 | -10.3459 | -50.81763 | 2025-08-13 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c743b82e-e913-3656-b97c-c3b88bff5050 | -6.89488 | -59.13175 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d846c114-9408-3705-b244-bfa3349ecd9f | -6.0991 | -59.92777 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a37af09-f1a4-3a5d-8f01-33ecb4704053 | -5.73471 | -51.66924 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 074fbfdd-c305-3530-aa48-7a249ba1c3da | -5.84906 | -59.92157 | 2025-08-13 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08e54582-1e51-3278-ab06-1db5e6f47f06 | -9.19997 | -59.65513 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68900a8c-7878-3268-bdd5-6f9f702301be | -6.9009 | -59.12918 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a8be7e96-af02-31ae-ae61-07cbf5f64c84 | -6.9038 | -59.14407 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d8ca8821-6bfb-3919-8cee-8d7b6ada2047 | -7.0729 | -59.20806 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb53f91b-9f5f-3d3c-90d5-99f55c9aa354 | -9.19805 | -59.66557 | 2025-08-13 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28f1c052-bd4d-334c-a972-5ae4b80e8334 | -6.01907 | -52.17282 | 2025-08-13 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5d62d69-1ca7-31cf-9dd9-ea8aef586bc3 | -8.57403 | -54.71251 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e247bab5-b7c8-3394-985a-fada44c38ded | -11.90368 | -52.53232 | 2025-08-13 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 276083c6-347a-34fd-a7f1-25411079030e | -7.27074 | -60.62706 | 2025-08-13 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97c39b9d-7ee0-3725-9090-0419f602d375 | -6.28073 | -53.64074 | 2025-08-13 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
