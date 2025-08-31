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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 739d8cdd-29c9-391d-966e-416b59d387d5 | -18.66397 | -49.09198 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a7cd81f6-8fc1-35a5-9f68-88a552eb141c | -15.71355 | -48.93241 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 193093a2-3710-348e-9a83-96e759fa7b2b | -15.688 | -52.74727 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77790065-8b16-3611-93b2-7aa0952dfadf | -16.22693 | -52.67738 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 159ffd33-e1e2-37c0-9e0e-b54af908209c | -16.96496 | -49.748 | 2025-08-31 04:53:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6a782c8-7203-39e9-86b6-b8a6f5f7b858 | -16.97604 | -49.31114 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d21bc22a-5911-374e-8b02-ba187a08db4e | -14.59054 | -54.54844 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c3b0911-2a48-36c3-a6d9-dcba682ba655 | -15.21762 | -56.05861 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d12de01-4075-3c14-8086-5f00adfde70c | -14.60436 | -54.54708 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1c9a8cb-da98-3657-a882-f2fea75ce738 | -15.72102 | -48.94112 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d0b77ca-8030-3fda-945f-91836885a48a | -14.59605 | -54.55665 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 945469bb-7b50-3831-8821-e12b1d80803b | -14.60776 | -54.50387 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1a2bfc3-468c-3e66-b722-d09345ace75e | -18.05963 | -45.9453 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ab2c23-402e-3c40-af12-fe73b8eac11a | -15.70731 | -48.94748 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49434689-451b-3deb-986d-755d4c4b778f | -14.59274 | -54.5561 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 15526337-307a-32d4-883a-01eb223c78ed | -21.12965 | -47.85881 | 2025-08-31 04:53:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42b1febf-4d03-34a9-b8b0-fcb8237905af | -15.21091 | -56.05736 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ef81106-4ed0-310d-b40a-369b060819f2 | -17.15182 | -46.08219 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a6f0bf7-1dcb-3a07-a498-0f29c9c859f3 | -18.05011 | -45.94706 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ce8e556-2ef5-3d49-b0d6-d5c5914c0b43 | -14.58942 | -54.55555 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1188d4d2-5a2d-3105-832a-eafc199063ec | -18.05542 | -45.94785 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1dc0c51-e36e-3f55-88eb-3501300eda82 | -16.23742 | -52.65456 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb62c322-5011-370c-acdb-63a9b6eea095 | -15.15531 | -52.33345 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f1b8db2-5531-34fb-b528-1238f46f5cfd | -15.20118 | -56.07444 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5183609c-73a2-3c75-96b8-1f5505a2936e | -17.20627 | -46.07496 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b43fdc28-a63d-3f16-8e2b-706f3844d15a | -15.7083 | -48.93978 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b17a202f-2a30-304e-b507-65226890bf47 | -15.21919 | -56.07015 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca4a8280-c866-3c9d-a2e4-3bdadf42bbb8 | -18.06458 | -45.94959 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7abc5191-5415-390b-b2c6-af38cbf49c2b | -16.22178 | -52.66433 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41897ae7-337f-30ed-bb56-e03c77e742ec | -14.60281 | -54.49211 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb34c72-58c7-32a4-a0ef-8e7b0bed0469 | -14.6072 | -54.50743 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 092ae7ef-e007-3ca7-81b5-b15cd17034cc | -15.71627 | -48.94464 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29ee9975-4138-3976-ba30-2b3ef263db69 | -15.77088 | -55.93765 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 46195783-9e1a-3ebd-b096-0c4f1aa523d3 | -16.53486 | -55.05096 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 74882887-2b2a-3fd9-8159-5f20a7b64c1d | -15.77542 | -55.93092 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 470be852-8fd9-389c-8bc4-26fc50b4f76d | -15.7231 | -48.92503 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53b1527d-6df5-3db7-8193-205e0e4738ea | -20.68703 | -54.58808 | 2025-08-31 04:53:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee11b21f-c5ee-3714-92d6-0ba3f7dc2a35 | -15.7183 | -48.92894 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fac9ffe-960d-3918-9722-e65998a48f3b | -14.59675 | -54.48745 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de742d2f-9238-308a-bc05-50134add57e5 | -16.97972 | -49.31569 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f186ec6b-6930-3573-b019-d0acae90fae3 | -18.65857 | -49.09314 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cf8ca625-9d97-3d12-959d-57e14e631c25 | -14.31074 | -60.35111 | 2025-08-31 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3050d1ac-5508-3e51-91ce-c5322e326fc2 | -15.79631 | -55.90823 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 000775fb-0353-375c-8c2d-5493cc855106 | -15.72051 | -48.94508 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c388627-0859-3f93-ad82-e6680e1ae6fb | -18.71104 | -52.92388 | 2025-08-31 04:53:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6082f076-21bb-3443-a029-41fa64265021 | -15.71728 | -48.93682 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23f3c4d7-2036-368f-9d39-e185ff35da36 | -17.20568 | -46.07401 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aeeb82c2-c12e-310b-bd6c-c0c1323e65dc | -17.62024 | -44.25408 | 2025-08-31 04:53:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79c289f6-5e09-3bc3-b3a7-4833e944dc28 | -15.72 | -48.94902 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55e9e673-6049-33a2-9ee7-c891f8b98126 | -16.40799 | -45.65431 | 2025-08-31 04:53:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a50764f6-8579-3fca-9b7d-6dece3e6eb6f | -15.72257 | -48.92915 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35343711-d441-32a0-996a-d8ee175a6f18 | -14.5911 | -54.54488 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 133c74ff-d6a6-318e-8e7e-a07a09c43a4d | -15.7146 | -48.92426 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28b56db8-56a5-33dc-ba6f-1847051c9f77 | -15.29951 | -52.7997 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 465cc68f-2ba0-37d2-853b-34a82f2268d2 | -20.26228 | -46.01298 | 2025-08-31 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| db059bcf-1f8d-36c7-bac7-6a5b0a8ee834 | -17.61877 | -44.25269 | 2025-08-31 04:53:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52d4d5f8-95aa-310f-873e-a1442431d2d0 | -18.05993 | -45.95572 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e9828bb-e9a5-3672-af11-72a13e7777cb | -15.72154 | -48.93714 | 2025-08-31 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1ad4293-6a8e-321f-8467-dfb664d8c84b | -15.21426 | -56.05798 | 2025-08-31 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2add0186-008c-353f-a6c2-314a669282e6 | -17.15212 | -46.07945 | 2025-08-31 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce0ff84f-94cb-3b40-a751-869fffd60386 | -16.99964 | -49.32668 | 2025-08-31 04:53:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10d46ebd-798d-3c82-9e69-56ee989d8b7a | -20.38101 | -54.57418 | 2025-08-31 04:53:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68e33bb6-bd7f-3aea-b591-e1ef4df668eb | -14.60496 | -54.52165 | 2025-08-31 04:53:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00485e63-4985-3a88-a0e5-3a796e29b47b | -20.25649 | -46.01573 | 2025-08-31 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4ea7005a-82f7-30be-b086-43aa77ef63f1 | -18.65803 | -49.09747 | 2025-08-31 04:53:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ed7eb7d9-c6ba-3b0c-a55b-2d0257f20eb1 | -15.68279 | -52.73903 | 2025-08-31 04:53:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57bc109a-faec-35c7-9947-dcf3d69121ee | -16.21603 | -52.65532 | 2025-08-31 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6198437-c876-385c-82cc-ebc20a4b4285 | -15.79297 | -55.90765 | 2025-08-31 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fe90decc-4ce7-3eef-868c-73d1a40e6d49 | -17.1476 | -46.07264 | 2025-08-31 04:53:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88781ecd-e2d7-333a-adcb-ce14ea03e301 | -16.77008 | -50.30303 | 2025-08-31 04:53:00 | NOAA-20 | SÃO JOÃO DA PARAÚNA | GOIÁS | Brasil | 5220058 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 693164eb-4b12-394f-a21c-493d7747da78 | -21.43246 | -54.1569 | 2025-08-31 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bec777f-913e-3501-a0b9-f292eb04f2f3 | -23.551 | -47.44875 | 2025-08-31 04:55:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac67e793-528e-34a2-aa2a-94008dc2539f | -23.55068 | -47.4522 | 2025-08-31 04:55:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd4a9395-b7d9-39c7-ac27-3d1e57b237eb | -21.98661 | -56.02688 | 2025-08-31 04:55:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e98211b-a159-3f85-8689-092812a6ffe2 | -20.55075 | -56.26198 | 2025-08-31 04:55:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbed0a5a-21b8-3ff0-8bc0-059dfbbba6ee | -22.6224 | -47.93969 | 2025-08-31 04:55:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 398457b5-adfb-3cdd-b272-2af41fe62638 | -21.43305 | -54.15292 | 2025-08-31 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d943ccc1-2e96-3210-a56a-e6321235ec14 | -23.54552 | -47.45138 | 2025-08-31 04:55:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 417269af-bc60-3b5a-904b-52fd72a183b0 | -20.55407 | -56.26258 | 2025-08-31 04:55:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fc317d6-24ab-3401-ae9c-93e2c73ffe2f | -22.24966 | -56.12252 | 2025-08-31 04:55:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b944145-f862-3e9b-ad72-0918ee1343b0 | -25.09957 | -53.11149 | 2025-08-31 04:55:00 | NOAA-20 | CATANDUVAS | PARANÁ | Brasil | 4105003 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f48985e2-2356-3804-84ba-ee0e74b3c74b | -23.54585 | -47.44791 | 2025-08-31 04:55:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 828f864a-3e2c-3eb2-b821-3d300188a7b1 | -23.70649 | -47.48028 | 2025-08-31 04:55:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 649d0a0e-0093-3cab-b3c1-3fcdf7672083 | -24.99658 | -53.46885 | 2025-08-31 04:55:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 277a8ada-60a6-3d31-b923-64b0debc1386 | -22.83583 | -47.78917 | 2025-08-31 04:55:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a004934f-0499-36d5-996d-ac441738224f | -21.15106 | -53.41012 | 2025-08-31 04:55:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7624557-dc0f-37a1-92f8-b1c7a2f1046b | -22.81972 | -47.33143 | 2025-08-31 04:55:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ecb4f57e-f285-317b-b224-3fcf52f65d5b | -22.24908 | -56.12625 | 2025-08-31 04:55:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6a520ba-9fb8-3929-969f-54c8def5910f | -22.8833 | -50.3247 | 2025-08-31 04:55:00 | NOAA-20 | PALMITAL | SÃO PAULO | Brasil | 3535309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a5e3ebd-ab84-3bc8-a783-680b5b982ddd | -22.83646 | -47.78311 | 2025-08-31 04:55:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 066938b0-27f7-3a82-8cc9-e7e0fc6676ad | -21.43648 | -54.1535 | 2025-08-31 04:55:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 53986cd2-e81d-3484-bc92-9ca55722298b | -20.55465 | -56.2589 | 2025-08-31 04:55:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bb5288e-2c52-35cf-9d5d-1f5a7b4f1c21 | -20.55134 | -56.2583 | 2025-08-31 04:55:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecd9e117-2516-333d-a7c9-a71b3aeec246 | -21.98719 | -56.02317 | 2025-08-31 04:55:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9f3d1ca-5f83-3516-be80-97a24ba66b2c | -23.54946 | -47.45029 | 2025-08-31 04:55:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8761f4d5-942f-3191-ba46-ea357a148940 | -22.62179 | -47.94552 | 2025-08-31 04:55:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af0fe314-85c7-3382-b32a-7550f3542f8d | -22.24577 | -56.12565 | 2025-08-31 04:55:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e9d0c87-9a20-3cb3-a7b5-17b93520bc68 | -20.98226 | -56.91782 | 2025-08-31 04:55:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17880eb1-e251-3c48-8e39-56f041df5f16 | -23.70618 | -47.48347 | 2025-08-31 04:55:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f8cf69fa-71c2-3715-81a7-87d7fb2f3b6b | -22.24635 | -56.12193 | 2025-08-31 04:55:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README72.md)
