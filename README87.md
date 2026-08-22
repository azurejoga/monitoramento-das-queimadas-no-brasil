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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd5321b-7975-3cbf-a875-d30d7462a3c4 | -11.9492 | -45.5014 | 2026-08-22 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 14be929d-9072-3ad9-8574-88e8d5097703 | -17.5891 | -44.6164 | 2026-08-22 13:10:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 7930ae01-99f2-3b30-8555-923ceaa7ba80 | -6.8569 | -59.4564 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 9c9951d8-56c7-34f1-ab9f-c8d415a35a1c | -6.8203 | -59.4001 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ab0ddc88-9050-3715-bce1-42e099708cf8 | -6.8005 | -59.6511 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 68d43b8f-a815-3b8e-afe0-18402a368aa8 | -6.8017 | -59.4394 | 2026-08-22 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c48eb494-9db4-31f4-8050-b7ee7d2fd69a | -11.3472 | -46.0431 | 2026-08-22 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 562c0747-f587-367d-b2b4-d0d9bcb45542 | -8.3904 | -62.6774 | 2026-08-22 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7b50973c-6f01-335f-9b4f-002f062ebd96 | -11.625 | -46.5484 | 2026-08-22 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 324.7 |
| 7f6df4de-b252-34c9-be80-38b22284d6c9 | -8.5218 | -54.8411 | 2026-08-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9d1f2225-fbb9-352c-8132-e8c3b58d37a7 | -8.4739 | -46.9831 | 2026-08-22 13:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| c9964ae1-cac0-37f6-9275-cf3c35ea9817 | -8.5221 | -54.8007 | 2026-08-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 29715f19-c4d8-3844-bc05-a47bf2f2230c | -13.54 | -51.77 | 2026-08-22 13:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1db0ecf4-7af7-38e0-9926-7cd37d581c5c | -13.54 | -51.71 | 2026-08-22 13:15:00 | MSG-03 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 467ac88d-bafc-3df3-a9dd-733cdb8481e8 | -6.8203 | -59.4001 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c10dee88-cdb3-3020-850d-544534424ed7 | -7.3624 | -55.693 | 2026-08-22 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 9fb11075-212a-345a-9b76-1fb61a3e07fb | -6.857 | -59.4371 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| ffe13ef1-cc38-3cc0-a165-ed37592a02df | -11.6055 | -46.5736 | 2026-08-22 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 466.4 |
| 411322c1-a71f-3c08-87d5-24558e261beb | -6.8005 | -59.6511 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 3fb9460b-047d-38cd-8123-f411e83b5e41 | -9.0348 | -60.4551 | 2026-08-22 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| bfe224ce-06d9-34f6-9ef2-bd8fc72ee43e | -8.522 | -54.8209 | 2026-08-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 339aacea-a7fa-3bfc-88f0-cbd42e402f9f | -11.3663 | -46.0405 | 2026-08-22 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 255.8 |
| c83cac57-4544-39bd-b587-762a2d5d0bb6 | -17.6092 | -44.6119 | 2026-08-22 13:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 3b4bcad8-b3f6-3d6e-a933-38e4ee2f3b9a | -6.8991 | -55.7176 | 2026-08-22 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1805591f-73a0-36f4-94eb-a21641d925fb | -7.3625 | -55.673 | 2026-08-22 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f1ec5415-e767-370e-a689-2da33807d0a3 | -12.281 | -43.1574 | 2026-08-22 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 184.3 |
| f5708cd8-b6fa-3ef9-aa01-5c4806e70e7d | -12.2806 | -43.1813 | 2026-08-22 13:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 99.4 |
| ef4b9c28-e387-3560-95e3-66e86ca4e14f | -6.8018 | -59.4201 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 01f5d72c-7cde-3e52-bc34-01fbb1b9df63 | -11.3667 | -46.0177 | 2026-08-22 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 050640b3-b50b-3c99-b466-9d2db426b2a4 | -17.9553 | -44.364 | 2026-08-22 13:20:00 | GOES-19 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 99.8 |
| cf122613-6f6c-3c6b-b34c-2fd96936198b | -17.5891 | -44.6164 | 2026-08-22 13:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 190.4 |
| ccbd6937-959c-3eba-a3cb-c31000c0fead | -6.254 | -55.391 | 2026-08-22 13:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 1452e6d8-cdfe-3a2e-adbe-0cfaf3058509 | -13.5481 | -51.7403 | 2026-08-22 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 62e809d1-9268-3071-91c1-7dceeb77bf2e | -8.4739 | -46.9831 | 2026-08-22 13:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9e41b4cd-7d19-33ef-9697-4f6ca3449f9d | -11.5864 | -46.5762 | 2026-08-22 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 4481ad50-6454-3901-ac55-ff468bf0be77 | -5.9997 | -57.8054 | 2026-08-22 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4dc31c81-1990-31e0-b143-a1bf3c902f0b | -6.7832 | -59.4401 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.2 |
| cabe5736-8a87-3dd6-997b-c40dd0618847 | -6.8569 | -59.4564 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| e1837f6b-f929-33c2-b29a-47ecd27fd31f | -6.8202 | -59.4194 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 79ab2dd6-8e3d-3733-8138-18857f4e554d | -8.3904 | -62.6774 | 2026-08-22 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 1a631db2-3e83-305d-bd8c-417996c82ecb | -6.8004 | -59.6704 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 261.5 |
| c8cae682-4462-35ce-986d-5de00846291a | -8.5406 | -54.8197 | 2026-08-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 173.5 |
| cc68c716-efcc-3bd2-9bb3-6e0eb89c2ba9 | -11.3475 | -46.0203 | 2026-08-22 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 92c4538d-b0bb-3435-b145-1020b5c3d975 | -6.8188 | -59.6696 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 32b13d38-91c6-3983-9a8b-940baf31c5fa | -8.3903 | -62.6963 | 2026-08-22 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 7e987ca0-2415-3a83-9d75-e9d3b566ec67 | -6.8568 | -59.4757 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9183e9a2-8683-3985-b5aa-d70708d0225c | -16.1273 | -43.6437 | 2026-08-22 13:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f267cccb-5b7b-3c9c-b787-73da0d6a9a54 | -7.0191 | -48.0323 | 2026-08-22 13:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1f7b2da4-6531-3219-ac0c-6cd5d6007993 | -17.5897 | -44.5924 | 2026-08-22 13:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 3a6c0719-164d-3327-b79e-35ee36c59c22 | -8.5218 | -54.8411 | 2026-08-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| e8a5a32d-dc76-3f26-ae60-7c816dddeb4a | -11.6063 | -46.5284 | 2026-08-22 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 64241911-5c69-33b6-ac20-02a929029ea6 | -6.7833 | -59.4208 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7acca260-c747-3b30-b0c5-bb5c93b905aa | -16.1279 | -43.6194 | 2026-08-22 13:20:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 7a9c4525-b32f-3ac9-8b34-5b57f313242f | -6.8017 | -59.4394 | 2026-08-22 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 4ae8d01f-7fad-3d96-8de2-c0e6a987514b | -8.9936 | -50.7215 | 2026-08-22 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| ea377490-5edd-36b7-8491-40a26f3b0705 | -11.3472 | -46.0431 | 2026-08-22 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.1 |
| 993deb31-f64b-38c2-8590-b51c584b14c9 | -7.7503 | -44.5725 | 2026-08-22 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2351a78b-8f22-3bb2-b1fa-f6c43c978b6a | -11.4494 | -44.5353 | 2026-08-22 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 245.3 |
| 3602a9cb-e600-329e-b08d-3aaa40502cae | -9.1722 | -59.4629 | 2026-08-22 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 574f110e-5711-38cf-af79-1df574e533f0 | -8.3289 | -46.53 | 2026-08-22 13:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 76623eae-6773-3a94-b1f7-643ee84f8643 | -8.5221 | -54.8007 | 2026-08-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| a10f934b-e82d-3e8f-bbd9-19578fb642c4 | -8.5404 | -54.8398 | 2026-08-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| c5917214-9c73-3955-bc16-a8f203bae08c | -8.5408 | -54.7995 | 2026-08-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| ea2d4241-b39b-3830-9b52-6e48c55f131e | -10.7847 | -50.5706 | 2026-08-22 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 94647218-8090-3447-9083-640c20d3e800 | -6.254 | -55.391 | 2026-08-22 13:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| ecd1ee3e-e555-3bf6-a242-ca50140873c8 | -6.8569 | -59.4564 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| e96b4d6f-0da6-3e0d-a19c-1f3fc9260caa | -9.0124 | -50.7199 | 2026-08-22 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ecf0cca7-e9ad-3581-8cd7-eb854f285ca2 | -9.0534 | -60.4542 | 2026-08-22 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 35e22b41-3074-39f7-bbdf-dd1067d642a3 | -16.1273 | -43.6437 | 2026-08-22 13:30:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 708674a4-0d81-3988-bbd2-1e4851bf5303 | -9.1722 | -59.4629 | 2026-08-22 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| bc70faee-4b10-3217-99c6-c733c4df5c53 | -8.3903 | -62.6963 | 2026-08-22 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3fdb41ae-80d7-37ea-a438-a6e46b40e947 | -6.8991 | -55.7176 | 2026-08-22 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 56547d0b-560a-3e8a-95bb-392a25f19a2e | -11.4494 | -44.5353 | 2026-08-22 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 09d91907-a8d1-3bbc-9707-8be4eeae2c20 | -17.5897 | -44.5924 | 2026-08-22 13:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 18be6b66-3511-3933-955b-c56a6f5b5af6 | -6.8755 | -59.4364 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c6b64430-2637-3a94-a3c5-49f50eebb66b | -9.1724 | -59.4436 | 2026-08-22 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 8391d2bd-f065-309d-92d0-ded6d100b50c | -7.3625 | -55.673 | 2026-08-22 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d6887728-8447-39f5-9df0-0a1e7b5269b5 | -10.7847 | -50.5706 | 2026-08-22 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 67b1b63b-f612-3f07-bc19-7eabae4762d1 | -6.8568 | -59.4757 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| ec6497b3-e612-305a-93aa-b5a6386bf825 | -14.0688 | -54.01 | 2026-08-22 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 204.3 |
| cfb16c47-a8f4-309b-9ce8-3c94d83116cc | -11.1351 | -46.185 | 2026-08-22 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 31d075dd-2695-3848-baa5-dd026b0b5f59 | -8.3904 | -62.6774 | 2026-08-22 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7d29cfc3-4712-3991-969d-c370b0a2fee2 | -6.8004 | -59.6704 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 330.6 |
| e0bd7084-b207-3e1a-ac79-b86330156b2c | -8.4089 | -62.6767 | 2026-08-22 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 51a91c22-c67b-3d23-a0ab-cadcde80528b | -17.5891 | -44.6164 | 2026-08-22 13:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 2f394e44-2fea-32c2-b225-411e80d02041 | -12.2806 | -43.1813 | 2026-08-22 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 10fa48a2-85c1-3742-a4e9-78314b04d7cd | -6.8005 | -59.6511 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 76d5993b-6122-3492-9974-7c2b02d9749a | -12.281 | -43.1574 | 2026-08-22 13:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 151.5 |
| 0c5a9c11-26b6-335b-9de3-4f243aad8bef | -6.5302 | -58.5227 | 2026-08-22 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9474bef3-d3fb-391e-9214-05908abfe76a | -6.857 | -59.4371 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| da014983-9fb0-3688-87ce-6d3deacd6c84 | -9.035 | -60.4359 | 2026-08-22 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9b24670a-f9c2-3156-b044-73017173c6b7 | -11.3663 | -46.0405 | 2026-08-22 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| f0038009-f90d-3c14-b8e4-58fbf50e2ae1 | -13.8387 | -53.995 | 2026-08-22 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 0f733c7d-ab19-3626-acb1-825a2cb79bf6 | -11.5864 | -46.5762 | 2026-08-22 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 3b87540f-a1e9-3ac7-836a-346d5498ba4b | -11.6063 | -46.5284 | 2026-08-22 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b347e925-214d-3142-bb8d-deb76a63f015 | -13.5481 | -51.7403 | 2026-08-22 13:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 80aadd86-c35a-36ff-b019-e68d3cd2709b | -10.8037 | -50.5686 | 2026-08-22 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b38d0744-d105-3323-b969-603f488a6bfb | -7.3624 | -55.693 | 2026-08-22 13:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 806d63ed-f640-374c-bed4-1e5600a889ae | -6.97 | -59.0465 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 974ca484-4f60-301b-a3de-98a1240dbb0a | -5.9997 | -57.8054 | 2026-08-22 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |


[Clique aqui para ver as próximas entradas](README88.md)
