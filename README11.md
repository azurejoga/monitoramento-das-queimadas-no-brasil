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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3293fbd2-dbf5-3dd8-8af4-e464b314fe36 | 1.08431 | -59.25229 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| beb72d4f-d52b-333c-8986-be2f499b2638 | 0.85967 | -60.40855 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff6319f-fc17-3d8d-9e80-a07da0fd23ef | 4.42238 | -60.75929 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5127c52e-26b4-35e5-a4dd-d778fb8d5c75 | 1.87854 | -60.91563 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96ac1ac9-c0c4-37ff-b481-840ea3c5c771 | 3.4649 | -60.82014 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e63e8306-5fab-3011-a3dd-01062678bf9f | 2.3015 | -60.59035 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628eb00d-1f1d-34fc-a236-9a95539d660c | 1.49528 | -59.92688 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bb264ba-e36c-3c65-ba41-5e1802ae45bd | 2.90763 | -60.44556 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee194503-05e7-319f-b265-0a51e2db6575 | 2.18755 | -61.91541 | 2026-03-01 05:59:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33fe2d6e-3801-3ec4-9360-1128a28e21e8 | 2.90998 | -60.43269 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5407142c-4433-35d2-b531-7749f1bd579c | 4.15097 | -60.70785 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0544d4dc-4b01-30e1-8537-cb8fc4cbdd57 | 2.52569 | -60.80896 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 341212f9-460b-3a07-92f7-1dfe0c3a5991 | 3.31717 | -59.89503 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d417f660-f8a9-3005-b4f7-df87772a5075 | 1.02376 | -60.54112 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fa85aad-b837-3c77-9987-982ebf72220c | 2.30086 | -60.58633 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40c61455-bc22-3fa6-9c4e-c75c829d7e1c | 4.34156 | -60.58599 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd0e430c-13ed-36ae-a1c8-c4ff1a6697a1 | 1.5022 | -59.91165 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 06e24c06-4962-3ab2-8dd5-2bceaf0c84f4 | 1.49304 | -59.91294 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 8cb63e83-92c7-3842-9fab-72a56dc6432d | 1.86866 | -60.40573 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 337e5c2e-9f47-3cbf-ba37-6e9d71a4c745 | 4.3424 | -60.58681 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bef4e57-033d-3594-b74b-3d6b6344c511 | 1.36367 | -60.30523 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cca5631e-0b1b-37e8-b231-5550b1b33e02 | 3.45474 | -60.81028 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 049955fb-8f2d-3d96-a967-d8e524b255d8 | 1.48921 | -59.91826 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 27.1 |
| e0151d66-a222-3cae-8c8f-5128e11e871a | 3.45412 | -60.80654 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3dae3bc7-ad57-38d1-8029-84f24f72d338 | 3.15832 | -59.91916 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2509f389-41b6-35d1-8798-059651fdbecb | 3.4535 | -60.80278 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 441fba27-23e2-3d6f-a050-4fd286c36b86 | 1.40682 | -60.74419 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21136edf-cd14-3e1e-9e6e-032a4708b8ba | 2.3235 | -60.38615 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3173e1d-7137-3a9f-b75f-b96e4f10e946 | 1.51115 | -59.93833 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a33c91a-72c4-3791-9fb7-3361b74b2fe7 | 3.16058 | -59.92111 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae7c3792-2c84-314b-91b4-bbd86209aa6b | 1.47321 | -59.93509 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424bb411-99e8-3bdb-ac4f-e3a785a89497 | 2.31918 | -60.38713 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 635456bc-2a12-3d9f-882d-991a491742ab | 0.57171 | -59.91079 | 2026-03-01 05:59:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05f68fa6-bd0c-315b-91e8-e8a026b24136 | 1.50971 | -59.9293 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0241ac8f-707a-3398-a7a4-dbb10207ecac | 1.51043 | -59.93381 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d9fe2878-e2d4-399d-a74b-bbaf41f4608f | 3.44996 | -60.80724 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c52fe95a-3490-37bd-828b-59b53c9dae55 | 1.07865 | -59.24779 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1313fbaf-6a5c-3c64-ace6-a5159be4fd9a | 1.48162 | -59.92923 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a5b35e5-1d9e-3bf4-819e-add959b26c39 | 1.07467 | -59.25378 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c27dc1d8-6e5f-3626-a0d7-b1b8dfef983b | 1.48767 | -59.93773 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97ae6a9b-c1de-346c-bcb4-4630d18fb16e | 3.16502 | -59.92038 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b464e9c3-bd56-38c1-b0e7-3444e45403a2 | 3.15988 | -59.91675 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4dee5f82-906d-3b56-b216-9c1a1499ced6 | 1.02307 | -60.53685 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c5e24a-5c64-3f90-8b80-521daf76df59 | 3.45288 | -60.79902 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1026fd1b-61fc-3530-82f1-882f1c97bb80 | 1.50589 | -59.93464 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea875e24-3e73-3121-929b-27843de1ef45 | 3.45163 | -60.79144 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43cf48e9-3b96-3d45-8f80-e4a37184b587 | 0.64954 | -60.37188 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1c6588b-cb1f-36be-8aa4-549800a97664 | 0.85453 | -60.40494 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8bdd6d6-b50e-3cfc-8ec8-08ed2dbc2270 | 1.50061 | -59.93089 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 700fdfa6-fb3e-30fd-9350-f16c5a8c9fc5 | 3.48495 | -60.78588 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ca37943-aea6-3a8e-bcb0-d735c39b8267 | 0.85899 | -60.40418 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40fdcbe9-4238-364d-be95-42b4ece14f05 | 3.15758 | -59.91479 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae65137f-7d25-3438-84ac-20926660002f | 0.64861 | -60.37536 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb8f2355-1609-36a4-9856-4554062afab0 | 1.47245 | -59.93044 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fac6072c-6e53-3e8e-b01b-e1636f33841b | 3.44872 | -60.79971 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b449835-5d89-30f1-aa7f-1dc0f5672170 | 0.85711 | -60.40667 | 2026-03-01 05:59:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d37b02d-f7f3-3ebf-8cd8-8168cb20fe55 | 1.91826 | -60.57326 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdf51487-f1ec-3457-9531-de1b07802bb7 | 1.08347 | -59.24703 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0adb432b-7345-389f-8a0a-f696771953f9 | 3.16362 | -59.91164 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ee06dc2-b2dc-3241-a0c8-1f8effa9ff54 | 1.86358 | -60.40223 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0fc3c54-8f11-30b8-9e40-70404aa400ba | 1.48236 | -59.93382 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36abd417-bf60-3d6d-b7e7-529a1950abb8 | 1.50293 | -59.9162 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| ada5612e-f0c8-3b6c-b2b1-05fd5955a929 | 2.52147 | -60.80965 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a0aa688-203f-344e-8127-0b38b4913b4d | 1.36813 | -60.30452 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41ea3f8d-7c2f-394d-9b61-7d691bc32f9e | 1.05938 | -59.25087 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 798b7b66-bd09-3122-a5ca-c42810c52887 | 0.5519 | -59.86164 | 2026-03-01 05:59:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02df34cf-c0aa-3f96-8078-fb8c6993c21a | 1.49835 | -59.91684 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| c2aa4a98-6f29-330b-89b9-718e0f7bf90b | 3.15544 | -59.91748 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d70ce0b-8455-340d-8e79-87641d98fe27 | 1.93414 | -60.80683 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20768b86-7033-30f6-ab31-d74c5829014c | 1.08829 | -59.24626 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a09f2430-99a4-3c55-bc36-a0f89946d8ee | 3.95649 | -60.607 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eddfda6e-b764-332a-b6c7-4a904d8da562 | 1.49603 | -59.93155 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36729b71-955f-3bf1-9388-9fa277fabf43 | 2.91165 | -60.42987 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6d88731-9542-39d9-9841-a1e0e2844678 | 1.51354 | -59.924 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 35ffe7e9-e04d-3006-b3af-b9b91049a76c | 1.08913 | -59.25156 | 2026-03-01 05:59:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01d0e5a0-fe12-3bf2-88ae-83f09c5ff9d7 | 4.4401 | -60.73869 | 2026-03-01 05:59:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82059ffe-3c6b-3c23-b356-70b4c250ea78 | 3.48789 | -60.77764 | 2026-03-01 05:59:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bea675c-f321-3a31-94e0-03aeb748e6c7 | 3.15387 | -59.91988 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 447061eb-7a19-32a2-953c-d4d5d60d1a1e | 1.48617 | -59.92846 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d72c31d4-75bf-3b21-80ba-d3e63351976a | 2.62236 | -60.61321 | 2026-03-01 05:59:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2778b4a6-ab0d-39e9-ae02-db36971fb50a | 3.1672 | -59.9177 | 2026-03-01 05:59:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bf7f15d-f9e9-3ba8-b99f-b654cad29e77 | 1.50898 | -59.92473 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.1 |
| c724674a-b466-322b-9063-d5470684bdd0 | 1.17891 | -60.36374 | 2026-03-01 05:59:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5fbe823-23cb-37e4-a3b6-306c18326b9c | 1.5047 | -59.9116 | 2026-03-01 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 115.7 |
| ab69ae71-b512-3411-9202-ff3b6c310868 | 1.4864 | -59.9308 | 2026-03-01 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 56f6d15a-3a0a-3896-ac3c-8950acc77020 | 1.5046 | -59.9306 | 2026-03-01 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 50fc7e5b-cda9-323e-b396-1d7f0958c7f9 | 1.4864 | -59.9117 | 2026-03-01 06:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 127.9 |
| d924e189-f3fe-3e46-84b3-ffa28025bcf5 | 0.10095 | -60.63546 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b557cd2-43ad-3076-8191-db1d42608cac | 0.09206 | -60.63683 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b37eff5a-397d-3042-a097-c23a1913afaa | 0.09581 | -60.6318 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6cc7d565-f56d-351b-90a8-db9900685ee0 | 0.08011 | -60.64761 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc97ed8c-20d2-3397-a796-fc1abefcacf9 | 0.07636 | -60.65261 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1686ef2b-77af-3db0-b831-029cc431d889 | 0.0965 | -60.63615 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5af0faf2-ba60-37cf-a8c2-845d02938a6e | 0.10026 | -60.63113 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 00093999-a2ad-34fc-b297-fdff467cfedd | 0.07566 | -60.6483 | 2026-03-01 06:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a757b78-4242-3024-8f46-6bd98f5bfc5d | 1.4864 | -59.9117 | 2026-03-01 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 111.2 |
| f5e98bd5-c59f-3abe-a7e7-f7e4311067b0 | 1.5046 | -59.9306 | 2026-03-01 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 118.3 |
| c27023a1-8fdb-34b0-9b64-d3ebf29e3717 | 1.4864 | -59.9308 | 2026-03-01 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 116.6 |
| d2f7a48e-f13e-39ee-94fc-5c9a58307edb | 1.5047 | -59.9116 | 2026-03-01 06:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.2 |
| e0c692f1-db4a-39fa-a912-0d1ad2fe7ad9 | 4.42659 | -60.74285 | 2026-03-01 06:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
