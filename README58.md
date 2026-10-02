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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcd10f53-7176-3dc4-ab23-c025073b3ffd | -4.2657 | -50.76739 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5128a2ce-2098-3c25-857a-09bb09cc7e3d | -7.34158 | -55.22207 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b746cb09-6358-39a8-af3b-97b69eba33c4 | -5.7416 | -55.74562 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e255e2c3-d2bc-348c-8098-429408c4b046 | -2.02956 | -54.29095 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 092e9b95-0ee0-32f7-b2d3-3767f9746635 | -7.51046 | -47.334 | 2026-10-02 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a13ade02-dea5-3787-8309-8ce46ceed759 | -3.84988 | -55.80601 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e506962-688a-3405-8623-e7fc5d953e88 | -2.96708 | -51.01875 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67c3cf39-5f74-3571-be4d-31b47c336b70 | -7.33002 | -55.23088 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3a1d5b0-61e6-3bfd-93a1-67a017f418fa | -7.05349 | -55.6468 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c13617f-c6ca-3c66-b841-3d60b017671e | -8.08265 | -54.88214 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1ad9ec9-065c-3624-9e43-e0bc0dc22a56 | -3.16778 | -54.08323 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b00447df-4a95-3d30-ab61-45723d02685b | -7.83324 | -55.12672 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a6ae878-53f4-316d-a57c-c642906428bc | -2.5806 | -49.99905 | 2026-10-02 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1869545-aba3-3ee1-9a30-7cdad60ca2ba | -8.17474 | -54.79026 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50220062-8d28-3fbc-981f-fdb3c2445a35 | -4.60927 | -50.91741 | 2026-10-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 643a8c16-220c-3136-8b96-1dcefefb8066 | -6.79325 | -55.54786 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f7cf1fa-5c67-3467-b9e9-da6f49f7208f | -5.85758 | -53.48203 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63583525-d957-3eb8-bd08-184ac4b3fca4 | -3.10651 | -50.2821 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 23c7d382-5c03-3f7d-9900-1de2c3d0df8b | -7.3267 | -55.23037 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62b72b03-1488-348e-9dc7-97b3f46bba94 | -3.10323 | -50.30329 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21b95d21-ec9d-3b8e-8d1b-c491b1418f74 | -5.84487 | -53.4764 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 712c3f76-4e84-39e1-8106-497e12980afa | -3.00867 | -54.23089 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f157dde2-73cb-3945-9b18-a117b54a11f3 | -7.45891 | -54.99535 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 361fef22-49f7-3e4a-acde-7660e94b83a2 | -7.87384 | -44.17576 | 2026-10-02 04:57:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c3d35d0-677b-38aa-b42e-8fcf6e58ef29 | -5.97295 | -55.37708 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e1a4d35-e2ef-3d2b-993e-aa4fbb531d62 | -7.39866 | -55.2062 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 422a396d-fd2d-3674-86ff-e53728f79782 | -2.50444 | -56.91048 | 2026-10-02 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7850f444-14b3-3044-871f-0e01ffa9bf0b | -6.43372 | -52.70308 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b787988d-868f-36eb-8c7d-361a87d4f9d5 | -2.89447 | -54.13544 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ba41a80-41ae-389c-a0cd-26544c19edf9 | -2.98751 | -51.02588 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b22e6e5-f009-30db-889e-13a17d1a1c6f | -7.73509 | -54.79501 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10a72c92-6ad5-3061-987f-322275f3622f | -6.22209 | -52.43784 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97513a50-c86e-3b71-bd2d-3f63ef5ad171 | -7.55638 | -55.02552 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7b0c01a-6300-34fa-92f4-c070cf6b3537 | -7.6566 | -55.10174 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d14b4674-18c5-3aac-8e20-ce02c9e29110 | -3.16448 | -54.08273 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6efa9d33-52ea-37a2-b0ad-e195b21fcf4a | -5.67908 | -50.09528 | 2026-10-02 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 95bf91ae-0ac3-3e95-8a1d-0599d5034ccd | -3.59443 | -54.55375 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03ae8a07-efb4-378e-a9af-490b12f91229 | -4.45591 | -47.91829 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 73cb20e3-8418-3d27-89f6-3603fdd12e96 | -7.74115 | -54.79951 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90499c2c-71c9-3625-974d-344638b4cfeb | -8.06597 | -54.83339 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8264a8ad-6eb4-34f1-90bf-9ec75510de73 | -6.75958 | -55.09372 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bb85c08-eadb-35b9-889f-96c86647b0db | -4.30437 | -50.89972 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 186c7d12-4646-3e28-b8c1-a568826477e5 | -2.17787 | -56.30992 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01c09d81-45a8-385a-a694-9e6ed1c1eee9 | -1.3675 | -56.9157 | 2026-10-02 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44450b0b-b2af-36dd-a3c0-359f02407904 | -8.17918 | -54.80515 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 818b9192-5275-331f-af1b-c088ecf0984c | -6.41087 | -56.39928 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9faaf7-78f6-3fbf-bceb-d16242deda2e | -6.36346 | -55.14485 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306701da-6df5-34ae-973c-eab9b401e320 | -2.88006 | -54.87624 | 2026-10-02 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4b4db06-c166-3b9b-872e-1dac7f9d5f5c | -4.26397 | -50.75437 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f32f61f4-1bf3-30f2-8b6b-5194b0c4f92e | -7.63014 | -55.07627 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 260b0c3c-1ccf-30a1-a65b-0fee622517c8 | -5.73418 | -53.61913 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a9fbe63-7852-3c1b-87dc-07e26640dd53 | -7.05855 | -55.48507 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f569ea3-7b8b-3d3a-b0d1-ea13bfd06d4d | -6.23782 | -53.13394 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db4677f7-9b59-35fd-a78d-d700f97a774a | -7.05016 | -55.64627 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c111f81d-3b68-37de-ad36-d629eec7e37f | -3.04651 | -53.88098 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72b8a82d-06fa-368c-98ce-0f3ec650c4ed | -3.29121 | -53.85992 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e313681-942a-35b8-b375-b44cdb3fbaa5 | -4.26273 | -50.76267 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16c2808d-58eb-3a6b-8cc9-a13c6afb94e7 | -7.32947 | -55.23438 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66f83cfa-7502-3459-ad65-d77940ae2cc9 | -2.5008 | -56.9099 | 2026-10-02 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27335c5e-6172-3a86-a14b-91c3816fbc57 | -6.31441 | -43.34118 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d40a5d0-f41a-3112-82b1-595b18e1b173 | -8.17804 | -54.79078 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2025b98-913b-39d6-90ba-92872c89ade3 | -6.24116 | -53.13445 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb025a0d-f48f-3c6c-89d9-5cc09c8da4da | -7.83767 | -55.14164 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60550236-b56b-37f4-8869-45457e911de5 | -3.69268 | -55.48815 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d5c4d10-2cd5-35a7-bfa9-e80133b67d46 | -7.57362 | -55.1313 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 641570a1-feef-376c-b20f-ed9b19fb48dd | -5.89587 | -53.49857 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7f117c4d-4f9e-3224-884c-b71c6fc0ec1a | -6.24676 | -53.14259 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 946447e2-571a-397f-a27a-a31ac8c4f79f | -6.24434 | -43.77388 | 2026-10-02 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 31dda437-4c26-3945-bcd8-f5d7ae9ab910 | -7.41634 | -55.58939 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1477721e-1503-39c4-8c34-f45458963918 | -7.82388 | -55.12169 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cf5f0c1-0a6c-31ce-85e7-855012699d78 | -8.24697 | -54.65696 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d49a314f-d69d-3e8b-bb14-5750a59014c5 | -7.89062 | -54.71735 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ce78ea9-2d74-3616-8f93-889048e5f5be | -2.95819 | -54.09589 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 820bff65-7338-3312-8b05-a6f20590cc3f | -2.89555 | -54.12855 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6837be67-2b27-3fd8-87b2-fd5a616bd969 | -0.95393 | -52.33227 | 2026-10-02 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cef2066d-e9ca-3616-b6ea-e52d84bab610 | -3.14562 | -53.74945 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc01acbc-6025-304f-9373-ebdbdc3a3d01 | -6.13935 | -53.06741 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68e04a4e-8f9f-3018-af91-4c98ceb2a7bc | -6.74065 | -44.14098 | 2026-10-02 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ca3a0dd-32bf-38ed-9ff7-e54a3c960be8 | -3.1095 | -50.2869 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7f2e387-a1ee-3b42-be42-a13355f9f18e | -5.29758 | -55.87286 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a6cd5b1-352b-3bdf-978b-e26f54dfbc90 | -8.91971 | -49.25537 | 2026-10-02 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ee19890-fc02-343c-9631-4b9ed6ebb367 | -3.22019 | -54.31402 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32c95581-b0cb-3f2b-a364-87a2103d3cb0 | -7.28098 | -55.58544 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f65b93d2-1149-352b-9c73-10a0f38f5af3 | -8.25544 | -54.73272 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80cae7a6-78d8-3119-93ac-546381f2fc56 | -3.13519 | -53.75135 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 54c56ee7-ddff-35b3-a4ec-6d0e1515804c | -4.29982 | -50.78532 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d11e51a4-1457-3864-9961-7213fdcc826b | -7.05405 | -55.64326 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d441447-2c09-34cf-b9b5-1c5af546bb1a | -6.70754 | -55.57362 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b708562-def1-39e8-b4cb-791b92c09730 | -6.20813 | -53.25997 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2509c142-ac68-3827-ade5-4212ec0ea400 | -6.23837 | -53.13037 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26335f3f-f7af-3134-a15e-8d4bc878d7ad | -7.83607 | -47.92199 | 2026-10-02 04:57:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46dbc9c1-82e6-341d-aee2-b35fe102f7e7 | -4.46021 | -47.91895 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7ef4d1d-f57f-3f08-950b-32a3a7305729 | -1.34674 | -55.24366 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0fc364f-a7ee-368d-bc3d-96658f3ae535 | -8.1925 | -54.83277 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 755489fc-3f2b-38df-8ba7-d22062f08b78 | -2.3944 | -56.98981 | 2026-10-02 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a936ee7-ab82-3197-8553-bb387d3aaa80 | -4.45473 | -47.92648 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 52a8cffd-b502-364a-9baa-11aa05925436 | -7.04628 | -55.62751 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b9f0517-8158-33e5-8c9c-ed8f724f541e | -7.57308 | -55.13478 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c56da6f-402d-3762-8f7f-232431f501cf | -9.52756 | -45.34431 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c1843d7-0f28-3d2f-ab7b-b5e128152e24 | -4.29713 | -49.09638 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README59.md)
