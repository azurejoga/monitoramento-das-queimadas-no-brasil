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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6251c25-0dfd-3cc3-9934-3264b26094f8 | -11.31939 | -47.42347 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd30c044-47d1-3e3f-b78b-a2dd2b13c8cf | -12.22236 | -46.60447 | 2026-05-19 04:44:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac0be8c4-380c-3fc3-acb4-2f999de0be70 | -14.16197 | -52.88832 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c5486e3e-8cbb-360f-aa1f-362b0762abe1 | -12.06025 | -45.28504 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ce83f86-e5bf-3cf9-909f-4677064e9fa4 | -14.59672 | -47.88705 | 2026-05-19 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55c3726c-f14e-3af1-b39f-deb21d879bd4 | -14.15048 | -52.89061 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f47b0cb1-3159-396a-be27-75eab5b646d8 | -11.63583 | -48.02451 | 2026-05-19 04:44:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc08b9cc-84cf-3202-b4af-94f2361e21eb | -12.5524 | -48.36134 | 2026-05-19 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17225605-b9b0-368c-87cd-8b8dac3dcb7d | -11.91793 | -54.10331 | 2026-05-19 04:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52308148-bc52-3dc5-899c-3952a76c84ca | -14.16268 | -52.88417 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7affbf07-d5c1-3bb3-8b04-26eed3a21bb0 | -11.46218 | -55.12212 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec666da3-97c5-3dd9-824e-d8adae21b376 | -11.45476 | -52.92248 | 2026-05-19 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 235a9ba8-42be-344f-82fe-0d1b4bb30c59 | -11.46297 | -52.91931 | 2026-05-19 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22413b9b-2766-3fee-8a25-2f575f18a57e | -11.61214 | -47.1024 | 2026-05-19 04:44:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d805f81-fdd6-3472-96a5-2cc59eb3feef | -11.45087 | -55.11174 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| beeb3238-023d-3643-a512-1c0f6cf51c91 | -10.87825 | -51.31799 | 2026-05-19 04:44:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ef9524b-fab1-37a9-af03-17ffc15c5bdd | -17.70371 | -46.23312 | 2026-05-19 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d6d806c-0e44-377e-9b7e-6d2e56e0497b | -12.05016 | -45.27391 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 281a8a57-ade2-37b4-ba4f-4300e055e9b9 | -11.4501 | -54.09079 | 2026-05-19 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4a4104a7-a73d-3e1b-af02-b63d98d7fee2 | -13.29077 | -50.2354 | 2026-05-19 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3ae0915-fb75-35fc-ae26-074d1df5acea | -14.70922 | -48.32461 | 2026-05-19 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e3a5659-7ab7-336f-8534-c9e5f1750473 | -11.03293 | -49.48231 | 2026-05-19 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de3151be-5321-33a9-ad36-a2a18fe27662 | -12.05463 | -45.26978 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d59cbaad-ce69-35b8-9366-e7920b169a29 | -11.84436 | -48.25403 | 2026-05-19 04:44:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a15d443c-8535-3219-bad1-7755c5f79b37 | -12.00529 | -43.84271 | 2026-05-19 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce4153f3-0820-35b8-9d8a-57b497a7c525 | -11.97991 | -47.36404 | 2026-05-19 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9572e1c-030e-3a93-8234-b5db6d5032f7 | -11.46362 | -55.1141 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cd1a264-8e51-3ada-abcd-8753b5c5ed5d | -11.20793 | -55.92767 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f61ca82f-097c-308c-86f9-270adc752600 | -11.61272 | -47.09854 | 2026-05-19 04:44:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d2dcc29-41b8-3602-bb8a-1efd21ba3dfa | -13.59421 | -47.4188 | 2026-05-19 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9ee13b3-661b-3e5e-b6a9-72f109d4dbeb | -11.44918 | -54.09601 | 2026-05-19 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7264b783-0a02-3595-b48d-74b5acd7edfe | -13.03135 | -49.93303 | 2026-05-19 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 400c6133-51ef-3c30-ad92-e62514d97e06 | -11.45159 | -55.10774 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 741f7b30-7085-3836-bfc1-8e1e472cb97e | -15.32911 | -47.84067 | 2026-05-19 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f246fcc3-efba-388b-9a58-9be3b69195f4 | -11.27352 | -49.48142 | 2026-05-19 04:44:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5138c22f-4922-3f2b-93f1-829db12a15cd | -12.23061 | -49.39471 | 2026-05-19 04:44:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a42e3b5-ca2e-3de7-b7c4-c8d4285ab86d | -14.70581 | -48.32406 | 2026-05-19 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e2270e0-9d3b-3889-ab00-7a53905204ae | -11.97877 | -47.37164 | 2026-05-19 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2592c833-d08c-397f-bb9f-2c27eb3dc67d | -14.59614 | -47.89098 | 2026-05-19 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36de46d1-cc0a-3d76-bab0-02a51bc3f58e | -11.75049 | -54.79491 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df7eb5f8-d32c-3b39-999b-ba9e63424b4c | -11.63464 | -48.02468 | 2026-05-19 04:44:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ead222ee-3c70-311a-b6a9-5caddd26ed75 | -13.52919 | -46.7167 | 2026-05-19 04:44:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e9446aa-dab7-3130-b65b-8d49fb9458e4 | -11.45865 | -55.11731 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6af285b-f361-3b8e-855b-6860bf4368f1 | -11.18467 | -55.92107 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97094e02-26b1-3399-b4db-1e28f34e0ae4 | -15.03999 | -52.22269 | 2026-05-19 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8216eac-b175-31d2-8ddc-05ec01b36ed4 | -15.33396 | -47.84037 | 2026-05-19 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28020258-8698-30b7-bbd2-306d90d420bc | -11.45512 | -55.11252 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7bea3542-36e4-3032-b299-b88f7d2708b1 | -13.59074 | -47.41818 | 2026-05-19 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21ecc3ce-e910-38a8-8a94-75b7088a59d7 | -13.03079 | -49.93658 | 2026-05-19 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fd29bed-5431-3d67-ba71-3e75a225c7e9 | -11.84713 | -43.96659 | 2026-05-19 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb6a558c-c60a-3faa-bab5-e8f90dff642e | -11.96261 | -49.52522 | 2026-05-19 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96724723-2e7a-344b-acf0-46ee07309919 | -11.18703 | -55.91455 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 457c9fd0-93e7-33d7-af79-31d38e22c7d5 | -11.33023 | -47.44439 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6472bd1f-e9f8-3c58-972a-cafcd69fc597 | -14.15335 | -52.89544 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb8bfc87-c1ee-3434-a2c9-846a3d9aec53 | -11.45439 | -55.11654 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18040aba-b369-37f3-ba18-722eae813928 | -12.05072 | -45.27664 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea64802-a2c4-3788-9558-b36a0c837d6f | -12.06406 | -45.2856 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b5a766d-4498-3523-8f59-80fd94fceb8d | -11.45924 | -52.91866 | 2026-05-19 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9130d00-bff4-34bf-a6bd-019e877b9791 | -11.17718 | -55.91742 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10b10263-e8c0-3af1-97f7-9c657a0f5697 | -11.45552 | -52.918 | 2026-05-19 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a122227-642d-3d32-b64a-2835267b6bdd | -14.17705 | -52.88674 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 943bab22-9ea6-33b3-8ea8-a91c762bae08 | -14.16627 | -52.88481 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c7af3a4b-785f-34eb-811a-a54c219de621 | -11.32738 | -47.44008 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63369221-12a4-31f4-99b8-7d3d84bee334 | -11.60867 | -47.10186 | 2026-05-19 04:44:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80688bd2-69e9-3df8-8e77-a00d41370801 | -13.51146 | -47.67772 | 2026-05-19 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd34aa38-fdb7-3112-935c-4487964975cb | -11.97532 | -47.3711 | 2026-05-19 04:44:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4c3360d-b3c4-3bbb-9421-dce4457719e8 | -16.35299 | -43.87889 | 2026-05-19 04:44:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fc63ed9-fcc1-38c4-8bda-b6b3fca3ffcb | -11.43324 | -54.09311 | 2026-05-19 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9beee1af-53ba-3379-94bd-5adf9821d46c | -11.07913 | -48.26175 | 2026-05-19 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f8e509f-6063-33e3-9562-02df1e668529 | -11.4629 | -55.1181 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08227496-aaf8-346c-a361-b1236a5672f1 | -11.74566 | -54.79796 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eebabba-7a47-3608-aa3d-e2d7dff6dc4e | -11.74497 | -54.80182 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f46eeac4-e4bc-307a-8e5c-11336da38dfc | -11.1862 | -55.91904 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 551e5242-94a2-3bc4-ab1c-472739f019e6 | -11.45848 | -52.92314 | 2026-05-19 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef6781fe-3ff9-3ec0-a08a-d557ee6ff3ad | -11.97672 | -52.46465 | 2026-05-19 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ddb1442d-7485-36ae-a420-ed5371b6f312 | -14.15621 | -52.87873 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58248277-a094-3444-8348-bb0f41926571 | -11.93405 | -49.47676 | 2026-05-19 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c896c73d-e36f-3fd7-b73e-ba88fbb1e98d | -14.97404 | -45.45694 | 2026-05-19 04:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 355216b7-cf9a-371a-b188-6db5641bfb29 | -11.83193 | -47.51155 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bbe24b0-f798-3973-9e44-96aa949f6599 | -11.45014 | -55.11577 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abdfa48f-4bb0-3f65-b7e6-adb2060ebb1f | -11.45937 | -55.11331 | 2026-05-19 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a9edca6-d38b-35de-ab18-130317b7ede0 | -15.33259 | -47.84121 | 2026-05-19 04:44:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63fdb50e-9ddd-3cf6-b5a8-7306ec3e79c2 | -14.15838 | -52.88767 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5f82c6e4-f8ae-332a-8a67-b429e7caa7cc | -14.1598 | -52.87938 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99109d9c-4faa-3fd1-962b-bf8452b5a3af | -11.18546 | -55.91656 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94a753be-85e2-3e80-ad8e-e11fb899deae | -14.16483 | -52.8716 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51fbc4c0-71d5-377a-a81d-2fad84ab5ea7 | -14.16339 | -52.88003 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12675d4d-32d6-3815-ae2f-7f5c34bca104 | -11.60925 | -47.098 | 2026-05-19 04:44:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53a52b75-9b92-3e18-88ff-fc02c5ed2cad | -11.18016 | -55.92022 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46478a1d-79fa-3115-9071-63850796b58d | -11.18169 | -55.91821 | 2026-05-19 04:44:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 185aaed6-b4ff-3eb1-8463-8a0a12ef4b43 | -12.05141 | -45.27196 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dc0f0fd-2f32-329f-a58a-d101600d872a | -11.3137 | -47.41479 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adb559ec-6b10-30a1-9f87-feaacca5a4e6 | -14.16698 | -52.88067 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6dfac0b-87f6-3bfe-bd02-cc56382bd586 | -11.31712 | -47.41531 | 2026-05-19 04:44:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79c85163-0c21-3d82-b27e-a43265e9e22e | -12.05397 | -45.27447 | 2026-05-19 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f31124f-c87e-3bd9-80c7-63a2a6865167 | -13.02802 | -49.93248 | 2026-05-19 04:44:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dc8e827-bf4e-3ec2-8514-8f48230b157a | -11.47041 | -52.92062 | 2026-05-19 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fc7637d-54c5-3230-b747-9a643710c272 | -11.44428 | -54.10052 | 2026-05-19 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6535e5f7-b152-3068-a201-bf5824a0cdca | -14.14975 | -52.89482 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7ddf068f-a6dd-36e4-ac68-f18f33a7f5a9 | -14.15909 | -52.88353 | 2026-05-19 04:44:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README6.md)
