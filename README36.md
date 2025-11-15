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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 527ac87d-7528-3fa8-827b-eab600f58c88 | -7.88345 | -45.69476 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f88e19fc-0049-3c6a-b980-946d4935cd52 | -3.91142 | -50.04078 | 2025-11-15 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c3a08d5-6eb4-3acc-b3fb-47a1e517da71 | -9.93655 | -44.93338 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 434b9d80-5f36-3185-acc9-b33bc7f9bed9 | -4.18761 | -43.80575 | 2025-11-15 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c596241-5572-379f-9070-5a80931c8af0 | -7.88885 | -48.39325 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad14b2b8-deeb-3300-8ddf-198e6b1a6675 | -6.73675 | -42.96424 | 2025-11-15 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ddde30ad-8a14-3770-99ad-c2914695e6a8 | -4.41496 | -50.81992 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 654e1f10-0f0c-3313-9007-c868cac358f9 | -3.31934 | -42.39859 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6f627a7-3eac-32eb-9dc7-09b0d1fa7c74 | -7.73553 | -44.57932 | 2025-11-15 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42d71178-4e9d-3b92-bdce-35ffdcfaf60b | -2.45195 | -48.82376 | 2025-11-15 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7d2cdb0-8da5-3e2d-b3eb-76b85961805b | -5.72475 | -42.36625 | 2025-11-15 04:25:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b909d4a0-57b6-395f-a3f6-497a6f61fcc2 | -5.12703 | -46.8233 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1649a922-84af-3d74-bfd8-bd916181e4fd | -6.06307 | -43.6818 | 2025-11-15 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c1490359-a2cc-308b-aacb-1497d1742470 | -7.425 | -45.23482 | 2025-11-15 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5589a52-4700-3284-8a45-bad19e4143da | -4.07908 | -47.2343 | 2025-11-15 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6207cb70-9b8a-34b0-8298-33d3b5934829 | -2.95068 | -41.97483 | 2025-11-15 04:25:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4250ad62-81cf-353b-8480-237da688d425 | -5.75977 | -42.72739 | 2025-11-15 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 66d2f422-f7d2-3780-b142-aa19c8632232 | -8.75669 | -45.6895 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d54052d1-8bfd-3a6b-ba5b-ae87fb32c035 | -7.76151 | -45.16592 | 2025-11-15 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebd3534e-558d-345f-8847-704658b65509 | -2.06527 | -47.43329 | 2025-11-15 04:25:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 115b4705-b1be-3484-9c22-f6aa38860fce | -9.81231 | -44.23038 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 707642cf-eaad-3317-aab9-d953e96b4791 | -5.05024 | -44.68018 | 2025-11-15 04:25:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8849ba4-cd0a-30f2-8cb2-8728bf01bd7c | -5.65934 | -41.08761 | 2025-11-15 04:25:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2dafbfb2-741f-36b9-9657-6f9bfd28497f | -7.11998 | -44.34533 | 2025-11-15 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 582cdf93-d087-3654-a224-2ea697e666e9 | -6.32783 | -47.2626 | 2025-11-15 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a886e03f-049e-366c-bdfc-c458721caca4 | -5.52905 | -41.77212 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6316f977-13c6-36be-85e2-e064a58c18b6 | -5.4269 | -40.6637 | 2025-11-15 04:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4b60251-9756-3901-a6c9-250209dfdebb | -6.13419 | -47.00827 | 2025-11-15 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02164f8d-0d05-36d3-a405-e6a95a2de6b1 | -4.32993 | -47.57483 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acb4bc84-4823-3145-89dd-ce57c52330f0 | -3.28256 | -53.82584 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 330cedf0-648c-3588-a6e7-dea44355cb82 | -3.28242 | -45.46674 | 2025-11-15 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94ec655f-e4c2-315b-874a-05b5b5bec7b0 | -4.72683 | -47.15683 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aec4a217-3997-3de6-9437-ae24314175f0 | -5.58493 | -47.10411 | 2025-11-15 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d77b839-46f4-3c50-acb8-60f997501157 | -9.85958 | -44.17829 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb316333-0ccf-3b2b-97da-b0d81ce820f6 | -4.54516 | -43.22251 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 04a41b19-ea33-3398-9b56-1a82a5118730 | -6.2813 | -44.74797 | 2025-11-15 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6af07fc-2e89-31f6-9dd0-541e2912a962 | -6.45619 | -45.65811 | 2025-11-15 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b150ea6-6953-3031-acb0-d4b7ece656d6 | -7.76206 | -45.16235 | 2025-11-15 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54a804aa-80ba-3376-906e-230e74bc4ea7 | -9.86018 | -44.1742 | 2025-11-15 04:25:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d218fc4-1774-39df-a5ce-1a4f51eaa6e8 | -4.60761 | -41.74651 | 2025-11-15 04:25:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 322369ec-f4be-307e-8398-e299b92b2394 | -7.55293 | -47.25356 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 451466fc-8d06-3e45-b808-51f4690f7b55 | -5.61987 | -42.81209 | 2025-11-15 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 36e21fad-3fb7-329a-9e97-2f027f19b098 | -7.70687 | -49.3883 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5851a062-544b-3005-845c-23f0a2d52b6c | -3.28559 | -49.48231 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e481b0b-3432-30f2-a14e-557654bafcc9 | -6.28635 | -44.73762 | 2025-11-15 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7967bac8-2e8f-3450-ae99-7f29ffcaf86f | -7.45519 | -42.56348 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 76f537ae-3b50-3961-a088-3a4506c19416 | -1.83016 | -53.79145 | 2025-11-15 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909f1680-e622-37d9-9548-a61b016c39f8 | -4.59076 | -44.31987 | 2025-11-15 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7e64bcc9-aa9d-3b7b-82f2-6625e23a23ed | -8.51528 | -45.62974 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daebf88d-a003-3df7-8dd0-3ed5cffb1a9a | -4.55143 | -44.59238 | 2025-11-15 04:25:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 737d3176-80d1-3f5c-872d-0359941cd021 | -4.91799 | -44.78665 | 2025-11-15 04:25:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 095c2fa8-b75c-37a7-b587-57c6f746ba28 | -8.06564 | -47.17104 | 2025-11-15 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01f3083f-9577-3b92-89e3-0279956b0845 | -10.42547 | -40.54834 | 2025-11-15 04:25:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b966dbe8-b14a-3672-86d8-7254b9df18da | -2.95906 | -51.51259 | 2025-11-15 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fecec3d-e226-339d-b844-c9d8bc27fc74 | -8.32966 | -45.40413 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5d0ac9c-8994-30af-b3c0-c77a1de2c4e9 | -9.44891 | -44.86868 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85a27a9a-742a-32a1-a42c-9dce432207f1 | -7.28586 | -48.32366 | 2025-11-15 04:25:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51b6e305-bccb-3010-b744-261e7e8fc03b | -9.96631 | -44.94155 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78e88bf2-0724-3f1a-bd4c-bd5cb1934abd | -7.10373 | -42.73909 | 2025-11-15 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d98e7ae0-2124-367c-aa0f-1088bfeebf4f | -4.19139 | -45.45499 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3d26ac6-137c-351a-9cbc-fffafe127640 | -3.99214 | -44.27644 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6b8b5c7-fafd-361b-b1c0-6cdf78c746a1 | -4.24172 | -48.38626 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6981f922-ccae-36af-871b-c249798b5664 | -8.58192 | -48.74729 | 2025-11-15 04:25:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ceb6d03-3ad2-3e8c-a719-415a04944f5a | -8.89824 | -47.89632 | 2025-11-15 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68323758-db67-3add-83dd-efde0353af74 | -5.90217 | -46.39227 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40889c1d-bc97-3eaa-aa34-d73a945e8335 | -5.84243 | -46.66272 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b32f9c5-34bf-35e6-b700-4cb5e8998bb0 | -8.99833 | -44.18822 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb95503d-09ec-37ef-bd49-8ee2321d595a | -5.62635 | -43.92811 | 2025-11-15 04:25:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 170a163d-9d3c-3ed4-a8ac-d2a1817968b4 | -3.14625 | -52.26659 | 2025-11-15 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 278c0677-d364-38a0-8701-2801c778b15a | -8.74779 | -47.70832 | 2025-11-15 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1b42f68-074c-375a-83b5-431a2ecd1ba7 | -7.44074 | -42.77238 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| af1d24ff-53c7-3644-9dd8-a4a2c0b088cb | -7.44205 | -42.76338 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fdbe3482-835a-34c3-b9c3-c5b528418d5d | -4.52032 | -44.26089 | 2025-11-15 04:25:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 455bc034-1e21-35ad-ba1f-daf994de70ff | -9.52587 | -42.93941 | 2025-11-15 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2b5d8400-d9c3-39e2-89f5-55dab92765da | -9.86514 | -44.71485 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb016c33-6171-335a-aab2-1df01b99a983 | -4.53935 | -43.21359 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d17dc2e-fad3-37a4-832a-a6cd15c6aa58 | -7.08143 | -41.58416 | 2025-11-15 04:25:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3e9f2ef1-71bd-372d-9a62-df23bfab4e2c | -4.35024 | -46.49359 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c987cda2-80f8-3b93-8b76-c72e04e5b272 | -4.65033 | -46.72243 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ede9333-3ee9-3ce7-bd01-7ae5a1c8ff95 | -4.19104 | -43.80627 | 2025-11-15 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6129c621-5760-3965-93c9-c89372f0d4d7 | -2.9413 | -49.35952 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 344b0c6b-cd6e-3fc5-8564-d3f85964bfb7 | -9.80406 | -42.21116 | 2025-11-15 04:25:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 16bbea2c-876c-3c7d-92ba-73ccdd6f1419 | -4.41439 | -50.82341 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adb5f7e3-774e-358c-aa0e-a11c41aacfc3 | -4.64488 | -47.94978 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a69ff60d-57b4-3ce1-89aa-813069db0da0 | -8.96276 | -49.16261 | 2025-11-15 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 283140c6-2add-39f1-8d28-7795ddafd104 | -4.2685 | -50.53461 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e799e19-9590-397c-a658-beb9e71b6539 | -4.902 | -44.05732 | 2025-11-15 04:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2ac9410-bbae-3b3b-bb29-735fa3305ec8 | -5.69432 | -45.96697 | 2025-11-15 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54a8a93f-fbf0-34c7-a631-581d6ce4d424 | -9.82375 | -45.12068 | 2025-11-15 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d57b1f8e-e324-3bdf-8c39-5117f8cd3039 | -3.53389 | -53.00347 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40b86ae9-aec5-3282-afb9-560aa9fc026c | -6.25814 | -47.0821 | 2025-11-15 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ec1b713-8ab8-3149-90df-85b79c6e1216 | -4.29964 | -45.99697 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c6b994b9-2dee-3303-b1c3-e61218a9da21 | -2.02284 | -47.3275 | 2025-11-15 04:25:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a9d68ab-5737-3713-8b28-2b7bc30d0f3d | -3.28183 | -49.48169 | 2025-11-15 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a35743fa-6a4f-3793-8de6-6cafcf5298da | -3.98827 | -47.99916 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de197cb4-73a1-3145-bdb1-0c8b7b29a177 | -3.52742 | -56.32118 | 2025-11-15 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24a13ead-0018-31d4-951a-ca61f65d0812 | -6.03249 | -43.78828 | 2025-11-15 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ddc9ea6-1770-304c-ac7a-033ce36ea3a3 | -4.02504 | -42.47673 | 2025-11-15 04:25:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c32ace65-0d3b-3fbf-a6b5-0e6bc0b8415a | -10.05137 | -45.34979 | 2025-11-15 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 285aa8d0-a2fe-301a-b347-47fd8ea49cf8 | -4.47163 | -46.43451 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
