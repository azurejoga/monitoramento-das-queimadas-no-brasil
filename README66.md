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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc7ef5ba-f178-3b99-8d90-1d9ddc4e2aad | -6.78437 | -55.67128 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddbc9112-1072-3b94-ab37-db11723233e7 | -9.16535 | -59.50841 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62db0107-766c-3c5d-90ec-a96b0ec62cee | -4.35889 | -55.02716 | 2026-08-30 05:53:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 650a1add-19c1-3ff8-8981-5369e36955b9 | -8.18477 | -54.93631 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c3dbbfe-cc0b-376c-94af-fcd48476e42c | -8.61189 | -54.77314 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a56a0d2-2091-384d-9f84-3116331be869 | -3.25992 | -60.65799 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbfeafe8-5d2d-3fc3-a7a9-55f0e5be8704 | -7.56215 | -61.32273 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37932c8a-9c71-37d1-b455-ccb4a62f6eef | -4.0835 | -54.11196 | 2026-08-30 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7df11cbc-bab2-3f88-9c34-60e7c09a3e6e | 2.23974 | -50.75465 | 2026-08-30 05:53:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1452caba-5812-33ae-aaff-7ec5b45ce39c | -7.3035 | -60.61451 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47c73227-3ffc-3e30-bc84-be2f599924e0 | -6.93005 | -55.70215 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb0989a9-f6ee-30d7-aec0-25d9aed5f100 | -8.58379 | -66.95394 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9822dabe-0713-32d4-9fb9-5108f9380f5a | -7.30959 | -60.60103 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0349304a-d68c-38d7-8f8a-34f658ac8ea3 | -8.96179 | -62.40155 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 798d5243-d445-3202-9fd5-1a1b9cfeaa26 | -9.01487 | -65.40137 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cabafd5-35d9-349c-bed5-397dfb838c24 | -9.01847 | -57.54311 | 2026-08-30 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a27d040-21c0-3ee8-a964-aebbdf43a424 | -8.63076 | -66.54395 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3046f2d3-ca78-352d-be7b-6debc977c88d | -7.55657 | -61.30699 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09e37850-1b81-3bd5-bf04-52684c983604 | 0.13793 | -60.40215 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce9ead47-717f-357f-924a-46b3c68510f1 | -6.94799 | -58.95899 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0fa5045-c8e2-32dc-994f-3f07ccb0906b | -7.32876 | -60.61103 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 998c89eb-9256-332b-a08e-90ba0a42f1ed | -8.93287 | -62.40388 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 857ef0a7-66ab-3e24-bb3b-d491b62937f4 | 0.58007 | -60.44695 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 286dc861-1c21-3836-aeae-88ca3af0bc96 | -7.30555 | -60.60042 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 074541d4-7f75-3807-8f0a-4ecb33bc1e2c | -7.40313 | -60.58213 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 604f8e80-22d9-3282-9aae-ca557747d2cf | -6.7905 | -55.66845 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b86013c7-c22b-3586-8e41-bf1642a70ecf | -9.15407 | -59.50457 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1433694b-5cc6-325e-9916-d61eca6f8181 | -6.93975 | -55.71476 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b016a16-8ed6-3787-8ef6-801ec9a56ab1 | -9.04593 | -65.43479 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6aed24fa-afda-3046-a05a-f24953752866 | -8.67228 | -66.51136 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82108c17-1917-3e10-be2c-91ff91ea84df | -7.23849 | -60.63048 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 056c755c-25ec-364b-a7e9-a5f19e0da401 | -9.89175 | -60.28415 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 24002b47-e832-3d12-80da-c76b8c87e2fc | -8.57766 | -66.94927 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ffd52b7-0a9f-304a-a56e-71769ed9bea4 | -1.24633 | -55.70509 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30b5571b-3f2e-3877-9bbe-e926fbefddaa | -8.60723 | -54.80798 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831ba703-8179-3bf9-9f39-4129bd4422c9 | -9.09206 | -65.4889 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfe16ce2-e663-38d4-bcf4-a7da79bfdec2 | -6.94483 | -55.71939 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87765dcb-6f3d-3102-9231-9e4b4c8980fd | -9.07165 | -60.48853 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7684b39-a165-397d-835a-efbe5073dd22 | -9.89234 | -60.28007 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| de5d3d6b-ccb4-38d7-834e-25c0433dd8f3 | -8.49861 | -55.30465 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f76d896-1c89-39cf-9c98-77e9c5181d56 | -8.25868 | -62.75574 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e72d910-9d0b-3d0d-8eba-d8cc399ea6c7 | -8.2293 | -61.42481 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34ba1ffd-aad1-3730-b1e6-103e19ff7693 | -7.26372 | -60.62702 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 123addda-f7cd-34cd-a4f6-6a10343bdbbd | -9.00435 | -65.44648 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7b9fdfa-50ef-3acc-a76e-8af7be45b67e | -8.96115 | -62.40596 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16298fe0-e4a0-3cdd-af36-9b8c2597de67 | -6.72351 | -58.7086 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e916857a-550b-366d-9fef-229f09f1c526 | -6.71056 | -58.56933 | 2026-08-30 05:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a506bf-3490-3257-b429-425846ec64de | -8.94493 | -62.37422 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f47aafef-3a13-346c-80b7-de9ab9f65dce | -8.25807 | -62.75986 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d44feab-cc1f-3736-9d40-17f1996f9023 | -9.05479 | -65.42179 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2f6089a2-b5b0-3c35-a544-7093ce5110f0 | -7.00844 | -59.65199 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc1e1a8d-c312-3069-870c-dcdc37056b8f | -9.16345 | -58.31083 | 2026-08-30 05:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7794c8a7-e6bd-3dba-bb1e-60228b687016 | -9.8978 | -60.27251 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 18ad49b0-924a-3e71-910e-9bcd7fa455ba | -6.78944 | -55.67587 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 625ac720-7d3e-38f5-85a4-b53ad0e00850 | -7.59407 | -61.34728 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b763ea25-f825-3966-b217-9de6206fa6db | -9.84952 | -60.27373 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc0a6ce4-08b6-3782-8a4b-fe290b52a06c | -6.93923 | -55.71858 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62bdd63c-21c7-314c-b8b5-f5afe20dcb01 | -3.19914 | -61.16593 | 2026-08-30 05:53:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce803049-8783-3c7c-b220-412479818c6f | -6.72427 | -60.014 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d1ab35c-fdbe-34bf-8987-7c69cfbec0f4 | -6.78565 | -55.6849 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbb96c08-1f17-320f-ad56-b0f957d3746e | -7.559 | -61.3173 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6d04ad2-0170-3a1d-8b52-30a9eabc4c86 | -9.0049 | -65.44297 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef29f4f0-e683-3787-86c9-e8867510eb25 | -9.7091 | -60.74718 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 351573d0-16bc-3acb-96ee-880e64d5a148 | -8.6537 | -62.84501 | 2026-08-30 05:53:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6aa6ee2-4559-350f-8294-1a7008b011fc | -9.22459 | -59.76144 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b798e5-327a-310d-bc73-6ade37102e7a | -7.55548 | -61.41996 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7be43206-cdf5-313b-a660-51a3e433f55a | -7.01387 | -59.64463 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 906dc3b9-95af-3dbe-81b2-cd4369b3dcfe | -8.58715 | -66.95448 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbc7063b-e2d0-3517-a15c-111dd8254fbc | -8.24953 | -62.75937 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbb0506a-180f-3711-ad06-a62698fa293c | -10.73656 | -54.04327 | 2026-08-30 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 918d3e45-11e9-36b2-9dd3-1e314e58f98b | -8.94798 | -62.37918 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a33bab77-eb90-3bba-b84a-2bc6d3c4d071 | -8.50616 | -55.29294 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd4bc59d-b40f-33f9-802e-c56e07d5f167 | -9.21969 | -59.75974 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a2f378-2c9e-3319-85ba-eea616a7eeb3 | -9.07554 | -64.25144 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de33c8c7-e6d0-3315-a000-b4801748d4ce | -7.24251 | -60.63113 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e2250ef-ed33-3093-bd52-de6382672aac | -6.72012 | -60.01329 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1cba7e92-a387-3bbf-b807-c90d106b9993 | -6.93451 | -58.95712 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7c166ea-18a0-30db-86a8-189789dacfb3 | -6.91081 | -59.48996 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d533e0f7-5415-313b-9052-eda105c0624f | -9.06819 | -65.4887 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6891b85f-38f1-3cec-85aa-da5e9a49c808 | -8.60545 | -54.77343 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a1696a4-5d9c-3174-9fc4-899d520dc46b | -9.05201 | -65.41775 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff635144-b6ce-3ec4-af7f-ea4f4ce109b7 | -9.88688 | -60.28759 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 120ab988-b58a-3307-8611-cd641538a7db | -9.17422 | -59.60844 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab787f07-7b97-3648-8c98-c9a94ba2cc90 | -7.56045 | -61.30759 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb5d0b91-3376-3140-80aa-f8608d55f319 | -7.5636 | -61.31301 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 072c78ad-5e48-352f-87f5-a6bae142757f | -7.24356 | -60.62411 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e2f3c5d3-d0d9-3365-b743-1335f331d7a3 | -7.29799 | -60.59569 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14d2c078-7ae9-3463-87f5-7c447d264099 | -4.09008 | -54.10868 | 2026-08-30 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dccc78e-068a-35c4-a866-07b739e8d4be | -9.05589 | -65.41476 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f07d2b48-1585-3281-87ba-59bd85f027c7 | -8.50559 | -55.29721 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfb377e5-fd8b-3e0f-9ba8-1a09b9668fb1 | -9.71074 | -60.73587 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513347e2-9bf7-328a-bce8-15c5241ba603 | -9.15195 | -59.50644 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43389956-bf8b-3c29-9684-2c43e91b7f1e | -9.15031 | -61.09266 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4a127df-5f5c-3db3-959b-ce0034c0b9da | -6.86316 | -59.4762 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e6d5c997-f905-3adb-9fa6-dbfb39835dbb | -7.30254 | -60.59278 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 978def8b-c128-3042-89ec-f8bbdb6aa140 | -8.61065 | -54.78237 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb02f831-69c8-36de-814d-e6c5e48e64e3 | -9.00601 | -65.43596 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79925f29-a2b5-3c17-b931-232accb0befc | -9.65381 | -58.94218 | 2026-08-30 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4fd58ee-8d46-3476-af1d-098e839aa88a | -9.89292 | -60.27599 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e5fae825-050a-329f-bc0e-6f8d32d6f94e | -7.58392 | -61.33591 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README67.md)
