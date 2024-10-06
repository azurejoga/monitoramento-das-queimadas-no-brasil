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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ae477cf-ba30-358c-9814-d37e5fd0ef46 | -8.63479 | -50.04725 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3f33b602-bfa8-3de5-a4bc-e326a68e005f | -8.6333 | -50.03583 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1fb55a64-2f4a-3463-8473-a0d5dcf502dc | -8.6158 | -46.50419 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dff9f5df-0d38-3c0e-b754-905dd774bd69 | -8.61455 | -46.49528 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9bee199a-9344-3fff-acea-a7a5a1fe4f1e | -8.56935 | -46.50774 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0bb37356-2230-3c15-a620-86d7576e8ce4 | -8.48686 | -47.30276 | 2024-10-06 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ef997035-441b-3429-ba29-9eb999ad3d3c | -8.4496 | -46.4404 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| f3097be1-7c81-3eb9-ba41-041d1609b70d | -8.44834 | -46.43148 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a5f23d49-f0c9-3fde-8ac5-ff7aabbd0712 | -8.40153 | -46.29201 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 999ea38d-53d9-3aba-8785-62b4d68f1d78 | -8.39265 | -46.29331 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1ed51d37-8cd6-3eaa-a249-89c27090608d | -8.13781 | -50.00123 | 2024-10-06 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f5ebb63d-4c01-343b-8c5a-50d4ff28e37e | -8.11787 | -49.53552 | 2024-10-06 00:52:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d7d7e37b-ddcf-3346-8511-77607a9b5281 | -8.11647 | -49.52499 | 2024-10-06 00:52:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| cca5f839-9aa2-3bd2-8d02-4d7141094d34 | -7.76244 | -46.14246 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51038cbc-5afe-33e5-8379-f35d205111dd | -7.72773 | -49.8357 | 2024-10-06 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d44eda5b-b045-3564-b8ec-1f38e0799808 | -7.71804 | -49.83706 | 2024-10-06 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 15c2afee-67c0-3844-9669-00edc8ac73c1 | -7.38402 | -46.1385 | 2024-10-06 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| bf9c93c3-4f41-38fc-9ff5-e4053f1aa652 | -7.07078 | -46.59498 | 2024-10-06 00:52:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d5940fb1-6f2b-3a94-9292-54e2d174fc89 | -6.9205 | -47.69333 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e2691365-025e-3129-a834-9fda3a588dd9 | -6.90947 | -47.69178 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ec7ba3b8-7178-3efc-8be1-afbdc58eacbc | -6.90823 | -47.68288 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a8876894-40d5-3bc8-913b-d5a2b9ad82b2 | -6.90185 | -47.70193 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cd24b0d-97d6-3f39-b434-191849272cd0 | -6.90061 | -47.69302 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fa12bcd6-944e-31f7-8dff-7dd5a119f03d | -6.89937 | -47.68411 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 82a641b1-8755-3dd4-bbc7-fc912dfaeb0b | -6.89051 | -47.68535 | 2024-10-06 00:52:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0005fafe-3ea4-31f0-910a-6efb9e1dc081 | -6.69354 | -44.97784 | 2024-10-06 00:52:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2f5df04d-0f15-39a4-8168-74ac4c6c3947 | -6.51443 | -47.82652 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f977b9b2-eca7-305b-b844-47f844fcc9fe | -6.41527 | -47.71114 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b5ed3bab-fa36-32a0-b618-ac025fddeefc | -6.41404 | -47.70228 | 2024-10-06 00:52:00 | TERRA_M-M | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0663780-d8db-31bf-8019-0281fffe00ed | -6.40803 | -45.82316 | 2024-10-06 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 16fd35b0-76cc-3834-9068-3b6467a86f76 | -6.35658 | -47.54804 | 2024-10-06 00:52:00 | TERRA_M-M | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7b80fbf-4511-393e-998e-ee768caa9091 | -6.34664 | -45.71274 | 2024-10-06 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| bb5ab8ef-b8d1-3eba-9e68-a5019a692186 | -6.34532 | -45.70337 | 2024-10-06 00:52:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 30185630-afba-3efc-a7e1-59d3370e1be7 | -3.48545 | -48.91368 | 2024-10-06 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bc47457d-f9d8-3385-ad07-7d3394d1e0ef | -3.46911 | -47.66823 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 38ac6a56-dbbf-311b-9a5a-acc338ac5fbf | -3.46788 | -47.65941 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fdd33a81-bdf9-347c-9085-87e2ebf995dc | -3.46027 | -47.66948 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 84ebd832-500c-302a-8eb6-077c862a549c | -3.44363 | -50.66152 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92308496-481b-3da1-8b01-230ab15548bd | -3.42535 | -50.14453 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 82a45006-c0fa-3e34-bc3d-19b9ddb7dc44 | -3.42398 | -50.13449 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c30196cb-5639-3eaa-9459-92d2119c5e83 | -3.42067 | -50.39269 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 08531ab3-988b-338e-956a-051a3bc77f77 | -3.41928 | -50.38241 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 5d30025c-de19-36ff-8939-34b28cea5fda | -3.40582 | -50.39029 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7c226ea2-bee6-33f2-b522-3419fc1a492f | -3.40439 | -50.38001 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3a49bbe0-c8c1-3f34-9931-d1cf5fab0304 | -3.38625 | -49.25808 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c08a33a4-d232-3630-8d0d-a22d49838e48 | -3.38498 | -49.24889 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 995ff8ee-db3c-3c61-89af-1bd17ac1afc5 | -3.37436 | -45.54293 | 2024-10-06 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a67c83c8-8774-37ff-b1ae-a6d619bbfabd | -3.37291 | -45.5326 | 2024-10-06 00:54:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e6379c67-1b08-36ff-bdd8-755de6bb7421 | -3.34662 | -49.84537 | 2024-10-06 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b8bddb18-d3d2-3728-8432-b3244d72af2f | -3.3279 | -53.38893 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| a6dbccdf-76f9-30a8-b326-0b2a531da196 | -3.32394 | -49.14253 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 15aa93de-c299-3e5e-bb94-4cbe96335ad2 | -3.32362 | -50.0735 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ea5f2c0e-4eff-36d4-8d89-3264813b4e5a | -3.32345 | -50.46033 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 16d7fa38-a30c-3c01-bed0-ba358a1a8ac1 | -3.31536 | -50.472 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a0ff2d73-8ef8-3d94-879e-b678c7b688ec | -3.31496 | -49.14379 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1aaf6be5-bbf5-3451-a9da-7dc5c4d8951d | -3.31393 | -50.46166 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 0c276675-fd1a-3702-999c-d4d4c9a5608e | -3.31249 | -50.45131 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 4dbd4867-07c7-3241-a01b-d6577e0b8ae6 | -3.30584 | -50.47334 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c401699e-d568-3317-a69e-a94b6b6b2c07 | -3.30441 | -50.46302 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4cc00adf-efa1-31a5-a069-19834e3f5056 | -3.29967 | -51.4699 | 2024-10-06 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 915ce670-b246-3985-9787-5076b5e822d4 | -3.29808 | -51.45804 | 2024-10-06 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d6389209-7086-36fe-86e9-2453a367651b | -3.27778 | -49.13972 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5b9c8b91-dc3d-362b-917f-1b54209b5058 | -3.27006 | -49.15011 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6134358d-4de4-30ba-9ab7-56b49bc60781 | -3.2688 | -49.14098 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 5897da8d-0ffd-3abb-be8e-e20aeeac26b1 | -3.26755 | -49.13187 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c3e4ba34-80c1-38ae-9b99-beebac42de55 | -3.2663 | -49.12279 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5e165bb1-133d-3bd0-bb04-abaa11cb9863 | -3.26504 | -49.11369 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e0e43e90-fa67-33b0-887b-52a0c3a14933 | -3.24288 | -50.36702 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b26361e4-f145-302a-8f64-7bd7ff184077 | -3.23535 | -50.84451 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 16e648f3-c472-37a6-8d9e-6871c260b810 | -3.23387 | -50.83365 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| ac2a1f2e-c763-3d42-b2a7-ead6f1ba7452 | -3.22561 | -50.84581 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1f97c7cc-6c29-324a-a7c6-5b768ef0b308 | -3.22414 | -50.83496 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 20af1564-1927-3318-a527-f34ef7bf1371 | -3.21687 | -48.9696 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81e5c2bb-2019-3299-a9ca-d31aa30ee312 | -3.2035 | -53.14939 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d393fee1-0d1d-37f7-9dde-69ad093b6c2c | -3.13525 | -48.9719 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e76d59e7-7d06-3c0c-bd58-fc06ff16f222 | -3.13401 | -48.96289 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 71fdc21c-a510-3e29-b38a-7998ed8c5f3d | -3.13277 | -48.95388 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f123768-98c3-3452-a3af-a8260b749273 | -3.12565 | -49.17331 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6c3f04ef-9558-36e3-8e1e-084041de425d | -3.12478 | -48.97047 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1822c999-2bc6-3db0-a41d-86d8f9c60838 | -3.12353 | -48.96147 | 2024-10-06 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 5a1d598a-082d-3ea9-81f0-1148700cf703 | -3.12145 | -48.60969 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d5be21a4-7fc7-3c40-82ce-2a0b87f19db4 | -3.11402 | -50.41792 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 00ac7ab1-6a73-3560-93be-7cdb2b296b8f | -3.1021 | -50.4718 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2e148b84-0e5a-34e2-aab6-a722c6ea0bc8 | -3.10069 | -50.46153 | 2024-10-06 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 67d7b46f-7a93-333c-ad7b-b2537feff1b2 | -3.09329 | -51.22649 | 2024-10-06 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 117b03e4-0daa-332f-85bd-ae1cf6760d52 | -3.04009 | -53.04167 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d319b7c3-2e1b-3745-82af-4ad999696705 | -3.04003 | -53.05174 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 30b2728b-5260-32d3-9617-2878323363c1 | -3.038 | -53.03633 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| bc888cb8-733a-3016-a4e9-c78f827b1436 | -3.02868 | -53.04331 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| dbbdfbf0-6d1e-3cf8-aac1-976365253f86 | -2.9498 | -53.70901 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3614329e-538b-3ffa-ba5b-c0742a0ea468 | -2.94268 | -53.7043 | 2024-10-06 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c7e2d230-19cd-3f44-861e-f31a517c9d73 | -2.87722 | -48.90768 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80a32545-f36a-3874-884d-730dd1383d40 | -2.83854 | -48.43396 | 2024-10-06 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3a91297e-bd0b-3357-a316-2f75111ca9a0 | -2.81761 | -48.60785 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e378fb81-412a-3450-8179-c077053da231 | -2.81638 | -48.59901 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 141d5e07-b3a3-3451-88a8-5dd038a7fb3b | -2.81003 | -48.69599 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 2559c3cb-1eba-3a1c-8d4c-feeaa4c2eb24 | -2.80879 | -48.68713 | 2024-10-06 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 9c76ef91-4f03-3679-bd73-490e780f3c53 | -2.76931 | -45.96251 | 2024-10-06 00:54:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 996e6f32-8a03-389f-b496-c78297823452 | -2.74351 | -46.76378 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dae65649-d330-3180-a39c-53fa4aacc984 | -2.73971 | -46.80202 | 2024-10-06 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README20.md)
