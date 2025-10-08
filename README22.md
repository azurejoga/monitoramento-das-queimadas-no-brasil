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
| 39f8e6d7-6086-39ab-abc6-b2907687f3b3 | -15.25821 | -46.34319 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b82b8e0a-12da-3fd9-91ea-140b574b47c8 | -11.78929 | -45.04907 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a8abe37-e86d-3454-8d07-93bd8f0f300b | -12.78997 | -48.82156 | 2025-10-08 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c84220ee-2432-32ce-9ac5-1d1e3013444e | -11.18999 | -49.77534 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c72296c-c10d-3d38-bc0d-78bbc1fa8803 | -13.07146 | -47.93024 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb4614a5-e054-3536-94e1-c31c378c43a8 | -13.74974 | -45.75669 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36332d5d-4a17-3924-9a5d-e2035ee98d77 | -13.36515 | -47.55992 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a80066cc-a9cb-3aae-81d2-4467b389318a | -14.95406 | -46.83671 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4eb80fa7-3735-386a-8837-1140309c306c | -13.35987 | -47.55921 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6649b26f-d441-3587-a03a-86c00a781950 | -14.79744 | -46.07787 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2272d10f-d28f-33e2-81e9-0a3a61b6e09e | -12.91996 | -46.82277 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a998cf84-0eb9-38b8-ae15-08b41d8a47b0 | -15.08481 | -46.62153 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5a4108c-2f4e-3819-b3aa-6728878693e6 | -15.30663 | -46.16655 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 111f7a0d-976f-32e5-8bff-92809c410f61 | -12.37729 | -50.30439 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5af5de13-aa01-351c-b3b1-de1a298494f5 | -13.271 | -47.56879 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98313365-6100-3543-bf49-2e87f13c09dd | -11.7167 | -50.94661 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 6d54b4ba-c9e9-3619-8650-d73d0711397c | -10.68565 | -40.49489 | 2025-10-08 03:49:00 | NOAA-21 | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 88a0f7f0-8870-3439-8570-0360f485618d | -13.00446 | -46.78717 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| df4a4a3c-aa3a-3859-b49f-f9975233447d | -9.77575 | -48.28979 | 2025-10-08 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51d1d16a-6453-320f-b67b-b2580d60cf3a | -10.72917 | -47.65537 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14a8a993-7805-3900-8cb6-609db0669246 | -9.39891 | -45.93942 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 355a6071-bea7-37ec-b18e-4d327719114b | -12.02062 | -45.20563 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bc6f5b13-34c4-382b-8374-5082163ff787 | -8.55517 | -46.23447 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e306ab4a-f5a5-3f26-836c-a7888510a097 | -12.02607 | -45.20168 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 918e4fa1-413d-3bcb-83f9-a0477071033c | -11.70886 | -50.95112 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 24e09f20-d438-34eb-91eb-3388ef899270 | -12.78671 | -48.81555 | 2025-10-08 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c303aee-3d2b-3c3f-848e-20029597003b | -13.06627 | -47.94059 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c0afebe2-db09-33ad-b4d3-df586290dbee | -11.5153 | -51.49273 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fabcc98-ab72-38c8-97d3-8dc37d369ef5 | -11.84747 | -44.91043 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e157fef-9daa-3e46-a87a-973633c4c24c | -13.22358 | -47.17585 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7889fb9b-ecb5-3f80-a29e-4f346d3240bd | -12.39086 | -51.14436 | 2025-10-08 03:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ce0ba63a-31a0-3275-8290-577605aa01b3 | -11.71792 | -50.95194 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 25d1234f-df84-399b-a34c-0e5a3d16b662 | -8.22211 | -44.19704 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b12284e-2c2c-312f-be12-04542495e40f | -9.77398 | -48.29485 | 2025-10-08 03:49:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dda1890-0ec1-3f9a-8630-e555237d482a | -13.28368 | -48.04149 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f07071fa-df82-3a36-8327-a8b1a9ce87bd | -15.56548 | -43.8429 | 2025-10-08 03:49:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98883e4c-be80-322a-953c-123096100fcf | -10.94194 | -51.03479 | 2025-10-08 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ac87862-96f2-3f93-8e98-65ad1f379122 | -11.90923 | -46.74831 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4681182-ebbc-3b5e-b537-89aec6021282 | -12.02237 | -45.19606 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55728426-7409-386f-8df7-a130102c82a0 | -8.23125 | -44.19598 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cdee3711-854a-34f9-bb59-732e789fe107 | -9.20808 | -46.89502 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fedf0fb-87e8-31a8-ac81-a94daf13a0bf | -13.07913 | -47.93215 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9417354-8aa0-3a30-9d81-d67393f4e72f | -12.23906 | -43.77945 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27823b1a-92bc-3382-8142-1a6a1176c915 | -14.915 | -46.81232 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4f32808-ca87-3ca6-bf5c-19ea4b4d7515 | -9.18085 | -46.92167 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6d159766-a4bb-3aec-b22b-961f59cd07b2 | -8.2275 | -44.19043 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c3db7408-4679-3449-af59-cabeeb1b0f8b | -11.70652 | -50.97416 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3db0e8a-59f3-3d54-b33c-635a1066b260 | -13.45744 | -50.40448 | 2025-10-08 03:49:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9e844ae-67b2-342e-9b7a-e91aa75ef6e4 | -14.95452 | -46.80861 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b5793c0-98a7-3f15-a5ea-141103af448d | -13.06819 | -48.01488 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a20738db-f050-39a3-9c04-0990cbf7166d | -14.74649 | -47.86062 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85ade3cb-b0a5-39a8-8e36-f7f419061dca | -14.71438 | -46.0681 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d8ff8e3-d10f-3a52-847c-a514fd783018 | -12.9383 | -46.86334 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a956de2c-0dc3-32aa-98c9-6bd029990585 | -8.46816 | -47.20164 | 2025-10-08 03:49:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88be4167-dc6b-34c4-8f00-5b17326e6ee7 | -12.41693 | -45.62715 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 51c98fb8-f31e-3a98-a209-34d48b182291 | -14.72 | -46.03809 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ccd647c-fffb-3638-84cb-6dacd5f865d8 | -11.69192 | -50.96607 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4883a948-f9f0-3cef-a2f1-d18276108c68 | -8.23457 | -44.17995 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5a320570-6038-3038-aa16-32a30c521ddc | -8.52834 | -46.23402 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adb0ec9c-1bc5-37ec-acf8-f77f4680abab | -12.78588 | -48.81961 | 2025-10-08 03:49:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 655b6e77-1018-3c76-afa6-59964dbc402f | -9.20214 | -46.89705 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 408753d2-7e86-3e57-8855-bdb241281c8a | -12.32371 | -50.2637 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 109e77f2-7d07-3acf-8044-53ace1f31eaf | -14.44379 | -48.7901 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a40c7efe-47cd-3403-ab72-7aec9722426c | -11.77252 | -45.13966 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c23f8364-71b8-3322-9429-7967d4efd1be | -3.43015 | -43.14722 | 2025-10-08 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65242a73-5abb-39b4-ae22-25af560e54f6 | -8.52307 | -46.23336 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19800b7c-51c2-33c8-8879-73d0ec1e59db | -11.73407 | -50.96244 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| f28a67bd-58a6-3f45-b199-48d45d13e4f8 | -8.37557 | -47.05818 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75b5aec6-b453-335b-b635-e5f1ec604570 | -15.26569 | -46.32944 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a73724b4-3aea-31f8-8451-a7cdd2d2b57e | -12.21885 | -44.25728 | 2025-10-08 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d303227a-4425-3742-a787-f787fd011ea4 | -13.36477 | -47.227 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fafbf70-cd9a-3feb-9ba6-ee2d6eb0b9d3 | -13.3712 | -47.5555 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e93f1ba0-4972-38ff-8b9f-8bd16e909c40 | -9.42229 | -38.83373 | 2025-10-08 03:49:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cd92c71-bca9-3ecc-8f45-680e0d244e08 | -13.22905 | -47.1886 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8375c6ec-e384-3533-8502-24f81524a535 | -13.22849 | -47.19162 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 09a6cb50-ad20-38f9-a890-b31a97137413 | -12.23779 | -43.78654 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b049797-fa8c-39f7-8a84-4d64285e9e79 | -13.06693 | -47.93727 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b19e360c-36c2-34d7-aeb4-e1712d6c5b17 | -9.39443 | -45.93541 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c075e53a-7a84-30ec-92b1-3022080ac55e | -3.24293 | -46.78912 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b2329b0-59c8-3a66-b6cd-b42983ee839f | -12.37394 | -50.30658 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2261d438-0548-362d-83d2-8d0f8b9ee51b | -9.18278 | -46.91132 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 98d4d90f-f06b-3389-b186-b61731aa819d | -8.51876 | -46.28592 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d914d424-35eb-3e27-b5f4-2a96655c3a03 | -11.71975 | -50.97692 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 073be18a-9b95-3bf7-972c-c752349fbaa1 | -13.28845 | -48.48333 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81ae1f3e-13c6-3d1c-b309-43bc03776030 | -9.19339 | -46.9142 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 797fc296-a778-310a-8c2f-c07aedc68e93 | -11.73773 | -50.94485 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a6ad1c59-e4ea-382b-9be4-aa480e76be1c | -3.29148 | -42.62257 | 2025-10-08 03:49:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f116ed41-c2fd-3afa-9e27-e47fac48b061 | -14.91308 | -46.81523 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 006df60f-33e0-31fa-bc1d-d7da1f6c3a97 | -14.75224 | -47.85886 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce447270-f736-3074-b7a2-e8b9699fef8b | -8.23003 | -44.17907 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c8cd412e-a4b1-37e6-a772-84c18b718e77 | -8.23087 | -44.17438 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4083682a-c977-38af-bc27-5fbfdc1b2fb2 | -3.44596 | -45.59196 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9aa4353a-20eb-33e6-af9d-399d3cd877f6 | -9.79432 | -47.74876 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 025df37c-e029-39d0-a782-20c3c1cdbcf7 | -13.2573 | -46.47166 | 2025-10-08 03:49:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 540f01b9-1bf9-39b5-a6ea-ba48874ffbfd | -15.30766 | -46.16117 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddc9dbc8-e6ed-3166-9e61-29a8629289b2 | -11.50101 | -44.96829 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7c78b45-a93c-3982-b0b1-ce47998d3df4 | -12.94443 | -46.85844 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8a1555bd-0660-331c-a444-32aaa302ed09 | -11.45441 | -50.21804 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6b72aaa-0513-39c3-b0e2-00b011dc8d9f | -11.81531 | -45.13839 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 427f070c-eb47-35cb-9654-058c1f9608cc | -15.94758 | -42.60338 | 2025-10-08 03:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
