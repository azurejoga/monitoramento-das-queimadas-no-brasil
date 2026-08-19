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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca80a860-3d56-39d0-ab08-fdccde50fd15 | -6.74783 | -59.04684 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db5fbb1f-d9da-323b-97df-57d986e31c19 | -9.39421 | -60.55242 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dfd1b74f-d798-3cc1-a9eb-bd843ff679a0 | -6.04279 | -57.804 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ecbc0a-16cd-39ae-8987-992d02e5e7e6 | -6.75676 | -59.16291 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 283a40b6-4078-39cc-93b7-17fad2bdf605 | -8.55418 | -54.7549 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f770453a-ca51-338c-8777-8a901589e54e | -6.12372 | -57.71863 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d707709-2c09-3d5a-87b6-b30fd49ea4d3 | -6.74614 | -59.16674 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a709dc-39bc-36fa-9f52-9620b28873e0 | -8.54971 | -54.73538 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 72205d19-b8fb-32de-aa3b-c4c1e1d564d3 | -8.5579 | -54.72445 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4cef19c-3581-3c86-a916-877d2ea34b38 | -8.89474 | -60.57079 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa9ce389-44d9-3e29-b072-68be866e3c53 | -6.02092 | -57.8417 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ff5cb38-1ec0-3a81-b940-70bcf4c56fb9 | -6.6905 | -58.94576 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 785a1f52-926b-3ce6-a4e7-82560493330e | -8.19058 | -55.00199 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 90904cc5-621b-3e5b-97b2-e915ff1f4f0b | -6.8442 | -59.00988 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e49eb894-05e4-3f23-beff-e1f9407d0141 | -6.00922 | -57.84724 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33c49f40-adbf-3819-a9f2-7e2a21c7b67e | -9.40024 | -60.56196 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d74ef4fc-be17-3142-9f2c-e190d92d6927 | -6.79415 | -59.44114 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41bb0306-1cf6-348f-b7d7-0d22fdb1c708 | -8.58873 | -54.73092 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcf7d54f-4b0a-31c3-81aa-dd9b28c7db33 | -5.49299 | -60.14092 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efbe426f-75de-325d-a3f3-674254752f1b | -3.93225 | -59.33038 | 2026-08-19 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55af2631-bf82-3cda-bd09-5b0f8a89c8ad | -9.42551 | -60.42569 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f248e5dd-dffb-3732-854c-87238af4ea5f | -8.89739 | -60.55158 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d46c6f0e-6b54-3c5d-bdc3-68a7519e2a16 | -8.56314 | -54.68153 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f64f98b3-71c7-32f4-80e5-9b338195093c | -8.56298 | -54.7708 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7775434c-2547-36c8-aee7-53534e17289e | -8.57442 | -54.73548 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0fbadf2f-73cd-357b-986a-da67e4ede397 | -7.61994 | -60.97036 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2765df0-d494-38e7-9ed8-fe051290e3e8 | -8.55351 | -54.76046 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| feede754-dce7-3093-8cc9-9e52221245aa | -6.3441 | -54.90935 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cea353c6-ecda-36e1-a2b4-2e44dce36010 | -8.54356 | -54.76212 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6137765f-4d8b-3f4c-ae6a-108e9dd5911b | -8.58343 | -54.73996 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| acc42710-fa3e-3ad3-929f-4d24c8f80e4a | -8.54666 | -54.73801 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 95e62bd0-eea0-3f1a-8b31-361e977e40bf | -7.05443 | -59.84245 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e78d6a10-44fd-34d5-9cb2-6a9b7a8196ab | -9.44317 | -60.29314 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3bc341e-908d-32c6-b438-e34e14779a28 | -6.1412 | -57.88236 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 162ae002-b441-356e-afa4-9900c6e74fda | -8.57226 | -54.77489 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb87a1ef-8d8d-3eff-a5e8-b7059dd696fa | -7.43171 | -59.78682 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 860c743f-74c7-3015-92e5-902f5cdec242 | -8.07762 | -61.35942 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa578417-4d63-3b50-bb87-fd3462b40be5 | -8.55116 | -54.72348 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ffd1788-685a-3d61-a41a-e74eba1cf8a7 | -8.57123 | -54.76002 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d1771133-9599-31a9-8343-4cfcc32c4c94 | -8.5767 | -54.73892 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3dd48cc-0600-3f6f-aebb-7e60839f3d4f | -6.76332 | -59.15222 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac9cb3df-6889-36d2-bfa8-983ddf6cfb86 | -8.57916 | -54.69901 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9d71af3-e6a8-3728-baed-c069085324bd | -7.04866 | -59.84016 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2be41f85-c84f-362a-a550-95fa563b72ba | -6.34338 | -54.91478 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88cb4875-ffc0-34bb-a367-5462b19dd45b | -8.56994 | -54.73815 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 92231b87-ea36-3888-b9cd-7af9216430b8 | -9.4049 | -60.56263 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 477064ac-5e60-31f2-90c8-56f943327ed9 | -6.14438 | -57.85935 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 920a1fe5-3eb1-31b7-a5da-6a1e32a102db | -9.39626 | -60.55647 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ceaa38aa-6863-3b6b-829c-8341b26b67a8 | -6.84481 | -59.00919 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a15d592e-23f1-390a-9ab0-0dcd78d463af | -8.56695 | -54.76248 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 50d766bd-93c7-33f4-9005-fcb7c954754e | -6.84499 | -59.00413 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2483f4a-26b1-3a9f-8874-f5144df920f2 | -7.61857 | -60.97233 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bcf029a-6851-3706-82bc-5f68cdd68636 | -4.46501 | -55.45786 | 2026-08-19 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd71a19-bf0f-3c2b-b9f2-e1eb932fdcde | -9.01443 | -60.51132 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ba56497-a3d6-345c-8f58-d23074f8f7c8 | -9.40678 | -60.58274 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28a9e812-3fec-36da-aa60-765239603a18 | -9.38954 | -60.55178 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a20de906-ce56-35c0-b1bd-2d7ddfc334ad | -8.57142 | -54.72606 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce437adc-d8cb-3349-835e-455e47b8c992 | -9.42596 | -60.41452 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d2a39087-1069-3b6b-8432-56bbc2555ee8 | -6.00294 | -57.85295 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd02fbb4-d9bf-3b93-b9e1-4b0bfc52b889 | -6.74537 | -59.17222 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be553ca3-0231-3e82-aa1b-1c944ae8a13c | -8.54678 | -54.75947 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a74f53e-95ba-36f1-bbfc-1e90181fd918 | -9.40623 | -60.56904 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58c8aa3b-6624-3bfa-ad2a-eb2ef97ef11d | -6.10508 | -57.73359 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 002959ba-182a-3fe1-973a-8a4a997a6c59 | -7.61235 | -60.96059 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5617b315-9656-3085-826d-af4ef3cd0b09 | -6.02043 | -57.84509 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 650927eb-e117-37b1-abb2-6f2c3b4e69dd | -8.5526 | -54.74514 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8946b6ff-2d88-3f79-acd0-3bf85916d247 | -8.57746 | -54.73272 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0cb321e-8141-37e5-a7d8-0e9f4be9b055 | -9.42384 | -60.42945 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d59421f7-b5c5-3c5a-b822-4e0487272e91 | -8.58044 | -54.76407 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 76cd4d1d-4c10-36d7-b4a8-fb3e03128f25 | -8.54142 | -54.72537 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4c302cd-5503-38d8-88d2-c1cc64d33e5d | -6.08422 | -57.91916 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ae9d7719-79c1-3375-a717-e1c25938fe08 | -6.3519 | -54.90545 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25a2eaac-5dc2-30cc-a290-2c4b38ab74d2 | -6.34469 | -54.90973 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50436718-6223-39d0-b668-a2d38ad32c61 | -6.14044 | -57.84829 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e058ed5-18a7-3f8f-9055-ebc9d3871ea4 | -6.81201 | -59.45465 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 059c031b-9510-39e1-978c-d6fd39382199 | -9.40892 | -60.58433 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40b8d802-1b9c-391b-9c0c-7f09c2046d87 | -6.60789 | -58.3964 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d13cb73-94ff-329d-8cc1-ee2e8df34d98 | -5.99762 | -57.85207 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2045d2df-fc77-3e85-b884-254d3be2f527 | -8.57442 | -54.75742 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 08edac68-4314-373d-937f-bdbf42843247 | -8.64585 | -62.83338 | 2026-08-19 05:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9530b0ae-dc99-359e-9192-0f8cfccd54d9 | -8.5879 | -54.73727 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e574203e-1891-3702-b7fa-09481f48cbb7 | -6.33896 | -54.90335 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a91965d0-5f04-3b94-be7f-8600c17ce14b | -6.88723 | -56.43469 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff55bc41-f185-3233-8863-9daa24f5ab60 | -8.55626 | -54.76979 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a5a0d91-70d3-370f-ab12-834d009f0125 | -8.58271 | -54.6902 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 202ddc0d-278c-3c5c-99c7-3ce941c0e892 | -9.42666 | -60.40955 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9294f0e-acc7-3a10-bee4-4fbcf0798bb0 | -5.49495 | -60.12731 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1122e167-869f-39c1-8693-94180e0c25b5 | -9.39695 | -60.55158 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0d0b3bd8-3a7e-3548-88e0-fd8d34746ff3 | -5.49604 | -60.14267 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e62de522-b6f5-3371-97b7-325741c5c775 | -9.42687 | -60.45123 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a20e426-cd12-3825-b379-6cdb3aa07645 | -6.74458 | -59.17776 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0041d7a0-6029-3c1a-9381-4f62b5739f09 | -8.56843 | -54.72878 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 84405711-071d-3aae-adff-a97a2b4f21ba | -8.57521 | -54.72937 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e20dcd5-5196-367b-b02c-485606906c2b | -6.14653 | -57.8832 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 685239f4-84e3-3520-945d-07512a89fa41 | -9.38693 | -60.55521 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 64f803e9-72d9-3578-8e33-caf298e6cdbb | -6.61232 | -58.95743 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd2a146c-5515-3d35-9a44-a39f750b4da3 | -9.3916 | -60.55584 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2f8adb6f-5946-3e7a-a165-c82f54e7ff9d | -6.0078 | -57.85707 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cfae207-c31b-3571-963f-813d29823ceb | -6.10344 | -57.86069 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06526b5c-81ee-3af1-874e-d02fd50d1ca7 | -6.76827 | -59.15284 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README68.md)
