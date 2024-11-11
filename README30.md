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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76a859fc-92da-3c98-b35c-205895b1a0de | -1.66315 | -52.64109 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4321628-49f9-3ad5-a194-45bef44397b2 | -3.73755 | -44.538 | 2024-11-11 04:18:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99424c4f-2937-3525-a493-63b3f456bfe1 | -2.36396 | -46.79467 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0f5a011-e1cc-3c09-ae73-3262ead27b9e | -2.35781 | -46.67112 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 239dfc07-f10b-37ab-9e93-54e287333b7a | -3.23581 | -46.52909 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6479b3f3-bc78-3be2-b398-4a27615df528 | -4.46181 | -38.74557 | 2024-11-11 04:18:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01b3c11f-57d1-3743-a671-2ef2c7dfa965 | -3.92594 | -49.92065 | 2024-11-11 04:18:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a783d9a0-5218-3dd6-b176-a1cc1ba2c4c1 | -2.26356 | -53.74926 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 014ff9ba-64b4-3f74-96dd-9c2547d00147 | -1.39944 | -52.37408 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62948ce4-123c-35e1-adbb-70f4d6bde06e | -2.93215 | -46.71441 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4212cc85-9787-3a21-8327-05d10e808b33 | -3.1371 | -45.9723 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6563aedf-c138-3249-93d6-4f6ec5a21da1 | -2.61134 | -46.16689 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff749c42-6226-3c83-9198-9a0db8c750fe | -1.56892 | -53.42282 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ac95d94-ff60-3503-8a52-b5545ffb70a4 | -5.37487 | -42.76481 | 2024-11-11 04:18:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 83a0a0bc-5b97-3d79-a039-e3026098f594 | -4.63122 | -45.91256 | 2024-11-11 04:18:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7977aad3-55a9-3bf3-b5c9-689f47c8b334 | -2.40526 | -46.51211 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af6a4bb-01eb-37c4-a3af-f85c4882c6fe | -5.81606 | -44.12361 | 2024-11-11 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3b67055a-90b4-3c35-a776-22d63c2b5dca | -4.13218 | -38.70192 | 2024-11-11 04:18:00 | NPP-375D | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f76178bc-77ef-3abc-8284-22e9df93245f | -4.56619 | -49.59932 | 2024-11-11 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68c8fa27-b78c-3949-817c-78c233510a38 | -3.12386 | -45.96635 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bffecd5b-1e2d-39ee-b6f7-270e493de17e | -2.63153 | -46.15733 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f6379a-ac22-361a-9b77-4446022fa32d | -4.58803 | -47.07278 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c222ac6d-7468-3518-ad10-a582d26b572a | -1.1843 | -52.08447 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4873de77-8b1f-3629-b0e6-a1abea37f784 | -6.28495 | -43.39627 | 2024-11-11 04:18:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 72e69509-98db-3550-bfa3-ed625898b003 | -2.3997 | -50.32187 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d014e60e-12c8-3aba-9416-af1357c59414 | -2.53642 | -47.30861 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27d44deb-b4af-3648-87d6-a7cdea88dbee | -2.37265 | -50.33829 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5312fe6a-a92c-3dcd-b49b-693fabbb69e2 | -3.08653 | -51.07714 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db8da26f-6083-305b-a408-4892ffe3d73c | -2.69953 | -49.33926 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88fa0236-c336-3b92-a749-615676b3d2ec | -3.96261 | -46.69836 | 2024-11-11 04:18:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7821412-654e-395a-9ed2-c12868a437f2 | -2.25345 | -53.7395 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c2b08206-211d-36e5-a5e4-673af0d26ef5 | -2.22534 | -48.39031 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70d5d8b5-cceb-3049-a4c6-2325355b0563 | -3.12551 | -45.97821 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec2132b6-1fba-331d-b2fc-fa410c7ad06e | -1.44528 | -51.66698 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 566b244f-628b-3925-8b1f-f26eade5a680 | -4.52222 | -45.69762 | 2024-11-11 04:18:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b40df397-42c6-31e9-9acd-37d36190c5eb | -2.56571 | -47.348 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfc31d74-741d-3080-b198-fb30adce28d7 | -1.83963 | -52.4054 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cee66d0b-b6f4-3fd0-bf97-96faf91c1fd7 | -2.9776 | -45.83675 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9663f949-4123-3200-979d-9d81dfbe7e2d | -2.34552 | -46.56477 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6da8c0b-4029-31cd-b2c9-01e3f6bfc44a | -2.65012 | -46.80239 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59e6f511-4122-3894-a126-3c987b41dd78 | -2.55292 | -47.45079 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd2842ec-b070-374d-bc16-e69b1dc9f35f | -2.54172 | -47.3081 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6592935e-6364-3e1b-9a54-262a9f348093 | -2.5965 | -54.24704 | 2024-11-11 04:18:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07ba7ebe-ac1f-3c85-b717-5bf3f0085bab | -3.24283 | -46.4856 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dac46d1-479c-3cfa-a671-a47dbceef4c4 | -0.91153 | -51.65296 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7797a936-65b1-3767-a5a6-ddddaeec2d9e | -2.53622 | -47.35837 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f5440ae-463a-36bd-b439-90ec42e7b9bf | -2.98611 | -45.25543 | 2024-11-11 04:18:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cb894b0-9ae1-3eef-b167-da38567b5db6 | -2.69699 | -46.6713 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6af4953f-6ffd-3f17-bb4f-fbee255b84d9 | -6.01057 | -38.66038 | 2024-11-11 04:18:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fefa207b-0516-381f-8700-496ed1e991eb | -4.07035 | -43.94949 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1d551ff-f073-3950-93ce-016856462750 | -2.37991 | -47.9262 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f844e6db-b360-3158-93e7-78c319fd2484 | -1.64965 | -47.98827 | 2024-11-11 04:18:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e241771-657d-3180-abfc-24582c148727 | -2.20708 | -48.37693 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b347428-42e9-38d1-85ef-8e7772139df1 | -2.51529 | -47.34595 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85cc93e2-d9ce-3f8a-977c-d5d978b3e735 | -2.61216 | -49.23989 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e1b11a5-c2a0-3e00-8dd5-410b88068428 | -2.62741 | -46.16063 | 2024-11-11 04:18:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb3da05-f5a0-37ed-81b5-6b068be87a69 | -0.88395 | -52.93507 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6bdce8a-4f14-3792-b1ef-fdd0a846692b | -2.13129 | -48.56553 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b972d329-6f57-3759-a147-998d90c78db4 | -1.65357 | -47.9889 | 2024-11-11 04:18:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75a4970d-de07-3cd2-b82b-fc7bd2a80d1b | -5.84719 | -42.48508 | 2024-11-11 04:18:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb4c5f4b-9a21-3a61-960c-cb0a1ca58600 | -2.24034 | -53.77476 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2695f34-e8f3-35d5-bcd5-7c45d737de3c | -1.92708 | -45.56881 | 2024-11-11 04:18:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af4c4b00-5f30-33a1-ba1f-b8da08b8313c | -2.93869 | -52.77027 | 2024-11-11 04:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911ea2ba-c251-339a-b0b1-212bc3b9827c | -2.63435 | -46.80832 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 616d1206-9fb1-3711-be56-e85bd4623b12 | -3.71115 | -53.75471 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58664680-2059-38ce-8f19-143e9b14f8ff | -3.24347 | -46.48164 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0154060e-5867-38a8-bd38-14abb2ee0ca1 | -3.78346 | -47.46038 | 2024-11-11 04:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02e58c17-d019-3e6a-ad7c-490559c3513f | -4.71295 | -46.38449 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d66751a-7582-30f8-9993-ebe2471bb421 | -2.06216 | -53.41136 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 723910b3-7cf9-31a2-a6d5-0c852db0b8ef | -2.53307 | -47.36097 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e77733e-5407-3b6e-9656-9042950c9386 | -2.23364 | -46.43741 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ac0843b1-8d88-3871-bcc3-7849f4f1bee2 | -2.73767 | -45.20937 | 2024-11-11 04:18:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 653e1d29-cb44-3217-b93c-c0ba954ba769 | -3.24526 | -46.30995 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5ffb628-5435-3e4a-a5ea-246f1cdafe7a | -2.63863 | -49.52577 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f50ab97-e471-3152-b572-deecc7b4e10b | -2.26305 | -48.75362 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebe93d54-b0f7-3407-beec-9db2c64acace | -1.39532 | -52.37309 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6921a180-16f6-375a-bf14-5082e18d8529 | -1.56752 | -53.41839 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57c8b4b9-88f1-3d40-9427-ccd4e7fbc180 | -1.9779 | -46.80765 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a92fae81-1dbc-3c37-919d-27c9ec9749ab | -1.61661 | -52.39647 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07a8a3a4-54ab-3f4e-9a54-7d99de76aa89 | -3.02741 | -45.82468 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c84b0d1-5a7c-33ea-8be9-40297f4dae4a | -0.97287 | -53.18198 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4fcffb0a-611a-3e47-8ef3-db1c31b106d7 | -3.5391 | -43.56181 | 2024-11-11 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b068efd-227c-3dac-a05a-879bd0724db3 | -2.91311 | -49.48791 | 2024-11-11 04:18:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d4ae31f-c882-3c2d-8fe0-3c6de7ee59ac | -2.38377 | -47.92681 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df954b48-24b3-3150-814d-858413ee3417 | -2.1892 | -46.57952 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c72490c5-6d53-39c1-8a95-0a79a608a731 | -3.21338 | -46.4895 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55ef9e37-bd63-34c6-9c81-ebb502c1bd83 | -3.95128 | -48.9997 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 158b26d0-e052-3593-8917-314e41ea7924 | -2.32092 | -48.77809 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c784082-edaa-383b-b0d9-b6e23c5ea0f8 | -2.11634 | -47.89248 | 2024-11-11 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f4e45f7-acdf-35ce-abf6-006532cb451d | -2.18803 | -48.36865 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4f6e9d1-a8cd-32f8-b492-b0a9a9959126 | -5.4286 | -45.53113 | 2024-11-11 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78fa5944-fad7-337a-a41e-351e7df86160 | -4.14223 | -48.97674 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55cecc24-24f9-37be-8d16-72f203144a79 | -3.38035 | -45.2758 | 2024-11-11 04:18:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dbc488f-ae8d-3a7b-8e22-89559c534d66 | -3.1277 | -45.24046 | 2024-11-11 04:18:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 901d8aee-0eb3-34ce-aed2-ef432759e6cb | -2.38314 | -50.33068 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4814cd20-7531-3c82-9249-ade2cc92f82b | -1.60525 | -54.40646 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49d58fb4-9a01-30b5-ad33-08a325c4dcd0 | -2.48437 | -52.5628 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 283dc085-800a-3011-b764-fb356372ab50 | -3.03085 | -45.82522 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbb09954-ceaa-3a25-84e2-cb026f62e0ac | -2.65633 | -49.39182 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3934631e-194d-364d-860f-ff58ff2eac9c | -2.1352 | -46.70988 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README31.md)
