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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 221f1b80-d8a9-3fe5-9c78-70612eb3ece3 | -17.07185 | -56.00442 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ef47545d-cf77-35f8-9ce8-50ac005644f5 | -17.07114 | -56.0085 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e3679d9b-6ff5-397f-a21c-07ea44465543 | -17.06904 | -55.99968 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aea6ddfe-19d1-39e9-a158-6a1bd7ede8e2 | -17.06876 | -56.00534 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 59b918e2-4243-3ecd-be5e-8ec1a4e7fdc8 | -17.06623 | -55.99496 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a6eb1234-04c3-3008-8d79-81b0fbec6e6b | -17.06593 | -56.00061 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 21247d95-8a94-3c01-aa06-cb6b6f2cc6f9 | -17.06552 | -55.99903 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2f620ef0-2739-3b8e-967b-f7ca40466a53 | -17.0631 | -55.99587 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 50ee8d1e-f9e8-34b2-aa33-743e5958df0d | -17.04212 | -56.03418 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 59754942-ad8f-3b0f-a3cb-dd7567ada7f1 | -17.03992 | -56.00422 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 32154e57-b953-38bc-9db1-9457bb60fa7c | -17.03923 | -56.00831 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d30f22c2-1f3e-3f0c-bc78-2cb06c5e09bc | -17.66923 | -56.23618 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d83de6df-970d-3539-9298-4e96f403943b | -17.02237 | -56.02206 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ee49c5ea-2de7-3578-9513-2e28e829b01e | -16.90181 | -55.87921 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dea5c67f-9ae5-3deb-86b2-e06476e21c1e | -16.89899 | -55.87451 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 14eddb48-1de0-3182-8a99-dd3e77a7c689 | -16.69952 | -55.85654 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 6f817da6-58e0-3c74-9449-d57ba9be8290 | -17.69963 | -56.24443 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d7dcf2bc-f7d0-3214-9f7a-3d325577a844 | -17.69823 | -56.23141 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8f2b1221-fe92-3687-b579-eea5a2137860 | -17.69752 | -56.23552 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1ab3f7ac-7598-3866-80e1-9b8f3c546803 | -17.69681 | -56.23964 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 71b5546c-5ce5-3362-8e02-edd2f14f4d1f | -17.6961 | -56.24377 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ef8aa657-9830-3924-a8cc-a731fbe1ae82 | -17.69538 | -56.24789 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 58eb88c1-9b21-3100-8dc7-a961b0951d3d | -17.69471 | -56.23075 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9e7687df-6daf-3cbc-a261-428a77fcbff0 | -17.694 | -56.23486 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d044948e-fb6c-32b4-96c3-9efdded8fd65 | -17.69257 | -56.24311 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5701b33c-083a-305d-bef2-84fe454dbefb | -17.69185 | -56.24723 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c998c684-5e66-3ecf-992e-8db32022c666 | -17.68975 | -56.23832 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1a424467-019b-396e-ac8a-8f98ac540e4f | -17.68904 | -56.24244 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b3adfa86-27db-346e-8bcb-3b02d6177ee9 | -17.68833 | -56.24657 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f6759f10-853b-3ac2-91c5-3d73dfbfe02c | -17.68623 | -56.23766 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a9b0f58c-77ed-3d76-bc0d-20f6f4082593 | -17.68551 | -56.24179 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5ede88ff-47cc-3efa-9769-d9a957478357 | -17.68269 | -56.23701 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ca231ea2-f376-3793-a18a-9b2023dbbc17 | -17.68198 | -56.24113 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 54c51819-0f01-3e51-a84a-8522acb512db | -17.68052 | -56.23402 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b3135251-58c5-3ca6-971c-7ee1620d2835 | -17.67982 | -56.23816 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8ea8d076-1f61-34ce-8413-8159badfc4d6 | -17.67916 | -56.23636 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d1415156-a486-3641-8da7-afffb5ad7e63 | -17.67699 | -56.23337 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7da3a794-06a6-340d-80b9-837a026edd4d | -17.67563 | -56.2357 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 21aa26f3-1bd8-32ca-a61f-a224e79d3753 | -17.67346 | -56.23271 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 914daf04-7e62-318d-b5cf-220514576816 | -17.67276 | -56.23684 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f4e5f71e-2afb-3d4e-a25e-612a7523483f | -17.66993 | -56.23205 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 68649587-1a58-31d7-ba85-f1d2ad0707e6 | -17.65654 | -56.24658 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 334f6d65-b8b7-3970-84d2-f28dea7d7443 | -17.65513 | -56.25484 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7a4023f3-a071-3c22-8955-749aa67e3067 | -17.65371 | -56.24179 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e7859b43-427d-3e4e-ada2-381075f41bd6 | -17.65301 | -56.24592 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| abb72721-636b-32b3-967b-05b6f8e7748a | -17.081 | -56.01455 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7cb4c038-1f16-349c-8d10-20b499ea731c | -17.07888 | -56.00573 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3919c713-1fa3-393d-98a4-b678d29beadd | -17.07748 | -56.01389 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f827ad2a-e318-365d-ab99-7decdb2def05 | -17.07466 | -56.00916 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1d8facb0-df3f-3448-b14d-1f09e6560e95 | -17.07396 | -56.01324 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4ba60c0a-e529-3943-b4c3-568b081e1779 | -17.07326 | -55.99626 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e6d3f923-8adf-3015-b59b-de3db4c2d858 | -17.07255 | -56.00034 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 169b143b-3c9b-3f82-9189-13c3153323ed | -17.07014 | -55.99718 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f7b276b2-fd15-3230-8eb8-2d17674ed0ad | -17.06945 | -56.00126 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f6603c1d-909e-39e6-84cb-8580d1f0f291 | -17.06833 | -56.00377 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c6a8c865-6a14-31ec-abcf-c31b3b99a7ae | -17.0667 | -56.01763 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 185d43a1-ac88-3ca4-a53b-f190a4394347 | -17.06662 | -55.99653 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0333fe79-82d6-3cda-b3d5-9d26aea65a33 | -17.06241 | -55.99995 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8b58d82e-3e94-3606-add2-37b9fe131701 | -17.04633 | -56.03074 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 38682763-bd2b-3c5f-ad33-e7d9b73023cb | -17.04275 | -56.00896 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 799f7692-64ec-3042-91a8-49bc66180166 | -17.04136 | -56.01714 | 2024-10-14 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2de6b275-d01f-3f4f-b8c6-89241f11aaee | -17.73209 | -56.26757 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 84b3bdbc-d45f-3794-a38c-35a66fa5cac6 | -17.73138 | -56.2717 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 633711a7-922f-31f0-8c21-823158ba97d6 | -17.73068 | -56.27584 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3ceb6a44-5de3-3d7f-8bfe-3b680a8bfcb5 | -17.72997 | -56.27997 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bd5cd3d3-2c58-3fce-872a-d1b307ef304b | -17.72926 | -56.28412 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9ce71ed6-4c41-375f-8077-9bf22fae32dc | -17.72855 | -56.28826 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1ca3f322-4f96-3d3e-8179-e69303807fe3 | -17.72714 | -56.27517 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 84c1c4bc-9d05-307a-97b7-095a72bf41b9 | -17.72643 | -56.27931 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5f64c523-9794-3164-8163-092aeafe6175 | -17.72572 | -56.28345 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b680c0dc-e260-3239-b412-77cec9409773 | -17.72361 | -56.27451 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 88165126-3d8b-32a2-b29c-297f5636a869 | -17.7229 | -56.27865 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 71b57890-b1d7-3582-afa7-d3d11d343d28 | -17.72008 | -56.27385 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 56a4e3a2-dd26-3a9a-a212-8a4f186ca883 | -17.71937 | -56.27799 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6d236cc2-fe01-38f1-a50d-cbaaa4de5dfe | -17.71725 | -56.26905 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e26f89e9-c259-3ead-8a8f-1e5ea1817bee | -17.71655 | -56.27319 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d262a841-588b-3dc0-a44b-34ffc450de41 | -17.71227 | -56.29803 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2cae7b92-850e-333f-b01a-e3e93d2aaf6a | -17.68392 | -56.31414 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 27fc702c-9410-333f-93bd-980c1d8c3bd3 | -17.6832 | -56.31829 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1a4bf7a2-8cf9-3ff6-8596-86da4118a49d | -17.68037 | -56.31348 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d039e1a8-fd8b-3033-aac4-bcfb503ffc98 | -17.67966 | -56.31763 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 309c1a7f-72c4-3be2-aa92-5f24a8a57fd9 | -17.65446 | -56.30177 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0cbe1e0a-0777-3b12-a930-202fcdd1458e | -17.65376 | -56.30593 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8c2d81d5-272f-3c6c-b732-24459106d5a5 | -17.65163 | -56.29695 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8ee85b28-3943-3925-9f8e-ad9bf23cc021 | -17.65092 | -56.30111 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cbf3ee1a-cd77-3432-a276-d0b361055fb8 | -17.65022 | -56.30527 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9f1c73f1-6398-3282-b61d-e845f6cc7c71 | -17.64951 | -56.30941 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 799c1144-a01b-32f1-ab3c-85f1b3c11252 | -17.64879 | -56.29213 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c064c5dd-ecce-3649-b00c-82d3f2e22be8 | -17.64809 | -56.29629 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 44a25d6e-a49c-3f6b-b825-78b1f066509c | -17.64738 | -56.30044 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 069adfa9-912e-3aed-b0e6-10c3f66f63ff | -17.64668 | -56.3046 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5e7c5f7f-6edd-3d50-8b60-57578e9ed89b | -17.64597 | -56.30875 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 55a4c755-6e6d-30d9-b2c0-038ff59fdafe | -17.64526 | -56.29147 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e4070aac-4cf8-3443-988f-bc2d7565a5f9 | -17.64455 | -56.29562 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e2fd3cee-b199-3bd6-9dac-68b58c373fad | -17.64384 | -56.29978 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6f68eaf2-824e-39bb-9e09-7a519f6977b7 | -17.64313 | -56.30394 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 704016ea-34ea-30cf-b1d6-84a09fe1d1a0 | -18.20441 | -56.84744 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| bbe8a128-994b-3881-9df2-1ae59e097f6b | -18.20155 | -56.84241 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 86244fb2-2cb6-3cf2-8266-d4ca3e77c409 | -18.20019 | -56.82874 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9c7bdd1f-4e01-39a2-8d28-5fdf1ab9da83 | -18.19944 | -56.83307 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |


[Clique aqui para ver as próximas entradas](README101.md)
