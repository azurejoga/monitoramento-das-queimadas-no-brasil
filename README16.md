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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd45ccf7-7fd8-3e6b-94aa-f1e9f4b5ab7a | -8.29804 | -49.30665 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c99cdf00-f12b-314d-af29-63f81ed71c5a | -9.29977 | -59.42456 | 2025-10-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4206bffb-65ce-3547-8a4a-7dfc4c9cc966 | -9.45408 | -49.84922 | 2025-10-21 04:46:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b687c390-a97a-308e-b32d-0e39b10c4d7c | -8.59714 | -48.81409 | 2025-10-21 04:46:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57d63bda-b1ab-3bbf-801d-81aa41b122ba | -12.42253 | -54.42129 | 2025-10-21 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c0a96f4-fac5-35c0-af85-e84639b7da57 | -12.42316 | -54.41748 | 2025-10-21 04:46:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46f74ae6-b843-3925-aea1-569a755667cb | -6.88225 | -51.14171 | 2025-10-21 04:46:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b1d5298-2e67-379a-a446-9a2d7675e9d5 | -8.88958 | -50.17017 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7af4cc4-3033-3222-a977-7e48d34de6ef | -7.13542 | -49.29725 | 2025-10-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffed34a9-0287-3e31-b7ed-9e08bcf6a87f | -8.71531 | -50.04435 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38629832-6569-3ac6-ae6f-9a90acb62ded | -8.84799 | -49.70512 | 2025-10-21 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5866743-36fe-3275-99d7-0f945de9210e | -10.08256 | -65.16556 | 2025-10-21 04:46:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eab72a6b-52ba-3662-97d4-4f6d70ae47b1 | -7.94628 | -47.98749 | 2025-10-21 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7040a202-7bcc-3967-aee1-33d04137e01d | -9.11506 | -65.3604 | 2025-10-21 04:46:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 171e8006-69cf-31da-9c3b-c956be80ac14 | -8.29403 | -49.30992 | 2025-10-21 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0014caf7-5fb9-310f-b197-9a51baa2ec08 | -8.15141 | -47.99303 | 2025-10-21 04:46:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb8d81fa-4a50-31e5-88b5-b75466d842f0 | -7.98822 | -49.95523 | 2025-10-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58eca8b1-fe7f-358d-acca-be7944ded786 | -8.64158 | -63.05106 | 2025-10-21 04:46:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f0c661f7-105b-33b5-9792-7e57e2f538ee | -7.36794 | -47.75115 | 2025-10-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6e5d4b9-9e1c-3cab-8571-51c3401ccbb4 | -9.01923 | -49.75742 | 2025-10-21 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4d960c89-8c1a-3abe-9657-467937821ad1 | -7.36429 | -47.7506 | 2025-10-21 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b548da6b-8be8-38d5-8ec4-3c154d7b008b | -19.09217 | -57.53832 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5e78ed45-c65d-3c98-9bd8-1095582b3cba | -18.19172 | -52.97845 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 59a8e11d-a134-337f-9a43-9fc86c385b64 | -17.42031 | -55.05622 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7ba9993-76b0-362f-8c6c-ba4490a76df7 | -18.17957 | -52.96896 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976dbc59-14f3-36bc-849c-a3f5ff6f4d67 | -19.08853 | -57.53762 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 08afe803-d06f-3907-8ae6-3668c5bc0df2 | -18.16794 | -52.97823 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83e6e617-aaf0-389b-a749-179cc9237ceb | -15.89705 | -59.61027 | 2025-10-21 04:49:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 14189b10-9f3d-3989-afcf-881a82beab0d | -19.09582 | -57.53902 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9f6143a6-21f6-3e8a-8ec5-2878500a1e63 | -18.18288 | -52.96952 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54dd6307-39f7-36ab-b1e4-c623ff0a7751 | -19.90763 | -44.35786 | 2025-10-21 04:49:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| befa0b12-241c-30ac-975b-0a0e6d6ed115 | -17.68458 | -52.23988 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| df0880af-327c-3793-84c9-16861b2a3fd9 | -17.68683 | -52.24783 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48321f5e-b22b-336a-bbc0-6e7816e40aa4 | -17.41756 | -55.05188 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 41981f30-a07d-38a2-a34a-e6bae714659f | -20.14573 | -52.83805 | 2025-10-21 04:49:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4b19dc1-2b30-3067-ab8a-1e436116d7cd | -17.44082 | -55.03669 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e1203ddf-76d9-32cd-a0c9-5880c8748e8b | -18.17569 | -52.97205 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 963f5584-526b-3a4b-b8c3-96551df22619 | -17.42491 | -55.04931 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7bb98d10-d48c-3e77-afa8-31d23fcf9ac0 | -17.40623 | -55.05759 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7c93846e-0a1a-3a68-8a83-85590eee21a0 | -18.59498 | -51.71468 | 2025-10-21 04:49:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c7ac6240-7d08-3f8f-aa80-88b80362e2aa | -19.09866 | -57.54421 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 11d5aa17-2b98-3ab4-833e-c900fe7b1008 | -16.79937 | -51.35085 | 2025-10-21 04:49:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fceaf5a5-b175-30b1-8252-c1afff788727 | -16.41429 | -53.62597 | 2025-10-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88442757-5f10-3360-adfe-5e4a6424bcca | -16.53167 | -53.72288 | 2025-10-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32cb4c12-1c87-325d-a553-ea3961162695 | -18.80269 | -47.01105 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b61ab62e-f390-323d-ae5b-0928933f7f57 | -17.4292 | -55.02305 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f4819cb2-94dc-3a66-90a2-9e32f4ff63db | -19.09947 | -57.53971 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 947bf6fa-c9eb-3d6c-ba96-2a0b07218f7f | -17.44567 | -55.03775 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0b9e3190-6377-3216-b8e5-532a908436bb | -15.25529 | -50.21108 | 2025-10-21 04:49:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc153e08-ccf8-38fa-a835-43e5eebca609 | -18.60716 | -48.20892 | 2025-10-21 04:49:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 249a0dc5-5727-369b-9ef7-1a8ca941ff0b | -17.42154 | -55.04871 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| fb8672bb-e42d-3e7b-a08b-078815de8da0 | -17.42889 | -55.04616 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ae381868-7b7f-3d25-90de-3ce4e802f5f4 | -21.03985 | -44.66903 | 2025-10-21 04:49:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fff2a197-07a4-314d-81c9-aa6cc6d448e4 | -17.43286 | -55.043 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 5e66b2c1-a832-3415-b4ef-8d832e34845e | -17.68627 | -52.25155 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9296274-d3ab-32f9-b077-7abeb2465893 | -17.41296 | -55.05878 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3803c857-b5b9-3cd6-a240-bcb6bd57e3b2 | -17.68347 | -52.24729 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83a90590-7b7d-37d1-837b-7bd3dbedb9b0 | -18.5944 | -51.71863 | 2025-10-21 04:49:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22b418c9-60b5-3a3f-aabd-d6878cd604d8 | -18.79999 | -47.00928 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0edc2129-68a5-3a9c-95af-bfe89acea92c | -17.40499 | -55.0651 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cbeeb655-839f-3002-9894-1a56235523c7 | -20.53401 | -48.07558 | 2025-10-21 04:49:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3ec6ffa-e0b8-3060-9220-587214bb5f21 | -17.42827 | -55.04991 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 08b3ebfe-84a5-39f1-8fba-2bc9ffc1ce87 | -18.19228 | -52.97482 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02049abb-1f95-3232-83f2-460ce90ae905 | -18.16463 | -52.97767 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9073fca-c5bc-3b69-8d91-54b86b007b36 | -16.3695 | -51.43764 | 2025-10-21 04:49:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59c4b8fb-f17a-3f35-be45-55124632a43c | -17.42522 | -55.0262 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e942ba10-3d50-3e56-b154-632b9356e408 | -20.43102 | -48.03723 | 2025-10-21 04:49:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25a633cd-58fb-3169-ba7c-9ff0ec330239 | -20.95771 | -45.81591 | 2025-10-21 04:49:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9dcf7d0f-7c25-3412-9296-e0f7d97e430e | -17.44418 | -55.03729 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 494d3fa8-a26b-3679-84c4-3b4145c9b416 | -19.03739 | -48.4758 | 2025-10-21 04:49:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83434221-b696-3f5c-86e9-b0585609d6e8 | -19.91339 | -44.3549 | 2025-10-21 04:49:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fe1ae45b-d876-3208-914c-3dd37df30a61 | -18.79768 | -47.01521 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d91f1e79-4b75-3d2e-baa8-3b68dd50c3f5 | -17.44021 | -55.04044 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 86176e0f-ca6f-3762-977f-542ef3f66857 | -17.68738 | -52.24412 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ad9a14c5-430b-38cf-a296-a018bc1fbc21 | -17.42583 | -55.02245 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 89d446d1-3a23-3a46-b7d3-0af016cfe6b7 | -19.33583 | -44.69035 | 2025-10-21 04:49:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cd36c96-519c-3286-aff1-c2fa9f70c620 | -18.79944 | -47.01374 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49d28980-8bb3-329b-828d-1a028096ba15 | -16.53498 | -53.72345 | 2025-10-21 04:49:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c8473ae-4c0f-351b-a0b2-d537ac47059e | -17.41633 | -55.05938 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ed74b18c-f17a-3e40-a2d9-f4f0d4ce278f | -17.43562 | -55.04735 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 27.9 |
| 6ccb522e-497a-38c3-9ad8-04ee4945308f | -18.79889 | -47.0183 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8467a0f0-5efe-3df9-b0ea-c7a226db5383 | -18.59783 | -51.71917 | 2025-10-21 04:49:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3de1ba6f-7cf3-364f-9bbd-e5eac878d656 | -17.4197 | -55.05997 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 214999c6-85de-393c-a4db-ed92ea7288a1 | -18.80339 | -47.01854 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48b851fc-5ea0-3fa6-a3d4-901948c52208 | -19.91302 | -44.35857 | 2025-10-21 04:49:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e02f02d1-5ba1-31c3-8ed7-5a842685193a | -19.09268 | -57.53573 | 2025-10-21 04:49:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 637e679e-159c-3ba0-b31b-d86f87dcaca8 | -17.44143 | -55.03294 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cc521d28-c26c-3e3d-a161-49754b7a254e | -18.17182 | -52.97514 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec1b3497-f543-3726-b034-70306641f5ca | -18.16407 | -52.98131 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f894e6fe-79b4-3920-9ed3-e233e2860b56 | -18.33526 | -51.76693 | 2025-10-21 04:49:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f5bcf63-5c4e-3401-aa10-30cfd1296584 | -17.41082 | -55.05068 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1e3bd20c-b094-3531-9687-b5bd60412145 | -16.8028 | -51.35137 | 2025-10-21 04:49:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d2b2c80-ff4b-3c00-9803-86e6749cf0fc | -17.43806 | -55.03234 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3d0e27e9-acee-31a7-896e-c2b11f6629f8 | -18.7982 | -47.01067 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82b10af7-8b9e-3c2b-8304-7365488b192a | -18.17513 | -52.9757 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3527d036-faa8-3de8-bf8f-efdccf4b784a | -17.68292 | -52.25101 | 2025-10-21 04:49:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1622e060-8b28-315b-8fd3-dcbc0c736a50 | -17.43684 | -55.03985 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| b474e850-833c-3d08-9312-69ea8ac928e5 | -18.80217 | -47.01551 | 2025-10-21 04:49:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79346d88-6cb7-3836-949d-3d30b1c3aca8 | -18.13919 | -50.7901 | 2025-10-21 04:49:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9e87759-a06b-39c6-9db7-13f4ee6a1ef5 | -17.42429 | -55.05307 | 2025-10-21 04:49:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
