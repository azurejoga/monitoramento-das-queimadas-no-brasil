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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4ecec2c-3cb5-3f14-bb1f-5ab524d3ecfb | -17.82096 | -46.73469 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a97d5ba4-de42-357b-aa8a-48c45150a47b | -14.32856 | -54.12112 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e74913a2-6941-37a1-97ef-5e592364f44e | -13.21632 | -51.75778 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fdeccc07-26c3-3036-8f38-0df8624583f0 | -12.98801 | -48.00284 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96e7faa6-5a6c-3680-91a1-d59f43545ed2 | -13.36465 | -41.92614 | 2025-09-12 04:27:00 | NOAA-20 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0ff2ad4f-581f-3d9e-8fd5-8158e8a38c38 | -16.42094 | -45.68678 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d43bc5f5-be4b-330c-8713-637f4c911fac | -18.34768 | -49.32812 | 2025-09-12 04:27:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 092e9f29-0962-3545-b1ca-7700ee661393 | -10.3341 | -58.0213 | 2025-09-12 04:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656d1e47-7107-3a15-838d-b45e1322fd40 | -18.53878 | -48.40896 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| d3521634-4c6a-32a2-8cf1-6b3b1d7fa8a6 | -12.24029 | -47.3393 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d864e95-5580-37f6-9675-180592967153 | -11.95115 | -51.17648 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ee449966-ce94-3f42-9521-6043ba6ee1c9 | -17.76382 | -50.95242 | 2025-09-12 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e078608-73b9-31c9-b2e2-560447448885 | -15.44645 | -43.64277 | 2025-09-12 04:27:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3e7a6470-8063-318e-8b55-e66f62e7d0fc | -12.91489 | -54.77093 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29f1892f-8ceb-3a9d-b16f-75c30ae2f71b | -15.07444 | -48.01488 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c967893f-d732-3993-8c03-ef39320579e6 | -17.25401 | -44.48256 | 2025-09-12 04:27:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d05a5054-8a55-315c-a72c-6d9e602e88da | -13.89736 | -48.24407 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ec4a3a-f740-3908-9ea4-3ff7cd293f0e | -18.44656 | -49.55818 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac6275ef-e00b-326d-8210-aab4067c6ce4 | -14.37259 | -47.28866 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66da37be-95c3-39f3-841d-9e7f1a3a01b3 | -13.26974 | -51.71565 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 75ec7f23-89fd-309c-818b-f428b7629409 | -14.11767 | -44.31927 | 2025-09-12 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4674b953-8667-3dfb-a6d8-c5017c027598 | -11.95302 | -51.17937 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b5e58b28-430a-38a0-b7a7-c4f3e97186e3 | -12.56678 | -49.14376 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1657c125-de23-392d-80c7-a03fc959ef34 | -17.35876 | -46.69202 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a14b1930-c70d-336b-9808-9cf168c4c54e | -13.95546 | -48.19912 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50b3bb2b-4f57-3b53-8e92-cc23ae0caa9b | -18.05732 | -45.44014 | 2025-09-12 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54b0b646-6c9b-3a3f-8014-cec7c3de8c17 | -18.44988 | -49.55875 | 2025-09-12 04:27:00 | NOAA-20 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b219108-3a07-3899-8e6c-04025d688fa2 | -15.6034 | -52.73957 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdd6b1fe-f6a8-313a-973d-b7eb8ef17ac8 | -18.30194 | -50.4239 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a180650e-142c-3015-8243-a95572706e27 | -12.56183 | -49.1316 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f9648e0-24f3-3e6f-a7d0-1d810456bc48 | -12.89094 | -47.97303 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c238606-d4e8-34a4-9b22-0e1fa9ae0f6a | -19.62408 | -46.43776 | 2025-09-12 04:27:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 297b5359-58ff-3f5e-9f83-02eb39a513cf | -20.1547 | -43.68092 | 2025-09-12 04:27:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 53602cef-dc3d-3400-9267-5908e3c2e4a0 | -15.10778 | -52.45998 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93505698-841c-33a4-8d91-0233ea0f1ead | -15.68882 | -47.01534 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 594a08dc-aaa0-3344-93fd-a5aea70d1726 | -15.58007 | -54.76194 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25a0b2a8-8c2b-3765-a0e7-ab8c93181d0e | -13.91111 | -48.26448 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4954b57c-c917-3007-bc72-b81e21b0cea1 | -12.9328 | -48.00825 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec1ce18e-5729-3014-88ef-1e8806025bd0 | -12.80783 | -44.75657 | 2025-09-12 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db0cd81e-a9d3-3b9b-b62e-391fb454449a | -17.38005 | -52.95878 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 9652d5d0-4580-3d78-a22e-8ae71733954f | -15.65862 | -47.04583 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a20ef85a-43a3-3a8f-8e67-58b0e5a477a6 | -12.42717 | -47.79183 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf069ce-d5e2-3f64-bdfb-cd5fc0950f3f | -16.43395 | -49.03864 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c74d675-37af-32bf-8c5a-42d3f25561aa | -18.53822 | -48.41262 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| fe4d5d46-f0c2-36e3-855d-718bccda83e0 | -15.80799 | -52.21829 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95105241-89d1-3813-93a3-596822ee2c03 | -11.798 | -50.56925 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c45f28dc-1b02-3ed6-8cb1-25007261f1c4 | -12.92788 | -54.80286 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d757dc44-38a6-3cfe-a4eb-a2155cf3156f | -16.51342 | -46.85556 | 2025-09-12 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f174e6d4-e887-39c8-a0e8-6068f8edb0cd | -16.8139 | -47.82668 | 2025-09-12 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96cda7a8-ddfd-3e12-b214-cbfc5d5378f3 | -16.25782 | -46.78857 | 2025-09-12 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb3d7c79-66c8-3d9a-9ff4-b6e91bc7116b | -13.2655 | -43.74999 | 2025-09-12 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b972ccc8-40a4-31da-a6df-1b0754fa75aa | -12.54691 | -49.15927 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7fae826-d97a-36fa-8f78-72a2cf5ef693 | -16.05338 | -49.87926 | 2025-09-12 04:27:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f320dbe-36c0-34f7-b387-c577095ed173 | -16.43006 | -49.04168 | 2025-09-12 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95f734a1-2d5f-3cce-ba8b-555fb5327fb1 | -16.21195 | -50.82828 | 2025-09-12 04:27:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 514b6cb1-ccfb-3832-a5da-a475dff84d87 | -15.11554 | -48.09824 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8690eb28-8cfb-3fda-97d9-b95f1458cea8 | -17.77027 | -43.45437 | 2025-09-12 04:27:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1222df5c-b880-3aae-a3ac-4a1f1584525b | -12.47047 | -47.4955 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10fa99a8-7e23-30c9-81e6-53e68dd1e6f1 | -11.17628 | -55.05678 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 823faaf4-0bd8-366e-afca-e5ed3ce77223 | -17.81269 | -49.9861 | 2025-09-12 04:27:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d6c3219-e78b-3aaa-a542-426ae7e75fb0 | -13.27499 | -51.71473 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 51846474-3f12-319b-9d9f-4d38092f743d | -13.27641 | -51.72166 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 89200ecf-1fb2-30a9-a412-d9ac5ccd9082 | -14.12771 | -45.38063 | 2025-09-12 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bd8d47c-2404-3e6a-9337-075fe8426b49 | -15.52975 | -48.55116 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c333db91-ff71-3c01-8478-03dfbcdfc4c9 | -15.11144 | -52.45842 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0365633-177b-319b-a114-35bac4be21ff | -15.6795 | -52.23255 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bffd5c2-2ccd-3941-b286-4b8df96a3e8b | -11.59985 | -52.22842 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18e75d09-6000-3384-a33a-6f7d0766d6fe | -20.26917 | -42.11836 | 2025-09-12 04:27:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| fd20739a-aaf0-3030-b814-d1baba2dbe52 | -12.88049 | -47.9533 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6f66955-d0cc-3b63-b6ae-d3cb70a12456 | -14.16396 | -46.19594 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 420fd078-f168-32e1-94b4-9ce1cafd5a36 | -13.36431 | -41.92143 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2bb6e449-6bb9-3bc3-a726-1c443d423991 | -12.89923 | -47.96357 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2637ee5b-71ba-3cba-8fc5-7517d387c74e | -18.64959 | -48.14837 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 669dfefc-8781-3fa0-83cb-4dfb9ff7611e | -15.10858 | -52.45535 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a476c4f-98ae-3de9-b880-65d210ad4d7c | -12.96564 | -54.75446 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51cdc454-35ab-32d2-a06f-1faecd6b07e3 | -13.22913 | -51.75056 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b44a6da2-78e7-3dc7-af58-a75aa21c493a | -17.13157 | -48.4912 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f64bedd1-5cfe-3fa1-8d24-f88014f546f2 | -12.45998 | -47.49741 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31a92ec8-2a2f-31d2-b1ce-e750236fa76f | -12.24416 | -47.33631 | 2025-09-12 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea102a4d-caf3-3dc1-aa1a-d47429019037 | -16.28163 | -45.68125 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32b9c21f-d124-3123-ad46-4cafb49256e2 | -14.4728 | -46.35357 | 2025-09-12 04:27:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64582624-d721-337e-a699-2b82a9c2b5df | -13.97473 | -48.20524 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08b298d4-411c-377c-b286-aa4cfd38a59a | -15.91616 | -51.79567 | 2025-09-12 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0cf4366-ff56-3137-aee9-dc0fd5af9108 | -11.94565 | -51.17805 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0b9e5c4c-f4c8-367a-8e6f-ff702c9d3d60 | -17.81808 | -46.73018 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 404c5d71-5643-3543-b958-d6b1601cb4ee | -14.41009 | -52.92685 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8fbbf98d-1d8c-33a4-abd0-d7a9dd5637d5 | -13.31768 | -44.09076 | 2025-09-12 04:27:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4c2e9658-dacd-3196-8ecf-6a46766df1f6 | -16.43575 | -45.68486 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a163c514-65c5-37e1-b8d5-e6f2f42c6168 | -15.08141 | -48.03408 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 413e8a77-cc77-3fd1-9666-b97af2c30d8f | -12.84626 | -47.95488 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65099cb8-81eb-384a-8c69-972a05e731aa | -12.01065 | -48.54912 | 2025-09-12 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79e9c0e8-fa71-3f97-be49-7cc8fc725542 | -15.22355 | -44.0548 | 2025-09-12 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7898300-f146-35d4-8fab-58cd320471cb | -11.8767 | -58.82509 | 2025-09-12 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 310667a6-189a-3512-902a-e823803a353f | -15.09559 | -52.46263 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4b098a5-9381-3143-b641-9f0645502c65 | -20.15891 | -43.68121 | 2025-09-12 04:27:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 963fd121-5fe8-3f63-ad4f-6fd95ea2179a | -14.44804 | -47.30466 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6bbad24-b11b-39e7-af5a-023a5b803d43 | -12.84521 | -52.97166 | 2025-09-12 04:27:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fddf11a8-70df-38b6-963e-2f9371769b17 | -20.08301 | -44.48038 | 2025-09-12 04:27:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 29796ea4-7009-3c88-a07e-d030fa1436ab | -17.94659 | -45.27567 | 2025-09-12 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee3ad13b-e499-32a5-81f8-5df09d5e58a4 | -17.71885 | -46.14387 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README91.md)
