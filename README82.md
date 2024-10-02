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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ca35c20-166b-3f9b-aee7-b425c1ec7d21 | -3.47231 | -43.3552 | 2024-10-02 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2fc49714-060d-3130-a4a2-2db502f65552 | -3.47193 | -43.35868 | 2024-10-02 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b2efbcd0-bded-3b9f-86b4-88974250a052 | -3.47162 | -43.35995 | 2024-10-02 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aeceba0e-3e67-3d6f-842d-69d7df19181e | -3.46733 | -43.35798 | 2024-10-02 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91578bb2-abd3-3115-adb4-0578273cb0d1 | -2.78928 | -43.33783 | 2024-10-02 04:44:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96077861-bf6b-338f-890d-dfb9e9b50997 | -4.03942 | -43.24203 | 2024-10-02 04:44:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 941b1bb1-fc6f-330c-8dab-c6c10cff868e | -3.59278 | -44.54713 | 2024-10-02 04:44:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e33690b-387d-3e1d-a05f-af53e6de7e4c | -3.59218 | -44.55106 | 2024-10-02 04:44:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64a414d0-5bbd-35e5-9787-d30fef288d5b | -1.15423 | -46.97544 | 2024-10-02 04:44:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d086e4a8-497f-3aea-b5ac-f1dac6d86f6b | -1.01311 | -46.78535 | 2024-10-02 04:44:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e7f0108-90c7-3386-b3d8-54b0040ce847 | -1.01016 | -46.78072 | 2024-10-02 04:44:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 407f0143-bc42-3341-a318-efc3d66ab2fa | -3.32158 | -47.02381 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b1712b6-53ae-37e6-bcc6-3df79842a3d9 | -3.31795 | -47.02325 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 583449c2-803f-3735-b633-55fc78d22940 | -3.3133 | -47.00528 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac9ba26a-e119-361f-88dc-5b02d6c28e90 | -3.29101 | -47.12609 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec99e11d-e7ef-3208-96c8-6957c3e4051e | -3.2874 | -47.12555 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8679291b-da27-3042-8e4f-109e796bea51 | -3.21641 | -46.78287 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8abe8a35-cd3d-3df4-9717-3a96fe9a1a12 | -3.21575 | -46.78717 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1e3c0851-706f-3cf7-b14c-c1ec84a4a7bf | -3.0082 | -47.36164 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7496835f-2a68-3a9b-8b9e-74c187581b36 | -2.9081 | -47.11372 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f63a9969-9e42-34e8-9e6d-41ea9af2bea6 | -2.90635 | -47.11092 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b114125-6bb3-31ed-abfb-7aca9d79fc9e | -2.9057 | -47.11502 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7d869b1-2905-34ca-b122-3831b61de13f | -2.9045 | -47.11323 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a71ac251-e2b8-3eb1-b61e-5f78410147f5 | -2.7428 | -46.76976 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7f92e68-f7ee-3d71-914b-fd8791c4fb6d | -2.72725 | -46.79487 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e648134-f171-3f58-ab71-15b60c880e5f | -2.72396 | -46.72004 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5f29bf6e-a77b-3376-928e-a286af5fd4f3 | -2.62423 | -46.90883 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ee563dd-e5e8-3366-91a1-77f049301c06 | -2.62061 | -46.90826 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8da89e1c-7fcd-3581-bd5a-509ac6a28b0c | -2.61997 | -46.91246 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45afaeb3-6ccd-32cf-bd15-85d0aa0f5607 | -2.51668 | -46.05679 | 2024-10-02 04:44:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccea67c4-183b-32f9-be87-a5e60480a68b | -2.18813 | -46.99097 | 2024-10-02 04:44:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed018f50-ec6a-34d3-9f6e-0e03926cd734 | -4.07791 | -46.21491 | 2024-10-02 04:44:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce9d4cac-7b47-3f88-a244-ca4b9f01bbe0 | -3.70013 | -47.59986 | 2024-10-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e052a38-ee91-3e80-976b-113b6f0341a7 | -3.69976 | -47.60117 | 2024-10-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 078971c1-bfc4-3eb0-a9a4-09d5114aca02 | -3.69953 | -47.60386 | 2024-10-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fecaa39b-3465-32f3-896d-c7b14533238f | -3.69914 | -47.60516 | 2024-10-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebea1793-ffee-3d98-8514-7c8d7dc8fdcc | -3.69659 | -47.59932 | 2024-10-02 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14304267-6e4e-3e0b-9ab2-fcca2e27e9ec | -1.8666 | -47.98569 | 2024-10-02 04:44:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf76092-b654-3579-9184-8d66a00cc395 | -1.00009 | -47.82406 | 2024-10-02 04:44:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a10b34a-d57d-3cd4-bec0-a33ca4600dd9 | -3.46869 | -47.66462 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48330565-1dad-305b-9e8e-c54fc9033fd1 | -3.46517 | -47.6641 | 2024-10-02 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4230c6a4-7bf5-37a9-917a-4adc7247e4c5 | -3.40447 | -49.09348 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0d536922-31e0-3f35-af7d-f75942a0ae8a | -3.32446 | -49.04078 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0b105fa-44ce-327a-89dd-34aab7c16559 | -3.21956 | -48.92675 | 2024-10-02 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d34141b-24ca-3ff3-b93b-a4c964488289 | -3.13462 | -48.99375 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43123c45-4c2b-384c-a94f-1ad95dd62e12 | -2.95914 | -48.00372 | 2024-10-02 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3f45ff-3829-39b9-bf26-f14f2549fc30 | -2.95569 | -48.00319 | 2024-10-02 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6baf8bf-7218-3236-a225-ba89695c0c25 | -2.95224 | -48.00267 | 2024-10-02 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3ff2acb-4cbe-3f09-8df0-b3477a6d1a3f | -2.84458 | -48.0862 | 2024-10-02 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6afd8f56-fc48-3a6d-bd47-a2ad1006808c | -2.844 | -48.08995 | 2024-10-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd7c2161-f57b-3b25-bd5d-ea303b1f09ed | -2.62555 | -48.32229 | 2024-10-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af054b98-6c66-3f54-9c93-fccea418fea9 | -2.59982 | -48.03449 | 2024-10-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6507f171-64a5-3630-ac5b-9f6a04f88c2a | -2.59923 | -48.03823 | 2024-10-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b076dd0e-98f2-3132-96ad-1e2970d8d98b | -2.59865 | -48.04199 | 2024-10-02 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9075f055-0e8c-33e7-8bb5-cf0079137058 | -4.2876 | -48.07452 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d98c3774-30f3-31da-b559-3f3b9124b88e | -4.2847 | -48.07011 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1850eee6-9f8e-3db5-8cdf-56f26e6d05aa | -4.28411 | -48.07399 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc4e39d2-3483-3985-a6c7-1d770b1a0601 | -4.2818 | -48.06572 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e4742101-faaf-3480-a4ae-6e40239881b8 | -4.28121 | -48.06959 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f8953899-3aae-3831-84ad-52c3966fe92f | -4.27985 | -48.06646 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 484dd7bb-517b-361d-9593-47d9e2cb3b61 | -4.27831 | -48.06519 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4fb9923-9331-3646-a700-90fc32570fbe | -4.19421 | -48.22966 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd241227-91de-336b-84b8-1f1c8ee7f028 | -4.19363 | -48.23346 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c78307f-c85c-39af-a36a-85722d76c7b6 | -4.19018 | -48.23288 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a113d0bb-2339-37e1-9371-c151a7d61201 | -4.17698 | -48.77807 | 2024-10-02 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cf4b20f-bfa9-35d0-9da2-6165f90f908b | -4.17642 | -48.78172 | 2024-10-02 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 879111ff-0666-31f8-b749-7b6b39d997fa | -4.15439 | -48.39726 | 2024-10-02 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a225297-ecab-3b10-9c08-6707afc88497 | -4.14294 | -48.40316 | 2024-10-02 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e71a6c2-56c0-384e-bfde-166da74e7659 | -4.08905 | -48.2756 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31bf19d1-b4b4-37b8-9815-5cd41279a8d3 | -4.08847 | -48.27936 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89217b18-5f1b-3f4f-912a-193fc0811099 | -3.99907 | -49.03523 | 2024-10-02 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38ce69c2-0099-3ea2-8812-773659ecdceb | -3.90071 | -48.35941 | 2024-10-02 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 660da537-b277-30f3-a177-d749df1fc460 | -3.69856 | -49.21484 | 2024-10-02 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72cbbaf0-49b7-3dfe-a5b4-ae59f5c56ab3 | -3.30495 | -50.44945 | 2024-10-02 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 376b8918-db1c-3ef5-8e8f-0478c59e9418 | -3.30166 | -50.44894 | 2024-10-02 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc179c91-a9fe-3cf6-a7be-59b911ed2312 | -3.27278 | -49.10888 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1a6638a-0165-39fb-a09b-7dfe68901d45 | -3.27223 | -49.1124 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee87c134-5ab3-3eb0-8898-1c0b2137cca3 | -3.14237 | -49.42243 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6f93f568-b932-3ae4-acdc-9ffe366d6f0f | -3.14183 | -49.42591 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 53dd35bc-6b00-37b7-8e53-63c58a8c715e | -3.13959 | -49.41844 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0a2524ad-4fde-39a1-9999-986e1e8394c1 | -3.13905 | -49.42192 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 189ca11a-a529-3396-b0cd-d7bb60e42693 | -3.13851 | -49.4254 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 08bc4ed6-f6ec-378d-8fee-a7834c2183a4 | -3.13797 | -49.42888 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6b59c42f-1c7a-3c05-bb96-5f2c7a857d8b | -3.13627 | -49.41792 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 83c6fece-ffcc-359b-a108-da6f31dc02af | -3.13573 | -49.42141 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ac44acb8-43fb-32bf-9abe-8eeb53048871 | -3.13519 | -49.42488 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7c6346c0-faa6-375d-9daa-506375dbfe5f | -3.13465 | -49.42836 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c867d368-3759-3d47-a7fb-dda3f2b9cf9f | -3.13296 | -49.41741 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ab46e848-9bed-3702-80c3-48bcdf7441d4 | -3.13241 | -49.42089 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1cfdfa23-15b2-395b-a9c6-c6ec75dcd754 | -3.13187 | -49.42437 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0e555bb9-4862-3847-9d39-6fe67122ff2e | -3.12909 | -49.42038 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00e89108-8e54-3cb5-a708-8a5ffb55aded | -3.11744 | -49.40788 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ef20f79-b923-3f65-8fd4-720bc2d21d67 | -3.1169 | -49.41137 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dcfd70f-a32a-3375-a48d-6972823de7bf | -3.11412 | -49.40737 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93aaebc1-19a0-3514-9c82-a5eecf8e0e8a | -3.11358 | -49.41085 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c364af-06b0-3d42-b4de-cfa333523963 | -2.96126 | -49.36179 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9704086f-11b2-3c5f-b177-def74138e1e7 | -2.96072 | -49.36527 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce370856-4fb5-35ea-849a-08007cd5d7f7 | -2.95848 | -49.3578 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5b3f8a0-7817-3436-9aa7-b6d935e1b197 | -2.95794 | -49.36128 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 007d17a8-9143-326a-be71-45df57030d69 | -2.9574 | -49.36475 | 2024-10-02 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README83.md)
