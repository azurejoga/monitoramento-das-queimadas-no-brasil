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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a862c82-c449-3a10-8d06-c477be586702 | -11.33864 | -44.88344 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 2c6bcf25-a148-37e6-803f-936e4666ae28 | -11.16502 | -54.85803 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4077ae15-4645-3eb0-8391-d7ad34b3bb86 | -6.76192 | -35.19366 | 2025-10-08 04:17:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 10d2920c-84b1-39a2-a8b1-9bb05d68c560 | -12.32065 | -50.27294 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f96ab851-8f38-32c1-ad45-ce9fc163cde6 | -5.61314 | -43.94086 | 2025-10-08 04:17:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 265ab580-be0b-323d-bd7d-cb75dde21ef2 | -12.32626 | -50.26585 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 35a66f75-3552-35ad-b666-8a104dfb83d6 | -11.22647 | -47.75754 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4f7e620-884c-3adc-b5b7-b6421bf51af4 | -11.17664 | -54.89046 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ad9684fe-1d48-39e3-a6f6-c760084708d9 | -11.17668 | -54.89733 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 923b08e2-7cf9-302b-bb6a-f0461ab78ea3 | -4.30936 | -48.08517 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2e3a418-1470-3b36-aed9-296ddd8b9743 | -11.16837 | -54.87778 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e7ee098-f4c7-3831-9b36-fa944939f06e | -7.78276 | -42.40839 | 2025-10-08 04:17:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 806fa7b0-9649-3c82-98f5-6cf560e04494 | -7.7279 | -42.4071 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4b58ba75-38f6-3207-95d4-4bf7b48e6d78 | -5.31653 | -45.26022 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61550278-11e0-3ab1-9520-0ccb8575276c | -10.65397 | -48.98286 | 2025-10-08 04:17:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed5f7c1f-88c2-3452-b5bb-8108e32aa6bf | -11.84922 | -44.91249 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd0687f0-f319-3cfb-ac9d-30e2a085bb60 | -6.98115 | -45.19038 | 2025-10-08 04:17:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3f89321-b932-3e55-ae42-396b1e55d6cc | -6.74323 | -34.96559 | 2025-10-08 04:17:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 436bf960-824f-35ce-9e97-a13b7ecaac82 | -12.94058 | -46.86327 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 86b7a69d-889e-34a4-8cc9-ab516a7ef114 | -12.42723 | -45.6236 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5cb5b694-bffe-3755-8d59-874b7197d572 | -9.77598 | -48.28825 | 2025-10-08 04:17:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f76c16f8-c291-3d3b-93d9-f81500b04db5 | -11.22571 | -47.76201 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39b61ed6-3aeb-3548-b5ed-7be683a475d0 | -3.86987 | -41.5463 | 2025-10-08 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| abb10471-cfb9-3aec-b808-790d09539d4f | -7.28099 | -41.97916 | 2025-10-08 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fb9f530f-65b9-318e-9346-2277e7df98ae | -11.21609 | -47.77401 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 937b7638-3740-3475-b918-6ea608ba52db | -12.34871 | -50.28638 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 511dadd6-16a6-34c9-b177-b14f27db8130 | -3.56785 | -44.46263 | 2025-10-08 04:17:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e84d44fa-32f1-3193-8c68-259c033fced4 | -11.17256 | -54.88737 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f64a38ea-6765-343b-bf04-70dcf3675a69 | -5.97485 | -45.49401 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ebc9844-af61-32e7-8270-e113b05d19c7 | -12.23758 | -47.87269 | 2025-10-08 04:17:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d18b34-51e5-38ef-b6bc-37f23ffd5ac9 | -2.88655 | -50.7357 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d877413-9d6a-3b3a-93e3-d432f5ffeb33 | -13.07005 | -48.01416 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd1a033a-7496-31d7-966a-2e2ca63f0c11 | -5.25334 | -44.13995 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| df31f63f-a1aa-395b-90d1-0aba0f0825c0 | -2.29461 | -47.99471 | 2025-10-08 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8e44dc4-7606-3952-9966-d55697db8dc4 | -7.69802 | -42.39194 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f94fa43c-0742-378d-acff-ee8067dd5491 | -7.68292 | -42.40047 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89a85f37-cf9a-31b1-b793-b5d9def109b4 | -11.87723 | -44.9421 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a1db52d-1e2a-315b-af4c-ed155e2eec5f | -6.72309 | -43.72512 | 2025-10-08 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d6e869b-1ec2-31dc-ae7e-328c3a492e3d | -10.84192 | -47.55861 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a143f044-9a62-3574-8a56-f5014f46277a | -7.78697 | -42.62323 | 2025-10-08 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 400734cd-5f6a-3a21-8f15-fdeef213ebe4 | -11.81313 | -49.51711 | 2025-10-08 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc3e977-fa87-3dd6-8710-0a151911d154 | -11.16917 | -54.87364 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b6c76e1-a485-325c-8f5d-54e0b257b3e6 | -5.39688 | -40.9909 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b723be69-1b20-306a-a56d-0d26fe867288 | -10.35006 | -50.25256 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b905cfdb-09c4-35f4-86ab-3238c8527f2c | -7.72735 | -42.41066 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e128de7-0e0f-3eb7-bf34-ea00bd608c75 | -11.45203 | -50.21461 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4c99f1b-b6aa-3d16-8c6a-1a086596c4b5 | -5.4678 | -42.20829 | 2025-10-08 04:17:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5244c1e7-5dfe-30ea-96f8-2457bc7dec1b | -12.92208 | -46.8242 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b03217fc-f710-3f23-a6e5-e12f4eeafb04 | -11.11073 | -54.04491 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c946b755-5ac6-3ce4-b557-e86b77d26647 | -11.16914 | -54.89782 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bb0bfd3-90ec-37e5-8b07-b36f3c3ace82 | -7.67846 | -42.40703 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c00cd5f6-6a85-31fb-8996-550dfb9b7c00 | -11.81792 | -45.12988 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28c458ea-22f1-3275-9e91-e3df2ab38cf6 | -11.17338 | -54.87653 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4cb1af7e-f84a-3d62-94a0-ae8736fc4aa8 | -13.06026 | -47.93909 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8f3b503-cbfa-3b16-b587-95babc7da5a6 | -5.03861 | -43.61247 | 2025-10-08 04:17:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| abbe6aa0-79e6-38a3-9cc8-06326c9c225a | -9.63651 | -55.13459 | 2025-10-08 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5decd45-10a1-3617-a41d-e787e35f7bf6 | -5.59011 | -45.84208 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab4d20ac-df71-343a-9bd7-1492d3fbcab1 | -5.73315 | -43.61065 | 2025-10-08 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cee8bd0d-a63d-3d6c-810b-56fef1c867e5 | -11.77104 | -45.14405 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35505a80-7e14-3483-98d2-50bb8e952f7c | -5.74213 | -44.40413 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dd800ce-2e57-3707-9892-19862f7d1654 | -7.72112 | -42.38413 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 14a5fc67-3a98-35a6-bf20-5d8de153f6be | -10.38491 | -50.23296 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0bc11f94-b57a-35ba-b12f-226736d9ae42 | -3.07228 | -51.2043 | 2025-10-08 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecc1bfbf-9472-3ef3-994d-c8b6f5f85581 | -3.44347 | -45.59611 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3ff73ca-9d34-3805-a2e9-5f5fe77df353 | -4.42313 | -47.75612 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fad8178e-7425-313e-bb56-f6d9dc884ba8 | -11.76885 | -45.13632 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 926d85f5-82d9-3e8a-8a21-916a66147a32 | -13.03848 | -47.89158 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47afd955-7969-31a3-8396-d230cfaef7f1 | -11.73978 | -50.94339 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a55fc219-9380-3cf0-8cb3-823111c38077 | -3.83474 | -50.96812 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8f6d1718-118c-3084-9223-ce03412800f0 | -12.16543 | -50.98351 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cefcda9e-4cdd-31fa-a1e9-557fcb674c59 | -5.05006 | -45.18873 | 2025-10-08 04:17:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76749bbf-c726-389c-a762-d96a429f089e | -11.85476 | -44.92063 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0eeed8f-ef36-3594-9401-cd77f1d4229c | -11.51671 | -51.49283 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0160824-f218-3b97-8e79-0450e8819241 | -9.9796 | -48.78491 | 2025-10-08 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cec3a0c3-993f-34de-98b5-982f8fddf655 | -3.44709 | -45.59669 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 063280b3-34af-3e20-98f9-267037dce75c | -13.37077 | -47.55763 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cb19b99-c433-375c-aafb-550ba0c32b9f | -7.29226 | -41.97351 | 2025-10-08 04:17:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 084d1636-b64a-3874-895e-8d496184e452 | -11.78202 | -45.05434 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c44c0f3-b907-325c-8f1a-e38873eb6f08 | -5.16167 | -46.92123 | 2025-10-08 04:17:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32248432-2d1a-3f20-a563-73e2f77f0a5e | -4.50034 | -46.36341 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cf5eafe-efe9-3396-ba5b-4427fc6dd372 | -3.12119 | -48.78383 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00b9774a-9c08-3e01-bad6-e514fd100d9c | -12.53353 | -42.34458 | 2025-10-08 04:17:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 453e28d6-0874-38cb-8544-a79d565983bb | -13.28183 | -47.56396 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43a9f0e5-c6bc-3a2c-85fd-420f88421952 | -13.25615 | -46.47247 | 2025-10-08 04:17:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4dc8bd3-3f59-3a20-a1bb-a1e262f23f1a | -11.16095 | -54.88501 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1d78f4f7-e768-3e77-a1a5-3a0c2eaf67da | -4.04885 | -42.51674 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5a32a35-6ec5-3b2c-b9b6-1768e6e354cd | -11.15327 | -54.86234 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90629862-e46d-3931-a6ce-37a1be4bfef0 | -11.68291 | -50.96629 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 209ce843-3423-3e9a-afb2-b34f49f85172 | -11.70079 | -46.34719 | 2025-10-08 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8357a8d2-8f0e-3432-a863-a8b800c49ec6 | -5.53122 | -46.55138 | 2025-10-08 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc9d004-0d3f-39a9-b77f-23e309c6afa9 | -13.22965 | -47.16896 | 2025-10-08 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a06ee261-a9bb-3422-9fee-869e1785a253 | -7.58361 | -44.03496 | 2025-10-08 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 497c05eb-ef9b-3fe6-bd74-01017b678895 | -5.73494 | -45.25911 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7af2a08-eb9e-3fc3-982b-f4d7cde1b24b | -11.18758 | -49.78021 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a796ada9-91ed-3653-8fed-113d603b1c17 | -7.0012 | -42.88136 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 77ed84c0-a7e7-3bbb-a56d-9614ddcbfdf1 | -4.43882 | -48.00678 | 2025-10-08 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c97f0162-d6b5-3540-b7c6-b2264d6a28ad | -13.27435 | -48.043 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3429cffd-76ea-3a01-8106-217257079d45 | -11.18 | -54.87361 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae15eeab-3422-3775-b151-1193be4483e3 | -11.78503 | -38.42926 | 2025-10-08 04:17:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 276f8849-839d-3a30-9501-25e28462689c | -7.44311 | -43.15104 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README37.md)
