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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46fbefc9-ffee-34bb-aa9b-a2ec4efabff7 | -7.6491 | -63.1197 | 2025-09-04 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 188.0 |
| b9bec8cc-02a5-3fe9-98c2-bf37cdcf2bbd | -8.6604 | -68.7473 | 2025-09-04 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| be26b557-bef2-32c4-9087-edd86076bda7 | -13.7495 | -46.9573 | 2025-09-04 00:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 47de3fd6-df73-33b5-a049-60fae43e4197 | -2.962 | -49.3437 | 2025-09-04 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 8db76ad9-2439-3ec9-8807-30c2c6bb8e66 | -18.1305 | -51.7971 | 2025-09-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| a1449586-219b-30ad-b422-0352dfc90ced | -7.6306 | -63.1203 | 2025-09-04 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 122.8 |
| f8d7eb28-f0ea-3677-9a2b-5f2e0b29419e | -12.9668 | -54.791 | 2025-09-04 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 34a653fc-625c-38e9-937e-4eb1aae2fbc7 | -7.6492 | -63.1008 | 2025-09-04 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 1ced3544-a61b-3bdc-bdb1-3fd05aa4b3a6 | -18.151 | -51.7719 | 2025-09-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 4afe62bf-d59a-3688-a17f-6f5de422de4f | -8.0796 | -45.3617 | 2025-09-04 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0e008c67-24ea-3a2d-bff6-fed67a805873 | -17.7129 | -40.2695 | 2025-09-04 00:20:00 | GOES-19 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| e1e64e21-3c38-3eda-96f0-88b3960f9e7c | -11.6409 | -54.5315 | 2025-09-04 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3397961c-c161-3b48-951e-380e2c584255 | -11.0568 | -45.146 | 2025-09-04 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| e4ae52bd-104f-33f5-bd0d-cd93ddb3acfc | -5.908 | -57.7311 | 2025-09-04 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 21db3930-3cb6-359b-846a-696b8013cd94 | -4.9951 | -56.256 | 2025-09-04 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 03978bb3-4a3b-3236-b000-9a993580e69a | -6.797 | -44.0859 | 2025-09-04 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ce1eb75b-94b1-3076-9326-9b6d2704825d | -20.1024 | -44.118 | 2025-09-04 00:20:00 | GOES-19 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.6 |
| be66aa08-19df-3c77-95f8-3edc2ef88500 | -12.9859 | -54.7891 | 2025-09-04 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 08cf36f9-b07d-3344-8a1f-22e194b471f3 | -8.6603 | -68.7657 | 2025-09-04 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| cc2a973e-69cb-34dd-b4b9-e70717d29287 | -9.4833 | -47.6104 | 2025-09-04 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e66bf2b0-1871-320b-b2d9-451a82360fc0 | -20.1017 | -44.1427 | 2025-09-04 00:20:00 | GOES-19 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| a187cbd4-cb97-310e-95de-2e7e291f0ce6 | -6.7465 | -63.1297 | 2025-09-04 00:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d0359586-91df-386c-a283-53f2482221a4 | -11.6599 | -54.5297 | 2025-09-04 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 441f764c-6da5-3026-a74c-fcd9e0d14fe2 | -13.1079 | -57.1109 | 2025-09-04 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 8ce0545f-e079-376d-a540-42e3c6c54d87 | -10.4472 | -50.3713 | 2025-09-04 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 18a42f59-64b5-3f2d-a0e4-4c4d6a96f641 | -18.1505 | -51.7937 | 2025-09-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 8751599f-7b54-32fb-9752-f05146260a2b | -6.7649 | -63.1292 | 2025-09-04 00:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 0c6dc5b5-1764-3eb9-8131-8a029653c7f4 | -7.7066 | -50.3188 | 2025-09-04 00:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| cd5131cb-61aa-3973-b39e-d8f581788207 | -2.9434 | -49.3655 | 2025-09-04 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5bbe263b-8a5e-38c5-b16c-5863bff099b1 | -12.9861 | -54.7685 | 2025-09-04 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 3b0a75b8-f208-3b69-b8a1-9fab196390c5 | -6.797 | -44.0859 | 2025-09-04 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8d17dca4-11bc-3984-891a-2111fce54375 | -7.7066 | -50.3188 | 2025-09-04 00:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b53af372-6347-331a-851b-f8f4a63a9488 | -6.7782 | -44.0876 | 2025-09-04 00:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 78362b3e-ca47-3a5a-b24f-322d17fde494 | -4.9951 | -56.256 | 2025-09-04 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 72c10c26-3312-390d-9f4f-37be66cc9faf | -12.9859 | -54.7891 | 2025-09-04 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b2619e8b-f114-3212-8e8e-ef4bc259749f | -11.2005 | -55.0195 | 2025-09-04 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4d3be650-147f-340c-b989-5a77cd6e0649 | -5.6266 | -45.0252 | 2025-09-04 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 50a1f6df-64de-38fc-bec7-85266b2dbf47 | -20.1024 | -44.118 | 2025-09-04 00:30:00 | GOES-19 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 4f914987-db57-36b5-a037-860a31686a01 | -2.962 | -49.3437 | 2025-09-04 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f661244a-67be-328e-98db-8f18d19bd80d | -6.2672 | -42.6377 | 2025-09-04 00:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 4f61f4ea-d149-381b-a8fb-cb8556e6ceaf | -7.6307 | -63.1015 | 2025-09-04 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 738c1d82-5c0c-39f9-837b-1992373c850c | -8.6604 | -68.7473 | 2025-09-04 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| e04cd5b6-6904-3eb5-8abf-27e48e0f2899 | -12.967 | -54.7705 | 2025-09-04 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a2d467e2-0052-342e-9cc4-1f6d45f9849f | -6.7465 | -63.1297 | 2025-09-04 00:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 18f3d8f5-5645-36a2-a5a9-c480d84c20cd | -12.9009 | -56.9287 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 236.9 |
| 34db68e2-d7af-30d3-afc3-c1a8440cdf3e | -10.5316 | -57.7747 | 2025-09-04 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8ca7a43f-61e8-34ab-89b4-1cb3182b4cbd | -18.151 | -51.7719 | 2025-09-04 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 5d5a0b65-7e86-3ac0-b1de-28feb86ae822 | -8.0799 | -45.339 | 2025-09-04 00:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f987b8ff-2a35-36bb-95b3-85f8ee8a4308 | -5.5892 | -45.0278 | 2025-09-04 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 9cbf9c47-832e-3adf-b776-1f63616dd717 | -13.75 | -46.9346 | 2025-09-04 00:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 0b491b38-a0c9-36ef-ae49-8d79483e24ba | -7.6492 | -63.1008 | 2025-09-04 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 5f4d68b1-29b2-3888-ab80-2c1e0826d012 | -18.1305 | -51.7971 | 2025-09-04 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 37a89fcd-7357-3e37-9160-0de356ca2af6 | -10.4472 | -50.3713 | 2025-09-04 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 2ce8962f-f0aa-32ef-b361-e551095ea81b | -12.9861 | -54.7685 | 2025-09-04 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 98ad8471-d5eb-3fc0-ad21-f7ec8cbd5933 | -11.6601 | -54.5093 | 2025-09-04 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b00727eb-602f-3556-a419-2546f282df66 | -3.4232 | -59.579 | 2025-09-04 00:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 5cfa59fa-7375-3902-9148-3159a067cf17 | -8.6603 | -68.7657 | 2025-09-04 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 0ea2e014-509e-3d5b-9907-f1867ce1bde5 | -7.6306 | -63.1203 | 2025-09-04 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 74950047-eee3-3498-a895-6e833f1ebae1 | -11.0565 | -45.1691 | 2025-09-04 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| f04df134-0918-3cfa-8784-1ffc22ce9269 | -20.1017 | -44.1427 | 2025-09-04 00:30:00 | GOES-19 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 49726323-e72d-3afd-906c-ecbdfa10f632 | -11.6599 | -54.5297 | 2025-09-04 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 0d70e1d7-d82d-3ec0-85bf-9848261d8b33 | -6.7832 | -63.1474 | 2025-09-04 00:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 34541f5f-452d-3d98-a610-28844e5270ce | -11.6409 | -54.5315 | 2025-09-04 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f4de39f5-7396-3907-9e26-616d4fc8516e | -5.6081 | -45.0038 | 2025-09-04 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f6c7c85c-590c-35f1-a24b-1839c54db4e0 | -8.3641 | -48.3334 | 2025-09-04 00:30:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a3370282-fbf5-3c1b-902c-0157ed802ae2 | -5.8525 | -57.7722 | 2025-09-04 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c711f81a-a3e9-3e2b-b31d-e24e55654bca | -12.9197 | -56.9471 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 35ad14f4-121f-3889-9069-0f73d9e7a526 | -12.9006 | -56.9488 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 358.8 |
| a4dc9f34-e998-3874-8414-3860683e6f92 | -5.6079 | -45.0265 | 2025-09-04 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 27464dd0-a8d0-32ab-9215-b6e2ed5007dc | -10.4469 | -50.3926 | 2025-09-04 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 55ac2673-b80e-380e-a01f-d38a7e48c5b7 | -5.908 | -57.7311 | 2025-09-04 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7915c6ff-4a98-3b76-9ac4-034528bccb37 | -6.2484 | -42.6394 | 2025-09-04 00:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| dfcb495e-2ac2-334a-8c1a-31efc049fd5f | -12.9199 | -56.927 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 70e9af35-6609-370b-8c5b-4c7294f1cb11 | -5.6153 | -57.3715 | 2025-09-04 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c2290f92-a1b3-3e37-b071-a085a3a0fa22 | -7.6491 | -63.1197 | 2025-09-04 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 4edf4307-d82c-3a48-8df0-272c13d385c9 | -2.9619 | -49.365 | 2025-09-04 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 6d5b9ac6-aabf-3d27-aedf-2a56c235c049 | -2.9434 | -49.3655 | 2025-09-04 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d46c133c-0a40-38e7-b052-4771de62727e | -11.5779 | -52.115 | 2025-09-04 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| cdd5b5b4-889e-3768-a8ba-7256366a4150 | -13.7495 | -46.9573 | 2025-09-04 00:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 48f8eabc-4cf1-38cb-bb98-39911ec3ef1a | -12.9668 | -54.791 | 2025-09-04 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9bcbe0a1-327e-3b96-ab71-aa037d28ab0a | -12.8818 | -56.9304 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 0cc9268f-d65d-35b8-8324-933b17e5ef0d | -6.7649 | -63.1292 | 2025-09-04 00:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 2bd34867-931f-371d-af96-fb3ffd4efc63 | -12.8816 | -56.9505 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 8788b88b-165f-31d2-80f2-b31bea369e31 | -13.1079 | -57.1109 | 2025-09-04 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a32e0739-ceaf-39a5-a51f-61c405796dcc | -11.0568 | -45.146 | 2025-09-04 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 22b30147-9c2d-33d2-a67c-7fc500dd4b6f | -6.7833 | -63.1286 | 2025-09-04 00:30:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| b991886a-0610-308f-b0af-158907b758df | -9.4833 | -47.6104 | 2025-09-04 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 7dd8dc2c-32ab-38f8-9077-1a031bab7599 | -18.1505 | -51.7937 | 2025-09-04 00:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 136.8 |
| a5c88a81-071a-31d6-8b0c-a65d031cce1c | -6.7648 | -63.1479 | 2025-09-04 00:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| a842608b-628d-39e9-96e1-c8676d57b473 | -6.7832 | -63.1474 | 2025-09-04 00:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| da9956df-09a2-3b20-a116-e3a935998d52 | -12.8818 | -56.9304 | 2025-09-04 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3c9394ac-8142-387c-ad76-3d093c44515f | -6.7833 | -63.1286 | 2025-09-04 00:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| c052aa57-b29c-3323-bb66-fba66e5be1db | -6.7649 | -63.1292 | 2025-09-04 00:40:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 0da59817-c16e-33f9-b66a-b173e2be4fe0 | -10.4472 | -50.3713 | 2025-09-04 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 150.2 |
| cddfdf52-35c7-36e7-9b4a-a7373363abf7 | -11.5779 | -52.115 | 2025-09-04 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| bfb56b45-2041-3084-ba7b-9598fe6a471b | -12.9859 | -54.7891 | 2025-09-04 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 58fc67a7-f9ac-36e6-a080-fde9bbe9b2b8 | -11.2005 | -55.0195 | 2025-09-04 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 3be8bbe0-6ada-3fb7-8fd3-0fcb25c996be | -6.797 | -44.0859 | 2025-09-04 00:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a16f913e-8355-37d8-b994-b99717e9e8af | -13.5727 | -48.1291 | 2025-09-04 00:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| a655b003-6250-3431-81f4-c85981a335e2 | -4.9951 | -56.256 | 2025-09-04 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |


[Clique aqui para ver as próximas entradas](README6.md)
