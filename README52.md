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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5607ebcc-82ca-35b0-a419-c9f3d60ddc3b | -14.13601 | -41.6911 | 2024-10-10 03:57:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d304f91-7d82-3acc-8384-44acc9596a77 | -13.97932 | -41.87513 | 2024-10-10 03:57:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f10596c6-bb54-3d84-8260-4cfcaf28eee6 | -13.97531 | -41.87823 | 2024-10-10 03:57:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b85df9ca-f88b-34d9-9d24-351ba8aab1b7 | -13.76372 | -41.83911 | 2024-10-10 03:57:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1581df43-488d-3be7-8751-e034acb8e6c8 | -15.72987 | -42.39091 | 2024-10-10 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0d642d1-2db8-3ae5-b78b-d54c0f72169b | -15.61319 | -42.37056 | 2024-10-10 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 044e0673-d2a4-3794-a0c0-b6610ad22627 | -13.68052 | -42.50792 | 2024-10-10 03:57:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| add02631-4bc3-38ce-b4b3-73ae726f7bb7 | -13.67704 | -42.50732 | 2024-10-10 03:57:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7f6f01f4-2010-377e-a6be-be53d99cd9d5 | -13.31104 | -42.43053 | 2024-10-10 03:57:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ff55e7b-a184-3073-9b52-0b61b57975f6 | -12.59598 | -42.34461 | 2024-10-10 03:57:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 88201913-fab8-30cc-8444-c09ff2ad3f70 | -14.52973 | -42.28821 | 2024-10-10 03:57:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4903545-1d5e-36da-a3f5-acb536619513 | -14.33082 | -42.34114 | 2024-10-10 03:57:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05d387d0-2fa7-3e8e-9d1c-a011faa6487d | -14.27681 | -42.20129 | 2024-10-10 03:57:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3edad08a-b517-380d-9b6e-f3f3166b9df7 | -14.15889 | -43.30745 | 2024-10-10 03:57:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0e04643d-5196-3a88-89a8-ee8c8566f2eb | -14.43982 | -43.17754 | 2024-10-10 03:57:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b85d15f-dde3-3858-9c34-a9a9fc3bf9c3 | -14.07679 | -43.67199 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81e8c604-ef05-3657-812b-b2f6e3d38b0d | -14.07604 | -43.6764 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dbf11e76-fcba-337e-a839-4545cc23cd7f | -14.07239 | -43.67573 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f28eb6a8-a9cb-3b4f-9834-4bb37e887899 | -13.93662 | -42.55863 | 2024-10-10 03:57:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 834c3630-4bcc-3bbb-9466-547499386de6 | -13.8482 | -42.63715 | 2024-10-10 03:57:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 307cf8b2-d645-301e-8d30-5ce63066ba8e | -13.84754 | -42.64105 | 2024-10-10 03:57:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c34e5c86-4507-3f30-8d69-add433a06ba5 | -13.82705 | -42.41115 | 2024-10-10 03:57:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 860273c3-a6f8-3708-a54f-436ae89271c8 | -13.72026 | -43.09214 | 2024-10-10 03:57:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a893a660-d5f3-319f-aa8b-e762f8bcd918 | -15.4106 | -42.85128 | 2024-10-10 03:57:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ae8b2c3-0c3f-3baf-a0de-bf9b8f7f0763 | -15.2384 | -43.58928 | 2024-10-10 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e2ceddf4-d9de-3a23-834a-750201d7cdbd | -17.65923 | -43.89388 | 2024-10-10 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 491476d3-2bf8-3372-809e-36906b8bea36 | -17.65668 | -43.88961 | 2024-10-10 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 366da9b5-c343-34a0-ae83-4ea62b19abbb | -17.65598 | -43.8938 | 2024-10-10 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9bb2f1c3-3854-39bc-af63-e0f94a8b94fa | -17.6557 | -43.89322 | 2024-10-10 03:57:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d771e4fc-642b-3324-be82-d5ac682c8762 | -13.83257 | -44.53075 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b8dc2c8-782e-37e1-8535-7ab51e276d37 | -13.79691 | -44.62186 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07c6fe1d-8664-3b7e-9d01-393519b05eb2 | -13.57572 | -43.67568 | 2024-10-10 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 296e5ecb-a23e-386f-a82f-985746b0ecf4 | -13.42448 | -43.55089 | 2024-10-10 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60f5bc7f-d812-3e4d-8d44-34b704d5c309 | -13.38234 | -44.6849 | 2024-10-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b237bb1-29f0-3746-a8ec-ec4bd198d71f | -13.37878 | -44.682 | 2024-10-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50310ecd-3085-305b-8e40-a8e5f3eed316 | -13.37273 | -44.67034 | 2024-10-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 345cedb5-5b7d-3766-b2f8-5d193e5af68b | -13.37244 | -44.67258 | 2024-10-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c64d6e9-e953-3ece-8f0a-daf3473cc83d | -13.03634 | -44.95079 | 2024-10-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70ff4727-407c-36e2-bd6b-259dc6c0eab6 | -13.03234 | -44.95005 | 2024-10-10 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9388cb85-0450-3146-92a0-7d798a83965a | -12.36557 | -44.73175 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 662426e3-fc63-3a5f-a6a9-56d805bf0408 | -12.36496 | -44.73526 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc163138-deae-3e40-8d27-888f6b4201c2 | -12.36159 | -44.73101 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1cb3802c-d19d-3d58-90f2-bba8aaba6a79 | -12.36098 | -44.73452 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd2fb11b-b509-38d1-bc50-36d583f62eb9 | -12.29114 | -44.5964 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d424442a-32ac-3824-ac94-6da26d6318d6 | -12.28785 | -44.599 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf4c1957-5608-3354-a3ec-273acd27330a | -12.28322 | -44.39165 | 2024-10-10 03:57:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c575dce-acbd-3a1e-a185-559d0c0c6b9f | -12.26902 | -44.59 | 2024-10-10 03:57:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56f6f373-2355-375c-860f-ce1691bc4c3d | -14.99469 | -44.40643 | 2024-10-10 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce47b732-43f8-3692-ae21-38848b49f947 | -14.08808 | -44.15409 | 2024-10-10 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 96694b4c-1e92-3be5-ae19-dcb25f1a8129 | -14.08433 | -44.1534 | 2024-10-10 03:57:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 8e33546f-80c2-3c5f-97ea-16a6e1b457ef | -14.07455 | -43.68521 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8334d71f-64a0-330c-83a3-92b57a1cddf8 | -14.07164 | -43.68013 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3e7135d-0311-3dd5-943d-bfe28ce34dc9 | -14.07089 | -43.68454 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8781f2f7-8010-3af3-9d31-7c5e5c166ea3 | -14.06798 | -43.67948 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22495e05-22ea-3874-8d79-2a3b1951a436 | -14.06572 | -43.69273 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 63dec3c2-ed5b-3e0e-8a3c-9ca88a7372f2 | -14.03721 | -44.02557 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8cead309-c108-3870-89e8-6c653f708d74 | -14.03632 | -44.0221 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f445db36-428b-3a25-ade2-423f04b135d2 | -14.03554 | -44.02671 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6737c676-51d3-3501-8380-58b43c88dce2 | -14.03349 | -44.0249 | 2024-10-10 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a27e0665-2c2e-359b-97ec-2fc663f2624b | -13.83476 | -44.5286 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9a92b76-a629-37f2-b729-f0ddea9c65c4 | -13.83426 | -44.52094 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b5abfc6f-1ac2-3d00-a114-b6c31d9de482 | -13.83387 | -44.53355 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fcf71b51-d1f6-3027-8c9b-3b4a213fe795 | -13.83342 | -44.52583 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d01efab-aed5-3577-a7f5-8764f19420d5 | -13.83179 | -44.52301 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37e736c5-2025-3a98-851e-df9c315c7a7e | -13.83172 | -44.53573 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39782841-f7dc-387d-bc06-0f761c733b31 | -13.83091 | -44.5279 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f04c607-c332-3bc8-b31c-7913f1e499cf | -13.83042 | -44.56637 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4147c9ca-cce3-34e3-ac82-1477ff8ef2ee | -13.83002 | -44.53285 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0433f7d0-8037-3c47-ad89-249542dd765f | -13.82958 | -44.52513 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91715421-9fd6-3fec-a6c6-cdec9efa30e6 | -13.79304 | -44.62116 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f1f80af-e765-324b-a73c-4292ba5db0fa | -13.96003 | -44.54964 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31f64757-f118-3376-acb3-1ed2f55ed7c6 | -13.8827 | -44.48181 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61ec5329-1c66-3fc6-bd49-df0af85ffc3c | -13.87159 | -44.49989 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7bee7be8-a6e5-33f5-8ffe-5394e50f90a7 | -13.86392 | -44.49849 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e967b2fd-3ff7-35a6-9b10-875eca264fb6 | -13.85957 | -44.52301 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b1eb7ff3-68e4-3281-bc64-796f4e767e78 | -13.8592 | -44.50272 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c918eab-1639-3cad-89c8-130c2e510403 | -13.8587 | -44.52789 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 946304c9-5875-3613-a51d-8ed2673d9405 | -13.85832 | -44.50766 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31148201-1c3e-3b03-97ff-79c631cb71b0 | -13.85745 | -44.5126 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3de10549-ff12-3134-9758-89e238e64993 | -13.85658 | -44.51746 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| c765a923-88e8-3ed9-b8e7-50eda6328f00 | -13.85572 | -44.52233 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 1f9c146f-e8ea-3224-a3ee-bd6fb91512ac | -13.85536 | -44.50206 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98bb5f12-b51e-3fc2-b710-649f6a38cb21 | -13.85518 | -44.54772 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 244cddbf-e66b-3c58-adcc-18de47774d10 | -13.85485 | -44.52721 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cbf06147-b58c-337a-825c-959d9772277d | -13.85448 | -44.507 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 163a12fb-8b8e-34b5-a35d-28e78413dc7a | -13.8536 | -44.51192 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f82096d4-9bcc-3a55-b609-543ba2332b6c | -13.85274 | -44.51678 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| eddc1576-85ac-3126-aa65-c0c957e23538 | -13.85187 | -44.52164 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| ab3889b0-2bd8-3cbc-b306-862839f6606c | -13.85151 | -44.50138 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9fde949-45b5-33a6-966e-757bda471546 | -13.85133 | -44.54701 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 534d0a9c-002e-31ef-9c2f-84edf7a76900 | -13.85101 | -44.52652 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8afd8f2f-685f-322c-af98-a5a2e9b57484 | -13.85063 | -44.50632 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab88881-836b-3f7a-a5cf-9e69e226b638 | -13.84976 | -44.51124 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e76aa37-6e73-3b78-9bef-a6d87f1e4b62 | -13.84889 | -44.51611 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 72a76943-323a-304e-b9bf-61dda765f320 | -13.84803 | -44.52096 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| df73e8e8-548e-3862-8fe0-f50bb3fcfde5 | -13.84748 | -44.5463 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 980b380f-c076-3990-8028-99f3308651b5 | -13.84716 | -44.52583 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98f1ebd5-020b-3c58-9758-368d0b1d5e98 | -13.84679 | -44.50565 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec240c9d-a506-36d9-af7f-b39189cac597 | -13.84591 | -44.51055 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba8ba9ce-0e98-3772-9b5d-791fb06775bb | -13.8453 | -44.50283 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
