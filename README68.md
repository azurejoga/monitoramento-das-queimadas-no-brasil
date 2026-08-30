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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebceb2b6-e2c8-3e16-a69c-5e189df2fcf6 | -10.55397 | -68.5891 | 2026-08-30 05:55:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d01711-6a0d-3299-9225-f8d13798043a | -14.93805 | -56.34108 | 2026-08-30 05:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a616ea45-d451-38c9-9b8d-bfe871f40c33 | -8.48812 | -70.61666 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed98250e-0e0a-314b-87c1-d5589e4b32ac | -4.22192 | -59.55881 | 2026-08-30 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bd14795-112f-3241-9de5-823fdad3d2c2 | -8.9167 | -66.9491 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8ec4532-1806-38c6-9f8e-5f9e32861cd8 | -6.12255 | -53.55755 | 2026-08-30 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3050de26-7ea4-3343-a938-d98d577d4d67 | -10.73632 | -54.03785 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c07c0b31-304d-34bb-bf32-aa47abecc1e4 | -9.49327 | -66.75202 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 887ec64b-b82e-305c-8432-df1581f5f788 | -9.89048 | -64.98537 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c40157d9-2ea8-3d2d-9817-6c7980d6e9d8 | -8.95896 | -70.81411 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e1878f0-b45f-344e-b774-6f16e1ed06d8 | -5.48685 | -57.15587 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a61a34a-e456-3f3d-8d85-97db8c4e028a | -5.87367 | -57.77425 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e47fa7c6-72a4-3aec-802f-c0dcfb613a46 | -11.29535 | -54.03076 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97e66b89-28ec-3be2-924a-f447c1b80120 | -8.93257 | -67.36432 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c16cb5a3-f548-3819-82be-f8a21757914e | -14.42716 | -58.45445 | 2026-08-30 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4756b4bf-d727-372d-8381-073630ef7b27 | -10.73497 | -54.0493 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61dbd5bd-5b85-300a-b115-d5a32942eb6a | -4.95508 | -55.84337 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ac186cb4-595c-3f61-ac21-e9da4c71bc06 | -9.92224 | -67.87871 | 2026-08-30 05:55:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ee6ceda-9cc5-38b7-ae05-7a5d1612f262 | -8.9122 | -66.95567 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04cff625-69bd-3fad-a59e-4277230216a1 | -8.92977 | -67.36013 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9f4741bf-ff02-3f17-9c29-1d9711f6d36f | -10.02475 | -66.98764 | 2026-08-30 05:55:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e32a8b15-b494-3e33-a7d1-9f25b3242710 | -9.04071 | -67.62555 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a05f9da-56b8-3689-aa4d-168ce7d05177 | -11.2947 | -54.03633 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6d32967-e5d1-32e7-936d-d1fe2842026d | -14.94402 | -56.34189 | 2026-08-30 05:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 639d96b6-9c4b-34ad-92f8-34e1ff252026 | -11.04082 | -57.22916 | 2026-08-30 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d695782-a079-3e2f-a076-7f40c4ee63b1 | -9.51385 | -65.58108 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee381b6b-8c1c-3412-ad24-d1549e44cd22 | -3.64669 | -61.70665 | 2026-08-30 05:55:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c95994e3-7fd1-3a88-b219-a114b032adb9 | -5.97281 | -57.69409 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e63542f3-2f10-3dbd-9e17-b2cb59157f35 | -8.9314 | -67.37157 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b22aa695-bc23-3462-b727-c0ba42aceae2 | -14.94353 | -56.3463 | 2026-08-30 05:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 61ce5197-0244-3975-84e7-c35f1fe8b9c4 | -10.7494 | -54.03977 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b350846d-9d10-3c17-98c7-edefaeb8456a | -5.96394 | -57.68733 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46ad9b51-0e9f-316f-895e-d4426265b19a | -3.62364 | -60.55286 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 124bc8ee-1082-3836-af6a-915cd8ed5201 | -14.93855 | -56.33664 | 2026-08-30 05:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ab57aeb1-4987-394f-9e5a-4d66737d579e | -11.29405 | -54.04183 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c646cf51-99c7-3035-91d9-440fa8e7ea1a | -10.48355 | -64.50562 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f125e47-eeb1-3b4e-89c2-beb9a20f9c60 | -9.93472 | -60.52401 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88bf5304-2ac7-3ae5-8f80-fc19b810e63b | -5.9647 | -57.68216 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd1d65ea-e75c-3593-83b2-f1d15c16dc78 | -14.16746 | -52.81411 | 2026-08-30 05:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe7bb227-1a43-3360-a6bc-afac060335de | -5.49429 | -57.13984 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 46817958-7fc0-3f7b-9cae-3f65346c30b7 | -10.48299 | -64.50937 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b60aacc9-e4dd-3162-ae8b-22f2eb143cb9 | -11.24455 | -54.0066 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9d09192-56df-3307-99f8-ca9d83bdd3ce | -10.50525 | -64.52437 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9426efcd-83ea-3c3f-a647-aa9d52009206 | -8.59656 | -70.21353 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 016eb566-9da1-3c0a-b5cb-380b784da0d3 | -4.96489 | -55.83633 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f608e93f-25a4-346f-a29b-1eaec88b68ad | -10.48667 | -59.61558 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 105e49f1-60ea-3b0a-a9d1-fb1f3aac6f9b | -9.20395 | -67.7803 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f744e322-2fb4-3e5a-b630-c0d0d4132c6c | -10.48641 | -64.5099 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b8f0960c-c9ce-3436-bb7a-5c21e1fc5992 | -10.49182 | -59.6117 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83dba54d-8956-303e-a2c0-2a6371f81ac6 | -6.16736 | -57.79478 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06314523-9a8c-37ff-bc0e-dce6ebe3f6b7 | -4.1243 | -60.78002 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a729a368-21d0-3486-97b6-9a441ff340a3 | -4.15174 | -60.68993 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08b25865-7878-30eb-996b-3c3443734073 | -8.93304 | -67.36454 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83b625d4-6c1c-3260-8f5e-0a44181aa393 | -11.24127 | -54.0008 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e1246ded-df5f-3793-b395-abc3f618daa3 | -8.93523 | -67.37234 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72118f45-1dfb-326c-9c5d-979f46bd848d | -8.59408 | -70.22802 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50e1f566-f46a-34d2-9557-215055c9323b | -9.93528 | -60.52012 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f15d7ec9-8a6c-322f-91dd-338105f51fef | -5.97307 | -57.68467 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6111b0e-0121-3208-99d3-b7c64cc3adba | -4.22137 | -59.56252 | 2026-08-30 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c096e958-b559-3fc8-97cc-8d73e91d110c | -13.84037 | -54.03039 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d178d872-8b6a-3c51-9831-2f762b4bde47 | -11.03546 | -57.22842 | 2026-08-30 05:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da32c8a5-c4cb-361a-9fe8-bba1014a5604 | -5.87289 | -57.77947 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daf6890f-ab3e-3970-91aa-626bd9b1e3dd | -9.88656 | -64.98843 | 2026-08-30 05:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e1ea310-b73b-3248-95cb-f8bbfa3a0644 | -8.72141 | -69.63866 | 2026-08-30 05:55:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d46e7037-8fa4-32ad-896d-56014bd5a7df | -9.94006 | -60.51677 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ff49879-b633-337f-9d0f-416b884e99c5 | -8.60509 | -70.21009 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e878b4b1-ca45-31d8-81a5-f883cc75cad7 | -3.9373 | -59.32945 | 2026-08-30 05:55:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8fb2cc17-43af-34c4-82e2-aa8555caf79d | -9.93005 | -60.43502 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 200657a1-082b-3bd4-aa3c-5c69d5ae431f | -9.93417 | -60.52789 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4331fca0-c42d-38f8-a132-f306d17b683e | -10.48216 | -59.61485 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e1d12506-db3a-35eb-91bf-d962c95cf37f | -4.95746 | -55.84921 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 241dd6d8-4424-3e68-ba1f-781596917210 | -9.02881 | -68.50774 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4187a2db-76bc-3d1d-be46-2e604f446230 | -4.96194 | -55.83384 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b6cc120-03bc-36d5-bb56-3af8a9df678b | -14.93756 | -56.34551 | 2026-08-30 05:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6184aa50-a1ee-30e0-a2ae-1f9eaf0d5a49 | -8.91277 | -66.95212 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80f78f4b-8728-3304-9ed3-d8161cf22a0a | -4.92537 | -55.76664 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f217f94d-90e1-3795-860c-952a0215bc35 | -9.9395 | -60.5207 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57d4272c-8fd0-38e9-9e7a-b0aa04c6db4e | -5.87257 | -57.77546 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4da4d39-4069-31bc-be63-18cd92b9c138 | -13.85928 | -54.11374 | 2026-08-30 05:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4c1f7da-b82d-3686-97bd-80a3776f7d38 | -9.03851 | -67.61765 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31ae8a46-2805-3fb7-b81e-baa14df52713 | -11.4429 | -61.48478 | 2026-08-30 05:55:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c39bc3a-c83b-304f-a8c6-20c78540b1a8 | -11.2452 | -54.00091 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0d3406a-9857-344d-9525-6f7de0fc92f6 | -5.89465 | -57.75804 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c7a539a-c6ab-35ca-a7b1-a4ab9b97b22e | -5.96899 | -57.67858 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1263419d-de9c-3c61-b1ee-ac61689d8bba | -5.97234 | -57.68993 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 077e6a33-d2e5-3152-953a-b8b609eda28d | -8.91555 | -66.95622 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 369f5fd1-018a-3c4e-b2f4-ca61eb6f28e0 | -4.96144 | -55.83735 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eb55f350-b5f7-31d7-8832-2c6e022316b8 | -11.1862 | -55.10199 | 2026-08-30 05:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d6ef0c0-66a3-3c43-a67e-4f47abebf265 | -5.8906 | -57.75211 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c7a089f-521f-3c4d-85ed-de112192b725 | -15.22742 | -57.66062 | 2026-08-30 05:55:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2841909c-144b-3f3a-8bfd-b252b1690086 | -14.45078 | -58.47676 | 2026-08-30 05:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d0697f3-7ca7-3691-8f2b-d87bc128f53e | -6.61467 | -55.44835 | 2026-08-30 05:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9861c2b-2b08-332e-84e2-8857b2317e36 | -8.54436 | -71.43693 | 2026-08-30 05:55:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6238cf7-89ee-3cea-a17b-894fc1f40829 | -3.61744 | -60.54218 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49862367-d588-3054-a34a-826a4f45c6fd | -15.2219 | -57.65991 | 2026-08-30 05:55:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42b1d386-0b21-3973-8d8a-331e1f6e98ec | -4.96688 | -55.83789 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1dd3cbb6-cc85-3b45-a27c-a16a8358ff73 | -4.96544 | -55.84806 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 38b902fa-bbc4-319b-8107-413a9db0b5c8 | -10.75007 | -54.03413 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3acbdb50-1d62-3ebe-8acd-316778092269 | -11.2439 | -54.01229 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| af423bd6-de7f-3788-8463-dca3bb2b0fe8 | -10.47826 | -59.60969 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README69.md)
