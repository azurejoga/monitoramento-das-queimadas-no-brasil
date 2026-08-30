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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cdefe95-9fd1-39d2-8bff-f67dca91b782 | -9.9468 | -60.5232 | 2026-08-30 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 4d7e1a89-afc0-3fbe-bcf5-93d0b0eedeaf | -10.4774 | -59.6207 | 2026-08-30 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 22a015b1-2765-3b36-9133-cde92be7c309 | -11.0057 | -49.6677 | 2026-08-30 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ae83a99d-47bc-3c85-be84-136374d04410 | -15.3651 | -53.8097 | 2026-08-30 16:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| a800c8ea-c241-32e9-b81c-9c7f7288c649 | -10.5593 | -50.4663 | 2026-08-30 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 939f059b-0d19-350a-ba64-4e9600a044b9 | -10.5406 | -50.4469 | 2026-08-30 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 2646836a-bac5-3666-afcc-dc5602a8e887 | -7.3479 | -55.1544 | 2026-08-30 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ea570d7b-5fcf-36c1-94e8-ff0be10d6b7a | -11.3619 | -45.1724 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 235.0 |
| 4b86f123-cae7-3f36-a0fa-c8d287efed0c | -11.1545 | -51.2112 | 2026-08-30 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| b5eca7bf-96cc-3c11-8267-c4781c1d3203 | -10.8253 | -45.3152 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 129ea666-92ad-393b-a716-9875e0125608 | -6.0541 | -57.9591 | 2026-08-30 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 1eb66a39-c02c-35ca-8533-fc69761fc505 | -6.9363 | -55.6958 | 2026-08-30 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d7bb0ea7-4626-3e7f-bfa7-1f9cf3f741c8 | -8.5925 | -66.9564 | 2026-08-30 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 289.1 |
| 16ba3225-011a-3e59-a939-9a5bcb304277 | -7.9907 | -46.5177 | 2026-08-30 16:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 7780e62c-51f6-3b76-bce8-14b6d98e76c9 | -10.8046 | -50.5046 | 2026-08-30 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 90a0a28c-a10a-3f0a-a24c-5e33f893edc9 | -8.231 | -61.4304 | 2026-08-30 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 154.0 |
| b9f28a82-861f-3d18-96ea-76250b957d4a | -5.8874 | -52.1271 | 2026-08-30 16:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ea026ccf-7f34-3e97-8753-0dc6bfc3d233 | -9.1711 | -49.9835 | 2026-08-30 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| df40b9ff-dc2c-31a0-a9b9-3d84225d36c5 | -7.9611 | -44.275 | 2026-08-30 16:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 64932fb0-10be-3eab-87dc-1af304702568 | -13.3425 | -51.4042 | 2026-08-30 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| af048af5-5720-3c3d-b1b1-98bcffcb100a | -6.9315 | -59.3184 | 2026-08-30 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 84903a5b-663a-3e55-aebb-4a140d15925f | -11.2298 | -45.0759 | 2026-08-30 16:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| a54cfcb8-91ba-3989-bcc5-b985e9548d9d | -9.9281 | -60.5242 | 2026-08-30 16:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a0ccde97-b6d6-38e6-9578-6bb72c594692 | -8.6158 | -54.7541 | 2026-08-30 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 85fbf749-29c5-3a2a-91a7-2d8ea25fb3c3 | -13.2643 | -51.4992 | 2026-08-30 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| cb0b0d05-0c4f-31e9-be49-69da6a898000 | -10.1348 | -45.7006 | 2026-08-30 16:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 91aeb1b2-ee67-3179-869c-a5293e38ffb5 | -6.1743 | -53.4834 | 2026-08-30 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 886b3916-9d12-3de5-aeb1-6b9db49e2d5e | -6.0541 | -57.9591 | 2026-08-30 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 85390c7a-fe98-30ae-a79c-ea3bfd5a612b | -7.9422 | -44.277 | 2026-08-30 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 281.8 |
| 479d0d56-42b9-3064-bfe8-8d212b9928e4 | -6.9363 | -55.6958 | 2026-08-30 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 677d62ed-1dff-3c80-aade-049d0190a03b | -7.5644 | -49.5857 | 2026-08-30 16:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 3ba1c32e-4f9b-3f66-970e-1200d7b0640e | -12.1895 | -50.5838 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| a507b4b2-47a1-3e25-959a-45ff281bdeaa | -12.2277 | -50.5792 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 76171a00-37f6-318a-a534-b76740f1dd65 | -11.0054 | -49.6893 | 2026-08-30 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 930bc21a-1168-3b0c-8ce7-70785bb6bcaf | -7.9419 | -44.3001 | 2026-08-30 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 2469933f-9c8b-38b0-ac19-fe66e7a0eebc | -10.5404 | -50.4683 | 2026-08-30 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 7d95f85b-90f5-3241-9024-8566024fa5d7 | -9.7027 | -60.7482 | 2026-08-30 16:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 095e45e1-49bd-311d-a1e8-09b83e682538 | -12.2086 | -50.5815 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d8bcbbfb-27b0-3dd1-b575-6099ab190210 | -5.982 | -57.6697 | 2026-08-30 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6f9f7759-fb36-3168-80dc-6bd565d2ae11 | -6.7883 | -55.6834 | 2026-08-30 16:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ded8c29c-27c5-374d-9749-6b00b8dfdbc4 | -10.9673 | -51.0614 | 2026-08-30 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| be13d303-d1f6-3cbc-8e19-d3cae4d220e0 | -7.5272 | -44.3413 | 2026-08-30 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 142.7 |
| c9b106b9-5832-333e-841b-b0daa98e837f | 0.1367 | -60.393 | 2026-08-30 16:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 9322c71d-e442-3d8d-9054-39b0b860545f | -11.6396 | -50.4553 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 77101ad1-30a6-32a6-89de-3cef6585dc6d | -10.9405 | -50.255 | 2026-08-30 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 098dc332-e4cf-3f00-8c5e-59f73c11ce1c | -9.2262 | -65.8784 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 654a522d-1b19-33c2-b476-ddf999ca6bb1 | -12.2281 | -50.5578 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 53b855b5-812f-3b00-b927-6c381e4ccd33 | -9.0723 | -60.4148 | 2026-08-30 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 86de6ef0-39a9-3ae8-b854-2052cddd4dc4 | -11.6247 | -50.1783 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 6d57b9b6-b632-3d6e-a3c2-7dbfa6f230b3 | -5.9636 | -57.6704 | 2026-08-30 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 2b4da4c2-e3ec-343e-acff-37e64bf406df | -10.9402 | -50.2764 | 2026-08-30 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 7b6baab1-10ac-301b-a446-321c7f03b640 | -11.3619 | -45.1724 | 2026-08-30 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 271.5 |
| 1f8ad9e3-23ab-3dfe-b42c-e150757bd531 | -9.1525 | -59.619 | 2026-08-30 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 0e772a35-ed85-35e5-94c0-f8daba434e3f | -4.1699 | -60.6874 | 2026-08-30 16:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 51deeb85-71b8-3abb-8292-011183c04747 | -7.3479 | -55.1544 | 2026-08-30 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2f5d8090-b7af-31aa-9890-bc686252cafe | -8.1534 | -45.4904 | 2026-08-30 16:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 219.5 |
| c072bfa1-fb16-3bef-a1f8-d09f69d7435f | -13.3425 | -51.4042 | 2026-08-30 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| ac5d8a5a-df84-31d2-82e1-3b11aaecc131 | -11.1634 | -50.5727 | 2026-08-30 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| dcc2d5bb-d1fc-30f1-b34b-4296cc6777cc | -7.9425 | -44.2538 | 2026-08-30 16:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 7d18cc94-6680-3d69-b8e0-a9c0923ecc03 | -13.4191 | -51.4159 | 2026-08-30 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8ae0a088-adbb-3312-b43d-0f397c1583a3 | -8.9873 | -65.4379 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 2e32398b-4b30-32cb-b57e-d68ca41157b0 | -9.9468 | -60.5232 | 2026-08-30 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| d1f4e6c0-fae5-36b6-af40-50f20f85ed55 | -7.9117 | -56.6353 | 2026-08-30 16:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 14fd20a1-b7a5-3267-8bb4-fc8cab39ac51 | -6.912 | -59.4927 | 2026-08-30 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 162f7ee7-33e6-3274-a82e-54b594d76e0d | -15.2478 | -53.8666 | 2026-08-30 16:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 364.1 |
| 20699a0d-55e5-3b7f-a885-ef2d6d2ab58a | -9.9282 | -60.5049 | 2026-08-30 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 5a0a9cb5-263f-3022-94a2-93b0d415072d | -6.0 | -45.0889 | 2026-08-30 16:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| f1786a41-19fd-380f-aad6-607f42c1912f | -13.4187 | -51.4372 | 2026-08-30 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.3 |
| ec3acfa2-2fdf-3213-b6f5-d4a8c07190e1 | -5.9635 | -57.6899 | 2026-08-30 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 6a29c711-942f-3c34-b565-43783566e760 | -1.8779 | -55.1287 | 2026-08-30 16:10:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 235a0ef6-71dd-3206-8461-9cdb8642d75f | -9.9284 | -60.4856 | 2026-08-30 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 88d9c20a-03dc-3b9f-825d-44036c024ee7 | -21.0176 | -57.8103 | 2026-08-30 16:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 45b64a67-8997-349c-b9a9-5820950e767a | -8.3679 | -57.6737 | 2026-08-30 16:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 4494d8a4-33f5-3cea-a698-d20aa10bcd00 | -12.2468 | -50.577 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4f859a1d-b3c1-3dab-bbf6-2b9dd4c0069b | -8.2227 | -54.9613 | 2026-08-30 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 79d257be-d78a-3ced-8b2c-593994e3c2dd | -11.1349 | -49.9117 | 2026-08-30 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 40f1b6ff-7f81-32e8-87bb-2377a696640c | -9.208 | -65.8044 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3f43b2b4-57f3-318d-b6ce-ed9b734dfc9d | -8.631 | -66.5473 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 06530845-e060-30e6-87ea-38516daf537e | -8.9966 | -60.6109 | 2026-08-30 16:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| dd90c625-fafb-3575-bc88-0cd9e5b5d7ef | -3.6399 | -60.5466 | 2026-08-30 16:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 92e44229-5978-3109-93f9-4c47f6f764c2 | -8.574 | -66.9569 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 0e9d6771-909c-3990-b307-9796c2b9f896 | -7.9907 | -46.5177 | 2026-08-30 16:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| e23628d1-a6f3-38f4-aa47-2e2862bf2d7e | -7.1312 | -42.7708 | 2026-08-30 16:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 177.6 |
| 3cc14fbd-c159-3dde-8e3c-ebb69e9ab207 | -7.3294 | -55.1555 | 2026-08-30 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| aa01d878-3193-3337-8036-5213b88f84e3 | -7.9611 | -44.275 | 2026-08-30 16:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.3 |
| dc16eb73-7d6e-364a-8d6d-802c3ee71eb0 | -8.5739 | -66.9754 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 152ff14f-a843-32c3-b643-99138542095f | -9.908 | -67.0131 | 2026-08-30 16:10:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 9053de9f-e859-3b4a-ba4a-3387c14e5232 | -10.3226 | -58.0847 | 2026-08-30 16:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 0f36fc34-be23-36f0-86c2-4d2b8afd3d1e | -8.9142 | -70.6917 | 2026-08-30 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 52.9 |
| df854289-4c14-3422-a8b6-352e7533b757 | -11.3431 | -45.1521 | 2026-08-30 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e950ad2a-504e-3776-9cd3-3c39778558e5 | -11.0244 | -49.6872 | 2026-08-30 16:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 54b0fb3a-5036-3b08-962a-23cabba4e3ed | -4.1698 | -60.7064 | 2026-08-30 16:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9a64f254-26d9-3d96-a03a-61e5b5144a10 | -11.6586 | -50.4532 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 85ad8de0-b6f1-3892-82c1-d56f922e3a85 | -3.4943 | -54.6567 | 2026-08-30 16:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 37309e69-cd0f-3f45-97a3-f1d03284e4ca | -10.8249 | -45.3382 | 2026-08-30 16:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 298.3 |
| c68f501c-d7fd-3007-889d-c2dc925aaff9 | -10.9935 | -50.5271 | 2026-08-30 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2d85f255-cfd2-3fbd-ab3d-ec31db12f4da | -11.1913 | -51.292 | 2026-08-30 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 36deea78-4d68-3a39-b080-c8c8d7120cdd | -11.6243 | -50.1998 | 2026-08-30 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 2ba281fc-bf2b-3f07-a54d-bd4da0d28ae5 | -8.5925 | -66.9379 | 2026-08-30 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 738206a9-d03f-3245-a676-aa325c714dcf | -7.2932 | -60.6096 | 2026-08-30 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |


[Clique aqui para ver as próximas entradas](README97.md)
