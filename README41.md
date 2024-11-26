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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b55875a8-0ab3-3933-af4f-5591957d93ad | -3.47063 | -47.68807 | 2024-11-26 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27373024-59fe-36bd-8ee2-867c4604b8d9 | -3.68408 | -50.22775 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| faaedf40-d688-3800-bb3e-c2f0741ceb02 | -3.24097 | -53.27722 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae1e5442-6d16-3902-9b17-4655222bf282 | -3.23039 | -53.93109 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 815ebe24-3664-3505-a36c-bf530293de29 | -2.58326 | -51.92366 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92a5dda1-23d7-3775-b264-99c5416672d7 | -3.44106 | -50.0167 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 597374e2-5555-3613-9875-d0a4d365ff29 | -3.23148 | -53.92409 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81f8c205-2e35-3a30-b853-80bfe36b5e4a | -3.97706 | -48.07883 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 146a6011-9d9c-3185-adc9-ad7df5edb791 | -2.18901 | -53.6625 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e191cf-7337-32b3-99bb-5dc5c9322c91 | -2.18115 | -53.26064 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a004a488-e3f9-34ba-8062-aa7307f48fbe | -2.58925 | -51.71926 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c62caa2-11d5-3726-8e0e-f27d55a71270 | -3.28972 | -53.6832 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ebef629-e875-36ca-922d-1ca3b9262cbe | -3.43944 | -54.07155 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8646219b-ffc3-3b6c-8b85-3ac70f849f60 | -3.33144 | -53.71484 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45927af0-afe4-3c8d-9419-e0da04859dfc | -5.76002 | -47.8171 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d45a011-474b-34fc-98d2-109bfc1ec993 | -3.97337 | -48.05116 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b78aac2-c097-3d24-90a4-b153722bf590 | -1.92556 | -53.35008 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5509ecf-3a30-3ac3-8917-5ecb5bfabaf5 | -3.2426 | -53.6321 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce29cc6c-a148-394a-8bb9-1396bea4bc4f | -3.17814 | -48.44503 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 003117fc-33d2-3545-ae34-5620a2af6419 | -3.28726 | -51.13122 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69417d90-4155-3c0f-bb56-665db5f38ee7 | -2.86594 | -51.5738 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17966d41-3d27-36d4-aad0-5f9d87ba828a | -3.97102 | -48.08768 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 444e929a-6e95-312c-9baa-b69238a5b05c | -2.27043 | -51.91196 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c96f8e1-21b6-3514-8b19-18772fc8ef51 | -2.58617 | -53.96784 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1381ed1-6794-3502-b116-b3f47c4b9a73 | -3.07424 | -49.19806 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b8cdc2f1-403f-39df-a5f7-6684bda71b8b | -2.33324 | -53.86813 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cae10f7-e733-34ba-84d9-b97535781940 | -3.07789 | -49.20264 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 672d9529-2e10-3a9b-a62e-20bd80d24afa | -3.42712 | -54.0193 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0fa9008-bfa9-3f5d-9c13-7fda106b78eb | -3.60534 | -51.30925 | 2024-11-26 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2e2c2dd-93cb-3f68-a76c-15dfa2137625 | -3.2923 | -50.27715 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e901bb4-2c57-397a-8750-44eb103f923d | -3.96871 | -48.05053 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7d5983c-7ff6-3970-a410-f3254eec5980 | -3.10036 | -53.73748 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9b9061b-8da2-3425-91e0-9a3a3dc44b76 | -6.07115 | -48.03462 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2f94d7cb-02df-3d64-9b47-23c96e9600b9 | -3.11492 | -53.75423 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 068a8412-cf0a-3eb9-b50b-05d58b206d72 | -2.45056 | -53.92141 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d34c8cc-9071-3ea8-a004-bec2ac8be693 | -2.85988 | -53.3201 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02296c24-5c86-38cf-a528-760a554ce00a | -3.50872 | -53.82613 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a2607236-0c2d-3ff9-baec-f81f01659ae0 | -2.77114 | -48.5817 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43543d60-c09e-3b36-9e2b-a14549a0fa51 | -4.29603 | -48.23691 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a068145-de7d-3a96-9282-c21453a2b590 | -3.05802 | -53.27972 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02b012f0-c33b-3aa2-b800-cee489c22ee5 | -2.45992 | -53.68589 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d89b6c2e-e2bb-396b-8ea2-d2c61e7bf6ff | -3.96259 | -48.05945 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3ea8b9b-4be2-3384-8684-0d4f555e4c5c | -2.99017 | -49.58754 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b86f5a48-31d2-3d6c-aed9-01c7a74576c0 | -3.98931 | -48.06002 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d209abcb-f58b-3229-860d-aa2f1cf92534 | -3.22814 | -53.92357 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 381d7da0-a81f-3c88-b684-034a1f40c569 | -6.08003 | -48.04113 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 49e862f7-fbab-3948-968a-e2bfbc7d0cd8 | -2.9324 | -48.01714 | 2024-11-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebc23660-c94b-3439-a2e3-487337addddb | -3.96595 | -48.05724 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6d37bdad-cfe0-3977-81d2-23c1c0b87c79 | -2.81029 | -53.02839 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c06f3899-cc2c-3f1c-844b-d48e0a41109e | -2.80802 | -53.02048 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fc3f630-0e91-387b-b953-8302c4733c7b | -3.26752 | -53.82502 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f58e4c37-a150-3db5-8daa-7117e32398a1 | -2.80745 | -53.02418 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b5a0dd8-9f89-325f-b5ff-ca5f39a24c0c | -2.61334 | -53.96846 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c8d1490-1011-322b-b63d-88a60302cb00 | -3.98067 | -48.0541 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7279799-2d75-3732-8392-7ccf9ad6727f | -6.07596 | -48.03529 | 2024-11-26 05:01:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cef9e1e1-8bc9-3654-809b-2b9c5d375729 | -4.54718 | -43.27704 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae865d5d-8353-38ae-a32f-d0a4d4763d45 | -2.24968 | -53.47266 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba0b26e6-178a-35ef-8c46-712ebe0103bd | -3.09303 | -53.26218 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07641d0c-e332-36e1-8f1a-a57888d34615 | -3.99001 | -48.05524 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02284ab4-009d-3ed0-846e-7b4316dd2090 | -4.65884 | -49.7239 | 2024-11-26 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91323345-db72-318e-a561-aecb5898177e | -2.70398 | -51.98667 | 2024-11-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a063dacc-7d27-3a09-a57b-8d283e63fbb5 | -1.92893 | -53.3506 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cb41a23-6ab3-319f-84ef-e512f39ac8a4 | -2.88708 | -48.73963 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64000974-b7a0-3bf4-ab9b-c14e7097ae0e | -3.05855 | -53.28295 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3ac37921-8cfe-3893-8389-8fbdfaf9e480 | -3.91112 | -42.42025 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 854665f0-4617-3122-9258-59ec43bd5acf | -1.57454 | -54.39423 | 2024-11-26 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 775adb04-2a14-386a-8cae-5701345d25cc | -2.24302 | -53.62392 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd5efb15-71e8-38c1-a7ef-bd9b2b81845f | -2.36062 | -53.71434 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25d8ab7a-42f5-38c6-8a90-150d4ddd4087 | -2.9318 | -48.82731 | 2024-11-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e376f967-f592-3ffa-a672-1766e6b82f75 | -3.22107 | -53.62494 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c41285cd-0ffa-3f8d-bd1e-acf0e02c3610 | -3.96503 | -48.0746 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 83929255-b2be-380d-8511-1b113db338fb | -1.88183 | -53.32143 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 646d7cbc-ccca-3a55-8af5-4ec2dfe98e46 | -3.42323 | -54.0223 | 2024-11-26 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84fbcb17-8cac-3a8b-912d-9e5a5025fd84 | -1.92948 | -53.34703 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4deba71-8947-36f6-9b40-f382565f4ed2 | -2.22188 | -53.67117 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 144c1f9c-0b5a-35ed-8292-01e0207989ce | -3.1359 | -50.56155 | 2024-11-26 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fb8db73-c08e-3f1e-8e4e-72f3e3ac4856 | -2.80518 | -53.01627 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc5d7ea-7af9-3ac1-ad0c-1b9d0e6b2bb3 | -2.07437 | -52.28657 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a309bce0-eda8-3fab-bf63-013ab04f0ea1 | -4.31533 | -48.65053 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 087c1176-7a59-3ebb-842d-4397abeae5b5 | -1.89405 | -53.01391 | 2024-11-26 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fc39f14-db4a-3713-9e1e-c59e7bd3cd86 | -3.18527 | -48.42792 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e754bdff-7417-3827-9f47-2dc57df66415 | -4.11208 | -51.05463 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da9c5ff7-5c2d-3843-aea2-d31d2e661090 | -3.9086 | -42.41915 | 2024-11-26 05:01:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1ace8a1c-a3fa-331a-9ac7-f4a2fa1d06a2 | -4.53884 | -43.2814 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ba632ca-7136-3a4d-b3f0-67766c32db10 | -3.08458 | -49.2157 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af4231fb-544d-30b1-a0a9-9ab40ce68457 | -3.9713 | -48.0531 | 2024-11-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7b5a26a-732a-36c9-a52a-134107a8ffb5 | -5.0661 | -46.77534 | 2024-11-26 05:01:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33de51cb-d44e-368a-abda-b2f2f3521324 | -3.17433 | -48.43992 | 2024-11-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 91962cee-5d86-316f-bd14-2c3fe1f5ccad | -2.6117 | -53.97893 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fa779b8-62a0-3cd8-bed8-1618e6dc0829 | -3.05911 | -53.27929 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 13896a3a-51d8-33c2-94f0-7a8c1a06612e | -4.54374 | -43.29291 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 70e7bda2-6f1c-34ed-978b-d0f73649e271 | -2.98605 | -49.5869 | 2024-11-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f68b0b58-b627-3182-81f1-b4bea3ecd0b2 | -2.58671 | -53.96435 | 2024-11-26 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ae67c4b-77d8-3542-b201-eacbf07d5f03 | -2.79436 | -53.01838 | 2024-11-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67e854ce-0077-3cec-a5e1-d2bd3e3470f5 | -4.54422 | -43.29846 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7f81bba5-2408-3a88-9aa6-c2664654c2a0 | -3.28819 | -51.12922 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8a0dd24-9a81-321e-aef1-e9e1718c7285 | -4.53162 | -43.28592 | 2024-11-26 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65ec5421-8d6e-3774-a247-e122e31337aa | -3.69208 | -50.22889 | 2024-11-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c61388ec-5b39-363c-a608-d37fc4135b8a | -4.24824 | -48.59305 | 2024-11-26 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e19203-eace-35df-958c-3e0b3bb4ef71 | -3.14557 | -45.25658 | 2024-11-26 05:01:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README42.md)
