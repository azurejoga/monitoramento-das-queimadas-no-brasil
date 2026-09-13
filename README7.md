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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e9bb858-8fe6-3da7-bf5d-b836908f1ab7 | -2.6602 | -57.5119 | 2026-09-13 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 92432f1a-b0f1-3666-a909-f9f786732152 | -10.6829 | -54.1475 | 2026-09-13 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 42cd3972-ddb5-33dc-aa06-00cd63ff9b16 | -3.3293 | -42.2893 | 2026-09-13 00:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ea3bb1ab-efd1-330f-8dd0-bf962f28f314 | -6.1111 | -57.6645 | 2026-09-13 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 37cd7115-f01b-3ab8-84dd-35cf9e22d984 | -6.906 | -34.954 | 2026-09-13 00:40:00 | GOES-19 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 9224a5e6-38d0-3b8b-a5ec-70ad13a0f1ce | -3.728 | -61.7555 | 2026-09-13 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 5fb6f525-e1e2-3b1f-9c8c-d062527e5823 | -6.6021 | -58.849 | 2026-09-13 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 52081816-1f5e-3411-85af-27c7abf67bcc | -6.8632 | -55.5601 | 2026-09-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 906346b0-78f3-32a3-9d2a-b995941655e2 | -3.5743 | -53.0015 | 2026-09-13 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8be161e0-d173-3113-adf2-e30121678214 | -10.7015 | -54.1663 | 2026-09-13 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 90f721d8-e87a-31e1-a144-02b032627e1b | -2.6602 | -57.5313 | 2026-09-13 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 0bc5d56b-bd02-3f78-95bf-0b65425d5549 | -9.3954 | -50.0908 | 2026-09-13 00:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 146.9 |
| c98b495f-c7a4-39b3-acc4-c5815393ad92 | -6.863 | -55.5801 | 2026-09-13 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 8147c43c-2ff2-3922-a4a2-6e7621a08d50 | -2.9579 | -50.3988 | 2026-09-13 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 29da1845-d55e-3055-8a7f-cd089b86185b | -6.121 | -57.561901 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 478704a1-de84-3981-89f7-a0b40a6f7ea6 | -6.0978 | -55.657501 | 2026-09-13 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e41844b8-7875-3fff-b73a-8c247e8d749e | -6.2203 | -51.6646 | 2026-09-13 00:43:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3902d6a-1e44-3c03-90f6-631889f0c8fa | -6.675 | -58.6945 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c5531e7-05d0-323a-95d6-f80d3bb6d7a5 | -6.0838 | -57.852798 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f4edff-de59-32a0-86a5-17b71f49695e | -3.5614 | -52.989799 | 2026-09-13 00:43:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33380857-62fa-3265-a8f7-cb5f4906bb6c | -10.5771 | -51.352402 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c84eb32a-33c0-308a-8a97-02071a181c38 | -9.4001 | -50.0914 | 2026-09-13 00:43:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c38ea91-ecd5-345f-bee8-2ec9c94b1b3b | -4.3509 | -55.681301 | 2026-09-13 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 481102df-f8df-308c-8550-a9a3ae28dced | -12.6588 | -54.719799 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2e89fb-0c1a-3196-b438-df4fb7f1d9ed | -3.7341 | -61.746399 | 2026-09-13 00:43:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6348eec0-12ad-347f-b2f0-91410cf653c2 | -2.6117 | -54.749199 | 2026-09-13 00:43:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdde7860-616e-36ef-ba51-fddf9e84cad8 | -6.1134 | -57.665199 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25b8bc26-217b-3357-ab81-57be94d153f3 | -9.5803 | -55.1511 | 2026-09-13 00:43:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86262b69-6de8-399c-9b78-d332529afe7a | -6.7397 | -55.624298 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b470baf-7f3d-3633-8374-b74a0bf58079 | -6.1734 | -57.7024 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78508e6a-a9ad-3850-a2b2-d03aaa55019b | -15.5673 | -53.771198 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 328e5af7-c2c3-3e12-adb2-686431733fca | -10.6777 | -54.146301 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2b9b350-6ff4-3148-b973-45c550d4643e | -6.3062 | -59.947601 | 2026-09-13 00:43:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf0db12d-8a35-300d-b22d-4c85d6b62504 | -2.5387 | -54.655499 | 2026-09-13 00:43:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd6925a-2962-3cf4-bd22-e00916b0ae26 | -6.1765 | -57.716202 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cd219da-2ad2-38e4-8532-5baeaef43c54 | -8.033 | -54.840401 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7acecb8f-b4f8-3346-997d-20085346e97c | -13.2998 | -51.7127 | 2026-09-13 00:43:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d813a865-1aca-35e6-aa56-7cb075c38155 | -6.9568 | -59.728001 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 997949a0-3ed8-3626-afdc-f6312b6e8a56 | -9.1838 | -59.429901 | 2026-09-13 00:43:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 494a35f4-b114-3191-894a-0a66aae65681 | -12.6801 | -54.722801 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| af61c826-7e56-3f90-b26f-7e08311f16ac | -8.0232 | -54.842701 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57144aec-1b49-3d5c-9383-0a0a9f9a2c31 | -6.5868 | -58.8521 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 709ac446-ab62-3960-b0b9-375d3cf8465f | -5.9875 | -57.700699 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d80ba75-f97b-3f46-9f1b-4a7f701895e9 | -8.5477 | -54.702702 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ed39bd-452e-3f13-92e5-32508644d978 | -6.8501 | -55.566299 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09a108e3-4b71-33d9-8cfe-343c818308e8 | -6.1554 | -57.713699 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17123cf-4838-3778-87ed-9b5eec9bc56e | -10.5132 | -57.440498 | 2026-09-13 00:43:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff93e6c2-5f63-3c9d-8dfe-c1ed73fce79e | -8.5322 | -54.6805 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c7ab1e-fda7-3bc7-8c58-21dd7862751b | -6.5951 | -58.842999 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2aedd1c-93b7-3c2e-916a-eeb5fc1e816c | -7.852 | -54.683701 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3a2bec8-a7ef-3ecd-aba0-892a1c45b61d | -15.5593 | -53.781399 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0c50b89b-6211-3240-b598-fb28bca2db2f | -2.954 | -50.4086 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa267458-dc17-3a80-9214-a7fafacaf460 | -6.3769 | -58.284302 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a99074b8-0eae-350d-94f0-70701918e5a4 | -6.2137 | -51.680199 | 2026-09-13 00:43:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcfae557-8109-3dc9-aaf3-ba0c119c1f6a | -8.0525 | -54.8358 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea3c2899-5581-3956-aeb6-3b175ed2e17e | -5.9706 | -57.762501 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1b300d9-9040-3a9a-b968-ffa8ca019447 | -15.5514 | -53.791599 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4a8fe78-62a4-3cd4-b064-9f2faa210c4a | -6.1718 | -57.695499 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f998d873-61f1-3ee7-9efa-5696baf8c34c | -9.7138 | -54.349701 | 2026-09-13 00:43:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d04b3387-076c-39fd-a119-1198b3bcd5d3 | -12.6651 | -54.7024 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3f83df-bb23-3065-a9b1-3b8f067ac229 | -12.8295 | -44.341999 | 2026-09-13 00:43:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bb3b0f8-e072-3c40-bdc0-ce22e84e5007 | -6.7979 | -58.783298 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0cc62ac-1d88-3089-9a0e-8fc80acc0b5b | -5.487 | -57.221298 | 2026-09-13 00:43:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2febed4f-3462-37e3-9610-e075937d4671 | -5.9804 | -57.7603 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce930574-2a57-3695-8d4c-97bee7edbbf0 | -15.5575 | -53.773602 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ebd186e-06d6-3dce-b55c-fb9283791d91 | -2.7145 | -57.629398 | 2026-09-13 00:43:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 082b8d7d-fac4-3bc0-91cf-2bd9b13fa0e6 | -10.5285 | -51.364601 | 2026-09-13 00:43:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b42f5907-c83b-3770-9007-6add52ce310a | -6.8258 | -58.631802 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3b6501b-9aa6-31c4-9f3a-d5d537812d44 | -6.6162 | -58.845501 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5735910e-c47f-33dd-b7b5-820014d806f4 | -3.1577 | -58.629299 | 2026-09-13 00:43:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b12479db-d5f5-33f8-8d19-f3c9991be444 | -3.0391 | -51.245899 | 2026-09-13 00:43:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe707c13-6136-36c3-abf8-f29a55364e9f | -12.6571 | -54.7122 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb1ccdd2-f72e-3dbc-914d-4cdf23119dce | -12.6784 | -54.715199 | 2026-09-13 00:43:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 575d37a9-9287-3a91-a0ce-da44275778b0 | -8.1153 | -54.795502 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f98977c9-3d6e-3240-b104-4c8cb8c4c709 | -6.0626 | -57.8503 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2e434ad-cf15-3dea-8362-0bf750a27a27 | -6.5904 | -58.822201 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60efc0b7-2128-36c5-9fa3-6c68889c80ed | -8.0428 | -54.8381 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba9ab85d-79b4-3e98-b9c4-d26f05fc2a7c | -10.6815 | -54.162701 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8637ac3-08eb-3785-8c21-adbff535849c | -6.6714 | -58.8624 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed091c19-c94b-3b55-9406-5dd2fc3f9ae6 | -15.5709 | -53.7868 | 2026-09-13 00:43:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe61b975-0dad-3593-a7f5-404c6a70f8b0 | -9.1822 | -59.6101 | 2026-09-13 00:43:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 443df705-4eab-3d58-9a26-831b4164b98a | -11.2403 | -54.124298 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a959c509-855d-3891-b9a3-1bbe5c7db9a2 | -6.6049 | -58.840801 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49de2614-cb0e-337b-b941-3e0258789609 | -3.3833 | -50.750999 | 2026-09-13 00:43:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a125742-69a5-32df-ae73-3d76259badf3 | -2.5365 | -54.645901 | 2026-09-13 00:43:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04bd1117-8a7c-3830-8ee2-71c0d7fcd128 | -6.6064 | -58.847698 | 2026-09-13 00:43:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0838a141-a883-3c91-848f-4fa1cec9f5c4 | -10.6913 | -54.1604 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8b62de-6c29-3c7c-a9dd-cca16d86775f | -6.855 | -55.275398 | 2026-09-13 00:43:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 853b7f4a-9514-37c0-9225-404ecc4bb25a | -8.0134 | -54.845001 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ac0c7f-6773-34a5-bfc6-6d356b020640 | -5.969 | -57.7556 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a10e3ef-a3f8-3510-81f7-b73aa49ceae6 | -3.6389 | -58.615299 | 2026-09-13 00:43:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a32ea85-b0d9-314a-966e-313c1e03325b | -6.8 | -58.884899 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cadf5be0-3c52-32b2-928d-b1321a221137 | -6.1311 | -57.697399 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4ed5be-5e48-34d2-a2d1-3d726fe55175 | -6.7521 | -58.946701 | 2026-09-13 00:43:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1c7e8f6-0fec-3e31-862b-6e70d8675095 | -3.5957 | -59.062199 | 2026-09-13 00:43:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 857b0e73-81fd-3816-8c84-b349d0573606 | -11.2441 | -54.140598 | 2026-09-13 00:43:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 895acaf6-6c8a-3be9-9983-66eb933653d2 | -5.8174 | -53.7873 | 2026-09-13 00:43:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb5d6bfd-31cc-3b43-910e-4128af242faf | -6.0953 | -57.676498 | 2026-09-13 00:43:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6adc9c00-43cc-338c-a665-eb03de23f6b4 | -3.3099 | -59.348301 | 2026-09-13 00:43:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2be47f36-fde7-35d1-b520-92f1496d4c6c | -1.7278 | -55.832401 | 2026-09-13 00:43:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
