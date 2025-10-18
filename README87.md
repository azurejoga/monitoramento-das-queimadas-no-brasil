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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20c2bddd-acb2-34ce-897d-3711a5cc3f46 | -6.53696 | -68.40253 | 2025-10-18 05:42:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5af55bf-8172-33e7-bf7f-47286fd870d1 | -6.5363 | -68.40668 | 2025-10-18 05:42:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7b085d8-1a16-3b16-a063-279834895c9a | -9.68433 | -63.16479 | 2025-10-18 05:42:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5d882a1-8f20-389f-abc9-613154eb4b6c | -6.76629 | -56.86166 | 2025-10-18 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90da23cc-5055-3ab5-9afc-9cd84f413ef1 | -5.10157 | -56.15155 | 2025-10-18 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 795f18a0-4419-3b6b-a592-ba745fb25c4a | -8.97595 | -62.04465 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203fbe25-75a3-3f7b-84c9-58486e05ee2a | -9.12072 | -61.28283 | 2025-10-18 05:42:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4256e1b6-e54b-398c-ab70-119e48bc1692 | -3.54365 | -65.23301 | 2025-10-18 05:42:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00299b48-f613-385f-9ed6-3197125ed6ec | -7.80827 | -61.3419 | 2025-10-18 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7587993-b64a-353f-b39f-facf337e3ba3 | -9.21107 | -61.54362 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c6abdc4-9390-3401-a1b4-4a0538b1f249 | -6.76586 | -56.86467 | 2025-10-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c394fd7-9c08-3756-962a-b7cb7757946a | -9.47145 | -62.36716 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68ded0f8-ce89-3d72-bead-11cffed4a203 | -7.86314 | -61.49646 | 2025-10-18 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21b1e7a9-5636-38ef-ae01-89fce026e79b | -10.33815 | -57.38239 | 2025-10-18 05:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45309733-2458-3110-b4b8-997afae9f24e | -7.49826 | -63.51443 | 2025-10-18 05:42:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2be2a76-e86a-37eb-ae08-82c373379f72 | -9.74588 | -59.30289 | 2025-10-18 05:42:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8bfe8e8-7130-3d82-be28-9020cc4dff7b | -3.53112 | -64.46712 | 2025-10-18 05:42:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae0465ce-d48a-3d54-b64d-320dcd090fb9 | -9.21492 | -61.54421 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd36d58a-8f8a-3b98-b8cf-028eef720ea1 | -4.54518 | -59.92776 | 2025-10-18 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ff4853a-60b6-3c43-8c98-294d928d47cd | -7.88721 | -63.72453 | 2025-10-18 05:42:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc5f14c6-ee8c-3ba4-9695-b77e63c40d8e | -9.00228 | -63.65577 | 2025-10-18 05:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6cbe38-b224-395f-b506-562a32dc92c9 | -8.58222 | -63.37081 | 2025-10-18 05:42:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c93227-96b6-316d-a063-5d2c7e6f5d66 | -6.93205 | -59.53083 | 2025-10-18 05:42:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af23ee6d-7654-39b5-8ea9-47bc97436ae2 | -9.01234 | -62.004 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 062d9015-4e78-3fbb-9790-15a6a8177b7a | -6.54055 | -68.40311 | 2025-10-18 05:42:00 | NOAA-21 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e254b2dc-a739-37e3-8773-d41bc09b0ccb | -9.16237 | -62.08406 | 2025-10-18 05:42:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae393ee1-861a-3986-bb99-4e652f1905b8 | -4.58406 | -59.9407 | 2025-10-18 05:42:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48b4c7fb-8375-3782-9cec-bd423da6f9eb | -6.36146 | -58.2087 | 2025-10-18 05:42:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb09f767-e5ee-3314-851b-4b2d9abce00d | -10.33483 | -57.3811 | 2025-10-18 05:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6288564c-7c24-3469-85b4-2676295c8a9b | -9.93266 | -60.19017 | 2025-10-18 05:42:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31c60097-e31e-3225-a4a1-102c38b58cf6 | -5.1068 | -56.15228 | 2025-10-18 05:42:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5213ccee-af2f-3af4-a8c6-7a27ab30a4bc | -10.81527 | -54.6118 | 2025-10-18 05:42:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a08192ff-691c-3344-8efa-6382ec276574 | -7.86823 | -55.37261 | 2025-10-18 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abc430af-bae7-3340-b8b7-bfd393fc03fe | -9.74267 | -66.33176 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e43d8af-1c6a-322e-b8d6-50aa21e03330 | -10.69175 | -63.47298 | 2025-10-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fa55edb-0452-3c1b-8ea5-6a91a47541c9 | -9.76559 | -65.0906 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2296f141-146b-302a-9bbc-4fc65d672311 | -11.75397 | -61.07271 | 2025-10-18 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0b55c14-b764-37e2-9ed3-8505b29ac567 | -12.60372 | -52.81576 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0e607ed-f84e-322c-888c-5ff52a8add24 | -10.68822 | -63.47245 | 2025-10-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0198435-d516-3324-afab-957843023fd5 | -9.89877 | -64.17384 | 2025-10-18 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 215f5e1c-5960-318f-b9a1-dd3ada4d44bf | -9.89536 | -64.17331 | 2025-10-18 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdd8348e-ced7-3a0e-b80d-a4ee5fca9e74 | -12.60937 | -52.80603 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96b7b455-4b26-3ec8-840f-6a94a7884aa2 | -14.69277 | -60.26236 | 2025-10-18 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d7fb226-b379-3460-a454-4682ad1bea73 | -11.73285 | -59.31925 | 2025-10-18 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fbae78fe-1631-3964-b4d2-7c14270ccc4b | -9.92446 | -65.00657 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8ccbf122-6916-3708-b081-e083e8ac52f7 | -11.75756 | -61.07706 | 2025-10-18 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d8f20d-614d-3ead-abf7-d79b1c9a9500 | -14.68758 | -60.2672 | 2025-10-18 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d4d1ac2-1089-3cbd-b0f0-2cd8c6f3e131 | -9.89592 | -64.16959 | 2025-10-18 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43540b5f-15e9-374e-b90e-7dbfaca748f8 | -12.01256 | -63.9378 | 2025-10-18 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d387938f-ac47-3a0e-93b3-d1e61d5b8caa | -10.6957 | -63.47222 | 2025-10-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72293408-6247-3ccc-99f5-eb0440e2c8b2 | -11.7586 | -61.06958 | 2025-10-18 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 772d9b4d-f033-3470-b52d-c5f4dcd719d8 | -12.60647 | -52.83395 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a9f235ba-9426-3a2a-89ef-9481219f446e | -12.60082 | -52.81925 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 43bd78db-59f3-3426-91ce-0b8c8b960fd0 | -9.76892 | -65.09112 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b7101aa-6657-34dc-8225-46a8420a077f | -9.95549 | -66.77127 | 2025-10-18 05:44:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f9f3d8d-cc91-3630-a9b4-6a941177c6ff | -10.68865 | -63.47113 | 2025-10-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 266b5457-805b-35ba-8925-e850248fbfec | -14.6906 | -60.26603 | 2025-10-18 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 889961fd-2b94-3935-8a68-4829faa741d5 | -9.76614 | -65.08706 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7f3bd7f0-0467-3e9e-bec5-ffdf8a2501bf | -9.89362 | -64.98755 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4719f13-3947-3c10-8252-48ad91296b59 | -9.87296 | -62.58973 | 2025-10-18 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f17fe10e-72fc-3d74-acef-67159c812d75 | -12.07431 | -63.69107 | 2025-10-18 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79d0f2c2-0cb9-31c9-a9d5-34f538e394eb | -9.925 | -65.00301 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d44b90-b67d-34b0-86b5-591ad24bf558 | -12.60154 | -52.8123 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa5b2b18-b0ea-321a-bcb1-7e2b55d37f61 | -12.10444 | -63.70819 | 2025-10-18 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1ef2b27-8c92-3da3-a7fa-2b915727663f | -10.38583 | -61.23141 | 2025-10-18 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c56b9e3e-9295-38aa-9f4f-972b91bbcd10 | -10.03128 | -62.16086 | 2025-10-18 05:44:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e308f8dc-69b2-3c83-a10e-84a4087731ba | -11.72495 | -59.12099 | 2025-10-18 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf0db1af-ab4e-31bf-bcb0-5dfe9ed9faff | -12.07489 | -63.687 | 2025-10-18 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc10bbdb-73e5-3fea-abf6-64228acee182 | -9.71253 | -64.96977 | 2025-10-18 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88425514-83e1-3cbd-b420-6a6ff1d220f7 | -12.61573 | -52.8139 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a3852be-981c-3edf-8c43-2c10f132161a | -10.69218 | -63.47167 | 2025-10-18 05:44:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73ecef83-5b04-3377-9a8a-ffa5ed83ddf1 | -12.00905 | -63.93727 | 2025-10-18 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d79da7a1-61f3-37cf-b739-eba74a932081 | -12.615 | -52.82088 | 2025-10-18 05:44:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3eafe91c-6c77-387b-b811-27a3f128d0d0 | -18.37507 | -55.43311 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8ed75ecb-752e-3acc-b51f-4d40ff7e3fa1 | -18.38442 | -55.47375 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b1fa6b42-005a-32bc-9e42-ca8f72f004d7 | -18.38391 | -55.47932 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8e2b917-a4e1-33a1-a04c-61eff9fe3a1d | -18.39036 | -55.48005 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1b00bd81-628e-3fc0-beec-730fbd60308e | -18.38501 | -55.47792 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c2f5f73e-ab51-3440-82a6-40be88d1a102 | -18.38548 | -55.47234 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c1659919-5033-304e-ad2e-480883faea64 | -18.39146 | -55.47868 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d0bca6ab-a53e-3466-865b-6ff3f86e9e45 | -18.37456 | -55.43871 | 2025-10-18 05:46:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a4053a9b-6042-3e4a-b1a6-d42b2d3d3f70 | 1.7664 | -55.9805 | 2025-10-18 05:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a164568c-81bc-33d3-aa42-1574459dfd97 | 1.7664 | -55.9805 | 2025-10-18 06:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fe53ddfe-5dcb-3d20-8ffa-0dcd5103dbb4 | 1.7481 | -55.9807 | 2025-10-18 06:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| baa31b81-6a0b-337b-93eb-56b1ca9d8e42 | 1.7663 | -56.0001 | 2025-10-18 06:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| b977ae75-ce86-310d-8694-829dbae3facb | 1.75207 | -55.97882 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4adff62-ea4a-3267-88bc-fd92af698926 | 1.76537 | -55.92556 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe18e6a7-716b-3e84-a0ec-d842a7ce5cb7 | 1.76338 | -55.9859 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c898b25-e0fd-3f6d-83bd-38ddd548a5af | 1.76046 | -55.98478 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7f05a74e-73b9-324b-bfe2-64bbd2af03a1 | 1.76095 | -55.97193 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 336a472b-36ba-30fd-a1a2-508cc627e891 | 1.76763 | -55.98349 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05b8059d-8eb9-37e9-bbf0-88212c3d7e28 | 1.7677 | -55.93954 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8d007ab5-6a63-3ccf-8cec-291ce15470a0 | 1.76793 | -55.92679 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65fc44ec-f472-3339-a545-7f0235b8a495 | 1.76934 | -55.97762 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 47def412-bb2f-3887-985c-19f4229a555c | 1.76646 | -55.97645 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd7fcaee-e115-394a-b0b5-2f55f923fa96 | 1.77164 | -55.94817 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e78bfec7-7f65-3baf-b28d-6a4e6aa4449e | 1.76165 | -55.99188 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4a6650ad-fbfc-3632-8658-87feba021fc0 | 1.76193 | -55.93495 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7274de8-0ad0-36d4-a10c-b623bbe6a1e2 | 1.76318 | -55.94213 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4458f1d5-f826-341f-8ebe-af61f6d22506 | 1.75927 | -55.97768 | 2025-10-18 06:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README88.md)
