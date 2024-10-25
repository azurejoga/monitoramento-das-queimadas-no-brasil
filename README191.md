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

## Dados Diários - Página 191

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f207ed-8854-314e-8a64-86ec6f47e1cd | -7.0833 | -47.2171 | 2024-10-25 18:15:45 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 322bfba6-4aaf-34ab-a183-c3af151457ab | -7.2267 | -44.3007 | 2024-10-25 18:15:46 | GOES-16 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 0c7054b4-501b-3257-8030-1f62a49d18db | -7.5289 | -45.8434 | 2024-10-25 18:15:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| b4d53c24-aae0-3497-9d1c-e0bb0cb9426a | -7.5477 | -45.8417 | 2024-10-25 18:15:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| cab5cf38-a14b-38f8-93a6-8772531c1910 | -7.796 | -40.923 | 2024-10-25 18:15:49 | GOES-16 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 85.7 |
| 1fdb6fbd-61a8-3bd4-b5d1-b46b304393d5 | -7.9288 | -40.9076 | 2024-10-25 18:15:50 | GOES-16 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 4b7b26e5-6e20-39f8-8d04-0c30048f6a87 | -8.7396 | -45.3388 | 2024-10-25 18:15:54 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c015d350-332f-392c-a71e-623774c1d1dc | -9.0835 | -45.0499 | 2024-10-25 18:15:56 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8a7699b7-5c8c-30be-aeeb-f1f09cfd1744 | -9.3727 | -43.3687 | 2024-10-25 18:15:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 110.1 |
| a348e7e7-9349-3930-8e03-99a018ddde13 | -9.4699 | -43.215 | 2024-10-25 18:15:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 61.5 |
| 360d8fac-6cae-3927-96cb-1e1408404e56 | -9.5193 | -49.1991 | 2024-10-25 18:15:59 | GOES-16 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 2d057d53-eca5-35bd-893d-8281e5dacaf1 | -9.6153 | -47.6183 | 2024-10-25 18:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| e579cee8-7e4b-3feb-88c9-ce387f821af3 | -9.6156 | -47.5962 | 2024-10-25 18:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| 541eb007-4e6d-37de-bde5-12ec613b51d5 | -10.3016 | -42.3886 | 2024-10-25 18:16:03 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 53fe1136-9fa9-3d27-9324-458944d74a8f | -10.3012 | -42.4127 | 2024-10-25 18:16:03 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 17239829-9edc-3c2f-8706-ae853e2058cd | -10.5105 | -43.5941 | 2024-10-25 18:16:04 | GOES-16 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 13211f67-2d96-3562-8054-0811a09ae497 | -10.6292 | -43.3416 | 2024-10-25 18:16:05 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 90206715-cc9b-3a5d-8e29-9e54680eeb0b | -10.9 | -47.8249 | 2024-10-25 18:16:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| f0c07339-fee5-3c58-b97f-4def0150bab1 | -12.3118 | -43.5565 | 2024-10-25 18:16:14 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0a7489e2-47dc-33c0-9b04-aecc2f0368da | -13.4726 | -42.5619 | 2024-10-25 18:16:20 | GOES-16 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 80.5 |
| bbe73964-e8ef-3777-a32c-63a679a4fcf7 | -14.4169 | -42.1331 | 2024-10-25 18:16:25 | GOES-16 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| cfd18234-40ab-350d-99d7-c5336a9791e0 | -19.5461 | -56.7192 | 2024-10-25 18:16:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 9d9f15cf-cfc6-3f64-bddb-57f70bcc0fc2 | -19.587 | -56.6716 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 136.4 |
| ad0d1014-d6f7-3a7f-aa3e-32b7bf1c0d44 | -19.645 | -56.7891 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.4 |
| 83249ae7-0b9c-3dcf-a1dd-23eafea1c8cc | -19.6245 | -56.8129 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 112.0 |
| 98dbd961-b3e4-3152-ab17-477449813a6a | -19.6446 | -56.8101 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.1 |
| a6c1cc1b-343f-3e34-953c-ccbb774db636 | -19.6651 | -56.7863 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.0 |
| d133b236-7793-3406-bdf6-eecf751eb522 | -19.5862 | -56.7136 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 122.5 |
| a09ea71d-52b0-3c92-b787-4ba9037a3fd7 | -19.5874 | -56.6506 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.2 |
| b12bec89-0673-33f8-9f86-7259fde60d9a | -19.6655 | -56.7653 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 116.0 |
| 6ca661cf-54b4-37c7-a336-a0e01eca2254 | -19.6639 | -56.8492 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 5d69186a-1c73-3283-9c30-0e802ca3d0ef | -19.686 | -56.7414 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| bb8fe7d8-0172-361f-af40-909b3ad99ee9 | -19.6063 | -56.7108 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 131.0 |
| 904552b1-a1f3-353a-9896-9c45d2de2c52 | -19.6075 | -56.6478 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.5 |
| 4536cf5b-59ec-39f4-a30a-5777c8d1f621 | -19.5666 | -56.6954 | 2024-10-25 18:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 1a389e9d-6783-39f2-9844-4763a676c54f | -1.0368 | -53.5171 | 2024-10-25 18:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 209.9 |
| 9e12a6f2-5061-3de5-8151-aea944814726 | -1.3637 | -55.8472 | 2024-10-25 18:25:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a659ae03-13e5-32e6-8c5e-08fc85c89875 | -1.4003 | -55.8862 | 2024-10-25 18:25:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4073926b-9d41-32b5-9551-6c51d6c9ad69 | -1.4004 | -55.8468 | 2024-10-25 18:25:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 32e8aa56-cc02-351d-9c4a-3bbc850b254e | -1.5651 | -55.9041 | 2024-10-25 18:25:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| fc423b7c-3a39-3bcb-8d85-09d500962f9f | -1.4918 | -55.9443 | 2024-10-25 18:25:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f2dc051e-e146-39c3-a4b7-8e954fda0dde | -2.0232 | -55.7798 | 2024-10-25 18:25:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ef7c3093-62ea-3839-9d49-7b152954fdde | -2.1829 | -50.502 | 2024-10-25 18:25:18 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d094949f-298c-3ddd-ac1d-d8d6e781e5b7 | -2.3056 | -46.637 | 2024-10-25 18:25:18 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ac4407be-610d-3955-a2ab-ee06ef1b4104 | -2.3057 | -46.615 | 2024-10-25 18:25:18 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 64365618-1337-30d7-86b1-4deebf7819df | -2.4438 | -49.6336 | 2024-10-25 18:25:19 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 184c9a06-478f-3299-b20d-fc049e1e3736 | -2.4932 | -46.0116 | 2024-10-25 18:25:19 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 30270160-7fee-35c9-8c03-3f89ecf50211 | -2.5117 | -46.0333 | 2024-10-25 18:25:19 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 88ed86fe-525a-3ed2-a8ed-89cd5421e7f1 | -2.6473 | -49.5225 | 2024-10-25 18:25:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 51a20b99-8136-386d-a1df-273eedf21432 | -2.7387 | -49.7739 | 2024-10-25 18:25:21 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 59fb09c9-1b99-33e4-8456-677840671728 | -3.1102 | -54.146 | 2024-10-25 18:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 4476f686-5497-39fc-b3f6-63c6aae18755 | -3.1116 | -53.7234 | 2024-10-25 18:25:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 4a8e00a0-731d-3c5b-a7ec-06425be190fa | -3.3041 | -43.5078 | 2024-10-25 18:25:24 | GOES-16 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| e470d0b2-abc8-37b7-b8ee-7cc132fc21bb | -3.4766 | -54.4572 | 2024-10-25 18:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a5f06369-e522-3625-ac6e-9fdc1754f87d | -3.5496 | -46.3957 | 2024-10-25 18:25:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ba2ee564-d153-3e90-92dc-08ae4f8789f8 | -3.4951 | -54.4366 | 2024-10-25 18:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 1f63081c-0ecc-3ed0-8e1a-132aaaee31fe | -3.6526 | -51.935 | 2024-10-25 18:25:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| fa2bc17e-e072-3902-9956-8ce20e119bf1 | -3.6908 | -44.3647 | 2024-10-25 18:25:26 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6eaf6cdd-1542-366d-aa53-35d085fd7bc8 | -3.7095 | -44.3638 | 2024-10-25 18:25:26 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9ad11ec2-7700-3e84-ad06-406694d21afe | -4.2861 | -50.7498 | 2024-10-25 18:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a3116071-413b-3430-b9df-3e0daaa505b3 | -4.3982 | -50.5358 | 2024-10-25 18:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b47bcd9a-291a-3a43-97da-a0b6aeaecae6 | -4.5437 | -50.9686 | 2024-10-25 18:25:31 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 29684af4-5b2d-37fa-97c5-e8840e0ec8c7 | -4.5912 | -56.0924 | 2024-10-25 18:25:31 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| a3698e85-c85f-3f7f-93c7-75bbe67829f7 | -4.9221 | -41.9595 | 2024-10-25 18:25:33 | GOES-16 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| caf2a049-77d7-3eef-857d-4be0ec683f44 | -4.922 | -41.9834 | 2024-10-25 18:25:33 | GOES-16 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 106.2 |
| 5b841ece-1802-38a2-a7bc-b49e508af458 | -5.0769 | -43.6644 | 2024-10-25 18:25:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 247.4 |
| bd8e3858-bb9f-3053-9ea2-cbe7537aa761 | -5.3553 | -46.2344 | 2024-10-25 18:25:35 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8880a4b2-5967-3fa9-9b33-da62974955ef | -5.3799 | -41.1084 | 2024-10-25 18:25:35 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 5d18ac8e-b79c-3591-a724-fc9d4833804e | -5.9873 | -44.4286 | 2024-10-25 18:25:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 81bc068c-7aad-397d-b4de-e0046c3e215d | -5.9775 | -41.5421 | 2024-10-25 18:25:39 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 306.2 |
| 7c1996f3-0fd0-3186-a66c-c65e7ab914df | -6.2744 | -47.8253 | 2024-10-25 18:25:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 024c7bbe-508c-3d79-ab9b-ab4de32ceb33 | -6.7045 | -43.9554 | 2024-10-25 18:25:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| ba491804-23aa-3ef1-9c88-ddccac161053 | -6.6857 | -43.9571 | 2024-10-25 18:25:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4031b8de-fcee-3906-8da1-ae99dfd032ee | -6.5266 | -62.9483 | 2024-10-25 18:25:43 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 9e8d94b8-1415-32c9-8b51-1481bd3e2d4a | -6.8927 | -38.987 | 2024-10-25 18:25:44 | GOES-16 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 127.8 |
| c2243531-f33b-35e8-89ae-2011910ee6d2 | -6.9593 | -41.3296 | 2024-10-25 18:25:44 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 118.4 |
| f8b0e62f-ffa6-3a56-8285-24d190897394 | -6.9655 | -39.2313 | 2024-10-25 18:25:44 | GOES-16 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 818527e6-acd9-3f19-991e-631231362cea | -7.0137 | -46.6921 | 2024-10-25 18:25:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b1f791b2-d561-3901-bea6-81c247d9738d | -6.9571 | -46.7411 | 2024-10-25 18:25:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 4d557152-0958-3da3-9209-6e72c9cefd0d | -7.1625 | -46.7908 | 2024-10-25 18:25:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d46e82a7-bbbd-3477-ac8c-cf0c6b9776c9 | -7.2946 | -44.9589 | 2024-10-25 18:25:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f1c52837-50d6-3567-8d31-0454e57dc5a1 | -7.4003 | -45.5846 | 2024-10-25 18:25:47 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| b927c29d-9f83-347f-993f-95b705bbe36e | -7.5511 | -47.2444 | 2024-10-25 18:25:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 1d289246-dfbe-393b-b41a-27a8db17e08d | -7.5289 | -45.8434 | 2024-10-25 18:25:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4afee52f-44c4-382e-aae0-e7ed420ef863 | -7.5477 | -45.8417 | 2024-10-25 18:25:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 1dc66882-89ef-3a40-8391-44ccc62ce545 | -9.0835 | -45.0499 | 2024-10-25 18:25:56 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| f82f992f-3053-3b0e-a830-de49212e5b08 | -9.2024 | -43.3429 | 2024-10-25 18:25:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 6765f3ba-fe4f-3fc2-923f-8072a1b51a95 | -9.3537 | -43.3711 | 2024-10-25 18:25:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 113.9 |
| 9193947b-44a3-3c4f-864e-f6acc6252154 | -9.4699 | -43.215 | 2024-10-25 18:25:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 4cc80108-a706-3388-b555-9417bfa5c971 | -10.5948 | -44.261 | 2024-10-25 18:26:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 957d13c7-a372-3515-a249-ff7f76cd8d26 | -10.6292 | -43.3416 | 2024-10-25 18:26:05 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 49804c0f-8c40-3fe1-ae28-b92efa5d7a1a | -10.5753 | -44.287 | 2024-10-25 18:26:05 | GOES-16 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| cb540739-976d-353a-b486-212e7153f06d | -10.6249 | -55.9757 | 2024-10-25 18:26:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| b9bd9f37-6d7a-38c0-9dca-79f3f6113094 | -12.1179 | -43.6354 | 2024-10-25 18:26:13 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| e1b29ee3-d394-36cb-a3a8-6630ef1dd8e4 | -13.4726 | -42.5619 | 2024-10-25 18:26:20 | GOES-16 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 774d0ddc-5194-323e-bcde-dcdff609c64c | -19.5268 | -56.6801 | 2024-10-25 18:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.1 |
| df30a14d-5496-3fe7-add2-1cea982b1195 | -19.5083 | -56.5989 | 2024-10-25 18:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 9c7ca458-9b40-390e-9913-cc5e970b78fe | -19.5079 | -56.6199 | 2024-10-25 18:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| c262b982-bf7b-3421-b7f8-067e964b294e | -19.5071 | -56.6619 | 2024-10-25 18:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.3 |
| a6e3da35-ab46-3981-b5b8-70f5b3a99fbc | -19.5075 | -56.6409 | 2024-10-25 18:26:54 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.8 |


[Clique aqui para ver as próximas entradas](README192.md)
