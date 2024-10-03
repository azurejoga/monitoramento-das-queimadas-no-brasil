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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 444ba412-9150-37fb-8dfc-64f34e1e7f2f | -22.76934 | -44.66499 | 2024-10-03 04:55:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07af5578-33e0-3eae-b9d1-4e64bbb5bf9a | -22.76902 | -44.66867 | 2024-10-03 04:55:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8868698f-400a-39ef-8168-ed15edd5d90f | -22.18256 | -48.60936 | 2024-10-03 04:55:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31ba27a7-75f5-3417-b116-c31777433c45 | -22.17646 | -48.5773 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e332955-33d3-3114-b018-48d716fe9893 | -22.17591 | -48.58245 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2edb9779-7bf5-3b50-a48e-22615dd87b87 | -22.17445 | -48.58104 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c569bbc7-cc0b-35ff-ba6a-5a0d16b41941 | -22.17121 | -48.58185 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| eb03baa1-941c-341d-b075-1a97ea24440a | -22.54187 | -48.54068 | 2024-10-03 04:55:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b9490c0d-e966-3ac7-8605-e0bf7c07c8dd | -22.5413 | -48.54602 | 2024-10-03 04:55:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c1b2a3b5-836f-3b0f-9c12-f7982202e92d | -22.39088 | -49.2776 | 2024-10-03 04:55:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d193469-0131-3252-9662-060da30eda8e | -22.38413 | -49.25671 | 2024-10-03 04:55:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4a164db-0e01-364f-b379-b57813ec2901 | -22.38358 | -49.26151 | 2024-10-03 04:55:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 053c718b-380d-31ab-9a96-ac33695f4a27 | -22.36336 | -49.27821 | 2024-10-03 04:55:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 7b12c26a-142c-38b3-b193-3bec2479d553 | -22.36282 | -49.28297 | 2024-10-03 04:55:00 | NPP-375D | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 3d01dba4-8f28-396d-a6ff-cd4323c72fa0 | -22.22891 | -49.63362 | 2024-10-03 04:55:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9eb71cc5-04a6-3a4e-bc17-2b9c17f559b1 | -22.18912 | -48.63683 | 2024-10-03 04:55:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 586dcaad-c8e3-3e71-bb3c-c62013b96004 | -22.18856 | -48.64198 | 2024-10-03 04:55:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 31d02404-3a55-352d-95e7-e9a00417cd21 | -22.18388 | -48.64135 | 2024-10-03 04:55:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5888a1cb-5331-3b1f-913d-e579edd4f90e | -22.16207 | -48.62303 | 2024-10-03 04:55:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d20c475-44b7-3864-8f40-2bd3db647926 | -22.16149 | -48.62849 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 08e95eb0-98ee-3886-a25d-0bc0c996a252 | -22.15972 | -48.62694 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 0c728d08-0bc0-3ec2-b4de-dc597a26b44a | -22.1568 | -48.62789 | 2024-10-03 04:55:00 | NPP-375D | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 59a60b35-a760-3c9f-8493-d0c455279e92 | -22.15502 | -48.62637 | 2024-10-03 04:55:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9ea6de8c-ca74-32d0-bd15-5da7beb3d674 | -22.15211 | -48.62728 | 2024-10-03 04:55:00 | NPP-375D | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f667d345-1ba0-3527-8e64-6d69e751f1a8 | -22.02259 | -48.73392 | 2024-10-03 04:55:00 | NPP-375D | BARIRI | SÃO PAULO | Brasil | 3505203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f46ee577-6bcc-3fbd-91ff-95ab0b13a4b4 | -22.97713 | -49.17255 | 2024-10-03 04:55:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e40c52cc-93d5-3693-ae32-e97e4b6c4cef | -22.97657 | -49.17766 | 2024-10-03 04:55:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f77906a-7fdc-3fdc-af48-5adaaa649a91 | -22.54041 | -48.81421 | 2024-10-03 04:55:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2991f525-fb70-31c4-9beb-d335c672f51b | -22.99666 | -49.60963 | 2024-10-03 04:55:00 | NPP-375D | IPAUSSU | SÃO PAULO | Brasil | 3520905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b2cbc92d-7285-32ae-b501-fc5d7f87a6cf | -22.38404 | -50.23385 | 2024-10-03 04:55:00 | NPP-375D | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cd1feed4-62d8-3e4c-80d5-7fc061d98299 | -22.68462 | -50.47295 | 2024-10-03 04:55:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35ac4ac8-c307-3d16-8af1-5028626ff879 | -22.68412 | -50.47703 | 2024-10-03 04:55:00 | NPP-375D | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a2c9588f-8a7c-3a91-a1f1-c23a5b42acc7 | -23.02414 | -51.18539 | 2024-10-03 04:55:00 | NPP-375D | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 90267f10-34fc-3a9c-ab62-f89482ec0b44 | -23.0201 | -51.18484 | 2024-10-03 04:55:00 | NPP-375D | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3f4e8527-2406-3fd2-b0e7-696d4a47af44 | -23.01939 | -51.19051 | 2024-10-03 04:55:00 | NPP-375D | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 339cb146-5791-3f63-9aed-327ebb6945cd | -22.77224 | -53.36827 | 2024-10-03 04:55:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dd2ed8ed-9ad0-3c8d-a64a-1f4c23961522 | -21.34145 | -55.6669 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f2d01df2-ae17-393d-b76d-21a2cf8f0db7 | -21.34133 | -55.68982 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4098e809-d861-38fd-9776-1ac391a9cd00 | -21.36914 | -55.68706 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eb35bc6-fdc9-30f6-aef9-041ff64d48f7 | -21.36857 | -55.69078 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39428a28-05fd-33ba-a9f9-ec415807b043 | -21.36799 | -55.69451 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0124ad10-79a4-3653-9015-ace1e918a75b | -21.36741 | -55.69823 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99a13077-51cd-3585-9c58-daf9d234c0a5 | -21.36523 | -55.6902 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 872c3cea-2bdf-3d3b-a13d-3491a887039a | -21.36465 | -55.69393 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f4164ed-e9fc-3c64-b2ce-c303c92fe23d | -21.36408 | -55.69764 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56aaedca-b6ec-3fce-8bd8-07b6a3d639f8 | -21.35741 | -55.69647 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0438da62-0a80-3b8e-8ca2-d491ac102653 | -21.35408 | -55.69588 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 172b7ec5-8dc5-38bf-8d46-2410d65deab4 | -21.34926 | -55.66064 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57dba3f0-9139-3251-8f27-65368d22ad62 | -21.34869 | -55.66436 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eebe822f-3775-3e91-9737-67a604449ca2 | -21.34811 | -55.66808 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 056b639d-7772-34d1-879d-9438d59c3203 | -21.34754 | -55.67179 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dc8c6bc-fa1c-36d9-a759-f737983ba8ab | -21.34696 | -55.67552 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5b89a08-59e1-3e35-9b46-e460b4f9b76d | -21.34593 | -55.66005 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3be4c396-182a-3cb5-801b-a53d5d3dff6e | -21.34536 | -55.66377 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 158d0e1e-c5d8-3039-bca9-4f09c167e43d | -21.34523 | -55.6867 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e00983fc-46f9-3ee2-b30a-906d0648c5a6 | -21.34478 | -55.66749 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71e3091f-59de-3235-84fa-c431b85487d7 | -21.34248 | -55.68238 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7367e24-d35c-3b17-b105-a8c41fc568f0 | -21.34202 | -55.66319 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cde258f4-96e1-360c-b4d2-70f12fe85a74 | -21.3419 | -55.68611 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea7458a-cec7-355a-a0ab-0d9ddaef2488 | -21.34087 | -55.67063 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a6c33a5-2a4f-37be-8ffe-2a59c0e38568 | -21.3403 | -55.67435 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9da470ac-4169-339c-87f5-b5e9ed4979ba | -21.33972 | -55.67808 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a36e1c33-5d19-362f-9ce8-ea0bbcafae31 | -21.33914 | -55.6818 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba3a10d4-89eb-3d14-adc3-2008f4015d07 | -21.33811 | -55.66632 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 504faebf-ecd3-3d6b-892e-3173e260a658 | -21.33799 | -55.68923 | 2024-10-03 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab62a182-867a-3fdd-ba77-14fc6731e8ae | -21.33754 | -55.67005 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe6d6df4-62ee-3418-9ce6-2d101f51113b | -21.33696 | -55.67377 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37a52863-5342-38b1-83bf-9e82c4e8c6c1 | -21.33648 | -55.66636 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b1c62a3f-f4d4-315a-89de-597e5fefcee9 | -21.33639 | -55.67749 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab663269-3082-3a0a-9e2e-5fcfdc7fe774 | -21.3359 | -55.67008 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1cd7f8a3-129f-30cb-a985-07697a369bce | -21.33581 | -55.68121 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8728d9d7-41d2-3060-afcb-b675ec952cd5 | -21.33532 | -55.6738 | 2024-10-03 04:55:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 15918126-e32a-38ac-87e9-330b0912b436 | -3.43 | -42.27 | 2024-10-03 05:05:09 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8329f6cc-6740-3a7a-95ef-3593139119a1 | -3.4 | -42.27 | 2024-10-03 05:05:09 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95fe16c0-0294-31c3-8a0f-2e3da669c93b | 0.81288 | -51.85045 | 2024-10-03 05:12:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19d24840-9966-31c5-9e26-b1f42dc4463c | -6.11911 | -44.94287 | 2024-10-03 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b27db72d-3c1a-36d8-9168-65779038b251 | -6.11199 | -44.94157 | 2024-10-03 05:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d12f730f-7e6d-39ff-b9bb-e488eab88daf | -4.67828 | -45.88825 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a63c90dc-1ade-3223-8ddb-624c83efc974 | -4.67591 | -45.8833 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f519f2e4-8fb1-3a96-b160-42f53dbdfd0e | -4.67516 | -45.8888 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3957d4b7-97de-3029-b138-8bf41ad41084 | -4.67248 | -45.88137 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fd13d48-8f2c-383f-819c-b959d898aa22 | -4.67164 | -45.88717 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4c234fc-7fb5-3e35-ac2c-b3173eba64ca | -4.67016 | -45.87569 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffdc496a-2c5e-38ee-9c98-b6d6fdda034b | -4.66934 | -45.8817 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04b9fdb6-483d-3698-ae46-a3c127623db9 | -4.66853 | -45.8876 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d69ce5ea-7c1f-30d1-bbef-93b8c9c0c608 | -4.66673 | -45.87407 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b71a2a23-ebf2-34d7-b4e6-f63d4961bad0 | -4.66591 | -45.8798 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b242eb83-98ca-31a7-9710-0c572c89576f | -5.84574 | -46.23591 | 2024-10-03 05:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfa7554b-18e3-35b6-a8fe-d21d9af324eb | -5.84493 | -46.2418 | 2024-10-03 05:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4d02e83-d3d3-3c0a-ae71-4bcc53af1f0e | -5.08678 | -46.12098 | 2024-10-03 05:14:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 87df9c22-906f-3469-966e-371e614813b1 | -7.20745 | -46.68386 | 2024-10-03 05:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 32414bdc-6e69-336a-a345-d13c3005fa22 | -7.20695 | -46.68045 | 2024-10-03 05:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6222bdfb-e95e-30e5-b424-b7bfaec6ca1a | -7.20669 | -46.68945 | 2024-10-03 05:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8a395edb-f126-322a-923a-317a235fcffb | -7.20625 | -46.68595 | 2024-10-03 05:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| af3b5d42-0cf0-32be-ad10-f3aa1b4f08b7 | -6.66271 | -45.33441 | 2024-10-03 05:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23547f9e-b67e-31b5-8b08-c5ca6917788f | -6.64445 | -45.32982 | 2024-10-03 05:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb5e3ac-0865-301c-acc1-4f705d097794 | -6.64225 | -45.32602 | 2024-10-03 05:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 804e34cd-300a-3d5d-9793-cb041882d9db | -6.63737 | -45.32904 | 2024-10-03 05:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b470ba1-1c79-37a7-ba7d-8c1ba3626c36 | -2.53827 | -47.22808 | 2024-10-03 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10e27a4b-ffbb-3e02-a32e-02c6aae06d80 | -2.53761 | -47.23241 | 2024-10-03 05:14:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README149.md)
