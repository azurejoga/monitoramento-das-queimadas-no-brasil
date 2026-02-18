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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 609428e5-2bf8-3749-94d9-88cb5dc88c4a | -11.1187 | -46.60784 | 2026-02-18 03:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de8233f8-4249-3077-bdde-9a93d3391f6b | -14.41879 | -44.59278 | 2026-02-18 03:57:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eabcfb5f-c8ab-32f7-88e9-1bccda751f34 | -12.48605 | -43.6491 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fd9636ca-51d3-356c-bcd0-d6f21b01e8bb | -16.25604 | -39.06278 | 2026-02-18 03:57:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1161ada3-4d72-38ea-bea8-32bf38c1645d | -13.01253 | -45.05486 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7e33217-b7de-3430-a1f5-45ecaa67462c | -15.41578 | -43.68459 | 2026-02-18 03:57:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 473d041a-3929-3fd6-9404-26462d0bc2ee | -11.88236 | -45.28438 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59736a2a-d642-32df-afa4-0f5c3be1d5d5 | -16.48146 | -43.76724 | 2026-02-18 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44742234-c433-3d50-a266-47c8fb3a930c | -14.41499 | -44.59211 | 2026-02-18 03:57:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae3a47a-0e3b-3078-a3b1-7b25818ea540 | -11.88322 | -45.28894 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11df39c6-ce60-3fbc-85d9-6d364b83059c | -12.60186 | -46.82997 | 2026-02-18 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 703df533-210d-3f92-9a35-a4bce177e7ba | -12.42891 | -47.88139 | 2026-02-18 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9374e51c-0aab-33e7-bcc9-26b1186f9698 | -11.8865 | -45.28504 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab1f9d0b-38c8-396c-ab16-0f037d8a32ce | -11.89475 | -45.28648 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74e7d603-1e56-3b3b-ad62-daea7505d6f0 | -14.36227 | -44.56086 | 2026-02-18 03:57:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22fef8bc-5262-3109-b577-bff83b1a1f26 | -11.11412 | -46.60711 | 2026-02-18 03:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5dfab2-128b-338d-8c79-6784df570c28 | -13.02371 | -45.04965 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b736e77f-c8da-3cda-a330-ee6c79facf0f | -11.85991 | -38.20309 | 2026-02-18 03:57:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf0698fd-c8bc-3b91-9595-83b374900d73 | -15.67653 | -40.88708 | 2026-02-18 03:57:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2111a09d-1411-3d5f-8062-338ed97bb5bc | -14.86097 | -43.85133 | 2026-02-18 03:57:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a1a1ba7-e55f-3a44-bb27-f2e80c97e2c9 | -15.59344 | -42.38851 | 2026-02-18 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87e4cee9-6f7e-30f2-b7e6-9f50a349f279 | -11.88719 | -45.28123 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24dd8ea2-d886-385d-a258-0a503936f995 | -16.79265 | -41.52972 | 2026-02-18 03:57:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2dad1b1-3108-3755-8afb-db5d944e19c7 | -11.88521 | -45.27745 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 738425dc-e377-3952-ad35-dfe21194ade5 | -16.68242 | -41.36645 | 2026-02-18 03:57:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 91237857-8151-34c1-825c-e873bdc260a3 | -15.18172 | -52.30231 | 2026-02-18 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 449a26eb-e3f1-3ee6-aa70-78c55ab08bcb | -11.88389 | -45.28509 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ceef511f-25d3-399a-a223-7c8754c2986f | -12.4831 | -43.64394 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9322afa4-acaf-36a8-b39a-ae31db63730b | -11.88994 | -45.28956 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e2e6b84b-bb64-338e-a31b-0792a5af9694 | -13.01974 | -45.04887 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 512acbbd-1c4d-362d-9df9-928f3a7ec99c | -11.89407 | -45.29029 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 09b2b2b9-40c6-3030-bfa6-f2d6cf0a3606 | -12.48848 | -43.64773 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 12b4d6aa-11be-31fd-b648-67e803ac4045 | -12.49218 | -43.64838 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 00db662f-4c2a-31de-9bfe-3105b2cc9cf1 | -12.81629 | -44.83517 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a798884b-957e-3f9b-9db4-896f422b17d7 | -13.01846 | -45.05596 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2872fde-fdf8-33b1-98bc-256d857199b1 | -13.0132 | -45.06232 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc51c2f9-e0f5-3d9f-8622-90422da7a70d | -15.31816 | -42.05278 | 2026-02-18 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 38b66da2-3b14-3008-bcf1-c5cddb6547bb | -17.83579 | -40.40848 | 2026-02-18 03:57:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1569055-eb3e-3d95-9358-1f306a9513d9 | -10.93197 | -44.66611 | 2026-02-18 03:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6803a923-4d70-38ab-bbd5-a866bad5f126 | -11.89131 | -45.28195 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75c3dcdc-f171-37a8-bd2b-43dc07a2bce9 | -11.88581 | -45.28887 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ed75d4e8-389b-314e-b12a-ed8d2baee910 | -15.38285 | -40.8487 | 2026-02-18 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 64f8e715-74f3-3df9-8f2f-e654ae68f5cf | -12.81809 | -44.82478 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 023a1165-559e-3fa9-aed4-d0cfe472735d | -13.02308 | -45.05319 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3f5abec9-3d8a-3178-9534-ad4c01842cc4 | -14.98527 | -39.3549 | 2026-02-18 03:57:00 | NOAA-21 | BUERAREMA | BAHIA | Brasil | 2904704 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b39bcfd-eb74-34f4-9262-5bd53b36c1a4 | -12.25409 | -38.32379 | 2026-02-18 03:57:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6643448d-1960-39ac-b27e-6afcb0a4fbbc | -14.51251 | -43.62621 | 2026-02-18 03:57:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d617dd3c-4f34-3da1-803e-a1de5f75d832 | -12.90969 | -41.51175 | 2026-02-18 03:57:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e16339e-2724-3ad6-bd73-bdee79271f4d | -15.42062 | -41.44343 | 2026-02-18 03:57:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 252b4714-af4a-33e8-b1f1-5dca638f802f | -11.89063 | -45.28575 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89ea3f7b-ba2c-39b1-b2ac-40af8d6624e8 | -17.62875 | -43.92843 | 2026-02-18 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5648d03-45d1-3ef3-85e4-37f15983cdf6 | -13.01511 | -45.05169 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dfe39cde-c659-3317-8d05-cefc12e0cb49 | -13.01447 | -45.05523 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0ead15c7-0f7e-3e2c-9349-5531c863cfcc | -13.49601 | -46.70947 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757e937b-6d23-36cd-b80d-8330d2aefeb9 | -15.38672 | -40.84568 | 2026-02-18 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1759c067-65a5-3883-b274-7d78b8b716fd | -15.55505 | -41.79036 | 2026-02-18 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cd11de47-4811-3c38-aa7c-a39980c0f8d8 | -12.81324 | -44.82925 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b61cdd-aed0-3b3f-91fb-2d29a9da2fd1 | -16.64362 | -48.49361 | 2026-02-18 03:57:00 | NOAA-21 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cada4098-0498-354c-83eb-4088c4111561 | -15.31755 | -42.05651 | 2026-02-18 03:57:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 25e56dbf-c97d-3aef-bf21-4001c8a67c17 | -12.42407 | -47.88042 | 2026-02-18 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adefb423-465c-36bb-8322-fb134777a08c | -13.01191 | -45.05841 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30629455-eaa8-3a5a-9c50-ed56b73a526b | -12.81719 | -44.82997 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 364d0768-2391-3186-a75e-8d601b7cd259 | -12.4868 | -43.6446 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a7f34804-fc5d-3799-95da-a70878332a27 | -11.89544 | -45.28268 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68b39be9-288a-30b1-99a0-283b71a5051c | -11.88374 | -45.27675 | 2026-02-18 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e2d2558-254b-3e8d-b81f-77932fe09a47 | -12.69091 | -46.69901 | 2026-02-18 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 33811ad6-0b71-3af2-ac7d-bce4e59f49ee | -12.14983 | -38.06604 | 2026-02-18 03:57:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74adfb2a-5518-3862-87be-fba77fbf4a90 | -12.25072 | -38.32326 | 2026-02-18 03:57:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 461d0fed-4202-3102-9551-8e6380e1d4a9 | -15.38342 | -40.84513 | 2026-02-18 03:57:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 10596b34-5997-3382-80ce-e8cc08947a81 | -15.57936 | -41.45177 | 2026-02-18 03:57:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 61524c11-5e32-3a23-a959-c0a17697b22b | -11.82348 | -38.24957 | 2026-02-18 03:57:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5a87ba48-c303-301b-8c85-9d00c33c7f1a | -16.48745 | -39.86747 | 2026-02-18 03:57:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b4d37b3f-0668-3774-be44-984d9c309a1c | -13.30667 | -44.2929 | 2026-02-18 03:57:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 921aabdc-c46e-304f-ad60-caf0f5cca9ea | -12.48769 | -43.65223 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2b18d588-12db-3b69-8de6-a0abf679cbe4 | -16.68573 | -41.36699 | 2026-02-18 03:57:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 873f869d-bd43-3ed9-a62d-3c37b349bcf6 | -11.71178 | -44.73362 | 2026-02-18 03:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a55be791-8756-383c-9f63-285339f12437 | -12.48975 | -43.64975 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 87b32c89-1904-36b2-bdc3-daedb9e8ce8c | -12.46859 | -43.72998 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 740d9136-7f41-3500-ab0e-0b68e2995740 | -13.0191 | -45.05242 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7bb82f96-b64b-3b73-8ee9-d9c62f745961 | -12.81415 | -44.82406 | 2026-02-18 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bc97495-fdce-39f5-9565-7902e0a7dee3 | -12.45286 | -43.62006 | 2026-02-18 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7cd8b1f-913b-3dc4-be56-1d72be7152f9 | -10.77012 | -45.01422 | 2026-02-18 03:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d69455d5-7fca-314c-8c19-1ed7cfb2db68 | -18.80579 | -51.60979 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebbf2cb1-fefa-3454-9fbf-44d903c1697f | -18.81271 | -51.605 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aeb0f64e-0111-33a8-84ae-ad0c7243908f | -18.81188 | -51.60878 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47cf45ca-9539-3b11-bf0d-754a80f674af | -17.62368 | -46.66256 | 2026-02-18 03:59:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4a76615-6013-3927-a783-eb26b7a34cef | -22.78684 | -42.98451 | 2026-02-18 03:59:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6e41f214-627b-3336-b7c1-db0eaa6e45f1 | -19.11532 | -40.59754 | 2026-02-18 03:59:00 | NOAA-21 | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d2653afd-7e4d-3d77-bf7d-80d1c805d0f4 | -18.51795 | -44.55245 | 2026-02-18 03:59:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b5dfd23-05e4-311d-9f56-620f9e4a734c | -18.52077 | -44.55749 | 2026-02-18 03:59:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6a0ec39-4bfc-384a-9fd9-5558a030e123 | -18.97944 | -49.80366 | 2026-02-18 03:59:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bf0ea77-8811-3b8a-a733-fa6fa7951417 | -17.5621 | -50.44055 | 2026-02-18 03:59:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ad24c46-575a-3376-b151-66ae2c713db6 | -18.8121 | -51.60703 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76eb71ec-ccbc-38e4-ab23-3f97edcb2370 | -18.70234 | -54.98815 | 2026-02-18 03:59:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f6ecfd3-d7ac-35d3-9670-48f250d245f3 | -18.76175 | -48.56257 | 2026-02-18 03:59:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d160a38-b20a-3130-a549-2ada8b6e3005 | -18.80659 | -51.60599 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbaa33f7-3ca3-345a-b081-a6847df6406e | -22.51147 | -43.14902 | 2026-02-18 03:59:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74a09fb1-bab1-35b5-9e68-ce4f85551943 | -18.81129 | -51.61082 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e590fa8-a481-3761-a8b4-546304013813 | -17.62684 | -46.66283 | 2026-02-18 03:59:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 455b23fd-3a5a-31eb-b41a-d447e1a67948 | -18.81105 | -51.61256 | 2026-02-18 03:59:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
