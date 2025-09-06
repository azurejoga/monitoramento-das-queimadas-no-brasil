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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7116dd27-b4d0-3b4f-84b5-a0ed14a9ae6b | -6.32509 | -58.18207 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 55397e06-b713-32de-9569-08cc064f28e9 | -6.27687 | -53.43272 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 5ee6b7fe-a996-38a2-a544-c7cf559f53a8 | -6.16625 | -53.68863 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| cf092dfa-ed96-3891-8db2-ceddd6af7f74 | -5.00749 | -56.04339 | 2025-09-06 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 03a3e9a3-1ade-3e90-a8ca-02975a619a8e | -6.5462 | -49.51943 | 2025-09-06 01:11:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d2ec835b-42e9-36ae-8fbc-4a1f7a0ff9d0 | -3.24601 | -50.7914 | 2025-09-06 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 138636a4-50b8-359d-a01e-0955122dff69 | -6.84063 | -52.80384 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 5f7a7941-7632-3b9b-a2b5-de4f926941c5 | -6.32387 | -58.17326 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| f83d9998-befe-3826-b4df-89668f871bc0 | -5.9801 | -53.60001 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| bdda6d05-8fe6-3f9b-b24a-72ed0f8a3ce0 | -6.33389 | -58.18082 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 581cdcf7-5dc8-33d4-8f02-897d02a7a201 | -6.43867 | -58.14169 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00daa961-cd13-36a8-a8ad-14d02f793425 | -5.86823 | -51.7257 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7d24aa91-ee2b-387b-9436-58a272d48f14 | -6.4077 | -55.55688 | 2025-09-06 01:11:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cfaaf278-a8f8-312a-92a9-db8101f5ca34 | -6.54147 | -49.4898 | 2025-09-06 01:11:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| bc794522-43ca-33cd-bf56-abbbb0b56329 | -6.43989 | -58.15051 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0e83fcff-7d84-3177-bc59-24b8a324e248 | -6.4487 | -58.14926 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9dcdae0d-5b0f-3a78-9d9e-f25c1eb25e01 | -7.90318 | -61.51421 | 2025-09-06 01:11:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d1f01a1-dd47-3b34-b081-7000b3f96bd5 | -5.06993 | -56.07568 | 2025-09-06 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a698d0da-5326-31be-aedc-4000c58bdd26 | -4.27021 | -48.19007 | 2025-09-06 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 75c420a8-7fa1-3c5c-872c-d0f43bd74884 | -6.26788 | -53.44905 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1f60757b-acd2-34a7-ba69-833937708ab4 | -6.20362 | -53.24743 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a00e26c8-2133-3299-ae28-7b79935fb2e1 | -4.27122 | -48.18454 | 2025-09-06 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 48238ddb-7115-3e01-9cc7-3be6e20a530a | -5.48497 | -60.13153 | 2025-09-06 01:11:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| c1bcb367-63c9-336e-9ea4-a060535f1b6d | -6.279 | -53.44732 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| f6032a8a-21b4-3169-acad-6d580ce24965 | -3.24979 | -50.81777 | 2025-09-06 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 23251066-be9c-334c-90f2-dc886e3fa1d2 | -6.15336 | -57.94911 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 493c8373-8641-398f-a50e-28ddcccc2bbd | -6.27922 | -53.44072 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 97796e5e-d961-315b-895c-cc023b9a91b4 | -5.86973 | -52.16867 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2accb9d0-6682-3797-85d3-e907093ea1c3 | -4.38051 | -48.08251 | 2025-09-06 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f38cb91e-5987-31c0-abd7-4164e1f8145f | -7.72104 | -61.52525 | 2025-09-06 01:11:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 58777066-549d-3719-8d25-766ba59b9f00 | -12.5227 | -53.8485 | 2025-09-06 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 30c6ac04-30ec-30aa-a610-e440cd2b9308 | -9.7038 | -49.504 | 2025-09-06 01:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 016ed8d8-c912-3344-8680-4eb5fc29038e | -4.5033 | -42.862 | 2025-09-06 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 559cd033-f991-3d28-a667-2889a7c71acd | -10.6131 | -44.3051 | 2025-09-06 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0f798f3c-707a-3c0a-a314-cc3eec3f46fa | -21.377 | -51.7464 | 2025-09-06 01:20:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.5 |
| 332e0cff-5bb0-3f19-aae3-d3500dc1a3f9 | -6.5393 | -49.5101 | 2025-09-06 01:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ab933dc3-3aa1-3f18-ba1c-3df2c5eea209 | -3.2331 | -50.8087 | 2025-09-06 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 2a951fae-60cd-369e-a93e-022bc59d25b7 | -9.5343 | -40.3282 | 2025-09-06 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 98aab828-f1e9-350a-9988-93f4d5b95c43 | -5.4918 | -60.1189 | 2025-09-06 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d75ec6c2-737f-3701-b518-f2004a372ba6 | -9.7041 | -49.4825 | 2025-09-06 01:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 9536d3fe-8da8-3972-8d26-d2f689d59845 | -15.7186 | -53.5743 | 2025-09-06 01:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 09339f7c-dba6-3e09-9d6b-37d76a79f308 | -4.5029 | -42.9089 | 2025-09-06 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.8 |
| b5ffbd92-d8a4-3dd0-aec9-43f00209cfd9 | -4.4844 | -42.8866 | 2025-09-06 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d2416bcb-9590-3265-9f98-1e836434d00e | -7.3324 | -48.4857 | 2025-09-06 01:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| dfcc15e8-a1a7-3b05-8ec4-3c4d0be4f963 | -7.3322 | -48.5074 | 2025-09-06 01:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 063af56b-bd1f-36df-a017-49e02352cfbe | -12.5033 | -53.8712 | 2025-09-06 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3ae2f964-2e5d-3068-89ba-d3d0ebdfadf5 | -5.4917 | -60.138 | 2025-09-06 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a412a9f1-8334-3b4d-8a90-3bc1f524d96f | -15.5942 | -52.9149 | 2025-09-06 01:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 58bad3ca-d86f-39f1-b8b4-17ce235a1439 | -9.5347 | -40.3033 | 2025-09-06 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 213ffdf3-2163-353b-bf0e-4b186ad17c1b | -4.5031 | -42.8854 | 2025-09-06 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 432.4 |
| 908dd147-a0f9-332f-bb82-2fad5d5c51c8 | -13.0044 | -54.8282 | 2025-09-06 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f689f999-1c8f-330b-8636-459e730dd1bc | -21.3976 | -51.7423 | 2025-09-06 01:20:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| ef2c5b15-5c6e-39ab-9929-0f0a074feb1c | -12.4846 | -53.8525 | 2025-09-06 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2de24b70-5c4d-33f3-bef3-5afb27d7dcd1 | -14.9015 | -49.454 | 2025-09-06 01:20:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| db8d22da-c68e-336e-9aac-ff6cc1c2961a | -12.5036 | -53.8505 | 2025-09-06 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a48fb649-3244-3a84-8146-41de258fba8f | -12.4843 | -53.8732 | 2025-09-06 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e6691a21-a19b-36c3-a99f-b4d15b2559cd | -10.5937 | -44.331 | 2025-09-06 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 43620ddd-afc3-3692-8507-cba7fb2cd795 | -15.5751 | -52.8963 | 2025-09-06 01:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 18f888b7-41b3-3d7c-ba0a-215269962ba1 | -3.2516 | -50.8082 | 2025-09-06 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| bb4b0245-b0f1-3b16-951b-59623f558bae | -10.6128 | -44.3284 | 2025-09-06 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| f75b48f2-4e29-3a60-8662-f8aa25368eeb | -12.9665 | -54.8116 | 2025-09-06 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 1c6554eb-d032-3ac8-b776-2189a2b69e34 | -15.5747 | -52.9175 | 2025-09-06 01:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 61a53f3b-f4a9-34b7-8bb8-0b5f2a62a3bc | -10.594 | -44.3077 | 2025-09-06 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 8c0e16b6-8b2e-3a23-9984-d81a0cf8e106 | -12.5033 | -53.8712 | 2025-09-06 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 304c27bb-4289-31de-9d33-828f3ef8bc04 | -15.7381 | -53.5717 | 2025-09-06 01:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d19c895f-246f-3d51-af31-4289e9fe2745 | -9.7041 | -49.4825 | 2025-09-06 01:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| a791f0d4-b3b1-3577-a65d-5365f7019015 | -15.5942 | -52.9149 | 2025-09-06 01:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cc29e707-5d14-330e-ae53-2953062936b1 | -14.9015 | -49.454 | 2025-09-06 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 277.9 |
| 4939482a-80c2-3572-a9ec-b75333dbbae6 | -15.7186 | -53.5743 | 2025-09-06 01:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5810ff33-8933-378c-b071-e6ff3696afc5 | -4.5033 | -42.862 | 2025-09-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 05a89921-bd9e-3caf-b8bd-2e439f630c52 | -5.4917 | -60.138 | 2025-09-06 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| c99f07ea-4519-348d-a846-d03587527ff8 | -7.3322 | -48.5074 | 2025-09-06 01:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 22b762f2-ba0c-343b-b311-6e4cb4e1957c | -4.4844 | -42.8866 | 2025-09-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6708f282-0b58-37c9-903b-a3defe69331a | -14.9209 | -49.451 | 2025-09-06 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 129.2 |
| f781ddc0-6165-378d-bc0d-f533ea5ce980 | -10.6128 | -44.3284 | 2025-09-06 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 3cf658bd-175d-3248-b4c7-5fd0c34f5fb8 | -12.9665 | -54.8116 | 2025-09-06 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e523a472-0689-3a68-8b78-2d4cd1e2ff50 | -10.5937 | -44.331 | 2025-09-06 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 685e7a49-b894-3ce4-adfd-5aff5d1d2e5c | -14.882 | -49.457 | 2025-09-06 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 1c98c907-2405-3691-a1e5-8823fea293b9 | -21.377 | -51.7464 | 2025-09-06 01:30:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 150.5 |
| f788b9f0-de09-3e2c-b9f5-ff08128fa7ae | -14.9019 | -49.4319 | 2025-09-06 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 52522fb2-2e1b-3ed2-8a34-938bb2cb7530 | -9.5347 | -40.3033 | 2025-09-06 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.7 |
| 0a003d38-4ef7-3206-bf20-e63bf4643204 | -15.7385 | -53.5506 | 2025-09-06 01:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 021dfd58-35b7-36c8-a325-b9fd98607c30 | -4.5031 | -42.8854 | 2025-09-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 433.4 |
| 5cd10dfc-29c7-3196-b561-35eb30126f06 | -12.5227 | -53.8485 | 2025-09-06 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 924d8c10-b650-3075-b4ba-cb2a3f2cbb4d | -12.5036 | -53.8505 | 2025-09-06 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 66b0b362-87e9-391b-af51-bf08a902f392 | -17.7129 | -40.2695 | 2025-09-06 01:30:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 234.2 |
| 12189fbf-a7a6-3873-a264-83919071d54a | -3.2516 | -50.8082 | 2025-09-06 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 2c985eb1-80fb-38f4-8415-44b056e47035 | -14.901 | -49.4761 | 2025-09-06 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 31a1a128-7666-3ed4-af5e-cc0b0c6b9620 | -17.7323 | -40.2899 | 2025-09-06 01:30:00 | GOES-19 | SERRA DOS AIMORÉS | MINAS GERAIS | Brasil | 3166709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 103.8 |
| 0e86844c-c853-335d-a6ea-89b60a9c770e | -14.9214 | -49.4289 | 2025-09-06 01:30:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 50.8 |
| faad810e-1cc7-3e6b-807f-6bfcb99781d1 | -13.0044 | -54.8282 | 2025-09-06 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 60c12732-d339-3ea4-b60a-101222799744 | -10.6131 | -44.3051 | 2025-09-06 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 46341406-738a-303d-9869-f99c2c4a545f | -10.594 | -44.3077 | 2025-09-06 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6cd21d4a-4820-3771-82b0-94cf11864ad4 | -21.3976 | -51.7423 | 2025-09-06 01:30:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.7 |
| 303624ed-42f4-355f-9ac2-36b9d7e4f04e | -9.7038 | -49.504 | 2025-09-06 01:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3eff34e0-ce9b-38cc-be1b-1eced632073a | -12.4846 | -53.8525 | 2025-09-06 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| fab18177-8cd3-3484-9916-9ca224b07be1 | -9.5343 | -40.3282 | 2025-09-06 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 95bf23e1-88ce-3544-9dcb-fc3f9e8da051 | -7.3324 | -48.4857 | 2025-09-06 01:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| bfff825d-ff6b-3015-9032-7db2e6900ede | -4.5029 | -42.9089 | 2025-09-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 44848fba-5b26-3a9e-a836-313c2562e4b6 | -17.7331 | -40.2639 | 2025-09-06 01:30:00 | GOES-19 | SERRA DOS AIMORÉS | MINAS GERAIS | Brasil | 3166709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 232.4 |


[Clique aqui para ver as próximas entradas](README17.md)
