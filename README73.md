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
| 1da2074c-40d9-30bb-b73f-8c4805b89992 | -12.79276 | -48.1888 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 561f7586-6f07-3fb4-8b35-49a0cf0ea74b | -10.46846 | -57.94661 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f24bcde8-aaad-3e28-a0c4-ac1c2c5d3f31 | -10.46287 | -57.95918 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6ecd68d2-b02a-3b14-9d16-d237201fc190 | -10.84005 | -60.8095 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 450dbe85-112f-3242-aaf9-7436dba40f1f | -8.68787 | -62.87376 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e08c07a9-b762-393a-95e7-b1556a94f4aa | -10.47882 | -57.95274 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4707a2e8-a624-34aa-9b1d-cce03ffead6a | -8.91015 | -60.71639 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b85312-d081-3bab-94e2-2ebcafed55c7 | -8.44511 | -70.14816 | 2025-08-28 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1bfe900-2c56-3040-8265-12fcd678f0ce | -10.80496 | -60.77125 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55f466e3-b452-35e0-8dc1-50aaf9881945 | -10.45878 | -59.12288 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67d728ce-b538-39b5-a823-4c3a8bc18e17 | -11.35791 | -63.2789 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fa30b1d-e04b-365e-884e-ea22e2c148fb | -9.55151 | -65.68925 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45acfcb7-8fe2-3fc1-90af-4f98f839a23d | -9.15647 | -59.56349 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2802454c-1cd6-39e6-b3ae-1abbed396e56 | -6.85351 | -55.11601 | 2025-08-28 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f20264-eb29-330b-ad96-e53c90940a79 | -7.54142 | -63.85906 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31ef439b-67a2-3c94-9575-f312552ab3bf | -9.40979 | -60.52204 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86f0cc61-3cce-3902-9b52-4a34954fa652 | -9.15758 | -59.53369 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c265d00a-c98c-39bb-8c68-5dbab7733eef | -9.48207 | -62.39482 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38558a28-bef4-3773-a42b-23b84206653a | -13.01365 | -56.8984 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74fbf400-e088-39da-a12d-fff2528ee17a | -13.13697 | -54.9246 | 2025-08-28 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb842459-c6ea-3701-a25d-bfb9756d259b | -9.41532 | -60.50848 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a02182d-a8b4-39b5-91ac-16b2e9847b1e | -9.15989 | -59.58643 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fef63c2-1d3b-3943-9325-22e480b69490 | -9.25219 | -65.89722 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d09ed8c-8442-3391-b98a-682d4ed1f49f | -9.47312 | -62.38595 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f823f00f-68be-3771-bdd1-51417be68ad6 | -9.79895 | -64.27424 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71ae67f9-2c0f-39b3-a274-154404775b57 | -10.49102 | -51.58609 | 2025-08-28 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 501b13db-2696-3a4a-81e2-9381c619401d | -13.37634 | -51.77315 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57588ced-f040-3e99-a2ab-ec962190fca8 | -9.41211 | -60.5729 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 87efecc3-592f-36e0-9330-fc5395726bf3 | -11.32877 | -63.28547 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e70ffc-cb87-31cd-9f7a-04b2773d7ebf | -8.89996 | -60.56412 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 165f9d9c-2957-3f1c-b16b-142dd4b9b82c | -9.15196 | -59.57026 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ab00ef1-569f-3ec3-93c5-cb0560d125e2 | -9.19681 | -59.64471 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17643f1a-8d53-3e7c-906d-dff16d3a63f3 | -9.41093 | -60.53665 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f45c303-8d91-3321-9b40-2a5b7913b8d2 | -11.35852 | -63.27517 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 132bfb01-ba72-3c81-99dd-0dc915215a1b | -8.87362 | -60.75357 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95f87457-826c-3304-ba49-95fcba608165 | -9.17404 | -59.60727 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 913a3c01-03bc-3caf-8d5c-c71a11d8a39d | -9.53746 | -62.39968 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4984347-574a-3999-b95c-2c86aa1fc8be | -9.21681 | -60.8082 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22d85b43-b357-31da-a509-8fb350c63635 | -9.01423 | -65.68832 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12df2a2-4a98-3252-a235-6cc41c9c5b25 | -9.16665 | -59.56512 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f814486-30bd-3fcd-a71e-90d12a797c02 | -13.3768 | -51.76902 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ef7b32e-fad3-3dd9-8d09-9efd70781f6e | -8.88082 | -60.75113 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa44701b-a5b3-30f2-b314-957d50a35f05 | -9.79372 | -64.23916 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c92f3bec-bdff-3aea-b24b-9b59d5d335db | -9.2036 | -59.64567 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdb5f434-9691-3a21-9fd6-389f88af5b5e | -8.56155 | -62.64338 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9b36472-8cc6-341e-9a92-cf89e7ed6461 | -6.24401 | -60.02805 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d69a4e7c-539f-34d3-941e-5a5e6c8ca4d4 | -10.79828 | -60.77018 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 878d98ea-ef41-37d6-a5aa-eebde1241621 | -9.1565 | -59.58591 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc7b643d-56dc-3679-838b-7ab67a875e6a | -11.22642 | -55.05263 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feccb6c7-d637-346c-be53-53a3f08fb2c6 | -10.47278 | -57.94278 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea622a54-b8b7-3ca6-9b4c-fa4a092d75ae | -11.36656 | -63.26888 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7533f5c4-34ee-3119-b813-ade5c7ea3433 | -9.53467 | -62.39553 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 810ba92d-2910-3c7f-801f-12bea7722cff | -9.4866 | -62.38817 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ce89e9a-d5a8-3371-be8a-13a14f2e126b | -8.70802 | -50.38081 | 2025-08-28 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ed97cda-b257-36ec-b268-63a005f2e62f | -9.40033 | -60.51693 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63e8aff0-1f7e-33c3-9ecc-8c222800586d | -7.37472 | -64.36514 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c7251750-bc96-31b8-be3f-b23f0a1f4bca | -9.1528 | -62.35614 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1a28eef-934a-3827-b5a0-82ae2adc11e1 | -7.54524 | -63.83487 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57f54a20-1bfc-3ead-bf7f-58de9dc6b5d0 | -10.46415 | -57.95045 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0294cb4-068c-34bb-a9d5-2bec92d3523d | -10.93742 | -63.63207 | 2025-08-28 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bb315cc-ee4e-311a-ad6c-cbf2b8062d41 | -9.54349 | -68.58014 | 2025-08-28 05:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df807992-7efc-3288-8699-d1e38ab4a739 | -8.96629 | -61.66539 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30b934e7-9f11-3d3c-9027-77252be79019 | -10.25746 | -64.50224 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 336236be-7a0f-3294-83dc-864edd8968a7 | -9.25778 | -65.89996 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a6ce11d7-6296-335c-a0ac-dc329ae6cf4a | -9.36546 | -61.53512 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f585e1-15e6-39d2-8822-eb94d6212296 | -9.18633 | -60.80688 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0353987-f47e-37d5-b1be-17a3a79b9277 | -9.64625 | -59.6236 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 374a95d9-bab9-3db1-b08d-1e38782e2865 | -6.0113 | -57.84901 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 111ce9af-40e8-356d-a1ff-b75ad1711e83 | -10.31917 | -62.61971 | 2025-08-28 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| afa9ccd3-9585-384e-856a-e4b83a775351 | -9.1268 | -65.78321 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bb02f862-d183-3785-8664-d403f3890cbf | -9.53629 | -62.40691 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 132638c2-f225-3304-964e-0fd9c001efea | -8.97743 | -63.10927 | 2025-08-28 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 264c7bf7-9f2d-3f18-add9-ab5868509571 | -9.28279 | -68.26044 | 2025-08-28 05:25:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab821c73-d989-3aca-a3ad-a89e87d13a73 | -9.40531 | -60.50689 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5668ced8-1b81-3609-a420-fa1dce0ed4d7 | -9.40536 | -60.52855 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bcc8f2f-c45f-356d-8e48-e6bd8ee949d2 | -7.47435 | -59.9054 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dab1e3c-b072-37a9-818b-23628833bd28 | -9.3191 | -57.69965 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22517ee2-684d-345f-b340-71f39e2a8702 | -10.37436 | -62.56156 | 2025-08-28 05:25:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d806f668-0831-3aab-b3eb-59e16973a2d2 | -8.34357 | -62.94601 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eace8bbf-71c6-3a6b-ad5f-a9df94ff8f51 | -9.20077 | -60.2873 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 820b2a61-5062-347d-9de5-000be8c4f08e | -7.44806 | -63.16386 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2281c944-e1a6-3ac0-bfd6-e9b9f56163e5 | -8.90106 | -60.55711 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49f44456-e01d-3221-a73c-e1b21ab5bf1d | -7.54094 | -63.83844 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97cd9e0f-834e-35a6-8818-ee40b2d466ae | -9.54083 | -62.40024 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf79a37b-9b40-392e-8362-087f39ebf5c2 | -9.22959 | -60.91767 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0713ce5a-fcf2-385d-b03b-72af0bfd0a67 | -8.56403 | -64.21951 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b8e7082-e224-3e7b-bc8b-6314678ea8dc | -7.27729 | -60.29747 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecd7d98a-7d59-39fe-8da1-9725897d6f2d | -9.4176 | -60.53771 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cad3d76-1b17-3a32-8249-88bb2f7fbced | -9.41308 | -60.50091 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 965e8661-546b-31d2-883c-f8bf0685e928 | -8.95336 | -65.94703 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b44eca3d-689a-380e-b73b-29f36bc8b155 | -9.4737 | -62.38235 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c71be36b-7dbf-3671-a84a-aa19a81a29d9 | -12.86937 | -48.11659 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33a052db-f911-3722-9dc6-5682a3fb2abc | -7.3507 | -57.62912 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80b41192-8723-33f4-aeda-e4778f15e970 | -9.53804 | -62.39608 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee1d016b-e032-35b7-97f3-101943811118 | -8.95835 | -65.96597 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 05792ffd-c65d-362f-81f4-91726df9b72c | -9.55779 | -55.38536 | 2025-08-28 05:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6de0fc5-109d-3c0b-94da-e08f9b00f3ca | -12.80712 | -48.16314 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97798ff5-e237-3a5e-9388-b16d88b9149c | -8.88877 | -62.47762 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae62e477-4278-3b94-87be-7f40aeee7f45 | -9.03578 | -65.72863 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9120bc24-c19d-32fe-81cb-9572ddae9ecf | -7.37845 | -64.36577 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
