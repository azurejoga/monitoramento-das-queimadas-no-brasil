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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3971693-3d82-3539-a9ea-2c404bdf248f | -11.69191 | -65.21802 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24921907-c187-3fa9-899e-c1d72604d789 | -11.68899 | -65.21305 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56298f88-aeeb-3569-8096-2e787da328d4 | -11.6883 | -65.23978 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5e05da4-a447-3daa-b97e-34accd992155 | -11.50996 | -65.1169 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1698d12e-26c5-3735-806b-53cfc62c170d | -11.50196 | -65.11995 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5980676f-c294-373b-8f24-2915b6592911 | -11.49832 | -65.11934 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba426433-86d4-322f-b035-58578d06eb0f | -11.49468 | -65.11871 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de624f5-95a7-3ec7-8006-557eabe4f55f | -11.49115 | -65.11515 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e5050d8-2f00-3426-b478-280682389369 | -11.49105 | -65.11808 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b488482-5ae1-36dd-a8fc-fb5b7a51c2bf | -11.48894 | -65.10591 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba7f5e9b-0094-3a5e-a3b5-7de27d6769c8 | -11.48889 | -65.10886 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48bc80b9-5ccd-32a0-b05c-a7d2ce353ce5 | -11.48679 | -65.11884 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db71f634-4489-3223-b771-f194478b140b | -11.48602 | -65.10098 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb2853a7-4dd9-3e68-a481-63eebd8ab0ad | -11.48599 | -65.10394 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 203fbf09-3e79-38e4-a739-6b2033cc5d05 | -11.48525 | -65.10824 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ace5641-c701-3793-9bdd-6ab718aea5b4 | -11.48452 | -65.11253 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 617810bc-ff2d-3945-9aa9-6ac9ad22a4b6 | -11.48387 | -65.1139 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 203c99ca-107b-3dc0-bafc-2c45be2a1a50 | -11.48377 | -65.11684 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bddaa11-860a-3b40-acf9-be24423d5d7f | -11.66088 | -64.8278 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a4ac322-a69a-3c3e-957b-9e5e73de303d | -11.66017 | -64.83196 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5ee2945-c3d0-3ae3-80c7-644556265603 | -11.65659 | -64.83135 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7d7116c-b6cb-38e0-8aaa-1451f41dbdaa | -11.65443 | -64.8224 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a475956e-6820-3be2-88e2-2d2b6052b5cf | -11.65302 | -64.83074 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f033d94-b278-387f-90e2-9531a92db82e | -11.65015 | -64.82597 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0f2143-eb02-3e2a-8adc-896efb42912f | -11.5165 | -65.12246 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a6090ed-f1e4-3226-a135-662d8d3dd94f | -11.5136 | -65.11753 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4480f1f6-e82e-3291-b62c-3dfcc630a302 | -11.51287 | -65.12183 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae6a785-9dcc-389a-b364-9908579d7f74 | -11.49179 | -65.11378 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c559993-94d7-39ae-a268-c68a17a5a512 | -11.48965 | -65.10161 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5d1ea953-7c14-37af-9ba0-774aa50f1aba | -11.48963 | -65.10456 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72ddf99b-46ec-3eb1-9006-8af70d54d4bf | -11.48822 | -65.11022 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05305c94-6b67-3d51-b4e6-ab9fdedbbe63 | -11.48815 | -65.11317 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7244605a-42d6-3638-8809-a7ee41adf57c | -11.48751 | -65.11452 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2d1466b-47f2-362f-85a5-60cdbde2a8ca | -11.48741 | -65.11746 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5043610c-308d-3b44-9485-e4d32b1f0553 | -11.4853 | -65.10528 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7678781-6165-304b-857c-f89f09a57931 | -11.48459 | -65.10958 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9ccf92d-4c80-3203-8661-4eb169b9339d | -9.1483 | -68.86987 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 762a70bd-1777-3c83-8c7c-d0d0499bddbf | -9.14009 | -69.14017 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a5e6330-7c0e-3539-8cea-5d35cb17f459 | -9.02995 | -69.24625 | 2024-10-16 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e0d048-f791-3f44-8169-0306fe52cc63 | -8.97612 | -69.54192 | 2024-10-16 05:25:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70e51c76-5dbd-35a7-9eea-0e9d19592c5e | -8.61881 | -70.03277 | 2024-10-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42e64e20-95b9-3121-b56c-25057999d047 | -8.61823 | -70.03598 | 2024-10-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b05f3627-88b7-3bd7-9332-cb5dd4186a4e | -8.61358 | -70.03185 | 2024-10-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74898bdd-969e-3394-9d98-e28cce335e77 | -8.613 | -70.03504 | 2024-10-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b48a7de6-8b1a-30b1-8f5c-e5b585170b72 | -8.61242 | -70.03825 | 2024-10-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a15a86f-b638-3af9-8529-c75d49bf7527 | -8.61183 | -70.04147 | 2024-10-16 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a888e5dd-7947-365a-8992-4e7aabe8f3b1 | -9.80558 | -69.0845 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 261c4acc-21a7-308b-83ce-1dc805d79c57 | -9.8048 | -69.08622 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aca30015-a8ff-3d84-b613-4cbdcebfcd4e | -9.57597 | -68.98861 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 290ce8be-66d9-3eea-8821-de9d3eefffe6 | -10.88419 | -69.39502 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d5b7de5-ab52-32f8-91f0-566cb1123993 | -10.88123 | -69.41106 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 853705dd-728e-3d95-b44f-4eef771de5f3 | -10.87989 | -69.28443 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e3e068f-fb59-3dec-82a2-bcd396a5dc04 | -10.8794 | -69.73229 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f3e4abc-a3fb-3443-b6cc-5995b8423ca7 | -10.87839 | -69.72886 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc8c5cbf-3cf3-3495-8ffd-3adaa9aaeda6 | -10.86761 | -69.43083 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0b45b2c-6c55-3e94-b751-acb63f6df5e4 | -10.75313 | -69.4079 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5004051b-68fd-3439-aaff-4d8bf76cf33a | -10.7092 | -69.43713 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83fcf8d5-b6df-3633-97a6-2ffbfc987d99 | -10.57014 | -69.33018 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41c34b9-0fff-30ed-80ec-2bc7da12da0e | -10.51163 | -69.35622 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270a27a1-7088-3028-9dd7-88254367cecf | -10.51114 | -69.35256 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb550c65-bae2-3fcd-bbde-0ffb114bdc1c | -10.48096 | -69.25111 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ddca195-b3b7-3cef-8327-03209a7477eb | -10.46082 | -69.25272 | 2024-10-16 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ed54f4-c4e5-3ae8-b6e4-3b2295997b1b | -10.452 | -69.30054 | 2024-10-16 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b080950-100c-355c-aa0a-5ce4cf5a0ab0 | -10.38015 | -69.51171 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a02938d-4baa-3423-b0eb-d5f5dd662d3d | -10.23098 | -69.40269 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 083f95d5-19c2-3a76-a88b-8575a4ef4dad | -10.11588 | -69.17017 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 826253cc-7cf7-32f5-aad0-a294d17ee4e4 | -10.11586 | -69.16676 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a884259b-b829-3862-8cee-83ff4fcc0d4f | -10.11487 | -69.17209 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eae0ba4-9fdf-38a0-a216-3bf8f62d7184 | -10.11107 | -69.16935 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8d58c9a-3cb1-3637-bbe8-8bec949060c6 | -10.11006 | -69.17129 | 2024-10-16 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e173990-03f3-3030-9e5f-ff62237572a2 | -10.90812 | -69.634 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a9bedfe7-fe75-3593-986d-70605c4c6b35 | -10.90707 | -69.63952 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0d054884-6b08-3c74-8248-82d4955e8158 | -10.90537 | -69.63588 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 83cd7b9e-6133-3266-b53a-47a165149073 | -10.90437 | -69.64143 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b5e8eff0-c8d4-338e-bc75-7746b040fa16 | -10.9022 | -69.63855 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c78c25cd-885b-3653-9c37-a6f256af9de1 | -10.9005 | -69.6349 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc49c61c-afee-318d-b7bd-3231556c6623 | -10.89949 | -69.64046 | 2024-10-16 05:25:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ba07dc3a-eee4-3ae3-ab36-dc9d25e1d207 | -8.51971 | -70.85796 | 2024-10-16 05:25:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69acb32f-c672-3086-b3f2-4614f397075f | -7.75432 | -72.28539 | 2024-10-16 05:25:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efc27be8-fe0d-314f-89a5-fe27333ea4fd | -3.1283 | -54.2259 | 2024-10-16 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 74837d39-b35e-3dac-b8ff-46f7abf9eb06 | -3.1282 | -54.2459 | 2024-10-16 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 00874660-a798-3b08-9f09-10088fd54153 | -3.1099 | -54.2263 | 2024-10-16 05:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| bce5e277-f56f-38ae-b6bf-73fe0a1f300f | -3.1098 | -54.2464 | 2024-10-16 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6d5f5f00-a1d4-3ad1-a090-ddd5f8cf403b | -20.43192 | -50.13205 | 2024-10-16 05:27:00 | NOAA-21 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e6bbb842-0890-3960-9446-b3d51a883550 | -20.43145 | -50.13824 | 2024-10-16 05:27:00 | NOAA-21 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3366f1b1-fdbc-3f96-91f8-e5355b60550c | -20.43028 | -50.13452 | 2024-10-16 05:27:00 | NOAA-21 | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea2ef251-2486-368d-951f-d7342dfa62fc | -20.85541 | -49.87318 | 2024-10-16 05:27:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 37982177-e242-3d22-87bd-a4ad2f8ebb6c | -20.85489 | -49.87988 | 2024-10-16 05:27:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 7defcfde-ce1c-3cd5-ba3b-59f6d5f842e8 | -20.85489 | -49.87302 | 2024-10-16 05:27:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| f9b61901-11d2-374a-b0da-11ea8dbdaa46 | -20.85441 | -49.87971 | 2024-10-16 05:27:00 | NOAA-21 | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2751a04b-cc21-323e-90c7-fe274034d604 | -19.59523 | -56.99287 | 2024-10-16 05:27:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.8 |
| ea1cb1f7-6ab5-38a5-ad4e-cfebd968500c | -21.15139 | -53.63178 | 2024-10-16 05:27:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab656623-f46b-372e-93a4-7fc1acd52096 | -21.15031 | -53.63073 | 2024-10-16 05:27:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad123e40-75bd-36a4-881b-c165abcfabe1 | -21.14996 | -53.63459 | 2024-10-16 05:27:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a7f6f68-f58c-37ff-902f-49ce628b250b | -21.14582 | -53.631 | 2024-10-16 05:27:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e4e0907-39eb-38c2-b910-08ab89630eb6 | -20.58505 | -55.53197 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39e9e7bc-dbb4-3876-86ed-93776ef7351b | -21.89197 | -56.10979 | 2024-10-16 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60468a07-c569-3529-99cc-403e88d3b56c | -21.66832 | -56.02659 | 2024-10-16 05:27:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08aa6e6f-fce3-3651-9f17-0a31d45dae3e | -20.99718 | -55.23711 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f0b562e-24ac-310e-8c70-d1b7f0ec2a72 | -20.99685 | -55.24019 | 2024-10-16 05:27:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README65.md)
