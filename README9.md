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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fd01acc-7883-310e-a574-5553aee2f66e | -17.3365 | -43.6383 | 2026-08-20 00:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 0de22201-9ab3-371a-9ffa-1cfe9eebcb55 | -11.1936 | -54.0199 | 2026-08-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 6549510c-f3c5-3162-b220-f1952ce9fa97 | -18.0285 | -44.6113 | 2026-08-20 00:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 341e731d-5189-3947-92e9-4a900f534b71 | -6.6014 | -58.9844 | 2026-08-20 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| a981b41c-ddc1-3d43-aa4f-32ba0eb30a9d | -8.654 | -54.6505 | 2026-08-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 46daae21-f9a3-30e2-8d9f-a64e37af3d7d | -7.9751 | -44.6648 | 2026-08-20 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 22962d53-0c18-3b0a-b598-e0bbc63f5ec4 | -11.1939 | -53.9993 | 2026-08-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 59aac52b-d55e-37a5-91e3-46339b1bd6f5 | -7.36 | -45.8361 | 2026-08-20 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 357.2 |
| 3dd2a0e3-f2c2-3069-bac9-677dd822eec0 | -12.4916 | -54.7364 | 2026-08-20 00:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 07eafc93-19e4-31d7-84a1-4ef88ad3d0c7 | -6.4392 | -52.7138 | 2026-08-20 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f8d0de68-08ff-3632-800b-e79dc2c08e1d | -1.8242 | -54.492 | 2026-08-20 00:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 86e92cde-af52-3c8a-bb76-461803d1345b | -6.4389 | -52.7548 | 2026-08-20 00:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d2f5ab69-08c6-3c4e-a88d-72b40df664dc | -7.9563 | -44.6667 | 2026-08-20 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 5664abac-93da-3291-80df-2620b82e17cb | -11.2189 | -55.0585 | 2026-08-20 00:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4716e377-9964-3752-827d-0d5ee2563f68 | -21.71554 | -47.16139 | 2026-08-20 00:45:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 84c3472a-894f-3009-9357-1136b00461da | -23.07318 | -49.16089 | 2026-08-20 00:45:00 | TERRA_M-M | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 4ab2ce23-126c-3a2d-8f30-14fedee234c1 | -14.21429 | -52.89766 | 2026-08-20 00:48:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| dd519f1e-43d7-3e0d-aa3f-030dfc34c2a8 | -12.47335 | -54.74273 | 2026-08-20 00:48:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8862dd66-2eb9-3b32-9898-09ab10067f9a | -14.02864 | -53.63628 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| bb3ebee7-fdd0-301d-bcc5-153c574c2f46 | -12.49574 | -54.73866 | 2026-08-20 00:48:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f683a0b0-cea1-3300-b77c-9dbe372b39b6 | -14.16361 | -53.06978 | 2026-08-20 00:48:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cb97bce9-8e78-3dd1-bb76-235a553645ca | -14.02224 | -53.67278 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 6f093d6a-72d2-3dee-b626-9cee0a00e75d | -16.50314 | -55.18801 | 2026-08-20 00:48:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| a34c276a-c64d-3d7e-abce-d10dfa200186 | -13.57577 | -51.68081 | 2026-08-20 00:48:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| be64dff2-60ed-36e7-b400-4187b842a71d | -19.04583 | -57.36043 | 2026-08-20 00:48:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 4b41907e-1730-3bb7-aaf0-288f089736af | -13.40644 | -54.3758 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6d7ec702-a675-3ed4-a6e8-2f4aedf038b1 | -14.1729 | -53.04865 | 2026-08-20 00:48:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 7d974d06-1357-3662-8012-70cd35dad20a | -12.95117 | -56.63811 | 2026-08-20 00:48:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5e4ba9e6-af85-30a0-871f-0f62ccd96a4a | -14.17601 | -53.06757 | 2026-08-20 00:48:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0b574426-1225-37ad-af85-09a682474519 | -14.01622 | -53.66747 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 20332b5a-3ec8-3b7b-aeb7-09224b9c6202 | -12.48454 | -54.74071 | 2026-08-20 00:48:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| eef8821f-f2c9-30ab-acc8-46ffc24f6670 | -13.44342 | -57.07444 | 2026-08-20 00:48:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| bdf1f9aa-ad07-37d8-b244-0c2e65616569 | -14.0195 | -53.65558 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 99841762-1e88-39c7-8281-a410d7faa595 | -13.43248 | -57.06551 | 2026-08-20 00:48:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1dd1e5f3-04c4-3ac8-885f-e322b691e6c6 | -16.07863 | -54.97498 | 2026-08-20 00:48:00 | TERRA_M-M | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a04501f4-663b-38da-9030-487c440a1621 | -13.58973 | -51.67816 | 2026-08-20 00:48:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6e7785ce-6fcd-3d7a-901c-16cfea822480 | -12.48691 | -54.75573 | 2026-08-20 00:48:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 200.5 |
| 62ffdaaa-5a65-34bc-8e08-bc3e9fea3da2 | -14.2267 | -52.89455 | 2026-08-20 00:48:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c7a484f1-9452-322d-819b-3e8c1ee8d8d6 | -14.02515 | -53.6479 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 431ccbb1-5d2f-3aa3-a557-631b90ec65cd | -12.48215 | -54.72557 | 2026-08-20 00:48:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ab3d042c-6490-3467-a109-0691630ed907 | -13.58021 | -51.6744 | 2026-08-20 00:48:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| abf70ca8-62d9-3340-8af2-bf8d6c4f5cfd | -14.16047 | -53.05079 | 2026-08-20 00:48:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| eb094d18-ce8c-38d7-bb02-d6dbd1749a7a | -16.50121 | -55.17575 | 2026-08-20 00:48:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 358ec671-cc70-3315-9cfc-418905c9b3aa | -13.4084 | -54.38211 | 2026-08-20 00:48:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 0725c84c-3d1d-3abb-820e-c22b6f6dc4ca | -8.6727 | -54.6492 | 2026-08-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.4 |
| f9b6f97a-cda6-3f3b-984f-78f7c4079f53 | -9.2071 | -59.771 | 2026-08-20 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 8ac4a02b-d951-3ff9-a7a2-45aad72801ae | -9.4071 | -60.417 | 2026-08-20 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bc61fd5a-d552-30ac-802c-b2c8b1c4e94a | -6.7114 | -59.0958 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ae0d14df-d944-3de9-930c-b47727b0f546 | -11.8377 | -58.8445 | 2026-08-20 00:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 0138ffee-f030-3be7-8cb4-baf528c77a8e | -10.2478 | -54.368 | 2026-08-20 00:50:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 9507f83c-d384-3957-883a-32e1608376e9 | -11.2189 | -55.0585 | 2026-08-20 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a6b3cf1c-7a64-3293-b455-67d4462efb82 | -9.207 | -59.7903 | 2026-08-20 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| e95b95ac-8644-3b86-87ca-c0cc47110925 | -12.4914 | -54.7569 | 2026-08-20 00:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| d29f4a0d-46e3-3879-a970-75c2cadd8f0d | -7.3603 | -45.8136 | 2026-08-20 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 279.2 |
| d5b969a4-86d9-3a3c-9dc9-0981ddf0e44e | -7.3413 | -45.8377 | 2026-08-20 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| bec0e648-d8fd-35be-a33a-243926d68919 | -14.4559 | -45.6019 | 2026-08-20 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 3788e95f-5668-303f-9444-93637c33b894 | -14.1607 | -53.0587 | 2026-08-20 00:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| f6026e7c-8c2b-3f1a-bfcf-e3e72cf560aa | -6.7123 | -58.9412 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 82f48cc7-5e33-30b2-b091-76d7a8787e66 | -14.18 | -53.0564 | 2026-08-20 00:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 013331cc-c487-3782-a4e5-760919a8b361 | -5.7904 | -55.7103 | 2026-08-20 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 30b09109-1a7b-3e0d-8125-9ffb115b04ed | -11.1936 | -54.0199 | 2026-08-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 7f1c2480-fbdd-36ab-b98d-8612e38bf0c5 | -17.3372 | -43.6139 | 2026-08-20 00:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 1aafead0-9f7b-3ac1-8dac-a7a8f9b505a7 | -8.654 | -54.6505 | 2026-08-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 30fa8d28-4d9a-3fbd-a85b-c470099bb3a8 | -11.2125 | -54.0181 | 2026-08-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6dab23a6-9216-31cc-b44c-dcc9f1089566 | -1.8425 | -54.4917 | 2026-08-20 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| f5b35631-e9ee-3880-9129-647b93ff6783 | -9.4256 | -60.4353 | 2026-08-20 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| d4a0e5bd-47ba-364c-a0d1-f69b5bb93194 | -8.5214 | -54.8814 | 2026-08-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| da805a63-2c3e-3c4c-baa4-eda00d64a1f9 | -5.8087 | -55.7293 | 2026-08-20 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 37bcf1d6-8222-3c07-a6f5-7d31a09ed86c | -9.4254 | -60.4545 | 2026-08-20 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 35119d37-b8a2-32bc-b037-2b268773e418 | -6.583 | -58.9658 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3026b2b1-190a-3622-9641-88e4aba0683e | -9.2258 | -59.77 | 2026-08-20 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| cb46590a-52c9-349c-9d1d-6579a0e04b71 | -6.4391 | -52.7343 | 2026-08-20 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 2ee20e7a-4f53-3b4c-b851-50c58c5f3777 | -23.0838 | -49.1511 | 2026-08-20 00:50:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 71.2 |
| c7214220-c036-3e8f-be70-9352c350af85 | -9.4069 | -60.4362 | 2026-08-20 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4016cbc7-dc5d-37f9-bdf5-2c9bc954a92f | -6.6938 | -58.942 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| b850b066-1e33-3a63-972b-bd29aa3f1dab | -9.2256 | -59.7894 | 2026-08-20 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 23cf4d89-887c-3487-b450-2c03b8073ea4 | -8.6725 | -54.6695 | 2026-08-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7976a8f2-6050-34f6-9b82-8b15abd29894 | -9.4257 | -60.416 | 2026-08-20 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 83cd7a32-f872-3a68-a0bf-527a05151f14 | -9.12 | -61.6011 | 2026-08-20 00:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 0176b64f-c0e3-3577-8459-7f4cbe74a7b6 | -12.4916 | -54.7364 | 2026-08-20 00:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 7ba44f0e-853a-3a81-8982-1a5b6b2bdc8c | -11.8083 | -44.8072 | 2026-08-20 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| a10e2f31-b107-30ec-a0ae-52cb58ba0d46 | -6.6015 | -58.9651 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 5e580034-3b93-3b47-bcde-575e9eab5606 | -17.3365 | -43.6383 | 2026-08-20 00:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 118.8 |
| f6f079c8-3ec7-3171-917f-0e29e82b96f7 | -8.6729 | -54.629 | 2026-08-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 818208ee-1cf9-311f-a869-334f628df468 | -7.36 | -45.8361 | 2026-08-20 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 310.2 |
| 061e6908-e037-3353-95b5-f595dde10716 | -2.5629 | -47.2445 | 2026-08-20 00:50:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| fa6e3161-2337-3f97-baf4-79efe7d8d199 | -7.9751 | -44.6648 | 2026-08-20 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 21647117-9e5d-34f6-aa67-6f02ec97f360 | -6.4392 | -52.7138 | 2026-08-20 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 8bc033a2-28b7-36fc-bb08-7a37b5216928 | -7.3415 | -45.8152 | 2026-08-20 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 205.8 |
| abb100bf-c01f-3499-9529-b21f16af4057 | -6.6929 | -59.0966 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f7c73872-6072-35b7-9794-468f6613a927 | -11.8275 | -44.8044 | 2026-08-20 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 5aadc772-d935-337c-9862-7c7c0f348094 | -14.4554 | -45.6251 | 2026-08-20 00:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 59e2c458-6473-397a-93ff-6a0671a51096 | -14.1611 | -53.0377 | 2026-08-20 00:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 1692305f-b509-35c2-8de7-2885841a55fc | -6.5829 | -58.9851 | 2026-08-20 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 5dc5f80f-971b-3e69-acc2-6866d824dbca | -11.2128 | -53.9976 | 2026-08-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9d0c06bb-eeda-390c-8e60-c31a4f44bc91 | -6.3863 | -54.9451 | 2026-08-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 61632bf9-9459-3a8e-bbcb-01966070f50a | -14.1797 | -53.0774 | 2026-08-20 00:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3795c116-c5cc-3b5f-b7ae-2af0aca9be84 | -11.1939 | -53.9993 | 2026-08-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 25cfa8ae-333a-3a3f-9dfd-faae8fea01f0 | -8.90046 | -60.5537 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| bea3a232-4c49-3deb-8033-1653851f1e26 | -10.24867 | -54.35794 | 2026-08-20 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |


[Clique aqui para ver as próximas entradas](README10.md)
