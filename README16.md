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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b699d28-b49f-3b96-8892-e54b9517a0c4 | -13.50022 | -46.98329 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7eb430bc-ce7b-37bc-ab68-c45a418d1fbf | -11.37657 | -43.62084 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abbf65cc-2e6d-33b5-b493-f6f983a83403 | -13.69763 | -46.8799 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14c95be9-44f2-389d-9d62-0a972d97faf1 | -8.19524 | -46.77238 | 2025-09-01 03:45:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c368bdd1-c6e8-322b-8afe-c8c90e1df6f9 | -11.80285 | -44.94483 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38d92095-3c7e-31eb-a324-aef8ddc057f1 | -11.78736 | -46.43705 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f08627d0-b34a-3c15-b9e7-1ca06f416184 | -13.34727 | -47.03767 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74468c2c-0459-399e-9d39-ac9805719802 | -11.89939 | -46.68548 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d1e5f78-fb86-34cc-9e5c-f89246fa088e | -11.02897 | -47.03105 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36a9c306-0a61-3548-8d66-3d7684ce8baa | -13.51931 | -46.83127 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ba30c45-23c8-31e1-b6c0-05b18ec10c91 | -12.59093 | -48.19453 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d9dfbed-2e21-370a-b96c-50e1169ddeb5 | -13.17685 | -45.28492 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2701b0d3-5565-3edc-8ef1-718dcf77759a | -11.02662 | -47.04315 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 640970a9-a711-3f46-aad3-91d69ab5e2b6 | -12.31306 | -45.68063 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9e594c79-fa2c-3a38-a062-83e749a5c9df | -11.04846 | -46.9612 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbcbd9b2-9fb3-3505-9fde-8ddde1976a1b | -7.95329 | -46.36193 | 2025-09-01 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fcbc262-19d0-3ba7-8102-c2b4547d90e5 | -11.37085 | -43.59988 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b10e0d5e-6d4b-383f-912b-2e482b61e8fc | -13.33571 | -46.86322 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13e9e68f-6e65-3666-9e32-7077b51782cd | -8.84263 | -47.51454 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eba87991-9ae0-31f2-9596-715f0cac1d15 | -11.08972 | -44.61585 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f90e52dc-9e09-3f95-886e-4d9acb955a2d | -10.60861 | -44.3259 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 73d79693-eefb-3e47-8456-6ebfbc78ee21 | -11.78807 | -46.43338 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a7d023e-b6cf-34fd-aad0-49fa79d0eb27 | -8.17482 | -45.03995 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23d6f608-b428-3df3-b0f7-f06f05d061c6 | -13.48699 | -46.93534 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05746837-1758-32e3-9c41-feda6bf414ee | -13.47515 | -46.93821 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7395c07c-46aa-3fb4-9b17-2fd900411e85 | -13.47595 | -46.93414 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c034c557-ed2d-396e-ae23-481c669cbfe6 | -13.40641 | -47.02523 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8aba7668-6fde-333c-853e-2da4fb5d47ba | -12.96517 | -48.11089 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 481a977f-5d61-30d7-ad40-55902f15cc2f | -13.37695 | -46.318 | 2025-09-01 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08c2a771-594a-32ae-9ea2-0516b3763c92 | -13.29466 | -46.89729 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f64515d-b0e7-3954-a022-3a6ea4b47248 | -12.21872 | -43.87683 | 2025-09-01 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edf9f1d8-6773-35f8-b050-137b931334e1 | -7.4587 | -44.81364 | 2025-09-01 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 085307fd-f2ef-32a1-b883-81b4d12236cd | -11.03623 | -45.14577 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f53462c4-a038-3a5e-ad14-798cb6621513 | -9.63672 | -47.79969 | 2025-09-01 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e04c8bcf-b2e3-33d6-8e3d-ea733f2973a2 | -11.95855 | -45.80166 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6a92818-41e6-3296-884f-41c72342e24c | -11.80731 | -46.42208 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f36eb239-e40b-3f56-bdfa-d3881e63f288 | -13.46995 | -42.47946 | 2025-09-01 03:45:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 77bdf2e9-4f65-3482-8948-8571462af950 | -13.48657 | -46.99408 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3989232f-5315-3a58-8600-82e423fb370b | -11.35534 | -43.52867 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bd7b99e-54b1-3720-b939-5f407d273093 | -13.41195 | -47.02628 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 28abef00-6754-3d30-8dbc-caf1d1fb5e42 | -10.8915 | -45.80574 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd694221-990d-3bab-ba3b-048b71cad140 | -12.58349 | -48.20581 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4537bae-5e35-3c0d-a482-33b5f8d30ee2 | -14.04236 | -44.55352 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 346b85c6-3e19-3328-a23f-ac3bd8ca8f66 | -11.90563 | -46.68304 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5606813-6238-3ccd-b341-e3692dce85d7 | -14.04604 | -44.57339 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c0e6741-5e6b-3f4f-bbd1-d0a1491c5096 | -8.83644 | -47.51346 | 2025-09-01 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f659876f-a55d-3f31-9126-934a7a498a32 | -9.6691 | -47.04406 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b71fc299-c255-3ad3-8b13-6cfd7cb5db2c | -11.3705 | -43.57549 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 159d38b8-e459-3a53-9f01-d54a322df826 | -7.63006 | -46.55109 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be106ff2-a9d1-36a9-8398-73ab0eb19117 | -13.2939 | -46.90106 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d3dead8-6e35-3084-acf0-2d63c5a688b4 | -12.41088 | -46.45932 | 2025-09-01 03:45:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecb560ea-e402-3cd1-82e9-e993327b0615 | -8.88095 | -47.20661 | 2025-09-01 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a76e1e09-bf77-3235-9e1e-99c8e4bbe9a8 | -9.67115 | -47.04601 | 2025-09-01 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c20299b-b9d6-341d-b3c1-e22bf3cdf2e6 | -11.3722 | -43.64527 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08dedefe-9a2d-3231-b394-cbfad53b05dd | -11.04806 | -46.90176 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c4393f4e-c5c1-3449-9ec5-e804556c4b69 | -13.16691 | -45.28304 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f214c69b-25ab-3348-b1cb-3f99c4d091cb | -14.0321 | -44.47915 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d1acb0f-e57b-3f4e-8e88-6aa9b2bf6571 | -11.95511 | -45.84906 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d3d2642-c074-3dbe-9123-6b9f996f86be | -11.80836 | -44.94287 | 2025-09-01 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85e369d5-83f9-30bd-b045-bf0bdba88024 | -12.78497 | -48.08546 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd9cf7c6-652f-3860-a1b0-84af0dfc7898 | -9.63958 | -46.60571 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a68ff4fe-9913-3361-9c07-7ef9621ac4e4 | -7.67492 | -42.66101 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 06680ac6-b135-3391-b7de-4d24d272a02c | -11.03039 | -46.99286 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c42baa63-5ad1-330a-9afe-ca759fa65ff1 | -13.7049 | -46.90073 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d8e6f4f-8735-3c2d-92fb-8756c41c6cf3 | -12.32635 | -45.72292 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d00f5d2-b53b-3313-b960-74df03d15306 | -8.17011 | -45.03551 | 2025-09-01 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4932af14-eb7f-3f05-8224-cd9e10d93cd7 | -13.36522 | -46.94571 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63ec74ab-868d-31a6-be29-5a0fb133e7c1 | -14.04515 | -44.56453 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 055d3632-3728-3598-9987-1c0b0be9ecef | -12.23605 | -50.16752 | 2025-09-01 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4be1bce2-5701-3872-b860-7bab071fa836 | -7.62878 | -42.65525 | 2025-09-01 03:45:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 965997cd-124c-3141-a53b-1ad13ba9112e | -13.70002 | -46.89995 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e367e3b0-98d6-338f-877c-d34805dfdc91 | -13.47636 | -46.98786 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 408bee2f-d908-337c-8f86-0cb8fe482f95 | -11.37025 | -43.62963 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d540c4e-f503-3b0b-a87e-86903e366c18 | -11.05063 | -46.9192 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ce57b58-ba8a-3da5-8fa3-834fd5cabba4 | -13.37631 | -46.94755 | 2025-09-01 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6c15188f-898d-3d0f-81f6-ce362db97288 | -14.04778 | -44.58951 | 2025-09-01 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e5d1fd9-c454-3426-9433-2d98a5664e83 | -11.03884 | -47.04197 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| ebd3cea8-1136-3dcc-b560-a9d4bd065a6a | -11.89439 | -46.74195 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c010222-fb30-37c9-a5d4-45b3963d4492 | -11.08755 | -44.62727 | 2025-09-01 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b57ba595-e147-3344-812d-dabaa9fe1450 | -13.16747 | -45.28012 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| bd8686ed-5ed5-37c5-bf63-aa98c7b2b47a | -12.5685 | -48.21745 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| eec752cf-caa0-3f6d-b26b-caaa1088596b | -11.95941 | -45.85068 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 390c954e-3e6d-3703-a14b-cdb77eac0346 | -8.01551 | -44.05377 | 2025-09-01 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e483f406-c7ac-38cc-9fdb-4f10d1b29c07 | -12.31133 | -45.68307 | 2025-09-01 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 139cee2b-6172-3e07-b800-4a91c8851f2d | -11.02111 | -46.94851 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe5d82cd-4e99-34cd-840e-145aca7ef4be | -12.60869 | -48.20557 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 415a95b4-f983-3de2-a86c-2fb89db5d1cb | -13.35739 | -44.62365 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57e6785a-46a1-3387-8006-d0bc725f7938 | -13.98843 | -44.53223 | 2025-09-01 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84464ad9-c92c-3711-8eb2-c9ad8be4f334 | -13.17188 | -45.28397 | 2025-09-01 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 92ae60c8-0601-3dc2-b043-4be670a3df3b | -11.80807 | -46.41816 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a200f1e8-4821-3171-9d87-fc833cb88170 | -11.87909 | -46.70097 | 2025-09-01 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 282bfb76-d1ed-355d-b815-ff6383ed720f | -11.80187 | -46.42083 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d09a8fc0-bc4a-3261-9852-e5db14cebfb9 | -8.19038 | -42.30462 | 2025-09-01 03:45:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5367bf62-0c4f-3895-b587-03a13f56c415 | -7.10772 | -45.34757 | 2025-09-01 03:45:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a0b83d7-4460-3ce2-aeba-bac41bdd754d | -11.01835 | -47.05482 | 2025-09-01 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dffe3b2e-43cc-3ee4-81be-696548c2d8c9 | -12.60263 | -48.20449 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4e2119a-fc73-305e-a26d-44c8c8e5ca0b | -13.71103 | -46.92759 | 2025-09-01 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82cbed39-bfba-3697-b144-a7b83b8baabc | -9.58024 | -46.00217 | 2025-09-01 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2476778-0d7d-34c3-bb17-471fcea75b7f | -12.59976 | -48.21852 | 2025-09-01 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f5ebe80-6f54-35b2-9aaf-961287e76d5c | -11.37571 | -43.62568 | 2025-09-01 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
