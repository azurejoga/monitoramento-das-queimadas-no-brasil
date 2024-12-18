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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec524604-0fa4-3d49-a62c-4f4e0f4eca9c | -11.25674 | -39.23554 | 2024-12-18 04:27:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 20c81734-0360-3c41-aabb-c1a293274d1d | -13.32179 | -52.41589 | 2024-12-18 04:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f57f02-a8fc-3f6d-98b1-963547338a4e | -15.45185 | -51.80777 | 2024-12-18 04:27:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daae4f20-74ab-3fce-8544-4fc4016b3c58 | -12.41311 | -43.79919 | 2024-12-18 04:27:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24b2c6d5-493d-3875-86b5-bc18c82af9ff | -12.37337 | -44.29622 | 2024-12-18 04:27:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27e9b298-5c43-36cb-9ca7-bd97bc23aebe | -21.06966 | -48.76612 | 2024-12-18 04:29:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0d40c723-1a79-3587-be18-86322a59d478 | -20.15848 | -47.39733 | 2024-12-18 04:29:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ff7a270-3f12-3c0d-af20-905a4b3dab83 | -20.73257 | -54.42105 | 2024-12-18 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23bd3ff9-5001-3f57-a4da-4a031da73235 | -18.15192 | -54.63568 | 2024-12-18 04:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9cd2f5dd-0213-30d6-bea4-554f8bba0fc5 | -21.7897 | -55.99711 | 2024-12-18 04:29:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb125c83-67fd-311d-85d3-e7f9d21e088f | -20.7287 | -54.42021 | 2024-12-18 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1b25a42-010a-3d5d-9057-a31856a62829 | -22.54 | -48.813 | 2024-12-18 04:29:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a557492-676f-3b72-8f09-6d7d424e5254 | -18.36343 | -54.9839 | 2024-12-18 04:29:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c98cda5d-b31b-3e33-8171-bb20870842e0 | -20.73162 | -54.42617 | 2024-12-18 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 050b8691-1a4b-32e0-b757-95da152d28dc | -22.20145 | -53.15826 | 2024-12-18 04:29:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 24232416-f69e-3dda-8fc5-be18dfc8ac1d | -20.77368 | -49.84654 | 2024-12-18 04:29:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ce5a9a6b-16d5-3caf-8feb-0184c080a078 | -22.20502 | -53.15897 | 2024-12-18 04:29:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4fb73a26-563a-383b-bbd7-da7b84044bbb | -19.76587 | -50.95598 | 2024-12-18 04:29:00 | NPP-375D | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e507a37-2d8b-3ba6-b52e-c0848811c72a | -19.66895 | -49.14891 | 2024-12-18 04:29:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1fe45bc-94e8-35f7-b51b-9310135f1819 | -20.76485 | -46.76888 | 2024-12-18 04:29:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 07ab1f8e-21ff-3774-8b0c-da363bfebefa | -20.70559 | -55.32371 | 2024-12-18 04:29:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aca43604-4dbc-39b6-ac85-a34c40771842 | -21.0557 | -49.22854 | 2024-12-18 04:29:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2919438a-4646-3691-beca-2d434c8c2844 | -20.72775 | -54.42535 | 2024-12-18 04:29:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d4fdee31-b2e0-3c53-8ad2-484933d3cf6e | -21.78551 | -55.99625 | 2024-12-18 04:29:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bad4d5b6-a9dd-3536-8e2d-e9d355f875ca | -21.35343 | -48.62157 | 2024-12-18 04:29:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 779bd373-5608-3ec6-8342-b9f5fdff3cc7 | -21.1904 | -49.86165 | 2024-12-18 04:29:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8902113-0cd6-3b8a-976b-c83fd6560276 | -19.66837 | -49.15259 | 2024-12-18 04:29:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0406f3f-3d58-3cbc-b0ad-c9798533061e | -21.07023 | -48.76236 | 2024-12-18 04:29:00 | NPP-375D | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b885836e-44d1-309e-9c74-94fd21d2fcec | -21.37865 | -48.66111 | 2024-12-18 04:29:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7277d98-9687-379e-a836-18b85393c438 | -20.77975 | -49.85143 | 2024-12-18 04:29:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a517ee86-ac46-333d-bc61-1b6ad20b3cb7 | -21.33564 | -50.28836 | 2024-12-18 04:29:00 | NPP-375D | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7c6ee65f-fffe-3adb-9d7d-4375c0464fa5 | -19.06062 | -52.86109 | 2024-12-18 04:29:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9004977-0050-368c-b8f1-2b4de09a1886 | -19.06507 | -52.85736 | 2024-12-18 04:29:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10c6ed1f-0786-30aa-85f2-7639441e700e | -20.777 | -49.84714 | 2024-12-18 04:29:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9f974a10-ea3d-33ff-bc9e-964a5916b24d | -19.10221 | -50.37547 | 2024-12-18 04:29:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f9d8d0c3-39e5-3230-9c06-d6223a59d5cf | -21.32189 | -49.19321 | 2024-12-18 04:29:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1c4b596-b56d-36ed-be8f-6a91e4d2e797 | -21.5881 | -49.23435 | 2024-12-18 04:29:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0cbc4ee7-b039-3b0b-b6e5-dd1d3c3a4b64 | -19.06873 | -52.8581 | 2024-12-18 04:29:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f74cdb7-78fd-355d-a78e-13d12f7fce11 | -21.354 | -48.61776 | 2024-12-18 04:29:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dd621559-df7d-3cf9-8db9-ff41ae9ea73e | -20.15905 | -47.39339 | 2024-12-18 04:29:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35c27525-f93a-33dd-b346-f7addfc02dc2 | -20.70633 | -55.31977 | 2024-12-18 04:29:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b815fb1-87a2-373c-ae56-8ff2713b3f22 | -19.70885 | -49.86515 | 2024-12-18 04:29:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a370dc12-19a7-3f82-8ff6-17ee8023a153 | -21.82758 | -53.28243 | 2024-12-18 04:29:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5aefcca9-8a73-3cb7-91de-2ddaadae4732 | -20.51369 | -55.53318 | 2024-12-18 04:29:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad1cbee7-05cc-38ad-9d10-e5c89477691b | -19.06794 | -52.86258 | 2024-12-18 04:29:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 062d281a-a770-3d32-98c6-0bcf9ceef78e | -21.58753 | -49.2381 | 2024-12-18 04:29:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ccca3091-f103-3981-ad8d-c215f927d2f5 | -20.99672 | -51.79193 | 2024-12-18 04:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| efb2e02a-9d2f-3130-ac5d-87ac0d7b3a23 | -19.05697 | -52.86032 | 2024-12-18 04:29:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89f173f2-64fc-3529-b422-6646fd31e833 | -22.29585 | -49.71025 | 2024-12-18 04:29:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 04f18ed9-e052-32d4-ba89-976625cfb4d1 | -19.06428 | -52.86185 | 2024-12-18 04:29:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b6b6ed4-8721-39f1-b991-cfb124228492 | -21.05627 | -49.22483 | 2024-12-18 04:29:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dca73cd9-a1fb-3f17-b82a-a6f0b24eff24 | -4.9828 | -43.7401 | 2024-12-18 04:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 87d4f5ac-a5b2-301a-9dd6-6d6d588ba7f7 | -4.9832 | -43.6938 | 2024-12-18 04:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| c4c8b78d-1061-3835-b8d9-c69985729119 | -3.2503 | -46.8709 | 2024-12-18 04:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f404ca83-f73a-3f62-9bbd-eaa0eabe1b9a | -4.9643 | -43.7182 | 2024-12-18 04:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4cbced06-c54d-3a8b-a959-098855e6d322 | -4.983 | -43.7169 | 2024-12-18 04:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| a58ccb20-75f5-3698-be3e-da51588f27b0 | -22.06774 | -56.20337 | 2024-12-18 04:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7f30d30-a727-3104-9a53-1a984f5d4c0e | -23.71076 | -46.89351 | 2024-12-18 04:31:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c21f566-ad8d-38d7-9491-1de24b3dc548 | -23.63475 | -46.28615 | 2024-12-18 04:31:00 | NPP-375D | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| af63a022-bac1-3c99-a89c-3fad104d5ad7 | -23.71013 | -46.89815 | 2024-12-18 04:31:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0fb550f8-2c1c-3864-a938-05ab66414248 | -22.15433 | -55.28631 | 2024-12-18 04:31:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 051986bc-3eac-3b0c-845c-59a932c55606 | -22.07193 | -56.20441 | 2024-12-18 04:31:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 332438aa-44a1-3f90-89ee-3d435c70c5de | -29.85875 | -50.8147 | 2024-12-18 04:31:00 | NPP-375D | GLORINHA | RIO GRANDE DO SUL | Brasil | 4309050 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 93fff682-acbe-3aeb-b11c-ea08dc84a5d3 | -29.85949 | -50.81338 | 2024-12-18 04:31:00 | NPP-375D | GLORINHA | RIO GRANDE DO SUL | Brasil | 4309050 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9189018c-b211-3ca9-a0ee-cc5798a34294 | -23.39867 | -47.00883 | 2024-12-18 04:31:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 27c129d4-79d4-33de-91f6-c689602894de | -23.57625 | -54.7464 | 2024-12-18 04:31:00 | NPP-375D | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| acd9114b-873d-3729-a376-f15eff0f5827 | -23.59223 | -47.43744 | 2024-12-18 04:31:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4110d74a-fd17-372e-ba8e-93c49059376f | -23.63194 | -46.42574 | 2024-12-18 04:31:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d65ab97c-c23a-3122-bfd2-af5bdb97e711 | -23.70546 | -46.47794 | 2024-12-18 04:31:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b88729d-8edc-3291-94bd-069b5aac86cf | -30.14952 | -52.02401 | 2024-12-18 04:31:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 938e6cd3-a2f3-3948-a203-1ecf6677d4fc | -22.15036 | -55.28537 | 2024-12-18 04:31:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62f5d145-ae22-320d-b84c-12f2e11e4201 | -23.3987 | -47.00621 | 2024-12-18 04:31:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8fe77c46-320e-3b10-bcee-f87716021b9a | -23.52188 | -46.97376 | 2024-12-18 04:31:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e84a018a-644b-3b8f-9085-ba25edea6084 | -23.33765 | -46.77087 | 2024-12-18 04:31:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 19349ed9-d8c5-393d-9b73-58581ef47d76 | -22.15106 | -55.28799 | 2024-12-18 04:31:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 219dbb6a-77a6-39d5-81f0-84b7afc113e0 | -3.2503 | -46.8709 | 2024-12-18 04:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f344d629-af53-37c4-9877-6e51c57ceaaf | -2.70417 | -47.73149 | 2024-12-18 04:48:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8a0fe00-cf98-3fc0-b515-aa33fe1fe7db | -1.57392 | -46.0445 | 2024-12-18 04:48:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0605c93-4353-3df9-906f-77817f791fcd | -4.02629 | -46.90657 | 2024-12-18 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aa638e3-1196-3a8a-b63d-8c94fca07ccf | -2.45993 | -47.8294 | 2024-12-18 04:48:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc56454e-76bd-3fc8-96b7-632b236bdb00 | -0.12136 | -51.73704 | 2024-12-18 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb06d924-a16c-3279-8e29-7623cefc195c | -4.93401 | -45.09882 | 2024-12-18 04:48:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da867b81-deff-3871-baf5-823de6457cf3 | -1.54343 | -53.7323 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95db56a6-d8b6-3c80-9bbe-a20ad0dbb9d2 | -1.70067 | -45.78077 | 2024-12-18 04:48:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d103641-bb69-3e7a-9f08-e2ed9f546b9e | -4.96654 | -43.71897 | 2024-12-18 04:48:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8bad077-dbc0-3193-88cc-e35ae2ffd742 | -4.09757 | -46.8186 | 2024-12-18 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d2d6712-a3af-3843-8ce4-44aa3cfd9fcb | -1.57448 | -46.0408 | 2024-12-18 04:48:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b1c5c3-adea-39a5-9215-d820a89bb48d | -1.62053 | -45.85165 | 2024-12-18 04:48:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92bcf02f-2371-32d5-8b22-dcb67594f8b5 | -3.58749 | -53.71119 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99ef3333-6032-36ba-b64c-e4cdbefc3a4d | -3.02394 | -45.23805 | 2024-12-18 04:48:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5ba3b34f-585d-3136-bddd-e1b555b42472 | -3.87753 | -46.0752 | 2024-12-18 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83dc5d37-49d7-3803-a56e-170f659c5368 | -4.10265 | -46.67482 | 2024-12-18 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4778c36-f55f-3d86-9f9b-10cdc31685a2 | -4.03033 | -46.90715 | 2024-12-18 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ce08b1-05ca-3542-802d-7f5e93187223 | -1.54056 | -53.72797 | 2024-12-18 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a666f55a-42e1-30cf-a0ca-1deaa63f5271 | -4.18567 | -48.14042 | 2024-12-18 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a7ae1c2-3191-334a-a424-7ea91d0e4d64 | -1.70488 | -45.78141 | 2024-12-18 04:48:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5dc9f67b-7234-3f94-897a-f69225137435 | -6.0574 | -44.05008 | 2024-12-18 04:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee6081e1-a599-3fa7-af10-fb4ef2fb37d3 | -4.11026 | -48.12638 | 2024-12-18 04:48:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 494c780a-9163-37b4-9ba2-091b7e645381 | -2.69688 | -51.64713 | 2024-12-18 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ab64510-73e1-35cc-841c-522c7fb0a2d6 | -3.50048 | -53.94923 | 2024-12-18 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
