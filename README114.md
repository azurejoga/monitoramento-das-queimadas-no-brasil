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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64b0b0db-a6b5-39e8-85da-f38f8cdd4d5c | -6.7778 | -47.8763 | 2026-09-20 12:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6e8517ad-7722-3b07-9b51-efbd2da1cecd | -14.6661 | -46.6919 | 2026-09-20 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7ddfa2b6-0ada-3c87-b1d0-23daaeb03759 | -9.8394 | -46.4586 | 2026-09-20 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 02c6108a-bc80-391c-b73f-34c91c86cb51 | -12.7621 | -46.18 | 2026-09-20 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 92c97657-4882-30e7-b0b8-f7f04f8b572a | -9.8397 | -46.4361 | 2026-09-20 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 378.2 |
| de903c85-6aaa-34f1-bd4e-ee57c8883708 | -11.4537 | -45.3892 | 2026-09-20 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 223.7 |
| af2f853c-922e-31dd-bea6-b441aaaadd34 | -7.5334 | -45.4367 | 2026-09-20 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 87515388-4823-3d12-b86c-1f5a21277adc | -8.8636 | -45.9596 | 2026-09-20 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 10313c0a-cd2e-3376-b911-9647e1e03819 | -7.5522 | -45.435 | 2026-09-20 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 5d25ccc0-5376-3d9c-9f36-2a9ae975bba8 | -12.152 | -47.0383 | 2026-09-20 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 04de2049-9370-3bcf-b07a-928e63cf4a5a | -7.211 | -44.0252 | 2026-09-20 12:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 150.1 |
| d18b63c4-4b0d-3820-b051-81a6d3595289 | -13.0298 | -50.6089 | 2026-09-20 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f326a41f-2b7b-3ae2-b336-004de9962774 | -12.6423 | -50.9144 | 2026-09-20 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 6cbc1d01-342f-32eb-95a6-56230c903db6 | -14.6856 | -46.6886 | 2026-09-20 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 69ff043d-eb55-306a-a034-69e7d7b4477c | -11.4924 | -45.3608 | 2026-09-20 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 610946a2-6fcd-3895-b9f1-8dda77448ff1 | -11.1183 | -54.0062 | 2026-09-20 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 3a255f77-5745-3980-b233-12faef223001 | -7.211 | -44.0252 | 2026-09-20 12:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| eaec015e-4a6d-3bcb-b68d-4f8ac089cfd2 | -10.7899 | -46.3429 | 2026-09-20 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 34311a2f-bf22-3c09-9825-bf18420906ab | -12.642 | -50.9359 | 2026-09-20 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 45487540-fb81-3fb6-ab04-41642e2cb8e9 | -11.379 | -51.42 | 2026-09-20 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 240.8 |
| 1067a169-340f-395a-b10b-dc0aebf8c77d | -10.8367 | -50.9266 | 2026-09-20 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b5534d42-9e07-3cbd-a896-fe20686b1cee | -12.6423 | -50.9144 | 2026-09-20 12:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 964e0933-e7d6-3efa-a86c-b2a09a507de5 | -9.2606 | -45.9164 | 2026-09-20 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 6afe1079-ab78-3c13-8939-4ad3641aeff5 | -6.4486 | -59.9717 | 2026-09-20 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 34bc2cda-b2be-33d5-a6b3-bc1f2638e111 | -10.6 | -50.2486 | 2026-09-20 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2131e819-e121-3f4e-b096-520c7ca48dbd | -6.778 | -47.8545 | 2026-09-20 12:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| f33badbd-efe1-34ff-994b-2a0b5c92479f | -11.0065 | -48.3187 | 2026-09-20 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 437b24c2-11c5-3725-94d7-f22f3687a934 | -5.841 | -53.5205 | 2026-09-20 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a9275296-98eb-3437-bc11-819c6762052f | -11.3787 | -51.4412 | 2026-09-20 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 77a50e04-1616-3a15-b4df-c46d0b7fcaf8 | -9.84 | -46.4136 | 2026-09-20 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| d7ed0a22-ac94-3528-ac44-c80715046b50 | -11.4924 | -45.3608 | 2026-09-20 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3e2afa94-9eda-327e-afa9-48e925308c88 | -10.8364 | -50.9479 | 2026-09-20 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| eb282ed9-1c7a-3813-967c-e757ca49ca6e | -11.0991 | -54.0285 | 2026-09-20 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 0625baac-89a4-3e6a-847d-4e96106d667d | -15.4174 | -53.0236 | 2026-09-20 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 168b17c7-1580-3f0d-8ae6-70b080b7f610 | -8.7729 | -44.2568 | 2026-09-20 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 3b541a6a-c8ce-3784-81f2-88aadb1b409b | -12.1328 | -47.041 | 2026-09-20 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| cfb203cf-19ce-3d98-9e6a-41c98301a254 | -12.7625 | -46.1572 | 2026-09-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 0e5c7c95-94d7-3211-9f9e-6f5e6fe9d01b | -13.2606 | -51.7335 | 2026-09-20 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| fb728261-e811-3fa4-89c8-fb9f4e8c718f | -8.1376 | -46.8155 | 2026-09-20 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 63de1c3b-aef1-36bf-a6d9-b517ce4f1d1a | -9.8502 | -48.4053 | 2026-09-20 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f55700c2-efc5-3d42-9e22-70664cac0a65 | -8.4317 | -45.8241 | 2026-09-20 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 600660c9-621b-3fc7-990a-dc62b89ee8e7 | -12.7428 | -46.183 | 2026-09-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 14dbf69a-2be4-3d35-a80a-6bfaaeecfdee | -11.3977 | -51.4392 | 2026-09-20 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a385b6d6-aa1b-3ca6-8b12-1a96abb33276 | -11.118 | -54.0268 | 2026-09-20 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 169.6 |
| de2a1253-7f57-3137-b832-91553a42efcd | -14.1458 | -45.5638 | 2026-09-20 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3316e133-034d-3b11-926e-ec000a8c9b17 | -8.4376 | -46.8757 | 2026-09-20 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ab9f6a77-e170-305c-85dd-8bdb9877fbe6 | -10.7902 | -46.3203 | 2026-09-20 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 20b422c3-b3cd-3f8c-8535-a0f8d8f0bb4f | -9.2603 | -45.939 | 2026-09-20 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 1753ab80-e950-36a9-8f25-58f7f372e330 | -12.152 | -47.0383 | 2026-09-20 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 186.7 |
| f4ffbd4a-28af-3d1a-afe6-2af1056f2c41 | -11.8747 | -49.9983 | 2026-09-20 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 55a9deb9-8792-35f2-828c-93d22777a94c | -10.8553 | -50.9459 | 2026-09-20 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f61a7a53-1060-32df-ab3b-f62ac896a47f | -8.8639 | -45.937 | 2026-09-20 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 800fee0a-8c4d-3360-b145-719ec95925f1 | -9.26 | -45.9616 | 2026-09-20 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 31aa15a7-9066-3ba9-a95c-d8c71fcb039f | -11.0994 | -54.008 | 2026-09-20 12:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 01aa7aa6-82d7-30e5-b127-735463409777 | -10.2787 | -50.2605 | 2026-09-20 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| bf13438d-a4e7-3ee4-bef6-764bf1b83a58 | -9.9451 | -45.701 | 2026-09-20 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| f835756c-d76c-3943-9365-3965942f57e0 | -11.398 | -51.418 | 2026-09-20 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| f52418d3-32a1-32ba-a933-ada0f8faadb8 | -9.8313 | -48.4073 | 2026-09-20 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| b571a5e2-3c9d-3f25-a96e-10ac53645d84 | -7.8003 | -45.1163 | 2026-09-20 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 65aaac20-d7e1-39c8-a52d-2e3a09b7898c | -10.3168 | -50.2352 | 2026-09-20 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| dd2499a5-0f04-3918-9b4b-6e7ec8542f8c | -12.2341 | -50.1703 | 2026-09-20 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3de5b755-98aa-353d-af54-44e199506ef6 | -12.1711 | -47.0356 | 2026-09-20 12:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 2bc6b7b6-bbc5-365c-b119-6581e9027d5d | -10.3917 | -48.8915 | 2026-09-20 12:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| f402fe2e-9737-3441-8da4-84e89f48aec6 | -12.7621 | -46.18 | 2026-09-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 397.5 |
| cf861e4d-ecd7-3982-85d4-71140b214893 | -10.41 | -48.933 | 2026-09-20 12:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 44a884be-1578-3d6b-8f21-5710aaa3b49a | -11.4537 | -45.3892 | 2026-09-20 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 231.9 |
| c9ab07d1-840a-3425-8982-191a9aadc885 | -7.5337 | -45.4141 | 2026-09-20 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e8663a28-f6c4-394b-8e95-1e954191fa13 | -8.4314 | -45.8467 | 2026-09-20 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4d018c9f-ca0a-345d-ad0a-eebdacc65a36 | -11.3793 | -51.3989 | 2026-09-20 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d6cc7287-265a-3497-8465-a37594d90699 | -7.4286 | -44.7409 | 2026-09-20 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7c9871d5-fc1d-3d98-b765-e51f822e91e9 | -11.8487 | -46.8781 | 2026-09-20 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 33a9412f-cd38-338c-92ee-7257dcd23cc9 | -12.2344 | -50.1488 | 2026-09-20 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.6 |
| b3823e75-66dc-3cad-a5fc-98fc7217f816 | -6.9225 | -42.9088 | 2026-09-20 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| cb3c4003-8989-32b0-b267-e97d61f0d531 | -7.3259 | -55.6153 | 2026-09-20 12:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ca00d6e9-f8bd-318b-9c91-cec4d8d0ae30 | -6.4485 | -59.9909 | 2026-09-20 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| bcd23498-ace4-3b62-b7a7-478c871dfd4c | -11.6609 | -43.4239 | 2026-09-20 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.7 |
| 7b47d95b-62f3-37ec-aadd-76ef571dddba | -10.3914 | -48.9133 | 2026-09-20 12:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 535dc383-36c3-3df9-9a68-70612968a45e | -11.3612 | -51.3374 | 2026-09-20 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| fed8692a-4b32-3dc1-bb7e-622401eaeb1a | -9.8394 | -46.4586 | 2026-09-20 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| dcde1494-1468-3bbc-9697-08af31c98461 | -10.3171 | -50.2138 | 2026-09-20 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 9d9ff3fc-c562-3487-864b-677c5c47af36 | -11.0256 | -48.3164 | 2026-09-20 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ba111e69-1e77-3219-8e38-0363135c47ba | -12.7616 | -46.2029 | 2026-09-20 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 675.8 |
| 1f95e090-6946-3b7d-88c3-b6be022fce2f | -11.0259 | -48.2944 | 2026-09-20 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 111b630f-2628-3478-a20d-4f21494c39da | -10.2598 | -50.2624 | 2026-09-20 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 578599d5-857a-3cda-bce1-62e19b1e5949 | -9.8397 | -46.4361 | 2026-09-20 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 289.2 |
| 819f49a2-d9c8-31d8-a403-cc550324f09d | -12.7653 | -52.8661 | 2026-09-20 12:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 08c21b5e-dbb5-3f34-8cd7-2a2a56b1eca5 | -11.4541 | -45.3662 | 2026-09-20 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8da3cdf2-b5ce-34a0-935f-f4228d8b3ae5 | -11.8744 | -50.0199 | 2026-09-20 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 086491d5-c5bf-319e-b26e-c7c92fcdb5b1 | -7.5334 | -45.4367 | 2026-09-20 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4db045a6-f1a9-3e93-9217-3d6b378fd80b | -14.6856 | -46.6886 | 2026-09-20 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 25334c23-a9f1-3c97-a040-72cd323bcd51 | -14.1458 | -45.5638 | 2026-09-20 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 534909f1-986b-3209-bcd4-5e160a8d4556 | -6.9414 | -42.907 | 2026-09-20 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 6124f962-fabd-39fd-af69-949fa59fc327 | -10.8367 | -50.9266 | 2026-09-20 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 74a0130c-9aea-3528-95ff-945615c84f36 | -6.467 | -59.9902 | 2026-09-20 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 92a87dbd-bfcc-391f-bcff-e56ef70ade2e | -7.8789 | -44.8348 | 2026-09-20 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e7879091-0686-38b3-bd02-48af06b01860 | -12.2344 | -50.1488 | 2026-09-20 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3818b395-21b7-3066-a86e-8ca585afd75f | -11.0065 | -48.3187 | 2026-09-20 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 72b54356-941f-3516-b64d-103fc2a57f84 | -5.8593 | -53.5399 | 2026-09-20 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b4c8e180-3026-380b-8e3d-d967cd7f5e6f | -9.2603 | -45.939 | 2026-09-20 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 10166836-bb11-32e1-82ba-0a200324aa2a | -12.7621 | -46.18 | 2026-09-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 205.1 |


[Clique aqui para ver as próximas entradas](README115.md)
