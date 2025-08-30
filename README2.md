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
| 6d9f6382-3890-327f-9a5f-d585432bf51f | -9.0799 | -65.4349 | 2025-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bf5e970e-3e2d-3001-8e69-acab3b78d43c | -9.7044 | -49.4609 | 2025-08-30 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 7a1a638d-287c-3486-92f1-cea2dab28704 | -9.7041 | -49.4825 | 2025-08-30 00:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| f3a0e71c-0610-356f-a93e-82069cca7308 | -7.8895 | -63.0171 | 2025-08-30 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b21ac661-efb7-39b4-b708-6edcc9857af1 | -14.0118 | -44.5614 | 2025-08-30 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3525f134-bb96-38fb-adf8-edfdb0ad40a5 | -8.5551 | -63.0303 | 2025-08-30 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 0ad25719-6dc9-3e14-a853-b47974abd941 | -5.6083 | -44.9811 | 2025-08-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| fc953ae1-6040-3bdb-8972-87b017adc2e6 | -9.4311 | -62.3493 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| fae1456f-97b9-3933-8d99-995715a0b2e4 | -9.0614 | -65.4355 | 2025-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 153.6 |
| dedf0061-47ef-34c5-8f69-50df690c05d2 | -5.6266 | -45.0252 | 2025-08-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| e638004d-c04e-3ed2-a9ee-a9c7ab47fa31 | -5.6079 | -45.0265 | 2025-08-30 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a3b6f77a-241c-35e7-b90f-8d2eca9f2f19 | -8.894 | -62.1066 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 114.6 |
| b2539cf8-f604-3445-b3a2-19da4fcc3eb7 | -7.7257 | -50.2751 | 2025-08-30 00:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 414e7cb7-987f-38e6-a5de-9592b76e7b33 | -9.4497 | -62.3485 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 111b29f3-7dc9-3fca-8510-fb8a38607d23 | -13.4019 | -46.9667 | 2025-08-30 00:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| fb79b576-e6c2-34f1-8cdf-940b50d78836 | -6.0033 | -44.7247 | 2025-08-30 00:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 6a176565-0ce4-3221-b6ca-850eb6dae805 | -7.9081 | -62.9976 | 2025-08-30 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3158bcca-5f21-3f5f-9aad-f712cbce42af | -7.908 | -63.0164 | 2025-08-30 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| e98e8000-a97f-3c5f-bab2-e2cc91bd9880 | -9.1155 | -65.7699 | 2025-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| aa4121e2-2bf6-34ad-813b-adc317cd3ab4 | -8.8941 | -62.0876 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7352c21e-519f-3eab-9fc8-50cd187124ab | -8.9126 | -62.1058 | 2025-08-30 00:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 2e0d445f-d3b5-37ac-91fd-22616f9ae1aa | -11.8564 | -46.426 | 2025-08-30 00:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 562c8d0b-c701-3643-8e4c-9108934830b6 | -14.0113 | -44.5849 | 2025-08-30 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1745b3ed-4fc1-375a-85c9-7990a5a4bb71 | -9.0613 | -65.4542 | 2025-08-30 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 9dbeba91-ae84-3566-a497-536183b6f32a | -11.367 | -63.2472 | 2025-08-30 00:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 1289c23b-4b95-3377-8942-f01a54f2c07a | -7.908 | -63.0164 | 2025-08-30 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 4f0963ff-10f6-3e0f-8f96-a57c23426493 | -11.8564 | -46.426 | 2025-08-30 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0be0bbdd-97f2-33c2-a10e-02da38d47686 | -9.0799 | -65.4536 | 2025-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5f7d80f7-f2e4-335c-934a-1a5d7d26b82c | -13.3628 | -46.9953 | 2025-08-30 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 862a17f7-a67f-3e54-8039-5489150d0242 | -9.0613 | -65.4542 | 2025-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 45cd305a-7a65-38d3-b094-f8ac824fe515 | -13.4019 | -46.9667 | 2025-08-30 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 81409878-1243-3265-9e1e-b19abb1497b3 | -6.0033 | -44.7247 | 2025-08-30 00:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 66c3346a-9840-3be7-949e-452c792b514d | -8.9126 | -62.1058 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 115.5 |
| eea68a27-6763-3a51-b6cb-1a0f9f2188c0 | -13.3817 | -47.015 | 2025-08-30 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3fb15a33-1b02-3c3d-afe7-e36aa2a2e0b5 | -11.3321 | -43.5926 | 2025-08-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| aba34261-af9a-30f0-8d4b-415d8701ac40 | -11.3513 | -43.5897 | 2025-08-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c47ae78e-2241-34c9-b513-5ff98cb16a91 | -7.7257 | -50.2751 | 2025-08-30 00:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 64d3bfca-895d-3c45-82eb-b851a2ac5f0e | -7.9081 | -62.9976 | 2025-08-30 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 863f5c39-fd3b-3adb-988f-4c9bf08c1aa5 | -13.3821 | -46.9924 | 2025-08-30 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 193.6 |
| 1b8912f5-3a29-32e6-b84a-a9564461b342 | -11.8764 | -46.378 | 2025-08-30 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 3a372c36-4e95-38b7-ada9-e1ca728f52f3 | -7.8895 | -63.0171 | 2025-08-30 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0002c5bb-b341-37c5-946d-c0ed45aabcf4 | -9.4497 | -62.3485 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 3377e84b-04b6-3b23-88cd-b8a64be750fa | -9.4498 | -62.3294 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 173.9 |
| 349d3c30-c51e-3288-aa48-fd9cf908937e | -11.3709 | -43.5631 | 2025-08-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 555acf2a-df3e-398d-b084-ab66fed0d050 | -11.8768 | -46.3553 | 2025-08-30 00:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 8f8bcc2b-c72c-3ccc-84c4-c3191ecfdbfb | -8.8843 | -60.7315 | 2025-08-30 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f6db4207-26a9-3f5e-9483-1663b4ada9a5 | -7.8896 | -62.9982 | 2025-08-30 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 659addf2-5527-3fdd-8977-38fad0922879 | -9.4495 | -62.3675 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| dd41d8d0-7e73-37f0-a9c1-ff516490f0c9 | -13.4014 | -46.9894 | 2025-08-30 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 31c31f40-a39c-38f2-8b30-517029b8097f | -8.5551 | -63.0303 | 2025-08-30 00:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 4122c2c0-5b09-3bc2-b0f7-599b703d371d | -9.0799 | -65.4349 | 2025-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 30f74166-031a-3084-827a-93836a4b65ef | -9.7041 | -49.4825 | 2025-08-30 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| acca4ce9-0298-3d2c-869c-c5ba3fd2ad38 | -9.0614 | -65.4355 | 2025-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 0e7c9394-243f-30c5-b384-730e8ce7eebd | -5.6081 | -45.0038 | 2025-08-30 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| dcd26724-2dd9-3ce4-b6eb-d47c57684045 | -13.9918 | -44.5884 | 2025-08-30 00:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 73a91690-38a8-3277-9aa6-67247a15443f | -11.8572 | -46.3807 | 2025-08-30 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| cc3fd263-8b3d-3e2f-8e4b-1adb675d819b | -9.1156 | -65.7513 | 2025-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3dca8fb7-5b3e-3cdd-a876-236fddd5e8ed | -11.3517 | -43.566 | 2025-08-30 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7947b193-4ad8-36f7-b420-f7200da3415a | -11.8568 | -46.4034 | 2025-08-30 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 595b8129-a216-34dd-bd0d-77ca44d256c2 | -13.0154 | -56.8982 | 2025-08-30 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 6297052a-2382-3ada-a520-7cfa6c3cda20 | -9.1714 | -59.5793 | 2025-08-30 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 525c2a7e-4a52-3fa0-bc9e-c588f99c5a84 | -9.7044 | -49.4609 | 2025-08-30 00:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ec88f75a-970c-32f9-827d-9e13eef424ac | -9.4312 | -62.3303 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| cc56381e-6f8d-31b0-be64-beb6ee26be05 | -5.6268 | -45.0025 | 2025-08-30 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| e50b6b9a-d6d3-3311-ab0f-0e436c1ba4d9 | -9.1155 | -65.7699 | 2025-08-30 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| a9af39d3-d65b-3547-8746-4f53bde83700 | -9.4311 | -62.3493 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 856ff3f2-98d2-3a11-97f6-f0d521d0a030 | -13.3825 | -46.9697 | 2025-08-30 00:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 92.7 |
| bb0649b2-b64b-38fd-bbdd-9c89476df216 | -8.894 | -62.1066 | 2025-08-30 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 9cd0c00b-843d-3fad-94ed-93bdbf7e308a | -7.908 | -63.0164 | 2025-08-30 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| b656c8de-debb-3a81-9f35-ca0192483787 | -13.6295 | -48.1874 | 2025-08-30 00:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| e8428940-2c32-30b1-af0e-cb440a5870b2 | -13.3825 | -46.9697 | 2025-08-30 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 5e5b333c-9cd5-38e8-b2bd-71a0e00b599e | -8.8843 | -60.7315 | 2025-08-30 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 522cd808-5a65-35e9-a7d1-c633f994b4e8 | -9.7041 | -49.4825 | 2025-08-30 00:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 47e7391f-dc65-3daa-bf9f-c6264a2df0ef | -6.0033 | -44.7247 | 2025-08-30 00:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 966882c2-d7bf-3b5b-92b5-4132223d6367 | -9.1156 | -65.7513 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 930cf038-4b6d-3fa3-8f19-8fe55944c7a3 | -13.3821 | -46.9924 | 2025-08-30 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 209.4 |
| ca8b369a-db90-3fbf-b163-d44d3118a200 | -8.5551 | -63.0303 | 2025-08-30 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2d07fd3a-2a54-30bd-8b2e-c2fc54715c96 | -9.0613 | -65.4542 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 342512a0-649f-3504-b160-b72964de3e81 | -11.3321 | -43.5926 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 98991977-df7a-3df2-b95f-acc69e66364f | -5.6081 | -45.0038 | 2025-08-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 306.6 |
| 2eacfa55-214a-3735-8f7f-b554cd38181f | -11.3125 | -43.6191 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9589b468-7254-32a4-be28-f25e7803384d | -5.6079 | -45.0265 | 2025-08-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| f7ee84d6-ff7f-310a-8bb7-416fddb57a7d | -9.0614 | -65.4355 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| d95c5d60-035e-34d5-85ea-d856a18bb00e | -12.0153 | -43.9818 | 2025-08-30 00:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 0f828c4f-07a8-3b8f-90f1-8443175cfb04 | -13.6488 | -48.1845 | 2025-08-30 00:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 8942eca0-bacd-3e65-a2ca-ae0e0238589b | -5.6268 | -45.0025 | 2025-08-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 441fbc26-e9af-39a1-99ea-883d3d808b89 | -13.3817 | -47.015 | 2025-08-30 00:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 193e19e1-6e6c-3c51-b6eb-dc6ce96e9d1e | -8.8842 | -60.7507 | 2025-08-30 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ae6cbcad-4ab6-332f-b6ab-987ff3a30b7a | -7.9081 | -62.9976 | 2025-08-30 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 7bd391dd-2c63-35ee-9a81-3d8b1af4e61e | -8.9126 | -62.1058 | 2025-08-30 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 5d78c1ef-a39c-31d0-b7f7-37e30d9211e4 | -8.8658 | -60.7324 | 2025-08-30 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| ce7091c7-a42f-3bcf-af25-1a165c6ddf30 | -11.312 | -43.6428 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 604c1d8f-b8ae-3b09-904c-b6d16fc308fc | -11.367 | -63.2472 | 2025-08-30 00:40:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| a9750455-9099-322b-b2bc-b93f09aef8b7 | -9.0799 | -65.4349 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f90e7d40-90e3-32e0-8158-eaa26a98e7ac | -9.0969 | -65.7705 | 2025-08-30 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 87b6b260-ef44-3d6b-97f6-f82ffd35f5c0 | -11.3317 | -43.6162 | 2025-08-30 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| abee3687-641a-3fdf-b14c-0ceeae9afa36 | -8.894 | -62.1066 | 2025-08-30 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 77a5a540-c652-39b7-9a52-0fd938c6b762 | -5.6083 | -44.9811 | 2025-08-30 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 8df11192-d8a1-3acb-b6e7-02f9e2a0ef58 | -11.8764 | -46.378 | 2025-08-30 00:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 26a375a3-e5d5-3191-aa6e-4836a66915da | -11.8768 | -46.3553 | 2025-08-30 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |


[Clique aqui para ver as próximas entradas](README3.md)
