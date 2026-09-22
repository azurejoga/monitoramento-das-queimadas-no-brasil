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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c52298f6-0d76-316e-8a55-343cd84ae71b | -9.6203 | -43.94546 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c8ac5d20-2018-3a63-a41b-b3dc2a9576ef | -6.69744 | -59.95736 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dedd129-43be-3579-8050-12c3cf2e10bf | -8.2529 | -55.25019 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cda44e8c-dba4-3fff-8aca-bbc3cd854eca | -6.67667 | -50.94839 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ad29457-fbac-386f-8dba-c96141e69dbd | -6.78492 | -48.68052 | 2026-09-22 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99aaf808-75f2-36b0-a71f-3415d517c3f3 | -3.45178 | -50.5998 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e581b19d-a0ac-363d-87c4-9ecf208d42ef | -6.78481 | -55.61113 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c9aa5e-a2e2-3fdf-b3b4-4756151345cf | -4.64169 | -50.99486 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54020375-f8a3-39a5-ae2d-3f229ad7ac2d | -10.79277 | -50.8422 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7691c85f-e494-39be-bf30-b609fe1d781c | -7.83026 | -45.25742 | 2026-09-22 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a13f4a0-5d31-382b-b00f-c314c0ff9cf3 | -6.57717 | -44.1502 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3d8d75ab-898a-33fc-8228-d812502732d1 | -3.90256 | -51.88665 | 2026-09-22 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03f9a358-0ebd-3ce4-b899-c23e1d2ba290 | -7.38295 | -46.03675 | 2026-09-22 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9427047f-67e6-3faf-a4c5-bfb49fe96a83 | -3.68791 | -60.57428 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a33f3a8-f640-3ac9-b490-5115137d7e56 | -11.54954 | -45.36915 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e91bba4e-49e8-3192-8d2e-883b89dd3a17 | -4.14197 | -51.10263 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 660d5cd1-74b7-375f-ba7f-c143e374c754 | -10.20161 | -44.15396 | 2026-09-22 04:46:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 11196ab9-958b-3579-9444-40e661c486bb | -4.87258 | -55.8419 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 291c48ba-0f39-3b3a-bfb2-92cc5185a7a0 | -6.43138 | -55.60944 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3f76454-2b99-3d80-a8c4-5a165ba8554d | -5.9815 | -44.72233 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f2342bd-4477-30de-8e1b-3e86d4817b0a | -4.97081 | -55.82932 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3366d7e9-522b-31c0-95f9-7666e06ba217 | -3.00249 | -54.16877 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f15d171-dd04-3aa9-8747-c404ae506b7c | -6.51607 | -44.05247 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d1464ee-d003-37b1-8f51-cf68f54b226f | -6.30759 | -57.7389 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03823cd7-e931-382b-a80a-74ed392f5d9e | -6.0956 | -57.6821 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc765636-66d3-3042-a4a2-a3aee6a5fe6c | -7.2461 | -55.58818 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1879058c-3f89-37c3-ab9c-d9a4425f0314 | -6.64474 | -59.92566 | 2026-09-22 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| aeb0a8f6-355b-3b01-9759-8eaeb87e35a8 | -3.44687 | -50.60959 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c9438e8-38b9-3499-b633-63d7efc94d37 | -6.45038 | -54.99789 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c9f5439-57df-3341-9db9-2ef42e07c6aa | -3.51702 | -56.90804 | 2026-09-22 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a330cab4-9cdf-3c3c-bfd0-83b11ee785b6 | -3.51308 | -59.57935 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edce953f-88b1-3764-a728-43d6db17f1f2 | -9.20452 | -60.28804 | 2026-09-22 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51654394-d6e2-312a-8463-8a54f24fbbb4 | -7.33331 | -55.59986 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 393c8c94-df2e-3179-87f9-7459357ef304 | -3.45347 | -50.61061 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0e7e14f-fb4d-3fd8-ae28-cc50a7b026ba | -8.62021 | -54.63556 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 817114bf-4c7b-3fc2-9254-1291cc6b1c09 | -5.32215 | -43.42442 | 2026-09-22 04:46:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a877ec3e-4125-33af-833b-3857a11d3d11 | -5.73635 | -53.4653 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9da5b471-af49-3ea8-ae2e-f6483930b9e0 | -7.25145 | -55.5795 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e5c3a25-ef8b-35d4-90ad-68f7c1e34c67 | -3.39207 | -50.43602 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a2a9c72-ec64-347a-9098-7d942e093f87 | -6.00911 | -47.90034 | 2026-09-22 04:46:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2cad3465-95d4-3e1f-9377-2312bcaa0f00 | -8.35151 | -50.869 | 2026-09-22 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 573f8a67-7339-34d4-82a4-ed1e424f91c6 | -8.31588 | -50.9459 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a19f644b-88da-3984-be4e-34ad5b040ffe | -10.868 | -50.16079 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b654d8e-c90e-3407-9728-53e602cb3778 | -6.09232 | -57.61947 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 933071c1-5149-3d94-af8d-57c474a1e2a1 | -3.46511 | -58.33025 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5588bbf-40e4-32a1-8ceb-80d443eb155e | -5.84944 | -53.55032 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0147ab50-3ee1-34f5-9d03-1b48b05f733c | -4.77906 | -55.69746 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7e54ca3-9038-31f5-9664-057ed3bfefbb | -6.399 | -55.25948 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05f2b1e9-449e-32f3-82a0-0b43655af440 | -5.99475 | -44.72425 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 26771925-34ac-37fb-864f-c4c85b26a7a8 | -5.76746 | -57.45326 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f6895ff-44fa-3af1-9921-cf7e00d699c3 | -6.32431 | -51.85198 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1abd1b2f-da30-3362-9726-4d5c2e6d9d9f | -7.13489 | -42.08314 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 94ba2818-8e0c-3008-b6b3-dc8d64fea8f6 | -8.62443 | -54.63206 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02041148-d94e-3675-bd86-663b99944d86 | -5.59693 | -48.23043 | 2026-09-22 04:46:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 908c4ab6-ea88-3247-b589-0ccd6b062079 | -9.90144 | -48.41891 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3226b4d-75f7-3df4-baf2-6d42da727dbb | -6.29661 | -47.65569 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e8ccc482-eefc-386b-a5b9-9f10ebad77d8 | -6.57121 | -44.15919 | 2026-09-22 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 567bab3d-79c9-345a-98be-50268bb3174a | -3.78753 | -51.34426 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9639279-3da1-394b-8531-274bcd8beec3 | -7.12717 | -48.43099 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4da9c2f2-6aee-3b56-aff7-273e656ea9c4 | -3.44489 | -50.66553 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1384371-562e-3f7a-b1e6-5abc67199364 | -5.72979 | -52.23259 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7825ee38-804c-362e-b6d4-eaea4c78d779 | -6.07019 | -57.87508 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e6c0a32-8817-3a57-89ed-28f6de1160d7 | -3.36095 | -50.76514 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30713d1a-8ed1-30e1-b23c-52ac4a4bd102 | -3.175 | -58.59505 | 2026-09-22 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dfeb467-add1-3e18-a6d4-92b0de21c3d1 | -2.97199 | -54.15599 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b8e7fd1-692e-39cd-bb51-143729d7e663 | -9.02841 | -44.91106 | 2026-09-22 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5a31707-e089-3aa1-8b64-222c8a614967 | -5.87065 | -53.64137 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1c0c63c-d313-38b4-9e32-6a5326cf3019 | -9.57649 | -46.54279 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b214b44-43eb-3519-8831-a52caea33d8a | -6.94087 | -42.90643 | 2026-09-22 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4da3286-7d7f-3f62-9baa-8a7b5ce4fdd6 | -6.44536 | -48.46218 | 2026-09-22 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f0df6c9-0a8e-3717-aa05-4824e957fa2f | -4.96223 | -56.26536 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4a037a7-0954-34fb-bd9c-88e73f082c3e | -10.84796 | -50.15383 | 2026-09-22 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fedaf177-1b79-3b62-8c98-9bef104cfa9d | -10.45545 | -51.33502 | 2026-09-22 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd707ebb-434f-3415-8815-cb3044328980 | -6.74151 | -59.42819 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b889d531-6136-3e0a-afdb-43b9d5d82164 | -3.44004 | -50.60506 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633afe79-d68a-34b1-af2a-75790395ca48 | -3.05574 | -54.41197 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed4df5ab-6167-30cb-b34a-e6156cc636f5 | -5.6124 | -44.84465 | 2026-09-22 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8795f1be-ee97-3df5-a995-a791d788894d | -6.19611 | -57.78518 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 19e76ae8-f4cf-3ea6-ba5e-f556cbf07aaf | -6.46362 | -59.96916 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddf0c19a-dbe1-3c48-8f38-904e3353ee89 | -5.9973 | -55.67931 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5112053f-0aa9-32b4-b9fa-93b9fd2c3649 | -4.20775 | -59.90934 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cf53723-c772-322c-83e8-5663b8b092ca | -5.45938 | -60.15228 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6afa48bd-9dd4-3358-9e26-aa6965f70bcd | -6.66676 | -50.94685 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf177daf-6504-3929-ac1a-0fba23348d8c | -9.27836 | -46.17934 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 782c2cc0-376e-3525-b738-709f8edac8f3 | -9.72071 | -47.7653 | 2026-09-22 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d2cdfc7-3e5c-329c-b23b-04588a73afb6 | -7.78393 | -44.80811 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9693477a-00d8-3daf-8725-1866647f8e15 | -5.90668 | -51.95388 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6d99edb-060f-37c0-9ea2-e8a1266ab2e5 | -3.68856 | -60.57047 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2b35174e-49e6-301f-9c2d-5abf56648cbe | -3.36415 | -50.46335 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b4b311ac-d556-3c78-a83c-ae4134d266a5 | -6.09632 | -57.67779 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e3f5c3dd-bc10-38a1-91c1-2411dbec9e3d | -5.85254 | -53.53104 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8624f699-1152-3590-877e-33026b97b259 | -3.17222 | -51.36213 | 2026-09-22 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 760d4e94-dd54-3cd6-8984-e432197fde62 | -6.19758 | -57.77625 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb0709ae-053a-3fbc-92e1-22892363c908 | -6.65845 | -50.93496 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f50eb2b-237c-339e-8672-e95860da3bdd | -11.14557 | -42.83757 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e806252-6029-396e-8f8e-5256e0a66401 | -11.14515 | -42.84111 | 2026-09-22 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 314bc1a8-79c9-35bb-9764-ce5eb1230d0a | -10.69103 | -48.72277 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1da8f18-911a-3b9a-9586-dfb315181386 | -7.61088 | -55.35844 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b80d798-09c8-3714-ba5c-f81d0bee552d | -6.30686 | -57.74331 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5213862-e0be-368f-9c6f-07b239d86b58 | -3.06021 | -54.40805 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README49.md)
