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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 218b7d43-b7bf-386b-80a0-c635a0751ef3 | -15.1161 | -52.5131 | 2025-09-13 01:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| d3060260-c0c0-3f71-a6fe-924761ca3c0c | -11.7192 | -46.6257 | 2025-09-13 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 0add114a-46ec-3dc5-b56d-081721216f9f | -9.2843 | -59.418 | 2025-09-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 1d10d111-b4bc-3d03-a71a-d23b9459fb5d | -9.2844 | -59.3986 | 2025-09-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| b9906fe5-9e45-36de-9365-fed4acd58522 | -9.2503 | -51.2472 | 2025-09-13 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bbc31ec3-0878-3d0a-b2fe-89323dbea9c9 | -9.2658 | -59.3997 | 2025-09-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.4 |
| 0308db3d-f79b-33f5-9ab1-1cd24622bb9c | -9.2656 | -59.4191 | 2025-09-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 83b4a6ff-ed41-36f0-8879-663e383639b0 | -11.1508 | -51.4863 | 2025-09-13 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ac43153d-0bdc-3529-8d35-fddd39564bee | -16.0056 | -47.9555 | 2025-09-13 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 34.7 |
| e1d03d52-cfeb-3efd-bbf9-cbc9e3d7be60 | 0.6904 | -50.6481 | 2025-09-13 01:30:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c1d39be0-eba7-39d0-b845-4579c1513071 | -11.7196 | -46.6031 | 2025-09-13 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 223.0 |
| e95d8cd0-6a06-3de6-81e9-7f95bfa56d97 | -21.6187 | -46.8115 | 2025-09-13 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| f33d19b1-e946-3859-840f-b51bbfb0b692 | -8.4334 | -47.2306 | 2025-09-13 01:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e3e058e9-19d0-3a7f-84a4-49a2e9df37f5 | -9.4996 | -46.4075 | 2025-09-13 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 093094ff-84d2-33e6-9b8f-b493f88bd8e6 | -11.7388 | -46.6005 | 2025-09-13 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 262.3 |
| d3671edf-5f04-312b-8b99-d27ae818862c | -15.1165 | -52.4918 | 2025-09-13 01:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d0194c58-a465-3a3e-9708-1898ad2cf6f7 | -16.3418 | -51.5434 | 2025-09-13 01:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 26e75930-3797-3773-9151-d9c388029d2e | -20.6156 | -50.3998 | 2025-09-13 01:30:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 49920d8f-5b5a-3fba-b604-08b0341c3356 | -9.5324 | -54.6277 | 2025-09-13 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 90dfd162-8dfb-3f21-8b56-89c34a63a6a0 | -9.4993 | -46.4299 | 2025-09-13 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 1e1098c8-1c64-30cc-9b3f-56f8083497bd | -17.4633 | -39.8982 | 2025-09-13 01:30:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 4fee5f09-dce5-35f4-acee-4091876c8099 | -16.0252 | -47.952 | 2025-09-13 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 69f133fb-fe2d-3b03-9628-0575cc398aea | -10.7664 | -50.5299 | 2025-09-13 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a10b1e92-e34b-3875-af25-f49a84772cd7 | -3.2282 | -47.6371 | 2025-09-13 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 23ec5ffa-9f52-3490-8636-eaab0ff952da | -15.2036 | -56.6803 | 2025-09-13 01:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 16016d2a-58f3-384c-badc-abdbd3ab5d35 | -9.2472 | -59.4007 | 2025-09-13 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a0ad112e-07ca-33dd-beb7-5db74ca602f0 | -3.2305 | -47.135 | 2025-09-13 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 7af9cb20-4f18-3f7b-a3c3-5842bf9fb735 | -12.5795 | -45.6591 | 2025-09-13 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ad18c048-0511-3645-86d9-a8337e01cc7b | -16.0061 | -47.9329 | 2025-09-13 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 57.1 |
| dbda2f38-b58a-3e37-bddf-24fdc44fd1df | -11.3851 | -63.3416 | 2025-09-13 01:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b99085c5-cd62-3ca1-ac69-c87266738469 | -17.4641 | -39.8721 | 2025-09-13 01:30:00 | GOES-19 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| e3914ace-39c2-3747-94bc-1bad41665ef1 | -9.5006 | -55.9588 | 2025-09-13 01:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c46e6ad7-0654-3739-b623-0f76f5a66589 | -11.3849 | -63.3606 | 2025-09-13 01:30:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 31ecd42d-17d6-33fd-ad98-723334697623 | -3.2321 | -46.7836 | 2025-09-13 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d445ecc0-15ab-3998-bb4d-afc3e5c5814f | -13.8979 | -48.2804 | 2025-09-13 01:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 10f6883a-5c9b-3bf7-80a4-62102fa9560b | -11.8472 | -50.5598 | 2025-09-13 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 07b9a932-d83a-378f-97a3-afe0701bb486 | -17.2836 | -47.2364 | 2025-09-13 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 94b4bdf8-5dfd-3dd8-9735-2d7eb62bace7 | -13.9172 | -48.2775 | 2025-09-13 01:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| ebf5c01b-28a4-37d8-a7e5-62352ccb5fb0 | -9.5006 | -55.9588 | 2025-09-13 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 2787d1ad-ddf7-366d-8e81-51aca39766fc | 0.6904 | -50.6481 | 2025-09-13 01:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 66.4 |
| fdd92787-4558-3f19-8bf2-a3aba01ddf50 | -17.3622 | -42.7029 | 2025-09-13 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 5d52d992-bd0a-389d-a71d-5a84af4adc76 | -11.8472 | -50.5598 | 2025-09-13 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 621742ba-e89c-32bc-aba3-aa8cb5b7de55 | -9.4996 | -46.4075 | 2025-09-13 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 1c6d5378-d564-3a87-a102-1749d831d054 | -9.2656 | -59.4191 | 2025-09-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 210.6 |
| 75303a82-9fde-3fe0-861d-e3a87e358d52 | -11.4076 | -50.7378 | 2025-09-13 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 93288ace-0890-3281-946a-1a8b2be2313c | -16.3418 | -51.5434 | 2025-09-13 01:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8fd91936-76e2-334b-8fc9-6adf8e819fd6 | -9.4819 | -55.9601 | 2025-09-13 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e27ade01-90a1-3333-a900-f0207729de13 | -3.2306 | -47.1131 | 2025-09-13 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 2bf5e68b-8612-33f6-b953-d308e9ee0280 | -3.2283 | -47.6154 | 2025-09-13 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 81fb9650-8986-3c3e-adf1-0a359b0e02bb | -12.0056 | -47.7728 | 2025-09-13 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d34c1173-126d-3513-888e-d8790493cc0a | -9.2472 | -59.4007 | 2025-09-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| be0dee84-55c0-312e-a699-82cca7934c8b | -17.2836 | -47.2364 | 2025-09-13 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| fb691e1f-c7da-398f-83b0-d7e1be4334ed | -11.1519 | -51.4018 | 2025-09-13 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 828d29ef-21e6-3ac3-85aa-d8e236e67fa8 | -16.3614 | -51.5403 | 2025-09-13 01:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 5526de41-d947-3cc2-9edf-0939e5ddb30f | -11.7384 | -46.6231 | 2025-09-13 01:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| f74cf3e1-b755-329b-9a65-9f87fd5b63ed | -3.2305 | -47.135 | 2025-09-13 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c518a08a-2c68-35c1-9347-9f06f6269403 | -12.006 | -47.7505 | 2025-09-13 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b50c58b0-af8f-32a6-b60b-4da482310afd | -9.2844 | -59.3986 | 2025-09-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| c4a081af-c440-3c75-82b0-f7f9a5a57455 | -11.7388 | -46.6005 | 2025-09-13 01:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 67ba48c6-ac96-3146-b703-378751ad3eb4 | -16.0257 | -47.9294 | 2025-09-13 01:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 31.6 |
| d45eb71d-35cb-3e71-9e49-6468a0ea6865 | -9.5193 | -55.9575 | 2025-09-13 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| bd3aaf9b-9689-339e-911e-9bfdedea0658 | -11.1706 | -51.4209 | 2025-09-13 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 30a67d8e-7365-388d-a3ee-f3c29c876fd5 | -9.5004 | -55.9788 | 2025-09-13 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 917504e8-54cc-38fe-8502-7450cad408df | -20.5952 | -50.404 | 2025-09-13 01:40:00 | GOES-19 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 33c27cdc-1016-3b43-84f2-c82b10f4ab97 | -11.8468 | -50.5813 | 2025-09-13 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 356c7292-616a-3554-936a-2421e2b70bb1 | -9.247 | -59.4201 | 2025-09-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 2e6478a3-0001-3cbc-a246-bc0fa154ecaf | -13.8979 | -48.2804 | 2025-09-13 01:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 57b53c91-ebda-39a5-9a12-fd9cfe28f180 | -12.5791 | -45.6821 | 2025-09-13 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 83251208-24e6-3b71-8803-3334ab064962 | -12.5795 | -45.6591 | 2025-09-13 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| b097732c-b314-396e-a3ad-e446b9810a6e | -15.2036 | -56.6803 | 2025-09-13 01:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4f114460-616b-3595-8cc0-d9d4e2104308 | -8.4707 | -47.2491 | 2025-09-13 01:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 4be6879f-bc75-307d-a283-f4e50dbf4517 | -9.5324 | -54.6277 | 2025-09-13 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 406e8836-3635-3373-b82b-6829de6cdb93 | -11.1522 | -51.3806 | 2025-09-13 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0d78f2b3-56a7-3f7c-99cc-692128f5b999 | -11.7196 | -46.6031 | 2025-09-13 01:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| ff3c3ee3-06a3-3d16-86ca-acdd424f50f3 | -9.5137 | -54.6292 | 2025-09-13 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| c2fb6eb2-6ee0-30b8-82cd-4737aa5b00ca | -11.7192 | -46.6257 | 2025-09-13 01:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| d2b09985-7af6-3161-9641-280042ff521c | -9.2658 | -59.3997 | 2025-09-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 1acbaa74-55fd-393e-8481-42a006f29567 | -3.2282 | -47.6371 | 2025-09-13 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 3a39db21-d458-3b4c-8ca0-2f3eadc0fca4 | -9.2843 | -59.418 | 2025-09-13 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| f25bd6e9-e7c0-3d12-85c1-cef6b4c1d73e | -9.4993 | -46.4299 | 2025-09-13 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 06408536-94dc-3a62-93d4-00d50feec59c | -12.9292 | -54.7538 | 2025-09-13 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7c66fd9f-8712-3a86-bae0-c26966c7536a | -12.5603 | -45.662 | 2025-09-13 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 66a2482f-58fc-3f33-9986-dabf792f1e2d | -11.1709 | -51.3998 | 2025-09-13 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 51fa7afc-5504-325b-9989-9192f1c7444b | -16.0796 | -49.993 | 2025-09-13 01:40:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| d5980b6e-778d-34f0-9973-d36e61a38170 | -12.5603 | -45.662 | 2025-09-13 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| d4c6474c-51de-357c-8922-942b40114988 | -11.8468 | -50.5813 | 2025-09-13 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 72e906e0-47e3-37fa-bc49-4722b7b3280e | -12.006 | -47.7505 | 2025-09-13 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3fe4f2cb-1208-37bf-b8ea-fbe3e6a05a86 | 0.6904 | -50.6481 | 2025-09-13 01:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 888a2ad6-f4e9-3ab5-9236-129337755e68 | -18.3483 | -50.9483 | 2025-09-13 01:50:00 | GOES-19 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 71c09a69-0394-31ae-a623-1cb4bfbd6539 | -18.3278 | -50.974 | 2025-09-13 01:50:00 | GOES-19 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 167.6 |
| b056e1bb-ecf9-3e6e-9f8b-e2d51c18bdbd | -11.1519 | -51.4018 | 2025-09-13 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ff98d080-0824-376d-b2e1-8b7a4ab9a195 | -3.2283 | -47.6154 | 2025-09-13 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 9ed4bfbc-74e5-3ea3-aa9f-e19aef239cf4 | -11.8472 | -50.5598 | 2025-09-13 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 76bd339b-1004-31be-9751-fe5b8bfa50c5 | -8.4707 | -47.2491 | 2025-09-13 01:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 2330b7d8-3e1f-383d-9ec3-f389429788f3 | -13.8979 | -48.2804 | 2025-09-13 01:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a1a941d2-a01b-3daa-97a3-569394c6d736 | -15.8656 | -49.9397 | 2025-09-13 01:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 01446ed9-6b0d-3c88-9c81-15e0e20e9e25 | -9.2472 | -59.4007 | 2025-09-13 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| f5e67d51-9ec2-3b73-8f45-a985ece69bf6 | -16.0796 | -49.993 | 2025-09-13 01:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 83a2a160-ba8a-3fcc-8f49-ead4c73fe0e3 | -15.8852 | -49.9366 | 2025-09-13 01:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| e42b440e-33e6-3a0a-99d2-803604cbd306 | -3.2507 | -46.7829 | 2025-09-13 01:50:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |


[Clique aqui para ver as próximas entradas](README14.md)
