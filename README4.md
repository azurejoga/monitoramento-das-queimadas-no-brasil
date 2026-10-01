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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4da133c-982b-3c14-8d74-b96dceb70db4 | -10.77678 | -50.56299 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b89ba927-679f-3fa3-b27f-a0c0792460a5 | -14.42896 | -51.25607 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5e83bd80-45df-3645-95be-775619470fa4 | -10.72939 | -50.53198 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aafba053-c8e9-3f82-afdc-fcc897cf6334 | -7.53736 | -47.12689 | 2026-10-01 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 53c61eba-9634-346e-883a-2088a0a354b0 | -8.23292 | -54.7487 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6b99b3b-305f-3ee7-b6b1-76e775017839 | -8.79339 | -48.00376 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1dfd7234-37b6-3b84-b050-f30fb905e076 | -10.55653 | -50.04995 | 2026-10-01 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 24da99ae-a2e0-3867-a148-edf0de7421b0 | -10.25587 | -49.67366 | 2026-10-01 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7d8323da-6b94-365f-bf1d-299f09017bb3 | -11.44435 | -43.40899 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 879.2 |
| 198ee220-748a-3bfd-a2d1-f73d33c87a87 | -12.38829 | -54.09143 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 3339e416-a789-3290-8d25-53aee5f6c160 | -6.7378 | -44.14391 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 44aca418-def1-35bf-9eac-7167e116b522 | -10.65995 | -50.7564 | 2026-10-01 00:18:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1ae17c80-5a25-3039-9742-97b71afc361b | -9.31607 | -57.71533 | 2026-10-01 00:18:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 04a7799a-c64f-322f-b5d0-84692ab8e7ea | -8.25967 | -54.74496 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 785e2858-5c0d-3b04-a0a5-80b97d7056e1 | -14.87294 | -51.85474 | 2026-10-01 00:18:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a92075a4-df37-3eab-92b1-043b71d316d3 | -12.85811 | -44.34503 | 2026-10-01 00:18:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 91622f8c-821f-3141-8292-22ee04e4ea6a | -14.4303 | -51.26549 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| bbf12154-2ccb-3528-a962-837bab415694 | -13.42338 | -43.82085 | 2026-10-01 00:18:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 4772690a-f47c-34f0-b7b9-9c0573ab8a6f | -11.42804 | -43.41204 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1018.4 |
| 7b2ec1db-05e4-37a3-b54b-68b73ef54889 | -11.40765 | -51.02388 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 051b4469-e7fe-3925-af70-73964f89c9f4 | -11.37541 | -55.12146 | 2026-10-01 00:18:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4570e40f-2028-32d9-90f2-75be0fe10b0f | -10.32986 | -47.78104 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 99382240-1205-330c-9977-1ee2e15a1403 | -12.7758 | -54.03128 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9b50eb24-bc17-3b86-b2d7-62b32fb6c70c | -11.1948 | -45.18222 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 7db89809-9f98-35d0-8634-09d985c267d0 | -12.38953 | -54.10076 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c0b7a673-5f28-3099-afea-fd068ba0f3b9 | -8.37401 | -50.88383 | 2026-10-01 00:18:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4706849-9d1c-3e6c-9675-fdbbf924de64 | -7.85447 | -45.81939 | 2026-10-01 00:18:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d55c54bb-71b4-3b48-b268-2e237dd28450 | -12.77455 | -54.02194 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8be0cce0-e03e-3e5a-8ccd-cc76175f9e39 | -8.30226 | -54.7142 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bed0f613-c860-3603-9606-7e7e3614e78f | -11.4179 | -43.4088 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 2e9124c3-99bd-3eba-8418-c0c00ce59b34 | -13.64741 | -53.94249 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 2c73b6a1-bc68-3f00-ab23-300795789bdb | -13.66668 | -53.94939 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 98328c2c-c8de-390a-b533-76ef31446ca8 | -14.42131 | -51.26688 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c162b81b-7a1e-3fc4-87b5-540da20960de | -8.6245 | -45.38112 | 2026-10-01 00:18:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.2 |
| e023b0d6-1db8-31f2-9e0b-8e23951b0db7 | -14.43928 | -51.2641 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 6c9d4be3-3486-3850-91a8-7da2c9e3a01a | -11.67632 | -43.49889 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 3d9ec04b-01a0-307c-afc1-267dc38e90b4 | -11.45045 | -43.44458 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 588.0 |
| f5dc0d78-aacf-3c44-a0fd-a4c9a2b7b656 | -7.71896 | -49.55329 | 2026-10-01 00:18:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e268c845-9ead-3bdb-93c0-d90233539cce | -11.40619 | -51.01382 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d6bd5c52-43e1-36b0-b06e-1f43db7c9ded | -14.49087 | -48.30563 | 2026-10-01 00:18:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 84daece7-b84d-378d-8556-bad871c6168d | -12.19285 | -48.45107 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d560b05b-f8f2-3523-a485-fa3503914079 | -10.56329 | -57.77338 | 2026-10-01 00:18:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9ed200e3-9551-39ba-94cb-aaa6f92a8a8d | -12.25713 | -54.00252 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e451748a-87e1-3972-a018-edde464f4b0e | -12.31363 | -50.28576 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6bd62615-b0dd-3320-8abd-591f70711359 | -8.21207 | -45.47569 | 2026-10-01 00:18:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9069413a-5673-354d-a305-093c291f6189 | -8.31849 | -54.76741 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 197369ad-bd66-3578-8744-02ebb985d6a5 | -11.72709 | -50.42042 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f224a98e-466d-3dee-92d5-f343c5eb6512 | -8.24603 | -47.99123 | 2026-10-01 00:18:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 56e37aaf-13d1-377c-9307-ec77be1b5789 | -11.80174 | -50.50043 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| f1e8338a-2e50-3dbc-95f9-372447c86f8b | -10.85297 | -48.71193 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| e34aedc9-9293-3a44-8d3a-942a5c6b7f0b | -14.44062 | -51.27353 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| a9d482be-91fc-30d9-ac4c-753179d7fd9a | -11.4342 | -43.44769 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.2 |
| 23b5c2f9-013e-395f-9ee8-1a996ad61a3a | -10.85079 | -48.69807 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7c5cef31-8114-3730-b5b1-c4c6bb6cba5f | -8.23659 | -54.77592 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e96f17d4-934c-3c12-a217-daa5bfec11ec | -11.38468 | -55.12022 | 2026-10-01 00:18:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a407555c-0595-3d38-9bbd-d1af3d082bd7 | -9.08185 | -45.00168 | 2026-10-01 00:18:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 45.8 |
| a3eba033-70c9-3358-a887-3e08718649ff | -14.40873 | -51.30729 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc7b28ef-c400-3a54-b10d-8f2eae85f4df | -10.4125 | -53.77539 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5ac548a3-0a3f-3aab-b499-e6c64acd96f6 | -8.16613 | -54.80087 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 11c4b8d7-aa9f-3258-92aa-6b1b7297a9a5 | -10.7406 | -50.5413 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 90850126-473f-30a1-b1f0-6761d67b072c | -8.80043 | -48.00924 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c49c5a8b-71be-3d5d-b869-f50b3496e7dd | -13.66543 | -53.93991 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 1082a0f6-ad73-37f9-9a48-f12144fb8b96 | -13.65767 | -53.95068 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| e101aa8e-d87b-3d75-bcb8-968abac414dc | -10.76556 | -50.55371 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d6cd9f29-7b3a-3ad1-a1c4-6119a48c1fef | -10.77358 | -50.54145 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 285.3 |
| 1460ffeb-52db-3667-baec-19001c8a9248 | -14.14296 | -51.12457 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fc5e753e-547f-32c8-b39c-5daa48581105 | -10.56229 | -50.85229 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3b36b966-8d59-39bf-a956-8841f147a755 | -11.19249 | -45.18796 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| d2ffe70a-0550-33ec-87a3-757247467bab | -7.38645 | -46.42893 | 2026-10-01 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b39d6e51-8217-3bb2-ba48-2c863801cdab | -8.38347 | -50.72951 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e19325c1-9fa5-3d9f-80e2-784c9acca7f4 | -11.32673 | -50.96993 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 504ecb94-9b7e-3e50-9e84-8a6004c51045 | -14.41997 | -51.25746 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5256015c-31c0-37ce-a7de-44cfdd901d51 | -8.17505 | -54.79964 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3eb21840-9d4c-3f3d-8696-ad096f170fae | -10.8421 | -48.71409 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 0ed2f754-fafc-3c3a-ab8d-d5a2df642482 | -10.75303 | -51.66243 | 2026-10-01 00:18:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b5c110f4-0d52-39d8-97a6-229f1d75e21e | -12.19707 | -47.38734 | 2026-10-01 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c4c4900e-48ea-3343-8046-64169f29010b | -11.16803 | -54.11695 | 2026-10-01 00:18:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 24922c67-b508-3d91-99a6-5a5942e2a04a | -10.3179 | -47.78244 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b54f4754-33a0-3e13-b588-ac047a30029d | -11.45051 | -43.40271 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a794a1ef-a7e3-3ec2-a005-78fca6e08f7a | -9.74429 | -53.88269 | 2026-10-01 00:18:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fff209e9-3b2d-31bc-aacd-fc089fe9fb62 | -11.46314 | -43.47367 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d1301c88-6222-389d-8175-01df09e0bed8 | -8.30568 | -46.749 | 2026-10-01 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1bd984c7-9cc1-3710-be00-013058da3b94 | -8.06442 | -55.34478 | 2026-10-01 00:18:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a4bb36a7-4093-3f2a-8295-7672e35d0343 | -12.19466 | -48.44438 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 4f0fabd9-5917-36d6-93d3-407bdcb8a64f | -9.58956 | -54.63485 | 2026-10-01 00:18:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c116814b-762b-3b9e-ac8a-1364767d6c26 | -13.64617 | -53.93307 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 7d7b9d74-4b0a-3b9e-bcd0-8364a5766c72 | -8.16212 | -54.83854 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8c348e60-9dca-3a57-83ba-7e4e7a6ea438 | -12.19072 | -48.43702 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b1f376f8-7b4f-3af9-aef7-bdc4d7355acb | -8.29224 | -46.75098 | 2026-10-01 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 57f04912-1d4d-3ce4-a461-f93b2b6e3b68 | -10.42987 | -53.83683 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f53abaa2-cb32-3694-9a5b-eb2a6c9b3a30 | -10.76395 | -50.54294 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 9bc09b6c-fc1b-3744-ae6c-698a9b643887 | -11.95481 | -51.0463 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 64415c69-c740-33df-a415-1e59e151e245 | -10.73096 | -50.54279 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8a6837a2-7450-3bdc-b0ca-27e3225e2dd8 | -7.38188 | -46.43494 | 2026-10-01 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 7330bd94-7cb8-3005-a786-74b047e869f5 | -11.80018 | -50.48985 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 42bcb9fa-4c59-3601-81c4-123d7fde4f00 | -13.88861 | -44.4544 | 2026-10-01 00:18:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 2033e6e1-5d71-3c92-9f35-70fb6b178277 | -10.84003 | -48.70092 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 8ec199d3-ecd3-3b61-914c-3f962c6c1443 | -12.26484 | -53.99197 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 70655c40-bdfc-32e7-832e-1f761773f7fd | -13.4268 | -43.82701 | 2026-10-01 00:18:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 8ae80ba1-46ee-313b-83ca-4afbbc21b14a | -13.64866 | -53.95197 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |


[Clique aqui para ver as próximas entradas](README5.md)
