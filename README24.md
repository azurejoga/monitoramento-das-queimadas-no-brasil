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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e10028a-9a89-39d7-aac6-a8722bfd64fc | -13.39969 | -47.92942 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 323ed0d4-122d-32ce-b2b0-1fe21b0df6d0 | -14.57894 | -48.22867 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6752f4f-5b58-3b57-ad3f-d25911a79f87 | -15.72489 | -41.77626 | 2025-09-29 03:49:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e323ec51-c80a-3827-83cb-13f790273b13 | -12.93364 | -46.77181 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae1533c0-d326-33c1-97a8-5cf5537f0943 | -19.8599 | -43.80257 | 2025-09-29 03:49:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 292c39ed-1932-36e5-bfbe-ed3f1180655c | -13.7902 | -47.86988 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06bc438f-6728-3651-a612-9b753167751a | -12.92093 | -47.15908 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7cdd38-8f8c-3b82-a399-205241b39a97 | -15.24613 | -40.44154 | 2025-09-29 03:49:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4120fa1e-3c05-3f2f-9d9e-666db8199bb3 | -14.57325 | -48.23757 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f9786ef-fecf-3963-9061-2ea0a5938360 | -14.56414 | -48.28074 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8baec0f-88bf-38c7-a451-53a219b3d1b9 | -13.77867 | -47.86631 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1beadc2d-b273-3e91-b550-41bab423a983 | -15.53157 | -44.32896 | 2025-09-29 03:49:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5ee141cd-1f0c-3c40-a95a-8ccb1d6ad8f3 | -14.70527 | -45.20839 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5844513d-01a6-318f-8fca-f93d1c3d9e80 | -12.97091 | -46.2427 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d420f51-fbf3-32fc-a34e-e892e4672fd5 | -14.52568 | -48.4035 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 659893b3-796f-3d40-aacf-6139265853b7 | -12.84988 | -46.88633 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0edcb9c-d8c7-3909-8f78-c574d439f1fd | -13.81945 | -47.4835 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ee8523f-ea5c-38c3-8578-896c49782b60 | -15.04649 | -46.97403 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 65dec0ac-7eec-33a6-9bca-79269813a23b | -13.78953 | -47.87319 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3885417c-88f4-336e-a8f9-5861a6efb575 | -13.1802 | -47.4501 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6e8be575-e49a-3314-95ba-da0487899a14 | -25.00536 | -49.38484 | 2025-09-29 03:49:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b036e88c-4abe-3bf9-8bf6-9f995a5adda7 | -13.22625 | -50.95441 | 2025-09-29 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cbacd1c5-30fe-3ca5-98f3-d3c2600ef03e | -14.67568 | -48.15983 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7bd5db5-3736-359e-9d01-1913bc971e7d | -13.58167 | -47.29273 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d82ffa5e-2512-3d7c-beef-79a1f4615ff8 | -14.74912 | -45.67476 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca118385-ae35-3d77-bea3-ece056e1d783 | -14.49598 | -48.54304 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c0d5288-b4cb-3ba4-98c5-dda772970268 | -22.08505 | -46.83592 | 2025-09-29 03:49:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 881c182f-f159-3fef-a743-d5795536013f | -13.01789 | -49.45913 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36a49935-1d7d-3334-9480-f1fedab92e02 | -13.83702 | -47.48588 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 609c6d28-7668-39c3-9a81-e18bd7b7612f | -13.35419 | -47.29545 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 451c8227-cbbc-3cd7-9f18-9f653d43e60e | -13.22823 | -50.96341 | 2025-09-29 03:49:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1030a478-3d1d-3436-8378-cd99ca4d8a3b | -14.56608 | -48.26147 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83800104-b657-36d9-a7b6-7402d29ad0fd | -19.31059 | -48.91852 | 2025-09-29 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81628ce4-e98a-3d1f-8d06-d5bfe96c6c22 | -14.58991 | -45.00967 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 294574b4-5328-3e43-a1d2-19370f2efd06 | -13.39473 | -47.92342 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03111a84-b26d-39ea-96dd-30f369047f68 | -14.61809 | -48.28957 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ac59169-4406-37cf-9288-6bd00629e442 | -12.90076 | -47.11134 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4dc382e-522c-3aad-8871-13ab6a15f038 | -14.53231 | -48.42672 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad8f6ab6-60b7-360f-b17f-7160060bc5e4 | -14.5308 | -48.4036 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e862cc4-ca6d-3d72-a5c6-8116ab265fe0 | -13.80012 | -47.95719 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fb5847b-b58b-3e74-92ad-1cf797ac1ebd | -13.00748 | -49.43262 | 2025-09-29 03:49:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54c1a5b0-09c3-36ad-b84a-19ddf1c635c7 | -14.5724 | -48.2416 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 447b3b69-b457-3ee3-86ab-624e4a2334bf | -22.08978 | -46.83689 | 2025-09-29 03:49:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cabb907-dc30-3412-8cb3-39ea012e1f36 | -13.63202 | -47.31435 | 2025-09-29 03:49:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37720282-88fb-3af2-a080-1c0b3094e3c0 | -14.59368 | -45.01606 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b74d6efc-a744-3fc2-a87a-fa653d881f77 | -14.84139 | -45.56974 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bc61a38-dd73-3574-a9f4-2e40f666f8f0 | -15.03718 | -46.96428 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fb679f6-a575-3431-b4c3-22119ced4af2 | -14.68157 | -48.16106 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c68b390-9403-351a-b120-8d53a4f38cd0 | -21.55564 | -41.25667 | 2025-09-29 03:49:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f808816d-acb2-3128-ac62-b5baac1ad592 | -20.20607 | -41.38583 | 2025-09-29 03:49:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f0631725-5a40-325a-9b06-94a059e52d48 | -13.5684 | -47.3064 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e6477dc-acd6-3ab5-a4ea-4cb8fc70c051 | -15.0584 | -45.05788 | 2025-09-29 03:49:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67ed6360-7a94-37a0-9bea-ccaa4e09ab9a | -14.6795 | -48.15864 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9c0f41d-a211-3150-8d98-bb258149d852 | -14.77478 | -40.09322 | 2025-09-29 03:49:00 | NPP-375D | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c28c6c1-4e4f-3e19-9cf4-6cdc6d269001 | -12.77157 | -46.85446 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50630bd7-b735-34bb-9bc2-62fdbe9ac776 | -15.2454 | -40.44582 | 2025-09-29 03:49:00 | NPP-375D | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 356a77b5-6bf3-3d13-a984-c8674306dddc | -14.55063 | -48.40376 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0530b58-d9e1-3131-a732-6c7a9b70f108 | -14.51798 | -48.40519 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc1a725c-bf83-3f20-9949-b66da18c9ef6 | -13.38502 | -48.15547 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 427ef396-c971-34a0-8382-c721414c3778 | -12.91606 | -47.1537 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4d9cb8a-d153-3de2-b67b-41f5ea781cda | -14.67457 | -48.15295 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b1e6a83-7197-3111-815a-abca7f404051 | -13.57657 | -47.29548 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f45e9b26-d21d-3ee3-ab29-e4c16660949d | -15.04131 | -46.97044 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2410528-7605-306a-b2c5-00ce3a47f8b0 | -13.6152 | -47.30958 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e541d4-159e-305c-a084-41a7ee5375b5 | -14.56526 | -44.98207 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0572390d-5e4e-3092-a8e0-99d4f05bffe7 | -14.67665 | -48.15511 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a8cd247-538d-3856-ac0e-5d07bcdc84f7 | -12.97823 | -46.26255 | 2025-09-29 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcf603ec-6b27-3775-a78a-77ed87cc178a | -14.4677 | -42.17301 | 2025-09-29 03:49:00 | NPP-375D | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ec6220be-fc02-3356-813c-8c570e113a62 | -12.88962 | -46.99043 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b75fd339-8405-3e1e-a35e-919a5f0fe316 | -23.4167 | -49.46119 | 2025-09-29 03:49:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30750249-3505-3593-a00e-5d7cb22b5c88 | -15.43069 | -39.47831 | 2025-09-29 03:49:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| da3b42fa-2727-327d-9601-cc69d2c27cbc | -12.86335 | -46.96664 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85d799d8-d9fd-35ff-816e-88248a663dca | -19.30501 | -48.91692 | 2025-09-29 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da124fa2-7b70-3db2-adfd-0339410e5e2c | -15.15665 | -46.41351 | 2025-09-29 03:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ece5694-38f1-3a2b-96f1-eb29fd4630e2 | -14.52493 | -48.40177 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f06e3e7-aeaf-3b8b-9b0e-988d99d699f6 | -13.83645 | -47.48803 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09309a07-5de7-3abf-8786-96884199828a | -20.14661 | -46.3852 | 2025-09-29 03:49:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ea6457f-7b72-3ffb-8ecd-59178c4602c7 | -14.4427 | -44.88263 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64383d53-12ce-369f-9c6d-078d6358653a | -22.03273 | -46.4917 | 2025-09-29 03:49:00 | NPP-375D | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71ab6958-63e9-3501-97d7-f923c4d5e37a | -15.04672 | -46.97165 | 2025-09-29 03:49:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86f03230-93be-3432-8f7f-2522bfcdfcda | -13.79967 | -47.89979 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9986548-b5b7-3ae2-a054-3183cc7253ff | -13.64126 | -47.32738 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5e67f20-df28-30e4-8077-b7abe18e05b5 | -15.05941 | -42.33812 | 2025-09-29 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d83927c4-43af-398a-aa92-3e0e0894f8a3 | -15.79304 | -42.20024 | 2025-09-29 03:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fc9dd6a5-1752-3847-afda-5c46c7b40bf5 | -22.08868 | -46.84222 | 2025-09-29 03:49:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06f3c5ca-7772-3a74-8326-1adce8cc5060 | -19.99195 | -43.96232 | 2025-09-29 03:49:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 703721a7-faaf-37eb-800c-5b0709292032 | -14.52097 | -48.39623 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f29c1d2-abe1-31fb-827c-7efda4b844c2 | -20.5398 | -45.10175 | 2025-09-29 03:49:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 448c306f-bd7a-319b-9929-e5f8195c8770 | -12.76095 | -46.84907 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 047d7e4f-d71a-33b7-a877-f3b4c9c05d5f | -14.83643 | -45.5686 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbbcffc8-7c85-3e8a-92a2-118b070ca96c | -12.89756 | -47.09771 | 2025-09-29 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5ced2c5-6c53-32ec-9a05-116842741a15 | -15.05488 | -42.34052 | 2025-09-29 03:49:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| e36fa97b-e9c7-3929-b39a-3d9969b80119 | -14.75411 | -45.67596 | 2025-09-29 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59873538-8dff-3f7a-b8ef-80855f39611b | -14.52011 | -48.39478 | 2025-09-29 03:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 890a6a82-7ca4-3e33-9269-83efa7d60fd9 | -13.38662 | -48.15344 | 2025-09-29 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 82cffd38-f898-3028-9155-9433f2d57ded | -13.35798 | -47.30643 | 2025-09-29 03:49:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6eb1bae3-beef-3bc9-b6b6-20d1c396d30a | -13.80989 | -47.90982 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c61476c3-ab9b-376d-a6be-c1717fa0e12b | -13.7677 | -47.92093 | 2025-09-29 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f6732a-9f99-3269-8ea3-72838c8b038a | -13.76603 | -43.98016 | 2025-09-29 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d674ac2c-adf1-33bc-b089-67d46844bc1d | -14.28428 | -49.40074 | 2025-09-29 03:49:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README25.md)
