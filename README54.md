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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e17728b8-9ea6-37a4-adf5-8cfc9472549c | -9.33084 | -64.43438 | 2025-11-18 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83587f97-6ce8-3ea5-9080-22a987d92848 | -9.49187 | -63.50403 | 2025-11-18 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48912dc6-75df-3c1c-9a98-cb72c736e68c | -2.33837 | -55.79692 | 2025-11-18 06:01:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c8f55418-2550-320e-821c-c11db6417a80 | -4.6547 | -47.9444 | 2025-11-18 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 06a72c90-5943-3ea9-a1c6-36ff4bbe1da3 | -4.6361 | -47.9453 | 2025-11-18 06:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 97f9985b-06d4-389b-a016-53d2f18e8b71 | -4.6361 | -47.9453 | 2025-11-18 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3945e3f5-d27f-3ca0-a099-1fd1eb1de505 | -4.6547 | -47.9444 | 2025-11-18 06:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 32e0f59f-44e3-37e8-b455-cdbe95803b42 | -4.6361 | -47.9453 | 2025-11-18 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 23ed3969-c5f1-3be6-a884-8a6a0a6330e7 | -4.6547 | -47.9444 | 2025-11-18 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 95d15ad0-b541-3164-9c2a-1dbc6c90afd4 | 0.81237 | -51.84876 | 2025-11-18 06:35:00 | AQUA_M-M | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 18.4 |
| fbaac03d-9ac5-356c-8cc7-5ebcf7827a0e | -0.98881 | -47.06855 | 2025-11-18 06:35:00 | AQUA_M-M | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1d20c6ad-d3e2-3ccd-ac48-520c6887d69a | -4.13344 | -52.11772 | 2025-11-18 06:37:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d931f9cc-c56d-36b6-9fbb-29c387c7acc0 | -3.23088 | -50.50567 | 2025-11-18 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 884ae839-06a5-34fd-88fc-aefc10631862 | -4.64001 | -47.94106 | 2025-11-18 06:37:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c659b61f-031f-3db9-bc1b-9ff2c4bc9bc3 | -3.46898 | -49.9859 | 2025-11-18 06:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 54523af5-c438-3e76-a415-763d45c3b96c | -3.14789 | -51.4851 | 2025-11-18 06:37:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 85f4c379-6c2f-355c-a497-295b68fb75ce | -3.17292 | -48.02487 | 2025-11-18 06:37:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3ae1bf36-38f4-3774-b29d-573b6744aae9 | -3.17339 | -48.0196 | 2025-11-18 06:37:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c1a71d7e-5a5b-3fed-be3d-436bbefff326 | -0.97455 | -52.4451 | 2025-11-18 06:37:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a2b0084e-f864-3bd0-904b-47860cbbd5a4 | -2.52372 | -47.80136 | 2025-11-18 06:37:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 661724dc-c886-3d2d-ad61-496fe922c36c | -3.3596 | -50.17819 | 2025-11-18 06:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a7b61c64-07cf-3a1d-a1a8-2c3d192bf31d | -0.88588 | -51.9912 | 2025-11-18 06:37:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 90e135ed-7c03-3540-aaa3-d2ba6441c1c6 | -3.2328 | -50.49261 | 2025-11-18 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c7f81e74-6389-363a-854a-4144af4cf907 | -2.537 | -51.18176 | 2025-11-18 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c91d3dc7-7b99-35d8-85bd-5d174eec1107 | -1.91811 | -48.78856 | 2025-11-18 06:37:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1666a3ae-46ab-3f9e-87df-aac80c571068 | -2.52708 | -51.18031 | 2025-11-18 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9b9575fa-9d5c-35df-99a6-fa3b74a5dd31 | -3.47498 | -55.42914 | 2025-11-18 06:37:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d860fa91-0981-3116-83ac-3737f4c5ddc2 | -2.98354 | -51.0712 | 2025-11-18 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 55827231-672a-37d6-809f-81cf88f8a2e7 | -3.7202 | -52.05869 | 2025-11-18 06:37:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 10ec0a87-b846-3295-8b61-1867af08da26 | -2.33663 | -55.79802 | 2025-11-18 06:37:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44497e4d-fa14-33da-ad9f-7f23185823b4 | -4.13051 | -52.11052 | 2025-11-18 06:37:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd08a0a8-0268-3959-8f42-dc00b2ac5fa9 | -2.52074 | -47.82173 | 2025-11-18 06:37:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 66a7d762-4d99-3690-ad28-71d8e3c33d7f | -1.91566 | -48.80508 | 2025-11-18 06:37:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0ac1d36c-c720-389c-9792-a1f80464eaac | -2.47315 | -50.23611 | 2025-11-18 06:37:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3590ee96-6150-367f-add4-b872e308c2ed | -4.63659 | -47.94588 | 2025-11-18 06:37:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 4dba5e4a-94e9-3f6e-87c9-3b7682556a38 | -2.5078 | -47.81982 | 2025-11-18 06:37:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| de896d90-a07c-345a-8934-a87ee8688138 | -9.39583 | -48.43311 | 2025-11-18 06:39:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 55d55f09-2183-3bc1-8722-85efeddce5c4 | -9.39274 | -48.45681 | 2025-11-18 06:39:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 40c37cf3-5ba4-3c08-b2a3-b42493444691 | -9.40105 | -48.4409 | 2025-11-18 06:39:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 1b77910f-0e48-38a3-b90d-2e2ed9e3b3fb | -12.8917 | -54.7215 | 2025-11-18 06:39:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 241a3eac-446f-3dcf-b56a-63a653d22b15 | -2.5238 | -47.8115 | 2025-11-18 06:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5bd80592-6826-3f30-884a-ad3e00d33b18 | -2.5238 | -47.8115 | 2025-11-18 07:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9564391e-101d-3d7a-808e-e7cdb5ea1f5c | -3.1467 | -45.2053 | 2025-11-18 07:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| eaf34ebb-b56f-3c9b-ae29-a3493f567a19 | -3.1468 | -45.1827 | 2025-11-18 07:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| cf3259a1-d390-386b-b5a2-56deb47eb0f5 | -3.1653 | -45.2046 | 2025-11-18 07:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 175635e4-7c68-37df-b0f6-4f302e97286c | -2.5238 | -47.8115 | 2025-11-18 07:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 59f41160-227e-34c9-bd75-803df0ae3570 | -2.5238 | -47.8115 | 2025-11-18 07:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| ababe639-28fe-390b-b5dd-59feaf905f5c | -3.983 | -42.3743 | 2025-11-18 07:30:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 27bd8e2f-7814-3602-9b51-4a7e6f0c68e4 | -1.9292 | -48.7946 | 2025-11-18 07:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4888bb78-c37b-32f1-abdc-6a753e0b48b8 | -2.5238 | -47.8115 | 2025-11-18 07:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3e9ff497-add5-3d6f-b56f-f67e29fc63e1 | -3.983 | -42.3743 | 2025-11-18 07:40:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| f936deda-3776-3dc1-bc83-fd7c3f1cc81e | -2.5238 | -47.8115 | 2025-11-18 07:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 868127b9-c193-3513-9016-4e55a6ec3d49 | -2.5238 | -47.8115 | 2025-11-18 08:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c66d42e6-fd14-3af1-a027-c882b5d080e3 | 0.2334 | -51.10884 | 2025-11-18 12:14:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6231a801-e6f8-303d-b9d0-c270bba46162 | -3.45814 | -42.09877 | 2025-11-18 12:16:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 62ebbf7a-a05b-3475-b141-d56e7fc954cb | -5.90886 | -38.15984 | 2025-11-18 12:16:00 | TERRA_M-T | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 40.6 |
| ef0966b4-82a4-3182-bb61-bdd97961f6a0 | -3.71221 | -42.16787 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 403.0 |
| 92470bb7-5ef1-3562-b734-938c5c462a9a | -6.35419 | -41.74269 | 2025-11-18 12:16:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| ae25ca97-ea8c-30ce-a0df-665433b13fca | -3.93971 | -46.14764 | 2025-11-18 12:16:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 030d689a-598a-35f6-acdd-d18f952a712e | -5.75327 | -49.25994 | 2025-11-18 12:16:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 962e9e56-928c-38fe-8389-6961099cfe51 | -3.02913 | -44.47746 | 2025-11-18 12:16:00 | TERRA_M-T | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| cd682fb3-de56-3a5b-b97c-b3cdebfd6346 | -5.3379 | -43.76812 | 2025-11-18 12:16:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 68da1bd9-c7ed-3715-8244-614519c9ec25 | -1.8341 | -47.56689 | 2025-11-18 12:16:00 | TERRA_M-T | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1a95d133-78fc-305f-9f1e-c930849e746c | -0.99044 | -47.07474 | 2025-11-18 12:16:00 | TERRA_M-T | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 911b9732-4bb1-3bf7-88e8-2d0074c15c66 | -4.8987 | -43.46369 | 2025-11-18 12:16:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d6e8c476-53e3-321c-b0ad-3495814065f8 | -8.87868 | -43.9331 | 2025-11-18 12:16:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8406bd7e-4be3-3c72-af40-fe713086a4ce | -8.46194 | -45.12942 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 779fd492-7a5d-3b13-803f-bef2a6efcfab | -4.97921 | -41.8516 | 2025-11-18 12:16:00 | TERRA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 2ac2aa6d-42f9-3779-9fc6-6ae64d529b21 | -1.42497 | -47.20162 | 2025-11-18 12:16:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4a541e4e-cddb-3b44-9a85-36f25483c89b | -3.24761 | -43.03535 | 2025-11-18 12:16:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| e93918a5-5af3-390e-a87d-caa6441bc93d | -5.83919 | -47.83596 | 2025-11-18 12:16:00 | TERRA_M-T | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f19dae1-37d5-337e-8fd1-9369e48a562f | -4.6526 | -46.71899 | 2025-11-18 12:16:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c4f46b72-387c-3745-ae8d-546be8cf473f | -4.48607 | -46.59177 | 2025-11-18 12:16:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| bc777ead-11c9-32ed-ad0c-d8ef7bb7b5d8 | -5.42899 | -43.03577 | 2025-11-18 12:16:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 27547117-d177-3690-a394-22ca7aea647b | -8.14774 | -47.63732 | 2025-11-18 12:16:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 15f1fdc1-4c17-3e7d-8ee0-ac8240d21ec8 | -1.7591 | -46.55384 | 2025-11-18 12:16:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| da3baaec-1eef-3f0e-8c8b-85d4b466a769 | -3.25842 | -43.0368 | 2025-11-18 12:16:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 2a9639ac-c055-3e69-ab36-b6a0afbf448b | -1.10322 | -48.09446 | 2025-11-18 12:16:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e0d9b515-15e6-396f-8252-cc481327c384 | -4.34606 | -44.34639 | 2025-11-18 12:16:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c79c1c0c-9338-3647-8b01-d6537a79062a | -3.66319 | -42.43344 | 2025-11-18 12:16:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e27fb582-4689-305f-b1bc-20baeeb764c7 | -3.67053 | -42.21133 | 2025-11-18 12:16:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 7e8c50bc-6ec3-3e24-8e87-af5c55b0b9a9 | -8.48962 | -48.98891 | 2025-11-18 12:16:00 | TERRA_M-T | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 99b40b7d-017c-3540-8e57-4bed7c0b390d | -8.4757 | -47.99005 | 2025-11-18 12:16:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 4e13a5fa-f00c-3783-a0b5-b02d91f118ff | -5.43341 | -46.2819 | 2025-11-18 12:16:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ceda46db-d0ba-3815-b494-e4b20a8b3b50 | -3.9384 | -46.15684 | 2025-11-18 12:16:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 473e3feb-03da-3933-be7c-2943e4e54a83 | -2.51829 | -47.81983 | 2025-11-18 12:16:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0f980b5a-41f9-3759-8e8e-dcdbb3b19220 | -7.5065 | -37.99419 | 2025-11-18 12:16:00 | TERRA_M-T | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 5504dd16-6c6f-3edd-a303-815f28d1dbc5 | -0.79653 | -48.68549 | 2025-11-18 12:16:00 | TERRA_M-T | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| a1633b0e-5d86-3abe-a2fa-0cf50db93b50 | -8.19557 | -49.79581 | 2025-11-18 12:16:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0a85aeba-f610-3a34-b575-748c5b56eb01 | -2.22788 | -47.02217 | 2025-11-18 12:16:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1c2f3e7b-890b-36c4-942c-87405446d095 | -4.09813 | -41.99786 | 2025-11-18 12:16:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| aaa94666-5e81-3db7-85d1-fd6fcfe33566 | -3.60021 | -41.38684 | 2025-11-18 12:16:00 | TERRA_M-T | COCAL DOS ALVES | PIAUÍ | Brasil | 2202729 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 5cbdf982-f40c-3eba-bbaf-05f56cf87f78 | -1.51458 | -47.80105 | 2025-11-18 12:16:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| b420f1dd-0d96-3cc3-aa24-f0bc04b72a19 | -4.52982 | -45.61923 | 2025-11-18 12:16:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2f0adbd3-8429-379d-9b84-6f47e98a6f1a | -8.45983 | -45.14701 | 2025-11-18 12:16:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 46.6 |
| a3c06e59-7753-31fd-b158-2b295128f1f1 | -8.55399 | -46.04003 | 2025-11-18 12:16:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| bdf43241-1a94-3996-8e82-5d92f6e42ef5 | -5.90365 | -38.15321 | 2025-11-18 12:16:00 | TERRA_M-T | POTIRETAMA | CEARÁ | Brasil | 2311231 | 23 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 26d6319b-a111-3d8e-a90a-8caf40f43ee4 | -3.70994 | -42.18399 | 2025-11-18 12:16:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 282.5 |
| f73cb8cb-5f4c-3752-b82d-867ed3744367 | -1.91562 | -48.79999 | 2025-11-18 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| daeb8474-6f9c-361e-ac6e-842ea949fba3 | -4.7151 | -45.81534 | 2025-11-18 12:16:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README55.md)
