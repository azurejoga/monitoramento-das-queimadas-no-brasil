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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69975e70-4b92-37d2-a2ad-beb03c76c999 | -12.9245 | -51.2002 | 2024-10-01 03:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 00b1d1b3-2aa7-3dfa-9876-0695a818d1cd | -12.8588 | -62.8403 | 2024-10-01 03:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bc70b610-69b1-3e02-bbfe-4a3ca95b53de | -13.2116 | -51.2073 | 2024-10-01 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9298b179-5048-3e36-9091-bc47543074ec | -13.2304 | -51.2262 | 2024-10-01 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 0f060c0d-2c4e-3d68-b51e-eac181b43a4b | -12.9169 | -62.6829 | 2024-10-01 03:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9b6c4f44-3c45-303d-8c65-64ce4f4557b5 | -12.9736 | -62.6987 | 2024-10-01 03:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c824adbe-5574-3b5e-9325-1de0aa18f41d | -13.2112 | -51.2287 | 2024-10-01 03:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a69824b6-7474-37b6-9ea3-e8a6086c5f9a | -14.7406 | -48.7498 | 2024-10-01 03:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 22bed99d-302f-3f09-a9cf-c71460d6b209 | -16.474 | -57.3553 | 2024-10-01 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| d0a135fa-57ea-32e0-9761-c1c6d128e760 | -16.4743 | -57.3349 | 2024-10-01 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| be06cb62-b4ef-3b3a-92d2-ece8bd7623e3 | -16.4935 | -57.3531 | 2024-10-01 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 61470f60-cf9f-31a6-87a5-052efc95b3c1 | -16.4939 | -57.3327 | 2024-10-01 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| fad6da1c-2cb5-39ee-914d-df4bd551463a | -16.5131 | -57.3509 | 2024-10-01 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| a5c8d575-357e-331b-bfd4-533549add48c | -16.5134 | -57.3305 | 2024-10-01 03:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| aeb94381-f9a4-35a3-ad2c-5bae2fba34d8 | -16.7461 | -57.4265 | 2024-10-01 03:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| c642441c-6bce-3a55-bcf2-17940226defb | -17.705 | -53.2046 | 2024-10-01 03:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 928372bb-e02f-31db-8984-d1d35d3ef0e2 | -21.342 | -46.4296 | 2024-10-01 03:07:03 | GOES-16 | MONTE BELO | MINAS GERAIS | Brasil | 3143005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.0 |
| 2323500c-e850-37b6-b350-1a0b62eff792 | -22.3498 | -49.3293 | 2024-10-01 03:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 4eafbd74-19ee-3200-9454-1f8b2bed9c0f | -22.37 | -49.3477 | 2024-10-01 03:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 237.6 |
| 8b92fe0a-7f5a-3b95-ab5a-6349929a6d68 | -22.3707 | -49.3244 | 2024-10-01 03:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 517.9 |
| c8fa2892-fe82-3958-94f7-1a160696179c | -22.3713 | -49.3011 | 2024-10-01 03:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 158.7 |
| 8e47d084-4b7e-3fbd-9df4-2b98de886fdc | -22.3916 | -49.3194 | 2024-10-01 03:07:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 724f9d29-aa04-37c2-ba3f-7aee579fbb6f | -23.0793 | -45.3951 | 2024-10-01 03:07:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| f5e655fc-21f0-3a7e-9631-ff5d2bfb493f | -2.3863 | -50.3299 | 2024-10-01 03:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8c8eda0c-38d8-3da1-8d79-ec8e145eef41 | -2.4046 | -50.3505 | 2024-10-01 03:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| de42668f-504c-3a77-a038-c98ca2d0eb42 | -2.4047 | -50.3295 | 2024-10-01 03:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| 33732cb4-76fc-3670-b4ea-d842f77d9928 | -2.4231 | -50.3291 | 2024-10-01 03:15:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| c4eab15f-a8a9-32aa-babf-68c9e9d13452 | -3.0282 | -51.3345 | 2024-10-01 03:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 338197d5-7994-3cdf-9045-10df128a8d42 | -5.9786 | -45.3847 | 2024-10-01 03:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| be2a8de4-3c96-3657-bdfa-d8e462507628 | -5.9788 | -45.3621 | 2024-10-01 03:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 836eb7ca-7fb4-310a-956b-93e3b2635d71 | -10.9237 | -50.1069 | 2024-10-01 03:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ca800f56-abbe-3c81-89f3-70c7a6d0145d | -10.924 | -50.0854 | 2024-10-01 03:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 0dcb258c-4f40-3b3c-97a3-eb3aa097090b | -11.6555 | -64.9991 | 2024-10-01 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 31e56f32-0b61-359b-acf9-52bbec4fe128 | -11.6556 | -64.9802 | 2024-10-01 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 1b40e717-f22a-3528-944b-a6c4aa893a6d | -11.6743 | -64.9983 | 2024-10-01 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| f0969ec4-9fa4-31a3-adc0-50a6f92aba4c | -11.6744 | -64.9793 | 2024-10-01 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 774f1b55-34be-3818-8453-2ef8b9d9342b | -12.1402 | -50.074 | 2024-10-01 03:16:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9734bb26-2db6-3341-9072-ee3884c08f4c | -12.1406 | -50.0524 | 2024-10-01 03:16:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 160b7b53-8494-3857-909a-b7b79a2cd5a4 | -12.2545 | -53.9999 | 2024-10-01 03:16:15 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2440f466-ca31-3b5e-921d-aec5dd1db35c | -12.2547 | -53.9792 | 2024-10-01 03:16:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 313db515-e4a3-3b0a-bb53-72494d314e3d | -12.9245 | -51.2002 | 2024-10-01 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 7449fb7f-e263-32d7-ac60-c371bedd280e | -12.9437 | -51.1979 | 2024-10-01 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 75eb8db8-80c1-3cf0-9c22-cd1f35387ca5 | -12.9588 | -51.4517 | 2024-10-01 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 258514e4-103c-32f4-9c1b-a8c736e98dd1 | -12.9591 | -51.4303 | 2024-10-01 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e73a2277-79c1-3b94-b0f8-7b53ef1c8f20 | -12.978 | -51.4493 | 2024-10-01 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1081d2d9-f88b-3bf1-99c4-67d1b2bfa0a7 | -12.9783 | -51.428 | 2024-10-01 03:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 46d06825-4ed5-3b40-b7f7-3c1b3330db94 | -12.9169 | -62.6829 | 2024-10-01 03:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c92c257e-083a-37cb-9522-3b7bc947a9f2 | -12.9925 | -62.6976 | 2024-10-01 03:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 205302c1-2d15-3b6e-9c32-72cd2bca0c4d | -13.2112 | -51.2287 | 2024-10-01 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 89148601-692a-371b-8d19-d1b555d8b6ce | -13.2116 | -51.2073 | 2024-10-01 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| d101ea0a-9998-3a82-9ab3-28d686717514 | -13.2304 | -51.2262 | 2024-10-01 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4e21a5a7-1da1-39da-a38a-fbb48e9886c3 | -13.2308 | -51.2048 | 2024-10-01 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 8074d426-630e-361b-ab8f-9ec51d618570 | -14.7211 | -48.7529 | 2024-10-01 03:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 18a1263f-5124-37f3-bba3-f5a1253c3f3b | -14.7406 | -48.7498 | 2024-10-01 03:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c334e915-1676-3282-a761-c464d5d93dae | -16.474 | -57.3553 | 2024-10-01 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 9aceb045-2586-3b49-a5ac-4a9795099fda | -16.4743 | -57.3349 | 2024-10-01 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 647437e1-ea49-3101-a0fe-218530a43ac4 | -16.4935 | -57.3531 | 2024-10-01 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 46c4b7c8-ff23-3fe4-86fe-76908851ed21 | -16.4939 | -57.3327 | 2024-10-01 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 1ee91716-2def-399a-9182-6dd1def47346 | -16.5131 | -57.3509 | 2024-10-01 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 0ea12dbe-4a65-3252-ac1e-68700f13935c | -16.5134 | -57.3305 | 2024-10-01 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 1e5a8d3d-08cc-36ac-91a0-5993fef7188f | -16.8288 | -55.936 | 2024-10-01 03:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| e74d2fae-aeed-36da-bfb0-d0784660c79b | -16.8292 | -55.9152 | 2024-10-01 03:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 063762a5-5be6-3fa9-9ff1-dd6e88fcbbc4 | -16.8484 | -55.9335 | 2024-10-01 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.6 |
| b99cb282-c37c-37f3-b4c1-c83d086e7fc5 | -16.8488 | -55.9128 | 2024-10-01 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| fba8552c-646d-369c-a060-497005667e07 | -16.8491 | -55.892 | 2024-10-01 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.6 |
| 47a0f727-8fa1-3ad5-a463-5ec40a46fad4 | -16.8684 | -55.9103 | 2024-10-01 03:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 344fb901-6670-3bf3-97b4-c77c5a78e4c9 | -16.8784 | -57.7175 | 2024-10-01 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| e0609910-4733-3d00-8145-637103b8b51c | -16.8787 | -57.6971 | 2024-10-01 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 5f8ead6d-8997-3523-a79e-220a8cef2083 | -16.898 | -57.7153 | 2024-10-01 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| b85a74b5-612a-3386-b353-ac559266659d | -16.8983 | -57.6949 | 2024-10-01 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| b84d7056-1cc7-3ee6-be17-2a93c123f721 | -18.6973 | -57.333 | 2024-10-01 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 078281f0-150c-34fa-8569-f613fda7fd10 | -22.3713 | -49.3011 | 2024-10-01 03:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.7 |
| 7539628f-815a-35a6-a572-d8817b1b2e33 | -22.3498 | -49.3293 | 2024-10-01 03:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 117.0 |
| 78546f82-5d69-3b6d-8173-95cf09d6fd03 | -22.37 | -49.3477 | 2024-10-01 03:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.0 |
| d1c281ae-ab9c-33f9-812e-5e483121c5ba | -22.3707 | -49.3244 | 2024-10-01 03:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 343.2 |
| c7fa5b4c-70ab-36a6-8887-e2c0df169af8 | -22.3916 | -49.3194 | 2024-10-01 03:17:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.8 |
| fc7b0037-82f3-3f84-9234-c7495b5d3a32 | -23.0793 | -45.3951 | 2024-10-01 03:17:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.6 |
| 3a6435b4-a42f-385a-ba43-ec711da2141d | -3.96516 | -41.48837 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5099c49b-e87c-396f-ab75-9205482c3986 | -3.94753 | -41.5165 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8f103f52-3b54-35ab-8420-ad06489868c0 | -3.96433 | -41.49332 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 22ed20ef-d371-3bb3-a80e-0d048817b679 | -3.96242 | -41.49039 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e39eb172-4938-3027-b320-954c062d4dce | -3.95805 | -41.49241 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fbb795cc-d316-357e-b88c-e6cd2719a859 | -3.95381 | -41.51748 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8bfca327-b730-3a49-8466-6c17e2c4e85d | -3.95295 | -41.52258 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3fe38e30-09c6-32f5-938a-129b6163e3fd | -3.95174 | -41.51443 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c1d7b3a3-2d4a-3c5f-a5cd-651d6661e64f | -3.95084 | -41.51951 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68dc1c1a-59c0-39ed-9006-62dab093cf91 | -3.94546 | -41.51348 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bd3a711b-e92f-3afe-b4c5-57c4f199cef2 | -3.94457 | -41.51852 | 2024-10-01 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c91f467a-6698-3f3c-99b5-a1d59a70c08f | -4.08111 | -38.3792 | 2024-10-01 03:21:00 | NOAA-21 | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a7173cf-d9fe-34f5-b845-58e1cccd3a68 | -6.68642 | -43.55025 | 2024-10-01 03:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0bbcffc7-ae1a-3f12-ba11-215bdae027d7 | -6.26617 | -42.54226 | 2024-10-01 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5d0bdc73-5633-3b3b-a283-27c9009c6d4d | -7.85456 | -43.08547 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b472689-9c31-30bf-be64-33f0a01fd85d | -7.85451 | -43.08712 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6861328e-7775-37b1-a4b6-699c29b85530 | -7.85349 | -43.09125 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 373a1c28-0fd8-338d-bf17-e814e576b200 | -7.85339 | -43.09291 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca4e850a-54be-3a01-9045-afdbf98f7527 | -7.85228 | -43.09872 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5e381093-fda6-316b-817e-81a2c50d7121 | -7.84813 | -43.08407 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4a69f313-c7ca-30e8-a121-8e6ecb623776 | -7.84808 | -43.0857 | 2024-10-01 03:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a736cf4-0a2f-3e41-b7ed-920f2132e29c | -7.28188 | -43.38189 | 2024-10-01 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b66a8334-d91e-30fa-97db-8e2002fdca48 | -7.28081 | -43.38751 | 2024-10-01 03:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
