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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06e67372-16c6-3e98-818c-fa3c3419fd67 | -6.8939 | -59.4356 | 2026-08-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 185b9e9e-993c-3afe-84b3-774644bb959b | -8.9042 | -60.5385 | 2026-08-21 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| b10f18e5-840e-344a-b9a2-ff1af28342fe | -5.6168 | -43.9965 | 2026-08-21 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| aa99c73d-142a-3a90-8437-6a37777537e2 | -6.8755 | -59.4364 | 2026-08-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 320672a7-1e1a-306a-b539-c8272b63ec55 | -6.5829 | -58.9851 | 2026-08-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| a5875f30-9d00-3197-b7a7-64a78cd5f4dd | -6.2487 | -48.6506 | 2026-08-21 13:20:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 89862d4e-b0f1-3c05-a799-de21f200f283 | -6.8756 | -59.4171 | 2026-08-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e4ae8052-20e2-30ce-af81-4932741f9c98 | -6.857 | -59.4371 | 2026-08-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 10acd0d7-34f8-38c8-bf12-583d46646a86 | -13.3734 | -54.3779 | 2026-08-21 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 57545e5d-03d5-3407-aed0-c8f6a224b422 | -13.3926 | -54.3758 | 2026-08-21 13:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1af925ec-f027-3fde-b3ed-abf326eb1af8 | -9.4257 | -60.416 | 2026-08-21 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6c437060-8d59-35aa-a799-ead86be3609f | -14.3343 | -51.8944 | 2026-08-21 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 598f7b9d-abb6-31a8-afb2-bd21e9ea622f | -11.1747 | -54.0216 | 2026-08-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| c4ea33a0-842f-3cea-9e6b-a733526d0b03 | -11.367 | -45.9949 | 2026-08-21 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 0fc631f8-50a1-3c7a-aaf6-3275825d5742 | -9.4071 | -60.417 | 2026-08-21 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 1729ce90-9602-3e2b-b77f-0f2b9c59a923 | -19.6591 | -46.0388 | 2026-08-21 13:20:00 | GOES-19 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 1e595a1e-fe11-3d3e-af36-b2da3e183171 | -8.9041 | -60.5577 | 2026-08-21 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.3 |
| ec5014c7-d957-3811-a539-af61dc4f2f7b | -8.8855 | -60.5586 | 2026-08-21 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 60798072-1d7f-3ea4-8b60-be533bc818a6 | -8.8856 | -60.5394 | 2026-08-21 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d2448c29-b91e-3a8d-889d-029aafee7ddb | -13.7188 | -51.8675 | 2026-08-21 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3157f57a-3f0d-31b7-abe6-1f6e11827063 | -11.175 | -54.001 | 2026-08-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 45085a04-cb27-33cb-850b-45ab4542bdbe | -6.1177 | -59.9069 | 2026-08-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 4692d811-a54f-31b3-b94a-30a28f23c3ac | -6.1361 | -59.9063 | 2026-08-21 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| fbcbf709-5a72-3a45-86f2-f5f0ece595d2 | -13.2427 | -51.6508 | 2026-08-21 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b1472e66-bf5a-3e1b-aad9-1450d254ec00 | -11.3667 | -46.0177 | 2026-08-21 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| ec6f0a00-59ad-3727-b473-6cb84b702431 | -5.598 | -43.9978 | 2026-08-21 13:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 488.9 |
| b2a91f06-173b-3e42-b488-39059736e44d | -6.5828 | -59.0044 | 2026-08-21 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1dde48f3-fc96-32ed-9352-44436a324a34 | -13.4516 | -51.7736 | 2026-08-21 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8c256f26-a2f4-344a-9737-9ffd4cb45654 | -6.8756 | -59.4171 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 965f7587-51ea-365f-a61e-d4ed8955d2b6 | -13.3926 | -54.3758 | 2026-08-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| f7dc2329-1b4d-3a7e-b8d8-7b9abafa9703 | -11.3667 | -46.0177 | 2026-08-21 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 50c274e4-9fbd-32f8-a8d3-3b6b1ccb3885 | -6.1361 | -59.9063 | 2026-08-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 9adb86a6-67cd-3599-82cf-5a5c0d814c0b | -17.5978 | -45.8002 | 2026-08-21 13:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f9fbb187-f7ac-3a9c-98c5-53af87f8ea2a | -8.9042 | -60.5385 | 2026-08-21 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 3165974f-6c15-3e71-8979-2455910c2135 | -8.3902 | -62.7152 | 2026-08-21 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 71ee35dd-8249-3cb7-bece-91a2d12048b2 | -6.1177 | -59.9069 | 2026-08-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 27d23be5-76f2-3829-88f4-2d430b60902c | -6.8755 | -59.4364 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 729f1165-9fea-35b4-93fa-177df94c5764 | -8.9041 | -60.5577 | 2026-08-21 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 1d1e20cb-8b18-3fde-aacf-0b6f6b7acbcc | -11.175 | -54.001 | 2026-08-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6b587f24-6b42-33e3-a52e-c055cf6d3565 | -13.7384 | -51.8438 | 2026-08-21 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 2b55dc02-eed5-3782-9e16-a02176f355a3 | -8.3718 | -62.697 | 2026-08-21 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.3 |
| cb0698d9-6b0b-3309-a8fc-6d50f2805265 | -6.2341 | -55.6109 | 2026-08-21 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 49d25713-248d-3bb8-8bc5-a69583c889cb | -8.3903 | -62.6963 | 2026-08-21 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 18679288-74e8-310f-b901-46b2bc1357d9 | -8.3717 | -62.716 | 2026-08-21 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| d468549b-d93e-3ae1-9702-0d5fdea4d6bf | -6.857 | -59.4371 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d2672cf8-f1a8-3432-8fe7-4eaf51706214 | -9.4071 | -60.417 | 2026-08-21 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 8a952bc6-2f21-39a6-9aed-3293f740b01b | -6.2487 | -48.6506 | 2026-08-21 13:30:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3050a42e-d702-30db-9882-ce6eebd23e55 | -11.367 | -45.9949 | 2026-08-21 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 221.6 |
| aa7c57f8-132a-3b00-a2e1-7b768d6a996e | -6.1362 | -59.8871 | 2026-08-21 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c48ece30-4a42-3362-b085-f99c83aa5faf | -8.8856 | -60.5394 | 2026-08-21 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 441d41ff-8d41-3b19-a381-5cb4cb5f4e2e | -6.5828 | -59.0044 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 219ed86d-56b9-3030-a95a-6d17ad001061 | -13.7188 | -51.8675 | 2026-08-21 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 516ea89e-56df-390b-80e0-d24ecc69c651 | -13.3734 | -54.3779 | 2026-08-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a51f2b9f-8c90-3bc3-b675-d4142a383dd6 | -5.598 | -43.9978 | 2026-08-21 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 332.0 |
| 242eab58-5e08-3b03-b3ce-8a3975fb02db | -9.4257 | -60.416 | 2026-08-21 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| bed30172-9605-388b-a8f0-3962107acc5a | -5.6166 | -44.0196 | 2026-08-21 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 264.7 |
| f4616370-465c-3e49-af70-ce4e43f69e43 | -13.6624 | -51.7897 | 2026-08-21 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 64c58710-f0b4-35e0-8846-2f011f4686f6 | -8.8855 | -60.5586 | 2026-08-21 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 5bc7b014-a6b3-3917-ad77-b2e358a84b25 | -5.6168 | -43.9965 | 2026-08-21 13:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| eab3541b-e865-3a26-bb5c-bc0110fee4bf | -5.7854 | -46.1168 | 2026-08-21 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 8a986fbc-a284-3efc-a9d7-0aa0c99beec3 | -6.6014 | -58.9844 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c68c6c69-e796-3322-999a-515b0ebe6f2b | -11.1747 | -54.0216 | 2026-08-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 55fd8b30-a553-3d9e-8da5-7545d0feb325 | -13.6243 | -51.7732 | 2026-08-21 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 410fcf5a-1968-33ef-9423-86765349e78e | -6.8939 | -59.4356 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 5e32dba5-bf91-3f8a-bfa2-1823c35176f8 | -14.3343 | -51.8944 | 2026-08-21 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 5b0f860a-b9fc-3dad-adfb-4fcba1b926a1 | -6.5829 | -58.9851 | 2026-08-21 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 154e9e12-6c68-33ab-b109-a1a9b258ebfb | -9.4072 | -60.3977 | 2026-08-21 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d9d831db-ba41-3ffc-95d6-9bdcb293f045 | -11.175 | -54.001 | 2026-08-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| d78006dd-aaa2-30af-a4ee-2d0de9b33bc8 | -6.8571 | -59.4179 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e7fb795f-420e-3a64-a76b-43a5723fafc1 | -13.3734 | -54.3779 | 2026-08-21 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| ea9cf124-b685-3289-868a-63c97aa7ec16 | -5.598 | -43.9978 | 2026-08-21 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 15488222-8585-31dc-807b-ea69183032a0 | -11.1747 | -54.0216 | 2026-08-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 46b2cfda-189f-34a9-97fe-1ccf6c8001d6 | -13.2431 | -51.6295 | 2026-08-21 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.9 |
| e626e76c-97e4-3502-8131-71a490b21ced | -17.5978 | -45.8002 | 2026-08-21 13:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 651af4f9-01d9-33b7-be22-d338bee0c023 | -6.2487 | -48.6506 | 2026-08-21 13:40:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5851c5b0-7d86-3e9d-88b8-890bb75c88e4 | -6.8756 | -59.4171 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2b1d17f4-4215-399c-b67c-76e85dd93948 | -6.8939 | -59.4356 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1773ab02-bea6-3659-9047-618efa8e236d | -8.3903 | -62.6963 | 2026-08-21 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c5e9ad9e-9321-34e0-91e5-a29ff6e641ac | -8.4554 | -46.9628 | 2026-08-21 13:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 4d6ebfba-7beb-342a-b354-b6053b59f488 | -6.5828 | -59.0044 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| f62601ae-5dbf-3dec-85d3-7408c25b4161 | -6.1177 | -59.9069 | 2026-08-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 49ae9441-2d9f-3817-ba8f-42172067db84 | -6.1361 | -59.9063 | 2026-08-21 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 61a18ddc-db96-336c-a270-316b357d33b2 | -13.7384 | -51.8438 | 2026-08-21 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 567e44af-05ea-3d43-92db-e8688da0c883 | -5.6166 | -44.0196 | 2026-08-21 13:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 267.8 |
| b17e594c-b931-3471-ba03-18c012ecf200 | -9.4372 | -48.2518 | 2026-08-21 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 7b949383-6748-3792-9391-9cb2cce9d389 | -14.3149 | -51.8969 | 2026-08-21 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| adedfd2b-aae1-3262-96d0-fb438e2ec7dd | -8.9041 | -60.5577 | 2026-08-21 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 3aa6ce4c-f7d0-32c2-abca-bbec33e03473 | -9.4072 | -60.3977 | 2026-08-21 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 48e6bf6f-bd98-3385-9ca2-b6d2e613cea4 | -13.7188 | -51.8675 | 2026-08-21 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dd655aa9-6d1c-348a-bf8f-b59d520a4700 | -13.3926 | -54.3758 | 2026-08-21 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 84c40367-5cd2-3042-9d59-cefa71687f2f | -6.2341 | -55.6109 | 2026-08-21 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 83f33a57-fb44-3f25-8df4-0cacfbdf6dc9 | -8.8856 | -60.5394 | 2026-08-21 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| c03bf360-eabd-32fd-bc96-1498be6c6586 | -7.0191 | -48.0323 | 2026-08-21 13:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a779e72d-95c6-34b7-bbc7-19ca13c4e18b | -14.3343 | -51.8944 | 2026-08-21 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ca6cc7ab-0350-33ff-b9ba-02c99c8025e9 | -6.857 | -59.4371 | 2026-08-21 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8f361fc7-b306-38a8-a204-7638c68d0d63 | -8.8855 | -60.5586 | 2026-08-21 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| c80ae4e2-4a82-365f-8a64-56ee7e871dcb | -6.3654 | -58.3354 | 2026-08-21 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e53c86c8-22ff-35f1-bc4c-aea3726e7b41 | -8.9042 | -60.5385 | 2026-08-21 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 18603a25-75e8-3abe-ab1a-270e39dca04a | -8.3672 | -46.4816 | 2026-08-21 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ca46e63d-1b48-3e8e-b021-82ada4270d2c | -17.9546 | -44.3882 | 2026-08-21 13:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |


[Clique aqui para ver as próximas entradas](README92.md)
