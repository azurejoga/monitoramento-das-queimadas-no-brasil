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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71f55171-344b-3491-8c05-134d4973b374 | -11.64782 | -46.38704 | 2025-08-28 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 190f0acb-28b5-322c-818a-26ccb310cf4b | -9.63632 | -49.7642 | 2025-08-28 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7dad8662-2667-33d5-9b45-52ac49812645 | -12.79076 | -48.19002 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6a3f24e-7b57-37f9-a390-2d8c8b26bd03 | -13.63188 | -48.21531 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0914a942-b910-34a1-912b-a9c3cb2a05d8 | -12.40749 | -46.48714 | 2025-08-28 04:08:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04cdee27-70f2-35c5-9654-51ee8e168a0d | -10.48924 | -51.58892 | 2025-08-28 04:08:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d7cb848-8ebd-39a9-849f-06c7caaaa184 | -12.79445 | -48.14574 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9b2d48f-c184-31e7-b525-5b3d0abee1af | -11.32632 | -43.52435 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3a31349-50d7-3cd2-ad2e-9d44b19f69e2 | -13.6685 | -46.88057 | 2025-08-28 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73541cb1-f12c-3c4e-98be-6a6ac077bc46 | -8.26822 | -45.1672 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7aa3015-526d-3c0d-995b-92d964500126 | -7.26162 | -45.35693 | 2025-08-28 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42f67d10-1d19-3aa9-b7e0-0014b91b53f4 | -11.81221 | -44.25848 | 2025-08-28 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b25b6800-eb32-38ea-b74a-ff32f6d55358 | -13.39947 | -46.86963 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1e1be25-85f1-35c5-bcf6-22d1958b2b29 | -11.57322 | -47.62266 | 2025-08-28 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f04e50a-7327-331a-994b-ea89881ae6bd | -12.80801 | -48.16285 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f377f8cd-9710-3019-b16e-115cea5ec02e | -10.70758 | -47.01834 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 2e094478-f9d6-366e-b0de-37c0997bd3b3 | -13.43582 | -46.96761 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e2b0beea-44a2-34be-aaba-45de4734b27e | -13.98254 | -46.33957 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 93d6ebb3-eef2-352b-9478-dc5fca0029f4 | -8.27486 | -45.19403 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d8238fb-08cc-309e-b593-e038a1229d0f | -12.43995 | -45.96208 | 2025-08-28 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7d53686-8848-39d4-b65b-2af9dc39a171 | -13.42103 | -47.00888 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c675c738-543e-3e6d-a6ad-0909aa92bc00 | -7.23728 | -45.43412 | 2025-08-28 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2cdba4a7-2e63-30e9-ac9a-181c8986da3a | -14.23258 | -48.03561 | 2025-08-28 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a7b12a7-7fc3-394c-97c2-cf5bc5adc84d | -12.68029 | -48.17664 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6dd9b277-925c-3b7e-be4c-4d14a7d8e8db | -13.62388 | -48.21415 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1779fcce-ee64-35f6-aa80-816aa76f0764 | -8.28899 | -45.15371 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b3a75e02-09cc-30d3-a843-6737e12e4847 | -13.98969 | -46.34075 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bb69233-c038-3887-b2a8-3caddd8f13a1 | -7.90235 | -42.79498 | 2025-08-28 04:08:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f584b8e2-9105-309d-acdd-3642f6dabeb8 | -12.79044 | -48.14497 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa3d11e7-0f9b-33d4-8233-97c5afc317ce | -7.73917 | -50.27613 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62f26d8e-1212-3e0a-b671-fc2ad6e90c80 | -9.85715 | -44.68565 | 2025-08-28 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02b4e8a8-5e13-37a3-ab88-3f9737c3cd49 | -11.33347 | -43.54375 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f6dcca-1aaf-388b-81c1-864c2535e1b3 | -12.79141 | -48.18633 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39624064-a58f-3e97-a43e-58ef4bd1c93d | -11.32965 | -43.5249 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 549d966a-9f00-32ac-b206-0e9dbf127032 | -12.69841 | -48.16822 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47c669e0-f821-3ca8-b80a-e38744d0b07f | -14.50393 | -43.85645 | 2025-08-28 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 422214f6-085e-37ac-82f8-9968af11be38 | -8.08845 | -45.00736 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02aa39db-04a9-3058-a4b3-8e8259750f76 | -14.63953 | -46.8442 | 2025-08-28 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 222edb8b-ae76-387d-874e-ca5efbfddba2 | -12.9569 | -44.5752 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ac9697f5-8426-3782-a3be-dd0cb248a991 | -12.69777 | -48.17184 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2f7ebb0-0c43-37e9-8f7b-3e518f56effd | -8.45274 | -43.70803 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a037da-2fa6-3712-a954-ec18c5d4c1ae | -11.74374 | -49.08382 | 2025-08-28 04:08:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75a8b72d-33f7-3390-97da-d3a80854140f | -10.52627 | -46.69322 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| b9c05657-2b05-33a8-9326-85bd1192c3e3 | -13.47323 | -46.99492 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1584afbc-dc18-3975-9e25-169c4c4133e3 | -11.22376 | -55.0629 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| efecaf34-8cec-33cd-8695-c53b03912a08 | -12.06428 | -46.62908 | 2025-08-28 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5ebcefa-0f11-3c77-baa5-1f573f9f3556 | -12.95811 | -44.56786 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 09a919c3-7f65-3abe-9bce-d095bec2954a | -13.42844 | -46.96611 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4de8e9f4-eba9-3abb-b3c3-6c10ef6995f3 | -12.79994 | -48.16156 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df328d62-1bed-3cc3-87fc-b1546801fbf5 | -13.46322 | -46.85287 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f86af9b1-c611-32d4-8c5c-79c1db68ab60 | -11.33127 | -43.5361 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5d869b4-00c1-36b7-81bf-8fd1eb35ef03 | -13.54639 | -46.914 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e6fadbf-9264-3b96-9be5-28a967ee3b1b | -11.28276 | -43.30633 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cc6bd8f-ba87-36e8-ab9e-c31345a4f40f | -13.38665 | -46.88743 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f178eec-f9d9-3b72-807a-f48e3e7e7670 | -13.41812 | -46.85 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 19bfc555-4c48-3db9-bd13-f08e7e128926 | -7.74909 | -50.27888 | 2025-08-28 04:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48eb5e07-f061-384f-9402-06a5de71debd | -14.14282 | -45.40679 | 2025-08-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 330d5470-cf4a-346e-ba0c-fd3397c9c78e | -13.60082 | -48.21775 | 2025-08-28 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05fead9e-5fef-3976-9a41-cc22733d8324 | -12.80187 | -48.15062 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7889dd3-137a-3439-a82c-ec617c7b5575 | -12.70248 | -48.16868 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4271e582-5813-3147-b217-66d1adacc032 | -8.08473 | -44.98545 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 397c1f83-dc38-3376-b8f5-205ca0242498 | -12.81366 | -48.10724 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06f2295e-4974-36bf-be14-e5baa5cf85fb | -13.43662 | -46.85288 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f4b9ed7-68f5-30c0-8643-2fa805cb53e9 | -11.81377 | -46.81982 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16214ffa-affe-3f89-9cf2-98328fcd2a28 | -12.78403 | -48.18111 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8783ea83-7cf0-3b69-844d-0abde0cef331 | -11.79742 | -46.80235 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa9dad3d-ef55-39e3-94fe-df9445515c0f | -11.34221 | -43.54868 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4b943107-36d9-30d9-a5c1-bdc66a9fbfee | -12.8958 | -44.64542 | 2025-08-28 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 096c1a39-3c12-32ff-96d0-19e751a1177d | -12.79524 | -48.1647 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0535b358-40a2-3d03-b9c8-f0385f08ebc6 | -9.86409 | -44.68676 | 2025-08-28 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 338867f8-f08d-31a5-b1b1-fbdf57491054 | -13.44843 | -46.85053 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 771200a3-21a9-3098-a7c3-1af513032a67 | -13.43039 | -46.97698 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca02aefa-92cb-3bcf-9a9f-c4f9c8d41a6a | -9.13162 | -40.55888 | 2025-08-28 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2ce8c176-bf2b-36ea-9c40-abae6cb407e4 | -8.23859 | -45.06957 | 2025-08-28 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 94c828a6-9414-3622-85e4-a1603d78748b | -13.45584 | -46.85159 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5b0ff51-1366-33ac-8fad-9e83f942403a | -12.7853 | -48.17393 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2428a982-ad02-3881-8492-193c193482d3 | -12.80928 | -48.15564 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b406237-ccf7-3dbb-a53f-53e165ceed15 | -13.73231 | -51.90968 | 2025-08-28 04:08:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbb8e847-110f-3056-94eb-1416a7d3a015 | -11.55227 | -46.35343 | 2025-08-28 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5551d3e3-81f7-3fd7-a557-83a0d59c1af0 | -13.18593 | -45.29407 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bf3d368-e774-31d0-b224-5c8697c4f6f6 | -11.22463 | -55.05634 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e6948af9-8afe-3cfa-8770-45adc2bcf1b9 | -7.54346 | -47.48174 | 2025-08-28 04:08:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 977b9698-2081-35a8-b1b1-077e9d036570 | -7.71262 | -43.96721 | 2025-08-28 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9abe350-2de9-3689-9c88-32a82b08d050 | -11.57624 | -44.64937 | 2025-08-28 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7010b74-afd3-33ca-a8b5-53eb11f8ff0e | -13.17624 | -45.28843 | 2025-08-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b31d5131-c11f-33b9-b937-b490332f341a | -13.98182 | -46.34377 | 2025-08-28 04:08:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3c8876fb-4763-3ec2-95a1-31835af35ba1 | -13.51582 | -46.87099 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 466dc5ca-6ba9-3bd5-9ef1-1e9c10d2ebaf | -11.34183 | -43.53419 | 2025-08-28 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a09acdd-81bb-33e1-924d-af87e84a7950 | -11.65152 | -44.87545 | 2025-08-28 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddc26ac8-dbe2-38da-b38a-b7d9665e8157 | -8.83484 | -47.9226 | 2025-08-28 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f14859ca-c25e-32a1-9711-9da44f7c3b29 | -12.78784 | -48.15962 | 2025-08-28 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 504494c0-fc45-3b08-ae85-33dda5af34a7 | -8.43874 | -43.68691 | 2025-08-28 04:08:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d4be4f3-6239-3857-b844-7d24809519dc | -13.51295 | -46.86569 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 55f0a203-4953-3b0c-ada8-3b62ec605713 | -10.5415 | -46.69577 | 2025-08-28 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95b516eb-ca9e-3931-8436-05b31acadff6 | -11.56926 | -47.62195 | 2025-08-28 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e82c490-6b44-3f1e-a12f-d57596b5e46e | -6.4913 | -53.39406 | 2025-08-28 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9a3926e-4146-333a-bd4a-b675835896ab | -9.77315 | -49.88398 | 2025-08-28 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 069ad549-9941-3786-997e-7e21c6ff8899 | -11.22892 | -55.06844 | 2025-08-28 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80d9a1d8-c811-3a73-b202-0febac6a875a | -13.49998 | -46.86001 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8b777d9-7e50-3b2d-ac90-2141d3ebf74b | -13.42668 | -46.97628 | 2025-08-28 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README36.md)
