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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 717e9902-45f5-3f0b-a0aa-7d135a15ce3e | -10.21661 | -53.87619 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b6b6ad-5147-3889-a7ee-b221e248f888 | -7.29802 | -45.2698 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ac35c67-56a4-3e92-b456-2716e5d54e9a | -5.81412 | -43.81774 | 2025-10-03 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4639cf1d-0912-37d1-94cc-5bb6110a0c8a | -7.7559 | -42.55412 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c2d23fc1-8b4f-3b9f-8ca4-779d6c33d093 | -6.99629 | -47.20634 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ed2e314-62d4-3c80-8292-19506d3a9f0d | -7.75721 | -42.58894 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1507af1b-df45-30f5-9c4f-a78294dd3d6f | -10.86405 | -47.04113 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| face0ff8-b3b4-36b0-bafa-c5232e07c30c | -6.87376 | -44.51623 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6704788d-b75e-31db-a054-620b8ef6f92a | -10.12291 | -52.35048 | 2025-10-03 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cba3f70-c8ac-39e4-9b9b-825c2c0c514f | -11.808 | -45.02977 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8739ee3-7d1e-332d-b7d1-9443584b4791 | -7.55406 | -42.40121 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25d1db34-18ad-38b1-a98e-a637b07fbf97 | -11.90566 | -46.74353 | 2025-10-03 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 381fae56-6344-38b3-b944-dab73d22cf6c | -11.91772 | -46.26658 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b41f7a4-2bfe-3687-af8b-3fc74d28ed41 | -7.55881 | -42.39801 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e01937c1-cea4-3cc6-aaa8-55edc00c13d3 | -11.3132 | -47.84282 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 587000fb-5d88-391f-bc9e-64bdeeb0e7e4 | -7.75306 | -42.57317 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3d29bcc7-f57f-323b-bd7b-630e1c3400a3 | -7.55825 | -42.40179 | 2025-10-03 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 03f65cc0-788e-3339-96e4-b70e67100cd2 | -11.83137 | -45.03065 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3b826c4-9242-35d5-93fb-96991978b01c | -8.33569 | -46.22377 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a03e47ee-c4e3-31a1-94d7-534983bbe5bf | -5.85155 | -43.36596 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48831591-0e70-3096-9932-c1aa3f2db283 | -8.73225 | -47.35204 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ff2f29f-2963-3600-b12d-c310ef72d4ab | -5.62934 | -43.89602 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8913ba5a-f4ae-3cda-97dc-87936dae9723 | -12.12147 | -43.44122 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afb13e01-83ed-3655-9ca9-cfb48bb15f80 | -11.94425 | -47.05048 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b317eccf-180d-3aad-9fe9-26415960ecec | -10.60637 | -48.71948 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 083c9e77-ac0c-3b9f-b05a-9105db36ee80 | -6.7069 | -42.81675 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2c940fc-6358-3f28-92fd-668bb33948ca | -8.99844 | -47.47307 | 2025-10-03 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2ee725f-28eb-315c-88be-617f49e18cac | -11.83646 | -44.94025 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09ee3790-783b-30bf-b0f2-22eb96e6f646 | -8.7328 | -47.3485 | 2025-10-03 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a180f08f-43d0-39c8-bee4-5c3fccc78117 | -10.85215 | -47.21607 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c4afeef-a168-3af6-9284-1125701c61ca | -12.11206 | -43.44782 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fadf314c-5167-383b-92c2-64e0b15bdfae | -12.12082 | -43.44588 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f4a2f387-8472-3f6f-8e12-ecadb6f0a23a | -5.78476 | -51.74136 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b1dcc45-4b8a-3c8d-a8c6-ac75a11b67b7 | -8.62166 | -54.98649 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6fe1f06-75b1-3868-a3d7-4a3eda449e7c | -5.63408 | -43.91506 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 170619de-2dab-325c-93fb-9f334559aa9d | -6.2786 | -44.05156 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ab1b64c-07fe-3b46-94b4-ce04619f5641 | -7.75685 | -46.23191 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bf05ad84-b903-30ff-9293-004567c852b0 | -5.63846 | -43.91114 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 018afba3-dfb5-36f6-89a9-2f087acef8d2 | -11.18291 | -47.7457 | 2025-10-03 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b2a943a-c869-336e-a17d-a9b0a5c5e000 | -6.23333 | -45.34808 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 05e48330-75fc-3ce9-9443-7fc94d6ba679 | -7.74988 | -44.79966 | 2025-10-03 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad8c124c-cff7-39b9-8955-67ba7596f66c | -8.46116 | -50.07642 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb58ec0e-a50e-3af4-9e0f-18cf39154a10 | -8.19692 | -46.80237 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76e0b9fc-11b6-328b-bdf5-65efe5e5018c | -8.62695 | -54.98285 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc5e804-0b15-363a-a6ba-818634ccdd35 | -6.2397 | -45.35297 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53f7c8ce-d85b-316c-8485-52019b5be122 | -7.64782 | -45.4445 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f535e54e-09f2-3812-b2df-26e741ca60bc | -8.76272 | -49.92451 | 2025-10-03 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbe74e84-a3c4-34e0-bec7-6ca1bbd4f002 | -4.57306 | -46.5033 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f79397b3-018b-317a-b801-c0bfaa9ac6d8 | -8.62774 | -54.97833 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 255575e5-029f-3a98-bc80-9bd44eada35e | -11.10068 | -47.83506 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65fa9f92-67a6-3ff5-817d-f7ca970f8b3c | -9.65703 | -48.2129 | 2025-10-03 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65b36cf8-158f-3492-95b9-90637586b84f | -11.74757 | -46.82363 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58bcbe9d-a50d-3b6e-821c-a83dbaa616e2 | -11.04796 | -47.80484 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51ecfbec-61df-307f-995f-aa56adaa23ff | -10.89777 | -46.70531 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a40a3d7d-08de-3e84-a168-1efa5b4296fa | -5.82773 | -53.66528 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a95b01f6-7a96-3830-b072-9eb24900f0ae | -10.97274 | -51.08915 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f685857-0570-3a70-8398-60dd5f6621f0 | -9.92199 | -43.76399 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3c3f4826-957b-3713-8aa3-5d1c3baa533d | -10.36209 | -51.19028 | 2025-10-03 04:32:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2528bfbf-61be-39d8-9103-5a34375cbd7d | -7.73323 | -46.225 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99b83ca8-90e3-3aaf-a0c0-51e5c1084b7c | -5.40102 | -41.33963 | 2025-10-03 04:32:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8af5694d-e32c-32ea-9150-d9df608bc4ea | -8.6151 | -54.97122 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8daef3a-d748-34a2-962b-f59aab102743 | -10.01155 | -50.22789 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6c923b9e-812d-31f3-932c-dd0ff701cd64 | -11.94082 | -47.04995 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ddf12b3-2a6b-31e0-b5df-155bdaca0137 | -7.77271 | -47.38865 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eac91263-6b6e-3443-818f-16dcf7857590 | -9.48834 | -45.91544 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ba61e6b-3bf0-35dc-8b76-53ac9724664f | -6.38842 | -43.60338 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c124d91-b3ec-38f3-9fdf-1d3e9d13e89c | -5.24958 | -42.97054 | 2025-10-03 04:32:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 28b1f059-6934-35ae-b321-408b74763ff2 | -11.12011 | -43.3941 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4abf3058-c038-3bcc-a1c4-2c0775e67678 | -5.47387 | -44.69218 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d42c130-e334-3b76-88e7-ad66d3fd250a | -9.95322 | -43.71632 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f94c4150-3603-356c-8f9b-c4ab461d7c14 | -11.11632 | -47.86671 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| daae2917-2493-31e9-968a-b999043a238e | -7.87744 | -47.32617 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 735c9411-2b14-3c4a-9f14-2cb846ad5567 | -10.86969 | -46.68156 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aaa795e3-03fc-318f-ad09-07b7cf8060ef | -3.8954 | -54.12522 | 2025-10-03 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03fcea5a-619e-3896-999a-22ca03b581d6 | -11.91472 | -46.28687 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81e47408-e746-3ed3-9467-ac7d0d19817f | -10.83363 | -41.27249 | 2025-10-03 04:32:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0b6c9a2f-e5b3-3925-b6b2-eadaccefa1b7 | -11.80734 | -45.03427 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed157b14-aee8-3d5e-94e8-4444487bd1fe | -6.55459 | -44.15014 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d20366be-fbfd-38bc-879a-d039e8826d96 | -11.06857 | -47.80431 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a60287c8-e99e-370a-ab35-5775c3cd4c11 | -7.52189 | -50.49667 | 2025-10-03 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27ef9bb8-2afb-37ef-a51b-78ed3e6cba84 | -11.08584 | -47.80331 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2a70034-2a4c-3cc1-b021-c32d0bd59ac1 | -8.83263 | -44.80702 | 2025-10-03 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d0408a8b-d5b4-3276-932b-8509a6641980 | -11.11462 | -47.85555 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3f9ba2a-4be9-3070-8017-8585928768b7 | -7.75855 | -46.26666 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 25b4a87e-ee4c-3402-8e8e-860b6fe3d39c | -10.29835 | -47.93411 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d2c968a-a085-3c02-8650-2fef6d10d824 | -9.09732 | -46.71696 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d3ff2e3-1602-39d8-ad52-1ac17d1fbb38 | -11.12427 | -43.39443 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15bc1dec-64b2-3692-9f31-28e815b48cb5 | -9.02566 | -46.67949 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4369bc0-a875-3631-91c0-4dee63dea86b | -11.83113 | -45.02913 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddaf8011-23ce-30c6-9313-6cd80cb1bb3f | -7.79963 | -42.52938 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e6a01296-ff9d-3247-817c-e2f4059e36af | -10.29448 | -47.93711 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19c8c368-cd4f-3623-8f36-cd77d94d6428 | -9.38231 | -45.85137 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd9708bb-5913-3090-ba43-c7d058d1591b | -7.74337 | -46.24959 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16e28de6-f45e-3774-ba6e-169750b3fd32 | -11.821 | -44.91381 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5f19ff-ea50-3311-9756-3da59abf262c | -7.88799 | -47.3458 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 087d0e2d-460d-33f6-8c69-537ac022a0ce | -5.93947 | -42.88633 | 2025-10-03 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6aae2fd9-5cd7-3acc-a114-f5d6feeb2763 | -10.85391 | -47.25016 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e500e0f3-18ff-369b-ba12-4de7d0a92abc | -11.18553 | -47.25604 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ee50cda-b0f6-36cb-93f8-4be79ed5a11b | -5.73878 | -44.26113 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1cbc00e-43d3-3dcd-8b60-f6dffbb58fba | -11.48924 | -44.98959 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README101.md)
