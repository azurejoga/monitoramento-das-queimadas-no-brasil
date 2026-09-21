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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1ffba04-415c-3df9-94de-3c50ac2d1aaf | -9.03448 | -61.66156 | 2026-09-21 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de659994-9294-37fe-ba29-88ac781fcd0c | -6.79862 | -58.94706 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c24e3f0-63a9-3fdb-ab5c-db49bc6de87d | -11.0855 | -54.03166 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 433b63b5-550a-3b44-96e3-853861bf4dea | -11.37654 | -51.4458 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf19b7ea-f5e9-3b3b-b066-852f3d192c8f | -13.72267 | -48.78957 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7946eac-a130-32be-be28-ca7fd325a05a | -7.58601 | -63.0459 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd97e4f0-6ae0-3da5-b813-a4125f00cf05 | -10.40374 | -50.23704 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 5062ccba-c0fb-36d5-af54-64cc164e81a1 | -8.65088 | -54.79826 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8eb70b4-3bee-3483-b946-8f69602c67f2 | -11.04836 | -54.91643 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c14262ca-161a-3019-9d30-956f93ae9af7 | -10.42226 | -50.23508 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9178c6ab-7f10-3d0a-8b2e-e3ae1c08e6dd | -8.0479 | -61.33128 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99ecefc3-bf05-3d70-b5ba-e70655b4d92e | -8.95799 | -64.40487 | 2026-09-21 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edf580ca-b2d3-3273-b008-4d859cf67c71 | -9.36403 | -60.31369 | 2026-09-21 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7dabba4-d337-3313-838d-1bcfaa2930d7 | -11.33304 | -51.3495 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ff72daa-b05f-31d9-b625-abe40b86de06 | -12.86458 | -50.95498 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b514d0a-2dc9-3570-bd91-358e8cc4f9ac | -11.35611 | -51.34296 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29115094-fc5c-33fb-ac4c-21e3bc28ff13 | -12.31151 | -50.6892 | 2026-09-21 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2677900-3e43-3e9c-a5b1-55ee70521895 | -10.62118 | -67.92622 | 2026-09-21 05:06:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c2727d8-b22a-357b-b6d9-5c65dbb9097c | -9.55106 | -66.00846 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3b65f45-2f10-3209-970a-341b95060833 | -10.94665 | -54.3677 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102d7c98-0fe6-3d53-b0b2-10871733ada9 | -10.42876 | -50.24223 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d7400459-fb27-3c95-ad9a-e19d21139865 | -11.04435 | -54.91974 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c074627-4b7b-3c11-8676-aa7f578aacae | -11.03268 | -54.15024 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed5a508a-7fc8-3aef-9c20-65a34b8ff96d | -10.47434 | -50.27626 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 23635d5d-f301-3502-9428-165088f794a4 | -9.45505 | -45.40595 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 9701a380-b6be-3567-8e03-e2735b6963bd | -12.82049 | -54.04748 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4be09a3a-a46e-3182-8296-c9648f48da3c | -9.97887 | -50.25783 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 39bf7eab-3bf0-3c82-a9c3-4fca8cae48b7 | -6.75374 | -59.1114 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d30f484-e768-3c42-8857-822477d5189c | -10.88841 | -53.9707 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72e8feb2-8721-3551-ad3a-4a83fc8035f2 | -13.17596 | -43.56227 | 2026-09-21 05:06:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| f208d7fb-606f-3ca0-9c7e-59d67ac5a05d | -10.38321 | -50.22034 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 94383c59-0737-3378-9fd5-021847c05b5c | -10.80701 | -50.83931 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0869b87b-1ced-3043-887a-51b64e96e901 | -13.27472 | -51.76516 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68512791-ccc6-327c-b5c3-b289235bdaa7 | -6.74116 | -59.41848 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d42474da-b892-33ba-ba1a-68687691877c | -9.66084 | -54.32797 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b481367-26d7-35dc-b83a-aebb8047dd09 | -11.72384 | -54.56504 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2cb84313-dcd3-3591-8dc1-53f7c072c801 | -11.5468 | -51.42642 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5afc592-e713-3af6-b1d5-844811c08dce | -9.56415 | -66.05676 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0366ebc-41d6-3a9f-b9d5-7c1ee767d591 | -8.08784 | -55.3449 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36bc2ebd-5e8c-3e5f-ae3d-b31819704e3c | -9.55068 | -66.04008 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e74f0b8-4d86-3582-bcd5-c6340caecdce | -10.88166 | -56.23317 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63d0c232-3c00-3bab-be32-0263f82b7794 | -10.88125 | -53.96963 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7221c2c-af6e-32d1-84f0-4c13b8ac631f | -7.25533 | -55.58438 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3aa2372a-4635-325b-9d55-535fedf57ce1 | -9.75526 | -46.24081 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b28e654-5c38-32c6-955c-f1efd176c059 | -7.89058 | -62.54451 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 977d0d1d-0f99-38a4-aaea-7bdcdf998cb2 | -10.42817 | -50.24674 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2bec21c4-6d96-3872-85ca-1d499c8bef3a | -12.82413 | -54.04802 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7a195fa-0b2b-3bf2-bf9b-631e461c956c | -10.42488 | -50.23707 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1a1a9d48-00f1-34fe-841b-ae2ed9325cdf | -6.69683 | -60.00786 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ceb7216-1477-3c25-b617-433a4b66401d | -13.94317 | -47.8395 | 2026-09-21 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c4e2f2c-956a-3a43-8180-69c568ea44c7 | -13.62088 | -46.91523 | 2026-09-21 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 463ebc84-f157-3721-b98c-bd5af8898531 | -6.45723 | -59.97684 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10702338-d727-3d51-b54f-4df1109f922f | -8.60737 | -54.78782 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07068ec2-95bb-3242-ae5a-73ca76e94dfa | -13.26528 | -51.80437 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e581b0b1-4f78-3bff-81b2-ca4d83a17ed0 | -6.74474 | -59.07634 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c6341cca-da2a-3b7c-b3b7-1bd91c4780a9 | -6.74047 | -59.42275 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4dbcc236-05fe-3187-b485-fbf13d7d93cb | -11.03185 | -48.31946 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65785010-077c-3484-bd9a-f19523846338 | -10.67629 | -50.73517 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 909c17da-790f-38cb-9972-8ff767debcc8 | -7.33248 | -55.2173 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f980732-c1e7-34ea-be9a-4874cd9cbaff | -8.7974 | -60.7953 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09d3ae92-2b86-339e-8d29-56c37d0cd70f | -9.54398 | -45.3947 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a030251a-231c-3b7b-831b-01609f6f1757 | -7.24762 | -55.59031 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52e4cc61-0a83-3496-90c9-327d005414bc | -11.02678 | -54.14103 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8563db0c-3f15-3aa0-a473-7da2d0890d84 | -11.749 | -54.5648 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ae4acaa-d385-3347-8b5e-95f89183ee28 | -8.85336 | -62.35989 | 2026-09-21 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15c40ffb-777f-34c9-8a13-43384072c867 | -7.24438 | -55.61119 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 22e895f5-7f6d-3413-b6e5-f22aa55d9dd5 | -12.83444 | -54.05397 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec42f87-635a-35e4-9586-1f41ed0c0c0e | -10.74488 | -50.79451 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0eef4082-62ea-373a-9aa6-7e168355873f | -9.56949 | -66.05778 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b8a0fa-fda4-393c-8655-ad9c41af900a | -8.24254 | -62.83748 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47d2acc9-319b-3297-80fa-e446a8c05e5f | -10.46257 | -51.3365 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 48606b7b-0880-3343-a0f1-bca10b6920da | -10.76103 | -50.80534 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdf0c380-87ca-31c7-a0ba-25e1c8f55ea5 | -10.40436 | -50.23254 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b70da162-13b3-3713-af50-0c4006b28114 | -8.78369 | -48.74998 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6fc672b-2a37-3519-816f-4228baa28217 | -10.82771 | -50.15183 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae636f8a-3ca8-37bd-afac-1a5df602d107 | -7.77196 | -61.50723 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c12cec3-2d7f-3918-84a4-fd42e6b7e9ca | -11.12542 | -54.00824 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a30e290d-536e-358b-b3ec-cbb1d172c528 | -7.59439 | -57.66838 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb6e7fff-7319-3879-ae99-6136d33f5eb5 | -9.03569 | -61.65448 | 2026-09-21 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a2f896a-32ab-3bc1-b00d-08d8417fd49e | -9.18959 | -51.52418 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28202daa-8a12-3910-8866-4caf5ad0dd79 | -10.36978 | -50.21843 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35fa141d-a4c1-38cf-9dcb-279087964f60 | -9.4572 | -45.39336 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8678a676-27af-3a85-9393-fafb932b6efb | -10.55531 | -51.29399 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1efc5a39-0fea-3012-87e0-9e00da24ff32 | -7.58418 | -57.68893 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c101a8c-5a1c-326e-b674-491e7c641685 | -9.5667 | -66.04304 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45f174e5-f110-3e18-b13e-223f19a33251 | -7.25516 | -55.60983 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed86fb33-fd8f-327e-90ca-44c27f6cf00c | -10.22018 | -53.92129 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bb3deb7-a537-3d64-ba0a-6bd1b3716bf4 | -9.76547 | -46.05787 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91bc48ae-8f34-375e-b8f0-7b826dbfeec5 | -8.78627 | -68.84805 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5b4d91a-1141-32de-aaf3-89dacb68a4d6 | -12.89839 | -50.9703 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b66913-1996-3902-8091-f34865063016 | -6.7832 | -58.90725 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d48f24ac-ab00-3bce-9782-3fde731293ea | -9.93172 | -58.31504 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca09cf05-9870-32d9-a5eb-666f0a511824 | -9.68344 | -54.34328 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 146984ae-bd16-317c-a803-73bb64469877 | -9.27345 | -46.21543 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0109d19-91f5-324d-8a24-03abb44f2606 | -6.92839 | -62.91314 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55fc12eb-0888-3144-9105-c0cd82358b87 | -10.99895 | -48.23367 | 2026-09-21 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1593da92-b71b-3932-b40e-b44795b2e858 | -8.78722 | -48.75129 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 90d536eb-979f-3c55-8a66-464f70fe3517 | -11.98869 | -58.07212 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cdf9ab67-97fe-338f-b22b-5d3dda5c26bd | -7.25208 | -55.60525 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 881b7be9-d91d-33f2-a58d-cd71d4d6cd68 | -8.24246 | -62.83915 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README82.md)
