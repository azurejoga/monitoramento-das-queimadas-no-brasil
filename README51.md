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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f40ecdaf-445c-30b5-9348-e860dae93cf7 | -2.00456 | -52.10724 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecf1444a-25f7-3c08-b862-0329842a6675 | -2.00127 | -52.10387 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc3c291e-5223-3d0e-a1ad-2b233f9820ec | -2.00077 | -52.1071 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee30236a-1e8a-396f-b3c0-4b8446f825f2 | -1.99975 | -52.10319 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c93dd0ea-80bb-39f2-9e1a-9178af13bade | -1.99927 | -52.10643 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3822f4fa-3fc6-3ac3-8be8-57842807a6d6 | -3.06092 | -53.23547 | 2024-10-17 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f012530f-1dbb-32f5-9369-b0e19e6a6dee | -3.06005 | -53.24124 | 2024-10-17 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7432cb25-5570-3f62-88ff-245e0c5b2aaa | -3.05594 | -53.23473 | 2024-10-17 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b3992822-3c76-3dee-ad49-ef26166e3c09 | -3.05509 | -53.24042 | 2024-10-17 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 63412d9c-f64c-310a-941c-541862c65d62 | -2.68334 | -52.43094 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6b8198b-2ef8-3092-be82-06d927fed314 | -2.68287 | -52.43405 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ced5af1e-629f-3f30-9fbf-188aa9362f7f | -2.09048 | -53.40359 | 2024-10-17 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43bf1637-8a06-3d59-ad16-6566f41c6b1f | -2.08967 | -53.40885 | 2024-10-17 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfe86091-86e5-3997-8144-71e97b454fe0 | -2.78115 | -52.09684 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7afef8a7-2187-37bf-bde1-3883b0dbe352 | -2.78064 | -52.10026 | 2024-10-17 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9a40c6b-dde5-3c99-9ec1-79e2503b30f3 | -3.77778 | -52.39742 | 2024-10-17 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65ae0e11-bc8b-379e-ba95-edfbfda09716 | -3.77422 | -52.39671 | 2024-10-17 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ac54087-695d-35e1-b8c8-15d65d07679d | -3.77374 | -52.39989 | 2024-10-17 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8cb5623-dfe4-3638-99b3-409e6d798afc | -3.77253 | -52.39609 | 2024-10-17 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3899dba-694a-309a-8d27-6fed66e3f65f | -3.77207 | -52.3993 | 2024-10-17 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab331fef-9bb8-3353-9c99-2b35ec388375 | -2.47679 | -55.6227 | 2024-10-17 05:27:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abaf2785-f2a9-3975-a90c-557ab998cb9d | -6.34967 | -58.17685 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef2fb01e-f82b-3b2f-b1a1-ce7ab89339f6 | -6.34829 | -58.1859 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f5704b3-6da1-314a-8ce8-adb64e9795ae | -6.34659 | -58.17176 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 147c2d45-1d49-3fb9-b61d-59d47b4cd253 | -6.34453 | -58.18533 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c45e12a7-58ac-37c6-8931-4b1fb1f7a4c6 | -6.34352 | -58.16668 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99a282bc-9422-3eac-af47-f50be54f8431 | -6.34284 | -58.1712 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b7ec4c9-a16b-3178-9fde-733236e306c5 | -6.33908 | -58.17065 | 2024-10-17 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf6a38a4-8e20-3487-88b5-ec77d7edbe50 | -6.28539 | -58.27274 | 2024-10-17 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd253bb5-5808-35d6-95c0-a10d965de5d9 | -6.634 | -58.72795 | 2024-10-17 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8504cf4d-3e22-3161-b712-9e531f7e80a4 | -6.63161 | -58.71886 | 2024-10-17 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 183ac675-1963-3c26-a78c-377b54863aa0 | -7.3452 | -59.79161 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b15a5c19-6266-3387-b0f8-9e105a465e38 | -7.34227 | -59.78728 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04735734-ab51-344e-b655-392bfe94ed82 | -7.34168 | -59.79118 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 401d8ac0-d562-3a92-bc7e-6615eba01ab8 | -7.33816 | -59.79073 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b81b4072-f604-3273-b455-3384c777fb32 | -7.01231 | -59.3521 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 275f48d7-ecf6-3744-a59e-f3ba91080479 | -7.00875 | -59.35156 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ae6cd3f-6995-30e7-a479-12ac5c1ccfb1 | -6.99103 | -59.32413 | 2024-10-17 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cee7d92b-0635-39bf-ad0b-e08ff88d04c7 | -7.35684 | -63.21803 | 2024-10-17 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9fd313a-a3b1-3747-ba45-611622e2376f | -9.18986 | -66.07991 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 641332c1-fa63-3149-9a2d-eec3ed08833d | -9.18475 | -66.08788 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65cdad70-c4c9-3cb1-9a84-8493043bd162 | -9.0752 | -65.91661 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68a6b844-9ad3-3e22-9f7c-95f8e9ea6cd4 | -9.07449 | -65.92088 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 264a56fb-6c30-3a98-a465-b9e66caf50ac | -9.07156 | -65.91602 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961a20aa-856a-3ce8-bf3b-93e007c3a71b | -9.07084 | -65.9203 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9cd2253-82e6-31b3-8859-59c6cca532a2 | -9.36667 | -66.50251 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b46f05ad-50f8-3ad1-8911-b1c04fcf3d98 | -9.36292 | -66.50185 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f91eaec-c0d7-3158-b2d9-72f6ef6934c8 | -8.45803 | -66.95766 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56c0d62b-59e5-3b7d-8ec8-1a685ed6281e | -8.45718 | -66.96263 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b750b97-d1ef-3214-9009-8a2a0611c48a | -8.45634 | -66.96758 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69eb2404-3a68-3913-92ef-fde88115f56e | -8.45413 | -66.95702 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0039124d-6231-339a-a01b-74ac494eac5e | -8.45329 | -66.96198 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a3d70af-1cd5-3db1-bdde-dd1f3832a0e3 | -8.45244 | -66.9669 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8a76cb6-798f-35e5-a81e-f07f865820b6 | -8.45024 | -66.95633 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e627706-b9f8-3964-ba99-f01d0bc64fe5 | -8.44939 | -66.96128 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c425acc-d5b5-3fbc-80e4-41ea8025b4e5 | -8.44855 | -66.96622 | 2024-10-17 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 057e052c-4ddd-3e6a-82ef-ad32c61f705d | -9.50576 | -66.55051 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10f6fe86-cb1a-3f08-80f1-faf9d446206e | -9.49921 | -67.10812 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6f5a137-4fd4-313d-805d-ddf2fc57ca0c | -9.49874 | -67.10587 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 338f9b0d-0ba1-3d09-bff3-bd7360478447 | -9.49793 | -67.11072 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c63850-af6d-3f4a-9561-596e77e0711c | -9.49631 | -67.12051 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd5b951d-92ce-3f50-b369-4dea3d48b1ff | -9.49533 | -67.10744 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f88a079a-f224-3daf-aaff-89bc06c4245c | -9.47632 | -67.09695 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e0737a-dfb7-3f20-a198-70c805b95514 | -9.47407 | -67.08656 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54e03302-b4cf-3bf8-8f38-f7c1793efd2e | -9.47244 | -67.09627 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e60ded78-57b5-3331-8019-8c76c9871338 | -9.4702 | -67.08591 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab0e59c8-2e1c-3a7b-9e97-185944aeb62f | -9.46857 | -67.09561 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fcaab6f-7edf-3d20-abe7-dc049a707f27 | -9.46692 | -67.10542 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3eb8417-bee2-3410-94b5-1d5d6a962af0 | -9.46469 | -67.09497 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17b74816-e498-366c-94d2-bdde2326d014 | -9.46387 | -67.09987 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdb0c6a0-e43a-3165-8353-2964440cdb1f | -9.46341 | -67.15009 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4859fd77-f8e7-3c57-ad2a-7186411bd688 | -9.46259 | -67.15504 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1552e18d-ceba-31f4-bb64-aaacac1bf591 | -9.4587 | -67.15437 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16d2504f-ec01-38cd-a310-331c67872c52 | -9.45259 | -67.14317 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d856b91-9c91-3834-a35b-97f6d2b1f150 | -9.45175 | -67.14809 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7168d59a-b092-3c65-93f2-c73f6ace1bf8 | -9.4487 | -67.1425 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4fe7400-e675-3b5d-b251-4189d54e0916 | -9.44787 | -67.14742 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 268f499d-aac6-3cba-95fa-104eb4c35173 | -9.44252 | -66.74599 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b25aa59-25c4-3b09-b998-b6d4aea457e8 | -9.42898 | -67.16444 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 883e688f-432e-3d48-8588-fb68f088b0fb | -9.76247 | -66.11413 | 2024-10-17 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38bcfba4-549e-379a-8142-545d8eb42ef4 | -9.9992 | -66.90421 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ca85680-77df-3dfc-a12a-2ef4e606d4b6 | -9.96797 | -66.86294 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f09ff87-616c-34f1-acab-f795a34985fc | -9.96684 | -66.86502 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 388f41f4-6c91-3c4c-b34d-d82fe20b3e33 | -9.90116 | -66.86548 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc6d576-dda2-3813-ac78-8bfd454cfb71 | -9.8898 | -67.21294 | 2024-10-17 05:29:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b975799a-70b5-3b6c-a3a2-ed9c8fdcba62 | -9.81373 | -67.26051 | 2024-10-17 05:29:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08c2453c-abc7-396a-b703-9224b98bfa02 | -9.71738 | -67.06813 | 2024-10-17 05:29:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e665706-3f5f-30d3-aacc-674d9fabe9b9 | -9.68123 | -67.37813 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d956292-809d-3714-8dde-8cd702350e45 | -9.67731 | -67.37743 | 2024-10-17 05:29:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a81ca1bc-8fa5-3d03-a70a-0b1775213c04 | -9.67086 | -66.83028 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76882d76-3111-3940-bdc9-378ed556ae72 | -9.66706 | -66.82962 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab3d8240-cfae-33f3-9b54-db456f5944aa | -9.66326 | -66.82896 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08d46744-b767-3d6a-9da8-4821e648dd72 | -9.61899 | -67.15595 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b27095c-ec18-31a5-97fb-f04f043995ab | -9.57244 | -66.63695 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0986483e-d3db-3946-8189-b8c060dbe8d4 | -9.57211 | -66.63935 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c79c21a-929f-3e33-b7d8-5843eb04a37e | -9.57169 | -66.64153 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d245e10b-d300-3802-93d4-8db9a9f9f4f9 | -9.57132 | -66.64394 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fb4dfac-ffd3-3280-bd26-e4746e01fdf2 | -9.56834 | -66.63873 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 637da5e6-4cb5-337d-a15f-606ebac43d09 | -9.56792 | -66.64091 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ae0392-ec5d-33f4-8b63-0705a4fd3297 | -9.55871 | -66.72005 | 2024-10-17 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README52.md)
