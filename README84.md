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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8db1c665-b93d-3662-ba03-882ec4dd0c34 | -10.8001 | -57.2007 | 2026-09-28 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 14dceb6e-6696-3959-839c-309753372726 | -12.2435 | -50.7914 | 2026-09-28 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 1fde2457-b42a-3bae-b4de-58941ee67bf7 | -12.0987 | -50.2943 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| ea7b2011-4c89-328f-a725-e11b9c725869 | -8.5982 | -54.6341 | 2026-09-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8cb28aee-66d0-382d-a6d6-62e8d0b6c070 | -11.497 | -47.3727 | 2026-09-28 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 21aa412e-ffcc-3b01-81fa-b36190e3fae4 | -11.5352 | -47.3678 | 2026-09-28 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 228f3e5d-d023-3a93-b2fd-3194a1ac08a0 | -10.6035 | -49.9913 | 2026-09-28 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.9 |
| c29e3edc-9f28-36dc-bd48-344f5e0f136f | -11.5821 | -50.4833 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e7b1725e-c3cf-3726-98b6-cac5e26640f6 | -11.9399 | -50.7201 | 2026-09-28 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| e46bd04d-cb03-3a9b-9bdd-68e1ff390f4d | -10.9538 | -50.6592 | 2026-09-28 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 4d131842-cb3a-3389-bdce-51f65d1882a5 | -12.6878 | -45.0192 | 2026-09-28 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| ed689681-de6d-3ebb-a0f5-cce2dfcfee8b | -9.997 | -50.1607 | 2026-09-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 0fffc765-c57e-32b7-a2cf-e632530d47ed | -10.7064 | -44.4317 | 2026-09-28 15:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 557e347b-e1d8-311f-95e9-3ecd44293cdf | -10.8189 | -57.1993 | 2026-09-28 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 0931775a-5ef0-387c-afce-a238c19c02a1 | -7.6852 | -54.7532 | 2026-09-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b834096c-d0a8-3747-8c93-c8f8aaa1e4a7 | -11.5815 | -50.5261 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 552c0316-918f-3057-9bf2-e5b27681e5dc | -10.8967 | -50.6866 | 2026-09-28 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| d44d7744-0d97-348a-8cdb-bc046e7171ae | -12.7417 | -47.2909 | 2026-09-28 15:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 588cf964-e1b9-3b35-88f5-8d8dd3b29669 | -11.7126 | -50.6608 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| dffa3632-99ef-31b7-94a6-ed300708f1e2 | -12.6643 | -47.3245 | 2026-09-28 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| be8174a9-b022-3e2c-8fb7-30b3a3fb7c36 | -9.9967 | -50.1821 | 2026-09-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f489c8f8-d453-32d0-94e2-dea6850c8009 | -10.2565 | -50.5185 | 2026-09-28 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| bb549336-0a25-39e5-a54c-ad14726dbf80 | -13.4676 | -48.6102 | 2026-09-28 15:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| db60890c-b815-30f6-81d8-12bc204838a1 | -13.468 | -48.5881 | 2026-09-28 15:10:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| aa191790-c5cb-3bc7-80f3-c693100a0f56 | -11.2118 | -54.0797 | 2026-09-28 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 87b534be-ac8a-3dc4-af96-d80aa77a5d04 | -12.3088 | -50.2688 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c6dfdcc6-3d36-3b77-b067-471f97233b9d | -12.2445 | -50.7271 | 2026-09-28 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 41020528-e104-33e1-b41d-09dead7bf373 | -10.7677 | -60.7279 | 2026-09-28 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 28dc700c-f833-3a4c-bde1-cd86e463043b | -10.9861 | -49.7131 | 2026-09-28 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| c1e11e3f-e321-3d53-bb7b-655033f24a2e | -11.0241 | -49.7088 | 2026-09-28 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 7e6568d8-9a78-3e31-80f0-aca998823c62 | -20.1966 | -48.5773 | 2026-09-28 15:10:00 | GOES-19 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 8c199f4f-90e1-3ebc-97b3-4e5e0f922dcb | -10.2446 | -49.986 | 2026-09-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f5900c63-7890-3c0e-b0a8-f666b658b543 | -15.0984 | -54.7189 | 2026-09-28 15:10:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 750df754-18ef-3f91-9d65-f1af30b2f828 | -12.2119 | -50.3666 | 2026-09-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 0097b03a-fd8a-3f4e-947a-3a8a423a9f06 | -11.9586 | -50.7393 | 2026-09-28 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 6334029c-6138-37e3-982d-a485894fd06b | -11.1966 | -44.7805 | 2026-09-28 15:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 674.0 |
| b8546ce0-22b7-32a3-810f-8fb3e4f79451 | -9.7874 | -44.8289 | 2026-09-28 15:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 68333244-1204-36f8-bda9-476e327adce5 | -10.8106 | -48.7355 | 2026-09-28 15:10:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| debf714c-bda7-3ede-9c83-e03f9794d7fb | -8.3608 | -45.4695 | 2026-09-28 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| cd305def-d29d-3638-8053-6fffb008c8c2 | -11.5161 | -47.3703 | 2026-09-28 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e3a82829-ae6c-37d8-8f42-2ca666d070bc | -10.6928 | -60.7322 | 2026-09-28 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 64aacb96-56b2-3049-b484-938725f7b59b | -11.1904 | -51.3555 | 2026-09-28 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 2aa0d5ee-d044-3913-9ba8-defc74de49d7 | -9.52 | -46.37 | 2026-09-28 15:15:00 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06d38133-34e8-32b2-8de5-d2204e9b916d | -11.15 | -50.08 | 2026-09-28 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70e5c765-602d-37c9-91c0-7247c669fe99 | -11.19 | -44.85 | 2026-09-28 15:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80836040-f32e-387f-8332-592e05601f27 | -11.15 | -50.03 | 2026-09-28 15:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e9e0567-73fe-359c-ab9a-7c609aa49f2c | -10.98 | -50.69 | 2026-09-28 15:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f968a7bb-12d6-322a-af58-b3d70cb647f4 | 2.1266 | -50.8788 | 2026-09-28 15:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 95f80a7b-2383-3e84-9ea2-c105e3e048fc | -15.3998 | -47.9261 | 2026-09-28 15:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 58413a6f-e001-387d-94fe-13a2cd3094a9 | -12.3283 | -50.2449 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 0139c2c5-82a6-3334-a575-44ebcbed4037 | -11.7357 | -54.5227 | 2026-09-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1ba37cfe-f52f-31e3-8de3-c67167eeac67 | -11.7135 | -50.5966 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0b05548f-688e-3fc4-994e-c95d143fcccc | -9.1337 | -49.9656 | 2026-09-28 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 4c211abf-ac32-328e-929d-33e656b24399 | -1.2455 | -49.062 | 2026-09-28 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f80545a9-d732-31d8-b456-dd5e995a4662 | -12.1075 | -45.2248 | 2026-09-28 15:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 181.7 |
| aee9cfb2-43b7-3843-b284-d3cdced8733d | -12.6836 | -47.3217 | 2026-09-28 15:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 61edd45d-3d06-3fe8-8a00-e09136f7da9b | -11.7122 | -50.6822 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 20528514-d4d8-32a9-a1b7-a39b2a1288d8 | -12.288 | -50.3789 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b00d2685-b067-3ff4-a337-85ca54e261e5 | -12.2498 | -50.3835 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 7744b429-a807-3450-9f77-88b89e5b9e40 | -9.9976 | -50.1179 | 2026-09-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 1bd34b18-51a1-327c-a20e-788f9ea167af | -12.2639 | -50.7034 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 84545025-a9f7-3d3e-b50b-d722e8baa28a | -7.5057 | -44.5733 | 2026-09-28 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| a7fac01d-79c0-32bc-a566-b7f4f8fcd507 | -10.9154 | -50.7059 | 2026-09-28 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 5dd53c34-b7b0-38ca-9b0c-2acb1ff6d844 | -9.1057 | -60.9511 | 2026-09-28 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| aad161f4-0018-3fb4-b5fd-5f757dad9fb8 | -12.8513 | -50.9957 | 2026-09-28 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f40704c9-5757-313f-8306-fe0d2169a49a | -12.7674 | -54.0502 | 2026-09-28 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 75df49bc-8ade-3bb1-86b5-7cfe745278e9 | -11.7828 | -51.0578 | 2026-09-28 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 6c6424b6-eb13-3a0e-a4ff-104912f16107 | -13.4325 | -57.061 | 2026-09-28 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 67577a85-0627-3668-8683-0ad0f0383fb9 | -11.2853 | -51.3454 | 2026-09-28 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 8155be0a-19bc-3ff2-8cfa-b5a40513ba97 | -12.3088 | -50.2688 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 1178fca7-b29e-343b-a237-6450fe2a5af1 | -12.2689 | -50.3812 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 3eb838fe-227e-3ffb-ae19-ed08f6bdf16b | -9.1771 | -61.3882 | 2026-09-28 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d00408a0-3ad4-36b6-ad4e-4c0aa346ad84 | -13.3436 | -51.3401 | 2026-09-28 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 18830a6e-2bc2-3ff8-b1e2-fb864a46154d | -12.2508 | -50.3189 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f81bccce-99e1-38d3-8d69-b86b52974bf4 | -13.7142 | -48.8172 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f9123b70-e153-3929-a106-42b378a3fa11 | 1.6201 | -55.8641 | 2026-09-28 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| fd73d087-77e7-3a0d-91b2-4bc6cb970445 | -10.1713 | -63.0571 | 2026-09-28 15:20:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6f037b39-712d-3c6e-b258-bf7d710e7272 | -12.2897 | -50.2712 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 377d8018-2816-3ec6-8188-4218cc826172 | -11.5161 | -47.3703 | 2026-09-28 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 90799ed8-3e39-3b1a-b9e9-b678694164a6 | -10.8191 | -57.1795 | 2026-09-28 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5572d5a4-3272-39d7-a02c-5cdfc1c64bb5 | -10.6035 | -49.9913 | 2026-09-28 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 40edd100-971b-3263-b7a6-8ac2cb822342 | -10.6928 | -60.7322 | 2026-09-28 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 082796dc-2770-3abd-8c2f-cd77360f6dc4 | -12.6878 | -45.0192 | 2026-09-28 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 6e886ac4-603d-38a9-979f-5b3962ce1ba0 | -7.6852 | -54.7532 | 2026-09-28 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 2da12aeb-647b-30b6-81b5-eb4bfd5dbaf3 | -11.5628 | -50.5069 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| baa6f445-2234-335b-b69e-f1521d539823 | -12.9112 | -52.0508 | 2026-09-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5c12972c-ce3c-3eef-afe0-148b9baa4a39 | -8.2862 | -45.409 | 2026-09-28 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9b2306cb-d967-3db6-b610-be095f462086 | -8.3608 | -45.4695 | 2026-09-28 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 88684c77-e2c1-3595-850f-5f2d42066267 | -10.7115 | -60.7312 | 2026-09-28 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 0e12220a-6b1e-3ae8-9123-e8f050d6ac30 | -12.2696 | -50.3381 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 143e359c-2529-3aed-96f4-3cf49efdec19 | -11.9596 | -50.6751 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 78f6473c-9845-3748-964c-7afeb0637381 | -1.3008 | -49.0613 | 2026-09-28 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| def09686-bfc2-3dfc-b50b-40658bc1395c | 1.5835 | -55.8251 | 2026-09-28 15:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 50db8daa-f7e4-322e-93c7-65ebc6141ec4 | -10.9349 | -50.6612 | 2026-09-28 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 17b4f79d-693d-31d4-9b32-af687cdb30a1 | -11.7325 | -50.5944 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 39cb93d2-7858-3f14-8af3-a4c29b5fcb89 | -11.5818 | -50.5047 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| e51974e4-0f65-3617-978d-f8a689ae8497 | -13.161 | -48.5437 | 2026-09-28 15:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 11f95608-6c6d-3f41-be13-c3eae32b46d6 | -10.8187 | -57.2192 | 2026-09-28 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 2d79b0af-3f58-3c29-b092-637804308b95 | -13.468 | -48.5881 | 2026-09-28 15:20:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| edae9b96-851b-3378-9f9e-8ae4682417b8 | -12.2244 | -50.7936 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |


[Clique aqui para ver as próximas entradas](README85.md)
