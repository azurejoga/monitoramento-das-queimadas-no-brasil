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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40297e74-67e0-32c6-9ad7-6c858d0dd306 | -13.3232 | -54.37412 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42951d2e-c493-3e8f-860b-7fa350b31493 | -13.26627 | -54.35189 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc011eb9-5a22-30c2-8fe1-dadcbb1b9cc3 | -13.26469 | -54.22999 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14f344b9-ad00-38a8-93c9-47c7725b5d86 | -13.25908 | -54.3506 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43e1bbd8-f9b5-3a22-af66-42aeedcde0eb | -13.25466 | -54.2239 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 982c24ac-c0d1-3733-b575-74ffce17c825 | -13.26122 | -54.33794 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07cf8e57-0532-3744-b02a-2aff54687db2 | -13.28802 | -54.34152 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 839e32ce-4fb0-3d84-9b1b-629992db4688 | -13.54109 | -52.91314 | 2026-07-07 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0f98206-3c01-377b-9213-4d3c824e00ad | -13.08784 | -48.16651 | 2026-07-07 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33d11baa-ac59-38a2-ae49-585c4bca2daf | -13.31961 | -54.37346 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 212fe624-a975-3715-b4d7-2aaa3901ca41 | -13.27184 | -54.23127 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73c87ccb-db5c-3ca2-9b04-e8afb82b5424 | -13.31674 | -54.36852 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3cf0584-6d44-3b08-b9f6-5aadadf6df3b | -13.2684 | -54.33927 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4aed2d31-6648-3610-8235-670a3d6b3438 | -13.32107 | -54.36493 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23c36312-b97f-377a-af6b-4c7434e2ab12 | -12.84156 | -58.30638 | 2026-07-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dee4b9b-c5d1-32e4-9f15-4c4cfd33ab7b | -13.08428 | -48.166 | 2026-07-07 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f49db534-3ba4-30fd-a52a-20f0573594de | -13.29375 | -54.35123 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d6f7fa7-79aa-30d3-8cdf-a8d7a5708640 | -13.27347 | -54.35323 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d377d208-5531-3d31-9b82-07efc8b5b51d | -13.32034 | -54.36919 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38b86768-8d08-3307-9ad6-0d1e886501c6 | -20.52562 | -43.97203 | 2026-07-07 04:46:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 84ce9e68-9f73-3b43-9ef6-2f4602a5810e | -13.28208 | -54.34608 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 667c8246-f52e-3d50-9890-c26132b00bc1 | -13.29 | -54.39445 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a7ac970-b7ac-32b7-896e-80d3cbfdca00 | -13.2569 | -54.34151 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03a5ea5c-32b9-329b-a4c4-09fe740e0c7a | -13.27276 | -54.35743 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17212799-4665-3e2a-bad0-a94032ab9bd3 | -13.32753 | -54.3705 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb964121-232d-3191-b07f-51c8ce514e19 | -13.27716 | -54.36137 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30097c8e-dd09-3476-8145-9d0aa41d46f2 | -13.28368 | -54.34515 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d684afd0-3c16-3396-836f-13be570eec2a | -13.31461 | -54.35931 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d81a42e-e5e6-3a90-9020-784ed64c0800 | -13.07657 | -48.16898 | 2026-07-07 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 663b72fd-0af7-34cf-b696-3c324eefe1e2 | -13.31601 | -54.37278 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87a0aeeb-92bb-3b75-9dbc-59ac721a2201 | -13.2605 | -54.34215 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 377ad75c-7cb9-3a4f-85ec-73331431c97a | -13.27853 | -54.36721 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f0b429f-4a0b-3899-8a0e-5b1ac0e5059b | -13.27861 | -54.35297 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89cb4446-0aa8-3570-8a23-8374882a6be8 | -13.78971 | -52.72654 | 2026-07-07 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbc85ae0-b37b-3594-958a-1ad3f6ae7979 | -12.84617 | -58.3073 | 2026-07-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07592252-9314-3c71-8308-72ee194d3acc | -13.54449 | -52.91372 | 2026-07-07 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6bbd411-793c-353d-8a7b-accc1005bfa0 | -13.28137 | -54.35032 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77cdcf6c-5d10-3f07-857f-965a0baf54c4 | -13.27356 | -54.36071 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce44f372-c03e-368f-87f2-8e2df745de39 | -13.32248 | -54.37838 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e34b005-5c34-3650-b2ea-2bae0e3d691a | -13.28509 | -54.35845 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39b2b979-820f-3526-80e9-98e750be98ad | -13.30023 | -54.3567 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d5d784e-a644-35fe-9485-391a8aab7f90 | -13.26827 | -54.23063 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ff89a22-27df-3c44-a835-99911896efc7 | -13.26339 | -54.34702 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4252b4c9-90f2-31b4-a87a-018837e4e448 | -13.28081 | -54.34031 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 135a2a19-af87-3eb7-8365-a8dbaf1a662e | -13.21077 | -54.37272 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ab990cc-7f42-3633-9ace-2254ee2207a5 | -13.2799 | -54.337 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16bee99f-3dcf-3437-b77a-9c8fd1f09836 | -13.27129 | -54.34415 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3547e47a-412c-354a-be66-1a702718af6f | -13.28222 | -54.35361 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc3566db-50ef-3899-bf9e-be1e12f37d16 | -13.26769 | -54.34348 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 760d6af9-7c97-3c67-9ea4-5d66c3097fcc | -13.31102 | -54.35864 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cca31861-e560-3e4d-8142-5b9baa173966 | -18.55003 | -46.82004 | 2026-07-07 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5613e87d-645e-32df-aeee-2e372fcbe6c3 | -13.31821 | -54.35999 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b786ea35-2c59-3c07-93c9-08c5e210dc13 | -13.25762 | -54.33729 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb9fafb6-4fe6-3449-9769-c3ba3ee3a28b | -13.28942 | -54.35486 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a18a68-a6fa-32b8-9fdf-20d7a5a72a1b | -14.18497 | -54.71111 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00c486c7-1eb3-39f1-87b1-03708269baa4 | -13.30163 | -54.37011 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3221300-2c45-3499-9c19-a3f747502f26 | -13.27205 | -54.36164 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eba825a-5e10-3572-b00b-1aeb6700bd33 | -13.30831 | -53.34263 | 2026-07-07 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c06ad762-48fa-3b8c-80f5-82458e30780e | -13.2835 | -54.3376 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f86ab2e8-46d1-3ca5-9cfa-9b27da949493 | -13.29302 | -54.35547 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1eddea64-dc14-36ed-870b-2f38a3e09ba0 | -19.85072 | -49.07375 | 2026-07-07 04:46:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b16f9988-2077-382b-b279-b7e484ee002a | -13.28422 | -54.33337 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 525fbd0e-1e6e-38cd-9f31-11b81f756cce | -13.29736 | -54.35184 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e09655e-33ae-34d1-a69b-b714aafded69 | -13.27418 | -54.34901 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13278531-47d9-3591-baa9-112610de2256 | -12.93167 | -56.6271 | 2026-07-07 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 714cf052-bd6b-3bbc-b8c5-c6e5851c2697 | -12.93512 | -56.63166 | 2026-07-07 04:46:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca90528-9274-3779-b54f-af32102df2d5 | -14.48482 | -47.05725 | 2026-07-07 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d80e5079-31f4-36b4-bd84-fbfbf3182cbf | -13.32681 | -54.37476 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57e58033-9471-38a3-af29-7de7e7372466 | -17.65054 | -46.41447 | 2026-07-07 04:46:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e8960c3-ab78-3046-b617-f710eb9a534b | -13.27995 | -54.35875 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5d8284c-443f-355e-805f-11e33e1e9ac8 | -13.26481 | -54.3386 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9756cd21-b96e-3a59-87e7-0899ca958e54 | -13.28066 | -54.35454 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcdf27c7-f156-337c-b5d0-197652512950 | -13.26111 | -54.22935 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5660f9c-a30c-35af-9a82-d4b0f27a5a9c | -13.2202 | -54.31765 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f12b43f7-ba30-39e2-98ce-2766dcaeb230 | -13.59954 | -56.61435 | 2026-07-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffa45136-8219-3a70-9d88-9ac9d13e765d | -13.28008 | -54.34454 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1be60072-f737-3053-9e28-abe2e7adf209 | -13.5377 | -52.91255 | 2026-07-07 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0693c6b-1cdc-3d96-9608-a0f73a4681bb | -13.27636 | -54.35809 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d722381-e4ed-3ba6-84e9-be6e59e09bd9 | -13.29015 | -54.35062 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4675899-c28c-3b81-9dff-cc76a173e89a | -13.27925 | -54.36296 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2be075c6-3189-3c43-80d1-432698199401 | -13.2763 | -54.33637 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bd3fb67-865b-3c40-8974-cb0d2b379322 | -13.2654 | -54.22581 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25ae55ca-ed0e-36c5-af67-9ab5c173a613 | -13.29662 | -54.35609 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fafd76e1-6361-3766-905e-1990c586954c | -13.27919 | -54.34124 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7bac6bc-8b94-3c7b-b781-182cab9cd1fc | -13.28728 | -54.34576 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fe50901-1cf5-337b-b243-45a42385175b | -13.27642 | -54.36559 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f308f176-4ccd-3608-9ebf-5c25252e935c | -13.26987 | -54.35256 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504ea939-1b81-3990-aa3f-b2bd8082c16a | -13.29162 | -54.34214 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5580ed3c-56cd-3397-8bd9-2015fb9e891d | -13.27058 | -54.34835 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49fe719a-9cc7-339e-a55b-31ec6965eef1 | -13.28149 | -54.35781 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd96e77-793f-3398-9a99-c748b8421693 | -18.09306 | -54.02538 | 2026-07-07 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e42879fd-ed21-353e-b566-3a45a14438f9 | -13.2274 | -54.29723 | 2026-07-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e269b5-ec91-32ba-9fc7-3a441db76334 | -18.08967 | -54.02475 | 2026-07-07 04:46:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cd8b425-cafa-39f9-bc4e-213d41a3698c | -23.8218 | -49.024 | 2026-07-07 04:46:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5a87af1-37b2-36f3-ae33-efaa2dee5f03 | -23.82568 | -49.02448 | 2026-07-07 04:46:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58635721-edf6-30c1-b94d-d239150e4bcc | -23.56641 | -47.5143 | 2026-07-07 04:46:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 26784fb7-d3ac-350e-a1b5-bee0f1dc9e2e | -23.5622 | -47.51366 | 2026-07-07 04:46:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4a97cc0d-2193-31d4-90be-84fca412c51b | -21.44929 | -47.90315 | 2026-07-07 04:49:00 | NOAA-20 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3731c0a5-73ab-3c43-aa87-c9a18345b83c | -22.027 | -48.2257 | 2026-07-07 04:49:00 | NOAA-20 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34f58504-5f27-3be1-a01e-b63cb2464a5b | -20.71186 | -47.2897 | 2026-07-07 04:49:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README20.md)
