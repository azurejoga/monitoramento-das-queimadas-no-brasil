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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 653c83d7-46fc-324b-9946-26aa0fbb75fa | -3.55136 | -59.03494 | 2026-08-21 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4403d38b-7b4c-32d2-b340-3ba660a39eb5 | -2.32542 | -60.06367 | 2026-08-21 05:40:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9905c5a-4756-3589-a70c-cec3ea8c57b2 | -5.66326 | -51.65192 | 2026-08-21 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6747629f-7997-32fe-a9c7-499b3841bbaf | -3.84175 | -59.38118 | 2026-08-21 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01c6da73-a072-3c27-9823-4360205513c2 | -4.5837 | -59.94272 | 2026-08-21 05:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f19ff99d-d3a6-3797-95e7-608526075bca | -3.3849 | -59.52687 | 2026-08-21 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b83121ce-f1ac-334e-b827-6715bef42779 | -4.45093 | -55.39421 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9912bb4f-bc61-3368-b56a-9d9ca9d6a882 | -4.95719 | -56.25981 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30c9020d-0c9a-3943-ae3c-1814a011bf89 | -4.10515 | -56.36261 | 2026-08-21 05:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f19eb661-4439-3b85-82f9-850344432354 | -4.95959 | -56.26427 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 08b29803-5591-332d-b45a-e4c92222839a | -5.66404 | -51.64628 | 2026-08-21 05:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c77f15b6-a9a7-3775-96d3-bd3bbd89eb95 | -3.84242 | -59.37947 | 2026-08-21 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 678a4b08-1b61-3a7d-8277-bcdd00f6975e | -3.76177 | -59.42488 | 2026-08-21 05:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71e62e83-bd3b-3013-82cc-2398844713e9 | -4.96114 | -56.26587 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54ac0896-de5e-3125-8b72-990789979864 | -4.35132 | -59.54107 | 2026-08-21 05:40:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 387844e6-35e7-3b70-a0e5-da7d5d70c8ff | 0.30146 | -60.44818 | 2026-08-21 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e885292-971b-3074-a283-04959e93b88e | -4.95415 | -56.26841 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77afe288-d041-3ec9-a247-4ae06363c839 | -4.94254 | -55.78401 | 2026-08-21 05:40:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5af28d4b-e7c9-326f-baae-7a6f235fd850 | -3.3842 | -59.53128 | 2026-08-21 05:40:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09afbeec-81b4-33bc-8bf6-428f06b59df8 | -4.4715 | -55.39914 | 2026-08-21 05:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1dedb990-b818-350b-b9a8-d7b55277afca | -8.89932 | -60.54731 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 09c12758-c5ab-334c-895f-9d5ca162b35e | -9.42007 | -60.42467 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16995b2d-3d06-388f-9f9b-be1aa554b8d0 | -6.89567 | -59.43399 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 688f1524-2302-3463-9e5e-72f597adc8ab | -11.68517 | -54.57634 | 2026-08-21 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9b357bf-984f-30af-839b-e19d3e01fdf6 | -7.77396 | -61.15523 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a933aee-a401-3ee1-8f11-55d20d3b3173 | -6.21315 | -55.48112 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17d7f7ab-853b-39a2-a333-8a25228b5fc5 | -7.60282 | -60.95283 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d432660-4cac-3af3-bcb7-57e01e8bb90a | -6.01801 | -57.82375 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0fb323af-a314-33a4-bed2-4cbe6e7133c9 | -6.86997 | -59.44552 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aaec1e8c-5fae-3ae9-8438-1104f3093e7b | -6.122 | -59.90608 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6204f6cb-19ce-39d3-8b29-962f1fbc322d | -6.89925 | -55.71763 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f8cd113-41af-3663-ac41-00694d3371fc | -6.88323 | -56.42126 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58016808-373b-3ec1-85ea-d6cf295c8e81 | -7.79667 | -61.18689 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b12942a-bed8-36f6-8e26-0920c70eb040 | -6.10122 | -57.8724 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35bcced5-2209-3514-9f43-19ed7a234609 | -8.58701 | -54.77864 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04091ec0-4576-342c-aef7-d32292c106f5 | -6.92322 | -59.35618 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2edf1c3e-0b8d-36f2-b2d8-d92c16ee97df | -6.52353 | -58.60192 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0eb404-7012-3ff2-86ae-b01438b72b5c | -6.92472 | -59.34605 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bc46369-1767-3a08-b90f-90ae61778c49 | -9.42459 | -60.42051 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6096ce7-bd47-32b2-9c52-de8e2d8c4c56 | -6.23488 | -55.40244 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7647c9a9-1d4b-3bf5-ab08-99ed9171e291 | -6.42415 | -52.74559 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7d81c81-6869-3a3d-b254-a8e4ff217f88 | -6.43279 | -52.72758 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 021309a1-3b7b-35ec-ba34-3d88aa1ee52b | -6.54947 | -56.26507 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 133f4707-f960-3948-b082-f7e8706c3012 | -8.58517 | -54.74871 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 878d3a61-d61f-3094-b617-4d42db887264 | -6.5763 | -55.44628 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3af6777b-bbde-305c-94f7-ee30fb94dea9 | -8.38818 | -62.69309 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb6ebfd9-fde0-3cac-a27f-822033ee725e | -6.9129 | -59.34425 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c60436a-b312-307b-b820-59ec5f68a61d | -6.85966 | -59.4338 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5a5dcc8e-5b78-3cc2-acd7-fef9e6dec551 | -6.35983 | -58.33678 | 2026-08-21 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4484b725-eec8-372a-9f74-5664dce1333f | -6.22404 | -55.61924 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| aab2e63b-0a3d-3d55-86de-79c2ae733911 | -9.4507 | -51.6027 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f31502f-ab45-306b-b988-a2d1593bc197 | -8.59554 | -54.71266 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c1b8012-5f14-31b8-90f1-32a0f629f572 | -6.86503 | -59.42443 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93ab8e30-2c0d-37fd-95c8-c64660d63946 | -9.41683 | -60.41186 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 3bf968b3-2816-3135-9a0d-246f2fad8fb0 | -6.93749 | -52.78352 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d372e95-fb32-3345-9b57-c18e54c64629 | -8.49594 | -54.87174 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f38181f-bd94-3bed-9f9c-4f952d057095 | -6.86038 | -59.42884 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 065d662e-ea6f-32a1-86b9-7e42c7f984d0 | -9.41727 | -60.43609 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d90394d2-e160-3068-a84c-9e8cc28f149e | -6.8643 | -59.42943 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 326d49b2-f3c0-36ed-a94e-2cc228de7657 | -9.39146 | -60.56398 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51c17afe-b2a7-3594-ae0c-614796c89cb5 | -8.40458 | -62.69942 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa13be81-ce7b-3198-8b09-0251e4db4ec1 | -6.86895 | -59.425 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d98c40fe-9ba9-3ec7-b865-6710fe21b5af | -7.53509 | -55.58046 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec92967e-e12d-3cf2-908b-7786f9f07cc6 | -8.89623 | -60.54219 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b33fef0-88cd-37ef-a457-738da0297cc5 | -6.86214 | -59.44434 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6d1c178e-c918-3024-b154-3bd39f14627b | -9.39982 | -60.55803 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e80819f-c0b2-319a-8d5e-2b44c7ce74ff | -6.09692 | -57.87185 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e358cfc-6f2e-368c-81f5-c2e757438496 | -9.41345 | -60.43552 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05cd8333-0c6d-3af4-9f80-c0f0e8a63092 | -7.45788 | -59.9964 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7373a64-bc43-322f-a3d9-9e0f344e4394 | -8.40969 | -62.68893 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db18808d-eeaa-35f9-85ef-1f7ef4c86758 | -10.38461 | -61.2134 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61e19603-97f3-3886-9957-c06a453b387f | -9.4229 | -60.40574 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 88fa195c-fe02-3d92-8db7-9eeabdbd363b | -9.25038 | -59.8135 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ef734f-8621-3403-aa05-b957a479fcdf | -9.40863 | -60.42292 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ea51e6d8-7a80-30df-9b30-fdf679dad8af | -6.90527 | -58.99599 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 175d49e9-cc90-3ed7-b1a7-27d0a0e00708 | -6.21778 | -55.48489 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fdc681b-17a2-356c-877f-714936bf4ffa | -7.86707 | -63.77077 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81e9e0d6-e2af-3742-ac25-6e1e2017b2e2 | -9.20804 | -59.77066 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7bb80e29-26cb-3f15-9c20-e8cd928df26c | -10.39159 | -61.20794 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0f99060-6dbf-3228-84ed-969827d8daeb | -8.5912 | -54.74625 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9f21593-b4b4-3415-b644-6a3a6c55ad44 | -8.59723 | -54.74311 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bffec89-22ce-3cd9-bb46-745f7b261dd0 | -9.45169 | -51.61081 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0ba381a-7f95-3992-ab90-efcd818a4709 | -6.88538 | -59.42225 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 62e75f68-e33d-380d-aa4a-3a5433cc4566 | -6.69178 | -59.10042 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc3f7409-a3b3-34c1-9191-6074a643a202 | -7.60319 | -60.95569 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a7c1a61-8ce6-3f47-9d27-2454b3787cb0 | -6.87926 | -59.43665 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 79785dd4-de77-3262-b40c-269f89097acd | -8.65654 | -54.63501 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b301689d-a76f-3fa8-86a6-f48dc36997f9 | -6.72077 | -59.09742 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a52f10-06da-3dd9-b6c1-48b5746e6e84 | -6.85759 | -59.44631 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f9a406d8-6e87-38e2-b399-b9c20bffce0d | -6.89825 | -58.98783 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43c3d76e-7bf3-3403-a2f6-1c7aa04f4adf | -9.4148 | -60.42607 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eb0d7949-8fda-3527-8e5b-dc49e4189a60 | -9.11893 | -61.60273 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c21f009d-00e0-31f6-956e-31542551b184 | -7.86208 | -63.75928 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a47c1de-70b9-3991-951c-c666a13b1b9b | -7.59985 | -60.94804 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef6b7e75-6019-36ec-a318-d8902af8547b | -9.39733 | -60.55062 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6cb91fd-af5b-36a3-999d-d0dc243aebc3 | -6.4194 | -54.93859 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7423f9c4-2420-3aa8-8d8e-0974813e2ee5 | -8.89489 | -60.55131 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2ce62f3e-adfb-384a-8318-9308ce61bf97 | -6.85594 | -59.43079 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 61e53faf-971e-33ab-8869-6d93673db25e | -11.17321 | -54.03061 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 23d08cd8-0a5c-3dad-b60d-6346f69683c0 | -9.40112 | -60.55116 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README75.md)
