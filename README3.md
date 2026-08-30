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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e74441aa-8011-3f82-9319-cba865a0bb59 | -7.5182 | -55.332001 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 203d0c2c-9191-308f-8472-7e55c576a2f2 | -9.3119 | -56.789902 | 2026-08-30 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee7de878-8f3d-3dcc-90ed-828f17e3dc71 | -10.5667 | -59.600601 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6f361d2-568f-33d2-a21f-6526a2ce5832 | -3.5953 | -55.293598 | 2026-08-30 00:32:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6a4724-a53c-370b-93c0-369a1eaacd60 | -8.4963 | -55.2868 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d8dc76-07dd-3ffe-8ca2-85901ee285cf | -4.1487 | -60.6674 | 2026-08-30 00:32:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aed7f6c5-86a8-32af-a59d-dd0610d5d847 | -9.9351 | -60.4874 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e97b428-308c-3d2f-b6d6-f291e191f60d | -7.0747 | -59.712502 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27b5d9d3-c277-3cf6-baea-77f62f2f6183 | -11.0414 | -57.243 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77c1537b-daad-3102-bc08-0900b4d13f5c | -9.6688 | -55.052601 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0d72fb3-392a-3e44-90a2-f825cdb43c88 | -6.1176 | -57.680599 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe5f0187-1ab8-33ec-ab32-82fea3b8fe97 | -15.1252 | -53.5788 | 2026-08-30 00:32:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e3bf9e68-8ff2-38ed-b011-2abecd246726 | -8.6188 | -54.685902 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0eea713-303a-3ad7-a8e0-fc5bb3315b88 | -9.9377 | -60.499599 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5db46937-8162-36bd-b92e-fcbd53b69133 | -19.480101 | -57.543098 | 2026-08-30 00:32:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cacee47f-f465-389b-ac18-8bad62420aec | -10.5743 | -59.587601 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81463cd1-5a74-3ed1-a5ad-e29c4bf2df58 | -9.8881 | -60.2607 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1017a9db-7222-351f-8f51-8f3bb3a847bf | -7.0629 | -59.7048 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 493120cc-9ccc-3bea-bc7c-a54e00016093 | -14.4115 | -52.5504 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c250cfcb-b7de-395b-9334-8eda15432889 | -7.0886 | -51.5681 | 2026-08-30 00:32:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9bf77d7-196b-31d9-8e9f-2b378dfe80fa | -14.5888 | -53.063702 | 2026-08-30 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 72e722f0-a687-3dfa-a399-a7c7dd6530ac | -9.6064 | -55.095901 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e91bf12-c745-3303-8efd-1ff3e464f941 | -7.0788 | -51.5704 | 2026-08-30 00:32:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae8716d3-2796-3e3f-b118-ba2edc55d6f5 | -6.9047 | -58.975399 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df769653-2c1c-3834-98b8-a619be5b1f74 | -7.3685 | -55.1703 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8d3ee6b-01c5-3598-bb79-590063248c4a | -6.935 | -55.7159 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af96014c-b0f5-3108-a3f0-e1b72c1aabc6 | -9.2821 | -57.076599 | 2026-08-30 00:32:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07402581-df4f-3303-a10b-42d876b279a0 | -8.6092 | -54.826 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01cc8713-f1e1-3a08-bdd3-4983d1502958 | -6.7087 | -58.546799 | 2026-08-30 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78721de3-7bcd-33b7-a092-fdbdd682633b | -5.7529 | -51.6745 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9961cb10-0fb0-3460-9ab6-cbd202a533aa | -17.597 | -51.592098 | 2026-08-30 00:32:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 071daf0c-711c-3236-9f34-cd5536faf431 | -7.5931 | -61.3256 | 2026-08-30 00:32:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2cd88139-7278-363e-ace0-3034d201a548 | -6.7663 | -55.6521 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d40abd-d1a4-3fda-b90b-0d8d2995f882 | -9.0132 | -57.539299 | 2026-08-30 00:32:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8b79f1-01fd-3f6d-bbc2-c6b3bdfd479c | -10.7364 | -50.673401 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00104e53-ab67-35f2-ae92-254eef8e40e0 | -9.0747 | -60.4673 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7fb2f10-4916-3dad-90c4-1ad1aa8fa7f6 | -6.8764 | -56.5592 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0ce2ea-c58b-30e1-bdd6-345c132b069f | -10.3406 | -49.9641 | 2026-08-30 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da64573b-80f7-31a2-9051-794be5ee5d8f | -7.5629 | -61.278999 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf20e694-56da-3787-97f0-8a4743288f9b | -9.1527 | -59.480099 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84708b73-67c7-30ef-a42c-50de32820ed0 | -6.771 | -55.672798 | 2026-08-30 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7456aa-90f9-303a-9ab2-fc04e88981c8 | -6.491 | -53.260601 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13733330-6ad0-322a-8dee-34d67b812520 | -5.8585 | -57.532001 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32bd2fe3-5615-3ea3-bac5-7602796ccf60 | -16.3545 | -50.986301 | 2026-08-30 00:32:00 | METOP-B | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd675b0a-da24-31f4-b414-0143959c23a2 | -5.2574 | -55.902 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a830859-fb7e-3bee-b2fb-56599d4cfbe2 | -3.6836 | -51.989899 | 2026-08-30 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 687a6ac1-d380-3814-8926-93497cc02028 | -7.3411 | -55.140301 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0102bea2-165d-3784-a2f7-14d383c5b0f5 | -6.0798 | -57.881901 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97e84c0b-adc6-39f9-aa9c-c6dae9186220 | -5.9736 | -57.680401 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82d062b7-9f8e-391f-954f-9a29fbd5d938 | -5.9932 | -57.676102 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff88341c-5724-3e01-802d-0b4854191c16 | -4.9565 | -55.8465 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dc1e2b3-8d5e-3361-8201-300e4cfcbf4e | -11.0298 | -57.2369 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb5456d3-89c5-3724-bac7-8419dca85c07 | -2.7912 | -49.566601 | 2026-08-30 00:32:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16b1a922-0fad-3345-ae17-2846b69cc265 | -10.4818 | -59.584301 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a29a4658-da87-3b58-b56c-a75b9e3ff6d5 | -6.1608 | -57.783401 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa248a36-c94f-3258-9699-8d551e267606 | -10.4863 | -59.605999 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f91849a9-6451-3db8-b2c5-16d1db67fd63 | -4.9519 | -55.826 | 2026-08-30 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ab51a05-ec41-38d2-bcdb-2cc75484e9d8 | -8.6065 | -54.768501 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eacd893-e906-30db-bfc2-9a6ec99489c7 | -10.81 | -50.504601 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b3219ee-e36d-3a9b-a453-a4e2a8da0ab2 | -9.6637 | -55.075699 | 2026-08-30 00:32:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fe6ba60-d2a1-36e4-8139-2b3b7744d7e4 | -8.6081 | -54.775398 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a90846ae-1bdf-3e1b-831f-8ce381481d1c | -10.7505 | -50.864101 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df7046a7-9807-343a-8a75-de72493f2d8d | -9.2174 | -59.738201 | 2026-08-30 00:32:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95dd5edd-4213-3e0b-a3cc-4efa5583880c | -23.153 | -48.664001 | 2026-08-30 00:32:00 | METOP-B | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 47192873-7010-3da4-899a-fb7425d4f0e4 | -10.7266 | -50.6758 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5ec7881-66d7-3f89-b220-2e64d682cc73 | -7.5727 | -61.277 | 2026-08-30 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4950b7af-5507-3a81-93d6-f8ee0efd1ecc | -14.1664 | -52.834202 | 2026-08-30 00:32:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f40a447-6b55-368f-91d5-6f8afc361d88 | -13.8265 | -54.034698 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8a22f5a-cfa9-31fc-98f2-ac84a1895146 | -10.7386 | -54.036301 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf2c1a8-fbe3-35be-87c1-cd51b2ec9c03 | -3.7584 | -59.321098 | 2026-08-30 00:32:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 464a0cde-8033-32f5-97c9-bb7771c1b561 | -7.2913 | -60.5784 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d467ac32-1d7b-309d-9a9a-48c6427d71d4 | -10.3504 | -49.9617 | 2026-08-30 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a93ba0e-346a-3577-91d9-ea5a83d202e5 | -2.7943 | -49.579899 | 2026-08-30 00:32:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec3814c-51f4-3a32-b3b2-10d89116c2b1 | -10.7371 | -54.0294 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f999503-306c-3b7b-a5eb-d8e25239bb83 | -13.8347 | -54.025398 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5a23b82-fa2c-3fe6-9f9a-f022cbdf7184 | -21.314699 | -51.3018 | 2026-08-30 00:32:00 | METOP-B | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 282411ea-f9df-38f4-95e7-a42b1bc1e8cf | -9.4208 | -51.573799 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9073790-1f2a-3137-baae-3fe01eb551b1 | -4.6867 | -55.655102 | 2026-08-30 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c36f405-e34d-39c1-86e3-f1f8a7f1480f | -12.5635 | -55.734402 | 2026-08-30 00:32:00 | METOP-B | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ddc22b5-811c-348c-ad18-65f454ef6fab | -13.8421 | -54.1054 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7001d215-858e-39bd-aa9c-7b3e2ce54065 | -14.9117 | -52.620499 | 2026-08-30 00:32:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c46bd8a5-7706-3591-84bc-f5301f8e046d | -10.4938 | -59.593102 | 2026-08-30 00:32:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b88c364-3444-3713-b32a-064dd2b45ead | -11.0459 | -57.216301 | 2026-08-30 00:32:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1292f0d5-bbc9-31da-9d11-7d735684a45c | -13.8549 | -54.117199 | 2026-08-30 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9405f312-f26d-3daf-8922-bbbd60aeeb67 | -9.0115 | -57.5313 | 2026-08-30 00:32:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9a0d9d-4a7d-33a3-a4a7-6e2cfaeccc82 | -6.1689 | -57.773499 | 2026-08-30 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5507d820-a0dd-3cdb-a355-5acabc7178bc | -10.7488 | -53.990002 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d92ccf2c-683b-3faa-a7fe-9f996e7619fc | -8.6163 | -54.766201 | 2026-08-30 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b011ee91-2a13-3b99-ba3c-29baa48afb5c | -9.0625 | -65.380699 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0426804b-fd76-3bfb-8161-61a946800e17 | -10.7504 | -50.688702 | 2026-08-30 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db20abf1-489b-39c0-8f88-f7f55ce72729 | -6.9479 | -58.938301 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88874829-e511-37f8-9330-e4836b878130 | -10.7696 | -54.036598 | 2026-08-30 00:32:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96e97a02-b0c6-3695-a07a-316d78e99ef9 | -10.9985 | -50.5158 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c4887c9-f379-34c5-83e9-9d063d86d836 | -10.665 | -55.136902 | 2026-08-30 00:32:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5aae5b1d-c808-32f7-86fb-17684a0aab31 | -9.0528 | -65.382599 | 2026-08-30 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee47c346-3938-311e-96c7-95f494bdef4d | -6.4991 | -53.2509 | 2026-08-30 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37770af1-6cd9-3bb9-adc2-28034d0a8bb9 | -11.7208 | -54.515499 | 2026-08-30 00:32:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7623ee3b-413e-3970-ac16-71661edcdaca | -10.7492 | -44.845501 | 2026-08-30 00:32:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 469150c4-e8a4-3503-8d93-fc8068705dd9 | -11.0006 | -50.5247 | 2026-08-30 00:32:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6a71726-079d-3565-847d-4e90fed99fe0 | -7.3035 | -60.587502 | 2026-08-30 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
