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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb45810b-af3b-329e-99bd-d63be617bc03 | -13.68871 | -43.00534 | 2025-11-14 03:55:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a79a418b-d0f3-3c98-9dab-bc89940c2721 | -14.94053 | -49.79161 | 2025-11-14 03:55:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 05623386-0ad2-30fb-a05d-607ce671e643 | -10.75928 | -44.91109 | 2025-11-14 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ae844a-34f9-3f5e-8772-c573399ea6ac | -4.61391 | -43.38531 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fd2b154e-96bf-322e-838d-b9f1a57d84d4 | -11.99179 | -44.28988 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7d99d336-999b-3011-8d03-30599d7b8ac9 | -12.01777 | -46.7655 | 2025-11-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 839cb469-642d-329f-872a-b1e4b01d8308 | -13.46584 | -44.03444 | 2025-11-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e92a80ea-8faa-3386-bf27-b3ee2ff329b8 | -8.94584 | -49.81309 | 2025-11-14 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef233538-ee45-38be-8fa8-6f965f29d946 | -9.05064 | -48.71778 | 2025-11-14 03:55:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7cc7128-7d1e-322b-b09f-126e3a9799c1 | -3.74521 | -44.27505 | 2025-11-14 03:55:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e49e2459-aa57-3844-a5b4-3fd0ec5968c2 | -12.59999 | -48.37404 | 2025-11-14 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2697575a-1a88-3c7f-a217-727d8f6239bc | -3.7738 | -47.72564 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d5c7b73-f7d3-3529-a349-ab00b63e3f39 | -10.3243 | -44.27915 | 2025-11-14 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe77ef13-1369-3ad5-a8d7-a18751b84d5e | -3.26785 | -43.52471 | 2025-11-14 03:55:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d52526d9-fca8-39ec-bd04-4ed21c06dd89 | -11.94526 | -44.59415 | 2025-11-14 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9aa78b65-ce25-3308-bfd1-dc24b9d377a5 | -4.81797 | -38.6435 | 2025-11-14 03:55:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87ee06d3-9f20-3752-a237-f15e12e03c28 | -13.6825 | -48.4223 | 2025-11-14 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dd59cc9-6039-37da-b41a-4e46be1e33d5 | -3.80046 | -40.96276 | 2025-11-14 03:55:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6e96dd80-9674-3dc2-a567-542df879be3e | -9.35601 | -46.60196 | 2025-11-14 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a966bf21-c7d2-3b33-9390-e613e23fef58 | -11.99082 | -44.29187 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d8ef2ad-d9b9-3130-9b41-5f0b8d88dbdd | -11.99261 | -44.21342 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2895acb-4841-3125-b235-42dc3ae28f4d | -10.8833 | -44.39116 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cabf379b-6567-3d8a-9c39-47c1775692e4 | -12.82822 | -43.44503 | 2025-11-14 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 773c1772-2080-3843-8cf3-b546ebba2684 | -12.69195 | -45.43354 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c52affa-e7f4-3fa4-9bbe-e1a4410c088b | -11.66561 | -48.4636 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e89f59eb-3d85-3ea1-9dfc-764876da7e91 | -9.25063 | -45.20067 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04581235-29de-334f-b32e-c2c085f70d5c | -2.96054 | -45.7556 | 2025-11-14 03:55:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4505ae7c-1d6d-3ff7-ba31-b56e2d730750 | -8.54192 | -49.58234 | 2025-11-14 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02730434-da88-39ee-9495-e1daf037e668 | -12.58869 | -43.35691 | 2025-11-14 03:55:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f033d5a-609a-3c91-8a7e-56691b5d63f6 | -3.43331 | -42.42532 | 2025-11-14 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93061962-56de-3ef7-8de9-605a523e3152 | -10.62905 | -45.00922 | 2025-11-14 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 130d1bd5-66af-3383-90f4-f32aa46b946e | -12.45166 | -44.63802 | 2025-11-14 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d9b411c-8c4d-3c78-97b2-88a421624e80 | -11.7385 | -48.53746 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d889994-e3cc-37a7-a9d2-88da8b7d9124 | -9.66756 | -43.89365 | 2025-11-14 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6dcd13b7-16ce-3c38-a836-19275e14e3fe | -10.74426 | -48.17815 | 2025-11-14 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a071494-d013-376b-bfac-76b369d1d73d | -12.78489 | -43.62936 | 2025-11-14 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76b63cb3-8677-3953-b878-7abcaea196ed | -9.00711 | -45.45309 | 2025-11-14 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5f7367d-6be9-3945-87c4-8c40b3dcdf38 | -9.05982 | -44.77977 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6dbaed66-f323-3a5d-bccc-f14c9bf0aad3 | -2.46592 | -48.2275 | 2025-11-14 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f6f5353-e9c5-37d0-ba8d-08981e480e82 | -4.04579 | -46.12972 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b180d72-17d3-3b23-859f-03e523613948 | -14.70016 | -46.61203 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 312057a9-b211-3805-ab12-66e679214c47 | -12.07323 | -48.20736 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8523610-7550-3c7d-a4b9-7fdafe9dbf46 | -13.37582 | -43.20852 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 955f0bba-5a64-34fd-a27e-1ad079b317b6 | -11.94463 | -44.59771 | 2025-11-14 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad11a021-fe1f-3be0-a50f-06af86857223 | -11.03468 | -44.65052 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d182313e-0758-3fa6-9ce8-a3c3a193349c | -5.39944 | -37.86508 | 2025-11-14 03:55:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cfb7c0aa-c25a-39dc-a1bb-674f149bc434 | -11.74616 | -48.52544 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9da8680a-c870-35d3-a617-e097456b6349 | -15.21322 | -43.4823 | 2025-11-14 03:55:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88e2acf5-e456-3743-a2a3-f57e6cd86c15 | -10.37343 | -47.68568 | 2025-11-14 03:55:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b725447-b298-3456-a2ac-d8735d3686ce | -2.51856 | -47.80672 | 2025-11-14 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac07bacb-10e6-3ac4-b979-d75ebf0aecb0 | -3.76674 | -46.00861 | 2025-11-14 03:55:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6839cfac-a9f2-31eb-ad13-1668fe7f66a4 | -11.24466 | -47.49934 | 2025-11-14 03:55:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41dd396d-f472-312f-a422-52b30e00d4d5 | -14.77524 | -46.67355 | 2025-11-14 03:55:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2c7f4f2-467e-316c-9189-7f3fff5a1b32 | -4.71626 | -42.9388 | 2025-11-14 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d9517fd-4f2b-34ac-9370-be849ea6ee01 | -8.69061 | -44.39466 | 2025-11-14 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f89fb6c9-686f-39f6-a27b-8f0e5ae53f10 | -3.57417 | -41.72315 | 2025-11-14 03:55:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75dd77ea-5c34-3067-91d1-df1188b3cac1 | -3.76424 | -47.74773 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0824cf58-81d6-300f-b61a-20da89fe45e3 | -3.76489 | -47.74389 | 2025-11-14 03:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7022551e-b783-3a78-9264-4b6f53690519 | -9.98774 | -45.14821 | 2025-11-14 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82f2e2aa-4934-3e1f-8ba5-2f74c18899b8 | -14.70365 | -46.61761 | 2025-11-14 03:55:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c632c8f0-677a-3875-8b33-ad2262958fb8 | -10.80332 | -44.85484 | 2025-11-14 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b00848eb-23d1-382f-90d0-ba5d54458464 | -11.17126 | -43.57439 | 2025-11-14 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b7954b9-3ab3-3144-b76b-f373a96096f1 | -11.73633 | -48.5202 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 803604f4-b1bc-3f55-8e62-74cefad98719 | -15.30101 | -47.3817 | 2025-11-14 03:55:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a97dac60-f1ba-3a1e-b2a4-7b847c7520bd | -15.78537 | -41.4685 | 2025-11-14 03:55:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86f1c0bc-9f5f-3df4-b943-4fdbafd0a0ab | -11.73502 | -44.66793 | 2025-11-14 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c9f3ed5-e97f-381c-aa53-f2c3848ce888 | -10.37848 | -47.6867 | 2025-11-14 03:55:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 236cab36-13d4-3148-bc82-f21c1be34b0d | -9.99027 | -45.14851 | 2025-11-14 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a33aaf3-7cb0-351a-a142-d4b2896c695e | -13.68756 | -48.42298 | 2025-11-14 03:55:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725aa99b-b2eb-3817-8487-e77d15f9c153 | -13.97768 | -40.60126 | 2025-11-14 03:55:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 25b3f7c8-5c27-31ac-9c42-d1fb8fa58a0f | -13.50168 | -43.64264 | 2025-11-14 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f0fd413-8048-32ad-83db-ee27b2c243dc | -11.08354 | -44.84911 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08fe7136-49da-3bec-aebb-6c52208d0091 | -11.66565 | -48.46613 | 2025-11-14 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82c591a6-25c1-3b82-ab8e-80b4a748f18e | -12.62649 | -48.40121 | 2025-11-14 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a99149b-a7db-3fb7-8e9d-7d89302aa1e1 | -11.9922 | -44.21637 | 2025-11-14 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57a34997-5eae-3825-9c37-9c1ece8fd5e9 | -4.45649 | -43.47467 | 2025-11-14 03:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a5b7131-5ba1-36f6-9787-a129c9b598eb | -12.62642 | -44.14143 | 2025-11-14 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7fc221f-819c-3e0f-bd85-e1faadeff444 | -13.97711 | -40.60484 | 2025-11-14 03:55:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 15f040aa-ec3f-3245-b7ca-8857b1426da4 | -5.16298 | -37.57368 | 2025-11-14 03:55:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac6060ae-92ce-3c62-b3eb-5cc6a1136e71 | -9.66696 | -43.89713 | 2025-11-14 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| abd31141-96c5-3328-88e5-b37732667fcc | -12.59676 | -48.33589 | 2025-11-14 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0011b64f-ddc2-3ce6-9483-cfd5511a35fa | -2.45451 | -48.81933 | 2025-11-14 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d9f1490-145b-34af-8b32-b8a869476252 | -10.92379 | -44.58923 | 2025-11-14 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7e4f9fc-5ab7-37a9-b510-eca4edf754e6 | -12.32547 | -41.09273 | 2025-11-14 03:55:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc5f8ece-80e3-3e20-a6e5-1301cb85bb3f | -3.36191 | -42.44885 | 2025-11-14 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38240e48-499f-32a1-8137-01e7dcb1a734 | -12.04589 | -49.44128 | 2025-11-14 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eabcf2db-44ae-3803-9dd5-e41a5e632d33 | -10.08814 | -36.45201 | 2025-11-14 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6d4503bb-49cf-3582-b469-43742ae098b8 | -12.7066 | -45.42405 | 2025-11-14 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d3611a33-07b8-3155-940d-5b5728741951 | -10.29017 | -44.3563 | 2025-11-14 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f65f2915-51bb-3d5d-9fcb-9701977200f5 | -3.39183 | -41.14692 | 2025-11-14 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cf948084-f0db-3bae-b63c-e87763a59946 | -4.07201 | -44.13469 | 2025-11-14 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45c6441b-a67d-34be-8c61-0bd199945f11 | -3.45773 | -43.18194 | 2025-11-14 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af882520-321b-3e7f-85b5-32d67f60e2c4 | -3.36041 | -48.3961 | 2025-11-14 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0df4f0f4-2650-3600-90f1-33b33878702f | -3.46549 | -43.1871 | 2025-11-14 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29646c7f-9319-316c-ac9a-e395111b0d67 | -4.12815 | -43.00854 | 2025-11-14 03:55:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71209562-a207-3283-80d1-412fbb2acfdd | -3.25334 | -43.29277 | 2025-11-14 03:55:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bdd9bc55-254e-30e6-b8ae-b2cac56e54d1 | -9.14217 | -45.17467 | 2025-11-14 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf672a3a-e268-32f6-95e8-020257680ed1 | -15.24891 | -47.94459 | 2025-11-14 03:55:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01d21b9f-13a1-358a-825b-3c79cfab6b6a | -12.00304 | -46.76764 | 2025-11-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e965a101-4ebe-3630-be6f-048fb2322f16 | -3.4613 | -43.18644 | 2025-11-14 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README23.md)
