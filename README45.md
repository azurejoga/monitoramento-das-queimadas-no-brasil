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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0f2e398-52e5-3830-9442-af4d3e140afc | -1.6809 | -52.6578 | 2024-11-23 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 63a24339-6676-386d-a76c-78a25dff8ba0 | -3.2569 | -54.2226 | 2024-11-23 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| c8b44f05-973e-32f5-9690-9b751886ac40 | -3.2385 | -54.2431 | 2024-11-23 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 6b856258-9d9f-3ee9-9f28-551ad6e90fc1 | -4.6085 | -46.5002 | 2024-11-23 04:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 49d31ca4-a656-35bc-b81a-6920e66e8541 | -1.7359 | -52.7385 | 2024-11-23 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| debba4f1-a089-3a8e-b78a-4cea1cb90fdd | -1.6075 | -52.5977 | 2024-11-23 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0e2aded6-230b-3ab9-b393-ed2f9ae3da0d | -3.2569 | -54.2426 | 2024-11-23 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| e934abd4-9de8-356b-a141-ad61f522378c | -3.2768 | -53.8199 | 2024-11-23 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 731f9faf-4d6b-32bf-b273-b66ea01e8fe4 | -1.7359 | -52.7181 | 2024-11-23 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 88123bb7-8339-3d32-963e-f83c9a16aa66 | -3.2386 | -54.223 | 2024-11-23 04:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| e6ce0700-1f29-3863-94d5-fdcfef0a53cf | -4.5216 | -42.9078 | 2024-11-23 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 6fc4827b-7e44-3f1a-a9ab-9b1ec5ecfe85 | -1.6075 | -52.5977 | 2024-11-23 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e65069d8-9dd4-332c-b653-37410200de32 | -3.2386 | -54.223 | 2024-11-23 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 47a5b4ca-1e59-313f-a4e0-51dea22a0070 | -1.7359 | -52.7181 | 2024-11-23 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 64a9d0e2-9bb3-3206-a310-f72e109b3e97 | -4.2605 | -48.697 | 2024-11-23 04:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 76f1bb2d-b163-350b-81b1-b57995fab976 | -3.2569 | -54.2426 | 2024-11-23 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| d99d11de-4daf-39b7-92fa-d07042203c23 | -4.5403 | -42.9066 | 2024-11-23 04:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 0b97ede0-8d34-30a6-a06c-aa64b2f23405 | -3.2768 | -53.8199 | 2024-11-23 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 98ca48be-3138-3f2d-8c99-63637152ed84 | -3.2569 | -54.2226 | 2024-11-23 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 07ab7e8a-6a9c-3a48-9797-0d810d44060c | -4.6085 | -46.5002 | 2024-11-23 04:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a3232ae3-4c55-3d61-a214-40b852686314 | -1.7359 | -52.7385 | 2024-11-23 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d60b2de2-e666-33ce-91c1-6bab37655ec2 | -3.2385 | -54.2431 | 2024-11-23 04:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4dcff2f2-275f-3ca5-9b93-93707c4a2932 | -4.5216 | -42.9078 | 2024-11-23 04:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| ccf01c7c-1c18-3ec7-a3af-3de381ce5ef0 | -1.7359 | -52.7385 | 2024-11-23 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 16ad0773-1a35-33f0-b217-a3c1ff255b81 | -2.4456 | -49.0816 | 2024-11-23 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0613fa8b-3520-39c8-9d4d-e781c8782f4b | -3.2386 | -54.223 | 2024-11-23 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b0ac368c-c0de-3b7b-8818-d707b98cca44 | -1.7359 | -52.7181 | 2024-11-23 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 5e224ab9-9146-3b49-bb89-186a2c31eb7b | -4.2605 | -48.697 | 2024-11-23 04:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 76774269-76d3-30cb-b95a-5363ba5fb6a9 | -4.6085 | -46.5002 | 2024-11-23 04:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 134.4 |
| c603e5a0-330f-3199-912c-59fb37f51d26 | -4.5216 | -42.9078 | 2024-11-23 04:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cfe2706e-6c3b-3674-aff4-9a9b39cabc06 | -3.2569 | -54.2426 | 2024-11-23 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dd461cf2-f2c1-3ab1-825a-ff59934b8e69 | -4.5403 | -42.9066 | 2024-11-23 04:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 69f63230-4b83-3fd0-81ad-8852b30e771e | -3.2569 | -54.2226 | 2024-11-23 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| ca7ab877-2244-38b6-aa67-7273ee338a8c | -1.6075 | -52.5977 | 2024-11-23 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 396c9e03-4133-3998-833b-13fb483f0d2b | -3.2768 | -53.8199 | 2024-11-23 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e494dc65-9e6f-35bb-9184-2dd0687acaab | -3.2385 | -54.2431 | 2024-11-23 04:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 63d830fd-2bb5-307b-aa6c-791ccef03e3b | -1.7359 | -52.7385 | 2024-11-23 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 14538400-7798-31f9-a417-5a37bd379228 | -1.7359 | -52.7181 | 2024-11-23 05:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7fa3a7e4-ed0d-38d7-b164-201286f1c78a | -2.4456 | -49.0816 | 2024-11-23 05:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| dcc739e5-7b82-3256-bc9c-f0b52974dc2c | -4.6085 | -46.5002 | 2024-11-23 05:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 1310c8cb-e6c4-3cae-8bd7-be97372deae0 | -3.2385 | -54.2431 | 2024-11-23 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d3eaf856-bff1-3616-8d50-346bca102956 | -3.2569 | -54.2426 | 2024-11-23 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 0a72b697-101d-3add-99d3-eba3654b1660 | -3.2386 | -54.223 | 2024-11-23 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a81cc8ec-5e7e-36bd-b416-29fefec167ca | -4.2605 | -48.697 | 2024-11-23 05:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 19fa20af-7302-3cc4-b447-e28d37c85986 | -3.2569 | -54.2226 | 2024-11-23 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ff7648fc-8615-3881-be47-e177ec6e0bdf | -4.5216 | -42.9078 | 2024-11-23 05:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| d618fb13-0853-3c22-b160-e6f508d361fd | -4.5403 | -42.9066 | 2024-11-23 05:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| c780c24c-7654-3ebe-a165-99e63abfd22c | -4.518 | -42.90941 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e1305852-abae-35be-9b15-2dee1d341491 | -4.53721 | -42.91239 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b5ceb5da-1e73-3b2c-a00e-d99abe031f18 | -5.10655 | -43.16062 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f15e3245-a8a6-3e54-b4dd-3016142b35cc | -4.69751 | -45.83981 | 2024-11-23 05:01:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 8ac4f249-a59c-3f86-9098-5df50632703e | -4.25437 | -48.70396 | 2024-11-23 05:01:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e10f7d52-8364-3d6b-9440-675465ff00c2 | -4.12095 | -43.22305 | 2024-11-23 05:01:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 31bda496-00cb-3fc5-9425-7ad90a70f1c2 | -4.44366 | -48.18058 | 2024-11-23 05:01:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 6466552f-bf81-3876-b21d-525f70e19fc5 | -6.0574 | -44.03373 | 2024-11-23 05:01:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cb189cd2-dfaf-3196-8c3c-8bc6ff5f18bf | -5.10819 | -43.15002 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7832a007-bf76-3266-840d-8db71ff830e8 | -2.69937 | -46.25336 | 2024-11-23 05:01:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e907dd0a-5e50-358f-af7a-18988a26aa9d | -6.14055 | -46.67855 | 2024-11-23 05:01:00 | AQUA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e3360c02-7d3d-323e-b8db-a1ee6c4a1402 | -4.52761 | -42.9109 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 58d1db2d-286e-31df-900a-f7df39b225cf | -5.74894 | -46.25479 | 2024-11-23 05:01:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 082911b7-3a1c-3d92-8202-459d76de2c3b | -4.41416 | -44.11942 | 2024-11-23 05:01:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3018cbcd-0eb2-392e-bb9d-cfaa128cad29 | -4.25898 | -48.6753 | 2024-11-23 05:01:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 0f8157ac-97a2-3683-9360-efcd0c3fefd2 | -3.96557 | -46.64188 | 2024-11-23 05:01:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 86004d66-6336-36c6-9ffa-447ec0e55700 | -6.49205 | -47.03667 | 2024-11-23 05:01:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 0a530be6-414c-30fd-8f92-32d2cd80c9a5 | -2.69633 | -46.2729 | 2024-11-23 05:01:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| ca02850d-780f-3734-be1b-34cc4482319b | -4.5929 | -46.49905 | 2024-11-23 05:01:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 30.3 |
| a28787c4-1d91-3460-8a90-6cbdc2f33003 | -4.60551 | -46.50082 | 2024-11-23 05:01:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 5508bf11-a535-3232-9757-a419741750af | -3.15345 | -45.19139 | 2024-11-23 05:01:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e6f58551-5639-3da3-bf5e-b150b79483be | -4.68927 | -44.40387 | 2024-11-23 05:01:00 | AQUA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 940b9ec0-09be-312b-a609-d5d2408f6b2e | -9.72867 | -37.0158 | 2024-11-23 05:01:00 | AQUA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 57b5d639-22bb-3b1d-a030-44a18d7f3f9b | -5.28941 | -44.8624 | 2024-11-23 05:01:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| fa8d47be-ff5f-3777-bad6-fdf4b015a8e1 | -6.49098 | -47.03127 | 2024-11-23 05:01:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| d76c332a-6605-3224-ad13-93930553d684 | -5.29158 | -44.8488 | 2024-11-23 05:01:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a8fb24ca-5fc9-32af-b48e-b72fb46d1caa | -4.44677 | -48.18614 | 2024-11-23 05:01:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| f9f199e1-947e-3886-8981-6d395523eeef | -1.70114 | -46.8586 | 2024-11-23 05:01:00 | AQUA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 5d0c2043-4ed0-3eed-bd32-17e0168c1626 | -4.6948 | -45.85696 | 2024-11-23 05:01:00 | AQUA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f2279c09-4eeb-3ba2-be6f-542ef906c8f5 | -4.71654 | -45.49446 | 2024-11-23 05:01:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b960d5a6-8b05-3518-9d0c-3f349f656e85 | -4.71906 | -45.48929 | 2024-11-23 05:01:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f62804f4-a2c2-35f6-a189-7c7cd25222c6 | -4.60848 | -46.48204 | 2024-11-23 05:01:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 46d99cf4-6650-3b76-b088-ee9bd1dba347 | -3.74784 | -50.00652 | 2024-11-23 05:01:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3cea242c-6e81-3b5b-99fa-a2cf26b6213c | -2.70913 | -46.2748 | 2024-11-23 05:01:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8fa24ece-e828-3ebf-ad06-dfa6ab359bdc | -5.09686 | -43.15916 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 26c45157-7f12-3871-a36f-59f063c77202 | -4.10535 | -42.46799 | 2024-11-23 05:01:00 | AQUA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 952fd259-ef98-3902-98bb-f0452aade5e0 | -3.66401 | -39.57945 | 2024-11-23 05:01:00 | AQUA_M-M | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1b61f870-747c-3d23-8b5f-9633a7aa8661 | -6.34722 | -39.79042 | 2024-11-23 05:01:00 | AQUA_M-M | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 284b1684-14fc-31f6-8dee-552f000d885e | -4.5292 | -42.90046 | 2024-11-23 05:01:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4f678ffe-b312-3deb-8faf-ba4f57f860a6 | -4.21059 | -46.1615 | 2024-11-23 05:01:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 71777c7c-71d6-37bd-bf89-f694c39683fa | -4.59591 | -46.48015 | 2024-11-23 05:01:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7a1c30ad-71fb-3435-8cb3-fe477c8e33fb | -3.96571 | -46.63677 | 2024-11-23 05:01:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 37a0d82d-a904-33df-90f1-d55849b2f49a | -6.05554 | -44.04543 | 2024-11-23 05:01:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c9fa4710-8d04-31dc-b88b-770c4381ac1d | -9.72675 | -37.02979 | 2024-11-23 05:01:00 | AQUA_M-M | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 17.7 |
| ae74d07f-8962-30e2-9443-e10dd3dfaed1 | -4.41613 | -44.10672 | 2024-11-23 05:01:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f7053ae2-a9ef-31fe-9f7c-1d5a05c5d6c4 | -1.7359 | -52.7181 | 2024-11-23 05:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| affeed4c-d543-30e0-827e-d469fe7bfc88 | -3.2569 | -54.2426 | 2024-11-23 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 5bcbe711-9794-316d-a35b-efbfb627b291 | -4.5216 | -42.9078 | 2024-11-23 05:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 2ab405e3-49ff-3b15-9135-4a492c8873d8 | -3.2386 | -54.223 | 2024-11-23 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4241bb09-3ed8-360f-b4f7-5f4f583764e3 | -3.2569 | -54.2226 | 2024-11-23 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 98798251-2988-375b-be56-2f07e4a46909 | -4.6086 | -46.478 | 2024-11-23 05:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8e1088ec-1142-352d-bc34-49e36ed3ce55 | -4.6085 | -46.5002 | 2024-11-23 05:10:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 35b8d4b5-cccf-3a53-9a97-1691fff883dc | -3.2385 | -54.2431 | 2024-11-23 05:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |


[Clique aqui para ver as próximas entradas](README46.md)
