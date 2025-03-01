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
| 9c78f228-0d72-3c5f-a1c3-ee3d0df7571a | -20.87621 | -54.78435 | 2025-03-01 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88146cee-747c-3adf-846b-ea8edce0c3d2 | -19.77213 | -54.79541 | 2025-03-01 05:01:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 314e0cfb-6eeb-33eb-9e80-ba46ff354328 | -20.87977 | -54.78491 | 2025-03-01 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c90bd36-c8e5-3794-b007-38e3bb7ec51b | -22.54059 | -48.81393 | 2025-03-01 05:01:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6606cf3-7171-342b-95b1-a901b8321419 | -21.61262 | -48.47052 | 2025-03-01 05:01:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9e01439-cbd9-3926-b22d-8ea2bf0c9989 | -20.8768 | -54.7801 | 2025-03-01 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d350d719-0d4c-34da-a3a6-d85bfba4701c | -17.32626 | -53.73974 | 2025-03-01 05:01:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a421b606-3139-3810-86e7-f81460aa866f | -20.87207 | -54.78802 | 2025-03-01 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 762826aa-c802-310c-a4b5-90fb0d133eb7 | -21.07524 | -54.19456 | 2025-03-01 05:01:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0a644d8a-f1ed-3ba6-a3a4-d72aca9d6662 | -20.47647 | -53.67571 | 2025-03-01 05:01:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06fc517c-2ea3-3a60-bab8-3e2224d7d02c | -21.61776 | -48.46919 | 2025-03-01 05:01:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49cf043f-babc-3408-a827-4ce4d33d790f | -19.72613 | -55.19699 | 2025-03-01 05:01:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f498084-c086-30d6-9bf5-5a7125e66464 | -17.33405 | -53.73656 | 2025-03-01 05:01:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73cdf248-1e30-3903-a0a9-3abc503f274f | -21.09789 | -56.03434 | 2025-03-01 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2db6fd91-5efd-35a0-842e-5ab8bc053404 | -17.33047 | -53.73599 | 2025-03-01 05:01:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dad99e86-5cf1-374f-a9e7-22d9d39b115e | -20.51874 | -55.5224 | 2025-03-01 05:01:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e122af5-7a1b-35bd-b2ef-d09df2231a8f | -21.61821 | -48.46802 | 2025-03-01 05:01:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c76bc4d-3710-3fc4-9019-1bc0f94d627e | -22.71142 | -47.12397 | 2025-03-01 05:01:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47f8f3f3-7983-36eb-a346-b507199751bf | -23.77797 | -55.1568 | 2025-03-01 05:03:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| e4e85f97-999a-367e-bd60-ea3b330679ba | -23.78157 | -55.15739 | 2025-03-01 05:03:00 | NPP-375D | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| ced42999-43b7-38a3-85fa-62b2da4a5881 | 3.87853 | -59.63549 | 2025-03-01 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7258e27c-dcad-3cca-93d0-fa8c1cd88561 | 3.45824 | -60.24518 | 2025-03-01 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 404f494a-c900-312f-aa4e-cd61ca6f0061 | 4.33798 | -60.35641 | 2025-03-01 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55661846-ca4f-3705-93dd-3fd7d959b274 | 3.46107 | -60.24096 | 2025-03-01 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecff983a-578e-3991-81f2-4759b287631f | 4.01466 | -60.78826 | 2025-03-01 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b5190e2-f942-3f91-a159-cc617781b652 | 3.98083 | -60.85296 | 2025-03-01 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec770742-8e5f-3d8a-85ba-5928d462a3e4 | 4.34205 | -60.35986 | 2025-03-01 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5da871b-ff9b-3cae-a7c6-ad88e7246c85 | 3.98022 | -60.84902 | 2025-03-01 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6147196-1215-3dbb-a96f-0db3df74f686 | 4.29425 | -59.93774 | 2025-03-01 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f64d342f-f481-3867-8730-2e888aed900a | 3.98144 | -60.8569 | 2025-03-01 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cd59918-c0e7-3518-8c7b-08182d35d453 | 3.89568 | -60.08108 | 2025-03-01 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| faf53d23-bf43-302e-a776-6f0014c744af | 4.34143 | -60.35594 | 2025-03-01 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76df5767-20f0-30e7-b188-de90fc07173a | 4.3455 | -60.35936 | 2025-03-01 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daa81bd6-e876-33b8-a628-d072fd856da9 | -3.02373 | -54.5912 | 2025-03-01 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 553ff976-5d06-351c-be03-1ec08eb81279 | 2.10629 | -61.81574 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 67940cf6-6552-3bff-bf43-b7b15e37efab | 0.97127 | -60.52922 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1a6a7e7c-711d-3a13-8754-29360bbf4e8e | 2.18637 | -61.8546 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 94536f0d-55bc-35dd-bd2a-72fce4f43ef4 | 1.12606 | -60.52824 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ded35d9-95d9-3dd8-8c96-003086b6b658 | 1.06972 | -59.23159 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8241b3f2-0c8f-30e4-88ce-7ab7ae1a181f | 1.07302 | -59.23107 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 481ad625-3429-3bec-8ff9-c0e8f1f71b8d | 2.89989 | -60.00899 | 2025-03-01 05:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d0770fe-e674-3439-8e2c-acd8e1ea5c8b | 0.70808 | -59.43964 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d0186219-75f2-3d31-bf80-9a760bca43e3 | 2.44297 | -60.65628 | 2025-03-01 05:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dde13c3-937f-372e-8431-9cb16607641a | 2.11479 | -61.82291 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 513c8fc2-ca8f-315e-9ebe-af4ade9a5156 | -3.01372 | -54.57489 | 2025-03-01 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3a648ba-cb74-34ec-9612-80cc560c8c7c | 2.18702 | -61.85877 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e758227c-1657-3518-8729-a42cc40a1839 | 0.96393 | -60.52664 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 57d0a178-5f1e-34e8-9772-4061cb7a6ada | 1.31615 | -60.06592 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 319bf802-3a22-3abc-b883-32a9d8d65525 | 2.11118 | -61.82351 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96cfa08e-6de6-33b9-806e-fd39c9b27d02 | 0.8323 | -59.94974 | 2025-03-01 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a42a154-8117-3fb7-90b7-9862ab765693 | 2.44453 | -60.86877 | 2025-03-01 05:20:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aa0aedf-e8aa-35a1-87db-96272e673d49 | 2.18933 | -61.84988 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 002ef250-4651-3269-971f-d49e5283c5a6 | 0.97466 | -60.5287 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5c85b0a-9fcb-3db6-9b35-5f118b5d00c7 | 0.99202 | -60.46309 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10c7fedd-220e-3830-a039-2569758c2239 | 1.3128 | -60.06644 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fce5fb22-31a8-3baa-b61b-d85c4c68c4a2 | 2.19064 | -61.85823 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a790f3ea-3b1a-353b-8578-acdec2a91513 | -1.53955 | -54.54441 | 2025-03-01 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94602c99-cd57-3c54-bc75-167bba038fd8 | 1.07026 | -59.23501 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49dd26bc-02d7-346d-b0a9-a3905049258a | 1.07741 | -59.90837 | 2025-03-01 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff5907a7-756f-37f3-b382-ee4ff74c7514 | -1.535 | -54.54731 | 2025-03-01 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bedd4c4-04b4-3474-a458-a4db9c718e21 | 2.10991 | -61.81519 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1f6634ed-6981-3d26-9941-324c2e0fefbd | 0.99539 | -60.46257 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25dacd8a-5570-32dd-a6e6-95173b6a4e41 | 1.07356 | -59.2345 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 345cf8d4-4c5a-3d5c-ae07-7837fc5d1986 | 0.81189 | -59.66748 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 12272371-6864-3203-8ccb-1031bdb98bee | 1.17657 | -60.10925 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b03f98e0-5bc7-3652-8bb3-9292a4ca03aa | 0.96788 | -60.52974 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60496bcc-6516-3cef-9d7b-803323a2e0f5 | 1.94091 | -60.38469 | 2025-03-01 05:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 983e93ae-2e1e-3d2c-920c-093bb871340a | 2.63438 | -61.01379 | 2025-03-01 05:20:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77cffbfe-a5dd-3b8f-811e-5a834474a193 | 2.11055 | -61.81935 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| acd37e6b-986b-31f2-a9bc-32c1271ba5c1 | 0.97409 | -60.52508 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0913f54-1d09-3620-b6d8-e48049f46f7d | 0.82213 | -59.53836 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b6a05815-44e9-3d0b-a1ef-4ce63c0f1101 | 1.08015 | -60.41978 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 097e4715-78aa-314d-8261-39f33e994dbb | 2.82825 | -60.81617 | 2025-03-01 05:20:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa983e4c-c3a4-3e2f-85d0-88954e5467d2 | 0.96732 | -60.52612 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0244281-a8bc-35f7-a2f8-0e834d77d515 | 1.69178 | -60.22701 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87fbaaeb-81bf-3e91-adfd-1e4965e5a9d9 | 0.96507 | -60.53389 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bb3f0bc8-b266-38ae-a99b-b744ad1e8c8d | 0.96111 | -60.53079 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ebf4c4e4-46a4-3d8f-be1e-cc0363e79684 | 2.02909 | -61.40766 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf5f8127-8b2f-3ac1-943d-a738e6aedb54 | 1.31001 | -60.0705 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b42f9687-caa6-3662-8767-f56dd37d1c0a | 1.13277 | -59.5464 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e0178e0-e6a1-3d8f-8d6e-674b771ee63d | 2.18209 | -61.85096 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad438553-e478-3170-8736-ed182155b279 | 0.96168 | -60.53441 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09036a2c-1cd7-3912-bcfc-ec76533b7f05 | 2.11542 | -61.82704 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 053f3f06-0735-3cae-9ca3-54e80d528670 | -2.71531 | -54.61891 | 2025-03-01 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671540aa-0205-3944-ba34-3ae36697e72b | 1.33905 | -60.70491 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bb6ff87-240a-3656-99d9-95169172edb8 | 2.31654 | -61.74748 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9c9be32-1b42-3cec-a29d-a536abd505e0 | 1.69234 | -60.23058 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79a323a9-cf51-3c6b-9815-0b0451026ef4 | 0.97013 | -60.52198 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29906539-f01a-3ac6-9387-36b920931c87 | 1.30946 | -60.06696 | 2025-03-01 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66465d62-45ef-34cb-a31d-538fc959cb23 | 0.96055 | -60.52716 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5b83e29-34ab-3148-a3fe-26e83f02075e | 2.19361 | -61.85351 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87c22bbd-c8cd-30a5-95e0-b0afe5d94051 | 0.96675 | -60.5225 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6501298-fdd5-3eb3-a6cf-579d88f39ce0 | 2.02556 | -61.40822 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7aa19e0-8416-3165-b04b-36973115d89b | 2.18999 | -61.85405 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4009746-ef53-35f9-ba3f-7263389567f6 | 0.74207 | -60.54241 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20e55266-c9ab-3dcf-9a45-b05367962f43 | 0.8721 | -59.68299 | 2025-03-01 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6933f31-da22-3f3f-9fa3-1bfeef8e61fc | 0.96845 | -60.53337 | 2025-03-01 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6d35a1f-2099-32a4-b398-5aca2e6a9085 | -1.539 | -54.54791 | 2025-03-01 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c1897f9-5d96-36ad-b7ec-7c327a461329 | 2.43953 | -60.65682 | 2025-03-01 05:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88556156-b8df-3184-a021-2ee380ad6717 | 2.18571 | -61.85043 | 2025-03-01 05:20:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README5.md)
