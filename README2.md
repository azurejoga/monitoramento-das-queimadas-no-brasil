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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36b24e1c-e930-35fc-978b-b2cc5f94dbef | -12.0122 | -45.1929 | 2025-10-08 00:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 83b62025-f190-3fad-a589-a527663f8c74 | -17.3034 | -42.6678 | 2025-10-08 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 992ac55f-eefc-328d-8754-439b326a5dc2 | -17.982 | -57.485 | 2025-10-08 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.3 |
| 9e329870-ca49-3a36-91d5-ec3a0438ba6b | -5.1416 | -44.9443 | 2025-10-08 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 3b038e81-2061-3048-adbc-d26fded22f50 | -4.4978 | -46.3509 | 2025-10-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 7a8def90-59d5-3ac1-9fd0-ae9fa67a9771 | -3.4608 | -45.5972 | 2025-10-08 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f8dd5593-dc5f-38eb-9b82-2411b2ff3efd | -4.8371 | -45.7522 | 2025-10-08 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| a967f5e6-02c6-3d8e-8a86-f9e6803f661d | -5.1414 | -44.967 | 2025-10-08 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 302.8 |
| a56ffefa-9b42-36b7-9e2d-edfe472a55b2 | -17.284 | -42.6479 | 2025-10-08 00:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 368.5 |
| e32f4fe3-b050-3fac-82ee-7388f922c40a | -4.8557 | -45.7511 | 2025-10-08 00:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 133.7 |
| b94ebef9-4e25-3067-ae77-80fbcc40ab61 | -4.6873 | -45.8504 | 2025-10-08 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 4fcaede9-c08f-38bc-a7d1-4554936cbcc6 | -4.6875 | -45.828 | 2025-10-08 00:10:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 86edf450-b270-37e7-929e-f743cfcb9dc4 | -3.4422 | -45.598 | 2025-10-08 00:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 63d0235c-8a71-3553-ba59-a6cfa66b258c | -4.5033 | -42.862 | 2025-10-08 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3fdcceb8-af9e-35fd-8a7c-33c9a8b15dee | -7.7922 | -44.2229 | 2025-10-08 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 5c04af56-e43e-306d-bef7-2fdf7d04b3a8 | -17.9817 | -57.5056 | 2025-10-08 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 7f253757-5f8b-3754-bdac-10b0b4b15916 | -11.4534 | -50.198 | 2025-10-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| cbf0ed62-4951-3e81-af7b-02a3dc87d006 | -14.7184 | -46.0636 | 2025-10-08 00:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| da404a2a-58c3-3a09-b531-bfc583f7fedb | -4.6873 | -45.8504 | 2025-10-08 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 585c6c9f-53ef-3a98-a229-95a6bb54b18d | -5.8467 | -43.4229 | 2025-10-08 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| e93fe75b-0943-36ed-962a-0d1ed6229de9 | -4.8557 | -45.7511 | 2025-10-08 00:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 056eb582-42cb-38bc-9eb5-d8ea549d2f2e | -14.6988 | -46.0671 | 2025-10-08 00:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 01d5dadf-e9e8-37f7-9910-541f06586317 | -13.7165 | -45.7064 | 2025-10-08 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| ed0972e8-4806-39b2-ba81-26d9c34ba446 | -4.6504 | -43.2038 | 2025-10-08 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 526603e4-e42d-3342-b346-1091ab88f6c9 | -14.8442 | -48.4218 | 2025-10-08 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 508b33c7-500d-3f47-bdd8-a5a7405413db | -11.3378 | -56.1997 | 2025-10-08 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 5930d889-b056-33b1-902d-ad7bc567147a | -5.1412 | -44.9897 | 2025-10-08 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6039efbf-7533-3ee8-b679-100276a248ba | -5.8469 | -43.3995 | 2025-10-08 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 0d4695c8-740c-3ce8-aec0-045ca6e09d8e | -7.017 | -42.8762 | 2025-10-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 20a5f336-696e-3b30-a64a-ed9c2d775943 | -17.982 | -57.485 | 2025-10-08 00:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 0b68f12d-b088-33bf-adac-a84a9e922a1d | -17.3041 | -42.643 | 2025-10-08 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 642.9 |
| b8d6f9bb-9d2f-3cf4-b10a-dde7f3a5e2d6 | -12.0314 | -45.1901 | 2025-10-08 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| cb13f033-e3b1-3a19-89d7-5c8d1d1e89c7 | -3.2507 | -46.7829 | 2025-10-08 00:20:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 9a721466-e95b-3802-b65e-67c3b35a7439 | -19.8584 | -46.1569 | 2025-10-08 00:20:00 | GOES-19 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 127.4 |
| ff36bc59-eddc-307d-9121-8f260e53cd3b | -12.4538 | -54.7196 | 2025-10-08 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 71b394d7-96cf-3698-89d6-93468f08febf | -7.838 | -46.7321 | 2025-10-08 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 356e6efa-f20e-3169-9774-340998e56e38 | -4.6691 | -43.2026 | 2025-10-08 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 72f7758b-d59c-34ab-840a-8830c42a936b | -12.4536 | -54.7401 | 2025-10-08 00:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ead79fc1-4f2e-33bd-bd79-de8cfcc5b720 | -6.949 | -63.1048 | 2025-10-08 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9aa0ad1f-12d9-3f73-bc6f-4f06cb769ae7 | -12.031 | -45.2132 | 2025-10-08 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| e44c89ec-9096-3e4c-bb62-e1e1c9b18fb5 | -4.6505 | -43.1805 | 2025-10-08 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| bf1ea0ce-5870-317a-86fe-2a0d789de538 | -7.0167 | -42.8998 | 2025-10-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 01b5f833-aa1b-326a-afb4-2b28eb36e721 | -3.4608 | -45.5972 | 2025-10-08 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e018e33b-ec33-3b60-bd24-8e3925fa3202 | -12.0036 | -46.7667 | 2025-10-08 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7d65c9ed-acec-35f4-9a2f-3af5adcd7996 | -11.4531 | -50.2195 | 2025-10-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 258835b9-49f3-3a0a-bda1-3f99f4aa4f52 | -17.3048 | -42.6182 | 2025-10-08 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 30429708-eed7-3844-a6d1-e95cc7991b76 | -14.7179 | -46.0867 | 2025-10-08 00:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 611d940a-e09d-3936-a0e9-8b944ab77ceb | -13.7364 | -45.68 | 2025-10-08 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 4b297790-2cff-3025-a3e2-53b88bbd835c | -12.3159 | -55.1008 | 2025-10-08 00:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 4ca927ef-627d-3683-a6be-67fe835469d0 | -5.8657 | -43.3981 | 2025-10-08 00:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b26b2b86-1804-3fb6-be69-0776f37224e3 | -3.7937 | -49.4211 | 2025-10-08 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 40dec0b6-d8c2-3e51-885f-ec2e6658cb12 | -5.1227 | -44.9682 | 2025-10-08 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 5ca59fbf-7cdb-360a-85da-f8638d69b786 | -13.7169 | -45.6833 | 2025-10-08 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 0e4412ed-b44e-373a-b7a7-03e60180c19d | -14.6983 | -46.0902 | 2025-10-08 00:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 558a5333-49ae-3a9d-bfee-969d74578e0f | -4.6692 | -43.1793 | 2025-10-08 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f6135fd0-2124-375c-94d4-c46c9856608c | -10.3729 | -50.2722 | 2025-10-08 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 79ddc3d2-f2d4-3b0d-8fde-a73e7db5471c | -17.2833 | -42.6727 | 2025-10-08 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 134.0 |
| d8599a35-d676-329d-b236-5f3a288259d8 | -5.2601 | -44.1368 | 2025-10-08 00:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 47874106-511e-3c48-b5f6-265461dd2ac4 | -5.1416 | -44.9443 | 2025-10-08 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 172.6 |
| b1771404-12bc-3e28-8eec-adfa7853e9b1 | -9.4154 | -61.8928 | 2025-10-08 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0600e1d7-0099-3a1e-8014-a2b844afb00f | -4.5033 | -42.862 | 2025-10-08 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 414a0a98-66d8-39be-87ce-c642b6f2b382 | -12.2969 | -55.1026 | 2025-10-08 00:20:00 | GOES-19 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c1eaaa45-1942-3f14-9c59-bbba515df25a | -17.3034 | -42.6678 | 2025-10-08 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d7c7b4c8-d333-33b2-ae3c-dc0e4b25aec7 | -11.434 | -50.2216 | 2025-10-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 8a171ddb-83b2-3e1d-90fc-2c8a48a66a0e | -7.8193 | -46.7338 | 2025-10-08 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b4b51940-1cab-3c7c-888d-cc2a75dcb531 | -4.4978 | -46.3509 | 2025-10-08 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 51d3bb01-b112-3725-a069-452fbccf33d8 | -5.1414 | -44.967 | 2025-10-08 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 334.3 |
| 06cee35e-42aa-3126-aed9-b30951213c43 | -17.284 | -42.6479 | 2025-10-08 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1048.6 |
| 98ce8d4d-651c-3b48-b1ef-d5c9ac99c86c | -13.7359 | -45.7031 | 2025-10-08 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e6c75ce6-7ecb-3fff-8bd3-bc7837eb1834 | -4.4977 | -46.3731 | 2025-10-08 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1fc005f3-b775-381e-8576-48ee4f3f6574 | -17.2847 | -42.623 | 2025-10-08 00:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 147b2229-f172-3f40-81c7-b6b99a0666f8 | -6.9982 | -42.878 | 2025-10-08 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 15b29dba-252d-367a-a2b8-5a76257e34c0 | -11.4344 | -50.2001 | 2025-10-08 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f9213e9f-eef8-3625-964a-ef993b09e448 | -3.4422 | -45.598 | 2025-10-08 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| e7fb1e8b-7013-3e91-a8df-b38ae46b5c16 | -4.6875 | -45.828 | 2025-10-08 00:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 104.0 |
| f5b0d322-d4aa-366c-ac0e-0002c15acfbb | -5.2601 | -44.1368 | 2025-10-08 00:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 50c7b9c8-ee1c-340c-ac08-fe22843f4da1 | -5.1227 | -44.9682 | 2025-10-08 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 2088b988-6c2b-3bd6-bfda-5e1c1ea9f0a0 | -7.0167 | -42.8998 | 2025-10-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| c0e8dced-8b98-3dd3-9eb0-d8bafca621a5 | -4.6505 | -43.1805 | 2025-10-08 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 35c92632-ec1c-3395-b0a1-07a74f28ed3f | -17.8157 | -40.1897 | 2025-10-08 00:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 81623434-205c-387a-be8e-1672a8c80d99 | -10.911 | -51.0249 | 2025-10-08 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4917d632-e003-3e08-94fa-25ce1924aa5d | -5.1412 | -44.9897 | 2025-10-08 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 10823dc7-1f98-312f-95ef-527902dcb63e | -11.4531 | -50.2195 | 2025-10-08 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 6c30d90c-d916-36ca-a5fb-1c5ff9c5ffeb | -11.4344 | -50.2001 | 2025-10-08 00:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 85901485-8cef-32ea-a412-18186c6093bc | -17.8359 | -40.1841 | 2025-10-08 00:30:00 | GOES-19 | SERRA DOS AIMORÉS | MINAS GERAIS | Brasil | 3166709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.1 |
| 455844db-b51f-3a93-ab07-247b513793a2 | -11.6888 | -50.9833 | 2025-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 4758fe40-81bd-374a-966b-a6cf52dc2634 | -14.7179 | -46.0867 | 2025-10-08 00:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| d669da01-aa5b-30b2-b256-0377e55753f2 | -4.8557 | -45.7511 | 2025-10-08 00:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 59259dd9-de59-3318-9c98-c7ea6490e6a7 | -9.6295 | -40.3392 | 2025-10-08 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 7053eb01-7d61-301d-a19d-018a9bb0e57b | -11.6698 | -50.9854 | 2025-10-08 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 166.2 |
| b5daf5c9-c49b-3c6f-baa0-0455b91a60ed | -4.6875 | -45.828 | 2025-10-08 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 8432a95a-3095-3954-9916-c49c5d4eff0e | -4.4977 | -46.3731 | 2025-10-08 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 381d8617-0142-3e69-8466-049aa328781e | -4.4978 | -46.3509 | 2025-10-08 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 9858d66e-9872-3bff-9c36-665f8f3697b2 | -13.7169 | -45.6833 | 2025-10-08 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 91c747e9-2ef3-3203-b134-9d9334bd9c37 | -7.017 | -42.8762 | 2025-10-08 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.1 |
| 982c6ca1-f342-3689-bacc-9d6a08debf7d | -4.6692 | -43.1793 | 2025-10-08 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a9808929-c096-3359-8cac-16d7dc85992e | -12.3971 | -63.8811 | 2025-10-08 00:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6a6ece30-4bb7-3cf0-9078-8158f2ebba06 | -4.6873 | -45.8504 | 2025-10-08 00:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2ec680dd-cead-38d3-b7c6-dd4d21cc71b1 | -14.6983 | -46.0902 | 2025-10-08 00:30:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f8aa4913-d9c6-38b3-afb6-5f497d8d847f | -3.4608 | -45.5972 | 2025-10-08 00:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |


[Clique aqui para ver as próximas entradas](README3.md)
