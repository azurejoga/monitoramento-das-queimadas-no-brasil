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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17179bc8-c8db-3f4b-b591-eebebefb6767 | -8.51665 | -43.30276 | 2025-07-22 05:16:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 44ff96c6-db5b-3d96-8ad1-844daa009de2 | -4.37625 | -43.29139 | 2025-07-22 05:16:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| ab42d109-6cd0-3d71-9179-52b27802a9d0 | -4.37887 | -43.27485 | 2025-07-22 05:16:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| e14383c3-94d2-3b03-87ac-d623b0e3557c | -8.50569 | -43.30098 | 2025-07-22 05:16:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| b95cb4a6-a199-30ce-a06c-13df19da0cc8 | 0.68968 | -51.4605 | 2025-07-22 05:16:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5907c33-231f-3b02-9b47-e490523ac49e | 0.69205 | -51.46138 | 2025-07-22 05:16:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf025529-aaac-3b70-947b-df95388bbac9 | -14.38338 | -47.73989 | 2025-07-22 05:18:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 7a69438f-b780-3fb8-8b22-eb11d1377997 | -13.68499 | -45.67897 | 2025-07-22 05:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 96cd455c-43d6-3721-a883-55abbaeba250 | -15.93119 | -43.51876 | 2025-07-22 05:18:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 9e85eea1-0067-3aa1-9c33-2b48467a0c89 | -14.38637 | -47.76231 | 2025-07-22 05:18:00 | AQUA_M-M | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 26.6 |
| bf59aeb0-f6a7-338b-84a9-00816ed4c43d | -11.73401 | -48.17789 | 2025-07-22 05:18:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 10ff5e60-f5f0-3e9f-9694-02b98607fc57 | -11.73271 | -48.18219 | 2025-07-22 05:18:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6d7f89fc-1bac-322f-9e07-3ea6b84d87ee | -13.65174 | -45.72763 | 2025-07-22 05:18:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1ae7bb40-d013-322d-af1c-68b740fbab26 | -3.04512 | -47.38079 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3db57e78-0477-32b7-880d-f5a517651d3a | -3.04787 | -47.38092 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72dc4a27-42f0-3205-b29d-0e19b9cd2a56 | -7.14583 | -46.09764 | 2025-07-22 05:18:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ed207ed-80fc-32cc-a5de-eb41870d36e9 | -6.5719 | -45.61107 | 2025-07-22 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8f877e8-06ee-3748-9c10-d9d3d7498da4 | -5.56795 | -45.21318 | 2025-07-22 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07976994-fb67-3dd6-bfdc-ccc8e007a60c | -3.58569 | -49.43292 | 2025-07-22 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c4b2576d-8884-39d4-b633-0933628adf8d | -2.91606 | -48.24405 | 2025-07-22 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5de526c9-924c-39d7-85af-1b1081d5e51f | -8.08349 | -50.08776 | 2025-07-22 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8e0025c-3dae-36e8-93bb-c98f09301acc | -6.21524 | -57.77271 | 2025-07-22 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 32f51acb-bfeb-3b2e-b384-996119e36227 | -7.14518 | -46.10342 | 2025-07-22 05:18:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67cfc89b-097a-3049-9b50-760600da2889 | -7.146 | -46.09704 | 2025-07-22 05:18:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84887bf7-2a01-3ecf-89ee-851da2eec08d | -4.34488 | -55.77227 | 2025-07-22 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc8e18f8-39c2-3c97-a6a7-6bd2a834e91d | -4.54507 | -48.00725 | 2025-07-22 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc90352b-dae1-3e02-9e7c-0de8afbe3a3c | -6.64114 | -49.75831 | 2025-07-22 05:18:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5167268a-0c57-301b-949d-9bd7f0066646 | -7.51906 | -49.44272 | 2025-07-22 05:18:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d414f149-5fc7-3e68-aafb-f6c132d14507 | -3.58043 | -49.43209 | 2025-07-22 05:18:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35552519-e00e-3521-8526-a49dcc71574e | -7.15362 | -46.09159 | 2025-07-22 05:18:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e20bb15-9863-3f97-ba96-c4d572eaf43d | -4.54659 | -48.01043 | 2025-07-22 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1802173-d496-3f52-b018-594369789c4d | -6.63036 | -49.75682 | 2025-07-22 05:18:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39825b46-9643-3944-bbe8-a0958b913b71 | -8.09733 | -46.82798 | 2025-07-22 05:18:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb42438-22da-3da9-a256-0df36027a5f0 | -5.30417 | -55.97356 | 2025-07-22 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ddb1f0ae-cc32-3b97-80ae-bc512e24c375 | -3.65412 | -48.32154 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 616a0777-c794-3b33-9948-165a3e82d46c | -5.1336 | -60.36401 | 2025-07-22 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 22f0424d-9ed9-3838-9986-58f3e194dbac | -8.08879 | -50.08921 | 2025-07-22 05:18:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd560945-6d60-3d2c-9cc0-be256f8675f5 | -8.10395 | -46.82898 | 2025-07-22 05:18:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 255a5f47-bf40-3982-b9ad-08914be3087e | -2.91661 | -48.24027 | 2025-07-22 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76bf83dc-0e0a-3e6a-8ed2-ce593bd14fc2 | -3.82784 | -47.74019 | 2025-07-22 05:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ecc3373-7081-3ff9-80a3-e508a35183da | -4.99946 | -56.29326 | 2025-07-22 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ede13b8c-60e3-3af4-8605-c5abe3d77a15 | -4.70346 | -55.96909 | 2025-07-22 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12a3f716-710e-3925-a87a-1a3288cf3d17 | -4.54722 | -48.0062 | 2025-07-22 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e617934f-bb4c-3aa7-ab89-7ed4c595dd4d | -3.64969 | -48.32358 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 832f3267-9eb9-30e2-bd37-a1c4a5f220b0 | -6.64243 | -49.7613 | 2025-07-22 05:18:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d675e122-09e1-309c-bdf8-4e9ebe3358e7 | -6.64289 | -49.75788 | 2025-07-22 05:18:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7816c783-819e-36a1-a080-3bfbec1a45cb | -5.13701 | -60.36456 | 2025-07-22 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e95e8152-5f48-3c08-8c86-4135bfe01066 | -4.31927 | -47.98694 | 2025-07-22 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 723a2aa4-e555-3a41-a5a3-e41cd0dd4ea2 | -3.65535 | -48.32452 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 861fcce7-29f2-384c-b030-a982909ead1b | -5.56703 | -45.22004 | 2025-07-22 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3315889d-4148-3282-8b38-620d041fce79 | -5.55997 | -45.21905 | 2025-07-22 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 527f9af9-8fcb-3094-82f3-d4d07c683272 | -3.04126 | -47.38431 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a8372e7-1d96-3b38-a035-cfbb36a84179 | -2.92498 | -48.24077 | 2025-07-22 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d62ee91f-dbd7-3d2b-a419-61429e36a25d | -7.15375 | -46.09096 | 2025-07-22 05:18:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccc2964a-6e9e-3ec8-b663-e44cde723b29 | -3.65354 | -48.32533 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85ad632d-bf29-35ad-9ae5-dfac41390b68 | -3.04449 | -47.38494 | 2025-07-22 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a72ba46-9e1a-3c85-a9d0-f2c608a2b10c | -1.8844 | -55.52621 | 2025-07-22 05:18:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cadab1cb-b172-3b27-9111-e2df8e514acb | -2.91876 | -48.24367 | 2025-07-22 05:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5573ed22-bc9f-3e4e-8a6d-c3877430ab05 | -4.99597 | -56.29274 | 2025-07-22 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72b67ad0-1294-366b-87fb-742a9ad85d9c | -3.82955 | -47.74278 | 2025-07-22 05:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9687f9c-767f-3afc-bd8b-b0e1d9498473 | -5.56412 | -45.21437 | 2025-07-22 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57f82d9d-dc65-3323-97d9-867275fcd23c | -3.48146 | -53.9748 | 2025-07-22 05:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4d5d45-30f2-3ab4-a881-488983c94583 | -5.56316 | -45.22122 | 2025-07-22 05:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0877217-1518-3bbb-bb26-77c64ecc0c74 | -11.7317 | -48.1849 | 2025-07-22 05:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a8ba6942-9669-34bf-8291-e7a62b205db3 | -8.5211 | -43.3063 | 2025-07-22 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| b3e46957-645a-32e3-91f9-b4f2f869ac37 | -20.06346 | -41.39955 | 2025-07-22 05:21:00 | AQUA_M-M | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| a921a61b-d8fa-34ef-97a6-f9cf50b7eaf2 | -9.46129 | -63.14674 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d7d3bf0-f213-30e1-913a-0ac5dab26bfc | -11.30805 | -55.12083 | 2025-07-22 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0f0bb61-daf8-39cb-9a2b-6c5800f847ad | -7.24129 | -60.19034 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d1eb870-733b-38e3-a0b0-6d13a2adec24 | -10.29717 | -60.54148 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd0d3194-9718-3656-b250-2a78958297d7 | -7.24072 | -60.1939 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9925c7f2-db60-334d-9322-15748355e54d | -11.72736 | -48.1885 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2feeb4c5-d4a5-3e9f-97e0-ac47628c3577 | -8.88514 | -50.15992 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b771abe8-f026-3699-a6e1-36322c75c42b | -11.3128 | -55.11617 | 2025-07-22 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 817685ef-0e59-371e-a3c2-c80d63293e48 | -11.2415 | -50.36731 | 2025-07-22 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44977859-da82-3f10-a3a9-64b063ba57d0 | -11.75008 | -58.34848 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d51f6422-87be-3898-a33e-ccc2ca1be07e | -9.3555 | -62.64598 | 2025-07-22 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7438497e-cb03-3578-9b3b-97fc3acf2f3d | -7.29614 | -60.17001 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80c97cbd-748e-3a39-be02-a0d239729edf | -14.76562 | -48.25817 | 2025-07-22 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 024906ce-89b9-3cef-b8bc-054c294125b0 | -10.56286 | -50.38227 | 2025-07-22 05:21:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c066679a-3418-3370-85f6-a09958be2472 | -14.38795 | -47.74664 | 2025-07-22 05:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 454bda4d-a564-3037-af84-4e9a75a90e18 | -8.31059 | -55.11292 | 2025-07-22 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61363316-b932-37c4-a223-2b669f122cef | -9.83289 | -60.73569 | 2025-07-22 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8909b0d-7eb4-3239-b03d-73f34729cb59 | -8.87972 | -50.15924 | 2025-07-22 05:21:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fb8fbf2-f0f4-3127-8ae8-7e65a267fb82 | -10.05045 | -59.10163 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1337c25f-51eb-330a-95d6-d305e048029a | -7.26313 | -60.18291 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef31976d-fdad-32c0-8c8b-0621f06bbed9 | -7.2816 | -60.17497 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16011212-65dc-3079-aa5e-03552278ee86 | -11.32336 | -55.21368 | 2025-07-22 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d8ef747-81df-3c11-af4b-307807bfca0c | -11.73374 | -48.18935 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 625c8638-7aab-3f34-b8f2-b28b926065df | -11.73437 | -48.18392 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 403e637c-ddef-35dc-9cb1-2fe4aecf4d20 | -8.95741 | -62.24082 | 2025-07-22 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 869b0325-1d71-39be-ab36-480e7e327567 | -14.77226 | -48.25842 | 2025-07-22 05:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ea0dbde-a8f6-362b-b441-c24f5c54500f | -11.727 | -48.18234 | 2025-07-22 05:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4e869146-6f3c-3244-8eea-d9073cbaf990 | -12.49777 | -57.76951 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| baaa0ac4-d604-35c0-a8f0-a3a5c1645e49 | -7.26762 | -60.17636 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f25cebd9-f9d1-33c5-ba03-5a5f05809e26 | -9.337 | -58.84121 | 2025-07-22 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d233a0db-0419-3ddc-8080-da3deac0f4d7 | -7.97175 | -55.29554 | 2025-07-22 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2636aca-af8d-3e00-b6d9-1104051e5a06 | -10.03767 | -59.09598 | 2025-07-22 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bd16c26-d821-3212-a63b-1c1b08b1dcba | -12.5048 | -57.77057 | 2025-07-22 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e144ea6-2f06-3da8-a1ca-f353a0a898c2 | -7.28944 | -60.16893 | 2025-07-22 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README18.md)
