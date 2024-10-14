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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bf1501b-c80e-3fa5-8b31-18408cf307e1 | -17.13273 | -56.86087 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0df7056c-7eb0-3952-b7fc-d8e0d51abfb9 | -17.13197 | -56.86531 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c9115743-d0a6-38e1-bb91-d8fb5685e181 | -17.12955 | -56.87169 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d05d14db-4894-3169-93e5-d500aa4d2361 | -17.12831 | -56.86461 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2a6ffde3-990a-3971-89b0-f7688214e601 | -17.12755 | -56.86906 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3e9a4803-1e64-31fc-b2dc-86cfb0270097 | -17.12542 | -56.85948 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5b34eb16-4c39-3fd6-88ae-877ce721d9cd | -17.12465 | -56.86392 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 468d4804-bb02-31af-9396-2200368cc06e | -17.12024 | -56.86766 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 877a0bd8-299c-37c1-bb1b-d9cf4f0fb015 | -17.11735 | -56.86252 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4dff92f6-ccba-3c72-9c5b-a89fcc1094e9 | -17.11658 | -56.86697 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 11f23f04-6333-34d9-9e82-e66e26d4b319 | -17.01833 | -56.85033 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c6f0f3b7-fb06-3b1a-979e-f8de7b73cf7d | -17.91904 | -57.31418 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d40fde0e-225f-3053-8d42-058212130d79 | -17.9182 | -57.36144 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| e3de3696-3aef-335e-81ad-08be80fbbea3 | -17.91781 | -57.35928 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 01a3f842-2484-3f89-b7e8-37e086d9ce33 | -17.9176 | -57.31649 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5b132f66-828e-3423-8328-10f349017746 | -17.91702 | -57.36381 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2f21513c-0f16-3469-b60e-d6d31f9fec4f | -17.91623 | -57.36833 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4d532477-1b71-3fa0-9f19-4b2c5f8e1cb5 | -17.91615 | -57.35156 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 02a874c5-284f-37f8-873d-0eed47525af3 | -17.91449 | -57.36074 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2e7d2799-aeed-3a90-a098-9d872bae9941 | -17.91368 | -57.36523 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c26697a1-2118-3a94-ab88-a82069b34055 | -17.91331 | -57.36312 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 430dbdef-d63b-3a9c-8312-d1042fd1d156 | -17.91288 | -57.3697 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ce54c090-eac7-387d-8673-f21f0c7a3aae | -17.91252 | -57.36762 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 108d76f6-9108-3405-a356-7306f4616bb7 | -17.91173 | -57.37216 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5217c097-9623-39ab-aff9-bd91e70869a8 | -17.9102 | -57.31506 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 13d6d87c-a79e-3419-81e9-ffbc42726b16 | -17.90997 | -57.36457 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 266ac505-e961-32c9-bdee-c8cd5c73043a | -17.90915 | -57.36908 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| ee1377f4-0dbc-344a-9077-18689279eea9 | -17.90881 | -57.36694 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| dc98fa9d-fa23-3cd6-993b-b2e2f5867fe4 | -17.90859 | -57.32422 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 46920fd6-504f-326c-8b2f-e1514d9be00e | -17.908 | -57.37155 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 09975012-5aef-3a16-b395-7989f032f0d1 | -17.90649 | -57.31434 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 07ffac62-0fdb-3798-a085-693caf1ad4a7 | -17.90508 | -57.36629 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 12e435d6-2647-33af-8c97-03f3948abbdc | -17.90428 | -57.37088 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| b67524ca-1510-39f7-a4af-7ad429bf2811 | -17.90199 | -57.3182 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ffde420e-acad-3f9c-bad4-498f335d6fd4 | -17.90137 | -57.3656 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fb9e8746-720b-3c3e-9e6e-f751c4d6824e | -17.90056 | -57.3702 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| b2492b18-064e-3867-a12e-c9cd1bfd5c9e | -17.89975 | -57.37482 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 3077d0df-bfba-3997-86ba-56f1f89fb1af | -17.89604 | -57.37412 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.5 |
| d5a55800-508e-36b0-ba2a-cc7045802d7e | -17.89475 | -57.35957 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e5da42c5-45a6-3ea2-82f6-0384f35b3451 | -17.89394 | -57.36418 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3a0d121f-303a-3969-8ec7-fd6efca15896 | -17.89313 | -57.36879 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 9737742a-3715-382b-92a3-c5697054b44d | -17.89232 | -57.37341 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.5 |
| 56178d1d-7689-3bca-81c5-064d4be5d04d | -17.89104 | -57.35885 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5c04a32f-c17c-3652-a9a0-c3305c899f1c | -17.89023 | -57.36346 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab1dffcc-bb54-3ebe-b1ce-384603e80942 | -17.88861 | -57.3727 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 269c5c98-c4b5-32e0-8148-8118671b0ad0 | -17.88733 | -57.35812 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4e2f545e-160d-3e24-a1c6-763a8233db68 | -17.87991 | -57.35669 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b278a555-3663-3283-8620-3eabace1ada7 | -17.87538 | -57.36057 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f37dfe4f-4a32-300a-84f5-7ab0f1d11da6 | -17.87376 | -57.3698 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2708a2c3-f5e8-3ef6-bf4d-ef6b65c346b9 | -17.87294 | -57.37442 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 217b18cd-ed41-39df-a8c2-f44ed0cfb079 | -17.87005 | -57.36907 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c628759c-f494-34c3-86f2-538e11c234f2 | -17.86923 | -57.37368 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.6 |
| d33c8765-afd8-3c42-ba43-884b76f08e81 | -17.86552 | -57.37296 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 784354f5-1c87-380b-ad21-d08f504d47cf | -17.83372 | -57.31442 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.3 |
| a35d9214-00d3-3684-99f0-79c789b725da | -17.83127 | -57.37107 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5ea26ec3-c68d-3531-8c0e-581d6d5ba3e8 | -17.83002 | -57.31371 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 808232d8-f7a9-32f5-9976-083e3099e856 | -17.8292 | -57.31829 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 90943a59-27a4-376d-9292-f37502205c48 | -17.82837 | -57.32288 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 255ec7d5-ee0e-3b4f-aa6b-a2655e338d45 | -17.82755 | -57.37035 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 30a4b222-8770-34c1-a83e-5a38e06207d4 | -17.82673 | -57.37497 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0c7f0b88-583f-34af-bf57-c4df4c27e8e1 | -17.9131 | -57.32035 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c0a3a6d0-e728-3eb3-849d-0da635cab992 | -17.90569 | -57.31891 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f763f915-746f-3eac-baf6-0f7d99df9c3a | -17.89909 | -57.31289 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e25a2a5e-7513-3508-943a-d782413ec407 | -17.82838 | -57.36574 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4bbb8cf9-56c6-3262-80c3-e385ef595c66 | -17.82755 | -57.32747 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2b5ee220-cf0f-3e2c-991e-70c7cd728b61 | -17.0524 | -57.36985 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ae7eb688-3028-394f-acd6-a5c166c3747f | -17.05158 | -57.37456 | 2024-10-14 04:49:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 82c61795-de02-361d-a691-86ce909e089a | -17.98448 | -57.35534 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| dcc22a39-d436-33cd-bf32-a3137c1fda8b | -17.98367 | -57.35994 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| c242b759-7cfd-3f3b-8914-608a1c1b3eb4 | -17.97915 | -57.36382 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 25bcac47-1647-3aba-82a8-47405bc54c10 | -17.96885 | -57.35705 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 09a10894-2504-3a4f-b458-4ee803a3c5e1 | -17.96433 | -57.36093 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 633b75fb-c4ea-3aee-8020-336a1aa3196a | -17.96062 | -57.36021 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 2241b951-2397-3397-8048-2ba383b47606 | -17.94498 | -57.36192 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 3e933736-4073-3eb2-aeb0-b38105d171e9 | -17.93756 | -57.36047 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.8 |
| eef4446d-6f75-37f1-9003-5bad53b3a6bd | -17.93303 | -57.36433 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 984be3b3-6192-3547-803c-40651d4f871b | -17.98401 | -57.33627 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1b77ec96-a4a2-3c16-8d6d-82d63515860c | -17.98321 | -57.34086 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d7361607-73e4-3fea-bef2-a4aa8c2b64eb | -17.98159 | -57.35003 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 677.9 |
| 03de1cbf-6c59-36c9-ba0b-30da83f3832d | -17.98112 | -57.33097 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 36d45d20-89e9-3759-ba80-f073052f20e8 | -17.98078 | -57.35461 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 5d1ab5dc-3d6d-3005-befe-9ae9a6e65f5b | -17.98031 | -57.33554 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3d802ed4-6751-361d-8970-10b7b30bd2db | -17.9795 | -57.34013 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7e5daccc-1816-31b4-bafd-39ff703d73ac | -17.97869 | -57.34472 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 2f1d0881-33ff-3aeb-bf69-540f2da6c509 | -17.97788 | -57.34931 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 36cd9667-8b9e-3068-9376-e16afe2f5643 | -17.97707 | -57.35389 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| c124892b-2217-3541-98d5-169772a8b704 | -17.97661 | -57.33483 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 91415e10-4fb0-3a3b-9220-615b1b321bd5 | -17.97626 | -57.35849 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 64f0d861-3b00-39b6-946d-4454f34075ba | -17.9758 | -57.33941 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 286b85e7-9e79-339d-8b13-9f2a1bea7db7 | -17.97499 | -57.344 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 9a563e55-2741-3f84-a24e-6b0d93e6f30d | -17.97418 | -57.34858 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.7 |
| 9a9ea937-740c-39e0-a544-41877de6e55a | -17.97337 | -57.35317 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 15c5e6a5-b072-3d41-9628-d3b5f2e8442f | -17.97256 | -57.35778 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 30cf7add-199d-3a16-a442-f0e5c422beea | -17.9721 | -57.33869 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ce54c7e3-c1d6-38ec-a627-1f1dd287645e | -17.97174 | -57.36237 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e96be300-80f5-3a7d-9f72-e6473ea21656 | -17.97129 | -57.34327 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| dbee1aa5-e2f7-3bf2-9353-eed8284c23cf | -17.97048 | -57.34786 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 45225d3d-abdd-3506-afb0-2e2b14e7b68c | -17.96966 | -57.35245 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| bcc2ecce-f279-3a9e-89e0-3c28800048b3 | -17.9684 | -57.33797 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 702ae193-d9b9-3bef-9697-9505457062ee | -17.96804 | -57.36165 | 2024-10-14 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |


[Clique aqui para ver as próximas entradas](README94.md)
