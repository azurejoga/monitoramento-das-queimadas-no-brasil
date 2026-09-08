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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b04e63c-be33-3452-8810-9aa3ac5079aa | -3.3862 | -61.3143 | 2026-09-08 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba85b8c3-4759-3681-9210-f23d6ad975d0 | -3.46001 | -59.51106 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 798368f8-2043-38ee-8ebf-303125843204 | -3.37882 | -59.42519 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4738a964-28dd-3155-a4cc-9f4d138b59be | -3.37424 | -59.42446 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65dd5764-6bed-307b-b7e5-7bc64ecdfc4d | 0.30823 | -60.44585 | 2026-09-08 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57f3c286-db25-3a33-a470-80f8b867d0ac | -3.0592 | -59.26926 | 2026-09-08 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b93c868-56fa-3639-b7d6-83eb74455030 | 0.58709 | -60.44563 | 2026-09-08 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 548e0263-1dfd-37c0-af82-ff124aed6b88 | -4.09568 | -60.66314 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4bd5f792-a2e5-30a6-a02e-af4168673da8 | -3.05388 | -59.27335 | 2026-09-08 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8852b142-d1f5-32ae-9f40-c3d7b3955481 | -3.77623 | -58.85134 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 130643f8-a558-3333-a753-72722fca5ccc | -1.19279 | -55.73 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 564cef38-9db7-3b1e-bbad-0a3d670d62cd | -1.19792 | -55.73477 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d250ff-b68f-317a-9773-c87bec8db467 | -5.28445 | -60.11671 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4656e964-83e5-3a30-bb82-6a43e2f6fe86 | -5.18707 | -59.75825 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bfb6546-3b3b-3518-8881-db8498ad3d08 | 0.30418 | -60.44648 | 2026-09-08 05:48:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b8a54ee-ad0e-3b91-9066-e65a7a3a2a60 | -5.28378 | -60.12122 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fe3f2c9-6421-3b7a-bb1a-67d4f256326e | -1.19445 | -55.71876 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a301bd0d-51e7-3ca4-a4b6-c3dca5ee5079 | -3.77548 | -58.85658 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e0a65237-fb22-3673-b4de-44f9a1a93b22 | -3.06242 | -59.27945 | 2026-09-08 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f1101ac-0248-328e-9106-ea9b8dbf6bbf | -3.14893 | -60.65429 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c5264989-bdf4-3c20-8259-a57f86031d8c | -3.15414 | -60.65361 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| deb9c141-3c54-315b-b638-502026032daa | -5.45526 | -60.1732 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce3dd6d-13fd-3bac-9668-68eade2e16b3 | -5.48518 | -60.20379 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95ef35d1-2879-3d33-8843-d74b06ed8d85 | -3.0585 | -59.27401 | 2026-09-08 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5b926dc-bfe6-3f5a-b977-bc181233e092 | -5.37094 | -56.02217 | 2026-09-08 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 200ffa6e-d756-3f82-b298-465537656e7f | -3.88733 | -55.82203 | 2026-09-08 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76227a66-b429-3d21-becc-d386ee50bfd6 | -3.14349 | -60.63362 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adc59626-791e-3305-8fc6-55c60b41121e | -5.45011 | -60.17707 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6debd43e-c058-32fc-8a23-e604a5d4e11b | -1.19221 | -55.73389 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea783778-7a8e-363d-b93c-f74c41c8e595 | -3.69897 | -58.94471 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0bc49231-6296-3f69-8187-f223217d55aa | -4.34722 | -55.2256 | 2026-09-08 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 749b4675-a520-3469-b557-91007a70f253 | -3.37355 | -59.42918 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c2fb9bb-76c2-3210-8f4e-88a90fd736e5 | -1.19548 | -55.73847 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df607f4-555a-3337-bb68-0d51fe519560 | -5.54865 | -60.24078 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80cd66c4-f9f7-3594-9574-b1b25299a413 | -1.19609 | -55.73459 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69698a76-8c4d-3417-89a4-87196d83097c | -5.37034 | -56.02654 | 2026-09-08 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90d2f7ae-f90c-3a0b-be83-b79a76d1f4e3 | -2.8435 | -53.9904 | 2026-09-08 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9640e36-99c4-323a-a053-e2fa45b18003 | -5.59649 | -60.24481 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 681c48c1-97e3-3a71-abda-af9d07e02a5d | -3.4607 | -59.5064 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a13c472e-b95c-36eb-8705-b326cd07fcb5 | -1.19038 | -55.73367 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7a7e173-1dd9-38f1-a7ea-35a07852c4c9 | -4.34655 | -55.23027 | 2026-09-08 05:48:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f27a538-1aca-35f9-9f22-2ca71c4b20ff | -5.59349 | -60.24742 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 887c35d1-3b62-3701-a956-0b93ab0fdd14 | -5.29063 | -60.11935 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48b7bd81-0411-34a6-ade0-8fb697dd83cc | -3.95687 | -58.95641 | 2026-09-08 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 618d243c-340e-36f9-9109-d71cff03e65b | -1.19331 | -55.71484 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ae971ac-291e-3692-8c82-65c69ecdb2df | -5.4546 | -60.17774 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb005142-d09a-388d-ae7d-6b7023888eb7 | -3.15357 | -60.65749 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d98b21c-fe9b-3078-bcc4-ef0e27b0d88a | -2.56116 | -54.74525 | 2026-09-08 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d694a67-3379-3613-8fa0-825f48047478 | -3.13929 | -60.63294 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca99583a-9257-3315-a187-66cf06c3acdf | -3.76353 | -59.42635 | 2026-09-08 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cce1c357-f54a-3d3a-bd3c-4a9735bb5bb8 | -3.89317 | -55.82336 | 2026-09-08 05:48:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8809894d-07dc-3295-bce3-c50add3db02d | -5.28828 | -60.12189 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d81ab8-8e33-3a73-8719-d10d4f4bc0de | -5.36974 | -56.03092 | 2026-09-08 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36e2d05f-edf8-3671-ad05-3cc50640020c | -3.15253 | -60.65884 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37719276-ddb1-3ad2-bcd2-1e1fb86e7d72 | -1.19273 | -55.71859 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23fe0df3-de22-3874-a5ad-f96afe03975c | -3.38524 | -61.3147 | 2026-09-08 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37783bcd-0999-3132-914c-a1328fc6b13c | -3.7045 | -58.9403 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92bbd7ec-1a49-3a1f-b4c7-22b2462d523a | -3.77143 | -58.85058 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f850adb-f53c-39d3-b925-d42b8d80abaa | -3.96054 | -59.36195 | 2026-09-08 05:48:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e517c70-298d-36e8-98c1-8e3f4dfba1b2 | -1.19734 | -55.73869 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e17ca833-2835-3179-98ea-6545fa96ab3b | -5.45077 | -60.17254 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8a22195-458c-338f-87e1-f71e46eec11c | -1.20422 | -55.71988 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c63767db-5511-3905-9ec5-d8ddd385f1b3 | -8.86268 | -63.3879 | 2026-09-08 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc34047c-e1d3-3f79-aec7-99f598131291 | -8.13483 | -62.89811 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb16466-2962-34ef-90bc-4f05cea21c98 | -10.08656 | -58.55201 | 2026-09-08 05:50:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a02f2e-f252-3e71-a8c2-f00137ebbfd6 | -9.36381 | -66.66833 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb090cb4-5d92-3671-9685-994851ab84da | -7.06821 | -56.46546 | 2026-09-08 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fa615f6-cf9a-3465-b6f9-c1ecf0d0c231 | -8.55901 | -63.88575 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2905e98-d41b-3e47-afbf-157e96af101c | -8.53383 | -63.85028 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdc244de-b43f-38c8-af2f-10a980c79948 | -7.06395 | -56.46839 | 2026-09-08 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f5f4db6f-6596-354c-afab-ae05c166b4f2 | -8.98913 | -65.41428 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eed05edf-4c8d-3c6c-90e1-28130e1cd08a | -6.79817 | -58.95047 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ef3ea5b-fbd2-3977-841e-6b3a681a76be | -6.95138 | -59.75235 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17c529b3-1563-3f7c-81d5-03b2f30ff376 | -8.98567 | -65.41375 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f395cbb-82c6-3a04-8c15-a57d98b7a5e9 | -7.06989 | -56.46911 | 2026-09-08 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64e3d655-b03e-3bb3-b109-beb9b33a107f | -8.53013 | -63.84973 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ccbb027-31bc-3ff2-a45b-09c402f4881d | -7.07411 | -56.46648 | 2026-09-08 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ba13d48-1959-39f4-a39b-b003de42f963 | -8.13516 | -62.89986 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27216402-e29e-3820-896b-6d50c1b1f62c | -10.087 | -58.54859 | 2026-09-08 05:50:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3d8d02b-8268-366f-8091-ec57abd49549 | -7.78629 | -66.95757 | 2026-09-08 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0d12c3b-49f8-3f3b-a5c3-88daf6383c6c | -8.5123 | -69.79681 | 2026-09-08 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b64084d-58f3-3e32-8c5f-5f6252deb37d | -8.51168 | -69.80063 | 2026-09-08 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4267b881-77fd-3018-b6d0-3d967fb722bc | -8.2629 | -63.99463 | 2026-09-08 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d06e61b-4735-36eb-bafa-ce95260e0543 | -6.95612 | -59.75301 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 991c1a19-eb62-37f5-a3db-57cdd1cb4eb2 | -9.75135 | -66.61906 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41b1f96b-3241-38ca-80d6-10d8e447cc6b | -6.76614 | -59.42944 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24033bf8-1c4b-3e87-9d7a-bfa50a416c1f | -8.50884 | -69.79623 | 2026-09-08 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03b7932f-7ffb-362b-b049-5602d09461ef | -6.63791 | -59.43704 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 42cefa84-9154-39f8-a023-9dfba9e7d7e2 | -6.76538 | -59.43482 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0635cab2-3c2b-332f-afa8-1d1c880e35b5 | -8.5332 | -63.85472 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1c9711d-a20c-3e82-a63a-e3ce6fe19263 | -8.53127 | -63.85145 | 2026-09-08 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 452f8f54-cd31-35c3-86e8-1f96c0268c25 | -11.11974 | -68.62943 | 2026-09-08 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0272fdc1-56c7-3fcf-98eb-fb0a3caa393c | -11.40996 | -62.12582 | 2026-09-08 05:50:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 948ef654-43cc-3685-b72e-d904c66b266e | -7.78575 | -66.96104 | 2026-09-08 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ba4068a-93ab-3a3d-a037-f34eb33b5c1c | -6.95492 | -59.75209 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bf7d202-96f7-3c47-bb8f-99b5673e96f1 | -8.25923 | -63.99408 | 2026-09-08 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dca3a23-32f0-37cf-855e-2d956e94998b | -6.6372 | -59.4421 | 2026-09-08 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3ae280c6-6e73-332f-ad2b-65e311ed6fee | -10.20467 | -63.55366 | 2026-09-08 05:50:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a69a21c-6461-3bad-a5b8-9d22d1d83253 | -8.85886 | -63.38731 | 2026-09-08 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f38d91e-f837-3ac8-b515-9e32bf54a472 | -9.36327 | -66.67189 | 2026-09-08 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README25.md)
