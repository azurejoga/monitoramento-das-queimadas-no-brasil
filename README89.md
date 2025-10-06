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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef89d839-a661-3c0d-9565-162482b5c693 | -8.6139 | -46.3227 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 424ea497-8ce0-3ba1-b260-fc4239f9cc30 | -10.3247 | -46.9612 | 2025-10-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 066fa6da-5c68-3e59-9e3b-fcbf6e0a5ae3 | -14.5433 | -46.9861 | 2025-10-06 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 370.7 |
| 5b89a80c-ce2b-393b-a1f9-3e27d8a3e3a8 | -18.2862 | -45.4348 | 2025-10-06 13:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 101.6 |
| bb987954-b219-35b2-8a7a-f88777686a21 | -10.4099 | -50.3324 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| b0c47404-37fc-35a8-b6f0-d5db413d3de3 | -19.5111 | -44.8545 | 2025-10-06 13:30:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 73c79895-496e-3c3a-b3ab-7892d9085f9c | -12.5733 | -48.1393 | 2025-10-06 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 11bef2be-928a-3c0f-a322-a8f6b494c95e | -15.5901 | -47.259 | 2025-10-06 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 64960443-28b5-3f21-81ab-dcb04c999370 | -15.5896 | -47.2819 | 2025-10-06 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 48f95446-17ae-3391-9d1d-9ded11beb756 | -8.5198 | -46.3098 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 33eaa05d-a5fb-37de-8898-eb60d3375634 | -14.8828 | -51.4777 | 2025-10-06 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 4a9702ec-62d0-3db1-81b8-4393f04187b0 | -15.3546 | -47.3007 | 2025-10-06 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 0f443db7-9223-34de-9a77-8d2972c03cbb | -9.9215 | -50.1682 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| cc2924cd-782a-312d-a5f2-16e12bc6ad2d | -15.3541 | -47.3235 | 2025-10-06 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2c76f2f8-6b9f-3830-945c-b11d08336aa6 | -12.8954 | -47.2909 | 2025-10-06 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 6c3e085a-bd42-3506-bb78-d0f0d57c7199 | -9.9018 | -50.2341 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2fce161a-4d95-3e4e-aad0-0c0fff023fc9 | -15.2351 | -49.2914 | 2025-10-06 13:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1018e81b-9a59-3e6a-8e98-79d4460bc70a | -7.7014 | -42.4043 | 2025-10-06 13:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 03a2bf70-b783-30f9-99df-a276b4e54c8a | -16.0038 | -50.8365 | 2025-10-06 13:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 0715ff17-6129-3de1-b3cc-6c184228acb6 | -11.8038 | -45.0624 | 2025-10-06 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b1916387-65d0-30a0-b50b-c91fd6e498ee | -12.9841 | -51.0648 | 2025-10-06 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 88a158cd-6166-33dd-961d-4780c467f70e | -14.5633 | -46.96 | 2025-10-06 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 054e928c-9fe5-302a-b7f8-5473267fe46e | -12.5541 | -48.1419 | 2025-10-06 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4313e89f-eca6-3bd8-a540-09c632ab92ee | -12.9844 | -51.0433 | 2025-10-06 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| afcc973e-1234-3f98-a3c3-160d2b6b2dc4 | -7.7935 | -42.5845 | 2025-10-06 13:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 7e087b12-2657-363c-8509-ed257cada392 | -7.2778 | -44.7778 | 2025-10-06 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| a9c33774-eb0b-3ac4-a4bc-8bd58d0de189 | -12.4853 | -45.5587 | 2025-10-06 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 75068c36-46dd-3f41-877d-a0c95696cac2 | -9.9779 | -48.7405 | 2025-10-06 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 8b45d44a-6559-314d-9e68-035e1abe3c9f | -13.2515 | -47.7979 | 2025-10-06 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0fe288cd-b187-37f8-96e8-2d2c603d4d4c | -9.9212 | -50.1895 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| c4890a94-465b-3cca-b730-944035dd3d80 | -10.4054 | -45.3931 | 2025-10-06 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d2f6b099-b75d-353d-87ee-2d747c6d8f5f | -10.7281 | -46.6433 | 2025-10-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3ed12ecd-e1c6-3565-9391-4a7c6caf6723 | -8.0866 | -44.791 | 2025-10-06 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 282.9 |
| e7562bc7-27e7-3bc1-8f7d-0b5b92356d3e | -14.6897 | -48.3797 | 2025-10-06 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 172.3 |
| f01eb912-ee24-3353-a504-5d68af2cdee2 | -14.6325 | -52.5137 | 2025-10-06 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| a67719cd-977e-3e46-9d36-64ba8e5b6e89 | -14.5623 | -47.0056 | 2025-10-06 13:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e0e395d8-9b9e-3b3e-a48a-0cb39b1dc374 | -7.2094 | -45.8942 | 2025-10-06 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4968b8db-8730-3592-81f9-f08e14a84ead | -14.6985 | -45.1858 | 2025-10-06 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 392af654-c065-3259-a176-ffcf84a172a3 | -9.4863 | -46.0039 | 2025-10-06 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 959fc93f-580e-3f55-84cc-4e60d5b28d40 | -14.8626 | -51.5234 | 2025-10-06 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 6dfe7ba0-bfd4-3c18-88c4-4c434d5f7c04 | -8.6327 | -46.3208 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4b27c3a4-909b-3be1-abf1-d9447eab1c09 | -11.1181 | -47.243 | 2025-10-06 13:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 35e138c0-e9b8-30ba-9daa-ddcc0da70458 | -18.2869 | -45.4109 | 2025-10-06 13:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 1bb6ca23-c3f2-340e-9779-eb92fdba7502 | -7.6804 | -42.5728 | 2025-10-06 13:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 0858d632-f6b7-33e5-a8c3-7740c6dd0475 | -8.0678 | -44.7929 | 2025-10-06 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 36453452-8833-3899-a15b-f021a6103fd8 | -10.6184 | -46.3646 | 2025-10-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d803b670-64f7-327e-b401-896ccdbada43 | -14.3339 | -45.8545 | 2025-10-06 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 35e6acf1-8f17-3f29-af3d-14d3091ead2e | -16.0086 | -55.9949 | 2025-10-06 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 0933efdd-2db4-37aa-9af6-f6b30d87192a | -7.2776 | -44.8007 | 2025-10-06 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3bf3d60a-f312-3a91-9b91-57ebedf17538 | -7.4672 | -43.0438 | 2025-10-06 13:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 6165359f-96f5-34fb-a1d2-978b477e15d9 | -8.6144 | -46.2778 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 9af27991-72bd-340d-bb8f-2469a35b26ef | -11.8221 | -45.1059 | 2025-10-06 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| abf35363-ce56-3f22-8d42-4266c0bd6c76 | -12.1458 | -50.9523 | 2025-10-06 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 375a7879-861b-384d-a14e-46618b6b966f | -14.6893 | -48.4021 | 2025-10-06 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 82f80bd9-c325-3d98-92f5-b120dcd1c3b9 | -11.8029 | -45.1087 | 2025-10-06 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 95619669-a7b3-3bd1-a346-9fae0dbc95ae | -11.8225 | -45.0827 | 2025-10-06 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| a1771ca1-5c1b-3cdd-8673-469f71140872 | -11.655 | -47.039 | 2025-10-06 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 416d7517-7e01-3d85-b7a1-8789c36f9b20 | -7.4276 | -46.5239 | 2025-10-06 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 12c95af2-e81b-370b-9758-70fe601b28b7 | -7.2091 | -45.9167 | 2025-10-06 13:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7e770388-5a60-3c31-a7c6-4b531c6f49a3 | -7.7203 | -42.4023 | 2025-10-06 13:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 466d49a6-f454-3f68-8ccb-75d8dca052c9 | -10.9681 | -47.1058 | 2025-10-06 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 9556b360-3352-38b9-b172-7e1de5975a3f | -9.9204 | -50.2536 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 59b8d5e1-041d-37e1-834a-7de5edb8244f | -8.5196 | -46.3323 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| f196a7af-87cd-366d-9219-8a6a2d5069d4 | -9.9207 | -50.2323 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| e03dbdf9-5ac0-30ec-bf7b-aa411b98ac2a | -9.959 | -48.7425 | 2025-10-06 13:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4de8a4e5-4273-3fed-96d8-b3d1c028e125 | -15.6616 | -47.5642 | 2025-10-06 13:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 4b7a9a44-7e22-396f-abfd-269ca2aa2214 | -7.6801 | -42.5966 | 2025-10-06 13:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 9c82f747-d46a-3130-836f-186caaefc893 | -10.386 | -45.4184 | 2025-10-06 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 01836d6a-40cd-3f2f-9448-abe1e35562e7 | -13.343 | -48.0519 | 2025-10-06 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b34ebef7-777e-3db5-9faa-e941f2b27770 | -8.5193 | -46.3547 | 2025-10-06 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 472c428d-96a0-31a5-a44b-236ee869a98c | -14.6321 | -52.535 | 2025-10-06 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 4dabdfe7-2cf5-38de-a49d-d498b6d59c44 | -8.88 | -47.6282 | 2025-10-06 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a88b4654-c096-3c65-be77-080147908450 | -17.8417 | -57.6254 | 2025-10-06 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| c5b4a48c-9452-386e-957e-9c30151822fe | -7.7206 | -42.3784 | 2025-10-06 13:30:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 1814231c-1959-3e67-88bb-c773580b7c1c | -10.3437 | -46.9589 | 2025-10-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 9373e0b2-41bc-3bc4-aacb-aa480a834835 | -9.9024 | -50.1914 | 2025-10-06 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 6be5e81b-69e9-32f5-a4a3-7b64d2a8ebc9 | -8.1684 | -44.2766 | 2025-10-06 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f8636c50-18a0-3f67-8183-71e2c5843711 | -14.9161 | -46.8312 | 2025-10-06 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 15f62014-33c5-3a0d-bac2-3da7b43a5dba | -7.6804 | -42.5728 | 2025-10-06 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 3aaeeba6-466d-3880-88f6-392474cf26cf | -7.4089 | -46.5255 | 2025-10-06 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| f3336018-f75c-3482-b9c3-49e6fa23317e | -6.999 | -42.8072 | 2025-10-06 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 61147250-5456-3629-98a8-0833dca11aae | -10.3724 | -50.3149 | 2025-10-06 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 58c06998-4d56-322b-a2d0-f97556088a27 | -7.7206 | -42.3784 | 2025-10-06 13:40:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 5e4cdd84-4d28-3172-b7bc-db6b50ee67fb | -10.4054 | -45.3931 | 2025-10-06 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 46d321f2-1b02-3850-8380-f50adef9b600 | -13.2586 | -48.4635 | 2025-10-06 13:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 2cdb62d7-2ebe-3c56-8301-ba9b086e8797 | -13.0939 | -47.9992 | 2025-10-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5288e563-ad3a-3846-831f-32c57cc2babe | -14.8634 | -51.4804 | 2025-10-06 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c47b6691-81d9-38b3-aeb6-c4576bb9f7d8 | -9.9018 | -50.2341 | 2025-10-06 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 8addfa1f-d9ae-3cfd-a4f4-f347ab01e0d2 | -7.699 | -42.5946 | 2025-10-06 13:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 1e47a79f-7671-3395-9c3a-264c4f3250df | -9.4863 | -46.0039 | 2025-10-06 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| f0444179-286b-3feb-8620-4a627282c251 | -11.4421 | -44.9535 | 2025-10-06 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 8a74274a-c632-3e88-801b-e03bb5662cde | -10.386 | -45.4184 | 2025-10-06 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 5f42964f-a0d6-3ffb-9241-0c49841d1a49 | -11.1181 | -47.243 | 2025-10-06 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 7377181f-1a69-3705-bdab-f20a3ffd979c | -7.2091 | -45.9167 | 2025-10-06 13:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 7d42771b-116e-34fe-85b6-b424152b4a9d | -15.3546 | -47.3007 | 2025-10-06 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 70b89057-3e8d-3e5b-8668-b0f37b88483e | -8.6144 | -46.2778 | 2025-10-06 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 208.4 |
| d4ca97a9-798e-3fb7-ba8b-6327a0254d19 | -13.1132 | -47.9964 | 2025-10-06 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1abc7857-d256-3da3-a2e6-49732fdc4bf7 | -10.158 | -45.4244 | 2025-10-06 13:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 5bd2783f-91bf-37bd-8c7e-9d5a6a1e6ca5 | -10.3864 | -45.3955 | 2025-10-06 13:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7b4e399a-0b8a-317b-b5a3-dbc5234929b0 | -11.8033 | -45.0856 | 2025-10-06 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |


[Clique aqui para ver as próximas entradas](README90.md)
