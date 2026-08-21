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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a09a2eee-e1a4-33ab-8023-47df71ff6fb5 | -13.37512 | -54.37776 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 269a032b-c565-3d22-9d8d-0b391809e172 | -13.93075 | -53.84853 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec21d8cf-90a4-3652-aa48-172237c61da9 | -6.22971 | -55.61628 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d6de66bd-acbb-367e-8fa1-e91757cf3cb5 | -6.82059 | -59.40187 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 94b8e013-c14d-38b1-9e48-3697c31f8ba5 | -6.71028 | -59.09106 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57c52477-37b4-3d2d-9500-f10b31aa5c85 | -6.23214 | -55.42291 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a516329-ebec-314f-a738-3901f8e15e5c | -6.87069 | -59.41758 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac46a389-c0b6-3d42-a3c1-3601d7526dda | -7.25447 | -49.9099 | 2026-08-21 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b6dd7d3-6022-3678-a8ba-3484838c08fe | -11.3248 | -45.01173 | 2026-08-21 05:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7290414a-a0bb-309a-a02f-ba73064d3620 | -9.16211 | -59.66376 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fdc80fd-0724-3612-b97b-4a5f5cd4f0c2 | -7.60947 | -60.95376 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79502f3c-7676-37f1-9468-b0f22ac8d973 | -14.0249 | -58.88021 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cc5bc36-c292-3c49-b689-0ee59d2a8f6d | -9.06484 | -50.88231 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 989e0c8e-f4c9-303e-bf77-58a925f11c7f | -6.86949 | -59.42499 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96871767-7f3a-3540-9d3a-105edc5a45e9 | -6.8848 | -59.4389 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5701818e-e12e-380a-8877-abed6c5d5162 | -6.82523 | -59.395 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7934122-28f1-390e-93fa-dc3838584b7f | -5.81213 | -55.72248 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d624ec27-6e1b-34a5-943a-340f7ca4cc01 | -14.08374 | -58.86759 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16610999-bc89-3615-a437-001e6b69f665 | -6.58609 | -58.99709 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00393a04-71bc-30ee-be8a-2fd529728b6d | -7.77609 | -61.16585 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6f64aa85-1d8e-3764-b44d-98daeda922e2 | -6.79879 | -59.43262 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ce42d7e-56da-3709-894d-c7b8a8e1e6b5 | -6.87129 | -59.41389 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ad34313-2f8b-3407-b813-1578bd69f040 | -7.0679 | -59.9632 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cca2397-f9be-3c83-a133-95cd6db861af | -7.83758 | -61.13045 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59fdd2eb-1885-3de9-8437-97fabf1db7b3 | -6.12529 | -57.69069 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18e47371-40a8-3735-add9-46fc816c2343 | -8.15729 | -55.37483 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1aa3891-ba1c-3af2-8dcc-104fd14eef71 | -14.02378 | -58.88734 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3a624a5-a859-396c-b392-0c9cf5085427 | -7.45283 | -46.15582 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07c45b72-f018-30fe-8b6a-675f66f4f951 | -7.42419 | -56.26591 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cd96779-f34a-3128-a36b-b6eda6ce5711 | -13.4475 | -51.78276 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c6f45f7-9d11-3ba8-966d-54479842e78c | -4.95269 | -56.26414 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f177198a-e965-30f5-a10b-c473c81979e8 | -6.82462 | -59.3987 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56dd9e3d-f2b0-3f69-a6f8-1fb2adc0d09a | -6.60039 | -56.37493 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8abdb6c-9056-3cea-ae17-5c6741c82707 | -6.83146 | -59.3998 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a82b4c77-af84-3c66-850e-ca9da2f4e241 | -6.00562 | -57.86742 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eeed27a-b643-3b4c-8717-39ff90dfa2e2 | -9.05175 | -57.0682 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a723580c-7e66-3773-957e-2df47fbf8e1e | -3.01485 | -51.05751 | 2026-08-21 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e953d327-bd9e-3ff1-b6c2-cecd46183411 | -13.37907 | -54.37836 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 3b893863-f5bf-337c-ae55-a4b70921e425 | -6.10372 | -57.86872 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4149086-7653-3570-90e1-71afd01a4d42 | -14.45491 | -45.62555 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 798578a4-448d-3955-be82-d20dce86574c | -5.82007 | -55.71623 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19795b6d-bbe3-366b-8e96-2221b591cd7c | -6.08598 | -57.91578 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 284f1c53-b454-3943-a2c4-6dee4f8f520b | -9.06955 | -50.88284 | 2026-08-21 05:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21ce6d6f-11be-3826-9877-a60f4c2e9276 | -7.5498 | -55.55935 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fd9e002-aaaf-34d7-bff1-cdbd1a9c77ed | -8.89746 | -60.54366 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5fbe7754-2a89-328d-af58-933dd37ca268 | -13.38446 | -54.36872 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d5cd9321-6a26-353d-ba1d-42b8e95e638f | -7.36118 | -45.80725 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 880331c6-0150-3af1-b9bc-e56b56322fc3 | -12.49739 | -54.75896 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9169fe52-24bc-3b0d-9db5-eaa13aaff5d2 | -13.93435 | -53.85303 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e48b03a6-a7d4-308f-a9c0-b22fbf91a8dc | -8.9003 | -60.54506 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b671aec1-8167-3d3e-a7a8-d821c229a417 | -14.31386 | -51.88825 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c0134603-b355-3325-bc04-99236b371a2b | -13.39091 | -54.3802 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 83d2910e-ba0f-39e1-998c-f772c132b51c | -6.17239 | -55.44432 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 6925fb01-9b08-3df2-b213-154d586f6c44 | -6.88719 | -59.4241 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d2ae2610-2b75-364f-b7bd-c61fa75b867a | -13.4361 | -51.79655 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 865278a5-55f7-3a2c-a0f0-3c78ac673e78 | -8.10481 | -51.66748 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cafb274d-a918-3f0c-bf12-c1267dff2c57 | -6.12145 | -59.91848 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15805dda-809d-3433-bafc-dafbcb9b2786 | -14.31257 | -51.89847 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 578b6d3f-4ca0-39d0-a3a2-22068f296c7a | -7.25521 | -49.90471 | 2026-08-21 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5907a95-c178-399f-84da-f9c16bd54063 | -6.87693 | -59.42242 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7ab47067-29fd-30bb-9ad4-84eb86a2a0c3 | -8.17508 | -54.99303 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74786c58-b5e0-31ee-b5a1-6834841ecc52 | -6.82744 | -59.40295 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75f6f22d-4ee2-3cf8-b110-17bd31891fa4 | -7.60052 | -60.82818 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2f576a9-c18c-3419-b586-172cc5fbfcfd | -7.60877 | -60.95798 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b8565d0-aff9-3e82-b50b-c8580fd8329d | -8.54582 | -55.30485 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 829c3829-5c24-31eb-9c78-102736a4acdd | -6.00285 | -57.86341 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f44934f7-bcd4-3152-adc3-59e83997fa8b | -6.7069 | -59.0905 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7761fc0-2250-3179-b479-ea16385fc25d | -13.40412 | -54.38961 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67c03945-a506-32f1-9bd9-9d6333b921f6 | -6.71987 | -59.09636 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da1aa9e-a092-38f7-af35-7211810c539c | -6.8622 | -59.03733 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d96505e3-8ddb-311d-8169-ca0a406a4787 | -10.30331 | -48.23187 | 2026-08-21 05:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700a5c0b-e661-3012-a947-317948a77775 | -6.64824 | -56.40752 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abbaa758-3580-342d-9d05-52fa9f92dbd0 | -8.40509 | -62.70111 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9da15fc4-cbaa-33c3-be3f-b0a96d25d260 | -8.54115 | -54.78578 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76514d03-2326-3919-9be0-d14f2efc0a9f | -8.57807 | -54.78713 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7f412bf-dd9f-39d3-abb6-5faab88aa952 | -8.41077 | -62.6916 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 680e0a21-0b62-3c66-a6a3-12805bdade34 | -8.06248 | -50.10765 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2e14ba7-7aba-3390-b657-f06c90997b0c | -14.07265 | -58.87307 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38fe5df6-6628-3412-92c9-bfaca97b178c | -14.00809 | -53.68182 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bceba07f-7a70-3d83-8301-1e539aa02f46 | -8.49611 | -54.86486 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8273ebd-a2ca-3abc-8e4a-7bbddcf59d96 | -9.44977 | -51.60954 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7cea296e-01b3-312b-9ce0-96eb95b1a15a | -6.88377 | -59.42354 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| daa8d1f6-cb9d-34c1-9e1c-e05e7bf30e2c | -7.61032 | -60.97123 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5513294-f78c-3975-a625-28dac9d4474e | -8.59963 | -54.74287 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5458dabf-b5d3-3973-a46a-833582c069f9 | -7.00076 | -59.04846 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9d7187e-e0d5-3d40-a33f-ef98ba3ee037 | -6.58739 | -58.96758 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28b651e9-bff3-3911-85d9-825e304bc8f8 | -12.50569 | -54.75538 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c14b313-f3f5-3893-97c8-f2f1d4ac94fb | -6.57608 | -58.97317 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4206e21-5e03-3f63-a210-40fe01142dab | -8.58723 | -54.77564 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65d8b975-414a-3c7d-b436-b8f2d54c970c | -7.77304 | -61.13897 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31da35ad-79e9-32db-b7ad-130c279b3bce | -4.51025 | -55.45053 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f563fa98-26e2-3663-847f-baae0c3d68a1 | -6.88762 | -59.44316 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e7ef289-b607-314a-b1e5-4c2c6d7504a7 | -13.40889 | -54.36719 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 232c987a-88aa-3a40-9598-54022fea2703 | -3.53464 | -48.17981 | 2026-08-21 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ad7c223d-8581-367f-b155-14fb5c91864e | -7.6361 | -45.77028 | 2026-08-21 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 242cfc12-5211-3423-a527-ea0fcdb28ef5 | -6.09984 | -57.87167 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5db0caea-89ba-33b8-bfb6-7c65c3738eb4 | -8.09228 | -51.6614 | 2026-08-21 05:23:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38c7672a-5d2f-3725-9314-81310d4935cb | -6.92076 | -59.34618 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa6d962b-1651-3dad-a396-5b64753e3fca | -13.43667 | -51.8084 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f02be6c-b6c8-39fc-8233-65e47fb77db3 | -6.8747 | -59.41446 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README58.md)
