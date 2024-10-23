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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76a233a6-1c47-32be-90a7-199de1dca63c | -3.7255 | -41.6748 | 2024-10-23 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 7bb7c201-0091-3fa7-8d2e-b8ed3c073f70 | -4.1719 | -47.9894 | 2024-10-23 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| d6d6e6de-5c96-31d1-9415-9c94a5d7268c | -4.1905 | -47.9885 | 2024-10-23 01:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6c6db5f4-e47d-3c4f-aae9-6f1bbc26c438 | -4.6775 | -44.6089 | 2024-10-23 01:25:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| db2500fc-6363-3676-b3da-2fb0cf7e93ea | -5.5671 | -43.2576 | 2024-10-23 01:25:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b642686b-7a5f-3cfa-a496-51e0c6e52fab | -5.5858 | -43.2562 | 2024-10-23 01:25:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 160de31a-90e3-3fe2-a91b-92a267afffd9 | -10.6725 | -58.749 | 2024-10-23 01:26:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 2d92804e-c8dd-365e-9579-45a99b46ced5 | -11.322 | -54.3359 | 2024-10-23 01:26:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| f727f8f8-f06a-3d4c-a7a9-5e3da861115d | -11.3406 | -54.3547 | 2024-10-23 01:26:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c46f6c89-354c-35da-83be-fe675ff595cb | -17.7848 | -57.4885 | 2024-10-23 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| c68a3a94-0860-3faa-a423-96c2fbdfa29f | -17.7637 | -57.5732 | 2024-10-23 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 4438df85-197e-3c75-8400-9e1b993abb7b | -17.764 | -57.5526 | 2024-10-23 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 150.5 |
| 9b653c21-7b2f-37d6-9701-d0ba5763fd39 | -17.7644 | -57.532 | 2024-10-23 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.8 |
| b007016b-667a-3f4a-be85-ba3c962b1021 | -17.7838 | -57.5502 | 2024-10-23 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.4 |
| e3ff7c0f-9315-36fa-9efc-99a29ae9dbef | -17.7841 | -57.5296 | 2024-10-23 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| a930a0e2-c89a-3c79-878d-c459c60eff15 | -18.2637 | -56.0603 | 2024-10-23 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.1 |
| ce404ae6-3327-3809-bf1e-717ddd060023 | -3.1091 | -45.2968 | 2024-10-23 01:35:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 118a1a2c-640a-34f7-a4e0-4335a88babb5 | -3.0917 | -54.1666 | 2024-10-23 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| be30ce28-519e-3398-aaf9-cb0c3949c590 | -3.1277 | -45.2961 | 2024-10-23 01:35:24 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| bcefb8e7-5301-3518-bac7-d7843f38bb02 | -3.1101 | -54.1661 | 2024-10-23 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| cefc3bf8-e796-3fc6-9adf-83937d7fa6dc | -3.1102 | -54.146 | 2024-10-23 01:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| a255ac5c-0fc8-3458-9a59-dcc03f464ec6 | -3.5491 | -54.7351 | 2024-10-23 01:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7f05c94b-f2dc-3b2c-b6d8-4fce80fae008 | -4.1905 | -47.9885 | 2024-10-23 01:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 435265fb-cec9-393b-81f7-9c7dc1afe461 | -4.6775 | -44.6089 | 2024-10-23 01:35:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 89932e32-b7ed-38f3-87d4-bb01e2c54c89 | -4.7254 | -45.7363 | 2024-10-23 01:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c1071947-60a7-3651-abb0-e434eb4ec03b | -5.5671 | -43.2576 | 2024-10-23 01:35:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 6dc708c0-57a5-3610-bfac-9addb3822095 | -5.5858 | -43.2562 | 2024-10-23 01:35:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 895448c7-da63-3388-921d-a8651c89b176 | -6.6765 | -43.0491 | 2024-10-23 01:35:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| ed4630da-59aa-347d-a59b-7991ee0b9e0c | -10.6725 | -58.749 | 2024-10-23 01:36:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c4c8ad12-9c8a-331f-9fc2-bfa4d519ce7d | -11.3406 | -54.3547 | 2024-10-23 01:36:11 | GOES-16 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c27fc57d-30a1-3cd6-a881-7090ec4f59cf | -11.6115 | -48.5521 | 2024-10-23 01:36:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| f7097197-5bda-306e-a30f-23b8a4f72d13 | -11.6118 | -48.5301 | 2024-10-23 01:36:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5ffd8824-1b39-31a2-b53c-1d62f7e22f81 | -17.7848 | -57.4885 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 31a95740-5d55-3b1c-b99f-f1b1c8597171 | -17.7841 | -57.5296 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 0de12afc-840e-390b-9014-839e7481a276 | -17.744 | -57.5756 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 5e03df92-5b45-3384-8460-241860e4ecb4 | -17.7637 | -57.5732 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| 85d4ab21-d767-3944-811c-8f99146a21f1 | -17.764 | -57.5526 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 21979c29-a1bf-303a-b2cb-079cf29e9e36 | -17.7644 | -57.532 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 17e7676a-76b7-3295-aca6-384a8f2e50b6 | -17.765 | -57.4909 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 2894d424-5355-3823-89a0-26e265e4292a | -17.7838 | -57.5502 | 2024-10-23 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 6db8fad6-0ac2-37d2-899d-fadb82010727 | -18.2633 | -56.0812 | 2024-10-23 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 9314284a-6210-3550-92d7-5da8981a055a | -18.2637 | -56.0603 | 2024-10-23 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.8 |
| f6702608-61eb-32e9-90b2-d353e5ee11d5 | -19.5465 | -56.6983 | 2024-10-23 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| adf88bbf-1328-3f31-8ef8-233eb8b71179 | -19.5469 | -56.6773 | 2024-10-23 01:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 61c65a1a-726d-3e24-b200-d0dc61170b0e | -3.0917 | -54.1666 | 2024-10-23 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 80c4cee6-c004-3428-96ae-74e42a87ee10 | -3.1101 | -54.1661 | 2024-10-23 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 24282273-1418-3a59-9cff-820b746599a1 | -3.1102 | -54.146 | 2024-10-23 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 687cc751-b1f4-3f19-852a-bb8d6b34c0fc | -3.5491 | -54.7351 | 2024-10-23 01:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ae03cb4e-2eef-3bc6-88d0-34f71188410f | -4.1905 | -47.9885 | 2024-10-23 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 291b8877-3473-3d95-bc1c-730ebb63d79b | -4.6775 | -44.6089 | 2024-10-23 01:45:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| c7a3ffcf-522f-3a9d-bffb-88caf7b7e978 | -4.7254 | -45.7363 | 2024-10-23 01:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1c7b2d26-c7ed-3187-a16f-ac8629a1772b | -5.5671 | -43.2576 | 2024-10-23 01:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| d9c8f9eb-57ee-3910-b514-7c8913c12197 | -5.5858 | -43.2562 | 2024-10-23 01:45:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 99707485-71c2-3186-be22-f3621d282064 | -10.6725 | -58.749 | 2024-10-23 01:46:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 16d1bb71-aa60-3ac8-9405-3546c9d4dda5 | -17.744 | -57.5756 | 2024-10-23 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.5 |
| c546e850-7f2a-34e4-891e-de382eb328f1 | -17.7637 | -57.5732 | 2024-10-23 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 6a3135a9-b216-31ba-b4f8-1dcddf1d36ad | -17.764 | -57.5526 | 2024-10-23 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 7db1019d-cdc5-36ff-b6af-4f58f10e8603 | -17.7644 | -57.532 | 2024-10-23 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 769da510-be48-333f-967b-82f6ef9fb74f | -18.2633 | -56.0812 | 2024-10-23 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| d9d6639a-9214-3f03-becf-fe5ff139d1f7 | -18.2637 | -56.0603 | 2024-10-23 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| ab3f5d03-b76d-3af7-b33e-51b92c32cd7f | -1.388 | -51.9867 | 2024-10-23 01:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| a37da6bf-9a06-38f6-912f-a2fe04d760ad | -3.1102 | -54.146 | 2024-10-23 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 54c829ca-abb3-30e6-a811-ba63eb3e9e92 | -3.1101 | -54.1661 | 2024-10-23 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 728bc8a9-4ae7-3f8e-9731-f72cc9332214 | -3.0917 | -54.1666 | 2024-10-23 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e8a3a671-b521-3c2d-a258-f77ccb12fc60 | -3.5491 | -54.7351 | 2024-10-23 01:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e2bdf388-a76c-361e-9b6d-f42da267db64 | -4.1905 | -47.9885 | 2024-10-23 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 7103dede-dc79-329d-b616-6602c945fa0c | -4.7254 | -45.7363 | 2024-10-23 01:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0499b2d9-6749-3732-ba22-b3b3b6f3e99f | -4.6775 | -44.6089 | 2024-10-23 01:55:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 982923e6-a7a6-3d55-9646-67eb37a0b660 | -5.2305 | -43.1886 | 2024-10-23 01:55:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 14f7b60d-0c76-32af-aeb4-443870bc3ad9 | -5.5858 | -43.2562 | 2024-10-23 01:55:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 8d061e08-6ca0-34d5-bf4e-1d252a48b9bf | -6.6765 | -43.0491 | 2024-10-23 01:55:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| c32c0c90-331c-3caa-bd91-06ed0eec82f3 | -10.6725 | -58.749 | 2024-10-23 01:56:07 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 9e9a040a-ace8-3e4d-aa64-de0b3c741320 | -17.7644 | -57.532 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 19254831-ecab-38c6-b17d-3e6b41895441 | -17.764 | -57.5526 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 400e30bb-c983-390e-bb9b-abb08a0da6d8 | -17.7637 | -57.5732 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 1806a266-a0ae-3037-8cb7-cb2cbfad7a20 | -17.744 | -57.5756 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.8 |
| d6fb5cd1-92de-3d79-8892-6ce1094af32a | -17.7065 | -57.4569 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 46be9118-ae13-3b0a-af18-7b50d8a116f2 | -17.6871 | -57.4387 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| f1b9d5db-1175-3f8f-9454-cb5524849fc2 | -17.6868 | -57.4593 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.7 |
| 6edff2a3-1164-3472-9ee3-02eda3a9cd83 | -17.6671 | -57.4616 | 2024-10-23 01:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| ae72b345-a54f-3c9d-b9c3-6c43d29fcfcb | -18.3207 | -56.1986 | 2024-10-23 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.1 |
| a23aefff-9f14-3c20-9143-ce529c6f4c05 | -18.3203 | -56.2195 | 2024-10-23 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 30e28fc3-ca8b-34e8-a861-2777b7056143 | -18.3004 | -56.2222 | 2024-10-23 01:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.3 |
| e41aa8fb-069e-3c6f-8a19-d0904d09f754 | -2.5225 | -54.0992 | 2024-10-23 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5f8e959f-ffe1-370e-b5b4-da20676325e5 | -3.0917 | -54.1666 | 2024-10-23 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 9224ad6d-b390-35cd-bf48-b1ed5f50caef | -3.0918 | -54.1465 | 2024-10-23 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4cb3e87f-3fc6-368f-9558-b6720a626315 | -3.1101 | -54.1661 | 2024-10-23 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| fc8dc670-2d9f-3bcc-a2f3-eeab4a7b0d10 | -3.1102 | -54.146 | 2024-10-23 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| c6dc3e26-2f2e-3e49-b6f5-a5fb01dae93b | -3.5307 | -54.7356 | 2024-10-23 02:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c7b5f0f9-a0a8-3c38-940c-bec6ea06165b | -3.5491 | -54.7351 | 2024-10-23 02:05:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 33ad9d30-f7ed-398e-b2e8-ca9b5f672968 | -4.1719 | -47.9894 | 2024-10-23 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 306828bf-c7e7-3002-bdee-484fc22c45aa | -4.172 | -47.9677 | 2024-10-23 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| fe5a2160-d4bb-38d4-b666-0da0e33d6eee | -4.1905 | -47.9885 | 2024-10-23 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| fd7d778a-52fc-33e5-90f4-797f21b56c09 | -4.7254 | -45.7363 | 2024-10-23 02:05:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| fc95531a-a903-3dba-a1c4-bc20a83fb894 | -5.5671 | -43.2576 | 2024-10-23 02:05:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d462d752-feb1-3c01-ac13-3f121a994189 | -5.5858 | -43.2562 | 2024-10-23 02:05:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 432dc20d-b9b4-34ee-b463-f8f7988d94eb | -17.7637 | -57.5732 | 2024-10-23 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| e8f145db-e209-31d6-b944-de88350264e0 | -17.6865 | -57.4798 | 2024-10-23 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 6c5e5969-5f91-3aed-aa68-73578c200e34 | -17.6868 | -57.4593 | 2024-10-23 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.0 |
| 555b0467-00e4-3003-8f4d-15c9c5f5acef | -17.6871 | -57.4387 | 2024-10-23 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |


[Clique aqui para ver as próximas entradas](README11.md)
