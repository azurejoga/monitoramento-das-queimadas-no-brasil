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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4de3195f-b015-3dfa-9795-1252356e8afc | -7.61278 | -61.61469 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0853c1ce-0c96-35df-859d-a81d8b71d5c8 | -9.17116 | -58.33463 | 2026-08-23 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83789a1f-23ce-3450-bd3f-985dc05b0b10 | -6.113 | -59.94026 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a489a424-e1b3-30bd-ba27-eb16a2aede3e | -6.82222 | -59.6618 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5ec72a4e-64a1-33df-aeef-777644fa7dd7 | -8.9273 | -48.54611 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e01bc0a2-39e6-3a37-8aa1-8396b132c9f3 | -6.89672 | -55.69928 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 06dc054c-a16b-3de9-8761-a3a50966e156 | -6.95163 | -59.07074 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a5dca67-609b-3079-946d-da0cf6fdddbc | -6.67622 | -58.74656 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c72f58df-520f-3313-b526-22af27e59eed | -8.68363 | -54.69596 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bf75128-1026-3a79-a4ea-f88931be3d01 | -6.69939 | -58.72601 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cab7f3eb-0de6-3afa-8c1d-fa6c286d7ccd | -9.65826 | -63.84431 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e083cf1d-e03e-3baa-bcd5-d121522a0ce1 | -10.83987 | -50.97737 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| af57156b-7bcf-3740-b578-f23b85d2fedb | -8.99217 | -50.75991 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 372f89f4-1769-3b53-9365-f99749418411 | -8.52874 | -54.81726 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a61864a-163f-37a7-86f2-c77a8cfeff12 | -6.43721 | -56.1814 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba2c2e8-d0f1-3d5e-ac9b-7fe797185f50 | -6.6647 | -58.74466 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a6abb8de-5215-3c90-a9b5-f39bf90b85b3 | -8.98966 | -50.76675 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b36720a-ad5d-355d-a97e-ebeaa7cae7be | -6.81118 | -59.65224 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6483c3be-d31b-3501-b915-be17f26e6046 | -6.79063 | -59.80174 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a65c0f43-d3a2-3f92-97f0-a32516c7ba38 | -6.77601 | -59.44178 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 572a95dc-4e28-30a2-bb54-8351cf056041 | -9.08047 | -65.40901 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e5358f0-8168-3f4e-8a2b-46281709afc3 | -9.09565 | -60.92374 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8d776213-ca0f-346b-9bf4-90029a517f9d | -8.52931 | -54.83516 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afe55dce-9b7a-3ac8-9b15-eaee70129633 | -9.21355 | -60.89964 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaf74c01-94f2-3f21-b077-66ceea144ed1 | -6.19708 | -53.53215 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9afafae3-15cf-3a78-8a4f-2a0d08d6b858 | -6.45029 | -47.66499 | 2026-08-23 05:04:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82a1e478-30f8-3e88-8a22-b4d53a88334c | -7.73843 | -46.17266 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7acbe22c-0240-34ff-96eb-168c5605610c | -8.52987 | -54.85305 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69212ca6-9984-30fa-b580-9e1bd84664a9 | -11.57934 | -46.94288 | 2026-08-23 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6c8639a-31e7-3155-8b31-4ab88bdb0e89 | -9.17693 | -59.45221 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02cceb26-6be1-3148-93e7-255e0b0cd936 | -8.98339 | -50.7559 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ef21f01-31af-3ce5-9535-f7b24984c508 | -6.82011 | -59.42416 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3690df0d-2aa0-3be6-96c4-6e78c883c5de | -8.53152 | -54.84263 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ac9ea55-e05b-3585-9f2e-6a87aed662ec | -6.69497 | -58.94369 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff7528ab-a83f-3a17-ab25-c24dea27f50c | -9.10336 | -61.58884 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e813470f-4cc8-36b6-823a-c8cdbdd7c0f2 | -12.23774 | -43.1273 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5d5632e6-b46b-3933-9076-857f50a96dbd | -8.91923 | -60.7182 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10e20bca-892b-3a9e-a8d9-9cd2c1432af9 | -11.43957 | -44.53099 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b5430d5-e75e-3bf7-8d67-c3b04ee3214e | -8.08515 | -47.26666 | 2026-08-23 05:04:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cfb1e907-6de0-3edb-af77-e27f06aaaf21 | -6.55335 | -58.53268 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90acfe94-6971-3caf-819c-22085fd7ef80 | -6.82566 | -59.6661 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8098ec0e-20f2-33db-8215-8c9419c6d750 | -9.13883 | -65.959 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6b36c3a-cfd0-320a-ab96-ed8e5b9a4e58 | -7.0131 | -59.56821 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 260a269c-a2fd-3d85-8992-346fd0014e58 | -6.11363 | -59.93641 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b57f511-4068-3b2a-88b7-c0d3a7e7a150 | -6.80224 | -58.64393 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4bb78670-b539-326e-a13f-8804518308d6 | -6.78919 | -59.43687 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b0352bd-e4dd-32db-ab09-ce92d1d8df43 | -6.87422 | -60.01404 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad385dee-4b9e-35d2-9b52-92a5ad174b6e | -6.65965 | -58.79798 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f25b1e7-64f7-303f-a082-fdc10e94e9a7 | -6.24012 | -55.38317 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 954b35d2-6fda-3f8a-af6a-922069815bdb | -7.06566 | -59.9777 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 604255ed-74e9-3179-9ae0-f2612fc7a131 | -6.8067 | -58.66404 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a19fc279-34c0-32b3-b110-1e8b429c3c25 | -6.88526 | -59.41441 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03821851-a90c-3974-bfec-da31622e251f | -9.02452 | -50.74217 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1ae15c7a-00ca-3280-824c-cbf109ef0ec5 | -6.18789 | -55.43624 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372bb6aa-94b2-3f15-a4f0-41d0c1c2b660 | -4.53099 | -55.51424 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78b6ff88-9b77-3c42-9b3d-98728b42a984 | -6.80446 | -58.65404 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc4a50ef-44c0-3903-acbf-688c0b2962dc | -6.81851 | -59.38467 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44c6e538-2d60-3716-86b0-d5857c502177 | -8.53097 | -54.8461 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45e1b323-4952-30de-a117-98ebb0500a05 | -10.38053 | -50.41057 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0bcf4839-3097-3af4-ab3a-e44025189195 | -6.94466 | -59.0645 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d58cc1ba-da10-3adf-b29f-bd554c74ee1f | -6.9345 | -60.08706 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee0d81d4-eb7f-3fe9-bc1d-0772097a2f3f | -8.39797 | -62.68655 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef528d87-ab56-363a-8c09-a85113416f36 | -7.5938 | -61.23271 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee668322-1ff6-3583-85a2-5c5a85b66383 | -11.61806 | -50.55605 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0e1f2e7-ceee-383f-adf0-e02c61bae310 | -6.08339 | -59.96317 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40459f8e-8c5f-3b33-8be0-e4f3f1235597 | -7.56363 | -61.19542 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8df8860-33dc-36dc-aaa3-601210787aae | -6.69329 | -59.09898 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1241b48-5f2c-37e4-8c02-95934ce39d24 | -11.84768 | -51.67458 | 2026-08-23 05:04:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4290a8c1-d04d-3847-8d6f-74a9eab5c592 | -4.9334 | -55.78259 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041a4df2-5ffc-3eea-914b-761b95926e10 | -6.79937 | -62.90432 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56c6d7e-e936-389d-8591-38a1516cfd3d | -11.57543 | -46.93246 | 2026-08-23 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3c7629d-bda6-3085-9cd2-d6e5e89b929b | -6.80188 | -59.65798 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c1db831-f43a-343f-9a47-8583b10f3fd8 | -9.39906 | -60.58394 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cafad1f9-ca9d-3ba1-9afe-dbd99c791885 | -6.37759 | -54.97106 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7338a2f1-a014-3229-a28a-65a50c95ecf0 | -7.66354 | -63.33993 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3449d62-8cbe-321f-a0e5-740a92e0afff | -10.70352 | -47.73735 | 2026-08-23 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9721d1-d0e6-3ac2-bc0e-9a4f7fd76aba | -9.43612 | -51.60311 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ddc3f270-fd58-31bb-b4ab-8e64eea92e47 | -8.59261 | -54.7135 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 849b8cb1-0a8a-36ab-a522-34d53406f38a | -7.78162 | -61.42725 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d428e9c-b174-37db-af1f-d78ded5b98c0 | -8.92901 | -60.71187 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 585e36b2-99a9-34b4-b132-bc1b2f6e7e80 | -6.5399 | -56.26228 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a615bba5-7bba-3004-bd2b-0c17be852fb6 | -7.43073 | -59.79062 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8462acc-af95-341f-ad0d-8988e0a39ac0 | -5.77414 | -57.57011 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 166b4325-d902-3f4a-bd19-ed802c0f590a | -6.97633 | -58.32202 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe97637f-35ba-3b5f-a72a-acd168672746 | -8.03755 | -54.01084 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0985aa74-a02e-3e4f-99dc-d045739a3383 | -9.52982 | -51.6505 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4405cc35-36ca-39b0-a8b9-1664da2fc97c | -10.83669 | -50.97189 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 39495ca7-54fb-3283-af15-c0544e4e862a | -6.88467 | -59.41788 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78f355ff-e9d5-398c-b532-6fc1a6679e6f | -11.204 | -55.08124 | 2026-08-23 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d03351-19a5-3d2b-a24b-0a1ce131a41b | -6.68932 | -58.73908 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4aba0fcd-e349-3f0a-8136-668e7c24f6db | -8.27821 | -57.35366 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7830303-d37e-387b-a500-644765f182e2 | -9.21286 | -60.90366 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a2c70448-6cdb-3b0e-9af3-18387663e454 | -6.16972 | -55.57161 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4d00176-ddfa-3691-87b0-00fac08b00fb | -7.46009 | -62.31485 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8b7b06f-ca72-3684-beca-4420ce1d88dc | -6.54331 | -56.26284 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 708a2db4-5e4b-3ba2-b113-53ac3b15e2c9 | -6.85096 | -59.41148 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e175ab-c2b1-3fac-8229-5159f3f66ad2 | -8.89705 | -60.54489 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b00f956-dd17-345d-a683-0f98aef8fe58 | -6.13467 | -57.84085 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2d6f4e7-54ed-3cd9-8a33-4f602121c8bd | -8.55799 | -54.84686 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d05a5c0a-9015-3e7a-a2f2-f2f1bed85bdc | -6.78506 | -59.65874 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README53.md)
