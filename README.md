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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8f9c0db-feb6-3617-a010-852cfba8ba15 | -2.7801 | -48.5592 | 2024-11-16 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 2952e9f1-f98e-3392-86f2-ba26bf933147 | -2.1378 | -53.7244 | 2024-11-16 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| bcbcc100-3479-3010-8931-ca34b3992f96 | -3.7685 | -50.7908 | 2024-11-16 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 47faf16f-d66c-39b3-97b7-7fde83749b64 | -3.1272 | -54.5464 | 2024-11-16 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 91defef8-6bc0-3d34-9c13-4aa57a7f7f66 | -2.1562 | -53.7039 | 2024-11-16 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 319.8 |
| 44905d14-9626-3b99-9d1b-d1b08edf89c6 | -3.7686 | -50.7699 | 2024-11-16 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 463a878d-6b67-3130-803b-e834720406d8 | -2.3741 | -54.6626 | 2024-11-16 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 33dc7fa9-2342-30cb-8eaf-033817d83118 | -4.9969 | -44.3378 | 2024-11-16 00:00:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 0885d7de-b6ea-3935-abed-1475788d8992 | -3.5851 | -50.5255 | 2024-11-16 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 87c8064a-a2c5-35e2-871b-caec47e23bd4 | -2.5767 | -54.4188 | 2024-11-16 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 1e759f1e-ae2f-3378-b8cc-734ab81ea880 | -6.3007 | -39.4763 | 2024-11-16 00:00:00 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 99.1 |
| 17cefd00-527a-31b8-95ad-519fe1441727 | -17.5879 | -57.4917 | 2024-11-16 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| ad754abb-0ffa-39fc-aa6c-3f02100e75c6 | -2.1563 | -53.6838 | 2024-11-16 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| b432a406-30dc-3fdf-9609-c59a8b075efe | -3.1456 | -54.5459 | 2024-11-16 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 54a33d65-a64c-3638-aec4-36098571468e | -2.1379 | -53.7043 | 2024-11-16 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 18f601e9-5565-399d-bd8b-9dc15c6be4fa | -3.1273 | -54.5064 | 2024-11-16 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d205e4c6-77c0-3be9-bbf4-0a54b49fc1e1 | -1.22 | -53.6969 | 2024-11-16 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c64a139b-5f7b-3b25-a914-b36ce6475eb2 | -4.9971 | -44.3149 | 2024-11-16 00:00:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 6cc685b5-779d-31d4-9648-b1063483ca3c | -3.1456 | -54.5259 | 2024-11-16 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 253.1 |
| e22adb31-3b8a-3e4f-b6d8-e29a81a7dfd0 | -4.3754 | -48.0882 | 2024-11-16 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c4d446f8-8081-3463-945b-560a51afb353 | -3.3171 | -52.8667 | 2024-11-16 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 402bcc12-3014-3298-9756-c9208bb6528a | -2.6131 | -54.5381 | 2024-11-16 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 69bcf62c-97e7-3c7f-9f2e-7cb99cc09bd6 | -3.6255 | -53.9912 | 2024-11-16 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0542a7d6-7795-3791-add7-caea8f0cd2ec | -3.5438 | -51.5051 | 2024-11-16 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ff3bd04b-b080-3fd9-8c26-f07c8b4cd990 | -3.5083 | -47.212 | 2024-11-16 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| a563f4b1-c880-35b3-8722-4d7bf4bb2f8a | -3.75 | -50.7914 | 2024-11-16 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 3371653c-76fd-3ca1-adc3-42193cda4027 | 2.6171 | -60.4122 | 2024-11-16 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| eebd0a98-bae6-38c1-9962-ce75d07c48ee | -3.1273 | -54.5264 | 2024-11-16 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 92b337ef-6818-33eb-818e-17f141d7660c | -19.7724 | -55.4004 | 2024-11-16 00:00:00 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7c729cbc-523a-3957-85cd-3305e924db2a | -4.9784 | -44.3161 | 2024-11-16 00:00:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 5bb62582-a00b-3716-969f-a2a70f061ff4 | -3.5439 | -51.4844 | 2024-11-16 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 234e7588-10ef-3e5a-af97-d0922e39cec8 | -2.1562 | -53.7241 | 2024-11-16 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 194.7 |
| f2a783e1-547a-31d4-9835-09f5bb5fdd28 | -5.0157 | -44.3137 | 2024-11-16 00:00:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c5127645-3533-38e6-ac80-0b64c9e77dc4 | -3.1457 | -54.5059 | 2024-11-16 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f34989a0-d488-38a7-aa2f-d61e19c411dc | -3.4898 | -47.2127 | 2024-11-16 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 36990975-879d-3fd0-9e79-768a16527aec | -1.8613 | -54.2714 | 2024-11-16 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d76a7e79-a0cd-330a-b84d-30004f9f5ef0 | -5.2352 | -44.9155 | 2024-11-16 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 87f1b2be-05c6-31a2-829d-ae782c39ebbe | -1.4765 | -53.9958 | 2024-11-16 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f67f8251-3c92-376d-a0af-475789f7c5ac | -5.0 | -44.31 | 2024-11-16 00:00:00 | MSG-03 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc555df-eb45-3b09-ab83-f7511012735c | -3.1272 | -54.5464 | 2024-11-16 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 95cba01c-55b8-37de-93ef-ad66d2cb39da | -1.2384 | -53.6967 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 4df69c6a-f8ff-3b61-88a7-2f40ab692eb5 | -1.8613 | -54.2714 | 2024-11-16 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| fc0abe9d-4fe0-3a0b-b61a-3abab6decaf0 | -5.2352 | -44.9155 | 2024-11-16 00:10:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| eddfa4bb-92cc-3751-a3bb-e667a97340a4 | -2.1379 | -53.7043 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 1e1f9fe7-fe50-3ec3-beef-742352f883a0 | -3.5229 | -44.4181 | 2024-11-16 00:10:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4edc656b-1cad-32b1-9edb-c594ff57786f | -3.75 | -50.7914 | 2024-11-16 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8105128f-e65b-37e1-b741-02ca0b6599c7 | -4.9971 | -44.3149 | 2024-11-16 00:10:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 53425830-94d1-39b1-8f0b-8090558f77e5 | -2.1562 | -53.7039 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 294.7 |
| 1a6af26c-382f-3e44-a3f2-62f9fe7039e3 | -16.9384 | -57.6291 | 2024-11-16 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 78cd5fc6-6988-3f5b-b26c-47b0c9d5728a | -19.7724 | -55.4004 | 2024-11-16 00:10:00 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c7a73c89-c3e7-3dbc-9be1-bd23f0d92aa4 | -3.7394 | -45.6523 | 2024-11-16 00:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a0386f18-cabe-3ce3-899b-6c63a6d0df9c | -2.651 | -48.477 | 2024-11-16 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 8d250f94-b7f4-3a06-82b8-6ece034c6504 | -6.3007 | -39.4763 | 2024-11-16 00:10:00 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 86886e69-4662-381a-925a-ef369fcefa33 | -3.1457 | -54.5059 | 2024-11-16 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 143fd555-a3d9-31f7-ac9e-4bb63461a02c | -2.1746 | -53.7036 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 653fe967-1577-3b2b-bc07-782f6aad0b35 | -3.7686 | -50.7699 | 2024-11-16 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 62b30e02-6c5a-3c3c-8ad9-719547089c0c | -2.6509 | -48.4985 | 2024-11-16 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| ba9cf1de-f3c3-3512-bc29-df1b50c1372c | -3.1456 | -54.5459 | 2024-11-16 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 541f3922-6047-349d-90d5-63dbacb61b2e | -3.7685 | -50.7908 | 2024-11-16 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 32fb0efa-f856-3202-8c6d-128b46bd44a3 | -3.5043 | -44.419 | 2024-11-16 00:10:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| c73a6bfe-6489-3f8c-b2dc-0d9291eedc16 | -6.141 | -35.1839 | 2024-11-16 00:10:00 | GOES-16 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 66.5 |
| 132805fa-4a3a-3646-bc50-6c2e4c7f08bf | -3.5439 | -51.4844 | 2024-11-16 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 106386ba-9087-3cec-81a9-0bdeeb4914bf | -3.1273 | -54.5264 | 2024-11-16 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 84e1ca15-d6c1-3234-931a-99d5f0d997fb | -3.5438 | -51.5051 | 2024-11-16 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 20931d2b-7f5f-39dc-b4cb-7dac6338093a | -2.6131 | -54.5381 | 2024-11-16 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 24b50f7e-eeaa-3da1-90d0-edec5ea8fe25 | -2.1562 | -53.7241 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| 17e6401a-ea16-35e7-9c3a-396eff3cad5e | -3.1273 | -54.5064 | 2024-11-16 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0ef5296e-e0f6-3d10-82ed-b887fc2ed119 | -3.7393 | -45.6747 | 2024-11-16 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 49b40c39-63f9-33b0-9340-75891f5f7e95 | -2.1563 | -53.6838 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5603d452-eff9-3650-b664-fefbd45b6039 | -6.1413 | -35.1565 | 2024-11-16 00:10:00 | GOES-16 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 72.1 |
| d1c713fc-32ba-397c-8be9-6238841bf9df | -2.1378 | -53.7244 | 2024-11-16 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 156b1fc6-5c94-3301-83c8-bc1561b03316 | -2.3741 | -54.6626 | 2024-11-16 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9f2034bc-3174-3eff-9e18-a845d30be6c4 | -3.1456 | -54.5259 | 2024-11-16 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 188.5 |
| aa67caee-1ab7-38bb-babd-46c38f74403a | -2.5767 | -54.4188 | 2024-11-16 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3ef318d2-cd63-39d0-8e72-95876f6d68bc | -3.5851 | -50.5255 | 2024-11-16 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b57c3af8-17c6-34b3-8f30-33185775faa8 | -3.6255 | -53.9912 | 2024-11-16 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e283f057-0881-3ceb-ad23-b0a6a359991f | -2.5766 | -54.4388 | 2024-11-16 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| bb0b58a9-42fa-3f3e-bd7e-487fa064a250 | -3.1456 | -54.5459 | 2024-11-16 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| c14e607e-294c-308c-a2e7-4e6647813c18 | -2.7615 | -48.5812 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 231f5694-e1dc-34da-a720-853234712e74 | -3.4725 | -43.4074 | 2024-11-16 00:20:00 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 06858a6f-b764-38af-96a3-8ef90f0707f1 | -6.3007 | -39.4763 | 2024-11-16 00:20:00 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 5003ff0d-2a29-39e6-9069-8c4783c85cab | -2.3742 | -54.6426 | 2024-11-16 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 07a85a62-139d-314c-8cf6-1bf52c715ba0 | -2.7801 | -48.5592 | 2024-11-16 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d8c2f98f-0878-308e-8328-5222488f3a13 | -2.3741 | -54.6626 | 2024-11-16 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 4f4be0f8-a899-3688-9a00-3cefef071c81 | -2.6131 | -54.5381 | 2024-11-16 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 622f9c80-efd6-355d-9d63-3ac8f25ffbc3 | -1.4738 | -45.746 | 2024-11-16 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 80e47ad1-2433-3026-8ac9-d16b878c3c91 | -2.1378 | -53.7244 | 2024-11-16 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 4131378b-af16-3cb7-b679-1e66439447e5 | -6.141 | -35.1839 | 2024-11-16 00:20:00 | GOES-16 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| a4ff4d1c-f9b4-3a2a-8217-d853a1ba70f0 | -2.1391 | -46.5531 | 2024-11-16 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 03fe677a-9d96-3527-9e7d-d75820c0b5c2 | -3.5229 | -44.4181 | 2024-11-16 00:20:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 0a4be337-b6db-3992-b738-d3ae9f582cc4 | -1.8613 | -54.2714 | 2024-11-16 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5b2329de-b324-3676-b8e8-25e452a108cb | -19.7724 | -55.4004 | 2024-11-16 00:20:00 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 1c2e76e7-1aea-3a27-be67-8a36d84a198e | -3.7394 | -45.6523 | 2024-11-16 00:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7f38f221-e132-3dca-a9f8-afec813bddb8 | -2.1562 | -53.7039 | 2024-11-16 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 246.3 |
| ac1007de-92b5-3768-9edf-a6780f80a231 | -4.3754 | -48.0882 | 2024-11-16 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 5d8df2f9-841e-35e7-bb9c-e8d9dcc15932 | -2.1576 | -46.5527 | 2024-11-16 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 4cce8e90-7855-3ccc-a8aa-a53e77e9e5aa | -3.1456 | -54.5259 | 2024-11-16 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 209.0 |
| de2b310e-7726-38c7-8468-b42222a91112 | -3.75 | -50.7914 | 2024-11-16 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7b219360-4dfc-3f1c-8340-07952fc08482 | -2.5767 | -54.4188 | 2024-11-16 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 09430e73-579f-3b0e-84ed-490a558bb57c | -17.5685 | -57.4735 | 2024-11-16 00:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |


[Clique aqui para ver as próximas entradas](README2.md)
