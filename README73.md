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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28bf69e3-76c5-313e-982e-ed152701e8c1 | -13.92445 | -48.10801 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffe3f7bf-7fb3-35cd-90eb-43443d7c86e8 | -11.81145 | -44.98056 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b46e8f89-f3ed-31a7-9c05-5ba1be484722 | -16.03076 | -50.88753 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddf4fe8f-7f56-3b46-b9a8-b4ff8d2506bf | -9.23912 | -50.62856 | 2025-10-01 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 843e6b11-0e18-3eee-88d9-017307b00213 | -14.72654 | -48.14436 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e4eb2b3a-dba7-3d9b-9bae-adf64a789457 | -14.98237 | -50.761 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05c9e619-a1e2-36ae-8bc2-2fc2fc49f5be | -12.69247 | -48.56511 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec724fa3-4d48-393b-9923-de6387dd2add | -12.87817 | -44.60374 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e4fe0fc-1e66-3343-b742-0a714c9ab37e | -11.857 | -45.01691 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| c59a552d-90ce-3cb7-b067-87f76c92dfcc | -11.47001 | -45.07957 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a37cb71-7c39-3430-9a83-8beec21e7ec1 | -11.59211 | -45.03675 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88f1d4ff-f343-3fb3-8635-b26779f3f0fa | -14.98155 | -50.76565 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aca82a08-11dd-381a-8e82-eae480103614 | -15.61275 | -46.52828 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b543206-ab60-335a-963a-9ef83becf138 | -14.72534 | -48.15179 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85c33a65-aeb1-38eb-b456-62b06d95e65f | -11.48676 | -54.60211 | 2025-10-01 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe60a2b-4fbe-3ead-a460-7f2ef6c58226 | -11.69513 | -45.36129 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20ac2fe6-0ce3-3f43-9a3c-78fb8758f041 | -11.52843 | -43.55379 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78895921-e645-3150-8d87-5dadbeeb1f38 | -13.31051 | -47.20994 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f0681a7-eed6-390d-914f-19d3c3a513a8 | -16.37895 | -47.0693 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 42902dcc-e45a-3286-8165-328002971568 | -16.52357 | -49.06702 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83e09c05-72b8-33b5-90f6-f685285a9ca4 | -12.8889 | -45.2709 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 218bfe40-2b28-3f72-8f19-9b89cd013b60 | -14.18619 | -46.12066 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 01e1d6c8-9cbb-37af-8271-9aa85dd10472 | -10.9276 | -54.33296 | 2025-10-01 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d48ab79-8f97-3048-8735-22bd269b13c4 | -13.77479 | -47.96472 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a22df1c-e099-338e-b464-3e5130562691 | -13.76982 | -47.95272 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ffba9c4-886e-3efe-93c7-32f8ce1d6283 | -15.21476 | -48.17459 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c3c8f6-5fcd-3b79-b6cd-e316068d63b1 | -15.39949 | -47.0661 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b9202fd-26c0-3b3c-a672-cc2613c0e5be | -14.10037 | -49.7517 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c20c1fb5-a7cc-3e80-95d2-40e75b6e41a0 | -11.47447 | -45.09479 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10614faa-fcc7-3086-b28c-1bdee478584b | -15.66822 | -45.24132 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77150eba-3c1c-37ce-b253-780c5885759e | -11.54351 | -45.06536 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c1b294d-0361-365e-adf2-b80cf8bd863d | -16.36747 | -47.03438 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 954fc9f1-1232-3a3c-8c2a-f1573c69e477 | -14.01924 | -44.85073 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c31856b3-67f1-3077-86e7-41dd7344ef0c | -11.81363 | -44.96627 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3876fb44-9abe-3550-9624-a127907614b2 | -13.76936 | -48.40973 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88be8c3e-f65f-3ff2-b542-cb8fd4121a36 | -15.26545 | -47.84165 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0e601bf-3bf8-3021-944f-cbe35f18bb68 | -16.37677 | -47.0616 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1f30fc9-ac97-3895-8689-b0b755cbe867 | -12.87292 | -46.90001 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efd1dca6-1cdf-312e-bddb-b4b1fb21bf32 | -11.73638 | -46.85453 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aeccb335-ea51-312e-8ba2-b7238dccd64d | -12.942 | -48.4161 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c573fa36-57db-342d-8149-6bad844b632f | -10.63612 | -48.58946 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de7b4af0-2f67-3756-8252-5d1655f76347 | -14.35257 | -45.90323 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8abb9d12-282b-32be-a4b9-73f757551f8d | -14.40023 | -46.18784 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a7abbe2-69ec-3bee-9e48-bec53c343663 | -13.66108 | -48.03716 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da246ee-a081-3a3d-91a1-8f5460bf658b | -14.90321 | -47.21341 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0da76e1d-9b1a-36e6-8468-bbb5e82e3a87 | -12.82996 | -47.02065 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0b1cc52-dc99-3601-b86e-b04dac061037 | -10.45042 | -48.08546 | 2025-10-01 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e84bf16-5faa-390d-917a-2b9b9737b067 | -11.84777 | -48.05522 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d69d08ff-e41c-39ee-b0c1-3f7710f5e7dc | -13.10165 | -47.02567 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc45aba0-9590-3169-b266-9bdcbd2669f9 | -13.66734 | -48.08422 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0c094f86-d63a-32de-910d-9397ea26fb70 | -12.15373 | -47.77412 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d232bec2-fce1-35e5-a62a-c541455e7040 | -12.88644 | -45.66417 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64544d30-634b-329c-a220-7ee1db2aa02a | -11.81908 | -44.93056 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 205a0c19-f5af-3854-b164-eb48fff9002f | -16.1265 | -49.14833 | 2025-10-01 04:21:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71b71077-5d01-303d-b51e-87aa2d4db5eb | -10.6319 | -48.59303 | 2025-10-01 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8eac691-4fb4-3fb0-9484-d3f87cfd8e68 | -13.98092 | -45.06024 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68f73fe0-70f6-326a-844e-cad6a6876c9c | -14.51049 | -48.47984 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5a70c221-beb3-3a80-947f-73dd26f49c7a | -9.40646 | -54.71162 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a942d062-e8b1-3e0e-9852-a408e87411a9 | -11.84156 | -48.05023 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f53b322-fd74-3031-8375-d4309afb534e | -12.18549 | -40.4074 | 2025-10-01 04:21:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3c597a1d-30cf-305c-83e6-932dc7122c48 | -10.10802 | -50.29235 | 2025-10-01 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0af9016-12ea-317d-abd1-1226166cb4b6 | -11.91809 | -47.90429 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ec88dd69-985f-3c3c-9c6c-72cf0f26e8e1 | -12.04027 | -47.90873 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c052209e-bef3-3de7-8d28-9d7c03d4c006 | -13.33099 | -47.82158 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94eed697-4c6b-316a-af2f-921d146a82f2 | -13.06431 | -47.06694 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed67b25d-55e7-3993-bd5f-b0269e7f0cd3 | -14.18949 | -46.12119 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b4178896-dfc6-37e2-b1a1-b33533580ae0 | -14.722 | -48.15109 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1b88a35-2b54-3d8d-928c-17ab041ae69d | -13.32856 | -47.83653 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 301c05f1-954e-3854-9197-307c9da354f6 | -13.24075 | -47.32718 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7447d119-e299-3fa3-b236-c68fb63945b7 | -12.35149 | -54.15442 | 2025-10-01 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ceed79d-422f-3425-9048-4af4d0db5c91 | -16.00973 | -50.89833 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64984a0c-cf0f-3e48-a13c-2b0723d039ed | -12.85818 | -47.01437 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fad3e109-2c88-35aa-bb52-982bc765d051 | -13.96876 | -44.91102 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 599b2740-fa79-3fb5-aba8-fa805b4461f6 | -13.666 | -48.04957 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05afe44e-d744-33db-9c34-d55db942db2a | -14.04863 | -47.97332 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f3d73cfe-508d-3cd8-9389-50a579f38935 | -10.91736 | -44.31031 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b748368-5c31-310f-9dbb-b9894bfa0f82 | -11.82477 | -44.98258 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfab79b5-3e56-338f-b9c8-e64b655c7783 | -9.42366 | -54.70764 | 2025-10-01 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41e5b85f-970a-34c8-be4f-785c63da6e2d | -14.71434 | -48.13444 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88415c41-e8e0-35a4-bd70-9cbde4481de7 | -10.88594 | -49.39676 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 457e9123-a64c-3455-b31b-27dc1fc8eebc | -13.7758 | -47.97982 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 44b4e432-babc-3def-8f54-f48f93f197b5 | -15.16066 | -49.09558 | 2025-10-01 04:21:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f6884cf-364a-3259-950c-ac9c259bbcd9 | -13.8896 | -51.84752 | 2025-10-01 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93059c59-9b80-321f-af05-441b2a628dbe | -11.45565 | -45.08462 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7efa910-b31b-3528-87cc-5ac1104e479c | -13.27776 | -47.22289 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82067581-5d1b-3ab9-8390-42670a93f9d7 | -14.80201 | -48.32872 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eb8bd7ed-7536-30d5-9b17-3ab01f0ef23a | -12.86657 | -46.98294 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aace689a-3faa-358e-8f8b-ad878e5d6b87 | -16.39719 | -47.03935 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 441d168c-9fb4-3c70-a6c6-d5e9f5f65b52 | -11.94175 | -47.08217 | 2025-10-01 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a9b66a5-9d9d-382a-a0ec-90eed32e4577 | -10.90871 | -46.53703 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8f6f9a8-6e49-399e-8606-21b5bb2ad2c7 | -11.58308 | -47.65386 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27a7ee0e-7af1-3076-ac9b-1c717a52856c | -13.98157 | -44.87143 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a907a4f-d46e-353d-9feb-71856622cd53 | -12.85826 | -46.99247 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d4e5361-2ff8-3527-bbdb-2cde10a7cb55 | -11.47501 | -45.09125 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f72c56c1-7602-3f88-ab14-ea47a9b5d40d | -10.35108 | -43.73836 | 2025-10-01 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa172f2f-7930-32bd-a93e-a45688b53af2 | -13.1446 | -47.41468 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49329b6d-71b8-3f96-86d6-c4de06138901 | -14.70946 | -48.27088 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1770a8b0-470d-338f-8643-c3e4aeb566b8 | -11.33799 | -48.31561 | 2025-10-01 04:21:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b516c7f-83c8-3086-8571-00b7196ea502 | -14.94711 | -45.54436 | 2025-10-01 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 523e3e01-8bde-3fec-96d2-71d3d9aef8a0 | -14.99275 | -46.96917 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README74.md)
