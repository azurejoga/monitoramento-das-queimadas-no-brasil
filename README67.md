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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e0e16d0-660d-3836-8cba-d934846fa98d | -9.1339 | -65.788 | 2025-08-28 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 164.7 |
| d6a90aa9-a252-3ca5-a14a-5c4e35a95680 | -8.2896 | -45.1357 | 2025-08-28 05:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 72dbe582-4213-36f1-8e98-98daf4af2377 | -9.1154 | -65.7886 | 2025-08-28 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 288.7 |
| 30b083c4-65ac-3591-8c3e-a521198cc9d1 | -8.2702 | -45.1833 | 2025-08-28 05:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3bd8177a-2bca-367e-9797-38a11c8a598e | -10.8236 | -60.7633 | 2025-08-28 05:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 13b3fbcb-5266-3806-8453-a5ba0fc9b48b | -9.1153 | -65.8073 | 2025-08-28 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| ff8a5072-31ec-331f-8387-e2775df39afc | -10.4738 | -57.9366 | 2025-08-28 05:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 38c9b412-9dd9-340a-bfc5-9b53742219b0 | -10.8047 | -60.7837 | 2025-08-28 05:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 5c92ed26-b559-38b4-8de3-1cf57f2596dd | -9.1155 | -65.7699 | 2025-08-28 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 157b78b9-e9f5-3a04-adf4-e5a93bdb7af2 | -7.3955 | -39.6845 | 2025-08-28 05:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 175.5 |
| 0f9beda7-3a6e-377d-aace-52b6dc9583bf | -9.134 | -65.7694 | 2025-08-28 05:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 33bfdbc3-116e-314e-aa86-a6ca88fadc9c | -11.3329 | -43.5452 | 2025-08-28 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 479b9245-b33f-378b-8cf1-d2094c83caa3 | -7.3958 | -39.6595 | 2025-08-28 05:10:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 59.6 |
| fa1c3c12-ece2-384c-9cbb-4d9d91869b76 | -10.786 | -60.7848 | 2025-08-28 05:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| d63e4b92-7d3d-36ad-90b0-ec091401a84a | -6.4355 | -44.5764 | 2025-08-28 05:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 89869b59-1516-3f65-82ab-6a5c1f0621e3 | -10.8049 | -60.7644 | 2025-08-28 05:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 446.4 |
| b70d1b0a-7077-35c0-98e9-adf2464a5aad | -10.7862 | -60.7655 | 2025-08-28 05:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 6c46560c-4379-31e2-a844-0cd1df38b712 | -10.4736 | -57.9563 | 2025-08-28 05:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0965ac86-6042-3f4f-b56b-576df1a8cab9 | -8.2893 | -45.1586 | 2025-08-28 05:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 29ed4f0d-495e-3cc7-baa3-f9821a4b92ac | -6.8772 | -43.6152 | 2025-08-28 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 818e38cb-088a-34a0-8e70-025edd89a061 | -8.6989 | -63.8356 | 2025-08-28 05:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d8271983-f7a9-3b18-9a3c-9fd9ccffcc76 | -10.8236 | -60.7633 | 2025-08-28 05:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d186ae19-e476-3533-bec0-73f68faf8636 | -9.1339 | -65.788 | 2025-08-28 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 201.8 |
| ec1537e9-7bdb-33a7-9e99-f15caff2b1bd | -10.4738 | -57.9366 | 2025-08-28 05:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f1f8ec92-97b0-301d-928e-7d32577a6511 | -6.896 | -43.6135 | 2025-08-28 05:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 734a2a90-4fbf-32ef-af24-b9d7ff91f0ce | -9.1338 | -65.8067 | 2025-08-28 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| fbedff20-1713-3e56-a96a-0c87b5ca3434 | -10.7862 | -60.7655 | 2025-08-28 05:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 7d3f0f81-9ca3-3152-b26b-67613407c8a9 | -10.8047 | -60.7837 | 2025-08-28 05:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 9052fab9-5601-3d39-9ad3-b387823b5f42 | -9.1153 | -65.8073 | 2025-08-28 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 660ba98c-f713-394a-94c5-eb1e96be681d | -10.8051 | -60.745 | 2025-08-28 05:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| b6ebc2a5-c17f-301c-8f73-ec15f00bc00e | -10.4736 | -57.9563 | 2025-08-28 05:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d5e69be0-f22b-375c-a9f0-b5529fb9304f | -11.3521 | -43.5423 | 2025-08-28 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9a21198d-a531-3622-b6d1-e06d670dfd08 | -14.2958 | -53.042 | 2025-08-28 05:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 8463b030-6ebc-3cb5-823b-71e5cbf8e44f | -8.289 | -45.1814 | 2025-08-28 05:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1224bfc5-a45d-3086-b007-0723a831193e | -7.3955 | -39.6845 | 2025-08-28 05:20:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 76.8 |
| f22d9ae8-561b-3cdd-8a78-683e13cc12eb | -9.134 | -65.7694 | 2025-08-28 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 38575944-3a79-36a4-9a87-83fa39c77de5 | -10.8049 | -60.7644 | 2025-08-28 05:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 257.8 |
| 40417b86-3eaa-33d6-9c57-c3b6a43c0e9d | -9.1155 | -65.7699 | 2025-08-28 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 2011a876-d980-3967-99c2-e7f5ea74491a | -9.1154 | -65.7886 | 2025-08-28 05:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 240.7 |
| 98ef3b16-7183-3d78-b338-7b4fd317ba5c | -8.2893 | -45.1586 | 2025-08-28 05:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 6f5ef081-1ec5-3c96-9742-52cda7f3542f | -2.83151 | -54.56319 | 2025-08-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ef4ccf6-2eea-3445-93f1-2a7a6525b69a | -4.96356 | -55.81272 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1afdbdcb-8d3b-312b-be15-40ab527ba709 | -3.7606 | -49.05964 | 2025-08-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7c34df2-4ab0-3197-b46a-5953cc47b071 | -4.05519 | -56.33495 | 2025-08-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc967621-d15e-3346-a847-797efe834253 | -4.80075 | -47.2663 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f59e1260-3c7a-3b63-86af-ac4d91270db8 | -3.7659 | -54.82367 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc847832-0c28-35e5-a676-84c3d4db34f3 | -3.76751 | -54.8133 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b90e80c9-548a-32b5-9202-0ed85cf71d44 | -3.75526 | -49.05439 | 2025-08-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f788fec-20a6-3839-93b5-36f5ad27ac51 | -4.24802 | -54.92184 | 2025-08-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35c5c476-c62d-38e8-94b4-f13e4c77ecdd | -5.32101 | -55.87758 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42131fde-db28-3f24-a0ef-09409d953d74 | -4.08385 | -48.04456 | 2025-08-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 090ed19f-7ef4-3e48-9a12-87787788c3d2 | -6.16602 | -47.27923 | 2025-08-28 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 564b1204-b689-3e63-b3e7-0e6709b2f019 | -3.24132 | -50.80583 | 2025-08-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f13fe493-3bdb-3d0c-82ce-336e35d3db0a | -3.10015 | -54.5963 | 2025-08-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 839eeefa-d8c1-3390-a608-318ab0e0044b | -4.8016 | -47.26024 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5279cab6-1043-31ef-be9a-c405e7e5c41c | -3.75836 | -54.81887 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d683af65-9e4a-3923-8f61-e7bf15d63c8c | -4.95969 | -55.81212 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9398c0e3-8ae2-3c60-8d44-056700c017f7 | -5.32027 | -55.88247 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| decbde7c-c9d8-3046-8158-68929c3244be | -4.79237 | -47.262 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5255ff85-bc21-384a-8999-eaf337db5044 | -3.98104 | -47.88404 | 2025-08-28 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8dc922b-f699-3a55-9201-07604594f4ed | -3.11999 | -59.35014 | 2025-08-28 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d8e726b-3e93-3575-82fc-d3759c517765 | -3.84794 | -56.97519 | 2025-08-28 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef528376-d098-3cef-b718-1d68ef95812b | -3.76347 | -54.81265 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0eebb668-70f7-320c-83da-a3af07abd044 | -4.78371 | -47.27396 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98c9d706-b107-372f-81de-ca023576b3ee | -3.75942 | -54.81199 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ab003a49-9051-3ec1-ac6a-a4acb63431fc | -3.4065 | -52.72724 | 2025-08-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ad3153c-60ad-3ec8-8332-558e6ce91f6a | -1.88243 | -55.5252 | 2025-08-28 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b415349-6550-3efd-88f5-0211f7d6da03 | -6.15969 | -47.27967 | 2025-08-28 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1dc5cc2-ee93-334a-b31a-51ab6254e93a | -3.75685 | -49.05602 | 2025-08-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0f3e24e7-f336-3a6f-898f-7e5e47aca968 | -4.7949 | -47.2586 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 418dac10-6648-374d-bef8-73e8e27ef6d2 | -5.19097 | -46.06601 | 2025-08-28 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c02b28d-488d-3ee1-bc37-4687274bf258 | -4.79054 | -47.27459 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e88dc7f-53a6-367d-9ecd-0154770ef77c | -3.76698 | -54.81675 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5c987e52-cbdb-3e6c-a85b-795ea5777ff4 | -3.76125 | -49.05523 | 2025-08-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8285712-0698-3479-ab3e-6a451c32840a | -3.75342 | -57.21002 | 2025-08-28 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17b6c2c2-d3a7-3997-914e-1503e864fa5b | -2.67522 | -54.79605 | 2025-08-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc3a020b-b277-35c3-b388-4f735b03d555 | -5.56443 | -52.07534 | 2025-08-28 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c675dedc-e7fa-36fd-bc0d-a912daf602c1 | -4.48718 | -55.55758 | 2025-08-28 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2a0e536-106e-3068-9291-89410fb0de53 | -4.79909 | -47.26336 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a1cf2a6-5bf5-363a-a394-47122938afe1 | -3.7624 | -54.81953 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ba3ea48-65cf-3d64-9de4-ebb8d3ae3d42 | -4.56056 | -55.96014 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fb8a4c6-b80d-35e9-b974-2c99431ff664 | -4.79997 | -47.25736 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 16d9a925-4e17-3280-9c4f-5cd2c84ca416 | -4.05587 | -56.33057 | 2025-08-28 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e823f0-5edc-3bc2-a41c-4ea429053fb5 | -4.07745 | -48.04354 | 2025-08-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c429161-823b-3366-873f-dbe53a49dbb6 | -3.76644 | -54.82019 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8af51fdd-1056-36a8-bc9f-d7b0be35cfda | -3.23602 | -50.80511 | 2025-08-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 945d1684-0693-3da8-bc5a-a6522b19fbfc | -4.78638 | -47.27023 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e15462e9-d7cf-31f2-8ca2-785b61d0b2b8 | -4.95897 | -55.8169 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd43294-731c-3657-9849-fadf7b883873 | -3.75889 | -54.81543 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 642783ba-e900-3e8e-8484-f96a7e9f772e | -4.79405 | -47.26474 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 06be4240-fbaf-3220-ac23-7c9ccf2fc9a7 | -4.79146 | -47.26825 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 94689907-b372-36f5-9e8a-bd62215696d7 | -6.1666 | -47.28049 | 2025-08-28 05:23:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc00be1c-5054-3242-b1e8-10dc8e01e02d | -4.89207 | -55.8095 | 2025-08-28 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc4db9ef-8b4b-3d6b-97d2-c2f07e7e1f0d | -5.19823 | -46.06736 | 2025-08-28 05:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19dcf398-865c-3982-a866-922d38ecafe9 | -3.76293 | -54.81609 | 2025-08-28 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da965301-2c69-3d4b-9cf0-cc8d0a65b371 | -4.7982 | -47.26943 | 2025-08-28 05:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 01ca9363-2c31-32f3-b20a-378ac4d298b5 | -7.3475 | -59.66167 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffab7985-7a80-31ab-944f-2ede05f312ba | -10.08614 | -62.89298 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1268c22c-54ec-3d48-8320-092ddd31cb03 | -8.23836 | -61.45425 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3ad2e04-f5c9-3da7-aeff-1ab39d131ccb | -9.31239 | -57.69426 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README68.md)
