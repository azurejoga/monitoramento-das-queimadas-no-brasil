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
| 61be0ceb-1d03-3be2-9337-e2364de26256 | -16.98523 | -57.48366 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 1df3813b-019c-3a72-89bf-b2ae722b3388 | -16.98521 | -57.44361 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 793fa888-f129-3c64-8294-4bea1624d515 | -16.98422 | -57.44397 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 297e6c27-439d-3761-9084-bd3a4a955834 | -16.97227 | -57.445 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d646c1b4-77ea-3a4e-a8d9-b3f8086c73b1 | -16.90725 | -57.80074 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 049873e7-6767-3986-ae34-6080da4f411d | -16.90652 | -57.80475 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 84b7070a-9cc8-393e-81ae-c15b9ca35445 | -16.90307 | -57.7999 | 2024-10-13 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 78885ebd-a741-3523-bd03-6d9149cc6886 | -11.89844 | -57.46798 | 2024-10-13 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 526d0a43-2486-39a2-9e85-ac0168507753 | -11.89397 | -57.46719 | 2024-10-13 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a3298cc-9086-30f0-a358-2e71852ce39f | -11.89313 | -57.47176 | 2024-10-13 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ca3c657-434e-3de3-a7bb-c25519a30898 | -11.38474 | -58.32541 | 2024-10-13 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73bcd00b-ecb5-38a4-a890-393e0843b662 | -11.38421 | -58.32866 | 2024-10-13 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f5250b4-75f1-3a8f-b6a4-915f5a7f74c5 | -10.91908 | -58.0643 | 2024-10-13 04:42:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5537b9c3-27d7-39b2-9b66-fddabb96cc90 | -15.95806 | -59.12583 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cef583d-9c9f-3846-b716-f1a5a8f893ed | -15.9543 | -59.12038 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e10f583b-3fa7-3bbe-a598-c0a2f2de6622 | -15.9535 | -59.09962 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92bff7e4-e2f4-3bd3-9426-5ee3fb2a1cfe | -15.95341 | -59.12501 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2103dc36-a728-3042-9ddf-d13d3ff75143 | -15.94985 | -59.09364 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c725c7a2-4196-3a12-b532-eee5d1f86959 | -15.94966 | -59.1195 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c22e10-6836-3fea-80e0-de5d51b67fe8 | -15.94875 | -59.12417 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0025bfc6-27bb-3e0a-869f-50ccd4010c6e | -15.94525 | -59.09262 | 2024-10-13 04:42:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95021430-56e5-3fe7-b7fa-19fc114131fc | -15.69401 | -59.33904 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0a24ac0-2012-3f56-af88-700d26e15f73 | -15.6931 | -59.34374 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c442b802-3162-3851-bdb0-b087733d2944 | -15.68837 | -59.34279 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d823419-342e-31cc-9d65-245b2fadf10b | -15.68748 | -59.34737 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc76f008-3122-3923-8267-a00678d6eefb | -15.68464 | -59.33675 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2c70194-6f65-3f8f-b9f5-755cdf24610c | -15.68375 | -59.34135 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4c2336e-154d-335c-80ff-ecdd60b0d7d0 | -15.6753 | -59.33433 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d142e1c1-33b2-3dd3-a7c2-b57b111c37f7 | -15.63088 | -59.3851 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9024ac6a-d07b-3f9c-b203-5b45752e65c8 | -15.63084 | -59.3821 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 084d5070-d923-3e34-b632-225d0dabb462 | -15.62989 | -59.38705 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23636674-7120-33d2-bf28-ccf4e9737b6d | -15.62885 | -59.39252 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59a60178-9e62-3cf2-9dbe-8fe29fad8a53 | -15.62394 | -59.39526 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd6a4a11-a868-3f76-807c-62c0e25d5bd8 | -15.62302 | -59.39726 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4e0ad91e-6a11-306b-9e26-302e7eb7b9e4 | -15.62206 | -59.40229 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42ddee53-d5f8-3d7e-a95d-946bb47df649 | -15.62194 | -59.40532 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db105236-ea25-3b9e-9607-79ff2ecd5f12 | -15.62112 | -59.40724 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b0dbd8-ae7a-36ea-a0a9-d5421a27f09e | -15.61733 | -59.40125 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbdb5b53-d21f-3f07-9615-2c3ac836a1e4 | -15.61722 | -59.40424 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03233f11-59fd-31e0-9929-815b5ff49898 | -15.61642 | -59.40603 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8e8195f-bc41-3f62-8d35-947a853558f2 | -15.61352 | -59.39538 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc0fd153-dc1b-32b5-b3c0-f7c671d57542 | -15.60871 | -59.39477 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e301efc-9a7d-37fb-94f8-d6c110cc56a4 | -15.60389 | -59.39417 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 572a91a3-144b-397e-9d8b-751e57b87040 | -15.60289 | -59.39938 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93ca1f52-339f-3191-99d3-ee77c228ae38 | -15.5991 | -59.39347 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8d4f95d-cd30-3fdb-afad-29ba3798620c | -15.59712 | -59.40373 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed866e89-3ba7-37e5-9637-50a3376c2d68 | -12.1572 | -59.88425 | 2024-10-13 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d168fd6-8007-391f-8a9d-465a6e2e7d99 | -12.14697 | -59.88008 | 2024-10-13 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e9d5c53-3f6e-3407-a944-08c8df1425a6 | -12.14172 | -59.87918 | 2024-10-13 04:42:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f05539ed-2bed-36f4-952b-9dbee7e0854c | -12.97036 | -60.05733 | 2024-10-13 04:42:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3cfb34c-cb7e-34fe-ad2a-d2d75c54da12 | -12.96516 | -60.05628 | 2024-10-13 04:42:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab891f49-e167-3dc7-9ddf-164029705cd2 | -12.96456 | -60.05942 | 2024-10-13 04:42:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c32b4b6a-985a-3aaa-a5fb-dd1a8229f2e9 | -12.81828 | -60.16992 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f28e92fe-ac81-379b-9eb1-0cfd46dc04fb | -12.33786 | -59.87534 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 349ae748-8979-323c-8743-c10d0322b6ac | -12.33725 | -59.87853 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a42a31ac-d75c-31a0-a4c8-8ffffdf20744 | -12.33663 | -59.88176 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9425b1f8-2146-38bc-bc11-6e8eacf01c43 | -12.31658 | -59.81797 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e6da455-fd7b-3bb3-b723-76bfe05bb009 | -13.74021 | -60.11804 | 2024-10-13 04:42:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20132e8d-2047-39ea-a894-1987531a282a | -15.64785 | -59.97429 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f3aa490-471e-3b5a-b61b-e740f1d99fcd | -15.64669 | -59.98009 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cb08953-8c94-3701-a1a5-77db24de99e9 | -15.64408 | -59.9675 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f402388b-f7f9-3861-bb61-eb679f69f2a8 | -15.64292 | -59.97329 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b91b085-a5ed-3d26-b5aa-cf1a51688b2c | -15.64213 | -59.97137 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b32a12e0-18ed-326b-8b27-1825a4764fef | -15.64176 | -59.9791 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fcbd54c8-bc08-3ae8-8bbf-67a989971f3c | -15.64102 | -59.97717 | 2024-10-13 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1cd8fa3-b9af-3d0f-93a6-bd694d810f3f | -11.28186 | -60.47298 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 684be839-8935-3145-94b5-fc92a75ab5ef | -11.28059 | -60.4496 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bab6f7e6-3762-3973-ad16-c0d2e0d7cc4d | -11.27989 | -60.45327 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1998304b-000b-3e53-9974-65e0c5fb155b | -11.27627 | -60.47233 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4df8b49f-0447-3c3c-a5ae-bdc5736e8d86 | -11.2749 | -60.4495 | 2024-10-13 04:42:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 85aaa86d-b19d-3a3b-9ee9-be215b97e9e8 | -12.93428 | -62.53148 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec23b9fa-9e0e-33e6-928e-8b960b4baa8d | -12.92821 | -62.5302 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9866aef9-938b-358b-a3d7-36612594b485 | -12.7704 | -62.28031 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a693cd3-a048-3aac-a518-0af774e05411 | -12.77001 | -62.2729 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 388504ed-a02f-3fb7-bbfe-01be88d14e52 | -12.76909 | -62.27752 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5f0729f-3be2-351f-b8a3-5416ca08dcf1 | -12.76816 | -62.28212 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6e9cc2b-6f90-34db-8206-8e6b947c5d5f | -12.76535 | -62.27448 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70877191-00ec-3cee-9403-4d7df7911f34 | -12.76494 | -62.26704 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdbe2d7-0a43-30c9-9e40-2e715428f802 | -12.7644 | -62.27906 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dddb9fe-ca06-3e5e-8cc8-1131d15fdfe2 | -12.76345 | -62.28365 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc47158b-6560-3403-bac7-a8301c39d41e | -12.76309 | -62.27627 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a79558e6-b3ad-3aab-b99d-10d9963d9dbb | -12.76217 | -62.28085 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d1f2c46-e6b9-388b-9c85-a8b1b0af3e6d | -12.76125 | -62.28541 | 2024-10-13 04:42:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ec5c271-0c9a-3b82-a5b6-535d5ca2fc97 | -12.48093 | -63.00819 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6458debc-16ca-3a39-b1f5-e6c8ae7a5b40 | -12.47985 | -63.01347 | 2024-10-13 04:42:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2a6331cb-5f92-3409-bb67-3dd29c71df6f | -12.39732 | -63.7366 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 661f6c63-bd68-3cfa-826f-73220a0c72a0 | -12.39611 | -63.74236 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c17a3e1-9662-35f2-96e5-6fbe69eba619 | -12.39474 | -63.72545 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8d2de7a-ca5e-3e2e-a916-d00856f00b2c | -12.39354 | -63.73133 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6c3ed79-5a48-3d3c-a1be-2cba105111ac | -12.39235 | -63.73715 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 65797747-af15-3699-a232-b25a909e924e | -12.39199 | -63.7293 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae1ebf8e-d637-378f-8510-ef8c07a90cec | -12.39076 | -63.73513 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b2af2e5c-6858-3f26-aa11-ba463a1b3504 | -12.38955 | -63.74089 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a1a0b510-9036-3307-90bd-162a558621a8 | -12.38699 | -63.72978 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d3a386d-3bd6-3b2f-a502-e4aa7d6cb26e | -12.38579 | -63.73565 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 011ef419-d97c-3cfb-be05-c0430d79d69f | -12.38544 | -63.72778 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d7344611-0cbe-3826-8f3d-1124efde3dc7 | -12.38461 | -63.74144 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 80c8c754-908c-3fb8-a4df-478923264633 | -12.3842 | -63.73363 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab2421d6-540f-3fa6-a245-e5cb2f8236e1 | -12.38297 | -63.73947 | 2024-10-13 04:42:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 178df872-1e68-36c8-a91e-6e1bdf0e61cd | -13.20852 | -49.82138 | 2024-10-13 04:42:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README69.md)
