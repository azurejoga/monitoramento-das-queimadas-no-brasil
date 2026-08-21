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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50c261bf-4f8b-377b-bc59-c29572e96b82 | -15.7211 | -47.7827 | 2026-08-21 00:14:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 150549ad-618f-3584-b5f9-db2bf2e7893a | -9.4211 | -60.4048 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 327c0fa9-d73f-31f2-936e-c8197801530f | -6.2081 | -55.478802 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef211b0-c9a1-3f2d-ae28-5f9c60f3e918 | -15.0026 | -52.6731 | 2026-08-21 00:14:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d16c6e17-f828-3b8b-8388-dd86e6d0f36f | -4.1139 | -48.920399 | 2026-08-21 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2d5c653-66c8-3451-ab63-4093a31cc088 | -8.5689 | -54.785 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af456ce3-3250-3f76-a82e-90553d55db05 | -8.6859 | -47.486 | 2026-08-21 00:14:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7da0cc1c-e36b-3f6c-b250-2f99b7738d02 | -10.7467 | -50.3433 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1b1ba4a-3d8b-3a33-aff1-bf949d03061e | -14.58 | -53.001801 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 764b07ab-bcd7-33c7-9717-fdeadfa4d3a1 | -6.2159 | -55.4678 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94212072-1dad-3e71-90e7-a3c967b995b7 | -8.8972 | -60.509201 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59d9ed59-f3f0-3ff2-852c-5352e6f7f505 | -10.7713 | -50.315701 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e958fcc8-ef45-34ac-ac98-45b6913a3ac8 | -5.7245 | -53.705299 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd90ef1-1792-305e-bf07-e2ebe2646cf5 | -6.2374 | -55.613201 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82999587-556c-3483-b40a-17dc3c5029bc | -8.5749 | -54.7654 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9ad90d-ec5d-3c53-9ccc-c77bfb517c82 | -10.2516 | -54.367901 | 2026-08-21 00:14:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a71eaa57-e5af-343d-9666-c7d8dcbfc438 | -9.2086 | -59.749199 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 108321e8-84b0-3026-8bef-ced9c9ee6d78 | -4.941 | -55.781101 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f926aeb5-80f9-3722-8117-f5da67789098 | -10.2916 | -48.220001 | 2026-08-21 00:14:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18c275ef-9693-3963-8775-7ec9b2100fc2 | -6.2277 | -55.615299 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1da33396-1633-392b-8026-111f01531849 | -5.8631 | -57.471298 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e994b1e-b0bf-3094-ad84-ee5557849bb7 | -8.5455 | -54.771702 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b249351-c680-30a4-b8e2-9ff6ebfebb0a | -8.4444 | -46.943401 | 2026-08-21 00:14:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d551f59-11d8-3176-bd9d-13f169135d62 | -6.1071 | -57.844898 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 478f65df-26c0-3fba-98bc-3ce30e8aee69 | -10.309 | -50.274899 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52b6d0bc-bb5d-3214-90cd-2712e838dc18 | -9.4267 | -60.382099 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| babce8d2-f658-3e54-b716-d7badf96978e | -6.6915 | -58.911701 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d830a779-1dbb-3873-a1d3-2ee9779d361c | -18.7885 | -49.436001 | 2026-08-21 00:14:00 | METOP-B | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0e21129-1927-3b00-a912-cb5cdc14b7e8 | -11.1878 | -54.003101 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2a83dc3-1f67-38c3-bc81-ae6712488697 | -8.688 | -47.494801 | 2026-08-21 00:14:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f898ac56-7755-3dce-b5e2-298035576826 | -6.4378 | -52.705799 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be184e33-2564-3ada-82ab-f8d2d877b7c2 | -3.5386 | -48.168598 | 2026-08-21 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3088f6-0fce-3617-bdcc-76a8fdba8e63 | -15.7114 | -47.785099 | 2026-08-21 00:14:00 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 663697e0-b6d1-305c-a684-ff352aa1071b | -14.8977 | -44.7915 | 2026-08-21 00:14:00 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23836dc1-8f4a-35ef-9d0a-3a5bb42f320f | -6.9443 | -59.000702 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b945a1a0-6f82-3a14-baaa-5fe9bf2d24f8 | -14.3403 | -51.913601 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0dcb2ff-fd57-30e9-a913-e76d3ffc1c64 | -6.3864 | -54.9347 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d4550eb-12e5-3092-b04d-b4c7ec616730 | -8.9014 | -60.530102 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0116fa17-b8e2-38fe-9fa4-9cd74a681ef0 | -8.5541 | -55.287899 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7036e7-c4a9-3204-958b-a4d1ded1ace0 | -17.7237 | -44.2015 | 2026-08-21 00:14:00 | METOP-B | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 40c00be1-8a9f-3798-b575-c629a3e67bd1 | -9.2183 | -59.7472 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e766803-5dce-3904-a98f-ebf3458b9d0d | -11.2055 | -53.990299 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41ba1ff0-b76a-31c2-91db-d90994b3337b | -6.3981 | -54.941002 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5b3375-3282-3131-b11f-d6fb00d4489e | -7.7739 | -61.091202 | 2026-08-21 00:14:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3280830-2dbb-318d-b95b-4b93b8ba11c8 | -6.884 | -56.4212 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec82fdc-b25f-30d1-95c3-8f9e8e9b9c09 | -3.2112 | -50.915401 | 2026-08-21 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1364ee3-c6a4-3c63-abb3-76c82e7899b5 | -7.3373 | -55.6759 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7afbf2fd-c001-3cc0-8382-2d0693b5a582 | -10.3181 | -50.360901 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3af110f1-8590-3ac0-9ff9-f5a81d032a60 | -6.4291 | -52.7593 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4752c120-746c-3309-b77f-d383492a2b25 | -10.3106 | -50.281898 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ace9a6c8-3264-362e-9eee-d2ae32eecc70 | -18.0319 | -44.6138 | 2026-08-21 00:14:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57c98c9a-6095-3be7-9572-1880de9fef9a | -9.4114 | -60.4067 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97aff7af-2772-3a31-a79e-89f0bd9257ca | -16.2199 | -47.842999 | 2026-08-21 00:14:00 | METOP-B | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b9fb635-a36b-39b6-8d9f-49c4aaf93936 | -4.4524 | -55.381802 | 2026-08-21 00:14:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b9ebc5e-e127-3c1c-b5e9-ef774fc82350 | -10.7631 | -50.325001 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc14c79-a190-38c9-8769-9bd27dc103e6 | -7.3569 | -55.6717 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e8b9eb-c61f-310d-ba19-978bd336ca39 | -6.4391 | -54.9408 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb094024-d35c-3831-ab3f-6abeea537ed6 | -9.0591 | -57.0453 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6bbb21a-2803-3f6a-b3ee-e8fee3944fed | -8.5721 | -54.6572 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef2341a-659a-3378-aa4f-00817f7aab47 | -7.3535 | -45.825802 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f80eef0d-6726-33f6-8849-320ad7519d38 | -6.4374 | -52.750099 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fcc59d4-c2b0-36b1-857f-a4181fa0a3d8 | -8.5581 | -55.306499 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b71869fb-694e-3ea3-9fc4-21f7c2941a82 | -8.388 | -62.639099 | 2026-08-21 00:14:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7839b58-df66-3879-b692-991dff9c418d | -11.4795 | -45.1008 | 2026-08-21 00:14:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5cbb929b-6e6d-39a8-8114-ad28f7e3835f | -14.355 | -51.8386 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b6d343fc-8c74-3c3d-9bdd-7c0b00abcc6d | -7.6236 | -45.7486 | 2026-08-21 00:14:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e25a05e8-1b7f-3418-95ae-fedc4df9bcf8 | -11.1896 | -54.0117 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8533e018-c786-3967-8f51-1b6764a463f1 | -6.8664 | -59.016899 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a333312c-e4c9-35ff-a793-f8c8eb50192f | -6.8632 | -59.001701 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 107a23a2-652d-3605-8c55-36d998ee8174 | -8.1606 | -55.362499 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b3a6ce-0df7-357b-8513-827dcab66d40 | -13.6767 | -48.765202 | 2026-08-21 00:14:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 920a6e16-b2cb-3702-83e8-e676a759fc36 | -7.3411 | -45.8167 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f930866-49d5-3876-b0ac-5b27b5949aa4 | -9.2048 | -59.730598 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2e949d0-d08f-3a8c-a765-f6036450e242 | -16.719299 | -47.681198 | 2026-08-21 00:14:00 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13f4911b-8c04-3d10-8208-b890769fa728 | -10.2682 | -50.276901 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39f04e86-8009-3de1-8a20-dc3232c7a8e1 | -6.336 | -44.0812 | 2026-08-21 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cfba614-8287-31d7-838a-1daa66c73bda | -6.2514 | -55.395302 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a64b4ceb-eefe-3a6a-90d6-318752725c1d | -11.1798 | -54.013802 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97e232cc-b28c-323b-a8d0-dd12134cd738 | -9.2145 | -59.7286 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bad21209-eca7-385c-9e8d-5ba1fecfae7c | -4.9614 | -56.246899 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e643ff81-ce3e-3175-85c0-a5a5adac0c49 | -10.2399 | -54.361301 | 2026-08-21 00:14:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a20b0d27-b29e-3eac-9d0e-70b8ecc3af1b | -11.2023 | -55.0429 | 2026-08-21 00:14:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d07a9648-d284-3a77-b6de-e61457ec3156 | -12.4299 | -43.389599 | 2026-08-21 00:14:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbf69cc3-bf9a-3e84-8cc6-91e5f99893ce | -6.0973 | -57.847 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9034d7e3-e667-3086-a297-028eab97e07b | -18.203899 | -50.740501 | 2026-08-21 00:14:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e190bd71-4ffb-3851-a120-c3f0fc792971 | -12.4264 | -43.375702 | 2026-08-21 00:14:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb6f4e98-f1c3-3c9b-b3e9-d10b4cef4e7b | -5.6626 | -51.639099 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 854ebb66-1f94-3e1e-86b9-8169d17b5e88 | -12.7621 | -48.463902 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87a59bb1-a75f-38ee-ad2c-d67f70cbf842 | -3.9438 | -43.093601 | 2026-08-21 00:14:00 | METOP-B | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba8aa8ba-91c4-324f-a499-92855621736c | -12.521 | -54.753601 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62808663-b685-3bce-8209-077aa8c1be00 | -18.7031 | -47.4674 | 2026-08-21 00:14:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4f7266c-9142-34d0-8870-b520642be653 | -6.6713 | -52.876099 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0b07bc-0adf-3d56-8904-c741b963fd97 | -10.3212 | -50.374802 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22414a30-da2a-36f0-af8b-a9f36ffb2907 | -4.1855 | -49.410301 | 2026-08-21 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9cd108-b9cd-3eee-b66d-0597298f9222 | -5.8165 | -55.704201 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c66e9118-ba29-3ba9-b8db-2d3533e84795 | -6.4389 | -52.757198 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aece4614-eaa0-3663-b436-85126845b047 | -8.5572 | -54.778301 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7f82c8-a473-3eaf-b219-f1de605d2bb2 | -8.105 | -51.6479 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d01b4081-82fe-3d68-a2b7-351edae179dc | -6.7044 | -58.9245 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 179d89d1-50a8-34d8-9d97-1e303b508276 | -6.2257 | -55.465698 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
