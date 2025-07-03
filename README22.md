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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b2ec3db-550a-3020-a534-d7d6e630ec9d | -13.22887 | -57.13406 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae11f483-e77b-31b7-b25c-13683b7f0bee | -9.79504 | -47.74953 | 2025-07-03 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e4400ce-a955-3bbc-9486-7a7973d6c9b6 | -8.49792 | -47.42296 | 2025-07-03 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 022ad01f-10c0-3704-a2a4-23eb7d76656f | -8.71946 | -64.17068 | 2025-07-03 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eec6aea-5c90-322b-9a4f-6c1477131a5b | -11.32775 | -55.2107 | 2025-07-03 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 259b6115-6b55-379c-97a3-2699f860dddc | -8.52964 | -54.77351 | 2025-07-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f929a8a-e96c-3b73-9c27-7894947c49ab | -11.85746 | -44.84809 | 2025-07-03 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f79853f-7ce1-3caf-8742-2a65d850ff9c | -10.8919 | -56.4554 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1d28789-7e3f-3843-bc81-4c2428d7cb17 | -12.16302 | -45.5318 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37134f79-51f8-3e1d-9cf8-db6a6f61e0fb | -8.43395 | -49.19976 | 2025-07-03 04:57:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76269a88-5ca9-3862-9af9-a2483f2c6185 | -11.65322 | -44.57748 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c72d5262-07d0-3f4f-8503-23df15579c9f | -10.77049 | -56.29953 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5ccd74a-6f7e-338f-ba58-4f35fe92382d | -10.30454 | -57.13328 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ca66c7e-0642-3919-9202-4fbabdd62def | -11.83843 | -47.55389 | 2025-07-03 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4b2603d-e2ae-30cb-814b-b3b84be75354 | -13.38695 | -47.84657 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c119b697-9510-303d-b311-16e6e9fcde65 | -11.63995 | -48.07766 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 292b16a2-41f7-3725-894a-f91f5500068f | -11.65971 | -44.59526 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 726c5e87-369b-3550-9ba8-0eb21a8596e4 | -12.01443 | -47.77556 | 2025-07-03 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| afc0cf43-9ef5-3381-8b3f-19c7626f07e7 | -10.30734 | -57.13761 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a687316-fab9-3452-b6dc-9d2c822951a6 | -13.3925 | -47.84203 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7af0d0a4-f53c-3186-a0d0-9d394606bab6 | -10.29894 | -57.12465 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87135daf-9425-3cbf-a70b-2ed04e396105 | -12.11156 | -44.98899 | 2025-07-03 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9497598-5d59-3b7e-afea-52af1f916428 | -11.47879 | -47.92667 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 257d1e09-d9aa-372d-9cdf-e0938112f5d4 | -12.43226 | -50.0285 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93a0796d-98c1-36d4-a00a-041bb1cb5653 | -9.62862 | -61.46649 | 2025-07-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33827b20-d955-3883-9f04-7a4f1ee2b2a2 | -9.83104 | -48.37281 | 2025-07-03 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 738d87d8-1de7-3fbe-b5c3-52f42a0ce7be | -14.6329 | -53.88307 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2908de0b-c49b-3078-b20b-4aa0d3222ac1 | -14.63348 | -53.87915 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0a2e3e8-8af8-3346-b8e1-0e28babace0f | -18.21675 | -51.3507 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5bd18cb8-8859-3dd0-ab39-414c0ff956c2 | -18.21209 | -51.35416 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 25363e1f-3743-302a-8fbd-e11d8302ddc0 | -20.76433 | -46.76839 | 2025-07-03 04:59:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 78800420-f6cd-383e-982f-41001bcf8451 | -18.20892 | -51.34567 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd885dc9-35dc-3a03-9a55-951d210616fa | -18.21725 | -51.34671 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dc723114-e758-3a47-bb13-baf59b7e1e60 | -16.07367 | -51.56359 | 2025-07-03 04:59:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 074d2d05-bfb4-3a26-bbf8-e1b31ffce71e | -14.63636 | -53.88362 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee4fa1d-2f28-3947-a97a-cc06dc3181e2 | -14.63983 | -53.88418 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 730160ab-647c-3732-bc30-033ed01cde59 | -17.90908 | -54.13955 | 2025-07-03 04:59:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ac615a2-dd34-38e6-8a4d-6a0e2632f119 | -18.65834 | -55.74066 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1206b922-4560-3a38-8579-36d1ad0b2af8 | -19.43889 | -48.55073 | 2025-07-03 04:59:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20f8e719-1ce7-3fdb-9603-2357e939c774 | -14.63694 | -53.8797 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b676f5e9-5d50-31b1-b029-9b8c504e01c1 | -14.77939 | -59.57193 | 2025-07-03 04:59:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff7e4f5f-48e5-3031-a209-f93e1519c48e | -18.20793 | -51.35365 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5bc510c-52e4-3735-a3b4-3eeb2f4c6fe2 | -18.21259 | -51.35018 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5748dc6e-6daa-320a-9b0a-a3d2f606e968 | -17.86138 | -44.56672 | 2025-07-03 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d4577d-5459-375e-8eb5-32126697f16d | -20.54198 | -48.75272 | 2025-07-03 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d5d871a6-1fa7-3702-8cf6-290d0a460c8d | -18.21359 | -51.34218 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d6ecd30-6f28-3a2a-ad04-d3022cde957b | -18.65554 | -55.73634 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0f0b844f-e06d-3c53-9b6a-198bf9136421 | -18.43016 | -54.55758 | 2025-07-03 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5bbc7fe-85cb-364e-b1aa-ffb94a5fa499 | -19.74463 | -45.96711 | 2025-07-03 04:59:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc1dc62f-f491-3a24-a365-34866c40e158 | -18.20842 | -51.34968 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1f90ef3-53e6-36c9-8b40-e4c535813dd2 | -19.37293 | -47.68879 | 2025-07-03 04:59:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3925c4-7f03-3e47-a1ce-ee025aee3316 | -18.65441 | -55.74387 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 92667a50-bddd-3199-9db0-e6efbc04ac9b | -18.40841 | -55.59237 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1499b106-7ff5-3dcc-b0a7-23c8b04eb19c | -18.40503 | -55.59182 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b55d1650-0d2f-3e5d-99c9-494d5a08bda9 | -14.78039 | -59.56953 | 2025-07-03 04:59:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 114736fe-3cef-3d97-8cd8-9ca5fa18ce99 | -18.37361 | -49.26783 | 2025-07-03 04:59:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8431aa15-a6a1-3da1-800b-ef2b842bfeb2 | -19.37055 | -47.68885 | 2025-07-03 04:59:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e92fe90-0b0c-3688-8fc8-2b7f5c6ee0dc | -18.21309 | -51.34619 | 2025-07-03 04:59:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7b3fb90a-0387-342d-a747-73c29cf39758 | -14.63232 | -53.88699 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 751401f4-0fb1-3793-8fee-14dc592167cf | -17.65567 | -46.83186 | 2025-07-03 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b8b0611-a76d-356f-be8a-72abe1ef20c9 | -20.5423 | -48.74955 | 2025-07-03 04:59:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d7e8dbea-9523-3449-b1dc-95c27eb8065e | -14.62829 | -53.89037 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d34ee1c1-97bb-3532-80c6-b9848ce74b2c | -14.63925 | -53.8881 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 021da917-87e1-3c4b-aaf7-ad8c14b138e2 | -19.37592 | -47.68958 | 2025-07-03 04:59:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02ee0023-402a-3df5-b663-670b1843e078 | -18.66436 | -55.7558 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 772dfe20-245e-3bad-b34c-d7e027c2010c | -14.62539 | -53.88593 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e828323-ade3-30f9-b71c-c610e3b5bd54 | -14.62886 | -53.88645 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b198a205-7126-3f8a-b927-5d57423d9a2b | -15.6797 | -56.08872 | 2025-07-03 04:59:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 363ffd80-ad2b-36f2-bc22-7c2e8b40e8c0 | -19.74511 | -45.96216 | 2025-07-03 04:59:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 690d256f-9e06-3e96-ae2d-3f0d640928d6 | -18.66492 | -55.75204 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 41de5e86-1d14-36bb-a504-7743c31bb079 | -14.63579 | -53.88754 | 2025-07-03 04:59:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e5a6a7-f764-3c96-9bf0-a33e27922767 | -19.40283 | -54.46324 | 2025-07-03 04:59:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69a74370-40db-3170-8d1e-515d2cba8be5 | -18.65497 | -55.7401 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9b552bb2-252f-3a5f-88c5-6b339777bb32 | -18.65778 | -55.74442 | 2025-07-03 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5dd69e7c-b165-34b5-b891-037532f664f4 | -6.9605 | -42.8816 | 2025-07-03 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 265.9 |
| 518bd201-268e-348c-a61c-de3777123854 | -5.9938 | -43.7366 | 2025-07-03 05:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5b7cdbbf-89af-3cab-b2d3-9dc79fe5f5e6 | -6.9416 | -42.8834 | 2025-07-03 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| c7957cf2-7a8b-3d29-b5bb-2cf954914ec6 | -6.9793 | -42.8798 | 2025-07-03 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 60fe1d73-df9a-3e99-aac0-e85165ba7863 | -6.9602 | -42.9052 | 2025-07-03 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| c3d432d5-2a0f-35cf-94b8-76709452ee5e | -21.61596 | -57.55969 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 008667b6-736d-3998-a180-050769e69f3f | -20.72679 | -56.65283 | 2025-07-03 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5bd462ff-977a-3dc7-ac6e-c01a811084b6 | -21.88774 | -56.11212 | 2025-07-03 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 783ec9dd-b709-3b72-8a55-6939230d46a1 | -21.70273 | -57.67749 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a4f371a-f852-3c99-b0c2-467b704e4465 | -20.72288 | -56.656 | 2025-07-03 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0d7ee911-045a-36aa-841a-422ef017b83e | -20.72622 | -56.6566 | 2025-07-03 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 15ef4c77-0145-3fc1-b425-d77e9f26ac2e | -21.61091 | -57.57022 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00f075d3-b180-30df-8a9a-1e2aa98ed314 | -20.79189 | -55.79071 | 2025-07-03 05:01:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 127525de-3e37-3702-a9c9-30f3f20d3f74 | -21.68974 | -49.50173 | 2025-07-03 05:01:00 | NOAA-20 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c3117598-e87d-35dd-bae5-e3356bd31c7d | -21.95436 | -57.58825 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa2c7552-92cd-3845-a23d-226550d66d3c | -20.70549 | -54.8908 | 2025-07-03 05:01:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 584cf062-ae69-357b-b83c-6db82dc1a53f | -21.88717 | -56.11604 | 2025-07-03 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c460fe6-9927-3f81-b5da-7ac54af1c70c | -21.95494 | -57.58454 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 239a484c-1942-3f14-8bfa-39274ee1a784 | -20.72345 | -56.65224 | 2025-07-03 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb595130-0540-3e46-8047-e597c995854f | -20.73013 | -56.65342 | 2025-07-03 05:01:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae7d48ff-3122-355c-b306-4fe25de8af66 | -21.12628 | -57.52028 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| df2da0e9-99a4-35e6-9ffc-fa6d85cf7cde | -21.89694 | -56.7387 | 2025-07-03 05:01:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96232ac8-b392-3b78-9dd4-e7e092c6ac32 | -21.61538 | -57.56339 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 531ace84-50e2-38fc-9e13-0a3eae508e46 | -21.6148 | -57.5671 | 2025-07-03 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa9c806b-2808-31b7-83c3-98deadabc4c1 | -20.20691 | -56.61616 | 2025-07-03 05:01:00 | NOAA-20 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| e832fdd8-2ee4-386b-8b53-2a218267f782 | -6.9793 | -42.8798 | 2025-07-03 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |


[Clique aqui para ver as próximas entradas](README23.md)
