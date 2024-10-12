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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83063b7c-2b6b-3430-9879-fa0df68334ce | -12.27007 | -47.65064 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6646392a-86a8-3f67-845e-bd05c0865673 | -12.26793 | -47.63959 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8a2bc28-67fd-3dc6-9512-0f895e23389d | -12.26703 | -47.6447 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb33f35c-4c19-39f0-ae4e-22551e2b7223 | -12.26612 | -47.64991 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c720c632-898b-3a07-893b-c85f1c152c91 | -12.26399 | -47.63885 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0514d63d-c4a0-37ed-b25c-43fbdec10218 | -12.26309 | -47.64396 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1f30ee1-cb4c-35e7-b8a2-9bd5ac6e2115 | -10.67663 | -47.67494 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ebe56d3-b2a7-3cef-8cef-757b29c7a426 | -10.63066 | -47.84494 | 2024-10-12 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ad55745-4bbb-379d-b363-409d422e4d6f | -10.63005 | -47.84849 | 2024-10-12 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef7c16ff-a7d9-3f92-90af-17e608f3cb5c | -10.47424 | -47.66154 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfac1643-d7f6-35ea-bd5a-5d5c3aed91f2 | -10.47407 | -47.66107 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d26d79d8-4a1c-3849-bd6a-c4c2b028ce06 | -10.47363 | -47.66512 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d42b68e-704d-3b08-8772-32af6bbd0fe1 | -10.47344 | -47.66464 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f29b5b82-0094-392a-b54d-cc676948f8f3 | -11.72467 | -48.94182 | 2024-10-12 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc1de435-6b34-39b7-a0ad-23653ae47f2f | -11.21018 | -47.85191 | 2024-10-12 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c45d4449-6d06-34c1-9695-03cd406e2ff5 | -11.20612 | -47.85117 | 2024-10-12 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74b03213-634a-300b-aa10-6167a761a86e | -11.20331 | -48.20304 | 2024-10-12 04:08:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ee3631a-9786-3b8e-aea6-b4b9043ec0fe | -9.57297 | -55.80064 | 2024-10-12 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2752ef5e-c9c9-3f87-bfd3-854dd941d6ea | -9.57204 | -55.80007 | 2024-10-12 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f4e58036-50f4-374c-bfae-648937d37c8b | -9.57165 | -55.8073 | 2024-10-12 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ebee62cc-601b-31e7-a800-e521e7d9069d | -9.57068 | -55.80671 | 2024-10-12 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 957275a6-da30-38f9-9d26-0598b49a7e15 | -10.4795 | -55.58533 | 2024-10-12 04:08:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e680ba46-95bf-370f-a895-80c47f7acba6 | -10.47277 | -55.58391 | 2024-10-12 04:08:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cb464c3-7bb6-3363-a102-37f90aa767b7 | -11.76359 | -56.33465 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3340607c-bd5e-303f-bbf3-3dc67196d5fa | -11.7629 | -56.3393 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 073246ca-9ea7-398e-b9b2-5bb6b938d5e9 | -11.76225 | -56.341 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be4a39a1-c630-3569-9331-1e317fec8097 | -11.76158 | -56.34577 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a601cb45-94b5-3821-9b27-24190dba8ea5 | -11.76089 | -56.34748 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 476ec080-c5f2-3849-b32a-739bba8e0f91 | -11.76025 | -56.35229 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1c3526e-57c7-3bea-8729-544f0d391efb | -11.75731 | -56.33157 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac0b291e-0042-3337-8a00-5bd3cddd4ef3 | -11.7567 | -56.33329 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b5a8d99-c8e3-3e24-ba2f-4a24a049c7be | -11.756 | -56.33797 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acbe1729-f9ea-3ff7-ad9e-af06ad377716 | -11.75534 | -56.33971 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b68c678d-a610-3b7f-9523-7542467d5d5a | -11.75467 | -56.34449 | 2024-10-12 04:08:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68fba524-2187-3a2d-ae0d-3927f19a5bc3 | -14.35349 | -57.61215 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e13520f1-3e9a-378b-9ea2-af35f3aa8412 | -14.35043 | -57.6094 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2e50d0a4-2773-33ee-8cde-c31285782624 | -14.34703 | -57.60787 | 2024-10-12 04:08:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e6fe1bb8-a199-3665-8cbe-0a0583e6ea91 | -10.54735 | -49.94992 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac8b892c-0f10-34c4-8f16-b512e68fc0d5 | -10.54187 | -49.10899 | 2024-10-12 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce862495-fa0c-3c5f-a7ad-4b7f130a5b7e | -10.54027 | -49.1071 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e97e2b4f-8556-3c63-b123-f2b5fbea8e6d | -10.53741 | -49.10814 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a62af69-c045-38dd-ae13-395b6b87ef11 | -10.53581 | -49.10627 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a9d24b4-098e-3f54-a71c-d317eb5a2154 | -10.53497 | -49.11083 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b40f7b3e-165c-3107-803d-b4dcaf21561e | -10.53295 | -49.10728 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1b75060d-db18-3ab7-aa42-86ec0148ae53 | -10.53214 | -49.1119 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 754d0b19-041b-361c-991a-a5d821ad9279 | -10.52769 | -49.11103 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 977ce250-760f-3861-86fe-1be1145ecbc7 | -10.51247 | -49.78452 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e62f6cbf-e79e-3475-9fff-c5f73efde6f6 | -10.51157 | -49.78952 | 2024-10-12 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e121000-5546-3a3d-911b-6371bcb33400 | -11.20582 | -49.93524 | 2024-10-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e35111-b60c-3bbf-8b49-d5e790b57917 | -10.86679 | -49.7466 | 2024-10-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dc7af91-8871-3330-9bb1-dd4d41484f95 | -11.25908 | -51.43419 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eef3bf0b-6d01-3a25-89b7-3067d4930118 | -11.25452 | -51.43004 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22fd370e-582e-3ae4-816b-7a8e5242f337 | -11.25393 | -51.43317 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5bb3873-d17c-376f-b1a3-bad21d4edd58 | -10.69289 | -53.02438 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef3dc7c3-889c-3551-839c-69cac784ab4e | -10.6928 | -53.02255 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed157f52-52e7-32a2-a259-e840537f6ac4 | -10.68715 | -53.0232 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 944cb17a-0a71-38cf-ae1c-6ba72e5e527f | -10.68706 | -53.02133 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f7c8581-3c6e-329f-afd3-8bcd896361c6 | -10.68633 | -53.02735 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 202540fe-6b6f-3fad-863d-b109c0ffc900 | -10.68627 | -53.02549 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c46e0f86-9ca2-365b-a243-5009933e6f42 | -10.61108 | -52.82899 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a283dc7c-6bf8-3bc2-890e-08375970be76 | -10.6094 | -52.83017 | 2024-10-12 04:08:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efdc457e-6ff2-392a-a88b-f1c05a710fe8 | -12.89412 | -53.52117 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 144cf84d-a96b-3ac4-ba95-d0bf37421b12 | -12.89328 | -53.49567 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8f00ebb-e271-3e2e-a277-1fd93696d7b5 | -12.89246 | -53.49976 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d552e8a9-27dd-3f16-99a2-b85e8a973ba0 | -12.89164 | -53.50386 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3441b68-3fce-3d0e-890f-ca9dd9316402 | -12.89083 | -53.50789 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e736737-8130-309f-9604-efe86e8845f3 | -12.89003 | -53.5119 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e6c78ad-d458-325b-b3d0-03a4e366e291 | -12.88922 | -53.51594 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d52e0a0-27c0-3361-8a2e-36e8b50cab73 | -12.8884 | -53.51999 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 680c757b-ab34-3639-a16c-d076594d9f44 | -12.88758 | -53.52406 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f8d427a-19c9-32f6-ada4-0b56a0d24e0d | -12.88677 | -53.52815 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a10a11c1-833b-3ff1-af27-9c5a0a98fc33 | -12.88676 | -53.4986 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78b6af2-392f-375b-b02f-f55324128ea3 | -12.88593 | -53.5027 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd74a91d-7f68-3b71-81b6-5470fcd9e672 | -12.88512 | -53.50676 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d79a0323-35ac-3455-9a39-f66a959c1837 | -12.88431 | -53.51078 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 743b54eb-21aa-3cc9-b35a-41eef4c70306 | -12.88349 | -53.51483 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd68ce47-2fca-3184-8458-eb0b60734191 | -12.88268 | -53.51887 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c28f3d0e-0f01-3503-a8c9-bd3bc8f7e52a | -12.88186 | -53.52295 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddda63dd-f56e-3a0d-933a-886964963090 | -12.88104 | -53.52702 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee296f99-347c-310e-80e3-d645b42b969c | -12.88023 | -53.50151 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8db3b25-d42a-33f4-b90a-53345efc59cc | -12.8794 | -53.50561 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecc164df-f394-3ead-bef5-228a2e66c231 | -12.87858 | -53.50967 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f86bba12-a397-3d17-91f9-94b9785ef129 | -12.87776 | -53.51374 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a291335e-a0fd-3bf1-b39f-9a4107f9f737 | -12.87695 | -53.5178 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6779f55-f8c3-3793-99c5-65b6c3ba40ec | -12.87613 | -53.52187 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6893120-6cc2-3958-8a18-4698ec2e580d | -12.87371 | -53.50436 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe193141-d607-3c23-98c8-8b5c29f5ca4e | -12.87287 | -53.5085 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6322a28a-f9ba-3330-bf4b-af66a406679f | -12.87239 | -53.50576 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f5d35ea-7493-381b-aceb-09d136312c5c | -12.87158 | -53.50994 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2121b530-0fed-335f-a40f-e80deca2f689 | -12.86803 | -53.50306 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06e49c4-9bd3-39dc-8fcc-43a479948f48 | -12.86719 | -53.5072 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa64057-8129-33f9-8aaf-df4969415040 | -12.86635 | -53.51133 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9736800-d029-38e4-bd2d-578441ea2842 | -12.8659 | -53.50859 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64abc712-67d7-3071-92c1-432b997d2ea9 | -12.86552 | -53.51544 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db8005bf-4b0a-37f5-8ce0-af85ccc93e5b | -12.8651 | -53.51272 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa6024b1-3c64-357a-a903-babf6b0e1189 | -12.86429 | -53.51685 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df37f014-ac40-3349-9371-3c7200be8384 | -12.86385 | -53.5237 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e82a97b-df0e-3ad5-841c-1420a69d67b3 | -12.86348 | -53.521 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff9028bc-ffc1-3512-8a5e-029f2a56fd0b | -12.86267 | -53.52516 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bfcbf93-fb94-3dc8-9bb1-beaef8864b6e | -12.86068 | -53.50999 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README51.md)
