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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae3ef20-7763-3cad-a51c-d9facde72d03 | -11.67208 | -44.41402 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9318e71-b29d-36db-8edf-b9d1834a27c3 | -9.24589 | -44.49549 | 2025-09-25 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6f504e7-dd35-39fd-8ec7-ade1f95d4bcb | -11.67142 | -44.41628 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f299f028-b2b0-3d61-b76a-39becbab9d74 | -11.66392 | -44.3867 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ad6a8e4-48e9-3553-b51c-08dc94f9a156 | -11.66679 | -44.42082 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fb7c733-d076-32c1-bbdd-e5134ae8f267 | -8.78732 | -43.03114 | 2025-09-25 04:34:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fea41c2-e7c3-30e4-b37d-9e026c878563 | -11.42182 | -44.9674 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2357bc2-40b2-3818-a8d9-84561788e409 | -12.07067 | -44.8597 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3068797f-270a-34e8-b55b-2650399e879b | -11.53481 | -43.65152 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cd173d3-f779-33e1-b08d-0aa4768b837f | -9.58416 | -45.45515 | 2025-09-25 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 396f7eca-71af-31d2-8fc4-39597a9ad0f9 | -11.91379 | -44.77204 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e04dd8c-4818-3ebb-85e6-a2bc472452c2 | -13.84205 | -45.62659 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 12462a35-8780-3d5e-9926-d0d0e0be04c2 | -11.01794 | -45.91286 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98dd1ccf-2fd8-3b30-9aa3-21eb40056d45 | -11.7866 | -45.58025 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92be380f-8646-39ec-8cc3-ca063a8e8d9b | -11.67351 | -44.40092 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed2a6ae1-055c-31e1-bc74-868c03b76940 | -11.42905 | -44.94366 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28b5708e-ed37-3aa8-b264-13bbd1630c17 | -11.38968 | -44.94814 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf6b9333-210a-311a-99c1-7106667c7619 | -8.49757 | -45.00493 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29009c4a-e87a-34cd-bb39-7a0b4ffbd942 | -12.84883 | -44.67641 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac409c72-e025-37a4-bc53-b65492095a03 | -8.13965 | -44.46293 | 2025-09-25 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ab979a7-d659-3a30-a7c0-8a876f72e1b2 | -10.37057 | -46.1389 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7c67f6e-2ec2-3b59-8d50-c5e3dcb35510 | -11.42112 | -44.97232 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a25d3565-53ad-3278-bc32-c08c60acb47e | -8.30207 | -44.93531 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b167b010-c9e3-31c5-a288-e02448989936 | -10.37116 | -46.13493 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00c99099-b49f-3785-ad6b-8d3ef415d155 | -11.62771 | -44.44392 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cb341db-74ac-3993-99b6-7a0d5e8792c1 | -8.84511 | -42.9973 | 2025-09-25 04:34:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fe2008d8-de93-327d-9a97-d3161e4ce6cd | -10.95389 | -45.6542 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fea3d62-3fa4-3c2f-a361-1bcf8c10fad3 | -7.77668 | -46.19335 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 760edc6f-d6f8-3710-a9a0-551c78010ff4 | -13.88438 | -43.73863 | 2025-09-25 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 319e23bd-2342-395f-9748-8cf8ab917d73 | -12.89468 | -48.89216 | 2025-09-25 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81709983-3d77-3b03-a8d6-cb1643dcf56b | -10.9396 | -44.26528 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af48e7be-9304-37f4-a320-9a95c84e1fe2 | -11.78596 | -45.58469 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd873330-2f5c-3272-98ad-b36fd6b199e8 | -11.79825 | -45.57762 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b8525c1-39c2-3b3b-9b7e-e6d7d2c91e76 | -11.64165 | -44.43038 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4c228ff-9ce8-3114-b25f-e546a0521693 | -10.39985 | -46.18414 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 360bab00-a673-390b-aacf-10e9bae7b9cb | -12.06776 | -47.9866 | 2025-09-25 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d11a9f8-d199-3705-8008-71f7618b0ed8 | -9.05846 | -40.52584 | 2025-09-25 04:34:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 88c42047-5bbf-30de-bab6-6de2eafcab2d | -10.59427 | -44.07308 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad8a81fa-4a48-3d94-bad4-12de87d271c7 | -8.48901 | -45.0124 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a571ff68-a950-35d6-9510-7c3343b2b768 | -8.48232 | -45.00724 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d485669a-566f-34f7-b074-446557de2049 | -12.05164 | -44.82671 | 2025-09-25 04:34:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 893238b8-028a-32d8-9aaf-ac0e7cb2ba71 | -8.12835 | -44.14007 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7a4c55f-9dfa-37da-9b34-833e35cd82a1 | -8.50611 | -44.99759 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 680b44c3-4000-33de-adf7-b39acfeedae7 | -11.04248 | -45.89497 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 16ba0ed5-4778-3180-b851-62072dfbad59 | -10.58385 | -44.06098 | 2025-09-25 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ac5213f-a0ee-32fe-adcd-4f89f8c297f2 | -11.39662 | -44.95386 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf808aa2-bf57-304c-b83c-1b59c253e8b5 | -10.38935 | -46.13361 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2751535f-e202-3c21-9b97-fc23160aef73 | -7.77383 | -46.18895 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32eb2b31-846c-3ac7-8a1c-6c6d9c7be630 | -8.85277 | -42.47443 | 2025-09-25 04:34:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c7b2c32b-0cc4-3f06-9ee6-910da802351c | -10.82758 | -44.8223 | 2025-09-25 04:34:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 660dd5b1-bfbd-3236-96e6-9ae5664d40b7 | -9.05645 | -40.52539 | 2025-09-25 04:34:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aec0af64-c924-360e-ab7a-54b7241149d8 | -12.47118 | -44.30552 | 2025-09-25 04:34:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 271d9555-df1f-388c-892c-8d4e3b67eb08 | -10.58884 | -44.08287 | 2025-09-25 04:34:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f32fa21e-581d-3dcc-b01d-c5980902bdff | -10.40103 | -46.1762 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 781478fd-1331-349a-9926-cafd6b968ca5 | -10.24983 | -44.96505 | 2025-09-25 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ac2dad7-a719-3ed8-9b43-1a8c19fe6dfd | -11.40357 | -44.95956 | 2025-09-25 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c38b21c9-5d51-32c3-b38a-a8586b144feb | -10.39167 | -46.16658 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6851c1ff-9cbe-3692-8c91-21d612d63522 | -13.8365 | -45.61139 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8d9c895-6c47-3173-8299-3755407e82c8 | -10.31042 | -45.21546 | 2025-09-25 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67cdae8c-36bb-3883-ae46-f1d24fbfc8ae | -11.04368 | -45.88668 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b410154-7e2d-3f1a-b2aa-dd51814aea84 | -11.66748 | -44.41571 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9ded0b8-b54e-3b9b-94ea-6f39fd0710f4 | -12.41885 | -44.74601 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cb3a354-cedd-341f-9194-fd41f40804ff | -10.28995 | -45.22696 | 2025-09-25 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab33d27e-10dc-36aa-9b21-ac15d0d19f0b | -11.61523 | -44.44725 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aed45977-d207-345c-81ad-ee90ad762ba1 | -9.43973 | -45.5854 | 2025-09-25 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30d978ae-245d-3c14-b6ef-aba5c5dfffcd | -11.80321 | -45.56938 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 355493b3-6811-39ea-9318-b05256aa5b5c | -10.00988 | -46.30447 | 2025-09-25 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 639fb7e7-2ee7-3953-8290-f65c0d03c24d | -11.63164 | -44.44449 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed9cbf58-38fe-36a1-97dc-c437e128fd78 | -11.68727 | -44.32939 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0373198-1627-34ad-8e12-f5465ad7753c | -13.43152 | -46.72736 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45a2eee4-6e8b-39be-8a59-ca99b96395cf | -10.92642 | -43.75219 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03743f31-4f19-3a50-a8a2-63e0942d8475 | -8.2885 | -44.95136 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b561fb8e-4a91-3dff-8d32-6a6628d58e49 | -12.86526 | -44.67362 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 760208df-6374-35e9-99fd-0616797f609d | -10.84919 | -44.80693 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac2e93df-bd62-3dde-9637-af8ba3e53714 | -8.8522 | -42.47855 | 2025-09-25 04:34:00 | NOAA-21 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3675bed3-d116-3413-959e-f0952577ae20 | -13.58972 | -44.54682 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6da3be7-81f8-36e2-8713-3e94e40443d5 | -11.60739 | -44.44609 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 294e1a2f-b90f-3ce3-8bfc-5a7fd302f52c | -10.84876 | -44.80855 | 2025-09-25 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac7b1777-c361-3c95-a1cc-cc2f3a05e223 | -11.67354 | -44.40379 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1958a9b-af6c-350a-a978-6b1809e9dde1 | -11.491 | -43.54015 | 2025-09-25 04:34:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a8752e0-ed9e-36ed-bd03-1ba78e78a290 | -10.57731 | -46.2823 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4228196b-b1b4-3b9d-86be-64d3164fb7ab | -13.56438 | -44.51011 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29cfc909-ae0a-30aa-8d38-1c857da8a064 | -11.63949 | -44.44563 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25630c2c-ce14-38f0-afa9-2676dea715f3 | -11.80753 | -45.56552 | 2025-09-25 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9de6397c-24e9-38a8-b659-bdad15b9dc6b | -13.592 | -44.54701 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ffa926-3b8b-360b-a8b3-b2629c93c2ff | -7.77326 | -46.19275 | 2025-09-25 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa402215-df1f-3f5a-b678-809df5baecdb | -11.62597 | -44.31279 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 630afdeb-446e-32be-b649-777b72dbd999 | -11.96542 | -46.61006 | 2025-09-25 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40e0f611-2796-3b33-bdfd-f78d417cf739 | -8.69192 | -44.03696 | 2025-09-25 04:34:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6129753c-be78-31c3-9a70-6c46d350d8a0 | -12.41565 | -44.7404 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 539b6e55-d112-3fa5-9ad8-c7a79df5dd4d | -12.85276 | -44.677 | 2025-09-25 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fae53a77-28be-3a5d-b052-ac11859481f8 | -8.64439 | -40.39626 | 2025-09-25 04:34:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 84ac102e-4fed-3f83-92dc-acac5a3c6287 | -8.30142 | -44.9397 | 2025-09-25 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d139a204-24d8-3b7e-9093-7f0486e8fa2a | -13.84271 | -45.62189 | 2025-09-25 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca8ccab0-d617-3aac-a062-924e4f0a44c3 | -10.19059 | -44.84374 | 2025-09-25 04:34:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c2377ba-ed42-3d73-b8c9-5b0fcb142c0c | -10.78741 | -45.38022 | 2025-09-25 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b34357f7-cd13-3f19-b0f0-4df6f7d32cfd | -11.67211 | -44.41116 | 2025-09-25 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be839156-d8cf-3d62-a797-32b0c8f96d0b | -10.38876 | -46.1376 | 2025-09-25 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62a67e40-09ae-30a9-8cbc-03969de9b2ce | -10.29863 | -45.21894 | 2025-09-25 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c47fe874-4765-3fcc-913e-1934a27384bc | -10.11093 | -45.32724 | 2025-09-25 04:34:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README22.md)
