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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e41ba83-0467-3ae7-9e14-ec9ecbc85dcb | -7.55877 | -61.3343 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9df9a5eb-b917-3183-bcb4-95e6aa0eda42 | -10.67796 | -50.73347 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd3604b2-feb6-303b-bcdc-4609eed06376 | -9.17179 | -60.85416 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8a89ce0-1fb5-34dc-ae44-f93b87c97487 | -9.46669 | -45.36638 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb068d9a-8aac-3b6d-8217-13b336b02091 | -11.27742 | -54.12913 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 262b2053-6271-3190-a971-9bbb6e469bed | -10.91165 | -53.96157 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b875e263-6fae-3963-8a9b-94322280d2cd | -11.28486 | -54.06015 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55ec930b-d9bf-38ee-a628-e6e75d78ed5e | -10.89139 | -53.97538 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73cc0092-1b05-368e-b807-4df63dd00b48 | -9.67205 | -53.58775 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99e51b7a-05f1-3657-a625-6a52e0ec63d4 | -8.18581 | -54.76925 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8ef2b7c-0046-39b5-8816-500b5e89f7cd | -6.75349 | -59.09026 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1883f99-5b0b-36b1-8a7e-194f95b8c3df | -12.30705 | -50.68857 | 2026-09-21 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 804421ca-074a-317d-a9b6-0c55174962e2 | -9.12311 | -58.92231 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a143ccd-a806-38e4-b1cd-07376d87bbf9 | -10.46019 | -61.31225 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b80c29-4fc5-3a9b-a3bb-e3a64f1fc79d | -8.65426 | -54.79879 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f6cc82-e55f-3f96-883f-6509b14a018e | -10.10106 | -69.13568 | 2026-09-21 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3650af5-c13e-3ff2-8b62-8b5b56b8799b | -9.45557 | -45.40673 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| ea0c0c05-ae93-3d56-956b-eab110bd558f | -8.18471 | -54.77653 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3671ea6e-500c-3415-bbf8-271cf5e505be | -8.54108 | -54.69156 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4478b655-f7e4-315d-9bb2-e94cad9e770c | -6.7761 | -58.90612 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7220dd21-8701-33ec-9414-cd6cc829c064 | -11.04606 | -54.90832 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 543ed1a6-3b5f-30d8-9d3b-56efda5e5200 | -8.08451 | -55.34438 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 786f93f6-79f2-3f12-9ea0-6382c3e4013c | -10.4782 | -50.28138 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9576491f-c854-37ba-b73b-0061cf06ca1c | -12.89895 | -50.96589 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37ddcca8-00aa-3e73-a5f3-61283a376559 | -10.14995 | -47.68049 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4ec58c-36e5-3f9b-87e4-479ac8920bd7 | -7.58534 | -57.68172 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c54a6ae3-d782-3ce9-b076-56f556b65815 | -8.78865 | -48.74035 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b34b06c9-2f8f-3ef0-8218-7a30a2e9114c | -7.97301 | -62.04277 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc44c92-31a5-3223-b4ea-8123f1be687c | -11.28049 | -54.1143 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fac01e1-cc65-3e86-bc12-76a9f90af266 | -9.73887 | -54.81432 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| faa380d1-305e-3e95-8685-18052baf0adb | -11.04663 | -54.90453 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2f1b98e-1690-35fc-ae68-287bf9d82fe9 | -7.3787 | -55.55768 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16fabf7e-d9f7-3823-9236-709adc4f6b0c | -10.76161 | -50.80116 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 4653d7e2-f6a7-3bf6-a55e-bd78aee22e57 | -10.88448 | -50.93402 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed3ee0bc-2ae8-3d66-a5f4-89c9f60c38bf | -10.85487 | -50.15567 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08f148c8-f947-306c-a17e-e1a0117d391d | -10.91942 | -53.95851 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49e5997f-e40f-3949-9d7a-d351293fd8d8 | -10.38313 | -51.87104 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c91cc28d-4634-3493-b427-42d398b89d55 | -9.93604 | -60.72882 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9bd53a3-66c3-3009-944b-e6fb33051e05 | -11.75191 | -54.56932 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60c39a95-e163-3751-8862-18e2bba61bd5 | -11.37707 | -51.44189 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44bc9742-607b-321e-9b8a-2a7e0a2d959e | -12.41968 | -47.03213 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 67d5e562-0855-3f9f-8c2f-d26db319381c | -8.19861 | -54.70765 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7420b88f-a808-363b-9019-5bedd5c5fd97 | -9.89624 | -57.06077 | 2026-09-21 05:06:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8215598f-6b36-3f8d-ab32-cb926ff17338 | -9.02759 | -51.51857 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6fff67f-f123-3dfc-b4cf-fe97e9f4ed99 | -6.75098 | -59.06054 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 327f0762-fca3-3be4-aec9-7f39295b203a | -7.52094 | -55.27502 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00930f83-fa9d-383f-b421-ffd46872799e | -11.0986 | -54.01678 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e630664e-6b0b-379d-b11b-56de4cb9459b | -11.95229 | -46.49588 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a0db404-d35f-3f0d-8f15-9e7cf7e75230 | -11.05352 | -54.90555 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ce94e3c-27f3-3c48-a47e-8464e592ad03 | -6.57476 | -59.00828 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6191dcaa-b6ee-38f2-b6d4-33d534cc0299 | -7.59381 | -57.67198 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0b90ddcb-68fb-34c7-8b9c-84a3a3ebdb44 | -8.18636 | -54.76559 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37f374d2-7da3-323e-b1a9-7b5915baab50 | -10.093 | -48.40745 | 2026-09-21 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fe8d964-1031-3099-8bf6-28f28a355cd5 | -8.18526 | -54.7729 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ed3db1-fdb2-365b-a0f4-b5b5fee0029b | -9.1193 | -51.57563 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6805a81-27a9-34a9-ae9c-3e60797f202b | -6.44901 | -59.97753 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0945949a-9af9-3cc8-a758-2c4e094aa82c | -8.09784 | -55.34644 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7cc3489-4a62-3d63-a3c4-87dfc75af32b | -8.19238 | -54.70294 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d17774e-c15c-3bce-a005-60ee79b7b1e0 | -9.74817 | -65.05554 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d71d133-af9f-313d-b0e7-9ecba16a6c7a | -10.71497 | -54.02266 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b3a338f-7084-3537-804d-f333b74a5740 | -11.73555 | -54.55867 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 728a83a3-c744-3dbd-ac23-17ee55f29834 | -8.35252 | -50.85867 | 2026-09-21 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cf0cd34-4a32-3f24-ba31-c7ac89d85da5 | -9.28584 | -60.61352 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c407cd7b-e48c-39b3-9b13-82ed7dbaedbe | -7.24877 | -55.60474 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7776953-6c27-3f30-ace7-e74f13325787 | -13.26891 | -51.74409 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a49ad0df-eec4-3eb6-b9b5-078314e0fae3 | -11.98926 | -58.06857 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3de48fe4-44eb-3602-b0a8-e6d935bd5155 | -11.05614 | -54.90894 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f786d2d5-b193-3baa-92dc-e273ed8ba8d1 | -9.44895 | -45.40514 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| acbdeb00-0999-3832-898d-d084ba1b3ede | -9.67939 | -54.34658 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dc02dc1-e8ce-3f90-94b2-ccee375ad4d2 | -12.86899 | -50.9556 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb44cc8a-b5fb-3d9b-8808-b6279cfdc775 | -10.87771 | -54.09519 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 687f52f6-ea80-3b98-9cc8-c996007f3c37 | -10.89436 | -53.98006 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8f72603-ffb7-328b-871b-3697aece542e | -9.29935 | -60.53101 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7992eb80-3e25-3bbf-a200-5ee53bba07de | -11.86932 | -49.97955 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a494eef-240c-3cea-b3b6-094cc0ca3b68 | -11.83718 | -46.81947 | 2026-09-21 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ed06d97-88dd-3774-9e5d-95a86991f2af | -8.08172 | -55.34032 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecf89dd-0f85-3dd8-9c0f-a368c6c3ece2 | -9.55257 | -66.02991 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b87dc94c-f122-3258-8361-2069a8da4468 | -10.86056 | -54.1134 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34fd28c5-bdc8-3602-aa34-feeee335ec3f | -7.57283 | -57.68302 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 62fa51e1-5f51-3dca-b154-5a4fabaa3246 | -9.74935 | -46.2414 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 319faffe-816d-313f-ac65-4ae1301fb582 | -6.79922 | -59.13871 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54befbf2-81c5-32e1-b242-403fe776f854 | -7.24823 | -55.60822 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b9776d6-b1f4-37af-9e72-0000828900a8 | -11.46976 | -47.77256 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec7d8808-46c0-317c-a940-68aeda84d672 | -7.86525 | -62.53587 | 2026-09-21 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4136a3e1-3a87-3902-8302-8d86aea7e9a9 | -10.42311 | -50.2506 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d359c6cd-d2e8-3ab5-9c6e-93bd5d663bb8 | -10.42039 | -50.24859 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85e7243f-488b-330f-889d-7abc1d4757f0 | -12.73751 | -54.51009 | 2026-09-21 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e265dde1-3e31-3a9d-958c-c8bc5bc017c9 | -9.97716 | -50.26485 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f19fa36-8a8c-3546-acec-57a95a083b6b | -13.86321 | -48.59021 | 2026-09-21 05:06:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 020c3f0f-2fb4-319c-a771-5694d46b4d46 | -8.61697 | -54.60807 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ee59544-1145-32cc-8211-54bedea5de0b | -10.37991 | -48.91874 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b8afe155-ea4d-3ec5-96d8-09872f276760 | -9.76636 | -46.06086 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e10ea263-5fd3-354b-93e9-917a867a3090 | -9.82273 | -48.44329 | 2026-09-21 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9ebd94df-35ef-322c-bf66-55c0b281f667 | -7.86592 | -54.70591 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf7f2c9b-f72e-394d-8745-ab1fe3aad60a | -10.8717 | -53.95977 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38925fb6-e8f7-3346-a871-e1647f0fa0b0 | -11.1296 | -54.00468 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2711dfa4-7221-3f0c-97fc-e70dddb8b735 | -10.54385 | -57.44136 | 2026-09-21 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a8e6ee8-dfe8-3dbd-b9ea-b8cc77f0233a | -11.04508 | -54.16453 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5588253-bf6b-3693-ad6b-4b017bfe9fde | -13.17524 | -43.56933 | 2026-09-21 05:06:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 9613fcb8-d46c-3b61-a534-a5dae5f3fcf5 | -6.45047 | -59.97102 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README71.md)
