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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74c778af-5f05-31d7-99f4-9438086858f8 | -6.3257 | -62.6721 | 2026-09-16 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5674f788-d792-3987-9cde-a207918a4696 | -18.0298 | -50.9606 | 2026-09-16 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 48.0 |
| bb1be664-2f6e-3bec-9bad-6d9d1c74d79c | -18.0303 | -50.9385 | 2026-09-16 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 75da314d-03f2-3f7d-9182-ac0623606ae9 | -6.344 | -62.6904 | 2026-09-16 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| cb44fc9b-fe0b-37c6-bc29-d1f37eb0a33c | -18.0497 | -50.9571 | 2026-09-16 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 27ad4170-e1d2-33a5-a8a4-2fe302c6f7ea | -6.3257 | -62.6721 | 2026-09-16 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1e1154ac-4145-3567-850d-8a50a37fac5f | -18.0502 | -50.935 | 2026-09-16 06:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 76d068fc-222c-35ba-a9cb-c5caf90c1cf2 | -6.3256 | -62.6909 | 2026-09-16 06:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 69550d8a-d430-381d-bcf7-904e56c96e46 | -12.6064 | -50.7691 | 2026-09-16 06:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 81c4b628-fe2a-340f-9412-c19fe31112ef | -6.3257 | -62.6721 | 2026-09-16 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9d01c902-7dc3-39fb-be78-742c85aa3ba2 | -6.344 | -62.6904 | 2026-09-16 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 1580a44b-f80e-3cd3-a89a-32563e58232e | -12.6067 | -50.7476 | 2026-09-16 06:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 0ea1c1c3-bedc-3bf7-bcc3-6073a6b68c73 | -6.3256 | -62.6909 | 2026-09-16 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 42e64493-8c22-3d5c-9212-c67dacedc0c5 | -12.6255 | -50.7667 | 2026-09-16 06:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b26054dc-cdf1-3cc3-9e14-bb3ff02a2ae5 | -6.344 | -62.6904 | 2026-09-16 06:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a7587e19-8105-39eb-a395-02a14d74191d | -12.6255 | -50.7667 | 2026-09-16 06:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9d98cad9-a34a-3600-8536-e82c9f64c36b | -12.6067 | -50.7476 | 2026-09-16 06:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e14c4329-a899-3b2e-870e-8230735578c5 | -12.6259 | -50.7453 | 2026-09-16 06:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4e515b07-f12b-3648-b0cc-b33a2b43dadc | -12.6064 | -50.7691 | 2026-09-16 06:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c1b355ea-1f0b-3461-94d5-b82d22060b71 | -12.6255 | -50.7667 | 2026-09-16 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d0f71afc-3ed9-3d21-836b-699ea94d1e4f | -6.3256 | -62.6909 | 2026-09-16 06:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 042198b8-73d1-3895-99b0-4b04becae280 | -12.6259 | -50.7453 | 2026-09-16 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| cda59495-5e74-3f48-b137-1ea538db4b3b | -12.6067 | -50.7476 | 2026-09-16 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5571dc06-4b48-36b4-afce-ab338caa8cc5 | -6.344 | -62.6904 | 2026-09-16 06:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 6408ceea-422e-3991-9662-dd85ba19d434 | -12.6064 | -50.7691 | 2026-09-16 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4f221b37-fe33-3ad4-b558-ae50087b1405 | -7.60973 | -67.24783 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53245322-0be3-3d05-85e9-e98c535bf07d | -7.63987 | -67.17243 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1beed501-3a1a-3b66-bbf9-e61c4ae27887 | -7.64737 | -67.16743 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ab4dec80-f06b-34d8-b523-d4d7020e719a | -7.6466 | -67.17347 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd32b80b-3be8-35e6-b0b5-cd2e7fb4e918 | -7.61645 | -67.24874 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1fa56cd6-c83a-3db8-893a-c5c59b2445b3 | -8.64675 | -66.59232 | 2026-09-16 06:40:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6e1885a0-015e-367f-8492-3ccd7bb3b20d | -8.54501 | -71.49262 | 2026-09-16 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dbfdd5a-1015-3cb2-8d97-0fa078f6efbf | -7.65412 | -67.16839 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c57e45ce-ea34-3155-96b6-c499e5881298 | -7.64995 | -67.16646 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| be272b5b-4fd8-3182-8c80-56e7b3cad840 | -7.65069 | -67.16037 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c8cbcb8-bafa-3e3c-b06f-539db3f3b677 | -7.6567 | -67.16742 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 995f926e-7d25-35ee-889c-9586a8c53afb | -7.64064 | -67.16638 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ff1b082-397d-3578-8cf0-c29fc46a7f80 | -7.6549 | -67.16232 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8c2d386b-3f57-315b-b5e2-ac59e9283d19 | -7.64921 | -67.17252 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1494a488-f337-3267-b121-7fb345952ef0 | -7.64815 | -67.16135 | 2026-09-16 06:40:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd279dc0-445b-3111-899a-ff00745c8c1a | -6.3257 | -62.6721 | 2026-09-16 06:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4bcaa148-9f7d-3f52-ad0e-124893b1c318 | -6.3256 | -62.6909 | 2026-09-16 06:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 5bba4361-8c87-3f1c-a110-cd690b159bac | -12.517 | -45.9205 | 2026-09-16 06:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1d0d9285-d644-3b1e-bc21-3a7523b2212b | -6.344 | -62.6904 | 2026-09-16 06:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7583f8aa-5895-3e2f-a77a-0c4405971b43 | -6.3257 | -62.6721 | 2026-09-16 07:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b40dfb94-8681-3c09-931b-3280003c1341 | -12.6067 | -50.7476 | 2026-09-16 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e724c74e-c959-3a3a-8773-cfe7f17aa531 | -6.3256 | -62.6909 | 2026-09-16 07:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9b126862-fa42-3506-b999-f8fafb49aee9 | -12.6064 | -50.7691 | 2026-09-16 07:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 885df27b-2c10-33e1-bca4-d3ffa43cc558 | -6.344 | -62.6904 | 2026-09-16 07:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a1943339-2d9a-385d-97c4-64de2fe067e7 | 1.18066 | -50.95325 | 2026-09-16 07:07:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf577bc4-3e33-37c4-b2eb-6503bd2cd6b9 | -3.37828 | -50.83281 | 2026-09-16 07:07:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2f96a370-3223-39cf-8b57-53a729407a00 | -5.12762 | -47.60538 | 2026-09-16 07:07:00 | AQUA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d4c8dda9-55fd-3644-b1e6-f200b5feb857 | -4.36525 | -47.78474 | 2026-09-16 07:07:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 721022c9-90c7-3063-9c64-3f64d62ca0fa | -3.53926 | -53.98703 | 2026-09-16 07:07:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 225c8c11-85a7-3c73-bc24-20716746cff9 | -2.1052 | -52.05384 | 2026-09-16 07:07:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f07318b7-a295-3c51-aafd-c98f4dad8bbb | 1.17323 | -50.96324 | 2026-09-16 07:07:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ff085def-2454-38a5-85d3-11f2f63f2b6e | 0.17407 | -51.4599 | 2026-09-16 07:07:00 | AQUA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff2b4c09-a87d-337b-8ceb-1d5cf3421ee3 | -3.73343 | -55.93551 | 2026-09-16 07:07:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3eb397e0-b52d-33e1-a619-f288132e0e5f | 1.17191 | -50.95454 | 2026-09-16 07:07:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| aa75f571-1bce-3f39-afb0-be772b3c2f9c | -3.37689 | -50.84204 | 2026-09-16 07:07:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3e2a2759-5c25-37ce-860c-d148d3fae5fe | 1.17934 | -50.94454 | 2026-09-16 07:07:00 | AQUA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 533bddca-b0dd-3e4e-8b2a-e511c7880d2d | -2.10652 | -52.04515 | 2026-09-16 07:07:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29c348f6-7aac-3bc6-beda-f88ed0cf599e | -3.0153 | -51.34268 | 2026-09-16 07:07:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54008c53-88ff-3573-ba1a-9ab44de45ac6 | -10.10312 | -45.60973 | 2026-09-16 07:09:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 0da660b0-1c1e-35ef-91ff-fa98781c4a0b | -4.53891 | -54.92847 | 2026-09-16 07:09:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 301359ca-68b7-3ec7-b558-5500727298f7 | -5.63388 | -51.69595 | 2026-09-16 07:09:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf73e717-46c8-3f40-982e-94ba796ab716 | -10.93297 | -54.07971 | 2026-09-16 07:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6d1c963-da04-376e-96f1-ce749604d299 | -5.69366 | -52.28967 | 2026-09-16 07:09:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b264041-f392-3dce-8dc9-08348b02270c | -10.69743 | -54.17641 | 2026-09-16 07:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4882995a-fcc2-35db-9117-99d741d4fbd7 | -11.78711 | -46.59229 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a1b05118-16d4-313a-aa3c-21dd6a96e6d1 | -10.76847 | -46.21662 | 2026-09-16 07:09:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8b31d38c-ac08-3c5d-abd6-9f9d385869d3 | -5.75418 | -57.59469 | 2026-09-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ffba7a77-7967-39af-89c2-6f9e788df929 | -9.38572 | -60.31174 | 2026-09-16 07:09:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 79a0f49c-d85a-3640-8946-179f1a417c3d | -10.10694 | -45.59015 | 2026-09-16 07:09:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 29e1321c-a1a4-32c1-afb8-2731c9776e9e | -5.85712 | -51.93974 | 2026-09-16 07:09:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44206e77-9860-38e1-be08-3d30f5a029e3 | -12.59775 | -50.75849 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 24.2 |
| b932ed5e-8771-3104-be28-b7260000923c | -6.7106 | -58.80412 | 2026-09-16 07:09:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 58c8df8a-3b2d-334c-84ae-c6de73eaa12d | -6.32434 | -62.67839 | 2026-09-16 07:09:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 9cbec2ba-265e-344e-9950-6da75e341fdc | -10.10369 | -45.61655 | 2026-09-16 07:09:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 5c874949-8382-3fbb-a226-488125015951 | -4.57028 | -54.9126 | 2026-09-16 07:09:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 67139c07-1811-3558-8100-2f9101fb0b73 | -6.76721 | -58.80058 | 2026-09-16 07:09:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 522d4465-4e13-3fd9-ae02-dc1fdb3a3ccc | -11.54278 | -46.86027 | 2026-09-16 07:09:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 798b7f60-9bbb-387d-9649-b366f805a921 | -5.15066 | -55.93394 | 2026-09-16 07:09:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 372933d2-93e3-3eb0-9773-b71ba0de230a | -9.80437 | -46.49089 | 2026-09-16 07:09:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0f291689-04f0-301d-a462-aab5cb9b7895 | -5.13072 | -55.93113 | 2026-09-16 07:09:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6ae2adf4-aab1-3949-aad6-0cfd3295f796 | -6.37066 | -55.82518 | 2026-09-16 07:09:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 75fc7437-1502-39bf-8afa-fcbe2953d6b1 | -11.19574 | -55.02408 | 2026-09-16 07:09:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8d366b34-bbc1-3320-b20a-3d099d8b11b0 | -11.88789 | -43.8217 | 2026-09-16 07:09:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 3456488e-a021-3678-87e5-cd2fdb9741fd | -12.11381 | -57.19006 | 2026-09-16 07:09:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 53b3f21c-30e7-367a-91bb-3949e5ae6f6b | -6.02642 | -57.76979 | 2026-09-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 94265b70-cc26-3d16-b4fa-2e1c8707b569 | -9.79081 | -46.48916 | 2026-09-16 07:09:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| e0a3d050-1467-3d4e-af44-5048f6d4e251 | -10.69878 | -54.16753 | 2026-09-16 07:09:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56ef94b5-3d8f-3b73-aa06-020686b79cef | -12.60956 | -50.74781 | 2026-09-16 07:09:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f302088b-5f7a-3c25-8548-c0ef95644531 | -10.77542 | -46.19936 | 2026-09-16 07:09:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| ae1718c5-275d-3218-8cb0-e1e7a9336a2c | -9.3858 | -60.29802 | 2026-09-16 07:09:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fb65d535-a642-3ff8-97fe-ea77c9a9ecd0 | -5.63524 | -51.68692 | 2026-09-16 07:09:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c1e29e51-2931-33aa-a04a-8f415bc50c9f | -6.02654 | -57.7642 | 2026-09-16 07:09:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 10e1b822-ad11-33ab-ad27-674fbf8e64c4 | -5.15245 | -55.92258 | 2026-09-16 07:09:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ec559341-5686-34d6-b04c-1e08fae2498b | -10.40579 | -48.64358 | 2026-09-16 07:09:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 24784c4a-f139-3410-85cc-b9f45c67b192 | -9.70655 | -52.02217 | 2026-09-16 07:09:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |


[Clique aqui para ver as próximas entradas](README67.md)
