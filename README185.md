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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3db5ee84-860e-3461-8931-de7bc596d959 | -1.48454 | -52.00864 | 2024-10-25 16:54:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b02cce26-6a97-3345-be1f-c0ee1db57658 | -1.25402 | -51.94612 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8e3979b-a467-3618-a121-90844ca9a40a | -1.25072 | -51.94662 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 38edfaff-1661-3f37-9bc4-137ce8b26468 | -1.24741 | -51.94712 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d87dfab1-e51e-32d4-b0d9-b5869aa7bda3 | -1.24689 | -51.94369 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f5eb26ab-d6d9-3570-9984-16dd967c83a9 | -1.22122 | -51.93434 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bf698f95-c290-39dd-943e-54953c85a342 | -1.1346 | -51.89828 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 24e2310d-f0e3-3c6c-871d-c4d8ebebcf9e | -1.13129 | -51.89878 | 2024-10-25 16:54:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8018173d-f1d0-3511-9b1c-01360b1466d8 | -0.88472 | -52.00119 | 2024-10-25 16:54:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 456ba519-169f-3a78-98d4-50cc78d3f8c1 | -2.25504 | -52.06771 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ce3a9482-47c9-35f7-ba5a-fdefa8cd3916 | -1.99971 | -53.29676 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 11b303e0-6249-32f8-8da7-1f83a36d84ef | -1.99915 | -53.2931 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1901353-a19b-38cb-8a8b-f36ef7b53698 | -1.98142 | -53.19874 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0b1c85e2-7ed1-3308-8ef0-66f76a9a59a5 | -1.97613 | -52.62208 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a3de5a2f-1e32-3d5d-a646-421e961ac49e | -1.94944 | -52.94169 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e845bb3e-edb9-3d64-ab8b-2bbd9d9c09f6 | -1.92978 | -52.94829 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f814408-ba4f-33d4-8dfc-8072f7d164e0 | -1.92924 | -52.94472 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bddba522-766c-3fd3-a1bf-3190ab8d2dfa | -1.867 | -52.30956 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4c81cf8a-5767-327e-868f-4f1f9e0f3c3d | -1.86594 | -52.30261 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cba1a860-85e6-322e-bba2-13bcc4aa0a4b | -1.86262 | -52.30311 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 38eda2ba-b341-338a-b2da-0258d643b3dc | -1.83538 | -52.16896 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6cdfdd07-0473-3ed5-92b5-43cae6cb94f5 | -1.83245 | -52.43961 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b52188e2-eb18-3d56-bf03-76d2dd7cd7b0 | -1.82912 | -52.44011 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 516b40b9-64db-357c-92a5-b2fcaa6ca8d0 | -1.82633 | -52.4441 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5aec79d9-c820-3235-a8f8-b898f5f31ce3 | -1.75015 | -52.32385 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4683234b-8af5-3ae9-a0be-8260902fb3e4 | -1.74736 | -52.32783 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 49744a31-6b92-3aeb-972d-b19da2dd4b31 | -1.74683 | -52.32436 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 18f4475e-aa3f-3524-a3a8-a156586f9a58 | -1.7463 | -52.32088 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a1212006-b605-371c-99f8-ecbc49a3c048 | -1.74351 | -52.32485 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 754a51ad-77a2-3206-ae83-324cd926e7de | -1.74298 | -52.32138 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eae0fd46-7d14-32ed-a668-16e4ec7d2ac9 | -1.74245 | -52.31791 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b7cadee-93b1-335c-a080-e4ba89ffd24f | -1.73808 | -52.31147 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af1314d7-ab1f-30ae-b8c0-7a7123bad328 | -1.72167 | -52.69357 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98b2de99-6ec9-3a19-b309-8c99707ae4c9 | -1.71833 | -52.69407 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3c5d7329-9f85-3a5a-a906-186a264b0cff | -1.70549 | -52.6996 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 314da68a-c0bd-343f-8669-70e83f06f146 | -2.18366 | -53.24264 | 2024-10-25 16:54:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3efab00c-777e-3ccd-8558-8b41cbe3d05a | -2.15331 | -53.64178 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3bc75696-54ef-3ee8-b68b-0b47f45e3ef6 | -2.09247 | -54.58721 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 8a310f64-a5e5-3c1a-876f-3088cf1e50a2 | -2.09185 | -54.58308 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2a75b70f-4c17-383d-8c5d-e6a2b226fc4b | -2.07771 | -53.55742 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1c951bd8-051c-3cbb-bd79-846de9f0bd02 | -2.07427 | -53.55793 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2745e94f-d014-35bb-9523-1476d7374b44 | -1.89792 | -54.03934 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 83c22d67-a53c-3799-9aca-a6d9b2bf9cdd | -1.88632 | -53.58984 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c57b1a6b-d582-3030-b42a-76d21ae8d475 | -1.84446 | -54.85602 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3ff78c4-369d-32f5-9f51-c43cbf2496bd | -1.59999 | -53.39063 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| caf4a2ee-8967-332d-b983-91e8687961f3 | -1.56904 | -54.59474 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c748066c-fd52-3190-8f95-576d361eba58 | -1.55829 | -54.59619 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8c8b2c44-441b-39a1-9928-46efde6aad3e | -1.4226 | -54.65123 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| f7e6868c-7136-3f45-bea4-475ca6a83fc1 | -1.37561 | -54.17844 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0386b3c8-3dec-330d-bbf0-de041a89a4e3 | -1.37504 | -54.17465 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3239153-2fbd-3330-956b-c0af9cfd4d53 | -1.37447 | -54.17086 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4abdc5d8-c176-3d0f-ae59-5d62afb72a65 | -1.37388 | -54.16698 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b50ffa8a-0a13-3ea6-8d49-f1302a35daa0 | -1.37211 | -54.17894 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a23d1e62-a448-30ae-82ba-867df7213436 | -1.37038 | -54.16751 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ce856b9-7ef6-33cf-9492-affab0bee2e0 | -1.36803 | -54.17565 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 437889bf-73b6-3604-a19b-3ab7c8a69564 | -1.36746 | -54.17188 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a37582bb-f462-300e-834b-bc36e7134634 | -1.36688 | -54.168 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7e48bcfc-2b19-3eeb-9fb9-d7114310dfba | -1.36452 | -54.17611 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b7520e12-0212-3442-be44-f2ad0c1c9677 | -1.36395 | -54.17234 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 67271603-fe47-3a92-87bc-fbaf86bee633 | -1.36337 | -54.16848 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 7b68933e-2a29-3b7c-bdc5-792fdef37e65 | -1.35206 | -54.64469 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 503ed567-f4b0-3a47-b7af-0d9efb18b64e | -1.26024 | -54.68354 | 2024-10-25 16:54:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c3c8897f-9bc2-3ffe-9c31-bee23ddec886 | -1.18565 | -53.66366 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a147d086-15e1-3ab0-8bf6-82e3b216727d | -1.18222 | -53.66419 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 90b10f73-06f8-3bb7-a360-337822e93c29 | -1.18001 | -53.90179 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2d5f7235-4a11-32b4-885b-8a55c9caeb4c | -1.17936 | -53.66843 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| b2d307dc-4c2f-3a80-95a7-71461b27b3c3 | -1.17881 | -53.66473 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| fd39b46f-7006-39dd-ae09-e5b8f9254c76 | -1.17595 | -53.66899 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 63e76f75-32e5-3b7e-a6da-c546fe95100c | -1.17301 | -54.1811 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| faec8223-6776-3754-934d-5d2dd71d3a57 | -1.12012 | -54.14884 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55d5e61d-46ff-32b4-9caf-aa370c6a35c0 | -1.11231 | -53.41664 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa89769e-c75d-3cba-b1ba-2d67457bef0a | -1.10891 | -53.41713 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 507be4ee-fc7f-3ea3-a1ff-cc8f00d0962f | -1.07885 | -53.65359 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 061c891a-5f9e-36a6-814a-7431b7d30d2a | -1.0783 | -53.64996 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf9b7e89-2847-3fa6-9926-2b6fdf05d186 | -1.07489 | -53.65054 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3d71569-f9b8-38fe-a8dc-85771fcf4dd7 | -1.07369 | -53.66573 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1cd3f151-0d6c-3798-9577-cabfea95573b | -1.07312 | -53.66199 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 36d163aa-6f74-304b-b38e-e62030b53cf4 | -1.07257 | -53.65835 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 2753e4b5-11db-3bd5-97fd-dbb6d9fe0db0 | -1.07084 | -53.66999 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9725b19a-aac3-3472-93ec-6b1de59eb19e | -1.07027 | -53.66624 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3fb1068a-39ce-358b-810f-6891fd684b48 | -1.06971 | -53.66252 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| cffdc4e7-769b-338d-9ea0-331d1a2a19ab | -1.06915 | -53.65887 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| daa2de63-6443-3e26-85d4-6a9fc2ed7ba9 | -1.06685 | -53.66677 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f8da4eda-62db-3b99-bbe8-519807d2428a | -1.06343 | -53.66729 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| dbc6c210-c2ba-3351-bd07-b3b068e729c7 | -1.03786 | -53.52109 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 22de9962-7433-3f79-a977-e89e7c240841 | -1.03708 | -53.52096 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9db2394b-c3af-315b-bbfb-5b254197e441 | -0.87714 | -53.68802 | 2024-10-25 16:54:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 53f9ac1a-c0c5-3f41-98cd-213494f77047 | -2.58194 | -54.65841 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 197b5b1c-8b1a-3562-a9b9-476921fab0a2 | -2.48588 | -54.45098 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 814fa81a-db8c-3c0a-9fa2-ff79f181a1c4 | -2.48459 | -54.47757 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0750bc7c-e5e9-39c7-aa5e-6b1e73da7835 | -2.48452 | -54.45237 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc5e32d8-2d61-3b93-838a-93569df9b74f | -2.48398 | -54.47345 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3afee42b-e414-3722-9600-1bf07ede8353 | -2.48249 | -54.47665 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ec86b439-5ce7-38a3-9482-7f70b2734c72 | -2.43935 | -54.58022 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 844477d5-ea4f-3ad8-b3b5-ec6a2002242a | -2.3713 | -54.34712 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 749a7b68-7464-38c9-b299-969892cfd75a | -2.36472 | -54.32743 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ba2beb1a-065d-3987-95c6-a2827437354b | -2.36329 | -53.95883 | 2024-10-25 16:54:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 231.4 |
| 88f234ce-5ec0-33d7-a1af-b40f3e130a69 | -2.35817 | -54.32825 | 2024-10-25 16:54:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f3f1563-49c4-3e70-90b7-1beb664d393c | -2.17756 | -54.47896 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 857b289d-6f81-3963-952c-d5eb8658012b | -2.16978 | -54.47594 | 2024-10-25 16:54:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |


[Clique aqui para ver as próximas entradas](README186.md)
