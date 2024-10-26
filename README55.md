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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e9a2c9b-742c-3b41-944a-4fc4a3d25bfd | -4.34473 | -55.36216 | 2024-10-26 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d2f4ae2-c88e-349f-803f-d5bb7768b326 | -9.99924 | -56.24888 | 2024-10-26 04:19:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 920d44a1-7d41-3f23-9195-5ae77c658755 | -9.99336 | -56.24763 | 2024-10-26 04:19:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66c72fe6-309c-37e8-903d-8267fc10d2e9 | -9.86772 | -55.41297 | 2024-10-26 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fe2f2f4-daf6-3cc6-9eff-3c6d1dae1fa0 | -11.16767 | -56.28966 | 2024-10-26 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1140c2b-7303-3af3-b981-bfbdcdfda97e | -11.16185 | -56.28865 | 2024-10-26 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee980d36-b03b-39a5-9d88-78e0326c92f8 | 1.57207 | -55.64001 | 2024-10-26 04:19:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e9e575-bfa7-3ff2-8c69-c4d871059eed | 1.57066 | -55.64086 | 2024-10-26 04:19:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1d16476-e092-3d47-bb74-d713de0d4ba7 | 1.56528 | -55.6411 | 2024-10-26 04:19:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a7e48a7-5e9f-3607-98c5-d2badda2222e | 1.56386 | -55.6419 | 2024-10-26 04:19:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4deedbc2-6f60-3a79-8ddd-cb2a491c609e | -8.77464 | -44.72911 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d71717b1-bdc5-3bd1-b60f-799a0cc12606 | -5.85435 | -50.35465 | 2024-10-26 04:19:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81e661e0-67a6-3453-9bbf-7e0a5936bb85 | -5.07752 | -56.22653 | 2024-10-26 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 731f2cab-3991-3e00-835e-ed5eb3c0640b | -5.07111 | -56.22549 | 2024-10-26 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dac2f0b-b1ee-38ed-bfb3-81f27da2bf8d | -5.25676 | -55.96441 | 2024-10-26 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96ce8530-d49b-354b-948c-cfa0c5772eb4 | -5.25052 | -55.96314 | 2024-10-26 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c9fc677-3f6c-3f4e-bf28-6ba0c451cdbf | -5.24963 | -55.96816 | 2024-10-26 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40b9e2b2-dcef-3d40-860c-87ea23f885a8 | -5.24337 | -55.967 | 2024-10-26 04:19:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18bb30f7-1c5d-3b19-b8e4-30fb102293b8 | -18.046 | -57.35228 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 87e13fab-f25b-3a6b-9a9b-c9b707bf71b5 | -18.04591 | -57.37954 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 31a78ecf-ea3d-3227-bd06-8b8509e3e6fa | -18.04222 | -57.31656 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a93598e6-04aa-33c4-b888-85e46a780c12 | -18.04143 | -57.32023 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b028eec2-5b46-37c3-9ca4-4f13f4de64f6 | -18.04135 | -57.34731 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3ff5f727-bd1e-342c-92fc-8cef205bfc78 | -18.04056 | -57.35099 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 25d27005-4fca-39e3-87cf-d126ab97349e | -18.04046 | -57.37826 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 40e68bdb-ac57-34ea-bb3c-df6aa9ea11e7 | -18.03599 | -57.31897 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0ee54bb3-6f0f-3c3a-9e9e-959e19c41c8f | -18.03591 | -57.34601 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 871afa1c-918c-33ed-8b2e-c7c4a2bd3cd7 | -18.01891 | -57.31878 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 52226a2d-0d13-3b25-a51c-9729125ec3ce | -18.01859 | -57.31897 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ab93eb50-24e0-321f-8465-eadce70c1f3f | -18.01812 | -57.32246 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 53644a1a-2ffd-3dd2-aaee-d38d8136e26e | -18.01792 | -57.37722 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 79b8e6d4-a1c3-3596-ac92-fbf99a8a1a97 | -18.01785 | -57.37683 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4d1f7f89-3b61-3143-8de3-bace809c10b0 | -18.01783 | -57.32266 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9fa10a14-b933-36a6-be63-a9e614bb6d30 | -18.01732 | -57.32616 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bf84d2d3-460e-3fdb-a0f7-ab2de68ef9d9 | -18.01706 | -57.32637 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d8a3db68-9070-3079-b241-1576a3ca79b4 | -17.81925 | -57.5622 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0a4b082f-3803-3652-882c-6101247d0a22 | -17.81843 | -57.56606 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ee4d4faf-12d7-3d3a-ae6a-6b9f45f52616 | -17.81434 | -57.58537 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1f3b25be-38b4-3343-8ad1-250a4353cd3d | -17.81352 | -57.58924 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7116af40-5b3a-389f-a1f1-c01b2d0bcc55 | -17.8127 | -57.59309 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2ba1649d-f971-3666-9413-d05eebc4fab6 | -19.76816 | -45.65463 | 2024-10-26 04:21:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8f4f2db-a4b3-33b5-bc7e-f4b8d0faa4cd | -18.61684 | -46.92824 | 2024-10-26 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43ffb5ed-dd3a-3ebe-bf9b-895f01f52187 | -18.61627 | -46.93189 | 2024-10-26 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07c26a63-354b-3066-88e5-e1597cb77794 | -16.54186 | -47.8484 | 2024-10-26 04:21:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89ef8bf2-fcf2-3001-81d8-72e6004ff0cb | -16.04344 | -43.7257 | 2024-10-26 04:21:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a149f0de-48de-3a3b-870c-29f75b37c834 | -16.03984 | -43.72517 | 2024-10-26 04:21:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0200a24-742a-3d95-9d83-3aa2e383c64a | -15.96071 | -43.55309 | 2024-10-26 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e8a67ac-6159-3a45-9c6e-fd38c15fddd4 | -15.96009 | -43.55741 | 2024-10-26 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76e60fbf-e470-3e68-aa06-265d0182ffc3 | -15.77703 | -43.06433 | 2024-10-26 04:21:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea611722-21ad-3bed-8b9e-add6409f12f9 | -15.76654 | -49.24744 | 2024-10-26 04:21:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9142f01-dc5d-31e8-bd57-4e9e299f602e | -18.0282 | -57.3287 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 38c61622-8f93-3260-8f17-932eff920fb4 | -18.30797 | -56.1805 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8b6ed025-eb8a-35f9-a03c-370a7abb697f | -18.30294 | -56.17935 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7d7b23c7-c079-3b92-8861-3d0a5024035d | -17.9468 | -57.55185 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 95c2ba62-0bb5-30ec-8072-e661a5ac2a95 | -17.9461 | -57.55515 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8e7e0021-3dda-3125-9415-32ddf436098c | -17.94127 | -57.55062 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aa64ebc2-aa33-39ae-a160-8d0922d34b95 | -17.94066 | -57.55347 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 62b82dcc-d504-3693-971f-addace157446 | -17.93764 | -57.54039 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8328fddd-dec5-3876-b587-16f0ab3c6e1f | -17.93717 | -57.56998 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b43b9c1a-889c-30fc-ac0d-a72ae1785a2c | -17.93696 | -57.54359 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 1464cd7c-9527-3d99-b8a1-4421fb3d5071 | -17.87166 | -57.52373 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ab496c69-5054-3558-9efd-acb2da7ad6fb | -17.87091 | -57.52721 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ef5583bf-3568-3641-bde7-a5b363744b06 | -17.8702 | -57.56858 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0b7a4b35-8af1-3e61-aa1d-5a82e9e2d044 | -14.55358 | -42.9786 | 2024-10-26 04:21:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65582dac-9fb5-3de4-b97a-fd018a4841a2 | -14.5499 | -42.9781 | 2024-10-26 04:21:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9ea948a2-ff69-325d-b39e-a9a22bcc16af | -13.29368 | -49.57914 | 2024-10-26 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4cfd31e7-1112-3cb4-b7cf-a4b781f87132 | -19.23971 | -40.02306 | 2024-10-26 04:21:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4dbce1b5-702d-37ac-8215-7f868970d6bb | -19.23891 | -40.0219 | 2024-10-26 04:21:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b7fee214-5b68-356c-b148-63e553b79dd0 | -19.17327 | -40.13393 | 2024-10-26 04:21:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 14ddc778-1bba-3216-bab5-74ab285dcf45 | -15.6147 | -40.78674 | 2024-10-26 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a206696c-ac7a-3103-a56d-15cd5ee71f58 | -15.61395 | -40.78507 | 2024-10-26 04:21:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8c145dff-7473-3cab-bd33-f3065ac0b1f1 | -15.5845 | -40.44696 | 2024-10-26 04:21:00 | NPP-375D | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ec62485-b3de-3b6e-b1e0-0905ec1e035f | -17.81011 | -41.06377 | 2024-10-26 04:21:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2edf2917-2f22-3011-b91e-3413850251b0 | -17.80577 | -41.06345 | 2024-10-26 04:21:00 | NPP-375D | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e6dd0cf-8bf7-3aac-bd05-a2f002d15edd | -17.21487 | -41.1588 | 2024-10-26 04:21:00 | NPP-375D | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1ee9322d-dfff-34f2-957d-70cca4fa23af | -20.7259 | -40.60146 | 2024-10-26 04:21:00 | NPP-375D | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0610f9ac-c7ef-3265-bc68-95c6a97fb2e4 | -14.76838 | -41.61585 | 2024-10-26 04:21:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46e501e8-f62a-3cbd-80b0-948634d20ee7 | -16.54041 | -41.63175 | 2024-10-26 04:21:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce9a0072-29a6-31f2-ac17-8da793eb9499 | -16.02486 | -41.18989 | 2024-10-26 04:21:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fc01e155-049e-3701-9f45-ba4706f1c647 | -16.02121 | -41.18529 | 2024-10-26 04:21:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 46ad1adf-caba-3885-9d65-308744ac1ad3 | -16.02073 | -41.18902 | 2024-10-26 04:21:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ca7b8048-1c3e-36d8-884c-a62d63910443 | -15.32012 | -41.74805 | 2024-10-26 04:21:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1d4aef86-8f96-32fb-abfd-c342adec55d9 | -18.08851 | -41.83525 | 2024-10-26 04:21:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74b4b402-5593-3adb-b337-1856832ba564 | -17.77497 | -42.25747 | 2024-10-26 04:21:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 184880f9-079f-3d24-b1d7-d50950f216b3 | -17.77331 | -42.25595 | 2024-10-26 04:21:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ff494efb-6bb1-3fb9-82f6-7daa6edccf59 | -17.68574 | -42.11065 | 2024-10-26 04:21:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9a3e1f64-10ff-32d9-baa7-0b557ccebc2b | -17.68502 | -42.116 | 2024-10-26 04:21:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c04c2d0b-b22c-3bb6-9797-4383be54c533 | -17.32224 | -41.39342 | 2024-10-26 04:21:00 | NPP-375D | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 10899ce2-5937-3f21-8790-a290b25499dd | -18.16044 | -42.45023 | 2024-10-26 04:21:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4effcd12-7492-3878-a221-728d7f935641 | -18.12672 | -42.24223 | 2024-10-26 04:21:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 35ebf83b-c314-3627-b13a-17432d5b418d | -20.8509 | -42.88965 | 2024-10-26 04:21:00 | NPP-375D | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ef3c92be-2e87-36e0-87f3-3acd0ab2e810 | -20.41673 | -43.5517 | 2024-10-26 04:21:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a16ee9d-297e-301e-b037-b35bab8312d6 | -14.66444 | -43.10822 | 2024-10-26 04:21:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4a12c979-dd44-3d11-b359-586bf00db51d | -14.44485 | -42.44608 | 2024-10-26 04:21:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 12b85b4e-6f8f-3c48-9d82-125131c6915f | -14.12418 | -42.65137 | 2024-10-26 04:21:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c7010b4-6b65-3e55-87b4-f4a3f19bc6ee | -15.60809 | -43.73026 | 2024-10-26 04:21:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c5440df-0788-318a-aa14-bf640263053c | -15.57046 | -43.76296 | 2024-10-26 04:21:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5913cf78-ba3c-3da9-af4f-72831444c074 | -15.56986 | -43.76715 | 2024-10-26 04:21:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e005d583-7695-3199-b6d0-82f0857941dc | -15.30249 | -43.70905 | 2024-10-26 04:21:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bb6e7b88-2dba-306c-a93d-1887293a773a | -15.26954 | -43.05846 | 2024-10-26 04:21:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README56.md)
