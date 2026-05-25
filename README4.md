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
| 03935085-95bd-320f-bfd6-7daed7648bbc | -8.26032 | -43.91557 | 2026-05-25 12:14:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 6a947ff2-33e6-3c65-aeb4-3d336927e041 | -7.84187 | -42.05702 | 2026-05-25 12:14:00 | TERRA_M-T | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 23963d26-ccc5-3b6d-89de-25ac98977f6c | -8.85713 | -46.68701 | 2026-05-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5f4aee1a-bb81-36ea-9d27-8da340ccedc5 | -8.85491 | -46.70433 | 2026-05-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 3ef07e51-020b-37e2-8ab0-acac56cfd17c | -11.55478 | -56.93607 | 2026-05-25 12:17:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| c3fa9a42-1e8f-341b-9d81-20c79cf3a956 | -10.43034 | -52.15022 | 2026-05-25 12:17:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7812859b-49cc-3f5a-ab88-0069acf5abb8 | -11.7349 | -54.79686 | 2026-05-25 12:17:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2c9de7a-2e8d-3784-acce-d4d6f8e8fce0 | -11.36872 | -52.95139 | 2026-05-25 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 30a7a814-523a-332b-a0b8-f2bae6f4a35f | -11.27614 | -53.96296 | 2026-05-25 12:17:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 07ac3561-76d6-36c9-819a-df519cdc1b90 | -11.36743 | -52.96032 | 2026-05-25 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1f181076-7772-332d-86e1-8584045aff66 | -12.64525 | -52.12979 | 2026-05-25 12:17:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 994d74cb-8679-3b62-b59a-33749adb034b | -12.64395 | -52.13904 | 2026-05-25 12:17:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e8e3bcf9-8089-3615-8f09-803ae9bfe900 | -10.70883 | -56.24022 | 2026-05-25 12:17:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b03e651a-73a6-3d5a-9d86-9434ee72453c | -11.64758 | -52.85791 | 2026-05-25 12:17:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dbfecd4e-00b0-3100-b172-4f37a02978b1 | -10.67687 | -49.6953 | 2026-05-25 12:17:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bccbb5db-7d85-38a2-af0e-c8c60fe8786f | -8.2674 | -43.9185 | 2026-05-25 12:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| df875f8f-8cbb-347a-b21b-2a9362d4853a | -8.2674 | -43.9185 | 2026-05-25 12:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6b053d7b-a85c-3ae8-b4dd-07982f173dfd | -8.2674 | -43.9185 | 2026-05-25 12:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4adc97e2-5260-36c2-b94d-18a0fa797613 | -3.9594 | -43.1271 | 2026-05-25 13:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d48b985b-b25d-3cf6-9bf0-e82bbb1764f8 | -8.2674 | -43.9185 | 2026-05-25 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| d607974d-9d4b-3839-9df7-82ade0c07289 | -8.2671 | -43.9418 | 2026-05-25 13:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ee7799dd-7781-3393-8746-c99951b93935 | -3.9594 | -43.1271 | 2026-05-25 13:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bff29b88-ba9d-364c-a5c0-d66b957ca795 | -3.9594 | -43.1271 | 2026-05-25 13:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| f5e11c9d-1f59-37bc-a94e-c5030e3b4927 | -8.2674 | -43.9185 | 2026-05-25 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2998db6d-358b-371a-ac3e-852cee52bc29 | -12.8859 | -58.1891 | 2026-05-25 13:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a1f40a58-9e91-3759-9448-8b7ad3baf120 | -3.9594 | -43.1271 | 2026-05-25 13:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 4032a972-6ef1-3f44-ae07-11fc95de887e | -11.3584 | -52.9514 | 2026-05-25 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e6988f28-c3a4-3817-83ab-1cbecfd849a6 | -12.8859 | -58.1891 | 2026-05-25 13:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 41e07f4e-4a67-3e26-896b-f57785c74b08 | -11.3584 | -52.9514 | 2026-05-25 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 9bd9722d-5b15-3fe3-bc9c-841bef58dc91 | -3.9594 | -43.1271 | 2026-05-25 13:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 56b15c78-9643-32ed-8127-7167d6407887 | -11.3773 | -52.9496 | 2026-05-25 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b1f66c72-78b7-33fc-858a-abe1c2063c15 | -11.5559 | -56.9432 | 2026-05-25 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 0c3c7835-41bb-3b03-bbce-3d888892b177 | -7.8381 | -42.0552 | 2026-05-25 13:50:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 350.9 |
| 2791916f-1e58-3339-8115-e916f0933024 | -11.3584 | -52.9514 | 2026-05-25 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 796ae769-39a5-3168-97d8-aabcad25bbc7 | -12.8859 | -58.1891 | 2026-05-25 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 42685e1c-6542-3567-9b5e-bb5c7431e465 | -3.9594 | -43.1271 | 2026-05-25 13:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 423a1013-d142-3581-8d1a-7b4b16fa5245 | -7.8191 | -42.0573 | 2026-05-25 13:50:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 350.4 |
| d31ca6e3-30ca-39fc-b290-f22df7771722 | -11.5561 | -56.9232 | 2026-05-25 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| ef3c1fe4-485d-3679-9878-23d1bdfb8417 | -7.8191 | -42.0573 | 2026-05-25 14:00:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 346.3 |
| 4ad07487-8526-3728-9261-2fad2f573bcd | -11.5561 | -56.9232 | 2026-05-25 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 9b8b0b6e-905b-36ec-ac61-d3dedfa6612d | -12.8859 | -58.1891 | 2026-05-25 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| c78b02ee-2eda-3e92-96f5-a0657d20911b | -11.3584 | -52.9514 | 2026-05-25 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 9a8517a3-2017-3bb5-b52f-71ccdb10f027 | -12.8857 | -58.209 | 2026-05-25 14:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7305a906-cb49-3ae9-9b73-cd401116efbe | -11.3773 | -52.9496 | 2026-05-25 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 26a32297-fdbf-33ed-9d20-7dd47fb6047e | -11.5559 | -56.9432 | 2026-05-25 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| e118e9ed-89c4-3032-81f4-0efb8d24117f | -3.9594 | -43.1271 | 2026-05-25 14:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 71932a0c-20b8-37c0-9277-fa37999a81ff | -7.8381 | -42.0552 | 2026-05-25 14:00:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 346.2 |
| d36d7f9f-9f4b-3681-93bf-7926b2019bc2 | -7.8381 | -42.0552 | 2026-05-25 14:10:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 395.6 |
| 44fe8a3b-40f1-37f0-ace2-e9e6889e4118 | -11.5559 | -56.9432 | 2026-05-25 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| f9b8df70-db25-3c8b-9213-98d4552620f9 | -6.1081 | -45.533 | 2026-05-25 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 3c2762cb-57b6-37f6-b3c7-1f258c0fc287 | -3.9594 | -43.1271 | 2026-05-25 14:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| a81307f5-05e2-3227-b624-64eccd6eeef0 | -11.5561 | -56.9232 | 2026-05-25 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 9e62494a-b3f0-32a6-a146-e089deb4dce5 | -11.3584 | -52.9514 | 2026-05-25 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| ed467221-947b-3d9f-be74-75e628c2feaf | -12.8857 | -58.209 | 2026-05-25 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 29e124c0-0911-3fc5-86b3-248cbf780522 | -11.3773 | -52.9496 | 2026-05-25 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 41e1a94d-4f84-3533-a95e-dedbeec0aba8 | -12.8859 | -58.1891 | 2026-05-25 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 163.8 |
| fa48e204-ee37-3558-8b96-67026c81be46 | -7.8191 | -42.0573 | 2026-05-25 14:10:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 433.7 |
| 0f6a66bf-112e-3f52-b11b-50fe5e0fd3a9 | -12.9049 | -58.1875 | 2026-05-25 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 3a40036e-c722-381e-ac57-717a43648270 | -11.3773 | -52.9496 | 2026-05-25 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3a3d3290-3e84-35c1-ad87-22d4e29dd2ad | -12.8859 | -58.1891 | 2026-05-25 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 98c13ee2-235b-3315-8ccf-f9bbddf9e9da | -11.3584 | -52.9514 | 2026-05-25 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| ba7c20a0-c376-349e-829c-ade5fb21b545 | -3.9594 | -43.1271 | 2026-05-25 14:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 198.0 |
| 245fa1db-8548-3867-9f44-e27fd9bca1b8 | -12.8857 | -58.209 | 2026-05-25 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 6a561e7c-4bf2-3fd1-a1e5-b43b4d8d4ddd | -11.5561 | -56.9232 | 2026-05-25 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| b46c57a1-a785-3033-bd91-dabf44e3d29a | -7.8191 | -42.0573 | 2026-05-25 14:20:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 475.9 |
| cdf00365-7446-30a7-8e45-7a15a235b1bc | -7.8381 | -42.0552 | 2026-05-25 14:20:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 422.7 |
| be01d793-9559-3dca-ba62-c113e0f2f161 | -11.5559 | -56.9432 | 2026-05-25 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| bf95a43f-d702-320c-b2f1-65633cc0d5ad | -12.9049 | -58.1875 | 2026-05-25 14:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| ce1f7258-b9db-3be2-865d-08892675cbb8 | -12.8859 | -58.1891 | 2026-05-25 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 2b211d95-76fe-38b0-a5e5-43f8673f26a8 | -11.3773 | -52.9496 | 2026-05-25 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 6a42c57e-9fdd-3559-ab17-d7bc59f68ba2 | -11.3584 | -52.9514 | 2026-05-25 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 06a407e4-bb67-3c38-9df8-67f7208f41c5 | -6.1081 | -45.533 | 2026-05-25 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| f1841a4c-1d21-3ef1-9d3e-4b1158332f8c | -7.8381 | -42.0552 | 2026-05-25 14:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 345.2 |
| bb6c9c12-a773-3b58-8085-c29aedca524c | -12.9049 | -58.1875 | 2026-05-25 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 254daf47-715b-3810-aaac-c7a2e0261767 | -3.9594 | -43.1271 | 2026-05-25 14:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 345c6352-c3e3-3884-b107-e52378c026b8 | -7.8191 | -42.0573 | 2026-05-25 14:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 561.1 |
| 21ef8fcb-2384-32dd-8621-c8cc73f9422e | -11.2527 | -49.6397 | 2026-05-25 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| aa2a9bb3-b66e-3857-8853-4f8959397856 | -12.8857 | -58.209 | 2026-05-25 14:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6a681723-e714-377e-8fdb-e196b81e5de0 | -11.5561 | -56.9232 | 2026-05-25 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| fd90d187-0084-3b4d-ac98-e5abad8d8ea8 | -11.5559 | -56.9432 | 2026-05-25 14:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 37b34c0d-c8b8-3cc0-9796-30d1f29dc794 | -12.8857 | -58.209 | 2026-05-25 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1cec9d44-3068-327b-9ae5-44f180452810 | -12.9049 | -58.1875 | 2026-05-25 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| aeaf45bc-1802-3eb0-805d-607032372910 | -7.8381 | -42.0552 | 2026-05-25 14:40:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 318.0 |
| f6b0ccf0-33a0-34b5-ae3e-8eadfdbf5de6 | -12.8859 | -58.1891 | 2026-05-25 14:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 262.0 |
| 10db69fc-bff7-3d4b-8422-c4f20bfe19fa | -11.3773 | -52.9496 | 2026-05-25 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 57553a00-0f1a-36dd-954c-f3d21be37bcf | -7.8191 | -42.0573 | 2026-05-25 14:40:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 554.2 |
| 249ba951-c632-34fc-93e5-5319e1228701 | -11.3584 | -52.9514 | 2026-05-25 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 5645d793-e3cd-364e-b932-1980dcecbf73 | -11.5561 | -56.9232 | 2026-05-25 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9b8b17f5-8856-3136-8b26-459cc8c4280e | -3.9594 | -43.1271 | 2026-05-25 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| a505fb58-d88b-31fa-a563-a35ca853e09f | -3.9594 | -43.1271 | 2026-05-25 14:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 096391d1-f007-382a-86dc-8cb1d2d870a2 | -7.8191 | -42.0573 | 2026-05-25 14:50:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 365.6 |
| 735a1e53-2d78-389d-84fa-a76d0863b493 | -12.8857 | -58.209 | 2026-05-25 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 9201a7a1-f301-35a3-a66d-8f00f727d53d | -7.8381 | -42.0552 | 2026-05-25 14:50:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 366.9 |
| 5b8aeed3-e832-3341-92ac-b445eff0a00f | -11.3584 | -52.9514 | 2026-05-25 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 187.1 |
| 3c6de6db-5824-3f48-b4e9-9978a9ce176d | -11.3773 | -52.9496 | 2026-05-25 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 805996f8-c06c-3895-b274-105aa90ef4d9 | -11.5561 | -56.9232 | 2026-05-25 14:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 145.3 |
| 4d9c93d6-3ffe-32bd-a3e1-b9368c94c8c0 | -6.1081 | -45.533 | 2026-05-25 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3aca9775-fd1f-3bd1-b150-9450c4cf83d5 | -12.9049 | -58.1875 | 2026-05-25 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b3e41656-021c-37d6-ac9b-bba3fd02077e | -12.8859 | -58.1891 | 2026-05-25 14:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 323.2 |
| d0ef22b5-766e-35ef-b2fc-ecccb655618f | -11.2527 | -49.6397 | 2026-05-25 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |


[Clique aqui para ver as próximas entradas](README5.md)
