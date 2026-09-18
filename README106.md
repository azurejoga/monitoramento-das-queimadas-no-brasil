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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17f50734-9343-33dc-94ea-750a6dbb3a56 | -10.6726 | -50.4758 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 225.3 |
| 6805498c-a3b3-389d-a7f2-3ef32d46cdd9 | -2.4814 | -49.4208 | 2026-09-18 15:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 133.0 |
| e531074f-bbca-3469-89ea-d2d098e9709e | -14.9314 | -49.9103 | 2026-09-18 15:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 811f728a-609d-37e9-98ca-86ffa368e4ca | -10.2821 | -50.0035 | 2026-09-18 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| eb8577c0-2aef-356a-8464-dbf099739fdd | -15.6557 | -52.7366 | 2026-09-18 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 651a3847-11ad-3388-9186-0343a1424150 | -8.6374 | -44.5029 | 2026-09-18 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| ee7b5b02-7ada-31e8-8c33-9d615bf41968 | -10.6376 | -50.266 | 2026-09-18 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| fe3faefd-bc56-3fa0-92e0-a2539ba090df | -4.58 | -42.93 | 2026-09-18 15:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72b71b32-3ee4-30b6-a45b-863d9b0add8b | -10.85 | -50.21 | 2026-09-18 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d679ed5-b301-3a3c-ba98-4bcaf24ad0e7 | -14.14 | -45.16 | 2026-09-18 15:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13a679d6-3e6f-31cf-beed-fbbe638ffa97 | -10.82 | -50.2 | 2026-09-18 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c40d864-62b1-3c67-8500-de9ff2ea78c5 | -4.58 | -42.97 | 2026-09-18 15:15:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e57abe6-0534-3f78-8991-489c2382b716 | -7.69 | -46.1 | 2026-09-18 15:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3732ab21-9a8c-3cd7-accf-100f95decbd1 | -10.82 | -50.15 | 2026-09-18 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c590b11-3117-3694-98bc-a3f30c0d12ac | -14.1737 | -45.1641 | 2026-09-18 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 279.4 |
| 209703a8-00bb-313a-90ff-e011ffe4995e | -11.2975 | -43.3851 | 2026-09-18 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 79312ffc-5831-39f2-9e3a-38ea1819c9b1 | -10.6376 | -50.266 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 4a53c55b-df44-3464-b0ae-e92208221107 | -9.9956 | -50.2675 | 2026-09-18 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c12eb863-3250-341e-a3df-2cf01ffb0f86 | -10.3307 | -45.3112 | 2026-09-18 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| d45d1c96-f2c9-3d16-87a6-933bf9a69ffb | -11.3809 | -44.0788 | 2026-09-18 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 258.1 |
| ec756b67-f55e-3e4d-a003-606d555c32d0 | -15.6752 | -52.7339 | 2026-09-18 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 15bfa675-be06-3b00-839e-9f0e364a8cbb | -2.8285 | -50.4653 | 2026-09-18 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 201.6 |
| 64c0735a-ded7-3f49-b8f5-62456d1033b2 | -6.2936 | -45.6991 | 2026-09-18 15:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 5d235357-d437-3f45-954e-0deb91387bd4 | -2.8101 | -50.4658 | 2026-09-18 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| ed9f1d4c-8d4c-33d1-84d7-12442004056e | -11.2979 | -43.3614 | 2026-09-18 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 188.7 |
| b7fba5bd-fbd4-3a4e-a7b3-c4ee2ac261ff | 1.2427 | -50.7681 | 2026-09-18 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b9054f01-e88b-3bdc-851a-c2b019e9b496 | -14.8026 | -48.5622 | 2026-09-18 15:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 36d91b3a-e15e-32b3-84e3-590b62254d28 | -8.6817 | -45.4359 | 2026-09-18 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 8635f3a0-32ca-3818-9e2f-ca9e4133f8b9 | -0.803 | -48.6611 | 2026-09-18 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1b515511-6884-3ad9-a2ac-edb6d008c0b3 | 1.2794 | -50.8718 | 2026-09-18 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.8 |
| a476187d-2e12-3616-99df-b349da62b5b7 | -12.0238 | -51.4763 | 2026-09-18 15:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 8ac061c1-3029-3eb2-b423-8d427fdd77e8 | -11.3437 | -44.0141 | 2026-09-18 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 189.0 |
| 2e4cfd03-feae-3900-b340-5ab796d1a109 | -2.4815 | -49.3996 | 2026-09-18 15:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 647b31e3-7082-392f-af06-a702c243f7f7 | -10.6539 | -50.4564 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 526a4173-2368-3186-b56a-a0d5af316500 | -10.7276 | -50.5979 | 2026-09-18 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b617d602-077b-3c09-8da6-15e161e1cf24 | -14.1547 | -45.1442 | 2026-09-18 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 605c8bd0-fab2-3ab9-8b6d-41b4ef2771af | -10.6723 | -50.4972 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 222.6 |
| b623b33f-177d-3126-8956-3f526a920fc4 | -12.9243 | -44.7484 | 2026-09-18 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| eb0a5783-ebe8-3e74-a97a-0ba899332f17 | -9.9509 | -46.6026 | 2026-09-18 15:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d749b01b-f7ec-32fc-ab81-a6756930326a | 1.2424 | -50.9346 | 2026-09-18 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.4 |
| daa4d0a3-6cba-300c-8b9b-6e023055f574 | -12.0241 | -51.4551 | 2026-09-18 15:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 25bcaa41-836d-3b85-9603-06779de164a7 | -10.6525 | -50.5631 | 2026-09-18 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| a9bf23d8-4484-3147-b008-3917dd6de73a | -10.6726 | -50.4758 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 348.4 |
| cb149135-726f-3901-88b9-baf1d590fdb6 | -11.064 | -48.2898 | 2026-09-18 15:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4b23cca2-73e0-314c-809b-bd598b1c3e63 | -2.0768 | -56.4282 | 2026-09-18 15:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 85af6c7c-dff1-3c9e-a213-302cfc0308d6 | -11.875 | -47.5902 | 2026-09-18 15:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 3110a1d3-6c52-3a22-b6a0-b221da93f48a | -12.998 | -46.9381 | 2026-09-18 15:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 139.1 |
| c98cb1e5-177d-3918-bf92-8fc26c146af9 | 1.3351 | -50.6001 | 2026-09-18 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.5 |
| b7752131-4907-3cdd-a94e-46ee9011865e | -10.5838 | -48.696 | 2026-09-18 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 77dcfc3c-6d13-363f-90c5-3e6df8ce4af5 | -2.463 | -49.4001 | 2026-09-18 15:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 283eb9fd-2c3e-3abb-9f50-92fddbd2d7a4 | -9.3251 | -48.1758 | 2026-09-18 15:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 22f3ab18-11cb-304f-8cc5-42c61307eb7e | -1.2193 | -54.2192 | 2026-09-18 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 6ce36b3f-23e2-3eb9-a21c-6fcb7812deed | -15.6557 | -52.7366 | 2026-09-18 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| f6f466d1-91c3-33d1-9e3e-ff61de9ec90d | -14.1742 | -45.1407 | 2026-09-18 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| ede2a821-b9e7-3dda-8146-49c92388f7e2 | -10.6187 | -50.268 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 690547cd-66cd-3e64-aab7-12a270761a87 | -8.3769 | -47.236 | 2026-09-18 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| da8da40e-5f19-32d8-8eaf-10eb4b0983d6 | -10.6755 | -50.262 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 16fab752-d954-3ef9-af04-d9ac731aacff | -1.201 | -54.2194 | 2026-09-18 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 3a4c7d7c-f1ea-3d56-883e-1a50f9fe2158 | -10.2821 | -50.0035 | 2026-09-18 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0fd34a4c-d60a-3ffb-940b-801a140db5af | -0.4503 | -52.056 | 2026-09-18 15:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b9808ff7-cc86-382d-9317-768e79e329c2 | -2.9395 | -50.3994 | 2026-09-18 15:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c61eccad-6831-3b7a-b29f-ad11a2623387 | -2.4814 | -49.4208 | 2026-09-18 15:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 4a126761-280e-3711-986a-3721b67f8ace | -8.6377 | -44.4798 | 2026-09-18 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| e220f245-d000-37df-8054-dcb4c2e4cf5f | -10.8087 | -50.205 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 412.5 |
| 79f97971-1c11-3be2-a4c2-650a9b2a891d | -11.8115 | -46.8158 | 2026-09-18 15:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| db26ac4a-72b0-3aff-afef-8fd674a570ab | -10.6536 | -50.4778 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 301.7 |
| 0dd62abe-9bc2-392c-8162-335bfdc3441a | -10.6533 | -50.4991 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 1c3bd2f6-2e4b-3d54-a6b3-a9da01ce7aef | -0.5442 | -49.1324 | 2026-09-18 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 5caad946-2fde-3b50-b098-61fd9532bda7 | -10.6189 | -50.2466 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| face94e6-e8b9-343d-86e7-69e614d5630e | -14.1542 | -45.1675 | 2026-09-18 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 309.7 |
| ab7b0667-78b7-3167-840e-69fa9466be42 | -11.3446 | -43.9671 | 2026-09-18 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 69f724b3-2e6c-3a80-9912-6ef63e5b8f8e | -5.5829 | -48.1094 | 2026-09-18 15:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 75.7 |
| bc7905d5-c5eb-34e8-a8f7-3534d34ed588 | -0.803 | -48.6825 | 2026-09-18 15:20:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 70ad8c63-e53b-3533-bef5-de1c226d1884 | -7.8036 | -44.8422 | 2026-09-18 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 4c46472a-60e4-30dc-9423-bb021de62361 | -11.3442 | -43.9906 | 2026-09-18 15:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| ca9256ac-8988-35a9-a28d-567306b5f199 | -10.6729 | -50.4545 | 2026-09-18 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 7ee54777-dbaf-34c1-a413-91447f1921d7 | -10.3704 | -50.4644 | 2026-09-18 15:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 9d4b36ca-0825-3c83-a61b-c370949278c5 | -11.4541 | -51.4754 | 2026-09-18 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 63ad1bf0-2749-3e53-bc22-616f99efab0d | -8.6817 | -45.4359 | 2026-09-18 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3c7c56a6-c404-347f-b16c-27adbaa96db2 | -7.8033 | -44.8651 | 2026-09-18 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 6d2c0410-2c91-3e76-946c-7bad67050529 | -8.6377 | -44.4798 | 2026-09-18 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| fbd8cd37-982a-322c-9d5d-52d09c44b1a7 | -0.803 | -48.6611 | 2026-09-18 15:30:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b713c185-1bc4-3ac8-b443-34a47972b217 | -1.6042 | -54.415 | 2026-09-18 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c7280104-341a-3554-aa21-fd18478c39ba | -14.1737 | -45.1641 | 2026-09-18 15:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 242.7 |
| f1bfc9e1-960a-3220-b4e6-f8fdcbfd2fe1 | -11.3809 | -44.0788 | 2026-09-18 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 4c7df7cc-0e31-377d-8480-39eb5ba3142c | -7.7842 | -44.8898 | 2026-09-18 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 03383279-63d1-3b0e-8342-e06738f57a54 | -8.3176 | -47.4842 | 2026-09-18 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| be1e2887-56eb-314b-a6b9-b3bbb9734aef | -12.1448 | -44.243 | 2026-09-18 15:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 5eee9030-51b7-30d1-8886-11b7c24f71bb | -10.3704 | -50.4644 | 2026-09-18 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 16d24b2a-7601-3b51-a38c-ebb6f871544d | -7.8036 | -44.8422 | 2026-09-18 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| f8e3b874-1d5e-399f-94a1-0c253b3d02da | -14.1927 | -45.184 | 2026-09-18 15:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| c8a21f5c-988b-368d-828e-d94e7330ed2b | -11.3161 | -46.7699 | 2026-09-18 15:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 1db6fe65-84bf-35de-bfff-478ed72bfff4 | -11.4541 | -51.4754 | 2026-09-18 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 3591b29a-1da5-3a48-99e8-d29beccab1a4 | -8.6188 | -44.4819 | 2026-09-18 15:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 23c47b58-4eeb-302e-94ac-6f1569009562 | -11.3442 | -43.9906 | 2026-09-18 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 5ec5ba2f-047c-35bd-9c0d-cfbc454eb4b5 | -8.8642 | -45.9145 | 2026-09-18 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 422ddfa9-a6a5-3076-b8c1-73d005f56a9f | -11.3437 | -44.0141 | 2026-09-18 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 258.8 |
| 4b6d96ae-5df6-39c5-b407-98a4134f1813 | -14.8026 | -48.5622 | 2026-09-18 15:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 3296e7d5-00da-3a8f-86b5-6429104bbee2 | -14.1547 | -45.1442 | 2026-09-18 15:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 6734243f-aaa9-3eb6-b973-648857ac52e0 | -14.1742 | -45.1407 | 2026-09-18 15:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |


[Clique aqui para ver as próximas entradas](README107.md)
