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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b3ca3a6-d1a7-35dd-83e1-7d1ce7c95832 | -15.95716 | -59.12204 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c867f401-7a88-3e60-b8b5-647c2818d335 | -15.95657 | -59.12569 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3406127-343c-3a3b-8656-bb8f3eedc9c5 | -15.9556 | -59.11042 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b735288-a27f-37a0-a707-5c20a3a6add4 | -15.95439 | -59.11779 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 303ca488-e627-3281-8ce2-9cefdf0cb94d | -15.95405 | -59.09875 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 334ed5fb-3fae-3b13-8ba6-173fe3145241 | -15.95379 | -59.12147 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73feb7fc-89a5-3970-a335-0dea72882056 | -15.95319 | -59.12511 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 325f7fc7-89d1-3a2a-aeb5-c460b974ee30 | -15.95223 | -59.10984 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75c4d254-3882-3d58-9807-a36825772ca8 | -15.9519 | -59.09077 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35698891-d035-3323-9062-cdc220f52a0e | -15.95163 | -59.11353 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d33cd62a-d2c6-3d2c-b783-96bd80e4e563 | -15.95129 | -59.09447 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c86a1e24-59c6-32aa-8f10-3551e44173c2 | -15.95102 | -59.11721 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5067f47f-22d0-3ba0-80fc-d088365d2a31 | -15.95042 | -59.1209 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9811be6e-d710-3f59-97b2-a12579b06323 | -15.95008 | -59.10185 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73403b0d-4615-332e-9d7c-2c55abdf2524 | -15.94982 | -59.12453 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97f93e20-3620-36a9-ab03-2a6b25f9c33c | -15.94947 | -59.10555 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb7fd990-25ca-34e2-91b2-074202c3ba40 | -15.94853 | -59.09017 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 423b4bf1-01e6-32e5-8e76-3acd2f10197e | -15.94792 | -59.09388 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1824e9cd-da1e-31df-9a16-26a2541d23e1 | -15.94705 | -59.12031 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a925de7-06fa-3ee1-b737-822d56b34884 | -15.94671 | -59.10126 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87923ab1-99f5-3276-9145-5808cd70f091 | -15.94645 | -59.12396 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ce68df3-ecd0-3e59-89e6-839a2b0294b7 | -15.94517 | -59.08957 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b96a12a-82b5-367e-9b83-0507f0dc56ff | -15.94456 | -59.09328 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 205622fa-4c01-3d2c-b095-1ce321567dd8 | -15.94398 | -59.08985 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 549c18ec-b24a-3587-8a91-8ecfd0c34f32 | -15.94395 | -59.09698 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b48925e-692a-3183-be64-eca4fc99a654 | -15.94338 | -59.09356 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c78d0fc5-b256-377a-905d-2986ca4d3273 | -15.94335 | -59.10066 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6479544-8e8a-3927-a3e2-185d74a53297 | -15.94278 | -59.09726 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c39d72b3-f9d4-3e43-a99d-2fb6afa5b220 | -15.94218 | -59.10094 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b527945-30e1-3fcb-8468-61790341d9de | -15.94061 | -59.08925 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2bc7284-b2c1-30e1-81eb-4369a744c983 | -15.94001 | -59.09295 | 2024-10-13 05:06:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b230de3f-e031-3e22-8852-08e07359ed2c | -15.67012 | -59.33382 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4de61a4c-6a04-31df-9ae6-14f9f67a2070 | -15.62569 | -59.39166 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a1ac36b-54b4-3e7e-bc32-3d07752a7444 | -15.62507 | -59.39543 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba04b69-08bf-3766-b77f-a3b510a7c63c | -15.62323 | -59.40661 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 844a3422-542f-3cec-ac3b-936ca6774fb4 | -15.62167 | -59.39488 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8762891-543e-3ea0-bf85-5f575add007f | -15.62044 | -59.44478 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2435cf35-f818-382c-822d-f2216f462b57 | -15.62044 | -59.40231 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6508cf14-9472-3b48-b48c-80d75bf5ba68 | -15.61983 | -59.40602 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6792124b-0357-31fa-9212-ff2808e1d4be | -15.6198 | -59.44864 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36ff2bf6-8f80-399c-8371-6b7e818c7a20 | -15.61768 | -59.44026 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 346a5f51-0267-3e32-8295-31cec66f60ca | -15.61704 | -59.44412 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fac7e524-3cd7-37db-b4cc-b90eaacc9096 | -15.61704 | -59.40169 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0161c8b-2498-3301-b1eb-9704252de3f8 | -15.61644 | -59.40538 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a90de83-8101-330d-9ca7-ca7339014ce5 | -15.61428 | -59.43964 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09d12357-285e-3f61-8d5e-dc85779df025 | -15.61365 | -59.44346 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f36c3b6-3928-32bf-970b-388324584306 | -15.61304 | -59.40475 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 610c24d0-b568-31c5-9afa-cce381c23da6 | -15.61244 | -59.40842 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d371361f-e317-3dc4-b3f5-b4d79b19b087 | -15.61088 | -59.43903 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 801a6dcf-0ae8-37e6-bf7c-2f15971146f8 | -15.61025 | -59.44286 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 318a08ce-12c1-3f96-8997-f33eec5edb58 | -15.60341 | -59.39951 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68d3461-758f-3419-9bd6-2d2bf7e0c277 | -15.6 | -59.39896 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 163a1a3b-bc58-331b-b9c5-d1ccafff945a | -15.59939 | -59.40268 | 2024-10-13 05:06:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5355f1db-6959-34b8-9971-3ff4498f5628 | -13.13764 | -59.69156 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7b07bc9-8ec3-3bc8-aa29-ff7385c6312c | -13.13286 | -60.26192 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b14eeb8-bbfe-3edb-a9c2-377bf096d63d | -13.13068 | -60.25284 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49903fb8-0fcb-3638-8da2-63df573a36ab | -13.12927 | -60.26127 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c2184c-08c8-3831-9d8a-1621c86f4c7f | -13.12708 | -60.2522 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053b43b8-8c01-31c8-8595-eb3b66fd0796 | -12.9685 | -60.05826 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ba3ceee-21ad-3202-b7bf-9bdb931fd61f | -12.96711 | -60.0574 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da582e6f-0733-3f41-8ba5-609a742472ec | -12.96562 | -60.05353 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a14acd95-086f-3fef-88f8-bba19b83d274 | -12.96494 | -60.05762 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2835260-aa98-388b-85de-967f1a2d1cb6 | -12.96355 | -60.05677 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d403d792-9a89-3217-8125-1232f239ac56 | -12.96285 | -60.06084 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7a8f4dc-0343-3a51-ac19-1684e7d16693 | -12.96069 | -60.06106 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f35a7c0-619d-3287-a7af-ab9669ed830f | -12.81954 | -60.17074 | 2024-10-13 05:06:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b216927-2ea3-3106-99bb-822683289879 | -12.81595 | -60.17009 | 2024-10-13 05:06:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3effcc93-6b49-3a36-8651-b0a0d7ab5719 | -13.47603 | -59.91479 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ff59a4cf-2823-3978-b461-a1b44ccbed6f | -13.47251 | -59.91417 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b70d7248-a46a-3d28-bc43-a7f4adb471c7 | -13.7712 | -60.55692 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cc8e8f-d6d2-39ac-bb35-bd682c4228ad | -13.75377 | -60.5714 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 809437bb-410e-3e49-b723-427ca63bb198 | -13.74431 | -60.58294 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b142866f-198f-3533-830e-662548e57180 | -13.74356 | -60.58722 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bf92029-6031-3a9b-93e8-45cc6c601d51 | -13.73994 | -60.58656 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c217b31f-42f9-3b85-9397-fd8df85f74a5 | -13.73875 | -60.59238 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08ec9907-9c19-3e14-a2d0-513efb146f27 | -13.73803 | -60.59668 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c455a77d-84b3-31e0-8976-5e22581b4349 | -13.73077 | -60.59536 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| baebaa2e-c5ab-3706-be74-0634f9787f55 | -14.74613 | -60.03358 | 2024-10-13 05:06:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8ff568f-0e13-3cd3-9db2-d75805baf9dd | -14.74263 | -60.03296 | 2024-10-13 05:06:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e5b69a-c072-3bb1-beaa-eba0f3c9538d | -13.76685 | -60.56054 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5207db5-424f-32e6-bbed-bc122971c89b | -13.76611 | -60.5648 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a745a21-4d8d-360a-bc19-466626444de5 | -13.75525 | -60.56286 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fdc4438-4708-33e2-a6e2-1260ca9a89a4 | -13.75451 | -60.56713 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 62c52c42-be02-3078-8961-9fde9fd233ca | -13.74766 | -60.10241 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 155f3e57-bd22-3740-aedb-9fc1780bb8db | -13.74489 | -60.11874 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b34d431b-8db1-3849-bc87-a3f11867589a | -13.74453 | -60.58018 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09faa294-2417-3bee-b4f7-d3ece4817aa4 | -13.74381 | -60.58447 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 52de4e1e-f866-3357-ae3e-1fd0c514d9a8 | -13.74135 | -60.1181 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a5c3c7c-4b2d-3bfd-b23a-b7e6fde119a7 | -13.74068 | -60.58229 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f280745-fd86-3567-ae11-85bc52dada4c | -13.74065 | -60.12219 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d291de2e-6dda-3017-8b92-412b5df9430b | -13.74058 | -60.10113 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a64514e-d5d5-306f-a06a-08ff318f2a2e | -13.73995 | -60.12629 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e77358e-9c48-35a1-8da8-2e904dc73b40 | -13.73947 | -60.5881 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4567c1b-2de9-3df5-9334-a5d21bae6d80 | -13.7392 | -60.59085 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49784b3a-c556-3ea2-b966-6f1c66d7fca2 | -13.73845 | -60.59513 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 957605f1-c238-3347-b11f-dfcda8c788f2 | -13.7378 | -60.11745 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb82264-7b1f-329c-be27-8372f21e5a55 | -13.73512 | -60.59173 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aa84c9b9-288f-3428-b689-aa65e2d7208a | -13.7344 | -60.59602 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb01d7e9-00d2-3ad6-9b02-255f95c66382 | -13.73426 | -60.11682 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05c1c9e5-1bd7-31e9-9ef2-38d2993e5c1d | -13.73419 | -60.09575 | 2024-10-13 05:06:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README93.md)
