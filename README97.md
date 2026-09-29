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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44698e91-3ceb-31f2-95a5-baacaa3824ab | 1.9241 | -50.8202 | 2026-09-29 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4d34819e-33af-39b7-acf2-047b493d25cb | -11.0767 | -51.3674 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| a5010009-fd7e-3544-a562-926f37d2b4fc | -11.7834 | -51.0152 | 2026-09-29 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 47552e48-60a0-3ea7-9524-daaf6ecdaa99 | -11.0991 | -51.1111 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| a0c80ce4-1644-35c2-bb1d-fc616f7c3914 | -11.1364 | -51.1496 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 2892e618-3fad-371f-8c7e-710d7bb286b1 | -11.7513 | -50.6137 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 99331df3-ef3a-328e-a2c1-1f5d5b951fcc | 2.1082 | -50.8583 | 2026-09-29 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 6b0bc027-21c3-3d06-a9d3-bfb08512557a | -9.9781 | -50.1626 | 2026-09-29 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b32001ed-3626-3eb9-80fd-218a780efda8 | -6.9795 | -71.755 | 2026-09-29 16:20:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 514.0 |
| 6aae6c87-f4c1-3dd7-9d68-1ea184fb7195 | -15.3998 | -47.9261 | 2026-09-29 16:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 943ad4bf-6b7e-3466-ae69-9f8a83214e3f | -1.4672 | -48.931 | 2026-09-29 16:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| de1b4bcf-4fb6-3fab-9dd1-2a7449c51242 | -11.9929 | -50.9913 | 2026-09-29 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 94c0b143-e1ca-377b-acd0-a552da4d53cc | -11.1359 | -51.192 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 58288fce-76bc-3bdd-876c-6ded22db5840 | 2.1266 | -50.8788 | 2026-09-29 16:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 22436be4-8448-3225-a67c-0dd4db545a52 | -11.7129 | -50.6394 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 0044c9ec-43f9-3133-ba3a-834659dd0b29 | -20.9159 | -57.8246 | 2026-09-29 16:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 125.1 |
| 10e8e1fa-8a50-3be6-96a9-346c0a14a624 | -10.9722 | -50.6998 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d9ffde2f-c952-3cd0-9f6d-18762267bc97 | -6.9795 | -71.7732 | 2026-09-29 16:20:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1170.7 |
| c915139c-ca48-31a1-a9b4-ef8f37c0570d | -11.1361 | -51.1708 | 2026-09-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 4671d861-f317-3530-8a5b-476991d88347 | -11.7319 | -50.6373 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 001d4e07-6921-3979-b938-8a7f2b6039b0 | -11.7828 | -51.0578 | 2026-09-29 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 652f6768-ee4a-3da1-b55a-406963f31fdc | -11.8669 | -50.5147 | 2026-09-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 2d499843-af21-3fb5-b459-17517352d041 | -11.8611 | -50.8999 | 2026-09-29 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.2 |
| a292f410-878b-307a-bf9f-a0a94fa3a406 | 1.9241 | -50.8202 | 2026-09-29 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 451f23bf-f674-3473-9133-0a6bc6b54765 | -11.8802 | -50.8977 | 2026-09-29 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 39ebe0ce-b03e-31e5-b7a6-0ba5692dd702 | -11.0991 | -51.1111 | 2026-09-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 22851cd0-e9ac-33aa-9509-3241cd19a1c5 | -11.1178 | -51.1304 | 2026-09-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 350bfe2f-4ceb-3762-a02e-dbfa5b7823ca | -11.0988 | -51.1324 | 2026-09-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 38361cfb-a333-3292-91d5-a26c8170962f | -11.5628 | -50.5069 | 2026-09-29 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 5bf04d0c-f56c-346f-85dd-6d498398499c | 2.1082 | -50.8583 | 2026-09-29 16:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 88.8 |
| fa5dd503-408b-315b-a18e-5839a2ec86d9 | -10.9912 | -50.6978 | 2026-09-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 0a23a592-bfe8-3984-831f-915918622f23 | -1.3193 | -49.061 | 2026-09-29 16:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ca57a26c-5769-3b7c-a83f-ef1cc402d33e | -11.1364 | -51.1496 | 2026-09-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9d38c664-392c-3515-8a5b-6a8522f131fd | -11.8662 | -50.5576 | 2026-09-29 16:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b46102a8-f0dc-30c2-99b5-b68a635c168d | -10.9154 | -50.7059 | 2026-09-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 0467bfed-9779-3cae-856e-941825f32625 | -12.4351 | -44.1497 | 2026-09-29 16:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 403.3 |
| fd88256b-9b68-35c8-b54d-d5567f374584 | -12.1362 | -50.3328 | 2026-09-29 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 28f2d664-7ece-34ed-978e-693583068969 | -1.3193 | -49.061 | 2026-09-29 16:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 4b513521-0c3a-3ef6-8640-616949af8259 | -11.1178 | -51.1304 | 2026-09-29 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 0d05b572-4f2e-3819-9b4e-e0c67c7d797d | -11.7828 | -51.0578 | 2026-09-29 16:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| c97cdfb7-eed2-3054-a1af-c1385aae62fb | 1.9241 | -50.8202 | 2026-09-29 16:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 7e7ca4d4-cc5d-3e16-a8df-e16848823ba4 | -12.4351 | -44.1497 | 2026-09-29 16:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| b448e99c-b440-3862-bebd-05e6ea207416 | -15.3998 | -47.9261 | 2026-09-29 16:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| ab707e65-6f03-398e-bbd7-827ed39577b7 | -11.7643 | -51.0173 | 2026-09-29 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 224879c7-0740-3a5c-9a23-ec95ff554fcc | -12.4351 | -44.1497 | 2026-09-29 16:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 454.6 |
| 09e941ae-e77a-34e4-b2a1-0b3707c6a761 | -12.4351 | -44.1497 | 2026-09-29 17:00:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 89e97b35-367e-3822-a61a-f51eb3ab61e0 | -11.0767 | -51.3674 | 2026-09-29 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| faf7ebb6-7438-3665-83b9-27847ad3e475 | -11.7643 | -51.0173 | 2026-09-29 17:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 314e301d-2bc7-3e10-90b9-5b98c095bcde | -11.1178 | -51.1304 | 2026-09-29 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| b8f5b6cf-187f-32e7-996d-df5c96188ad8 | -12.1175 | -50.3135 | 2026-09-29 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 49b092d0-32ce-339c-976d-8352a23c3fbd | -9.997 | -50.1607 | 2026-09-29 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b0d3704a-53bd-3a33-9319-7c59a0883363 | -1.4303 | -48.9102 | 2026-09-29 17:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 295de138-d372-3ff9-9040-5d989c10a8f0 | -12.2696 | -50.3381 | 2026-09-29 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 3cc8783c-f346-30e8-a075-4dd139f86e70 | 2.1082 | -50.8583 | 2026-09-29 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 84.8 |
| eff46530-b9e4-3596-be12-e9f2388a73d2 | -11.1178 | -51.1304 | 2026-09-29 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.6 |
| c2f8b606-23dc-3e33-8abd-93f7c66e584b | -11.1364 | -51.1496 | 2026-09-29 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 6d156727-3b98-346c-88b2-5eaa4117374a | -11.8853 | -50.5554 | 2026-09-29 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 728e0bae-3e18-3476-801b-3164551ed064 | 2.1266 | -50.8788 | 2026-09-29 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cccee3ce-9eea-3d89-8e95-c0fa0c866b69 | -11.7828 | -51.0578 | 2026-09-29 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 7a83435d-9c3d-3d4b-a031-af083c4a5c86 | -11.9047 | -50.5317 | 2026-09-29 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| a434301e-4ca9-335f-a4d1-12e5a1466992 | 2.1082 | -50.8792 | 2026-09-29 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3b8ed18c-18d2-3088-bf25-66a18f4e4f6c | -1.4303 | -48.9102 | 2026-09-29 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1db848e6-ac3d-363f-90dd-993b53d45e34 | -15.3998 | -47.9261 | 2026-09-29 17:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 42e36876-3296-3963-afc0-4a54ddfc39f8 | -12.1557 | -50.3089 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 86e2ef94-a168-3ac3-88fb-496334d4f4bd | 1.924 | -50.8411 | 2026-09-29 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 826ccc0f-e88e-313f-98c5-475c959ec26c | -11.1364 | -51.1496 | 2026-09-29 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| d320073a-b6c8-364a-b022-370082884813 | -9.9582 | -50.2499 | 2026-09-29 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6cc7a921-e9f0-3fa1-8b19-f4cfab84b0f9 | 2.1082 | -50.8583 | 2026-09-29 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ce011c80-b018-3b14-a215-e10be7db02ba | -12.0806 | -50.232 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 2e71b28e-aeb7-3a2b-9299-0dcc9be6754f | -15.3998 | -47.9261 | 2026-09-29 17:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| c6ec94d2-2bf5-37e1-9551-6044c0180dc2 | -11.8472 | -50.5598 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 338d78a6-f9fc-3adb-beae-59da2383f518 | 2.1266 | -50.8788 | 2026-09-29 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 09f1f69f-fc41-3275-b872-f70248eca2ed | -11.8669 | -50.5147 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 0bf1c588-8de3-34d2-9a00-b4c6a7dff0ca | -10.7056 | -50.8341 | 2026-09-29 17:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 176.0 |
| fefc5ac3-1ec9-3953-8a3c-5bac51e190a8 | -12.1747 | -50.3066 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ca2dde28-26f8-308f-afbe-6112c8e619c4 | -11.8662 | -50.5576 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| d7ab66c1-ee9c-3b15-893b-917caaedc6fd | -12.4351 | -44.1497 | 2026-09-29 17:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| a5f97760-7c79-3f9f-aad4-87e159472b01 | -10.2254 | -50.0093 | 2026-09-29 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a59f2077-5448-37b2-b6ac-b9fb4a7eaeae | -9.9595 | -50.1431 | 2026-09-29 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| b3c6492a-cb3e-37ca-9386-405079475d12 | -11.1178 | -51.1304 | 2026-09-29 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a712b774-4677-32a4-a3aa-f0e231e8baee | -20.8373 | -57.6891 | 2026-09-29 17:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| a6e17520-9486-3838-9986-5f153bc7e4f8 | -11.9964 | -50.7563 | 2026-09-29 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 6f096c39-4c75-3cda-9b00-c6886dc5c3ed | -12.0612 | -50.2558 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 0e87009a-607b-3f28-bf66-59b1ce9ba2bc | -11.1359 | -51.192 | 2026-09-29 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| df24821a-43fa-35a9-b5da-736e0dc6c043 | -11.8853 | -50.5554 | 2026-09-29 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8c3119d5-611c-3425-9af5-a2c9727765ae | -8.0262 | -72.3298 | 2026-09-29 17:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c0cc110a-32c3-3ff9-a67b-65b6644735fb | -11.7828 | -51.0578 | 2026-09-29 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| db9a1012-b595-31ab-ad65-585f290803c1 | -10.8967 | -50.6866 | 2026-09-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ac9f7147-d78a-3db0-ae62-5d8f4b2e85d9 | -12.0618 | -50.2127 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| e7a89c43-02a2-354c-9eba-a433252980a5 | -12.4351 | -44.1497 | 2026-09-29 17:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 82fec758-f1f5-3f79-b901-52bf6d547db4 | -8.0262 | -72.3298 | 2026-09-29 17:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 49cbe4cb-bfc3-35b9-9303-25102cbae76e | 1.675 | -55.9028 | 2026-09-29 17:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5b808613-5a38-397b-87b0-734d90f5bfd9 | -9.9595 | -50.1431 | 2026-09-29 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| cc89aa4e-0d57-30a0-aa2e-402907fae791 | -11.9402 | -50.6987 | 2026-09-29 17:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 66851fe5-f668-3c21-98dc-08c744540181 | -11.373 | -43.4446 | 2026-09-29 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 51dcc4ec-48b7-3ea6-8abb-51338c3d02fe | -9.9396 | -50.2304 | 2026-09-29 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 8ca099b8-b6cb-36dc-a1ab-175e4dbf9e08 | -10.7056 | -50.8341 | 2026-09-29 17:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 44a69bbf-7037-39ba-8b65-a9671a42d1fd | -11.1178 | -51.1304 | 2026-09-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 8de1795c-d1e0-3a99-abea-ee3e5e41b207 | -10.8851 | -50.1539 | 2026-09-29 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 87c092b7-6159-3288-a89b-e22bb545f4e7 | -11.8097 | -50.5214 | 2026-09-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |


[Clique aqui para ver as próximas entradas](README98.md)
