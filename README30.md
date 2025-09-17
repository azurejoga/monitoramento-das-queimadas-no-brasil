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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4248d99-b11f-35f9-87e2-73294801b135 | -12.72461 | -48.02582 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24422fbe-f2e2-3dc0-a2bf-a238e54a189f | -11.17654 | -50.65959 | 2025-09-17 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1db8faaf-0b6d-3860-8e61-2f59fa33abb2 | -12.43977 | -49.73286 | 2025-09-17 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b568d1b-d60e-3057-94ad-0981c1ed04ff | -14.82171 | -48.11476 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1bbda00-9da9-393c-96ea-8c9768c30de8 | -12.72863 | -48.02658 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 369370ac-d97c-3416-ad50-682e49fa9d87 | -14.59976 | -46.37776 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2375d27b-d599-3601-aa53-0caf392a614b | -10.79847 | -50.72948 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdf84863-35c2-3a37-9fdd-bcbf2f3a2858 | -15.72053 | -39.32371 | 2025-09-17 04:12:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 058f38dd-e534-3224-9b9e-5ded2ffa5eee | -13.14471 | -51.6131 | 2025-09-17 04:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d08abd9d-00bb-33ee-bb4a-c21bdce32527 | -13.2786 | -54.18834 | 2025-09-17 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 217596cc-1e95-3999-b9f0-ab87b9ce8688 | -11.47005 | -43.57162 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c096084-af4b-33c3-aa7e-982339f771bf | -12.75345 | -47.95741 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ac4ab11-cc0f-39a5-b84b-1345dc359cb3 | -12.70375 | -47.95514 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d0fcd6eb-a4fe-30a1-8bbb-e015e63a8a78 | -12.97048 | -47.95553 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ca7c7270-7183-34b3-b93a-8d262335a4ec | -11.12381 | -45.11573 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16d22589-de00-36aa-abfe-ffc538519355 | -11.13826 | -45.33138 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12abf6d1-6f2d-3771-82a1-a712be6c63f8 | -12.74944 | -47.9567 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db7578dd-13ff-3e2f-90d0-5094b0710d3f | -12.06558 | -46.54041 | 2025-09-17 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9629a9af-f332-3057-9535-eecd59331625 | -12.86576 | -47.14433 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f0ac2844-e527-32ef-87d6-d1af5c99f4e3 | -14.60697 | -46.40054 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9434d60d-0136-3020-ba21-439e5f159581 | -13.86222 | -44.88845 | 2025-09-17 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8aae1a38-212a-3b3e-be8a-fd1149d6c48b | -14.6238 | -46.39756 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f77d21d-1cbc-3185-b7c4-1b4dfc9a2adf | -13.0314 | -47.96038 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa6eb961-8d77-3af1-8c37-ffe571d8f315 | -15.39492 | -46.14055 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aed9a19-03e4-30f0-90ff-fce2e5f99584 | -10.7936 | -50.72759 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac4376a5-8021-3815-acb6-3e88d7fbaaab | -12.9883 | -47.948 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f9ddd7b3-3c5c-360a-919c-e85124c4f201 | -15.40059 | -46.14989 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c7b461c-feaa-3e8a-873f-5c4931db2803 | -11.46229 | -43.55566 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b019cdb8-6580-34f3-8226-8aac09142d43 | -10.30492 | -46.63499 | 2025-09-17 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a0894e4b-fe76-343c-bf14-b854e9bd5ac0 | -14.39596 | -43.53015 | 2025-09-17 04:12:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32f82b20-1477-31b8-9676-b158705336d8 | -12.72252 | -48.01436 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1367d6d2-4529-3290-897d-4eb702eacc38 | -11.46669 | -43.57107 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 063b76fb-6636-3b8e-a85e-e1fe7a2fcef0 | -16.03185 | -45.16838 | 2025-09-17 04:12:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d57c291-ccf4-35ca-b657-14cc56ef3f14 | -11.04053 | -42.25161 | 2025-09-17 04:12:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f8ad045-f23c-3559-a35a-ca6b22e970ff | -11.34971 | -50.86036 | 2025-09-17 04:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41ce2e60-c5b4-303b-b838-ee0fe706846d | -15.88161 | -41.94779 | 2025-09-17 04:12:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5196c10e-24b8-3aa5-9b0e-38ec7ee90399 | -14.54788 | -47.42839 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3b635cf-2b19-3847-bd2c-73f8b1b0067e | -11.01903 | -48.92569 | 2025-09-17 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cf8b3ad-8c85-32f4-8ea2-825da159b318 | -16.58539 | -42.91387 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 25b3ad1d-0039-35f2-9b50-0b03a8285cd8 | -16.11591 | -42.61612 | 2025-09-17 04:12:00 | NPP-375D | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7786c50-53d7-3171-92de-e1dbd40ba099 | -15.40127 | -46.14583 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23ba0b53-c76c-3e91-8002-56d2d1ff7c67 | -10.62447 | -44.21885 | 2025-09-17 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98ffb78e-f252-3d01-9eec-26fca5b6f2d3 | -15.42566 | -46.1493 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5a424432-e0e7-38ce-857b-704eb03d6eaf | -16.65238 | -44.94353 | 2025-09-17 04:12:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeb6d987-a401-385e-a797-e6a312d8f382 | -16.42728 | -45.67166 | 2025-09-17 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dea22f30-1a87-3dae-8ad6-dd7b20cbcbd1 | -10.96438 | -49.57425 | 2025-09-17 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16c0ec16-4916-353f-ab11-d5aafb9eae79 | -10.81205 | -50.65456 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3f8baeaa-98e0-3e6c-8826-402c82b1ca8a | -14.61057 | -46.40108 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02883f39-f7dc-3605-9f01-3c89abc695b5 | -14.9165 | -51.6921 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74370c3a-2ff3-3660-9f80-b4c8e8887e85 | -14.5387 | -47.34652 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 411385f8-19b5-3e08-86c3-b051316a49de | -12.6965 | -47.7621 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f69eba4-4438-3981-8dfc-54e8fe009f08 | -15.91505 | -38.92149 | 2025-09-17 04:12:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c6f12685-4d1d-3df4-a373-329c6b940f93 | -13.62709 | -45.37393 | 2025-09-17 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 25c8d7f3-2ea7-3dbf-8724-5a84e0f4e9c4 | -11.46784 | -43.56392 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d7dde0b-cbc5-3d8d-bd12-33a7186a19b2 | -12.60776 | -47.98214 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10ba2a58-d005-32d6-b63d-04f7f8009f88 | -10.81102 | -50.66022 | 2025-09-17 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0184c5da-2fe5-3779-9438-490f257ca936 | -13.65306 | -43.65305 | 2025-09-17 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd1b7631-0604-37ae-a807-66798fedb4c7 | -15.42284 | -46.14463 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1240f340-0978-3c00-a370-f427198bd6dd | -11.49866 | -43.67976 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 962885f5-3b78-36af-b594-a3b3684faa82 | -11.50742 | -43.7108 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 723a62a6-792d-3d5f-b12e-2f51c8fb185f | -11.20876 | -47.67121 | 2025-09-17 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8505f4d-aabe-3b08-a273-3566a62ed96b | -14.80435 | -51.71387 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15dac557-d6b7-3d05-841a-cbd207fe14dd | -10.87551 | -45.44046 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 157ad089-f0f9-390f-8132-76e561dab467 | -14.81778 | -48.11415 | 2025-09-17 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e065f50d-c4e0-3c32-8963-ffbb0a924b0f | -14.54411 | -47.42764 | 2025-09-17 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 820cdca7-2a4f-3e79-b460-6d9a1b2d43a4 | -14.59747 | -46.32602 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6839effd-dcb6-3da4-9f30-dcb7a0bab50c | -12.60257 | -47.98507 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3143c8f7-1756-3ccf-bd6b-0d6e395eff92 | -13.22368 | -47.29501 | 2025-09-17 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7203ca65-31a4-3e48-b14a-d2412be0c508 | -15.97927 | -46.44486 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 223c63ca-92b1-3151-9ac9-618a2f92b769 | -12.28157 | -43.82642 | 2025-09-17 04:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 006e2b6b-5a65-3d8f-ab64-a3362328ed78 | -12.94793 | -47.96147 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 378f3172-b1de-3ba3-b264-7539a7866993 | -12.81345 | -44.99259 | 2025-09-17 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efd033a9-f0ce-3ac0-9ebc-ff4ed78f095e | -12.72654 | -48.0151 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 83bf950b-dc87-3180-afe0-406cbd211d98 | -13.7259 | -43.57327 | 2025-09-17 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96b0abde-8121-3191-ad99-e750e8ed1062 | -14.91049 | -51.69675 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e86b0c5-aef1-3992-aadb-812dcac42870 | -14.93941 | -51.67923 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79d114cc-567f-32fd-9e48-186a51614548 | -13.60841 | -42.4987 | 2025-09-17 04:12:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ae4935db-0d20-3300-b736-0c5b4325a9f4 | -14.47301 | -46.3568 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19357c32-45c4-3874-b5a7-4f7d8c728dc8 | -12.99321 | -47.94352 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3246e05f-f9da-3c80-b5f5-627d58e86cd2 | -15.41956 | -46.14462 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 904a8d07-09ba-3b34-ade0-489f75c2d315 | -15.42147 | -46.15259 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c932da4c-cc22-31c9-8d10-153977957dbf | -14.93832 | -51.68489 | 2025-09-17 04:12:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95d8b2c3-40e6-3f6b-86a2-8b7f30d3b709 | -11.49808 | -43.68336 | 2025-09-17 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db74ca9-d579-3b34-8fa7-c342266a36c5 | -15.39423 | -46.14463 | 2025-09-17 04:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b41c274-6a40-3266-8b18-97285d714782 | -12.114 | -44.83023 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc9f1ee2-eeef-379b-be58-d4a51d49ba98 | -15.42427 | -46.15735 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5be4a1cb-f390-3552-b39b-19fffa6c2cad | -10.63351 | -44.228 | 2025-09-17 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03e0efb3-4cb4-35c2-85e6-6934d26035ad | -12.70061 | -47.97313 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28db92d3-2698-32db-9d8e-6d88af10a6c5 | -15.98703 | -46.44212 | 2025-09-17 04:12:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d468cc6f-0e8e-3592-a06c-560bea2009f3 | -16.61289 | -43.36618 | 2025-09-17 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2668344a-bf70-376e-ac4f-e23498a3eab2 | -15.42779 | -46.15797 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1ebb9516-7648-366e-bc1e-4719576b7cd3 | -16.28203 | -45.68235 | 2025-09-17 04:12:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a88a4573-52cc-3f2b-853e-140646c6c188 | -13.28053 | -54.18983 | 2025-09-17 04:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8517cab5-4ed0-3778-a677-deb16024dde4 | -15.4228 | -46.12379 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e2e22a-fd1f-3bd3-95db-791dc27d3e12 | -12.10085 | -44.82403 | 2025-09-17 04:12:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37c67127-d15b-3ec7-b9d9-5b6ee15ca422 | -15.42894 | -47.323 | 2025-09-17 04:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d2d093a-1074-3f01-b6da-07894879a0a2 | -12.71834 | -47.99148 | 2025-09-17 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 848d735c-dcb4-3415-91f2-cdb9d680e61d | -14.60768 | -46.39637 | 2025-09-17 04:12:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1befdc90-5396-389a-be2d-c4c6fa9db845 | -15.41866 | -46.14788 | 2025-09-17 04:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c59745b-5bf9-3f89-a60d-5d4841a7c64c | -12.35819 | -47.06248 | 2025-09-17 04:12:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README31.md)
