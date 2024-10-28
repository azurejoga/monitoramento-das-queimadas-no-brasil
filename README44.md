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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86e390cc-baf0-31b7-8e7c-830b236b857b | -4.04226 | -53.41528 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3850c9d4-1154-3eb9-bb63-df6d57a759d6 | -4.04128 | -53.42076 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95a71f2f-5cda-399b-983d-7fbd134eb802 | -4.03634 | -53.41748 | 2024-10-28 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b0cfd5a-d31f-3c47-80fa-888b0ba1ff91 | -3.59192 | -53.78432 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f2fa40e-f160-32b4-8b30-4c17a16e0ae6 | -3.59076 | -53.79099 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 720b4276-7c54-3319-a259-8ec1210f9b79 | -3.42586 | -54.58858 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e765dc60-93b7-33d4-8ef2-699d2c0afe8e | -3.42471 | -54.59536 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1906ee20-a809-3f76-81fd-7fe807b80893 | -3.42258 | -54.58939 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 73be6c61-3780-3831-a6e5-8314cad5d16f | -3.42135 | -54.59635 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e99e2bee-7fcd-3e73-8421-4ad332a3b1a3 | -3.40981 | -54.49711 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44e43de6-cdec-3e09-91c7-e745e5b6a481 | -3.40862 | -54.50378 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8a725937-59c3-3f9d-954e-bf3606ae61b4 | -3.40549 | -54.49471 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d6adf802-a670-317f-94fd-8f319ec59e14 | -3.40432 | -54.5015 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fa5aa003-bec6-3abf-8605-b3354f1bec4e | -3.40273 | -54.49609 | 2024-10-28 04:06:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e248214b-55fa-3673-ba5f-37ac5df94101 | -3.12949 | -54.27777 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c2dbf5d-6d1d-3aea-924e-524fe2bfa744 | -3.1253 | -54.27055 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a017ef5d-8e80-34e7-9d63-13b213af0989 | -3.12419 | -54.27707 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bba3b58-e6df-3625-8f18-0346de356e5a | -3.12306 | -54.28368 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3e3f166-99b4-3d79-94c9-02e0c79ba1f1 | -3.12252 | -54.27647 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d5e5e97-c39b-38f7-af17-f4dc2c6ef45c | -3.12136 | -54.28306 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e387b8d4-5c04-3088-884b-8d28262466df | -3.11495 | -54.28909 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 852170e2-49bf-3e9f-b469-0e0830ee77be | -3.11437 | -54.28184 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee7f7eb8-3be7-310e-8644-d0a02ec89842 | -3.11319 | -54.28851 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae3fdf9c-3708-36f1-be7e-a6c173b3321b | -3.1091 | -54.28117 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94ca1a2f-1491-3bdb-9b12-1fd505f0f6b2 | -3.10796 | -54.28787 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a4bdb8ca-a2a3-3ac7-8bbe-337379f0ac1d | -3.10739 | -54.28063 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4cdaab8-ca81-3829-bda3-6228f6b1968d | -3.1062 | -54.28732 | 2024-10-28 04:06:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5616f75-47f7-3c50-a638-0df8ef3500eb | -3.09751 | -53.72442 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe06b92c-5cef-3d5e-b1af-c79773286c06 | -3.09075 | -53.72321 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d4f6c83-42a5-3391-af71-0e775d332c5e | -3.07741 | -54.17353 | 2024-10-28 04:06:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c14c8f9a-9194-3802-bc45-c5f0e4332a9b | -3.07165 | -54.17083 | 2024-10-28 04:06:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f1cec0f2-2391-379d-98ec-0c01f50f99c4 | -3.07058 | -54.17723 | 2024-10-28 04:06:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 87b43e8f-5e12-3cb0-80f8-621986893deb | -3.07047 | -54.17225 | 2024-10-28 04:06:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d321cd57-555f-3eb5-92c4-d86ea2bd3cb0 | -3.06935 | -54.17868 | 2024-10-28 04:06:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 001f390c-1113-3240-afb6-d67dd4867fbc | -4.09643 | -53.9451 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47b84625-5af7-36c3-a746-384650adf088 | -4.09535 | -53.95123 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf4c9adb-bbc4-3f0a-aa36-691b27d222a2 | -4.08957 | -53.94453 | 2024-10-28 04:06:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38b9b2ea-94db-3e7b-90ee-ec208806fb07 | -11.93474 | -45.52132 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b18121cc-0340-3e00-91b3-bcf8c1023bf7 | -11.92771 | -45.5201 | 2024-10-28 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d633b28-4622-396a-b291-5cd58487373e | -15.36264 | -40.17709 | 2024-10-28 04:08:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 574e333d-c57b-3b67-928d-1a00fd8346f2 | -15.36202 | -40.18152 | 2024-10-28 04:08:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e4e2a9ee-87a9-3dfd-8f5e-a11aa0987317 | -15.35961 | -40.17217 | 2024-10-28 04:08:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35264fca-07a1-3923-b432-61ce56818b12 | -15.359 | -40.17656 | 2024-10-28 04:08:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6ecc7720-1fe8-387b-a051-55f7296782a6 | -15.35838 | -40.18097 | 2024-10-28 04:08:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a9d58a7-f0f2-3a50-be05-29086ce799ea | -15.20839 | -40.65513 | 2024-10-28 04:08:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a32bd320-94d7-31bf-b4c4-32bbf5926218 | -16.63097 | -40.41008 | 2024-10-28 04:08:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b2cc757c-231d-3e76-ac71-1deaee13ef3e | -16.62733 | -40.40942 | 2024-10-28 04:08:00 | NOAA-20 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 309895d6-651c-3d48-a4ed-356f14817ed8 | -13.37844 | -41.91415 | 2024-10-28 04:08:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b76b1909-d696-3999-8edc-baf86fb764f5 | -14.18666 | -42.04691 | 2024-10-28 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8afdb4e2-12b4-3d0d-bb0b-f8650f236ab5 | -14.12055 | -41.6783 | 2024-10-28 04:08:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae3bd544-5c64-3504-9204-bb5d6541233a | -15.5084 | -42.27256 | 2024-10-28 04:08:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467e6f27-f049-3f46-a077-43cc883c3403 | -15.50449 | -42.27572 | 2024-10-28 04:08:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0903ab36-e837-30a4-a658-b419bbfcab12 | -15.61364 | -41.84917 | 2024-10-28 04:08:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 38c41204-0625-391c-891c-12004b8f82ef | -15.61307 | -41.85295 | 2024-10-28 04:08:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1594778c-82ec-34c1-8c57-7e98dd484550 | -11.99123 | -43.08632 | 2024-10-28 04:08:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7f295c9-5fb7-3290-9d78-c27ea3f5060b | -11.28941 | -41.86061 | 2024-10-28 04:08:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 81875863-1cf1-3ec6-97e8-98da8c256358 | -11.28886 | -41.86415 | 2024-10-28 04:08:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e8fc9c48-92f7-3512-9c9d-07f797e15f9c | -11.13935 | -42.1731 | 2024-10-28 04:08:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a8ab28a8-1ca1-345e-a4e9-cb853fd64dac | -11.13881 | -42.17661 | 2024-10-28 04:08:00 | NOAA-20 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3687b043-e731-325c-be0d-02ec072cdd3d | -13.70418 | -42.88489 | 2024-10-28 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 449ebf6d-9fbd-3f00-80e6-b97ac6c25af3 | -13.57659 | -43.07036 | 2024-10-28 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5cc0310-b745-304c-8911-0fa18a8b8825 | -13.57328 | -43.06982 | 2024-10-28 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf85c223-8d4b-33ec-b16c-28a50ab99c6b | -13.1681 | -42.9678 | 2024-10-28 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 13ebf942-1766-3bd1-a388-8a542110fdfa | -13.16534 | -42.96373 | 2024-10-28 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 966b6374-2e9d-313c-aef5-af37bcb6ee21 | -12.75279 | -42.36452 | 2024-10-28 04:08:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 446555e4-610c-30fd-bf9f-4e691efed9f4 | -12.53522 | -42.36652 | 2024-10-28 04:08:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7541532a-053e-30fa-886d-8644c520a471 | -13.56749 | -43.43139 | 2024-10-28 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4055fc1b-b594-340e-89bf-9034383307ec | -13.56693 | -43.43493 | 2024-10-28 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6e26171-bac9-3666-b036-9cb3c1d0700c | -13.48784 | -43.46151 | 2024-10-28 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8df6143-8124-369e-83c4-5a5e8d31ae61 | -12.50185 | -43.20955 | 2024-10-28 04:08:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6154f0c8-c007-3049-a5cf-6e8046092712 | -14.33016 | -42.30409 | 2024-10-28 04:08:00 | NOAA-20 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ff57b6ab-388d-31ab-9c81-ee0e1fa678c8 | -14.13918 | -42.92614 | 2024-10-28 04:08:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d02458be-f578-3c47-bf43-306559b928fc | -13.7528 | -43.07336 | 2024-10-28 04:08:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e157f26a-65d9-3fb2-ba32-1e1f7cc6ee18 | -14.55206 | -42.97842 | 2024-10-28 04:08:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b42c0b3-8ad1-3d16-b966-4d7aa2dd1177 | -14.50731 | -43.11324 | 2024-10-28 04:08:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63cb6373-eb25-31c0-863d-9af55d0b0142 | -13.89591 | -43.43787 | 2024-10-28 04:08:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bebac1ee-d8bc-3542-b14e-0d05cfbb23f9 | -13.89423 | -43.44849 | 2024-10-28 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8338cddf-1c92-3b9a-af53-16e346fdd9bb | -13.89093 | -43.44794 | 2024-10-28 04:08:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4e95013-c0e8-3244-9830-44fed13a188c | -15.24403 | -43.65691 | 2024-10-28 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23f2bb49-2981-3763-9c4e-5c6464a09520 | -15.24347 | -43.66047 | 2024-10-28 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 042a39e3-d906-3f73-86f5-b2115df33897 | -15.24044 | -43.65678 | 2024-10-28 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b26c705e-847f-3350-b98a-721257bee770 | -15.23988 | -43.66034 | 2024-10-28 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9eed2512-ffe1-3e14-828a-e439597dd004 | -12.0381 | -43.94519 | 2024-10-28 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04a548f0-a0d5-38e6-8511-af3837826966 | -12.03752 | -43.94879 | 2024-10-28 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31316c54-1c1e-32c6-8583-f40778e65985 | -11.92636 | -43.94189 | 2024-10-28 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bfef768-e71c-3e8e-8940-fc4086ec67f5 | -11.92578 | -43.9455 | 2024-10-28 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c482cdb-89df-3fdd-bbad-d9ac0589babb | -11.92085 | -44.03305 | 2024-10-28 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f1511df-d97b-3a7b-9e20-86f79797a014 | -10.78578 | -44.33995 | 2024-10-28 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 667ba049-4d04-3283-a735-4da5dd5ac315 | -13.77186 | -43.62091 | 2024-10-28 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afbc0f61-53be-3577-91c0-553084744996 | -13.6915 | -44.0384 | 2024-10-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc376a6a-32c0-3093-9754-774d4160d953 | -13.67084 | -44.0607 | 2024-10-28 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67612cd8-9ea8-32f9-a289-dc1a895c8ae3 | -13.63275 | -44.57121 | 2024-10-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffdc39c0-0c5f-3da3-b05c-d8fd200d917a | -13.56164 | -43.72483 | 2024-10-28 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 980e0996-0256-3baa-843b-2f4f0dbb9e6f | -13.54881 | -44.33262 | 2024-10-28 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ddfaeffb-1a17-3139-9896-4057b6c26ad7 | -13.53198 | -44.71287 | 2024-10-28 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0c7e858-4101-312b-9417-25feafbab322 | -13.28804 | -43.65014 | 2024-10-28 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a280aec-a10d-389a-be8b-fa0f2d2fca34 | -13.0819 | -44.63393 | 2024-10-28 04:08:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aafa5690-c5e0-3e7f-86fd-626a67bda609 | -13.07853 | -44.63335 | 2024-10-28 04:08:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c35ddfc-0f4e-31e0-a521-b0f6607f9f3d | -13.0327 | -43.99154 | 2024-10-28 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4cfdbb3-0ea6-342b-9bb4-aad354fb94a5 | -13.02764 | -44.08646 | 2024-10-28 04:08:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README45.md)
