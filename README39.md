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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10bca137-de42-3a4b-9da4-147f3526a671 | -14.00287 | -44.04641 | 2026-08-25 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 181b9317-992a-302b-9148-7e0fd0d13cf7 | -11.90384 | -44.84822 | 2026-08-25 04:27:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08663fa7-7b8e-33e4-95f0-30485987096d | -10.56307 | -50.43044 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b73ca1d3-8597-31cb-be51-1fdff0f5dc69 | -16.38833 | -49.91614 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26e2d752-c57c-3ece-9733-b4ce0767c03d | -13.09183 | -43.37137 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c529e32-d825-309c-98d1-70dda63a0844 | -12.74909 | -46.46237 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1efd4311-fdd8-301e-a78b-71bae4fcc44d | -15.60344 | -46.57865 | 2026-08-25 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 879c12c4-4e4a-323b-a92d-65a07ff8a7fe | -12.12794 | -43.39062 | 2026-08-25 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97cae20c-fe04-36d1-8ca1-30306868408f | -14.80152 | -48.7637 | 2026-08-25 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6efa957-2003-34ea-abd7-057db4e2ecf1 | -12.71631 | -48.38506 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b1993e3-04d5-37e6-a841-96c4ea97a8ec | -12.78252 | -44.26435 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a75235e2-153c-3590-b556-043add831e5b | -12.89358 | -48.50036 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bf865b6-85e3-36a4-928f-4001dcdb4498 | -13.09829 | -43.36628 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0262852c-ab63-3f97-b752-5b7f098f3784 | -14.62324 | -42.53124 | 2026-08-25 04:27:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95a80781-8ae8-379b-acad-f024183ce47c | -12.77621 | -44.25946 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5e61af8-cf85-33cb-9c83-9c7d7a899a22 | -14.39375 | -52.95371 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c32e918-ea5f-3868-9b78-c65adba9f17e | -14.91244 | -52.64327 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ee360a7-c175-3b6b-8427-4360755bff96 | -13.86978 | -54.03294 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46e74597-8d7a-3754-8f1f-cf5d47abf53c | -10.79661 | -50.92493 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 12aefe4a-0e6f-3bfa-b6e7-494b72f26ded | -14.53163 | -53.2125 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc979f71-31bb-346b-a06c-739a1c8e32a2 | -10.90627 | -50.2452 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1437721-a334-3c6b-b0be-3bb1e7a12281 | -10.77877 | -50.93266 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| c5906557-15f1-33e3-85df-fad0735164e1 | -12.28131 | -43.13047 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51e064fb-0b71-34d5-868e-11509e73d319 | -12.61585 | -44.62814 | 2026-08-25 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 535a7df4-26f1-38a7-9276-448905db7e40 | -11.08113 | -46.14262 | 2026-08-25 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90bca9ff-7263-3c7d-98cf-4a9781886b1c | -10.31745 | -50.40695 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24051862-cef9-3ace-8ac3-6b407b6a1c3a | -15.28808 | -52.80327 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0bfc63b-4b05-3190-8422-0b3f491f0c43 | -12.85162 | -48.49722 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 61007507-6dc9-32ac-b66b-eb709ddddbed | -11.57299 | -46.97269 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 581fc332-f837-334e-9032-28617cafdc50 | -11.56966 | -46.97212 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb82e6fa-5883-3aa1-a223-257eaf849e83 | -16.40713 | -49.86935 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9520671-b931-3aa0-91ee-487e775c6cc1 | -15.27633 | -52.79645 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3242011-450f-35ca-8cc7-ebd74209c801 | -12.74965 | -46.45885 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa592990-7502-3a1f-99e4-e08f63200cdf | -10.60347 | -49.2019 | 2026-08-25 04:27:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64f788f4-928d-324b-82bb-b907610d16a3 | -15.31434 | -52.82567 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a4909ab-684b-3ef1-b415-e2cb045268bc | -10.32135 | -50.40764 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35737fbb-4bbe-3edd-80ac-65d0b0fbc3a0 | -12.77564 | -44.26328 | 2026-08-25 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f9ca106-38bc-3f91-94e8-6c3dbcc02dd9 | -12.84817 | -48.49668 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20bed785-050d-3a20-8784-5a786d49762e | -13.10188 | -43.36683 | 2026-08-25 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c318f23e-8f7c-3508-940f-5dbdb5e0d52d | -16.5006 | -54.6692 | 2026-08-25 04:27:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9429578d-79c1-3015-b2db-80fe720b2974 | -11.7782 | -47.23861 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2b74c66f-c9de-3233-afab-802bdb40a8e9 | -12.84127 | -48.4956 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b625c41f-cbf6-371b-bf0b-114c2f60cf71 | -15.37017 | -51.19595 | 2026-08-25 04:27:00 | NOAA-20 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96383c8d-89d8-3452-a15b-814b019b957d | -15.67693 | -42.4735 | 2026-08-25 04:27:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e3a0688-14f7-3edb-9551-fa50d1ef7306 | -12.75795 | -46.44938 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1ebb2f8-7e30-364f-841b-1bed3f91e63c | -15.24125 | -52.79825 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c7f55ee-a0fc-3cf2-9d8a-d986fcb5d155 | -12.58973 | -47.91664 | 2026-08-25 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa8b8628-d49c-3226-89f3-42c98ff93816 | -12.88604 | -48.5031 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27cd9306-be53-3454-ae40-527f8bcd1740 | -15.2358 | -52.80215 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1d12bde-f155-37cc-ba88-39404acb1329 | -16.06655 | -50.45912 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cd9f88b-8ed3-35f6-a9b0-84fd14c06593 | -13.35285 | -48.20803 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b1e4230-39f4-34ba-9d92-760312ac47da | -16.6385 | -49.40866 | 2026-08-25 04:27:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b6ea77d-fded-3784-8e50-2ebfb28b30f3 | -10.53386 | -50.78253 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 997abc33-d8a8-3001-8114-1449384c12c3 | -10.90755 | -50.2486 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19cc7a23-eb72-3f21-8d87-ab18dafc784d | -15.30408 | -52.81061 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab74d85f-c919-37ff-b7db-1baf5d3fd91b | -12.20257 | -43.1791 | 2026-08-25 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9b6be24c-ff4f-3a89-b6a5-302abfc0abe1 | -14.38947 | -52.95278 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51b82a73-38fd-3c8f-9cb4-4db0485a6123 | -12.86948 | -48.4963 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0b3b3e5-875d-33c8-beff-a13dbea5d903 | -16.4059 | -49.91938 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ac1fd2c-de18-309b-a0c3-48d40a45878c | -15.70474 | -48.31694 | 2026-08-25 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e972ce1-130a-3895-9b59-7a4ca24f06d7 | -12.88929 | -48.48362 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acf4e988-43a5-3ad8-a396-35b0e180927f | -11.65802 | -46.57222 | 2026-08-25 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ff57f04-8c0e-3e66-b300-9856025224fb | -15.25067 | -52.79189 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 063b7f50-6cc5-3893-8ccf-c1221a4c25aa | -11.98858 | -45.92362 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38b42060-9a8f-3158-b4bb-981ef214a961 | -11.16615 | -54.00648 | 2026-08-25 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f9248df-a04c-3fb8-bd9e-91db7bd704b2 | -12.7436 | -46.45424 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d918b5e6-7105-3c7a-8b2c-9cfa5197000a | -13.64311 | -49.031 | 2026-08-25 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37b7072a-1e7f-399e-a4f3-ba16e82e9ac2 | -11.43806 | -44.52626 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1e840a1-b461-39e5-869f-5797f97bad42 | -16.41277 | -49.87875 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45224c14-2033-3224-8390-395a60fe63ab | -14.40807 | -52.90032 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c3aef30-1aee-39e5-972d-d335d0ae0080 | -10.85089 | -50.5588 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddd9f2ba-a25d-3ac1-b5d8-44622629e99c | -11.98527 | -45.92308 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2462d91-cd04-3877-a524-4916d8131423 | -10.7914 | -50.93129 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 6b6cd879-8996-33a6-aa7e-0fe1492ac78b | -14.35415 | -52.89082 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b8455b9-8635-368e-a023-ce699e86cd47 | -12.87978 | -48.49817 | 2026-08-25 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee53a09b-99f9-3e85-9b69-ca967b896787 | -11.11718 | -49.88314 | 2026-08-25 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc983185-6628-3694-bccd-307f1fbf011c | -10.48094 | -50.4396 | 2026-08-25 04:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d125d300-4dad-3171-bdc2-2ba4bfeddbe3 | -12.71913 | -48.38934 | 2026-08-25 04:27:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 808403a9-dd50-3a13-a5f9-63f1e62c8e92 | -11.43753 | -44.55244 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8264af0b-dcf1-3f52-ae79-ed95d3753193 | -16.74371 | -49.181 | 2026-08-25 04:27:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 438d41d6-b45c-3a0b-a609-5a7387efa8e1 | -10.6088 | -52.22452 | 2026-08-25 04:27:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ae38ad-fdc4-3286-8fc2-0a4bfd76c17f | -16.84152 | -42.01796 | 2026-08-25 04:27:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.0 |
| ceb81e29-efa9-3b66-b171-f5b8b990ab27 | -13.86704 | -54.02193 | 2026-08-25 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45b0a8d3-66ee-37bd-930c-35f951b421eb | -13.35626 | -48.20855 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 760949be-08f3-3e79-8157-ebc5110a9e44 | -16.62848 | -50.4227 | 2026-08-25 04:27:00 | NOAA-20 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20314205-4b55-309a-b945-75fa05f048e9 | -11.57241 | -46.97628 | 2026-08-25 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81af7164-1d77-3e59-9b43-9a14d6dd997b | -16.0658 | -50.46348 | 2026-08-25 04:27:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddd9030e-d825-393d-a96a-794f0dc1f288 | -13.35124 | -48.19671 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3fdc014f-93bd-39db-84d9-fe78bec915c1 | -13.35226 | -48.2116 | 2026-08-25 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55f8cfad-fca8-343c-8bc2-60aef5991792 | -11.77293 | -47.27097 | 2026-08-25 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0f29596-680f-3504-bfdf-7596b6aa3a6f | -14.536 | -53.2133 | 2026-08-25 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fd20f34-6924-36f6-a32e-6d4d6132c245 | -11.99078 | -45.93119 | 2026-08-25 04:27:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2faf4106-3e7e-3ded-b5e7-47907dc2f070 | -16.40169 | -49.92286 | 2026-08-25 04:27:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 312325b5-734d-369d-9498-163ef8e8aeca | -10.93424 | -51.0741 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 157ceeb1-8396-3057-9647-24c111c4f072 | -10.77816 | -50.9362 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35fca54e-b71d-372d-859d-f7ca6e5f5ae1 | -14.92153 | -52.64079 | 2026-08-25 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28ba4210-27e0-33eb-85cd-ba888fdaf06f | -16.63491 | -50.4283 | 2026-08-25 04:27:00 | NOAA-20 | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a54916bf-1c0a-34c8-8f7b-8aaa1921943e | -10.91771 | -51.0971 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b576b7f7-ec58-351a-8475-c44631ec0760 | -14.87094 | -52.68062 | 2026-08-25 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57725078-f43c-34a4-925e-99f7a9e34b9c | -12.75408 | -46.45235 | 2026-08-25 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README40.md)
