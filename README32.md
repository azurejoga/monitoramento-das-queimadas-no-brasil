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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0de34fb5-ba5a-3757-8545-673a46644ed8 | -1.27341 | -52.98488 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70934dae-2e62-34db-bb6b-2c11610665cf | -2.66063 | -46.15987 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3613a311-0924-3839-81f4-6c73e2e139b1 | -1.69879 | -46.16451 | 2024-11-22 04:36:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76a0a18d-556f-38f6-9387-aa618d0ddfe3 | -4.13656 | -54.66293 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ae999c7d-3007-3218-a71a-b2f88dc04b0f | -3.1004 | -53.21111 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c74a5c1-8e2f-3d0f-a734-09f4e3da05e4 | -3.09958 | -53.21609 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cc87771-6ef1-3827-af70-73a2f92a4e2a | -2.50772 | -54.15642 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 60181fed-2f34-30d1-946e-641f7137494b | -2.72872 | -46.09846 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94a86d86-afc6-34da-8e9b-20a70ee7ae18 | -3.1816 | -54.32775 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 015be4b0-7e69-3357-a28f-96d8f653a1ac | -4.97482 | -49.82635 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f9af860-59b9-312e-8880-b1755f5947df | -2.69175 | -46.19923 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c90d3e15-cf5a-3404-9fb1-893f8db88e29 | -3.27012 | -53.83041 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61239b7c-3db2-3136-9c33-27d4112d863c | -2.65775 | -46.1555 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca55153d-3ac0-3d51-a1fc-a00473f61dec | -4.11796 | -54.59251 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9066efcc-741c-3fe1-b3ac-cf3a5e9811ad | -3.53274 | -51.10491 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ee807aa-5cc8-3538-9508-a213973f7234 | -3.21135 | -54.24964 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2aa7413b-91ff-3596-979f-9efa8c32425f | -1.31074 | -47.80771 | 2024-11-22 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 577909d2-8220-3b45-8d60-fa4332b4ae13 | -0.80745 | -51.79259 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d9872331-46e4-36a8-8bc1-19ae93a6092c | -2.19883 | -53.6749 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc9a5630-88c4-3d37-8570-7a574687d4aa | -4.57902 | -48.0203 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2a7190a-c1ab-3786-9b24-abc66df48e1f | -1.72162 | -52.71061 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e4b9748b-d5af-3dd2-96b0-697930cb2c09 | -1.14225 | -51.68409 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6ca2b8b-2249-3bdd-b460-ea832fd19ab6 | -2.22317 | -50.39235 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bae0167-96db-3de5-94d7-cdb61e4ecf42 | -1.96744 | -48.38497 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d89f506-27d0-34de-9a86-9bfcbf35a842 | -5.92923 | -43.78227 | 2024-11-22 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49cb2d31-ce38-3b52-aef7-93c0675f0509 | -1.43422 | -52.67984 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3efe5015-5191-3852-a34e-ad092efe66f3 | -1.96414 | -48.38446 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77365c9b-02f1-38d8-b9ff-bc8fa42ed527 | -1.6472 | -52.15342 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 952f5959-86f6-3aa8-b005-39eceeac588c | -4.24005 | -41.93034 | 2024-11-22 04:36:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9affb627-9bcd-312d-9fff-3b47c9e4154d | -4.40797 | -44.11641 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad7736fa-99a5-32e1-a447-283281b27d53 | -1.58189 | -51.27298 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02b8aec8-4f44-3c3e-9392-2f9665616f51 | -2.20857 | -50.77094 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e84ec8ff-2f2f-3b6e-ae4b-4379f5d522b2 | -4.61715 | -45.81434 | 2024-11-22 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 633d02cc-a1a0-3923-98fb-62c6d684a280 | -2.49263 | -48.99914 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 052f78ed-a9d8-3aa6-aac4-3a44e40316d7 | -3.46121 | -45.90204 | 2024-11-22 04:36:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ececbe9d-9782-3b45-b9e5-fbebdb5bacff | -1.14242 | -53.40007 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb7e3a4c-b10a-321c-99f2-f43168438f75 | -4.96155 | -49.84566 | 2024-11-22 04:36:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0cd73a0-ec85-3dc9-b160-b8cc141785c7 | -1.85429 | -46.69899 | 2024-11-22 04:36:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0a4a8f7-c9d9-3b61-87c6-6bc417c10ab2 | -4.28687 | -48.21835 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d4a620b-10a0-3475-ace9-01c25d91dc43 | -3.55972 | -54.2221 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9d8b41cd-92ff-3d2f-a0e8-b0aad39da9d8 | -3.5113 | -53.80737 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee307beb-e3d8-33f5-9a64-47e41756dad2 | -4.57624 | -48.01628 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ee1ea63-2d0e-3952-9df1-f3c7792d40f5 | -5.49688 | -49.51097 | 2024-11-22 04:36:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64c4c4a8-d4a0-37ea-9575-317104839bd9 | -1.62444 | -52.4166 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0a9dfe3-ae90-3a03-9f4a-ede7102fa257 | -3.85473 | -52.35508 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3124017d-e409-3ca3-802a-c8dae8fc8395 | -1.98754 | -53.13911 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 758f41ad-6353-34ad-a310-b1d96b650f73 | -2.95776 | -51.4108 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17021fc9-a4f6-34c6-8c4f-c3aa55380c20 | -3.27755 | -48.80567 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9030249d-7e7b-3f28-881f-60fcfd607541 | -1.47904 | -51.96641 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9987b2d-b919-30bb-a559-2cbb22502de6 | -2.25125 | -46.87413 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 864986db-9de9-38d5-bc73-f9abaf4bdd41 | -4.68423 | -40.69243 | 2024-11-22 04:36:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 99123f80-a91e-3147-b0f8-7feef72c9b0c | -0.9376 | -51.71955 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7975f5b-4a39-39b8-973e-1b02be77f950 | -1.58767 | -54.70641 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e93f04a-ff92-30f1-94a7-a45fef90037f | -3.28409 | -53.84718 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c2c4ff8-465e-3824-b176-0ae349bef798 | -2.4987 | -49.00362 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdbd10d6-a36f-305c-95c7-99f625f19ffd | -2.41398 | -46.02834 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 738cb5f4-8fdd-3a2a-b695-302526c69b2c | -1.67718 | -54.99586 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 299f6034-f786-30ea-898e-89bd495aacb1 | -3.21847 | -53.84065 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f83c936a-699a-330a-aa2b-ce7876d30b31 | -2.69063 | -46.18339 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12a0b2b4-5ee4-3893-9241-9b0d2f070fb1 | -0.79732 | -48.60976 | 2024-11-22 04:36:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5addcbf0-22f8-3619-9a0c-3e3ed2799252 | -1.26015 | -53.36774 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75387350-a6db-3f6c-b827-5f8f1a29af7a | -2.62994 | -46.84654 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 376bbe22-bb44-3ba7-878e-88a0fe489c4e | -3.52045 | -53.80186 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f36b015-963f-3fe6-a093-2e67d829f30c | -3.80312 | -51.99542 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80bd0147-66f3-38cb-a7ea-ed1c61ffd5ca | -3.10544 | -53.9979 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c5c3870-a2e5-3a6d-b942-92e635846abd | -3.24384 | -54.24271 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3c905961-f5f8-3c3a-a3e2-f1bb0d6bd6dd | -1.6199 | -52.42064 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ef070e0-1d25-3977-b902-c0da2b7ef65f | -1.77716 | -53.62774 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c895238-8d2c-3d67-8c78-112824ff104c | -4.37562 | -46.28159 | 2024-11-22 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf4045ab-9ec9-3b23-8f36-ce6964714607 | -0.92306 | -51.7395 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50dede42-6422-3199-8f19-80144b17e22a | -1.19339 | -51.95428 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff232454-4c55-3899-ac1b-fc72c949a447 | -2.21995 | -53.72672 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 193575a5-efcf-3809-820b-d1b66a3b87df | -4.1267 | -50.41847 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ed892b3-5622-37c2-9236-483a94e9734a | -1.59243 | -53.8145 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 900a5367-b73e-3390-8ddc-928a02a2c224 | -2.23683 | -50.08381 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 562c09f3-56d4-33a0-b6e0-51158aee37e2 | -2.24272 | -50.46762 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e94da16b-9821-3fbc-a68b-37bc82a2da2b | -2.49019 | -49.14382 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a703ffb-21c6-37ee-a469-cb902cb27549 | -1.80144 | -48.77119 | 2024-11-22 04:36:00 | NOAA-20 | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5369da99-cd18-3c1f-9ee2-084a1a00d2ba | -2.67426 | -46.24353 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b58aaca-24fc-31ba-b659-477c4e341788 | -3.24256 | -54.25045 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| f44c3952-66ba-3756-858e-a7214f73e471 | -2.8979 | -53.04842 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7185d73c-67d0-30de-9bc9-b6b7b0d6fe70 | -2.70795 | -48.66671 | 2024-11-22 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02aefe68-a896-334f-94d6-f89f5d904279 | -1.98504 | -51.51602 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef940ddf-887a-3f95-9926-e70612f6272b | -4.19925 | -53.497 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2cef7c5-75e1-39a5-ab5f-fed1e0f34594 | -3.26606 | -53.82977 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fe51860-3652-3240-889f-2016c2324cd6 | -2.55722 | -46.54973 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59d26683-4e25-34fa-9dfc-28a0e86ce1f2 | -4.28796 | -48.21141 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc953b17-f86c-3d26-9bca-cdafebffd4d9 | -3.96646 | -46.72527 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad07fdac-11da-3dc6-91ce-8ccef1038fdc | -3.8893 | -46.66005 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d24497-e885-3847-a613-51ae0a62f908 | -2.62654 | -46.84606 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d359ac03-7f95-3613-a279-781cf8952445 | -3.6961 | -51.27632 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76906a7d-7f37-3c40-bdb8-6c4abe2fbc86 | -2.23437 | -49.88067 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34ff347a-4d89-398d-baf7-76ecba628f64 | -1.73416 | -52.38418 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6600910-df6e-3477-a89b-bb5f0cd66ae0 | -2.60279 | -46.2568 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f693aa-20d7-39db-83cc-963f385c2d12 | -2.14788 | -50.27149 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ea59ba9-12aa-3389-8e90-395a7d4f0e66 | -3.51072 | -53.81099 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 378d150c-c6c1-33c9-b820-f4f6880c6fda | -1.61368 | -52.60778 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28819f34-03c5-30c7-83a1-b5ea447e5741 | -0.04804 | -51.74541 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da0caa04-5ba4-3fb3-8653-44745225c0cc | -1.2636 | -51.60097 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e43f435a-40fb-3a78-9179-94086180a704 | -1.46053 | -52.66434 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README33.md)
