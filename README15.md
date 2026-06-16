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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1c7f3f6-e718-3c8d-b0f0-822abac1c276 | -11.47826 | -57.11749 | 2026-06-16 05:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3cf8507-fe0c-3d4a-b59b-f0b7ce331604 | -12.92496 | -54.22467 | 2026-06-16 05:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fd9b0ac-9ed2-3ca8-b185-5e4e71664746 | -6.97462 | -42.87687 | 2026-06-16 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 8eb687ba-e79c-3c6c-94b8-cf9a1beba4ce | -6.97319 | -42.88608 | 2026-06-16 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 3868cf0e-c91b-3e2a-a6d2-17e002e4f484 | -6.30132 | -43.63919 | 2026-06-16 06:10:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e131ffa-ea20-3add-a1bf-6ced0a5d836a | -6.13611 | -48.5219 | 2026-06-16 06:10:00 | AQUA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 693caba0-12fc-3a65-b41b-50f1f6cee106 | -6.14097 | -48.51812 | 2026-06-16 06:10:00 | AQUA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2610780c-f01b-35b6-9278-526d70a42fa2 | -10.54218 | -47.03265 | 2026-06-16 06:10:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| b2df6356-ad2d-387b-8197-316dc4bdcdaf | -6.3926 | -44.17506 | 2026-06-16 06:10:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7bafc403-708c-3da4-a7d8-a47f1c75abf4 | -9.32866 | -45.48379 | 2026-06-16 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 93fa472a-2cbb-3a64-9e21-59ed3420b781 | -3.95929 | -43.11242 | 2026-06-16 06:10:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b1a9631a-00e1-3ddc-ab7c-6883294ae595 | -9.3406 | -45.47365 | 2026-06-16 06:10:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5f9cb967-f537-311a-a16a-71b78f47ce30 | -6.39429 | -44.16438 | 2026-06-16 06:10:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 94b315d4-f89b-3481-a9cb-30d3ad8b2c39 | -5.92814 | -43.47626 | 2026-06-16 06:10:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ed6e0a18-d887-3d8d-bda1-24a3e24c363e | -5.80039 | -45.06639 | 2026-06-16 06:10:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 385c2ab8-40ac-3556-b7af-8ffb03edcd98 | -5.83478 | -43.48594 | 2026-06-16 06:10:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 54a033cc-128a-3eb0-9697-c3794ed3fa5a | -12.84864 | -44.36706 | 2026-06-16 06:12:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| fb27ca98-6cc3-3d34-aa36-185ca5a5a734 | -13.54652 | -47.86813 | 2026-06-16 06:12:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fc57830a-cd1f-3655-bcdc-f36806da463e | -12.84714 | -44.37659 | 2026-06-16 06:12:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 85e638fa-ec57-3efa-999d-9206f66e59fd | -12.8548 | -44.3625 | 2026-06-16 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 5168e77e-7239-37db-b6bf-1b9177908932 | -12.8548 | -44.3625 | 2026-06-16 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| ac6b8021-2226-3509-bf34-ac83c4fece2a | -12.8548 | -44.3625 | 2026-06-16 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e26bdf2c-1260-31a9-864e-37751df0ae61 | -12.8548 | -44.3625 | 2026-06-16 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 388d9107-7a05-3778-8182-411ed23388bd | -12.8548 | -44.3625 | 2026-06-16 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 5e8acf5b-82b7-336b-9077-aa0359d45009 | -12.8548 | -44.3625 | 2026-06-16 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0af7672d-0597-3144-a5f7-11f2628da7fd | -12.8548 | -44.3625 | 2026-06-16 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| c27c82ac-94ce-3ee8-9d05-cbae44ba076e | -12.8548 | -44.3625 | 2026-06-16 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 46c1f8c6-63ac-3fc4-a86e-591e5a314969 | -12.8548 | -44.3625 | 2026-06-16 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| e5a5f767-96dd-3ed8-b462-4f327121d5e1 | -12.8548 | -44.3625 | 2026-06-16 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| a3160a30-dce9-38f8-ac7d-544d210e37ed | -8.8695 | -46.966 | 2026-06-16 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a05dda71-3a76-32c9-9243-000c9956fef1 | -8.9638 | -46.9563 | 2026-06-16 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 268460b6-cc1e-397e-b2f3-55716c2f9c76 | -11.8007 | -57.0032 | 2026-06-16 12:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 2e120171-3129-3ed5-b82e-d0a7eba07dde | -8.9638 | -46.9563 | 2026-06-16 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 5b7b1ee5-0c30-3f10-b03b-cdc31683d1bc | -8.9449 | -46.9582 | 2026-06-16 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 49f1d74f-5a27-3510-9026-0b5f6af863be | -8.9638 | -46.9563 | 2026-06-16 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b0a962a6-720a-3b1c-99f2-fcbf7aacd7b0 | -8.8695 | -46.966 | 2026-06-16 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| da1d60d1-78c6-37ce-a019-ff810c741557 | -11.8007 | -57.0032 | 2026-06-16 12:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 99f78355-2ed8-387b-b62f-1cf25de2fa06 | -8.9638 | -46.9563 | 2026-06-16 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 69928f75-7a19-30bf-aa8e-a44fa790f5b5 | -8.9641 | -46.934 | 2026-06-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6a7bc40c-8488-3045-a8de-5dcd12f31f47 | -8.8695 | -46.966 | 2026-06-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7f4dbb8c-c49f-3d3b-bc09-d7d6a7379f87 | -8.9449 | -46.9582 | 2026-06-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 429e025f-7009-3bdd-bbf9-a6781801e5bd | -12.8548 | -44.3625 | 2026-06-16 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8fdcebcc-5a7f-38ce-82e6-f76532b16a72 | -6.9793 | -42.8798 | 2026-06-16 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 8927674c-2b27-39b3-bc7c-446ba28647aa | -8.9638 | -46.9563 | 2026-06-16 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| fc5d412e-b2d2-32d6-a831-6bc6ba0605eb | -6.9793 | -42.8798 | 2026-06-16 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 92044cdd-ed42-3f8b-aaac-20ba954900bd | -12.8548 | -44.3625 | 2026-06-16 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a7690c3d-c54c-3365-bbef-1eec3e504eb0 | -8.9638 | -46.9563 | 2026-06-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 1e178fb0-686d-3b44-b2e6-b417f2f66df2 | -8.8695 | -46.966 | 2026-06-16 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6c1232ca-bcfa-37af-a59d-f265703478ce | -8.9638 | -46.9563 | 2026-06-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 227.2 |
| 4ef0b30b-b00e-3de4-a25b-9ebefdef2753 | -8.9449 | -46.9582 | 2026-06-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 6fb3e159-b4b3-3828-8f49-20df7b32aef1 | -8.8695 | -46.966 | 2026-06-16 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a3b0d9ee-8bde-3d8f-8cbb-136e107f9ebb | -11.5933 | -55.33 | 2026-06-16 13:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 495f00db-b6f8-3dbf-9d91-baf65d6b4850 | -6.9793 | -42.8798 | 2026-06-16 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| e54c2735-d355-3c44-9b0b-7b15b2a16869 | -12.8548 | -44.3625 | 2026-06-16 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 0ada037f-0551-38d8-8310-7f381d6b63a4 | -6.9793 | -42.8798 | 2026-06-16 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.3 |
| c47951a8-f1d0-3522-8011-171a97167044 | -8.9638 | -46.9563 | 2026-06-16 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.7 |
| b9038427-4c36-3239-ba81-859f5eaf1392 | -8.9449 | -46.9582 | 2026-06-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| ff864915-3071-3aae-9c52-1015d6491963 | -8.9446 | -46.9805 | 2026-06-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 47df0d39-11fd-39b4-a96b-f21e84a72413 | -10.7777 | -54.0983 | 2026-06-16 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 72b21285-7dfd-3ef0-a566-bcc457a6eaef | -6.9793 | -42.8798 | 2026-06-16 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| fdefdc73-262e-339e-8658-475fd404139e | -8.9638 | -46.9563 | 2026-06-16 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 228.6 |
| dcc96cf0-5033-3202-a1f0-127c1f3d8510 | -8.9638 | -46.9563 | 2026-06-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 391.1 |
| 364ffefe-9a63-3099-8fb4-6e5a433ce314 | -8.9446 | -46.9805 | 2026-06-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| c441b62b-2a37-348a-a803-fac96b9c98d1 | -6.9793 | -42.8798 | 2026-06-16 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 273c229c-3018-3c2d-ab10-1e469d035c26 | -8.9449 | -46.9582 | 2026-06-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 0556a2d1-d5e6-3373-8a90-57178f298591 | -11.5933 | -55.33 | 2026-06-16 13:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ea5675a1-182e-3ee9-b270-c3780e0c4ff1 | -12.8548 | -44.3625 | 2026-06-16 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| ed15af8b-73ba-35fb-805d-3a26fb03f4c9 | -8.8695 | -46.966 | 2026-06-16 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f1c5fb6a-fb33-3fc7-96f5-dbedd68b0c9f | -6.9793 | -42.8798 | 2026-06-16 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| f84321d8-2c58-3210-815e-932b8ea596ea | -8.9638 | -46.9563 | 2026-06-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 539.4 |
| b2bef41e-d6f9-3b0f-9c0f-8cc1b0050979 | -11.5933 | -55.33 | 2026-06-16 13:50:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a30904b1-314f-3a99-9817-ad614131facc | -8.9449 | -46.9582 | 2026-06-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 23a8a2e7-8ca5-39eb-ab86-ac16c4447c7b | -8.9641 | -46.934 | 2026-06-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c7e4d65b-5be3-30be-8357-60da17b14886 | -10.7777 | -54.0983 | 2026-06-16 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 888678e2-4159-3549-856a-a56a480cbe66 | -8.9446 | -46.9805 | 2026-06-16 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.2 |
| c0e95626-0dbf-3339-ac9f-fe71b4a85cbe | -8.9446 | -46.9805 | 2026-06-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 3f234ebd-dc7c-32f1-afea-877975af1778 | -8.9641 | -46.934 | 2026-06-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 220e1d70-e524-304a-8b72-24004638be51 | -8.9449 | -46.9582 | 2026-06-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 7a5d5b22-5df9-3fb8-86db-d74313aa5527 | -6.9793 | -42.8798 | 2026-06-16 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 68102317-adf1-36c3-889f-180d64f703e8 | -11.5933 | -55.33 | 2026-06-16 14:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| f4556a17-d752-3d4d-b962-4d5208c8e430 | -10.7777 | -54.0983 | 2026-06-16 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 71b0dfa0-486e-3125-9fd7-2b5fe89f350d | -8.9638 | -46.9563 | 2026-06-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 464.6 |
| 3379f207-f90d-3050-be24-af7645bce2a1 | -8.8695 | -46.966 | 2026-06-16 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6f79d2b6-eb21-3cd5-bd2b-0cc766eee21e | -8.9446 | -46.9805 | 2026-06-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 59a90abc-d10e-3acf-8de2-bc3df2d35370 | -12.9175 | -54.2202 | 2026-06-16 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 3be1144f-2a95-3270-af0d-5f8e3ee66082 | -11.5933 | -55.33 | 2026-06-16 14:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3a1780b5-d388-3186-a433-8e8f123b0991 | -8.9638 | -46.9563 | 2026-06-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 383.6 |
| 1acc4e01-54bc-3319-8c1a-d92c619aa37e | -8.9641 | -46.934 | 2026-06-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4df614ea-d5c7-3b3f-8d9f-ea66b5eebb03 | -6.9793 | -42.8798 | 2026-06-16 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 7fb49abd-5f4a-369a-b939-0b8e6a82bffc | -8.9449 | -46.9582 | 2026-06-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 81613454-2e77-3cb5-8bd7-63859465023c | -10.7777 | -54.0983 | 2026-06-16 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 46a4acf1-6852-3d35-b6b1-1eee42d3d45f | -8.9638 | -46.9563 | 2026-06-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 383.2 |
| d928e874-597a-3df4-b85a-38976d18cb78 | -12.9366 | -54.2182 | 2026-06-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| dbeb7b7a-4312-3c90-bf6b-1194dcc5fc25 | -10.7777 | -54.0983 | 2026-06-16 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 99a27b3e-1722-3d88-bbbb-581c698b3dc3 | -8.9641 | -46.934 | 2026-06-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| ae8ecfbb-393e-3770-9bc5-b0bd6673944d | -10.7024 | -49.6797 | 2026-06-16 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 3df77408-33b6-3ad4-8d8a-692ef2f4a4fb | -11.5933 | -55.33 | 2026-06-16 14:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f0c9c427-e740-365e-a110-2e3726300089 | -8.9446 | -46.9805 | 2026-06-16 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 1aa06f3a-c63c-3f0d-ac81-c24dc2fca8d7 | -7.7724 | -47.5773 | 2026-06-16 14:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 77fea673-89be-3ef0-a20a-b52196c50715 | -12.9175 | -54.2202 | 2026-06-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |


[Clique aqui para ver as próximas entradas](README16.md)
