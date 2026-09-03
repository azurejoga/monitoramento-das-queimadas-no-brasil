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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39bc690c-b984-32db-ab94-5c429b83befb | -11.1312 | -51.5306 | 2026-09-03 13:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 814ac061-3365-3800-872a-0a2aae81cb5a | -7.6171 | -49.9226 | 2026-09-03 13:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 80212332-798c-3d23-b82d-a92dc315aa2e | -12.1896 | -47.0779 | 2026-09-03 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 13847e67-92d0-39ee-b0c3-a6de3dcdadc4 | -5.9428 | -52.1654 | 2026-09-03 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| dde1eabf-8169-3536-ab6d-bdb8a063eae7 | -10.92 | -45.3483 | 2026-09-03 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 5e8de6b0-9ea9-32a9-b74b-652b6ef7aeac | -8.4677 | -54.6429 | 2026-09-03 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| b9ead4ac-7f4d-32a9-af53-b2b21472c820 | -11.5634 | -50.464 | 2026-09-03 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 14fe2f77-04ad-3b46-84cd-d8dff013c82d | -8.7851 | -54.601 | 2026-09-03 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8336c797-7013-3fb9-9b42-286627a0dc86 | -10.1842 | -50.27 | 2026-09-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b140895a-d1fa-311c-86cd-4ea55a555bac | -8.7853 | -54.5808 | 2026-09-03 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 9c5f8011-f153-3ea3-956e-27655c357f16 | -10.9204 | -45.3253 | 2026-09-03 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 81975e7c-65f7-36ff-ae0b-2b526912c709 | -10.9013 | -45.3279 | 2026-09-03 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a2008558-61e5-3982-b8ff-04aef3bbb61f | -5.3264 | -60.143 | 2026-09-03 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 967dfbc3-488a-39c3-a261-5fd35f7c8e8e | -10.8822 | -45.3305 | 2026-09-03 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4087681f-36bb-34b6-8e8c-34be401140d5 | -8.4675 | -54.6631 | 2026-09-03 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 45b8bee2-c07d-3bf4-a33c-42115e649207 | -5.5978 | -44.0209 | 2026-09-03 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 04911b80-274c-3df2-9212-e32dea221f1f | -11.5825 | -50.4618 | 2026-09-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 15049015-fe79-3981-8cf2-896dabdc656b | -12.1896 | -47.0779 | 2026-09-03 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| c14d98d1-70ff-3377-bcee-6c5a7b851915 | -11.1315 | -51.5094 | 2026-09-03 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2684fb0f-c670-322e-b82a-98aaa29ebfcf | -8.4481 | -54.7452 | 2026-09-03 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 59c7cee4-44a5-34aa-938b-1e25819880da | -12.0553 | -47.0966 | 2026-09-03 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 4fcc77af-312d-30c6-98d8-a3c131b213fe | -5.3264 | -60.143 | 2026-09-03 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 975f15a3-2912-3949-a080-f24e4484946b | -11.6573 | -50.5389 | 2026-09-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 863e5fec-f183-3846-af8a-4d99467f60cd | -11.1312 | -51.5306 | 2026-09-03 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b62d30dc-e122-3bb8-ac2b-f94c10b104b6 | -8.4677 | -54.6429 | 2026-09-03 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 294.2 |
| c2b2084b-dd19-355e-94dd-14f3ee369e73 | -11.5634 | -50.464 | 2026-09-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 211.7 |
| ee5711e9-f61f-36a1-afc3-6cbbb04869ea | -12.3626 | -48.1459 | 2026-09-03 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 986dbf47-e291-33f0-8e0b-21b7c192b559 | -7.6171 | -49.9226 | 2026-09-03 13:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 982624b5-4306-37f6-9369-8505d856888c | -8.4675 | -54.6631 | 2026-09-03 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 177.7 |
| e75da934-6205-34e6-9581-0b95dc502b0e | -12.0557 | -47.0741 | 2026-09-03 13:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 55c4151b-c7b2-357d-8707-717564cdb56c | -10.127 | -50.3184 | 2026-09-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 802b52b6-0027-320d-9101-acd5483f2340 | -10.1839 | -50.2914 | 2026-09-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 3007eca2-22e3-3384-805a-38d1a09c78d1 | -10.2815 | -50.0464 | 2026-09-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| cda71f61-9676-30c1-82a8-861c06100e15 | -10.1842 | -50.27 | 2026-09-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0c6d23b8-268a-3d00-8834-cebf14dc4f4c | -11.131 | -51.5517 | 2026-09-03 13:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 8765abbd-9916-3ed3-aa0a-c179294e10d6 | -8.4677 | -54.6429 | 2026-09-03 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 2d6df275-cabe-3695-9f52-2df80cc83921 | -5.3264 | -60.143 | 2026-09-03 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3ed3418f-d22e-3070-8283-c9f129e51f24 | -10.2815 | -50.0464 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 27bbb9f7-351f-3bb1-8bda-824a7b6ed903 | -10.8822 | -45.3305 | 2026-09-03 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3b055180-5cd7-3b2b-a4ae-1e935c24cbd4 | -6.6883 | -59.9436 | 2026-09-03 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2a49ad3c-e3bd-3f70-90bc-08460545a81e | -5.5098 | -60.1947 | 2026-09-03 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d4b32832-1ba4-36c5-85d3-5fec380e5c08 | -10.92 | -45.3483 | 2026-09-03 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 660b4bc0-5d0f-3f90-b096-579f5ba58630 | -7.6169 | -49.9439 | 2026-09-03 13:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 343a7c4d-0fb8-390c-a808-88cd1aca76a3 | -10.1456 | -50.3379 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8392e500-a3b0-3b5c-be48-cdf2bbb4e5a3 | -7.9608 | -44.2981 | 2026-09-03 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4da74b96-9577-3ecc-9da5-bcc578958802 | -10.1842 | -50.27 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2bcff80b-1226-34d6-a617-c56976b2770c | -12.3626 | -48.1459 | 2026-09-03 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9c200555-3f70-37b5-a52e-31c1b98756b7 | -10.1273 | -50.2971 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f5978a24-4d4b-3bd2-a1f7-343bd02c2266 | -10.5254 | -50.1709 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7fc0290a-07f4-3b29-adc8-0eb1fafc0bf7 | -10.3196 | -50.0211 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 7d9d49bc-0d60-38d3-9e1a-58e0c5addc17 | -8.4481 | -54.7452 | 2026-09-03 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 7a08e73b-eeb8-3fe2-845d-3fe21f709e9a | -1.4752 | -54.8157 | 2026-09-03 13:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 1495f038-f120-3602-9ac2-d4a5cfaa7054 | -7.6171 | -49.9226 | 2026-09-03 13:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 115cff82-169e-3d6b-8ed7-e79ce4a2820e | -7.6147 | -44.9062 | 2026-09-03 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2484f6b4-5ef7-335e-86e4-8486ecddc2a2 | -7.6149 | -44.8833 | 2026-09-03 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 06b60556-6bee-3ff3-bc5a-40f1b187316d | -13.3625 | -51.359 | 2026-09-03 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 3cefb609-54b7-361e-911c-14049084eff3 | -10.9204 | -45.3253 | 2026-09-03 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 9d985614-fa0e-37bb-8ea8-bb36a0acf21f | -10.165 | -50.2933 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 7a725cd3-6e75-318c-b565-1b16efdc2758 | -11.3334 | -50.618 | 2026-09-03 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9397655b-97bb-3bfa-ace3-c0cf0be30841 | -10.1839 | -50.2914 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 4db8ae87-7098-3fe7-9aec-2928b14547a4 | -11.5634 | -50.464 | 2026-09-03 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 9f9d34a9-ddd4-3f45-9f5e-759c18515608 | -13.3817 | -51.3566 | 2026-09-03 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b7a54c7b-747c-3658-bb8d-a86bb7741dee | -8.4675 | -54.6631 | 2026-09-03 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 6cf40c9a-6d71-34a6-bcc8-925fe8558095 | -10.1084 | -50.299 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4c80085f-70c4-3a87-aeb9-fb51fc45b6e0 | -11.6573 | -50.5389 | 2026-09-03 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a84b8c65-22b8-3534-95ed-801a7f504071 | -11.6577 | -50.5175 | 2026-09-03 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7e4aa409-a64f-379e-b7f5-dd4f3e8d55d0 | -10.3385 | -50.0191 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 596ecb19-8d53-3304-bd33-0da3f8401964 | -7.9611 | -44.275 | 2026-09-03 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f5e5c41f-1ae1-372a-aab4-a73cabd34b32 | -10.127 | -50.3184 | 2026-09-03 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 90a0aab3-8f6e-3c16-a44b-0c6ea0a607b6 | -8.9598 | -44.4204 | 2026-09-03 13:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a6200fa3-e603-37b9-b66e-961ced94884a | -10.2023 | -50.3322 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 8fa1d245-48bb-33bc-8f54-ca743475dc2a | -12.3626 | -48.1459 | 2026-09-03 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9346a6d9-e8e7-39c8-8089-4f2cc6c6cd1e | -10.165 | -50.2933 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d9ee4888-6661-3bf5-9ace-b91644f2b35a | -10.1653 | -50.2719 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ebf9ad50-f133-3017-806d-9b1cd5446fd7 | -10.3574 | -50.0171 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 632cf0dc-4a67-339d-9b70-39d4085f439c | -7.9614 | -44.2519 | 2026-09-03 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.8 |
| cb245b88-80a5-3f7a-9088-6a18473324fb | -10.7158 | -46.2169 | 2026-09-03 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 6d4a2ff2-6b95-3ec9-9143-fb34d47da5df | -7.9605 | -44.3212 | 2026-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 6689b14f-daeb-314b-abd0-ac47b05b60a3 | -12.0557 | -47.0741 | 2026-09-03 13:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| e5b27137-7aeb-31ae-86da-fa60966888d9 | -13.3817 | -51.3566 | 2026-09-03 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| f4c505a5-3a7c-3622-9471-d9bee602fe06 | -11.3056 | -45.1113 | 2026-09-03 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 840ed16c-1d1a-34cd-9a17-08c3fb3a4167 | -11.6573 | -50.5389 | 2026-09-03 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ac2463c7-aaf1-3cf6-a889-63cf4c89cf64 | -7.9608 | -44.2981 | 2026-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5f19b436-cf2f-3f5b-bcd1-16b207e63809 | -10.3959 | -49.9703 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c1a03f5f-0e64-3b2e-8cb8-bb248afbd813 | -7.6149 | -44.8833 | 2026-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1fa81845-8bbb-337d-b7bc-129c76e99f0d | -10.1842 | -50.27 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 32326ed9-cfec-3ef3-a8da-4dfdf0a08f08 | -13.3813 | -51.378 | 2026-09-03 13:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 7185bd5c-7bc8-35dd-8c10-3efe7f2fd257 | -7.98 | -44.2731 | 2026-09-03 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 5d277d93-6973-3705-9b58-b97a7ffbb1eb | -10.2398 | -50.3497 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 3555f829-e188-3208-9885-7f30e1a44a3d | -7.6147 | -44.9062 | 2026-09-03 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 9a740024-b6f2-333c-b2b4-cf5ede96d2cb | -8.4677 | -54.6429 | 2026-09-03 13:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 96e5379c-85b9-3cb1-9c2f-0dffca25b288 | -10.3196 | -50.0211 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 85d298e5-d8ec-3ad4-acc5-60e797fb0e2e | -10.3385 | -50.0191 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b7031fe5-56a7-3145-9bbd-04163509a893 | -8.9598 | -44.4204 | 2026-09-03 13:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| dc4bb72a-d2e0-3712-a8ad-70147ace3346 | -11.2879 | -54.0317 | 2026-09-03 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f995c6a4-8244-393f-ae1f-3e639c16414f | -1.8019 | -47.9586 | 2026-09-03 13:30:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9fb42024-9e25-33b5-b7ba-f0d68555ddcb | -11.1824 | -50.5706 | 2026-09-03 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f06dec76-d62e-30cc-8781-6b785d1f6e7c | -5.5098 | -60.1947 | 2026-09-03 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 323f4526-1db0-3601-a22e-2af8042cd16e | -10.1839 | -50.2914 | 2026-09-03 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c5cab506-be1c-3d36-9147-0abd095713e2 | -7.6171 | -49.9226 | 2026-09-03 13:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |


[Clique aqui para ver as próximas entradas](README57.md)
