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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbe0df22-3332-38ef-a6df-10a9bc1b9d9a | 4.63244 | -60.65926 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f146189b-b412-34b3-ac71-3a795e2d329a | 4.63628 | -60.65892 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0152647-a83d-3d28-9bf3-250c54e1eb48 | 4.80167 | -60.15414 | 2025-02-12 05:14:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cccdfdbc-4af5-3dd8-83f3-b18eddf6c2f4 | 4.62409 | -60.65549 | 2025-02-12 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 297a177a-1a7e-3cef-b9b2-859401bd6030 | 1.12523 | -60.52515 | 2025-02-12 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86b4c9d1-13f5-3a45-906a-c4efa8bc52ac | 3.07374 | -60.03743 | 2025-02-12 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73fedc4e-c950-3b52-8dd0-9127085819fb | -1.56548 | -54.02517 | 2025-02-12 05:16:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9fd4f58-0844-3e2e-a065-99c24e961060 | 3.0797 | -60.02806 | 2025-02-12 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 503ffe2b-934b-3369-9479-f56fd884ec16 | 3.07735 | -60.03688 | 2025-02-12 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b449705-a052-3f9f-979c-2b81572f8bf2 | 1.12588 | -60.52931 | 2025-02-12 05:16:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd85b9cc-dffe-3bef-af3a-79bcaf449d96 | 3.08331 | -60.02751 | 2025-02-12 05:16:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e38499c3-1191-3672-bd52-03f04924dc6c | -15.27054 | -60.31513 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3823ab2-8928-36ab-8036-da93f02d0175 | -15.2711 | -60.3115 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1856564-0af6-3160-b52d-d4fecc95e1c7 | -16.08373 | -60.06533 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41e3c738-48c0-3615-bbba-ea3dc1a083b0 | -16.0439 | -59.68047 | 2025-02-12 05:20:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 255016d9-d1f0-35b7-b042-f1f294db3785 | -16.08767 | -60.06216 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 695bcd86-1cf4-3bd8-98ba-223e5bd5d56f | -16.25052 | -59.60382 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c71ac034-7446-3bf0-8dd1-f190dcaa9138 | -16.46635 | -58.16828 | 2025-02-12 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 394e8045-2c04-355b-810a-8a476e0d6aca | -16.46568 | -58.17015 | 2025-02-12 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a8335d90-44bd-315a-bf1a-7dcecaad658a | -16.08318 | -60.06902 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8767ee1-fc4f-3864-a139-8d8b62e59b13 | -15.39306 | -60.17812 | 2025-02-12 05:20:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a8ae768-43bf-34fb-9496-4bb097b539a6 | -16.46272 | -58.1677 | 2025-02-12 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3db40da2-366a-3f20-a99f-f42001c11ff1 | -16.46205 | -58.16957 | 2025-02-12 05:20:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e4232e4b-1ed2-34f9-aa20-b19c6bd514fd | -21.82991 | -56.50245 | 2025-02-12 05:22:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff7ce65f-aab1-30d0-9a25-2edb0a2a05d4 | -21.0787 | -56.389 | 2025-02-12 05:22:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d85461be-b979-3c62-ae19-7587be184d72 | -19.49025 | -55.32702 | 2025-02-12 05:22:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 62fc6af0-d286-3cb2-a1a9-ba7a48a1b167 | -19.48969 | -55.33166 | 2025-02-12 05:22:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e9f8f88d-16a5-3f7d-bc74-7ba5ae21c03f | -21.96621 | -57.58568 | 2025-02-12 05:22:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9ffc208-3dd4-317d-bc76-d534ad842816 | -29.79677 | -57.11176 | 2025-02-12 05:25:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 4c356d7c-3acf-3252-86d7-656031685972 | -29.79218 | -57.1112 | 2025-02-12 05:25:00 | NPP-375D | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 7107eca4-9b2c-3add-8821-477a2a5013e7 | 3.64809 | -60.97242 | 2025-02-12 05:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9effc3eb-30f1-37b2-b0fa-4dac865cfeb5 | 4.63281 | -60.65807 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec0f1ba5-5a14-3f9c-a2be-a6af44ac94bb | 3.07223 | -60.03589 | 2025-02-12 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2641560-c130-305a-b9d6-f63364876f62 | 3.0817 | -60.02585 | 2025-02-12 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c84f1b0-3e3d-33fa-b85b-9185c528fda8 | 4.62817 | -60.65113 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f83ba4-c72f-34f4-9692-2f5521b65851 | 4.6316 | -60.65049 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4186d1e-b625-3ade-8967-4a44d88cb6af | 4.63503 | -60.64988 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6fc00df-3ecb-335c-9b17-19c9f5cf2f1a | 4.62938 | -60.65872 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8261cf92-45d1-3f60-8c5b-804da7c87456 | 1.12372 | -60.52994 | 2025-02-12 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a065348-f153-39c1-b5a9-52e3bd3c0f2e | 1.12666 | -60.52524 | 2025-02-12 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 899d6359-9013-3bb6-b877-0513a086565b | 4.62594 | -60.65929 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06d3dd66-9277-3428-97bd-df113486d0ee | 4.62473 | -60.65173 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 098e16c3-aca7-3d4a-91d0-2c14d831a42d | 4.63624 | -60.65742 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3d93f39-8806-30c4-aa3d-2b477e794109 | 1.12306 | -60.52582 | 2025-02-12 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55106bad-bddf-3935-a3c0-f8a93dda49c9 | 4.62654 | -60.66302 | 2025-02-12 05:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 20d737a9-03a2-3884-84c2-fb639833171c | 1.12731 | -60.52937 | 2025-02-12 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72d3ce4c-aa4c-33de-9e09-7e33eacee82d | -16.46456 | -58.16985 | 2025-02-12 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2218182c-7f3a-3bd5-be1f-3653d8901406 | -15.39173 | -60.17994 | 2025-02-12 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bd874c1-4cd4-331c-a8b6-bf1351564122 | -19.48874 | -55.33385 | 2025-02-12 05:44:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 118fa4eb-71f4-3fd7-99a1-5291d8f5b4a3 | -16.08474 | -60.06366 | 2025-02-12 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb7751dc-da8b-33f2-a2fe-09f5ad6525b9 | -15.2722 | -60.31222 | 2025-02-12 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 985120dd-7141-3a45-8232-9b3836a17726 | -16.46415 | -58.17342 | 2025-02-12 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 27ba22cd-6ef7-3668-a7a9-3e4d77ba2436 | -16.08945 | -60.06425 | 2025-02-12 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b6df216-ec62-3e3f-9fdc-f33372874a06 | -20.91236 | -56.5326 | 2025-02-12 06:05:00 | AQUA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41ba93bb-e9aa-314b-a35a-5d485cfad315 | -7.91595 | -39.98525 | 2025-02-12 12:12:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 257431d6-5cd6-3fac-9486-e8d49fd7d27b | -6.53301 | -43.11433 | 2025-02-12 12:12:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2a18d0d5-f9a9-3c2a-8520-8a4be3edab43 | -7.02629 | -37.85725 | 2025-02-12 12:12:00 | TERRA_M-T | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3143b7cd-f987-3d39-9fba-3b3abfe7e9e6 | -7.9146 | -39.99477 | 2025-02-12 12:12:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 49fdd6e3-02d8-384b-90e2-b12943b8191b | -6.71305 | -38.81987 | 2025-02-12 12:12:00 | TERRA_M-T | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 46368026-5623-3f32-9c55-bc3303a35d21 | -5.31972 | -38.08652 | 2025-02-12 12:12:00 | TERRA_M-T | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 578739ff-2340-35c2-b565-bf5d0b4112c2 | -6.53442 | -43.10469 | 2025-02-12 12:12:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 855aa436-0e97-331b-9c55-4b2b2679101d | -7.45099 | -39.94961 | 2025-02-12 12:12:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 3d805453-cf19-3781-be6c-e50ab98f9793 | -6.35353 | -43.38265 | 2025-02-12 12:12:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 01bbc8e6-0b11-327e-86a7-245b8c7e4025 | -6.17628 | -38.2538 | 2025-02-12 12:12:00 | TERRA_M-T | RAFAEL FERNANDES | RIO GRANDE DO NORTE | Brasil | 2410504 | 24 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 073c1294-de08-358a-b414-5835e8753ccd | -6.81189 | -38.01599 | 2025-02-12 12:12:00 | TERRA_M-T | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 5362aedb-379d-3d0b-981f-7025b5ac2f84 | -7.02738 | -37.86371 | 2025-02-12 12:12:00 | TERRA_M-T | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b7f6c7db-3e60-314e-b100-aee24f75577d | -6.23108 | -38.52477 | 2025-02-12 12:12:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1e96be88-d3a2-373a-af15-7fa33f85f964 | -8.07195 | -37.46402 | 2025-02-12 12:12:00 | TERRA_M-T | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| dd8a7205-78e4-308b-a402-fe6491278c89 | -8.09868 | -38.09419 | 2025-02-12 12:12:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 16e46612-7d94-3cca-83eb-151acf56a3e7 | -8.50169 | -35.31338 | 2025-02-12 12:12:00 | TERRA_M-T | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| ea83b9f2-55aa-3d57-9084-bac4ce285bae | -13.90782 | -45.28629 | 2025-02-12 12:14:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eba886d7-e6a5-3c6a-b416-d3de095fbdb4 | -8.18441 | -44.48309 | 2025-02-12 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 61df64aa-7435-32fb-b322-141de96d5499 | -12.9047 | -45.08075 | 2025-02-12 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8b184bdd-55d8-3cb4-974c-5acd13742712 | -9.18688 | -38.79485 | 2025-02-12 12:14:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 2634e4bb-cd87-30b5-a525-9e7bcae00979 | -9.75518 | -37.05096 | 2025-02-12 12:14:00 | TERRA_M-T | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 79be0b2c-255c-3264-af87-1d14c33ad3e9 | -8.3548 | -45.1919 | 2025-02-12 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| b520d147-ba05-3362-bfaa-03d664fec76c | -8.32172 | -44.93563 | 2025-02-12 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bbf9b2ac-d418-3848-80d3-455ac074ebb9 | -12.90307 | -45.09119 | 2025-02-12 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bbb9d98c-87df-3d9b-acda-f68291093578 | -10.65283 | -44.49595 | 2025-02-12 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| bf0da50c-1555-3e9a-8627-06ffe008ad27 | -7.97165 | -43.49318 | 2025-02-12 12:14:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 50f7e5a1-3424-3ee8-8b33-deb05ea64bbc | -9.1295 | -39.93681 | 2025-02-12 12:14:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e7402233-e152-354a-8138-cce83939c64b | -10.65438 | -44.48573 | 2025-02-12 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 91f1e449-10c8-3aee-9249-83d6fdb610ce | -7.67069 | -44.56685 | 2025-02-12 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 78778a5f-5492-3155-9185-5888654b2194 | -9.18533 | -38.80609 | 2025-02-12 12:14:00 | TERRA_M-T | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 5da466ff-8c5a-3be6-b931-e0e945a7f97a | -8.18279 | -44.49393 | 2025-02-12 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f4390c68-182a-3e36-aa26-b8219b25d311 | -11.06366 | -40.58873 | 2025-02-12 12:14:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 259cf50c-018c-3358-a90d-b14c747eb52e | -8.74188 | -35.58038 | 2025-02-12 12:14:00 | TERRA_M-T | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| 05fe6afb-f10e-3d15-8a60-bff5ea557eae | -7.66899 | -44.57803 | 2025-02-12 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5aed6ed0-9da7-3bc8-a566-5a053e3c4a42 | -11.66857 | -46.46607 | 2025-02-12 12:14:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 58a9fd08-3de0-32bf-b09b-377557d82154 | -13.20449 | -43.65436 | 2025-02-12 12:14:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 7af045f0-da6b-3964-8ad7-9579deccdd33 | -15.73716 | -46.11197 | 2025-02-12 12:14:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 5045faa0-a7d7-3f8a-a22e-23079cb2b26e | -18.96476 | -39.803 | 2025-02-12 12:16:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| bcf47484-b07a-3622-bb7c-9b2ba9bd8116 | -18.95581 | -39.78794 | 2025-02-12 12:16:00 | TERRA_M-T | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 94846ea1-8bb0-363b-afef-ef41581bae5b | -20.52321 | -42.03286 | 2025-02-12 12:16:00 | TERRA_M-T | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |


