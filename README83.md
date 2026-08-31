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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9d45c9c-f747-38c2-9a8d-4e441a3da335 | -14.98667 | -48.14602 | 2026-08-31 12:12:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| b616b95d-e400-3628-96ce-2bb5fc5a9486 | -11.24336 | -45.10647 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 77bac4b3-ce90-3472-ae6e-96cb215539f9 | -6.92091 | -55.69449 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| c44a4268-9d8f-3942-aca6-dd2e903d4ac5 | -11.5186 | -46.94945 | 2026-08-31 12:12:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 09fcc0ea-10d9-37c3-938f-a34a3b49a98b | -6.92979 | -55.63363 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f5fdf478-4a77-3811-82bd-3dd4d7a9d2e8 | -14.68063 | -54.90506 | 2026-08-31 12:12:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f7f71133-279f-31d8-90ec-e2ea48f4af84 | -13.96854 | -54.40878 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3fe82897-6b7c-30ed-ad35-6d9339ec3b40 | -14.29621 | -52.89484 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fd996e9e-9868-3496-a531-b300646878b2 | -14.15609 | -52.78105 | 2026-08-31 12:12:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 1a12b295-3f6e-3d9c-992c-ec9406ac9304 | -10.73719 | -47.95954 | 2026-08-31 12:12:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a0ed136c-eb52-3919-a1bb-8ddcb517304b | -14.44874 | -52.51223 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| d9d4df5c-e4ba-3ea7-8a72-9d4d48de5053 | -8.61339 | -54.77364 | 2026-08-31 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f6bc10bb-dd07-3c71-a952-bcd7467be35a | -14.39845 | -52.52691 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 7e82ac1f-3851-3900-ae08-8d1be8635d40 | -11.32452 | -45.1897 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 002be3e5-d840-3201-9cb1-7d83d3f5b55b | -11.74654 | -47.79789 | 2026-08-31 12:12:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b97c2780-dcac-380c-9f75-dcd867b23806 | -14.58832 | -54.12364 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 133ef30e-e83f-37a6-9419-961fae782e2d | -12.94808 | -45.92882 | 2026-08-31 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 2db40010-78a2-373d-a816-4d5a1967ecd9 | -14.42835 | -52.52008 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 5bcff54e-1b9c-3073-98c9-3b3387cd7cdd | -8.754 | -46.45555 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| e1e57e9b-2b3c-377e-8bd2-9282cc5191ca | -11.714 | -47.62555 | 2026-08-31 12:12:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 13b271b9-ec28-35d1-a86b-1707991132ae | -8.22083 | -54.93594 | 2026-08-31 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f1da736a-0c8f-3d49-afea-0d08846d5496 | -9.59333 | -47.59383 | 2026-08-31 12:12:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| d8593fc2-0653-3fde-be89-14ad9babe265 | -11.55024 | -45.45806 | 2026-08-31 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 0ce426da-ee7d-3870-b321-409edbd585b1 | -14.22931 | -52.84916 | 2026-08-31 12:12:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0003bf90-7a76-331e-b9fe-aa677fa0c67a | -11.52611 | -46.94502 | 2026-08-31 12:12:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ec954e2f-52bc-349a-8b0a-bb13e1339f3f | -10.15543 | -45.74825 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 289d758f-b934-3dfc-b2d2-b54e5751a4c8 | -14.14401 | -52.80005 | 2026-08-31 12:12:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| b8d4062b-5d8f-3675-a9e0-042bb3744e43 | -11.07833 | -51.51901 | 2026-08-31 12:12:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4034c158-3033-3995-94eb-920e182ddf6e | -14.26963 | -52.88093 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 03358576-5890-36f0-98f1-467d28828c4f | -8.82222 | -50.59513 | 2026-08-31 12:12:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 231a5aa5-567b-393f-b1b9-7098a7aa07e6 | -9.94113 | -60.51656 | 2026-08-31 12:12:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 489c5adb-d810-379c-a32b-b52a25237dbe | -10.74851 | -54.03552 | 2026-08-31 12:12:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 1a20e539-7db1-3975-8af4-629e9aa243ab | -7.5282 | -55.32371 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f733a743-ce3d-3091-823f-35915005bb7f | -9.98648 | -46.75227 | 2026-08-31 12:12:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 868e7e27-9721-385e-9193-273f6035513a | -13.96096 | -54.3984 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 103496f5-db4b-3ecb-9146-3e71221c9d4b | -12.22133 | -47.29192 | 2026-08-31 12:12:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 9a76e662-cba8-371a-94d7-ea10f8221ad1 | -14.39434 | -52.55844 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 77e8af0f-d0a6-3a3a-bd1b-290c80353a12 | -11.93169 | -45.05614 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c4ca95f6-61a5-3802-866e-8f77d1bab3bd | -9.44117 | -45.64107 | 2026-08-31 12:12:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 0cec11e9-7402-3584-9baa-bf3384ea7455 | -14.41884 | -52.51883 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 2e51037e-35ff-31bc-8ab4-4ff288043a18 | -14.30416 | -52.9062 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c9a16f5-a988-383d-a341-a78fe173657d | -11.69933 | -54.60522 | 2026-08-31 12:12:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5f6617d6-b146-3e16-9925-459d55af3146 | -11.18574 | -55.10438 | 2026-08-31 12:12:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 65ec8607-954a-32ae-877f-191d0f7280a2 | -10.79595 | -50.49935 | 2026-08-31 12:12:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d68a0604-7f03-3ec7-86e7-97dec18bba97 | -14.44732 | -52.52293 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 8ca00a00-046d-36e9-997f-69cd37722f4b | -14.15473 | -52.79116 | 2026-08-31 12:12:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 48068d6a-a5de-3d3d-8974-7a3d39016bf0 | -10.04826 | -48.67402 | 2026-08-31 12:12:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| a7a9e354-ca9c-34b6-95b6-c9e830274a94 | -11.088 | -51.52032 | 2026-08-31 12:12:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf75cd5f-5482-39a5-b24f-4eb58ce5d6ec | -10.80284 | -50.50682 | 2026-08-31 12:12:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 375c58d0-22bf-30dc-a728-3852de218df2 | -18.26918 | -52.7161 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5b1c7028-55b4-39ad-8b6b-9b1860b415b7 | -18.27065 | -52.70448 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| e0bb56ea-72ac-3112-ac8f-1498969a8824 | -14.82854 | -55.73637 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 09220589-3e5b-3ad8-bcb3-cfaffb0e43b1 | -19.11063 | -57.41126 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 4fcb2fa8-d8c0-3664-bbf3-b1a8ae909080 | -18.28198 | -52.69419 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 3179c831-07f9-3c66-be67-6ab756fe8e63 | -18.27212 | -52.69284 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 400115aa-d9df-3937-97f5-39de0c478052 | -15.79502 | -51.0686 | 2026-08-31 12:14:00 | TERRA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b432e38c-e875-3649-ab6e-60e4710810f2 | -19.14243 | -57.38257 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 8983b76a-e026-3f0a-9628-1066cfd46c8c | -19.12114 | -57.40298 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| bd812a9e-db58-375e-b105-593326522936 | -18.28346 | -52.68253 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 461f0bf0-6ce2-3b45-859f-4d444764bce2 | -15.98445 | -48.41499 | 2026-08-31 12:14:00 | TERRA_M-T | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |
| cee9171d-f7bf-3a05-8a10-cda6d1958acc | -19.11968 | -57.41275 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 05f061bf-ddd5-3a3d-8af1-d8d02963c631 | -18.27359 | -52.6812 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 55.2 |
| c8e54d54-977e-36c6-89f4-aca7bf5104dd | -15.79336 | -51.08223 | 2026-08-31 12:14:00 | TERRA_M-T | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2fc196a7-2c51-3285-8049-1ecce2ca27eb | -15.41395 | -52.71184 | 2026-08-31 12:14:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0826cbaf-2cf5-38f2-8fb9-5f83cedb8780 | -19.14095 | -57.39231 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| c1743f57-61ae-3f37-9c9a-b73f172bd5df | -15.98145 | -48.42144 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 5e056118-1981-393c-ac8e-220c149ad373 | -19.15147 | -57.38404 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.8 |
| 2ec9f5eb-f76e-3950-9d2c-6e5b72325850 | -19.13165 | -57.39469 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.1 |
| 8ae6d25f-b267-3b24-aadd-ae5bdc4a5fec | -18.27506 | -52.66962 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 46d96d56-8586-3cf8-9cc9-587b7fce182c | -18.26771 | -52.7277 | 2026-08-31 12:14:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 8d5d0802-8477-3cbe-9a3b-8daf5e33753d | -21.62048 | -51.15379 | 2026-08-31 12:14:00 | TERRA_M-T | FLÓRIDA PAULISTA | SÃO PAULO | Brasil | 3516002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 6feafc78-ef9d-397b-9c25-7f8ad43853f8 | -15.63639 | -50.09961 | 2026-08-31 12:14:00 | TERRA_M-T | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| afe9944d-426b-3aa1-bcc1-d372ecd61240 | -19.16955 | -57.38699 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 30.6 |
| d3cc0f5d-28ac-304c-bbf4-c5d60703a6f1 | -15.24007 | -56.38943 | 2026-08-31 12:14:00 | TERRA_M-T | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aeb1f640-b9ae-3792-aa06-05036cc407b4 | -19.16051 | -57.38552 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| cbea3c05-1a1d-3d53-bc67-b2d8ca2af61f | -15.99457 | -48.42326 | 2026-08-31 12:14:00 | TERRA_M-T | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c0d3ba86-b6ee-3bcd-a973-c036c90f21cf | -19.08348 | -57.40683 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 94f6582e-0c22-3c54-9198-377d1f76cc0d | -19.16808 | -57.39674 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 852fac1c-5ea1-30ee-afe9-5b8483be02be | -15.87063 | -56.49223 | 2026-08-31 12:14:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a5dee9e3-8003-3ea8-9291-45b169154840 | -19.15903 | -57.39527 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 50baea48-04cf-37f0-974d-6ef8095526dd | -19.1331 | -57.38493 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 059a865f-28db-3c97-9e3a-ab9b66f43f20 | -19.14999 | -57.39379 | 2026-08-31 12:14:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.2 |
| 23a17f14-ce2c-315e-bd1a-ca879e2ec8d0 | -8.75 | -46.45 | 2026-08-31 12:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4720c462-5c1f-3d40-8278-d297115dc8ce | -6.1294 | -57.6833 | 2026-08-31 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| f5975cef-5ce2-3ae1-b9f6-4e0289d1e3c1 | -7.9239 | -44.2327 | 2026-08-31 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0c8a4452-af49-31e4-9851-e2f0e30bdbb8 | -18.27 | -52.7068 | 2026-08-31 12:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 46d29591-2c35-3a20-b9d8-d12cb4719935 | -19.134 | -57.4005 | 2026-08-31 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 182.5 |
| 257c8c00-85b1-344c-bc78-e58041163f14 | -18.2899 | -52.7035 | 2026-08-31 12:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 056f029f-fa56-33f9-bdff-dbf89f84ba40 | -7.9605 | -44.3212 | 2026-08-31 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| d6cad1b6-34ee-37c3-a38f-ea21dcb2a47e | -18.2704 | -52.6851 | 2026-08-31 12:20:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 95fc8708-c882-3d68-858d-2fb4104c1d47 | -14.4007 | -52.5226 | 2026-08-31 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3dc3a2c2-f4d1-3a2d-a644-bb759e32513f | -3.5345 | -49.4733 | 2026-08-31 12:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| fd563b43-b371-3f15-8554-1141f64a6467 | -19.154 | -57.3978 | 2026-08-31 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.1 |
| e02c37b8-ea57-3ef4-957b-000a148ba5ff | -8.7442 | -46.4437 | 2026-08-31 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 15f5f20b-efcd-3183-98db-df5782aa829e | -6.6035 | -58.6166 | 2026-08-31 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8173a62f-9216-3618-9f02-ee99a1b8a6a3 | -19.1344 | -57.3797 | 2026-08-31 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.2 |
| 0eb86282-07b2-3bdc-82c6-cb8d1d419d52 | -5.2547 | -55.9105 | 2026-08-31 12:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 66dc8c87-9ad2-3d45-9f02-1324ec03b342 | -6.9177 | -55.6967 | 2026-08-31 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 803725b8-208a-3b26-aa91-46f2a765186d | -6.8992 | -55.6977 | 2026-08-31 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c7385d0a-3963-3ba1-a661-cd11ee9326c1 | -7.9797 | -44.2962 | 2026-08-31 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 198.6 |


[Clique aqui para ver as próximas entradas](README84.md)
