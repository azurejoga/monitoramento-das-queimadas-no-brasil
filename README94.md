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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dacecf2f-82af-3845-aba7-2770ebc657b8 | -3.41216 | -50.16105 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a49f07f-7044-3475-93b1-99e8f52a3219 | -3.26224 | -48.89421 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5b3bfdd-8550-3543-b6a4-d1d022b66b24 | -2.98206 | -53.28756 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8267252e-b08f-3345-a82b-843d43631771 | -1.23165 | -51.80359 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce966f4b-388e-38a2-b1fe-df5f592b7e38 | -0.9647 | -51.71642 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2fa6f8f-8d54-3808-920e-d3bee7592176 | -2.42336 | -48.54448 | 2024-11-30 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f65719d4-2a3d-3e0a-86bd-3415ec53fb4a | -4.44135 | -46.00956 | 2024-11-30 05:01:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1daddefe-e4d7-362a-a81a-e02731b47539 | -1.31312 | -51.67084 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3f07c38-8c58-356f-8ce6-96fc71174434 | -3.20837 | -50.27252 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| facf8b7b-9b19-3e0a-9370-a409b84c91e5 | -2.27042 | -46.42649 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f51cccf0-efa4-399f-8bd0-d5bdd95cbd83 | -3.16002 | -53.24297 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b1dd2bc-7d79-3873-9b64-28a58429359e | -3.27863 | -50.59698 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 128fb18e-0719-3604-bf07-4a9ef0c14f22 | 1.18295 | -55.967 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 181b8d74-03d3-3136-90d3-0624df1299de | -1.76202 | -55.6462 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d9218d3-0d2c-3c92-8b2e-9b191983af16 | -1.78342 | -52.74151 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1662d439-8489-35f8-9957-5a8ed5e8ce7a | -2.78197 | -54.21306 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 737fc543-90d9-3504-8363-c0ca95384a05 | -1.36128 | -55.17992 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9af9b403-5c51-37df-ae0e-6c05c954cb1c | -1.57988 | -53.74787 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 087d1464-5853-35e7-b092-60b50eba7f81 | -3.93193 | -47.97819 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c3a9503-eb37-3574-8bef-d1e870c9fc8f | -4.18866 | -50.67743 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddb84495-b07a-3a76-867b-40afef2770ba | -3.09258 | -53.72068 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df03bb81-20ab-3463-b6cc-dd8bfab5164e | -1.89182 | -48.64973 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ef5bd5a-d795-3074-a76a-f0d03ea59dab | -1.25088 | -51.63346 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 445c73a2-034e-3369-84f5-67dd024b5db0 | -3.17241 | -53.63825 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a4ed7ca-18d8-3489-86ae-b87c4295a723 | -3.91822 | -53.66645 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d59a46dc-965c-3eff-88d3-866179566261 | -3.11157 | -53.17596 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 214d61ef-7a0f-3ee5-8022-f55f783a9fc2 | -2.59239 | -51.83193 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5a90f93-180a-31d3-84ed-ff1b37d21241 | -3.3563 | -49.56391 | 2024-11-30 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af7f40fa-3caa-362d-b1b6-07d71c547f14 | -2.41649 | -53.84828 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02e79dd-5c88-3185-850b-dae2d2a3507b | -2.61049 | -49.25413 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 838a393a-023a-3c15-a025-99a53ed1f0a0 | -3.06549 | -53.91606 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7934040e-1fa2-34cf-bcb2-91bfd0bcac20 | -2.63035 | -53.99615 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08bd76dc-3f09-34d2-8d67-42b0d99e26e9 | 1.20546 | -55.93759 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc077edd-f28d-3852-a23f-50b23cb63c0b | -1.28658 | -48.27227 | 2024-11-30 05:01:00 | NPP-375D | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3276585b-2f16-3305-9d53-de1553b8b51b | -3.34712 | -50.74773 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba52de79-034b-3819-83b3-e5a3e9a79dab | -1.09747 | -53.39624 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da51c1a4-cc78-36ec-9114-b0f4e2b3d7d0 | -2.96224 | -53.88585 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35423ec3-11ca-33e1-a168-2e9ccccd028e | -2.14396 | -46.48872 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23d12e30-8b73-3bb7-b693-9faa4cd43f0d | -4.11143 | -54.4124 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 142eaf90-ff61-343b-b9b1-2b7b625b242b | -1.1244 | -53.73817 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63d2bbb-693e-3cb5-abed-a1bfc4bd9e68 | -1.90967 | -54.77053 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84d7aa84-28b5-3be4-889d-009bdd7f8789 | -4.25527 | -47.57794 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a6eaded-0074-3704-8345-e1afd466c2c6 | -1.65071 | -52.4023 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f39d4c4a-1327-32eb-93dd-2220f3136921 | -2.83313 | -48.47108 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35fd7fd3-21fe-36db-bda3-56d5bdaa6f3f | -2.6298 | -53.99964 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7ea95fe-c7f7-3de8-ad58-776777b3c8b2 | -2.56287 | -54.3174 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 403a1619-d56e-3a81-a39a-75b5f589a4e6 | -3.59057 | -50.3801 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a33a817a-cbb0-3b8c-a6e4-37f17b14601a | -3.29245 | -51.15414 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08a6a666-8a45-382a-aec2-1d8fbe73d3c5 | -3.0761 | -53.91409 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e233e8c3-4594-35df-896c-98aec8574948 | -1.88748 | -48.64905 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6afb210e-832b-3489-b925-8a87010246be | -3.96211 | -46.73572 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88f72386-3e83-33b9-84dd-59fcf0a318c3 | -3.59588 | -49.99034 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b284ed3-c330-3294-ba2f-fcca41fff743 | -3.19857 | -51.41797 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a14e701c-c779-3a9f-834f-6137689b84a2 | -3.99987 | -49.9763 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6e83b99-3a37-313a-abe2-a2309ded037d | -2.10473 | -53.25056 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e352e7-f760-3054-86d9-c6f4de5661e1 | -1.88658 | -48.65078 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d0fc281-eeb1-3ea3-8382-e26d5d891b42 | -2.7597 | -54.12418 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80115cff-1970-31fe-8e9c-3bd0acc34717 | -1.26771 | -54.55038 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1097d39d-af45-3ed8-bcdb-7672b28a6722 | -1.61777 | -53.33036 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e2bc3d1-bbe6-3607-aa4c-c3df482a07f3 | -1.09185 | -53.36633 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96f3c83-4a70-3146-8549-8b722a9cc10d | -2.82986 | -54.03825 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e51b1f74-4434-314f-a4cf-83b786396392 | -1.59977 | -52.28553 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 348aef17-f59d-307f-9149-46f3fca7f2f1 | -2.3328 | -50.50764 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdd3e668-154d-3ada-ac4c-54e56f5080e7 | -1.21707 | -54.18578 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c25b43b-49e2-343c-9a0f-b1c22442a206 | -1.63203 | -53.86684 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e207ae59-44ad-3cbb-be07-c6362d292b0b | -3.81925 | -46.54398 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c28022df-a394-3f43-9edc-d16838233850 | -1.51671 | -52.03456 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e76aba2d-5828-3300-ad3b-53ff8da5be52 | -2.39333 | -56.51715 | 2024-11-30 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9204c324-1c5e-3a8b-ad7d-29a9e5d56ce4 | -2.62028 | -54.2125 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67ec9a32-7c6c-325a-a446-e055dff7609d | -3.29849 | -53.83273 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1dcbec18-ad02-33ae-805d-a215ebbdbbbb | 1.97552 | -60.9205 | 2024-11-30 05:01:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aefbb039-759f-32ed-ade7-66e1e3e50d1d | -3.43846 | -54.53915 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e07f497-4d69-32b7-9747-0bf5a3490151 | -0.05572 | -51.60003 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13ac21cc-1060-30c0-92df-aed0eca348eb | -1.4923 | -52.3281 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1712b2db-eacc-3c0e-893f-3ef4d9ad1902 | -1.47472 | -55.12665 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93600946-dc54-374b-850b-14b97720655a | -2.59577 | -46.57307 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b99ebc-89a6-3c3e-9178-bf36e8601251 | -2.58744 | -53.98597 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8ae11953-b0e9-3299-9428-2a9cf8950862 | -3.81451 | -52.24631 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43461a82-c5b6-37e2-b304-2382da44990d | -2.9514 | -49.44343 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e5cec98-35ee-39ea-b77f-4e592a9045ab | -2.84108 | -54.07584 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea8476b1-4ffe-3e9b-a887-72ef2529eb2f | -3.28731 | -50.61824 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7e69dc9-39aa-3a29-8965-14b275ca8ba5 | -2.22836 | -53.68908 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91ddc7f9-f28c-3a61-91aa-04442dfa0ed8 | -3.77843 | -53.4187 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02fe46a0-61f0-3085-abbb-9cc8e687c4ae | -2.61059 | -54.33901 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af179f98-d883-3d9b-bc16-a288b477ef66 | -3.02555 | -49.52428 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1d9d1fdb-78db-3937-8848-aa5a5fc446fd | -3.18297 | -50.27914 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 745d7658-54ed-3801-90e1-9374d034260c | -2.44851 | -53.97174 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dcb4c20-630d-3783-9d4b-75a4bbb20d41 | -2.14903 | -46.48943 | 2024-11-30 05:01:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1422dde8-a960-341f-b968-4a32a209b204 | -1.07086 | -53.21402 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8747f20a-6748-3dcc-a4e9-445c06c2f9b3 | -1.72048 | -52.47918 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe29bb7b-5139-3c3b-9393-9d10e59536f1 | 0.98013 | -50.24987 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0120d8f3-d48d-3049-a003-f7a3d7510411 | -3.20075 | -46.57756 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d3efcdf-1959-3821-b61f-726d61936457 | -3.99286 | -41.5139 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1fd50dbe-3050-3d13-b411-df830df50184 | -1.58521 | -51.25999 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1940634-a7a1-3d96-b18b-a3510921b92e | -1.18314 | -51.77291 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7ddb9bd-a4da-3f1c-a6a3-d14c9d6b7e0e | -1.36024 | -54.97062 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e6b5624-e9a8-3943-a554-4ce336cf4531 | -3.23067 | -50.31235 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 747198e3-07bf-3029-85f0-076aa8ba656a | -2.67775 | -50.50202 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 905a3b7d-fb14-399c-875f-d3429d2ac229 | -4.86868 | -41.31262 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 06c410ee-828c-3e4f-b043-384c311c277d | -2.32347 | -50.68292 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README95.md)
