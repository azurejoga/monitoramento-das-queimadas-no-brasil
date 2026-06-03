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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7448284-bb44-38cb-a040-cd44776d3177 | -11.6329 | -55.1844 | 2026-06-03 00:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fe45433f-a547-348a-8c38-d6889ce9c483 | -14.1543 | -58.9556 | 2026-06-03 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 048517f2-9996-35a8-98dd-30c03be72799 | -11.8029 | -47.3323 | 2026-06-03 00:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| c08265f2-3717-3eeb-9ae9-cba5ae0197ca | -16.5851 | -45.8715 | 2026-06-03 00:00:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 53bf0d17-9651-323a-9558-0c3974a1a922 | -17.444 | -42.6337 | 2026-06-03 00:00:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 6c862166-f54a-339c-9b0f-6bfa303c9e16 | -17.4447 | -42.6088 | 2026-06-03 00:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a0aa1cd4-8939-3464-a766-932ceaa5b6a9 | -17.4641 | -42.6287 | 2026-06-03 00:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4504d4e4-f1b2-3834-ae2b-9cb007092dc0 | -11.8029 | -47.3323 | 2026-06-03 00:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2496f0a4-3bb9-396a-9d09-cda89b4b8a5b | -16.5851 | -45.8715 | 2026-06-03 00:10:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ebb51026-a38e-3918-ab02-8810784e4f38 | -17.4447 | -42.6088 | 2026-06-03 00:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| e33812e5-8b13-3e96-ab5a-0647a5fc3043 | -17.444 | -42.6337 | 2026-06-03 00:10:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 1f0c5afb-01b9-3bb8-9f5d-98d95327a57b | -16.5851 | -45.8715 | 2026-06-03 00:20:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 24be0552-8d35-3161-af19-a6b60ca2e22d | -17.444 | -42.6337 | 2026-06-03 00:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 3344f4ec-aead-35bd-8b46-5dfff60286de | -17.4447 | -42.6088 | 2026-06-03 00:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ba56d792-d900-3431-b3e0-3c7585e48ce8 | -17.4641 | -42.6287 | 2026-06-03 00:20:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 5606076a-a032-33d7-a46a-24b903375207 | -11.8029 | -47.3323 | 2026-06-03 00:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1eb95b47-1d86-32f2-b833-49b12e83a5aa | -9.4964 | -40.3088 | 2026-06-03 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.6 |
| 6c33b779-6ec6-3cba-a540-ed8b993eb992 | -16.5851 | -45.8715 | 2026-06-03 00:30:00 | GOES-19 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 658bd10b-a1fb-3616-b48d-1daf9748f7c7 | -11.8029 | -47.3323 | 2026-06-03 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 6c87a03c-a3d9-331c-b6ba-f4cdb8cff784 | -17.4447 | -42.6088 | 2026-06-03 00:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1f31c87f-50fc-39d3-9421-18ede6137dca | -17.444 | -42.6337 | 2026-06-03 00:30:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| c4e11b73-0cfc-36cb-9d95-c7f48a5bdba5 | -17.444 | -42.6337 | 2026-06-03 00:40:00 | GOES-19 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| b1178f12-867e-3f1c-9a22-a8dbe3885978 | -17.4447 | -42.6088 | 2026-06-03 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 120e11b9-1054-325d-87d5-8cc5536bd2ed | -20.88883 | -48.98112 | 2026-06-03 00:45:00 | TERRA_M-M | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 6203524d-848a-3b3f-a945-ada01c50f359 | -18.72089 | -56.57344 | 2026-06-03 00:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| c9751240-e910-3b79-9f99-d710c2820bf4 | -18.46789 | -54.70522 | 2026-06-03 00:45:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 06ffe267-aac2-3611-b932-40a6614a52e4 | -16.57586 | -45.89368 | 2026-06-03 00:45:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 2878b983-7d93-3207-ab83-d76ed5106c94 | -16.59125 | -45.89737 | 2026-06-03 00:45:00 | TERRA_M-M | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 57.5 |
| d482d4d4-3a5a-3610-9608-fe9b91c2fe10 | -12.731 | -54.206402 | 2026-06-03 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86047973-b189-3d97-8326-301fad65ba58 | -12.7368 | -54.186901 | 2026-06-03 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 942bf3f7-dbfa-3237-8ca0-9efbeca95dce | -16.1478 | -58.4837 | 2026-06-03 00:48:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a6e80ab-deac-3967-8022-e6c927e7f0f6 | -11.6279 | -55.184601 | 2026-06-03 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8b40c4c-2a59-3fbf-a790-70235c24abd1 | -16.5807 | -45.859001 | 2026-06-03 00:48:00 | METOP-B | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d48762c-85ac-3989-a532-7c5075ef2285 | -11.7994 | -47.3214 | 2026-06-03 00:48:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53664e76-bf96-3fbc-aa52-3868276e5324 | -12.7388 | -54.195499 | 2026-06-03 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c64fcdd-75f4-331b-be9c-fc2f6b1564b4 | -18.7166 | -56.566601 | 2026-06-03 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5a70e38-14b2-32f5-9d3e-05951e904252 | -18.465799 | -54.695099 | 2026-06-03 00:48:00 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1a01bf22-4f01-3454-a183-9228293871dc | -11.7534 | -47.071301 | 2026-06-03 00:48:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58094fab-61dc-378d-9629-6d067d6b2eb7 | -16.138 | -58.485901 | 2026-06-03 00:48:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed92e52a-fe41-3bc0-9a5b-72e4dfd79cd3 | -9.1887 | -58.0495 | 2026-06-03 00:48:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf9f9e0a-4bdc-3e3d-843a-44333637de05 | -16.149401 | -58.491199 | 2026-06-03 00:48:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84313b8d-1b2a-3147-84db-3abfbd0cd9f8 | -8.8697 | -50.1889 | 2026-06-03 00:48:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db757d3-c9c3-39a4-ba5a-33c9f381ca1d | -11.5736 | -56.335201 | 2026-06-03 00:48:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da0575d5-118d-3060-931a-69b2d75e8754 | -9.1789 | -58.0518 | 2026-06-03 00:48:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 226075a0-546a-35d7-ac62-7b6eaca3f7cd | -14.1604 | -58.938202 | 2026-06-03 00:48:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e47f616d-0496-3af1-b3d3-caa622fd9196 | -11.572 | -56.327999 | 2026-06-03 00:48:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03f63f18-4680-3642-b673-1c0a039bd180 | -11.5686 | -54.578999 | 2026-06-03 00:48:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d48d487-94a5-3813-9b4d-a54c79aeca38 | -10.5682 | -57.310299 | 2026-06-03 00:48:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf8c46e-7f38-3fc6-b038-1cabc4761643 | -16.5711 | -45.8619 | 2026-06-03 00:48:00 | METOP-B | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fe92f621-2b71-3888-b83e-127b5ce73e1b | -11.8783 | -61.0341 | 2026-06-03 00:48:00 | METOP-B | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4025e50a-ec53-3f86-9c12-dca37f054fcf | -9.1774 | -58.044899 | 2026-06-03 00:48:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dd8b42a-ac5c-3397-8a2e-9c2437df6e82 | -11.5666 | -54.570599 | 2026-06-03 00:48:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc27b01-fc87-3d88-b0ea-d6e26a3a2ae9 | -7.5069 | -55.0014 | 2026-06-03 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c87e7f8-c610-312e-beeb-7a8847076e51 | -10.5697 | -57.317299 | 2026-06-03 00:48:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21c98ffd-3344-333a-ab41-833738d3c1db | -18.7264 | -56.564301 | 2026-06-03 00:48:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 17c19a8e-999e-3ba3-a99a-f036f147fbf9 | -11.4795 | -57.099899 | 2026-06-03 00:48:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce8f189-754c-3ea2-b3dd-9251570c7e8d | -14.162 | -58.945599 | 2026-06-03 00:48:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 215ada8f-8267-393f-bbe8-f579b53115be | -11.6261 | -55.176601 | 2026-06-03 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0292c113-142c-3a40-8f7f-c8fe3950c688 | -11.7468 | -47.046299 | 2026-06-03 00:48:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe383321-f36b-366f-9224-b98daaffd90b | -11.8902 | -57.827099 | 2026-06-03 00:48:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e2eccfe-81c9-379e-aee2-c15f5b3d7fb9 | -7.5048 | -54.9925 | 2026-06-03 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75373711-b296-3b73-ba70-f549103a3101 | -12.438 | -58.3936 | 2026-06-03 00:48:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36d19548-1237-3c0b-bcfd-829fd86f2308 | -10.8164 | -56.588501 | 2026-06-03 00:48:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 083bc997-82f2-36c7-8bd3-c8c09c80a18f | -20.8827 | -48.977901 | 2026-06-03 00:48:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25d6edc8-16b2-3859-8176-71095c83ff34 | -12.4395 | -58.4006 | 2026-06-03 00:48:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a939b8af-8d4d-30d1-8fdb-c24c25f0ecce | -16.1462 | -58.4762 | 2026-06-03 00:48:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 347d007d-887d-32e3-9917-1ada3692c554 | -11.8136 | -57.346802 | 2026-06-03 00:48:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 581d3662-c41d-312c-8061-9fa81da3c189 | -11.5818 | -56.325699 | 2026-06-03 00:48:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10dd7b52-9530-3f06-95b6-73d34e8f3056 | -12.729 | -54.197899 | 2026-06-03 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88e700e5-346e-336b-8cd2-c25268ff7f2c | -11.6339 | -55.166302 | 2026-06-03 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d78bdd4e-ff71-374f-b638-62ac74873e2f | -11.7898 | -47.324001 | 2026-06-03 00:48:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77ebcc5a-8919-3c72-8b5e-fe98c36e7613 | -9.1872 | -58.042599 | 2026-06-03 00:48:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29e1d733-d76b-326f-895c-3dab925b28ba | -11.6242 | -55.168701 | 2026-06-03 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 448f0920-2191-3f70-b40d-e1b36391095f | -11.5703 | -56.320702 | 2026-06-03 00:48:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0bddcdc2-6bcd-3863-9ec2-b3287b2408a9 | -16.9118 | -51.841999 | 2026-06-03 00:48:00 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24aeb900-e530-36dc-b922-b912ae38814d | -12.44249 | -58.40317 | 2026-06-03 00:48:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 3f08acc5-afbc-390d-abcc-b4fa3356b1d8 | -10.86556 | -53.74108 | 2026-06-03 00:48:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7af56fd3-e436-306d-b9ce-b6a1a6121978 | -11.62636 | -55.17427 | 2026-06-03 00:48:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9a898482-ecf2-36be-a104-8c94784bb3c4 | -11.33141 | -53.95822 | 2026-06-03 00:48:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1121a7c8-7a18-34b6-bec6-a0222560f078 | -10.81966 | -56.59905 | 2026-06-03 00:48:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a04aa7cf-143e-3859-bf71-903b8f56dcf0 | -11.8111 | -57.36358 | 2026-06-03 00:48:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3125706e-a21b-3e89-9107-8acd06bd6c2f | -11.62792 | -55.18478 | 2026-06-03 00:48:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 734615bc-e35e-3f41-a0cc-1f23fc48e461 | -16.9113 | -51.86585 | 2026-06-03 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 62f78b75-27b1-340b-bd2c-1311fce8c5f3 | -11.57441 | -56.3322 | 2026-06-03 00:48:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 8aa93f5a-02dc-39c3-90f3-54a0ff92aafc | -12.80916 | -54.86623 | 2026-06-03 00:48:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 41e6f4f0-9267-3eca-8549-20c974c1c2b7 | -11.88539 | -57.83705 | 2026-06-03 00:48:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5a8e9272-06f9-3fb7-8d71-84a910365757 | -16.1414 | -58.48647 | 2026-06-03 00:48:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a3549bbe-b023-3066-8476-6e31f16c441a | -11.48122 | -57.10888 | 2026-06-03 00:48:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 96b69011-16a9-3902-9269-15bdf2a67a15 | -12.73122 | -54.20969 | 2026-06-03 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 36e6a0d0-d75c-300e-9b7a-4220f8b5273f | -16.91285 | -51.85916 | 2026-06-03 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 9e50c0c3-e423-36cf-a778-a7050572757d | -14.54561 | -52.73217 | 2026-06-03 00:48:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a8dd066c-7c1f-3e24-9fd4-0aa374501f0f | -11.8017 | -47.35737 | 2026-06-03 00:48:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 08308952-2ba3-3cab-b193-043b394088e9 | -12.74116 | -54.20815 | 2026-06-03 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d0e9f857-4e9e-3b77-a974-4bdfa935e6ef | -12.73943 | -54.19655 | 2026-06-03 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 04ef20c4-7bbe-3442-8489-381fd7e8fe18 | -11.79893 | -47.36285 | 2026-06-03 00:48:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| a2a43f91-4aca-3aec-93fc-4f09dcbeab62 | -11.57574 | -56.3416 | 2026-06-03 00:48:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 55383b9b-afc3-3831-9e0a-abf2d3479b7e | -16.90897 | -51.85118 | 2026-06-03 00:48:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d6fcba0a-bdbe-35ef-bb82-9c74574b735e | -10.57123 | -57.32198 | 2026-06-03 00:48:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 17c327e4-0e8e-35b9-896c-233d912a040f | -16.14267 | -58.49636 | 2026-06-03 00:48:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 8d9dffd5-bb3a-3776-9699-5d6973acca3a | -11.7493 | -47.0822 | 2026-06-03 00:48:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |


[Clique aqui para ver as próximas entradas](README2.md)
