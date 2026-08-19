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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e20cfa4-09f2-3482-b3d1-47ef8ce18ad9 | -8.58117 | -54.73627 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1193cfc-c3a6-3108-ad90-e306db5e2223 | -9.40157 | -60.56837 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79693eaa-d48f-3290-b32b-539765fe23fa | -9.17 | -59.70272 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f42ce1c1-5284-36a1-afce-9b9f108c69e9 | -6.14039 | -57.86929 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5221da8b-9641-30f6-930d-b7d7bf6d24e7 | -9.42147 | -60.42006 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7c76644-9805-3a7e-8145-117428ae1e0e | -8.64383 | -62.83157 | 2026-08-19 05:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 286bd1b6-b458-3d18-ae07-407a63849280 | -9.42418 | -60.43563 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ea5647a-9aca-3873-874e-07aab662326b | -9.42103 | -60.44925 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67013eec-51f4-3076-ad93-745a68091017 | -8.56042 | -54.68441 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c89d2ad-4bf1-37f4-b5a2-5607472b7d37 | -6.68774 | -59.07162 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae0e47a-98e3-3717-8a41-f38abdab8560 | -6.85764 | -59.02309 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32359d0d-6d2f-3fd2-b71e-4bb506ec3ce3 | -6.74365 | -59.04045 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c6ba6a7-25b7-3b21-9129-c4ad83312a23 | -8.57199 | -54.75411 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 079b4cbb-9466-381e-91c3-cf9c4561f63f | -4.12372 | -60.78201 | 2026-08-19 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a68a69d3-96bd-34b0-863a-1cf85aa00602 | -6.70721 | -58.93614 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11f86317-4461-38bb-9bb5-7b7dad9201d1 | -9.42525 | -60.41951 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6af85e4b-47a1-33f9-9950-baf6b1475872 | -8.56318 | -54.73734 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17977b31-d433-34a1-a82f-548e8be9950c | -6.88362 | -59.05546 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 319b33fb-3aad-3d79-a3ff-985e01c13f76 | -8.56604 | -54.74722 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a838c17-bae6-3797-bfa2-23d9c9765a4a | -6.84661 | -58.99246 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f9fa561-fa5f-353a-bcee-071095de009f | -8.57298 | -54.76906 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7961f3b5-66ba-3e1a-bb6d-00cd12045f45 | -6.63079 | -59.08058 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef15c7a2-cc19-3f1f-9d77-f59c6503265d | -8.54607 | -54.76527 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 24b354a8-63eb-342f-ba2e-b409debb1028 | -8.55103 | -54.7573 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f77df66-32c5-364e-bc97-8bb10d604b9d | -7.10866 | -59.7672 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82fd2244-fba6-3c38-80b3-fdc1e412562d | -7.1039 | -59.7665 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b14cf78-8ae1-3afa-b955-344d7fa0baa5 | -8.53915 | -54.74315 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3e6f60c-ddd5-3632-960e-056f7936491c | -6.35915 | -54.90097 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 66fe7216-b881-39ac-925c-fd900c85fd5b | -5.99664 | -57.85892 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7d58a197-ce8d-3d26-af98-a7b48152ed3a | -9.22258 | -60.82522 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2e1a8d6-3ae2-37f4-b5f4-1015157df234 | -6.84982 | -59.00982 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01d655d4-83e7-3e09-a6a2-abe5ef6f1b01 | -6.74443 | -59.03481 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0b2e8c7-00c5-399e-bfb2-0094cc929b61 | -9.39558 | -60.56131 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b06ddb9f-3104-33fe-bb57-bb33064702a2 | -6.34393 | -54.91514 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2ad0b78d-9de7-3f59-90ae-6337278f76f0 | -6.0342 | -57.80936 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57948aea-a7d7-38eb-a267-841e05aee462 | -5.99905 | -57.84206 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdfeef52-d284-34b4-bca2-3ed19ff88a11 | -8.55951 | -54.7673 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 413bf952-8e49-37b1-ba84-1c994c907565 | -7.88723 | -61.19109 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86c522fe-5c3f-3585-8d47-954cb6fdf661 | -6.86105 | -59.03513 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1dc49164-f7c9-3465-9a22-3623cb706234 | -8.5639 | -54.73149 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 31bead16-183b-3c9d-85d0-cf4f41a08a36 | -8.50383 | -54.85951 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 414446e4-34c6-3fd9-8eb3-291047834623 | -8.90202 | -60.55226 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c4acf20-d287-3ad8-8042-89d3c40ea5f6 | -7.88286 | -61.19048 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d22a8b4-b770-3e3f-bcb3-65ea5869f65f | -8.55208 | -54.77212 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 135960f9-3914-3986-b632-80f8e257c6a2 | -8.5654 | -54.71925 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4c3876d8-aacf-31d3-8f4c-3d7aed6ca636 | -7.8694 | -63.761 | 2026-08-19 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a96cd349-0689-3f23-bbeb-b5fe890f8433 | -7.43724 | -59.78219 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e74033d7-435b-3c24-9f45-f3b399355f46 | -6.04329 | -57.80056 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b96d9710-2182-30a9-b360-5079e3e4925b | -8.58791 | -54.75901 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf17eaa7-77dd-3fec-a734-0ca0c74d1292 | -8.94967 | -60.54937 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0be8a656-52a8-3afe-a0b1-354260b647b2 | -8.57645 | -54.77248 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1c58639e-fca4-349d-b2af-7a0eb064cb30 | -8.53242 | -54.7422 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47c39b27-a26f-3cc6-9c4e-71f952b61610 | -8.58073 | -54.68694 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e31f6ce-56ed-358a-acf4-6f2a72f174c3 | -6.14347 | -57.86596 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d61126b8-a447-319f-bc73-6d1077ae8384 | -6.85153 | -58.99816 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1353231e-553c-37ad-8028-2108479d45bd | -6.10298 | -57.86396 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f49eb90b-4aa3-3801-9b66-7432bdb35168 | -6.3585 | -54.90061 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f27657c-1f77-3728-b9e7-a85d4e0e7a86 | -8.55571 | -54.74243 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6adfde0-ba35-3c0e-83c5-786965fde031 | -8.58643 | -54.71571 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70fdc189-9566-3c4c-adff-c832c32c47fb | -8.56011 | -54.74002 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9c771fe-a9b1-3e2c-8f3b-bac3cce20426 | -6.78516 | -59.44926 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b93f973-9c80-32b6-a13f-e260bf93c10f | -8.55415 | -54.7331 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53306101-a575-3416-a2f6-ed550a64538e | -8.56718 | -54.6853 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c047281-fecd-32ed-8cdf-8fd501426de5 | -9.01509 | -60.50656 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23082b84-8b72-3a39-87a0-8ad34762e49a | -7.60983 | -60.94702 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da02c087-066a-38a8-8838-2a97f4faef65 | -6.76144 | -59.46326 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 581d498e-1410-3364-99bd-4a96a2814934 | -6.76772 | -59.45353 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 69580494-8b6f-3dd5-a0ec-43bbbf9154fc | -6.75025 | -59.17327 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db3a5658-1090-3805-a71d-7cb791a14eca | -19.7647 | -57.9191 | 2026-08-19 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 07f3930c-484c-3c38-a4ea-3e18f6c8cd67 | -14.8033 | -46.6453 | 2026-08-19 06:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 137.7 |
| c01b0043-70a9-3bd7-a5cf-bb9c4badb2d7 | -19.7442 | -57.9425 | 2026-08-19 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 85e48937-54ee-37f8-8d5e-99995c2b2b37 | -5.9994 | -57.8639 | 2026-08-19 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 887bd71d-df09-3297-9972-c9779b3a2e45 | -8.5785 | -54.7566 | 2026-08-19 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e5d6bb4e-d524-3d9a-838e-2963fcd0ea40 | -19.7643 | -57.9399 | 2026-08-19 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 195.7 |
| 10608832-ba9a-3a71-8a9f-cfc311c7131c | -5.9198 | -43.6264 | 2026-08-19 06:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 275053c6-2885-3248-9e7b-4e683c495f09 | -14.8228 | -46.6419 | 2026-08-19 06:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f9922089-364d-321c-9252-00109b1cfa8e | -8.56 | -54.7377 | 2026-08-19 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b651632c-d6fe-3b86-a368-fbe86c1f8964 | -21.5343 | -52.0046 | 2026-08-19 06:00:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| e878941e-75ef-3f2d-af2a-251b8f757f0f | -5.4317 | -48.4212 | 2026-08-19 06:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| e5ca4386-4114-3f47-9729-e7e30763bcfc | -19.7639 | -57.9607 | 2026-08-19 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 97745f6a-da24-3279-9033-5e58d76af187 | -8.5598 | -54.7579 | 2026-08-19 06:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 16928e8a-6f28-30f7-a9b3-c56a89a2ceaf | -14.8028 | -46.6683 | 2026-08-19 06:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 15e208ca-1403-33bc-970c-af997e604038 | -6.0912 | -57.9187 | 2026-08-19 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 93bfcf11-6e37-3c5f-8a7c-74ceaf9e3be6 | -9.55165 | -63.52413 | 2026-08-19 06:01:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da7509c9-1508-34fe-bf4e-0a9e0d47c2e6 | -9.08046 | -65.39021 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6be1f11-8abb-330d-8e4e-ec2bfcefb23b | -11.22854 | -55.0688 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c72e90a8-e14d-341b-9036-830541dbaed5 | -11.22244 | -55.06176 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519ce117-a933-3368-b6d5-5af31d3cbb4a | -15.77483 | -55.56566 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33935e51-52aa-33d8-a87c-1e867a5ffd41 | -15.76637 | -55.58022 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d22a19da-89d3-321d-9131-9894a054fb48 | -15.77436 | -55.57052 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5eed862-bb9b-324a-bbb8-4ff769d218ca | -11.23754 | -55.06269 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41c13ab6-abd5-3b85-8917-7132c84ee0ca | -15.32028 | -56.45619 | 2026-08-19 06:01:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85988d96-895b-3e96-810c-0f46a861bd98 | -15.31888 | -56.45603 | 2026-08-19 06:01:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d9b3355-fe5c-38b9-a2ad-47ff58092ad2 | -11.23537 | -55.06968 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fd3689ce-577a-3f21-8f2d-910f573620f6 | -9.07811 | -65.40557 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b7ee221-a5d7-344c-9957-233b1b81b51c | -15.87926 | -55.56877 | 2026-08-19 06:01:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 178269f0-b508-3826-a758-cd2f36758eef | -11.22319 | -55.05534 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16a411bd-9547-3b49-b2f1-dd9911bce079 | -11.22927 | -55.06259 | 2026-08-19 06:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 749ab3da-0392-3115-8bdc-92929332095e | -15.23161 | -57.66288 | 2026-08-19 06:01:00 | NPP-375D | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e60b9655-2c8e-3a73-b976-11e44b5d883f | -9.07405 | -65.40887 | 2026-08-19 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README70.md)
