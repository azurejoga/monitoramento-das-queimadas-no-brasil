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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dc84387-c9ba-356f-b9aa-ac99ff943925 | -10.73524 | -47.96284 | 2026-08-31 05:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| def91a06-73ae-3715-91f0-aede9c2e3c78 | -7.48798 | -61.40126 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f74bb51-673d-3a70-ac5f-2d3c06e0f129 | -9.17591 | -59.61778 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2786448-38c2-3559-b99e-dc5db1259aa6 | -7.33077 | -60.59821 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 605fe506-63dc-3805-b211-16786ac6bcc6 | -7.55774 | -61.32285 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fcda814-efae-36b8-93c1-bf787e1796c1 | -7.44023 | -61.42226 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fe945ab-d24e-34a0-ba10-04680579bc59 | -8.21289 | -54.94503 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12c2999d-acee-33f5-b8a4-7d1388c7125b | -6.88513 | -59.45047 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59a3c278-4031-3b73-beb5-7efd4139bee1 | -6.82689 | -59.41985 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ac2dce1-2ab8-36bc-9767-0ab13194b5f2 | -7.51538 | -55.27789 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| deec7230-419f-39fb-b094-1b62c6f958bb | -8.21228 | -54.94925 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06f9d520-7c36-3ef5-9265-cfebb253891c | -6.857 | -59.43136 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3767ee6-90f3-35c4-be56-98a64fb39183 | -9.17024 | -59.60934 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e56a5ec6-28ac-386d-83ad-2f078de2c4ca | -7.58157 | -61.34456 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9c3e580-9396-33fd-ac16-0fee363f2149 | -8.09415 | -63.83991 | 2026-08-31 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e332490-8589-3783-ba72-51a2c669ba67 | -9.15211 | -59.50055 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea267f34-2469-3073-b761-a81e4cdb14c9 | -7.57602 | -61.35799 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d05836-9576-332b-a6cd-b5ace96ab803 | -9.17304 | -59.63617 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 955a7c4d-9dd6-3cc4-a2d6-a57ea509abf8 | -6.90706 | -59.48695 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b04c7876-485b-3598-8dd3-de7ad07681e5 | -7.33464 | -60.59526 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30079dbe-05e0-3f75-89cc-999b53c50504 | -7.25471 | -60.63266 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b67f538f-5648-367a-a853-04e35c398147 | -7.30473 | -60.59051 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 050bf4b3-174c-3f89-8a0d-381ea0305ecc | -7.21822 | -60.66962 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45beb0ed-f90b-333c-b123-b6e84a5b9634 | -6.90163 | -63.06165 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3d8e861-a5af-3ffc-b0eb-d0f826a734aa | -7.40441 | -60.58492 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c813cd9a-bc61-3e28-ae88-6f297e1206ab | -7.40163 | -60.58092 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94c99920-6512-39d2-a2bb-0af94365361a | -7.61638 | -55.29532 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb672803-c5b5-304d-a107-b6d73df22331 | -7.5788 | -61.34053 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c54337-2f6b-3472-a5ba-e3c6ff4e9b6d | -7.58601 | -61.33811 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 873d3033-4ae0-3cca-8bad-3b60fced1a69 | -8.21786 | -54.94134 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e53b4ea-5c0e-34dd-ba6d-654f371fb3f7 | -7.33906 | -60.58883 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e39a11eb-dbc1-385a-819c-0e8ce56e2fb8 | -8.21852 | -54.93675 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5567834c-e9ae-305b-8116-e8fdb38676cb | -6.88848 | -59.40681 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbadd84d-ad8b-3080-abb7-5d06d618be84 | -6.8851 | -59.40628 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4212f91-9eaa-3885-92c8-2720038352cc | -9.16415 | -59.37647 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a13521e-76ff-3323-b2e5-2922150c2ce2 | -9.16463 | -59.51011 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6b57bdb-cc01-3017-ae53-8e14b0c24edd | -7.31302 | -60.58113 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e1e80df2-35bb-3bb7-95e7-6cf5e993f75a | -8.61455 | -54.79112 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7943d2f4-50f5-3d7e-9888-6a4bce48084a | -7.28186 | -60.65478 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3144a21-ce12-36e1-94cb-0199183bcb3a | -9.15323 | -59.53868 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39c4dd4e-2d81-3f41-95f9-d60da14a0aac | -7.69884 | -63.32735 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 577aa724-9872-3d99-ab1d-5346c63c62de | -7.76237 | -61.20541 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f94ae67-dbad-3e8a-b28a-9ac2decbf79c | -7.79249 | -61.58612 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1f2cb5d-325f-39e8-92d3-8707617cac9a | -9.00818 | -60.602 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11ed2436-00b3-3513-beba-ffde6e4cdbb2 | -6.8475 | -58.97585 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbb054e1-06a8-34f9-8ccf-4718639d5500 | -7.21932 | -60.66267 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c3bdd8d-0efe-316b-be40-26d0550d5f71 | -6.88176 | -59.44993 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bad6664-ab89-361d-adf7-93cd78f74716 | -7.57383 | -61.30754 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5bce336-c32d-3dc0-a929-8c2e8b73ceb5 | -9.15837 | -59.50533 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d277a9ac-ac3f-3365-a1f9-b1dbd6cae109 | -7.27909 | -60.65078 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2451f126-f7be-3166-b9ed-eabc6c176396 | -7.44245 | -61.4298 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac4580c-dce8-3a90-b57b-c4dfcb113f7d | -7.50455 | -63.65245 | 2026-08-31 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91d81203-e50d-3a17-b63f-da1154cb2f2d | -7.34461 | -60.59684 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 609a38c5-8bfd-3fbe-8349-00ae552852d7 | -7.30915 | -60.58408 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6483cbc8-fbfc-3279-a975-87921d8a87f0 | -8.71407 | -52.36508 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7f5c80e-0388-30aa-8a9a-d0e36cff68a4 | -7.5583 | -61.31936 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65b6f6ba-8cff-3315-8fd2-0e732306db3e | -8.40406 | -62.66335 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8cb3962-ed78-315a-b89b-0ea91992b502 | -7.33409 | -60.59874 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90f93240-2f93-347b-aa63-ecf9acbd0dc9 | -6.90099 | -63.06551 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76e6c5f6-a83d-3f0c-8602-d9d99a4a5385 | -9.15614 | -59.3829 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b49f97-b0ff-3f4a-a8e2-4b1507f3d25c | -7.78972 | -61.58208 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c409d938-d375-34de-9e8d-c23559bc0226 | -8.65758 | -62.82052 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a02f6d99-b0d9-3a9a-8074-7081ca265856 | -7.31192 | -60.58809 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3b9d02-b2da-3d7b-a2f2-d48b69a8da1e | -9.41168 | -51.68781 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22d63c94-ae68-30e0-adbd-aa04b3f54660 | -7.92538 | -61.3314 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a833e65-5677-3733-a72b-b918fc3423f6 | -7.96053 | -52.44483 | 2026-08-31 05:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0c39378-3399-3a64-a64b-daf8d72ed8d7 | -7.31525 | -60.58862 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80174a2a-23c9-3baf-8a4d-c3af62677cec | -9.15266 | -59.54236 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1545f6a9-fc90-32a1-963a-e04ec8aeaef5 | -6.80384 | -59.45667 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61a90faa-7d88-398f-85aa-b23d1718242a | -6.86044 | -59.47598 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa1c4e1a-0a56-31df-81f4-b0f539b70051 | -9.1613 | -59.37217 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 511834de-d630-36f7-8cd5-be6a4837713c | -7.29564 | -60.58925 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f721fbaf-5609-3f5f-861c-d5f794c19540 | -8.62137 | -54.69174 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5cfcdff-0b61-3b02-b226-ef69a44e4a8c | -6.86436 | -59.47293 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ff48b8a-db94-32cc-a0c7-16111d9d8766 | -7.33132 | -60.59473 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0fad9b00-3dc4-3188-9f1c-17c6380dbc58 | -9.15379 | -59.5577 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31ecf262-bc87-3292-87ec-0d72990fd989 | -7.81045 | -63.26139 | 2026-08-31 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33e45582-7b1d-3991-be45-46d3f17dfd3e | -7.30696 | -60.598 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7044a96-7bdb-3cef-9b80-0f6f04fce936 | -6.91099 | -59.48391 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 379a44f0-1411-3956-9b1f-fcb4a62b76b2 | -8.2586 | -62.76052 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a20d98-f110-3377-a0de-14975046b3e6 | -6.97772 | -59.59659 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d86f0a1-5ec2-3aaa-b91a-0883d26b4867 | -7.34128 | -60.59631 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f44ce5ab-bb09-3701-ab97-adaa75dfc7d1 | -8.21354 | -54.94052 | 2026-08-31 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc52ff8a-9451-3633-b1f0-6686f302a9f0 | -7.33796 | -60.59579 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb5d01f-8d3d-3722-ac2e-958c75204995 | -7.56495 | -61.32043 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 066cd185-fa8a-346f-9639-7664e2434926 | -9.15265 | -59.56509 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f88201d-d1e9-3c2b-8d00-dfd7ae6f4cfa | -6.66785 | -60.12621 | 2026-08-31 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89cd1390-447f-3739-99b6-65b4c1db81a6 | -6.86576 | -58.94842 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c7c43dc-a1ff-35f7-942e-19c423dd5750 | -6.98165 | -59.59353 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc3ff7d3-71d0-3c74-a43f-ad41671b24f9 | -7.44634 | -61.42683 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1255c19-85f4-3364-bdb1-8f83e8b05356 | -7.51481 | -55.28175 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8195cb98-9d6e-3925-9f66-203d002f15f8 | -7.60909 | -55.28632 | 2026-08-31 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb485fbb-7bec-3334-bf83-17fb18a772a8 | -7.31357 | -60.57766 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fed1eb1b-b14f-3a78-a3be-9035128c2821 | -7.61038 | -61.37058 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ed8a05c8-ceb1-3b2a-b10c-fe9910ceef0e | -7.33851 | -60.59231 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b39f0e42-c5bf-3d41-a707-135738cc24f6 | -9.1555 | -59.5466 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 321a4bdd-e751-323c-8adc-e6c419498519 | -7.33186 | -60.59125 | 2026-08-31 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef482a6c-23fe-318f-ab11-51b36bbba7a9 | -9.15671 | -59.37915 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf4180f1-9ee4-3fbf-81a0-031a4ed8e481 | -9.67064 | -47.93953 | 2026-08-31 05:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98c79a22-d336-334d-9094-7716af6b99d5 | -7.56162 | -61.31989 | 2026-08-31 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README68.md)
