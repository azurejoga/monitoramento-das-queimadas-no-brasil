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
| 24511428-a0f1-348e-a536-03cf369f8d12 | -7.88107 | -63.01947 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 89909b0c-29fc-357e-94dc-abe496bcc45e | -9.09591 | -65.71961 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a69749d-f6b4-3a68-b0ae-77eaad40a415 | -9.09534 | -65.72427 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5bc486a-fca4-36db-ad48-329d305c20d4 | -9.03193 | -65.73247 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8062a224-7f8e-33af-8062-e9aab7fa3037 | -9.0947 | -65.73074 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286f1fa9-a9cc-3ca0-890e-3156162d1175 | -7.3831 | -64.35394 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 35f9d313-69b9-3344-b465-0cb1665913ba | -10.4202 | -64.38789 | 2025-08-26 06:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69a27851-2625-3dd6-83b9-8eba3f284dfa | -9.00691 | -65.39598 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 307222dc-0424-3be4-8299-2d3a3fc2e4b7 | -8.99183 | -65.41418 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e023126-d903-3d1d-a908-d0a51b063e14 | -9.04419 | -65.73439 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8c7f855-bcaa-39bb-bb0c-af616f61258d | -9.09591 | -65.72146 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7656e9e-fe27-35a6-9bea-833c10cb3130 | -7.39624 | -64.34971 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 427cc8dc-6a88-3353-a2ca-6ee6a51f2454 | -8.97804 | -65.42239 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b2a7e72-0cff-311c-97de-641a1fde6889 | -9.0176 | -65.69721 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12bd0462-9348-3328-868b-279fa7f35efc | -9.01383 | -65.39178 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91201944-1a67-33a4-8d98-b555fe891fd6 | -9.80589 | -64.2575 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 338ec0eb-047f-333a-8666-e49874e0f3fb | -9.03806 | -65.73344 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc8c67cc-be5a-37fa-bd1d-b3631c35dc9b | -10.42095 | -64.38166 | 2025-08-26 06:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4afd2537-fb1a-3f48-a318-830046974250 | -9.01783 | -65.70013 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 026a7177-f966-3181-bc18-53b9aa512815 | -9.00627 | -65.40093 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 933cd447-a774-3e30-8b17-48cb1873c1fd | -9.07148 | -66.06538 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b8b26a1-c400-3f14-9b02-dfcf4e8f0495 | -7.3817 | -64.35907 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 423e5bf8-685d-30d5-bd2e-5aa527596359 | -7.3889 | -64.36039 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56847d21-01f2-34af-8eb8-a83120c78697 | -7.38965 | -64.3548 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 967cb7bb-f18f-32b2-a9f3-5e3d6731cb25 | -7.37655 | -64.35309 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2ccd54bb-60e1-395f-b1f2-bacd8b18f0f2 | -9.01104 | -65.70412 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81a8abaa-221a-35c4-9679-e9c031713185 | -7.39041 | -64.34922 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 197dac8b-ce84-3daa-832c-0339557a23ea | -8.98493 | -65.41828 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0dc3dd26-9ad9-342c-ada7-1b48a0886e99 | -9.0 | -65.4001 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75cfc1c6-3804-3c7f-8e61-52e6145b742b | -9.02697 | -65.72226 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ba7d9caf-6c1a-3c2c-976c-247908e28ab1 | -7.88908 | -63.01339 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3fa9730f-39e2-37dc-a6a4-7a3ffe8fb6d4 | -9.0448 | -65.7296 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 264b982b-9451-34f6-be12-f9b65cbd7e80 | -9.01847 | -65.6953 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d893928d-4659-3540-8891-b44534c34500 | -7.37586 | -64.35262 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fbbb1743-83dd-3536-bd6a-1d1b121a50d3 | -7.38824 | -64.35998 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90915ca2-8e55-320e-996b-2fd6af3abebf | -9.03867 | -65.72865 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bda4804-52ea-3f40-9e2a-b35d8bc3264d | -9.0577 | -65.72658 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1737c138-7bb0-375c-a372-d430e1235186 | -9.02316 | -65.7028 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ebbb5bf-5267-3858-ab24-6f2188a358b2 | -8.97992 | -65.40756 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bb8878e-5327-34f9-8d64-1ad5bb602362 | -9.01084 | -65.70123 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed2176e-a41c-3f0b-9ebf-626b0f9d4e13 | -7.88194 | -63.01249 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 417142e2-9ebf-3983-b12f-ae189c84aa72 | -9.07737 | -65.71957 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7c52f135-d8e6-38e9-a742-5c0e0458244f | -9.02011 | -65.39256 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d004f078-b917-3eb5-ba30-c17483824dd3 | -9.79838 | -64.26279 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ac9d452-27c4-33b3-9d1b-7a57542f6d09 | -8.9824 | -65.43815 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2f246bd6-074e-3d76-a084-45036eb41731 | -9.07617 | -65.72887 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d55fa0e-47fd-3e58-83bc-e53c5dd72c4d | -7.87856 | -63.01248 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e026aeb3-312e-338a-b1e2-e69b7c46ba68 | -9.02578 | -65.7317 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6b02e34f-833a-326b-89ff-23c784e644c9 | -9.04541 | -65.72481 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60440d86-80af-33ee-86dd-96f16772585e | -7.38159 | -64.36507 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6bff312c-777f-3157-aa40-232b7a31660a | -9.02637 | -65.72701 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| db0d027f-d52a-337b-ae36-69e427f08d13 | -8.96227 | -68.79848 | 2025-08-26 06:25:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a12b25f7-8cbe-34ee-b274-44bcabf7e063 | -8.10458 | -71.24751 | 2025-08-26 06:25:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c952b35e-fdce-36ba-be9e-28916d06a2b0 | -9.01025 | -65.70595 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aeb0d01-4a85-3a47-a9e9-49af959528ec | -9.08354 | -66.06691 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23702c5e-b0bb-3182-9a7f-c2862a47c46a | -9.07 | -65.7282 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 021aecd2-dde2-3e9a-bff6-485ab63ade44 | -10.42153 | -64.39162 | 2025-08-26 06:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cffab6c-b69b-35ec-9bd6-5cd79167888d | -8.10403 | -71.25134 | 2025-08-26 06:25:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dfbf7db-ce41-34c3-bd05-a85b53f6a514 | -9.06912 | -66.06637 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f5368f8-47d3-3532-8bf6-15fd78b17a7c | -8.9843 | -65.42325 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4a57c01-a790-37d6-8847-eda793ec0ad1 | -8.98304 | -65.43318 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5df5625-fa94-3b5f-8916-4345046a0950 | -7.39697 | -64.35011 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02f93ce5-4e1b-3cdd-9e31-701646fcd1bd | -8.97615 | -65.43729 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3398c74-2666-3ada-b1c2-a7f8fb7d6d57 | -9.00564 | -65.40588 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d830e09-cc39-37aa-ba7c-09a6c5c5dbc9 | -9.08855 | -65.72992 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3242cc3-41e1-34c4-9a61-caef42f1c51c | -9.08915 | -65.7253 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0011e89b-3d57-39bd-9030-4572113b3412 | -9.01821 | -65.69232 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c207142-4589-34b3-8cea-a9fdffe28b69 | -7.37657 | -64.34705 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9b796aea-880f-3b61-baee-46422f84e99b | -9.7991 | -64.25664 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab007cf-927a-3dcc-8f3e-216f38d9fd2e | -7.38313 | -64.34789 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da5265ec-c5d9-33f2-9554-c06c59316368 | -9.25739 | -65.62533 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63c5f195-0245-3bc9-b825-ee5b05ac7b47 | -8.97177 | -65.4216 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10dffb25-5148-3607-a6aa-0011a6415ed8 | -7.3773 | -64.34753 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 982e5d2c-8367-382a-8b5c-c561c12e391f | -8.81172 | -69.29726 | 2025-08-26 06:25:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7fed4bf-d100-386b-ac50-49e5eadae29a | -9.05034 | -65.73517 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d681be97-2de8-39e3-a326-82d66d20640b | -7.39552 | -64.35529 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 300fb5fb-e0fa-385d-bc62-90b5f6be3b1b | -7.88569 | -63.01336 | 2025-08-26 06:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 385b19a5-52b5-3052-b5c9-4150848501d9 | -8.99809 | -65.41501 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6da054eb-1d31-3c31-99b5-e5f00b7f2545 | -8.62925 | -67.24834 | 2025-08-26 06:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b6e2c10-33f8-3dca-a1f0-cd26c62003a4 | -8.97115 | -65.42653 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68311e4d-3fd6-3d74-8bea-5a9d3af3d724 | -9.25119 | -65.62447 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60ed342d-3eac-3adb-a90c-401ab8f2ca1b | -8.99056 | -65.42409 | 2025-08-26 06:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a238b4c8-9b5d-38ef-ad34-a1c46e61c59f | -9.80426 | -64.25699 | 2025-08-26 06:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f7b4561-fa55-354c-993f-85831caffa3d | -7.38241 | -64.35349 | 2025-08-26 06:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3e8ac665-2dc3-3915-8625-66db2a557daa | -10.64936 | -65.31659 | 2025-08-26 06:25:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa622ef0-f4ec-35bb-a480-ed8274265229 | -11.6277 | -46.3899 | 2025-08-26 06:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 63c9fc60-7b70-3850-b723-265d2f9616e3 | -11.5397 | -52.14 | 2025-08-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0b34cb0c-e3d7-3c1a-8cfe-47b789c7652c | -9.1717 | -59.5405 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 21dc83c5-423c-3bb1-aff8-276c1bfd4cf1 | -11.54 | -52.119 | 2025-08-26 06:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7e7e0b4f-97bd-368e-a34b-fabc2f8be439 | -6.7819 | -59.6711 | 2025-08-26 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 8335ce09-cdeb-3de7-ace5-b7b7fba9029e | -8.8363 | -62.451 | 2025-08-26 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 651c92a1-7bd1-33cd-9b10-a895779a2447 | -11.1396 | -44.7654 | 2025-08-26 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| b658d328-92ea-3de1-b2d9-3a22a52a0c76 | -9.1903 | -59.5395 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| e8e8e135-fdf0-3e14-b2e5-c9f85b8b955a | -9.1722 | -59.4629 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 188a6064-707d-3bf9-a01e-1b0cab0aa250 | -9.1718 | -59.5211 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 446c005f-4bb4-31d7-bebd-448d7a70b70c | -6.8229 | -58.956 | 2025-08-26 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| ca56ea51-f974-3354-9786-84523e46a1f6 | -11.6465 | -46.41 | 2025-08-26 06:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 1f092039-6424-3dc3-9122-05ba42c80ef7 | -11.1587 | -44.7627 | 2025-08-26 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| acb19074-7a36-302e-84c6-28bc79cc2a17 | -6.2459 | -60.0174 | 2025-08-26 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5b5b8413-a97d-3aaa-8bec-4a2ebf9ff555 | -9.6366 | -59.6313 | 2025-08-26 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.5 |


[Clique aqui para ver as próximas entradas](README99.md)
