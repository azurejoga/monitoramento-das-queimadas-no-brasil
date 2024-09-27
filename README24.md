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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a943af63-5949-30ff-b8c1-d542f07cfcd7 | -9.69144 | -53.49586 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cacfadc3-ed26-3ea0-8536-a33b4442e5f4 | -9.66716 | -53.51823 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 198e41cf-9c84-36ad-9252-2c2d9dc02237 | -9.62627 | -53.23126 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fe356d9b-686a-3f2e-8580-efc094d9a999 | -9.59751 | -53.41577 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72db415e-7664-3cf9-a901-fd8ed77cd4e8 | -9.58914 | -53.29395 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8207f6a4-a31c-3af0-8cff-ab311f29f89d | -9.56581 | -53.3886 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc0877ea-0edd-342e-80a7-d3f0ad86fa1e | -10.44987 | -53.31812 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 80f083f8-44e8-3727-bfa6-04abd161178d | -10.44855 | -53.30893 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| c550404a-215c-37c4-8c9d-b4211dd0b52e | -10.43652 | -53.68082 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 94caf73a-620e-3b13-8616-d2c4f7f3fab2 | -10.0485 | -53.34618 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bba1d420-ca1f-3cf6-af6e-940fa74e585c | -10.04398 | -53.44713 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 7c335075-51a0-3748-84b8-24a04483223a | -10.04268 | -53.43795 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| dc402c67-26aa-3dbd-8da2-10a928726668 | -10.04153 | -53.49434 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 319e6182-05f4-3856-897b-474e69c94dfa | -10.04023 | -53.48517 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 106e97a3-b075-3d92-9870-ce9cf253b67c | -10.03893 | -53.476 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| de570a84-8a09-3724-a848-79f24b3d9eaa | -10.03763 | -53.46683 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| f4fd17d4-457e-33b7-b0f2-4c2f3e1432e0 | -10.03503 | -53.44847 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 144d0730-e941-3aba-9017-beb0ca36bcbe | -10.03372 | -53.43927 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f18479c8-898e-321e-b280-a6afcf933dfe | -10.03128 | -53.48652 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 7b9d1cf0-fe34-3dd6-ac37-8d8de7cf3820 | -10.02998 | -53.47735 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 164.8 |
| b38db9b5-9c02-38e0-93fd-9613c27e66a9 | -10.02868 | -53.46819 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| c7831633-8043-368c-a38b-94c26e73e9fa | -10.02737 | -53.45901 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1303142f-a835-3dbe-942e-513b8e6526d9 | -10.02607 | -53.44981 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| e083cc41-809b-35c4-b00a-7ba8b074401b | -10.02103 | -53.47871 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| eadccfb3-8907-3b2c-86df-4950f75fb966 | -10.01973 | -53.46955 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 17.9 |
| cf5481ae-28a7-34d5-a0b8-ac0cdb64e7d3 | -10.01711 | -53.45116 | 2024-09-27 01:24:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8378341f-8f90-398d-89ae-b8c5d45f98e2 | -12.264 | -53.44359 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cc89b828-dd6f-30f2-8607-53ff600900eb | -10.8133 | -53.73901 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b8c5cf85-c75d-3cd3-9826-c153e1abf0f6 | -10.77624 | -53.54096 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c4778d42-38dc-3431-8aca-8ed56b47c0d3 | -10.76732 | -53.54227 | 2024-09-27 01:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 64568759-ce2f-3cb8-8bd5-b34b3b7502db | -12.86231 | -54.02809 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c98e8a26-b9f9-3893-b13d-9bec42bcc851 | -12.86105 | -54.01906 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 69521940-f2fe-31d1-bb36-f02671be797b | -12.8598 | -54.01003 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b8541c7e-0af9-3556-bf70-8a7256f89b46 | -12.85596 | -54.04747 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 99be8e69-e505-3564-9087-9d245f5a7a54 | -12.8547 | -54.03844 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 13994f18-8703-35df-8b37-6b4e2a15ffa5 | -12.85345 | -54.0294 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 87d5e07b-d52d-3dab-a4bd-2b819d406181 | -12.8522 | -54.02036 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5002068d-b947-30f0-8083-4f6930e3fce4 | -12.85094 | -54.01133 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 29a8c1bb-879e-3904-a498-85660934cece | -12.84969 | -54.0023 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 982d5144-e569-3aca-b129-f0d1d77d733a | -12.8471 | -54.04878 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2026a7ce-d636-356d-b82f-8fad918664ff | -12.84585 | -54.03974 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 4aa71107-44d6-399a-b45a-d4548b8c2165 | -12.84459 | -54.03071 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 041069ca-bba2-3ec1-bb3f-fb7d8a167a02 | -12.84334 | -54.02167 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 71882f5a-04cc-3a3a-8c28-e1cab92b7611 | -12.84209 | -54.01264 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8265bdd6-4fcb-34da-8c71-5365a6afc119 | -12.83449 | -54.02298 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 93eb2215-83c4-3425-ba09-f8fa19da2e03 | -12.83323 | -54.01395 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 08148c6d-36b0-330c-a50d-649a7257b2a1 | -12.82438 | -54.01525 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cd0f3327-05ee-3008-9be7-c7477f6d378d | -12.82312 | -54.00623 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 74e8ecba-dba4-3c7f-bf41-c71c51b396ef | -12.81552 | -54.01656 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dc5c9b12-2282-3df7-8054-8697477c3f82 | -12.81427 | -54.00753 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0b401f68-1e5f-3d65-981a-a4ed6c31ed03 | -12.80583 | -54.02388 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 23a4a1d8-d949-3830-86c9-a3ac62349430 | -12.80458 | -54.01485 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b2048c2a-8377-35f5-b8a2-058770120735 | -12.79698 | -54.02519 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4eb7695a-a703-383e-8dc4-1f095e2d56df | -12.79572 | -54.01616 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d2f761ab-6e8a-3d49-b183-e41ce855a8ab | -12.78938 | -54.03553 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 689f4f3e-90a1-34ca-a5e8-aac5db212aee | -12.78178 | -54.04587 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8012014e-c11e-3e14-93b5-cd41886d2cae | -12.78053 | -54.03684 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bc593d83-e3a3-33c2-83bb-e6f194c98146 | -12.73365 | -54.08984 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 302239aa-1eec-38b6-be8d-1d0eb279f906 | -12.72267 | -54.08854 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23fd612d-de03-315c-b3c1-9334999b64ca | -12.72141 | -54.07951 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 70530323-a0ad-3f01-a9f1-029cff674727 | -12.71255 | -54.08081 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3f24f354-a26b-3ba7-bc8a-6b34058dbe46 | -12.7113 | -54.07178 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a6eec3b8-af93-30c9-a51c-dad2a695230c | -12.70244 | -54.07309 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 29583056-2248-343d-9ff5-8a95caf497db | -12.70119 | -54.06406 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 584ec524-3ca1-37ad-b685-592cb479c520 | -12.69993 | -54.05503 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 46c5037d-e525-3360-82ca-f36b9233c41c | -12.69233 | -54.06536 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0241d64f-349f-3875-b1a5-50a947c2185d | -12.69108 | -54.05634 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| c9acdc1d-6cde-3456-a1db-44e2c3f800f7 | -12.68983 | -54.04731 | 2024-09-27 01:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b8e7c32f-d8ce-3356-93c9-bae9aace0084 | -12.6063 | -53.18467 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2c67236d-3340-3186-9005-b1edcd5a9a81 | -12.60499 | -53.17552 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f2af2fdd-0366-391e-a753-5818bfc160b5 | -12.60369 | -53.16637 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b8d12be4-5b4f-31bf-b5bf-21b5f864b641 | -12.60238 | -53.15723 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae2d8255-37e8-3b51-bae4-fe749a44ebe0 | -12.59318 | -53.16483 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 87bfddbd-6558-3927-bf59-70f9eafa34f8 | -12.58427 | -53.16618 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ee04813c-16c0-3bbd-8504-acbcce99ae6a | -12.58297 | -53.15703 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a9ebb89f-6be7-332a-b34a-c2f35ba4c57f | -12.57536 | -53.16753 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 90ee2f21-ac6b-302c-9a08-e4edb96c0308 | -12.54876 | -53.50274 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| abca5f2f-801e-33a7-9f73-1feee6c32023 | -12.54732 | -53.16242 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b8e639d2-d470-3d79-92b6-b3135ac6051c | -12.54116 | -53.51313 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7c9b1d84-b6e0-3705-9bce-b1ee994faba0 | -12.53861 | -53.49502 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 79aa40e2-2eeb-3b06-bc85-f586374fd5b7 | -12.53841 | -53.16376 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8161af20-41c0-3925-8a1e-473e7262e36c | -12.5321 | -53.18341 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 34d47802-7284-360d-a7d7-f31546ecf48a | -12.5308 | -53.17426 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 87fd2e77-aa14-34d4-8409-85fdce9ed19d | -12.51832 | -53.47956 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d145f83-e98e-3179-9a6d-8ca779b835cc | -12.49042 | -53.47448 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d923b658-1f67-32eb-bd9b-405c0b70b8f1 | -12.48036 | -53.53149 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bd2378f-d8ee-365c-8e0c-df15ceea2cd6 | -12.47908 | -53.52244 | 2024-09-27 01:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ec16ebbb-db90-3797-97ae-f10e7b2e670c | -3.39094 | -53.7185 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c159196f-9ca1-3ef3-8866-cbfc2edae826 | -3.32992 | -53.22537 | 2024-09-27 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1fb46ecc-ed55-36cf-9e85-c42ba4320bfe | -3.30778 | -53.37315 | 2024-09-27 01:24:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9939e38b-eb93-3fa8-a4b0-a19e433ab9d0 | -3.30664 | -53.70622 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 399be063-b513-3adf-a0b8-fc978be33701 | -3.30523 | -53.69633 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ea11e8a6-678e-33ac-bac5-56acf15a7e14 | -3.29584 | -53.69769 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5c66b723-a482-3439-9d48-cbd065f89916 | -3.28646 | -53.69903 | 2024-09-27 01:24:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e49b9f1a-8794-3f5a-9e17-530a26a3d925 | -6.25227 | -53.28373 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1000aab8-c55b-36ec-9fb1-d9e4397b2b3f | -6.25088 | -53.27391 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e71d8ebc-14f7-3354-9d2a-97f55997fcd6 | -8.02371 | -53.17741 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dff8b528-63fc-3a05-a5ce-82d7c09968c5 | -8.02145 | -53.22656 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6d1e291b-d1fe-39a3-90e2-23dadba8ea32 | -8.00817 | -53.19944 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e6fb6c65-c272-31a2-bb00-7ac37f9a4f2b | -9.10092 | -54.66889 | 2024-09-27 01:24:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README25.md)
