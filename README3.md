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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b4e62614-4947-3298-ae06-e60185a6e5a5 | -7.2857 | -46.261501 | 2026-07-09 00:33:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48330414-71dc-3968-a62f-8043d96fcac1 | -7.2923 | -46.245602 | 2026-07-09 00:33:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf4336c0-bf8f-3575-b11c-bcf8b26da63b | -4.3495 | -47.761299 | 2026-07-09 00:33:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac19a3c-4a82-3d09-a447-4d0099987113 | -10.7566 | -45.026001 | 2026-07-09 00:33:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bbd43736-d89f-3429-822c-3614667dd2c0 | -12.1794 | -43.4552 | 2026-07-09 00:33:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64645e31-93db-3ed7-9f14-25a46c316b68 | -10.7751 | -39.345501 | 2026-07-09 00:33:00 | METOP-C | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0262d835-e14a-33b6-ba19-90326aed46ae | -10.8586 | -47.593498 | 2026-07-09 00:33:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb73295e-80b5-3ff5-b4bf-638e5ed957de | -12.7563 | -44.525002 | 2026-07-09 00:33:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 319bb382-851f-38f6-85ca-c40d57d37ad8 | -6.6733 | -47.513302 | 2026-07-09 00:33:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 392a5a2d-2ca9-368e-baf6-4d7b835c63fb | -14.1458 | -52.881001 | 2026-07-09 00:33:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 89231191-769b-344d-bbd9-aafec3c391d9 | -13.3116 | -43.7075 | 2026-07-09 00:33:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e6c7cd2-b056-3e56-9ea2-f5e6430bea99 | -6.9426 | -43.707401 | 2026-07-09 00:33:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2201a474-28e5-31a5-9511-1a512c8a7331 | -23.558201 | -47.5103 | 2026-07-09 00:33:00 | METOP-C | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b7091cd-4ddf-31b1-b307-b3d5d39cd96d | -12.9247 | -49.482399 | 2026-07-09 00:33:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d62ce7b-1091-36f1-b5e9-af6500388823 | -17.7943 | -43.872398 | 2026-07-09 00:33:00 | METOP-C | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cb378e30-5cdf-3f16-856b-bdaf9e76dfc0 | -8.9651 | -48.003799 | 2026-07-09 00:33:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04c7feef-2a88-379d-b4dc-342db90fd673 | -17.5923 | -44.493999 | 2026-07-09 00:33:00 | METOP-C | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2cd154ac-61b2-37a0-92ee-7d9d1c7ab1a1 | -12.7596 | -44.539101 | 2026-07-09 00:33:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c44e4e0a-5e08-307c-8028-0a24ee8d40ad | -7.6333 | -50.023499 | 2026-07-09 00:33:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0883747a-4705-3a6f-b520-392cf652cb85 | -8.7307 | -48.337502 | 2026-07-09 00:33:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08395471-5f85-37e1-9177-8be2e0fc0cb5 | -8.3552 | -45.392899 | 2026-07-09 00:33:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82c68a6d-a42b-3718-8e34-88057331de48 | -9.3344 | -47.906799 | 2026-07-09 00:33:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 995e2f65-04f0-3171-a0a6-46a7e72969ad | -12.9267 | -49.492001 | 2026-07-09 00:33:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd63e4a4-489a-3810-a82c-37d35145a8f6 | -13.9466 | -53.899799 | 2026-07-09 00:33:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40fe9df6-8a84-367f-b3d5-9ce51744c12e | -7.2939 | -46.252499 | 2026-07-09 00:33:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc50d135-5d00-365e-b5f9-901bdee80e85 | -4.3397 | -47.7635 | 2026-07-09 00:33:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67a7d43c-f269-335f-a11f-ae60cd36d221 | -11.8309 | -48.2379 | 2026-07-09 00:33:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81bcafb9-955e-3989-8d90-a7b55eed0af6 | -9.5671 | -49.1064 | 2026-07-09 00:33:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d61b5af8-a0a9-3c36-be8f-096162abd1bf | -8.1156 | -47.104099 | 2026-07-09 00:33:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d5c3e62-8145-3437-ad26-ebe468e2dd4c | -8.347 | -45.4021 | 2026-07-09 00:33:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b40f5055-763d-3e05-8965-f74d69d33daf | -12.9345 | -49.480301 | 2026-07-09 00:33:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d039e538-e90d-358e-bcf9-a7c535badf7b | -8.3689 | -48.236301 | 2026-07-09 00:33:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1beda6c1-0804-3109-a2aa-86ec2e2c407b | -12.7547 | -44.518002 | 2026-07-09 00:33:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de54990b-daf5-37fc-9eaf-cbd336419c9a | -7.2825 | -46.247799 | 2026-07-09 00:33:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b008ae6-af79-30d9-8a0d-f9a7839d7283 | -8.729 | -48.330002 | 2026-07-09 00:33:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67f710d5-bf4d-3aae-be8e-e0ce68574652 | -7.8261 | -49.312901 | 2026-07-09 00:33:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aea7606e-9b62-390c-b698-8c4cf4d13a4c | -8.7192 | -48.332199 | 2026-07-09 00:33:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c2052f2-2109-3517-9d85-41100fb0e467 | -3.2006 | -49.053398 | 2026-07-09 00:33:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93799330-85b4-3d37-b141-0a793929b49f | -7.5405 | -46.023102 | 2026-07-09 00:33:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c56d2095-4aa5-35ae-b745-7599eeb46977 | -7.8243 | -49.304798 | 2026-07-09 00:33:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1754f84b-3e9c-371c-ba8b-ce1b16807a36 | -12.9227 | -49.4729 | 2026-07-09 00:33:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ebd6b69-0494-381d-9751-a002b64f5d48 | -17.5898 | -46.6833 | 2026-07-09 00:33:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2e14a0c-ddc6-3cf8-bc38-20179946f2e3 | -7.8341 | -49.3027 | 2026-07-09 00:33:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8807ec5-76d2-3c98-8f04-cdf928fe38c6 | -8.1238 | -47.094898 | 2026-07-09 00:33:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 111d62a7-25ee-37be-a1a2-968f6d41f999 | -8.7111 | -48.341801 | 2026-07-09 00:33:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d46b6c9-5d3d-3c9c-85b8-307f3be8edd3 | -17.586399 | -46.667198 | 2026-07-09 00:33:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e36d92bd-b4ac-3b3c-abf5-2068759afbb4 | -10.8512 | -45.033699 | 2026-07-09 00:33:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0fdb891-7346-3520-9a3a-f216c39dc9af | -8.3454 | -45.3951 | 2026-07-09 00:33:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd6d9e4-4e39-344b-bc42-572e7a9301aa | -12.7741 | -44.5396 | 2026-07-09 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 8d1688d9-50b9-3588-91b2-cf5b63b7c80b | -9.0155 | -63.5411 | 2026-07-09 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 28510890-e9fe-325e-8b0c-cc549fccf520 | -12.7548 | -44.5428 | 2026-07-09 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 9e270d8f-2bf5-3203-9e73-15c9401fe785 | -14.9147 | -43.4152 | 2026-07-09 00:40:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 49.5 |
| 06954ac6-560b-32ad-bcfe-ab7acc3aa5ff | -12.7746 | -44.5162 | 2026-07-09 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bcbb6ad1-56e5-3815-8cd3-9553430492de | -12.7553 | -44.5194 | 2026-07-09 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 29c7a56e-7e83-38b8-b7f7-300c376a0e71 | -14.9141 | -43.4394 | 2026-07-09 00:50:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 8d6b199b-6680-3cc8-87db-ac185c96e9f4 | -12.7553 | -44.5194 | 2026-07-09 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 00033538-6350-33f6-aa8c-f639e1341fc7 | -12.7548 | -44.5428 | 2026-07-09 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 85113bd8-b21d-31ba-b1f3-6492d4cb9b06 | -14.9147 | -43.4152 | 2026-07-09 00:50:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 78.2 |
| 4a29b5ea-763c-3081-bded-baf0a4028bc2 | -14.9147 | -43.4152 | 2026-07-09 01:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 58.7 |
| acf8b569-2467-3282-9da1-0d44594aced6 | -12.7548 | -44.5428 | 2026-07-09 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a93bf595-7610-3926-aa87-cd42010d85a7 | -12.7746 | -44.5162 | 2026-07-09 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2ca5e9cd-bde1-31c4-98ed-45d3827b25bd | -12.7553 | -44.5194 | 2026-07-09 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| ec96d0b1-db1d-3c74-af75-fa65ba6b2a79 | -14.9141 | -43.4394 | 2026-07-09 01:00:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 69.5 |
| a450b1d1-64ce-31ab-9788-71309806cb98 | -12.7553 | -44.5194 | 2026-07-09 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ed21e35f-9cc7-3123-ac63-f117e89d2cbd | -14.9147 | -43.4152 | 2026-07-09 01:10:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 51ef117f-1791-32e8-a0df-4bc5c30fcd63 | -12.7548 | -44.5428 | 2026-07-09 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 60554069-db07-38b0-8cc1-7600cb62a1b5 | -6.9326 | -43.7032 | 2026-07-09 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 64101439-6a98-3715-9fb6-936df9cea813 | -14.9141 | -43.4394 | 2026-07-09 01:10:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 71.0 |
| fae37c23-5597-3501-90e2-55087d19463c | -12.7553 | -44.5194 | 2026-07-09 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4181b391-6f78-3fdd-a11f-f48e2c97542c | -14.9141 | -43.4394 | 2026-07-09 01:20:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 62.7 |
| 5991cbd1-0163-3128-bdfc-08a94730de19 | -12.7548 | -44.5428 | 2026-07-09 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 58792cb0-1eb3-3320-aa93-79cafe19135d | -22.9147 | -49.2161 | 2026-07-09 01:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 52.3 |
| b2fdba61-a685-3b33-a84d-441c46f91089 | -9.02238 | -63.54054 | 2026-07-09 01:20:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 798dfabe-b0d4-3bd8-a159-6764e9ed0d1b | -9.02061 | -63.52865 | 2026-07-09 01:20:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a4c64cf9-dad4-32c1-93d7-5d076c0095ac | 0.86823 | -59.70419 | 2026-07-09 01:22:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 69730827-53ce-3cab-becf-35bb76b0ff63 | -12.7553 | -44.5194 | 2026-07-09 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c5e550e1-8876-39cd-9292-94ed95345933 | -14.9147 | -43.4152 | 2026-07-09 01:30:00 | GOES-19 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 60.3 |
| d1a69bf1-d362-36b8-9f26-0885e9b18bcf | -12.7553 | -44.5194 | 2026-07-09 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b45a6256-3cd3-387b-aeda-bb9f073f224e | -12.7553 | -44.5194 | 2026-07-09 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9a504c4e-51f7-34f2-b515-6db4ce1e30fe | -12.7553 | -44.5194 | 2026-07-09 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 09c54ed0-7961-3935-98fb-43ff7dfc8c21 | -12.7553 | -44.5194 | 2026-07-09 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 67f32eaa-7eca-3bd9-9aed-519de0d037dd | -15.462 | -49.6303 | 2026-07-09 02:40:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 245b717e-2488-3dfa-a088-b7b7fcc83e7c | -22.64 | -47.9719 | 2026-07-09 02:50:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 3fb2faf6-2fb4-315a-9f29-96397aca8e26 | -9.45678 | -38.92003 | 2026-07-09 03:13:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 51e61569-5b58-359c-a5ee-efa53bce84e8 | -9.45419 | -38.9168 | 2026-07-09 03:13:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 892bb1cb-00b1-3fde-b39b-102a85bde460 | -9.46014 | -38.91797 | 2026-07-09 03:13:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4347d63c-2f2e-3db7-aeaa-d8ecbe1c7dcd | -9.45503 | -38.91234 | 2026-07-09 03:13:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 56fcaced-e7d1-3a76-93e3-6ae51b3d65d9 | -9.45764 | -38.91556 | 2026-07-09 03:13:00 | NOAA-21 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b068bb50-6009-33d9-84e9-129c0a0bdbee | -14.91856 | -43.42666 | 2026-07-09 03:15:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 98e2dff7-2a21-3526-af70-30eef3f6fac4 | -14.90992 | -43.43224 | 2026-07-09 03:15:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a5a87ed4-720c-3f97-a9d5-1389a30f3101 | -14.91696 | -43.43375 | 2026-07-09 03:15:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.6 |
| e365637d-e91c-3420-803e-df698346dc4c | -14.9207 | -43.43059 | 2026-07-09 03:15:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 2b88bbd4-d888-3e98-b1a3-605948ce0585 | -14.91152 | -43.42517 | 2026-07-09 03:15:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 69f69a7f-beb0-3025-9229-2f829da77aa7 | -14.91366 | -43.42908 | 2026-07-09 03:15:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 402def61-e135-373a-a818-2f609bc9256e | -21.4745 | -54.4769 | 2026-07-09 03:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 116.8 |
| da650b46-0b75-3600-9018-f10e76818146 | -21.454 | -54.4805 | 2026-07-09 03:40:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5c9ba29e-1e04-3791-83b5-41328773a127 | -12.34874 | -47.42001 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 026baeef-82ad-3051-965d-4b4629e4f8bf | -12.84801 | -44.35298 | 2026-07-09 03:47:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82e2301e-7756-3c1b-ad91-89073e438830 | -12.34712 | -47.42511 | 2026-07-09 03:47:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fec34b3c-823e-3cfe-87f9-6f7479d532c3 | -6.99801 | -43.11418 | 2026-07-09 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README4.md)
