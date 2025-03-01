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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c19c84c6-00e4-3b7d-9ef3-5dfd5b486643 | -21.07863 | -54.19415 | 2025-03-01 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03fc3805-570e-3c2a-9273-8a68c2167c33 | -23.77881 | -55.15326 | 2025-03-01 04:38:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b621b23c-88f8-3ff4-a8a1-eb7b53dc2ac3 | -22.83942 | -42.76868 | 2025-03-01 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2779e7dd-8777-3715-bf21-084dfb023343 | -21.52586 | -51.47145 | 2025-03-01 04:38:00 | NOAA-21 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 112c13f0-2fc8-3afb-9202-4162f48f9c05 | -22.94558 | -42.77002 | 2025-03-01 04:38:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 3915ba81-c5bc-3bf3-a777-417f040f42de | -22.69164 | -47.43193 | 2025-03-01 04:38:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7079fbb7-7bb4-366d-b127-c19bbac5ed2c | -21.08214 | -54.19485 | 2025-03-01 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bac7dd45-1b2d-3f77-ab34-c882476a5f6a | -22.67826 | -42.85391 | 2025-03-01 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d65820e-5458-3b9b-add8-8470369f3463 | -20.87717 | -54.78985 | 2025-03-01 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbcc90ce-60e3-33e4-a903-843763f65ab8 | -23.78236 | -55.15397 | 2025-03-01 04:38:00 | NOAA-21 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| 527f5334-954d-3984-90ae-139946a7741b | -23.04634 | -49.89624 | 2025-03-01 04:38:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3ad34c64-3629-3689-b4e4-5f9aadb1c51b | -23.78158 | -55.15836 | 2025-03-01 04:38:00 | NOAA-21 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 91c6653b-8b90-31a4-be82-b64962c3ca83 | -22.78576 | -43.75695 | 2025-03-01 04:38:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 07b6e836-5e88-3eee-a143-f5ad43d5dbc7 | -20.88251 | -54.78425 | 2025-03-01 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eb37600-b2e2-3ac2-b4b3-a95b5f016568 | -22.78616 | -43.75745 | 2025-03-01 04:38:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ab006659-152f-3f77-89f9-5646961ebcee | -20.87874 | -54.78084 | 2025-03-01 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de7cbf58-6f59-34b6-b583-87b2fd28d213 | -23.34019 | -46.77273 | 2025-03-01 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5395386a-25b7-381f-8c56-9b66563cf7d7 | -23.63025 | -46.42719 | 2025-03-01 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b09bd12-2023-3d12-a274-b424b199a3f1 | -22.67795 | -42.85704 | 2025-03-01 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ff7a948-e35f-313b-9ccb-ff8b677643cb | -21.09696 | -56.03717 | 2025-03-01 04:38:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d847a1a5-d56b-3fc1-95d7-d280b5aa528f | -20.87433 | -54.78462 | 2025-03-01 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a29ab9c-ec45-3cbf-b65c-cbf651ffaa2a | -22.41089 | -48.21445 | 2025-03-01 04:38:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf87ca51-1bd2-3d2d-94e5-ba83d1add404 | -20.87355 | -54.78912 | 2025-03-01 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ab1acc3-10a0-3262-b243-f7ae08792264 | -22.8391 | -42.77181 | 2025-03-01 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bab92980-94db-3dcc-9d67-6f64656d556a | -21.08142 | -54.19906 | 2025-03-01 04:38:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05b73b8a-11bb-351c-9d9c-2f3c0fa9bdc5 | 0.97347 | -60.52603 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67ed5ac4-43a5-3caf-b695-07b01edae637 | 1.31192 | -60.07022 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd215616-93f2-32af-b6e2-00cf6a9e93f2 | 2.18179 | -61.85973 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77837fe5-d101-343f-ba32-92e97eae0320 | 4.34447 | -60.3611 | 2025-03-01 04:55:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9ae1064-fd29-3379-8408-b151550420ce | 2.1099 | -61.82573 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad03cbaa-b30e-31ea-b7ed-65e6ed98af4e | 0.95949 | -60.53384 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4128542-e5e3-30d5-8172-856a89f2ac60 | 2.02489 | -61.40741 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c81f6fb-acb1-38e0-b666-93a8d00ddc31 | 0.96853 | -60.52677 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 11796982-6def-3538-a5b7-556629fcca60 | 2.82851 | -60.8131 | 2025-03-01 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9283f9d-9eed-3368-9045-432138967a9c | 2.18732 | -61.85898 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c5caecbd-21bd-3945-891b-5dc264e4c9b6 | 2.19232 | -61.85464 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8120c11d-2683-3223-86a6-5fb2dc1ea281 | 2.18021 | -61.84904 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f87e5208-ce98-3716-b1f7-0ea28979a17f | 2.82897 | -60.8162 | 2025-03-01 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b75eac4-9f26-3b50-9f93-a9d8b213ba7b | 1.17739 | -60.11 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5260bd7-33d3-3b9c-9915-ef895d3b8a3f | 2.11536 | -61.82467 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f589c33-acde-3ba9-be94-ff59436df6c2 | 0.82969 | -59.94992 | 2025-03-01 04:55:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a463fb5-877d-3bf0-bcba-fb402fb5ae85 | 2.10829 | -61.81504 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7621a299-00a1-32bc-9126-ceea5427efe4 | 2.10883 | -61.81865 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9276dba2-c9d4-360a-b66e-be8ce9dc697d | 2.11484 | -61.82121 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f2cbe9c-4b1b-3e90-8b2b-c58d8d12988d | 0.96358 | -60.5275 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 52f25ee1-c296-3b19-9c79-737b152d7697 | 0.87287 | -59.68196 | 2025-03-01 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11bb9aee-5ac6-3424-af42-29a985457e29 | 1.12713 | -60.52916 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a54aeb30-8678-3564-868a-4d63cac0cfd4 | 1.3385 | -60.70378 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b00472d9-adb7-3265-bed2-c72f488561a3 | 4.34398 | -60.3577 | 2025-03-01 04:55:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1104ef4-9349-33fd-bfe6-ed8b514df95f | 1.17623 | -60.10866 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f130c02-2447-3c85-84e1-0d31459858f6 | 2.18639 | -61.84689 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b60e341b-2b23-3a21-8ccb-5ab6ed22cade | 2.02538 | -61.41074 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee24b1fa-a55e-375d-814f-8942c1935249 | 0.99574 | -60.46497 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| defaa11b-df28-3386-8d90-3ecc78bba868 | 0.96444 | -60.53308 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7e15dec1-ff29-36ef-a474-30a1ecc3dffb | 2.18749 | -61.854 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23323874-a897-32a2-b45b-997177bbec85 | 2.44153 | -60.65518 | 2025-03-01 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6073d303-14f1-3d07-aa56-660d145b479a | 2.19302 | -61.8532 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 983adc72-ee75-3b5d-9c35-413a740744c0 | 2.10937 | -61.82221 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93eab0a3-a4db-3402-ba3e-d83041fb92c4 | 2.44197 | -60.65816 | 2025-03-01 04:55:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0dedfdf9-2d53-31f2-a339-b3976f3ba50f | 2.11378 | -61.81423 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3c20fd9-bb70-3276-9802-e53e8f6a9bd4 | 2.18679 | -61.85543 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6ace378f-fef3-3eb6-81db-a3501afee509 | 2.18251 | -61.85827 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d13daf1e-9a18-378b-a6e0-c09adf2e85c8 | 0.87046 | -59.68414 | 2025-03-01 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 602c4261-e7c1-35b0-ad55-1463b331d290 | 2.18141 | -61.85117 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cdb9c6f-4e70-3850-970d-431405a61df5 | 0.9694 | -60.53236 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b6ba355d-b0ea-32dc-a634-a37b2be966ee | 2.82804 | -60.81 | 2025-03-01 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b8ffa726-0e8d-30e5-8f7f-a2ec35c95501 | 0.95863 | -60.52828 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ac3407c-434d-3522-8190-4dff0265f5db | 2.18627 | -61.85188 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f621ef3-f040-39fc-8603-50dd734d8928 | 2.18694 | -61.85044 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b82219d6-f8b3-3482-b6b7-681152b93cb1 | 1.12711 | -60.52693 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27cdd1f1-a01b-32b4-b538-5612fc3acfb7 | 0.99353 | -60.46075 | 2025-03-01 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1968e3e6-17f9-3226-a6a0-c5ec092f5ac5 | 1.33895 | -60.70668 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0bb5ed1-2b1d-3b48-8945-fe94db1c678e | 2.18574 | -61.84831 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42198523-da31-3dda-85a7-b2e7f81d4116 | 4.33878 | -60.3581 | 2025-03-01 04:55:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17b6fefe-7773-30af-a9cf-a95d7177a3fc | 1.68858 | -60.22886 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4a59383-a00f-3ab9-b998-c05462e31b55 | 0.82974 | -59.94812 | 2025-03-01 04:55:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46ebe6ee-ddfd-3783-becf-f656a974618e | 2.11588 | -61.82809 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 806b8145-f343-31b7-94b8-f287881c2b43 | 2.19179 | -61.85108 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5be3522b-77ab-32c7-84a7-ee76bf91f39c | 2.18805 | -61.85753 | 2025-03-01 04:55:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f21185a2-62d6-3110-b998-eb036ec58e52 | 1.69346 | -60.22795 | 2025-03-01 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4afba170-2ab9-3acf-95b9-a6ecc1597bd6 | 1.07093 | -59.23313 | 2025-03-01 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ed48187-2efe-3dca-8033-7127325bc388 | 1.1335 | -59.5465 | 2025-03-01 04:55:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59ea1107-9865-37a7-a76a-dbe352e35b59 | -1.5417 | -54.54399 | 2025-03-01 04:57:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b79f07d8-710e-347f-be66-a530666b7927 | -7.9042 | -61.5101 | 2025-03-01 04:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b730289-6d56-3fb2-aea4-8fec8ead91c9 | -2.71678 | -54.62029 | 2025-03-01 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cda2374c-f9e8-3aec-a75b-7bffee5f8b6b | -3.02219 | -54.59211 | 2025-03-01 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7812cefa-7050-32ce-825b-82b5e3dbca09 | -2.71398 | -54.61621 | 2025-03-01 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 724da433-206c-3f0b-a464-6a5d3c6f6aac | -3.011 | -54.57588 | 2025-03-01 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e05c1ce-ec69-3d28-bac0-67d030334b87 | -2.71734 | -54.61674 | 2025-03-01 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d81f7422-7a6d-3a9b-85f2-98229c89970b | -3.01156 | -54.57235 | 2025-03-01 04:57:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c1ccbfa-de6c-3290-9e38-592af838bc03 | -1.53776 | -54.54704 | 2025-03-01 04:57:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b98bb9a-9d72-35a5-bec0-85f8417ceef6 | -11.87774 | -44.38393 | 2025-03-01 04:59:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4db54ca-bcae-38d9-8ae6-5205831153e5 | -15.08007 | -48.94253 | 2025-03-01 04:59:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df98dcd6-091e-3d9a-844a-85f5fdb2a32f | -23.043 | -49.8954 | 2025-03-01 05:01:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4660b291-44da-3cb0-8cf4-fa9888a75f91 | -21.08195 | -54.20024 | 2025-03-01 05:01:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d568bc46-1c07-315e-b3bf-162553ae172f | -21.61228 | -48.47384 | 2025-03-01 05:01:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4ba2729-deb1-3207-bdda-639f9d16e8f8 | -21.0789 | -54.19515 | 2025-03-01 05:01:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c4fc422-ae99-3396-a28e-d29e27e27086 | -20.87504 | -54.79283 | 2025-03-01 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b49f45f4-a330-3ccc-a079-6a9a0179caeb | -21.52445 | -51.47469 | 2025-03-01 05:01:00 | NPP-375D | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff3ea14c-4640-324f-82bb-b9dcb95dc2b4 | -19.72411 | -55.19796 | 2025-03-01 05:01:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
