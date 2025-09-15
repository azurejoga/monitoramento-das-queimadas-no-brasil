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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bac7c904-5062-32a6-a715-17245802ab4b | -7.86832 | -43.56983 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da93e17-d382-303c-8aba-68461708a01f | -10.8927 | -45.55071 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f033418e-6343-3ed6-a445-3155d73bda17 | -8.91713 | -45.4635 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca035611-8dbd-3b30-926e-a8f94e892771 | -7.98515 | -45.6583 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bcbc567-ba6f-3085-9e77-c4aa2009d18c | -8.07459 | -44.52107 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8b2130b-5f08-398d-892c-b0684e575129 | -8.0928 | -50.16048 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a716c99-317d-341d-9ce6-27946fd94550 | -5.735 | -43.19906 | 2025-09-15 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cde19a2d-326e-305f-b881-f7fbfa54cfd3 | -8.94835 | -46.0418 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 381a0fed-8b00-31ea-8578-ed9b2de96c59 | -6.17631 | -41.19201 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a8b344b-6297-3cad-928f-2ce294a16213 | -7.36076 | -44.29449 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fadca545-c488-3095-b50a-a309a7aea8c6 | -8.99817 | -47.03859 | 2025-09-15 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ccdcfee-1995-3fcb-bba8-774eba945456 | -5.64898 | -42.59751 | 2025-09-15 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f66792a6-0766-340a-9447-15e1a193551e | -7.86499 | -43.5794 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 44072639-18bf-33e9-94da-bcb629afb07b | -8.89786 | -46.18999 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea0015a-ba0b-30c3-8d9b-142cb1b3f779 | -7.71027 | -50.3569 | 2025-09-15 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d5d099a-09e9-3186-b23e-e59b3cd92c7e | -9.23396 | -45.6611 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02210569-8cb8-32e2-9148-a436fa3b607d | -9.00065 | -47.04885 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e8c8c1f-b0bc-36dc-8e60-fdf681433745 | -6.66051 | -44.63815 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59c496f3-b78f-3d7b-8a52-95d0cc9e6fe1 | -7.40561 | -49.98435 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bdcc946-465b-376f-b64c-bb31ef419760 | -10.89208 | -45.55519 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a23a38-8f23-31a9-bada-5c7c6f7665d4 | -7.73766 | -45.30599 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d30f6f41-9e8d-3fc2-942b-10bd592da929 | -6.40638 | -46.9413 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9f175fa-4636-33e1-aced-daacead1ed38 | -8.18415 | -46.76592 | 2025-09-15 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eef62bca-525e-3b91-a16c-5429e9ae952e | -8.96515 | -45.77476 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b52787aa-3ebf-32fa-8c18-625ee0711626 | -3.8553 | -51.33709 | 2025-09-15 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca0db8bc-8422-3e20-b359-e0fbf52e2367 | -7.64176 | -49.74261 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb3ad40a-4b53-3bf9-9074-a6b1df20d654 | -6.18345 | -41.18151 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0edddf15-07b8-3cf0-b291-48368d65566f | -9.11964 | -46.93596 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70571fdf-f0db-3736-8f4a-8d8e5e152dd8 | -6.41004 | -42.61575 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edb100a5-0587-32cb-8036-0b7f1bc7da38 | -7.87881 | -43.56587 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 06928596-0250-39b4-a851-c9b5a32b7cd0 | -8.64231 | -45.69156 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6580333c-2aee-3e97-bde4-388dbc62298c | -6.40917 | -42.62167 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8863f089-eb35-3d90-9372-9c55b761b813 | -7.87393 | -43.56517 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 37d9962c-a5e9-3b6c-ac81-bf4829066dfa | -3.74569 | -52.37033 | 2025-09-15 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 819a79b3-c9bb-31e5-b912-94a4db27ee80 | -8.12966 | -43.6582 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93576928-11e5-31b6-a568-61e6611aed64 | -6.51908 | -43.24849 | 2025-09-15 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 676ecd74-89ab-30d6-98c4-458dd5e75d4c | -10.73822 | -44.76783 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c25bd953-9d51-3c87-bfaa-bd6731b89a1e | -7.39322 | -49.97505 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee885e05-3bf9-3086-91bd-a72d5975aacd | -4.63117 | -50.40938 | 2025-09-15 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 538bcd37-2b0f-3f10-bb01-0eed082a2415 | -8.97526 | -45.81913 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42739b7f-caff-3662-8838-10fc9fbce1f2 | -5.93502 | -44.86523 | 2025-09-15 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c21c31d-8c2b-3f4f-a769-685d71ded63e | -7.87216 | -43.56404 | 2025-09-15 04:49:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57107c19-c399-383d-aaed-1af9a00fc194 | -7.97411 | -45.64494 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd2ce610-557e-3c58-a60b-115632b93c70 | -10.43181 | -44.84181 | 2025-09-15 04:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205bbf96-60fe-3db3-816d-ad3b7091f7b5 | -8.9567 | -46.04322 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 529eb106-55d5-3107-adad-007921dc8f47 | -4.03888 | -51.03318 | 2025-09-15 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30996c68-167c-383f-a248-77288fdd2974 | -7.86128 | -43.58518 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ca0f1c9-56ff-3cc1-bc3f-a9fc15aa76c3 | -5.65356 | -42.60146 | 2025-09-15 04:49:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d9d9ae7d-9168-3d14-9e93-686fd43fe695 | -5.57337 | -51.97399 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73ad75f4-1a74-3898-9ec6-a01da42069dd | -9.05024 | -45.7204 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6a7f0b6-9c5a-374e-a78e-a339eb9f58db | -8.2075 | -45.54645 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d17c3ea-9282-3fcd-b5f3-3520f6da2437 | -6.15038 | -41.18543 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9d5f0092-bbdd-3f67-872c-bd1ca50f242a | -9.00606 | -47.03685 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b5e9f32-1d43-3540-8c02-4de01463dbb8 | -9.55067 | -45.97444 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c041b942-287f-37e4-835f-869482fa4187 | -6.45094 | -44.52602 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c6d030d-578f-3161-b313-a5b08bfb4177 | -6.41972 | -42.60524 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f979966-6203-3423-87de-3679706b5446 | -7.87705 | -43.56474 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 7c578e5a-5d65-3dda-861c-855bec4cd48e | -5.80172 | -43.93143 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f06aec-de93-3122-801d-5a14c19c78a0 | -9.07032 | -44.82341 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a505caf-d450-32c9-bb53-d1401ae2d368 | -7.70692 | -50.35638 | 2025-09-15 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 001c3d01-1966-3795-a4ae-eb9a8bd7fce7 | -8.13454 | -43.65884 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa304e68-fd9c-3d76-9214-406b04723cbe | -8.17017 | -46.77906 | 2025-09-15 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3690db0e-99b0-3205-bca5-917355aaec7c | -5.40037 | -42.83364 | 2025-09-15 04:49:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4b51d63a-e72c-348b-aa83-8e52d3635488 | -10.17016 | -46.14719 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b767c34-c6f8-33eb-b98f-835c1af765b0 | -7.85131 | -46.11451 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bffeac03-b217-3dc9-ae70-63873748a48a | -8.96426 | -45.77323 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcc89bf0-841d-35f9-9480-6fd6762fae5b | -8.62906 | -45.69283 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5931c872-a51a-328d-9a22-3e71cc0e3649 | -6.41375 | -42.61073 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b83002d0-2c4d-3c41-b93e-0ac8ad1ce921 | -7.87663 | -43.58202 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 77793dd1-10ff-3ffb-b029-72216dea335e | -6.52994 | -51.19164 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 027b2c37-7df4-3946-8a7b-7e3b463148d4 | -7.01933 | -44.53903 | 2025-09-15 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eeba4a09-114c-3b4f-9ce4-32b184946137 | -9.04652 | -45.71583 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a9d1c88-87c5-3a10-9329-ef73a354e629 | -8.91125 | -45.50585 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2ea2ac7b-fb15-3a65-952d-5fc3f7e3f79f | -8.50336 | -51.16177 | 2025-09-15 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4212dd5a-5266-3dbd-8843-9a4e64a2ed3a | -7.96627 | -45.63927 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15e0223-ec78-3dc1-8477-a20933b20c05 | -7.39381 | -49.99356 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7e446a8-47dd-3918-871c-2fcd87677ac5 | -6.40961 | -42.61871 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c55939d0-b12b-3b3f-b5a8-655a96789f08 | -6.97005 | -44.5493 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 752a8768-e12e-31fd-925c-03787127e02c | -6.16259 | -41.1799 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0861a6c-61cf-3945-b046-b89576bf6b3a | -5.69633 | -49.19815 | 2025-09-15 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8586e467-5c66-3df1-8de3-73f7a36d5ad6 | -9.14062 | -46.95892 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8a71599-8329-32dd-a479-555ca2f3d42e | -7.05274 | -44.14445 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65024946-2b93-325f-b410-a89bde33434d | -4.86148 | -45.73327 | 2025-09-15 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59d8c686-f4b7-386a-b7f4-61d106bf3cc5 | -3.55695 | -53.52915 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a98dcf6b-52b3-3cd0-96d3-d674b48ebfdf | -7.38989 | -49.99662 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc96b9eb-cb98-3211-850c-8242eb9293f6 | -6.41559 | -42.61342 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c34bf77e-3560-34cc-8d47-f432f97125f7 | -7.88638 | -43.58347 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 193.0 |
| 93ab0512-cccb-3076-b2b6-79dabc8562e9 | -6.21182 | -55.66628 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b3be9fb-e496-3657-9e79-93e59c77919f | -7.05521 | -44.1171 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e63ad387-5a29-3255-9b5b-02dde64de132 | -5.47237 | -44.68934 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3edaab13-4ddf-3973-8aee-7fbfc81c6cbf | -7.98458 | -45.66226 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5987f81-f269-3d11-a98b-2542758c6b4d | -6.63089 | -44.73009 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8efa8133-5336-3606-8b39-bfcdec5c6086 | -7.50967 | -44.36658 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2ee76db-82f1-38fc-8a38-d316c713320e | -10.39784 | -48.6121 | 2025-09-15 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9de7c7c1-26e0-360a-80d6-5d907bcf45ba | -10.15325 | -46.14458 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d33b39c3-0e6f-3252-9cd1-9b959e5137a2 | -7.69616 | -48.86478 | 2025-09-15 04:49:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 581d83f4-c7b6-32c7-a196-e7d2429cae74 | -10.63756 | -44.21372 | 2025-09-15 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 309dde7b-60b1-36e4-a94f-f40ef587e0c4 | -8.91417 | -45.48483 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bb07f00-ac6c-3716-a2ce-071266a33d14 | -9.05138 | -45.71243 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dfd3004-42f0-359a-beb8-a2ae02b7020d | -6.97979 | -44.54561 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README46.md)
