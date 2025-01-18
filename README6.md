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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b103b0fb-b8cb-346f-8c3b-391e545b07dd | 3.61594 | -60.10596 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fe5d86a-143a-33eb-99ce-be801e5f175e | 4.42883 | -59.9352 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9c720cd9-97d0-33fb-85ac-f2394d6222c4 | 2.94251 | -60.16293 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0ff1b1c3-6907-32f2-afdb-97fdb6ced74a | 4.3626 | -60.82087 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2454adf9-e260-320f-b800-b501a4c82d41 | 4.52811 | -60.68808 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 615fdae1-7b2a-3836-a856-ca4f9f5b1d24 | 3.61683 | -60.11126 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9acee292-29c5-38ed-ad37-b5e2bbdb1f0c | 4.36183 | -60.81633 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d00cd4e6-96a9-395c-a6fe-04595635d256 | 2.19584 | -61.81887 | 2025-01-18 05:59:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2189548-b669-32c0-92c5-aa90f8c3a4e8 | 3.27799 | -59.96702 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 530be9bb-e6c2-31e0-8460-c99ccd97977e | 3.75103 | -59.71161 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82211edb-e288-3290-b383-5e9fcc9a418c | 3.28595 | -59.95438 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b9644be-da30-32c5-b658-930369bf03b8 | 2.17948 | -61.85671 | 2025-01-18 05:59:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84449721-e071-3149-9673-8edc3a8ad198 | 4.36139 | -60.82261 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d214942e-7bff-39d4-a4f0-7ce2e8328c9d | 1.87898 | -60.3624 | 2025-01-18 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 398a4885-9c17-3070-a7f8-4e32ed656a59 | 0.06538 | -60.65892 | 2025-01-18 06:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c33c19b0-b119-302f-ae6a-a99702d3330e | 0.07115 | -60.66363 | 2025-01-18 06:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5b79934-29cf-33c2-ac3f-a61ac47a9fa1 | 0.06624 | -60.66442 | 2025-01-18 06:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 011db15c-74b0-3ba5-9b0c-6ad785652736 | -0.35697 | -62.75417 | 2025-01-18 06:01:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fae689a-6a0c-3d4b-81cb-48882422f415 | -7.92902 | -61.55504 | 2025-01-18 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c26667e0-9288-3ebb-bec0-9312e2033f6e | -7.92994 | -61.55304 | 2025-01-18 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33d60633-2e4f-3d4b-812a-f7b3c79c742b | -7.66738 | -72.34783 | 2025-01-18 06:01:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62623de1-f9db-39ec-99c1-d47fe7d1708c | -7.92952 | -61.55626 | 2025-01-18 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51e0c044-8fd9-3b11-86ef-79637fc3b883 | 2.37134 | -61.26021 | 2025-01-18 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49f5bdd4-74e5-32cf-befc-aa5e4050ef8e | 4.91685 | -60.293 | 2025-01-18 06:24:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55b7d4e7-faba-33e5-900e-8ec59eb170e7 | 4.36512 | -60.82087 | 2025-01-18 06:24:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4fb7ba83-37de-394c-a5cc-e444f3498865 | 4.81331 | -60.63374 | 2025-01-18 06:24:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 675ab4af-97ac-393b-9e16-1daa325ebeaf | 4.3711 | -60.81425 | 2025-01-18 06:24:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7188745e-26bb-3af0-9b9f-213c146a73f9 | 4.91359 | -60.2921 | 2025-01-18 06:24:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f110f5c-1248-3ad1-a488-5b3983dc519f | 2.37828 | -61.25887 | 2025-01-18 06:24:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe67453-51eb-3f06-963d-6a60f198f9c6 | 4.36623 | -60.82712 | 2025-01-18 06:24:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 54de7d5b-ea68-395a-97cc-0576527f6dd1 | 4.80628 | -60.63459 | 2025-01-18 06:24:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10e86b9d-4d46-34a0-9ed7-03e3b153047e | 4.91782 | -60.29817 | 2025-01-18 06:24:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19c6ee42-6712-3573-96da-f5214d847e35 | 4.36401 | -60.81467 | 2025-01-18 06:24:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 196cf926-2099-37af-9e92-3f3abcf060af | 4.37221 | -60.82055 | 2025-01-18 06:24:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 056954e2-c352-3aa4-aac3-85224d0445a0 | 4.91449 | -60.29705 | 2025-01-18 06:24:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ef1dccad-df6a-3aa3-9ecc-d165b8fcf007 | -17.37 | -44.92 | 2025-01-18 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 800c2e7a-4fe6-30cd-9ce7-0c313856936e | -15.73 | -45.95 | 2025-01-18 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca39b8b8-3ccf-3f07-bc7d-5007e3e754d9 | -15.83 | -43.46 | 2025-01-18 12:00:00 | MSG-03 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 511ffc05-32e2-3120-955d-3215e1414410 | -15.73 | -45.9 | 2025-01-18 12:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6826711e-854a-33a8-8cbb-1b6fa47ff6a0 | -9.42929 | -37.36567 | 2025-01-18 12:01:00 | TERRA_M-T | SENADOR RUI PALMEIRA | ALAGOAS | Brasil | 2708956 | 27 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b011243f-da1b-3d7a-b3f3-f7c99e0edd20 | -6.23628 | -35.49525 | 2025-01-18 12:01:00 | TERRA_M-T | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a1976605-65ae-3669-b208-a5780b0d37a3 | -6.20173 | -35.50557 | 2025-01-18 12:01:00 | TERRA_M-T | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 49.7 |
| 621c3c7e-9692-3cd2-9d42-b0e246f85777 | -7.94044 | -37.92335 | 2025-01-18 12:01:00 | TERRA_M-T | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3ccc4318-d734-35e5-8bdb-1ca7398e25ba | -6.20322 | -35.495 | 2025-01-18 12:01:00 | TERRA_M-T | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 58.6 |
| acc21d32-f5b3-3a44-8dfb-14c0be24269d | -7.90545 | -38.48083 | 2025-01-18 12:01:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 3e3232c4-7e23-3eb3-b445-c11562890a0e | -18.94844 | -40.13376 | 2025-01-18 12:04:00 | TERRA_M-T | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 5dcbcdd3-b7dd-3635-bfc7-0b8f88281831 | -11.28973 | -39.05631 | 2025-01-18 12:04:00 | TERRA_M-T | ARACI | BAHIA | Brasil | 2902104 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e70a2a24-2c37-3663-bbce-5c11879a7c17 | -21.69619 | -41.20878 | 2025-01-18 12:06:00 | TERRA_M-T | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 75786468-cf18-337b-9a63-4a057f40769b | 3.1094 | -60.765 | 2025-01-18 13:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 92757112-4fcd-32af-b627-055a5e017899 | 3.1094 | -60.765 | 2025-01-18 13:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 79f4f033-246e-346e-82cd-f66a7bfe52d0 | 3.1094 | -60.746 | 2025-01-18 13:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bb2a7959-2476-35fd-ab8c-c0379db9a952 | 3.1094 | -60.765 | 2025-01-18 13:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 189.2 |
| 86868831-3279-3789-b5d9-e7f275ee086c | 3.1094 | -60.746 | 2025-01-18 13:40:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 807f9a9b-9f5d-328b-b1b6-4e4e7b446283 | 3.1094 | -60.746 | 2025-01-18 13:50:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 90787cfd-a319-3044-ac57-723548f8363c | 3.2758 | -59.9637 | 2025-01-18 13:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d42589a6-eb03-329e-ae99-3d5249baad73 | 3.2758 | -59.9637 | 2025-01-18 14:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ba9d9472-7273-3e9b-87d9-81700eeaa1c4 | 3.2758 | -59.9637 | 2025-01-18 14:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 9dd2a7e2-881d-3ff9-ba56-2284d681bf16 | 4.1172 | -60.0033 | 2025-01-18 14:10:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d744ca82-c715-307f-bc4e-a6293f8e2770 | 3.2758 | -59.9637 | 2025-01-18 14:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 89b55a0a-fe41-33cd-8785-9b9aebf62938 | 3.2758 | -59.9637 | 2025-01-18 14:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |


