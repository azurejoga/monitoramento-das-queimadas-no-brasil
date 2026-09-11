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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10b48f53-6375-3dcd-92ee-6e85abb14fac | -3.15586 | -60.66048 | 2026-09-11 05:48:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6299253c-1e99-35cc-9295-c0d3d4ef832b | -2.71872 | -57.61275 | 2026-09-11 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b9861c7-7ae3-3925-a0ff-2897e6ce3d5d | -4.53129 | -54.96458 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff782cf1-e6a3-38fa-9831-20d6c4153cca | -4.35716 | -54.77542 | 2026-09-11 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ed4f6900-a27d-34c4-9c90-83fb99ad547d | -4.53696 | -54.96561 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e1aaaa8-ba3f-3e07-8bbf-de1372437cdd | -4.525 | -54.96773 | 2026-09-11 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27d0a049-79b1-3a80-a2ea-5de2161c468c | -9.18233 | -68.20742 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4328b9e9-7747-3985-8375-8ab466ffe6df | -7.75583 | -66.90913 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e8e1374-28eb-3514-bf23-d27424256577 | -9.34753 | -65.68036 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 003bafcd-ca44-3df9-bf75-40076510a67f | -7.64947 | -67.1927 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b1eb46a-06e7-36d6-8f47-1404326bfee3 | -8.46049 | -64.04979 | 2026-09-11 05:50:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d64c06d9-4498-37b1-a2be-3a5b8cac3844 | -8.88265 | -70.84088 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 014de83e-75a8-3b07-8590-d4be6a1dfe2f | -13.32079 | -61.6775 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce2b72a5-16ad-3560-8b10-717ea7039a49 | -8.63509 | -66.51271 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77f96cce-0a1d-31be-b40b-7cb56cc305a1 | -9.41066 | -67.41441 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ceaa261-5fb8-3de6-9814-ce04a449a390 | -10.22351 | -68.08529 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25117dc7-d5d1-3cc6-9b63-bf00d78de461 | -8.83166 | -62.48618 | 2026-09-11 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4e506f4-83d5-3efa-baa5-07a675af5c32 | -8.63397 | -66.51971 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d43607a-ce61-310d-8f9a-83b8dc7f0d27 | -9.75297 | -66.61861 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85830fe9-c82e-343d-acab-15e14f4cb5b1 | -9.04662 | -65.41364 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f70d7f60-cb63-3f7a-906a-8cdee7154d93 | -9.17889 | -68.20686 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e29ae0b-cf50-3d2d-99cc-8d5fc48dcd27 | -9.31189 | -65.88599 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04d5384b-b7f6-3bcb-8c51-ba20b2eb8e61 | -9.19264 | -68.20914 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eec76520-bfe9-318a-b09a-ef65e5af075d | -9.18295 | -68.20365 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92a54d34-9041-3875-85a6-bd8f33c6f857 | -9.46217 | -68.83689 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e12c50ba-c5b9-3c8b-80b8-734f648b3df8 | -9.04607 | -65.41716 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9c133f3-5cca-3111-b232-7dd6eff8337a | -13.25672 | -61.6031 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ed1a91c0-1197-3a77-a8b4-f043734a77e1 | -9.0361 | -65.41558 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2e2dc0b-9623-39a7-a87e-350a956b0bf8 | -8.63564 | -66.50922 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1986f48e-e46b-31bc-b757-e6a1255e42c7 | -8.9851 | -65.39313 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ba4435a-9137-33fc-9051-beb7e8512865 | -8.63453 | -66.5162 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e72da76-6d39-39f0-91bb-7afcf07eb810 | -7.75526 | -66.91267 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e247e914-e42b-3af4-95f8-4aef1b8d9ec4 | -9.03887 | -65.41962 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8553ea7a-13e0-363d-85d8-b7f0ea3b0bbd | -9.03554 | -65.4191 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af5ef0ff-ee5a-32d2-a1ab-d9b7fe67c8b0 | -8.65629 | -69.78989 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b41a3594-1f81-3dfb-8cbb-7ce609e835cb | -7.77793 | -66.96381 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aea4a340-8ab8-3736-b186-cdab0725c157 | -9.75827 | -65.03059 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf496204-2fcd-34bb-8325-cbd1f6275746 | -9.22617 | -65.58907 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d25d370f-0b13-32a9-8f2e-738ae243124f | -9.03665 | -65.41207 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3df53f2f-9e1f-3307-85bc-3419f22a31e8 | -9.7155 | -64.53953 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bbdb833e-a00a-3f5f-9b0c-59ddc8036ba5 | -9.23558 | -65.59414 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a778d92-be6e-303f-9eae-c69f72bc4415 | -12.15935 | -64.13729 | 2026-09-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc01882e-8c27-34e0-8fc9-62740cae225e | -8.86792 | -72.70068 | 2026-09-11 05:50:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ebf7697-e6c6-3eca-9b58-ad8b3aa4737e | -12.01293 | -61.84338 | 2026-09-11 05:50:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f8be8aa-e41c-3243-8b27-b3379755d4a1 | -7.75698 | -66.90203 | 2026-09-11 05:50:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73450048-6a81-39db-af4c-25e7ef4f7265 | -9.22837 | -65.57507 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8be944a4-53a6-344c-81d7-f47b77287d2d | -8.65554 | -69.79442 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afd89ce2-9f6d-3f8f-92b1-cf6ee008589c | -9.02335 | -65.40997 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8e3b6ed-d167-3c39-8648-654e0962376e | -13.24898 | -61.59812 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 69751f91-811c-328e-bacf-8f92ecaf8761 | -8.63896 | -66.50976 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf178e08-5a48-371d-876a-4d2a8ac9c1bb | -10.29338 | -67.27326 | 2026-09-11 05:50:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50293279-33ab-3b2f-a819-d9ee61dbb3f4 | -9.16018 | -64.41721 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 46725c1c-ea11-3260-9ac0-ac361f556e46 | -12.01243 | -61.8469 | 2026-09-11 05:50:00 | NOAA-20 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b7ab159-0da9-3ad7-8576-028dff93f0a6 | -8.83231 | -62.48181 | 2026-09-11 05:50:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66b980e4-ac79-3e3a-9742-d8d66b3ed212 | -8.63951 | -66.50626 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f54ee49-53e1-3dfd-952a-c2b6913fd1d7 | -9.50137 | -66.78939 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a085d5f-b419-3160-899d-004d1a5dccd4 | -13.25259 | -61.60251 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 55a23ff3-a546-3da8-8be3-1f3b32a3879a | -13.25311 | -61.59871 | 2026-09-11 05:50:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e99ba9a5-7aeb-3223-aa7f-3776d07a9065 | -12.15582 | -64.13676 | 2026-09-11 05:50:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae4157b8-4a70-366d-8abc-8ae9ae56042a | -9.02667 | -65.4105 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dc6f79e-aa30-3858-926f-67114844aa6b | -9.10221 | -67.68763 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4642134-a563-3e98-9f8c-d5b29965b682 | -9.14801 | -68.20638 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a19ed17-949a-37a4-89a2-1b39efc1a6f0 | -9.48611 | -68.4953 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10a52afa-43d3-3f5c-8125-2dde7891e4b8 | -9.13806 | -67.8367 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e357cc6-99ee-343f-9db5-64d61b02b385 | -9.49241 | -68.50034 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd2af6e-37f2-3361-bdae-8e670174f7d4 | -9.14288 | -67.80725 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff96aba-6d42-3867-b0d1-6f8c9758890a | -8.64116 | -66.51727 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 453b9ee7-6dcf-3a10-9fc2-731acaf83b36 | -10.2229 | -68.08899 | 2026-09-11 05:50:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4f09426-bda1-3225-99dc-16cc4b8f15d5 | -9.49805 | -66.78886 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d23e2a0-00bc-3dd9-92f0-a6d4c7f84393 | -13.31668 | -61.67691 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ca5a9ee-6465-3769-9a37-284087f181f6 | -9.49304 | -68.49649 | 2026-09-11 05:50:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b856389-8edd-3b8c-96cb-2d5296d5ce29 | -9.0156 | -65.41594 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 342d226f-7621-372b-b389-e988d76fe129 | -9.0433 | -65.41312 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a767cddc-84b7-3de7-8fa3-634b9f311e54 | -9.4096 | -65.93378 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07a2aacb-220a-34a7-bb48-3a90bd0c17a8 | -9.75826 | -64.94202 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a5a47af-70a8-3109-8a8a-f3456334c2d5 | -8.65182 | -69.79376 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84cde671-99da-3a1b-8e12-16028e859f90 | -9.14228 | -67.81092 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 925aaa8a-680f-346b-898b-6a0b8635c552 | -9.4353 | -67.11883 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10670124-17df-3642-b29c-43dbb1d78e80 | -9.11059 | -67.70028 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e54b2374-44b8-3aa7-9a3c-6d7e3074115c | -9.7577 | -64.94563 | 2026-09-11 05:50:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699deee9-c77b-37d4-8b2c-55311743b7f0 | -9.105 | -67.69185 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2956df7-8088-324f-aa4c-8f90865327f6 | -9.11118 | -67.69662 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 840e5a63-8242-343f-b051-614b2ae3fe5f | -9.03997 | -65.41259 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7516855a-c45f-3f10-8f40-2fd088f59ab4 | -9.01337 | -65.4084 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d9e115-478e-3f81-870a-a20bc82976d0 | -8.64735 | -69.79764 | 2026-09-11 05:50:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5b7d51-9640-37ff-b17b-17ca626191d0 | -9.10839 | -67.69241 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66c75477-bc0e-31e4-aa1d-a6e5625e2a6d | -9.04183 | -65.72526 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6894d6ab-2c26-3db5-b37e-705fd0538b1c | -10.2928 | -67.27681 | 2026-09-11 05:50:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e0af64c-1bd7-3058-bfea-7860a607475b | -8.46334 | -64.05405 | 2026-09-11 05:50:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 983ba65c-40af-3348-9659-70a22f33ed86 | -9.15856 | -66.06114 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ff01ba-3ffb-3151-9374-6353de6004e4 | -10.29614 | -67.27736 | 2026-09-11 05:50:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba51ecbb-5fab-3f4c-8c05-ea4bc2b18b1c | -7.39349 | -72.80105 | 2026-09-11 05:50:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a153147a-621a-3bac-b23f-5771b005334d | -13.34292 | -61.66913 | 2026-09-11 05:50:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f6808f3-e2a1-3b82-996e-8530bf5db083 | -9.42452 | -65.86132 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a9d7741-92d6-3ca1-893c-4b4edbe6f2a4 | -8.99233 | -65.41226 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab093231-aeb9-3415-a735-26aeee696127 | -9.08242 | -65.48789 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c19f0c47-246a-3b91-8652-050c7d2c0ebc | -9.17545 | -68.2063 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9e02fab-7a8b-36ae-b957-6324ee23d6d1 | -8.69248 | -67.25397 | 2026-09-11 05:50:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f98add32-40e0-34c0-b758-e65659342651 | -8.62845 | -66.51164 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce6583f-99e8-3c50-adc4-ff9f43356610 | -9.30147 | -65.88789 | 2026-09-11 05:50:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README33.md)
