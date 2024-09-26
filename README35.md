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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 003e9df8-0b04-3d45-a6cc-9a49001a4b81 | -20.5921 | -51.495602 | 2024-09-26 01:46:22 | METOP-C | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 395844b5-e1be-328b-ad92-7aadb75fe488 | -21.4 | -54.645802 | 2024-09-26 01:46:23 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c0de07cf-233c-3686-99c4-bc094c3515eb | -21.4032 | -54.658001 | 2024-09-26 01:46:23 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f2569832-398d-305d-a2ac-a4b1f022e8c8 | -21.390301 | -54.648701 | 2024-09-26 01:46:23 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 34697f4f-92be-38c6-9c03-44fc9abcdc9d | -21.393499 | -54.6609 | 2024-09-26 01:46:23 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dcd76a69-5732-3674-9894-32f3c12529a7 | -14.571 | -45.674 | 2024-09-26 01:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 25a1824f-5144-34c0-90b9-7a5e07375561 | -14.5705 | -45.6973 | 2024-09-26 01:46:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| fe00c6c9-7b54-3cda-9c86-80fd3eb1f1b9 | -14.863 | -51.5019 | 2024-09-26 01:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 41c35965-f4fe-3a31-b6c2-848fdf338f56 | -14.8824 | -51.4992 | 2024-09-26 01:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 976d30a8-552c-3019-99d8-a304de7d3b5c | -14.896 | -57.9873 | 2024-09-26 01:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 4b0df70a-0350-39ae-9c1c-d835ae0b2f9e | -14.9153 | -57.9854 | 2024-09-26 01:46:31 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 22a530d3-ea10-38c1-ac4c-4b62925e5254 | -15.7676 | -49.9555 | 2024-09-26 01:46:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| faf09180-0a98-3d78-b5a0-926f2e778bcf | -19.781601 | -51.467098 | 2024-09-26 01:46:35 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 57efe892-28ed-3c3b-a24a-8680f0a1a2ef | -19.787399 | -51.487598 | 2024-09-26 01:46:35 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cb3109c7-320d-3929-9234-c0c591b2dc5a | -16.098 | -52.0111 | 2024-09-26 01:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1abe0165-9caf-31f3-bef3-31fd60f5cff6 | -16.0985 | -51.9896 | 2024-09-26 01:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 0940669f-6ef7-3d3b-a025-c9333f6c2a55 | -16.1176 | -52.0082 | 2024-09-26 01:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b396f6b6-170d-3c10-91c0-ce21c2c5cad2 | -16.118 | -51.9867 | 2024-09-26 01:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| ea9d48a0-ca3e-3417-bc66-6524fd2a2c69 | -17.096 | -56.3576 | 2024-09-26 01:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 544cdad0-a912-3095-b958-8d48b7c93802 | -20.728701 | -57.485802 | 2024-09-26 01:46:45 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ff41e87a-7a71-35d1-a291-98d2d5025cde | -20.084999 | -55.517601 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 616f597c-cb7e-3843-9886-95384433a8af | -20.087799 | -55.5289 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f43f0fef-3d1e-35c3-8c2e-8a01bc48d015 | -20.0907 | -55.540199 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 92ef6675-11c6-3699-8fa8-9954c9726941 | -20.0753 | -55.520401 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 033528bd-ffb0-3aab-963d-a16371044801 | -20.0781 | -55.5317 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d5138d5-f69d-3581-9e54-f662a4e1966e | -20.080999 | -55.542999 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c4beaef0-aae8-361c-87e3-cd11a1d3244d | -20.065599 | -55.523102 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 14463e12-3376-3cad-99ad-dee4f2cf5219 | -20.068399 | -55.534401 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 00761c26-a89a-37ae-9bf7-1c44921afcc3 | -20.071301 | -55.5457 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5777c860-caee-38f0-a0e9-f2d9840bebe9 | -20.0221 | -55.474499 | 2024-09-26 01:46:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4acf66e8-bedd-33ef-a50d-14acc89f76e5 | -20.0124 | -55.477299 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6d275440-0ac5-341b-8495-e8527dae9b8f | -20.002701 | -55.48 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c390baf5-4ba9-3057-a25a-85bd02a49482 | -20.0056 | -55.491402 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| feaac52f-6775-3eb2-8468-baa2190b94f6 | -19.993 | -55.4828 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb4c6f3-1b8c-3074-8897-f61071413df1 | -19.995899 | -55.494202 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4f815745-d1ad-31f0-a71f-8c610b121a27 | -19.9988 | -55.5056 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 10c89542-7771-3d88-a7cf-1444d26e6671 | -19.9862 | -55.496899 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 273e5ce3-0594-36e7-b89f-be4407538842 | -19.9891 | -55.508301 | 2024-09-26 01:46:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3abdc189-e55d-3fda-bf46-3d7de103cebe | -20.003799 | -55.976398 | 2024-09-26 01:46:51 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 319b53c9-a947-3d60-9e3b-9d0ee8e042a2 | -21.9374 | -48.5688 | 2024-09-26 01:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c5cbbf8a-8f05-3450-86de-7908c5437143 | -21.9381 | -48.5453 | 2024-09-26 01:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7669bbf1-cc3d-3baa-9732-7033f449ceb8 | -19.15 | -57.471699 | 2024-09-26 01:47:10 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 390e5c14-0cb8-3ce5-a0da-642db72b433b | -19.140301 | -57.4743 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff178c59-707d-353c-b990-da2fb1b08932 | -19.130501 | -57.476898 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d3a75ec2-d6a0-39e6-899e-80f1204c824b | -19.135 | -57.495201 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 36f0fe7e-e88e-313c-8e62-1e94ac05bca3 | -19.137199 | -57.504299 | 2024-09-26 01:47:11 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea2f19c9-f8f5-30e1-a170-7752d1eff51d | -19.1208 | -57.479599 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aacb01d4-dffb-3f8f-b289-5b3014bb60d4 | -19.1231 | -57.488701 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 03d2bcb3-3c4c-3f45-9d8b-eaa449079501 | -19.125299 | -57.497799 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 333a063f-d7fd-3ff7-834c-83c289ebe273 | -19.127501 | -57.506901 | 2024-09-26 01:47:11 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2c77950d-2873-3111-b0f2-3dc5873c43ad | -19.111099 | -57.482201 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b6185dd0-1035-357c-ad04-cb5fa387353d | -19.1133 | -57.491299 | 2024-09-26 01:47:11 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca88b614-5230-33ab-875e-1c163bcf1ad3 | -19.115499 | -57.500401 | 2024-09-26 01:47:11 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5b455d8a-a4e9-38e7-9a0b-2993027ae8ca | -15.7571 | -49.923 | 2024-09-26 01:47:33 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7cceb821-562c-3ed3-b217-ac2f14e6b36c | -15.7659 | -49.953201 | 2024-09-26 01:47:33 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3244ddf-5f7e-3cb5-b2c6-73fd219ac8f1 | -16.1122 | -51.988998 | 2024-09-26 01:47:36 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca89c08-6f0c-3485-9770-868444144a47 | -16.0965 | -51.969898 | 2024-09-26 01:47:36 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68a20d1d-51fe-3a8b-adbb-450a8fd040fe | -16.1026 | -51.991901 | 2024-09-26 01:47:36 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6e7931d5-12d4-3c6b-8d67-de0f48cd70e4 | -16.1087 | -52.013802 | 2024-09-26 01:47:36 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 78d84d61-e051-3ad1-a55e-8006b47082ab | -16.087 | -51.972698 | 2024-09-26 01:47:37 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f14e795f-fb08-3e54-9e1e-7e6434f43b19 | -16.0931 | -51.994701 | 2024-09-26 01:47:37 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7d05ab12-7ef1-31bc-9f72-3512ee3d47b1 | -16.0991 | -52.016602 | 2024-09-26 01:47:37 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 66b8e3bc-e139-37a7-b635-adec4da1a83f | -16.5993 | -54.0956 | 2024-09-26 01:47:38 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 078d809c-09b3-3038-b61d-5ea9056f3233 | -17.0861 | -56.094601 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d900113a-7ccb-3fa7-a78b-0171933cd43f | -17.0891 | -56.106098 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| afa040b4-8b13-3230-b1ea-b53903be5b9f | -17.1064 | -56.174801 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3256be96-aa09-3628-a57a-2135bd5dd0b1 | -17.109301 | -56.186199 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0af94743-7f8e-368d-973f-de3c50114cd5 | -17.1122 | -56.197601 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22db0dab-b33a-318f-8c0d-e793269fa9e0 | -17.0735 | -56.085701 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29564a9c-3df3-369b-b13f-aefa81ccb9f9 | -17.076401 | -56.097198 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d83bf5d4-f0da-311c-a666-67d1a6911fda | -17.079399 | -56.1087 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5adcde16-4b15-3d7e-b2ce-979e52e6f2f0 | -17.091 | -56.154598 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03268b88-8e36-3737-9207-ece31260e499 | -17.093901 | -56.166 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3dac4aa5-256e-37b0-9ff6-a0dd578efc01 | -17.096701 | -56.177399 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8cb00be2-7685-3f71-9a73-a3de368d235b | -17.0996 | -56.188801 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 658e6881-0ef5-3b41-8a8b-4dbdb0712e98 | -17.102501 | -56.200199 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9b24774-57d0-32f4-86e9-a94d87440a32 | -17.1054 | -56.211498 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a775c038-55ad-3015-8437-a6114f3bbb55 | -17.063801 | -56.088402 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0d79b1d-fff5-3cae-9d84-c79b66de85a4 | -17.0667 | -56.099899 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cee7c7ab-e090-3cc5-b65f-4edb8527cef9 | -17.0784 | -56.145901 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ee99bee-4151-3df1-a3e7-268270da9579 | -17.081301 | -56.157299 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93763495-be11-31de-8f80-8f4257f0d41a | -17.0842 | -56.168701 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6f39a7c-bd16-3b13-8677-a8ae1c5f2877 | -17.087 | -56.180099 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7f7de16-872a-3946-afa1-04cb40ff9a88 | -17.089899 | -56.191502 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2fd72fcc-bf93-31ff-a7ab-3a82b07e506d | -17.0928 | -56.202801 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5255c2a6-caac-3569-bac9-2eb145ef4bb8 | -17.095699 | -56.214199 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6cf49d4-4c1f-366c-b785-ebcc4e6f3642 | -17.098499 | -56.225498 | 2024-09-26 01:47:38 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 687e49f6-e3f8-3a56-a1ca-567dcabdc233 | -17.0541 | -56.091 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ba0e5746-badf-37a3-84df-455142f5fdac | -17.0658 | -56.137001 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e399bad-3e04-30e2-b9da-9b6892b78688 | -17.068701 | -56.148499 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a9f2da24-256a-3a6e-a3e0-a65f9d24588c | -17.0716 | -56.159901 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b39d26ca-54df-336a-a280-dde30b2b4624 | -17.074499 | -56.171299 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc01eafe-78fb-384f-993b-c2b7a60707db | -17.077299 | -56.182701 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e71d61f-49db-3cf4-936f-ab4d160e2573 | -17.0802 | -56.194099 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 456b166f-d0f9-34ac-a7c6-a0a9c508351b | -17.083099 | -56.205399 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 587ef86a-4f41-344f-b6e0-a3b6cc647db4 | -17.086 | -56.216801 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 29dfa9b8-57d4-3d24-8f6c-0006e4a50d34 | -17.0888 | -56.2281 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53f508f8-fd6b-3771-8ece-c74bb0e11705 | -17.0917 | -56.239399 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a1692f0-1061-341f-87c2-14808468a83d | -17.059 | -56.151199 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 204ddeb0-77c2-3c37-b2df-c67578c388b0 | -17.061899 | -56.162601 | 2024-09-26 01:47:39 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README36.md)
