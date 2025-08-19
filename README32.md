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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd165acf-82c6-3f63-85f7-cde1f952023a | -15.15926 | -48.77741 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 841c3285-35dd-3e54-a943-9fe11a53ec34 | -16.18693 | -48.98987 | 2025-08-19 04:29:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bbff10d-bb34-339a-bd90-1fe6dbd379d8 | -16.42508 | -49.33258 | 2025-08-19 04:29:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afa0f98d-3e69-35d0-916b-accdf344a68d | -21.19058 | -45.10917 | 2025-08-19 04:29:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| db7795ee-f523-39de-a272-6439c05e09a6 | -15.7891 | -45.36761 | 2025-08-19 04:29:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788e95f8-425c-320a-a6cc-5ad86c0d8d84 | -19.29736 | -48.43337 | 2025-08-19 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccdc4acd-e9bc-3816-974d-a05001c4ca22 | -14.31233 | -53.3787 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d668dfde-c552-3e97-b993-81efe0e4ae15 | -15.92374 | -43.51627 | 2025-08-19 04:29:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3e6d462-7d4f-3cd4-a7e2-d25f9fb69890 | -18.94903 | -46.26987 | 2025-08-19 04:29:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb4e38c7-dd97-3818-8a7f-4ae2fd242953 | -16.47497 | -43.4897 | 2025-08-19 04:29:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92793a8e-d411-3857-829c-931427ca7564 | -15.50629 | -49.96995 | 2025-08-19 04:29:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 373fefce-f693-33b6-bfea-69c90c5a76c8 | -14.98472 | -54.80815 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5107b276-c6c1-3c79-aea2-d2d4dc0510b1 | -16.50608 | -45.10151 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29c05101-9fad-3ac0-bf58-f84a2eac22e7 | -15.76871 | -48.18399 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50cc288a-043b-356d-ace7-a2a256c3202a | -16.48025 | -45.0976 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe59f811-77d8-3eec-8fa3-7d7f99eb1b23 | -19.55222 | -47.75235 | 2025-08-19 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3d7a76e7-f967-32f0-ba3e-5e36bb32a3e6 | -15.96374 | -52.21096 | 2025-08-19 04:29:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 356062e8-2974-3b05-9504-f750baddc16d | -15.40224 | -46.59954 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bae4e60e-1293-3cf4-96b6-1e4e88cf5273 | -14.31634 | -53.3794 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e54f67a5-a35a-3b75-8f4b-41fe98976b19 | -16.47963 | -45.10212 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e401a6a-457c-3bd0-8317-af8e4606a699 | -16.79293 | -50.0954 | 2025-08-19 04:29:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5a21d8d-6473-355a-af36-b5bbfa3a5ae6 | -18.60924 | -46.6822 | 2025-08-19 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9dec6ed6-0e47-341a-90cb-3a21f6148782 | -14.2998 | -57.76477 | 2025-08-19 04:29:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67b368a4-462c-38bf-9590-4c9bb567e297 | -17.33826 | -47.1687 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ab8804-db14-3969-b1d4-d1c872f54498 | -17.34108 | -47.17316 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9424fb87-a4f9-3843-aca5-8d020de1638b | -16.48086 | -45.09307 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a34af582-181d-319c-b02b-3dae53663385 | -20.86472 | -46.36243 | 2025-08-19 04:29:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66b130e1-653a-3406-90b2-bfb31b00a96f | -15.78708 | -45.36596 | 2025-08-19 04:29:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b730a0ef-c353-3f36-b0fd-3f1722b09da0 | -16.71746 | -47.62039 | 2025-08-19 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cb3ffd2-62fb-3ac7-8b3e-429232c1b315 | -16.08595 | -48.08815 | 2025-08-19 04:29:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61282d27-921b-338b-8a4f-2e7e2a2cfaa0 | -14.98391 | -54.81255 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2e4b16b2-a474-3d79-b418-b69d52161143 | -18.61274 | -46.68277 | 2025-08-19 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 249bf932-3d59-3bc9-a021-9449238022da | -21.39846 | -45.01273 | 2025-08-19 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 8034a230-2bbe-32f6-bc5d-9bad1c29e25f | -15.50905 | -49.97423 | 2025-08-19 04:29:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2817c58-7a17-399a-87fd-7180a0cec205 | -17.33768 | -47.17258 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf5e497e-64c2-36b1-8d57-e4522eb257d0 | -14.29557 | -53.35713 | 2025-08-19 04:29:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06742489-697d-32e1-a120-a234bf9f6eda | -19.82005 | -44.3277 | 2025-08-19 04:29:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 485db62c-1d8f-326e-9fbd-71e74f1a1f5d | -16.71635 | -47.62771 | 2025-08-19 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1dd0d81-35fa-352b-a2fb-0af0ac324974 | -15.47913 | -45.81131 | 2025-08-19 04:29:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11ea7617-43e8-3696-9ca3-68a9c1e13230 | -20.29761 | -50.95924 | 2025-08-19 04:29:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d4f463e-f623-3b0a-9df3-d4254e95c0fd | -15.19971 | -48.75851 | 2025-08-19 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6c3c16d-5544-392b-b31e-9bb1daf4cae8 | -17.40213 | -46.70892 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5d9b12c-9009-3aa9-bf11-36acfcfb1aa3 | -15.74671 | -56.02404 | 2025-08-19 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ba4f5605-849e-3234-b6f3-8c1ab732fbd3 | -20.98215 | -47.42058 | 2025-08-19 04:29:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccf2d004-db8b-325f-b333-7a1648a52f3c | -20.8013 | -48.79591 | 2025-08-19 04:29:00 | NOAA-21 | SEVERÍNIA | SÃO PAULO | Brasil | 3551900 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| acd71e42-f2e9-307e-a8d5-0c346a350d9e | -17.90857 | -44.42426 | 2025-08-19 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d443eafa-35e1-3f61-a6e5-ab7eb3593e28 | -14.96544 | -54.79108 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6ad0f94e-1610-3755-8faf-e138770dd9d5 | -15.74682 | -46.6121 | 2025-08-19 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec4316af-9997-3741-a47e-896046593f83 | -20.35443 | -51.71774 | 2025-08-19 04:29:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bf5d46c-28d1-382d-b532-99d6f05d1b1c | -15.98089 | -48.08599 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59fa48ca-9acb-3206-b60f-f31a15a9ee86 | -15.79985 | -48.22539 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0a4be11-5410-3e87-a633-2f6519d57e70 | -17.34224 | -47.16534 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50950964-c7ef-30c7-813b-2632b2233040 | -21.3825 | -45.76745 | 2025-08-19 04:29:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0273d2c7-5fe2-33a8-84dd-cd1089b5b9d7 | -18.17311 | -43.98349 | 2025-08-19 04:29:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19b85e81-ae4c-3dc8-98e3-ea358b0df326 | -14.71921 | -59.67841 | 2025-08-19 04:29:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69b69aec-1bcc-398d-9920-b535348d6d8f | -17.89515 | -48.6082 | 2025-08-19 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4f41741-b341-3b8b-b4ae-32f936163666 | -14.6477 | -54.91454 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15d452d5-b107-3f96-8000-fd9f83c46d3f | -15.79628 | -48.22519 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42b7f236-b1d5-3c54-a95c-61ecbf7ef308 | -15.02087 | -54.8136 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| de5283e0-74c0-3dda-a221-59ab07bcab27 | -15.40216 | -49.13383 | 2025-08-19 04:29:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a567232-2f9b-33f1-9938-da50b345c8d8 | -19.7181 | -47.93463 | 2025-08-19 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ee3897e-a9db-3175-b86e-30c9ab8a6740 | -14.96562 | -50.12295 | 2025-08-19 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79ec7ba5-9b27-36d7-bef3-405da65f49e1 | -17.40271 | -46.70493 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86722b02-2ded-3697-be21-5433782f4432 | -16.47778 | -45.09512 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a7585b4-cbd6-3966-8de8-3f77fdf6ca75 | -15.03247 | -57.19135 | 2025-08-19 04:29:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc1d1905-eed6-36fa-989f-f640651b787f | -17.82315 | -44.49319 | 2025-08-19 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fe4fb55-d633-3ce0-af1f-ff4b2a876dd7 | -15.79517 | -48.23233 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13f78eb2-3b21-37cc-9549-0d15968248bd | -16.81458 | -49.36549 | 2025-08-19 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0ffbcd5-eaa3-38bf-98e7-76a1b41dbb70 | -20.42475 | -43.69701 | 2025-08-19 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6b88894-731c-3cc0-be00-4f762811f099 | -15.76927 | -48.18041 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03fefe66-4194-304b-b450-5adaafac94f1 | -20.42502 | -43.69526 | 2025-08-19 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 041399ae-240e-384e-acdc-2c195870f4b7 | -16.50669 | -45.09698 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c4d0d0b-0976-3cce-ac48-008437d81429 | -15.71309 | -48.62881 | 2025-08-19 04:29:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7aa77b72-4660-3931-9a09-c119e62ea83e | -14.64412 | -54.90925 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56e9d969-d4ed-30c7-a6cc-f721dd762023 | -17.42405 | -46.70423 | 2025-08-19 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bd7b9f2-104f-3c8a-ba9a-41136ab6edba | -15.49366 | -50.30989 | 2025-08-19 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a8b557d-6f0d-34ec-9658-58d660f98d9f | -16.62355 | -51.35212 | 2025-08-19 04:29:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5900d8c1-061d-3cb1-a724-137c42cf159f | -19.30977 | -46.83856 | 2025-08-19 04:29:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ba14f47-abbd-36de-986d-a02ea28c2f51 | -20.35434 | -51.71702 | 2025-08-19 04:29:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e656ecc6-07a3-3dc6-bc1a-7461a5cf44d3 | -18.01238 | -46.71746 | 2025-08-19 04:29:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9f330824-3f9a-3da4-a148-d75d5c67ba89 | -16.79628 | -50.09595 | 2025-08-19 04:29:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9a699cd-58a0-35d6-9042-3c8cfef5ade4 | -16.47842 | -45.0906 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 998b8fbc-1604-3bbb-9bfc-2f7fc0c7fe0f | -17.81603 | -44.48724 | 2025-08-19 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d300e088-89cb-3f9b-981b-da70b4db227d | -19.93717 | -45.06718 | 2025-08-19 04:29:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3e7380d-4702-3669-81f3-5d498504ebcc | -18.5284 | -46.28541 | 2025-08-19 04:29:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c01ccdc8-1797-3458-9e2b-f80b9c35c078 | -19.2007 | -46.84334 | 2025-08-19 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00f53694-f884-3c11-b68b-8ce18ece3bcc | -16.50177 | -45.10546 | 2025-08-19 04:29:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c379b4bc-69f7-35b1-99d1-fa20525d919b | -18.37365 | -49.35728 | 2025-08-19 04:29:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3696ae7f-7759-3239-a315-25827bfbaba1 | -16.01515 | -48.08423 | 2025-08-19 04:29:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b15c67a8-5ccd-32a4-9278-ccb64ace0782 | -19.06295 | -46.74789 | 2025-08-19 04:29:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d772adbb-c44a-32db-88b4-61bbfe2f3212 | -14.99339 | -54.80979 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0fa8730a-e9ce-39cb-b926-36fa385b1657 | -19.29347 | -48.43652 | 2025-08-19 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85f0fcf7-500e-3cd4-8ab2-9ba7f65e9db3 | -17.48742 | -45.85656 | 2025-08-19 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03ec0a03-9377-3501-8b24-15ce3694601e | -15.03487 | -54.8107 | 2025-08-19 04:29:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4703d22b-f56d-31b4-bf4e-46be1e3c2b35 | -16.71301 | -47.62715 | 2025-08-19 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fef82eb4-aa49-380c-ac98-693aed90a18d | -21.4214 | -45.33973 | 2025-08-19 04:29:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0148818f-f968-3b85-a886-8c74e53d7f69 | -16.71691 | -47.62405 | 2025-08-19 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60015480-f7ef-3532-8dd6-fba4c160aea3 | -16.1875 | -48.98629 | 2025-08-19 04:29:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b11195a2-fbb5-382a-9364-eb13507e8031 | -15.50569 | -49.97364 | 2025-08-19 04:29:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5702227c-58e7-3b6b-80f7-45114f689554 | -16.42565 | -49.32898 | 2025-08-19 04:29:00 | NOAA-21 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
