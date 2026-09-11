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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4146d6e7-7079-35e2-bac2-a3845e447383 | -10.2743 | -45.2726 | 2026-09-11 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 0339dd60-c35d-311e-9ff0-8b7b61df235c | -10.5475 | -51.3578 | 2026-09-11 16:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 221.2 |
| d032c4f6-7c1f-3f8e-a724-ae962f0f38c2 | -13.2088 | -61.8338 | 2026-09-11 16:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 0d6ad154-0d2a-337e-9974-f849722afea7 | -10.2743 | -45.2726 | 2026-09-11 16:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| fd9bc95a-01d2-30c7-b8b8-23b78c0c2517 | -10.5475 | -51.3578 | 2026-09-11 16:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 220.7 |
| 35cec843-496b-3174-847f-c7088d6ec194 | -13.3053 | -61.6721 | 2026-09-11 16:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 1e51c77c-695b-3dd7-93fa-12dc7c4b655f | -10.7542 | -46.1894 | 2026-09-11 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 3d6db042-46d1-301b-a61f-775094f3f7f3 | -13.4198 | -51.3731 | 2026-09-11 17:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| eb1df726-c32e-3295-845f-197e82117bd9 | -10.7359 | -46.1465 | 2026-09-11 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 3c3ec446-1e35-3d87-b3a2-5a46978f9ab2 | -13.2298 | -61.619 | 2026-09-11 17:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 248ac5f3-247a-323a-8eaa-a7ba5f7ab7eb | -13.2088 | -61.8338 | 2026-09-11 17:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 129.1 |
| f2c18b06-4f3a-3617-82b7-b73be48551f3 | -6.726 | -45.5072 | 2026-09-11 17:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 27f27233-bf61-3d9e-9662-15032bd8bc28 | -10.7542 | -46.1894 | 2026-09-11 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9391bc0b-a39e-3a8f-a3ba-6dc20452d2e6 | -13.2298 | -61.619 | 2026-09-11 17:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| d2412d89-3d96-38d3-8e5d-415c922d24f4 | -10.5475 | -51.3578 | 2026-09-11 17:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 214.9 |
| f581dee4-c465-3b8f-84bc-6cc7525ef61a | -13.2669 | -61.7135 | 2026-09-11 17:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 4a3b54d4-a5ed-346a-ba85-79270cc8894c | -13.2278 | -61.8325 | 2026-09-11 17:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 316.6 |
| ab174c29-4436-3353-bf74-81ba51da0e7c | -13.3245 | -61.6514 | 2026-09-11 17:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 07f992d7-1560-3bd8-918a-41d083e3b70e | -13.2859 | -61.7123 | 2026-09-11 17:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 24557b62-4a38-3bce-810d-ad45f073d8e8 | -13.2483 | -61.676 | 2026-09-11 17:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 4932079b-8d82-318d-96ac-ff49d2ee918c | -11.2488 | -54.1378 | 2026-09-11 17:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 437.4 |
| 6724fd31-defb-3f75-a62e-6fda81afb03a | -13.2673 | -61.6747 | 2026-09-11 17:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 86.2 |
| edea7e37-8a64-36a8-a199-6a813e40396c | -13.3053 | -61.6721 | 2026-09-11 17:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 6b2924ac-d812-35e8-b771-a351a94d1804 | -13.2088 | -61.8338 | 2026-09-11 17:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 134.2 |
| bc1f4c25-8237-33a6-80f1-c5d928fd3624 | -2.97 | -50.35 | 2026-09-11 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb485381-c11c-39e1-b557-f2d8a82cf13f | -2.94 | -50.4 | 2026-09-11 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddaeb97-8259-3369-a74d-36a23b8e9504 | -2.94 | -50.35 | 2026-09-11 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 713c9f6c-bb3c-368b-bbb9-41fe7476957e | -2.97 | -50.4 | 2026-09-11 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30931f9-e323-3717-b05b-8e984000600f | -15.07 | -48.5 | 2026-09-11 17:15:00 | MSG-03 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8d30f6c5-9363-386b-8bd6-23ff29d6afcd | -3.0 | -50.41 | 2026-09-11 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4a47493-fdbb-3230-a104-543059e3ac30 | -2.97 | -50.46 | 2026-09-11 17:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04810e36-ce89-3103-b219-416cc2314334 | -11.9547 | -49.7512 | 2026-09-11 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 8721c73f-110e-3416-bf25-83429f9c90b3 | -10.5475 | -51.3578 | 2026-09-11 17:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 6202de66-eb4a-3f11-bca0-52bc507a5446 | -13.3038 | -61.8275 | 2026-09-11 17:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8b950711-e013-3521-838e-0306ec251ae7 | -9.0797 | -65.491 | 2026-09-11 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 0af42132-23b0-3034-92f7-387bf851f7ea | -13.209 | -61.8144 | 2026-09-11 17:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 75a8d1f3-afef-377d-a715-7747a59ed24f | -6.6036 | -58.5972 | 2026-09-11 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7f4cefdc-4dec-3291-b36b-c4d9525c6097 | -13.268 | -61.597 | 2026-09-11 17:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ee2a668a-5306-3430-b4dd-f6840eb1ee2f | -11.2488 | -54.1378 | 2026-09-11 17:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 285.4 |
| 058cccac-f201-3fe5-96c5-ce421d16e736 | 1.2797 | -50.6843 | 2026-09-11 17:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b220b430-0198-38de-b06c-6edcc27bb6f6 | -13.2088 | -61.8338 | 2026-09-11 17:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 118.1 |
| cfda2ce7-f756-31b2-8b41-928166ae3047 | -13.3623 | -61.6683 | 2026-09-11 17:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 122.4 |
| c64960e1-594d-3e2c-aeca-07ab23f62819 | -8.9873 | -65.4379 | 2026-09-11 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 4c396041-94ff-3381-b992-3a89d1f98021 | -9.1167 | -65.5085 | 2026-09-11 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7996a8a2-c5dd-3c97-9cc3-9e49d09464c2 | -9.7131 | -65.0013 | 2026-09-11 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 6aae879a-f4ce-37c3-aaf6-6b7aa39ad81a | -8.6311 | -66.5101 | 2026-09-11 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 9c1c5028-bef0-3840-893c-98dcc4c554c2 | -6.641 | -58.4987 | 2026-09-11 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 91490355-c580-3e5b-9c07-f47b6b9a6fbe | -10.7084 | -50.6212 | 2026-09-11 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| e3f9be83-7377-330c-9b2a-ad3c1d3762b6 | -13.2682 | -61.5775 | 2026-09-11 17:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 101.8 |
| ce2d7fe1-2f8c-3882-9670-502a0807f4b4 | -13.2848 | -61.8287 | 2026-09-11 17:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 34ce663e-493e-32c9-8850-d44fb9e94c6a | -6.7864 | -58.8801 | 2026-09-11 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 25399716-5955-3912-a1a3-7b777ff535c8 | -9.0243 | -65.4554 | 2026-09-11 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 01c38cad-e5aa-3ade-9e03-4b5cce3ab858 | -13.3038 | -61.8275 | 2026-09-11 17:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f948c575-3962-3099-99a7-ba21816dad56 | -9.0416 | -65.7163 | 2026-09-11 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6be96845-8f50-3bbe-8c6c-62a53e04024a | -9.7889 | -43.48 | 2026-09-11 17:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 256.3 |
| 6fae8ea7-1d87-3466-9401-a1250f056f13 | -13.3247 | -61.632 | 2026-09-11 17:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| f8a481ee-42f3-3277-93fe-9dd3720ecfa1 | -9.1442 | -67.8317 | 2026-09-11 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 43f1904c-68dc-32c5-9de4-c2f9e2cb207e | -9.1443 | -67.8132 | 2026-09-11 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 2ae2c3ab-847b-3b42-b88c-011e2c3f15a2 | -9.9041 | -45.91 | 2026-09-11 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 8234e125-a379-3ace-b2f8-de6e0f282a4d | -11.2488 | -54.1378 | 2026-09-11 17:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 257.9 |
| 933fac2c-0be6-3a03-a528-591f8d4291d8 | -11.9547 | -49.7512 | 2026-09-11 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 168.9 |
| 589159c2-67a4-3c33-89a7-d1c1a82c8c71 | -6.6226 | -58.4995 | 2026-09-11 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6c9f0d69-85d5-3a36-b93c-807176ba4ab6 | -10.7274 | -50.6192 | 2026-09-11 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 235d845c-0189-30a9-99ca-c273818c2210 | -9.5003 | -66.8017 | 2026-09-11 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| b3f17830-4c14-32db-8ae6-038edf80173a | -6.7863 | -58.8995 | 2026-09-11 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 01561750-a0a7-3280-b235-0e0214095b19 | -6.2956 | -41.7064 | 2026-09-11 17:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 4a961656-a3a0-3733-9407-eeb428837d17 | -13.285 | -61.8093 | 2026-09-11 17:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| a8d18393-3132-3b4f-a135-72c5d3de7c8e | -8.8946 | -71.2788 | 2026-09-11 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 982db6cd-e14f-326d-b094-3cbd1b20e6cb | -9.0796 | -65.5097 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 4a44b037-3919-363c-baa9-2c23fbb6112c | -12.4641 | -62.5558 | 2026-09-11 17:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e610a3b9-421a-343c-8439-658d3b6b5041 | -10.7274 | -50.6192 | 2026-09-11 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 0af7ece2-51e8-384e-a81e-04306d06c370 | -10.7084 | -50.6212 | 2026-09-11 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 76f933e9-8231-328c-9de2-04ea503d6463 | -9.0057 | -65.456 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 9dd24c0e-0369-3ceb-aba5-4c9be5996bd0 | -6.7861 | -58.9382 | 2026-09-11 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 931740bb-56b3-34e5-b4d9-f7947e1ee33f | -6.7864 | -58.8801 | 2026-09-11 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 67ebe8e0-a596-302d-9121-5371b495cadb | -9.8079 | -43.4775 | 2026-09-11 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 299.5 |
| 25afd800-24f3-3d38-ba23-f1f442f356bf | -13.2848 | -61.8287 | 2026-09-11 17:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 26663124-c1cc-3ddd-aa1e-35b38bee5493 | -8.9876 | -65.3819 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 7e98758f-bca2-378c-a1b4-cc51af1b72fc | 1.2981 | -50.684 | 2026-09-11 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 919c8b06-3351-3cd4-96f3-5cd8c12d76e7 | -9.5003 | -66.8017 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9c0e23ff-9797-3761-8ec2-50386981a1ac | -9.7131 | -65.0013 | 2026-09-11 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| b730a0ed-20bd-35af-8762-6ba776879b2e | -13.3038 | -61.8275 | 2026-09-11 17:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 200c2a32-38b6-3080-a2cb-1d073ec77c3f | -6.641 | -58.4987 | 2026-09-11 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 9b264022-ddb4-3ccc-9249-0eec7d5b4f1d | -9.1167 | -65.5085 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 0543692f-bc38-31f3-978a-8c8581b0114a | -9.0981 | -65.5091 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 066804b2-1968-3d9a-a12f-ba576a017a74 | -8.9873 | -65.4379 | 2026-09-11 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 1c833b5b-b670-3674-8ba8-16ab4da19f0e | -11.2488 | -54.1378 | 2026-09-11 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.6 |
| b49b277e-35eb-3dbe-9bf9-660b01f8c327 | -10.5475 | -51.3578 | 2026-09-11 17:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 159.6 |
| 4d2e9356-96df-3319-bf31-2e9e91ef20e6 | -7.8412 | -73.4066 | 2026-09-11 17:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 0bc06010-2173-3dd9-a90a-b288f1b5e2dd | -9.1257 | -67.8322 | 2026-09-11 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 36341799-8787-3b20-95d6-e1f021ef36e4 | -9.494 | -68.4895 | 2026-09-11 17:40:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0b4e650c-2258-332f-a152-c7d2f8645e11 | -9.1443 | -67.8132 | 2026-09-11 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 5dc8ca58-3bf0-343e-be43-59dfc0487cc2 | -6.6226 | -58.4995 | 2026-09-11 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7e885686-7464-342e-ab77-33d3c2046826 | -8.6381 | -47.4096 | 2026-09-11 17:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a7c082c9-faeb-3e65-824c-92bcc829c6e6 | -9.1442 | -67.8317 | 2026-09-11 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 60c5c32c-4023-3916-8d0f-c0f9f252d633 | -6.7863 | -58.8995 | 2026-09-11 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 0bc2871e-3389-35f1-b32a-e12d06cef58d | 1.2797 | -50.6843 | 2026-09-11 17:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1d294944-c51e-3f80-9d46-cfa8f7ac8530 | -8.0628 | -72.5119 | 2026-09-11 17:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7af49db3-fc14-3ddf-9bf2-096f611ca407 | -11.9547 | -49.7512 | 2026-09-11 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ab20a3cd-d6b1-3ab0-b884-d4d1c35c358c | -13.3433 | -61.6696 | 2026-09-11 17:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 140.5 |


[Clique aqui para ver as próximas entradas](README48.md)
