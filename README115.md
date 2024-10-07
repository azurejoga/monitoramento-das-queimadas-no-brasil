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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8098172b-b24e-37c7-83a4-0f1e643256fb | -17.09879 | -56.69064 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b9c160ab-082c-3963-a535-7f5ef0640aa5 | -17.05424 | -56.0521 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 676d6e05-97fc-39c9-a32d-7cca60f6ea89 | -17.05374 | -56.05581 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7a16f211-30e0-369c-9450-08b15e931fa2 | -17.04967 | -56.05522 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| f7cd0b7c-9133-3b75-b65d-c00bf381c4e4 | -17.03314 | -56.67872 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| c1bf374e-d2e4-33e2-8528-b02a547c9a4c | -17.03245 | -56.68383 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 488c369d-5473-3b3e-b075-4e439c073d63 | -17.02854 | -56.68327 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.6 |
| 89ad81d4-c2d1-3e67-af6e-b71e7c5ddcda | -17.02531 | -56.67759 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 6a5c878d-8d55-358a-813d-c6b2291911c8 | -17.0214 | -56.67702 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 3177861d-9f6e-3e0d-a729-e2d52081a3d1 | -17.00439 | -56.68496 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9e9fde6f-9023-3c41-a214-24eeccac4668 | -16.9646 | -56.13678 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 850be3d5-7a09-3df2-9958-8d93c894aafc | -16.94182 | -56.6169 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| 81d056ab-8d38-35e4-b611-c9c7c673e8c3 | -16.9379 | -56.61633 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.3 |
| d05cab39-ce64-3e06-904f-e3a4d4ddd95c | -16.92136 | -55.87043 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 499ab88d-22d4-3e7f-b752-6f256d039b5d | -16.91774 | -55.86607 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 44810ef4-a3da-3b13-9452-73d0d4b9bdd5 | -16.89212 | -55.87014 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7f5e00c1-7557-3cef-8447-7a90346bcdeb | -16.85922 | -55.81242 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ffc9ae11-0a4a-3d45-8498-092126e721f1 | -16.70463 | -55.92102 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a28df5c3-7c11-3436-9a95-de102b3b5e15 | -16.69568 | -55.9576 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 27e10554-b4bc-3c0c-ae90-dbfc818ac6a7 | -16.68802 | -55.95272 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 036cdefe-6368-3ded-8099-96ddf7eaa0b8 | -16.67631 | -55.88269 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0ec37cf6-4ac0-3b06-95f8-2526e1e0e4f6 | -16.66716 | -55.88902 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 70f83f4a-4f5c-364b-b4ea-daad37f7280c | -16.66668 | -55.89276 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a742b920-25b0-33a2-bbcc-6dec5fbd6dfd | -16.65405 | -55.8994 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2d4542a1-59b6-3386-a8d6-c0943e56bdb7 | -16.64588 | -55.89824 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 3b4cb836-c7a2-3c5b-87b3-9eb1291ca112 | -16.63671 | -55.90452 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ba58d417-f3a0-349c-adfc-a96f44668aa9 | -16.63164 | -55.91138 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7ae0b550-1245-3526-836e-3f4127530439 | -16.62496 | -55.89903 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 171ac00e-ed03-338d-a39e-3133730745cc | -16.62397 | -55.90649 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2d99e942-f796-3564-80d9-64d008622269 | -16.62038 | -55.90218 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 58ad3ff4-5219-3fa0-8c4e-8367f0a9866b | -16.6163 | -55.90159 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a727e79c-671d-3ac2-9d93-2295995de9eb | -16.61433 | -55.91649 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a1b71d72-d76c-3e0e-8347-bfb1d02d28e5 | -17.02463 | -56.6827 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| ed55a522-c2a9-320b-b3f0-ee9a608bdbe2 | -17.01748 | -56.67646 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 8c31d2a0-b07c-3966-a2ad-9fb7291cd282 | -17.0168 | -56.68156 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 52057df5-457e-3613-8705-fe72e7cdfc55 | -17.01153 | -56.6912 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 94fbf46a-f7a5-300d-bfc4-ac381ac6855f | -17.0083 | -56.68553 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5b87693e-5541-3578-901b-135c915b5dd7 | -17.00762 | -56.69064 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| a21b8b4c-5e25-312c-9b8a-967f0bd9f1ef | -17.00372 | -56.69006 | 2024-10-07 05:18:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 06c0dacd-bd3b-3897-9838-191fbd5d04f8 | -16.97531 | -56.60604 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 28dc155d-82b3-34b9-80fd-1f928bc540ac | -16.97461 | -56.61118 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 62d0f7a3-e516-3f36-b0bc-3d7331fc9738 | -16.97138 | -56.60548 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d3db4ffe-7709-3341-89c5-970101a77b62 | -16.97068 | -56.61061 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3de7c1a0-b338-3856-8b49-b2a2d413ede5 | -16.96998 | -56.61576 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 346dbf0f-e541-349a-bf72-ceff7de664a1 | -16.96865 | -56.13735 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4b73f030-0e76-386c-9113-26fd00d9502a | -16.96817 | -56.141 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9b3379a5-7c4d-39ba-a988-3b7097294004 | -16.96413 | -56.14042 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 255e4db2-a676-3c2a-9207-6d9e0a408b1c | -16.93653 | -56.62659 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7252ed27-32e1-3544-979d-641fcb8e2b55 | -16.92678 | -55.82874 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c4730cc4-dad2-3478-b139-4fa2494d6204 | -16.89164 | -55.87392 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d46f10dc-d1b5-3c77-a7f6-7fc8c252ea2c | -16.85973 | -55.80862 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 388261c2-27a1-3f14-9b3b-e3fe88713223 | -16.70121 | -55.94704 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4215c3bd-3753-3fcb-a3e0-90e2c7fbf915 | -16.70072 | -55.95076 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a4febde2-4559-37b9-b986-a97f6e27bf80 | -16.70054 | -55.92043 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9a9050fd-c896-33bf-80b8-be73dd1a6ed2 | -16.69616 | -55.95389 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 74ebb366-632e-3218-9bef-ba50353f15da | -16.69257 | -55.9496 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 43ab47b7-1954-30b0-b921-0e28fd50a163 | -16.69161 | -55.95701 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9e8011e1-ba03-3cb4-a76b-68b97494caff | -16.68753 | -55.95642 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5c1b9f3e-ab88-397c-8812-a1f83590a82b | -16.67221 | -55.88211 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 772bf2db-dd2a-38d3-a7ee-176c05f2bb58 | -16.67173 | -55.88586 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a23caadf-0574-3be9-b206-2da06116607c | -16.67125 | -55.8896 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 31231549-69cd-3547-9ea1-ae755d57698b | -16.67077 | -55.89334 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fd605365-8731-3ad0-a4da-71084bfc0b9f | -16.66861 | -55.87778 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 177801cd-5b3b-3d9b-8b7d-37fbf7b85fd3 | -16.66812 | -55.88153 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ae60173-fb93-3b84-b564-ced99a302912 | -16.66764 | -55.88527 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9294b089-d661-3691-acfe-cefa5b17771b | -16.65354 | -55.90313 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a5784ebc-7023-3e81-9e9f-6b75fd2f2b8d | -16.65346 | -55.8985 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| cbbe5ae6-990e-3d5f-a088-de5019e9ce47 | -16.65299 | -55.90224 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| bcd78093-6676-34b3-b446-e7ab5b733dc7 | -16.64996 | -55.89882 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| d0bc0e62-2be3-3a86-92ce-7eb255541b11 | -16.64946 | -55.90255 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 268962c4-e3e7-34e4-b563-0dab5e88546a | -16.64538 | -55.90196 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| e929d349-428a-3fa2-88b2-dddf2cf7c368 | -16.64179 | -55.89766 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4f9cab95-379d-3ce9-aa05-e7bb79f39256 | -16.64129 | -55.90137 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ab9b6737-22b3-3f58-a3cf-8e831051eef7 | -16.64079 | -55.9051 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cc70fcfd-0e82-3a2a-8f22-0eac9df85b85 | -16.63213 | -55.90766 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 67533442-8dd1-357b-b3a2-c30cea65e138 | -16.62855 | -55.90335 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a9e406b5-c532-32b5-9cea-c4eb4d30826b | -16.62805 | -55.90707 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b232fabe-c766-3697-9339-34371453c012 | -16.62756 | -55.9108 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7a77f08c-ea9d-3064-8561-fcfb4f07c5bf | -16.62447 | -55.90277 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cdaa7911-d840-3d1a-aa2d-4244f8b75912 | -16.62248 | -55.91767 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 73dffa24-a689-36ab-ad5b-ce112b15caf9 | -16.61581 | -55.90532 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d2fe71de-93b5-33e0-94d5-77de02bea40f | -16.61532 | -55.90905 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d46973a9-92d8-31ee-98fb-0c5ac1932681 | -16.61482 | -55.91277 | 2024-10-07 05:18:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b69d70cd-688c-3e28-b242-32311d99cf3e | -16.42447 | -57.34026 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| f58ad4e9-1513-31aa-af08-ad5e17cfb4b7 | -16.40513 | -57.34212 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3822329a-a376-3870-8d74-3e721aff0d62 | -16.40075 | -57.34616 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d9782c8c-b863-343d-85a5-3c2ce0297ff9 | -16.14173 | -57.4166 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec1cad61-1ed5-36ce-ae70-c278e7f71246 | -16.56029 | -57.4733 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 96fa2259-192e-3cdc-b4a2-9c7e8988f19b | -16.53478 | -57.74045 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d29edf0c-fc62-3baf-9510-217b615dcfb8 | -16.53233 | -57.73111 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 75e3e479-4c7d-3a40-9fb3-abc3f311da58 | -16.52867 | -57.73052 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 20b11c3d-b43a-362f-afa4-c47697c3bc87 | -16.52806 | -57.7349 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3cfb080b-9141-3abf-a015-8180b6ff8a82 | -16.52562 | -57.72553 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 641a346e-fea4-38a3-992c-524c4161710e | -16.52501 | -57.72991 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 34af1756-9d60-3d95-811c-6cb17c5a7c22 | -16.5244 | -57.73431 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f77cb1ad-b94f-3932-b17f-089c53012ff3 | -16.52379 | -57.7387 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| c5eb898f-67bd-3b1f-a576-47767a6a8cbd | -16.52319 | -57.74309 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 24db1f23-88e0-3751-8586-3ea0e2a92db0 | -16.52195 | -57.72493 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f18b9307-b467-3e3d-8406-2cd3e091d23f | -16.52135 | -57.72932 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3621f35f-8aac-3f65-aa57-a09228f7b360 | -16.52074 | -57.73372 | 2024-10-07 05:18:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |


[Clique aqui para ver as próximas entradas](README116.md)
