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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 412f214a-d067-33d0-9801-e06b60c1ad65 | -8.89498 | -47.27514 | 2025-07-12 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30cf1d61-e8da-3c22-8872-d64e48e9703b | -6.60987 | -43.89101 | 2025-07-12 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcc4851e-c585-3391-b429-ca7ca4f17733 | -8.69525 | -47.19024 | 2025-07-12 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8f6f6bf-a537-3957-9fe3-e0a27c3213cc | -6.86241 | -42.77414 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6454de4e-8179-3818-9be5-62af36c559bd | -6.87092 | -42.77454 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5540bf36-ad28-3f9b-a3a2-e1c0bb2928fa | -5.84422 | -48.39363 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 1f09cb85-d77f-3aba-abb3-1d1faf4dd9df | -9.27348 | -46.6132 | 2025-07-12 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fe3c7d6-681c-39cf-8612-9384d9e0667e | -8.22991 | -47.55513 | 2025-07-12 03:47:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d642d6-132e-34bf-97ec-bbe065d6c052 | -6.61069 | -43.88628 | 2025-07-12 03:47:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b6f3fecd-f47e-3ac9-a886-cd829cd61c50 | -8.89574 | -47.27408 | 2025-07-12 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e09cf5be-6464-3e44-b28a-0c373b08e18c | -6.71295 | -43.11068 | 2025-07-12 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dec1df98-c8cd-3d5b-b828-3bf8e6b31a0d | -7.68667 | -44.36866 | 2025-07-12 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31366eb8-fbd2-3cc8-b400-94ad02a6aa14 | -7.94843 | -49.65868 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0cfef5f2-f6bc-3f60-9d6a-513f765687ab | -9.27286 | -46.61655 | 2025-07-12 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2aca1bd-af7a-3253-a44b-39c34abfa1b2 | -8.46619 | -49.61523 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a4fc7f62-91e0-33ec-ac01-6b597f940606 | -6.85818 | -42.77348 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 70410d2c-8483-39d1-b6eb-248a9b9c2e86 | -8.53544 | -36.29308 | 2025-07-12 03:47:00 | NOAA-20 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6497d59b-83d5-35d5-b525-a2fe0b7a00bf | -8.75352 | -43.95586 | 2025-07-12 03:47:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f082e0-0e5f-3b8f-a156-1fd872178f8a | -8.89505 | -47.27788 | 2025-07-12 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 591bc91c-d103-39f7-a98e-12fee525bf7a | -9.08507 | -40.53949 | 2025-07-12 03:47:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ac59b3a5-325a-3567-934a-d5ef88bc6f58 | -7.68119 | -44.37281 | 2025-07-12 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d424b4f-f410-36e7-a56a-7840e5d22e03 | -6.84906 | -42.7761 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| efd5fa26-b217-3721-9cd6-ab61a61b6c2a | -7.07985 | -49.61232 | 2025-07-12 03:47:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a2bceb9-1891-36fb-aad6-81a23e9208b0 | -8.9155 | -47.34877 | 2025-07-12 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d29295-f946-387a-bf6c-da0d62929b0b | -7.4705 | -47.5192 | 2025-07-12 03:47:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36db813e-d11b-3750-85ce-2acbf058c81e | -4.52763 | -38.6787 | 2025-07-12 03:47:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| da4632de-0ce1-38ed-aa4c-5edb282eeb4d | -8.46529 | -49.61678 | 2025-07-12 03:47:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dab28172-2c1a-374e-997a-23a693ba7148 | -8.75275 | -43.96021 | 2025-07-12 03:47:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77cf33de-f2ef-3e6b-be6f-6ed86550c951 | -6.84972 | -42.77213 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f50ff807-32ff-3a87-b5d2-50f12fdc3b73 | -6.8667 | -42.77383 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f980e5ad-f4cd-37f9-b6e9-fa92bd1624f1 | -6.87084 | -42.77558 | 2025-07-12 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0d106a08-f0f5-3b91-ba47-fbc435a30f45 | -5.84512 | -48.38858 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c3234567-bffc-3372-9791-8b42fa9782fd | -8.07206 | -34.97696 | 2025-07-12 03:47:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8b761a76-9b23-35b5-a149-bb2c1358db0c | -6.71712 | -44.32644 | 2025-07-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6c539900-bf64-3012-89ef-3e2aebde2302 | -7.68472 | -44.37033 | 2025-07-12 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40f6db25-9403-3c6c-81e4-6c4be1b8cbad | -7.18782 | -42.97737 | 2025-07-12 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ccd95c51-568b-38db-bd34-0f4a51d6cfcb | -5.85043 | -48.39483 | 2025-07-12 03:47:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44fb0c71-fa5e-383d-856b-abee72f8bd13 | -10.57357 | -49.12606 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5ef144c6-baeb-33ba-92a0-b014c413b67e | -11.738 | -48.52763 | 2025-07-12 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 800bf085-e24c-3cce-bc45-8e8f3285f4da | -10.89585 | -49.20309 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 808d4eb2-0e53-3e79-bae3-d5f947215950 | -10.56886 | -49.12643 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0bb6d04a-b5d7-3bc0-b72f-8884945d41c2 | -11.46286 | -45.10884 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faec1628-aa47-3d46-9c2e-ff57ec568b6e | -13.0154 | -47.82657 | 2025-07-12 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50cf7127-bf65-3b96-8400-44d71b575231 | -10.89494 | -49.20763 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 08c281c5-2ba9-3ade-8404-8ba03a1495ad | -10.69993 | -48.31078 | 2025-07-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f70963ec-0ce5-38da-85be-24d99b28bd90 | -11.45248 | -45.11454 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee95d57d-a176-389e-8d36-e1cbfaa2848c | -12.41466 | -45.35261 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b254845-5333-3753-80ea-f281a763d42a | -13.35596 | -47.77726 | 2025-07-12 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f124988c-e695-3c98-a2c5-9fee5735660c | -10.62422 | -45.23243 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49759e06-5f3f-3748-b0ac-367b61565395 | -17.09485 | -43.80302 | 2025-07-12 03:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38f9091a-c502-3db1-b1bc-2c0bde53465c | -10.67203 | -49.49896 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6354153-3df8-3875-a48e-fa030fb34772 | -12.9932 | -46.26669 | 2025-07-12 03:49:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1953a83-5cfc-3cee-8862-5eb0208be161 | -13.91077 | -46.87093 | 2025-07-12 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e6ced56e-eccf-3e68-9d08-8c4dddc18473 | -14.77902 | -48.20573 | 2025-07-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10234d3a-dab5-3f94-a664-197121ed0a9e | -11.94221 | -49.29356 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 280b9136-327f-3082-87fc-346d941dec95 | -16.66282 | -50.63358 | 2025-07-12 03:49:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 787da4f5-37d9-350a-b06d-24d138bccc4c | -12.60536 | -48.36867 | 2025-07-12 03:49:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cec39d18-3d7a-3f71-af70-35876bbc1e8b | -14.7803 | -48.20578 | 2025-07-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85abe606-709e-31ee-9d2d-414e5121729e | -11.42079 | -46.37859 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9f7c86cd-0029-3e85-849c-726bed025b74 | -11.42653 | -46.40345 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ede50706-c82d-3eaf-9564-96958f3fa34f | -10.5749 | -49.12753 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 282f342d-2b7a-3ee2-a9c7-e9e53973c448 | -10.70072 | -48.30664 | 2025-07-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16ad0a0b-1f5b-30d4-b1b9-eb2d16180791 | -9.8517 | -47.87914 | 2025-07-12 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b44c1d44-a8d3-38fa-bbef-f75b4bd13e90 | -11.42386 | -46.3899 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ac81500-c5c1-3ad9-945f-e900d16e4a16 | -10.83751 | -49.11136 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d7f35e4e-09cd-38cf-b503-64a6d1398bf2 | -10.57072 | -49.11714 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 11e2b6ef-d2b8-3e1c-9690-aad2c4b3dee2 | -14.78449 | -48.20581 | 2025-07-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c49e1d-7cfa-31ee-99ba-0017d84e569d | -6.18587 | -42.14735 | 2025-07-12 03:49:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1de84eab-74d2-3e23-b638-e711cc4655b4 | -12.40922 | -45.35646 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9dc22ca-8c00-3c7c-8696-c0ed3be621fc | -10.62887 | -45.23338 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3834cbbc-9395-36f3-889f-88772fd62a2d | -9.85485 | -47.87654 | 2025-07-12 03:49:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 260837fa-ba25-3d44-a925-6b457c2f0354 | -11.42614 | -46.40554 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 071e549a-8ea1-3484-931c-89e9fd17c3c6 | -11.76797 | -43.86641 | 2025-07-12 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 388384e4-4211-3f55-9b8e-7acfc2f0602f | -13.13472 | -47.27459 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5110cc4c-e70b-34ea-a038-6bd4b7202e4a | -10.85548 | -49.11482 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4f3f59c2-cada-3c08-8698-0f4cbed386c8 | -13.12023 | -47.29438 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7403f6f0-18c0-39ea-bf58-672d52ad5727 | -5.23906 | -40.8738 | 2025-07-12 03:49:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 893f0dc6-6324-3072-a235-b15c12a03389 | -14.77821 | -48.2097 | 2025-07-12 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83f5041c-468d-3d9b-b691-7c658b4671f4 | -10.37062 | -47.56233 | 2025-07-12 03:49:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2f972d5-bb48-36f7-b21a-b95993f4dfd1 | -13.12072 | -47.29184 | 2025-07-12 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f207c126-cd3a-370f-af29-dc80cedbba89 | -10.69484 | -48.30644 | 2025-07-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0e50585-65c0-33ae-b44c-0f578e20e11f | -10.57395 | -49.13227 | 2025-07-12 03:49:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9eac757b-e1ae-36e9-b0b2-23bd4352bab0 | -12.41705 | -47.50545 | 2025-07-12 03:49:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b82ca8bd-9407-30ed-aaa1-34f761528f5a | -11.42078 | -46.37958 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8b5c5ee7-7cfc-3415-a5a4-1d909fc89258 | -13.28897 | -49.15836 | 2025-07-12 03:49:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faff92a8-2b9f-357b-92c7-e435e2fd7389 | -10.83844 | -49.10662 | 2025-07-12 03:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cff47f05-2507-3a08-8870-c4cb714286f2 | -12.41921 | -45.35355 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0efbd4d-fb9c-3c0e-b294-83a1f20ebebe | -11.42781 | -46.39647 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e502eba-03c8-3b02-8663-8f68120dd797 | -12.41211 | -47.50677 | 2025-07-12 03:49:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b5ec2764-bb50-334b-b971-aeee3a522fb5 | -11.27705 | -46.40203 | 2025-07-12 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e63cb5ff-e589-3cd3-9b18-fe18dedc7453 | -9.80016 | -48.56777 | 2025-07-12 03:49:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c72cf9d9-fa62-364d-a246-8af3365b1bfe | -12.03424 | -48.76204 | 2025-07-12 03:49:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 639a7083-71a6-3183-813b-aa9ff9fa09ce | -12.9979 | -44.86927 | 2025-07-12 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b5f2a2d-1f92-37d2-a185-4dc3612de62c | -12.4164 | -47.5088 | 2025-07-12 03:49:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4bb54f-22ac-33ae-b142-f3c165dfac6b | -15.45035 | -41.69145 | 2025-07-12 03:49:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a5465fdd-f027-3123-832d-e09199a3ec4b | -11.46329 | -45.10681 | 2025-07-12 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfc89c5e-cf7b-388e-be32-523e7eb84cda | -12.41736 | -47.50787 | 2025-07-12 03:49:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19d64829-9e50-3cc5-9ad2-1e1b21ae7f1b | -17.12007 | -47.95217 | 2025-07-12 03:49:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bca46794-7f71-3d92-a500-41f70df5c8f2 | -12.418 | -47.5045 | 2025-07-12 03:49:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 057f1a89-3293-3e41-a3c4-3cc7757d9e25 | -10.69408 | -48.31038 | 2025-07-12 03:49:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
