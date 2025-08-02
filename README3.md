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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cfc80f50-0e24-3ebf-900f-1fee596336b0 | -12.6784 | -44.5085 | 2025-08-02 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 14317532-2d14-35d3-bd2c-45bcea555aa7 | -12.6595 | -44.4882 | 2025-08-02 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 299.5 |
| b5894f03-b141-3967-adb4-fa9abc64aa87 | -12.6402 | -44.4913 | 2025-08-02 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a3acd505-cb1c-3ed6-b742-5dbbf408ed59 | -8.0513 | -43.1001 | 2025-08-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| bcb7ed65-31a1-3098-80b8-af912c310290 | -8.0324 | -43.1022 | 2025-08-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 0eb0c444-8dba-3b15-ba03-9803cc6c65b3 | -12.6591 | -44.5117 | 2025-08-02 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 218.4 |
| ddb787b7-eec0-3bc4-a63f-0a753609ddc7 | -8.0321 | -43.1257 | 2025-08-02 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 263.6 |
| af240a89-e261-32e7-ab1d-8a1c040c743b | -12.6595 | -44.4882 | 2025-08-02 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 280.4 |
| ccf808b7-5ea9-37fc-9e85-077226d49d83 | -10.036 | -44.7056 | 2025-08-02 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4837f26e-ea26-39d9-a88e-69d25d18d6ed | -12.6591 | -44.5117 | 2025-08-02 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 196.4 |
| 87c1a11e-b461-3d7e-89fd-49c54099ba50 | -9.3989 | -45.4928 | 2025-08-02 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e48fb5a8-d1fa-36af-97f1-a3343de282b4 | -12.6789 | -44.4851 | 2025-08-02 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 946efef4-1e67-396a-b896-5a9e8cd71d34 | -12.6784 | -44.5085 | 2025-08-02 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 63b5d6dc-1f71-3f30-9c82-6638b1f3d22b | -9.4572 | -57.839199 | 2025-08-02 01:28:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9abfde60-9399-34fd-a880-e0ce00af2e18 | -20.883301 | -56.375099 | 2025-08-02 01:28:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a308fbc9-221c-30ba-89e8-0181198db444 | -11.4173 | -56.860802 | 2025-08-02 01:28:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21d2a847-cd76-3ecc-9b7b-f003cd9ff1b2 | -9.467 | -57.836899 | 2025-08-02 01:28:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cba79876-f87d-3e89-a85a-83a408504c35 | -11.4155 | -56.852901 | 2025-08-02 01:28:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0413eee9-1c86-3aa3-9dc4-2b45824c9403 | -29.7789 | -53.8437 | 2025-08-02 01:28:00 | METOP-C | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 64b68068-69dc-3ed3-aeb3-e7a1f652000d | -22.3622 | -54.979 | 2025-08-02 01:28:00 | METOP-C | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c07db95-3e5a-3f1c-83cf-b73babba9e46 | -22.364 | -54.986801 | 2025-08-02 01:28:00 | METOP-C | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b4c0bdb-18aa-33cb-b428-c2904b27f3fd | -15.12 | -55.213402 | 2025-08-02 01:28:00 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0bc796-dfcb-3825-ab1a-3bbae0f33b5e | -13.9911 | -53.940498 | 2025-08-02 01:28:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e1f2283a-8d99-3ed4-b0a8-6cf2c2d4d875 | -15.1179 | -55.2047 | 2025-08-02 01:28:00 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e701f3f-ceda-3138-a073-ce8f6cc49555 | -22.3701 | -54.968498 | 2025-08-02 01:28:00 | METOP-C | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a678497c-c43d-380d-9361-f566a4b7f9f5 | -11.4192 | -56.868801 | 2025-08-02 01:28:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f385042c-45cf-36d3-8cb5-4002517fbf75 | -12.678 | -44.532 | 2025-08-02 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| cdf70f5e-42ec-3d1a-81b1-c2b77c54550b | -10.036 | -44.7056 | 2025-08-02 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e216aeca-f4cc-3d73-a3b5-9858ba74d70a | -12.6784 | -44.5085 | 2025-08-02 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| f98d6c63-c152-3e40-87c1-f0a82239e993 | -12.6595 | -44.4882 | 2025-08-02 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 264.6 |
| ca372f04-fc05-3957-b5e9-5d74026438d2 | -12.6591 | -44.5117 | 2025-08-02 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 692b6af5-ed55-35c0-bad0-17156a8b097f | -12.6789 | -44.4851 | 2025-08-02 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 201.6 |
| d918498b-c265-39af-958d-e4f40db5b6aa | -9.3989 | -45.4928 | 2025-08-02 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0561bbbc-5c1a-39a1-b92b-401c1628a59b | -12.678 | -44.532 | 2025-08-02 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b817e0b4-f619-3258-8658-0e2a99db53ec | -12.6591 | -44.5117 | 2025-08-02 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 197.3 |
| aec83fb9-7447-337a-999e-0c1f5fdeb890 | -9.1937 | -45.2886 | 2025-08-02 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 11cd29ec-5f79-3d8b-a3a3-f8ed10400a01 | -12.6789 | -44.4851 | 2025-08-02 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 202.8 |
| 8bf81c81-11d0-3e6f-9b73-eb8dbc49a1f8 | -12.6784 | -44.5085 | 2025-08-02 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.6 |
| c85d209f-417d-3452-aba8-f2c2039b64fa | -12.6595 | -44.4882 | 2025-08-02 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 31299fcf-322f-35dd-9b02-ca4da63d1f27 | -8.2815 | -47.3554 | 2025-08-02 01:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 41ea67af-0a7f-3955-a4ef-9a3e8101f125 | -12.6784 | -44.5085 | 2025-08-02 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 3d54a9b2-0354-3a48-adb4-aa6fcddcee9f | -8.0318 | -43.1493 | 2025-08-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| ec7a08dc-36db-3c7e-8e6b-c091d3cef6f7 | -8.0321 | -43.1257 | 2025-08-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 191.5 |
| 595644d6-cbf9-33c7-8dbd-1d172c0c97a7 | -12.6591 | -44.5117 | 2025-08-02 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 88d72fb4-2dad-3d0e-b573-5329e8c58f1c | -12.6595 | -44.4882 | 2025-08-02 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 214.8 |
| afcdfdcd-7f73-342e-8ab8-98846daa3cfc | -8.0324 | -43.1022 | 2025-08-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| e1c57570-0d66-33c9-bbbf-4b53bb8b30a1 | -9.3989 | -45.4928 | 2025-08-02 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3f2bd97d-8d0d-3a5c-b21b-99e3e14f1731 | -8.0513 | -43.1001 | 2025-08-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 6e760336-50b8-3378-bb74-c9c298b99564 | -8.051 | -43.1237 | 2025-08-02 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 4b17b9c4-1e52-3616-83f7-291144186c62 | -12.6789 | -44.4851 | 2025-08-02 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 190.9 |
| 9b0e942f-d34b-3b2c-af5b-6d5e746beb41 | -9.3989 | -45.4928 | 2025-08-02 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 57b5a401-0372-3ff4-be47-9ef95dc8f9e6 | -8.051 | -43.1237 | 2025-08-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| e909babb-ca1b-3345-b7f3-1bfeee68b349 | -12.6595 | -44.4882 | 2025-08-02 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 71538071-f631-3ada-bfed-0b1e915aad6b | -8.0324 | -43.1022 | 2025-08-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 1b7c77fe-59a6-3202-9d78-d8fd529bc7a2 | -8.0513 | -43.1001 | 2025-08-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| d7aa6def-9997-3798-b034-ba0014a3e312 | -8.0318 | -43.1493 | 2025-08-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| bcebd034-ac6e-3778-b906-d2e9b52de352 | -8.0321 | -43.1257 | 2025-08-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 175.4 |
| 9826eead-b7dd-318a-8e27-e4d496fa3a99 | -12.6591 | -44.5117 | 2025-08-02 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| b9a5a752-f86c-3ddc-b5dd-04d5d3836867 | -12.6784 | -44.5085 | 2025-08-02 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 8e6bc344-beaa-33df-a756-7f0fb9436abd | -8.0129 | -43.1513 | 2025-08-02 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| e0acfa5e-1a1b-325e-9fcd-ce728bd9d910 | -12.6789 | -44.4851 | 2025-08-02 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| ca1d93d4-3d4c-3b9b-91bb-2c1cedd38b83 | -12.6595 | -44.4882 | 2025-08-02 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 197.4 |
| 5825daec-bab6-343f-b01e-ad7349174137 | -8.051 | -43.1237 | 2025-08-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 1d426ff9-b840-3458-84e8-c018a8625d9d | -12.6784 | -44.5085 | 2025-08-02 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 39049610-8686-346c-aa04-b3f281a6d8bb | -9.3989 | -45.4928 | 2025-08-02 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a35f9c12-301b-3f8e-a42f-c38b96dd92ae | -8.0513 | -43.1001 | 2025-08-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 8117d560-63c3-39c2-bd19-0cc45c7ea078 | -8.0318 | -43.1493 | 2025-08-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| ebb361b1-a5cb-3cc5-b373-77a3dd84d1d6 | -8.0321 | -43.1257 | 2025-08-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 185.2 |
| fc3da782-182e-3359-85d2-062c25282d02 | -8.0324 | -43.1022 | 2025-08-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| ccd5a417-0126-31df-acc9-232c84cd2dc3 | -12.6591 | -44.5117 | 2025-08-02 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 65766149-bcef-3f81-91db-e1394ef89f7a | -8.0129 | -43.1513 | 2025-08-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 5734917e-798e-3e9e-9ae8-9ec6e139f230 | -12.6789 | -44.4851 | 2025-08-02 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 4ef767b4-276c-3737-9404-61449a66f879 | -12.6784 | -44.5085 | 2025-08-02 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f918020f-8c9f-3912-9cdc-162866b5bd23 | -12.6789 | -44.4851 | 2025-08-02 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 85d37d71-5422-3ef0-8d17-21b9a1a3c594 | -12.6591 | -44.5117 | 2025-08-02 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| eae966b6-07d7-3bfc-a4a1-0dfdc6ab776b | -9.3989 | -45.4928 | 2025-08-02 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8be6530c-5487-3040-82bc-9d7cd01f30e6 | -12.6595 | -44.4882 | 2025-08-02 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 4848fc7e-339b-3aa3-8808-d6fc144ae39a | -8.051 | -43.1237 | 2025-08-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 8a3abbec-a085-3d16-b0b5-dfb5908e47a8 | -8.0318 | -43.1493 | 2025-08-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 8cc83e5d-493a-32c0-a09e-0544e1099641 | -8.0321 | -43.1257 | 2025-08-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 169.1 |
| 60f0c8d5-54bb-3d0e-9203-ea598271b022 | -12.6789 | -44.4851 | 2025-08-02 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.8 |
| d9148c31-5a1f-31b3-90dd-2b57b3008d30 | -8.0324 | -43.1022 | 2025-08-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 920ede9b-5a65-3fad-a231-89bdf6ed4ae5 | -9.3989 | -45.4928 | 2025-08-02 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b6712163-4d64-359c-b4a9-871bef717f9f | -12.6595 | -44.4882 | 2025-08-02 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.8 |
| b5ea16f2-18f7-3a18-9af2-cb290b0bb986 | -8.0513 | -43.1001 | 2025-08-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| acf73ddf-5b9e-3cd6-b4c5-153613b5f171 | -12.6591 | -44.5117 | 2025-08-02 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| d856ca93-cdef-33d2-be48-20b247eca1b4 | -9.1937 | -45.2886 | 2025-08-02 02:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 0264d5c5-2950-33e2-a76d-524472a9c9b9 | -12.6784 | -44.5085 | 2025-08-02 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 8a3bf91c-5550-38bb-a767-f56979444ee2 | -8.0318 | -43.1493 | 2025-08-02 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 44f0c772-dacd-3a1d-804b-92234733f158 | -12.6595 | -44.4882 | 2025-08-02 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 7b00a99c-30c5-3c33-91b3-a2ab0c24e727 | -12.6784 | -44.5085 | 2025-08-02 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 36becc2b-1e11-3e5e-9ef0-a07981937720 | -8.0513 | -43.1001 | 2025-08-02 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 1efcee26-c4e5-3513-9952-9779b0ec4cae | -8.051 | -43.1237 | 2025-08-02 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 0d798bea-694e-3f07-b413-492bca5d6a8f | -9.3989 | -45.4928 | 2025-08-02 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 926d042a-cbcd-3312-aeb8-57107c0b4b2e | -8.0324 | -43.1022 | 2025-08-02 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| f44c7264-ff4b-389a-b70e-4bd12200fa6f | -8.0129 | -43.1513 | 2025-08-02 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 0f168dd8-1225-3279-863c-96926228c042 | -12.6591 | -44.5117 | 2025-08-02 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 98f6e7b6-34a9-3d1a-9778-e69d321cf7a1 | -8.0321 | -43.1257 | 2025-08-02 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 163.0 |
| fcba5cde-755a-3a33-adf2-b19094612811 | -12.6789 | -44.4851 | 2025-08-02 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 952ff5be-94c5-3b38-bfa7-167d6841a974 | -12.6591 | -44.5117 | 2025-08-02 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |


[Clique aqui para ver as próximas entradas](README4.md)
