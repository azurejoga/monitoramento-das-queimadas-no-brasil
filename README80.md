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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 287c8963-2399-3e0f-93b3-82eb8c205c4a | -19.14322 | -47.69441 | 2025-09-12 04:27:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8eccbf1-ac9a-3765-8b2e-947627d6fafd | -14.43268 | -48.42299 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81af71ed-34a7-3433-b57e-ed6f8356a2b9 | -12.99575 | -47.99684 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7fc172d6-872b-3df8-a2ff-891acdb1a62a | -14.18188 | -46.19416 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffd554fb-2b76-3986-ba81-7f11bde182be | -14.1836 | -46.20608 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c11852d0-13a2-3288-841b-cd11c3f14f6a | -15.5489 | -49.74367 | 2025-09-12 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4b30602-d21a-33a7-8a17-be92b9e12b5b | -13.54025 | -43.00363 | 2025-09-12 04:27:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e6106949-b749-309a-a5a4-a63bcd9e234f | -19.75535 | -46.09021 | 2025-09-12 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 132a7c0b-dcc1-3abc-9f25-437455ad596e | -11.80875 | -50.57113 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d1ddd7d-3df5-3db3-91ec-07311c73af89 | -18.38558 | -50.55417 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de785d8a-8bce-3c80-9352-1544daec947f | -15.13751 | -52.35598 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ae96938-2127-35fe-ad01-1a09b5c4509e | -13.35645 | -41.92263 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3e228659-1904-389c-8396-0d0ea245dac8 | -15.86974 | -48.3334 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f415b32-6576-3045-9f5c-cfaa89630c43 | -15.67986 | -47.05201 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ea2cc27-efeb-32f9-bfb8-842eeee69d33 | -14.12712 | -45.38467 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74e7cf9c-70ce-3390-9bb9-386a1cffaab3 | -15.08078 | -52.43547 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d50dedb-918e-3a26-97e4-78fcfb00f771 | -18.97624 | -47.89986 | 2025-09-12 04:27:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ff1b567-21a3-360a-944a-52b4a55677f4 | -17.94855 | -46.9378 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b425985-99cf-33d2-95fe-2d4141797518 | -19.6604 | -44.90997 | 2025-09-12 04:27:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9567333b-e490-379b-83bb-0aedd0efcb7e | -17.2725 | -46.0876 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bf33e62-e559-3ada-9ce7-6c7a67c2cba6 | -14.51846 | -53.91287 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62ca7181-d7a5-3132-b1b3-75ee97518cfd | -12.85799 | -52.97028 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12eda9b2-3e4c-3eeb-ac66-38158374ad9f | -14.42993 | -46.40492 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 800452a1-b1a2-3610-b689-d2cd44c085fb | -18.82355 | -46.88202 | 2025-09-12 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31a734fa-cdb8-3380-b1a1-0baa507867ba | -11.18769 | -55.07512 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ae5ae02-f955-3c2a-b132-7380a5c94d0c | -15.78694 | -52.24 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60afa8aa-de29-328e-ae74-ce3acc24923e | -14.41972 | -47.33702 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e1637d8-c7a8-36c1-8e61-6b8b07429223 | -16.28518 | -45.68181 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5b21b70-c39a-39df-bca4-f74129339baf | -11.95195 | -51.12648 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 922572c2-43a1-320c-b413-f8b3794659d5 | -17.34673 | -46.70205 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68fab851-06f8-3cc3-a50b-a173bf630def | -15.28588 | -53.78234 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80ae792d-7abb-3669-b411-ee841860b97e | -14.33005 | -54.11292 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04dbdc45-4ffc-399a-8628-4a8520071221 | -14.38778 | -52.96048 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a796b1f-1698-351d-a84c-a501a728a19e | -16.10368 | -49.634 | 2025-09-12 04:27:00 | NOAA-20 | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bf4d839-c571-320f-8d01-5d08bfc49c6a | -15.10101 | -52.45398 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47af850f-cc67-32d9-a67a-610868c2357b | -15.10479 | -52.45466 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31e36261-9861-3ac8-903d-16b310b417e9 | -15.24146 | -48.0535 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb105524-7f95-3af9-b2ae-5b1a2bf1b36b | -14.45359 | -47.31301 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0427b613-b6cc-392d-b087-4b4d86e9f073 | -17.13101 | -48.49481 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c207de5-7e43-3982-bf84-bf3db672427c | -16.42617 | -49.04471 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 979a5424-1d14-3733-8317-d65cc600614b | -18.0514 | -45.43303 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad4bc2a5-226f-3424-9500-098c16d8a914 | -17.72823 | -46.15389 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad8bddce-e245-347f-b84c-0d51b89e6a26 | -18.06239 | -45.43473 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c170c39f-45df-3abd-bf56-2927796d0d06 | -18.30675 | -45.015 | 2025-09-12 04:27:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4adc53c-ff95-310b-bca1-8ee074d7bd0a | -11.77293 | -50.56487 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17d57c03-160e-3bf0-b774-ba0b6d1cfb28 | -18.44715 | -49.55453 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 34c4cdad-cca1-32f2-9d50-376fefef830f | -19.24269 | -48.03888 | 2025-09-12 04:27:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b41461f2-e69f-3aff-b03b-46b3bf329a6d | -18.32366 | -52.08277 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9f6cd3a-5f13-3ae0-b094-d1b6449ed198 | -14.28468 | -45.04565 | 2025-09-12 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86a190e3-c55d-3542-8ed6-b29f43982c86 | -16.41504 | -45.70277 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 626ad7d9-b08b-3e7b-92f9-73efae98f65b | -15.68939 | -47.0116 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58521047-77cd-3825-be0f-7ec1c8446e6d | -15.12658 | -52.46122 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9002cc1-5560-3b1b-bfe6-f9e9e469253d | -12.84957 | -47.95542 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e5732c2-bd2b-3ea5-966f-d76e2cfe0153 | -12.8562 | -47.9565 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c23902df-166e-36f1-8ca4-b402bc29b0d0 | -14.5053 | -53.91401 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a55c1ed7-d725-3d3e-b6e6-02ec545491fd | -14.39141 | -47.34356 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 012fa2f7-efef-34a5-8fa0-92f7833345ff | -16.29168 | -45.68704 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54b6461e-30e0-392a-ab54-ed298ced9f0c | -19.05844 | -48.33625 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d54ee21-1ba2-3560-8375-3f0fe4a6ee67 | -15.1189 | -48.61466 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9adf3c0-1fd2-39af-b94a-2cc0919568f8 | -16.82504 | -47.79866 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc2704cb-3139-3146-805c-23e17cdcbd96 | -14.37203 | -47.29226 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05614320-0c39-341a-b585-2a09a825b80a | -15.86918 | -48.33697 | 2025-09-12 04:27:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 284be6bc-0a0c-3e86-b65a-02e6de1ee30e | -12.47378 | -47.49604 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2714590-d1da-3e48-99e3-007eecfcd4dc | -13.98904 | -48.22219 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5b27ec7-0457-3d40-ab53-389cfe2e1f79 | -14.50388 | -53.9219 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11febe3d-b6e6-3c40-84d8-766a563b8a19 | -13.89517 | -48.23643 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8594e82e-18a4-3957-9d8c-6eceb406e81a | -14.13704 | -45.41506 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b355236-86d6-3eb1-9794-a9a8845d821b | -18.65307 | -47.65528 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0e00f34-2137-3fed-b1bd-a74aab620768 | -12.962 | -54.74887 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c124c5d2-7b60-31dd-af01-fafdbd308d26 | -17.34105 | -46.67447 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 995fece3-705f-34a9-9be0-9b8bcbd27493 | -11.93041 | -50.70121 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3174d85-4a84-37e9-91e4-f4ef5a688f12 | -15.15656 | -52.40216 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e7f5bfd-b266-3b3b-890f-376fc9c59ca4 | -12.92949 | -48.00771 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1954a6e3-8327-3d2f-abc1-1567ddaa61aa | -12.17244 | -48.7236 | 2025-09-12 04:27:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46e8b657-0175-3591-bc9a-77b179753892 | -16.66459 | -47.62273 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72438c4e-0599-362b-8bcd-5ce103604869 | -13.92066 | -47.94614 | 2025-09-12 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eeb68897-c0c3-354a-afda-d9380fa6d717 | -13.1322 | -54.92444 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5acd1f42-696b-3a88-86d2-385287e8aafa | -15.09469 | -48.01437 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04d124ab-14bc-374c-8066-9fa7c6729d5f | -15.54493 | -49.74679 | 2025-09-12 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a83693-c3ab-3e9f-bb6a-c1a2b53ee5d0 | -20.26395 | -42.12291 | 2025-09-12 04:27:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| e41acfaa-eb97-382c-ada6-fd14355a0f35 | -12.91838 | -54.75184 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 63d5f0a4-a9f7-3192-bc75-4971733c82b8 | -11.95379 | -51.17493 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f5914589-776d-3590-9e83-7bc1b2353012 | -15.10463 | -48.01601 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8c07e9e-e1ed-3d23-a5fc-94461581c56c | -15.66923 | -47.07689 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a05229a6-0a21-342b-9eae-bcf6c85ebdf1 | -18.06176 | -45.43912 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 503038ea-ca9d-3552-9452-ea6cf0a5e8c9 | -12.93733 | -54.75081 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c6455b09-aa19-37b4-87e2-35a529a2284d | -14.42028 | -47.33343 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 525f621f-2b50-387b-ba6e-29f404a43592 | -18.76694 | -48.5365 | 2025-09-12 04:27:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dd6bd4f-c080-387b-ac84-b9638490b663 | -18.66432 | -47.64946 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4eca33e4-35f5-3af7-894b-78704892dca8 | -12.88767 | -47.95087 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8698df2b-bf57-39e0-91f8-a2952da181c2 | -18.68456 | -47.67594 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a9c0245-19c9-3fea-8d60-27bd30567e72 | -11.19246 | -55.07607 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ba1b6b5-69e5-3941-acf2-f3c3132281dc | -14.26611 | -54.77881 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 564cfd16-5a8d-3d4d-bcc4-a0f5d51b29d8 | -17.71945 | -46.13974 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 525ea789-c4a9-3b4d-8632-4233100b1c86 | -14.42937 | -46.40865 | 2025-09-12 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb051945-2acf-3653-8ed0-71e30c2c1a8b | -12.89979 | -47.96006 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68a74b12-8f0b-3b44-b470-23f5f12f0291 | -18.61411 | -48.25224 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cb7fa845-72e2-357f-a955-a032fbf57019 | -13.36385 | -41.92496 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 46b32a92-8dca-311f-9843-dae9a36e83a8 | -15.12163 | -48.61882 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f626552-cc58-380f-9c0f-559e7e9872f6 | -15.13441 | -48.60265 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README81.md)
