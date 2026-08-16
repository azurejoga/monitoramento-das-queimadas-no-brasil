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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07edb990-8fe8-3e17-a459-4d5b6706eadd | -11.8101 | -51.7957 | 2026-08-16 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 543a57fa-219d-3894-a2fe-2c5a28b21ce6 | -14.4816 | -53.4598 | 2026-08-16 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 129.9 |
| db7e44e4-38da-323c-ac41-3f3fc5e88086 | -6.3872 | -45.6919 | 2026-08-16 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4b339d12-f644-318d-83f2-7da59d8fcee6 | -15.0355 | -52.6936 | 2026-08-16 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 07a0599e-8970-3509-a3b5-e50369c9780d | -8.9785 | -60.5349 | 2026-08-16 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 079b207a-6032-33cc-b1cd-198f44a88016 | -6.6198 | -58.9836 | 2026-08-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f8cf5335-e137-3d3b-b8cd-61faccaf95de | -13.8031 | -53.812 | 2026-08-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 4c4d8f6b-cd31-3d11-a3b3-f550902ccf61 | -6.704 | -44.0017 | 2026-08-16 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 913770ec-8e50-30c0-94a3-8f14212d3058 | -6.6014 | -58.9844 | 2026-08-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 186.8 |
| f9ad9f65-b22c-3730-877c-4132d0da6c0f | -11.08 | -47.2479 | 2026-08-16 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 09804597-8596-3515-8c33-1baf288fb3f5 | -11.0609 | -47.2503 | 2026-08-16 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ea545f89-6b65-35ec-a36a-91eceb29f326 | -11.8482 | -51.7916 | 2026-08-16 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 5d8ebc7b-b6a2-32ea-bb4c-4ae4cefc05cd | -6.82 | -56.4551 | 2026-08-16 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7f714589-c1a8-39ff-b753-d5b1356ca080 | -12.0095 | -46.4271 | 2026-08-16 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 905afa0a-ec7e-3d4e-a346-bf02b97be779 | -14.5382 | -53.5366 | 2026-08-16 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 154.8 |
| a8e05532-2268-3b56-9e2a-c5d08930ca41 | -8.9787 | -60.5156 | 2026-08-16 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 3942708a-217d-3c3f-858b-e502c59b0a6e | -6.6852 | -44.0033 | 2026-08-16 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 318.6 |
| 028057bd-c1d8-3792-9672-dc293a51173f | -13.8038 | -53.7703 | 2026-08-16 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 7c1cfdb6-cef0-3e28-8613-493cd69de3c3 | -6.0371 | -57.7065 | 2026-08-16 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 38938bfd-96fb-3546-8a92-a7a94fa2c0b1 | -6.11 | -45.3298 | 2026-08-16 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2f4973e1-b0ce-3fbb-a9b6-eaee90c5ddd4 | -12.0474 | -46.4444 | 2026-08-16 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b1e64a8e-4f12-3f5d-9ce1-9cfb2123b486 | -14.2755 | -51.9447 | 2026-08-16 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b88a42b9-6012-30ff-998f-2e83fcb93871 | -6.8597 | -58.9738 | 2026-08-16 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 55233afd-b15b-3204-8e2c-6d58eba09e76 | -12.0091 | -46.4498 | 2026-08-16 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 5a39c71b-e473-3df4-9181-2722bdcc7a27 | -8.96 | -60.5358 | 2026-08-16 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 1ccd15e3-3d1b-3fa9-908f-7ec6f0ba7175 | -6.6854 | -43.9802 | 2026-08-16 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 349.1 |
| b662cd64-bf2c-36f5-99f7-97af0b510fc9 | -6.7233 | -45.7777 | 2026-08-16 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 0674de1d-e33a-30db-877c-c8b722b98e67 | -6.1107 | -57.723 | 2026-08-16 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 29677a42-1c08-3f23-b10d-762665b15dbb | -12.0282 | -46.4471 | 2026-08-16 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| e65a0f86-af99-3aa8-b376-db0b80022d89 | -6.8572 | -56.4335 | 2026-08-16 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 522029be-4859-30c0-a99e-3f3938263e25 | -6.6714 | -45.3535 | 2026-08-16 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 026355fe-ed7c-3b60-bdc1-eb9a8c32f387 | -7.0254 | -43.8108 | 2026-08-16 14:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 6df441f3-2551-3175-b430-327933e7a625 | -8.9415 | -60.5174 | 2026-08-16 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8c3b4121-46f6-3e7a-a2a8-0967ebc9ce8d | -6.6664 | -44.005 | 2026-08-16 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 11309125-a893-3154-b0d5-35b5e4ceaf49 | -8.4461 | -62.6563 | 2026-08-16 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3a606ebe-e63a-37d0-a2ce-21f482edcfa8 | -6.6714 | -45.3535 | 2026-08-16 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 49051cff-5763-3a98-ad62-53b3b3309e97 | -15.3012 | -54.1527 | 2026-08-16 14:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 204.0 |
| af8e84ca-bece-3fd5-967c-9d6add5c58ee | -6.8387 | -56.4344 | 2026-08-16 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| f361366d-556f-301d-9c31-fb6f396a487c | -15.0355 | -52.6936 | 2026-08-16 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| af943f98-aa5f-3a73-a958-294b5b601e78 | -11.0609 | -47.2503 | 2026-08-16 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d39f51cd-fd60-380c-af23-f45f423bc49e | -6.0371 | -57.7065 | 2026-08-16 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| ed165a4d-04f5-3bd8-b2a5-68244846d224 | -15.0682 | -47.0098 | 2026-08-16 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7c327c51-b2ba-3095-95c3-02c5cac2e716 | -8.4461 | -62.6563 | 2026-08-16 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 09bc40af-80c6-384c-a53d-9ff0c6645ca5 | -6.8573 | -56.4137 | 2026-08-16 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 75effcbe-1282-3a50-a7e6-05282a10abb2 | -12.1577 | -50.1796 | 2026-08-16 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 44d5c94b-ac1c-35cf-bfd0-eb8dceb47f01 | -8.9601 | -60.5165 | 2026-08-16 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 164.4 |
| 5bed185c-a4d5-3aff-b1d5-b79daff0fa0b | -15.0677 | -47.0326 | 2026-08-16 14:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| b6d73362-45b0-386b-bce8-7a4baa933fe0 | -7.5871 | -60.8845 | 2026-08-16 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b0126c0e-1ace-308b-b2c5-f15b01108511 | -10.2576 | -50.4332 | 2026-08-16 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 3e082e12-8479-35aa-857c-8493b9639013 | -6.3137 | -43.6178 | 2026-08-16 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b722cca9-dc0e-305d-b0cc-74aed453c404 | -10.8984 | -50.5586 | 2026-08-16 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| a9392982-fa58-373e-a9d2-256362f5b326 | -6.7645 | -59.4794 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3b7987e9-0316-3427-b605-68317b61509e | -6.8597 | -58.9738 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 08052de8-25e5-3c23-9f3d-26293ab55915 | -12.0282 | -46.4471 | 2026-08-16 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| b64c67e7-8784-3bd5-877d-661c69a64095 | -6.6664 | -44.005 | 2026-08-16 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4bca6395-0890-37da-9552-513a1ef6ded9 | -6.1106 | -57.7425 | 2026-08-16 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0494ce4d-bfd0-38c1-b659-fec7b995e2cb | -14.4317 | -51.8388 | 2026-08-16 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6161e50d-9cac-30e4-ae84-6249d3a22540 | -14.4678 | -51.9832 | 2026-08-16 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b2a4d0ba-f3cf-30e6-ba74-53da783215ed | -8.4275 | -62.676 | 2026-08-16 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.5 |
| bf4a827e-b33b-3cf6-9da4-057f53daa445 | -14.4663 | -52.0685 | 2026-08-16 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 59a87665-0bfa-32be-8a40-a2f9e03ed606 | -6.1108 | -57.7035 | 2026-08-16 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e7212cfb-031a-33f5-921f-6ecce41268a3 | -15.5983 | -56.1661 | 2026-08-16 14:30:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 53f4510e-e7aa-317a-93cd-7a85fc79e9ad | -6.3654 | -58.3354 | 2026-08-16 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 748638e1-399d-3298-a8f4-4e0d2dbc9521 | -8.96 | -60.5358 | 2026-08-16 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| ff4732c6-61d2-32a8-9130-ed26a9c2d8df | -13.8031 | -53.812 | 2026-08-16 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 750346d6-0f82-31bd-9af5-cc0423129d46 | -6.2938 | -47.7367 | 2026-08-16 14:30:00 | GOES-19 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d6ea2815-a5dd-3a3c-b166-ec57bb0c1a7a | -6.058 | -44.88 | 2026-08-16 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a864aea1-9df0-311f-a1c1-001d56684c2b | -11.0991 | -47.2455 | 2026-08-16 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0586e482-89bd-3720-8055-5b515fdf7017 | -6.1107 | -57.723 | 2026-08-16 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 8954b457-747d-3a9e-831a-8fd89ac6fa5b | -11.8482 | -51.7916 | 2026-08-16 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 613cc0f8-51c3-3085-9da2-0204ac2b1897 | -7.4074 | -60.0108 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 1fb5bb0e-5124-3194-a45e-bb198854351e | -6.704 | -44.0017 | 2026-08-16 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8400877b-e6b5-310d-a072-77330e1703ec | -12.0091 | -46.4498 | 2026-08-16 14:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 70e94140-343c-3e27-9d42-3b83836539f3 | -6.6666 | -43.9818 | 2026-08-16 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 23da3f21-bf0a-3fe9-9d3a-e770450a2006 | -11.9365 | -47.3367 | 2026-08-16 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 68eb275a-ea1d-395b-8e15-ab8f8d0824f8 | -11.0796 | -47.2702 | 2026-08-16 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| e280328c-a9c7-3079-8d28-ca3f8bc0a496 | -6.11 | -45.3298 | 2026-08-16 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| e8e51297-9341-3545-8e1c-a90e67da4c4d | -11.8291 | -51.7937 | 2026-08-16 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 5dfdb690-d465-394f-81f2-01384ab3a1bc | -6.82 | -56.4551 | 2026-08-16 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a70c7e90-9b0b-364c-ab98-15cba35f870b | -8.9787 | -60.5156 | 2026-08-16 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.9 |
| 227e2a07-9af7-3788-a761-0ea5f07c27df | -6.6013 | -59.0037 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e2fdc32d-39f2-3bb0-9781-156056bf5493 | -6.6014 | -58.9844 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 6e6eba84-f824-3d8f-9329-7471c16fa962 | -11.08 | -47.2479 | 2026-08-16 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 8ec59e4e-0769-35cb-b550-0bb8b748249c | -11.8101 | -51.7957 | 2026-08-16 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| bb8f6676-d735-3625-a182-9744a65c4517 | -14.2755 | -51.9447 | 2026-08-16 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f635f3b6-82a2-3dab-b129-d03f5a4162a4 | -6.6198 | -58.9836 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 6b66a18e-74f9-3d50-be2c-f3c7a6213f3d | -7.4258 | -60.0292 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 525479c1-d35f-3580-be63-384f62d83e97 | -6.7123 | -58.9412 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0e2c456d-cd8b-3293-8672-bee62a5dd6d0 | -8.4276 | -62.657 | 2026-08-16 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 372f314f-d3b0-377c-b5e4-3e14415104b4 | -7.4259 | -60.01 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6feac2be-dc6d-3750-a470-5773d79f871e | -8.446 | -62.6752 | 2026-08-16 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 1de084c5-902a-37fd-9c78-a21f2d986d00 | -12.5592 | -47.8528 | 2026-08-16 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9197e72e-9ec0-3644-9ecc-5ecfe7179621 | -8.9785 | -60.5349 | 2026-08-16 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| a57389e6-2a23-30d4-9630-d6b63de3fda5 | -15.3015 | -54.1318 | 2026-08-16 14:30:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 9f16edbc-e600-3dfc-a0c3-4bd404936eaf | -6.6852 | -44.0033 | 2026-08-16 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 248.2 |
| c5b4e843-8a34-339f-b549-6d95f21cd51f | -6.8572 | -56.4335 | 2026-08-16 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| effca475-fe6e-37aa-9043-49763d52bf6b | -13.8038 | -53.7703 | 2026-08-16 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 4aaf0ce4-2933-3bb6-8ee6-d7ec3758b35a | -10.8798 | -50.5392 | 2026-08-16 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 93242b72-4489-360b-8155-b33ba786619a | -6.6854 | -43.9802 | 2026-08-16 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 259.1 |
| dc15a9f5-0723-337d-bddf-9fd1fb42d425 | -6.9702 | -59.0078 | 2026-08-16 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |


[Clique aqui para ver as próximas entradas](README65.md)
