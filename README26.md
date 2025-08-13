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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73a27bff-a7a4-397d-acae-4bccb2d1a395 | -8.56911 | -54.69765 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93135580-de87-304f-8abf-8d85cf742ef5 | -6.1064 | -59.92882 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 939e4b6a-4ce6-3ea6-b783-445c81d5cd49 | -9.70864 | -49.47947 | 2025-08-13 05:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0255b9f5-6be6-3ad2-8206-2b00bbe21692 | -6.88337 | -59.12907 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 18c132a4-b1e5-3da3-8c1b-1552ee7c76c2 | -7.0694 | -59.2001 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29af3521-c6dc-3800-a9f2-f94133405e7f | -6.92954 | -59.14545 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c1a03eae-088a-32cc-98ae-c333ea0cec0d | -7.257 | -60.0009 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0ea2158-890c-3232-b457-f00255bc37e5 | -8.5663 | -54.71582 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3b56275-2f07-3678-a77d-dd25a9ad059a | -8.56291 | -54.7153 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d4328adb-f157-37c2-92d4-b4926e873a7e | -7.45588 | -57.65258 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a28d85c-7fb4-324d-91f3-ccddd6a92d5e | -6.6114 | -43.88409 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 50bcc425-5c10-312b-85be-efa4e1e55206 | -6.89294 | -59.13946 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| cc1d4dff-5329-3894-93bf-07fccd8f4395 | -10.18472 | -49.50613 | 2025-08-13 05:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 365a7d6c-7eec-32dc-bfa1-b5f642b15b01 | -7.07616 | -44.94255 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6561d8e8-472e-39f7-8a36-68859db7932f | -9.84635 | -47.82059 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1c637122-4e41-308e-a13d-0167b14c3b96 | -8.56968 | -54.71636 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41fc9b32-bcd9-3389-b797-5cf6f2c19c0d | -6.8966 | -59.14008 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 5c0f92d1-2730-3509-87c4-12dd45db6395 | -6.92222 | -59.14424 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3cdda8e-4c9a-3937-aa3b-79ce6ccf49c4 | -6.88929 | -59.13885 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 5bc8e780-e418-3bb0-9fcd-8457008f2d06 | -8.11571 | -55.56625 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2032c30a-25ff-34bc-b5a1-e586d30a34c9 | -6.24621 | -55.36444 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12e29839-d677-3529-b67b-8bd7af36f0d5 | -7.06797 | -59.20873 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ed2e03a-90f6-39dd-bd26-5e1fdab4ea17 | -6.91253 | -59.63379 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc8d3f6a-3cca-35f9-a578-f5a6fa1609bb | -6.88859 | -59.14313 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 55f0f27c-e7a9-3577-9ef2-3dc5e6502d0d | -7.13882 | -60.13006 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 563dbcad-7de6-3bd3-91a6-7f6a5dfc3f19 | -6.27683 | -53.63678 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d66514-45a6-3e37-b48b-8e269e31339f | -6.90828 | -59.13761 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 03188b32-62de-31ae-9b86-6584caa3ad2a | -8.10905 | -55.56519 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c273a35-f435-3685-b770-dfa1d11c7030 | -7.25094 | -59.99021 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a401bc0-be84-3483-85cd-acce36394afa | -8.10408 | -55.57515 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a765fe5-1261-31d8-83e5-d2073f2b1f14 | -7.26003 | -60.00628 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf2d6c72-3a22-3c56-b783-de955cb2103e | -6.89521 | -59.1486 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8b7a72c8-7bc5-3bb5-a1f2-39f5b696f731 | -6.89225 | -59.14373 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 87285a23-0202-3664-9119-274e47a58ada | -7.07966 | -59.20631 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaecf02c-6d25-32a7-891e-216be305a174 | -6.898 | -59.13148 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 09116de8-0bd3-3ce8-99a1-32168a2d0c73 | -6.10094 | -59.93783 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39316709-0a1d-32b1-b523-13df91b87d1e | -9.8412 | -47.81976 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 965df485-769a-39c8-ac25-f8b703f00e8e | -7.12724 | -60.12819 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d557a53f-0aa0-3900-a0ff-69dcf634a643 | -7.45736 | -59.89013 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23b14ae0-b233-3fde-93ae-267f9841f2cb | -7.45547 | -60.62956 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d007e926-657d-3370-9e8b-18d064938b08 | -8.30621 | -55.10881 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdb591ae-d585-335b-ba7b-edd9899e284b | -6.55191 | -56.19153 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| defaf029-fad9-3a29-9553-8710b905ab2a | -6.09706 | -59.93725 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf2c3581-86dd-35df-91bf-f085164f7993 | -7.46115 | -59.89071 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d7c3395-842e-30af-8684-efe5a5e6ca0e | -9.84677 | -47.8174 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9cf748e-3e2b-3a35-b6ac-eef243cb6637 | -6.97764 | -59.28424 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84b5d470-6152-3319-b458-b5f450bd5e7e | -7.07136 | -44.93281 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc6bccd5-60a6-37a2-b773-633dce616cdf | -6.61068 | -43.88924 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9b6970a0-d49b-3b31-90c8-98903ac5a7ad | -7.09727 | -60.02491 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc9f3c81-9e85-3612-8786-95a4f0ef44e3 | -6.92588 | -59.14486 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| dd02718c-7885-3c8e-bc0d-1d7b6e63020f | -5.84834 | -59.91654 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1480efd9-3b21-32f0-8696-a4afe51732a7 | -7.09243 | -60.02131 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 85d4505a-0143-3b87-bdd1-9a515022da28 | -9.05727 | -60.64479 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35061212-7acf-36a1-9466-24a976c75b7f | -16.3063 | -52.92191 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bc462d0-eb56-38d1-a8d7-2a25ee482152 | -12.67219 | -46.96399 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4ea5e4d-85ac-36ba-b0b0-4e13f8442e52 | -11.91224 | -52.54012 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc519f10-7385-3b63-a514-7d894c16c0b8 | -12.14621 | -48.01667 | 2025-08-13 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 381468c0-5a43-3d39-aa22-676842706d03 | -8.93477 | -60.72559 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 434887cb-64de-38e3-bd19-0ac10a8b2d7d | -9.38624 | -61.52992 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16fcd071-4034-3322-8ab0-841eccde886e | -10.01981 | -58.43062 | 2025-08-13 05:08:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad694325-08b1-3371-b6b4-d9e155fb8b07 | -12.48355 | -46.96138 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c7755a7-a2ee-3a0a-8edf-e88442c2ba4d | -10.34081 | -64.47169 | 2025-08-13 05:08:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13fba225-5a50-3179-9c0a-e1daaa239bd9 | -16.36431 | -50.607 | 2025-08-13 05:08:00 | NPP-375D | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bccdcc7c-6933-3b4a-817a-8cea44327c9a | -9.19229 | -59.6622 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8f0fd288-c957-3800-8fcf-601f4b2e68c0 | -16.29022 | -52.91974 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 897a00a6-51b8-3446-947e-fabdb96aa935 | -12.58328 | -46.98457 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5eeee4c3-812b-38ad-ad19-3e9e4218dcd5 | -8.93784 | -60.73123 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a33429b6-69a1-321f-9a82-d919c7acd902 | -12.48307 | -46.96524 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf4bf961-6bd7-3e2d-98e4-428c0dde4765 | -8.93005 | -60.72983 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7af41c3-1d61-3121-9a41-4af51de93c1a | -10.7536 | -69.08482 | 2025-08-13 05:08:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcf89dd0-3e2c-3df5-8482-09d52ca0aa83 | -12.58191 | -46.99632 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4b6997b-8d58-3fd2-a174-83082ca00a5d | -8.91966 | -60.76543 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5666820-6007-376e-b0d0-6cbb5976f586 | -12.57721 | -47.05745 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e51d938-5b9e-3f73-a28b-2d8b3195819c | -16.39949 | -50.88302 | 2025-08-13 05:08:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ee28b637-f4f2-36b8-a5ec-ae96147a677b | -12.58458 | -46.9735 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62ffed2c-9e6a-3bcb-bd92-f0ca84f53c56 | -12.58134 | -46.97837 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bb40a23-9d88-3abb-adcf-4b3fff219148 | -10.9657 | -49.56998 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b4bc6aad-c22a-3c89-ae41-0823379e422f | -8.93866 | -60.72629 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 290a87df-2cb6-3d80-8f6b-23d87a07265d | -12.57981 | -46.9906 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 653a1933-1ddc-375e-8767-2bbb9803ffa3 | -9.06188 | -60.65855 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c1f9ef8b-8490-33bd-91ac-6f0b4e4be18e | -12.3653 | -59.83953 | 2025-08-13 05:08:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af3611e9-bd7e-39e6-bcf9-1d590129a42d | -9.065 | -60.64616 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b350d6e-bd21-3f82-bf06-9acf1f4df3da | -16.31324 | -52.90911 | 2025-08-13 05:08:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55bbe5e-ad96-354b-82d2-61869a1fc958 | -15.09364 | -51.35823 | 2025-08-13 05:08:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1974e6f-086a-3659-99cd-b45ea4e0e67d | -12.32319 | -46.05452 | 2025-08-13 05:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37c71683-87f7-33ab-93d0-5069ae18ac0f | -9.19594 | -59.66286 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 98ed0f34-4cbf-3076-bda2-852736b4c233 | -10.96633 | -49.57818 | 2025-08-13 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39caccba-e41f-3ac5-9955-ebb947bef6e2 | -9.20973 | -59.6476 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d0f9c444-041f-385f-93f2-933274fa3324 | -16.35968 | -50.60604 | 2025-08-13 05:08:00 | NPP-375D | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 995ac89a-18a3-3619-9515-26161e991c70 | -11.67985 | -50.14719 | 2025-08-13 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8beb3aa-dd3c-391f-b571-c624fb4829fb | -9.39031 | -61.53063 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc3818f3-725f-37ac-9d00-6c86f1c4f1c1 | -12.57743 | -47.03447 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57c29b65-fed1-3e6c-9af3-2f35379ab566 | -11.69157 | -51.60971 | 2025-08-13 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 838a6025-bb7d-3bc3-a3ac-656fd53677fd | -9.18427 | -59.66522 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd7e810b-a18d-3d80-9994-1e520557383b | -10.41907 | -54.40666 | 2025-08-13 05:08:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 314f08d8-f00a-3722-ad8b-7cb9b45622cd | -12.52864 | -46.98566 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8c6c38f4-fcb4-3c7f-8d34-e5f9846f5ab6 | -9.21338 | -59.64824 | 2025-08-13 05:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b967ec9e-b4b0-388e-9f72-52ddcda33718 | -11.69105 | -51.61343 | 2025-08-13 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c1d643f-7411-32c8-ad71-77da828d3068 | -12.58177 | -46.97485 | 2025-08-13 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba29b411-5d50-3c02-898c-2b6a69e019ee | -11.90836 | -52.53957 | 2025-08-13 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
