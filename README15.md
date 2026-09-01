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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1906ea94-43e1-3b2b-9181-5e7222281f41 | -9.707 | -68.622803 | 2026-09-01 01:54:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| baaf4f26-f118-329d-af60-bce3133d35e0 | -7.5356 | -61.3783 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9534af5b-9e9e-3829-a75e-894eef199a39 | -8.2683 | -62.746601 | 2026-09-01 01:54:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aa263525-c028-3829-909e-a4e3933e10af | -8.8744 | -66.887497 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 730d7d77-100f-3290-91df-a2bdc5af40e8 | -9.1622 | -60.941299 | 2026-09-01 01:54:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb57829a-8619-3c97-8b28-c45f042a4177 | -8.9282 | -62.356098 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2df46b41-663e-3463-8419-eb2957926544 | -10.0996 | -68.3983 | 2026-09-01 01:54:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4437d731-c603-3574-a3ce-c779b15f9f53 | -7.3612 | -60.579498 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99e7e704-ae42-3d11-8d0c-c1a31480cc3a | -6.602 | -58.5924 | 2026-09-01 01:54:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c569d2d-7864-3670-9374-6cb4fe23fadf | -9.0579 | -65.484703 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7a6a0ed-6136-3d21-b51a-dac134c56702 | -19.198299 | -57.321301 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec5b729c-36a4-34d5-8c8d-7c1c479ee5c9 | -3.1222 | -61.214001 | 2026-09-01 01:54:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51ef23b7-c3a8-3e96-9dbc-cce09ce9c37c | -7.296 | -60.565899 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7d17490a-1703-394b-8574-4d811dfb2f0c | -9.1494 | -60.9314 | 2026-09-01 01:54:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 633f5242-1e9f-3f6e-8ce2-35a1eb3b7124 | -9.0036 | -65.428398 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 100f651b-444b-312a-8802-a96cf7652bc1 | -8.876 | -66.894402 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23d66429-90dd-3b00-86b9-34d5dae14c26 | -8.5166 | -67.1278 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1b68306-6f02-3fd0-9b4e-4633d1fd1431 | -6.8103 | -59.555 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f846a6ec-279d-303f-8b77-b56ac70e1fea | -7.1933 | -60.6936 | 2026-09-01 01:54:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d132be7-4e66-3c5e-8585-4cc67e0378f1 | -9.4574 | -67.459396 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 789a88a7-c81a-362f-acf7-dd75e31c0c36 | -8.9469 | -63.296398 | 2026-09-01 01:54:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6c456a01-e321-35a1-a46a-c69c3ce5049b | -9.7087 | -68.630096 | 2026-09-01 01:54:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| abd2bc63-cf5f-327a-bc2a-eb3831852048 | -8.5932 | -66.965698 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab6269c-e276-32e2-99fa-806f37591edb | -8.5441 | -67.157799 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb561b95-995a-39cd-8e24-413f0b7f4ec7 | -9.0873 | -65.477898 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab1e43d2-414b-3ef8-9466-6dd146b78943 | -10.5051 | -59.6143 | 2026-09-01 01:54:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7d2cb3b-6e64-37fc-a061-18d1cc9bb187 | -8.9686 | -71.256699 | 2026-09-01 01:54:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 34147e93-96cd-3709-af81-f791986b1540 | -16.0459 | -54.381001 | 2026-09-01 01:54:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26a3c9d1-bfbd-325f-b301-24f38d6f171f | -8.5425 | -67.150902 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 50af7b83-8977-3435-8c55-d3edd1aa8664 | -9.0346 | -65.428802 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1fe1edc-f567-3c29-b90f-4ffaa36b0a96 | -16.062799 | -54.403999 | 2026-09-01 01:54:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2633c5ec-a405-3ba8-9145-e307c1c8a072 | -9.089 | -65.4851 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60c34ccd-262b-33ec-9966-299d271f295a | -7.5715 | -61.356499 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a99d7e8-ba83-3cb4-8a57-3b8578c0df9a | -19.179001 | -57.327 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 087da9df-6ef2-3ff6-b639-92cefd750fcd | -7.1899 | -60.679901 | 2026-09-01 01:54:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f7d995c-2ad3-31f0-ac03-7512e5a888c0 | -9.6189 | -68.596397 | 2026-09-01 01:54:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4846231c-d726-3fac-bdb0-5598368d2d45 | -7.5808 | -60.466499 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 447ed149-da27-3ca1-b0f8-61cb2ae73b00 | -9.036 | -65.390198 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 237170c6-0bc6-32fb-aa7c-1ca5190e33a9 | -19.1539 | -57.350201 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22c004e6-c2b7-337c-9388-714f16372948 | -9.0562 | -65.477402 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7be7baf-c8d7-3d76-90e4-e6ef4261316b | -6.7085 | -55.387402 | 2026-09-01 01:54:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 293fbf39-9765-3d23-9bce-7c47c98439b9 | -7.3057 | -60.563499 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6b76ccd-2006-3b51-bef4-12ef87b3aa49 | -7.9175 | -61.337101 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 448d73a7-0654-39ae-9131-cc41de33abbf | -6.8144 | -59.571701 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47260f77-337d-341d-84b5-12f5a2d78e17 | -15.6302 | -56.3703 | 2026-09-01 01:54:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd6d63d4-5f83-3e1b-9144-01d4553c69a6 | -9.0299 | -65.452904 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4bcbf81-5caf-3fc1-a7af-9968d072cfcd | -8.8673 | -66.765701 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28b70fa6-427c-30d2-8302-a179a015067d | -7.5905 | -60.4641 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d35ab86-72eb-3382-9839-fa859d09b1a6 | -10.418 | -64.452599 | 2026-09-01 01:54:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5d2b016d-2054-3545-abd6-840b0c7d31bd | -13.5412 | -59.7211 | 2026-09-01 01:54:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62b532fe-6870-3511-83a9-a48604a95aac | -8.8728 | -66.8806 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7f6682-7d70-3da1-bae9-b271e160b149 | -8.7915 | -62.4744 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8cd88895-1088-3b8d-9cbc-3e1f6394dd58 | -7.2994 | -60.5798 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6096d392-ca06-331f-b4e3-11d5fb7ae008 | -8.9328 | -63.2808 | 2026-09-01 01:54:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d59c713-bd95-33f6-8faa-7ad5e50a9a43 | -6.5923 | -58.594898 | 2026-09-01 01:54:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37fb4081-b8d8-3056-af60-af5a795824a1 | -10.0681 | -59.395901 | 2026-09-01 01:54:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6e92e9c-0e48-3e9d-91cc-f07813fd9368 | -7.1964 | -60.6637 | 2026-09-01 01:54:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75fdc0f5-bf71-361e-93f6-d92fb6b4ba60 | -8.5182 | -67.134697 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a84392c2-0d7c-3476-8c8d-c8dac62ad735 | -7.5842 | -60.480499 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca3cbc23-91e4-35e1-96af-9f17c7663a85 | -6.6989 | -55.3899 | 2026-09-01 01:54:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6221b9-45df-3ace-8fd5-014a07bab96d | -7.5326 | -61.366001 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e185c89-85e2-3d77-8fb5-88ca1c25a741 | -6.1819 | -57.7342 | 2026-09-01 01:54:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79b219bd-4049-3b62-a6c1-5e81b9b9bd30 | -7.587 | -60.4501 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0409af6-b78c-3ada-b624-a817f82efa6e | -9.4898 | -68.247299 | 2026-09-01 01:54:00 | METOP-C | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 041ca03e-663c-3d4e-b9b7-e95945364082 | -9.1524 | -60.943802 | 2026-09-01 01:54:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1edc5ba6-5ca4-3bb8-a9f0-a74a8187250e | -16.0555 | -54.378101 | 2026-09-01 01:54:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79fe556b-533b-37a3-9aee-f367ad8ab8b1 | -9.0694 | -65.489601 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf233180-ba1e-36ca-b721-7465c5263812 | -6.6068 | -58.5704 | 2026-09-01 01:54:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f894decc-1108-3571-8d1c-55b3b6e2aa66 | -9.0282 | -65.445602 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd7e776-a9f4-346e-bf4e-56a67bed62f2 | -6.1857 | -57.7089 | 2026-09-01 01:54:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa8a4ea9-8662-392a-b962-9b9b6a4a8dee | -8.8842 | -66.8853 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 064ab640-0d70-3347-bfd2-529557240f0d | -8.9404 | -62.363998 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9aace0-3784-3c36-a456-a4cdcc96697b | -7.1997 | -60.677502 | 2026-09-01 01:54:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 799380de-cba3-3d38-b8b6-be5cf5c250cf | -9.0808 | -65.494598 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| faf3f516-5853-3fb2-ac0b-80faccfacfa2 | -6.5971 | -58.5728 | 2026-09-01 01:54:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d238b958-e67b-3d24-93fe-2cff247def98 | -6.9639 | -55.624001 | 2026-09-01 01:54:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fca72cb-9c05-361c-87de-6fc5b0155089 | -6.9544 | -55.6264 | 2026-09-01 01:54:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33c1fdc6-2bbc-3c6c-80b7-f639c7cec6f5 | -8.7175 | -67.104103 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7662db9f-c859-333c-a9d3-f50dac38df99 | -9.066 | -65.475098 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f993182f-f2b7-3374-9209-97f41c2883c7 | -6.712 | -63.187801 | 2026-09-01 01:54:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0d94a7b-0f38-39ed-97a3-e624728131c3 | -3.6218 | -59.065102 | 2026-09-01 01:54:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1525ff1-daae-3bce-a210-bc8c4893046c | -8.6059 | -70.202103 | 2026-09-01 01:54:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3a7da0e8-658e-36e4-9372-df6b70f539f8 | -9.3987 | -60.560699 | 2026-09-01 01:54:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb3c16ee-8535-3ea6-97c0-6e4fce587558 | -3.6239 | -60.563599 | 2026-09-01 01:54:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe2dad8-e0fa-388b-bf92-3dc9e59aa455 | -8.5948 | -66.972603 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e73c93c-3b9a-3b83-810a-c7ad05714a87 | -8.7939 | -62.484402 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d5169c1c-d91a-3195-95ea-e0b300d9afc8 | -8.8657 | -66.758797 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 559d6641-7f56-32a0-ac25-a8b8853aa171 | -10.1012 | -68.405602 | 2026-09-01 01:54:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 67e77d7b-8d8c-36de-aa15-993907ac598c | -9.0677 | -65.482399 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e14050ef-a180-3533-b5b2-f6d593199db2 | -6.6068 | -58.6119 | 2026-09-01 01:54:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43451886-82ed-3d0b-87fa-f0ac919ce7a2 | -8.9166 | -69.279602 | 2026-09-01 01:54:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 04699841-8b40-3322-9fcb-d5bd75ff4bab | -13.5347 | -59.736401 | 2026-09-01 01:54:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1c55947-ce34-32e2-a068-44ddcc7be823 | -7.585 | -61.327301 | 2026-09-01 01:54:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 728f0aff-f8a4-3898-93ba-3d83780b15ca | -10.0247 | -67.830597 | 2026-09-01 01:54:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d7a90b1c-5feb-3e93-9020-e927ae55d846 | -19.192499 | -57.338902 | 2026-09-01 01:54:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed2cf641-6f10-3951-aae5-40fc3d46ea17 | -3.6337 | -60.561298 | 2026-09-01 01:54:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9838fe91-7bf0-358b-8d6c-e1c82b12d3ad | -13.5315 | -59.723701 | 2026-09-01 01:54:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 258e31d0-5ab9-318e-90f3-822b93343d7c | -7.5773 | -60.452499 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3504b9c1-342e-3ab7-81a7-0de1fcde086d | -6.1761 | -57.7113 | 2026-09-01 01:54:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c240662-b034-3653-8ffb-d8d3408efcef | -7.3092 | -60.5774 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
