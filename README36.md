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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55ae5788-3e9c-3563-9718-01abd6c96243 | -6.62952 | -59.07233 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 50052cef-e44b-35f5-acbe-bdbf1ad1f5d9 | -11.87794 | -51.94944 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f310613-ad5c-3e96-a2f4-6031fb82deb7 | -11.07859 | -47.28128 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9947c77b-94f3-362c-8b71-055fd1b2bd17 | -6.81984 | -56.46155 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 161dd60c-2ac3-3696-ae45-27e1cd1941e0 | -6.78647 | -55.84098 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a1f805e-385e-3fa8-bbf8-dfc2d7ff2577 | -6.62931 | -59.05093 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d34a46a5-17aa-3f1b-9cf5-17a4fd8f01f2 | -11.2096 | -54.8214 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48b377bc-d96d-3c4b-81ec-6b7afad228be | -6.62998 | -59.04677 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afa4e2c8-aa2b-32ab-b55b-ae215ceb2d54 | -8.96314 | -60.51192 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d623b73a-c7d1-3440-8f70-a7fe17759535 | -8.89529 | -60.59823 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d584c86d-2601-3a3c-afa2-ff6a4216e65c | -6.85996 | -58.96438 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99125bd2-37ef-3aaa-b260-9e20790060f6 | -9.27133 | -56.9054 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a42b7686-c6cb-341b-bb4d-64350e40afae | -6.36596 | -58.32071 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3a793dd-812b-3027-9d81-77977b96ee13 | -6.63802 | -56.39286 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ff3cb2f-a94c-39b8-a02a-7c30b58ff9f3 | -10.27578 | -48.29478 | 2026-08-16 05:16:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 865f8b7f-6ccc-3945-a553-98cf2f478335 | -11.48426 | -46.60359 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f99a4b0-9d0c-3890-86f5-dae328b67066 | -6.8215 | -56.45111 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 929520a3-1254-30de-a3e1-9baa9060851a | -9.37288 | -62.36465 | 2026-08-16 05:16:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c5e6c5c-b0a2-37ca-a041-7ccd8755b02e | -6.8508 | -58.97549 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9677d1be-a3bb-35c8-a91a-b76a52952e59 | -11.22407 | -54.81967 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b8e7539-d4b3-34f6-b801-a36a59780d6e | -10.53485 | -44.85538 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 326660ef-b00f-3fb9-8d31-ed6ca4e14f4f | -6.92998 | -43.63942 | 2026-08-16 05:16:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de9a71e8-c006-378c-a18e-f8933524208d | -8.79846 | -45.79177 | 2026-08-16 05:16:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43692d28-5eb5-3567-b8db-d04f1418ee54 | -6.64796 | -56.43414 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 457e5b34-034d-36a1-bdf8-fdde60bab281 | -7.78781 | -56.29216 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d99935f-5ea0-375f-9e8d-3d7a9dcb4a56 | -6.86192 | -56.4326 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d38a0e8e-b79f-3212-863c-8555830e895e | -11.80084 | -51.78792 | 2026-08-16 05:16:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 443636d2-fc98-300a-9f00-c580fcac9b24 | -12.03968 | -46.44372 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e5f8534-92b1-3289-83d9-3c0d221e8cd9 | -6.10865 | -57.71743 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 11fd34ec-0f66-30ae-9322-d95f93450f56 | -8.64466 | -54.7159 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbc6b4c0-4a36-35c6-ada0-d90208671383 | -9.25084 | -56.90567 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c74409b-0de5-3465-afa4-f46f1802ac34 | -6.821 | -59.88777 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb0d0248-9c2d-3b9f-b975-5bc8968ae247 | -9.49038 | -51.61145 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c62180e-b999-3f3c-a445-ed8d8e83140d | -7.02628 | -45.91288 | 2026-08-16 05:16:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e53ed0bd-2c9f-3dbd-b0a8-f4ee44e4f752 | -11.26748 | -54.84975 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c087689-848a-390d-b410-a1f4ba1b6fb9 | -7.05827 | -56.5172 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 986b96c3-2da5-31b0-9ab6-df649217ca36 | -11.19745 | -54.8313 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6afe0d06-4965-3d97-ae6e-bec0f7738ba0 | -6.11669 | -57.71112 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 632157cb-47dc-3ebb-8d31-bfa071581c0b | -6.85472 | -56.43501 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc50858a-be91-3e7b-8edf-bb78a7efe8a4 | -11.47947 | -54.61328 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 33137291-9d8b-335d-994b-d0e865435d09 | -8.95056 | -60.58641 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1c3c3ad-6908-30c8-8d62-5f9965694d96 | -6.43064 | -60.07147 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc14f8dd-0dca-38d2-ac4c-2c2f957f5fa7 | -11.48297 | -54.61383 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f866e1c6-001b-3dec-8633-56dcfa1d654f | -6.37707 | -58.31856 | 2026-08-16 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63cd1978-2bf0-3085-9735-b446d33e66ae | -8.97294 | -60.5231 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ef401068-63e6-3504-9a4f-3c6987bd0817 | -11.45883 | -46.61781 | 2026-08-16 05:16:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c831cd09-a384-347d-8f8e-ed142d2bf8dc | -10.52844 | -44.85443 | 2026-08-16 05:16:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 182b74e4-1f70-3efb-b5ec-a6c53de59947 | -3.56882 | -60.24825 | 2026-08-16 05:16:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 363cb179-0e5f-358d-9c0d-7343ac7ccd55 | -9.08231 | -61.39887 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9ce0ee6-fc51-31d9-a635-dab8ba9ea869 | -6.6037 | -59.00417 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b6928c5-bc4b-3fbc-87c6-adb8c69a131f | -6.83589 | -56.42488 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 126d08b7-34a9-37bc-b50f-d27d64a2e919 | -6.86262 | -58.94807 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cd75a39-fe2d-3d70-b51c-e9832c32a4ca | -6.61645 | -59.06163 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14290e54-eae9-3b9b-8024-eabd0b4a1252 | -8.90137 | -60.55397 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5e875765-1e24-3be4-83f3-68ebc92d5411 | -8.60319 | -54.66773 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86c8c895-d6ea-3642-bfc9-97ce33347a0d | -6.83368 | -56.46017 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68144d84-168a-3cc4-b17d-863e42303ad7 | -10.18429 | -46.40971 | 2026-08-16 05:16:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08c5d4ec-c40e-3e47-bf86-3866c82007bc | -6.84697 | -56.4409 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb5e0355-d4ee-3ae3-a1d7-58c50c1b5ae3 | -8.43364 | -62.67926 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| b3f769bf-261b-31aa-b1cf-fdc3a4239540 | -9.56909 | -45.37038 | 2026-08-16 05:16:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 430c5ea9-ef86-3dac-b459-a414a28fce95 | -12.44292 | -46.65347 | 2026-08-16 05:16:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66f12bdf-ab4f-3e08-975e-0c240b24935f | -8.43515 | -62.67074 | 2026-08-16 05:16:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ada14522-5504-355d-8144-404f650c6cce | -6.8514 | -56.43447 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f1bc49a-69f9-3cb5-bc9a-fff5b9c5201a | -6.85915 | -56.42859 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1f1ead1-1bd4-369d-a4ea-32682e78d94b | -6.82981 | -56.46313 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8c5ffc3-90bb-3d38-9d63-6126b0bbc149 | -7.45909 | -45.09448 | 2026-08-16 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64fabb96-353c-3757-965f-1e33c6e7a2fd | -9.42412 | -60.32579 | 2026-08-16 05:16:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9d0559c-43a8-374f-aa09-e32ed259bb9a | -8.6498 | -54.70533 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63156575-6ca8-38cf-b528-3b59cdee66a4 | -9.14282 | -68.20815 | 2026-08-16 05:16:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| afd530a9-850d-38ad-969d-6cb9359f0712 | -6.70585 | -58.93131 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 487b3d5d-5a92-3df1-8316-471879577170 | -12.00491 | -46.43276 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35c1c89a-79a2-3c10-bbcf-b4b8101d5ac4 | -6.83091 | -56.4134 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae74946a-64c2-3934-955f-b22385fda431 | -6.12786 | -55.81083 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee0d06e6-615b-35a0-a5f4-96969e520950 | -8.02927 | -55.14884 | 2026-08-16 05:16:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0a6c43a-3c3a-3e01-b5cd-0d47c3185fdb | -8.61171 | -54.70309 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c213f5b-5b88-3a30-aa85-1ebbf1f65786 | -11.19803 | -54.82745 | 2026-08-16 05:16:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd98c15a-bb49-3a96-9325-9a504350e1ec | -8.95608 | -60.5537 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61672a40-1a7b-3021-aa42-01009589a064 | -7.55624 | -61.17382 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac2a5d26-ff04-32d7-932e-68b545b947b6 | -11.50986 | -54.62597 | 2026-08-16 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94052152-0d75-3741-b801-9b4750ccbe6d | -8.60433 | -54.70571 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1bc3c9c-8563-379c-a693-ed8b48d00b13 | -11.3398 | -46.21272 | 2026-08-16 05:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5771d1c-681a-3652-a3e3-6cc46ebae890 | -8.90334 | -60.58792 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1ef2f3fb-4e18-3793-a11a-050f95724d18 | -8.89595 | -60.56269 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a203b453-b390-3e08-b3a7-b31389e1c0a5 | -6.81818 | -56.45058 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07b47564-8bbe-3f47-beb3-045656828e18 | -6.81596 | -56.4645 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55684390-0fe3-34c6-a0f1-cb7b84fd1a4f | -7.58467 | -60.8852 | 2026-08-16 05:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| edcf3d6b-b294-353d-82ee-42ba3f5dab1f | -6.62434 | -59.05867 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0932f81d-aa70-3730-a87d-7365de5d0ce9 | -6.69754 | -58.95926 | 2026-08-16 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7eb78e12-311a-33a6-9d04-776e742cb7ae | -12.00642 | -46.42037 | 2026-08-16 05:16:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 154226b1-27a1-3ca3-9343-3f48510efbbd | -8.96771 | -60.50793 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 448d96df-00ea-3f55-8a2a-859059596c11 | -8.97818 | -60.53832 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3976c08-a8eb-38bb-90c3-edf0d45f4aa3 | -6.60813 | -56.34533 | 2026-08-16 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93eb5c02-0d24-36c0-92ef-421eff051953 | -9.29549 | -56.81231 | 2026-08-16 05:16:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26da323b-67e6-32e8-b5d5-33cbff60e924 | -7.45749 | -45.09902 | 2026-08-16 05:16:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 141c47cd-6286-3745-80d4-9733251ac5d5 | -8.61798 | -54.68518 | 2026-08-16 05:16:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab743c25-2b0a-39cd-8fad-9a006fe9d80a | -6.10523 | -57.71685 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ef66e668-652f-3c8d-81c9-f056e330da98 | -9.08773 | -61.40165 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b61a58e-302f-3b34-81cb-4671961eed56 | -8.96392 | -60.5073 | 2026-08-16 05:16:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14100f58-3775-3501-9a0e-0f58acf3e140 | -11.08302 | -47.24493 | 2026-08-16 05:16:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3207bbb5-7e41-33df-8ee3-197966b71b58 | -6.12709 | -57.68561 | 2026-08-16 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README37.md)
