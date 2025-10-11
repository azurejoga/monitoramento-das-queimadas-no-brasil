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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57f1c763-57c7-372d-9e66-3ae3edf27434 | -18.07556 | -57.5316 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eb5fb7c7-2474-3eeb-b97b-64bf27ecb708 | -10.17115 | -64.73902 | 2025-10-11 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff8bb748-dc25-35d1-adae-f937b96f2674 | -10.84097 | -68.84656 | 2025-10-11 05:25:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b24692c7-7256-3113-a0c7-4321f84da872 | -18.0724 | -57.52338 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8a73bf7d-d469-3f78-adb5-4f43689e2eae | -17.95733 | -57.61599 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| daf31b7e-5906-33b6-a3d8-446b5dc0bb6c | -18.05178 | -57.56352 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 21c7fa73-a78d-3384-b504-f09dfcd65f77 | -10.08145 | -68.4734 | 2025-10-11 05:25:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abc6c8b6-7e20-376e-96ae-fb65588a1ac9 | -12.54619 | -62.02219 | 2025-10-11 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b78cae-e09b-34ab-bd5b-a9880ede332f | -12.59143 | -62.95073 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c326ffcb-c832-301c-a778-5863ba93e6c2 | -11.78477 | -63.18747 | 2025-10-11 05:25:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1006bb3-ed20-3d6f-be99-81955d0d1469 | -18.04353 | -57.5626 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bcf3fc52-503a-3c49-8d03-d10680522a8e | -10.06559 | -67.55096 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 3c969f75-37d0-3882-82a6-fdfa436c4f4a | -18.04806 | -57.55991 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 40808a3a-bd7c-3011-b456-30ba6239b3a7 | -12.40284 | -63.95551 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faf3c6b3-7925-37c4-8502-f655063fb509 | -12.3981 | -63.70718 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 626e712b-1f3e-311e-8a0d-061fd1ecbfff | -12.60306 | -62.00624 | 2025-10-11 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c2ba4fc-b501-35de-a45c-ea42f36c8e77 | -18.38481 | -56.16946 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cba1bea2-3783-387e-a4da-ef89b102cb56 | -17.90206 | -57.66302 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a4befe44-192c-3625-a1b7-acf6383761a0 | -11.5052 | -60.73499 | 2025-10-11 05:25:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8231cc6c-eb43-38be-9661-2b192725ea53 | -17.83631 | -57.65915 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1ecb7706-debf-3e93-9c7b-f15c6f7ed72c | -9.55853 | -66.74493 | 2025-10-11 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a0974b9-03ab-357b-a0c5-a7fc81f5165f | -17.81483 | -57.66472 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0b3bead3-93f0-30d3-add5-f41ed0f1fabe | -18.07606 | -57.52762 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fb4fe29a-feba-3f83-a596-9848c2c3b453 | -13.48735 | -48.10357 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16128678-8ad2-35c9-b211-daf2c276cbef | -19.50453 | -57.47291 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dac16454-506e-3972-b53b-47e9e41af663 | -17.84137 | -57.58489 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 92537421-d9a7-38ef-988f-9d070e869817 | -18.8181 | -54.96595 | 2025-10-11 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1105ba6f-a482-3e6b-98d6-85e8d931c2a4 | -13.45525 | -48.09836 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da1e7535-736f-3f53-8b0a-7d6a4698cc97 | -18.07779 | -57.54717 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 515cb8df-0aed-3646-bda5-d0cb0ff37a90 | -9.74877 | -67.22087 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad08bfa3-9143-3c01-b6d1-9d01cff36767 | -18.07732 | -57.5509 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ba68794a-6fef-321e-8711-2f991d3d07d6 | -17.9006 | -57.67419 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b7143569-3fdf-3b78-bb63-12a65f1f6b04 | -17.84041 | -57.65845 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cdd7a68e-a0a2-3dab-bd3a-9963167f71d7 | -10.06198 | -67.54587 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ddb5a067-1a45-38b5-8a08-6d912104758c | -10.06123 | -67.55015 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 06996053-1aa5-3a27-97db-2561b0f39ffd | -18.81975 | -54.96759 | 2025-10-11 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 676f1ab7-12c0-3514-b6e7-9561da291bf5 | -12.2378 | -51.13206 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25ede9bb-9352-3c07-b6e4-e396c7d242c4 | -17.83221 | -57.65769 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 957b7918-f442-3a9e-bfd3-d9a0779ddb06 | -11.84515 | -63.7169 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aadf3bec-5643-3a2a-9141-bdedab6a8d13 | -9.95597 | -64.85941 | 2025-10-11 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bb12e58-d4ad-3e55-a6c2-8e08b6e57aad | -10.62586 | -69.31828 | 2025-10-11 05:25:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6684f9a-4364-3959-8c17-aa044ab38063 | -17.83177 | -57.6612 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8525656c-50ca-3889-9da8-008aa15abf62 | -10.57426 | -69.06898 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54baf53f-5ad9-3721-9077-6fc1f86055cd | -12.39468 | -63.7066 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83e9c64d-c75b-3e93-a5a5-ed96c96df6c2 | -10.06633 | -67.54671 | 2025-10-11 05:25:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 71a5309b-9a4e-3e0d-86e5-33d10737e0f3 | -17.84696 | -57.57929 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| abab162d-b82b-3745-ac77-e2e0fe553293 | -17.84545 | -57.58558 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2a074d48-7c5f-3097-93eb-e4dca6e77a6f | -17.83995 | -57.66205 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6533ac49-f9fc-3c9d-9e07-bd8992e40185 | -17.8445 | -57.65888 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 90452bb2-2df6-3334-8dee-d6eb31594fd8 | -12.09098 | -64.24114 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b384bade-a129-3732-8563-3819c2b60797 | -17.83631 | -57.65805 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4df4bd1a-c463-3913-b8d5-9feedb147408 | -17.90614 | -57.66354 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cf2fd2e8-bd08-363b-a554-548f5c3651be | -17.81947 | -57.62964 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f9a884c5-9552-35e8-b1cd-cee920784ccb | -18.037 | -57.54845 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 763a9f43-d7cf-38e5-8e73-e48be19f2228 | -12.58633 | -62.96103 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65f66ffa-15b5-36ea-b2ed-423cd1d55679 | -18.07365 | -57.54678 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5d91fe90-154f-3bf3-b503-45f76efb234b | -12.23729 | -51.13623 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7aab53e9-b020-347c-8e19-0705f48d40fa | -13.26164 | -48.01656 | 2025-10-11 05:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0ba09661-9c75-3c75-badd-f460895c5a13 | -17.83126 | -57.66591 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2c537c5a-ca6a-3ff3-a6ec-31d928619e29 | -13.48677 | -48.10941 | 2025-10-11 05:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1e2f5f3-5be2-3b72-942d-41933046fe44 | -18.03661 | -57.55145 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 585e44a6-e71e-386c-8625-fe73b0ff9d9e | -18.03248 | -57.55101 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 801ed4b7-7a70-3924-b08a-4a4c2e9a2b54 | -11.5076 | -62.41798 | 2025-10-11 05:25:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e86d401d-d3b4-38e3-989f-6f93d7f80ffc | -9.49991 | -67.1367 | 2025-10-11 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4d44a41-9cae-32af-8604-4414fb8ee23c | -10.61134 | -68.67504 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edc45c84-f461-3e5e-a2bb-95b92e895dc4 | -10.90784 | -68.25829 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 086f703f-4a98-3f36-a30a-97062916378a | -12.23686 | -51.1398 | 2025-10-11 05:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa498f21-6030-384b-b969-a5af936c7ef4 | -18.0709 | -57.53536 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 492759a3-61dc-36bc-8e98-8c76f5f26b05 | -10.57903 | -69.06997 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a7e841f-379f-3d1d-bba2-d42d07d3db3a | -12.39427 | -63.8789 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b4030b-c599-3b2f-8844-a7ac37c418d9 | -17.82351 | -57.66179 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4a89ab21-5270-3918-854e-73075cceabe7 | -10.79083 | -69.31261 | 2025-10-11 05:25:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17ce578a-465c-3ea5-a3c5-e0b0b9c3b2f6 | -17.84086 | -57.65487 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cbe14c29-450d-34e4-a835-4333778fcba8 | -22.54044 | -52.05426 | 2025-10-11 05:25:00 | NOAA-20 | JARDIM OLINDA | PARANÁ | Brasil | 4112603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 692c9b11-d96e-3f93-8773-9e25c9a526c8 | -17.81939 | -57.66159 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c37665c2-16f7-33a8-b3dd-500d3b3a6cb7 | -12.39531 | -63.70281 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abf282a0-c5e2-3c2b-b00f-f4685b0deb16 | -18.03742 | -57.5452 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5bcbe42e-cd46-3dec-b0e8-618b78c64dfd | -12.6025 | -62.00977 | 2025-10-11 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5c914da-34d1-309c-baa4-898304d56068 | -17.89244 | -57.67312 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ea561e29-8f4c-3922-9ea2-3bc8fe73ae4f | -18.07413 | -57.54302 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9e6ddb1d-3318-3a52-a97e-eba372ee0d40 | -12.59478 | -62.9513 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57d3dd4d-f511-3c6e-991d-9b771d61994f | -17.82809 | -57.65853 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a2d77375-0082-3548-8fac-d80b90e64fc7 | -10.9352 | -68.3966 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60c577b8-799f-3b06-9b33-b4733445ca62 | -13.01015 | -47.90165 | 2025-10-11 05:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8f8aeb8-2e01-3354-9974-b3bf968ebfac | -10.69912 | -68.55175 | 2025-10-11 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb394e2d-4208-334a-96ed-29b90357d2dd | -17.89749 | -57.66621 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8941dbb9-cdc8-3eef-a9fd-aeec560bae15 | -12.09957 | -63.85798 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c618685f-2bdf-33c9-9d94-6c36cf99bdac | -17.83586 | -57.66162 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 44b91f1f-d529-3dcc-89f7-7aa918e5bdb9 | -18.04719 | -57.56662 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 89b05fd7-12d9-3c2b-a196-33db41989f34 | -17.82261 | -57.66862 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 826dbf33-0b0f-3556-95cf-ae817be5920a | -12.09612 | -63.85738 | 2025-10-11 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcf3dbda-fecd-366b-a871-b00354e5b5e3 | -9.95227 | -64.85878 | 2025-10-11 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a127352-12a1-30dd-8caa-395bd356bff3 | -18.06996 | -57.54285 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f9e2e00f-f91a-3afd-b269-cb0d81215640 | -17.8354 | -57.66524 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e8ddc7cf-88d1-31cd-b4e6-b13c22f544cc | -17.82306 | -57.66521 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 36c0d3cc-0b8e-3921-86e5-ea8ce2d417e6 | -17.83221 | -57.65881 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 50331bb4-2d72-3cd3-ba89-2aed10ffa77c | -10.79672 | -69.30796 | 2025-10-11 05:25:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f176492-f387-3fcd-8aa5-e25b6470526e | -12.09515 | -64.23777 | 2025-10-11 05:25:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e67a4c0c-2830-3df6-b362-b8bdc0e0f0f0 | -17.81894 | -57.66495 | 2025-10-11 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7bdff5e3-298b-3f1c-a600-6e0aef45ef63 | -18.81476 | -54.96749 | 2025-10-11 05:25:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README45.md)
