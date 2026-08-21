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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5451beac-e83d-37ef-81f3-ebfdcd45d350 | -16.3262 | -49.4439 | 2026-08-21 00:00:00 | GOES-19 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| bbb5de13-4cb7-31cc-9b09-e1797d04683b | -7.3788 | -45.8344 | 2026-08-21 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 4df24018-429d-39df-8f2b-31613e1b37ef | -6.6939 | -58.9226 | 2026-08-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 294fbc32-c8c6-3342-a69b-c74d003b5220 | -10.3337 | -50.3829 | 2026-08-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9e2063ba-ad64-3a0d-9371-dce15b4562ab | -6.6938 | -58.942 | 2026-08-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.9 |
| d29df96f-2b1c-349c-92b1-bc371fa52ba1 | -7.7887 | -61.1626 | 2026-08-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| d2e97534-be47-30cf-9292-5889f89c8a9c | -3.5407 | -48.1673 | 2026-08-21 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 799eb4b0-507a-39d4-b00f-8998913e6120 | -11.1558 | -54.0233 | 2026-08-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 78c59332-27fe-340f-88f7-9e56bcb8b3fe | -6.7123 | -58.9412 | 2026-08-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| bc378d4f-9cdc-3253-947a-9a93d0473f48 | -6.5829 | -58.9851 | 2026-08-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 06a0309f-40c5-3a3f-a065-2378aa984867 | -3.9596 | -43.1038 | 2026-08-21 00:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d0e7a3fc-e207-319b-aa90-15ffd167dd6c | -9.0668 | -50.8841 | 2026-08-21 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f8e4be39-635e-3623-a124-15ee1e648bea | -10.7693 | -50.3162 | 2026-08-21 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 38a1cd23-a118-3c3f-9679-20442240b448 | -10.3151 | -50.3634 | 2026-08-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 4073d4af-0f52-3860-9470-c0d6747d9a58 | -7.7702 | -61.1634 | 2026-08-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0e0275ef-05d0-382e-8e98-b02f77996f51 | -18.7832 | -49.4409 | 2026-08-21 00:00:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 380b8ec0-feff-38ff-ab73-fc37c1b0cdc8 | -11.1747 | -54.0216 | 2026-08-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 280.1 |
| f5c50659-dddb-31fd-b348-959a1f886f3a | -8.3903 | -62.6963 | 2026-08-21 00:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9d8d4c8a-64ac-320d-ae8f-b0598f1364fb | -4.0943 | -42.5097 | 2026-08-21 00:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| ba6fb91d-e762-3ba9-bfcc-758468bb60f3 | -6.9516 | -59.028 | 2026-08-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 617ad8bb-599c-309b-bafb-611438d358b3 | -4.0944 | -42.4861 | 2026-08-21 00:00:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| eb233b9f-9ec2-3097-bca4-7afcedb597ec | -10.3148 | -50.3848 | 2026-08-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 6d2995ac-3e8b-3c07-9952-d02b4a48418e | -11.1745 | -54.0421 | 2026-08-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 01e0a51d-73a9-300d-9410-e2f15faa3739 | -18.1934 | -50.7554 | 2026-08-21 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 517fb533-db72-3039-8cfb-4dac69a64afd | -6.9517 | -59.0086 | 2026-08-21 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 37073aa3-9f45-3b0b-af87-46686e32f8e1 | -7.3415 | -45.8152 | 2026-08-21 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 00e856e4-6e3d-3b42-9598-9201200d108b | -6.2341 | -55.6109 | 2026-08-21 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| a66bc29a-6bb1-3940-ac6a-3cdba55c561c | -7.3605 | -45.791 | 2026-08-21 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 35ef666f-4833-34ac-976b-7c89281b26a5 | -7.7703 | -61.1443 | 2026-08-21 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| cee5eeaa-8bb1-31f2-b2c5-6f241b5d23d0 | 2.5982 | -60.716 | 2026-08-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b50c9301-d300-39a1-bafd-7a301f1e0de0 | -10.3159 | -50.2994 | 2026-08-21 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 6e615b90-429d-3d71-a69e-c4213072657d | -3.5406 | -48.1889 | 2026-08-21 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 241.5 |
| 1b2b1669-0c75-3325-b711-285120d43c17 | -7.3603 | -45.8136 | 2026-08-21 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 406.2 |
| 769cecfa-234b-3ee9-84ef-2279a096c5da | -7.3791 | -45.8119 | 2026-08-21 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 27f91d15-160e-3591-9b17-292d090050e4 | 2.5983 | -60.697 | 2026-08-21 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 8c4fc2e1-a1f0-3638-9dd5-2eed4ae1c2a8 | -10.7501 | -50.3396 | 2026-08-21 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| e6a2e5dc-8913-3f96-8fa6-f70dc671dc06 | -18.2134 | -50.7518 | 2026-08-21 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 114e955e-a183-31e7-8728-5aedb47470a8 | -7.3438 | -55.694 | 2026-08-21 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ddde8bbb-10bd-352c-b31c-a16198c7c2cf | -14.7346 | -47.1354 | 2026-08-21 00:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| b493b2d4-e4b4-3750-934c-36787aa2c584 | -7.36 | -45.8361 | 2026-08-21 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 217.7 |
| 5a02f6de-89b2-3d2b-ab16-843c2749f29b | -6.2156 | -55.6118 | 2026-08-21 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3a4bb8e1-c266-3ac3-883c-588744a6038f | -6.2155 | -55.6316 | 2026-08-21 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 7283fe81-8121-3ae5-9158-329d8dc9445f | -9.2071 | -59.771 | 2026-08-21 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3b0220ea-7481-3235-8971-00df3ee86b7b | -11.175 | -54.001 | 2026-08-21 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 306244b0-c5aa-336c-861a-f6323247225e | -18.1939 | -50.7332 | 2026-08-21 00:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5dbce688-8e72-3d86-a8f7-d09dced0937f | -12.5104 | -54.755 | 2026-08-21 00:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 7ccf571b-d69b-3d2c-b8a1-0f2c0b8b8981 | -3.5591 | -48.1882 | 2026-08-21 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5d93b4e2-80a5-3cf0-89fd-03eee0ac7225 | -18.2139 | -50.7296 | 2026-08-21 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a0e78987-6b3d-35e9-acd7-83e18c66d857 | -7.3603 | -45.8136 | 2026-08-21 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 534.6 |
| 4b3811bb-e941-3ba7-ab7a-bff4d64fa6fb | -3.5407 | -48.1673 | 2026-08-21 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| a28478f1-5723-36af-9042-d4bc379cbc9d | -10.7501 | -50.3396 | 2026-08-21 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 8c59eace-953f-3985-b156-fe4644dc6619 | -7.7887 | -61.1626 | 2026-08-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 8a8fe417-337f-3af0-8d55-d3eee41dfdd2 | -6.2341 | -55.6109 | 2026-08-21 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 179.0 |
| f07ab1cf-55bb-32f9-8eff-910c6dd737fa | -7.3791 | -45.8119 | 2026-08-21 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 5ba79a88-26fd-3a13-a9a8-39ab4d6d6624 | -7.7703 | -61.1443 | 2026-08-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 496f5f82-a2ff-396e-a923-c30be51e5470 | -7.36 | -45.8361 | 2026-08-21 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 4903db0e-1291-3f60-881d-d7c1cad208cf | -6.5828 | -59.0044 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| d05b2231-1c0e-33be-aaa3-fe2c432f9054 | -11.1936 | -54.0199 | 2026-08-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d47e91e6-ce42-32a3-b327-651a40fdfd14 | -11.1745 | -54.0421 | 2026-08-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c4fdefcf-3932-3eb2-829a-4638b28f02db | -18.7832 | -49.4409 | 2026-08-21 00:10:00 | GOES-19 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| c318db05-1986-3901-917e-6a711e6670ed | -10.3159 | -50.2994 | 2026-08-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7413223c-f93f-35a5-a295-a9168718c250 | -10.2595 | -50.2838 | 2026-08-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c394ccd4-951d-39ae-80b7-1996cf79df7f | -10.3337 | -50.3829 | 2026-08-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 25e9501d-b76e-39e9-b548-c16ccd3a7349 | -3.5221 | -48.1896 | 2026-08-21 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 66abb944-8b44-3b85-8919-a70f75f252ab | -7.3415 | -45.8152 | 2026-08-21 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 682d632c-3fbc-368e-af3a-3e09aab3f639 | -7.3788 | -45.8344 | 2026-08-21 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 065500fa-4075-3df3-a138-6214f2c2f1f3 | -6.9333 | -59.0094 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 73cb3d90-16ea-3a21-a942-7596939dbbdb | -14.715 | -47.1387 | 2026-08-21 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9f0944af-47da-36c7-8056-9592ee6b264d | -6.8202 | -59.4194 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 1f255a0e-17a1-3828-9876-3105f601454d | -10.3162 | -50.278 | 2026-08-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b1af6b22-5e99-32f3-a301-91822f293315 | -4.9423 | -55.7837 | 2026-08-21 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c340cf9f-1fc7-3a1f-bc76-0663a8af73fa | -10.2592 | -50.3051 | 2026-08-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| ed50b933-1415-3432-94b1-fccb6820c1b1 | -6.6939 | -58.9226 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 26990fd3-f595-3e4b-b7a1-51a0b1a261ab | -6.9517 | -59.0086 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 3afe7e8b-0ded-3cbf-81bb-5d4014793337 | -7.7702 | -61.1634 | 2026-08-21 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 2f038a95-e693-32ef-b3c0-cba6423b59e7 | 2.5983 | -60.697 | 2026-08-21 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 5a542422-4a58-3367-ba27-619097a4abae | -10.3148 | -50.3848 | 2026-08-21 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 12f7a5a5-ecf6-30f6-b161-6c513185d21d | -18.2134 | -50.7518 | 2026-08-21 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 97e15183-dac1-3867-97b8-84d010d3d884 | -6.2156 | -55.6118 | 2026-08-21 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 627f2fd2-7462-349d-9672-15f2f759cd37 | -3.9596 | -43.1038 | 2026-08-21 00:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 975fdc6b-0401-30c4-9202-c77df41e25be | -6.8387 | -59.4186 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.4 |
| cd1b554e-b7b8-3cdb-93f1-66b4dbfeaa20 | -18.1934 | -50.7554 | 2026-08-21 00:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 13475667-59d0-366b-8797-9973a4292624 | -16.4007 | -49.6307 | 2026-08-21 00:10:00 | GOES-19 | CATURAÍ | GOIÁS | Brasil | 5205208 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| bac326a7-ed9f-35ed-832d-68e4e10bde20 | -6.2155 | -55.6316 | 2026-08-21 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 008b5d97-6087-3007-800c-2a6cadfb33fb | -6.6938 | -58.942 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 21210530-abfc-3e9d-a4b5-a3a11fc75373 | -11.1558 | -54.0233 | 2026-08-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 2e7a79be-b524-3ba8-9eae-62786d6cc715 | -4.0943 | -42.5097 | 2026-08-21 00:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 3eed2123-d70b-3b41-9f82-fe53a6ad6211 | -6.8388 | -59.3993 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 1ca6d611-4375-3c74-af56-a6748e76c1df | -11.1747 | -54.0216 | 2026-08-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 239.7 |
| 6fa81f00-fd2a-30fd-8cfe-cb2fe5cbf2fa | -3.5406 | -48.1889 | 2026-08-21 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 032d61cf-e316-3c64-b60f-f1a3a78f7477 | -12.5104 | -54.755 | 2026-08-21 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 3cdaccb3-00e0-342b-80ba-1d0a5883a6bf | -14.3343 | -51.8944 | 2026-08-21 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0437a01a-a292-3dfa-865a-03658f6006c8 | -15.7156 | -47.781 | 2026-08-21 00:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 52.9 |
| a12d257f-af59-3049-ae41-52af1e5921cd | -14.3339 | -51.9157 | 2026-08-21 00:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| f8902b66-5e0a-3ef5-8370-7db513649d6e | -6.5829 | -58.9851 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 5164746a-d54e-3eff-accd-2dd94b2cb0fc | -6.9516 | -59.028 | 2026-08-21 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 05328319-7245-37b0-ba0d-391f48cbaf12 | -11.175 | -54.001 | 2026-08-21 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 07b42840-8d59-35e3-993c-e4f653726ef8 | -7.4509 | -46.1469 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c187f89-8d1b-3073-9ff0-0104c6aac9d2 | -10.2934 | -48.227901 | 2026-08-21 00:14:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b40ee6a2-bfc8-38b5-8a61-abd4cafd6306 | -7.345 | -55.664398 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
