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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e8823a-d95b-3f26-8abc-d334bad49fb0 | -11.3642 | -45.0339 | 2025-09-27 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6d043ad6-c1e1-3bcc-ba4e-fe505741cc89 | -11.9651 | -47.9113 | 2025-09-27 11:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 34b9b99e-4087-3513-b6d6-f851d9efedfc | -11.9843 | -47.9088 | 2025-09-27 11:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| cadd5b49-fa73-32f1-babf-90f091c89706 | -8.8409 | -46.2544 | 2025-09-27 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 50bf780e-128a-3e84-986d-c74ee8a0f730 | -10.0062 | -46.7081 | 2025-09-27 11:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 954c29ce-eadb-3bd2-ab06-3dab952cce7c | -8.822 | -46.2564 | 2025-09-27 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 179.6 |
| d680c350-4428-333d-906f-f6a60cd5afbd | -9.6159 | -47.5741 | 2025-09-27 11:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| eada24f2-1ceb-3097-b508-ec63d863bb60 | -7.7794 | -46.9371 | 2025-09-27 11:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e9991a25-77cf-317e-ab54-840eed5f82df | -11.3642 | -45.0339 | 2025-09-27 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| e5e5d866-30cd-3846-81ad-a98473e667da | -7.7794 | -46.9371 | 2025-09-27 11:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c67fde36-2b60-3292-97d2-13006d795745 | -8.822 | -46.2564 | 2025-09-27 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 0b1f1d8e-d27f-350f-ac62-b3b4be308003 | -9.6159 | -47.5741 | 2025-09-27 11:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| de5d5f93-f53a-388e-be88-6ba65a288969 | -7.7792 | -46.9593 | 2025-09-27 11:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 1d0b90e5-020e-353a-b102-a2e7a1306545 | -12.2829 | -44.0568 | 2025-09-27 11:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 281.4 |
| 36563454-bd59-36d3-9865-8ffe8323ab37 | -11.9843 | -47.9088 | 2025-09-27 11:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| f21a7bbb-a98a-3a14-9198-a2db9cc6d34f | -8.822 | -46.2564 | 2025-09-27 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| f291e18a-fad0-32f1-ab19-21e9c6858374 | -11.9843 | -47.9088 | 2025-09-27 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 4fd7941d-a286-3f5d-95d7-09eb13fbb01d | -12.2829 | -44.0568 | 2025-09-27 11:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| c8830612-c85f-3628-a2fd-ceb33b17a033 | -12.2636 | -44.0599 | 2025-09-27 11:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 9eb37e15-1d6d-373d-8e4c-e43fcd4394cf | -10.0062 | -46.7081 | 2025-09-27 11:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2bfc2bea-11d6-30fb-8e13-9a20b6360fe2 | -11.9651 | -47.9113 | 2025-09-27 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 64853866-85ab-3330-8e97-71d5daebd731 | -11.3642 | -45.0339 | 2025-09-27 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 336.6 |
| a0ad75ef-fa85-34c3-8e05-aa7882ee82cc | -11.3455 | -45.0135 | 2025-09-27 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 535750f3-ae0d-3eaf-89ba-831a748d20ec | -11.3834 | -45.0312 | 2025-09-27 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 5222ed29-52da-3734-8c1c-5f7a3c609295 | -12.2636 | -44.0599 | 2025-09-27 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 260.2 |
| 109ba853-6e69-3f3f-a2ee-78b214ab98bc | -11.9651 | -47.9113 | 2025-09-27 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f176ad67-3865-3ab4-ad71-9a6d426c426b | -11.9843 | -47.9088 | 2025-09-27 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4bbf913a-ccb3-3aa6-8e33-d5652a9c8839 | -9.3517 | -47.5801 | 2025-09-27 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| cb51e9f6-c551-3c58-a992-54a68935de7d | -7.7794 | -46.9371 | 2025-09-27 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| e5697530-d7b8-3e15-8f18-1dda5b40daac | -11.3451 | -45.0366 | 2025-09-27 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 4e4bcad1-8ab0-30ab-bbe9-686ea925c10d | -12.2632 | -44.0834 | 2025-09-27 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 7b7301fb-5abe-3456-9f08-ca802415631b | -7.7792 | -46.9593 | 2025-09-27 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 531c484a-a1a6-36ef-9d5b-6bc55aa247b7 | -7.7982 | -46.9354 | 2025-09-27 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 531188c8-cd96-3b19-b1e9-e069ad2367d6 | -12.2829 | -44.0568 | 2025-09-27 12:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 923.3 |
| 44748be3-e832-34ac-acc3-0ba6fd8219a2 | -8.822 | -46.2564 | 2025-09-27 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8fafe6a6-5177-3ceb-918d-aefb6691e5dc | -11.3646 | -45.0108 | 2025-09-27 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| e4b59d91-60da-368a-a515-24c66c03df9a | -7.798 | -46.9576 | 2025-09-27 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 6cb94c9f-4a5b-3f30-9b7c-53c882451aac | -10.0062 | -46.7081 | 2025-09-27 12:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0de48d4f-180e-3e31-9bec-e6f1453d5d98 | -7.8637 | -44.5382 | 2025-09-27 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 292ac2de-c53f-329c-a764-5a6c8f212d39 | -8.822 | -46.2564 | 2025-09-27 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 45d071e3-68e0-3061-98f7-7f8606da01a3 | -8.8223 | -46.2339 | 2025-09-27 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 57cde783-a188-3d34-bb1e-0b646a05a4ba | -11.9651 | -47.9113 | 2025-09-27 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| f4567710-b598-39bd-be1c-4a1ff0e0207e | -9.6159 | -47.5741 | 2025-09-27 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6a530fa2-e196-395e-96a6-723552d3a334 | -7.7794 | -46.9371 | 2025-09-27 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| b83e9548-8c02-3a1a-8e28-3409f35b97ff | -11.9843 | -47.9088 | 2025-09-27 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 196.9 |
| bdaa6fb4-bd09-3845-b37f-49e46a756f5d | -12.2829 | -44.0568 | 2025-09-27 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 582.9 |
| a4a1e441-e479-3f0d-bc70-6a1838f6d79a | -11.3646 | -45.0108 | 2025-09-27 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 0f400b2c-51c9-366a-b31a-91d622154cac | -10.0062 | -46.7081 | 2025-09-27 12:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 9198cb1f-d044-3ed0-863d-824042c8991d | -7.7792 | -46.9593 | 2025-09-27 12:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| b642ca10-73a9-37b0-a3f9-71d4f48be893 | -12.2636 | -44.0599 | 2025-09-27 12:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| cc7b21de-b670-304e-b217-915f033adcf2 | -15.5776 | -51.7007 | 2025-09-27 12:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 937f8468-503a-366f-af20-9bf0b2ab1c22 | -11.3451 | -45.0366 | 2025-09-27 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0bd95667-11d9-3485-a837-5d6703660939 | -7.8637 | -44.5382 | 2025-09-27 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8fc4aee5-a335-33e6-bac3-1b114615b36d | -11.3642 | -45.0339 | 2025-09-27 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 349c8065-f72c-3266-bfcf-9420b2744dda | -11.3646 | -45.0108 | 2025-09-27 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 16040447-68b8-3c82-8008-dbb0f0384099 | -7.7792 | -46.9593 | 2025-09-27 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| c55fb1cf-d733-33fe-b458-f08e18c2ad3b | -11.3642 | -45.0339 | 2025-09-27 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| db7bf270-edd2-33be-a91e-58a52d4c39b5 | -7.7794 | -46.9371 | 2025-09-27 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 52f0ebb8-d92a-3e67-a6d5-daf977bf0bc8 | -11.3451 | -45.0366 | 2025-09-27 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b46af9bf-a4d9-317d-9e36-29f3bfd6043b | -11.9651 | -47.9113 | 2025-09-27 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| db57c0f0-fceb-3d4e-8648-b616988d1fa8 | -10.0062 | -46.7081 | 2025-09-27 12:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 5fb189af-000e-3e50-ba34-2cc2dc14946b | -11.4413 | -44.9998 | 2025-09-27 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| fed7def0-2723-3c8c-a6b9-323a7dd78a19 | -11.4417 | -44.9767 | 2025-09-27 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4a0c8f39-9616-37e4-b2f1-e43f3f5d22f4 | -7.8637 | -44.5382 | 2025-09-27 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f2d21d01-0316-33c7-80bf-7b07ae70486c | -8.822 | -46.2564 | 2025-09-27 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| c6677b42-ac33-39a4-af39-0c9573d2a437 | -8.8223 | -46.2339 | 2025-09-27 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3c3fe8d5-cc7f-3d9b-85d9-d187c948dafd | -11.9843 | -47.9088 | 2025-09-27 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| b7dff023-8dab-3da0-876d-8034b52f17cc | -9.3517 | -47.5801 | 2025-09-27 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| aa4edf29-91d3-3b43-a962-81672cab2f18 | -8.8409 | -46.2544 | 2025-09-27 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4f630571-1278-3168-8bbe-9307d38a2981 | -11.3646 | -45.0108 | 2025-09-27 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 147.0 |
| cab6a491-6f25-311c-bc7c-e7d9275e478c | -11.3451 | -45.0366 | 2025-09-27 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 6f5d09e0-c215-36a0-abe1-ec16c76a618d | -11.3642 | -45.0339 | 2025-09-27 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 204.6 |
| dce19ee5-7c43-3bfc-affc-b96b7056a748 | -12.2829 | -44.0568 | 2025-09-27 12:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 3ed4c413-3962-3480-94dd-a21d34e93bba | -8.822 | -46.2564 | 2025-09-27 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| eb0b4b47-6dc6-3ff3-b88a-5683f076f00f | -10.0062 | -46.7081 | 2025-09-27 12:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e4324f22-1bbd-337d-9920-e17c84c5908c | -7.7792 | -46.9593 | 2025-09-27 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0c285b31-3d3d-3dff-b147-239b94f7ecf6 | -11.9843 | -47.9088 | 2025-09-27 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 06e4afaf-23d1-3fa7-8db7-a89d5d641a46 | -7.5568 | -46.7128 | 2025-09-27 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0818e3c3-2d59-3b9a-ab43-3f3994646eef | -11.5511 | -45.2835 | 2025-09-27 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 555e2157-cbf4-3d5a-baa8-2cdba887484a | -11.4417 | -44.9767 | 2025-09-27 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| d0da8e54-f8e0-3960-814b-eca006965302 | -11.9651 | -47.9113 | 2025-09-27 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 595732b9-a602-341d-86a5-b9632693450a | -7.7794 | -46.9371 | 2025-09-27 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 9fdfe70d-60c8-3908-9307-79bda08240ec | -11.4413 | -44.9998 | 2025-09-27 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 154e941c-b854-3ca8-8869-1f3e53eb198e | 1.87692 | -50.82138 | 2025-09-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 246ad7e1-2332-34c0-bd2b-68478d8b10ac | 1.86424 | -50.85958 | 2025-09-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7ab63c5b-71df-349d-8ab7-381adaec6340 | -3.2 | -43.45828 | 2025-09-27 12:34:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| e1b2fad7-70e6-3570-a085-2b472ea8de19 | -1.4517 | -47.17333 | 2025-09-27 12:34:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 99948a5c-cdec-3fb6-af6f-e5361d913a20 | 1.88206 | -50.85713 | 2025-09-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 32.2 |
| d870c1bc-c9eb-3d2f-839c-f739deb00a06 | -2.57726 | -48.96193 | 2025-09-27 12:34:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a66ffb0e-3b91-332e-9548-444f9d7f3558 | -0.9358 | -47.34571 | 2025-09-27 12:34:00 | TERRA_M-T | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 688f7371-a827-33b2-834f-e41f0d02d7f2 | -2.57586 | -48.97169 | 2025-09-27 12:34:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f30c5ca4-5027-32c6-b994-a3a43f0551c1 | 1.87315 | -50.85835 | 2025-09-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 141.6 |
| cd240019-0a6f-3228-ac63-ba0e6228a9d6 | 1.87187 | -50.84941 | 2025-09-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 36.9 |
| f8ee34fe-6851-3ae8-97a4-8958a07d524f | 1.88077 | -50.84819 | 2025-09-27 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 27.7 |
| e595051e-8b51-397a-9018-d86a66740383 | -2.49653 | -49.26459 | 2025-09-27 12:34:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ba486c31-d079-39da-aa77-7231f9c9222a | -2.49519 | -49.27406 | 2025-09-27 12:34:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| fd45256e-050e-35ab-b567-6e5c40dcd800 | -10.72345 | -47.99802 | 2025-09-27 12:36:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e690270e-1a8d-36c1-bdfd-f827f252a86b | -11.60596 | -45.46021 | 2025-09-27 12:36:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 6acc4892-d4d6-3926-8071-3976b2f96f7b | -8.6194 | -54.99447 | 2025-09-27 12:36:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 42abe37f-b630-3a44-a1bc-131f1a211918 | -5.31377 | -46.34469 | 2025-09-27 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |


[Clique aqui para ver as próximas entradas](README61.md)
