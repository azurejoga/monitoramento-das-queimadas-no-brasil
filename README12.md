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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f197343-6515-3867-baef-e4e4defed9cf | -8.163 | -43.229 | 2025-12-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| deba8d6f-f435-3d88-9bcf-072416b7e965 | -8.0516 | -43.0765 | 2025-12-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 71806879-79bf-3998-90c1-19dade9a42ec | -8.1633 | -43.2055 | 2025-12-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 7e782883-3fb3-3db0-a15f-48dd4474286c | -8.051 | -43.1237 | 2025-12-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| c6ab18cb-a492-34ab-8b24-a28a7fe8d234 | -8.0513 | -43.1001 | 2025-12-02 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.5 |
| a4d3fa5d-736f-3a94-ba7e-78958c234662 | -8.0324 | -43.1022 | 2025-12-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| cb369c5b-b99d-3170-85b8-c2ab81340828 | -8.0513 | -43.1001 | 2025-12-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 194.9 |
| d1b5b44c-e6ae-308c-8fe1-b609a581ac39 | -8.163 | -43.229 | 2025-12-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 0a0e4121-f422-3c35-91e2-9b4692d83b6a | -8.0703 | -43.0981 | 2025-12-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 083e7af1-5335-31e2-ae90-39703f24e658 | -8.1633 | -43.2055 | 2025-12-02 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 49344cc5-620f-3d5b-876e-a1f1d1ea063e | -8.0513 | -43.1001 | 2025-12-02 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.2 |
| 7071be20-fc4a-35a9-8f10-4ac02afe35fb | -8.1633 | -43.2055 | 2025-12-02 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 80627a42-781f-3a68-a13c-68ba7bab8ac8 | -8.163 | -43.229 | 2025-12-02 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 53e7340a-4ffb-32ef-bb21-83813bcde017 | -2.25962 | -53.71205 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0c5bfd-6304-32c1-bf13-a07aee848855 | -2.71673 | -49.53563 | 2025-12-02 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eff0d028-c607-3f05-b31e-0b7242001006 | -1.14888 | -53.59347 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6a83970-a4f1-3841-8a27-aac541abb731 | -0.79264 | -52.41529 | 2025-12-02 04:55:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bd75d09-5650-3d97-a583-95748b52e204 | -1.21434 | -53.37091 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b35bf63f-efb1-349b-addd-cdcfa7aa5d4a | -2.47372 | -47.03608 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67bd6cdb-1667-3f4d-829f-36f1c1ffcfc4 | -1.6903 | -45.79877 | 2025-12-02 04:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b02c9e4e-0e79-33a1-a23f-cde443d05ea5 | -2.03387 | -47.1516 | 2025-12-02 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19adea5c-d7c4-32ff-8743-7e7c2154ac3e | -1.93386 | -52.1193 | 2025-12-02 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44a695fa-9098-3ed9-919b-344457a519ae | -0.96451 | -53.77013 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40687256-6fd6-3af1-a60f-0c46702f8aa9 | -2.44841 | -47.08401 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2ada170-b4ce-3c49-b744-b63516e9ebae | -2.93278 | -51.84708 | 2025-12-02 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdf46891-88ce-31ec-9a05-4bcd33701e12 | 3.53714 | -51.44889 | 2025-12-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cffaf70-0916-3cdf-b619-0638085abe86 | 2.36124 | -51.6344 | 2025-12-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2379e684-cbf9-32b9-9b35-246111296b21 | -2.44404 | -47.08332 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78bfbf13-f0c1-3ed5-ad9f-c9a4ddbc79d0 | 2.17524 | -50.88493 | 2025-12-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f28d1d9-a264-31cd-a046-5adacb887808 | -1.68895 | -45.79734 | 2025-12-02 04:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61c95d88-da2b-354d-84d8-cdea8dfc2063 | -3.23998 | -45.56711 | 2025-12-02 04:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| db61c37b-5ae6-373a-ac1d-769592b49ece | -3.25744 | -45.56486 | 2025-12-02 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c494baa2-4776-3800-9c5f-1aba4f256ce6 | 1.5566 | -50.79692 | 2025-12-02 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87d80dc9-a985-3338-88e6-2c2d1577f8af | 1.55716 | -50.80053 | 2025-12-02 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 381d6816-7216-3cd5-8019-58ef6c90001b | 2.01578 | -55.71751 | 2025-12-02 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d1c8166-3a83-3f78-ae32-a07d60ce780f | -2.46857 | -48.11534 | 2025-12-02 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ce3cc89-5203-3dad-a03f-3a56629e18a8 | -1.35501 | -47.40838 | 2025-12-02 04:55:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 239bac69-65cc-3408-82ba-6a5cd761511b | -2.69718 | -51.89562 | 2025-12-02 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63780d88-4313-3ee8-9698-d5c8aa137d13 | -2.68537 | -51.86072 | 2025-12-02 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1fae716-313f-32c1-a62d-8ddee764d93e | -0.69999 | -51.98511 | 2025-12-02 04:55:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| baeb47d8-39dc-36d9-89c6-a9e9c954cc72 | -0.84311 | -47.41094 | 2025-12-02 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01c20967-a3b7-32f2-a9bd-7804ab5008c9 | -3.25333 | -45.55854 | 2025-12-02 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9acdf11e-7563-30ea-9df8-3a04e369f6a3 | -1.28957 | -53.17165 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea42e807-5111-32db-96d4-04cee69ca879 | -2.47148 | -54.16052 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 441bb0ca-b0ec-3bd2-b46a-c5c616a4827f | -2.02955 | -47.15092 | 2025-12-02 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03939d4e-a91b-3b74-91ef-ea8eaa38ec60 | -1.68559 | -45.798 | 2025-12-02 04:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50dab84a-771d-31d8-83ae-561c97ad2391 | -2.045 | -52.104 | 2025-12-02 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e3060749-103c-3f4e-bfae-1f46066328e6 | 3.47714 | -51.26348 | 2025-12-02 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e99229b-cf43-3b94-9270-96957f6236a9 | -2.71345 | -53.18145 | 2025-12-02 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9a7a065-fe35-352b-93ed-83adf87360e8 | -3.39293 | -47.18536 | 2025-12-02 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 787f3c25-a2fa-386a-93f8-a0d60745a56e | -4.04421 | -42.35743 | 2025-12-02 04:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 90784c06-1b8c-3677-abf2-5aa7ff761969 | -1.48491 | -45.79441 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8e6a1279-097d-3892-bcd0-b675f5bbba36 | 1.06497 | -50.88001 | 2025-12-02 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93342a2d-4e6e-327f-81f9-92a3d5da5d5f | 2.0151 | -55.71316 | 2025-12-02 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be7bbf7c-e3ba-3694-a3e8-57d93b3f3297 | 2.00713 | -55.71007 | 2025-12-02 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f913f1c4-4d7f-3718-87ba-fc71221e5982 | -1.47954 | -45.78592 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12653f77-e839-32e5-a958-0102b5d35c2f | -2.47309 | -47.83324 | 2025-12-02 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a58b137-c0bf-34c3-bb30-382a68b1e0f4 | -1.60073 | -53.37867 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bb6f089-81c7-3fad-96fb-c1ef6ac25260 | -2.53867 | -47.31587 | 2025-12-02 04:55:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc162497-e222-3e82-9b3a-bfc13fb946a0 | -0.70054 | -51.98162 | 2025-12-02 04:55:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c3af71-21e0-3b9c-b399-245c5bacbd31 | -0.96838 | -53.76716 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c98a9ba7-5e50-31c1-bcb4-be057674d1a8 | -1.11437 | -52.40211 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f46ca3-d269-3dc8-9870-36835d335f2b | -3.2378 | -45.56171 | 2025-12-02 04:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70931bc7-93d8-3ae2-9d39-83db10868e0d | -1.1341 | -53.64424 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c45cd32-eac6-3c06-85f0-340180ef5aa8 | -1.3556 | -47.40451 | 2025-12-02 04:55:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e12fce4-91f7-3a26-a303-d6c8be3a624d | -3.26235 | -45.56563 | 2025-12-02 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77d59e86-9d15-3e27-8846-617be4000282 | -1.53549 | -47.21821 | 2025-12-02 04:55:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb2d1994-5fa6-3155-86d6-d669ed6d716d | -1.48565 | -45.78946 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3343e94d-82f5-3bd2-8f0d-0ab39e832a4c | -3.53381 | -45.79324 | 2025-12-02 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 91f6e793-262d-3982-a161-829a2c384fd1 | -3.40941 | -42.45532 | 2025-12-02 04:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c0a465cb-557c-3822-aef5-8fba3f24eb12 | -3.24191 | -45.56804 | 2025-12-02 04:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 804d9a07-65a4-3ed4-8eb0-4228184cabf3 | -1.10919 | -47.34153 | 2025-12-02 04:55:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f99b11a3-6c47-34d0-b59c-2fc8180b76db | -1.28626 | -53.17114 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8e1adc7-6db1-3227-a9ea-e528d7f321d1 | -2.44905 | -47.07981 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4d35a1b-34ec-3779-af9b-e0d42c7e9145 | -0.96783 | -53.77065 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d2f8958-ad5c-38b9-afb6-f7c8e9ea1a63 | -2.70055 | -51.89614 | 2025-12-02 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e83abefb-196a-3d0a-8bee-4cf98c8e2d28 | -3.60194 | -47.26268 | 2025-12-02 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05df78bf-7b2c-318e-a3a2-a6fe96b9c863 | -1.15219 | -53.59398 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fe5f72c-923b-3579-a0ab-4aa138017eeb | -1.68974 | -45.79231 | 2025-12-02 04:55:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc3f7105-0ae4-3b71-a51a-ac7786b5c321 | -1.92439 | -48.29253 | 2025-12-02 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de7f7a2e-63f2-3895-8fab-198879713186 | -2.60128 | -51.93575 | 2025-12-02 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 674f84a4-1632-3a65-b955-42cccaebf048 | -1.19907 | -53.09781 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dad8046-1303-3a7d-be90-d3b2f389dbd9 | -2.25632 | -53.71154 | 2025-12-02 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88f43b63-7bd1-3e66-96c6-2cf745489553 | -3.38876 | -47.27225 | 2025-12-02 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 591c5f94-d312-3f2d-aaea-9e664994bbf7 | -0.83835 | -47.41411 | 2025-12-02 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7ddecfb-e13e-3ece-858d-314cf523a34f | -0.88488 | -48.79731 | 2025-12-02 04:55:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98f59070-7755-3309-a487-35087aa214ba | -2.70111 | -51.89256 | 2025-12-02 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6743e692-f263-3d5b-8e50-1f93947e6552 | -2.44469 | -47.07912 | 2025-12-02 04:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 885bc0bf-ff5a-3ec6-9ae5-63a0e2e8273b | -3.24404 | -45.5734 | 2025-12-02 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ed19a9a-96fe-3739-b9eb-cf0250ca3088 | 2.01145 | -55.71373 | 2025-12-02 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb92cc16-f595-3182-af42-ec68a1aa3998 | -0.99251 | -53.20283 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32f8d53a-007f-35a2-8bbb-0d1295afccc9 | 2.42406 | -51.40475 | 2025-12-02 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7ca3dec-49e9-3a65-b463-986e1aa3a92a | -2.44108 | -47.18929 | 2025-12-02 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed6f45f5-d2eb-3b23-bff4-7055cbc51d7c | -1.21104 | -53.37041 | 2025-12-02 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 628a6e44-327f-369f-b624-106a9a0b2f81 | -2.26311 | -51.88775 | 2025-12-02 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b0138f1-d07c-3b96-8500-a45b9eb51b4f | 0.81932 | -50.21009 | 2025-12-02 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf6eca6c-7c80-3bea-ae59-a844f19c8ebd | -0.86695 | -52.37383 | 2025-12-02 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06e48a01-8e3f-3557-a594-a46c00f4a370 | -3.25825 | -45.55933 | 2025-12-02 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9ab21871-f419-3458-8003-d135cb38e385 | -1.4802 | -45.7937 | 2025-12-02 04:55:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 9a73a7c7-ace1-37aa-84ec-5ce8cddad6b9 | -2.71291 | -53.18488 | 2025-12-02 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README13.md)
