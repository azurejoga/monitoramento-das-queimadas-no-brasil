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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 625f8c49-1ea0-3f7d-99c6-d04c62916926 | -2.94055 | -50.46804 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eaf4a7e7-27ce-3e26-b745-f7e4eb48f0f5 | -5.67716 | -50.09895 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39762438-ad02-3e26-81d8-10df2b8170ef | -2.61031 | -51.21566 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f27803dd-611c-3afb-93b2-7c1a00c3c486 | -3.95808 | -59.36384 | 2026-09-09 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e56670d-4c21-36f8-8000-ec0a04cd69dc | -4.4337 | -54.83654 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dea4116b-9499-35b3-aa9c-28edcf113fcf | -2.93881 | -50.47893 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d3a855b7-3dfd-3da0-9fa9-a686cc7890c8 | -4.10876 | -49.06372 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4530b319-d07a-34b2-ad1c-b3c7f87f4f2d | -2.93203 | -50.47784 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18fa1ca6-fe94-3d25-8517-88215b037381 | -3.55079 | -54.69753 | 2026-09-09 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a019a9f3-2462-3eeb-ab60-b04b7a30d917 | -4.80615 | -56.13697 | 2026-09-09 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4714b1e5-c291-3902-836b-16a549b08dbe | -2.93377 | -50.46696 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91791ee5-471f-3325-844d-8eb38e72bc80 | -3.54593 | -48.17493 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 513b813b-91dd-3bdd-a3c0-6fb00be96ff6 | -6.25401 | -47.34393 | 2026-09-09 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3df9602a-dd2d-3cba-8544-a78741b4f886 | -3.85405 | -54.30306 | 2026-09-09 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48457ef6-d46c-3eee-8179-ab72275440b7 | -3.96758 | -47.58746 | 2026-09-09 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ab1eabd-460c-3dd5-bfc0-2c0e05177e6c | -6.16613 | -44.64983 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5b03606c-8c33-3e13-868d-9ef59dfc8797 | -2.05219 | -54.48099 | 2026-09-09 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211fff06-b2bd-3e48-8ec0-3a923a43d126 | -1.19191 | -55.72257 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 75c1a716-e926-3e18-bcc3-79d029a98d12 | -6.16403 | -44.66375 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2eb5174a-6392-3a6d-8c39-1bbcddbe16ac | -3.95441 | -49.00787 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb7b23f0-2453-3446-aea4-b85265d9f788 | -3.44309 | -49.70479 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41d20908-a435-3b66-b196-dd5bb7c5750e | -5.38002 | -49.1659 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1d33447-d608-34db-9fd0-aebb6d66db62 | 1.8234 | -50.95345 | 2026-09-09 04:44:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5388b74e-93e3-35e4-aa8b-683f263792ee | -3.26702 | -50.08705 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 941f79c9-f4c3-30d5-bca6-9bafb88bf2fe | -4.49614 | -55.49745 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec6ecfa2-4f20-3ae5-97f0-dfbad472f428 | -3.65167 | -40.34195 | 2026-09-09 04:44:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 72a6e179-095b-3c7b-bdf6-b2fc0684cbea | -3.6512 | -40.34509 | 2026-09-09 04:44:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60295010-9420-3b44-a20c-e9b82222ff3e | -3.23926 | -47.25017 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e3a4811-89f3-36e4-92af-e9a6c7306e4b | -6.36188 | -43.59165 | 2026-09-09 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 672b5d90-a815-336f-b52b-3765c57c46eb | -5.41542 | -44.79271 | 2026-09-09 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5565d316-4a59-3c78-8dfe-cfb000776d6e | -4.38181 | -55.04533 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c5dc00d-6551-305d-b4bd-5be2733d1888 | -3.75965 | -49.10027 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce635b7f-bae4-37b0-96a7-4ecd9ffcaa62 | -6.41528 | -43.07069 | 2026-09-09 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0870fd5a-0b64-34b4-b4fc-499774a6f2eb | -4.98813 | -50.64578 | 2026-09-09 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d9cec56-dda2-32ab-8697-795bf701af6e | -5.79727 | -50.1969 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dd907b0-6313-31d5-a056-804cbf7a7eef | -6.16508 | -44.6568 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0a93a47-605d-337b-9565-5efc18d140e8 | -1.03339 | -53.73075 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d2ca3f2-c5a0-3b95-8b3c-9f96b46e993c | -1.0323 | -53.73759 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16f346f5-1392-3c5d-a45e-dd7c374ffc21 | -5.71805 | -46.19518 | 2026-09-09 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f672279-f39b-395f-ad2d-87484f86a4b8 | -4.77206 | -48.06577 | 2026-09-09 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bb53b13-f276-383e-81de-70ca0b8c76a2 | -5.76988 | -45.07166 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ae7f1127-0253-36ae-b904-ad16a2fba61e | -0.92922 | -47.18888 | 2026-09-09 04:44:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 915ea08b-3b86-319c-81fc-99d6dba822d2 | -3.55384 | -58.5563 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f397fa9e-7012-3812-b743-9f8abc7f71c1 | -3.86873 | -47.10055 | 2026-09-09 04:44:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2b99897-651d-3ace-bd37-7622e9a2e1b3 | -3.55869 | -58.56094 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f473c9af-fae1-3aa7-b923-5d2c4b41cec8 | -6.36622 | -43.59217 | 2026-09-09 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7853c5c2-4ad2-36bb-a84d-92124a86827b | -3.89275 | -59.60804 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e02e5e8-95e2-3305-a592-cd0a54d318f2 | -4.66813 | -55.62989 | 2026-09-09 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03247bdf-86a2-38a8-a582-8ec789fcd0d8 | -4.56076 | -47.76324 | 2026-09-09 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1313cf3a-43ad-3a52-a888-110103ef7795 | -4.29587 | -49.08292 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bdffa3e-876b-3539-a0e6-760bf792ad9d | -3.76207 | -50.4566 | 2026-09-09 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bce9be4-b727-3c7e-9012-01e72b4c3351 | -11.54044 | -44.89443 | 2026-09-09 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91c1e76a-0aaf-38a9-a126-ef6b65ffb149 | -8.74261 | -62.40236 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74499723-07be-39b3-9bb3-01a102398e21 | -10.73706 | -46.01223 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24b24479-c0c2-3ddd-a7b2-42ec07ff55b1 | -5.82513 | -53.80062 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3752f29-838d-3c20-82c0-8cc21d787e55 | -9.69233 | -43.49563 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e6a72c06-e7a0-325c-9e91-33574b7f57ff | -5.81588 | -53.80896 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68f020e4-7ce1-3b6a-bad7-014f1f3d53c7 | -8.98085 | -60.58542 | 2026-09-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05c8352c-10b1-3cf6-848d-09c674159184 | -8.09477 | -45.67949 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f536ee6c-970c-375a-8349-6a49d951ee61 | -5.80199 | -53.82133 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 87e53d9c-8c59-336c-aa1f-914ad2bb30a1 | -10.71558 | -46.05 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e30685d9-d519-3ff3-8c74-e6459b752d58 | -6.77057 | -58.95974 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f967ee-1416-384a-a1e2-ecffe159bc03 | -7.19725 | -43.61548 | 2026-09-09 04:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3aed844-c537-3602-87cb-394d96698e04 | -7.08046 | -59.82434 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 697c45e4-79f8-351a-bcba-5321896bc651 | -8.72768 | -62.41059 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b261ad19-aaa9-3f55-980f-865d99780855 | -5.80741 | -53.81241 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9de735c-b3a6-3827-b238-8977472ee632 | -7.68403 | -44.32674 | 2026-09-09 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bc9e309-6934-3ac7-8e3d-cf8447088b09 | -6.2459 | -51.67696 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35a26100-fda6-3a4d-9a73-720b92ccd552 | -6.24307 | -51.67263 | 2026-09-09 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e155fe-df32-39fb-9dda-a75f722d1c39 | -9.70129 | -43.46347 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1790784-04a3-33e6-b053-339ebbdfe9e3 | -9.71899 | -43.47057 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb0bf322-5352-3534-8cb1-c05f0a0c652a | -9.75042 | -43.51338 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9167f076-2951-3bfb-a3a6-5ed52abcf6aa | -9.70241 | -43.42002 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e6cbc93-c8ae-3c7d-8f79-6d8af0fa6769 | -6.79674 | -58.95435 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aee1ac9a-a379-3e27-966a-e7d461d516af | -9.02237 | -46.60704 | 2026-09-09 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 865d00a1-711f-3d6e-9180-f804894ec0c7 | -8.98549 | -60.58434 | 2026-09-09 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7b2d87-35e5-3412-8c47-306db8c3dc2d | -8.0955 | -45.67463 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 208e9814-860e-36b4-9c01-8decfd88a4a6 | -11.00208 | -45.07982 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 64c648da-7bc0-3008-8eaf-cc007e9a3595 | -9.70025 | -43.47062 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 49757eeb-7062-3647-861a-ab39fd5d5b22 | -5.82129 | -53.8 | 2026-09-09 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35ec4a87-6066-3a4c-85f7-43bb20033444 | -10.93927 | -48.3145 | 2026-09-09 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 686d5ce4-67c3-338f-814c-7dc18eab43f4 | -6.39524 | -55.24511 | 2026-09-09 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae3e29b1-a3c3-3686-b9a7-342795b236bd | -9.69296 | -43.49094 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc094c7e-6196-3330-8756-179fbf6d8d83 | -11.00154 | -45.08374 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b2259b9d-34c1-31a1-86a4-a997141552ee | -6.63318 | -59.44823 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a534a78-2c4c-33a4-b57b-549b4f5b9143 | -12.43722 | -43.41362 | 2026-09-09 04:46:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e970b24-af46-35e6-8e92-0b457fd4049e | -9.69436 | -43.44616 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90937d53-f771-32f9-ac3a-c736f26ebb4c | -8.6153 | -47.36109 | 2026-09-09 04:46:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe477960-14d5-352f-b067-bb80fd4652b7 | -9.69359 | -43.48623 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a0f9111-b4e6-3e71-99a0-686a1501a7c1 | -10.75096 | -45.97027 | 2026-09-09 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e00b288-09bb-3629-b377-e79e610e2162 | -8.09937 | -45.67519 | 2026-09-09 04:46:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8290ca84-2ac7-3b2d-a999-3c099f7415e2 | -7.52318 | -45.92916 | 2026-09-09 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 943b2ab7-cfb8-3bce-af50-de50c0768e89 | -7.52373 | -45.92734 | 2026-09-09 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c2b9171-43a5-33d0-b349-60e534fc4958 | -8.72229 | -62.40417 | 2026-09-09 04:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0b68d5-b0c9-3ed9-a3f4-61b35f9135f1 | -7.9943 | -47.73289 | 2026-09-09 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b82ef7e4-889d-3f7f-8c57-8500e28a798d | -9.69504 | -43.44133 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1452a44c-9281-3bbe-b03f-0aad0a488642 | -9.71398 | -43.47252 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d41bced-291f-373d-847b-333fe7ee8a76 | -9.77654 | -43.45937 | 2026-09-09 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aee413c8-b46a-3b40-afd6-2064d3d28127 | -5.3097 | -56.10949 | 2026-09-09 04:46:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b664c44-41ff-3a88-97fe-682a07820b20 | -6.78591 | -58.93498 | 2026-09-09 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README21.md)
