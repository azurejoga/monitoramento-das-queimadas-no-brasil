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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53821211-aa37-3375-b992-75f19ca8f85c | -2.58053 | -48.40995 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 880ace6f-e30e-3ec3-92d5-6afce6597285 | -8.16948 | -46.42628 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0529ff2c-ac82-3cfb-b555-e0ed5bb7d8b7 | -7.75004 | -47.01845 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94822171-adc0-3d2e-ab9c-00b57a5adf9c | -5.83295 | -44.43417 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 23da1360-de7b-3ffc-be80-774f74d68725 | -9.75522 | -46.13346 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404f199c-da50-3b5e-85ff-8a749a271cc0 | -3.42536 | -43.1666 | 2025-09-28 04:04:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90e77549-7b3f-328d-9566-a233c25d3ef2 | -6.70307 | -44.5717 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aeea524a-9c69-327a-aa24-43b5ec3ffe84 | -6.78421 | -44.08736 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| a2f4258a-e6d6-3108-a6d7-4ff425c95a83 | -8.20158 | -44.4 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b803077c-7c72-327f-8479-cc0f639380a9 | -5.82251 | -44.44802 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adec6345-561e-355d-8349-7eddaf6fff03 | -7.00464 | -45.62466 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 875b83ab-b480-303c-a114-6162d7f1d0fe | -5.74821 | -42.88819 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5592ed64-2bea-39c3-9df2-edad0dbcd3c2 | -7.49016 | -37.1343 | 2025-09-28 04:04:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 185681d7-f912-3d2c-afb5-83e3562bf457 | -6.47945 | -44.51963 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cfadeae0-23d8-3c05-a1e3-5f7f97263eb7 | -9.04336 | -45.51571 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87ace639-9008-37ff-92b6-d83aedf09fa7 | -6.25576 | -42.46158 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a48af3d5-c5e1-399a-9819-e6c75fceb37c | -6.78878 | -44.0834 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| f3b14300-3870-3a45-904e-0d31991bbdf6 | -5.51427 | -42.73901 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 66215f3d-14ef-3b0b-af95-b8156dd47fc1 | -6.90324 | -44.76436 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f204852-8653-3fd3-8dc0-8db5afba5f5a | -4.91496 | -48.16444 | 2025-09-28 04:04:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25c5db6d-2255-3fab-80b4-8191afd46079 | -8.8232 | -46.01536 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c099c5da-9c72-3cb3-9b0a-56f97cb5628e | -5.81007 | -42.80473 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 51bd9efc-b840-38eb-a0cf-b1aeedce3cdd | -6.44256 | -45.90131 | 2025-09-28 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94eb4899-205b-3d9c-b4af-6f38881063f5 | -6.0737 | -42.44964 | 2025-09-28 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cffedfc8-ba24-3cd4-be7f-3f2ea45376f8 | -7.7525 | -46.97461 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4eab08d9-f383-31c4-b322-8e29eba86303 | -5.80872 | -42.81304 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6213cc3d-af49-3b99-8be0-d454e379a8c3 | -4.61336 | -40.21635 | 2025-09-28 04:04:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 76a686d0-9b5e-3203-8c8f-0c41f02ae12e | -5.81458 | -42.82233 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4efb132-a57f-33d7-86c9-89baa971b71a | -8.47882 | -47.79536 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46b449e4-5139-3e0d-a7b1-1216d1d6b9c7 | -7.53703 | -46.10265 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 617cfb70-d362-3007-9daf-3025a1fa834c | -7.53345 | -46.0979 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 70c01ca3-3236-39fb-b1bd-28dc834abed7 | -5.98533 | -44.12611 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b08d8205-a332-35f6-a549-543ce0c1a33d | -9.31509 | -45.6767 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04a0bdb1-a462-353c-adc2-58b924a61e98 | -6.45707 | -44.22319 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c81078d7-a764-3055-ab9a-6984b785bee9 | -4.77467 | -41.04847 | 2025-09-28 04:04:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 333b1b17-beb7-36e2-a85a-db8bbd422874 | -4.97251 | -43.20016 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ba5e78d-acad-320c-9ed3-b0e52731583b | -5.76218 | -42.82642 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6c1ff36c-9137-3bc2-b672-4d0333a1a237 | -5.16134 | -45.02152 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f564ffb-00d1-35b2-9fba-1a93c707640a | -2.65132 | -48.80027 | 2025-09-28 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f81ca5c-2282-3ac7-9387-ac63f46841d8 | -8.27405 | -45.46384 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81e9b837-06aa-390a-b03e-ec09d00ab956 | -6.24678 | -42.47255 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26575fc0-2e70-3214-bb57-78dc416e459f | -4.77866 | -41.04533 | 2025-09-28 04:04:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| de98d5c6-857e-3e61-9ab2-75e9c8c4b994 | -6.05519 | -44.86446 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75382d1c-5f37-362b-908b-78f72420e6ce | -7.3709 | -47.03796 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05c696f8-d3b7-311e-8392-afa0e7a51f0b | -8.29088 | -45.46293 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f20a4363-0636-3acf-925f-a14190914e08 | -5.35909 | -45.97456 | 2025-09-28 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2f9eee-6995-3b7a-81aa-24f6e7b4a4ad | -5.76298 | -42.83638 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 3c281cb3-c0d6-30c6-9170-a4fb841b9064 | -5.75909 | -42.81456 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 35098850-a8c9-3647-bafe-ffc42e7553c7 | -8.16875 | -46.43055 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3ba95c1c-8e01-31cb-8447-8a20ddfaed39 | -5.71415 | -42.66041 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03d08616-3e0b-3b36-81c7-93441ad6d881 | -5.98756 | -44.12841 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a28d0ff-24e6-3a4a-84a8-be0727fa8baf | -9.06507 | -45.53387 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f0933f4-3d64-37c1-8f99-1ee7fabdaadc | -3.91446 | -42.18576 | 2025-09-28 04:04:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c95a0504-5236-3476-a054-dabc0aa02192 | -5.90809 | -42.9338 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dc1e67b1-70be-3ee7-9be1-ceeaa4151ff0 | -6.44185 | -45.90544 | 2025-09-28 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e780270-c5de-301c-851e-c9ea8c1565ec | -4.1472 | -40.00372 | 2025-09-28 04:04:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 158a39e0-4b10-3dff-b7f6-8173d13dd249 | -6.42613 | -43.07599 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 67b39b01-72e8-3e78-8231-742d4adff494 | -5.5948 | -43.38588 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6052d75f-5212-3ece-a383-8bd98b9a6e2f | -5.4603 | -41.08228 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb8acab1-6231-39b6-a821-a550a9c51e9d | -8.8604 | -46.59892 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12327491-0ea0-3cd3-88a0-0d9cc230bcab | -5.81277 | -42.78825 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9863bb3d-9a3d-3b34-bc8e-4ed855935512 | -5.73629 | -42.65959 | 2025-09-28 04:04:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 877e229d-82d8-390d-8b59-17f0567d3176 | -7.37466 | -47.04341 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06e9f93f-2e3d-30fe-9f41-23a461ae87d4 | -7.75251 | -47.0046 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86f11715-49d0-3441-9aea-fd8c404905b0 | -5.80826 | -42.8384 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 568f66e8-61fa-3cca-9f88-36d2f8f2947a | -7.58377 | -43.90733 | 2025-09-28 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d865f9ee-f9b3-366e-94fb-2c59176fb828 | -8.65653 | -43.98774 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9034ce1-54a2-3f84-8f45-43ffdb7951f2 | -6.70763 | -44.59263 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b92cee4-7c0a-3756-83f5-2eff9b27704b | -9.04738 | -45.51637 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e50095-8438-39e2-be3c-7220b0d0a744 | -7.16857 | -45.50463 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0c027cd-aa6b-30d7-b87d-7f6b34061af9 | -5.29862 | -43.14578 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43f284e2-0e29-3ae1-8397-ed8cfc5e3d6c | -5.82817 | -44.43853 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81fa1f89-9c81-3018-94b4-9b34d212b1c2 | -6.06382 | -44.86239 | 2025-09-28 04:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1d2bd57-3e5e-3c5d-adb8-787dfadc9271 | -6.89909 | -44.11872 | 2025-09-28 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88717c63-9f4b-3ff5-8b59-573c29c13086 | -5.89759 | -42.81734 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 629d0d46-9771-39f0-8afa-db5e9c9a9afd | -5.76263 | -42.8014 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 35e3db7c-4ebe-32e2-a150-244b9b965aed | -7.24874 | -44.76159 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ae7f9c36-3313-3827-b708-8676f7a2ddd2 | -3.73957 | -39.34676 | 2025-09-28 04:04:00 | NPP-375D | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f43572c6-9e94-36ff-8383-d126c827d738 | -6.62554 | -45.90236 | 2025-09-28 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86c211df-86e7-3941-99e7-63887412216d | -5.73702 | -46.18209 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23df5589-4bb1-3308-9dd8-3ea1fece1a1d | -4.44622 | -40.98145 | 2025-09-28 04:04:00 | NPP-375D | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 85849792-5151-3117-be85-5aec81d4e0e8 | -9.06044 | -45.53675 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 187f36fa-9eef-34d8-81a7-ad6eadce7208 | -4.62697 | -43.11051 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f090374d-818c-3d3f-95d9-a7babf6c4934 | -6.42445 | -43.51214 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c0161225-0e2a-369c-b01a-8d834c62bb07 | -7.79112 | -46.99722 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6addd7d-69bf-3ca8-9f73-cf46e83c38a2 | -9.109 | -45.88413 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86d4b5f8-e3cd-3d6b-862f-8550d443651f | -5.41488 | -42.28485 | 2025-09-28 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0567df76-a950-37de-874a-c8dca259f9a4 | -6.24926 | -44.48975 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06deb82b-c6f8-3932-8310-cf5270101a48 | -6.25094 | -42.46882 | 2025-09-28 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07ece658-a429-33b4-bca1-6a084c3eb35c | -7.38162 | -47.03041 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| e5bf815a-a20b-32a9-ad9a-965a38998099 | -5.94659 | -42.90214 | 2025-09-28 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d402f433-3a68-3d8f-a04c-c782cafc8dfc | -6.54986 | -44.1482 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30ccba27-0c9d-3173-bb7f-def1c6aa6b3b | -6.62248 | -43.82921 | 2025-09-28 04:04:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c5f26c3-7cfc-36ba-9976-659be5d14fca | -7.00045 | -45.624 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0e36d61-73f5-3ec3-a444-ed584eac0c11 | -8.28703 | -45.43678 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 121c7e7a-41fd-3f25-9056-d1873c9ab203 | -5.90215 | -43.2937 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0734f808-2024-30df-bf9f-3d25d9c986f0 | -5.74139 | -42.83271 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eb00a2de-6822-3722-942a-a787481dcc1a | -3.2732 | -43.54203 | 2025-09-28 04:04:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e10d4d18-64cd-3596-9b4d-63f3990c6b37 | -8.27344 | -45.46739 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0f789c8-0436-36eb-ba3d-ad3c8d59a160 | -7.15075 | -45.50927 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
