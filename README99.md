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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7155f342-0f78-3349-bc4b-a789608ea218 | -2.81402 | -52.99691 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24aa0e25-0f00-3b84-8126-9d39191b2fde | -2.8724 | -53.98452 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51685197-84d6-3ac6-937b-210af293d2c6 | -4.08218 | -47.0312 | 2024-11-29 05:22:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28c5b814-abc6-37cf-9a9f-19a4baf589ea | -2.20594 | -52.10309 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46565e68-1a3b-3f1c-b7bc-df08ab5ae692 | -2.96907 | -53.72176 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f62d14f5-3a13-3c02-a424-c00285b8d231 | -2.0113 | -55.40374 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0419b92f-fd19-3a01-acae-2146881ad4b4 | -4.44112 | -46.58784 | 2024-11-29 05:22:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d560e317-7d07-395d-8676-4278767d1ec1 | -11.36083 | -56.2179 | 2024-11-29 05:22:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 937d74fb-6bba-3161-bf5d-aceeff7aa85b | -1.88464 | -54.4085 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64f3097f-2c6b-35ef-956f-3d8a0842b806 | -1.63665 | -53.86914 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8c6e8afd-b3ef-399b-80e2-7f550cad3f9c | -2.79521 | -54.12274 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d30fe22-be75-3b11-aa7a-757afe20f8b7 | -3.14177 | -55.00621 | 2024-11-29 05:22:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7750dca3-f68d-3e18-aa16-4f854b79751b | -3.03782 | -50.97933 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8f14185-56d8-3af7-a6a4-429b6b7eb233 | -1.70014 | -52.45146 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 8ecf2f66-017e-3949-8d8d-8fd0dcf9d2b8 | -4.07667 | -47.03024 | 2024-11-29 05:22:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5f6380-ac6d-3674-940d-8759577c5ace | -3.73911 | -50.79395 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cb1d23c-2b1a-3137-9302-31bf10361544 | -2.22872 | -53.69061 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1afb3040-7e7f-377c-9555-0f601aa4f35b | -1.34803 | -55.00678 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd88557b-2089-3721-a16e-27a6a752d06c | -2.30148 | -51.98705 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b19d7ed3-da23-3dff-be7f-0d4aa039e1d0 | -3.44078 | -54.06939 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a62f70ff-2117-3a08-97a9-78aecb1bb73b | -4.08397 | -54.34329 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1b8f0de-af71-36d8-adc3-6cf289bc3104 | -3.0794 | -50.25078 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7081fdd-e120-3a12-a6fb-9858619e1535 | -3.23604 | -54.22561 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dedc2812-4495-36a9-b8e8-ffc135c41c43 | -2.85738 | -53.99815 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f71a2072-09a1-3102-bbfd-0c7fddafa4a0 | -3.70358 | -50.50967 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cfb02d2a-2566-39e6-9408-ccc765f2ede3 | -2.26342 | -53.46722 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3d27855-2e7e-34b0-b57e-0cfdbc57a32d | -2.80468 | -51.58441 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f94a351a-3e00-353f-8aef-71ce46a83b97 | -2.57258 | -51.84032 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 962f1013-a44d-3197-ab74-c7859764174d | -3.24599 | -53.64091 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 305c001f-7b43-3171-8b2b-85dd60320ced | -2.6098 | -56.4551 | 2024-11-29 05:22:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201ae35c-083e-3f61-ab29-7c3e4f0fd1df | -1.35594 | -55.03232 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edd6020c-ed96-3c54-8eda-8a14a0294167 | -1.67557 | -52.49795 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 207cafcf-4677-3ff9-8a8c-1395a1d5b605 | -4.78588 | -46.10748 | 2024-11-29 05:22:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4b030090-9114-3021-8e50-40db8b4b4a78 | -2.26584 | -53.48025 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b5354b7-73d8-35d0-89e3-d832abb2c17b | -1.654 | -53.81261 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81b1c929-4479-3d3a-9f9c-ad187ea618dc | -1.88192 | -53.32775 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e980f94-4981-33ac-b088-ce693359217e | -2.84903 | -46.82165 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e5b4824-3630-3e18-972d-22faaf2bacb8 | -3.41707 | -50.16346 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f932b27-740a-399a-a3c1-b86c3c1921f4 | -2.59469 | -54.08182 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 637f5e5e-edb0-3ebc-8af5-85957696c6cc | -2.26278 | -53.47132 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adecd555-98f0-3d44-a3ca-670164d65d77 | -2.97996 | -53.35468 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a8f8796-ff38-3ab7-a477-83523b0d5b58 | -1.45492 | -54.3711 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8583d0f-8c3b-3af4-8b24-1f8f9e6f4496 | -3.25035 | -53.6416 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af42f24d-c074-36a0-a2b1-372d988a331a | -2.97643 | -53.28699 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9eb6ec77-977d-313e-9c4d-4c75f5f72b11 | -1.99019 | -53.29291 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccc918f9-2190-351a-870f-4c8db6ba694a | -3.31369 | -53.75161 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d431b7-f766-343f-b6cf-afcd4d266b1e | -3.04895 | -54.41238 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa8ce5c6-f40e-32b9-b9bb-52a1dd16c3ca | -1.45033 | -54.37405 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3d371ad-dfab-38bb-8fca-e20d51f83436 | -1.62344 | -53.87144 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a89b810-c906-389e-94e7-9def6f0229be | -4.16789 | -48.61935 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec8ef6d2-b842-3ad0-94f4-b1fd0c57f9ae | -3.32477 | -50.21922 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82368780-695f-389b-9729-3d6447dc47ff | -3.3314 | -46.69183 | 2024-11-29 05:22:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d08bb1cb-5e16-34c3-9cdb-bb5cea05a731 | -2.73113 | -54.40276 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb2fc779-b826-3bb4-948d-7b549f76b8dc | -8.28058 | -48.03692 | 2024-11-29 05:22:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3c86179-6770-3904-bad3-ace72ad6bdd6 | -11.36134 | -56.21418 | 2024-11-29 05:22:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c016036-8107-3728-8261-e91fd382554a | -3.42383 | -53.89113 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| add3ea7a-038f-3aad-8717-3a6d8142fd17 | -3.04049 | -54.04077 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 673c2255-0713-39c5-8d42-91fb8fd370aa | -9.8821 | -63.10811 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b378a73-f406-315f-bafd-bbfa7790fc1a | -17.65485 | -57.55656 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 741296de-c842-3565-8a00-68f651f3edea | -17.63584 | -57.57347 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4c99c5bd-1791-3f28-8726-97b5401ca86b | -17.7068 | -57.59024 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6de5304c-acf9-369d-972f-76e9325d0f1e | -17.55703 | -57.51532 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 06cba2b8-95db-3c11-aea5-22291852d0a1 | -17.65286 | -57.57197 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ccde0153-a52b-3683-be08-325ebf743af1 | -9.82104 | -63.24903 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f3c0420b-7ebe-330e-ba41-327c85d318d5 | -15.09045 | -59.63882 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f39ca6d-bb2c-3895-a456-d4a8028933f4 | -17.57494 | -57.60394 | 2024-11-29 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2e82bdec-bc41-39ee-95ae-b13d5a434f07 | -9.01785 | -63.76632 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b81b850-0561-322e-8452-a97704667165 | -17.64361 | -57.5785 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d6ddbba9-1d7f-3bf9-a8f0-ecec96a474ec | -8.60096 | -63.44949 | 2024-11-29 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4df1811c-a95c-3687-bf87-f995cbfe6721 | -17.56568 | -57.48101 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 83619139-d0fb-3036-91ea-5b8cfaf3c8a5 | -9.59023 | -62.05539 | 2024-11-29 05:25:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df726fc5-af8c-3c7a-b8ff-ef9b83b6b3ba | -9.94454 | -63.71036 | 2024-11-29 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9eb30ef-04ce-38fa-a128-e74c40c1f8c2 | -17.63633 | -57.56962 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d91f9b48-aee7-3cfa-8ae6-8e453e6ebe5d | -15.0863 | -59.64241 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35a74506-17b9-3142-a39e-de0189532dc4 | -17.6441 | -57.57465 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f124df32-382c-3095-b424-25239cb8e8fd | -16.24875 | -59.95791 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0de62af-a1dd-346e-aadb-34d4acea9da4 | -17.65864 | -57.59237 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f34b4d10-afb5-3858-9d0f-28c847781939 | -10.59414 | -59.08088 | 2024-11-29 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e732753c-097f-3b84-b29b-841ec1a2aaf0 | -17.64096 | -57.56636 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0f4adea1-d214-36bb-915f-18dcfa377d0b | -17.65121 | -57.55212 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 18cd3784-b81a-3288-8c54-6ecf2e7fb17b | -10.82156 | -56.23417 | 2024-11-29 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb7c80ca-2aa0-348a-ba9e-f5948790ce14 | -9.90042 | -63.21126 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eb38ac5-5ef9-3f30-91da-8892aa675b12 | -17.70195 | -57.58282 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a6ae5420-9704-398b-ac58-51a9094e623c | -17.70094 | -57.59052 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1a510588-b75d-3586-b882-3ed6a1adafe0 | -17.57906 | -57.60454 | 2024-11-29 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9ebc3f0b-0fb3-3488-bab3-f643e734ce6a | -17.70363 | -57.58196 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0d43857f-5bac-39b9-aeee-1b7adc29b325 | -9.64923 | -65.74226 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf2f38c3-7ef8-36df-854e-ad88a231930a | -8.46275 | -64.09176 | 2024-11-29 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71e6e979-a639-3aa2-a2cd-65434e0c9b7a | -9.9439 | -63.71429 | 2024-11-29 05:25:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d556ae3-02e5-3fc7-a9d6-491f1f341935 | -8.82866 | -64.27229 | 2024-11-29 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 238fee21-aa3d-3e19-999f-c87717e37ba7 | -17.64873 | -57.57138 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0e05a844-ad82-3cc8-a1a4-8de5c8145ff6 | -9.51411 | -64.46266 | 2024-11-29 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01a8b604-38d9-3f43-b6e1-e6de967e5714 | -17.64923 | -57.56754 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b1cfd775-ba4a-380e-aa19-403349c48fa8 | -17.65501 | -57.58794 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5d8f4c9c-9e67-3e2c-b2e2-8affb9cc1552 | -15.09401 | -59.63935 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38f38e16-d8ec-34bb-b089-8e14957497ac | -15.08986 | -59.64295 | 2024-11-29 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b1a043ca-b1c4-3c90-a8db-142d0a0264cd | -9.38299 | -63.21344 | 2024-11-29 05:25:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b620b3d5-e925-3244-a959-853163c15df2 | -9.18621 | -62.37872 | 2024-11-29 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05f3d28c-52e7-3114-b398-bb1b89b1241a | -9.837 | -63.36012 | 2024-11-29 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38a5440b-2354-3d0c-882a-dde630194b43 | -17.70315 | -57.5858 | 2024-11-29 05:25:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README100.md)
