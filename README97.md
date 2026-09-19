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
| 239d9e2a-46eb-371a-b66f-1cbc18490798 | -7.60091 | -55.69841 | 2026-09-19 05:44:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5177a112-dba0-3de3-832a-101ffcc53637 | -8.85623 | -62.35979 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0315ffbd-6966-38f3-bc15-d47805dd1a0e | -10.86528 | -54.1124 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3280d3fb-e079-339e-a4bc-4276a59cfac8 | -10.69888 | -60.73331 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d6c4e18-fb3b-325a-83f6-73a1c2a6a6f6 | -7.55942 | -61.32409 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92d3a6b5-36aa-316f-8733-8fc99b4a6065 | -12.27046 | -57.1774 | 2026-09-19 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0091a6ea-13aa-3bd0-bff7-e7237d6cf8d1 | -9.93541 | -53.98707 | 2026-09-19 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43eab3ae-c982-3361-95ca-29753ef0fea5 | -8.61149 | -54.60023 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41febf49-ea9b-332b-950c-f572055b8c03 | -9.10447 | -60.9497 | 2026-09-19 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2cdfb69-00e9-384f-8a5f-d5db26cc3b5a | -9.37006 | -60.31934 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e1e8a83-00e5-3493-b83c-f3ee436d413f | -6.80663 | -59.16262 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d309a350-888f-388b-b6a9-a45a3f0d1527 | -8.70677 | -62.54093 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 783fd873-0b8e-38a6-b10b-85bb95d24847 | -8.90291 | -62.40297 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdb718cb-3d3b-3f73-9c7c-b52bc7caae13 | -9.39587 | -60.35157 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 025c80ec-cf59-3736-9f0a-4a1a0d34f45f | -7.50264 | -55.0121 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4c8056e-733d-3a86-abb1-e3c49731bc6a | -9.17342 | -59.41723 | 2026-09-19 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a90d586-70d7-3a10-8e60-5e9fa7d8a080 | -7.55484 | -61.32839 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c2d4082-ed5b-386d-922c-5f4e51279b51 | -9.06402 | -61.37517 | 2026-09-19 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdfd85f7-c6ad-3803-b220-9452a8fa61c0 | -8.50544 | -57.63314 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae674ca-6619-3816-a605-cb59773d4a05 | -6.8161 | -59.19036 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1365d3a0-0edc-35b6-b5f8-92bee19cf2b5 | -8.70728 | -62.53851 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08390762-4375-34a0-b755-122273f96dd9 | -10.69329 | -60.73783 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f0b626d-52c1-35f5-8300-5ff83186ed7e | -7.37441 | -68.01413 | 2026-09-19 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9165965-cdef-3718-8fb4-e9e2bdc7bc05 | -8.05494 | -61.36729 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4719154-664d-3991-a969-3a58411bf1b3 | -8.16458 | -54.8264 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c4eeaa5-6096-3c78-87e5-b6b645a9ceff | -10.69416 | -60.7366 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6fefd040-6a23-37e5-8550-5f6feafec05e | -9.71475 | -54.81675 | 2026-09-19 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2481f7fa-f5b7-3fab-9c75-e20c97e4eede | -7.55799 | -61.33382 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5fb017ba-0477-3554-9380-e1e99cec7df6 | -7.87578 | -62.54702 | 2026-09-19 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a2b1484-7f0c-3c9a-ba2b-1d486104283c | -9.94223 | -53.98707 | 2026-09-19 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a789bda0-0d1a-3238-8de0-2bb290d26c15 | -10.68996 | -60.73596 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 474ed001-8556-33c3-8990-b45ac84bbbbb | -8.61131 | -54.59982 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51b1de97-fd05-395f-ac2d-91673efee366 | -10.22625 | -57.82935 | 2026-09-19 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f2afe39-e837-36e6-ac0b-d23c7b425f3b | -10.92128 | -53.97689 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f1b5cc87-e893-3f63-ae84-566fb4f4aa6d | -10.86657 | -54.10141 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df52fa0a-2711-3982-9fd0-c129847cbf2f | -6.80595 | -59.1647 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6e23a6f-986b-374d-9798-e6fcc7468317 | -7.5652 | -57.67225 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c2e116b-b1ee-312a-b808-17888f1e84bf | -8.49146 | -57.62267 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf161d23-3cc0-3cc5-8e49-ebb42f739d6b | -10.22977 | -57.82821 | 2026-09-19 05:44:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cab4150d-65ec-379f-a1a2-54e170b949df | -9.70744 | -54.82519 | 2026-09-19 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f808cbe0-43bd-36fd-a137-fb80e7e0e22d | -9.67065 | -66.82545 | 2026-09-19 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f28236e9-6642-35d0-9cb2-0d03c3732d46 | -10.70781 | -60.73061 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 184c10e8-14f4-3c55-9ca2-d33cdf0fe130 | -10.86613 | -54.10122 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2e4f91e-5662-3a0d-b79f-e7ef5d1ca24e | -10.91998 | -53.97654 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03e89e3d-05fb-3b81-8a50-80721767b615 | -8.17045 | -54.81285 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6417b349-8347-3e31-9b99-aea03acd45ae | -6.81561 | -59.19254 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f4140a1-6594-3699-844e-76ed5a45f3bb | -9.54587 | -63.78081 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12e9c71e-b241-37c2-8de8-35cfa0f899f6 | -6.76882 | -59.42195 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e382c07-4481-3647-b6fd-4c595493d89d | -8.03673 | -71.05504 | 2026-09-19 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 264aab7e-b0e6-3536-966a-98fe0f94be42 | -6.76449 | -59.42129 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e7043c3-d742-313b-840b-950999c06cc0 | -9.55521 | -66.02079 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4218e1a-7b2f-3791-bc23-2472e4f3d353 | -7.49793 | -55.01523 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd923be0-251a-3842-878c-078a11e8f6cf | -10.91276 | -53.98129 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d2849311-70ce-3fc1-aaeb-0bff3d54e90f | -7.56186 | -61.3344 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8319737b-2914-3ca7-a44a-50fdf1aaaadc | -8.27413 | -62.73872 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c70d4ef5-dd97-3598-b94d-e6262ca7135c | -10.69311 | -60.74443 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbd66dab-debb-3aed-ac24-3ce224830765 | -9.39404 | -60.30231 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebb2b35e-e074-3ca9-9528-a1a8c36aa458 | -9.39532 | -60.35555 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7af69379-f9a2-3fe4-a40f-0b0e3fb8692e | -7.49854 | -55.01073 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8d70874-2dc2-34dd-bf0d-e1c6b85592e3 | -8.85994 | -62.36034 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc961602-3a91-3358-b841-1d5ff905b726 | -10.69363 | -60.74051 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 063235cb-16d0-3e3a-8da8-ef9391d7bf74 | -10.86673 | -54.09575 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f19e281-c559-3e4e-9d60-73950b5dfaeb | -8.49651 | -57.62332 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8451c926-b4be-3f2a-a486-3e61636053a2 | -8.61021 | -54.61002 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c48dee63-fb9b-3f05-8c17-d033fc722464 | -10.70361 | -60.73 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b82dac63-ab06-3d5c-b94d-42898a883a9f | -8.92684 | -62.42004 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2863f3-4200-38da-a790-2590d8eb23c2 | -9.71535 | -54.81187 | 2026-09-19 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4789e887-66b4-34a7-bcce-8cb4f3beac59 | -9.54239 | -63.78028 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4d6ae3a-8bc0-38de-9a20-103bdd4fb9e6 | -9.54182 | -63.78415 | 2026-09-19 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818c100c-890d-3634-a07d-ba1e2fd86039 | -10.71255 | -60.72728 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 24b6e0f6-539f-34cf-8cb9-40e544351be4 | -8.61275 | -54.59058 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d8ca6e5-1e07-35a2-8a66-32c9cfe0ceb1 | -10.93577 | -53.95515 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f5e8a115-ec3f-3945-b79b-8052a8ad59fc | -11.13903 | -54.02306 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 89f898e1-a846-345e-9a8b-89c3aa1e56f5 | -9.68762 | -54.33352 | 2026-09-19 05:44:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8eeb87b-fbe3-38b2-aefb-ec61bde45b78 | -8.49572 | -57.62918 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6b7ad2f-8ec1-38cf-8d75-c82274686008 | -10.69274 | -60.74173 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dac173d6-ac03-3205-9095-80b303685235 | -10.86721 | -54.09595 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 415367aa-a75c-320e-a557-4c08b8c8fd62 | -10.87777 | -54.06268 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab6ee561-6bc9-3fc4-9ac9-1fb42bf02534 | -6.76326 | -59.4297 | 2026-09-19 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90f7b66b-bd60-36fe-9e73-d8f085d43468 | -9.33181 | -60.31542 | 2026-09-19 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 484d756b-7295-3ee1-a64a-32d26ad460bd | -9.9419 | -53.98802 | 2026-09-19 05:44:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f096b64b-be2a-3978-8e56-3066ef6fb61c | -8.89921 | -62.4024 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46b08744-92c3-37fc-8a13-d75d1a879db7 | -10.87439 | -54.09129 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9db01a2-be48-3660-9011-e581cb11b38c | -10.91339 | -53.97567 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00c891ce-d07c-3db1-8a9a-a24519618ad1 | -7.57854 | -57.68573 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4e2b9b10-581e-3f00-a7fb-22bdc3efca32 | -10.9147 | -53.97603 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d13ba18c-401c-3435-bf28-6c7ff896e66a | -8.50038 | -57.63262 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0db7b775-4f13-392e-b69c-b5c755f7c77a | -10.93643 | -53.94931 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3de6523-7d1d-381b-b114-b06fb0d75d08 | -10.87327 | -54.09653 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a17c106-c8b3-3909-988f-1c41807556aa | -8.16986 | -54.81733 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9db8de94-3fb2-396b-8f23-a8b3f06b684f | -7.49612 | -55.01603 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d12870da-069e-3346-8b5c-f906e68b78ad | -8.61191 | -54.59491 | 2026-09-19 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 652f75e5-eb60-3171-abbd-c53ae8c7b3f0 | -7.56873 | -57.67282 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 557df500-b340-304c-8879-40916bb4b7df | -11.02173 | -54.12836 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e8ad27a-d952-3cf3-a51f-df6036b0e400 | -10.86735 | -54.09021 | 2026-09-19 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e424bc3e-d92a-31cb-9c1b-e8b3a5d9cf7c | -8.01009 | -61.37574 | 2026-09-19 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcbf0804-e030-3ad0-a391-bec237286246 | -10.70256 | -60.73785 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84ab0d61-0b2c-3e9e-ab55-ee15571680cb | -10.71202 | -60.73123 | 2026-09-19 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 10a5d3e3-6e27-3092-9b69-a33f5b894f72 | -8.49611 | -57.62626 | 2026-09-19 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb0dd1d0-fb38-3722-82dc-38ece74f871b | -8.92379 | -62.41507 | 2026-09-19 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README98.md)
