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
| 74103e15-9deb-3bcf-8e0b-acf075acaed2 | -9.8047 | -46.2378 | 2025-09-08 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 886f934f-2eb2-3320-9b9d-8727669efd65 | -8.3239 | -46.9533 | 2025-09-08 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 6cfc6cbc-0b2b-39dd-907a-78dd2835cdb2 | -11.0234 | -46.0184 | 2025-09-08 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 53062759-de82-3a11-8141-17a4431b8dec | -6.2036 | -43.3709 | 2025-09-08 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4c8ea62a-c4c8-3735-ab97-f4b242520fb6 | -14.5251 | -52.0182 | 2025-09-08 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 3c9ed744-4e03-3221-9c49-50f26ad749a9 | -11.4135 | -50.3311 | 2025-09-08 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 537c5542-e43d-3419-a9ec-127348d0a3d5 | -19.1697 | -47.6729 | 2025-09-08 13:30:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f19ee08e-7b0b-3c33-9249-b8679af70936 | -6.6382 | -53.377 | 2025-09-08 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| af6f4bad-6d34-388e-af0a-0ae164d59075 | -10.8911 | -55.7131 | 2025-09-08 13:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 80b05e75-d4c0-3f76-8ed2-4b57457150b4 | -6.1024 | -44.144 | 2025-09-08 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 54fca7ff-9068-3b0e-a2d2-d3ecfdbe285a | -10.8722 | -55.7147 | 2025-09-08 13:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 095f553e-0f04-3e01-a40a-1a3598eccadb | -16.9615 | -45.8411 | 2025-09-08 13:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 27203d2a-5c04-3359-b20c-c3b6c1227632 | -6.6384 | -53.3566 | 2025-09-08 13:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 6043b03d-7248-353e-821f-ee8b6f0f840a | -5.211 | -43.2833 | 2025-09-08 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f3f3f10b-2c49-37f2-96be-108ca95fe695 | -11.4268 | -43.649 | 2025-09-08 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 55092186-b14b-3f48-8277-f7809488f44a | -16.9422 | -45.8217 | 2025-09-08 13:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| db7f85c6-2107-39df-8808-095d3e61e4c1 | -5.8354 | -42.6265 | 2025-09-08 13:30:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 5a62281a-adc1-3602-be48-789eb1d66717 | -11.2823 | -46.5043 | 2025-09-08 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 655312cf-71f6-3d30-8cb1-720f30ce4178 | -5.8485 | -45.3038 | 2025-09-08 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 28af9743-fd31-3fd9-a4f1-a30c4490fb2a | -7.6559 | -47.9593 | 2025-09-08 13:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 08eb371c-4524-3145-a126-25e076bec1e6 | -7.9928 | -46.3388 | 2025-09-08 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 9dcc92cc-204f-3307-b50c-cc9d3c2bca0a | -11.4128 | -50.374 | 2025-09-08 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| b2420a58-26a2-3a45-bd85-abd6161daca1 | -14.4359 | -48.4644 | 2025-09-08 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 03dec754-ec0e-3755-81d2-29e82c45d7ff | -10.8911 | -55.7131 | 2025-09-08 13:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| a48102f6-58a9-372f-b51a-f9a426967b5f | -7.7484 | -44.7332 | 2025-09-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 8585f041-e83a-3b54-97fd-981f090234aa | -15.044 | -50.1118 | 2025-09-08 13:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 1662f026-ba41-30a4-8e8f-cba44ce7264d | -14.527 | -48.7611 | 2025-09-08 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 913c5e9e-137b-3d5a-8cd7-6d01604d5016 | -6.1024 | -44.144 | 2025-09-08 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 5462daa0-d467-3f32-85d9-5f57002cdb33 | -11.0234 | -46.0184 | 2025-09-08 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 89386210-8216-3cda-b53d-a7a30badf074 | -6.4683 | -43.1848 | 2025-09-08 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 621cdc57-806d-333f-98ed-4d130abb5d72 | -10.0993 | -48.1595 | 2025-09-08 13:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 6429b832-649e-3487-89e4-6d538c4bddbe | -11.2007 | -54.9992 | 2025-09-08 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| f6a477b9-ac71-375b-afd0-635d055a37cd | -11.2823 | -46.5043 | 2025-09-08 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 73d48466-86aa-3127-b5ef-b141caab3bc9 | -6.6198 | -53.3576 | 2025-09-08 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 4def6b82-a1e9-3b7f-8cc0-1e5b6cf369d8 | -5.8672 | -45.3024 | 2025-09-08 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1258f56d-8502-3531-97ae-46a46efe85e3 | -16.9615 | -45.8411 | 2025-09-08 13:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 131.4 |
| f87f7fe2-b56a-3f78-80d6-c93f4455e0b0 | -11.4125 | -50.3955 | 2025-09-08 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 278.9 |
| 9a814df3-587f-3a96-bb1f-20144bb80719 | -11.4268 | -43.649 | 2025-09-08 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 8176503f-75cd-3ec7-85d0-e7b33956485f | -16.3345 | -52.9387 | 2025-09-08 13:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a963659d-b89b-3558-b42d-8f1a237c2705 | -12.948 | -54.7724 | 2025-09-08 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 65c3507b-479a-3003-9067-7bdb8dd6a9e4 | -5.44 | -42.7984 | 2025-09-08 13:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| bbde84ab-b4ba-397a-8d56-74cde765fd02 | -16.307 | -58.1055 | 2025-09-08 13:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| ad4a9ed5-dcc4-37b4-a82e-7b5ca66b639e | -11.2827 | -46.4817 | 2025-09-08 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4b07a778-87d4-3596-b4b9-06d9105d4045 | -15.2136 | -44.0255 | 2025-09-08 13:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 99c8d7be-4018-3484-b327-df770ecccb86 | -14.5076 | -48.7641 | 2025-09-08 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 2d34e5e2-2fa7-31e8-aa83-844dd1c14203 | -8.3239 | -46.9533 | 2025-09-08 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| fdd35d13-c84c-37de-90d8-a4729d28ed62 | -15.2735 | -52.3853 | 2025-09-08 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 532f68eb-98fb-3ae3-954a-70f51780de04 | -5.3671 | -44.7703 | 2025-09-08 13:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 799a9b63-f851-313a-a62b-9e68fdfa0d34 | -7.9928 | -46.3388 | 2025-09-08 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 55444400-79e8-3605-8b6f-ca5465b8baaa | -14.3681 | -60.3228 | 2025-09-08 13:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 177ed796-d8c8-367b-a8ee-aaf6301447d0 | -5.8081 | -45.6448 | 2025-09-08 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 40357970-28e1-3003-9d5f-067c98171e65 | -9.4611 | -46.4566 | 2025-09-08 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 40256278-5468-3b94-b5b8-75f8c0b81a48 | -8.0592 | -45.4998 | 2025-09-08 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 2ad014fc-7d50-3660-92a7-ff692616a30a | -5.6819 | -45.112 | 2025-09-08 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1a5766da-1b70-3d03-aad5-51f5abcd3bdd | -8.3179 | -47.4621 | 2025-09-08 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| eddaa7d0-06b7-3adf-bcf9-ad6594a3010b | -15.0635 | -50.1089 | 2025-09-08 13:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 0be2e895-31a4-3153-9369-e5d5d512686a | -16.9422 | -45.8217 | 2025-09-08 13:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fc33f2ef-f0bd-37ee-86c2-f6884f7249a7 | -9.481 | -60.4902 | 2025-09-08 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 88f19f97-345d-3d05-951f-20c666b0d602 | -7.6559 | -47.9593 | 2025-09-08 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 647225b8-67e0-34da-9ba3-6ae307c8395d | -8.4697 | -47.3376 | 2025-09-08 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| efda189c-0fce-35c2-bb9d-1b96cba4dfcd | -14.3492 | -60.3046 | 2025-09-08 13:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b2ebd6f2-d5e8-3ab0-bcf4-432ea9885b9a | -14.714 | -60.2551 | 2025-09-08 13:40:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| df70cf7f-4ca1-3a5d-bdbb-57143c4e0763 | -5.7113 | -43.8972 | 2025-09-08 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 40cf17a6-c468-3c1c-ae7d-e1ed48a91c8e | -7.7296 | -44.735 | 2025-09-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 9a34de64-62a6-3c8f-8646-a16f66660387 | -6.6197 | -53.378 | 2025-09-08 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4cba07be-a981-3795-b01d-9dbe84d0d7fb | -5.8485 | -45.3038 | 2025-09-08 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 42ef02fd-216a-34a4-bc09-a264bd21c1a7 | -14.2963 | -44.8852 | 2025-09-08 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 9c81b499-7d47-3b18-b816-44ef231e1f0a | -11.2827 | -46.4817 | 2025-09-08 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| af677f36-252b-3183-b500-b2e63d66c69e | -8.0594 | -45.4771 | 2025-09-08 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| c7a19842-d21d-3817-9fd9-ce0bec69b47c | -8.3179 | -47.4621 | 2025-09-08 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6ae25b80-9b0a-384c-a777-62d2b7a94f75 | -5.9565 | -45.769 | 2025-09-08 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| eda1e788-45ab-36d1-9b8d-9ff50e966163 | -15.2141 | -44.0015 | 2025-09-08 13:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 22991045-2788-3c61-8412-a72119b8b83f | -14.5648 | -53.0925 | 2025-09-08 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0c8ed507-1b37-3ff4-a5ad-71700eb48f4f | -12.8651 | -62.1074 | 2025-09-08 13:50:00 | GOES-19 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c3fbe072-4789-3a3e-a035-d5fdc79eca98 | -13.2986 | -51.7501 | 2025-09-08 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 75231e61-e251-345f-9a3f-6dc32af789f1 | -11.917 | -50.9787 | 2025-09-08 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 76fcacc1-dcdd-3b54-9b53-fa066e344260 | -6.2036 | -43.3709 | 2025-09-08 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| ec2cba38-0aef-3430-8adf-7114fa466c72 | -13.3178 | -51.7477 | 2025-09-08 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 61cbabb9-cb6c-3554-af7c-7751609fdf2a | -5.6106 | -44.7078 | 2025-09-08 13:50:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| b41e62e8-5b2e-379a-9264-fd50da8222fd | -14.3681 | -60.3228 | 2025-09-08 13:50:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 8967f121-051a-3808-9f76-3e16b78cd6d5 | -9.4611 | -46.4566 | 2025-09-08 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 79b8a525-72e1-36fe-ae2f-dac376e551ef | -11.2823 | -46.5043 | 2025-09-08 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8670c7fe-81d7-3798-82aa-e3189f86bd9b | -15.2136 | -44.0255 | 2025-09-08 13:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 145dd9ef-8f46-357e-be27-dc38f1fd6284 | -16.307 | -58.1055 | 2025-09-08 13:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| ae2f51a9-b19c-3425-bd15-4c8af46ad4d8 | -14.4554 | -48.4614 | 2025-09-08 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ef00a1e5-50ec-3061-8d8e-6109081b151f | -5.8081 | -45.6448 | 2025-09-08 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9959a86a-2a7b-30a7-8249-4776e6ff5ac3 | -7.7296 | -44.735 | 2025-09-08 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| b0c7da12-4c58-373d-8378-78880ef2bfd2 | -16.9615 | -45.8411 | 2025-09-08 13:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 5e73e7df-7900-33f4-b195-87a48870d65b | -7.7484 | -44.7332 | 2025-09-08 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9ff7f607-1f7c-3f2b-8a8b-539352c7d328 | -11.2007 | -54.9992 | 2025-09-08 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a56ebf8a-a2b4-366f-b65c-3a7cfa80ed1b | -15.184 | -47.9852 | 2025-09-08 13:50:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 145.5 |
| f07667f8-7d88-3a36-b6ba-497d0e2779ee | -14.4359 | -48.4644 | 2025-09-08 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 970cfbc2-ee86-3096-80c8-ca09e5dad739 | -15.2545 | -52.3666 | 2025-09-08 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 4f463b9d-3da3-3b8f-9547-d534956275c2 | -15.2541 | -52.388 | 2025-09-08 13:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0223fbb0-dd9c-3f8a-80aa-5ab0b24f3968 | -15.7377 | -53.5928 | 2025-09-08 13:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 12e4c2e6-bc33-3b50-a17a-5eef805cfa43 | -13.672 | -46.9696 | 2025-09-08 13:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b31d5221-5d0b-386e-adb2-1d6a292a5252 | -15.0635 | -50.1089 | 2025-09-08 13:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 7c424a69-f999-32eb-91d7-e830755721b4 | -7.6559 | -47.9593 | 2025-09-08 13:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f1a1a978-3589-35c8-9ac5-37bab7da3ab0 | -10.0993 | -48.1595 | 2025-09-08 13:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| f60a358e-eb64-38c0-87d9-945339983743 | -5.211 | -43.2833 | 2025-09-08 13:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |


[Clique aqui para ver as próximas entradas](README99.md)
