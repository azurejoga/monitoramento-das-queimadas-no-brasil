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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20694d74-934d-31e7-9588-ee0339405040 | -12.5871 | -53.14086 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d6e0cb-05f4-3f50-b972-32ef071999e0 | -12.58301 | -53.14012 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53e49e87-71ca-3433-9b7b-96946be4faf2 | -12.56727 | -53.13354 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7590cf6f-78e8-35c9-ba2c-c61de9be1da6 | -12.5666 | -53.13725 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ea75bb03-c64d-31b3-9d83-069627657a22 | -12.56352 | -53.13685 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 227a60fe-1673-394c-9171-3a4bf68eed64 | -12.5625 | -53.13653 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2728251f-aed1-3893-9ca8-48b71fdc08dd | -12.55942 | -53.13612 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 87026630-7f50-3ba6-9369-de0907c175f6 | -12.55877 | -53.13983 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5a0972a7-cf20-3ebd-8b35-1fefddcb79f6 | -12.5584 | -53.13581 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00a7e8c1-6f96-3896-b52b-e7be6d042b7b | -12.55772 | -53.13951 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98450178-9871-3963-b5b6-449dccb960cd | -12.55532 | -53.13539 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 042f8756-5e53-3b8e-9997-173805fa2caf | -12.55467 | -53.1391 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2cbb083b-f383-376a-ba40-00afcc8f4c72 | -12.55057 | -53.13836 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cfcc4e3-67c0-3a69-8052-849444b6d988 | -12.54647 | -53.13761 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b12754f7-35ab-3445-b181-3d137cc44aa6 | -12.54288 | -53.10988 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c64b614-42fc-3352-a871-40dc11b11864 | -12.54238 | -53.13683 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f0649a0-ada1-32bc-b743-e1823e6778a8 | -12.54222 | -53.11367 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 02728245-5c9d-360b-b22e-6c060b73d3a8 | -12.53813 | -53.11292 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3aefc70e-de57-3a8f-a2ef-a5b6ff8c8a14 | -12.53747 | -53.11667 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ebd43360-43d8-38f6-bf30-39d160c5f680 | -12.5347 | -53.10838 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1195689c-08bb-3a77-b8b8-78385b01ff8b | -12.53403 | -53.11216 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b98ed70e-8016-385e-aeea-dbdb36641e91 | -12.53337 | -53.11591 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cef3528e-7643-3676-a57b-80cbaa212543 | -12.53271 | -53.11965 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2704d7bc-28c6-3737-a00d-1a59d2775a46 | -12.53061 | -53.10762 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d20e7a3e-6e49-3e3f-b837-710e202fbd93 | -12.52994 | -53.1114 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1413ad8-f4fc-3b6d-90b6-69e5cba2ccf2 | -12.50004 | -53.13693 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 184d4368-3f3f-35e4-9bfe-48363144dc3c | -12.49938 | -53.14064 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 614c1ca0-a7fa-3da0-8022-bda6b3081c9d | -12.49872 | -53.14434 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 67467097-20b0-3b15-a83e-a660b6f869e5 | -12.49594 | -53.1362 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bee50efc-129b-3390-bd4f-7bc517c2abae | -12.49527 | -53.13991 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cfc4ee12-ca6e-34e0-9af1-b31ddd9b3b90 | -12.48648 | -53.1654 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 538e354b-add5-3ed3-a2ba-44064a8610f8 | -12.4858 | -53.16919 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fc97901-7146-3673-867d-6fc4a46ab4a4 | -12.61078 | -53.49426 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e864ebeb-af3b-39b2-9d93-d367f2f2e8a3 | -12.61005 | -53.49823 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af4abed4-bcd3-35cb-b571-59a3ffa1b4af | -12.60984 | -53.49473 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07ac1790-eba1-3fa2-be6f-0b2163a5f6b9 | -12.60915 | -53.4987 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81e925fd-6715-306f-956b-9533c4a34d05 | -12.60659 | -53.4935 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 818001ed-60c4-3e9c-85ab-49ce3fd6f8be | -12.60586 | -53.49747 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74a172c7-50c6-365a-b783-91de350002aa | -12.60565 | -53.49396 | 2024-10-03 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 812612bf-c979-393b-8799-e0814754c963 | -6.57743 | -52.92591 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8ff1774d-eb1b-339b-afd0-9a2275e8083e | -6.56252 | -52.93252 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99dc259e-72e3-385d-96d9-09a83d0baf08 | -6.55805 | -52.93174 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d96370b-df70-3f5c-98ed-bad4d7c7be73 | -6.45202 | -52.83677 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 207dfd82-539e-380d-b9da-ff1cf04377be | -6.43644 | -52.9814 | 2024-10-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe498058-5eac-324b-9e04-a9d5e15eba35 | -8.52412 | -54.77705 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b13d1e41-1aa5-3381-80e2-9f6dc1622e6e | -9.65307 | -53.58544 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 628e20fb-2ad5-3844-aaae-5cf16efad01b | -9.58468 | -54.63835 | 2024-10-03 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc3b71d1-2cb8-3512-b6fb-78107cbdb77e | -10.52528 | -54.59367 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3caf12ae-753f-3fee-821d-ee41bbd4d3e7 | -10.52438 | -54.59871 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8062031c-9282-3158-afe3-8828a54dd987 | -10.51971 | -54.5978 | 2024-10-03 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c10b4226-352b-37ab-b22a-1eb6fdcfd5fc | -12.32018 | -54.11042 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad56dc5d-5044-391c-b95f-4364411fa99d | -12.15051 | -54.26679 | 2024-10-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb75e53c-77d5-3628-962e-60aa64198a30 | -12.14969 | -54.2712 | 2024-10-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eb726827-273f-3853-990b-5eed2db41a2f | -12.14803 | -54.26352 | 2024-10-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b2b58908-3932-338e-a027-62442e2e3877 | -12.14725 | -54.26793 | 2024-10-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a1094c6-c24c-3149-800d-af5a2a7433ac | -12.14606 | -54.26598 | 2024-10-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 012b89e8-1355-347f-96ad-8618238dc4f4 | -11.23287 | -54.18086 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3569c0c0-6068-3f8c-9441-5b65963e96a2 | -11.03059 | -53.99419 | 2024-10-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4fa60247-7adf-3a05-80ea-98d06e35360a | -12.44577 | -54.46239 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76bbe65e-97a7-3021-a7b7-2d02f86c59bf | -12.41997 | -54.41232 | 2024-10-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0840d5e-3bb1-33bf-85ba-179ec764eeaa | -7.33414 | -55.08129 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a19903bb-ec62-3e14-a681-a467de87e872 | -7.33091 | -55.08295 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c583a0d-4e76-3fff-ae32-bc9d01e186b5 | -7.32846 | -55.08353 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cfffc59-1558-3d88-b49f-03cf2354ae10 | -7.00143 | -55.12407 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ef4b27a-52a5-3126-9dfc-9e580ae48847 | -7.9144 | -54.74932 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f11ff1a-acba-3504-9f4d-979ea51c67d9 | -7.91342 | -54.75494 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1298b5ed-652c-30d3-90e9-5e26e7f1ebd4 | -7.91141 | -54.74464 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da1c6c21-c5ce-3dcc-ab92-b60aa8fa3508 | -7.90946 | -54.74842 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fbd89041-87ae-3b6e-af2d-ca5c471e3d75 | -7.90937 | -54.75583 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05b32feb-7f26-3952-904c-7a9d8809683e | -7.90355 | -54.75309 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfca46ed-5e77-3ee9-9ff8-fbadd5cea457 | -7.90257 | -54.75871 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a3125f1-2599-3c44-a133-fb6d029f3dbb | -7.89762 | -54.75785 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad170635-aaa7-3133-afc5-b4fcb54024c4 | -7.61508 | -55.16335 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16aa7633-c712-3c87-8193-349b4b3d6615 | -7.61455 | -55.1664 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8af6bef-18b1-312b-b53f-d5dd49c0d653 | -7.91532 | -54.75113 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3936e2c3-73f6-340e-9f26-92bfc1b2fbb6 | -7.91039 | -54.75023 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| acea703f-1884-309c-8451-87a092acb648 | -7.90849 | -54.75401 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96a9e200-5de5-380a-8b97-159628f5d8f1 | -7.45198 | -55.41435 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc4b5a29-9b62-36cb-8c0b-247fcc1182a9 | -7.44675 | -55.41352 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cf03991-9662-3588-8689-f2e0366c2fdc | -7.44239 | -55.46861 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b025ba0-b309-34db-b94c-233af2fd61f0 | -7.40628 | -55.4293 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b40c5e29-209a-3b26-8487-4c0cd842a30f | -7.40571 | -55.43249 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36e1a322-d344-39ff-a7dc-f608d64d0f5e | -7.37662 | -55.50392 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec7074ee-ac7c-3e3b-b4f0-c7e888ac97aa | -7.37603 | -55.50715 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e6eed30-d77a-3bac-a6df-5eab861d60eb | -7.37545 | -55.51038 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92d2a8cd-e0a3-3344-852c-03e823f414f5 | -7.33356 | -55.0845 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a720c64e-59fe-3b32-862f-260cc5700887 | -7.33146 | -55.07975 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a034dddb-8184-3e57-9349-8354824c4162 | -7.32904 | -55.08038 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54a0de39-3e26-330a-84b8-f4cdcbd7a356 | -7.32581 | -55.082 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c4ec7bb-a757-3dba-a5dd-df031d912b28 | -6.65203 | -54.95202 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fb6b8e6-bce5-3006-a014-6bb6097cc6d9 | -6.64689 | -54.95127 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c7fe6621-fcbb-38af-91b8-c6a76f0a994d | -8.60037 | -54.9856 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0b592ae-bd82-371f-b375-b75be19a7a6d | -8.59987 | -54.98843 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a4704b2-3d2b-3653-81b7-1c60367dda0b | -8.48256 | -54.98124 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bfb02cf-52da-3a03-a2a3-7469513b80c9 | -8.44435 | -55.47146 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2246b43a-3577-36a7-b7a3-71e01432bc46 | -8.44251 | -55.47004 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e7c46c3-78f1-384b-b617-bd9d40d182d2 | -8.44196 | -55.47314 | 2024-10-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cd728e4-d134-3fb0-bdae-e4c089297d26 | -8.30723 | -55.09422 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f91e12-5b01-30cc-829b-72a24c0c08e5 | -8.17261 | -55.15913 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76df2ecf-dfe8-31dd-a712-af2dd985bbbf | -8.17208 | -55.16216 | 2024-10-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README99.md)
