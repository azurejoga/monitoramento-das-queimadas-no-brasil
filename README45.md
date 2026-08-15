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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8192d151-14a7-33f9-ad51-d9029e9f8141 | -6.8567 | -58.96413 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9442baba-890a-3fac-adaf-18f55744e510 | -7.39333 | -60.00122 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe76cd80-5daf-31af-8eaf-8972ab57b0b8 | -6.95911 | -59.29428 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b09b1edc-fde4-3073-9830-b53656990b0c | -6.83854 | -56.4264 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e64ebf1a-8115-30d1-92b9-b562035ea334 | -6.82938 | -56.42144 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 842b2bd3-fc6f-3a1e-94fa-8b940e1bcbf7 | -8.96196 | -60.51913 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 061c70c8-0e5e-3f6e-bcab-5ec92310857f | -6.70467 | -58.95626 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33fd4c18-f8cc-3fd6-8550-9f4c9641d464 | -6.78692 | -55.8359 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ab11fd5-0fe3-3a24-af62-ba258b60731a | -9.35301 | -62.34554 | 2026-08-15 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46fa95c4-db5e-3c89-8314-feda94604a26 | -6.7867 | -55.83295 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75ea5879-06dd-3129-8f85-1dff0aa3eb92 | -7.59064 | -60.87629 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6f3ed2b-b4d3-3e14-ba8a-e103c591f1a3 | -6.94144 | -62.88393 | 2026-08-15 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d434d88-b22f-328e-89c2-3b5f4f6190b7 | -6.79034 | -55.85279 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 179b5e02-e1ad-3359-9447-d9bd821ef84b | -6.78607 | -55.8377 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d80164-f2a7-3241-97ed-09ac57e238ca | -6.59745 | -56.36682 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa619370-b4f4-3ca7-8be7-4037d0ab0b1e | -6.70628 | -58.94474 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb0ac2e8-a3d5-3143-8e86-34e232928004 | -8.89594 | -60.56177 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da1e398b-cd8b-30bb-9961-c12e38f28553 | -6.95421 | -59.29355 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 49eca923-1e6f-3350-ba89-fd7699766524 | -8.60543 | -54.67781 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11c0ebb9-abf7-3a88-bf1a-a78ea9d86638 | -7.38863 | -60.00052 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edffaf02-c4c7-327a-bdb7-85d7855e9c38 | -6.82039 | -56.44222 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9601d9d2-d03e-32b4-ad91-6b455dc70436 | -6.851 | -56.42375 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 986c4301-86b8-3f9a-be75-31c2b641388d | -8.64891 | -54.71542 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96772d80-5d8f-3fd9-8d50-00b60712aefb | -6.96817 | -59.30114 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 989fdfc6-22d9-3822-8a57-3d02f395de64 | -6.79773 | -55.84433 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f607061-e064-3ca1-8fbf-3f1307234063 | -6.69964 | -58.95569 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 509df6df-7b27-37fa-9500-31e90d6e7ea2 | -6.20536 | -57.77198 | 2026-08-15 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9d8aba40-8db7-3e98-84e8-68d9508ee43e | -6.79241 | -55.84155 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84fd5029-532e-3b1b-9544-9291e0d85272 | -6.60576 | -59.00432 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e0403e69-d8c3-30d9-98a6-b8e67bb9c9b4 | -3.51557 | -58.95341 | 2026-08-15 05:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 649e30c0-dcc6-3560-9d81-25ed083471dc | -6.78482 | -55.84716 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70422305-152e-35e2-b754-8e5374c976db | -6.79792 | -58.7704 | 2026-08-15 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91d2f267-89ad-3c13-92e1-3550247d2634 | -6.83319 | -56.42122 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c3d8034-a639-3170-adf6-8aafbe0eb9e2 | -6.85161 | -56.41927 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5868893a-6329-31cf-9983-e0eb804a9625 | -6.95154 | -59.2974 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1b8a275-e4c4-3703-a188-afc5b428e48f | -6.8563 | -58.96698 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b03424c5-9739-3869-b559-53f2b91163db | -3.59089 | -58.61995 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dc609ee-29e7-3fa6-9781-c31e024443e4 | -8.96796 | -60.50998 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 632c13df-0251-37a9-915b-857f88141176 | -6.84389 | -56.43163 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a27887ea-9b8f-3655-a971-b2c46376b105 | -6.95726 | -59.29256 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10a684da-1148-3656-99c9-44a96a499504 | -6.9625 | -59.3059 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05eabc56-129e-3366-928f-0e3f1ae7ae8b | -7.55267 | -61.1706 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| de0251f7-9789-37d6-bd2c-2405afe711a3 | -8.02318 | -55.1257 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d065dd7a-4ec3-36c3-b472-868a847bdd14 | -7.58915 | -60.8786 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 679ad381-a2bf-35f5-8350-e8c58a2380cd | -6.79109 | -55.85095 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ebf93fb-6dd5-3fb5-8b36-93be6e4ab414 | -6.60656 | -58.99866 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 67f1afa0-5b7c-3f40-8479-501fc4138916 | -6.61652 | -59.00013 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0cda7879-8e69-326c-993b-056cc0dc6ce5 | -6.61427 | -59.0516 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15f365c6-cec6-3b4f-8695-b64aa9a4b341 | -6.59562 | -56.35349 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 95bd1df3-cff7-3eb8-b211-cb2cc220ab65 | -6.62003 | -59.04671 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 443be635-2534-3651-a499-6dc6da43b643 | -6.7971 | -55.84906 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aa715c6-b86e-300f-b84b-72b5563c6a92 | -8.78232 | -63.97192 | 2026-08-15 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 716f06a8-e133-392b-94a6-34e6260b3cd8 | -6.59371 | -56.36707 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57287e7d-e6b6-3a9a-a66e-26446e7645fe | -6.72297 | -58.93511 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1051d3a8-0d30-31af-9bbc-5b45c80a2cb2 | -9.19358 | -60.29045 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 743c058e-6ba9-3df4-b3c2-0d1faa7f5f72 | -6.58261 | -56.35988 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6251f1a4-c302-3a46-bc7c-d88edda70eb6 | -6.62342 | -59.05844 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 279a1d1f-7c00-3984-9210-db8d43b22d58 | -6.70929 | -58.95972 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed8792b9-7704-337e-87ac-9a3bfe0571ad | -8.64912 | -54.69625 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81e1d5cc-8576-386e-a7be-b43b405db0fc | 0.89083 | -59.69738 | 2026-08-15 05:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e74f16fb-9feb-384c-a072-8e15c58a362b | -8.95799 | -60.51357 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ecc7cf58-4f31-33f9-968b-2d74996e1b80 | -8.89661 | -60.55697 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 7e00fd82-0425-32ad-826f-ce7506a8c05e | -7.58403 | -61.23043 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e1fa5d0-c381-3284-b83f-133388f9498b | -3.59396 | -58.61636 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 276e6d78-048b-327d-a977-adb3222aedd6 | -3.59577 | -58.6207 | 2026-08-15 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed64f5aa-4a0b-3df5-9592-c99585b9b81a | -8.97919 | -60.5315 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daee037a-8197-3171-9d45-95c66995f723 | -6.85711 | -58.96125 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef230db0-36bb-331d-87c9-7df4b3eccef1 | -6.96216 | -59.2933 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a66f5a27-4159-32e4-980c-e7336aa91cfb | -6.79096 | -55.84809 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e4321db-ffbe-3021-86b4-b021abfa2004 | -6.83 | -56.41702 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c2ea170-32da-32a6-a260-56e5f8ecd8c3 | -9.07757 | -61.39813 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc58cc0-af88-3955-a7b1-53f07aee5b47 | -6.79267 | -55.69191 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db6e7fcc-c959-3d17-8ab0-d17d42ba0ce8 | -6.88988 | -59.02019 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc8036af-0151-3855-a1ab-c7f5571c4c87 | -6.78419 | -55.8519 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61b6c503-6545-3c89-815f-efc1ad29b630 | -6.62101 | -59.07527 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ab3ee3c8-0a74-3fb4-8afb-6b640a8dae6d | -6.96555 | -59.28397 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f9d2450-7537-3ed2-8652-4b1e7a89dfb2 | -6.69925 | -58.95849 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7828dec0-7198-3de3-9b3b-922111c73088 | -8.96729 | -60.51489 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 516b5a53-44fb-3d6c-b8a9-ba7539215303 | -7.59421 | -60.87482 | 2026-08-15 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7e4f5ec-1f66-3490-9c65-31d168f3faa4 | -6.9614 | -59.27774 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 39225842-2b57-3ec5-acdb-56c09ff34dc7 | -6.60023 | -56.36377 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5a48aa1-1547-33cb-98a4-e012d169608d | -6.81978 | -56.44656 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a27369bc-0107-39c2-abd9-e4b6189959bb | -3.25311 | -61.19158 | 2026-08-15 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa21043e-29c8-367e-a14e-f5db8a6e0a22 | -6.69502 | -58.95227 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ab5f62e-eedb-34f6-a23f-1ee3be4ac0d8 | -6.60632 | -56.34571 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c18d666-9fed-3135-b9a6-ababb45de961 | -6.63264 | -56.26331 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68e88b3e-8b6d-3bd6-95c7-72dfb7b78939 | -6.79374 | -55.83204 | 2026-08-15 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd84d869-ae9d-3e2e-b747-1dd0db766395 | -8.89266 | -60.55153 | 2026-08-15 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 57357e3a-470c-36fe-9095-d7757c6c3fa9 | -6.95835 | -59.2998 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3994772-1060-3e5d-b565-33ba0e92faae | -6.95806 | -59.28709 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ab455de-0bfd-3776-8de1-14c44008a767 | -8.6467 | -54.71481 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88fe51bc-39ab-3640-b514-d285b568129f | -6.62581 | -59.04177 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b714f3a-8dc3-34dc-9b9f-16bda237619b | -6.71674 | -58.94302 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaadd025-1cd5-3ecd-96c2-bc1e21039bf6 | -8.64236 | -54.69539 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e336497-089e-3a34-8387-d9bfad7a9c3b | -6.70507 | -58.9534 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e67c52dc-889f-3531-ae2f-254808b12e5f | -6.53542 | -55.18082 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57527a2d-6fcf-3c18-a17f-064f9dca77a1 | -6.58846 | -56.36133 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe4450cf-fb56-3c0d-8353-92614709be72 | -6.58322 | -56.35548 | 2026-08-15 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dc2db72-19de-32be-893f-5338fae4fd9a | -6.71835 | -58.93156 | 2026-08-15 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d2849c7-7653-3bfb-a4ab-0b459591c238 | -8.0283 | -55.14133 | 2026-08-15 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README46.md)
