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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f7c6b5-90c4-38d3-8d43-3803b14da985 | -2.83093 | -49.3981 | 2025-10-28 06:14:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 860302ba-e9d8-3fa2-8131-6d0202b23a44 | -7.94073 | -45.50438 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 40fdf2d4-a1be-37f6-a19c-4dc7a3af78ce | -7.8065 | -46.45494 | 2025-10-28 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 4656277f-4c98-320e-99f2-d5504f4ba92b | -7.81706 | -46.45644 | 2025-10-28 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 62f31913-67bd-30de-86a4-bcbaf2b86f21 | -7.60982 | -46.46765 | 2025-10-28 06:14:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4c1f580d-9ea1-3ba8-a0c0-b1e5fa56b193 | -3.02696 | -45.37539 | 2025-10-28 06:14:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c0371711-5f26-3777-b472-d7fb0d769fc1 | -7.94738 | -45.52828 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 0b36b63f-8eca-35c7-9365-10d0f5789df5 | -1.49437 | -53.1252 | 2025-10-28 06:14:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6565b8e4-2a13-3b32-a479-2d391578f89f | -9.46212 | -46.8805 | 2025-10-28 06:14:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 482ea353-24f3-3d1f-ba4d-1c79f09cfe84 | -3.08434 | -45.05329 | 2025-10-28 06:14:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 97896bb5-e8f3-35f0-aa3b-c2f41aacac98 | -7.94535 | -45.54354 | 2025-10-28 06:14:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f3bc849e-f5d7-3f9e-9786-3c2dbc7e9293 | -3.70304 | -47.64293 | 2025-10-28 06:14:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4d8c6776-acf0-30dd-ac52-c2acc39b1799 | -8.70238 | -47.98506 | 2025-10-28 06:14:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f344cdf8-2bde-3f19-9143-5a1797d46753 | -3.02885 | -45.36226 | 2025-10-28 06:14:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3034012d-f48c-36ad-936b-925c2bd6768c | -8.15789 | -46.99607 | 2025-10-28 06:14:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3ee72f4a-8d2f-323f-b905-c3b19b756ed3 | -9.56418 | -46.9658 | 2025-10-28 06:14:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1d462d53-3819-3f08-8755-784f167c780c | -9.22455 | -46.36356 | 2025-10-28 06:14:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9400aeb3-96cd-3273-8495-65a0fffc0afc | -10.91139 | -48.00553 | 2025-10-28 06:16:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 14874ffa-3679-3f49-a6b4-bbe8b9a65693 | -13.22304 | -47.08999 | 2025-10-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43acdc8a-a1e4-377b-b375-0b6312dddb6e | -9.13339 | -51.30424 | 2025-10-28 06:16:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e0cb5674-4e9c-3a10-8084-877a08453797 | -13.24834 | -47.95513 | 2025-10-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 388b7cf8-963a-3912-a3fb-d41436a8a995 | -9.95487 | -47.07715 | 2025-10-28 06:16:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5e459b4a-02db-3025-8c63-2b39ae2f23dd | -10.56009 | -49.79224 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 7d5a4868-68ad-3817-84b2-d860e5edace2 | -14.53044 | -47.98201 | 2025-10-28 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 960127ac-e4a4-3fd3-9e0e-f0ed1aea64fb | -13.21216 | -47.08771 | 2025-10-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bdaf592f-856d-395a-940a-a152c5c8dbb8 | -13.36773 | -47.38166 | 2025-10-28 06:16:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f28543d-2301-3e9e-9637-ff13384ac1f2 | -13.63483 | -47.01281 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7b3138cb-91b7-3edb-a80c-ab1e2c74ce63 | -14.62351 | -48.44046 | 2025-10-28 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bea50996-dd2f-3d20-98ed-65e4e179dd39 | -13.62219 | -47.01831 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7c2c21ba-71dd-3fd1-9f2a-74070be3815f | -10.57817 | -49.80063 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f1aa4cc9-bb88-3d17-ac34-4c20e29c1b74 | -13.63112 | -47.03601 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 8db7ddef-6d4c-3057-8476-6f88eb3d26c3 | -9.96363 | -47.16852 | 2025-10-28 06:16:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 45ed5840-bd97-3c47-b258-e64b3b2ad66f | -12.69505 | -46.31078 | 2025-10-28 06:16:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c338b8fd-dfb2-374a-a87c-29522a96233b | -10.96783 | -47.81929 | 2025-10-28 06:16:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 744a1e32-9b0d-3cd1-ab99-2cd071b1f2e1 | -10.56146 | -49.78292 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 999fa47f-cca2-39bf-bc65-97088b7f6d66 | -13.55204 | -49.58385 | 2025-10-28 06:16:00 | AQUA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4a8332be-2254-343c-955f-70cd85b05b34 | -11.28498 | -45.51334 | 2025-10-28 06:16:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2f32f48e-5e7f-3ea2-b063-7ba1dae0d59a | -9.86865 | -47.70886 | 2025-10-28 06:16:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3c68e4e3-bddf-3710-b87c-0201e058ea1a | -10.2932 | -47.1679 | 2025-10-28 06:16:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 287ea54e-c427-34e1-b63d-cd14b1ed2ef5 | -9.95315 | -47.0899 | 2025-10-28 06:16:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e27946a2-9966-3c18-91c2-50aa8fb31ead | -14.62516 | -48.42842 | 2025-10-28 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b52fd4e2-afb4-3bc2-b191-130707ae0974 | -9.97574 | -47.15742 | 2025-10-28 06:16:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 07376528-be0f-3f9b-a9c6-04cd47f36b03 | -13.22119 | -47.10395 | 2025-10-28 06:16:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6fecece5-fa69-31ef-866b-b1e920c31738 | -14.41919 | -49.42046 | 2025-10-28 06:16:00 | AQUA_M-M | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9f93d327-e12b-36ad-adf0-bb0e2f203d8b | -10.5546 | -49.82948 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8086a1b9-5535-3b69-936f-694e114cb612 | -14.41825 | -47.84718 | 2025-10-28 06:16:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 193b98e1-74e6-3628-88af-e4822d1eada5 | -10.57952 | -49.7913 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f074dac5-406f-32b8-b5ba-b3f3490f1dc9 | -12.70397 | -46.3165 | 2025-10-28 06:16:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2b13867d-2f17-3e21-a574-bd57d7ea9b1e | -13.55799 | -49.59048 | 2025-10-28 06:16:00 | AQUA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f812d803-a7e7-319d-a1cb-9f8fc0bd315d | -13.55937 | -49.58064 | 2025-10-28 06:16:00 | AQUA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 641ab958-7e77-31b8-aae2-d0cd93cf0e27 | -13.31577 | -47.68855 | 2025-10-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f7eb59a8-ed99-387f-9ad0-c5bcdf52bf80 | -10.2843 | -47.23114 | 2025-10-28 06:16:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 671e3d67-7062-30de-83fc-80632adb7927 | -12.00232 | -46.78644 | 2025-10-28 06:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 074eed23-80b4-3c16-bd90-286d9dce81e5 | -12.52993 | -47.53812 | 2025-10-28 06:16:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7319af2c-dc17-3ca7-b561-e4f9d822bed9 | -9.33282 | -49.28667 | 2025-10-28 06:16:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8c7552ad-8002-3a15-805c-0cb5213de928 | -12.00187 | -46.77965 | 2025-10-28 06:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 01b667a8-2837-3b87-9e97-088057cdb772 | -9.91342 | -47.67966 | 2025-10-28 06:16:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c9a4203d-aeb1-3c21-a274-a7a934193c8f | -10.55597 | -49.82018 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 608578ed-f132-36e2-894f-166fcbb33c8f | -12.00418 | -46.77197 | 2025-10-28 06:16:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4492a07e-15a4-37c9-a6c1-978c0134f9ca | -9.96184 | -47.1041 | 2025-10-28 06:16:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2467314-f2d1-336e-bd35-79e51a99442c | -15.1505 | -46.60417 | 2025-10-28 06:16:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ad7c0616-9e46-3688-8f54-2abd12cbbd7d | -10.94593 | -48.05198 | 2025-10-28 06:16:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b42aec0e-6bb5-3cdc-8e65-d234b5189dea | -13.62373 | -47.011 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e5c60b90-0800-3c6d-b240-724d240c68a7 | -15.15615 | -46.59785 | 2025-10-28 06:16:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 656d1294-80e2-34f3-ba47-b20ea6e2a63e | -9.13474 | -51.29535 | 2025-10-28 06:16:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 42c9b1ab-dc34-31d9-a668-e92cbbcc2c68 | -9.97399 | -47.17006 | 2025-10-28 06:16:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4b3e413d-ae99-37d5-ac4a-675b12e4835b | -10.9662 | -47.83115 | 2025-10-28 06:16:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3770e365-0799-3933-aaa2-67a0cc0eb087 | -13.63289 | -47.02807 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 21a71322-2644-3881-ab82-461a1b959036 | -13.62193 | -47.02519 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 026013a7-2f64-3d9e-8850-d684dd161583 | -10.55246 | -49.7816 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 64c03ec0-beb1-3228-9420-a4ad61efbf0a | -13.63318 | -47.02076 | 2025-10-28 06:16:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 257c147a-1ea9-3a3c-adc7-84cb941678e2 | -11.03489 | -47.85236 | 2025-10-28 06:16:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 00d28160-f890-3d20-948f-c8cbf04f68a9 | -10.55383 | -49.77227 | 2025-10-28 06:16:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e2a85aeb-04aa-3750-8fa6-375f2b32c92c | -15.15251 | -46.58758 | 2025-10-28 06:16:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 10c1a475-c5b6-3e77-93f2-aff70029e7ca | -12.8299 | -47.7254 | 2025-10-28 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 361ae320-f8d8-32e0-b812-ed47606b1bcc | -3.53793 | -41.62189 | 2025-10-28 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| f39dd620-be5d-3871-b46b-5e5a11abadd3 | -3.52703 | -41.62029 | 2025-10-28 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 83cebaea-2ab5-3d82-abbe-9b440e068dc1 | -3.3673 | -41.45641 | 2025-10-28 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| e79b1401-d91a-3565-9d9b-a087c33afd20 | -4.55087 | -38.25264 | 2025-10-28 11:36:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 98c382bf-34c5-37ab-888a-60940b521624 | -3.70708 | -41.57481 | 2025-10-28 11:36:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 5a5b890e-7ea8-3166-bb60-82b2981ef854 | -4.45619 | -37.81964 | 2025-10-28 11:36:00 | TERRA_M-M | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 29.4 |
| c41c5c27-ab09-30f7-ac19-e3f32d0628ad | -3.00835 | -41.69529 | 2025-10-28 11:36:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| f47b140a-eea4-3c4e-98f9-937cf1a0c11e | -3.3565 | -41.45494 | 2025-10-28 11:36:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| ba4f4186-745b-3b9f-a4e6-00d56312c4b9 | -4.48993 | -38.66889 | 2025-10-28 11:36:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a3d6de7c-7938-3072-b722-60255fc95e43 | -3.54441 | -41.88396 | 2025-10-28 11:36:00 | TERRA_M-M | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| f28be444-c7e4-35ba-9fee-1c0b82bdbe37 | -6.42837 | -42.32556 | 2025-10-28 11:38:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 20309d33-6174-39de-b4bd-74d7b45e5405 | -9.79991 | -47.014 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 2c4c1a04-ad3a-30f6-9f36-83e947909610 | -6.11822 | -42.45906 | 2025-10-28 11:38:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d2e5e066-8ec3-37cf-a7fa-823cf39617be | -7.42843 | -38.77753 | 2025-10-28 11:38:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 66029d8b-cea7-32b9-817b-629e80db3e66 | -10.56491 | -43.22486 | 2025-10-28 11:38:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 70e05b5b-b0b3-3050-bfc4-3a23ff688177 | -9.96846 | -47.10828 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 91429409-93e7-3d78-809c-479b5f9f9478 | -6.8776 | -42.84388 | 2025-10-28 11:38:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 816b0630-2b0c-3c37-9fcb-c1286e87212b | -9.54559 | -46.97974 | 2025-10-28 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 1aa62a3c-6652-3312-990e-5e1c7d17d2de | -6.48722 | -42.2339 | 2025-10-28 11:38:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 7fd4c3f9-adf3-37b6-b124-5f9a3386fdf4 | -7.61133 | -38.5276 | 2025-10-28 11:38:00 | TERRA_M-M | SANTA INÊS | PARAÍBA | Brasil | 2513356 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 889bae80-a540-3878-849f-bc75a65a3b54 | -7.42712 | -38.7865 | 2025-10-28 11:38:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| acd7aa94-6e37-3766-9d30-b43502077652 | -7.81527 | -46.4382 | 2025-10-28 11:38:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 77271389-840a-39ef-905d-234e170c3582 | -7.76834 | -45.39723 | 2025-10-28 11:38:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 28.7 |
| efa2a7e8-2e2a-3256-8f28-c449e199b8cc | -6.26702 | -37.79686 | 2025-10-28 11:38:00 | TERRA_M-M | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 28.4 |
| 98013570-7361-37ab-9709-4917ff88b795 | -7.75769 | -44.71605 | 2025-10-28 11:38:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 398.9 |


[Clique aqui para ver as próximas entradas](README88.md)
