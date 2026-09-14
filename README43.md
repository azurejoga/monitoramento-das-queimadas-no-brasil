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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 315cbbe5-d5cc-3e95-a6cc-12eb064e40ca | -6.37345 | -58.30125 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a0f01b6b-e302-3cce-ae30-6cb1e157fc31 | -6.323 | -59.98641 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0214ff3-59f0-314b-8016-c9352601ef79 | -6.58362 | -58.84055 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee180f44-72f6-302e-9232-6711c2ae7e53 | -6.13547 | -59.886 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77433975-4fad-3d08-aac1-6ce6e5964cb0 | -6.24752 | -44.79809 | 2026-09-14 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5acebe0a-e1e1-36b9-8222-d61b97fd75ad | -4.34499 | -54.78485 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb8275b6-1ec6-376f-8d2a-ed3b31b63469 | -3.72699 | -61.75591 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d1b298d-a998-3905-842e-802a8c467431 | -8.38839 | -46.2984 | 2026-09-14 04:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d12f3d25-e66a-332e-8856-6f779b29ae04 | -5.08617 | -56.25699 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cedca353-6efc-3732-9222-32c31d09d412 | -9.44924 | -50.12746 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 31af359f-68f5-318c-bb5c-64d48afeffc7 | -10.47303 | -51.32648 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4c339f5-6907-3bf0-ace7-49322f0895bf | -10.67339 | -54.16501 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ac5835f4-5ecd-3e94-998f-3a1c82d00970 | -6.59349 | -58.8693 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a8d0786-40cb-3fae-bd04-4b6dd45cfbf1 | -11.18772 | -42.81437 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 84cf87c4-cd8c-32a8-90eb-6c87a1a5d523 | -9.36589 | -50.145 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0846007-0a32-39bd-b2a8-909aca42d53d | -7.08809 | -43.55156 | 2026-09-14 04:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9856d434-edbd-3e6c-97aa-7d6ab785c83b | -8.60778 | -55.23352 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 550f7811-d7b5-3291-8799-036eb4f79339 | -9.71989 | -54.35514 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27027a98-b5cc-3888-8977-aa04e5c9b585 | -4.59401 | -50.9865 | 2026-09-14 04:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63cd4805-90c2-3647-9f2e-74a04ccc94c7 | -3.71557 | -58.8675 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10d4dd94-fa70-3a3b-a009-fcff9da82a77 | -10.17745 | -48.06857 | 2026-09-14 04:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2ad4655b-987e-3c2c-b60b-2628e8f7fe9b | -6.08836 | -57.90471 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99e2ab7a-878a-3b60-9c90-0e61db6126bf | -6.85238 | -55.56953 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fbcf739-ba99-3dcf-a5fd-d500b2b4835a | -11.22784 | -46.42806 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bee9acb2-a319-36cd-ae3f-7089c753ed05 | -6.29583 | -59.9591 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64b77428-3c21-360f-9079-b8ca5eae124b | -6.3044 | -55.27552 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b4b50e0-7649-3a1b-a6fb-4fed11f41008 | -5.89308 | -45.57346 | 2026-09-14 04:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ced192f-c9ac-3bf8-bb01-da7dad638448 | -9.36644 | -50.11853 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4cd597d-44c9-3ad0-b119-d5e6308396e3 | -7.11059 | -41.79617 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4eabbd98-80ee-3e3e-9985-2dcdaec51a29 | -10.68334 | -54.14739 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 77678a34-3ba8-3bfa-92f5-aeabe08bce28 | -9.4187 | -50.14182 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d78712a-3fd1-3d23-8714-241b7e818bf6 | -6.01631 | -59.94942 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b8b796b-8c8d-3d53-b9a0-d6d3fd7c71eb | -8.12036 | -54.80396 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9dbaaf8-b544-3b23-bd4b-e0cc4ab67138 | -10.20052 | -54.24275 | 2026-09-14 04:53:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d1efe2f0-778d-3a2b-9dd4-1d6a1ccc46dc | -5.84374 | -52.05724 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f99d213b-a2ff-34b2-9792-7fa3950273ed | -3.52631 | -59.06942 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d151234f-52d2-36ca-b314-80d2e733d876 | -6.10889 | -57.67382 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 38f73446-ff34-3357-97e4-e38eaae5830a | -12.52378 | -47.18552 | 2026-09-14 04:53:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49c06f1a-a289-3d3f-a66c-e9fab8d1b108 | -6.67506 | -58.87991 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f9c255d-b41a-3a34-af70-760be1d6370c | -11.51203 | -50.25068 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ca9f759-ab03-3d95-8d41-b671b524d9c9 | -9.68213 | -54.84519 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7890d382-b709-3aa1-800f-b02e65e929da | -6.28723 | -59.94757 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6610e6b3-23a0-3acd-8c80-9c7176396e9f | -10.65941 | -54.14329 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2d962f0f-8322-304c-9162-8343240d3b21 | -7.08202 | -41.80015 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 91d67c70-090b-3624-ad8b-14cd626fb72d | -10.69331 | -54.17223 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70603549-fd99-3c6c-8f6a-c98b3cc94bbe | -9.37555 | -50.173 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 247f3725-770b-32a1-8735-6fd07469ab3d | -5.1232 | -55.96058 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed4c7bc9-43ac-3a06-8f45-31595c05447b | -8.54445 | -54.71281 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1e7240a-0d71-3eab-8296-6c0a6150c0d5 | -9.13967 | -51.58197 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a18e702-4666-3fec-bdfd-f549a1d64d4c | -9.40847 | -50.16297 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 699bf7f7-8b72-3029-a285-6dac1bf00614 | -9.39936 | -50.1994 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 43197967-c5bf-3501-b3ef-9d8d15c423b3 | -10.96482 | -48.36353 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d81928e-5587-3830-9d9e-69b1199a8710 | -6.30969 | -55.29079 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 651af21c-0c58-38f7-904f-5d9432fdd29e | -4.13521 | -54.0149 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e421782b-d1c4-306f-850a-748a43e851b9 | -10.7464 | -46.26923 | 2026-09-14 04:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e881e56-a4d6-3cbd-9c48-9f5c2b49aa5f | -9.72079 | -50.84015 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d116fa0-2279-315d-b541-e616e59e0de4 | -16.22966 | -52.65041 | 2026-09-14 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8ff4bec-46d5-301e-8955-0a73fbfcee09 | -11.36975 | -43.96113 | 2026-09-14 04:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 601ba2b0-8ed5-3fc7-854c-04c0e6467e94 | -11.51433 | -50.25888 | 2026-09-14 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e0d6c05-5ac2-3829-9f8e-89b80629bd92 | -10.10514 | -48.85521 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa38e040-e97c-38ea-93d9-7d5d3bc89e5a | -6.60843 | -45.78831 | 2026-09-14 04:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d42230e-4736-310e-ae45-c0ef0fc08890 | -9.14298 | -51.5825 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8049306-5ffc-3b80-8d52-96be7b0585b4 | -6.31375 | -59.97831 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15fb94f3-ba6f-3424-8771-b1c5c6b9ab2c | -10.5968 | -59.41608 | 2026-09-14 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fafa504a-3ae9-332b-8ee9-2488aec87818 | -10.25278 | -57.6936 | 2026-09-14 04:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 117c9f3c-0de0-33d4-acd7-cdeb32a81058 | -16.23355 | -52.64733 | 2026-09-14 04:53:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5e0ba23-1833-3643-a05e-3a98a2bf055c | -8.53797 | -54.70755 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4bd6dcf-f366-390d-a4a3-454720ba029a | -10.51801 | -51.32262 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b66e08af-41ae-3fdc-b724-056c6aa3fd27 | -8.77388 | -48.7571 | 2026-09-14 04:53:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aff588f2-f832-33b1-9d7a-0c42501cef6e | -7.07646 | -41.79979 | 2026-09-14 04:53:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bb4b1acb-c9f5-33a9-a076-fd23538c51a5 | -10.68522 | -54.17861 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 222cf171-d136-326c-89ee-bead3e00ad7a | -10.68676 | -54.14796 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76cf4931-d93b-301c-a4a5-c7341e32bb37 | -9.36646 | -50.14129 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5484dc4e-1cc8-3fba-89a8-e20ebad50d0c | -6.91649 | -55.63427 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92fbeb60-2a2a-3ba9-97ab-232ee51ec262 | -12.0999 | -47.31251 | 2026-09-14 04:53:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e6ee389-2599-3313-8981-95ab14a116b0 | -9.71912 | -50.85089 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71fb35ab-bb99-3d87-8e5c-b64618132f85 | -10.65599 | -54.14271 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 86a1b93a-7ed9-3dde-9f82-047a3dd9e48a | -4.1206 | -60.6889 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8230ca11-2b1b-3930-ace7-04b4df349e17 | -9.71633 | -50.84679 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92f1d90b-7b9d-3b59-88d1-9cb4abc0d6a0 | -8.33577 | -50.75536 | 2026-09-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d32dc5-1b61-3bd8-aa65-ba58aecf9f08 | -10.67744 | -54.16182 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a9301f06-d4bc-3f20-b216-b09563607a7a | -9.61332 | -51.09684 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6aeeb721-db18-3c5c-9c10-9f00a0d49543 | -6.33519 | -43.36646 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7e575a34-9381-3c6c-b9dc-c40b644606ef | -4.387 | -55.20508 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b87648c-4665-39f6-ba9d-8826071d824d | -6.5957 | -58.85514 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1b4a9c6-636a-3ad5-8bb6-7bfcc2831e34 | -6.29531 | -55.28338 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7eff814f-6b6d-3d51-9cc4-a62960ddab90 | -7.0763 | -41.80017 | 2026-09-14 04:53:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a9bc621-e556-33d8-955a-3837557c4678 | -8.61145 | -55.23413 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151fce7f-2c90-335b-b1d8-60c29e031240 | -9.68568 | -54.84585 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 728fd5b0-8408-31d2-a7a6-adea957b369d | -4.34573 | -54.78029 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27fc5952-75d9-3628-9efa-765486813f4c | -12.16106 | -48.95839 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ca329e4-cc29-32f1-842d-0eede4a3a7d8 | -11.24951 | -54.1408 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc437945-11af-3d8c-acd9-be8183958f20 | -3.79754 | -55.88218 | 2026-09-14 04:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6a8a590-2147-3d89-a659-3314205c8712 | -7.11709 | -41.78966 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e00ac72-1fdd-3a98-9218-c310b5ac9173 | -4.13588 | -54.01066 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12c54862-b5ff-341f-a565-e90f174663e9 | -4.09131 | -54.44142 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b17e2fb5-e2fa-38b6-8130-43ba342e570f | -6.15107 | -57.69492 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 179d49b3-3fc7-3a6c-a89f-cdef40eb44c7 | -6.33833 | -43.3635 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 868eb3af-4fc5-3174-9eba-60035fa4b01b | -10.56299 | -51.33709 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34526e47-11ec-318e-ba2a-fe29903deee6 | -6.59478 | -58.86036 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README44.md)
