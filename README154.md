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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf7ea34-a23c-35f9-a915-44ed29af56cb | -3.1514 | -58.644 | 2026-09-22 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 49fbaac1-3b42-34bf-b811-be922e3ef2b4 | -3.3309 | -59.8673 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| e1ff76d8-4511-3824-a364-74711afaa194 | -8.1686 | -54.7634 | 2026-09-22 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1fdd17ac-e09e-3d64-adcc-3485424b45b6 | -8.7706 | -45.8567 | 2026-09-22 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 99bfe0c3-eb95-31dc-a3eb-e1db5a8d9602 | -11.5116 | -45.3581 | 2026-09-22 15:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 64dc7e85-6d93-39e3-976b-6d5f41318766 | 1.5836 | -55.7856 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8da1c2ec-4aea-3011-a505-ba113f1c0221 | -3.4186 | -61.2895 | 2026-09-22 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cbef7b43-0aea-3e93-8fdd-1542ea576fd0 | -3.1851 | -59.6982 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 7a97890b-4fc2-3627-acd4-32ce33306d12 | -3.3494 | -59.8097 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0063ec6f-505d-391f-b730-9a6aa9c90e10 | -1.0243 | -48.83 | 2026-09-22 15:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 89615d97-0595-3c5d-953a-6567d81fe788 | -6.1362 | -59.8871 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b47ca244-8295-3dc3-b40e-95f9dd780d69 | -3.2817 | -57.8685 | 2026-09-22 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 77d9fbaf-e017-3333-9217-3fccc7b96520 | -3.0616 | -58.0086 | 2026-09-22 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7fdce500-7925-3c55-9ef3-873efbe6ab1e | 3.0199 | -59.9683 | 2026-09-22 15:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5d5689b7-3080-3068-bab4-0d897e8def89 | 1.3634 | -56.0834 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 36d99a73-a07b-3560-aef1-9f6da9110e22 | 1.3634 | -56.0638 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| dba90092-a548-3a83-b42d-74a428ff8757 | -6.3383 | -59.9374 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7aea9db7-b02f-3571-b96f-eef90e3c4447 | -6.8017 | -59.4394 | 2026-09-22 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 86e1d688-7662-37d7-857d-b83e0d8b1fb2 | -3.331 | -59.8483 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 9a05ce98-3d2c-3565-88a7-702501a91b0e | 3.0199 | -59.9874 | 2026-09-22 15:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a35d0871-ce04-3274-b0d2-ceab7ebf39cb | -10.3921 | -50.2488 | 2026-09-22 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 91ee5b60-3f6d-3ca5-b29a-de7d969236ce | -3.6264 | -58.9228 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 187.1 |
| e26269e0-ea00-3ab8-8494-0b3cf1642124 | 1.4269 | -50.7657 | 2026-09-22 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f9404e06-72c5-3344-b7be-f05911b21bb8 | -6.1111 | -57.6645 | 2026-09-22 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 34ce27a7-da11-3834-89fa-ab222e9e1b0f | -6.7463 | -59.4416 | 2026-09-22 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 88cdf1ac-b7c9-38d7-aa73-edd746589e41 | -3.3311 | -59.8101 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0ea5fbc2-2b4c-3dac-9ebd-66fa83421bc3 | -10.6535 | -58.7698 | 2026-09-22 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 7a619692-d562-33ed-8530-bd37700a49e4 | -6.4487 | -59.9526 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a9c012d7-9d86-3fbd-b55a-e96e15ed50ec | 1.39 | -50.7662 | 2026-09-22 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2dd1b660-d0fa-39ce-89ca-52f10e758c51 | 4.0579 | -61.4095 | 2026-09-22 15:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b74ecfbc-ca7a-3014-ab37-fb1e0a5242f3 | -6.0925 | -57.6847 | 2026-09-22 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 291.0 |
| 79a89c6f-7e09-3408-97e1-6502d656d179 | -10.43 | -50.2449 | 2026-09-22 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a99e1289-003e-3b8b-9fd6-919f9de415d7 | -2.4023 | -58.2715 | 2026-09-22 15:50:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1aac04c6-a641-39f9-9bba-35a76791aec3 | 2.206 | -55.9938 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 25fc9781-3ead-3cda-937a-d9a37b27f839 | -2.4023 | -58.2908 | 2026-09-22 15:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| bb1a3fc3-d55f-3931-a35b-8c6283f9653e | 2.6715 | -60.6012 | 2026-09-22 15:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 26721690-8d52-39da-8418-e97478f13e74 | -3.6264 | -58.9036 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| cd93cb87-6ede-32d5-bb8a-4db6a45e35f1 | -3.1903 | -57.8316 | 2026-09-22 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 00519468-3b3c-37bb-97f4-7deebed8153a | -3.6814 | -58.9023 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a72ac18e-2296-3ee6-b5b8-caf396a4242c | -9.257 | -46.1873 | 2026-09-22 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| acb5f7c1-4525-3fc7-9def-20d1e268d6c8 | -3.3001 | -57.8487 | 2026-09-22 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 98e1759e-0332-351e-9f93-57493acd11a8 | -3.8645 | -58.8981 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 31ff21da-a2bd-300c-96ca-0e5c6caa4683 | -5.4363 | -60.2161 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 29367d89-36bf-3a5b-9e0c-58e5f5832442 | -11.3784 | -44.2195 | 2026-09-22 15:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 54588350-b3cc-319e-ac98-c3e444dfe77e | 1.5099 | -56.0426 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ae35fdc8-0ec7-3b32-91ef-ea77aeaa98c0 | -3.6813 | -58.9216 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 322fd09d-5a76-3f0e-b9ac-129a7dcddbac | -6.2832 | -59.9202 | 2026-09-22 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b192f3b2-84ab-3bea-9182-a10b6c8bb862 | 1.5287 | -55.7468 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 59c47b21-a57c-3a4f-8f10-daae8c18cce1 | -3.6763 | -60.5839 | 2026-09-22 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 50b0c71b-3696-3ea4-9437-c0d924a93e62 | -2.6783 | -57.5893 | 2026-09-22 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d3b06815-03c8-36e3-b7a3-85c8c6b01771 | -6.8796 | -41.6995 | 2026-09-22 15:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 381.6 |
| 6c66b443-b51f-32ce-9b2e-2134f33ec79d | -9.788 | -46.0819 | 2026-09-22 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| c30c688a-a22d-33b7-a262-9efb38132af5 | 1.3818 | -56.0439 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 44689509-20e7-3e27-bc94-590a7175c6f2 | -3.1541 | -57.6772 | 2026-09-22 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4aaba301-9fd3-3b9e-90aa-859abdb9a636 | -9.7693 | -46.0615 | 2026-09-22 15:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 75b82c3e-eeb7-3807-8664-3fb7a927fb54 | -3.1902 | -57.851 | 2026-09-22 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6512ff54-bb85-35bd-9641-5aa3674930c0 | -3.7181 | -58.8823 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0e1557b8-3abc-342d-b885-c86c53e51957 | -6.0196 | -51.7893 | 2026-09-22 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 56bc8b30-d5f5-3a86-aa71-88853e18f05d | -3.7313 | -60.5638 | 2026-09-22 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| cd72ffa9-a406-33fa-b302-039c573ea75c | -6.9228 | -42.8852 | 2026-09-22 15:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| 305dd236-fdcd-3d8f-850c-acc24efdb11b | -10.336 | -50.2119 | 2026-09-22 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3bf578bd-6270-3dbd-8e4b-2a60e8004fa9 | -2.8716 | -60.9203 | 2026-09-22 15:50:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 16a433cc-122d-3b6b-a1ab-1bb7e08a00d0 | -6.0924 | -57.7043 | 2026-09-22 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9e08e294-9df5-3d42-befd-12dd4221b67b | -3.6033 | -60.5664 | 2026-09-22 15:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 197.8 |
| baf61e78-93df-3bae-8360-d85be2c72c2a | -3.5893 | -59.0773 | 2026-09-22 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 30a2a048-2216-3ce9-8950-0f0fa7ca3f77 | -6.1653 | -47.5052 | 2026-09-22 15:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0278ee7e-bcfd-3438-87f4-025bd18ab5fd | 3.9717 | -59.7011 | 2026-09-22 15:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4bd831ca-6a7a-3cc5-bcd6-e4f8023302f8 | -0.803 | -48.6397 | 2026-09-22 15:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c8eb5584-b358-377a-9f3f-add868e89721 | -2.9525 | -57.72 | 2026-09-22 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| d24f3b48-9bec-3c1e-b0b4-ab4dfe147efd | -2.5687 | -57.494 | 2026-09-22 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 0fabaf67-e4b5-3bbf-8107-7a616d010d4d | -3.6449 | -58.8647 | 2026-09-22 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fc45a11a-71d0-3082-9a53-7a9fd55684aa | -9.247 | -57.1488 | 2026-09-22 15:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 3f7008d6-a43a-375b-a584-c79943112f2a | -3.4368 | -61.3081 | 2026-09-22 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9cadfa29-ce9d-3638-b50d-7192030950a3 | 1.4453 | -50.7655 | 2026-09-22 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1c98a571-a63a-3b01-a750-e69b40a394f7 | 3.9716 | -59.7393 | 2026-09-22 15:50:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| de6b60fa-c29d-3d07-bce5-da83ef9e3a9e | -2.9322 | -58.5133 | 2026-09-22 15:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| cefd1b04-d9d2-3fa2-9b23-6c0dcb9fdec0 | -3.5501 | -59.9584 | 2026-09-22 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fe778a74-c784-3504-9725-54f880ee7056 | -1.4487 | -48.9526 | 2026-09-22 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 21dbd0f1-9ddc-3f62-bf91-f37f311cb531 | -6.0926 | -57.6652 | 2026-09-22 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 2b21d6c9-1c49-3533-9d1e-be809d08906f | 1.547 | -55.7466 | 2026-09-22 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| fbf91a9b-6c41-3d1f-a430-930a14812bff | -2.4206 | -58.2712 | 2026-09-22 15:50:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3550fd7c-e32a-3bb5-a39f-ab44411ea0d1 | 1.5282 | -56.0424 | 2026-09-22 15:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 3d7e1fd5-c6d9-3726-b6c2-a59a2f73e564 | -11.7484 | -50.8061 | 2026-09-22 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f0221a16-dc89-3cc6-b79b-a3bcad1ac21e | -2.5687 | -57.5135 | 2026-09-22 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 0e602e88-6b4a-3916-b839-514b07e4a505 | -6.8985 | -41.6976 | 2026-09-22 15:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1280.2 |
| 63efc920-d505-3751-bbd8-a455fbe5e916 | -9.3609 | -48.3251 | 2026-09-22 16:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| e1f7011d-94e2-3d72-a34f-317d195c7c95 | -11.3784 | -44.2195 | 2026-09-22 16:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 233358d1-2fe2-3dcb-87be-4ff06f318f8e | -3.1079 | -61.408 | 2026-09-22 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 15140e79-ab75-3526-ac14-04df6fb72038 | 1.3634 | -56.0638 | 2026-09-22 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 04858559-a602-389c-a5a7-264d7b58d591 | -3.4186 | -61.2895 | 2026-09-22 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0eb4b665-ef32-31b5-bf42-7a2cbf232023 | 2.4212 | -50.9557 | 2026-09-22 16:00:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4be451e9-47eb-3fb8-bdad-357099e4067f | -3.44 | -60.094 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 5ac4ccce-cc9a-3b40-b3e7-1bc03949df06 | -9.247 | -57.1488 | 2026-09-22 16:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 5fc71af8-703f-39d1-b184-d949fcb7d232 | -2.4023 | -58.2715 | 2026-09-22 16:00:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 748e35c8-7236-3f88-8ff0-206a9ed7cc3b | -3.6997 | -58.9019 | 2026-09-22 16:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3ad59e6e-bae7-3068-a76c-1cdeb545786b | -3.3311 | -59.8101 | 2026-09-22 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 055e577c-65ad-33c0-911b-b691cadd2605 | -10.336 | -50.2119 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 66c17e3d-d7df-3e02-890b-aaa5fee16bba | -10.3171 | -50.2138 | 2026-09-22 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0beb36ca-288d-343f-8f74-cb0ba4639770 | -9.788 | -46.0819 | 2026-09-22 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 1e8f9a51-1d82-3847-b468-5b16ab95ef31 | -3.0719 | -61.1819 | 2026-09-22 16:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |


[Clique aqui para ver as próximas entradas](README155.md)
