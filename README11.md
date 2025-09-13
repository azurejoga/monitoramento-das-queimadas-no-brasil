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
| 0adc0e91-f48d-3575-9fed-45103d1de8db | -9.2656 | -59.4191 | 2025-09-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 0f4055c1-c1e1-33cb-88ac-2a8791188f1b | -20.5952 | -50.404 | 2025-09-13 01:00:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.5 |
| d20f88a1-c32c-30c2-901d-2589228e2a50 | -10.7661 | -50.5513 | 2025-09-13 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 20785a8a-31d8-3360-910e-919270745ca9 | -16.0061 | -47.9329 | 2025-09-13 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 47.4 |
| d23b9ccd-246c-3633-9e0c-d9ec972f82cf | -16.4906 | -55.1276 | 2025-09-13 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 128.0 |
| 80ab2e53-e375-317d-84b4-8d829d7e6c6c | -9.5006 | -55.9588 | 2025-09-13 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1c041d1b-9d53-3561-8ab7-0c7468bbe057 | -16.2546 | -50.0524 | 2025-09-13 01:00:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f152bfab-8d4d-367b-9c15-0a9bd6430d53 | -12.006 | -47.7505 | 2025-09-13 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8229180a-c316-3788-b0c9-01af9578ed04 | -9.2472 | -59.4007 | 2025-09-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| a83b37bf-a422-3904-b86a-3b4f3515d13d | -11.0945 | -51.45 | 2025-09-13 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 854b4b88-ec2e-3033-9c8f-bff9ac77fb03 | -10.7474 | -50.5319 | 2025-09-13 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| d674857f-7f4e-3bbb-8737-2cc470f60dcb | -16.0257 | -47.9294 | 2025-09-13 01:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.9 |
| e47306f1-52ab-3622-8f56-ca37d43e0269 | -9.5324 | -54.6277 | 2025-09-13 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 3371f39f-12ea-3a1b-9ff2-b9e74f424aed | -16.0997 | -49.9677 | 2025-09-13 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e1360b96-a0b6-33d6-afad-037160140567 | -20.5958 | -50.3814 | 2025-09-13 01:00:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| 9bdae0cd-9281-329a-8d15-5211f785a7a4 | -3.2305 | -47.135 | 2025-09-13 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 651c5623-e2b6-3ed6-9bb2-c31ac85effe2 | -16.08 | -49.9709 | 2025-09-13 01:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| b48aa274-562b-3895-bf76-d246ab69383e | -11.075 | -51.4942 | 2025-09-13 01:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0ea9cb71-7b88-3f07-bbb3-fb62f6fde3d5 | -9.5004 | -55.9788 | 2025-09-13 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ef72bbb0-99d8-36aa-977d-397446ca25a9 | -3.2306 | -47.1131 | 2025-09-13 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 37361a27-e5e6-34ea-a665-38fd9ccaa466 | -11.7196 | -46.6031 | 2025-09-13 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 216.7 |
| db9dc650-d626-34ac-91d4-5c21accb33b9 | -11.7232 | -44.2146 | 2025-09-13 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8633704f-a785-3eb6-8f7e-0c22dfaee4d5 | -11.1511 | -51.4652 | 2025-09-13 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9a108a0d-8f23-3784-9ea6-f2378c240f1b | -3.2282 | -47.6371 | 2025-09-13 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| f1b15887-44ce-3e59-9310-d6bafa88ae6b | -10.6579 | -46.2694 | 2025-09-13 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 77b450a0-fd4e-38de-b045-f0901b804a69 | -17.2836 | -47.2364 | 2025-09-13 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 9a07a375-e119-3944-a924-cad34379b341 | 0.6904 | -50.6481 | 2025-09-13 01:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 229b55fa-d210-3ff9-aef4-ed270fc77b2b | -9.4819 | -55.9601 | 2025-09-13 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0445864c-3b68-3ad8-a967-2cbe40b49739 | -10.6575 | -46.292 | 2025-09-13 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5706d2d3-df28-36e3-aa08-4363baf03e12 | -9.247 | -59.4201 | 2025-09-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 087c38a4-631c-3068-8a35-abd6fed953a9 | -12.0056 | -47.7728 | 2025-09-13 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1d4b6520-445a-380c-95fb-783c35fb5778 | -9.2843 | -59.418 | 2025-09-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 15b3a079-bd10-31fb-8c3f-02d405ad178f | -9.2505 | -51.2261 | 2025-09-13 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 31645854-8164-3c61-9ec2-29946fa33062 | -14.4394 | -47.3206 | 2025-09-13 01:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| f3530481-5644-351f-b14d-4d5bdd9f8476 | -21.1854 | -47.5346 | 2025-09-13 01:00:00 | GOES-19 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 86daff3a-7e73-3567-a4cb-df2f9dda04bf | -18.6139 | -48.2044 | 2025-09-13 01:00:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 898fcd60-69e9-3e3c-9fa8-cd5bbcb3853a | -9.4993 | -46.4299 | 2025-09-13 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 70e7f39e-145e-30cf-9d1c-b920f6742cf0 | -11.9869 | -47.7531 | 2025-09-13 01:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 42bb8a41-55a3-35eb-97c7-392cd3f9430b | -3.2321 | -46.7836 | 2025-09-13 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| b39e7a08-c60c-3cb4-85f1-67c6e9348ac6 | -10.6389 | -46.2718 | 2025-09-13 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| e5f2b371-d3be-3311-80e5-f9e793129c45 | -9.2691 | -51.2455 | 2025-09-13 01:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 48b39838-7c16-349c-85ad-eb2eca128f3f | -11.7384 | -46.6231 | 2025-09-13 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| b6d24fca-c394-3648-8000-799ca1fa2195 | -12.9292 | -54.7538 | 2025-09-13 01:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 8953a05a-a16f-3638-9726-b45ebf4a00c5 | -10.0129 | -50.3937 | 2025-09-13 01:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| 18aa3aaa-e36e-3008-9352-db579614895c | -11.0752 | -51.4731 | 2025-09-13 01:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e56b37e3-e8a1-3490-b033-672243feefec | -20.5946 | -50.4267 | 2025-09-13 01:00:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 9be12583-94f7-308c-bd6a-a1a3a3e12438 | -11.7388 | -46.6005 | 2025-09-13 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 8fe54123-487d-3109-b100-0f4c59914d64 | -16.2541 | -50.0745 | 2025-09-13 01:00:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| f2985478-924e-30db-bb05-7c6b96cceaee | -9.2658 | -59.3997 | 2025-09-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 241.6 |
| fa31b7e4-d1a7-3929-8348-dff1954914cc | -20.6156 | -50.3998 | 2025-09-13 01:00:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 166.1 |
| f03ea5ff-ba18-35d2-8da5-61f1322ac7a1 | -9.4996 | -46.4075 | 2025-09-13 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 18ea2217-971c-336d-ac1f-56716a33a978 | -16.5106 | -55.1042 | 2025-09-13 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 00ce078b-f5c6-3bd5-8d09-09e551493adb | -16.5102 | -55.125 | 2025-09-13 01:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 5c2624b8-7065-39eb-a9d6-6a7dbbf6377c | -15.2036 | -56.6803 | 2025-09-13 01:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 5e02a4d9-709e-3b13-be8d-d8a1f6ce18d2 | -17.2339 | -50.2398 | 2025-09-13 01:00:00 | GOES-19 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 385a9410-2324-3ff3-9caa-5d10b639c62c | -3.2097 | -47.6378 | 2025-09-13 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 31aa420b-6759-3a95-8a89-43b2ee2d6fcf | -11.0755 | -51.452 | 2025-09-13 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 98c56a20-6f68-3249-bbb6-159529f9ffe9 | -11.7192 | -46.6257 | 2025-09-13 01:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 4004380c-d8f4-32c7-8da2-b2a8a4a1c5ce | -9.2844 | -59.3986 | 2025-09-13 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| a6ae87e2-1b66-365c-bde7-745498d427ea | -10.6385 | -46.2944 | 2025-09-13 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b7ee6651-a8ba-3190-a2c0-052b5df21858 | -11.7424 | -44.2117 | 2025-09-13 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d3f8176d-de2a-34bc-b71d-dd19ac5d2f91 | -3.2305 | -47.135 | 2025-09-13 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| cf7a3c7e-e9cf-34d1-96dc-4a36e395e3f3 | -9.5006 | -55.9588 | 2025-09-13 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d8ac29d2-1666-39bf-bb00-d172ba81a5ad | -15.1165 | -52.4918 | 2025-09-13 01:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 3b634232-5bf0-372d-a1eb-10ee24c48a45 | -16.5102 | -55.125 | 2025-09-13 01:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| e29c60e9-3ae3-300f-ae00-6c0b001d1e1a | -17.2836 | -47.2364 | 2025-09-13 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 8f73387e-f332-3bfb-8db0-731873cd43c8 | -3.2507 | -46.7829 | 2025-09-13 01:10:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 19260cc9-ab62-3e0e-945f-c0e8ee87c43a | -10.6579 | -46.2694 | 2025-09-13 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e54c35f1-8262-30b5-967f-1fc366ba0040 | -12.006 | -47.7505 | 2025-09-13 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 3b1315b1-5d3c-38b3-8558-f6c2c3823b94 | -20.4607 | -46.4372 | 2025-09-13 01:10:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| bb5f8062-6c6e-3617-8989-f86c0ab41277 | -9.5137 | -54.6292 | 2025-09-13 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 6b6a51a7-4ec7-37bd-8c25-f33ae14999f3 | 0.6904 | -50.6481 | 2025-09-13 01:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ecffb99c-610b-391d-bd8c-9f596c204b67 | -10.6575 | -46.292 | 2025-09-13 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| e248efd6-2982-3763-9786-a31cc3c047a5 | -11.0755 | -51.452 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| f198a272-3111-3ed1-ab4b-697b0e5b5a40 | -15.2229 | -56.6782 | 2025-09-13 01:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e28c27f9-66c6-341a-b829-4caa1404cc61 | -11.0752 | -51.4731 | 2025-09-13 01:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 122.2 |
| fd9be9ac-f2a1-336a-8d30-ce584b57624b | -11.9869 | -47.7531 | 2025-09-13 01:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 53a755a6-21ae-38ff-a46e-aa721150fde3 | -9.4993 | -46.4299 | 2025-09-13 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| e9162842-cae4-3077-8f9d-2a61298bd70c | -11.7388 | -46.6005 | 2025-09-13 01:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| efca7e6c-2306-3b2c-ad25-b571422c3078 | -16.2546 | -50.0524 | 2025-09-13 01:10:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 0ad04d05-751b-36af-a064-b7f61cefbb6a | -14.4394 | -47.3206 | 2025-09-13 01:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 28e14c40-6c1d-3bde-a2dd-972c0b2d0313 | -9.2843 | -59.418 | 2025-09-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 2980e65f-e073-3448-bd27-12f9912eb3c1 | -16.0257 | -47.9294 | 2025-09-13 01:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 0633da69-7d62-32b4-a55f-1ee85dc29289 | -11.8468 | -50.5813 | 2025-09-13 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0d025362-f7c9-3749-a3d7-a92136f7a4ae | -18.6139 | -48.2044 | 2025-09-13 01:10:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2ff98058-eb44-375d-8607-82fab50b0d02 | -11.1423 | -50.7242 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 181.6 |
| ed4351d7-2f43-3c65-aea5-0e90a3289171 | -3.2282 | -47.6371 | 2025-09-13 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| d8983ff0-9726-3cb5-80db-0f31ff7afe39 | -11.1616 | -50.7008 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 43492419-8e63-3be9-af2e-e45208e18272 | -11.1426 | -50.7028 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 144.5 |
| fd566e99-dbf2-3018-92ad-65d366f839f8 | -16.3418 | -51.5434 | 2025-09-13 01:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| a95fc3f9-0edd-37d6-83e1-30d30fe2b2c7 | -9.2656 | -59.4191 | 2025-09-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 257.4 |
| fb873000-1035-3904-a864-069cc2b4e175 | -20.5958 | -50.3814 | 2025-09-13 01:10:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 9e35b252-0c1b-3736-87a6-8bb63febdb05 | -12.9292 | -54.7538 | 2025-09-13 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0c9c9bf8-ca90-33c8-a5c3-1c350b1409fd | -3.2283 | -47.6154 | 2025-09-13 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| a1a95fdf-d9e6-3a0a-b514-203cc9353558 | -16.4906 | -55.1276 | 2025-09-13 01:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 6de876d0-bd66-3d45-9186-56c0eb42f187 | -9.247 | -59.4201 | 2025-09-13 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 09473e19-f648-301a-b998-076c51cfba99 | -3.2321 | -46.7836 | 2025-09-13 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e017218a-c102-380b-891e-8b74d710938d | -9.5004 | -55.9788 | 2025-09-13 01:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7992b4fc-119c-371e-b6af-fb1fa31fa6a6 | -9.4804 | -46.4321 | 2025-09-13 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a3f642be-518d-39aa-ad8a-1858d6f40962 | -11.1709 | -51.3998 | 2025-09-13 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |


[Clique aqui para ver as próximas entradas](README12.md)
