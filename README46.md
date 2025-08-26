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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5718f565-74ea-3c19-92f9-eb221cbb9ced | -13.5879 | -48.19032 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30cb9c1c-d874-3f8a-9fb1-e8493be14885 | -14.97067 | -52.87854 | 2025-08-26 04:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a6dc465-c907-3913-b6da-c313186e33ec | -14.35925 | -51.91921 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cf8e6ba6-cfb2-3eec-a320-55087d1751a3 | -11.54051 | -52.12147 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 901d7919-e995-3336-b2f1-246096c99832 | -13.16763 | -45.29552 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34eb72ad-e9fb-37c2-956a-4da0d41a9596 | -11.51041 | -52.13988 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1c58085f-af1f-383f-92fc-b7921e5296c7 | -12.72611 | -48.16043 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99c7f6be-2783-3f67-ae32-1c6ae3b44f15 | -12.76325 | -48.1385 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b540a8de-c3dd-3cc4-a18e-ee15083ca33b | -13.42288 | -46.93195 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6f8a8ba-0b44-31ba-b47a-80ea78e07cf7 | -13.44579 | -47.02414 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55cb5779-c39d-381f-845e-46cc22d94068 | -10.54483 | -57.95803 | 2025-08-26 04:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58447609-c086-3362-a034-7360e5e90e56 | -12.93473 | -46.32882 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48d3da93-f7a7-3e27-b22d-5166ec1b8445 | -11.55318 | -52.10172 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0df03d28-0e2a-3d7e-908c-4666f91b119d | -9.63632 | -59.63716 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6c23331-2238-3d81-8b63-a7f9fb689ff2 | -11.54568 | -52.11799 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da8cfbf6-9338-3417-80bf-b91043ccf821 | -13.41129 | -46.91876 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44f49bcc-df50-3a96-9122-66ab10d39580 | -11.31115 | -55.11007 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cfe8a2c9-f6ca-3274-844d-e6cddffca24a | -15.88331 | -48.15155 | 2025-08-26 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca01eabc-35bc-3cf1-9a00-25d3c5e75589 | -9.16125 | -59.54192 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 990b44e5-c416-36fb-b7d8-2a9e3cca6d34 | -13.60041 | -48.20025 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c020520-afa4-3165-9bda-527b6267fea8 | -9.18523 | -59.53674 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1b7f3164-5ff2-3f97-9123-c7a26ea26668 | -12.76456 | -48.13072 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff04088-e40d-3fa0-9bf2-e5a2bd8ef55f | -17.75197 | -41.51556 | 2025-08-26 04:23:00 | NPP-375D | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5a136169-431c-3182-ad8e-0b72a2d9393a | -14.1182 | -53.98422 | 2025-08-26 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8cb3d7e7-8f2a-3b74-b5d8-a4c636a465a0 | -9.15838 | -59.51824 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e2c463c-3784-307b-8d7e-661857e98962 | -15.64908 | -52.73492 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b428aca-dcc1-3b4f-877e-7045804571e3 | -14.29094 | -60.36042 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9583509c-dc34-3a45-83f8-b3c8768a4abc | -9.17076 | -59.53368 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16175c00-b124-393a-b49d-b8b29a69e51d | -12.74379 | -48.09633 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 63b8d6a7-8825-3bab-bb1c-855047ffa2d3 | -13.45538 | -47.00719 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ab1a728-c895-3d17-aae5-edb570220d7c | -12.40977 | -46.49728 | 2025-08-26 04:23:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c79cc8a-65b3-325c-b95e-129e465a2c70 | -13.43409 | -46.92628 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d37529d-9de8-37ea-a8d9-7c0892c69e15 | -13.58601 | -48.2018 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e6dbc6a-8b53-314d-98d2-99bff9c2c0b9 | -13.51114 | -46.88765 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03a6c7d6-3340-3839-a17e-a5962a8f1908 | -13.6247 | -48.15222 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 205875f9-b26d-3f18-a933-9aea5fd85a1b | -12.76851 | -48.10724 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1860f540-2954-39d0-ab01-d389b1031db9 | -14.39891 | -51.94609 | 2025-08-26 04:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 995b31f1-2c6b-38ce-9d81-518439e5afc3 | -9.165 | -59.52494 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40a430f7-fd72-32b3-bba4-273fa994e136 | -12.74441 | -48.09258 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c44a2685-0b5c-3b56-8c41-44eea6954fb2 | -12.43975 | -48.71163 | 2025-08-26 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dd473d9-1b23-3c32-83f0-87fbd01c580f | -12.75033 | -48.16458 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 685a2bfb-61bd-3678-9838-25798d0f1d0d | -9.17006 | -59.45918 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 65a3dc9b-c716-3a32-8635-19ffcfd16eed | -11.53138 | -50.4544 | 2025-08-26 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eea1a85b-db65-3ed4-b373-a10d36752e78 | -11.54928 | -52.12309 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7266809a-1f7b-3f31-978e-df30a9a6c2c4 | -12.95675 | -46.33583 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbf3f95b-3ab9-3ff6-b0d4-7aaeaf0c7b46 | -15.88431 | -46.17496 | 2025-08-26 04:23:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba010ea1-539b-398c-9871-27766ac44c2b | -12.48515 | -47.22144 | 2025-08-26 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8c7299b-ef4b-3735-830e-a210d9d78d69 | -11.56241 | -52.12571 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a70970f-8683-35b0-859e-f260be39cd91 | -11.55835 | -52.09822 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a9641db-57d0-3f83-afe3-fa058a332303 | -13.47933 | -47.00781 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cf597b3a-5a98-362e-a5d5-2986e4a39ee9 | -9.17437 | -59.5136 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfe0cc17-fc70-396a-8f06-5fe94b10ccb4 | -11.29971 | -55.11156 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f042e60-6a8b-32d2-998e-1f3cf1bd4bed | -15.03401 | -48.68296 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 20eea462-d395-327a-8ad6-8dee2f144a8b | -15.05786 | -48.69818 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8736e973-f83e-3ab8-9cf1-9e191f172fe8 | -9.16561 | -59.55805 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69076ebf-f54f-3b00-8bdd-fd95dc72c940 | -12.44011 | -43.5624 | 2025-08-26 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af92d0ab-7266-3538-84f6-092217d6a86b | -15.95029 | -46.89359 | 2025-08-26 04:23:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 851a006e-55d9-3ca9-ae3a-d7a65b966a15 | -12.9375 | -46.33291 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d03fcfc6-7f01-3aee-8710-51be203e1acd | -14.43934 | -56.46208 | 2025-08-26 04:23:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af970383-b7f9-3bd8-9ce1-aeb106cd069a | -9.18253 | -59.51287 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3d0b24b0-c399-34b3-9d3a-d53d28a8cde9 | -13.65115 | -45.70649 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fd16846-b464-3abd-b511-89f4485a179b | -14.30132 | -60.36632 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e9589ae-6b19-319d-8be4-bda857a5f286 | -13.62294 | -48.14912 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53861ca2-abf3-353d-8229-ab476b4b20da | -15.64563 | -52.72988 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ad6cc4f-802a-3a3a-8b51-2303bf549d45 | -13.45204 | -47.00662 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a9c5c81-7b24-3c0b-813b-3e47db73e749 | -15.12195 | -48.63385 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b78d7951-8853-3cdb-93f4-2ce49fcd2e2e | -14.251 | -48.04821 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77c4a988-5697-372b-a1b1-7d1001b1620c | -12.94082 | -46.33347 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12f1cd45-6250-300b-8d8d-e57869949b15 | -13.41797 | -46.91988 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff4f2422-0081-37fd-8cd1-e2d5eba50a61 | -13.61951 | -48.14851 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03f79411-71a6-34a0-835b-df6a1d9bd0ae | -15.06605 | -48.69179 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7c60e4f-2eda-3fb9-b0d2-bcb2f6e2b67c | -10.64396 | -51.59489 | 2025-08-26 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c6d5d0db-38a4-34cd-bb48-d51b40a26347 | -11.03044 | -49.14322 | 2025-08-26 04:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 571858dd-5f29-3e03-88cb-62a6b425f006 | -14.4503 | -53.35773 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce966ad4-c408-3bdf-b68e-837349483540 | -14.24948 | -48.03617 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab7b88cd-b804-3bcb-a967-7045333ec3b3 | -9.18446 | -59.50051 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 123b8545-8c0e-370b-b535-4a2f7b959db3 | -11.63953 | -44.86272 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8170e46-478a-30a7-9f45-0ef70ecf1069 | -14.72647 | -45.36767 | 2025-08-26 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 708b6442-c97f-3fe8-8552-7360a9d599b6 | -11.62897 | -46.41282 | 2025-08-26 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ac33605e-647b-30e6-9d0d-46390ee3e86b | -15.65408 | -52.73181 | 2025-08-26 04:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04f55c54-0043-3def-818c-d54eabccd170 | -12.95457 | -46.32815 | 2025-08-26 04:23:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e45b10b6-3015-35bb-8438-30c06ced487c | -12.68052 | -47.86371 | 2025-08-26 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b10bfac-83e4-310e-b3ef-e53602c7d591 | -14.25693 | -48.03341 | 2025-08-26 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a96db97f-6a33-36a8-9add-48224e911ecd | -14.45108 | -53.35484 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a48a3f9-7392-3ca4-a594-4f5333caff32 | -13.50554 | -46.88697 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea7c925b-28a4-3f6b-9f8c-ebc7630a2142 | -9.16802 | -59.51009 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2e9c9a7-6c75-3d62-833c-33c99ba331cf | -14.28243 | -60.3659 | 2025-08-26 04:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50518eed-05bb-3dd4-af33-eaec048c41b2 | -9.58451 | -55.37006 | 2025-08-26 04:23:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f857c243-d1a2-3e49-8ec4-1fa3f16675ee | -13.43983 | -46.99716 | 2025-08-26 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3adce4a-ff70-3d5f-b7e4-113ddc52332f | -13.61483 | -48.15551 | 2025-08-26 04:23:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65c604e8-3b0c-39ca-a48c-96449bbd5c1f | -11.29905 | -55.11499 | 2025-08-26 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a0badb89-03b5-38e0-a5fe-85eea0c74bee | -11.55601 | -52.11103 | 2025-08-26 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30e2c700-c189-3466-926e-75d653ade7af | -13.16819 | -45.29194 | 2025-08-26 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2059f6c2-5058-33cb-a93c-1fc1c39ca244 | -9.1882 | -59.52209 | 2025-08-26 04:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bcc1d2e-3603-3459-bd50-efcf8c2191ab | -11.62893 | -44.86468 | 2025-08-26 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7e3a2b9-920b-3425-b0cd-558fd205e1b6 | -15.06214 | -48.71498 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0130efb0-e630-3e60-a850-02bab0631dd6 | -15.03683 | -48.68736 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f41e6f77-ae79-3d02-82a2-29bcf38dd3bb | -15.10988 | -48.7274 | 2025-08-26 04:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f9e248f-6cd7-32ad-a9c8-db623f988d89 | -14.24029 | -53.04553 | 2025-08-26 04:23:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc42b900-c68c-39c0-9db3-a777b91ca86b | -12.44262 | -48.71633 | 2025-08-26 04:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README47.md)
