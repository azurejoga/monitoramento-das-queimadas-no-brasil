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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28e6b69d-db6d-3731-a301-46805f4b6fbf | -11.79521 | -47.33411 | 2026-06-03 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8119ef5d-7eb1-3868-86e8-daa9b070f86f | -14.08751 | -59.3791 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9862d1bb-add1-3ae3-a132-147f00d6b1f0 | -16.17911 | -58.47879 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ecc29c09-16bd-3447-910c-ae2d0bdd496a | -10.903 | -54.13353 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6d69aac-185d-35c9-b20a-5b31e9cdeacc | -10.85616 | -53.74136 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 477dd309-0f15-371c-b278-a249eca05524 | -11.5682 | -54.58491 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4eecfd1b-4043-3318-b043-361a90914c41 | -16.59924 | -58.23524 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6de72a2b-a99d-32b7-83c4-8ec4067d2c34 | -11.26926 | -53.96836 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e1eed11-7250-370a-82ef-ecef699ddf05 | -11.79814 | -47.3349 | 2026-06-03 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2032a02e-ab3e-3fbb-a239-c80a9911e623 | -11.20825 | -54.98977 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b681b6c-b4ba-3dcf-952a-3892790ec31b | -21.29218 | -56.10565 | 2026-06-03 05:23:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d8315dc-10d2-3916-82cc-99d91d26b0f7 | -12.73765 | -54.20198 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b15c460-4626-3606-a6ee-062cd4fb1e45 | -10.87039 | -53.73461 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86b637a4-244f-30e1-9a78-500b480ef1be | -11.62417 | -55.18658 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98874eb2-5dd1-3408-a5a4-aeaf45485177 | -11.57353 | -56.33891 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35324bae-f77e-354c-bf21-8c60b2ed5578 | -14.08695 | -59.38279 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed3a154-e312-370f-8268-7ee642254a3c | -10.81717 | -56.59459 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1615340-eced-359b-a14c-832de6a09bd9 | -12.72963 | -54.20831 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcab88fb-0d0e-3579-9bbf-eb8fcd0bf1ff | -11.57791 | -56.3349 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63344123-2624-3879-ac4c-e2b275911ba9 | -11.87685 | -61.04559 | 2026-06-03 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01fdd2bc-32bd-3584-93ee-1535f8aae9d8 | -12.61742 | -61.99099 | 2026-06-03 05:23:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc7b4801-6ef8-307c-9f18-3c55551d5abb | -11.4345 | -54.0914 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59b5da75-6129-3497-ac1a-73b1f203b6e1 | -10.56986 | -57.31783 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99da7fd8-e479-3acf-82db-175dc12289bc | -16.90571 | -51.85532 | 2026-06-03 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6272641-6c47-379b-8796-6a0b84e76eba | -11.27357 | -53.96899 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bfce52b-75e8-3dae-ac04-2981af1617b5 | -10.85502 | -53.74998 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f7e9f33-76a5-30b0-9a15-27dfdbccb618 | -14.08639 | -59.38647 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98d4ba07-542f-37a4-81ce-2346d3091f6d | -10.85979 | -53.7386 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1730c2c1-28c2-30dc-9b2d-6e34a6c43056 | -11.88915 | -57.83884 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1d5fd0c-ca2c-331d-ab47-3478403e26f6 | -16.91682 | -51.85355 | 2026-06-03 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef6b7085-d75d-32cf-8b4c-4bf4302c06b3 | -11.63028 | -55.18373 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e7cd80a-d4c2-3db2-99d3-f74c7d3d072f | -11.62918 | -55.18013 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fbd7696d-18e5-3c2d-8a72-5f8ff390e618 | -11.87742 | -61.04203 | 2026-06-03 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2927be5-6220-331a-86c8-5254deb1edd4 | -14.08414 | -59.37856 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38659b49-41f0-3cb9-a714-c19e6ef9b1de | -16.91107 | -51.85624 | 2026-06-03 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f623384-1203-31ec-a756-51951001f2dc | -16.14088 | -58.49379 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 42257edb-092b-3ffb-b268-eed1f32dfb15 | -11.57546 | -56.341 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 307cd8da-4b63-3018-8f07-55e86fdcaa10 | -11.57418 | -56.33435 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f51b792-f973-34e7-978a-502cad11d41a | -12.73994 | -54.19701 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 787fa657-890f-38ad-9c47-96450c65b6fe | -16.14499 | -58.49022 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1b358fad-f2c0-35a8-b1c7-6ecc3a137bb5 | -21.69685 | -48.41426 | 2026-06-03 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a85fb164-ccee-36f2-85c9-11eacfd0c77d | -11.62969 | -55.17659 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b46cf3f7-6fbc-3b6a-9ca8-1c75ff405f95 | -11.63125 | -55.17667 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63ecb542-c327-33e4-8d2c-e65a0afaaf87 | -16.14147 | -58.48968 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 9ea615cc-e092-3372-a3d9-d7def7944c69 | -11.62817 | -55.18716 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01256847-e73d-3a5b-b4a7-3f5accab7ef8 | -11.32295 | -51.39259 | 2026-06-03 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46514575-ba0e-3a6b-abaa-39139dc0a839 | -10.59626 | -53.47321 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0470acb-63fa-345f-9c91-1a26bb591b08 | -16.1797 | -58.47471 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 841181c1-0c61-35fd-b900-af6989d0f5cd | -11.62067 | -55.18249 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60d86e5b-760a-363f-b836-4df12e5e3d58 | -21.81711 | -49.12702 | 2026-06-03 05:23:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 69567139-2f97-3f5d-a280-b7bd96e6e71d | -11.26696 | -53.96891 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09e98098-0740-347b-a6ce-f797105f8129 | -21.70247 | -48.41385 | 2026-06-03 05:23:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9c58be8-3a98-35e4-8946-eefae625f5db | -11.6344 | -58.24651 | 2026-06-03 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a0f7d2d-2d35-3f19-9e21-63616342ef99 | -11.80957 | -57.35871 | 2026-06-03 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5247273e-1d2c-3a61-bde4-b891710a7ed0 | -11.79747 | -47.34083 | 2026-06-03 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ad5a21da-7ad5-378b-a102-1a7c5087cd8d | -11.57184 | -54.58924 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd87e4f9-a348-3eca-9c06-1124eab48bed | -11.63076 | -55.18021 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 369dfe01-0b39-3f79-9ebd-b282db3cf0d7 | -10.04126 | -60.43618 | 2026-06-03 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a0d34c11-ae9c-3ebb-9dc3-d8e71de7071d | -11.62118 | -55.17896 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77d21c9c-c897-3146-b2ae-264294cc5e01 | -11.5768 | -56.33191 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1630099b-01aa-30dd-ba36-802c2bd0fbc2 | -10.81352 | -56.59403 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92dfe78d-5ca7-33ff-91ba-c356dc5a87f7 | -11.75657 | -47.07702 | 2026-06-03 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| cf172a87-d1f9-3856-a8df-0b0a391ae5e3 | -11.57613 | -56.33646 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f01a89bc-99b7-3c80-8468-08e251ca5e87 | -21.81758 | -49.12083 | 2026-06-03 05:23:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0104dbee-a4be-32bd-9f91-1b6308d45768 | -11.56926 | -54.57732 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abd49716-5e0d-38c8-9a9c-472b1e94a67e | -12.43727 | -58.39901 | 2026-06-03 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f97053a-99b7-3854-99e1-641dee427b9e | -11.26495 | -53.96769 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54feb7a7-f4b1-31a8-93c4-df6b37f49131 | -10.0337 | -59.34833 | 2026-06-03 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d7e0880-33fd-306f-9778-8d27633eeff8 | -11.63173 | -55.17311 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d78c1ec-07a5-3fc5-8381-4f59bcc22b52 | -11.87799 | -61.03848 | 2026-06-03 05:23:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b1e4c92-ca3e-3530-bba1-9c7350065bca | -16.14793 | -58.4949 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 361e6e9c-5b5d-3fc8-9f5b-337ca39928e2 | -14.02856 | -56.79717 | 2026-06-03 05:23:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28705d1c-f5f3-302d-988e-59e60657b76e | -11.47809 | -57.10693 | 2026-06-03 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70d1880c-35a1-3b83-872f-5354f391cd58 | -11.26451 | -48.36218 | 2026-06-03 05:23:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 257eca99-1a54-3a93-9109-ba7e60980f15 | -11.32335 | -51.38949 | 2026-06-03 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cc85a4c-0ba2-36c2-a1d7-e3dcadabc59c | -11.63496 | -58.24274 | 2026-06-03 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bcdc09b-8245-3f7c-a0fb-51a2f9dfe1ad | -10.86052 | -53.74199 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91f50657-9d21-341e-866a-e23b539c5b26 | -11.57482 | -56.3298 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fedcfd5-de94-3a22-98d1-13511e57dcff | -11.79413 | -54.01962 | 2026-06-03 05:23:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 394f0fff-4851-3c92-893a-fbb6a399e49b | -11.57727 | -56.33944 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c48e5540-6791-389c-8a24-ae1370131c45 | -12.80567 | -54.86504 | 2026-06-03 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1f9eb8c-245f-3b7e-9859-659d178b6a70 | -10.72649 | -56.04612 | 2026-06-03 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 959da4b1-b4d4-3eae-80c5-cc8e3c145262 | -11.80193 | -47.33482 | 2026-06-03 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b7c0631-2581-3843-a734-454b31ff0229 | -11.57343 | -54.57787 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c83e0b-a430-37ca-a9fa-c911daeab215 | -11.61667 | -55.1819 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3db6119-1b3b-3b8b-83b8-331319eed79e | -11.3282 | -53.95573 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c4f7ac-4569-30e9-a333-d7ea9695603f | -11.88974 | -57.83494 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 916b0404-d4f3-3a35-b9a4-dd79ec527a94 | -11.62518 | -55.17954 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9a65bca-a7fc-320f-ba66-4f59a01dd682 | -11.26265 | -53.96825 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1580b09d-212d-34a2-b5cc-b1322697e0ab | -11.26323 | -53.96415 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5442ce24-3e66-3699-814f-22b1c50c3f71 | -12.73217 | -54.20971 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fc4282f-b5c9-3a02-b41b-9ac8e83077c3 | -14.0847 | -59.37488 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91d3b694-9a3a-3ae3-a57a-67ed5f036d99 | -11.04542 | -54.19244 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90742050-1bb9-3c5a-8d83-b21e928e03b1 | -11.62867 | -55.18364 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d8b94f6b-1e5c-3807-a4c2-ed516c8798db | -14.1362 | -58.96489 | 2026-06-03 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2bb433c-8f21-3911-ae65-411a78707308 | -11.03985 | -56.92833 | 2026-06-03 05:23:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e539ce5-33c0-3ce3-9c40-fae6f6157ad3 | -12.73396 | -54.20898 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09ac0b7f-034c-3111-b9c0-44e5cefb062f | -21.81039 | -49.12644 | 2026-06-03 05:23:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 459ea9aa-d27b-37e9-ae48-1f0948f23c8c | -11.81312 | -57.35925 | 2026-06-03 05:23:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc5830c5-d301-3195-94b5-740510f9a0d7 | -10.56869 | -57.32573 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README11.md)
