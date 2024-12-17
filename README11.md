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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619c1c50-8d1b-3369-a8f8-391e75d4b87e | -3.76671 | -47.16095 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42bc81ca-fd74-3ff1-a321-b2bfae766d7a | -4.03284 | -46.90465 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 078533af-eafb-3504-8afc-58fc862e8e56 | -2.14622 | -48.04032 | 2024-12-17 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b627606-2cfc-3a5d-b380-8eed184c0b5e | -3.3035 | -53.36289 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 18319eb6-c90c-3ea0-bc42-5eb4835d97c8 | -4.09595 | -46.18358 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb27ad79-463d-3d25-837e-4b3630745e5c | -5.31639 | -46.48259 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22aceab4-ce4a-3b4f-b05b-0c8f290789fc | -5.09635 | -43.90426 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 6dbe2223-9a58-36aa-a010-70967160887a | -4.03172 | -46.9045 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 70ce1b99-7308-3492-b127-89347f06837d | -3.02683 | -47.83027 | 2024-12-17 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 15dcdfd6-76bd-3723-945d-cd39addb413a | -6.1012 | -39.86385 | 2024-12-17 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 70f51049-3644-3710-bb66-a1f18474d349 | -3.94456 | -42.63781 | 2024-12-17 04:21:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2ea9741f-a481-3775-9ccf-22cc0b053044 | -4.07641 | -47.10503 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3d2ad59e-c8d7-39b2-8bcb-4d9eb81a6f6b | -3.14159 | -48.60804 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 795c0b13-e902-3245-921b-7c2831ba4d29 | -2.32689 | -45.77933 | 2024-12-17 04:21:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f398019a-ae3c-3717-936f-fcfc5bd6c722 | -4.79252 | -46.39761 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 3e4022eb-4092-311f-96b8-274aa7a2f367 | -4.05196 | -46.91961 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35e6c0f5-4b9a-3f79-9e2f-cea93c88d795 | -4.04736 | -47.0154 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ae1d3ae-4262-3c1e-b6a3-4bba580e812b | -3.30292 | -53.36629 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 54ab1546-70f1-39cd-a915-9657fa8669b8 | -2.57312 | -45.95636 | 2024-12-17 04:21:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6767a83e-90a6-35c6-9722-7a6bbcd2aac3 | -3.96845 | -47.03162 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78399725-e0b8-30fc-a160-034841a93b45 | -5.20829 | -44.56254 | 2024-12-17 04:21:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec0058bb-4373-3a7a-bcdb-ee4671fd9188 | -5.31756 | -46.47525 | 2024-12-17 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67f60441-5b8f-3455-99af-ab392545cb70 | -2.62213 | -44.28629 | 2024-12-17 04:21:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73dc2151-3f86-3088-b7cb-9a851bbb9de0 | -3.77256 | -47.17007 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68757d48-78a2-32d3-9f01-8f082ba092aa | -3.78771 | -47.11827 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e889ab1-fa5c-3730-8a6f-1ebdd153b745 | -4.73114 | -46.80258 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fb59e29-ab30-3d2d-9818-77530ac39876 | -3.79213 | -46.81678 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d46e650-0a4b-3180-93e1-f603a6a31c64 | -3.99659 | -47.28572 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc52f1e5-3fc3-3904-bae1-734191e2db62 | -2.03607 | -48.57622 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0959cf8f-7583-30f6-abf9-699a4bfc0a04 | -0.92516 | -46.90251 | 2024-12-17 04:21:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e63bbf50-85b6-397d-8ad2-aefed7a200c9 | -3.77319 | -47.16607 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16c1843b-b2d8-34d3-8941-e01199118968 | -3.30497 | -53.36455 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bbb5616d-7440-3866-9795-73c0d2858ed5 | -3.29966 | -53.36353 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 58c15981-079a-387b-90de-d4d00695c5fe | -1.06257 | -46.83722 | 2024-12-17 04:21:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ec4c73c-3fd1-331f-bc04-5f3536c2eeeb | -3.89632 | -47.18763 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c330db16-a4c3-3353-a0fb-ab9adabc6e51 | -3.93242 | -46.89697 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2a177f1-42d3-36bd-9a9c-7ce8e8a55290 | -4.70535 | -44.38449 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf4b7bd6-c111-3af6-bf56-815ffbf6a66f | -4.06292 | -47.09884 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba2a2905-3ea8-34a9-a951-a53c034e20d8 | -4.10708 | -46.68718 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a97ffaa9-76f7-3a30-8bd0-59a53877c120 | -3.45538 | -42.03002 | 2024-12-17 04:21:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cd15bbfc-7c15-38f4-a42b-1fc281f29e6c | -4.0462 | -46.9108 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0708f20b-f094-33b4-b7d5-1a235a05b127 | -4.57017 | -46.58021 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b8acc89e-5615-3421-a47e-351502c7aa59 | -4.17403 | -38.13227 | 2024-12-17 04:21:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c560dc82-1236-33ef-adac-73f7300d0727 | -4.40152 | -41.4355 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1740c588-4d2d-3a2a-83a5-a7ad428b4a98 | -3.15295 | -45.97382 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d325a358-a372-392e-ac58-f6a4b7ff5d04 | -3.14238 | -48.60318 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf4dc02b-d967-36cc-a5c5-fe93d5f4dfd5 | -3.84841 | -45.8585 | 2024-12-17 04:21:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e1a75d0-a1f3-3613-9627-8d1d013dfe2e | -4.04949 | -46.67802 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d89c894-9f47-3250-a7bf-a7a8c053b54b | -3.13771 | -48.60744 | 2024-12-17 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 83fdd032-f3f6-31be-b9f4-c22a05baf75d | -5.08532 | -43.90969 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9913242a-55b1-31c1-9b1b-f83e966bebc2 | -3.16316 | -45.9754 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f901b940-a6a6-3544-bc9c-e1bd0e9b2779 | -4.04034 | -47.01419 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7f87b9f-38b9-3565-85d4-652fe19f0d1b | -1.54102 | -53.73063 | 2024-12-17 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 982f7f5a-b281-3440-bb56-9583b5a5612a | -4.03845 | -47.02597 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ef48dd-0a79-320a-886f-5a03b59850c4 | -3.89485 | -47.10648 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e3f2b1-53ff-3438-a230-dd415aebb01c | -3.29819 | -53.3619 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 50c740f9-a58a-3701-91ee-d7cd3b4592a8 | -5.34304 | -44.28705 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e0b8aa3-fca2-3c09-9bee-614c2a99211e | -4.05798 | -46.9045 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0400194-8edf-3abd-a89d-d7a403aa9e81 | -1.08832 | -48.21173 | 2024-12-17 04:21:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0327f8cb-cddf-35d8-ace9-5a767eb8c4fa | -4.08285 | -46.61705 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0ebba39-fe70-3e32-a9d8-f519a663b7de | -3.78546 | -47.10976 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a4d7fd3-4d72-3083-a1a4-c7c3412b45c8 | -4.04557 | -46.91469 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc33744f-6a18-374f-b9d9-47258e71a333 | -3.89505 | -47.10557 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f135dcc4-6c74-3cfd-ad19-195846b15e8f | -4.02815 | -46.8361 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 920fdaa8-da15-3c1b-8bb2-93f9e43df9fc | -5.36348 | -44.04562 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cd01233-49e4-3a1d-a906-b57c322c6735 | -2.51372 | -49.05527 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be50748d-d469-3615-b977-f2d934ffb4d2 | -4.38182 | -46.55094 | 2024-12-17 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80ed6151-2d04-3a19-8f9d-754738517b21 | -4.98226 | -44.15624 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ead8859d-13a3-3500-8fd5-dc39cccb4b1e | -4.72725 | -44.09147 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e41a10b6-3c42-3716-a0e9-1c27a42222e4 | -1.63757 | -45.85509 | 2024-12-17 04:21:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1336998-ebc0-35db-a3be-e6e877f11b37 | -5.09528 | -43.91121 | 2024-12-17 04:21:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 571a3e1d-79c0-3834-8d77-0cd3f592b2da | -2.89983 | -41.7145 | 2024-12-17 04:21:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 66c0a39e-a834-308f-9665-6f5c3aa76902 | -4.06998 | -47.09991 | 2024-12-17 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed2be272-39c1-3aad-b22c-c0a249f6a310 | -4.57947 | -47.0914 | 2024-12-17 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3d3b617-e457-39c2-be28-518e3e706478 | -4.67657 | -44.04464 | 2024-12-17 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ef91b49-0146-3120-a65a-197884aeb3a2 | -4.07015 | -46.59182 | 2024-12-17 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fd23b4dc-1451-3f77-aac3-35a181ae6c45 | -4.06085 | -46.90898 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b84c81ad-c1c1-3c14-bde3-0a0166361a51 | -4.82503 | -47.32372 | 2024-12-17 04:21:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e1ec6d5-eaef-3fa6-b6ab-38a801c44c11 | -3.15628 | -53.1835 | 2024-12-17 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 621118e1-9b2e-37cc-a621-7f63101bd85f | -3.7849 | -47.11457 | 2024-12-17 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 604ce642-8842-3f68-bc48-9cb1b9d10e6b | -3.9244 | -45.43982 | 2024-12-17 04:21:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19d4de36-5c0b-3af3-8e5f-45d73c6ae461 | -6.21634 | -36.6769 | 2024-12-17 04:21:00 | NOAA-21 | SÃO VICENTE | RIO GRANDE DO NORTE | Brasil | 2413003 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ef8990d8-da91-3d75-9fa4-7bc26e5fab67 | -5.11332 | -43.19996 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6a0fb85-6fb9-31ad-af29-9a293505616d | -4.65235 | -44.33038 | 2024-12-17 04:21:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7d1d4d5-4336-38fe-a57b-e13098cb2aeb | -4.99564 | -44.33493 | 2024-12-17 04:21:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91b1ca40-e808-3f14-a0d9-f9eac972572c | -4.14359 | -46.30451 | 2024-12-17 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed5a292f-d2ad-3684-bf0b-e1693d0d5f7e | -5.14143 | -43.24088 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78c44e5c-c849-39ae-994e-cc0a75e9407a | -5.29593 | -44.9362 | 2024-12-17 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4a60bc8-01e7-34ba-b92b-10f74f03585e | -2.58221 | -51.92095 | 2024-12-17 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 309964d3-a516-3ed5-8fb0-af211b8dbebd | -4.0427 | -46.91026 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aad1d0c-d7ee-3c53-929b-623cb7743ea3 | -3.15012 | -45.96963 | 2024-12-17 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9023a2e-16a5-32a7-bc30-ca71ab7d3f40 | -2.51718 | -49.05943 | 2024-12-17 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd4742e6-1040-3216-b3ba-308e7e48fd28 | -4.40215 | -41.4314 | 2024-12-17 04:21:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6b93e650-0100-35b0-8cec-04e6d378c581 | -2.76779 | -47.39141 | 2024-12-17 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63460816-0ca5-3a29-bcc7-066b9f52c3f6 | -5.01645 | -44.30991 | 2024-12-17 04:21:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2d3406e-ffe3-3e98-a898-1db8ff646dba | -2.14696 | -48.03567 | 2024-12-17 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e675aa2-a587-3caf-85b8-874ed5d5828e | -3.93718 | -46.88969 | 2024-12-17 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83a2dbcd-eed8-3725-9944-a2400827436c | -4.46089 | -44.64244 | 2024-12-17 04:21:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67b44120-6aee-3201-9b6a-864d6eff215b | -5.12005 | -43.20101 | 2024-12-17 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed453852-0357-3b6d-8f19-7b37325c070c | -2.54612 | -48.38017 | 2024-12-17 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
