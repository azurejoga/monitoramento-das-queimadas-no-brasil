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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ee8f045-9e4f-35ba-931e-69f872b1461e | -2.3863 | -50.3299 | 2024-10-01 04:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| d478db4c-b2c9-37ad-a190-e338c80f25cf | -2.3862 | -50.3509 | 2024-10-01 04:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a42ed6f0-b2f9-3ab2-902e-bfe7ad3c34df | -2.4231 | -50.3291 | 2024-10-01 04:05:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 63cbfa3b-af93-3fd2-bd39-2c46c8296068 | -3.0282 | -51.3345 | 2024-10-01 04:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 481b9249-b550-3fa7-b784-94ee12e7e2dc | -5.9788 | -45.3621 | 2024-10-01 04:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 15b76d80-81a8-3d42-b43a-14c4aa8eba0d | -5.9786 | -45.3847 | 2024-10-01 04:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 21753a9f-9852-39bc-b2cf-362e3bd7df3a | -10.9964 | -46.5192 | 2024-10-01 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 523ec9e0-c4ea-32db-8bf1-a7526632093b | -10.996 | -46.5418 | 2024-10-01 04:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 91e49cb0-1690-33c8-9d4a-57a8d1e3cf91 | -12.1406 | -50.0524 | 2024-10-01 04:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f17f2f32-a297-3c39-8be8-dfdd29d60053 | -12.1402 | -50.074 | 2024-10-01 04:06:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 71a271a5-21ba-324b-95cb-8adc557205dc | -12.2738 | -53.9773 | 2024-10-01 04:06:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 842cb57f-3854-3951-a883-427edf4875a6 | -12.2735 | -53.9979 | 2024-10-01 04:06:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| c9acf9f9-1e73-372b-af3a-73e7669368a0 | -12.2547 | -53.9792 | 2024-10-01 04:06:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| b933d3db-1fdf-3d65-a09d-4d765553945e | -12.2545 | -53.9999 | 2024-10-01 04:06:15 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 156.8 |
| aa07c6dc-358b-348a-8d3f-eb94faea90b6 | -12.9591 | -51.4303 | 2024-10-01 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 456b4790-38a7-30ea-86d7-7e7d30339d7e | -12.9588 | -51.4517 | 2024-10-01 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 8e3f2807-5f42-3d40-88d5-42fa651c4f06 | -12.94 | -51.4327 | 2024-10-01 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1ddf7a9c-7499-3a2a-aaea-3481778690f5 | -12.9396 | -51.454 | 2024-10-01 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e9b9e016-553a-39c2-a1f5-98e1c96acf5a | -12.9249 | -51.1789 | 2024-10-01 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e3826e66-65d6-3234-8ade-619a5e546596 | -12.9245 | -51.2002 | 2024-10-01 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 958fff1d-8f36-399c-bd23-6a6bf84ece33 | -12.7827 | -62.8832 | 2024-10-01 04:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f72288a4-5db7-3069-9f43-cdcaab9a443c | -12.7826 | -62.9025 | 2024-10-01 04:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7be0bcc1-c62f-3c8a-b45a-dcc768f46774 | -12.7636 | -62.9036 | 2024-10-01 04:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2ff6cd32-8f0a-3b84-8c56-d1377f4f2dbd | -13.2308 | -51.2048 | 2024-10-01 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e7411f91-a365-366c-a4cb-bfd2c9e05cf9 | -13.2116 | -51.2073 | 2024-10-01 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5ae3eeba-da40-3caf-b7b1-007604176ea5 | -13.2112 | -51.2287 | 2024-10-01 04:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fa48ecb4-2e63-3979-84e9-3b18ef75f7b4 | -13.5066 | -48.5825 | 2024-10-01 04:06:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| edc9e395-e1ed-3bcc-97c7-56f553b177b8 | -13.6357 | -51.0888 | 2024-10-01 04:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| f805b663-aeee-320a-8e52-719d64a281cb | -13.6353 | -51.1103 | 2024-10-01 04:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 982b856d-7cda-381f-bca1-14e9bb321afe | -13.6164 | -51.0913 | 2024-10-01 04:06:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3131271d-d1a5-36b1-a89d-193f6588ab8f | -14.7406 | -48.7498 | 2024-10-01 04:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 7a72ef65-b5c7-34e8-a50c-b62587890583 | -14.7402 | -48.7721 | 2024-10-01 04:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 319f3bf8-cba3-356b-9e74-f092588d2f34 | -14.7211 | -48.7529 | 2024-10-01 04:06:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8768e0d0-73e1-311c-8db4-e833a7a33754 | -15.9127 | -57.1733 | 2024-10-01 04:06:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 13eaa94e-e476-36ab-8543-e7d2a79de743 | -16.5134 | -57.3305 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 024ee1d5-4019-3026-a4e6-71d8d1e7b6a6 | -16.5131 | -57.3509 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| b22fa745-5378-3b69-bd05-f831bb3c4b9d | -16.4939 | -57.3327 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 1cad0f1d-ffd4-3721-ac8e-58d86f06a5d5 | -16.4935 | -57.3531 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| d74dbe18-8994-3abc-a80e-e057aaf8d63d | -16.4743 | -57.3349 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 1bf67745-398c-3daa-8572-c3e6da7f9626 | -16.474 | -57.3553 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 104f2107-30e9-381e-b1d4-85c32b549a4e | -16.4536 | -57.4188 | 2024-10-01 04:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 86565383-0c79-38bc-a877-4e80df91bcf8 | -16.6701 | -57.2922 | 2024-10-01 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| a84882f9-9fee-31d8-8685-26d9567f0f2c | -16.6512 | -57.2535 | 2024-10-01 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| efd73538-98ef-37dc-8abe-3a55de21d20b | -16.6508 | -57.2739 | 2024-10-01 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| e266e8c9-43c3-3f43-9a6a-edaa18fa97b5 | -16.6505 | -57.2944 | 2024-10-01 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| f5178183-9fe2-3093-a04e-54fa114c3d02 | -16.7924 | -55.7748 | 2024-10-01 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 125a53d8-4121-35f8-a830-5c1fa5134246 | -16.7732 | -55.7565 | 2024-10-01 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 78d96ee7-782f-3a8c-aa05-2b96ebcf8586 | -16.7728 | -55.7773 | 2024-10-01 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 380a674f-cd33-3b4a-8079-8eb3fd336847 | -16.7724 | -55.798 | 2024-10-01 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.3 |
| b11c3d29-ab36-34de-a380-900bb1ecaa59 | -16.7532 | -55.7797 | 2024-10-01 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 3300299d-922c-3e36-837e-92d7ad8cd42a | -16.7528 | -55.8005 | 2024-10-01 04:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.9 |
| 8fa1ec87-f8fa-3ed6-a09b-89bdabb4857b | -16.6704 | -57.2717 | 2024-10-01 04:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 867dafd0-cfe2-3bb4-bffd-d3750fb1090b | -16.8983 | -57.6949 | 2024-10-01 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| c9d337e3-9c3d-3dc9-b2a6-2297096c5fd2 | -16.898 | -57.7153 | 2024-10-01 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 6f9b4813-ed2d-3520-ae3a-c5aa6b3580c2 | -16.8787 | -57.6971 | 2024-10-01 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 98e277e5-15f0-303f-8c1a-71a33f802bf8 | -18.7176 | -57.3097 | 2024-10-01 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 3bec0d63-93cf-37c0-99f0-b9d79a65cf4a | -18.7172 | -57.3305 | 2024-10-01 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| f363f0e8-5934-30ae-b1b3-f309bf88fdd7 | -18.6977 | -57.3123 | 2024-10-01 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 03d14446-1c46-355b-809e-7b528055bf6b | -18.6973 | -57.333 | 2024-10-01 04:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 9202f379-f92a-3a25-a392-76dd9ff86cf8 | -19.1329 | -57.4628 | 2024-10-01 04:06:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.7 |
| d62eff68-82a1-33b6-82a1-df48c962f165 | -20.0082 | -44.5336 | 2024-10-01 04:06:56 | GOES-16 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 6f041491-b279-379d-9dc9-fcdeaa034f4e | -21.5864 | -47.8827 | 2024-10-01 04:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e273d2fd-41aa-3eee-b2f2-883bb0327435 | -22.3922 | -49.2961 | 2024-10-01 04:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.4 |
| d7613a9a-89f0-3dd5-b79a-e3b5b800c13f | -22.3916 | -49.3194 | 2024-10-01 04:07:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.3 |
| fff22860-7d4e-30ae-bd2b-bf33340bb30c | -22.3713 | -49.3011 | 2024-10-01 04:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| 60983784-dd5e-3326-b8b2-613e0f5215fc | -22.3707 | -49.3244 | 2024-10-01 04:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 255.6 |
| e5c11f81-204a-33cc-8d6b-107eb5d9f80e | -22.37 | -49.3477 | 2024-10-01 04:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| eead31ea-c301-3ab4-835d-001e1a7873dc | -22.3498 | -49.3293 | 2024-10-01 04:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 89c4dad0-a89f-3af8-9bfc-576c7d7d5ea5 | -3.29658 | -50.66745 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b202dd3-c178-31c5-86ab-504a1165b6ec | -2.90738 | -50.71885 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 733ea615-fc0d-3454-8140-0592b412b921 | -2.90176 | -50.72102 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63f4bfe2-4206-3185-bceb-36d296e115ef | -2.89816 | -50.71112 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c3a6e37-fe8a-3f90-82e0-697c85b68558 | -2.89153 | -50.71936 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 93153724-371f-3bea-8e58-0ef1df48565d | -2.88895 | -50.70339 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c18214d4-0429-3b38-96c2-c8dee247a301 | -2.88845 | -50.70639 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d7b0d85-2ef6-3f34-8dd4-0285487b8513 | -2.88794 | -50.7094 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f4f2b354-c3df-3d10-b98f-2d30177328c4 | -2.88692 | -50.71546 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 55e4b48a-0ee7-3d07-9500-9452bbd6b299 | -2.88641 | -50.71851 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2d192234-184a-3139-95fc-8ad937178d77 | -2.8859 | -50.72153 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 83dc6100-2d6f-3ef8-ba62-38d2617113e0 | -2.88323 | -50.72114 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e11eb49c-5089-3cc2-b9f8-1bdfca4ec3ea | -2.88233 | -50.71156 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b8b6158-2280-36c9-a257-0461f78ca21b | -2.88182 | -50.71458 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 204df777-fa0a-3ecf-bf36-ffed34743e93 | -2.8813 | -50.71761 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| efacc4d8-b7a2-3b7d-b03e-8f6c8bfd14ec | -2.88079 | -50.72065 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0414faab-178a-390a-81a2-22af74285853 | -2.88007 | -50.70813 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b93ed5d-881c-3f4c-a056-352c37f61d38 | -2.87959 | -50.71115 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88411acc-36c8-3be1-a4dc-9ee7f07e77c8 | -2.8791 | -50.71416 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 27b7bbe5-f54a-3ea2-9235-3e1e1c2d62af | -2.8767 | -50.71373 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66e97915-04eb-386b-a84b-8d7214d576fb | -2.87568 | -50.7198 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90405e0d-94f3-3b48-b38a-4dc619b803b8 | -2.87496 | -50.70726 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f4d24af-54f3-39f5-8388-a29b0a7805d1 | -2.87398 | -50.71332 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d62d689f-631c-3965-a171-457d37391534 | -2.87301 | -50.7194 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69831b4a-ac25-39e8-87ce-4e6921898392 | -2.8721 | -50.70987 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c25f97b4-c7ce-37c3-99e0-ce4a2f1d6341 | -2.87034 | -50.70337 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2ec60d70-69bb-3b80-93c9-6189894291c1 | -2.87005 | -50.72198 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4897510b-571a-38de-9ba2-5e0b76bb9149 | -2.86985 | -50.7064 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5e5596-4d09-3af4-9401-c7b710f59710 | -2.86936 | -50.70943 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b9b046b-ea47-34d2-9c9c-84ef1c17fd3b | -2.86887 | -50.71246 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a19e4ef-05aa-3209-91e3-f2e0cd3e1d4f | -2.86789 | -50.71852 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37fccfc7-8501-3844-8710-fda99462ac4c | -2.8674 | -50.72156 | 2024-10-01 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README61.md)
