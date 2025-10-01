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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2c16c6c-fb33-387c-a5eb-082933e0d40c | -13.33286 | -47.8457 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 685cbec9-c135-339c-80ed-b21f63e3fc7e | -11.63432 | -47.49334 | 2025-10-01 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1dee66e-5b6f-34ac-8c39-eda8548f12d2 | -11.46627 | -45.07194 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5e6429b-7932-3966-b9f2-1a39b164dee1 | -13.53722 | -47.26175 | 2025-10-01 03:30:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c7d94cc2-55bb-3a33-b59e-6284cf8cf07f | -10.8453 | -45.41397 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6c4e4ba-b874-39d0-b9a5-ef293094b499 | -12.58741 | -41.28535 | 2025-10-01 03:30:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4f59b723-9eca-31f5-9f74-5326cd329659 | -13.284 | -47.24119 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6f0ecb1-fe9d-3a60-8c54-318dc744363d | -13.29865 | -47.23766 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 489d27be-0ef3-3390-b0cb-2151a0b17753 | -10.91111 | -46.58138 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c1ea6e4-2c7d-3c25-aab5-7a120390743b | -13.66773 | -48.07185 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 10f7c605-40bc-3622-b485-5492f31094e6 | -14.34617 | -45.93392 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a0f1aba9-137d-3eb1-a676-219a1fc9674e | -14.67067 | -45.30093 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e2305313-5f7f-396a-8b6a-9697ca3df6df | -14.60556 | -48.31351 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75d76245-1a61-3f8c-8223-4a8243381d81 | -15.2436 | -46.96906 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0d9582d-bc11-38bd-87b0-8cd0f344e5c2 | -22.11256 | -44.69009 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d24f6df7-3348-324a-969b-775fffd9e3eb | -19.93153 | -43.89423 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 634c3922-bd82-37bd-99b2-d5ba36b443e7 | -15.1274 | -46.45052 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83f39e5c-d418-375f-948f-9a13048b96da | -17.78437 | -48.63357 | 2025-10-01 03:32:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 55254d5e-3cd0-33bf-8a28-c2a06259e45a | -19.86399 | -42.57955 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad29374a-85e6-3db7-9519-9062e228ab8c | -14.66076 | -48.13772 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dbd8d9ef-689e-3e81-9ed1-ef0bab1ab372 | -17.79078 | -48.63458 | 2025-10-01 03:32:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b4714a01-1422-3032-93d1-0b33b106e621 | -15.17556 | -46.40639 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61101003-762c-3582-bd3b-c8bfa9b44f20 | -14.70105 | -46.98626 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daadc4cc-5dab-3182-9706-a3d837cad1bb | -16.40457 | -47.05818 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfbaf12c-6b68-3315-913f-f8c949a58b39 | -22.25314 | -43.43671 | 2025-10-01 03:32:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9dbebdf8-18c7-34d3-8d92-3384a8eec9de | -14.69834 | -48.13549 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ee7bf567-ed5d-38b8-ae65-df0b4df34cbb | -15.53273 | -45.2175 | 2025-10-01 03:32:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41d628b3-3b21-33bc-be3f-fa0f8d76c1f0 | -16.203 | -48.28021 | 2025-10-01 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f90ab7a8-fc82-3bbe-9f60-bad041d474e0 | -20.6203 | -46.20808 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fda65e61-6537-35bb-bc42-7c88ff19063f | -16.20991 | -48.28187 | 2025-10-01 03:32:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40592a19-729a-317a-b94d-c5c25577566c | -14.35251 | -47.13641 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 039ac8ae-4f7a-3895-8333-dec8b73c69c7 | -19.77069 | -42.14989 | 2025-10-01 03:32:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d8c1dde-05af-30f3-92f8-2637d6afec5f | -15.78061 | -43.69631 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e15725e-8b4d-3575-b377-1e2c16763b3e | -14.36583 | -47.13996 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| efa04774-583d-3a33-bad0-3e89d1bfc760 | -15.36186 | -46.11524 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e09932d2-69d1-3363-a569-567b52da6a51 | -15.93643 | -48.12667 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4769c72-7e0f-3550-8c26-bdbbf2bc56e8 | -20.62363 | -46.20073 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09dd054b-a703-3d96-8a56-3602aeb196ae | -14.6866 | -45.28498 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3ad625d-21f2-385b-adaa-db4814d67aa8 | -14.68373 | -48.23298 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| da18b272-f12e-390a-98c9-65e717ebdde6 | -13.93417 | -48.12059 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb2ecee1-e69b-3bc5-910c-c9cb1f99459a | -15.81808 | -41.89602 | 2025-10-01 03:32:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| eb224536-2974-3fe3-8d59-1baa4b330edb | -18.91545 | -43.11362 | 2025-10-01 03:32:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 43a92283-15c0-335e-9c26-e24fc5a9fcd0 | -14.43147 | -46.35693 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef84a51-97f8-3ad5-a093-0ba34ddbd381 | -17.00277 | -40.02121 | 2025-10-01 03:32:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 29a7eb94-7e70-374c-95ea-0c8e0a6c0f26 | -15.75929 | -43.69159 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29c91183-155f-3578-bc16-5f8f891a9d18 | -14.74899 | -45.77636 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e16c78a1-22cb-3d28-98cb-97b23829659e | -15.93002 | -43.30797 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8268ba89-4aef-30c1-b9d5-a16034521913 | -20.4387 | -43.59894 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 264bb71c-9ba5-3c9c-91f7-81266c272455 | -16.37354 | -47.07753 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 67289c53-4dc8-3dc7-8f0f-3e2b181a9a7b | -14.77977 | -45.80506 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5eac3a62-22c0-3b7b-a61f-1e060433af41 | -15.47046 | -45.87673 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3be372f-9af0-3da8-8f38-ccc2b75a2395 | -18.69802 | -44.33521 | 2025-10-01 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 850db878-a913-3506-a3d5-0c53b71fe09b | -15.77919 | -43.70326 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd6bcceb-768b-3b8c-8c3d-34471cc859c9 | -14.34849 | -45.92296 | 2025-10-01 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 34c4ae50-d2e7-3c8b-b40b-9a2165d2c384 | -14.69839 | -46.98292 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e9019a2-ffb1-3249-a935-e3ece1120b97 | -15.31238 | -46.40355 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 756af03e-bee7-316a-84ec-b295548fb3a6 | -20.23534 | -43.88335 | 2025-10-01 03:32:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 01b4d97b-d3d0-3c00-834f-e4bb37a11950 | -15.27444 | -47.84222 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1827900-c434-3b54-8999-b6a2d4e9e3e8 | -14.96098 | -46.87582 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd7aa8ba-481a-3281-a086-5848bb2ac83a | -20.63206 | -46.18186 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ece8438b-4f65-32bc-ba98-c6ed3d8cf93c | -19.37936 | -42.78203 | 2025-10-01 03:32:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b104df24-35db-3db2-b5d1-b66d8ceed80e | -14.76023 | -45.75345 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18412d3d-5db8-3ace-a2e0-95499346f2c8 | -14.67167 | -45.29621 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db6caf08-88a9-3795-a26a-c79f7b8487e6 | -18.42952 | -43.80038 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92330065-93a1-3a7f-934e-da6c2ae909db | -15.26618 | -47.84674 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a44654f-4c0c-3c96-9004-f0750faacd16 | -20.70008 | -41.56284 | 2025-10-01 03:32:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c1623300-c63d-3cae-a133-d7934a7959b2 | -21.66064 | -45.33839 | 2025-10-01 03:32:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cc171547-1064-35c6-a057-214bf80db1d3 | -15.7276 | -45.26205 | 2025-10-01 03:32:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cbd1422-85c0-39c7-bbe6-51bb36d08966 | -20.47702 | -43.94584 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d1049b2-cbfa-3d54-a435-ff0466d41b7c | -18.89563 | -41.05143 | 2025-10-01 03:32:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8aee62bf-41bb-3d30-9082-f276f607bf4d | -14.96541 | -46.87714 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93a89687-e089-3a44-a7bb-b36fc3425dc6 | -15.267 | -47.84525 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a85c22d-3816-3af2-a1fa-1e10cd20b150 | -18.32487 | -44.77072 | 2025-10-01 03:32:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f39a345-ec10-3127-bac6-e842945634d3 | -15.40653 | -47.05349 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9db46506-22bd-3909-959b-3225d6147045 | -20.02903 | -44.53244 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f14eb861-109b-397f-b3b2-4da981eec69b | -15.24192 | -46.96796 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9147e52-c14a-3a3e-a0b5-6d84535bb40a | -14.87586 | -48.32173 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7c689838-21a0-3da8-a4b7-4d2db6d5bf47 | -14.70363 | -48.12831 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ce69208-ff9a-3ed9-b017-b4cfd564c81a | -15.63597 | -46.25721 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 652d71bd-9a43-327c-8aa2-5b07212a2f2b | -14.74799 | -45.7725 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5c13977-c27b-3cc2-9b8b-95d8496f121e | -20.1262 | -44.02995 | 2025-10-01 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb3f2af3-e7c7-359b-9d13-d747ce1fa576 | -20.62581 | -46.21017 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca853030-e565-3585-b39a-c76e0e4a51c1 | -14.95878 | -46.87608 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa22c680-0704-3a26-8b1c-3911a724256a | -17.85982 | -47.14895 | 2025-10-01 03:32:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ffd4c6e-314a-35e2-a113-a8157b1c26da | -15.38933 | -44.97483 | 2025-10-01 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1935aabe-31ec-3075-a8a4-c1c00c272b17 | -20.62659 | -46.21391 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2b8a8a86-ff2f-300d-93f4-a7402c4e4d3a | -20.62291 | -46.22329 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dc95d25a-9488-38d5-8142-b1c7cba1f431 | -20.79563 | -43.51967 | 2025-10-01 03:32:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 03e433a8-2fab-3a75-b25b-93f98ca6539e | -14.98902 | -46.95766 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 046aa8b5-0265-3f46-b2a7-a25c4a1a7ad4 | -15.77279 | -43.68005 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8116f6e-e4d3-3cd4-abd3-5f62ed687a9f | -19.96355 | -43.71907 | 2025-10-01 03:32:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 03f6dcc5-1a2d-3596-9c2f-55cdde2b8c21 | -15.82302 | -43.32665 | 2025-10-01 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7183c7e1-11d1-36fc-9150-4b192644d9fa | -15.39549 | -47.07227 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bf9591f9-32d2-3ad6-87d6-eccbe2dcc70f | -15.83283 | -46.2575 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32e76473-32a2-31be-8224-7491d7367d53 | -20.59844 | -45.88253 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ba65f54-28a7-35ff-8551-eac226a89ba1 | -14.69834 | -48.26738 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ecc37e6c-34d9-3451-b5b4-6f0c323fc619 | -20.62569 | -46.21788 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7e12899a-35bf-3202-b166-5f0f9e2b53f0 | -17.95779 | -45.02275 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d20c255-8537-30a8-bb1b-98cda51cfb0c | -20.12899 | -44.0169 | 2025-10-01 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6ef9c099-53c3-3639-9ed5-61529c34864b | -14.78278 | -46.97782 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
