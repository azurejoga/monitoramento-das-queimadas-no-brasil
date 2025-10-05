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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55311b4f-12d2-350f-8d64-37fbdfcef4e3 | -11.09091 | -47.88467 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c43f1d61-0acb-35d1-87a6-b09fac455822 | -15.37073 | -47.98307 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27d58174-707a-38b2-989d-8c08e317e3fe | -15.29823 | -47.95243 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 324c99f3-7eb3-3d14-b585-a8228456f921 | -15.82634 | -42.61512 | 2025-10-05 03:55:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c60b5629-5201-35c3-a15d-c22bd33c1a7d | -11.90733 | -46.23129 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43b7fe37-072c-3b9a-917a-72735b05e5e7 | -15.72736 | -46.25983 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0329b706-eec6-3de7-87e8-2fb3a364edee | -13.27438 | -47.19217 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d8736b5-ceb5-331a-b05f-85e579735960 | -13.46966 | -47.28313 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d44d2027-d657-3bf4-8f4c-e0aab18e5ce4 | -13.30685 | -47.56699 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a48fa8f-ab47-3830-a8bb-4a57d1d4c990 | -13.30051 | -47.80827 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6df8ff6f-9415-3081-a2e2-d9894779a890 | -13.3146 | -48.08828 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 496bcde0-191d-366e-ad4a-63c62a31bd5f | -14.6875 | -48.26742 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37038e9e-84d7-3e31-86fb-f4adbe7a3805 | -13.17983 | -50.87547 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bdb97e7-d4c6-3952-98ad-3e3aae4cf2ca | -14.66451 | -48.2812 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78abaf66-3677-380e-8226-04502cfef51f | -17.09596 | -45.50021 | 2025-10-05 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b9b0346-539a-35c5-abea-2c955767ef82 | -15.69794 | -46.27632 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5631474-b0c7-3f4b-b36a-113388d66fdd | -13.73361 | -48.08079 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 75c5b067-64b5-3f2f-ad00-71ffbb933b2d | -15.81566 | -46.25159 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38693468-80dc-3b6f-8675-3434cccff980 | -11.23055 | -47.80146 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43f5db5b-1194-3a88-b93b-1c2237e5d888 | -16.3462 | -51.46394 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e59815-b437-3895-a306-8a2fe2c337da | -17.56789 | -46.07945 | 2025-10-05 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6323fa6-3560-381c-92c9-8d822a87e273 | -13.7362 | -48.07659 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c39a5b6e-3975-322f-a1a4-9d2058247622 | -13.1419 | -50.94137 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 6cce8e99-27f1-3cdf-8e4a-d5aeecc49841 | -14.46272 | -46.3431 | 2025-10-05 03:55:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 195d94f3-d414-3c65-86d5-89000fbda7b8 | -11.09015 | -47.75547 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4615cc80-7e30-355c-a835-667c7f239612 | -10.35587 | -48.1635 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 399ac39c-6a32-3b33-a262-5c2baa72611d | -12.86737 | -47.27815 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e46bc11-f1f9-3bc9-a7a7-253c2acead37 | -12.93678 | -51.01114 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 270f3635-8b61-3db2-8903-4199678338ff | -13.40321 | -44.3849 | 2025-10-05 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 319819c3-c6dc-3f7f-9845-4228b4694442 | -15.77505 | -46.26025 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46448f22-4802-30fc-b527-e441aa8d6e8e | -15.20697 | -46.38868 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa88024-1e06-3638-bc82-e915769026c7 | -16.57043 | -46.36023 | 2025-10-05 03:55:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2570e730-31e3-3c6b-a9ba-c13cdade0c7d | -13.67844 | -43.18248 | 2025-10-05 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab5b4b1a-6b02-31e0-884c-828a78a4f930 | -10.78394 | -51.0022 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20ab8415-9ef5-3288-868c-b469819b3222 | -11.86096 | -44.94917 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b71a99ba-7c44-3d07-8034-8c43f3e07a35 | -14.25331 | -46.10607 | 2025-10-05 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eb885d5-79c7-38d4-a6c3-3b7a9d10889e | -13.28248 | -47.59005 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bbcd0038-65c3-3026-8b1b-4cf06431d874 | -13.28273 | -47.61713 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a8b17d82-c611-3076-9ca0-5d94acc27d23 | -12.92253 | -47.30284 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07653900-93c9-3204-a6e7-a174dbb95539 | -15.3231 | -46.3736 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f6fda98-608f-3dc2-b826-33f5a8230bab | -10.33797 | -50.39634 | 2025-10-05 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a8673f3e-529d-3c27-a2a9-2e068f5558ac | -13.52783 | -47.28229 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2f0ef6d-650d-398f-9031-0140e05bfaee | -13.12193 | -47.98137 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4d4adbb6-f0b4-3354-9c5c-e4b9d3bdebfb | -15.37956 | -47.93673 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3ac03c9-ff39-345d-9451-ac32dbf98d70 | -15.6107 | -46.94732 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed27e2fc-e5f9-3978-b574-04152237f6ba | -15.91071 | -48.83505 | 2025-10-05 03:55:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fd13bafd-0204-3fce-91b0-3cd5c47c3e7f | -11.23092 | -47.7442 | 2025-10-05 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d61018c-e531-3325-80cf-4c7f9d5a1874 | -11.90287 | -46.23033 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75732452-e333-3bb1-98e1-637a7cf0927a | -13.12417 | -47.97635 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b313ea00-4583-32ea-a353-7ef5c2fc802f | -15.78083 | -49.09803 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11c07fd3-e7d7-3d2b-b3a0-26881c364d97 | -11.6256 | -45.02578 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f536ded-5ae5-3ffd-9b80-0d079c61a839 | -12.59124 | -48.14171 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aee96d0-e074-32d6-81e4-4f5b37c47111 | -13.26566 | -47.6022 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 21f2634b-453a-36c6-b945-2cee75b5dad5 | -14.65398 | -48.35045 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c557b604-1420-3180-8b5c-9874c01bcc79 | -13.30361 | -48.11515 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72f79b30-99c7-3561-aba4-a7b0a29635b4 | -13.27056 | -47.60248 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f6245bae-587f-3690-ac19-f5ff909d97cf | -13.26356 | -47.61349 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e3bfa291-674f-3892-9e1d-3b06eda90cf5 | -17.38921 | -46.64472 | 2025-10-05 03:55:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19d32333-b3cc-3800-843a-3cdd13acdaeb | -14.01645 | -44.92601 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f011a86-812e-3c8f-8450-6c7f82c00fc4 | -12.45321 | -45.52911 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df0212fe-f4e5-3645-9cad-83bbcdaae040 | -13.29691 | -48.1264 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e35c0fbf-c082-3f97-a853-de6e0035f25d | -12.58848 | -48.15619 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3e8b698-47c9-3d0a-8028-cb6d3d4a45a2 | -14.91314 | -46.87273 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bfad2c4-85c5-3aab-bcc6-b09429632e1d | -14.32342 | -47.69875 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a58e4f53-0f9b-359f-b3bd-926c0fc78530 | -10.79013 | -51.00354 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 57ca8518-8613-34c8-98df-8c4144d22452 | -12.13094 | -50.91911 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bdf62f0f-423c-32c1-9c27-978461e8b5c4 | -13.255 | -47.82042 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8fd3429-bbb4-3f0f-8862-8d9b1c241476 | -10.79962 | -51.00971 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 08234776-6ef7-3460-9c97-6eb804217bdc | -16.94877 | -52.68282 | 2025-10-05 03:55:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d969eee-c084-348e-979a-38d4cbfa622a | -14.31968 | -47.69258 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc0ba6e0-bf31-30a4-9ee8-39adfa926421 | -11.1157 | -47.17472 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e017fe80-1073-305e-8c40-9d22561fc131 | -10.50145 | -48.10894 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 213c0284-1f25-39fb-95a8-3473bddfe04d | -15.72667 | -46.26345 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e829c672-68f8-31ee-b5c5-c5e1a37afe37 | -17.72916 | -44.40046 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cae52bfb-552b-38f3-b918-602a1ecc49da | -13.35393 | -47.24435 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ea29980-9a2d-3b15-a98d-fa6c4986a616 | -11.75974 | -44.74074 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| fa54fe30-2ebf-3044-adf2-6cca2b93f760 | -16.06961 | -51.0861 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0becb91b-b63c-35f9-9041-add8843bad07 | -13.25226 | -48.48868 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c118de2-aa5b-3960-98cd-09b921d8b90c | -12.69926 | -45.85197 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bac9e8f-e99e-3da8-9192-db692f148fec | -11.68892 | -45.27916 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7503a55f-7817-313e-b5cf-ff6713cad82a | -13.62987 | -48.68444 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecae9e44-be34-3cf4-877a-a5f4e24bd269 | -10.03293 | -50.4049 | 2025-10-05 03:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2e6410e-38cc-3c98-8e89-8aa24181fece | -17.57194 | -46.08007 | 2025-10-05 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f269f087-360e-3333-bf17-30fae286ebf4 | -11.23907 | -47.78379 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 183cf467-4cef-350e-9b4a-359118112bf8 | -12.56118 | -48.16264 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30c08513-72fb-38f0-aae3-cd7d8b8cd84d | -10.73959 | -47.89839 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3486faa-5869-3936-935b-516093c60dde | -13.31696 | -47.56523 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0a8ef0f8-d16f-33ed-9f63-25513ecc4eb2 | -15.23359 | -49.30949 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e41e980-081e-3def-ae4a-6ec0a731fe7e | -12.59515 | -48.14851 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0168ff07-7dc3-343c-b279-075f3bcfff73 | -11.06468 | -47.78077 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a898f6f4-d036-3b1f-9215-3030b203d281 | -12.57621 | -48.16586 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae8038ff-d1c5-3662-9a4d-298a10146abb | -11.49747 | -44.98997 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae9d7ea3-dad7-3ab8-964e-539dfccb2489 | -13.48485 | -47.22877 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 063d0069-b4e8-3d38-bf8d-0ff10ff5d168 | -15.70633 | -46.27805 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6f894a-17aa-3597-8971-cb72d26a2001 | -12.46657 | -45.52768 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d2c987a-592b-32cf-b3bc-02c6bce60eda | -10.94571 | -47.05613 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1288adf3-9a0b-30ff-8d10-c4baa209320c | -15.73088 | -46.26422 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97b003f5-4101-35b5-a958-041394baf9ca | -12.46728 | -45.52368 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 04ec3ff7-25dd-3b07-b6fd-49cc206f17b5 | -10.84108 | -47.97571 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 2183226d-0a6e-3220-9a3b-33acfec2677f | -15.55337 | -46.96376 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README60.md)
