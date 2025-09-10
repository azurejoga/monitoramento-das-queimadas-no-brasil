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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03b36226-ad94-3c30-8f7e-8a9e3c46f419 | -23.49849 | -47.20602 | 2025-09-10 04:17:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1682a674-fc8b-3521-9c9b-1e32e3ee2c2e | -17.29317 | -46.67958 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07e2379e-3a1f-3b87-88ba-ffb37dd0d830 | -11.18956 | -48.37463 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7d159b9-2ff2-3ade-a087-87ad2f85d572 | -13.87815 | -44.45084 | 2025-09-10 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f89409a2-c07b-3135-8535-6564dab291d7 | -16.61575 | -49.77805 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8277d052-4160-3496-ba4a-39337cbd3650 | -13.69094 | -41.3675 | 2025-09-10 04:17:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e9ece41-b3ba-3715-8b35-7ba97c0ee52e | -12.08846 | -43.3322 | 2025-09-10 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d467fa31-e260-3111-a620-a18a7d46af9c | -19.94879 | -49.26854 | 2025-09-10 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 74474a3d-50af-3446-bbaa-1f2657e1102b | -15.09318 | -50.07378 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| d2d9e4f5-8207-3ea7-9ad1-015452bb8365 | -22.1545 | -47.67705 | 2025-09-10 04:17:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f67e7b6e-eaac-3a4e-adfd-bd9fb7f189f3 | -23.0327 | -50.10078 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 51dac953-4081-3b47-90aa-4ba343bcd047 | -17.39733 | -44.99673 | 2025-09-10 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a4c6210-0296-393a-a487-fbfb71a6c927 | -12.02313 | -45.85617 | 2025-09-10 04:17:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8634a68b-b5d2-3979-bd8b-138b9c789b51 | -16.62036 | -49.77395 | 2025-09-10 04:17:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eaf1649-2306-322c-9b4e-9617f3a91853 | -23.39455 | -45.96417 | 2025-09-10 04:17:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| bcc51306-a147-3882-a50c-2196c9b8de13 | -13.04291 | -47.16865 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7115131d-8a78-34e3-aa07-717101ef5639 | -11.41317 | -43.57033 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d094038-105d-30c1-9cbe-ccee49629631 | -16.21635 | -48.4865 | 2025-09-10 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 929f07f0-12a9-3f62-9f64-ac477da32b98 | -11.1097 | -48.36573 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3530f4b-2f23-3211-8a32-2422298d530a | -11.24414 | -49.40514 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf3c8715-e7b7-3756-9e06-ea32511e0091 | -15.83618 | -48.96057 | 2025-09-10 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b8d70d3-7c23-36a7-8bfa-6b899895ec28 | -14.60161 | -46.33592 | 2025-09-10 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f23151f4-df9f-3a6d-835d-5a32e7d16f6a | -14.53512 | -42.48135 | 2025-09-10 04:17:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ebc6e655-79aa-3a41-8a63-fb6e43c00edc | -20.54864 | -47.62568 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad7b95a4-e473-3d1e-8960-6043e10254ad | -15.81 | -52.24156 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3b1e2b69-90e0-3b6e-94e4-e3f7c3014ab0 | -12.84103 | -52.94368 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f745c51-3cd4-3c2b-81ab-fd36693594e4 | -10.27238 | -48.81411 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1c04c2f7-1609-3ebe-8c46-7b0c86c00495 | -13.90689 | -47.97853 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72abd629-4131-3f1c-aa4f-48c67c3e0f18 | -14.35415 | -47.314 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1eecc0b0-d520-377d-ac98-135b1c1cf885 | -13.04831 | -47.15748 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a4f26a1-b11d-3ba1-b777-b49079b04309 | -19.93897 | -49.26227 | 2025-09-10 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 00b4f15d-d47c-3373-bf82-968197e21ca3 | -15.17683 | -47.9504 | 2025-09-10 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62a3b281-b584-375a-900f-43cc1d830305 | -14.243 | -46.69126 | 2025-09-10 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed1f5089-7d39-3bb8-9113-a5cb6c82a760 | -15.03623 | -48.09454 | 2025-09-10 04:17:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6aca8bc5-2f19-3c3c-9819-c90eaea7c298 | -15.82073 | -52.23354 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2d3bb9a-4162-3413-98a0-6e6eb970b6d5 | -17.24705 | -46.07344 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e50f1387-a7a1-3fb6-90c4-f7c2de25f35d | -9.97971 | -50.30368 | 2025-09-10 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bcc5641-94c9-321d-a759-4cd42da2341c | -11.29374 | -53.95327 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 744804fc-8326-3ed5-b5a2-8d453020703c | -15.47482 | -49.37379 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29e02f69-52b3-30bc-9035-0d08a8ce1955 | -16.76031 | -47.27134 | 2025-09-10 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0bf042f9-0048-317e-8acc-746f7c277261 | -12.1405 | -44.84317 | 2025-09-10 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e93cfee8-b58e-31ca-9306-6d26f4381fb8 | -21.39638 | -43.87653 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 442492c6-448b-3dd9-b1ac-a52e6690a216 | -12.18516 | -53.87211 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 662370e6-299d-3265-9186-b4b24793d53b | -20.54707 | -47.65633 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 483d1a4e-d744-3328-a124-ce794f9942d9 | -14.32842 | -47.30294 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fb649c1-42c3-3ac3-919c-8beb983608ad | -11.42204 | -43.579 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82248d98-35dc-3329-8cab-8e6c571c6c00 | -9.99979 | -51.7016 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96cf03ec-d3bf-3759-a69e-e509e441831d | -17.7447 | -44.49106 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50c336dc-9670-3667-9bbf-cde5c17722b9 | -18.12185 | -43.94764 | 2025-09-10 04:17:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46397890-27cd-38ed-9615-6d7055ec690b | -14.61658 | -46.3644 | 2025-09-10 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04963d6c-2a3b-3c0b-b47b-5259ac4f06d6 | -21.12414 | -47.73336 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 80424603-aad9-3132-aff7-76aed7b14aa8 | -11.04162 | -46.05564 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42ec90fc-52aa-3e8c-8b3b-fe99e1175f4f | -14.60342 | -43.92995 | 2025-09-10 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 71b2fcc4-fd37-379e-aa12-67c797d5bd61 | -10.27589 | -48.81736 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 213ef3d1-8268-3029-9709-c0a5360b5cfc | -17.30272 | -46.72628 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f0f65533-a46d-39f0-bf1f-b5a846679a79 | -14.65366 | -44.04556 | 2025-09-10 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 182532d1-cf22-3c04-a0e7-1547f293c470 | -14.36159 | -47.31186 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8479b77-9f4b-3ebe-a662-9254094878d3 | -23.03195 | -50.10506 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 571d8953-951f-34c6-9736-039591902794 | -15.66079 | -49.92961 | 2025-09-10 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc564147-7c53-31a6-85d5-7c9d903646b3 | -10.27324 | -48.8092 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d6e44be-f695-311a-aed3-41e2817cd6b9 | -15.01564 | -48.02317 | 2025-09-10 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fab281a-d91c-3402-9c50-4215a4b71708 | -14.78493 | -48.22596 | 2025-09-10 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edc246e1-9ef4-3bed-8512-3e72dfeae207 | -10.30375 | -48.81921 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c991b716-9608-36f6-9239-afc050c19bad | -11.11357 | -48.36291 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23b77f38-d9a2-3d8f-871c-1286a59e1aac | -20.54737 | -47.67558 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e67db6f-f843-3a05-bdfb-22c9a2f4d718 | -11.83527 | -46.74873 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e92da2e-052c-3501-8f17-0bcac08c03a6 | -13.00734 | -45.21315 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e662469-c3af-30fa-8c6a-d9c86e634ae8 | -12.41722 | -44.72653 | 2025-09-10 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e49f4ae-3370-31c1-b04f-8ac745f0be62 | -23.36 | -47.20042 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2c50d035-cbf1-3e1a-a30d-b5cf91027f9f | -15.48444 | -49.38519 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3b16443-8b5b-3e80-abf1-a32d2369c4c0 | -12.0219 | -51.00445 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75d922c6-0949-3b32-9675-eb99d3732f5d | -23.36389 | -47.19728 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5fe75727-4fe1-32cf-a787-6fc8ff9f7576 | -17.33227 | -46.71273 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0eff8603-8920-32a2-8879-e261852c4b06 | -23.70955 | -46.89666 | 2025-09-10 04:17:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c68f3816-c276-3569-a003-a315bd1799fe | -11.72728 | -46.69939 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3103900-ef89-38d1-87ee-142fab8efca1 | -11.8512 | -46.75962 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fba29f88-ccf5-3f96-9052-48557b7660c2 | -11.2902 | -53.95283 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c7b92e4-2b67-389c-a1cb-51a431c78f50 | -14.24638 | -46.69184 | 2025-09-10 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e840e10-380a-397e-82f6-9fd79e607695 | -11.87981 | -39.56962 | 2025-09-10 04:17:00 | NOAA-21 | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 676f680a-a7b1-3225-82a2-0ba6470b29b1 | -10.38555 | -50.547 | 2025-09-10 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19b4d86c-2ebe-3eab-9f32-aac8468f208b | -21.30703 | -44.66965 | 2025-09-10 04:17:00 | NOAA-21 | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4b838e28-ad4a-3fa9-8eb8-79ef5687c422 | -11.43491 | -43.64986 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 715cb616-3bde-3f67-bdd1-121ed3e93cc5 | -17.69625 | -44.45702 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50d59939-faa0-3a49-a8e4-561352faca95 | -16.88586 | -45.75428 | 2025-09-10 04:17:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fe0d9fc-c0ba-3a26-93d8-eee186f6de2d | -11.64183 | -46.62169 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df19233-5de9-3485-b2b6-288ca3520996 | -11.82904 | -46.74357 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2eeff1d1-5361-30b2-baed-ad32438e9fad | -10.55157 | -51.50857 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dc08d862-ac8a-3e3e-a3f8-975a3f92c517 | -21.02627 | -48.42075 | 2025-09-10 04:17:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d14476f6-8183-36c8-bb1e-722096173dec | -20.94176 | -45.79477 | 2025-09-10 04:17:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3b30c51-ecb7-39de-9f7c-422b7af16f04 | -13.93631 | -48.26104 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c5a01da-e4b7-3de8-a54a-ed3733d2eada | -14.33249 | -47.29971 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0fd7edd2-989b-3d65-ad53-cb9359748c5c | -10.03007 | -51.67012 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 229fbde6-7e0f-3cc4-9b0a-6219a1048705 | -10.19881 | -46.82193 | 2025-09-10 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b219aaab-81a2-3f3b-9a70-0f62c0a54a52 | -11.44601 | -43.62242 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e9830797-e2ee-376c-ba6e-d9bb3c5bf6db | -10.56573 | -43.66327 | 2025-09-10 04:17:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d60bb8f1-12db-3376-8d5a-b2215167eb0b | -20.37821 | -46.62788 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8998edcf-c327-3ffb-86d0-ac65efcfa919 | -11.91444 | -47.09972 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fae9338-89a4-352f-8f05-e632162ea53f | -15.80209 | -52.25899 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6196f9de-c903-3787-939d-c501d60d1229 | -11.1168 | -44.85968 | 2025-09-10 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61bb353f-819b-3a79-af38-b0e53e804c0f | -20.55047 | -47.61442 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README38.md)
