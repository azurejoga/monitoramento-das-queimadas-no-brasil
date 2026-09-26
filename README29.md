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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35b0657f-1b66-3885-9db3-7091ae3a3ae9 | -12.90626 | -61.71766 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02c8fb9b-1a30-3449-9c46-0a4d02c019db | -11.76524 | -50.64282 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcae8816-52eb-30d8-8cc9-bd337e356245 | -12.01052 | -50.64097 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f463b14-cd49-31cf-a3ce-f0c976e448f3 | -11.76603 | -50.63529 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1e1120d0-2314-34dd-8603-8e95d220dc35 | -12.9013 | -61.72589 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d66e6f8c-175a-337b-b411-79a7f44b2379 | -12.85112 | -62.16877 | 2026-09-26 05:50:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2404158f-cfbd-34d2-b022-36c6d87ccb36 | -12.90258 | -61.71711 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b76273f1-ab74-30f1-9044-e52c26b35668 | -11.87152 | -65.02831 | 2026-09-26 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 248af37b-9214-30eb-bc70-a6628e20d66a | -7.67568 | -72.28429 | 2026-09-26 05:50:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54af7eb9-1e88-39bf-a281-94584d16dbcd | -11.02364 | -54.04904 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13709ba0-6142-3d97-a634-8d63a25dde0e | -12.67244 | -54.64348 | 2026-09-26 05:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4fe2873-7213-346a-a3dd-fe07a0dd9be9 | -10.41282 | -53.81063 | 2026-09-26 05:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd6c89fe-ae98-39ef-8548-d3d6852ea4c5 | -11.87429 | -65.03239 | 2026-09-26 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfcafb40-d06b-371b-9b84-1fbe70d7d5c6 | -11.27575 | -54.43203 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f359162-3927-3d98-b257-7fa4cdbccea6 | -12.90194 | -61.7215 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58f00cff-df5d-32d0-b03f-33dbe7b58750 | -14.50768 | -59.80393 | 2026-09-26 05:50:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0995caa2-b814-3d24-be5b-75d6aed9deb0 | -11.75765 | -50.63657 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a703898-9216-356c-b2a3-2724186f554e | -12.01719 | -50.64359 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e312661-b8a7-34bb-b400-d781eec20a0e | -11.93323 | -50.59527 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5823c366-b2fa-359b-a214-6c56ff292509 | -11.77256 | -50.64372 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5a702b7-fd22-3101-bae1-ebe7d4cc8455 | -12.94608 | -51.06246 | 2026-09-26 05:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15971209-4932-3a13-8a19-bea4ce465d45 | -12.67292 | -54.63948 | 2026-09-26 05:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9154a74a-9cde-378c-83ef-13c6524fdd4f | -10.82128 | -57.20662 | 2026-09-26 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f79ce9-7606-3070-99d5-7c3b319d0785 | -17.04165 | -56.58172 | 2026-09-26 05:50:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 44f0c3be-4f92-3680-96ff-a7691ad05b1c | -14.50762 | -59.80357 | 2026-09-26 05:50:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8261adb0-f257-3427-af8f-7bfb993d4128 | -12.67195 | -54.6475 | 2026-09-26 05:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efe60ad3-3b8d-350e-aa5c-f99c8bafe1fb | -11.92588 | -50.59439 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d14f123-fa40-357e-b76c-5e59dd43b54a | -12.00985 | -50.64272 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c240022-22ba-32c5-b20c-dc90e064748e | -12.66711 | -54.63866 | 2026-09-26 05:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3a0a04f-96d6-34a9-96a0-ecb82a22bfdf | -12.01634 | -50.65116 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 347c02cd-84dd-3897-ba5b-dafd2c651ce7 | -17.0394 | -56.58576 | 2026-09-26 05:50:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c7dfaebd-023c-3a70-a286-55eb58c4ea63 | -12.90562 | -61.72206 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fc383c9-9572-31b7-8032-16135f2b58bd | -11.28205 | -54.42868 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 064fe50d-a9dd-33fe-b899-a30a9b5746fe | -10.41881 | -53.8112 | 2026-09-26 05:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efffc2ac-b851-3fd8-ac1b-04c21ce4ad68 | -11.8704 | -65.03537 | 2026-09-26 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b54104aa-1cb8-3ea7-83fb-448a45451dfa | -9.06248 | -72.21308 | 2026-09-26 05:50:00 | NPP-375D | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fab1d78-5f5a-38f8-80b3-0f129e7855a9 | -17.03981 | -56.58219 | 2026-09-26 05:50:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 32f5f34a-0da4-305a-9500-901396846902 | -12.03101 | -50.65283 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3db0bac2-889c-3996-8061-e70df58877bb | -11.28154 | -54.43283 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 55b51033-a0a0-3bd7-8315-5cd67085739f | -11.02958 | -54.04962 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cfaef58-42f9-36b3-866f-574f12a6b8e0 | -10.8165 | -57.20597 | 2026-09-26 05:50:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09d175de-9cee-3613-9399-11422e28728c | -12.60064 | -51.94543 | 2026-09-26 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3b7a25f-5493-31ad-b456-d7b47401ea1f | -11.28103 | -54.43696 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 10d4496d-39bf-3598-950c-f672fad7c665 | -7.68071 | -72.28518 | 2026-09-26 05:50:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8e061d-ad8f-33d0-b079-def1e6f82d8e | -12.89826 | -61.72095 | 2026-09-26 05:50:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0546b21d-764c-3e9a-9a1e-001bbc2e4697 | -12.02367 | -50.652 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d000069-bb50-34b3-a0a3-3687a1849a60 | -12.01704 | -50.64946 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c94cd9eb-a0eb-3bbf-8154-88e06c75837a | -10.41227 | -53.81507 | 2026-09-26 05:50:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be94d55f-7569-3b33-846d-875e4c8d16b2 | -11.75848 | -50.62905 | 2026-09-26 05:50:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3222ab9-4200-3a3b-82e0-f95aed3c1795 | -12.66663 | -54.64267 | 2026-09-26 05:50:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4386efa7-baf1-30d3-a9d5-f4eebfea2514 | -11.27525 | -54.43616 | 2026-09-26 05:50:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e9797a3-da59-3892-8309-bdcd1247faaf | -12.95332 | -51.06326 | 2026-09-26 05:50:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6420479c-c077-3d3d-b9a4-503d8a0bddf4 | -12.60675 | -51.95281 | 2026-09-26 05:50:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7af1d345-1740-33d0-986a-1fed20091a1c | -11.87762 | -65.03293 | 2026-09-26 05:50:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4756320e-2eed-358d-ab25-18be0cecc93f | -21.96092 | -55.93897 | 2026-09-26 05:53:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cdb6414-d295-324c-b701-6b8d5fe90439 | -21.9669 | -55.93975 | 2026-09-26 05:53:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 756e6e0a-3af3-31c4-af9e-290ba3299c7e | 1.5848 | -56.05927 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6be9cbda-0f54-3c0f-b2fe-eb4c37cd0a59 | 1.60942 | -56.03782 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 371df854-f7d2-36fc-abaf-a23d616f1283 | 1.62345 | -56.04109 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 847f4cf2-22da-3959-b2bb-5d6ab1b3e546 | 1.62229 | -56.04165 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4f426e8-d1d1-3ff9-992c-82de88bde2d4 | 1.60727 | -56.03274 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| afbbe231-744d-3932-b789-4dcddb72bac3 | 2.89941 | -60.28093 | 2026-09-26 06:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e14029d9-6d58-39da-b618-0647a97fbb96 | 1.6026 | -56.045 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0b0933b2-6627-35a1-bdcc-e5ee66145108 | 1.60822 | -56.03833 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 11f593cf-8c5a-364b-8c41-d0d5e1e261a8 | 1.57931 | -56.05989 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 780d3ae2-fd9f-3e23-8288-22d2a13ad36e | 1.60084 | -56.06786 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 255c0a61-a1c1-3fe6-88e8-a33dc3424e0c | 2.89362 | -60.27634 | 2026-09-26 06:03:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ace4a27-2ce0-39af-8122-ed6de838d08b | 1.60917 | -56.04391 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a41805b5-80a4-33ea-b6e2-475f44b3f78c | 1.60451 | -56.05616 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d6d3a316-dc26-34cc-929a-5863df6137f9 | 1.60356 | -56.05061 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f91c7f1e-18f1-386d-a515-3a73f632e5cd | 1.59794 | -56.0572 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a9627a37-9608-3a4f-8df2-ba85dfc6feb0 | 1.5859 | -56.05894 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d7a837-3058-326a-8b17-ed7546cd82f2 | 1.60469 | -56.05016 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c47206df-cd0d-3858-8c41-7110e20a9c7c | 1.62436 | -56.0467 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7baeffa-8488-345c-89c7-58960fd94b11 | 1.58576 | -56.06486 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efe548e0-497b-366c-b566-24fffa69b009 | 1.58682 | -56.06455 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4d8c2d1-39a4-3e23-8543-bccd11781a08 | 1.61098 | -56.01482 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d0d6ed96-4057-3c9e-9c14-62fdb16c4e6b | 1.60851 | -56.03222 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c176f91-bd8e-3199-a453-aa7fe2697196 | 1.59982 | -56.06822 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4a492048-f201-395f-b170-492239ad6664 | 1.62884 | -56.04051 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8107541e-b1f4-3d8a-9240-738207c6d18a | 1.62528 | -56.05236 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bb18b5c-73eb-32e9-91d1-b5cb93bbcca4 | 1.59888 | -56.06268 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 88d1898a-1d65-3de8-8408-e86fc0206975 | 1.59903 | -56.05681 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 61067a2d-3909-318c-b57a-b8da2aa71406 | 1.62419 | -56.05287 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 226b82c5-6f9f-3767-8bd6-0fa12d5d9156 | 1.62323 | -56.04723 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14678f67-d678-3f48-8bf7-9ed31fc204ec | 1.6056 | -56.05573 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b24c0bf3-5144-3e1d-92a8-fe044d6fed0e | 2.71653 | -60.68785 | 2026-09-26 06:03:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37e69958-4187-373b-8555-138a2b963624 | 1.60377 | -56.04454 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3e07afb7-8e18-3663-a7d9-0445cba63c2f | 1.59993 | -56.06229 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 088fcad4-33f5-302c-947b-051e28ffeb42 | 1.57184 | -56.05549 | 2026-09-26 06:03:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75c384ec-18e0-3ac0-9bae-d43c7ea3d927 | -1.68591 | -55.56009 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f93ab660-f486-315f-9778-da9e9f0f2936 | -1.34271 | -55.47461 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9d7fe10-4599-30fa-ab63-187fd6df12b5 | -1.69002 | -55.56274 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 30e2aa28-1962-37dc-8000-8b9b7bff35f0 | -1.68485 | -55.56672 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a92d477-c99f-312a-88f7-144c5b12aabb | -1.68901 | -55.56936 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b435eca1-a0e5-317f-a37b-4462f0404c89 | -1.3417 | -55.48129 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0ed6957-761a-3817-8f8d-94a45ed5121a | -1.68301 | -55.5612 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 984f686a-e284-39c8-8f1b-54965f345199 | -1.33461 | -55.48029 | 2026-09-26 06:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09006dbe-07d5-3785-897b-7a2ab98ce651 | -7.26449 | -72.69498 | 2026-09-26 06:08:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 720c52f6-21cc-34e9-846b-81ecdeb5c108 | -7.98186 | -71.34859 | 2026-09-26 06:08:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README30.md)
