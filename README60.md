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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 051181aa-91c4-31f3-874f-5ac611ffab1a | -6.95139 | -58.9549 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f729813-8d59-3153-80d5-b5c2d700b58f | -6.76311 | -55.6549 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7724f8f9-a0a1-3b03-929c-778fdc9bad68 | -6.59623 | -59.1158 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25c7d83c-2659-3f79-803f-216625967f72 | -6.78224 | -55.66171 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 94cbcf3f-91c0-3fc4-b2cf-0970863f19ea | -3.50402 | -59.03303 | 2026-08-29 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2685ae0e-e4ae-3caf-aacb-b6a80db81ca7 | -6.75482 | -55.67723 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d68bb1a6-05ee-3f1f-81ee-f8d94e377eeb | -6.76147 | -55.66649 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd7bed57-c2e8-3984-b91a-ecf3060da42d | -4.30179 | -59.47411 | 2026-08-29 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f16439f8-2c25-337c-b8b9-ec8e20f91513 | -6.77029 | -55.67437 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0694aae8-dbe0-3390-9256-cbdcda2ab098 | -4.19072 | -54.57479 | 2026-08-29 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45203515-40cf-38c4-b09e-cd23dba4c51d | -8.24134 | -54.96703 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f98835d7-c4a4-3630-9caf-c4e8d0313a01 | -5.88821 | -57.76694 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73dc42f1-8d63-37a5-82ac-8828877d7f90 | -6.77146 | -55.66567 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e241cdde-c823-3ebe-9e4d-44a40ec1ae5a | -7.00175 | -59.64034 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a27f83d-5a0e-3c1e-9c11-10643a082ad3 | -6.88561 | -59.44719 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6ca6855-bb33-3e9b-99d7-8d5485479c14 | -6.95067 | -58.95174 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 966d862d-0057-3286-b3c0-1576b3157efa | -4.3325 | -54.89978 | 2026-08-29 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e0c4bf9-d537-3c49-9a57-6016a14b8fb1 | -7.34603 | -55.17065 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4a6e5c6-43e3-30f8-b9d6-20582854096b | -6.78378 | -55.68814 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5949500d-8a5d-35e8-8522-212769b3b81f | -3.73056 | -58.99422 | 2026-08-29 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd4f0a10-eae4-3cb3-a5f3-d07db29daf51 | -6.15693 | -57.78545 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdf517f9-aee5-3c19-a68b-775b5002dc6e | -7.51462 | -55.31118 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a27f2466-788f-37fe-ac85-bca903a24f59 | -6.77066 | -55.67162 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 730aa5a0-8b59-30b3-b902-b4dc7fbe5acd | -4.54359 | -54.92598 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b51ccb0-3cd2-3632-b23a-e4cbaea374a2 | -4.06227 | -56.29269 | 2026-08-29 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c95691b6-7c74-3f2f-9531-a8d514fbd0d0 | -6.7727 | -55.65955 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a4a3ba2a-bfcb-3a9c-8653-9cfbc18dd653 | -5.88764 | -57.77083 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c18ac296-f635-3e25-80f1-4867fe711a5c | -7.50899 | -55.31359 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e275ca5f-ada1-3113-980f-31272156c24b | -6.88665 | -59.41191 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5962cef4-71a5-3bf5-97bc-de1fa3467da0 | -6.94768 | -58.94416 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1b5343f-5a3d-3e7f-8a6f-2d7ac841ef20 | -6.76604 | -55.67038 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8d37cd-b06f-3779-94e0-2123c86bd7a5 | -6.77645 | -55.66662 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5f4c3fe3-5828-3820-8e28-7d4318044c5a | -7.51111 | -55.29789 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19ee7009-e627-3848-9bd6-a0c4094f4c39 | -3.5231 | -59.03595 | 2026-08-29 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb089470-642a-3364-9821-941c1a220257 | -6.7675 | -63.04317 | 2026-08-29 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fc2eea2a-20c4-36d3-a787-a931170137c3 | -2.74934 | -58.17284 | 2026-08-29 05:36:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35aba371-f57a-3510-9c88-f399469f92ef | -5.98327 | -57.6742 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a60c82f0-567b-35de-866b-6b88882d3859 | -6.762 | -63.0567 | 2026-08-29 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 948df251-fa9e-35e5-b7f6-ac6db5157828 | -6.76065 | -55.67226 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47e91e84-4f8d-3a1c-b83b-2ce4e6448621 | -6.57376 | -56.54397 | 2026-08-29 05:36:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e8b146e3-309a-336c-858f-6975538d42ae | -6.1552 | -57.79774 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 107dd706-b1f6-3252-9e2e-84b23ccab855 | -6.94561 | -58.95814 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6f7bfb1-947f-3360-a10d-7fee2435f5b3 | -5.98146 | -57.68682 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 318388dc-4301-355f-9f88-e4cfe7e877a2 | -6.00382 | -57.8358 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46f8a6ad-3487-35a9-9557-e5a2f906319c | -6.77105 | -55.66868 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47e8f50e-e570-3b17-b65a-b9b8999b5548 | -6.77062 | -55.6742 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94905179-8cd0-38d1-a9b6-d006a7140fe4 | -6.77683 | -55.6638 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6bb8e4d3-0269-36a1-af5e-36b6d052c3c6 | -5.98206 | -57.68264 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c653a306-2228-3080-8ed9-a36c74e486a8 | -6.75561 | -58.7229 | 2026-08-29 05:36:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affb1ca1-4f3a-3d07-8358-854e3e5a26d2 | -6.72205 | -59.43864 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8de76c0e-0187-3d69-acf7-3676dc57b13f | -7.5055 | -55.30018 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3544861f-b21f-3bde-aa18-274776af3eb1 | -6.81998 | -59.4558 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f08fd3e-3432-362b-a607-797d99fe8d84 | -6.16007 | -57.79433 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0405001-d6b0-3ef3-b609-348f7cae8eab | -6.76687 | -55.66451 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 508dd33a-4197-38c9-b2f9-8def50b10202 | -6.5821 | -55.44034 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ba21440-4c7f-381e-a7c3-ebaefd27eee8 | -6.94613 | -58.95463 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 781baddd-92e3-3f02-a225-3f14b97c7ee4 | -5.28981 | -50.94324 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64a65d9d-ab45-36db-aa4c-4cd68625a637 | -6.77023 | -55.67695 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 037547c3-d3ec-34b8-bac0-d72c7c171fdd | -6.60164 | -55.44937 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2e84927-79e5-3765-a004-6ad0ff1a5e6b | -7.55614 | -61.30274 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad5b95f5-9e7d-339c-99ad-9f7c82a8ae4b | -3.10697 | -60.20432 | 2026-08-29 05:36:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68112338-f6cb-3daf-9752-81de7736e0a6 | -6.77226 | -55.65969 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bceb7830-57cc-3493-b04a-4f82b86e7f0e | -6.02835 | -57.69809 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36efd470-ff64-3ad3-8f7b-c464cc7ae5e4 | -6.86468 | -59.03547 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db4334fe-7438-3702-8125-082e8492f3b8 | -6.82898 | -59.9494 | 2026-08-29 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35ca11e3-b3bd-3bce-a244-7cbb06d52049 | -3.82918 | -52.41247 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfa73fed-a75e-363a-a59c-0dc296ffe3c0 | -6.88646 | -59.41021 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 507f19ee-5306-34b7-9324-234ffa5376c4 | -3.61337 | -60.54201 | 2026-08-29 05:36:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 745770da-e8a5-3266-87fa-b0b583daf06d | -6.77083 | -63.04369 | 2026-08-29 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7610038-9824-343e-87bf-149bf1d93a18 | -6.95015 | -58.95523 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b39528b3-97d5-3855-983c-63177074909e | -6.7781 | -55.65765 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 8ed0328e-8e92-37a4-a1d9-56e151cabd82 | -7.34561 | -55.17372 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c9b55e1-f04a-3f2a-a9f2-74960751dc52 | -7.49675 | -55.28621 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72902226-111d-3939-88f8-6456e402884e | -6.77051 | -59.46834 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92e1d2ad-8e21-3c51-8f5e-56829cfecdd5 | -7.3525 | -55.16249 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 428c9a95-ebc3-3197-9ed7-cbcc807ade05 | -7.5526 | -61.3022 | 2026-08-29 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53da1c5a-1920-3b13-8068-c884299ffecc | -5.89054 | -57.75084 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 184a9595-2f33-3039-bbce-72d570de779b | -6.95119 | -58.94824 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6aeb9b59-26aa-3dac-af68-ac8251f00a94 | -5.89304 | -57.76383 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d78b5ab1-602b-32e1-a774-572adc24c202 | -6.15462 | -57.80183 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f95d90f3-5c07-3869-b892-6a318924662a | -2.75111 | -60.23531 | 2026-08-29 05:36:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4c03b90-c00b-36aa-9800-c4b1fc5d0596 | -6.93354 | -58.95641 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fd1e8d2-3359-38a8-8622-8edbb4687eec | -6.74278 | -55.46812 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46b42e99-8be5-3035-9a5b-fb7950ca4832 | -6.16378 | -57.7991 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4aaad905-089a-3a96-8417-2c481d11f073 | -6.79667 | -59.39672 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cb1ab0f-dad1-3184-ba0e-85733148ef1f | -6.78729 | -55.66227 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0888cc7d-309b-30bc-a9cf-a8586864976f | -6.84098 | -59.94654 | 2026-08-29 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fbdaa37-2285-3cbb-a1e8-a72c608b3547 | -6.1236 | -57.69446 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d51a93e-6097-347d-a8ba-853eacdf0324 | -6.40886 | -51.67048 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b2bc26e2-a365-3421-bca2-9d8d1f63b6eb | -5.88935 | -57.75906 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9e28a8d3-b355-3cf4-80c3-bea8c30a9c93 | -6.59741 | -59.11471 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfd38c6d-426c-3318-82df-e52abc9114f0 | -6.76813 | -55.65565 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3d020142-ea59-3aa9-83cd-66e54fc741a7 | -6.77644 | -55.66928 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89f5af4f-32f3-3907-99fe-be38adfab968 | -5.87848 | -57.77362 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 24f70f97-f216-3bea-8aed-4dfc3ee44e10 | -4.47577 | -55.40203 | 2026-08-29 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bb38d6f-e574-3a3c-a8c2-c9802f2d7150 | -4.92657 | -55.76952 | 2026-08-29 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64566c12-05c8-34fb-ba58-1489dd8e06f5 | -6.84233 | -59.93727 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80232ff0-d25f-3022-8973-0b5fca98154c | -6.16866 | -57.79562 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63ebfdc5-4f40-391e-a210-fc7956b709e4 | -3.53667 | -59.02372 | 2026-08-29 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22dfdd53-711c-3cbe-987a-28dc48e63567 | -7.50113 | -55.29317 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README61.md)
