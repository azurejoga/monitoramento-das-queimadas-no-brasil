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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 070d2920-1ee9-3d56-a344-61c69eb1fc9a | -16.0225 | -50.8771 | 2025-10-01 14:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 9d23ac9b-b0b7-34e3-a16d-e6591d4d98b6 | -11.383 | -45.0543 | 2025-10-01 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 250.1 |
| f517e8ab-ce1f-31b4-a047-6bf1c981bdae | -7.646 | -45.4489 | 2025-10-01 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bff9d3bf-40b8-323d-a4a4-abe114d732ff | -7.5561 | -46.7795 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 8fb08cb1-7e08-33f1-8c10-c5e147242123 | -8.9109 | -46.6723 | 2025-10-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d32710c2-6922-3b96-92f7-1dae0a507b36 | -5.4583 | -42.8441 | 2025-10-01 14:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 9faceb2a-3fba-3d9f-9bc4-d394132ecf10 | -8.5267 | -47.2879 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 373e3b8a-cbe1-3097-acb0-0ff57dcee75e | -12.8831 | -46.9101 | 2025-10-01 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 2cc17826-6211-3acc-9f66-fcee558330ef | -12.8963 | -45.1943 | 2025-10-01 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 6c75def2-4966-3a55-8773-589a068b6265 | -7.2996 | -42.8722 | 2025-10-01 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| b646d1e6-dc8f-34e4-bf3e-fe661daec0d6 | -9.9391 | -43.6012 | 2025-10-01 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 3bbf9b6d-f2d0-3d9a-bd7f-98c2d6fda8b0 | -7.1815 | -41.6931 | 2025-10-01 14:00:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 7b13bf19-affb-3144-86a9-917b8dba3a3b | -8.4833 | -47.7763 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 4c7db66c-600d-3be8-b0a5-0ea9b2386bda | -7.8549 | -45.2702 | 2025-10-01 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 69bff8bd-801f-3749-8f3e-248ee9ffadeb | -8.8923 | -46.6519 | 2025-10-01 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 169.3 |
| e08c2e48-e6ff-3cb9-b33b-c07b894f88be | -8.5018 | -47.7965 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 479.1 |
| 4db27491-9da3-3cfe-ad4d-c29fa2fc2d5e | -12.2623 | -44.1306 | 2025-10-01 14:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 348d3a90-c972-3cef-b2a2-edb4c9ad6c12 | -8.6908 | -47.7126 | 2025-10-01 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e8839a61-8e8c-3e4a-a071-2c95fd68f1b2 | -12.2724 | -47.8256 | 2025-10-01 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1e0fdbd2-4326-307a-8b9c-722588cebe9b | -6.0405 | -44.7447 | 2025-10-01 14:00:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 52f01e78-9f2f-31b2-9b20-4ef595bfd5a5 | -11.1178 | -49.7845 | 2025-10-01 14:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 9e7ad4fd-b6b1-3d83-b3dd-bed22780a33e | -5.9271 | -44.8671 | 2025-10-01 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 92b5bc7c-dd4d-3e30-816e-2880b0080c75 | -11.6126 | -45.0443 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| cdd07322-84fc-3e57-8ee6-0502b2e8ed6d | -8.5773 | -44.7623 | 2025-10-01 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 4fa68e29-b864-3124-a325-47851c75cadc | -9.1889 | -48.5166 | 2025-10-01 14:00:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d50ce89f-442a-38ad-8ef1-24e04d54bd86 | -6.7168 | -44.5758 | 2025-10-01 14:00:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a981ed83-8478-3600-8db6-8a1dd4edcd77 | -11.825 | -44.9437 | 2025-10-01 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 80bdbbd2-04ce-362f-b73c-f979facd1100 | -6.525 | -45.0025 | 2025-10-01 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| a77bfd75-5a96-398d-9aed-98481a627d93 | -12.122 | -43.4215 | 2025-10-01 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 24c6c21a-c23f-3b1e-93c4-e27e5a1f1390 | -8.672 | -47.7144 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4cb21a54-e2a2-3282-a389-59da2bce0940 | -15.9388 | -43.2979 | 2025-10-01 14:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 286.7 |
| 1e12184e-3595-3be8-b173-f870c73c60c8 | -15.7707 | -43.7197 | 2025-10-01 14:10:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 69fa3a6b-5d7e-36c2-9636-f159f9023ef9 | -6.0625 | -42.4422 | 2025-10-01 14:10:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 8afa9950-903f-3476-8748-516e064211bd | -11.46 | -45.0202 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 9ace1e13-a26d-301b-b7be-53bad9614eba | -7.646 | -45.4489 | 2025-10-01 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 70446849-fb01-388f-8896-fa3a2f413b52 | -13.7876 | -47.9853 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 45519ea2-c813-3136-9c59-50c5432f4a84 | -8.874 | -46.6092 | 2025-10-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 61c397b0-a50d-388e-a4e7-e49a4873a872 | -6.0978 | -42.6758 | 2025-10-01 14:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 117.6 |
| 754467ed-95dc-3dbd-bb2a-7c4b104e7b50 | -5.4967 | -42.7471 | 2025-10-01 14:10:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 6eaeba47-32be-3ec3-a490-19530d1d4754 | -7.7944 | -42.5132 | 2025-10-01 14:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 9b88eb37-d5ed-3e93-a462-affb76878aa5 | -5.9271 | -44.8671 | 2025-10-01 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 08597f05-314b-39cb-ae14-91eacf0ad03e | -7.5563 | -46.7573 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b34f9ee4-dc5a-3378-8213-ec0706b39c23 | -9.9963 | -43.5937 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 0d3adf18-c81a-3701-80d8-0461ebbde258 | -9.9391 | -43.6012 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 724525b6-5a8e-35d5-8e1a-ea67583bd3b4 | -13.7873 | -51.2189 | 2025-10-01 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0c26d0ab-c564-35a7-9ecf-74037f66b6bb | -6.2718 | -44.0612 | 2025-10-01 14:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9abc1693-d1a6-33f7-b1b5-81d82afdc9bd | -8.8797 | -47.6502 | 2025-10-01 14:10:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| de1716aa-fa9e-3f42-97e4-98f107250720 | -9.9186 | -43.6978 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 496.6 |
| a4b98f70-cfa9-3695-b3c7-c206b98b87bb | -8.6722 | -47.6924 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7643d3de-35c8-3c55-a33a-612822b0a751 | -6.0602 | -42.6789 | 2025-10-01 14:10:00 | GOES-19 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 5605aa0f-67cf-38fa-9ef2-9dcd8a63f9df | -14.9733 | -46.8896 | 2025-10-01 14:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 139.3 |
| cf34bf4f-ad9d-3b70-9cde-07d98788292a | -13.1747 | -47.7869 | 2025-10-01 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9cc2677e-a276-3664-8689-832cbc1cdb24 | -9.1248 | -47.6256 | 2025-10-01 14:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9f86ee69-b261-3940-a730-cf512cccb480 | -14.3714 | -45.9172 | 2025-10-01 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 16d39fc1-bacc-3f4d-9a17-800fc10f2acb | -11.9411 | -47.0675 | 2025-10-01 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 980136b3-6c4d-3f30-bba9-1642efbdcd86 | -8.5267 | -47.2879 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7ef39659-8a90-339c-98ba-f4c8cc49d3a8 | -9.4458 | -47.5923 | 2025-10-01 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| e92946f3-9a43-3004-8200-ad54d5cbfa85 | -7.4412 | -47.0109 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 3c43febf-ca4b-3ac8-a6a4-f5de0ddd46c0 | -13.327 | -47.876 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 81864a42-969b-3309-bf48-9b57c688d057 | -6.7165 | -44.5987 | 2025-10-01 14:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 11ae2aa3-7952-3f7b-b71d-d98049f65979 | -7.5749 | -46.7778 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 01ff09c9-55cf-33d1-b21d-14880e106636 | -13.8354 | -47.5076 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 95a8f3bf-a4f7-374f-9921-5bbf9e38751a | -14.8212 | -45.8143 | 2025-10-01 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 21d3ec7f-3753-322e-ac89-c0d739b3b227 | -11.3296 | -48.3235 | 2025-10-01 14:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 215.9 |
| 2ca19714-96a2-3ee1-8366-f81dfbb4389a | -8.4833 | -47.7763 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 59abc685-dda5-3402-ae41-e9e3a83aaf50 | -13.3611 | -48.1159 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 323.5 |
| 44afc2db-c72a-3e79-bced-0634b5517535 | -6.3 | -45.0205 | 2025-10-01 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 691c1685-1c2c-3879-8698-e7eee866255e | -10.6429 | -48.5364 | 2025-10-01 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 62cd30de-8f1c-304b-983f-83aab223a55c | -6.6981 | -42.7882 | 2025-10-01 14:10:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| b7e51fbc-a2c0-3118-843e-a79ec0f44007 | -5.1512 | -43.7289 | 2025-10-01 14:10:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 6cc58c02-34ac-37f2-9027-3ce833d751d7 | -9.4644 | -47.6124 | 2025-10-01 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 34525da0-c598-327f-ae17-8af384238fe4 | -8.5584 | -44.7644 | 2025-10-01 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 61c156f3-3b81-3826-af79-e6981f00edf8 | -9.9383 | -43.6483 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 424.9 |
| 6021226b-f3e2-35a5-a15a-8c2733c43448 | -11.7797 | -47.5806 | 2025-10-01 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 121.7 |
| adbc288b-ad83-3267-b67c-9aa63fd1d803 | -14.3514 | -45.9437 | 2025-10-01 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 00f8ee43-026a-3a79-8bc5-3c036619f106 | -11.9272 | -47.8941 | 2025-10-01 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 306e8ab6-4e72-39da-9393-e826e56d047d | -14.1732 | -46.1124 | 2025-10-01 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 44254fac-4d37-3cab-ad5d-fcb0293bbcb2 | -8.5079 | -47.2897 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ff33a22f-69ec-3e45-b119-5575ce4346e0 | -6.544 | -44.9783 | 2025-10-01 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b4577673-1b57-302c-824f-06c93b10f07e | -9.8049 | -48.9756 | 2025-10-01 14:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 663a09a7-490b-30db-9a7d-5d88b1641fd9 | -8.3869 | -47.9824 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 17e727e3-7112-3e6a-8551-193c7a434f27 | -8.4827 | -47.8202 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9707b948-7a30-327d-a8bb-d6a10b8d48b4 | -5.3276 | -42.7832 | 2025-10-01 14:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 11ea3d46-4859-34d7-afeb-e02b4541b3dd | -12.2816 | -44.1275 | 2025-10-01 14:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 223.9 |
| eec20d0d-0c72-3f50-82b6-49350e02fb16 | -14.9079 | -47.2193 | 2025-10-01 14:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 17a0e731-de80-326b-8462-83e3e05539cf | -13.8165 | -47.4881 | 2025-10-01 14:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| b1dbf8dc-47db-3b7b-a117-5a7d5895d17f | -8.2105 | -47.0084 | 2025-10-01 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 9eef14b2-e615-334c-963a-9655049ad5c2 | -11.4608 | -44.9739 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 026c1397-23ac-3dd1-ab8e-a92a53dda32e | -9.9387 | -43.6248 | 2025-10-01 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| d61a4cbe-698d-3be7-a399-f61581b65608 | -11.9081 | -47.8967 | 2025-10-01 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 718ed13d-71ed-34c3-887b-1a4642d0f77d | -8.483 | -47.7983 | 2025-10-01 14:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 38e22c81-6651-30a8-ab6e-2a51faa1bc1c | -11.6126 | -45.0443 | 2025-10-01 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2e499c1a-d7a6-3a96-9a36-7ec87761f9cd | -10.6155 | -49.1274 | 2025-10-01 14:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 2cfe0d6e-fa8e-35c6-8f39-184fbee10e6b | -16.0029 | -50.8801 | 2025-10-01 14:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ba4077cc-622b-3a45-a530-3cef0dd9dd1e | -5.9368 | -45.8825 | 2025-10-01 14:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| c4ba6984-d58d-3da9-9580-75bf3d848114 | -5.7937 | -43.0766 | 2025-10-01 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 4b659b44-5b3d-3f58-89ba-71ef932a4591 | -6.5437 | -45.001 | 2025-10-01 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 84609c7e-1eaa-334c-9e94-997f4cabbc46 | -9.4455 | -47.6144 | 2025-10-01 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 9421d6b2-b4a5-39cf-9633-069a429706e2 | -8.8929 | -46.6072 | 2025-10-01 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| c85e9574-45c0-396b-a19b-2c1c83f4a0d4 | -10.6432 | -48.5145 | 2025-10-01 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |


[Clique aqui para ver as próximas entradas](README160.md)
