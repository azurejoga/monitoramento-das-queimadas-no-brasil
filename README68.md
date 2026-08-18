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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adc15ea5-bd0c-321f-b793-c4d8f3bcc3bd | -6.7814 | -59.7672 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 47a60205-f702-3fb4-abf3-3c09dcd92c18 | -8.5087 | -48.8193 | 2026-08-18 14:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 91.8 |
| fda8b8d2-4100-3ff9-95fb-55dfe02291f7 | -11.3606 | -46.381 | 2026-08-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 9f9e6b55-b932-325a-9ce9-e0a4de6980aa | -6.8411 | -58.9939 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e2cca805-3c71-380a-b01d-fee52de8e716 | -11.3239 | -46.2955 | 2026-08-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 0c911131-005b-386c-8803-e446f5a501f3 | -12.7601 | -48.4231 | 2026-08-18 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 40701f26-6dbb-30dc-99d1-9a2ea0e9a88e | -11.1368 | -47.263 | 2026-08-18 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5065fdc9-8566-32db-b393-850efb8b711a | -9.016 | -60.4945 | 2026-08-18 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e5dfedc1-506c-3a36-b8fd-bf7e988a7a3f | -6.7815 | -59.748 | 2026-08-18 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 86ea43a1-c587-3af1-a38d-237e6f7cc366 | -14.3525 | -51.9559 | 2026-08-18 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b506e23c-7d80-35d8-967b-7e826b0df5f8 | -8.604 | -50.3527 | 2026-08-18 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 6786c82f-35d4-3b00-acdd-ac3850cb076b | -11.3491 | -45.9292 | 2026-08-18 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.1 |
| 21ca13b4-1318-369b-b2ef-f387c6080c93 | -7.2007 | -43.2814 | 2026-08-18 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 9573df38-329c-3145-9c0c-6cac9dd34f16 | -8.6 | -54.74 | 2026-08-18 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc5082c-1497-332a-9f92-2776f675a984 | -8.54 | -54.72 | 2026-08-18 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9ef52c-8220-31b3-b4b8-75c3ebbe35b4 | -8.57 | -54.73 | 2026-08-18 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de5450ed-66ee-3117-9423-0868b1e74a49 | -8.55 | -54.78 | 2026-08-18 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa0da9aa-e167-3bf8-81bd-87bf2f1e7448 | -8.58 | -54.79 | 2026-08-18 14:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5588d1d-a853-3104-8bf5-fe0731a11c81 | -12.5207 | -47.8581 | 2026-08-18 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f8369b41-c924-39c2-aaee-a0dc355085dc | -9.1706 | -59.6762 | 2026-08-18 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e4f2e496-1a45-3141-ac44-0ae3b47a8737 | -7.0069 | -59.0449 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 945b7c9d-a563-3b44-8e76-55bf93911eda | -11.3606 | -46.381 | 2026-08-18 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| bde7f4fe-5780-3836-a605-5bf0e82fcd9a | -13.568 | -51.6953 | 2026-08-18 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 8a2bc9f7-c8d5-3101-a10e-bd9b0adb18fc | -14.3529 | -51.9345 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e5a4af76-238b-30d5-abf0-1202136835fc | -14.4704 | -51.8337 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 17c02f7a-4239-35f7-a776-5690da9d5382 | -14.451 | -51.8363 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 2a465994-087a-3ea2-9c75-54e4e095508c | -6.9884 | -59.0457 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.8 |
| ee0dab95-5890-3a0f-8ebc-8a67507310e6 | -14.47 | -51.8551 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| d6cb22bb-44b9-3d1c-81d1-6407715be7d6 | -6.8594 | -59.0125 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 68ece1e1-d4d1-32b2-b5ea-26b131720abb | -6.9516 | -59.028 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ac38c332-a11b-35c6-ba11-a07c8e7d5bc4 | -10.2765 | -50.4313 | 2026-08-18 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 7b796fd1-90de-344b-9520-d825d301a9c7 | -6.7832 | -59.4401 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| c7da0e4b-1aeb-353c-8169-89905ab89f06 | -8.6042 | -50.3315 | 2026-08-18 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e1f55ba9-49e1-3335-9c9c-5feb1dd8187c | -6.8411 | -58.9939 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| f7f65fa6-1952-3fc1-b265-24962d34be75 | -8.997 | -45.855 | 2026-08-18 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 05013e3d-1aac-3aed-9aff-fbd444df87a8 | -12.5399 | -47.8554 | 2026-08-18 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1afd1c91-3390-3b4b-9b28-58da03cb5485 | -12.7793 | -48.4205 | 2026-08-18 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b86d8000-8f56-32b8-bf22-88ded5ce0179 | -8.5853 | -50.3543 | 2026-08-18 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 0955c7bf-6f5c-39f2-811d-a203babef4a3 | -8.604 | -50.3527 | 2026-08-18 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| dd4d9e74-6dda-359c-9349-f6d1c72ca6b2 | -11.3491 | -45.9292 | 2026-08-18 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 26edd97b-d9e9-3ae2-b343-a11a1c45a171 | -14.1628 | -52.9323 | 2026-08-18 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| ae625866-900b-35c4-9dcf-907e77cbac61 | -14.1828 | -52.8878 | 2026-08-18 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 451facf5-9518-3e35-8ef1-a0dd6774f55f | -6.7123 | -58.9412 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e3e90368-7800-33e2-a315-ea72a7214245 | -14.354 | -51.8705 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 25da9c48-3b7c-3880-8df1-48c7ec0aa112 | -6.841 | -59.0132 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 81b6144c-3d47-39bd-abae-6c4235ea8fea | -6.0366 | -57.804 | 2026-08-18 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| faf9d004-c73d-3120-b17b-5a839b55ca8d | -6.9701 | -59.0272 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ffe26f74-d241-3ecc-97db-c7bd68512b25 | -9.016 | -60.4945 | 2026-08-18 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f5f3e68e-7eab-35f2-9a97-46e8a73f6bcb | -11.1368 | -47.263 | 2026-08-18 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 304c8fc5-203d-34b8-b330-dc21a0448a56 | -14.1824 | -52.9089 | 2026-08-18 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 76df4836-1c1d-360d-b667-54985c08eeae | -11.3235 | -46.3182 | 2026-08-18 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 53049aa9-a586-33d9-ab26-bc530d576e72 | -14.1817 | -52.951 | 2026-08-18 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c62d15d1-e005-36d9-b3dd-bfab0cd7bd31 | -6.8593 | -59.0318 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b714f8b9-aa27-3e7a-a980-14982d6d5495 | -14.4475 | -53.1913 | 2026-08-18 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0fa44398-1e86-3f63-8b9c-2e64caeadd40 | -7.7881 | -47.8607 | 2026-08-18 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 38e51bf2-4810-3582-bd1e-b089fe468f61 | -14.4656 | -52.1112 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c71986a2-ff84-385c-8db5-d8a3cf2cbe37 | -14.3525 | -51.9559 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ed90caa3-289a-3823-9a2b-4c8ae4397351 | -6.7815 | -59.748 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 68dbacc4-9e3e-3117-a431-de49b875d8b8 | -12.7597 | -48.4453 | 2026-08-18 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| d6146f14-2406-30ae-a253-1f0d9b755b45 | -12.7601 | -48.4231 | 2026-08-18 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 49b7b23f-7128-3656-b009-2e313491f4ba | -14.4514 | -51.8149 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 0c914888-e117-3f46-890b-4197b5d15866 | -6.748 | -59.1523 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 839de008-1de8-3a5e-8fbe-f11286fbbfdd | -12.5204 | -47.8804 | 2026-08-18 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f12351eb-e4a8-3fc3-af41-7dbf21802b62 | -6.0181 | -57.8047 | 2026-08-18 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3430d48c-4e1c-3281-8c63-3369127d86f3 | -6.6014 | -58.9844 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 58d3c4fc-f34f-3dc9-b6f4-b10f20d72e19 | -6.7814 | -59.7672 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 225.7 |
| d81e6471-f67a-3518-ae1b-a95242cf3daf | -6.0179 | -57.8437 | 2026-08-18 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 112d97dc-b4a8-3739-b3ca-e591b8db4652 | -13.5676 | -51.7166 | 2026-08-18 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| be664fee-388c-32c7-a533-acd26a7b52f7 | -14.466 | -52.0899 | 2026-08-18 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 7c33138c-c2df-3513-aeb4-71b288b5b359 | -14.1821 | -52.93 | 2026-08-18 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 58868cad-76e5-3b6d-980c-61465459f850 | -9.1705 | -59.6955 | 2026-08-18 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e103bf1e-3f23-3f90-a238-ed99d1c7820a | -12.7789 | -48.4426 | 2026-08-18 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| ea7b3c96-d502-34b7-bd5e-487ca059a639 | -8.4899 | -48.821 | 2026-08-18 14:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 62ed3350-2892-32e8-b0d8-cad716724d9d | -14.1631 | -52.9113 | 2026-08-18 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| a28d007e-8911-3675-9b1c-e9723d76e82d | -6.7478 | -59.1716 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 181fa485-6ead-3d56-8f88-bc9d6c7d9295 | -6.8596 | -58.9931 | 2026-08-18 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6af9f832-fb69-38f5-9023-a0983a648f0e | -7.8068 | -47.8591 | 2026-08-18 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| f35c6c99-aa53-3bd4-9309-9d2fd37f3ff3 | -8.604 | -50.3527 | 2026-08-18 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 192d7028-dec0-3624-8479-034a037a3eac | -8.6042 | -50.3315 | 2026-08-18 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 446c70f0-63d9-38c5-82c4-244954f89c42 | -14.3729 | -51.8893 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3b153412-7344-3305-a317-ee40373a77a6 | -10.2767 | -50.41 | 2026-08-18 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8a16be1a-585e-341d-8741-f4437f556009 | -7.0069 | -59.0449 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 574d17ef-f2e5-30e2-a8ab-ea0ff6bdbc11 | -6.6384 | -58.9636 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 14521f48-e556-332a-a301-51329f2c4007 | -14.1631 | -52.9113 | 2026-08-18 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 202.7 |
| 781686cd-c3fd-3946-8967-69504129b758 | -8.5135 | -45.3174 | 2026-08-18 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ad163a89-4419-3c1d-8d1e-a47907a4291a | -14.3529 | -51.9345 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1ee13ac6-b5e3-3bed-9e3e-d058e97e018d | -10.2765 | -50.4313 | 2026-08-18 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 197.3 |
| 5cd6df9d-7b47-31de-b7c7-8b93f0852c9a | -14.1817 | -52.951 | 2026-08-18 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 7f1d33ae-999a-3b67-8bfd-03b515c473e0 | -6.8596 | -58.9931 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| a7173435-ad78-391b-ad6f-68a34155efde | -6.7832 | -59.4401 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d6e4744f-5b6d-3891-9039-94d91e6c3e74 | -6.8409 | -59.0326 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8d3e72b5-866e-3750-972e-d930de4fb95e | -6.6015 | -58.9651 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 340e9728-ea49-338a-afd1-0764e8c79deb | -14.354 | -51.8705 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 92c766a9-b9d0-33da-8adf-974c917765e3 | -14.451 | -51.8363 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 887c2c7a-e0b3-39a4-a77a-021daf2acadd | -6.6199 | -58.9643 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 874a1f40-bf1f-30f2-a552-5d4c790ee013 | -13.5676 | -51.7166 | 2026-08-18 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| c726c3c1-b765-3cef-b9c2-eedd6eedd5c3 | -6.7814 | -59.7672 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 84e94f77-1614-337c-9d6e-5546cbb9cd38 | -12.7789 | -48.4426 | 2026-08-18 14:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 413bc801-d6e8-3936-8d2b-e6403de1ba12 | -6.9701 | -59.0272 | 2026-08-18 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c6de65e0-758c-3762-a20c-3c692f59451b | -14.3525 | -51.9559 | 2026-08-18 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |


[Clique aqui para ver as próximas entradas](README69.md)
