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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c0f5b07-4c41-3d1e-b7e8-b15d9b0cb7bf | -14.51389 | -48.66347 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4ab7de7-aca0-3104-9b3b-d284bc8f0e5b | -13.0766 | -47.36499 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed07156c-37a1-32b0-94f2-66da0534f9ff | -13.07127 | -47.36208 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18c4c964-ce5e-38e6-bef6-c96a6ac89a54 | -14.98797 | -46.97728 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f6e7ec43-4fda-377b-b329-77ea15bc6725 | -14.3136 | -54.14436 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d9ca8572-bba8-3ab1-8ac3-7a5b6602fdb2 | -14.49285 | -46.54581 | 2025-07-28 05:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2795b81-82a9-34f4-97dc-5398fbdd2234 | -11.76576 | -56.30743 | 2025-07-28 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d8decfc-187a-355d-800f-4d9011b2788d | -15.37373 | -52.18161 | 2025-07-28 05:08:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08e7a73c-f65a-3a26-8892-b6880fb7f245 | -14.9897 | -46.97248 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97811003-8b47-3961-9cfb-2bf06217a898 | -10.55303 | -59.70171 | 2025-07-28 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de558e90-8885-31b0-8a95-19a8409b45b8 | -10.31491 | -54.15434 | 2025-07-28 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 996ed471-c0d1-3858-83e4-33d144b3f4a8 | -12.71827 | -47.00858 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02ed6263-4342-3d34-a88d-169c33ad7abe | -8.51298 | -63.86542 | 2025-07-28 05:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afd25dda-d5d7-3f85-bfb9-f6f859dd9f4b | -11.51999 | -54.68364 | 2025-07-28 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee4cfe05-e2ff-3fef-93c4-1519a798f20f | -12.07538 | -63.55103 | 2025-07-28 05:08:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8bc214eb-7ff9-3dfb-8029-2403bff4338d | -14.31299 | -54.14872 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3db005ef-090d-3ce3-8b4e-e25b8879e97b | -13.11439 | -47.38083 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fabde47b-b03e-3983-9679-dbfa1315a2d0 | -14.31665 | -54.14922 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a0dab67b-f170-3c32-b185-84f8a8188e5a | -14.31238 | -54.15304 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 88fa7b1e-6244-330e-9eea-0da809ac28e5 | -11.29959 | -55.11956 | 2025-07-28 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39226019-c131-3dbe-8e93-bb3401b864da | -14.98833 | -46.97396 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5417675-e70c-3903-8ff1-e2da5ce99e1c | -9.03255 | -59.76822 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cf52c7f-2268-3f54-85c1-38e396e916cb | -9.46028 | -57.84865 | 2025-07-28 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55275ba6-009e-3ae2-bf37-957f7c2f8787 | -14.30871 | -54.15253 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc1a51b1-d556-3788-8880-35bd38ddf0a2 | -11.3019 | -55.1503 | 2025-07-28 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64608bdb-575d-3917-acdc-49bc0b31bc93 | -13.11478 | -47.37765 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e25388c-4c0b-3968-a180-34e29bfb2ad7 | -10.03885 | -59.10162 | 2025-07-28 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ea7bb4-57d4-3516-9b67-500a1c2bbdf7 | -14.51352 | -48.66658 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbad2b93-3038-33a3-bf91-991451240e38 | -9.02966 | -59.76295 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffb53cab-4b32-3662-b264-ed454d502b21 | -16.60954 | -47.82536 | 2025-07-28 05:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 696e769e-c080-3cc4-bbfa-1692ff6c8162 | -12.72318 | -47.01583 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f1a3d98-5376-34bc-8c72-32a1c67cd30a | -14.87443 | -48.39902 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e79f34b-ef39-3772-a8f2-41384683d25c | -12.66404 | -47.02785 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e445bd6c-c200-38e4-b77b-8847e445397f | -14.98269 | -46.97105 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb13584a-425b-3733-bb9a-6de4c6b22f7a | -14.50456 | -48.65262 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79dc829e-392b-3ea5-bf52-9fd65842c3c9 | -11.34644 | -51.24725 | 2025-07-28 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1318b23d-7d0c-3827-b764-ed5318872f39 | -10.59135 | -62.35156 | 2025-07-28 05:08:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09d6ef6f-d22f-3f70-ae35-20314af12261 | -9.272 | -60.77695 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7b27024-51db-33d0-9b5e-58d1c6899e7c | -12.71745 | -47.01537 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3502a516-0806-353d-9adb-05c09a50f156 | -14.49 | -48.64094 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14eabe66-f33d-3097-bcb6-69a09b58323e | -11.35064 | -51.24783 | 2025-07-28 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4049b227-009d-34fb-a14d-606399b96422 | -9.02299 | -59.7577 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdcdaaf5-7423-3957-8956-19f0777c770f | -13.1096 | -47.37357 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66281bc7-a634-392b-96f0-7e85c243ace8 | -10.29591 | -64.45775 | 2025-07-28 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1354a53c-a334-34e2-887a-0f4701e73a9e | -14.48188 | -46.53523 | 2025-07-28 05:08:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7965ecb-76f7-3e96-8c3a-4d65b42d860e | -10.54236 | -50.24589 | 2025-07-28 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d60e47a5-4755-3e9c-b27f-5e976e6042ac | -10.42146 | -60.27897 | 2025-07-28 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2458a1a-dce8-3d62-a11a-a3acbe3cb242 | -13.12124 | -47.37112 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d955ff05-c6e8-34f5-8c98-5246ed7ee44a | -14.32032 | -54.14972 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62cfaeae-05bd-3caf-a6ad-89a44594df2d | -13.12172 | -47.32017 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2df983f6-555f-3bfc-97ac-db4944c51690 | -14.49484 | -48.64492 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6715a57-25f3-3e5e-8040-c3ac95b8968c | -12.66755 | -47.02676 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03c2c595-3006-32b2-9577-552128ad1f0c | -14.50006 | -48.64574 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9a8faea-3578-3f33-a82e-0282f7d2ccc3 | -9.27588 | -60.7776 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28791cf7-a2ac-3a70-9370-e998e8b4488b | -10.31842 | -54.15489 | 2025-07-28 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d56c81de-339d-3d40-bb1a-a92b23ce3411 | -10.54624 | -49.49635 | 2025-07-28 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c90e5d6-669a-3d70-965f-8bce4122a4ac | -9.02668 | -59.75821 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae2531b2-e02b-3d4a-9de0-b07014bc742f | -14.97785 | -46.96079 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e62766de-9793-364c-b626-f313cfed0d7a | -14.98336 | -46.97594 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee01f607-b760-3190-b76d-806f18937537 | -14.98382 | -46.96051 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4edba668-e6f6-30b4-86d1-d56ee80c9576 | -10.54693 | -49.49143 | 2025-07-28 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 23fa6907-f37e-3caa-8384-ce6863511917 | -10.74731 | -52.76691 | 2025-07-28 05:08:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34788cda-531d-3733-ae33-daa851d1120a | -14.98236 | -46.97417 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 128156c7-db60-3c1d-ab27-d46a587455b1 | -9.45969 | -57.85229 | 2025-07-28 05:08:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 687c6dcb-4be5-3744-ab65-3fee1ceb37fc | -16.60387 | -47.82463 | 2025-07-28 05:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a90859f-ff35-34fa-a0ac-6cfaab5fed2c | -13.12734 | -47.36766 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1be6ad8d-ffc6-3bde-9d56-38b849c6462e | -14.31726 | -54.1449 | 2025-07-28 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 154d000e-7706-37ec-8e72-7f00e295dffa | -14.57686 | -52.87859 | 2025-07-28 05:08:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f430fd1c-b282-35f7-8a9c-83d6470381fd | -12.66712 | -47.03027 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d99530d-142e-36e5-91ca-41b8cc7c19a0 | -10.85167 | -46.67961 | 2025-07-28 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97c6ca50-ee17-35cb-bd0f-17a341b897a1 | -10.31433 | -54.15826 | 2025-07-28 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d5f8f52c-cd63-3965-aa62-59688b22ee00 | -15.95741 | -49.16851 | 2025-07-28 05:08:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b5c9262-39ab-3039-b7f0-27da400a223a | -15.1506 | -53.51153 | 2025-07-28 05:08:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63d866b-13f7-3b21-b4d8-da714122b4af | -14.5042 | -48.6557 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af606d31-ccdc-3ea2-8958-d3deeaf61add | -16.60907 | -47.8298 | 2025-07-28 05:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45be92bd-758e-350d-874e-257c693df82f | -10.31083 | -54.15772 | 2025-07-28 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14647e21-9627-34b0-a30c-e89086b33af5 | -11.35118 | -51.24394 | 2025-07-28 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cedc0a31-9dbf-3b56-9e8a-b53080db97ee | -16.60341 | -47.82896 | 2025-07-28 05:08:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7ff10c3-39e1-36c5-a312-457f464d9c54 | -14.97887 | -46.96305 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc1a035-699e-35d9-b48f-375ce0a263b3 | -10.54872 | -49.49327 | 2025-07-28 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 004c1ee8-6258-35d2-b65d-9ca6e1b6252e | -14.98869 | -46.9706 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af6e7c38-7000-3aa0-a1ac-bcd0ecaa4693 | -14.98489 | -46.9625 | 2025-07-28 05:08:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b7a5962-7804-396d-b28c-b998e5a70c5e | -13.12956 | -47.34937 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfb3a6d8-228d-3c48-b8b5-4a17d8840e27 | -14.51913 | -48.66402 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ea2752c-03ec-3a45-b978-f0a6fba206ad | -12.71704 | -47.0188 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8963a2f0-dcb1-3498-b3b0-89bf027c25b2 | -14.49898 | -48.6549 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e70b965e-fec6-306b-ab83-26df44288b62 | -14.49413 | -48.65106 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 123b8509-cc3a-3abc-99bb-18786ad76f46 | -14.48788 | -46.53596 | 2025-07-28 05:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d2171a0-0779-3a3c-bc14-d0995d701fb2 | -10.71462 | -49.48273 | 2025-07-28 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78bc6bea-e51a-35c6-ba00-36101e3827b5 | -9.02598 | -59.76236 | 2025-07-28 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 417f16be-a811-3071-8be0-8d67f0d2c685 | -11.27945 | -52.75719 | 2025-07-28 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df28f51e-4c65-3e54-8254-51091aef7198 | -10.4185 | -60.27399 | 2025-07-28 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8527e31a-3b9a-3b37-9f4c-9466d919b349 | -14.49335 | -46.54133 | 2025-07-28 05:08:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b53b887-5a2e-38f7-941d-8b0bd4b6e4f3 | -13.12697 | -47.37067 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70a9fd60-41f5-3637-aad6-c8675e3e7bb7 | -13.10917 | -47.37712 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51fccd78-6b84-36c6-92d3-296363339c2c | -10.84602 | -46.67868 | 2025-07-28 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43c798fd-50fa-30bd-bd50-1a298726ef09 | -13.13306 | -47.36724 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70e445c4-716d-314f-b571-553cc17e016f | -12.66445 | -47.02427 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f94e5673-b26e-3f19-8b35-cb3ff5025a57 | -14.87405 | -48.40227 | 2025-07-28 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21d9d60e-192b-308f-8237-fca9e9427a66 | -13.13012 | -47.34475 | 2025-07-28 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
