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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e23c0b05-0755-35ec-a1e7-a3cc1d746ee1 | -5.82432 | -52.32261 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 32dd8b49-d2c9-3f7b-aba5-be657361f152 | -7.35627 | -55.17646 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| dba7e72a-5566-37c5-855a-a4c29a41a692 | -8.94752 | -50.79572 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| de937123-4000-3481-a489-7b528629a969 | -6.9417 | -58.95205 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 047eb739-a53a-34a0-b376-6584e81cd8ce | -6.17179 | -57.78791 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 29d6f443-9b03-3c19-9e75-82ea1e6ba94e | -4.92531 | -55.76361 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d21069e8-7c54-33c7-803d-0a84a4c85f84 | -8.11356 | -51.65794 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 085ea50c-2fd3-3c7e-89de-a9434360a7c3 | -10.76083 | -53.97765 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 4a0a18f3-9c89-387b-be38-e7b35e5f9dcf | -3.67336 | -56.78209 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b5a17fc-4b8f-37e5-a8a5-d16062d4beec | -8.95566 | -62.3895 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| bac359e1-1143-3dea-b78b-8559fd7d73e1 | -6.77013 | -59.4434 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 74cb762a-3fb9-34ac-bced-c488833388b6 | -7.36194 | -55.16812 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 983c5697-081b-337b-82c4-65b0c0db0ec1 | -6.75066 | -55.6774 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2fdd7f39-3624-3b35-ad22-ac4b1f5716b5 | -5.77275 | -57.55713 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c06ca3ab-126e-321b-95bf-d7af4bd63e42 | -9.97374 | -53.93702 | 2026-08-28 17:28:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 03113a7a-705c-337a-b8eb-5a9fa5bc7b45 | -9.25197 | -57.07088 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4bdb02c6-e589-30fb-9bfd-df416a79fb70 | -9.76314 | -64.97552 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 8b48756f-43ce-3202-aaff-43b541105dd1 | -6.72127 | -59.45055 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 59caf341-039f-3db8-a5b4-6d4992fe9335 | -7.581 | -61.31991 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8b67fe6e-f159-365a-a80d-feb13fc6a22a | -7.74014 | -61.09447 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d87a2a7d-3c79-30d7-99bf-a1db1ee74d31 | -9.96986 | -66.7916 | 2026-08-28 17:28:00 | NPP-375 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 65da5459-8d2c-38da-8d6e-274beeed3d83 | -8.38306 | -46.60809 | 2026-08-28 17:28:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 70cf99de-7d93-3a5a-93f5-6cd6a7bdc24d | -7.92338 | -70.66218 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d7808101-b942-3793-8344-adb99f9aef20 | -9.22737 | -59.77182 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| ec419b18-ee24-3e69-9609-a2212650cffe | -8.79827 | -49.99167 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 03530b47-6382-39b2-b6ff-3a4bda9727cc | -6.32283 | -54.74604 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ad279993-35a6-343c-85f8-86f9738f413d | -6.51495 | -55.23949 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 19d77b30-d171-3fc5-b022-d7632d747437 | -8.6004 | -54.83052 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e77986f6-26f7-311b-96ef-5ae861bb3a52 | -8.87403 | -45.99985 | 2026-08-28 17:28:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c6f00595-b451-35ab-950f-a353abcfc7ba | -6.78131 | -59.44582 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b53d2a46-eebb-3268-8241-52e9a85f43c1 | -5.34317 | -45.15195 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 108d16c6-c64b-3f5c-8559-136c2a0366be | -6.54002 | -55.24636 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c55e7687-9a81-3dbd-9692-08a760b1d3c7 | -10.41196 | -61.2 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 0382220a-a622-3248-b58a-41fb0c5803af | -6.33556 | -54.73618 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35026cd8-4881-3b5f-bf77-036aaa89cc16 | -1.94474 | -44.76311 | 2026-08-28 17:28:00 | NPP-375 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 6d6b1ac1-3d04-3ebe-873c-7f6bd7faca78 | -9.00052 | -65.45463 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 91b744c5-749c-3835-8976-772c2d86d6bd | -4.93686 | -51.42805 | 2026-08-28 17:28:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e1f709d9-3ece-3d7f-a9cc-e6f64a9cf729 | -5.77222 | -57.55365 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 90af1a08-9145-305a-baad-73217b9f76d3 | -8.77722 | -50.07487 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| e1c3c418-e2be-37eb-a307-0f6b86ab5e79 | -10.56017 | -59.61791 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 677d20d7-2245-32b9-8cd7-81ecc7a11cea | -9.04056 | -70.58324 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2b25f7f2-b6f9-39a1-a662-b3ccc4559b40 | -9.65643 | -53.64331 | 2026-08-28 17:28:00 | NPP-375 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c39c02b5-ee94-3858-8393-42409cc6a35b | -8.23057 | -54.96585 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e5088cad-2462-36d9-ba70-f5bc5123a488 | -5.88826 | -57.76454 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| ff3b499e-a80a-3860-84a7-cf0037f376c6 | -7.02769 | -55.68417 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| afab30e1-0596-3f75-9122-e144b9a4414e | -8.55966 | -54.90453 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 189c73cd-9be1-3219-afed-7a443c539cef | -5.98404 | -61.46741 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| d333a772-9be1-35c9-9fe8-bfaaf041a1f9 | -9.25305 | -57.078 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 620fa5e2-0fce-31cc-8207-f5ab131308bf | -7.77686 | -47.6347 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f114393d-1a25-37ce-a328-0a94fad1c77f | -8.40682 | -70.34637 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cee2bbbd-128b-3bc9-8770-1e076ae1c4b1 | -9.76285 | -64.97672 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| ed88c8a3-e873-39bf-baa3-cfccc05f722f | -9.11181 | -60.3044 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 373c7fd5-1195-32b7-acd9-c513b0c8ca84 | -8.60954 | -54.71466 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b737643f-cb60-38b6-bbb7-1a09404ba539 | -5.91847 | -61.40044 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 29544848-7857-3cae-bade-b53ce5f34253 | -5.97522 | -55.6943 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 772df438-e108-37a0-bb9a-e7622a9ee43a | -5.76888 | -57.55415 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 120e2955-e2aa-32cc-ad46-71c92d3bf1bf | -4.89548 | -56.268 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a18a7707-eea4-3ba7-93e2-f72e19c8210d | -6.52345 | -55.23012 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c48bc78b-0229-3e1e-99a4-eb6bcddefa47 | -7.02965 | -45.77328 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 96ea3112-995b-37f8-a844-44fa871ec9d5 | -6.02106 | -57.79054 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| be951b60-a1f8-3fb5-a016-51b7595dc5a2 | -8.59143 | -55.2824 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ec859d85-1eb8-30d4-b7f2-93f27ae8a753 | -6.65857 | -58.50386 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a30e9eb5-2393-342d-b2cb-fbd0a12b0e24 | -8.99259 | -65.43536 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 213f8519-8640-3ae0-aa2d-801a1d587fb6 | -6.275 | -53.14122 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 78188710-e687-39bb-9aeb-e5fcdafa58fd | -7.52435 | -55.65259 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 22f9e58b-f528-3808-bd47-070a38b7e784 | -6.54387 | -56.26168 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e7da2d74-a877-3d00-93c4-cabcbb9e3673 | -6.95081 | -45.23488 | 2026-08-28 17:28:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58f511c5-7bbf-3f6d-9cf3-2b5eb1e6e39e | -2.72671 | -47.03488 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5d25d381-cd17-3499-abf4-81bc773e8232 | -6.75349 | -58.71942 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 2936f709-1011-3e76-833e-a04315e1fbad | -4.89884 | -56.26748 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a9a71908-647c-36da-b052-0f1d937d6e61 | -6.1171 | -57.82558 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d51a46fe-6277-361e-92e6-9c3b7ad9a32a | -7.13879 | -48.06859 | 2026-08-28 17:28:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4203428-0127-3594-90cd-c2c3997737a7 | -9.22611 | -59.76315 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| decb5e0e-5035-3adc-9d59-75e8e9698b86 | -6.84442 | -59.94934 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b8c528ad-4f21-334a-b76f-b408fee16336 | -8.01693 | -48.01163 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edc65c69-882f-329b-9ec3-b74bdfeb150e | -5.78685 | -57.60492 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c8704c2e-ee02-37af-87ef-6782a9151b73 | -3.54782 | -54.48965 | 2026-08-28 17:28:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7b203a56-d372-3b0f-b4a0-603d5894a984 | -6.77876 | -55.68043 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9130507e-3986-3026-8f70-ca45d06a00aa | -5.57985 | -47.45086 | 2026-08-28 17:28:00 | NPP-375 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14d59d64-fbd8-3ced-93e7-66fda90962bb | -10.39515 | -61.1987 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 46eafe7c-69ae-301c-82ae-0d410126aa06 | -6.38498 | -65.23884 | 2026-08-28 17:28:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 251e1d3c-e824-3b1a-90b4-f3419bc9080c | -5.00407 | -56.13791 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 849c8f2e-2046-327b-a8cf-3156fd4453e6 | -5.37414 | -45.65941 | 2026-08-28 17:28:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28addf91-6d06-3fc6-b170-7b38cad789c5 | -1.62265 | -45.03213 | 2026-08-28 17:28:00 | NPP-375 | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 08222cf4-e6c5-3f96-98b0-000429a487f0 | -8.5822 | -54.82585 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 5a3f55ea-19a8-3ef3-9d84-a863c53cd618 | -6.1398 | -53.51737 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b13274a6-5608-357c-af28-655abe5c1687 | -6.75404 | -58.72313 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 272.7 |
| eb2d371b-1ac3-3858-95c3-88857481a9c5 | -5.82351 | -52.31758 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 8e780007-6a4b-30ac-a7df-775216c0c6d7 | -6.9371 | -58.94494 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 923db8fc-a035-370d-9ef4-73ec66412b5b | -6.42303 | -61.38832 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9ba52ac9-7a5b-34c1-9f7d-32b553507021 | -6.9078 | -43.65181 | 2026-08-28 17:28:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c389b524-fd95-3780-8ee4-0b3a9bbe9057 | -6.79957 | -59.39885 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.6 |
| edd5f60c-76f0-3167-8dc0-1d4e1d4f5c64 | -5.80164 | -57.63479 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c3afeab1-2f11-3125-91f2-0576bcffd0ff | -8.33941 | -45.72973 | 2026-08-28 17:28:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 736158b8-06e2-3dfe-bc7e-b97ba7e0f37b | -9.03967 | -70.5759 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b02f881b-7c21-35c5-b70f-53ef5fa30d7c | -4.96279 | -56.27148 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e7663c62-2aa8-3a3d-b824-acfb6926e2d3 | -6.97919 | -55.64486 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7c2134dc-28d4-3bde-b3ec-927d7810cd45 | -6.13073 | -57.87031 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| b91d8793-8e21-3038-89d1-1bcce95ffa84 | -10.05305 | -68.83706 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 2d8dbaae-1ca7-34a4-a881-2e1e568edf6e | -6.48835 | -55.90179 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README128.md)
