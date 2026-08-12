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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bb9157b-6138-33a1-9514-7e98adac1cc3 | -11.9531 | -46.3672 | 2026-08-12 00:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 4e460d04-fa1b-33a5-9db3-510ba0aeb1e4 | -6.6013 | -59.0037 | 2026-08-12 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| ce0f6da0-f261-32a6-a221-d83ee28fbf43 | -11.4681 | -44.5558 | 2026-08-12 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 350.1 |
| 1758c30c-cc57-33fb-9f06-31dc8d2a973e | -11.9531 | -46.3672 | 2026-08-12 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 626f5be0-4f88-32a5-b3a9-eee6db730790 | -14.554 | -50.402 | 2026-08-12 01:00:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1556ea65-26f8-3fb7-8ca6-4e31e4c0e86c | -13.8989 | -53.8217 | 2026-08-12 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 396de4e6-9491-3914-84ab-e31d4e6829d4 | -8.9598 | -60.555 | 2026-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| afa9317b-3e73-3117-ac5c-7ac656af501b | -11.4677 | -44.5791 | 2026-08-12 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1e08aaf2-6b35-3f61-919d-d8f10c13960b | -11.4873 | -44.553 | 2026-08-12 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 3d97b1cd-148c-3979-afbb-c5f48f855972 | -11.4681 | -44.5558 | 2026-08-12 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 85d5aae6-5144-3b46-83f1-dc02bd9beae3 | -11.9535 | -46.3444 | 2026-08-12 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 4530baed-0a46-35b2-8aa2-b8801ab09da9 | -18.0623 | -51.2843 | 2026-08-12 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| d2a8184f-4ce8-32d1-8fe1-40f7008c641a | -9.1408 | -46.402 | 2026-08-12 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 7e9a757a-867e-3758-ade2-deed0cbfbb8c | -11.9539 | -46.3217 | 2026-08-12 01:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 011c38be-87ec-3d3f-a260-64ed93935971 | -11.8285 | -51.8359 | 2026-08-12 01:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b71d13af-c22e-3d05-96bc-a484815b0081 | -8.9414 | -60.5367 | 2026-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0f9c410b-9915-3224-85cd-0f33a62edfeb | -8.9602 | -60.4973 | 2026-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 353fb474-44aa-36b1-a4d8-8307328e2d6e | -8.96 | -60.5358 | 2026-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 43723536-abf9-32bf-8395-038a815e0eec | -9.1411 | -46.3796 | 2026-08-12 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| b8b6069c-a9b3-312d-a486-1a82dfabca97 | -11.8282 | -51.857 | 2026-08-12 01:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| f8209c2c-68b5-3464-9295-b6938825e25e | -10.0867 | -46.3846 | 2026-08-12 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6e8311d0-b240-3b5a-9a76-079479e0bc59 | -11.449 | -44.5587 | 2026-08-12 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b5b8f4d4-146d-3612-a777-6986fbf17c64 | -11.4686 | -44.5325 | 2026-08-12 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 3263b447-7c66-30eb-82b9-b22da30b6d25 | -18.0619 | -51.3063 | 2026-08-12 01:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 44f64509-11bf-322d-96fa-287ab73c1628 | -8.9415 | -60.5174 | 2026-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 6b416392-30c8-3088-aeb3-a602a5e4d3e9 | -8.9601 | -60.5165 | 2026-08-12 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 125efd01-665b-39a1-8f05-ac6d2cbdc289 | -8.9598 | -60.555 | 2026-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 85cdac83-f96c-3bc3-b780-a318700e2390 | -11.9719 | -46.3871 | 2026-08-12 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d2271e97-b582-3fb5-b618-69c49af94b9b | -9.1408 | -46.402 | 2026-08-12 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 2df5eaab-85e2-3a9f-82a6-211f80d390b7 | -11.449 | -44.5587 | 2026-08-12 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 1cebca6a-756f-3e6b-9183-3f0178d4d2e2 | -9.1411 | -46.3796 | 2026-08-12 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| aff39878-8122-398d-a6b1-d50e9df75344 | -8.9601 | -60.5165 | 2026-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 3f30b237-266e-3578-a30d-ba598867357b | -13.8986 | -53.8426 | 2026-08-12 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 994bdb24-b389-3f6d-942b-13c306154f2c | -8.96 | -60.5358 | 2026-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| fe14c820-eddd-3705-b0b0-082a5af3a8f2 | -8.9415 | -60.5174 | 2026-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 30d6a5dd-6c54-3583-a047-84019e3e9a2d | -11.9535 | -46.3444 | 2026-08-12 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| ae260366-359d-33da-9ff1-9876cbf4c6be | -11.4686 | -44.5325 | 2026-08-12 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 628b9a36-5f00-386c-8736-91f323f8dac7 | -11.4677 | -44.5791 | 2026-08-12 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 511b54b7-e75f-36a0-98fd-37d4f890d5db | -11.9539 | -46.3217 | 2026-08-12 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| ac64ba67-f76b-3f30-a266-f453037d158d | -14.554 | -50.402 | 2026-08-12 01:10:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| f84a82ea-9d0b-3615-9569-39f85e4b6d81 | -8.9414 | -60.5367 | 2026-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 2ef919bc-37af-30ae-86da-80b1f9a9817e | -11.8282 | -51.857 | 2026-08-12 01:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6e556654-8950-309b-a6d5-12487e91f275 | -11.9531 | -46.3672 | 2026-08-12 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 5b127165-9380-3746-99de-457cec08b17c | -11.4873 | -44.553 | 2026-08-12 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4cddc01e-0f07-3561-ab10-c1734d2d288c | -13.8989 | -53.8217 | 2026-08-12 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0b43296f-58ac-3a16-9c33-e37e911523fd | -16.1581 | -49.9802 | 2026-08-12 01:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9021668d-2098-3844-a216-1e1864c77827 | -11.8285 | -51.8359 | 2026-08-12 01:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ffed7fe8-1af7-3b7d-ae6d-fb01851aed60 | -11.4681 | -44.5558 | 2026-08-12 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 32334f52-732c-31c5-82b2-a1e6697ad613 | -11.47 | -44.55 | 2026-08-12 01:15:00 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74e80f4e-62bc-3b44-9556-752eea72c4e7 | -11.9535 | -46.3444 | 2026-08-12 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 2f7e057b-f5db-341c-bf71-0662ac42801b | -11.8285 | -51.8359 | 2026-08-12 01:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 828bef3b-6b8b-3470-9d68-80ab1a69fda1 | -9.1408 | -46.402 | 2026-08-12 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 322ce81f-e845-3b15-b8a6-45bc238d1083 | -8.9601 | -60.5165 | 2026-08-12 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 0d48643a-8fa4-3ceb-9290-467410d8ca1c | -11.9531 | -46.3672 | 2026-08-12 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ae71cf71-0db3-3126-bb91-7a04e2722f3d | -11.9719 | -46.3871 | 2026-08-12 01:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 1dd9702c-26aa-312e-8578-aaf1d6c9673d | -11.8282 | -51.857 | 2026-08-12 01:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 144.3 |
| ff144c18-14c7-3da8-b937-39f2424813bb | -8.9598 | -60.555 | 2026-08-12 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| f053d107-c433-3536-9c8c-8d4003c5b1ae | -11.449 | -44.5587 | 2026-08-12 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bac4ebbd-8b74-3559-9a4d-2a6c09e3bbf3 | -11.4681 | -44.5558 | 2026-08-12 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 915d30a2-1601-3d5f-b345-3326ea1166c0 | -9.1411 | -46.3796 | 2026-08-12 01:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 34f483cb-27d5-3c03-9424-4af63967700d | -13.8986 | -53.8426 | 2026-08-12 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8f86148e-3533-39e9-ab65-02e71cbe989f | -11.4873 | -44.553 | 2026-08-12 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 9c2838d8-1147-335f-93c0-9546e9cbbe66 | -14.554 | -50.402 | 2026-08-12 01:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| a8c719b5-e606-3651-a755-2bd16f293aea | -8.96 | -60.5358 | 2026-08-12 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| fa75e3f7-c0e1-3d80-a58d-b14af922bd83 | -11.4686 | -44.5325 | 2026-08-12 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5f1c0ae0-83a3-3d9e-9b0e-524b8b50b742 | -11.8279 | -51.8781 | 2026-08-12 01:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9923a68b-9687-3d1c-b0f2-274b8635443f | -13.8989 | -53.8217 | 2026-08-12 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 48456692-5016-38ad-af93-f76a0d725173 | -11.4677 | -44.5791 | 2026-08-12 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9ccb5fc8-53ba-33a6-9b81-dc10d5a3a846 | -14.554 | -50.402 | 2026-08-12 01:30:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| b7701965-4e3d-36ac-8940-689eb5a66873 | -11.8285 | -51.8359 | 2026-08-12 01:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 3e4b8171-17f4-37cc-a800-87d97389c0cf | -11.449 | -44.5587 | 2026-08-12 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 12497845-2bb7-30a0-b5e5-0e203fceabba | -8.9414 | -60.5367 | 2026-08-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 7c29fe19-4527-3f2e-8978-a4a6caa3d597 | -11.9535 | -46.3444 | 2026-08-12 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 354a357a-6239-3b0f-8653-d6968d8225c7 | -8.9415 | -60.5174 | 2026-08-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a3dcb2e6-24a5-3c70-961f-a94faff1934a | -11.4681 | -44.5558 | 2026-08-12 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 274.7 |
| da1b2fe0-0d56-390f-8f4e-5fc167bde2ca | -11.4873 | -44.553 | 2026-08-12 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0ba99247-9e32-3ae3-87fb-fa1ce29caf3c | -11.8279 | -51.8781 | 2026-08-12 01:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a37da169-aab4-3327-a283-764b09236948 | -11.9719 | -46.3871 | 2026-08-12 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 918c20b3-2e7b-3cec-a943-934f02a0b90f | -13.8992 | -53.8009 | 2026-08-12 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 15e55c8e-8ce0-3776-a9fb-d7667f5d644e | -11.9531 | -46.3672 | 2026-08-12 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b7860796-6a16-386a-883b-30674b7f6d87 | -9.1408 | -46.402 | 2026-08-12 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 11d17da9-822d-32cc-94ab-e1cf0f7a49e2 | -11.4686 | -44.5325 | 2026-08-12 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 15097b17-bc7f-3505-89cb-921f1ed1819f | -9.1411 | -46.3796 | 2026-08-12 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a0220b51-3816-3361-a8b8-10202e9bda36 | -8.96 | -60.5358 | 2026-08-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 7915a390-f923-35b8-a582-edebef29d043 | -8.9601 | -60.5165 | 2026-08-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| a246ed59-d82a-3c73-800c-b765e37e7d21 | -13.8989 | -53.8217 | 2026-08-12 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 04e96ce7-5472-3e44-8842-3cf07871382e | -11.8282 | -51.857 | 2026-08-12 01:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 61442a30-2fed-32f5-bf1f-2bfbccdaa081 | -11.8473 | -51.8549 | 2026-08-12 01:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9724f068-b6a0-3c81-a0a6-1e71da810573 | -9.1219 | -46.404 | 2026-08-12 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| ac720d70-1e38-39db-8293-f0fbfb4d0bc1 | -11.4677 | -44.5791 | 2026-08-12 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 59da340f-fa3b-3f09-9a0c-a4b7a1bf67b5 | -8.9415 | -60.5174 | 2026-08-12 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| e8d36ba5-63cd-3e08-a602-a001eaa1cde3 | -8.3544 | -45.9897 | 2026-08-12 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 4462ec50-44c4-3f59-b912-6db991a5fd15 | -8.9414 | -60.5367 | 2026-08-12 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 364cbe70-9348-378d-b759-9d0d56f8497c | -11.9535 | -46.3444 | 2026-08-12 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| e8837e49-d6f9-3a69-ae6a-1848ee8dfafd | -6.6013 | -59.0037 | 2026-08-12 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| adf2c309-d6e5-3a31-8d36-62caca010e8d | -11.4686 | -44.5325 | 2026-08-12 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d57488de-27a7-3b1e-a8bc-5aac7b24941a | -7.1883 | -44.3733 | 2026-08-12 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b43b6894-1d2b-3081-ae08-8a0a93fffb3b | -11.9531 | -46.3672 | 2026-08-12 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b3ce7c4d-9bcb-3c59-89a4-dbaaf82a5aa8 | -11.8282 | -51.857 | 2026-08-12 01:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 45f01887-1510-300a-8e1a-b9c20ffe8f19 | -9.1411 | -46.3796 | 2026-08-12 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |


[Clique aqui para ver as próximas entradas](README5.md)
