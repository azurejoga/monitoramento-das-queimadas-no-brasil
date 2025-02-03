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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 997a9b8b-8247-31ee-882d-78a9969ecd2f | 2.88668 | -61.58035 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07e7362e-49b3-3031-bb50-45e33be79464 | 4.43171 | -60.73489 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0057b6d4-d4a6-30f3-a5e1-ce226fc8640e | 4.4365 | -60.7379 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6909271b-b016-31b7-bf17-484369bfa64c | 4.11072 | -59.903 | 2025-02-03 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f721f26d-7498-36a4-bf34-8e87f29f6c83 | 4.43593 | -60.73418 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc4cd5d4-c0f6-370f-bb1f-465ab41677fb | 2.8854 | -61.57186 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b8fb57c-41d7-30da-9348-1bfa90a2f059 | 4.42997 | -60.72342 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f850abd-ec51-30e7-a9c1-89ef9cb0ca4d | 2.88731 | -61.58452 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b34298e3-2b27-3c60-b078-64e19df17b41 | 2.88604 | -61.57611 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 61fe5d5b-c2a6-38a2-87d1-495708f4ae32 | 4.45691 | -60.78893 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 309ab8f6-6cde-37f3-97f5-d291e5aef7c0 | 4.10624 | -59.90021 | 2025-02-03 05:05:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 414dd276-3085-3aaf-bf2f-4704c6d0257a | 2.89416 | -61.57058 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a176c3ad-c2fb-3bc5-9107-838738323e23 | 4.46979 | -60.75842 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e5de181-43c6-3315-b734-e31a6c0a12fd | 2.01958 | -61.41714 | 2025-02-03 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88f60495-025f-3ff9-8855-023dee393f3c | 2.88978 | -61.57122 | 2025-02-03 05:05:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c31bed1-4e80-3459-a8b3-ab38fe5a4aa0 | 4.43057 | -60.72736 | 2025-02-03 05:05:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bd1d3b7-837d-35b0-8e48-1d8ce86b6587 | 2.02019 | -61.4211 | 2025-02-03 05:05:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a265ff7-6e91-3aa0-8e68-cc587962cb20 | 1.02259 | -59.53088 | 2025-02-03 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 143581f2-34c8-3fa7-bca6-1777ed772652 | 1.0219 | -59.52643 | 2025-02-03 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 497cbfec-02de-34b3-8cb2-ad7505d9647c | 0.72468 | -59.41422 | 2025-02-03 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e565010-9ff4-36fd-bdf6-acbfacf8796e | 0.95206 | -59.5541 | 2025-02-03 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6072f00-8217-32f9-9bf3-bdb29a4cf4b6 | 0.72838 | -59.41365 | 2025-02-03 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cfba024-0ebc-3c4f-867f-8086fd1e3d50 | -19.59127 | -55.30737 | 2025-02-03 05:12:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb396f8d-3f42-3eed-b4a7-f4da2cedde0a | -29.6277 | -51.96896 | 2025-02-03 05:16:00 | NOAA-20 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ac811a2f-56c0-39d5-90db-e55d8af711f4 | 4.10129 | -59.8979 | 2025-02-03 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| daedf603-38bd-36e2-bade-95982433a009 | 4.45402 | -60.7907 | 2025-02-03 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fb191e0-d143-3523-a096-873877899e99 | 4.45335 | -60.78657 | 2025-02-03 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a4c11dc-106d-3585-9372-13670ebe546b | 4.10615 | -59.89737 | 2025-02-03 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68912486-d4e9-3947-8648-a7fe5bd800e1 | 2.89073 | -61.56892 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4336ac0d-a872-352b-8abc-1c531942dced | 2.88268 | -61.57465 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a835e0f4-d0bb-31df-a091-534b70ffb934 | 2.87971 | -61.58391 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afd117df-8e54-3304-a10f-76a22be8d2a2 | 4.10186 | -59.89839 | 2025-02-03 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 290c1ee9-b5bb-34a5-836e-3efd36591e1b | 4.10758 | -59.90318 | 2025-02-03 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9bec9271-3e0a-3aa9-a4d7-9e1fbf87cc6e | 2.88408 | -61.58318 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a80477de-3675-3ad9-aeaf-9ea21f461df4 | 4.42939 | -60.72507 | 2025-02-03 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcb679c1-3a9e-38bf-9017-8982f5337043 | 2.89003 | -61.56468 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5e3ae96-f613-3b7d-844d-f6df64641241 | 2.88775 | -61.57814 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f17f26ca-3c54-37d0-830a-596547125204 | 2.88705 | -61.57391 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9bbec332-04fc-3304-b1a0-f150aad45828 | 2.88636 | -61.56967 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc50b874-4b8e-3a47-990c-31e015ef2e01 | 4.44892 | -60.73089 | 2025-02-03 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 32136091-f4c4-3657-997c-148c68af187d | 2.89142 | -61.57317 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bf9b40e-b40b-3ed0-bbb2-5c2376a1e0e3 | 4.10707 | -59.90275 | 2025-02-03 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0c2d28b0-595c-3a62-bf09-43b9f885d21e | 2.88338 | -61.57889 | 2025-02-03 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1355d584-1f88-3ecc-b7b1-efd1fd68b342 | 4.1067 | -59.89778 | 2025-02-03 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 574cf8e4-ce0f-3236-84a6-b57b9e568c4d | -10.61516 | -68.47799 | 2025-02-03 06:01:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fe3e170-cdc6-3cde-9bdd-e9292bb6e5d4 | 2.88848 | -61.58256 | 2025-02-03 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6059a783-bd1a-3583-a4f4-1b0cbe1ac7aa | 2.89314 | -61.56905 | 2025-02-03 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f09744ad-0656-309a-ab41-5055b379c1de | 2.88741 | -61.57635 | 2025-02-03 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42d77e09-bdd8-3044-a3d8-c395878ec312 | 2.88065 | -61.57764 | 2025-02-03 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92173f78-367b-3db4-8dd6-d2ed50c0a427 | 2.88637 | -61.57033 | 2025-02-03 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cee87a2-40fc-3801-b4e1-fbe7fc976356 | 2.88171 | -61.58381 | 2025-02-03 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba3b9f9-73bb-3cc1-aa48-6d023f33e79b | 4.10972 | -59.90698 | 2025-02-03 06:37:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa070d72-5cf9-3cf0-82d3-66d5ee26610e | 2.89053 | -61.56297 | 2025-02-03 06:37:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fbe883da-667e-39aa-8149-1a7ebd07c3ba | 2.89184 | -61.5717 | 2025-02-03 06:37:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4a1dab26-4b3b-3ddd-b446-947f38f44b27 | 4.1083 | -59.8977 | 2025-02-03 06:37:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 53020fd7-a6d5-3428-8e89-beca55e0c9e6 | -3.96338 | -41.49316 | 2025-02-03 12:46:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 26cd6b03-1125-30f3-baa5-3d3c22c6467f | -6.76742 | -43.82522 | 2025-02-03 12:48:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 57c604fc-9319-3e51-811f-43db211c0a60 | -6.76966 | -43.81246 | 2025-02-03 12:48:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| bf9828aa-7438-3b69-9976-fd0b17d0dc96 | -6.93501 | -42.83138 | 2025-02-03 12:48:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 9b151295-5c03-3db4-a4d2-b2d154436063 | -21.93332 | -54.4343 | 2025-02-03 12:53:00 | TERRA_M-T | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 134b2415-72c4-3060-b62c-c39c58a27c55 | -22.43058 | -54.98733 | 2025-02-03 12:53:00 | TERRA_M-T | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 8cb85187-f0cb-381e-bb9f-fb0b97934e86 | -21.4768 | -53.59423 | 2025-02-03 12:53:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 89c4ad11-8fda-3d17-b578-50efb06639ff | -21.70008 | -54.26667 | 2025-02-03 12:53:00 | TERRA_M-T | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1de65566-42fc-3e08-a149-ad527f2df88a | -21.58806 | -54.15283 | 2025-02-03 12:53:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 70eb9462-3494-35f0-b1b0-e0eb80150646 | -28.97402 | -51.071 | 2025-02-03 12:55:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| a1c13aa5-727e-36e1-8e3c-3fca2ad1ae75 | -29.57406 | -50.79377 | 2025-02-03 12:55:00 | TERRA_M-T | IGREJINHA | RIO GRANDE DO SUL | Brasil | 4310108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4048e88a-178f-36de-a7bc-598f5e225896 | -29.26228 | -51.99282 | 2025-02-03 12:55:00 | TERRA_M-T | CAPITÃO | RIO GRANDE DO SUL | Brasil | 4304697 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| af5bb8bc-22c6-3c9a-b02b-559a2e7b528f | -29.03168 | -51.18341 | 2025-02-03 12:55:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 52c32599-a4bc-38d7-8e84-0835b237b542 | -29.25247 | -51.9911 | 2025-02-03 12:55:00 | TERRA_M-T | CAPITÃO | RIO GRANDE DO SUL | Brasil | 4304697 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| abf998de-19b6-3c28-82fd-979d818ceefd | -28.84818 | -51.89313 | 2025-02-03 12:55:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3ce6d8e2-27af-3cb2-9a69-81eb91ec6595 | -31.08054 | -53.27271 | 2025-02-03 12:55:00 | TERRA_M-T | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| eebf3c91-32b5-39a1-b372-a423797c7a20 | -23.42098 | -51.97989 | 2025-02-03 12:55:00 | TERRA_M-T | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b9645f36-9db1-3996-a4c3-34249171e92f | -23.98999 | -51.98505 | 2025-02-03 12:55:00 | TERRA_M-T | BARBOSA FERRAZ | PARANÁ | Brasil | 4102505 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |


