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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1f29b7e-add1-3392-a316-036311f18c85 | -20.55995 | -56.1503 | 2024-11-14 04:44:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c94a480-4be5-39a9-8bda-7a211214ea16 | -15.8787 | -59.29771 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0374b1ef-9cc5-37ea-8459-aec7df296216 | -17.59565 | -57.47805 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| fa4717f4-a40d-3aa5-988c-fa5a279428fd | -17.24023 | -57.47226 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b2356e9d-47b4-30b8-bd73-5e1431977d2c | -17.58365 | -57.54405 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9b37b71c-3b5d-3582-a06d-9776b1923291 | -17.57561 | -57.54247 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d6f7229a-0ac0-397f-a8e8-2697703c012d | -17.60777 | -57.54884 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dbe12509-decb-3360-a6fc-2db3b745945c | -17.56958 | -57.52983 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| ccb790a6-e30e-3082-a727-a01fe751f403 | -17.58163 | -57.55511 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 7447623a-4226-3ca2-8c2e-df0d0962415f | -17.59498 | -57.4817 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2b6febfc-f1ee-3308-a27e-5ff65c623740 | -19.02441 | -57.62368 | 2024-11-14 04:44:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 57e6d9bb-5d8b-3d72-8ab6-6dd828c196a4 | -17.26842 | -57.47779 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 9d61120b-8481-3fbb-9c81-904c422f1d8e | -17.59504 | -57.55014 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| de72fff8-b780-35c1-849a-15b5c7912f4e | -17.57829 | -57.52776 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 22eeb467-85df-3fde-a446-61d55d224a1f | -17.29016 | -57.31223 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 663f6db3-541c-3598-8814-e3fe18f7d366 | -17.72202 | -57.49639 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 13441ba7-d0c1-3b63-9cc5-4cb9d5e75323 | -17.71076 | -57.5358 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| ffe0a333-1d09-39fb-954d-a1d5c7e0b61e | -15.88236 | -59.29535 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f4622c82-04ee-3a34-aca2-008d66462a0f | -16.00754 | -59.3857 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c52e944-1637-3a41-8215-d2b164a315f2 | -15.31192 | -56.5177 | 2024-11-14 04:44:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f28099b2-e59f-3d99-84bb-2bb407b5c783 | -15.41206 | -58.6054 | 2024-11-14 04:44:00 | NOAA-21 | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1eacc6a-1278-3e6d-a201-7ed6da38c024 | -15.87406 | -59.29681 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 54e6b5fc-2684-343d-b926-c85dfc6e2837 | -17.25031 | -57.46279 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| ccb14585-c8c7-3067-9b69-1706154ae09c | -15.87971 | -59.29231 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f95ea436-5f80-3220-964c-5fe6917dc433 | -17.70876 | -57.54682 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| abc147fd-ecb9-3f39-8719-607879461259 | -15.88989 | -59.28136 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe3fd7e-53be-3e6f-b742-b4a3f7b13ad2 | -17.58823 | -57.40513 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 522aae10-1c04-3454-9be7-9c394dc97711 | -20.69521 | -48.80042 | 2024-11-14 04:44:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e11fe7d1-986a-3898-a1ad-a261fe48a78e | -17.25902 | -57.48358 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fdf5beef-2e74-383a-aac5-10d850e64f81 | -17.591 | -57.50365 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 42139010-77ce-314d-90d2-cccc8d8396c2 | -17.24561 | -57.46568 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| bc0bfa63-a449-389e-9d58-5ba8816fc1dc | -17.59031 | -57.48456 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 2e13af0d-d005-311d-aba8-557e50ea9be9 | -17.70044 | -54.09072 | 2024-11-14 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b671b4a-5027-3d31-8874-b6c405d3a993 | -17.58965 | -57.48821 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e43fe9c3-ad4d-312f-b8e0-4160a33e5824 | -17.63609 | -57.44555 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5c64fab6-dc0f-3fc7-b174-9c16dad18e6c | -17.71211 | -57.55128 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| ffbec27c-83bc-339d-a491-5ab7bf5f7ddb | -17.63379 | -57.54722 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0d241697-9de9-3f65-a1b7-c522aa032c53 | -15.87666 | -59.29991 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3c6232f5-1ef9-3065-93ed-b63079bf6bfe | -17.25634 | -57.47541 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 0bf6071e-773b-3b50-bcd3-f70d8c95fd66 | -17.58566 | -57.55592 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 926c8ad2-7fa3-3525-a4dd-b2a6c35fc444 | -17.57026 | -57.52615 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| cfa1fb7f-0363-3f29-aa07-0dc60edf65d8 | -17.26439 | -57.477 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fab41346-3ec6-3590-a01a-93bc8655ff24 | -21.07779 | -54.22403 | 2024-11-14 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 573ea7a3-d1bc-3342-9648-381978be5b7a | -17.58757 | -57.40875 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4e131291-d61f-324f-8b33-ec0d2fb61bd9 | -17.23956 | -57.47594 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 82adccf7-b8d9-31ae-9784-3d10e5635d7d | -17.57427 | -57.52696 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| ded19825-80d9-3ded-89a8-9dfb958991f5 | -17.62977 | -57.54643 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d4ecf718-7654-36fd-8625-fab5e32cf3a4 | -17.71009 | -57.53946 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 6c204158-cc59-3e7d-94a2-6cb6daf3d079 | -17.27044 | -57.48965 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 977d7b32-7b6c-3cbf-b17b-04e52876120a | -17.59102 | -57.54933 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 15fa4b95-5f82-396d-92f1-a23944c1b29c | -17.58633 | -57.55222 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 3ac42002-dafa-335a-87c5-706c1b12079d | -16.10207 | -60.09706 | 2024-11-14 04:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 046a831f-aef2-3038-bf8f-651a85a33c5c | -17.58228 | -57.4377 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 94973fe5-cdce-3ab0-9914-4a73d335798a | -17.60365 | -57.47963 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 8ea85a01-95af-3a75-9ec1-91cd84f95df4 | -21.14686 | -47.83022 | 2024-11-14 04:44:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29f7fe9f-9d14-354e-afee-88ee395ed4b0 | -17.59965 | -57.47884 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| cad78a38-3291-31e1-bdd6-4d70f3cdc96c | -17.60352 | -57.41188 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ea1a88f1-bc6e-3be6-89f1-1c73b862488e | -17.24091 | -57.46858 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| e17cee10-c050-3570-bc0a-432b925a655a | -17.29054 | -57.4707 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6cf1c611-e0f7-3d50-886e-89c141ffaf8e | -17.70475 | -57.54602 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 903cbb78-538b-3be4-8a2b-b23b95415277 | -17.70741 | -57.53135 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 0c78fd57-4d35-3c37-a409-a799590bcafd | -17.59169 | -57.54564 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 24480421-e54a-308e-b391-90bf6bc987ae | -17.59763 | -57.46711 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e3cdb169-7b03-3c1f-a208-0121c9fa0798 | -17.59297 | -57.46997 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d716a00b-4a27-3ec3-bef8-e9a7ca0588a3 | -17.63486 | -57.44434 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d295e6de-83cf-3798-80ad-d94eb0d30035 | -17.59437 | -57.55383 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| f813ef45-0aae-366e-bd60-8bec77683259 | -17.57895 | -57.54695 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 6b62d163-c073-3306-8a63-3db129514602 | -17.58499 | -57.5596 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| ea46b0f1-43ad-3e9d-af50-d715a70c60df | -17.58631 | -57.48377 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 769e6027-f4f4-3d49-a145-fe07e8b253fc | -17.27111 | -57.48596 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b1aee8d4-3d4b-31ea-99c8-aa55a413dc2a | -16.94798 | -57.64439 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 657ce1bb-2444-341c-aa9b-39c920d95491 | -17.63515 | -57.53987 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e7a12e67-77c0-3e3f-b533-c573aa022465 | -17.58298 | -57.54774 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| cb61dd4b-efde-306d-80d9-e256cdca0f06 | -17.57293 | -57.53431 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e147a577-fd41-33f8-854c-d8393d5dca32 | -17.60375 | -57.54805 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| aa2cc563-bb64-398c-9bc0-a1419ca08611 | -16.18913 | -59.35846 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83b1851a-2df8-3402-b1a5-a843ecdbff41 | -14.49737 | -56.91576 | 2024-11-14 04:44:00 | NOAA-21 | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fafbd19e-8b8b-345f-80e4-bdf5fdbd6375 | -17.58694 | -57.43487 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f0039b73-d50a-30b6-87b4-a71f0a86a693 | -17.5937 | -57.55752 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| 4107062c-7cf8-35bc-97f5-8d9bcb42c934 | -17.5736 | -57.53063 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3a19699a-26ba-30df-bf04-a9aab61bb642 | -17.58958 | -57.42038 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9f91b644-6784-3b88-a682-1c912f8b5188 | -17.5803 | -57.53958 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 28c314e7-f13b-3ffe-9289-41fcffd6f27e | -17.59697 | -57.47076 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c5ec429c-1594-3e3b-9c43-f78916d442da | -15.89924 | -59.2827 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c69f1e4b-843a-32df-a9ac-b175baf408a7 | -16.94869 | -57.64059 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e61e8706-8cc9-353a-9700-3348a9c78489 | -17.58561 | -57.44212 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a374acac-fe99-3094-a18e-a128e8976ab7 | -17.61232 | -57.55061 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7d6463e6-651e-3829-bf64-fd90f25de82c | -17.6071 | -57.55252 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0c5a2b66-f8ca-338f-b254-2cfc29ad98cd | -17.60031 | -57.47519 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| aa42c1fb-1df1-3423-b807-82d06c7ff13d | -17.26708 | -57.48517 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| af55fb09-8d35-3838-8bc5-a2ccbe896c2c | -16.95136 | -57.64899 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9d197e82-b851-37ff-a54c-7f4d7d655cd8 | -17.81593 | -57.37556 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f08973a2-60fa-3c71-ba5a-edec821823e0 | -17.5923 | -57.47362 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 8fd4ba15-6c91-352a-82e6-e56dc4e73f64 | -17.59953 | -57.41109 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 79d0ac5c-2b0c-3786-b9e9-15f8cc73c44f | -17.70675 | -57.53501 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9b242f1a-8f11-30ed-8b8d-516e5d0f5a0d | -17.24159 | -57.46489 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b5a28828-e23a-32c4-97df-5f3d69b3987d | -16.07365 | -59.70916 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f19ff165-6c73-34b6-b926-bfce8b322662 | -18.72658 | -55.58008 | 2024-11-14 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e78f4e64-a375-363b-8161-3194b4ba1ad0 | -16.9494 | -57.63678 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| e076bff3-3011-3ed2-897e-45890b11b584 | -17.63447 | -57.54355 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |


[Clique aqui para ver as próximas entradas](README39.md)
