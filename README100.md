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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ac56865-fbc8-3f25-88d1-da623fcc538e | -15.75 | -43.81 | 2026-08-30 17:15:00 | MSG-03 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0e4f7b2-efcf-3a4f-9928-ef96a2602767 | -10.71 | -47.2 | 2026-08-30 17:15:00 | MSG-03 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f24a02d8-94b6-399b-b269-0e4341d979ee | -12.11 | -47.28 | 2026-08-30 17:15:00 | MSG-03 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 426d6a55-8222-358d-9a89-97ef94cba42d | -15.36 | -53.84 | 2026-08-30 17:15:00 | MSG-03 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ccfc293b-7b23-34e3-ad1f-c72e2e5271b5 | -14.61 | -53.61 | 2026-08-30 17:15:00 | MSG-03 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a120dabd-e9f0-3cef-b183-b21d98df6a85 | -6.84 | -41.71 | 2026-08-30 17:15:00 | MSG-03 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46a3e3ed-f7f3-3a0c-b6b6-ebb976f0a8c6 | -11.06 | -51.45 | 2026-08-30 17:15:00 | MSG-03 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c81f3214-c5a6-3fde-99c7-c4831d2d4c68 | -10.82 | -45.37 | 2026-08-30 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da080c0f-2c8a-3432-a0ef-508d4b601f7d | -6.861 | -41.6772 | 2026-08-30 17:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 263.8 |
| 80c35455-49fe-3d32-8048-26ced60375ca | -5.9636 | -57.6704 | 2026-08-30 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 596a6b6c-2d40-3548-86a2-e2e2436355c0 | -9.6941 | -65.077 | 2026-08-30 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c7bc786f-a1ff-376f-8aac-e0cf260dbe4d | -11.1634 | -50.5727 | 2026-08-30 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| ceef087e-fc67-3ab3-8c05-f00ef99df94a | -10.937 | -50.5118 | 2026-08-30 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6fe0a506-cbe2-378d-9502-642956c28e71 | -11.172 | -51.3151 | 2026-08-30 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3f8751d8-272d-3829-9b78-f7828d33a05d | -6.8412 | -58.9746 | 2026-08-30 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4e7637ba-7e47-389b-95c2-d6eb4f0311e1 | -11.1916 | -51.2708 | 2026-08-30 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 004332b3-6b41-3fb3-a785-a9fe2e563aba | -12.3618 | -50.5417 | 2026-08-30 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 8717ac65-5157-3c2c-af09-283e60388bd1 | -11.8205 | -51.0748 | 2026-08-30 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1d39dd6a-ae57-3c9b-90b8-8429e98ef1d5 | -10.9367 | -50.5332 | 2026-08-30 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c8e99526-36d4-3c4c-9a96-6492b62e4ecd | -11.1913 | -51.292 | 2026-08-30 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b79e69d2-cc00-3734-8dea-ef87d1b9cc1d | -8.9873 | -65.4379 | 2026-08-30 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 70154f46-037d-34f2-b673-4f6ef2438553 | -12.1902 | -50.5409 | 2026-08-30 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ab66cff4-f583-3097-ad4c-1f1b08edf629 | -8.3717 | -62.716 | 2026-08-30 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 12dd9da0-4cc6-388e-a82f-f97b4e966167 | -11.3431 | -45.1521 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 307.1 |
| 1bac7acb-2757-313a-ac41-00ac764a39fd | -10.7647 | -50.6579 | 2026-08-30 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 6a1008b0-25d6-3d5e-9d9a-b1fbe3c86137 | -12.3427 | -50.544 | 2026-08-30 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 41a8ea4c-2d9a-36fc-aa54-c5d4ed52b72a | -11.1726 | -51.2728 | 2026-08-30 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b5b7b682-7ec7-3437-aa03-86564fa672b9 | -3.4185 | -61.3273 | 2026-08-30 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d0b2746c-b6ec-3e65-b1b0-c5ecedb0e360 | -11.2443 | -45.3497 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 2ddfc8d4-c644-3792-816a-1451b6f345ff | -10.8249 | -45.3382 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 443.1 |
| 25402ae0-b9ea-3876-b80f-0143c6f3db00 | -11.1939 | -53.9993 | 2026-08-30 17:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| c6945d29-9279-3280-96c3-8535479f60b8 | -11.8208 | -51.0535 | 2026-08-30 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 30df8118-864a-3cf3-be48-715f99dd2351 | -7.9611 | -44.275 | 2026-08-30 17:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.2 |
| b0735d94-1757-3159-bc11-f15e0e6639d4 | -6.7123 | -58.9412 | 2026-08-30 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1c352108-99c0-3cda-bd4c-4de44d34aef0 | -11.2255 | -45.3294 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 476.8 |
| 2fd8155c-a96b-35e6-80db-4a42667a3b03 | -11.8021 | -51.0343 | 2026-08-30 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d27c603a-45f0-3994-b767-1a06f21561d7 | -3.1266 | -61.2 | 2026-08-30 17:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1463515a-6b2f-3aa7-8c8a-c525baf39198 | -15.3647 | -53.8307 | 2026-08-30 17:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| f3369d1a-d89e-361a-8c89-17da1196b771 | -11.3427 | -45.1751 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 515.0 |
| 60fbd634-8f12-3791-ad1d-7ec567103ca9 | -11.8211 | -51.0322 | 2026-08-30 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| dcadaf30-1034-35eb-8368-f58643f4b2f3 | -11.1723 | -51.294 | 2026-08-30 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a9bfa2cd-ea91-3218-aa4a-6ed5a8f2b440 | -11.0054 | -49.6893 | 2026-08-30 17:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c313eb1b-66ab-3582-82f5-032924006a39 | -10.9177 | -50.5352 | 2026-08-30 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c18fc609-bd77-3cc5-92f0-0e92ebf7af04 | -7.9419 | -44.3001 | 2026-08-30 17:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 42489357-f426-327b-8f1a-75c8e4673984 | -12.3424 | -50.5655 | 2026-08-30 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 13eafc38-74e4-39d2-877d-ba0ab9e864b5 | -10.899 | -50.5159 | 2026-08-30 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| db3a2fbd-7da8-395e-aa52-7937d27ba698 | -5.8721 | -57.5569 | 2026-08-30 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bb9d325c-61b4-37af-9cd8-52ef354d53ed | -3.4002 | -61.3276 | 2026-08-30 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 131d6df9-6834-3746-bed6-0761b9ae7e92 | -11.2446 | -45.3267 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a98d08a7-da5f-3282-a303-49667ac6a761 | -10.918 | -50.5138 | 2026-08-30 17:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3c8bd130-634e-32cb-a4de-be91e5a0dbe6 | -5.982 | -57.6697 | 2026-08-30 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 211adef1-2ae8-3e7f-bcfa-3f03419eea1f | -8.948 | -62.3894 | 2026-08-30 17:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3965c5a4-a57f-34bf-8857-f010572b13d2 | -8.5925 | -66.9564 | 2026-08-30 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 72733584-5666-3dff-bc35-6c1ca0ceb4de | -7.1121 | -42.7963 | 2026-08-30 17:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 225.7 |
| 2e8dcf12-3bb7-3d23-9573-be44ecc40613 | -8.574 | -66.9569 | 2026-08-30 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.3 |
| b883b46b-f91c-34cb-9a44-79b3a1490784 | -11.245 | -45.3037 | 2026-08-30 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 501b9762-18a9-38fe-8522-b05ecf8be8ca | -8.9478 | -62.4084 | 2026-08-30 17:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| a4a7bde8-7c5b-3348-86fe-eda509f0b4c2 | -21.0176 | -57.8103 | 2026-08-30 17:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| f59a7320-855d-3dc2-85f4-e7dbe30662b6 | -3.4278 | -58.0009 | 2026-08-30 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 8c5ef4c7-baa3-30f1-b28a-213abce4b941 | -7.9611 | -44.275 | 2026-08-30 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| ebcfcf5a-e339-380e-8db0-4356b931e14c | -21.0172 | -57.8313 | 2026-08-30 17:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 95353a05-cae6-3261-b4b4-3c68edc416c2 | -12.1902 | -50.5409 | 2026-08-30 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| c4a93b50-7efe-366b-9605-691d53246e8c | -7.1312 | -42.7708 | 2026-08-30 17:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| a6dbf99e-22f6-3b48-9a57-b3d0dd1f44ab | -7.9419 | -44.3001 | 2026-08-30 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 176d4bdd-dedf-3087-81e3-c379fe85b7cf | -11.3619 | -45.1724 | 2026-08-30 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 523ec90c-d918-37f8-97a9-af94b4dba927 | -11.1939 | -53.9993 | 2026-08-30 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| f613fc0f-71cc-3f48-8a59-3eb4720d16dc | -11.1634 | -50.5727 | 2026-08-30 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| cb887867-893a-39b6-a4d2-f11ee82f03bc | -7.9422 | -44.277 | 2026-08-30 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 3f2bde22-664b-3337-87ba-3b3bc45d12dc | -13.4516 | -57.0592 | 2026-08-30 17:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 5bb3afcf-7273-397a-b7aa-16ab41b2ca7a | -13.4187 | -51.4372 | 2026-08-30 17:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 78a0cf01-8b64-3e0b-bf01-2909b29e6a01 | -10.8425 | -50.5005 | 2026-08-30 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b2829058-19f2-3f83-b773-0d4533f7187f | -11.8205 | -51.0748 | 2026-08-30 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| b7d532fb-18b6-3797-a382-fd09edc9c1f5 | -8.6487 | -62.8376 | 2026-08-30 17:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| ea5a9a72-1340-3b19-adfe-19c846420d53 | -8.616 | -54.7339 | 2026-08-30 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ac6fbdcc-45bf-30a8-aef2-cc3350829d7a | -11.2443 | -45.3497 | 2026-08-30 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 3c50ffb6-5c09-34fa-862e-d8bfe7ded639 | -8.6161 | -54.7137 | 2026-08-30 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b6206fe3-d574-3d73-a9ea-b6af4253d768 | -11.3427 | -45.1751 | 2026-08-30 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 641.1 |
| 2b4665fc-a3ed-31a7-a65c-6b0943c2d853 | -10.9405 | -50.255 | 2026-08-30 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e4b82871-21df-37d5-9b31-8e3e41702cd4 | -3.1266 | -61.2 | 2026-08-30 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d560e59b-be1d-31a1-8e1a-80b276e07c63 | -5.982 | -57.6697 | 2026-08-30 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fd61a111-7eb5-330a-ae7d-15143b740ba3 | -11.245 | -45.3037 | 2026-08-30 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b0841d71-0bf7-3937-aaf8-df3444b6dedb | -6.861 | -41.6772 | 2026-08-30 17:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 290.3 |
| 77366c7a-5700-3b3b-88fa-d38473de511d | -11.1723 | -51.294 | 2026-08-30 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 19a878b1-5f58-3688-aa3e-359fefbbfc61 | -8.3717 | -62.716 | 2026-08-30 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 77d85f2e-b311-3e2b-9fbc-786ea5c4cd20 | -11.3431 | -45.1521 | 2026-08-30 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 315.8 |
| 02c8bf75-c998-3c38-920d-d8e34edbadb0 | -13.4379 | -51.4348 | 2026-08-30 17:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 8f1fd0bd-ac32-36c4-995c-11def1ef546f | -6.7123 | -58.9412 | 2026-08-30 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| de91bb64-e241-33c2-8ef3-8e8bb93de6c3 | -7.1121 | -42.7963 | 2026-08-30 17:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 137.6 |
| d9a59918-0506-3bb7-b5a9-d9a37873b1fe | -8.6311 | -66.5287 | 2026-08-30 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| abca2d11-2972-30e3-acc4-aeae16372aee | -6.1108 | -57.7035 | 2026-08-30 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ccbeb862-0230-31dc-ad3e-307e3a61cea7 | -6.3322 | -54.7473 | 2026-08-30 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f11fd9e3-84fc-39f5-9e57-c0b45f119113 | -6.7691 | -58.6873 | 2026-08-30 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 629666ed-ba26-3be5-81ba-3e7a13a551cb | -10.5598 | -50.4236 | 2026-08-30 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4870613f-14e4-3476-8e83-eab1782d19fc | -6.9872 | -59.2582 | 2026-08-30 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 3ab5076f-a0eb-326b-a2f9-a303986e4fda | -10.9592 | -50.2744 | 2026-08-30 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| a523ac21-9b25-3352-85fe-767a5189503d | -5.9636 | -57.6704 | 2026-08-30 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| d2890413-0beb-3764-91d0-7014717f3a3d | -3.4002 | -61.3276 | 2026-08-30 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 13800182-e15d-3648-b09e-7dfc34537486 | -19.0944 | -57.3849 | 2026-08-30 17:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 165.6 |
| e73bfabc-bdd5-3b18-a30d-71b9415bef2c | -10.5601 | -50.4022 | 2026-08-30 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7f8af89e-4f00-3799-8c29-c995a431bfe6 | -8.3944 | -72.5825 | 2026-08-30 17:30:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 45.3 |


[Clique aqui para ver as próximas entradas](README101.md)
