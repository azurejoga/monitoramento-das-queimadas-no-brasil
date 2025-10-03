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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b743af6-55bf-3e67-9084-f825f718026a | -13.155 | -47.8121 | 2025-10-03 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| c592ac76-92e1-35c1-8fab-056cf1df4aac | -7.7749 | -42.5628 | 2025-10-03 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 189.0 |
| 69917385-5705-3e16-8fb9-45f6f5024ec9 | -11.8818 | -44.9815 | 2025-10-03 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 41465c80-2f97-3f84-93a2-b151c2631570 | -7.756 | -42.5648 | 2025-10-03 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 499.8 |
| fabd6627-670e-3715-b78b-73527450c7c1 | -10.1092 | -50.2349 | 2025-10-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c387624a-c824-3865-8a34-ca3c3c1ae623 | -5.6845 | -42.7092 | 2025-10-03 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| dfdf37fa-e068-3d05-86c2-be307f1de93a | -6.5551 | -43.8758 | 2025-10-03 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9aa058f7-5995-38aa-bf4e-167f6dc91a2b | -10.0339 | -50.2211 | 2025-10-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9daece43-61a3-3b42-9535-875552013f8a | -12.6131 | -46.9725 | 2025-10-03 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 74225ba8-6756-34d9-82ce-35f2e1cc5575 | -13.3611 | -48.1159 | 2025-10-03 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d8c5bc5a-3e76-3c08-a034-61988a55bf40 | -8.9118 | -46.6052 | 2025-10-03 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4eea9da7-aed0-3fdc-9406-68bd036af0bf | -7.7941 | -42.5369 | 2025-10-03 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |
| 634ceeb2-8941-30f2-99f4-bc3fbc4cadb6 | -5.7033 | -42.7077 | 2025-10-03 14:20:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| abe24562-bd87-3dcb-83c4-35c16702b8e1 | -6.679 | -42.8136 | 2025-10-03 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 313692ef-450f-3d7c-9c6e-2e7e9eb56159 | -13.8447 | -51.2328 | 2025-10-03 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| eb3df8fc-77a3-3c67-8618-d2543dad325b | -6.6604 | -42.7917 | 2025-10-03 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 3e391f0c-b20e-3a91-a2a7-4ca4d04969ed | -6.0809 | -42.4881 | 2025-10-03 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 0de2f24b-179b-3e2f-9c0c-76553e129aac | -8.8222 | -44.8043 | 2025-10-03 14:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 4afd4d3a-2061-3fda-8b07-c7b7ccc00c9c | -14.6497 | -44.7499 | 2025-10-03 14:20:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 81abf18c-8610-3fc0-bbce-667f7e15c30b | -9.8772 | -47.8103 | 2025-10-03 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f0ec02c4-5e59-35d6-8490-46b0b3aa98d8 | -6.6976 | -42.8354 | 2025-10-03 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| f2a2ac64-1a29-3369-a6fb-21c552f7feff | -10.8524 | -47.2094 | 2025-10-03 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 832e7b0b-5c54-3e4e-9372-deb89b9bcc9e | -11.9155 | -46.3272 | 2025-10-03 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 433.9 |
| 7ded8865-28cb-3ae6-9b81-931ee06bda09 | -7.4469 | -46.4777 | 2025-10-03 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 9a61ae5a-d7b2-3cbf-b18c-81a216f636ed | -8.1888 | -44.1588 | 2025-10-03 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 49fc06ce-edf6-3681-9b59-c8b425a1f5e5 | -7.5693 | -42.3945 | 2025-10-03 14:20:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| ceb90871-0f74-30ae-947b-df9ac05538e3 | -11.0225 | -49.8167 | 2025-10-03 14:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| e6ef07cf-7e00-34e2-99fe-09970522c5a8 | -14.0227 | -44.9576 | 2025-10-03 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| e4eba108-5d74-3c43-9ad3-91fc0993358f | -13.8247 | -51.2782 | 2025-10-03 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 65d685e4-4ce7-3286-9173-d3661cb3ee88 | -11.863 | -44.9612 | 2025-10-03 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 07a8d185-41cf-3ff2-8441-4b381eceee60 | -9.3386 | -45.7493 | 2025-10-03 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 02b246ae-a889-3066-af54-1eabc375d56b | -8.8543 | -46.6781 | 2025-10-03 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 43240c5e-b4a7-3ef7-b7bf-00388c332f15 | -8.8729 | -46.6985 | 2025-10-03 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 70aa94fb-6103-31bc-878e-da61c5f1d59d | -13.7862 | -51.2833 | 2025-10-03 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ba3f94eb-cf34-30cf-9de4-594eb1f81b73 | -9.8769 | -47.8324 | 2025-10-03 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 334b6af1-4e48-3623-abd2-2f0c6fe64331 | -16.023 | -50.8553 | 2025-10-03 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 5c1d23e6-5880-30ae-ba93-68021e26f2b2 | -9.9035 | -45.9553 | 2025-10-03 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 34fcc095-9352-3345-81a1-3cd2cce1d963 | -6.0621 | -42.4897 | 2025-10-03 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 2e0bd436-383f-3bdf-b1d2-8dd4e0197726 | -11.1275 | -47.8634 | 2025-10-03 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7dfa3e7b-ee64-32ec-badc-f07bf1e05e9b | -14.0037 | -44.9376 | 2025-10-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.6 |
| ffe9b256-5fa8-3006-8499-bda6fc86c115 | -9.3386 | -45.7493 | 2025-10-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dd06a004-ef52-3bda-b083-e8fee1e9b731 | -7.7306 | -46.2737 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ae5e835b-ecd1-3212-a191-ed025e38602e | -13.7862 | -51.2833 | 2025-10-03 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 2f8c2b93-4c84-3a2b-9eb0-16e56ca8a2c3 | -9.0989 | -46.7195 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.8 |
| f51792f3-5e16-3556-a050-d34c858d9494 | -13.7858 | -51.3047 | 2025-10-03 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 09588f39-f861-3865-a265-4416b7fbcf66 | -13.1936 | -47.8065 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 3f5ec5f3-4e0d-343b-ad1d-bd647bf26b9d | -13.7865 | -51.2618 | 2025-10-03 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 7f06e1b1-b5d5-36a0-9a7f-864e2d6f4288 | -3.748 | -41.0723 | 2025-10-03 14:30:00 | GOES-19 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 75f76f5f-7c0f-3412-9de0-a82844730aca | -13.1156 | -47.8625 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f2ff990c-5b55-329a-a636-f36f1e9474df | -7.7125 | -46.2082 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| dbe062dc-ae8f-3c60-94e4-ed40ec748398 | -11.863 | -44.9612 | 2025-10-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 40ebe66f-896c-3d33-8a87-6b219d08ab45 | -12.6131 | -46.9725 | 2025-10-03 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 8a538825-e6c2-3727-a95c-d4cc2e528d53 | -7.4469 | -46.4777 | 2025-10-03 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 70f9bfeb-1586-3a88-96a3-1f585359d519 | -11.1252 | -43.3874 | 2025-10-03 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 71195109-e964-310a-8860-b6645e3364cd | -5.8472 | -43.3762 | 2025-10-03 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 85c88372-6356-3530-a0f4-1f86e3b6b51d | -8.5035 | -50.9947 | 2025-10-03 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a06c622d-d51c-3af8-b989-9aed01e1c830 | -11.4988 | -44.9915 | 2025-10-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| c69d2b98-97ad-38fd-a0b2-e64c2d677a48 | -8.1702 | -44.1377 | 2025-10-03 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| daaa36b1-d8d4-3542-aa29-f9b5d0fcc09f | -7.7752 | -42.539 | 2025-10-03 14:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 448.1 |
| 1ad5dd36-cd68-3589-a0e6-7a039398609a | -13.1919 | -47.8959 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| bbce416f-2e9c-31e0-9619-b1b98024be23 | -10.1095 | -50.2135 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fa0e3f47-5100-31ea-a7c7-ae56163db29d | -10.1089 | -50.2563 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f1d2f443-a376-3de8-9f12-32dde7ec80de | -7.7941 | -42.5369 | 2025-10-03 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 167.0 |
| 1b12ca54-c953-36f9-84e4-34cc1ff00dd3 | -14.2316 | -46.1024 | 2025-10-03 14:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 350df9a0-1013-3811-b89b-f24aac2d292e | -13.6724 | -51.1911 | 2025-10-03 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e36cb2c8-1a7d-37ce-bca2-0f9659606d41 | -9.9394 | -43.5777 | 2025-10-03 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| 9d165cff-a538-3706-a52d-2506536585da | -10.0526 | -50.2406 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 11377866-efff-3ae0-b378-005800519f2e | -14.0032 | -44.961 | 2025-10-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 344.9 |
| 4607544c-3872-363d-88e5-565b3d33190d | -5.6845 | -42.7092 | 2025-10-03 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| f7d29dd7-3017-3996-a616-cb58bd610bb4 | -14.3675 | -46.102 | 2025-10-03 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 196.9 |
| cd26da34-7e1f-3c12-8b44-87efca1bfc7d | -7.7749 | -42.5628 | 2025-10-03 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 207.1 |
| 9ae5ea6e-cfb3-353c-b572-e1284d46d617 | -9.8769 | -47.8324 | 2025-10-03 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| cec353dc-e2a2-36d0-8122-cec1a46da3df | -9.9391 | -43.6012 | 2025-10-03 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 6f4cc92e-791e-3876-b34b-b0a719f2dedf | -8.1917 | -47.0101 | 2025-10-03 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 192.8 |
| ec2fa087-594f-36e6-9153-4af88f437fdc | -14.2944 | -45.8845 | 2025-10-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| d677304e-db92-3d06-97ed-4261c9fad654 | -11.8238 | -45.0132 | 2025-10-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d74223a6-4b1e-3354-9db6-9a2e522ed113 | -14.2934 | -45.9307 | 2025-10-03 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.0 |
| bf69e688-1bc2-3f79-a2e6-b3abc4c9f10f | -10.019 | -48.4964 | 2025-10-03 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 3deb9ddc-687b-3a1d-97e7-e7cb59c3ac88 | -7.7496 | -46.2496 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.2 |
| b25d8f9a-afc9-3e07-8039-61c4003969a4 | -12.1088 | -45.1554 | 2025-10-03 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 50b999de-e6be-3c41-8a59-2fcb19875132 | -5.7033 | -42.7077 | 2025-10-03 14:30:00 | GOES-19 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| d3021e4a-deb9-39d5-bb41-226def9d9e76 | -11.8626 | -44.9844 | 2025-10-03 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 815b3c14-873a-3dc3-aac6-7dacc444fb20 | -11.9155 | -46.3272 | 2025-10-03 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 271.2 |
| c5baf702-6579-3f51-8288-71bd52d257de | -16.0413 | -50.9177 | 2025-10-03 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 8f5f5338-c179-3868-9430-ca47255fcb08 | -14.8063 | -51.424 | 2025-10-03 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 86f5ef5e-b0da-3cd2-afb8-69b42b570145 | -6.3532 | -43.4283 | 2025-10-03 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2b3b7831-3c6c-3871-8989-2330a889446c | -13.1345 | -47.882 | 2025-10-03 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 6a21c94e-5d10-3bf5-a41a-cf3fa4efabec | -9.3749 | -45.8584 | 2025-10-03 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 18d078f3-3019-3cbb-ad79-a059f4f434f5 | -9.9372 | -43.7187 | 2025-10-03 14:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 204.5 |
| 19fe78b8-2fad-3851-a834-e91a1c209ddf | -5.4779 | -42.7485 | 2025-10-03 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 9d753488-67f0-35b8-a6d0-e311919b4f58 | -6.3973 | -44.6481 | 2025-10-03 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 41bbdf7f-bc70-3286-b0a9-9cb74c41f259 | -10.0151 | -50.2229 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| ec1b7d17-6987-37f3-bf40-37a119f98bbb | -5.7133 | -43.6655 | 2025-10-03 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 252.1 |
| cfcabd56-6270-33c4-ba94-2c99d6c26156 | -7.7311 | -46.2289 | 2025-10-03 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 16eb58d0-373f-3a49-8f65-d49a58159ed8 | -11.1444 | -43.3845 | 2025-10-03 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 129.6 |
| c60670ef-7fcd-343c-aae8-095d603c5dd7 | -9.3389 | -45.7266 | 2025-10-03 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 66ed4024-dead-3c76-a7c9-f7a2158480f4 | -10.2779 | -50.3246 | 2025-10-03 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e9231d54-120d-3567-bd55-9996b0d2ce84 | -5.4964 | -42.7707 | 2025-10-03 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| 9f7e0ca8-db68-3b55-9f56-6776fe66ae9f | -8.1888 | -44.1588 | 2025-10-03 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 20c6d5aa-6418-3395-8927-12c953a517cb | -6.0621 | -42.4897 | 2025-10-03 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |


[Clique aqui para ver as próximas entradas](README155.md)
