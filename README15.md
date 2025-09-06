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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50360bc2-2d06-3b7e-a84b-67ddad51075f | -9.71108 | -49.50661 | 2025-09-06 01:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 202.7 |
| a31bdaaa-d5b5-3444-901d-f2c44061994d | -9.23986 | -57.07483 | 2025-09-06 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2483f661-fdf1-395f-b605-d271522fe2d4 | -12.19179 | -53.90264 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| cbcaf043-184e-3d78-8385-458155d1137b | -12.96059 | -54.79072 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 459381b6-e8d5-300f-b8f2-771a919f0b49 | -12.48063 | -53.84946 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 27779e6a-4d81-3a2e-861d-491f33bf168e | -16.30002 | -50.48992 | 2025-09-06 01:09:00 | TERRA_M-M | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| a68c4fdc-4ada-3e85-a211-988d16e442f8 | -11.21597 | -55.02037 | 2025-09-06 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 464a2ec0-9773-3e16-8f9f-8e8e2a7a57d9 | -11.22304 | -55.02364 | 2025-09-06 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 282ce1ed-cbf3-3a3e-9270-a18fb768c7fe | -15.57487 | -52.89396 | 2025-09-06 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 96ca3df7-e5dc-3291-97f2-b1ee8c2c9edb | -12.50185 | -53.85761 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ef8577f6-a595-3944-a614-65d8a3ce8b15 | -15.4545 | -47.13151 | 2025-09-06 01:09:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ad597474-62f2-371e-ab61-80cc457a77a4 | -9.32493 | -55.22507 | 2025-09-06 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9598c394-0aef-3f57-9d5b-e41e8e161f2b | -14.25561 | -52.19026 | 2025-09-06 01:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 96b4b8f9-516c-3570-829b-a57bf1cee2a8 | -9.68462 | -51.08932 | 2025-09-06 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| adb05b3d-c0e2-3efa-a1bd-fa51775b1cd2 | -9.24258 | -56.90098 | 2025-09-06 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 151dd06b-fe29-3454-b79a-6ede716f5601 | -9.68732 | -51.11477 | 2025-09-06 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 483b2a80-ddd0-32ed-9167-f1b9708f29d2 | -9.24384 | -56.90995 | 2025-09-06 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 990d03c0-91d5-35d7-90d2-238d47660cec | -15.58023 | -52.92902 | 2025-09-06 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 4cdea4aa-00eb-3d86-99f6-2935e49e8e15 | -15.18652 | -52.37728 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| df71684c-e058-39b2-9d72-ec3d225ae0d0 | -15.5901 | -52.92718 | 2025-09-06 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| ec5d94db-d1db-33ad-8264-15572b8b352b | -15.07145 | -48.13184 | 2025-09-06 01:09:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 29.6 |
| dd25312c-155b-3d72-abbb-00f1da2a70e9 | -12.52264 | -53.84839 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| b2bfc441-a6e7-38ac-9522-d26a602e5a57 | -11.18168 | -55.04602 | 2025-09-06 01:09:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f24040b5-1770-347f-bb30-cc7e6be600e5 | -15.58831 | -52.91538 | 2025-09-06 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 0001e3dd-6df7-3658-abc3-177bd4e8ee44 | -12.51972 | -53.84327 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 1b671199-b030-3b1d-9015-f0a00972e581 | -9.68783 | -51.10888 | 2025-09-06 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| dab70853-2c6c-3612-b217-c1cf4aa1c59f | -14.85135 | -48.19791 | 2025-09-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 28f47dad-5dff-3aee-abc7-8274f80b33f0 | -11.2174 | -55.03032 | 2025-09-06 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 357d4404-a293-3ff6-b5b5-a4f784b1983c | -7.79652 | -52.13812 | 2025-09-06 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 467a29da-f6aa-3b33-96d9-c4e65154b1cb | -12.96495 | -54.8203 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7995a862-ff46-3a38-8d4e-dd4651394606 | -13.01392 | -54.83296 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 05d1ad82-471a-37ed-be34-9bbfe961638c | -15.57667 | -52.90577 | 2025-09-06 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| b42d183b-472d-34b0-9b95-97a8e405ce51 | -12.98701 | -56.91661 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| de7918b2-fb0f-32dd-a336-b45c56ce743d | -9.57186 | -57.74961 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0798a89c-4254-36a6-b29a-9ec60a0810d9 | -11.64164 | -54.54113 | 2025-09-06 01:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| b0b3c69a-894b-3047-9e42-27e34d729353 | -12.49208 | -53.85914 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| c2d928a3-5656-39ad-b39c-5118532d49a5 | -9.46842 | -60.52383 | 2025-09-06 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f7c63721-ffa9-34cf-981a-527e7d9fdb8c | -8.09792 | -55.72986 | 2025-09-06 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 81c46c29-1c56-3c77-ac70-eaca929cb3e6 | -11.20667 | -55.0218 | 2025-09-06 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9c4387a1-c8e6-38c2-8b3a-6c2a02de7c2d | -15.57845 | -52.91741 | 2025-09-06 01:09:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 200.2 |
| caae6a39-0888-329c-bc1c-34ad71baf63f | -12.48231 | -53.86065 | 2025-09-06 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 9e362647-a080-31dd-b636-fbbbc1d9c231 | -15.73586 | -53.60397 | 2025-09-06 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 6949bd66-3bba-3bc6-822e-84da39095d00 | -15.43367 | -52.97132 | 2025-09-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| eb2a138c-e087-325a-9077-8a453fcc1cfa | -11.47678 | -55.55523 | 2025-09-06 01:09:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ee00f46b-924b-393c-8435-f0f01a8d851d | -12.95136 | -54.79213 | 2025-09-06 01:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3a538e0b-72ec-3435-8478-7cb24cd43500 | -21.377 | -51.7464 | 2025-09-06 01:10:00 | GOES-19 | SANTA MERCEDES | SÃO PAULO | Brasil | 3547106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.2 |
| f872646c-e203-3ff4-a810-8bb7309e6fd5 | -9.723 | -49.4806 | 2025-09-06 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 57c03a4f-d520-38d9-9810-b23c6cc3ab1b | -12.4843 | -53.8732 | 2025-09-06 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1239a74a-405e-324a-802d-1b310b88eca4 | -6.5393 | -49.5101 | 2025-09-06 01:10:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5787c6b2-3dad-36a5-926a-216781683a8d | -12.5033 | -53.8712 | 2025-09-06 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9402ac36-41ac-37e0-bc64-c49ff2f55ded | -9.5347 | -40.3033 | 2025-09-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 253.0 |
| 30323f3d-ed42-3b31-b0fa-4404681713aa | -9.7041 | -49.4825 | 2025-09-06 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| f4bcec86-0bb6-3bcd-aac2-bf92a628bd03 | -4.5031 | -42.8854 | 2025-09-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 843.5 |
| df2f0dca-6c3a-3db4-9a2b-7b736320f758 | -5.4917 | -60.138 | 2025-09-06 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 1784ea3b-d6e8-3b77-ab04-c11e68445233 | -15.5942 | -52.9149 | 2025-09-06 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 145.8 |
| c9a4d271-2df8-385f-89f5-35c67a209929 | -10.5937 | -44.331 | 2025-09-06 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 3b55c1ff-f154-3832-815d-1c325eb27f16 | -12.9665 | -54.8116 | 2025-09-06 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| dd11864e-2cec-3c26-a48a-eff6b748795d | -12.5227 | -53.8485 | 2025-09-06 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3968a6c7-f785-3a05-9d03-03997aa4a321 | -15.5747 | -52.9175 | 2025-09-06 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| cd2aedc8-9342-3b87-92c1-d3b20bd55702 | -9.5534 | -40.3254 | 2025-09-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 119.3 |
| e2ec412f-7aff-372c-9e47-56046f6a9024 | -10.6128 | -44.3284 | 2025-09-06 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 0e183b03-159c-31e8-a3a6-6353bb9e8db2 | -15.5938 | -52.9361 | 2025-09-06 01:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 0a968482-6d64-3e35-acee-de33a39c8f5c | -15.7186 | -53.5743 | 2025-09-06 01:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 216be9f2-91c3-3e6d-a8f6-d3b71356055f | -12.4846 | -53.8525 | 2025-09-06 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 73721ec5-4258-36f5-a21e-9cc95c7a994f | -12.5224 | -53.8692 | 2025-09-06 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 76259f80-b657-332f-9a5f-682bbc295a65 | -10.6131 | -44.3051 | 2025-09-06 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 928a4d6c-3851-3a89-a22b-f79885cfcc9f | -4.5033 | -42.862 | 2025-09-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 9f2d89f2-1b3c-3157-9720-78451984335a | -22.2633 | -48.7463 | 2025-09-06 01:10:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.2 |
| c6ade13c-3791-3a9a-b89d-457285f55bfb | -9.5538 | -40.3005 | 2025-09-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 56cb5477-2807-34ee-a2a4-a935c930e040 | -9.5343 | -40.3282 | 2025-09-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 312.9 |
| 078f8b61-a28e-326b-bfbf-e32a4917b015 | -14.9015 | -49.454 | 2025-09-06 01:10:00 | GOES-19 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c459f886-00c6-35c3-8a61-9e4351c6d2b5 | -9.5152 | -40.331 | 2025-09-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 054e9391-8ca0-309d-892b-614ee4726dd1 | -3.2331 | -50.8087 | 2025-09-06 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 19deaff5-20fc-3afd-84fc-cfe0d40b0a1f | -21.3976 | -51.7423 | 2025-09-06 01:10:00 | GOES-19 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| f48fed8f-2476-3bb9-a79f-dde7b9265fbe | -4.5029 | -42.9089 | 2025-09-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 200.9 |
| cfc1ffa8-b722-3886-b49b-e6198dcbcee9 | -22.2424 | -48.7513 | 2025-09-06 01:10:00 | GOES-19 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 141.7 |
| 937ea258-d440-3831-a719-65de2c01f752 | -12.5036 | -53.8505 | 2025-09-06 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0c1f6658-dc00-31dd-8fbf-d85e193e2b50 | -13.0044 | -54.8282 | 2025-09-06 01:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ba309c4d-e0e8-3c79-a563-d088b5a1bb31 | -9.7227 | -49.5021 | 2025-09-06 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c4042f44-aa78-37cd-a08f-363d69d642e1 | -3.2516 | -50.8082 | 2025-09-06 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 619fdce2-cb1f-354e-a08e-cf7e95c502a5 | -9.5156 | -40.3061 | 2025-09-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.0 |
| f3efba88-66fb-3d71-ac8f-52fe538e51d3 | -4.4844 | -42.8866 | 2025-09-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 9db045ae-d936-3e1c-854a-a46f6f64e685 | -4.5218 | -42.8843 | 2025-09-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7ea4ca56-e8c3-3f9d-b06b-d193a91519dc | -9.7038 | -49.504 | 2025-09-06 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| be7d3366-bf4a-306a-be46-819a395df1d1 | -6.81749 | -52.80776 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6fba6ba8-cfb7-3ec0-9461-726238d976ad | -5.10814 | -56.14239 | 2025-09-06 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 90b6fa79-516d-3877-a723-8c877adce321 | -5.0685 | -56.06555 | 2025-09-06 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 57383ed0-50f0-3d51-9da4-790ae5c2af16 | -5.9506 | -53.79707 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 0da65af1-0ed3-3b3b-9666-a888cf794f61 | -5.96907 | -53.60177 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b923e2fb-6038-35e9-b01c-50938a397d33 | -6.43501 | -58.11525 | 2025-09-06 01:11:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 44336ba1-30d0-3b3b-be23-fded4b5de6bb | -5.00599 | -56.03309 | 2025-09-06 01:11:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3fba1e90-c222-369f-8712-51eb974522af | -4.38086 | -48.07572 | 2025-09-06 01:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 400e7e01-16c5-3e63-a549-63c21427697b | -5.69083 | -53.7549 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 048a65ab-2fdd-3425-a954-befe350b5c6f | -6.18331 | -53.26614 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e35747cb-733a-38a7-823c-c1105ac192a0 | -3.32733 | -54.90929 | 2025-09-06 01:11:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bfe90910-1776-3365-bba3-9c2c0b5249ba | -5.95261 | -53.81091 | 2025-09-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b3407a41-3c64-3410-b541-ace7aadc7c0a | -6.80588 | -52.80948 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b1640e41-2696-3b36-8ee4-87111aaf031d | -6.81981 | -52.82341 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1a5d2d0e-6b8b-3059-9da5-2f55f64b5d39 | -3.25118 | -50.812 | 2025-09-06 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c71acdd0-8353-3890-b062-b6fae7c9850f | -6.19232 | -53.24925 | 2025-09-06 01:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |


[Clique aqui para ver as próximas entradas](README16.md)
