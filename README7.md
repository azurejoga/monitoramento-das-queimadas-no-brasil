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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c5c03c6-7e27-3733-b0ca-def59d34bf01 | -11.10425 | -48.88737 | 2025-07-21 04:19:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e67d946a-6489-3f0c-8790-cfcbef39c7d5 | -9.81406 | -47.7418 | 2025-07-21 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b40b21a-47d6-3f9b-8457-3040091bcadb | -6.89793 | -42.78106 | 2025-07-21 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fe914f3d-1a1c-3c13-ab7d-e5f776db51bd | -7.29345 | -44.36898 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42733a99-ad2c-33d4-8333-d13ffe56eaa2 | -10.18203 | -49.50809 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 73b781b3-c47e-3efe-a50f-f0de8d8da4e1 | -7.27218 | -44.26552 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f66bc12-b7a6-3d78-957c-0d55b781a0e9 | -10.7276 | -52.51778 | 2025-07-21 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac01b93-3bd4-3c2f-9078-515454799533 | -6.83195 | -44.86458 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9897bef6-db4c-316c-91c1-e8cde184a0bd | -10.33279 | -48.90015 | 2025-07-21 04:19:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d08e31b-76fc-3dd9-bbc1-591f3baf1b6d | -8.0825 | -50.0965 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7dce35e3-8353-3676-b9af-35c3efa8c9fa | -10.67029 | -46.77446 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96ac9025-b208-37f4-b422-820442bf7637 | -12.38223 | -45.87984 | 2025-07-21 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff90af62-b0b5-32ac-abbf-ce51cbbe72df | -8.51886 | -41.19727 | 2025-07-21 04:19:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c4cc2ed7-843a-3a75-9d5e-6aca4e3a266a | -10.66695 | -46.77393 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 384a1ed0-cc4e-3699-beb5-d36adc8f713e | -7.93338 | -43.94516 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be6b9d80-c7e9-3c07-bca5-618e099d3921 | -11.58203 | -47.23304 | 2025-07-21 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbc4fecf-47f1-3501-b863-11d2c101eb5b | -6.95758 | -44.38765 | 2025-07-21 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b38a63d3-62cd-3d24-9b2a-f7cedd646609 | -11.77912 | -46.45186 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ae8aa3-78b8-3e39-930f-89665e6eac67 | -13.23616 | -41.97577 | 2025-07-21 04:19:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e242b722-ce9c-323f-ad92-110f486047d1 | -10.68476 | -46.76955 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 747f662f-5e62-33c4-9eed-7794d667efff | -10.13422 | -49.65482 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ca0b7795-557f-3202-b006-8a0f892285bf | -6.6988 | -45.70337 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cef04bb3-8ab3-3747-b0c0-bf45067b4d81 | -11.9589 | -47.0266 | 2025-07-21 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ef5baaa-849a-32eb-a4ba-960b9842ea39 | -6.69581 | -45.70295 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbf149e8-fd12-33b7-9360-fc6748aae752 | -10.64643 | -44.48509 | 2025-07-21 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d859097-08a1-3878-b4fd-7e9ae4e97434 | -5.32674 | -50.57929 | 2025-07-21 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47dcc0cc-e806-3385-a08d-126e53ccf7e7 | -10.379 | -49.92656 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cefb4f8a-0d47-3c67-9fa6-8190431fc3c1 | -11.9628 | -47.02358 | 2025-07-21 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c12814f-2217-3b4b-8ac2-6e910b606ead | -7.96251 | -43.97185 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 509c9ace-2770-3eae-b252-007a2a9bd5f3 | -10.37818 | -49.93129 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9f7bd0b-9965-30da-8d1e-8906872c3527 | -11.38599 | -47.97792 | 2025-07-21 04:19:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 170a1717-ac29-328b-8bb0-7a3cd2b4edb9 | -10.65971 | -46.7764 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf96f598-0222-322a-bd13-d44933f47f50 | -7.759 | -42.16235 | 2025-07-21 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9215386-48ed-30a2-ab3e-bcd614568fe9 | -9.61124 | -43.86084 | 2025-07-21 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 339da6ca-f6bf-3675-bd34-91bef04cd7d2 | -6.78267 | -47.16211 | 2025-07-21 04:19:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e11c07f-0caa-38bf-bb02-eb2e3fe519c9 | -10.64699 | -44.48147 | 2025-07-21 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f920bc43-de37-390c-b9be-952e46184663 | -12.4844 | -45.87858 | 2025-07-21 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54bec8c4-a026-3667-9a40-fbed84ecc3a3 | -7.75961 | -42.15829 | 2025-07-21 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b22522ca-5e46-3bfe-925a-61027ae87b49 | -9.59212 | -44.50101 | 2025-07-21 04:19:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 737dba7f-7925-30af-bd58-94528817dac0 | -7.11484 | -43.28417 | 2025-07-21 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09d3b29b-140d-3644-b633-3bcf5e695063 | -7.27164 | -44.26902 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecee54a0-2c11-31dc-b49f-5cb6297fff8b | -12.41089 | -45.89171 | 2025-07-21 04:19:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cf3eaf0-3a50-3b21-8d55-4a9c379ec281 | -8.42467 | -46.8762 | 2025-07-21 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42019edb-8f08-3777-afdc-f49ae98da2cc | -10.12968 | -49.65876 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ab185d2-e22d-3ad9-9831-74f8cd02f628 | -6.64879 | -45.01218 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f57a46a-8104-388b-8431-676b0eedf7b8 | -9.94328 | -46.26477 | 2025-07-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a394c461-1cd4-350a-aeab-6006d75cb1fe | -6.20968 | -44.30569 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62e7d1fc-42f9-3974-95ff-0a729104bf39 | -6.89852 | -42.77724 | 2025-07-21 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d1cf0fa9-f0ee-3891-af0c-a3e2aafddb8e | -8.26853 | -46.06981 | 2025-07-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c2d2efa-ab62-3e45-b070-44626026bb3f | -7.75481 | -42.16587 | 2025-07-21 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 93dfd066-e129-35a8-ba80-80ee2fc6f52d | -8.04209 | -45.41919 | 2025-07-21 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acd65463-ab5a-310c-99d4-a81bcdc7fdbd | -6.20382 | -44.38634 | 2025-07-21 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f8fbbae-5963-37c3-8958-4bfae7a40e45 | -12.46896 | -46.92069 | 2025-07-21 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d630dd-a054-3d41-a9bb-a0c3932504e9 | -11.96223 | -47.02715 | 2025-07-21 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faf08145-ddda-32d4-8aeb-2f5034a29894 | -12.37385 | -46.43016 | 2025-07-21 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73433fe1-420b-320c-b0c1-92d61fa1c1b7 | -6.44651 | -43.50462 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33117692-8a6f-39da-ac70-5ee2cb357804 | -8.91801 | -47.36144 | 2025-07-21 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb7ade63-8db8-3790-a833-96d9f7ea370a | -11.61801 | -44.22387 | 2025-07-21 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7ff3e82-066a-3bde-812f-da2ee3ef7f46 | -8.94292 | -44.43977 | 2025-07-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 305e92d9-c243-3e6e-8cdb-f83deede707b | -10.67419 | -46.77146 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94aabf6a-5b28-314e-b524-7a08c4751d74 | -7.96361 | -43.96471 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f76920e-1044-3231-b23e-a6f437c85c06 | -6.94819 | -44.38258 | 2025-07-21 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24b207e6-10fd-31a5-bcec-636a93f32635 | -6.49782 | -43.52003 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b29a78ce-a51a-3e14-819f-bd270882286d | -11.78531 | -47.55433 | 2025-07-21 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae0b5a70-efb7-321c-ac60-86e3bc11f44d | -8.93795 | -44.44979 | 2025-07-21 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8f43a55-986e-3436-9cd5-305ab5554d85 | -12.37166 | -46.42258 | 2025-07-21 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f4e9a36-e29a-3fab-ac90-ecf68e92d7de | -7.05945 | -43.50986 | 2025-07-21 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0474c171-3237-315d-977d-5af629a14c3e | -9.60617 | -43.87142 | 2025-07-21 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb84a9db-c473-394d-966d-a12dc3fc79ce | -8.26908 | -46.06633 | 2025-07-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa07d22f-8323-399d-886d-a63d18c7d055 | -12.46508 | -46.92369 | 2025-07-21 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aef16c21-6b4e-3473-9e2a-4963aa5a936f | -10.73207 | -52.51859 | 2025-07-21 04:19:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a43d5202-6ecc-3c2f-9deb-9599ed7c2813 | -7.4396 | -44.28089 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29234dfd-abb5-3147-8885-5641947fe77f | -10.6881 | -46.7701 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86927aeb-e473-313a-8a58-8905cf1da8cd | -9.61895 | -49.01754 | 2025-07-21 04:19:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f0aec4d-72ef-35d6-94ff-055640d6d3f1 | -7.05173 | -44.87132 | 2025-07-21 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9100e3b5-22ba-330d-ba36-b8b1cd6d05ff | -8.71097 | -47.85857 | 2025-07-21 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8cf2978-1ae1-39b5-a72e-0d33f538aadb | -7.41362 | -44.29474 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ece89e4c-6663-3e29-a93f-207168a97c0b | -13.23394 | -41.97789 | 2025-07-21 04:19:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e40df722-bb8d-3d60-b9a0-c8180c598810 | -6.46551 | -43.49298 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be9ccc40-f226-3384-82f9-d3c3330405bc | -11.778 | -46.45889 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1600344f-0111-3ccf-8576-5e9399972bfe | -12.37441 | -46.42665 | 2025-07-21 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ff9e77d8-b1bf-3860-bc2c-5ccb25386f5e | -10.14471 | -49.66146 | 2025-07-21 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76d07c7c-0924-3acd-9683-a9dfe1685cb8 | -11.78194 | -47.55376 | 2025-07-21 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1c0f682-e330-3f6d-b08e-777fd20ad3a3 | -8.27212 | -46.06711 | 2025-07-21 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7e811aa-31a3-3552-9e0b-4c5a4038dbbe | -12.14259 | -44.77547 | 2025-07-21 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4da35cb-a3a2-30ee-a4e4-1e6cf707a613 | -7.4103 | -44.2942 | 2025-07-21 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78de0d0a-caa6-3e97-a6f6-c8b03b57b07a | -9.08511 | -46.44401 | 2025-07-21 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a3e77bd-9715-3468-be3c-20789a24c3fd | -8.00157 | -43.69441 | 2025-07-21 04:19:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b83ca0da-9616-3da6-a83d-5786a5064e6e | -11.78928 | -47.55122 | 2025-07-21 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a0c7e2d-2327-36ce-890a-79b65978a792 | -7.55665 | -44.5533 | 2025-07-21 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb52c6f9-e61a-3eb5-be92-efe38fc2da87 | -7.94569 | -43.97627 | 2025-07-21 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9c443a4-97cb-3d0e-8e85-7eff2e03fbf1 | -11.77744 | -46.4624 | 2025-07-21 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f34dcbd8-dba5-36f3-8d4e-1307df9ab513 | -6.64994 | -44.16163 | 2025-07-21 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ca3744a-8a71-39f5-926e-925fdc835656 | -12.48165 | -45.87452 | 2025-07-21 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7a6b897-4206-3ee5-9ceb-fe12463c24ee | -7.75543 | -42.16182 | 2025-07-21 04:19:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 742a22e4-7469-361a-8f51-8985e96bd5eb | -11.14363 | -51.93531 | 2025-07-21 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8455fa3d-8cee-31e2-a279-8cbbb8db9c5b | -6.50118 | -43.52058 | 2025-07-21 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52e1339e-0dd1-37fb-87d0-38494c432baf | -6.95151 | -44.38311 | 2025-07-21 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 977a6881-57fe-388d-a2c8-c8421a1cbdcb | -10.67753 | -46.772 | 2025-07-21 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dee643de-7895-3f7e-b61f-1cf7b549ba12 | -9.61068 | -43.86454 | 2025-07-21 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
