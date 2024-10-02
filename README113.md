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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d18a4dfb-f2f7-32a8-83a8-ea0d514ab141 | -16.81762 | -57.48223 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 043ca7db-a9bf-3276-abb8-b97b448b3860 | -16.81727 | -57.47954 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 17a304e4-a7d7-3a84-a251-dafbe709f04f | -16.8153 | -57.55988 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 1581c4ea-0bd3-3981-9540-302ed7ce452d | -16.81444 | -57.56462 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 374811f5-69ca-3e61-b3aa-df955df37796 | -16.80692 | -57.56319 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bc683e7b-5297-3fe3-9f89-7f3473074e3a | -16.80639 | -57.48013 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0c6e8cc9-a997-3a3f-9dc9-56f52da0e4d1 | -16.80231 | -57.56724 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b55c0d7f-1988-325a-840d-1c206ee79f2e | -16.80231 | -57.4767 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ca1289f3-a0a4-3e11-9c1c-ab46ff421bb4 | -16.80165 | -57.56945 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| aca2c004-31c1-3112-97c5-cc56c7513a91 | -16.79856 | -57.47599 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 95c8cd66-0b46-3998-a15e-db0ead437945 | -16.79788 | -57.52722 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2e6fea02-07bb-3678-8812-6e9d82a3cc13 | -16.79782 | -57.5246 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 021f718a-d7fb-3b88-924d-71ef618f74ca | -16.79774 | -57.4807 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ed61e875-548e-3031-81b9-7e91cc9ae146 | -16.78778 | -57.49342 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 08ca8c69-902f-3b0c-aa77-a609832f602e | -16.78695 | -57.49814 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f80e1497-5632-3546-b9e1-a0d9e6ef052b | -16.78674 | -57.36755 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 4fd9c1e6-7cf6-31b9-918b-1bcaec11505b | -16.78592 | -57.3722 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| beec5ae4-60f8-37a3-af24-ff5c2f09eef5 | -16.78486 | -57.48799 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 93430692-1bb1-3688-b0bb-a481d9ff556f | -16.78383 | -57.36221 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad85a4b0-65f1-3e9d-8a43-655fcf899b7d | -16.77848 | -57.37079 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 622471a4-71ff-37a9-a8d5-dcb6924a249d | -16.77563 | -57.40873 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3eea55d3-d954-386a-8888-26278dafc196 | -16.77558 | -57.36545 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c17d9336-102e-3ab5-9106-32b37ea26a95 | -16.77481 | -57.4134 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 7f9dfbcc-3bca-3811-a3a4-d94080d95c6a | -16.77399 | -57.41807 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| ecf177d7-929e-3013-8e3b-f8f9f0b6f4df | -16.77185 | -57.36474 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 44ab132f-a977-336b-8cf0-2c624bbc6197 | -16.77108 | -57.41269 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 17afed57-57ad-3b5c-bb60-ec07e6050c21 | -16.77103 | -57.36938 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f8123d27-d080-3aca-b426-5687df18e3f4 | -16.77025 | -57.41736 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| cef5206b-7539-3ef4-811f-70559e98bb7b | -16.77021 | -57.37403 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e87d1ec7-27fb-32a7-8d47-acbc8465f90c | -16.76943 | -57.42204 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 1779d1a9-c281-3eec-a88a-c3c6fbe7df96 | -16.76939 | -57.37868 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 040bde8a-f174-38c3-a726-01dc7fc3b5be | -16.76774 | -57.38798 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 57819ab9-f90c-3263-946d-a8be41067c0f | -16.76731 | -57.36869 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8329ff02-7957-393e-a3e7-9bd365cce95b | -16.76692 | -57.39264 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c16a511e-242f-3e15-871d-4ab3f7db2aea | -16.76652 | -57.41666 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 504430a8-14ed-3786-9294-a9d92a8cb45f | -16.76649 | -57.37333 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| f249f274-1e2a-3792-b181-a3c2fb890951 | -16.7657 | -57.42133 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 0e17f75b-2640-3d20-9859-d0be296ec927 | -16.76567 | -57.37798 | 2024-10-02 04:49:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 00a0141d-2ac2-3667-a6e6-0f19fad7d971 | -14.84762 | -58.61807 | 2024-10-02 04:49:00 | NOAA-21 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e323d95f-cf88-3618-a85c-03ec2c056193 | -14.83456 | -58.61943 | 2024-10-02 04:49:00 | NOAA-21 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8280e498-2599-368e-a36c-992ef3a01134 | -14.83043 | -58.61863 | 2024-10-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc7cca73-9e7d-3c0f-9d0a-606db89b017e | -14.82834 | -58.63017 | 2024-10-02 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 705cf6b8-8905-3ffa-bd35-79c604b4a677 | -14.82769 | -58.61013 | 2024-10-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d139f75b-6e85-3f64-801d-22007aeb0525 | -14.82699 | -58.61398 | 2024-10-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00f1f115-2ee4-3532-99c3-7fccacc14c95 | -14.89836 | -58.03349 | 2024-10-02 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0af4e9fa-7bc3-3cc3-aa04-9d5721173422 | -14.895 | -58.02933 | 2024-10-02 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 34db8e4a-bec4-3d41-b566-14d53eedc3a7 | -14.84418 | -58.6134 | 2024-10-02 04:49:00 | NOAA-21 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b3328d7-b567-3eaf-963e-7dd6ab70e70c | -14.8435 | -58.61724 | 2024-10-02 04:49:00 | NOAA-21 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b6e7717-8555-37e7-8ab8-49e81a3710ec | -14.83182 | -58.61093 | 2024-10-02 04:49:00 | NOAA-21 | RESERVA DO CABAÇAL | MATO GROSSO | Brasil | 5107156 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09f13575-0655-3c62-995f-5e22413a2c52 | -14.83112 | -58.61479 | 2024-10-02 04:49:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fa2697c-0921-3863-a2e7-b1b0988a6045 | -14.82973 | -58.62247 | 2024-10-02 04:49:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4225e8cb-5eb9-34cb-90a0-756ffa19ee37 | -16.60964 | -58.22557 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b8f3f288-b3e8-3651-80e2-160d865a1055 | -16.6087 | -58.23075 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3a30b21b-6e44-3314-acd2-3d907494aa8c | -16.6076 | -58.21456 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 985c14e9-080e-314c-b219-660762ba60d5 | -16.60666 | -58.21967 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 1d8c62a0-73ad-3ae1-9a1c-58b41d6f02b4 | -16.60573 | -58.22482 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| f767fd26-441d-39ab-be56-cee933e55a26 | -16.60479 | -58.22999 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 6e724327-c3ed-3dc0-92e5-fad3e9c06999 | -16.60383 | -58.23523 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3107b45f-c242-3a8c-8c8d-2f9fdec4f988 | -16.60368 | -58.2138 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 77e77f20-f7de-344f-a511-6029db9dc1c4 | -16.60275 | -58.21892 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 19d8f40a-ae3b-362a-a285-e19b1ebde926 | -16.60181 | -58.22407 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| de0a4e03-c9c7-395b-a24d-2da0c6a0805b | -16.60087 | -58.22925 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 969d4546-fa58-3226-9709-885ef4dc12fa | -16.60071 | -58.20789 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aafd4a3b-cf14-38fd-995f-61e526327b8c | -16.59992 | -58.23447 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 32f6aab5-9ce1-3991-ac29-57c9acd92d24 | -16.59977 | -58.21304 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 8a361ba1-f5cb-3a72-9b28-58bfdb3b880e | -16.59896 | -58.23972 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e4e79355-f2c8-3a88-af27-4614913c23b9 | -16.59883 | -58.21817 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 2f871b16-e59e-36a4-95d6-3a7453fde915 | -16.59789 | -58.22332 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 219.3 |
| 323825dc-03b4-3cdb-87df-42a938451e18 | -16.59679 | -58.20715 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 88a74c10-8538-382c-9947-c9d2abb1ecd7 | -16.59599 | -58.23372 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 9bac5963-fb62-3ef8-b14d-4febc7a62839 | -16.59586 | -58.21228 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 56030880-c329-3916-b3de-6b35426c3d9f | -16.59504 | -58.23896 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 8e8d2a99-ba73-3690-8bad-32353a71f77b | -16.59492 | -58.21742 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| 79c3c1c5-9f45-3754-8855-030b84b4042b | -16.59407 | -58.24423 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9c79a9b3-c35f-3749-be83-8f9469e0d934 | -16.59398 | -58.22258 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 219.3 |
| cdaef19a-2926-3504-8a4b-ca96461ea95a | -16.59303 | -58.22776 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 219.3 |
| 2317485f-e6f0-3c70-aaad-a1f6e72c27ba | -16.59207 | -58.23298 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 5ccb014c-f0f2-3df0-8b57-949dd6c5fb50 | -16.59194 | -58.21154 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2abbc742-5696-316d-bf62-f61fdc7cd7e2 | -16.59111 | -58.23824 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.9 |
| 3c8c731b-c53c-3b2e-9970-1eb30f4ca224 | -16.591 | -58.21668 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d5e8746c-53cb-3590-8aed-e7bf65751208 | -16.59015 | -58.24349 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f4e69ee0-f55d-321c-a2d1-1d8b17c8c044 | -16.59006 | -58.22184 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 2b1ab344-fb9a-3b6f-bbc6-19464244bbc7 | -16.58911 | -58.22703 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 5bf0aa47-4b24-3c7f-9e03-f84d0b84dbf0 | -16.58815 | -58.23225 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| d133227b-8b8a-39e0-94d7-13ca7377ec88 | -16.58802 | -58.2108 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 09fe47dc-42ac-32a9-ad80-e96e788aa648 | -16.58719 | -58.2375 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| ba6b7142-e5c7-3c29-9808-e130200cfead | -16.58708 | -58.21596 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d2e8357d-fe28-3ed3-8910-88aa133d5e2e | -16.58623 | -58.24275 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2b29f6ce-4e39-3b98-974d-52bd88c9551c | -16.58613 | -58.22113 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 51c0df8c-8543-3222-985c-7945db3c4730 | -16.58527 | -58.24797 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f050356e-8e55-3db4-99b4-67a2e1cf651b | -16.58518 | -58.22632 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 07c86dcd-9b01-3421-a301-15846a6cfe66 | -16.58422 | -58.23154 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 77d06843-bd79-3b5a-b4f4-4e1e61d18475 | -16.58326 | -58.23677 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 0c1acc4d-5b3c-3dc4-90c2-3b44625ca162 | -16.58315 | -58.21526 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5c721f4-6cfa-300b-9ffc-a6dc9f88a5b1 | -16.5823 | -58.24201 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 79227b08-6caf-3680-8c73-fa71f5b1e2de | -16.5822 | -58.22043 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 566f8e46-ba25-34d3-b195-1dbf1f16062f | -16.58135 | -58.24723 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 0af00a20-d8c2-3741-8511-fa4b6c4ae7c3 | -16.58125 | -58.22563 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 59192c11-fd25-3eb4-8e3d-61a805224bb4 | -16.58029 | -58.23083 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 798b9189-5588-3390-987c-3cb43f1d209c | -16.57934 | -58.23606 | 2024-10-02 04:49:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |


[Clique aqui para ver as próximas entradas](README114.md)
