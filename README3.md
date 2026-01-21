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
| 65f8d7ed-e65c-3406-8577-5311a2edf384 | -19.42726 | -57.28796 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d1e2c376-080a-3786-ba52-8cbf29195875 | -19.4189 | -57.3057 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7e99b13b-65f4-3b3e-af94-6f183c7dcc4c | -19.44364 | -57.2662 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| de7c69cd-fa97-3a3f-9726-bd12d8e28e91 | -19.42835 | -57.28698 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4129368d-1804-3bc3-b8e5-62c07b86e5d4 | -19.41864 | -57.30341 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 35aef911-686d-3312-ac0f-b572c5470a95 | -20.33274 | -57.90814 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 26fd9fd9-4c76-3627-8e60-6200d80038d0 | -18.59857 | -55.94833 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b89fc0de-55bc-39f3-9359-dd2bba3be94a | -20.72889 | -55.16183 | 2026-01-21 04:25:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8410ecef-5e02-3b99-b518-802c79454ce5 | -19.43494 | -57.28155 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8aa2abdc-1159-3c43-bcd3-189fc954fda1 | -19.42764 | -57.29029 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b65159fc-2851-38f7-bedf-d8eb37f21a56 | -27.38223 | -49.25002 | 2026-01-21 04:25:00 | NOAA-21 | LEOBERTO LEAL | SANTA CATARINA | Brasil | 4209805 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9355e38e-60aa-3871-87f2-b59dcce1a8dc | -19.44294 | -57.26951 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4f9dc6ba-5b67-395e-aa5c-1b8f8e86d5a0 | -20.33199 | -57.91164 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6d2ce0a8-f5f1-3b09-92cc-df88b90b2726 | -19.43203 | -57.21289 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ad436533-edf4-3ccc-8946-8d091b84d763 | -19.21205 | -53.44159 | 2026-01-21 04:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99b953b1-4810-3e22-8746-ecbfdfed81cb | -19.44081 | -57.27942 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c063ad22-eb36-3ce0-b0dc-c8e8b66af32a | -19.42033 | -57.29906 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| bb87ec5c-85bf-3cda-89a6-9f77da0d26a5 | -19.44858 | -57.24312 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a9c6e901-a7e7-3e06-8c85-62161680ee4f | -19.67472 | -56.89119 | 2026-01-21 04:25:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 466975e1-4b60-3f2c-ad84-f95a639e5279 | -20.32974 | -57.89638 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| acb888fb-a7cf-3cdc-99bd-30c7ec74d29e | -19.44506 | -57.2596 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b9163342-4fb4-3b5b-9958-fc982f5ffe4c | -21.36911 | -49.19442 | 2026-01-21 04:25:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61a87286-701d-329d-8c3e-2e71daabe039 | -19.43449 | -57.27921 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 64a14655-7e1a-3416-88eb-819a79dd51b3 | -22.02205 | -56.34323 | 2026-01-21 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 38a84d8f-c9af-337b-90fe-470ef0ab9079 | -19.39178 | -57.27624 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5ef168cd-a15a-3b60-b135-8759bf373d27 | -19.43362 | -57.21215 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| abb60258-602c-3259-9210-81c6d59e1d95 | -20.34178 | -57.89192 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3ef67f55-c58e-3328-a824-e6523cb0c8e5 | -19.44542 | -57.22634 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1517500b-87b3-384b-833d-d985255ff37f | -25.25693 | -50.21196 | 2026-01-21 04:25:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0b52359e-f0e5-3530-a6da-ebd027caa467 | -23.60152 | -48.25849 | 2026-01-21 04:25:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93d8077c-c780-3b89-a6df-5762e9e6a68a | -20.34704 | -57.89319 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 067b2a3e-eecd-36c1-b955-060c0f34d329 | -20.79086 | -49.62312 | 2026-01-21 04:25:00 | NOAA-21 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bf05ca46-abd9-3e79-a2c0-6412f8649c3f | -19.43312 | -57.28585 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| aabd46ca-1318-3919-a042-20feb723a4f5 | -19.44999 | -57.23655 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a6dd3898-c7e7-3c7f-8b60-df3ff71bc750 | -22.73444 | -49.34257 | 2026-01-21 04:25:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8c09404-1969-3e05-9d3e-4973c02837f4 | -19.21586 | -53.43893 | 2026-01-21 04:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6657fad3-198a-332d-b21a-6029b0f35bf3 | -20.90706 | -56.38747 | 2026-01-21 04:25:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cd7f214-8016-3486-aa74-2dde3d8b0303 | -22.02356 | -56.3458 | 2026-01-21 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb4985b4-5904-3169-86e9-75a979aca53a | -20.34629 | -57.89669 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b105d844-bd46-386f-b850-8c132907f224 | -23.60815 | -48.25969 | 2026-01-21 04:25:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ebe121f-c1c5-3882-96d3-bd829e4792a5 | -19.43291 | -57.21543 | 2026-01-21 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b4fc881-c76c-3b19-94e9-66e02201af3c | -20.99305 | -48.84356 | 2026-01-21 04:25:00 | NOAA-21 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dd4c5159-8f0b-374b-b84e-0c79eecd62f4 | -20.99245 | -48.84725 | 2026-01-21 04:25:00 | NOAA-21 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ceba4a7e-1dae-3492-ac99-c36e71eab4f7 | -19.21104 | -53.44196 | 2026-01-21 04:25:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd3c0b40-1bc3-36e4-bad9-339b98765837 | -30.13385 | -51.9611 | 2026-01-21 04:27:00 | NOAA-21 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| f193b37e-030e-3415-b9b2-fedce2209613 | -30.90783 | -52.96317 | 2026-01-21 04:27:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 22c07751-a203-3d02-9d42-e9e046358f8f | -27.68787 | -48.75112 | 2026-01-21 04:27:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 64fd1aa3-60f7-3109-bad9-6b6c4d4c38e8 | -30.90443 | -52.9624 | 2026-01-21 04:27:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 7102a9a2-a792-3b53-b965-6a10bde9a865 | 2.92129 | -60.94319 | 2026-01-21 04:48:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d23bde-b22a-339c-89c8-4d64c0da3f87 | 2.92206 | -60.94839 | 2026-01-21 04:48:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd30bad-7891-33f9-a78a-72662b565ca5 | 2.91641 | -60.9546 | 2026-01-21 04:48:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe6400b-6293-387b-9b68-be7ec7bdee95 | -2.41255 | -47.45939 | 2026-01-21 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 69f5362c-6dab-38fe-97d7-00a57c814911 | -4.19247 | -48.56647 | 2026-01-21 04:50:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a91084f2-bbcd-31f1-8f0d-aa1a8395009a | -2.60903 | -47.35042 | 2026-01-21 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0d974347-eb5a-3223-ac98-6e3e16f260e9 | -3.48321 | -47.6877 | 2026-01-21 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9129ed8a-0ae9-3bff-91b0-1b528b16ea6c | -4.10192 | -47.30371 | 2026-01-21 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e7662143-88b0-321c-9985-5750c0a169ed | -4.09891 | -47.29885 | 2026-01-21 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af3e8e05-3e05-3614-9f6d-976b3a6ef7ff | 1.13071 | -60.52797 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc01e5ba-3142-3474-a048-b7d634d96588 | 1.02172 | -60.55139 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08786bb8-7ebe-307e-809f-b71b804dc00c | -2.35792 | -51.89246 | 2026-01-21 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5db6febc-1982-3203-a192-6d68e7034c1e | 1.02245 | -60.55599 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ead74a0-2ef1-31d7-bcde-1d727a883b93 | -1.58476 | -45.77643 | 2026-01-21 04:50:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abeadd6c-a25a-3f39-966b-d2d1fbadd27f | -3.15513 | -48.14782 | 2026-01-21 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97648477-b67f-3029-b4fc-5be31866fc4a | -2.42861 | -47.14429 | 2026-01-21 04:50:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ee5e73-2a6d-3ab0-928f-6bd1e5643859 | -1.95379 | -46.27727 | 2026-01-21 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1c38a67-5d36-3dbb-bcad-370cfe1a5d08 | 1.13039 | -60.52805 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8afe30b-4a0a-3e94-a049-669b88f798bf | -1.50635 | -47.32777 | 2026-01-21 04:50:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c14c184e-c139-341b-b216-b1a75e7e4d2c | 1.13648 | -60.52707 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0dd9ac87-49df-3a8b-9b58-755e05f4d470 | -2.70892 | -45.56411 | 2026-01-21 04:50:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d32d46-eb86-3e25-b01e-5c0de513d4cb | 1.02098 | -60.5468 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 818d6705-4610-3cd0-b4f5-aaef544f6dc8 | 1.1368 | -60.52697 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f19180da-831c-3f19-8057-6799c143cc3c | -3.15164 | -48.14729 | 2026-01-21 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a67667af-de21-3639-a2be-c4fc32347bc2 | -2.50775 | -47.26085 | 2026-01-21 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73008453-9975-3f85-8054-86ec752f32b1 | 1.02215 | -60.55481 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75660a48-064c-3cb7-a8ad-ffc628ca1744 | -4.09826 | -47.30314 | 2026-01-21 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db59503f-e5d1-3012-b698-e2413cabb341 | 1.02145 | -60.55021 | 2026-01-21 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50370767-3473-3b35-b51b-15ecf5c900f0 | -2.7405 | -47.3904 | 2026-01-21 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7aad87ba-1ba3-3b0b-b7db-16fee432176b | 2.56395 | -60.38368 | 2026-01-21 04:50:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6fe17c7-6020-300c-a4c8-6dc248e03202 | -5.47994 | -50.70251 | 2026-01-21 04:50:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b4992f-e0e6-3c1b-afe9-c08289f46bc8 | -2.42236 | -47.23215 | 2026-01-21 04:50:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d61d85e-1d8e-39ef-b62b-9ff295034b0c | -4.10257 | -47.29942 | 2026-01-21 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c4195ab5-a4d5-31e7-a7ee-6e94a1594405 | -18.81319 | -51.61243 | 2026-01-21 04:53:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16490ff2-7ca1-384b-a275-64ce80ff73a3 | -19.45026 | -57.24368 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 42837597-e61c-3b06-96b4-4ca5bbe6a081 | -19.41678 | -57.30809 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ead88bec-6f82-389b-a17a-70d28616afd4 | -19.4437 | -57.2601 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 07ab608d-9d3d-378e-87bd-ce0e2fd1510f | -19.29581 | -56.50664 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bf5e7946-415a-36eb-91b1-ca92fb41b6d9 | -18.81669 | -51.61301 | 2026-01-21 04:53:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13f02151-8046-38dd-9d50-09a92ffcdb88 | -19.43689 | -57.21459 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 13fbff0b-53bc-3430-b4e2-3604fccd6f2d | -18.93203 | -53.4001 | 2026-01-21 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f9f8672-4b89-32d6-893e-0e7641cd081c | -19.42187 | -57.3002 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9522c9d6-d348-314f-933e-a9b5d2baf12f | -19.43713 | -57.27654 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 789d6464-8c43-3a16-943a-fcbfa104f3d8 | -19.42618 | -57.2125 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f4e8bc22-9234-351d-b9f3-48d994943722 | -18.93363 | -53.39969 | 2026-01-21 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c9b626f-3804-32e8-a642-55decd0bb662 | -19.43332 | -57.21389 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 38a02edd-a521-36fb-af31-75c5e1c795a7 | -19.44952 | -57.24796 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9b721d2a-4ab8-349c-a7c7-aa4cb9b7903e | -15.97586 | -56.27697 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f0dd2460-b2a5-3750-83da-b5eae389e7d5 | -16.07054 | -56.58896 | 2026-01-21 04:53:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bba4a897-7384-336e-ac0d-22e81cb59219 | -19.44071 | -57.27724 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9a952fd3-8870-383a-9cc4-510ac27a2edf | -15.97429 | -56.27378 | 2026-01-21 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3b749f26-cc08-3785-98a7-2317b07f40fc | -19.39061 | -57.26744 | 2026-01-21 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
