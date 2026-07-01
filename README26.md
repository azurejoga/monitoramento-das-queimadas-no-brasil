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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e520a1f-620d-38b5-9b3f-a730711b6b6c | -11.04562 | -56.92244 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db09731-cad7-3fa0-a5bb-0cd641f56d2f | -17.11997 | -50.08911 | 2026-07-01 04:57:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dec8ec3e-2749-3d8e-afcd-9ac9ab3e2d90 | -13.72871 | -47.87367 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15856dad-0ca5-384e-ac4d-be3f4ff26886 | -10.77792 | -53.54123 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9bc4c65-33d6-319a-a517-0d5fc143d0bb | -13.72283 | -47.88437 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6bd2245-aeba-3ac9-8851-1f15d76d08a9 | -12.83741 | -44.34182 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 37ffc923-e94b-3cc5-a7a4-fb904b6c647e | -17.70546 | -46.78126 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7ee71cc-0ada-3d17-bae7-60117448017f | -12.75277 | -44.48454 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7f6b8ab-00ce-3c79-b4de-36902edf32b3 | -12.76329 | -44.48953 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d3b446ca-341f-3ed7-9d2c-5208ffd5edc4 | -12.83053 | -44.35214 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 586375f9-3a49-3c11-bc35-e5cb6ae6b16a | -12.76194 | -44.50033 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| bcc17dff-3dde-326b-81f1-10c646ca969b | -13.26112 | -56.79964 | 2026-07-01 04:57:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 076b74a3-56e6-3327-8f7e-86178bb5cf67 | -12.42563 | -58.41305 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e02ee98-4ca1-357a-9aff-a9aed52f8947 | -12.76742 | -44.50099 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 73a35d97-b1d9-3078-aa57-6becdfc566dd | -11.62351 | -59.01851 | 2026-07-01 04:57:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4dfa130f-8aa2-33d8-b007-dccdb03251e9 | -11.88824 | -57.13221 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a281c8-efcd-3928-a7c2-1c10699cc929 | -12.80047 | -54.86057 | 2026-07-01 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18436afd-5710-36c3-ab72-19ddc2951a54 | -13.48252 | -47.87449 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66a72a8b-1273-322b-9878-e0c1f51a11a3 | -12.41749 | -58.39159 | 2026-07-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 903a4d45-3d6e-3768-a512-24c026281da4 | -12.76379 | -44.48905 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ee21848b-a34c-36ac-aefa-1d1e6f41934e | -11.84258 | -56.94401 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 12807771-3335-3256-8b67-5c8c9029e84d | -11.30584 | -51.39991 | 2026-07-01 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac0aa7f1-2d46-3dd4-880a-a25247713bc0 | -13.72305 | -47.88572 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47254bcc-e9d0-395f-91f2-6edc5270170f | -12.76878 | -44.49018 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 347cebdf-f242-37e1-94b0-4086fe014eb2 | -11.42412 | -56.07095 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f936de4-6424-3377-a42a-6e04344ffdb9 | -12.83696 | -44.34552 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 9f121f42-e560-30a7-8c0d-fe38f4ebce0c | -10.76359 | -53.54609 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86de457d-5675-3683-88d6-3fa9cdf1d023 | -16.36206 | -56.65954 | 2026-07-01 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| b89fb9be-c9f3-3444-abce-cfc23284eb60 | -12.76465 | -44.47867 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3adfd3e2-5112-3ba0-b054-376ddc39b393 | -15.94506 | -48.1471 | 2026-07-01 04:57:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33ad575b-e04c-3cf0-a724-665d7bee8861 | -12.77336 | -44.49805 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 92c933f9-3282-3c4d-9386-35dfc4056346 | -10.79832 | -53.54094 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf25066c-5046-3056-b7cb-11b61378cbd5 | -11.89543 | -57.13346 | 2026-07-01 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be55e4d3-4ec1-384e-adb1-d26553ec1a26 | -11.50144 | -54.50392 | 2026-07-01 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7546d911-ca83-34bc-bff8-455f87773d0f | -13.46981 | -47.86877 | 2026-07-01 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce87f6e3-1a57-3501-a904-5c90826c14a7 | -10.77737 | -53.54473 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0976107d-a62a-387d-b9bf-c0f27266d391 | -12.44993 | -58.48953 | 2026-07-01 04:57:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 834b8746-fb86-3313-8836-e7a21a66a6dc | -12.76929 | -44.48971 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 26496a8d-fe5b-3e49-b363-cb11bc39030d | -11.902 | -57.38729 | 2026-07-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9be78686-f688-32f3-b3a6-59592dfcefb3 | -12.84714 | -44.35438 | 2026-07-01 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f71ccbb6-fbd2-3c6e-beed-f817b0e45064 | -12.79658 | -54.86357 | 2026-07-01 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fc87a46-41de-326b-89e9-d5adf46b5a5b | -17.70976 | -46.78806 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 978b11fd-05f7-3f3f-8afa-4225ae075143 | -10.08015 | -60.49885 | 2026-07-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2ad5da8-781a-3142-9f02-eddcbcab9a05 | -11.31334 | -54.46916 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ae42c65-61b5-3c28-8a41-05b757a2dadb | -10.83947 | -54.03103 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5f8c948-9437-33bc-a8e9-240bdc04252f | -11.42541 | -56.06323 | 2026-07-01 04:57:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 92d2cf01-76e5-33a3-aa21-88966c8407e4 | -10.67186 | -54.52765 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 335959ac-8ea2-3387-9261-f9e63b680d36 | -17.71512 | -46.78592 | 2026-07-01 04:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42ce7863-a882-3651-8218-d341e4eb21c2 | -10.83891 | -54.03454 | 2026-07-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e21a74d4-7c62-33a0-989f-631f6892f504 | -19.5131 | -52.74377 | 2026-07-01 04:59:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af4b8eb9-7290-3174-b025-f040c07ce70f | -22.94547 | -52.59127 | 2026-07-01 04:59:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8b58375-06ba-3551-9dea-3ad3218924c2 | -19.67178 | -46.19478 | 2026-07-01 04:59:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ceeb003-1dee-3483-8b10-e71fe291080e | -22.79269 | -49.34716 | 2026-07-01 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79e90d27-1168-34f6-a9a9-de9d1a98ab88 | -22.78814 | -49.34661 | 2026-07-01 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f326139-331c-3768-a3d3-7fd8f2a77588 | -19.51013 | -52.739 | 2026-07-01 04:59:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f85d092-5c25-3951-8a05-606e6ae684bd | -21.81214 | -52.71981 | 2026-07-01 04:59:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e4a6b86a-24e0-3521-aa2a-61c247580209 | -19.50953 | -52.74324 | 2026-07-01 04:59:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4914d354-cddf-3a32-883a-01db43759786 | -21.49289 | -48.53934 | 2026-07-01 04:59:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 026217ae-272a-39aa-8200-72fc78147b53 | -19.5137 | -52.73952 | 2026-07-01 04:59:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4278763-27b8-3179-ba59-1ba8e05b6783 | -18.921 | -54.83507 | 2026-07-01 04:59:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6afa24c8-356b-35a1-b48d-5f00a671e318 | -21.80848 | -52.71925 | 2026-07-01 04:59:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee2af0ce-9281-3c5e-b953-0cfe6902930f | -24.31884 | -53.59272 | 2026-07-01 04:59:00 | NOAA-20 | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b608f85c-c337-36bc-b5fc-15e92b59c262 | -21.0928 | -57.46595 | 2026-07-01 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 706dd926-1a26-37cf-9559-830ac5d84d23 | -21.80943 | -52.71704 | 2026-07-01 04:59:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7027b723-3e61-39ec-87fe-e0d1aa11ffbe | -21.09615 | -57.46658 | 2026-07-01 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 449528e8-c206-3db8-9976-c91eeea59248 | -22.8018 | -49.34819 | 2026-07-01 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8292af1a-84d0-34b4-ba82-dac36088622e | -23.82049 | -48.7132 | 2026-07-01 04:59:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b3ed82d-86ee-3085-b4a0-f79ded77ef24 | -12.8165 | -44.3454 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 162d0084-f970-36c1-a338-ba19a7d3ba15 | -12.8552 | -44.3389 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 320f066c-cb29-367c-b41b-000d1aa78206 | -11.4149 | -56.0525 | 2026-07-01 05:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ca91652f-b225-36b9-b8cf-37cc6a09deaf | -12.8354 | -44.3657 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 6f3a2ff6-436c-30a9-9c72-3ccc0e24310c | -10.6596 | -54.5372 | 2026-07-01 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| a675a62c-49ec-386f-9189-1f7342a10412 | -11.4336 | -56.0711 | 2026-07-01 05:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| b915b3ef-0e56-3276-a04b-1a59909064c9 | -10.9401 | -43.0355 | 2026-07-01 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 10b5a277-7cba-314c-82ed-b0c8f092dcdb | -10.9205 | -43.0622 | 2026-07-01 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| c42538d2-f559-3828-8af6-b5b1419b112c | -12.7751 | -44.4927 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 344.5 |
| ff7402ab-7155-3d86-a5ff-2b1c6ede4637 | -10.9397 | -43.0593 | 2026-07-01 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3aff4d00-6825-3646-b20d-4092938f0cc6 | -10.6784 | -54.5356 | 2026-07-01 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 3100d714-f903-3a58-906e-5f1f848ea955 | -12.7557 | -44.4959 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| a31f1542-0862-319b-bce9-624f7500248f | -12.8359 | -44.3422 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 329.7 |
| 034d04b5-3851-38fd-9c73-24e25ddb55c1 | -10.9209 | -43.0384 | 2026-07-01 05:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| bd42c2ba-8aae-37e5-b6b9-1dd068f826c8 | -12.7562 | -44.4724 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 173.7 |
| b468ffe8-de47-3cf2-b2e4-425d6c03cef2 | -10.6598 | -54.5169 | 2026-07-01 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| f9681872-d923-32dd-8b41-bd22ce5886a1 | -12.7755 | -44.4693 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 264.6 |
| 83e65ca0-42ef-3ae2-a3d3-a485d41e8e36 | -12.8548 | -44.3625 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.6 |
| ee5b912f-18a9-3158-b917-43060ac5af39 | -10.6787 | -54.5153 | 2026-07-01 05:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| e92d54db-0ffe-306d-b4d3-8deecd51d910 | -12.8363 | -44.3186 | 2026-07-01 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6a00be47-2170-3dac-a735-6b7ebe031b09 | -11.4338 | -56.0509 | 2026-07-01 05:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| c84d29fc-0066-3471-a5fc-5e1103e094a4 | -10.9397 | -43.0593 | 2026-07-01 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| cc7a1bb3-aa34-38b9-a3f8-c71cda31de66 | -12.8359 | -44.3422 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 348.6 |
| 7f19b26b-b97c-30c1-afbc-9df7361df97e | -12.8548 | -44.3625 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 4f55ab1a-8e5a-337e-8154-e9e6493b57b5 | -10.6598 | -54.5169 | 2026-07-01 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ea964747-6ca1-36fd-8834-e86c31035055 | -11.4147 | -56.0726 | 2026-07-01 05:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0437830c-b66c-3d8b-909d-2df4c75c14c6 | -12.7751 | -44.4927 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 314.7 |
| 4094a1fd-b37c-315c-b796-7c27e1b158c7 | -10.6784 | -54.5356 | 2026-07-01 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 2e6bea41-6997-3fcc-b15b-a2dc07a1117e | -10.6596 | -54.5372 | 2026-07-01 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d0ba3289-5323-333f-a937-aadc0efe9637 | -10.6787 | -54.5153 | 2026-07-01 05:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| edc754a7-10c8-3823-8452-69e246239dd4 | -12.7557 | -44.4959 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 265.0 |
| fca3a596-bf2e-3626-95b7-0c166941f07b | -11.4336 | -56.0711 | 2026-07-01 05:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a0989f09-707c-321b-896f-1d7d2c69f041 | -12.7562 | -44.4724 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 162.8 |


[Clique aqui para ver as próximas entradas](README27.md)
