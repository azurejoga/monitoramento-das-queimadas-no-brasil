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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae9c7839-4f39-3d27-b496-d33bd8e9a154 | -2.96699 | -50.39212 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 3d6628e4-4fdd-3da3-9f61-9a9b16f764c5 | -2.96572 | -50.40039 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c634ac1f-c56a-3f96-98e5-07790a11988a | -3.19877 | -51.0157 | 2026-09-12 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683b4803-6bc0-3628-8ce8-19e4f76db327 | -2.94414 | -50.46853 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd968629-4dc4-3a34-8eea-7404985a42b3 | -1.0312 | -53.73721 | 2026-09-12 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ec15efd-6a18-3af3-b795-85684aeb9d59 | -2.95362 | -50.40695 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ec3ce765-c054-3260-b12d-9bd064ff1c40 | -2.95001 | -50.40637 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| eedeb59a-4f4b-3814-b6a3-ef0a2e6db480 | -3.19525 | -51.26776 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8e7f48c-8688-38a9-a102-ad9b7f05b8b6 | -2.95977 | -50.39099 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 45e3d371-be21-3d11-a997-f3e1d2aee5a1 | -2.96635 | -50.39626 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 920c6d7e-6e1f-3632-a442-6a8373a8d5f9 | -3.47837 | -51.18701 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4492a1c9-250d-39bc-899e-b13cd74d65d5 | 3.98512 | -61.04253 | 2026-09-12 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 955ee0b9-97dd-3475-a020-c645ede8f142 | 1.22937 | -50.72603 | 2026-09-12 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c87a4560-adf2-3c86-a6dd-c56efdd08e87 | -2.97166 | -50.40973 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 97175d98-d092-362c-a9bc-b259ad83a441 | -2.72492 | -49.78824 | 2026-09-12 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19a88e1d-5734-3d7f-89df-29925604b8b8 | -2.94578 | -50.40992 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| deca9f09-ce60-3a92-ab73-4ee1d621881d | -2.95723 | -50.40751 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 1ac37b7f-0edf-3486-ad08-4198e300bf42 | -3.46656 | -51.62776 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d338d41f-997d-38f3-9bd4-a5996cc0be5d | -3.37929 | -50.75898 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d1d667-2031-3c8a-bfc0-c52b727c9320 | -2.96402 | -50.38741 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f94ebe70-fc27-3d0d-935b-d7ebc8baecdd | -2.96211 | -50.39983 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 07c9749b-fbcd-36f3-9566-aec14c08b82c | -2.94406 | -50.39703 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8365b6e9-6e15-363f-a23b-110aad3ec536 | -3.16139 | -48.60774 | 2026-09-12 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 31688cab-4fea-307b-82db-629a9ffae2b0 | -2.94894 | -50.38932 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5247245c-0e1a-3646-8966-d5055e073473 | -2.96274 | -50.3957 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| dc31b483-e494-3aa5-91dc-576a961d675e | -2.96869 | -50.40506 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 0350c508-3ce9-3f37-92a8-edfd668c5e20 | -2.97103 | -50.41384 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 99b0f411-3e0a-3e5d-a3be-b23964f63d86 | -3.36922 | -50.75333 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8fad6ca-fd52-310e-9505-b22e374cdf93 | -3.32777 | -42.29879 | 2026-09-12 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f644cef7-229a-37cd-88eb-ea90dfb84464 | -2.9428 | -50.40525 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28380182-0486-3540-8d49-86c30d24a9c6 | 2.51365 | -50.84674 | 2026-09-12 05:08:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbec2f3c-4a00-387b-8a07-30e8ddcc39e8 | -2.94704 | -50.40168 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 91a68d12-fce1-35c8-a4ba-988a6660b481 | -1.02787 | -53.7367 | 2026-09-12 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e0d59fc-a7cf-357b-9177-0c0a699a9b42 | -3.38285 | -50.75953 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d7e83e0-f755-30e1-80b5-33e4da2b75d3 | -2.94343 | -50.40114 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1eb1886a-cf0e-35b8-ab73-562456519c17 | -3.40886 | -48.88957 | 2026-09-12 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef6c41fc-80eb-363b-8dde-9362de1d5cc4 | -2.94226 | -50.48076 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90186892-619a-3340-9578-a2efe2051dd2 | -2.96147 | -50.40395 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7df8d610-b8ec-3a26-8fd5-9d5856d8136d | -3.95426 | -47.61774 | 2026-09-12 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 41474895-d5e6-3957-a83b-23c4195b905a | -1.77659 | -55.50488 | 2026-09-12 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec17b59f-cd3e-3c70-8d33-58af981c6870 | 1.03791 | -51.05723 | 2026-09-12 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e91f365-88d9-368a-a191-3daf5406e1e8 | -3.25119 | -50.81821 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb54a1b-bc18-3ac1-9063-0468b2f5db36 | -2.95382 | -50.3816 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c979382d-f61b-3609-8074-c753b5e31f95 | 1.32553 | -60.71231 | 2026-09-12 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e41aa844-202e-3934-9d1e-6a146950d308 | -3.37404 | -50.74585 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f23aaab-1496-3be0-af0e-3ceda532ab10 | -1.771 | -54.9481 | 2026-09-12 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba7231e5-10a3-3222-bd9b-679b11b90126 | -3.15737 | -48.60713 | 2026-09-12 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 758ad698-004c-3520-bc70-bc4ee4c0d292 | -3.22664 | -46.95507 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 3752fbeb-7d08-34e9-8dfa-8047bbb5b08b | -3.32631 | -42.29914 | 2026-09-12 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50a96407-e733-32de-b44e-bd69bd7bcaea | -2.96933 | -50.40095 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 062c26dc-df78-39f6-ae57-42b0ac381daf | -3.36735 | -50.76535 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1aec08cb-ccbd-3613-accd-4a0ff4481038 | -3.36441 | -50.76078 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eed783aa-07e3-3d20-b100-4a84a966e3db | -1.98856 | -47.04412 | 2026-09-12 05:08:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 922f1f54-4340-3a69-bfc7-1ebf83fe9d4b | -3.24764 | -50.81767 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d65edfbd-87ab-33de-8e12-d953c846b4aa | -2.9653 | -50.37915 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b70cb996-866a-3c5b-8e58-0a3ae7022a51 | -2.41574 | -47.96246 | 2026-09-12 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9acc29b5-4eba-3535-ad67-25926efe48f0 | -2.95596 | -50.41575 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3a7b86e7-dd5a-33d3-8728-4a656faf7712 | -2.9723 | -50.40562 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 91ed3155-7bc8-38d9-8f25-abf957858adc | -3.23254 | -46.9467 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 23c3f2ca-29c4-3ea7-9d14-3ef490e238df | -2.94648 | -50.47726 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e634633c-9a3d-3826-a846-d58db0368164 | -2.9568 | -50.38629 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54c9cc85-900a-3c24-a1d3-45aafec2e953 | -3.33245 | -42.30019 | 2026-09-12 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbfda2f9-568e-34d6-87a1-ee76ba2133d0 | -3.37091 | -50.7659 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05528e9e-b746-3540-b2a2-ba30957e9f61 | -3.19526 | -51.01516 | 2026-09-12 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdce9ef9-c154-3653-89d1-9c116af8449e | -1.77442 | -54.94864 | 2026-09-12 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95d6b273-e1c8-31bd-bfac-c01436b1ab65 | -3.36985 | -50.74931 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b00f099-440b-3523-aac4-6e0f8d9c29e1 | -2.93632 | -50.47152 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9113c74-d653-318d-8304-fb109de97d4c | 1.32004 | -60.7102 | 2026-09-12 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 991eeb49-7eff-3096-bdf5-945adb08c733 | -2.93866 | -50.4802 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8e69cbe-47d1-334b-87db-6a9b5a572f95 | -2.96763 | -50.38797 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b693a755-7087-34fe-b41d-a9743f7c2535 | -2.95489 | -50.39868 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 9a5fbe3c-6d5f-33ea-8b19-70fa80e972d1 | -2.96168 | -50.37859 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 878a3b76-4aa1-3d20-a930-84a2f55901c2 | -3.37572 | -50.75844 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a37beb42-0490-318e-8c87-f6d7622938a6 | -3.21737 | -48.96888 | 2026-09-12 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58691424-81d6-3bc7-a5fd-901eade50181 | -1.03064 | -53.74072 | 2026-09-12 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38419e78-a821-3277-b49f-69deec2a6e56 | 1.32049 | -60.71312 | 2026-09-12 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f23d8f13-9586-3b82-81d3-4730fa471087 | 1.22658 | -50.72649 | 2026-09-12 05:08:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313c9c70-3cca-3e45-8404-19f3c38227f1 | -2.95299 | -50.41107 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| af53f19a-a78b-3252-aa13-4a4515ee9e60 | 1.32508 | -60.70938 | 2026-09-12 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66c89467-ddf1-3e80-8a24-c886c614df97 | -1.73072 | -57.15755 | 2026-09-12 05:08:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ae11ad4a-7b73-331e-889b-56189035b6b7 | -2.95786 | -50.40338 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ab90a895-65b7-3223-a887-9a3334220546 | -3.38642 | -50.76009 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d0f7534-7530-3e2a-bd0b-656909eb4e35 | -3.54589 | -48.17878 | 2026-09-12 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e6ee9aaa-c56e-357c-b9e8-f3518c475731 | -2.95914 | -50.39512 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 27fddb34-bfa9-38b5-a7f2-af4f7d93fcfc | -3.19465 | -51.01906 | 2026-09-12 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4dd5a6e-de06-353c-abd9-09e3dc2aaac7 | -2.9483 | -50.39345 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a794a97d-4052-3cdc-bbc7-a9baeabe7d8d | -2.47282 | -48.04214 | 2026-09-12 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e54985da-55de-3f26-a3e9-20e20e90f583 | -3.3686 | -50.75734 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6526d22b-b788-3f13-a626-568d8b764463 | -2.96105 | -50.38272 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba57c9fa-4118-3ab2-9d2b-fe39b21ca317 | -2.96742 | -50.41329 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| a8a27fde-d814-3246-b82e-69e0cd63d979 | -3.05501 | -51.24293 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90af2c47-b73f-3826-9a2c-17aa1a4833a4 | -2.95616 | -50.39042 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0f36a0f0-d177-3d07-b545-b18c3f6529ca | -2.29829 | -48.58461 | 2026-09-12 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d0b4448-1c42-3bbc-b8a2-ca635b6900e8 | -3.19117 | -51.27106 | 2026-09-12 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e9a0819-bc96-3379-b3f3-9c30dc443c37 | -2.96678 | -50.41742 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 41f0793b-65d6-3b77-854d-29beb036a928 | -2.96508 | -50.40451 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a25158e1-e2b3-3ffe-a95d-bd5a2144b9e6 | -2.94351 | -50.47261 | 2026-09-12 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4bb1d11-70ae-3eb9-822e-46bb1cb7ab23 | -10.55302 | -45.21883 | 2026-09-12 05:10:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aed4623-d5bd-3aba-948f-0b681ee3bd3a | -6.28534 | -56.02279 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72a5a4a6-fdd9-3f84-9ce3-273fb22886b4 | -5.55235 | -43.43333 | 2026-09-12 05:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README33.md)
