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
| 480371b0-f4f9-384f-a387-b7f1f80c293a | -11.45712 | -50.1664 | 2025-08-12 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29a78021-65c0-3729-abf0-3151084477c0 | -11.69024 | -51.60504 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e592b5a0-1f68-3741-b365-8897cb20a2b9 | -9.38178 | -61.53144 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b89da9c7-93cc-3c82-8d84-e8ed265cd10b | -8.56791 | -54.70083 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90163c41-2f98-3691-bc10-7d7bb03c741f | -13.33671 | -50.2465 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8a9cb176-bc3f-3f53-a4ae-c85850c40638 | -13.04071 | -56.84082 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 758b4ce8-fedd-30f5-bc10-567ba788700c | -11.67138 | -50.13654 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a134c6b-2310-33c6-bcc2-630a8decb5f7 | -6.96972 | -59.28799 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ed2cc25-c409-36f2-862c-e2a2170e2d4b | -10.75606 | -48.79111 | 2025-08-12 05:25:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a29e000-9869-3bfc-be72-dffd600b266e | -13.3493 | -50.24804 | 2025-08-12 05:25:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 559041d8-bf15-3101-8473-b9fce37d3810 | -13.06145 | -56.84017 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92f077d0-3a77-3f09-b292-c8f8b807202f | -10.34526 | -50.81909 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20f73018-5fc1-3aaf-868c-c00f9ed00848 | -11.64773 | -61.64834 | 2025-08-12 05:25:00 | NPP-375D | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52ce5d60-d422-3994-b3ef-143f2033493d | -6.97254 | -59.29211 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d408b5d0-56c8-3fcb-90d0-241a0290af18 | -8.92627 | -60.73149 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3985e4-c9be-386f-be02-fccd123a6073 | -7.06296 | -59.19946 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c7fbd58-c2c4-3086-9a71-ad3603240050 | -9.03593 | -59.75998 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75d011e8-4694-3e0c-ba92-70e5973b3d17 | -9.1962 | -59.66597 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3da8a119-70ed-331b-bfa4-bee230a1b10d | -8.56231 | -54.70868 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9834215-a1a7-38a5-9379-be7bc59f621b | -11.64829 | -61.64482 | 2025-08-12 05:25:00 | NPP-375D | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38e71cfc-caa0-308b-adfd-3d4e8b0b95da | -11.71097 | -50.12169 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cfb43eb-2f18-3afc-ae57-14c2169a7f74 | -6.97702 | -59.28546 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b339b205-65c2-3626-98ca-da1b2a82c21d | -9.03139 | -59.75883 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb7e69d8-9a47-369e-921d-50ce4514f794 | -9.6496 | -62.9136 | 2025-08-12 05:25:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fa10d06a-4522-3364-84f7-872abc0d3bb4 | -10.36123 | -50.83378 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f881350b-f832-39b9-83c8-27bed65c8650 | -10.97286 | -49.56956 | 2025-08-12 05:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e157494-8882-3f3f-baad-80492c1b9649 | -8.57351 | -54.69293 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 805b93d7-8995-3904-9e8d-2aa179b39ce3 | -10.62309 | -65.00734 | 2025-08-12 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 823b0a48-3012-3554-a542-560881a79f12 | -11.6838 | -50.13812 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b69037-f0c9-35e3-a86d-350f928ca97d | -7.137 | -60.13012 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 034d24d0-1a39-3b0c-8ecd-0e4470f121f7 | -3.43028 | -49.03973 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de636d19-1edc-392b-bd54-61243584ac02 | -7.04099 | -59.18491 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 626cd793-d02a-382c-aac6-3eaa13c9946e | -11.67989 | -51.59552 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71958157-27be-329e-ba7e-6d43322891b5 | -7.28515 | -57.64743 | 2025-08-12 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08fd6c88-f743-301d-8edb-1e6563d49ff0 | -11.67195 | -50.13168 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a61662d-52d8-39df-923f-4c4f92e2ccd3 | -8.5729 | -54.6972 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30ec216a-aff9-3cca-a7b1-4d72e66f20bd | -8.56851 | -54.6966 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec8d2f53-5fa2-3ed2-b08e-eedff2cbba55 | -9.38788 | -61.53601 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6742307b-af10-32b1-a88b-8ecf6404f5db | -8.90904 | -60.5417 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28e36ae3-2811-346a-a9cb-4de0a4711c6e | -12.36361 | -59.84587 | 2025-08-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9661c5a8-1d8e-387b-8ff4-e1ae38f2e527 | -6.69569 | -59.13914 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71b10dc8-0c3b-37f8-ab1f-3d0f66f96b73 | -8.57229 | -54.70145 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dba9e21-d10a-36bb-9a12-1a50cde736bd | -7.06538 | -59.21037 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fec8acb-84dc-3a0e-90ec-315e4228ab75 | -8.57859 | -54.71971 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8b7d941-7250-34da-bbeb-e58afa8b4c9f | -8.92959 | -60.73202 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20696bc9-db07-3783-8583-d8eaa9afc26b | -7.44442 | -67.73627 | 2025-08-12 05:25:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ecff901-749a-38f0-9df3-b00a874987be | -7.06931 | -59.20729 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99713d7a-89c0-362d-aa7c-b9a9683bf542 | -9.71309 | -49.47711 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4f4496d5-eb05-33ac-a1dd-4f46e1235331 | -7.08 | -59.20524 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fbbc16a-e32d-304a-a26e-0ac03a2f1323 | -7.12702 | -60.12855 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66cb8422-4511-340d-95c0-992cd4575a3b | -7.13367 | -60.1296 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a876040c-06c0-3e65-a6d1-3103f7104b2e | -9.7218 | -49.47853 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11f08771-9e91-38c9-853a-264cb4dbfe4f | -3.83723 | -47.74508 | 2025-08-12 05:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea99fc29-f99b-3693-a532-e25ea6645c50 | -10.35162 | -50.81577 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 979c88d0-f563-3720-955d-89ae61905fee | -9.70859 | -49.48172 | 2025-08-12 05:25:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 08df2f20-44fd-3f2f-94da-001e1f85cedf | -6.105 | -59.93229 | 2025-08-12 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6a3767c-b9aa-37ae-ad4f-2b6daf8acd34 | -10.35641 | -50.82489 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4090388a-588d-37cf-ac5e-a5108605e351 | -13.06095 | -56.84388 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69feb554-f003-34ff-96ed-3964f8dca1d8 | -7.28875 | -57.64794 | 2025-08-12 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6444f2f7-8b7b-3774-aa42-60f953add40a | -7.44526 | -67.73148 | 2025-08-12 05:25:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28563b24-c858-34c1-a5ad-7afdd8e8c66d | -8.56974 | -54.68804 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59dc39a7-557a-3346-aeed-d79f7bb7625c | -9.37957 | -61.5239 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77ef581-43d1-3a71-a0c5-0021ab5fb553 | -8.57168 | -54.7057 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5cdb3d2-33bd-3df3-b771-a1762d8caaa8 | -8.57035 | -54.68375 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fa580d1-2d74-3673-bc1d-7bca36200677 | -11.70761 | -51.60387 | 2025-08-12 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d73c7a0-5eaa-3d68-a8f0-e7b520eebd65 | -9.37292 | -61.52283 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 812c9f49-97ed-3389-b846-1474d7a1199b | -8.56842 | -54.66594 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1566f6e-7ce3-300e-815a-311fd086348d | -10.34954 | -50.83226 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8fd3a51-2052-3716-a387-a9655c59d154 | -10.74252 | -58.01905 | 2025-08-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d165e4dd-0ad4-3fef-81de-99d717ee4828 | -11.73081 | -50.11423 | 2025-08-12 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f1b3f00-2af7-3e70-af53-6506878f5d34 | -10.35538 | -50.83302 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4130bb6e-fa64-396a-81ff-113527b2d974 | -9.53769 | -66.14424 | 2025-08-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b186232b-934b-3ca3-a7df-105da7208baa | -11.68312 | -51.59333 | 2025-08-12 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d06ba06c-9776-3bbc-b9a9-b16f47ba3e39 | -9.37846 | -61.53091 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 143b5188-df45-3c45-87da-27e814c945fe | -9.37902 | -61.5274 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7463291-26ef-34e2-98d4-680c1199a1a9 | -12.36017 | -59.84532 | 2025-08-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 09f0ace6-f2b3-3580-b57e-88a78dce5341 | -8.57412 | -54.68867 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b2df683-ab97-3a85-93d8-70c01458e70f | -10.36175 | -50.82969 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e65e71b2-111e-39dd-a534-f3073652c3c5 | -13.90329 | -51.82934 | 2025-08-12 05:25:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6a5866c5-e3d0-3832-9dc2-0ccd4364e5a9 | -7.13477 | -60.12262 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c7d70302-53a0-36a1-b3e1-bc13b3c0e6fc | -7.13531 | -60.11913 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e323b2ed-1f27-3f03-a24a-51ab8193d9b5 | -10.00637 | -59.95714 | 2025-08-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ca9401-3c95-3b78-8140-5349d9bcc5f1 | -10.35487 | -50.83708 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9b0beae-316b-3858-9257-838d87c7440c | -6.9742 | -59.28134 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d2f8085-17ca-3d44-8dc9-583b97ce52bf | -13.06551 | -56.84074 | 2025-08-12 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed97cbfd-754d-305d-ae73-029b98ec2d09 | -7.13312 | -60.13309 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab976691-b772-31c7-83f0-05113b06a980 | -6.97309 | -59.28852 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 48281457-30e7-3b59-a5ee-22cdf28c9f65 | -7.06703 | -59.19958 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac67801c-37e2-336d-bb3b-f1de680868c5 | -6.96409 | -59.27977 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 651939ba-fa98-3ece-ab59-f7d836743f4e | -8.56342 | -54.66962 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d9b4ff-764a-3216-a49a-24954d957aa2 | -7.07324 | -59.20421 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af4dbdbc-6605-3c64-ac27-1637c905fcbb | -7.08787 | -59.19908 | 2025-08-12 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66a44ff5-9834-39e7-a949-28fcc8576cf5 | -10.12288 | -62.16848 | 2025-08-12 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| be67b275-dc78-301b-a1a2-adab24f34a2c | -8.92962 | -60.7535 | 2025-08-12 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2581689-c196-31b6-990c-4222478cd94d | -8.57668 | -54.70201 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 681d874d-9904-3241-ace4-fab8cfd749b4 | -8.56292 | -54.70443 | 2025-08-12 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2e918a8-3469-3d92-be4d-64399937a87f | -13.89708 | -51.83271 | 2025-08-12 05:25:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66e80c52-a911-3324-8a89-5f6f5caf497e | -10.34892 | -57.60355 | 2025-08-12 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91f30843-e9a4-3a31-ad9b-465e1a40f87e | -10.3559 | -50.82896 | 2025-08-12 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd6dcbad-f6c5-3c73-bc88-48afc9cd8e76 | -3.43287 | -49.03761 | 2025-08-12 05:25:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README33.md)
