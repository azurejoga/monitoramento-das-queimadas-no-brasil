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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b29041c-93a4-3f7a-a618-9b96aba5bb52 | -8.5221 | -54.8007 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| ca5648c5-430b-374f-aa6b-828356230bfa | -10.2776 | -50.3459 | 2026-08-22 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| ac72fd7e-35cc-383c-8516-e87cb7e053e0 | -10.9627 | -51.4003 | 2026-08-22 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 4f4e78b0-8133-3e0e-bab3-b5bb1783a999 | -9.1536 | -59.464 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3e6d2ec0-5372-3753-8e74-a2e0808e4fb0 | -9.191 | -59.4425 | 2026-08-22 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 284d0503-d63d-3233-8cee-611cf2f08dc4 | -10.2395 | -50.3711 | 2026-08-22 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| a80b05cd-0346-3f0c-8408-c099730f8fde | -18.0867 | -46.933 | 2026-08-22 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9d0befc4-d7a1-3dae-b723-ec7c12e2cc01 | -8.5404 | -54.8398 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.8 |
| 061644ca-eef8-3077-9f77-5e062a6ddbfd | -16.4773 | -47.9381 | 2026-08-22 01:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 9785858d-2fd5-335e-af67-f9cb1db52422 | -6.3863 | -54.9451 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 88d99888-5984-3ac3-8db3-b52312455935 | -6.2712 | -62.5231 | 2026-08-22 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| de38277c-675e-39d3-8428-e112721097a8 | -8.5218 | -54.8411 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 154.6 |
| 34b38167-a9b8-3548-a5b1-3b0ea250d21f | -8.522 | -54.8209 | 2026-08-22 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 216.3 |
| 625e70ee-1fc1-32a0-a95e-39f5d98305b3 | -6.8373 | -59.6689 | 2026-08-22 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2e33a537-1067-3674-b8ac-827eb1291688 | -10.2395 | -50.3711 | 2026-08-22 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e1571cba-3c6f-38c9-870b-2e8a478e8c61 | -6.97 | -59.0465 | 2026-08-22 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 98aa2785-6f2f-3f57-8462-2ac9a327f04c | -8.9042 | -60.5385 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 59476c72-dbbc-3739-8254-0dfe404afe6d | -9.191 | -59.4425 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 423bfd55-81e1-38d5-ba9a-6d04b0543f65 | -10.2398 | -50.3497 | 2026-08-22 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 2377feca-3c58-395e-af22-b0306c505744 | -8.5221 | -54.8007 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 10c15a8c-39d4-3cb3-a99b-49b58c9210a6 | -16.4971 | -47.9344 | 2026-08-22 01:10:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 734e2dc6-51ac-3f13-ab28-efd929aac944 | -17.9613 | -42.728 | 2026-08-22 01:10:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| 56e95d2c-c42b-3416-ac38-3bf5bbbdf2ba | -8.5404 | -54.8398 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 66e1d8ae-6b8a-347d-9411-254502f8288c | -8.5218 | -54.8411 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 97e28d24-8f43-3115-b069-9428e0c0bb0c | -9.1722 | -59.4629 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 251.0 |
| f09b64a1-240d-3837-bd9e-b9a989f0f692 | -9.1538 | -59.4446 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 547d7fdd-9970-30d4-91b6-0a8582cebd83 | -6.3862 | -54.9651 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| afe63d91-6077-32cc-b0cb-fd88aca867f1 | -10.2587 | -50.3478 | 2026-08-22 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| e713daa3-f53b-3f31-af45-c29166e2c34c | -18.0867 | -46.933 | 2026-08-22 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 66.6 |
| dddf770f-ff0d-3166-b2d3-a941f07d3c7b | -6.3863 | -54.9451 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d4f1923b-fd81-38c7-b1d5-7142c64361de | -8.522 | -54.8209 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 191.7 |
| c064e516-0dec-38bd-9c23-c50a01291f03 | -6.8188 | -59.6696 | 2026-08-22 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 45b240d8-371c-3224-8e82-4f921e2dd3bb | -9.1724 | -59.4436 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.1 |
| c62a97fc-7fcc-3e49-9568-3cbbc38d5c00 | -8.5406 | -54.8197 | 2026-08-22 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 53582de0-0920-3436-8e01-5950dd6b1bec | -9.1909 | -59.4619 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 9c81f14a-08a7-37c0-be93-cf138b565e7e | -6.2712 | -62.5231 | 2026-08-22 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8adb4524-a240-3548-bffd-67475246ae4f | -9.1536 | -59.464 | 2026-08-22 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 2d624552-7d86-31a6-a29c-5122464f5ff6 | -10.2776 | -50.3459 | 2026-08-22 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f4c492c7-16e2-3445-8f15-ad0ea3c31508 | -10.2584 | -50.3692 | 2026-08-22 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 09578928-b77c-3926-8d6d-0d8df53501f6 | -6.9699 | -59.0658 | 2026-08-22 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 209.6 |
| 45914866-920d-37ff-86d0-b7de2893f404 | -6.81 | -59.4 | 2026-08-22 01:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 742292a2-338d-33a2-a41f-866fcddb4e22 | -8.52 | -54.84 | 2026-08-22 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6616a430-0488-331e-b632-eddfdfbf0852 | -6.78 | -59.39 | 2026-08-22 01:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a93db4ac-ddfe-35a3-ad82-a104613c8c19 | -6.78 | -59.47 | 2026-08-22 01:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9f90b9-5745-3184-b0d0-7429dae9245e | -6.77 | -58.63 | 2026-08-22 01:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37c54444-7276-3252-a483-1c99d237bd05 | -6.74 | -58.69 | 2026-08-22 01:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16a81f50-207f-3de4-92c3-f3fba16b05d3 | -6.8188 | -59.6696 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 72060a4d-6a34-3311-a93e-95ef49619d87 | -8.9934 | -50.7427 | 2026-08-22 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ed0d7d1b-a1a0-311a-9109-e1989d9d0514 | -10.2776 | -50.3459 | 2026-08-22 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 55db6fdd-65a4-33d4-86f5-fd631c04725f | -5.9997 | -57.8054 | 2026-08-22 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 08b00975-6acd-3761-bdf5-8399d23a6499 | -6.9883 | -59.0651 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| fd5a2e76-ce93-3b02-8275-13f2081fabb7 | -8.5404 | -54.8398 | 2026-08-22 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 915a2d7f-c1f4-3b28-89b9-d1952abdee48 | -6.2712 | -62.5231 | 2026-08-22 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 708fea0c-5ab5-392b-a0da-609adf2d8300 | -6.97 | -59.0465 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 283.5 |
| 539704ed-0281-3348-bd07-a34438e667c1 | -6.3863 | -54.9451 | 2026-08-22 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cf7055a0-7dcb-3ada-935d-9415d6856d17 | -6.9514 | -59.0666 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a175f14f-83a3-3d35-b886-2c2d43199cf7 | -10.2395 | -50.3711 | 2026-08-22 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 3d7d68cb-4946-393e-b3a7-155eb84ce650 | -6.9699 | -59.0658 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 288.4 |
| e7d8b2c9-d798-308a-8bf4-a91720e834d0 | -8.522 | -54.8209 | 2026-08-22 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 236.2 |
| 81442b60-6cc0-37d9-9e85-7d8e57d215c1 | -8.5218 | -54.8411 | 2026-08-22 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 6e765885-15ef-3a14-8d72-05b633228ac1 | -6.9515 | -59.0473 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| aa4c207c-44dd-3a4e-9b19-cbc12a5b4a1b | -6.2528 | -62.5236 | 2026-08-22 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 679205ef-cd9b-3641-b12f-2ea74959b682 | -10.2587 | -50.3478 | 2026-08-22 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 3657fa65-8f14-3f7e-be17-f6d4b3e4986c | -8.5406 | -54.8197 | 2026-08-22 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 206.7 |
| 0a9b2839-1438-3f99-9524-96e0b971b672 | -17.9613 | -42.728 | 2026-08-22 01:20:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.9 |
| 005fb166-7947-3be4-8a50-9b6c6d3fee63 | -6.3678 | -54.946 | 2026-08-22 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ae3a4a1c-6ed9-3701-96fe-fddc638ff4a9 | -6.8569 | -59.4564 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| efdb1d46-7e4b-35b5-8e68-8e6c5e4b5c55 | -6.9884 | -59.0457 | 2026-08-22 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 7f63a9f1-031f-3134-b71d-0cd17c9a673d | -8.9042 | -60.5385 | 2026-08-22 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0879374c-c6e8-3880-be43-9db06fc7ae09 | -16.4971 | -47.9344 | 2026-08-22 01:20:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 7ec771fc-a89e-3156-9d25-8f0801f17c6f | -10.2398 | -50.3497 | 2026-08-22 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 7fc61ade-03e4-3439-9f7c-5ea046298216 | -10.2401 | -50.3284 | 2026-08-22 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 78d85ae1-0158-381f-ba53-ce5f4dc4f0a2 | -8.522 | -54.8209 | 2026-08-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 262.7 |
| 474a77ad-563c-3f5c-b6b1-d68acbe59b57 | -8.5404 | -54.8398 | 2026-08-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 7b1414b9-d623-35a5-aed1-f6396ad63daa | -10.259 | -50.3265 | 2026-08-22 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2e4744c9-eae6-3412-9d01-e24a790d4bbd | -7.3624 | -55.693 | 2026-08-22 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b00d14db-d79a-3436-97ad-f4a65063c7af | -8.5406 | -54.8197 | 2026-08-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 230.5 |
| 275df82d-fdd2-3e57-8fce-2a2097c834c5 | -8.5218 | -54.8411 | 2026-08-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| c4ee0962-784e-3c11-a3c1-3e31008c5d90 | -10.2587 | -50.3478 | 2026-08-22 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 262dbeec-939a-397e-8054-807b443bc919 | -6.8569 | -59.4564 | 2026-08-22 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 838aaf8a-98f4-39f0-98c8-f855d074fbda | -16.4971 | -47.9344 | 2026-08-22 01:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7557e49a-6577-3d26-b084-c1f1696fde67 | -6.97 | -59.0465 | 2026-08-22 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 92ecfd17-7829-30a3-86a8-7c1090641f16 | -6.2528 | -62.5236 | 2026-08-22 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 9e13876d-eb35-3260-b917-9df3b5778ac5 | -10.2398 | -50.3497 | 2026-08-22 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 180.0 |
| f93eccf7-a922-3e20-b3e4-f2c37158397a | -6.9699 | -59.0658 | 2026-08-22 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 195.1 |
| aab09a85-c12c-3a6e-96dc-de41102fa7cd | -8.9042 | -60.5385 | 2026-08-22 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e217770f-9851-31b7-98de-b9ea364dba82 | -8.5221 | -54.8007 | 2026-08-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a7154b7f-c4af-35a6-9854-f0a8ffea7b76 | -6.9514 | -59.0666 | 2026-08-22 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ddb95edf-1f8e-3618-beb3-40ca6bebc85d | -10.2776 | -50.3459 | 2026-08-22 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 3194cf31-b578-3334-8a45-33cb056512f0 | -6.8188 | -59.6696 | 2026-08-22 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 4b0e05fd-13c0-3085-954b-19d44c70515a | -6.3863 | -54.9451 | 2026-08-22 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8a028e6e-e3b3-374a-a144-417e9aa9512f | -17.9613 | -42.728 | 2026-08-22 01:30:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.5 |
| e434cd3b-26fe-354a-93d7-c832ea675572 | -6.2712 | -62.5231 | 2026-08-22 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4b4f53e5-b856-3e78-9cc0-c95d3f83b90d | -10.9627 | -51.4003 | 2026-08-22 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 2b9ded1b-490d-3bbe-9499-6ae46c65fe34 | -11.5864 | -46.5762 | 2026-08-22 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 9697f6a1-51ad-3de9-ae92-b6c4b673e1e8 | -6.8569 | -59.4564 | 2026-08-22 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d03c5f2c-ae6e-3560-bc12-69598520dff8 | -8.5221 | -54.8007 | 2026-08-22 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 27f63aad-aaa5-3d54-b41a-286238cb43d1 | -16.4971 | -47.9344 | 2026-08-22 01:40:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 29543eeb-f500-3537-b805-0307a7445482 | -10.9438 | -51.4022 | 2026-08-22 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 655fe245-dba4-39c9-9080-cf71fe84fa3b | -6.3863 | -54.9451 | 2026-08-22 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |


[Clique aqui para ver as próximas entradas](README9.md)
