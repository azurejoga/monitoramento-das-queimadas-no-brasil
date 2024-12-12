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
| e3ab0ae2-352f-3feb-9c06-9c6f317480d7 | -6.9346 | -43.5168 | 2024-12-12 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 306.2 |
| ed6f4f61-e49a-3d57-b57f-c4f26e875a0f | -6.9156 | -43.5418 | 2024-12-12 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 0e2ad62c-5470-3576-aece-a48e25cf997f | -14.7461 | -52.6471 | 2024-12-12 04:10:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d7b00c99-b6ae-3200-a4f2-660444a7a38a | -6.9349 | -43.4934 | 2024-12-12 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 079670aa-1841-3cb3-b09f-06f848a6baf0 | -3.2317 | -46.8716 | 2024-12-12 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| f1127b4c-c3ff-30be-9007-63690f6330d7 | -1.8788 | -54.6908 | 2024-12-12 04:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 44a114ef-d94c-3a2a-a5bf-61b24a7f0998 | -18.0659 | -52.9766 | 2024-12-12 04:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| bd3a3c9b-221e-3647-9d9c-33c1246a86f8 | -3.2503 | -46.8709 | 2024-12-12 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5f336bde-0fb6-3610-92c2-0a7ff77d9697 | -3.2502 | -46.8929 | 2024-12-12 04:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1aabf3b8-3d3c-34c5-910f-517b17a7f58e | -6.9158 | -43.5185 | 2024-12-12 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 36eb9698-c349-3546-a0f3-fa0c9ac5a2c5 | -18.0663 | -52.955 | 2024-12-12 04:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ab968ce7-2a01-38cd-a952-2564143ec0e7 | -4.51532 | -43.61943 | 2024-12-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17044889-44fa-36a8-8fa7-9c00e1caa3fe | -4.02053 | -46.127 | 2024-12-12 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b917609-e7b8-3e39-ab34-c2ed5cc00178 | -3.66968 | -39.21356 | 2024-12-12 04:14:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad1b7996-fd77-3e9a-bf7a-19489b4c1ebf | -2.95895 | -48.61281 | 2024-12-12 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d40ce110-583b-3200-bf31-e666baba58b3 | -2.56615 | -51.88049 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb670def-8e38-3136-8fb0-c1146a802d55 | -3.75903 | -38.93799 | 2024-12-12 04:14:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 40a6e72e-0999-38f6-97f6-fe43c989f719 | -4.86993 | -48.52576 | 2024-12-12 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b48b037c-56ba-3044-a8e6-da977dc4b82d | -5.23823 | -38.50525 | 2024-12-12 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0ca76c39-f993-3bbb-a9b6-25beec814bb3 | -5.16316 | -44.36645 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1dec072-1e9c-30c3-be90-e2dfdbedf728 | -2.91455 | -52.95744 | 2024-12-12 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e8a6a1d-b607-3b36-afd8-c0ba88b6205c | -3.24825 | -46.8825 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| cbb0e94d-29c3-3c19-8565-63c63fdf99dc | -6.04135 | -42.16204 | 2024-12-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ec8e3cd9-0913-39fc-a8eb-10f5eea37497 | -4.08582 | -46.67161 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a0eac5-b4ca-3ae6-810a-73a5bbd3f439 | -4.55099 | -48.00682 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4d7bb0f-117f-3e65-8f19-7a902e7b0cdb | -4.11097 | -46.80177 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ba7ca16-ea6e-3821-8310-e333d21e44ba | -5.34955 | -44.19607 | 2024-12-12 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd01e0a9-ab26-3e11-af3d-dab02d013a83 | -5.35624 | -44.1971 | 2024-12-12 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7411e4b-6aaa-34e3-a281-1be182d1afea | -6.12683 | -42.55551 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e3214b80-0e27-3b1a-b8c8-924f72eac19e | -2.73503 | -47.53532 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d164579d-bf8b-328a-824c-23e066fd602a | -6.06024 | -44.04914 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e1d00164-31db-3130-b1a6-0c3a5f3d01f4 | -3.99233 | -46.50776 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d95eee6-304f-310a-8401-c9da2c6689ba | -4.39996 | -47.72716 | 2024-12-12 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6422bb61-a672-3da9-a5a6-76f36878bcda | -5.35289 | -44.19659 | 2024-12-12 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b1b7129-415c-3370-8ae8-358d2e8332ba | -6.05692 | -44.04861 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6addae80-b896-3e79-afa5-27eec2997d74 | -3.78841 | -47.09922 | 2024-12-12 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8574e685-cdc5-390d-934d-e09a74bf4193 | -4.50813 | -43.62188 | 2024-12-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14679138-02f2-36bf-b062-51acff4cf04b | -6.34062 | -41.53741 | 2024-12-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a842f13d-956b-3837-aeac-39fa1d8ac20d | -2.57585 | -51.88917 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 191e956c-094f-36f8-9fd9-fb122a0a2372 | -5.98632 | -43.47905 | 2024-12-12 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aac53aa9-50b8-3f9a-9bdf-6473b5bf7d54 | -4.37634 | -48.7523 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1ae4b47-bf6c-3935-a2c6-71e94a43e64e | -4.38432 | -42.14919 | 2024-12-12 04:14:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 085885f0-5533-320d-bf21-12ca6f132f28 | -5.92607 | -44.60006 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d6bc10d-68d4-33a5-893b-72c1a3a86cfd | -2.95713 | -47.89617 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b12c36c-3246-38bb-94c9-7cede4d6652d | -3.00647 | -48.05248 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32dae13e-089c-31b0-a480-afb966bf7a41 | -3.23952 | -42.42675 | 2024-12-12 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8658785-1f8d-335e-9d04-b8cf6489cb7f | -6.03801 | -42.16153 | 2024-12-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b409a077-51e9-342a-b7a2-29d5d9e06c3f | -2.5742 | -51.8888 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be9bf1ba-78f0-35fd-91d8-024351ae241d | -5.92044 | -42.35154 | 2024-12-12 04:14:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1c3177a5-3f89-3a56-b096-fdc7f117b641 | -4.25433 | -47.58583 | 2024-12-12 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7109e2e-0a77-3b5c-9adb-0d822a40695f | -4.0316 | -46.88538 | 2024-12-12 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a77daa1f-686e-3602-b833-08999bea0644 | -4.1117 | -46.79722 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1b23926-bb5f-3fe0-9360-59f0cd4b4bc6 | -3.83422 | -44.03775 | 2024-12-12 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 164cb851-9f74-3a49-8c81-316dec5563cc | -4.86152 | -40.75326 | 2024-12-12 04:14:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d2d23db7-283f-3c66-b99c-a93fd4720d2e | -5.59558 | -39.44592 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0b55cafe-3088-3a3f-b9e3-dd2906215647 | -2.07196 | -45.4073 | 2024-12-12 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c6116fa-69d3-3003-b2fa-d42263395cd8 | -4.32981 | -48.71621 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b6e814a-8e76-3959-a3c6-7f5107bd6adb | -3.85597 | -40.45375 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a059696a-a60e-3189-9925-8ea85f165c63 | -6.13069 | -42.55255 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3daf996a-a29b-3085-9303-d62ae6c85ea5 | -2.58746 | -51.91979 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0cbc365-b3d4-3d3f-ba7c-7c6510176f09 | -5.92551 | -44.60363 | 2024-12-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da00a8a7-ca1f-3ab9-bf66-dfb7d3de5811 | -3.56547 | -43.49473 | 2024-12-12 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dace1c25-4402-39df-85c3-c684e5b5c586 | -3.82103 | -40.69912 | 2024-12-12 04:14:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b86e9a33-084a-3cb6-b7e8-56f21306a5c0 | -4.07663 | -54.30341 | 2024-12-12 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61ede24c-3a2c-3a32-affe-310cba3cb998 | -3.85471 | -40.45277 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b4b53ece-d8e7-3250-843f-620f0a2766eb | -2.51847 | -51.78737 | 2024-12-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93e01ee5-67ec-3c71-87c1-dad88cbdc965 | -2.52386 | -51.78832 | 2024-12-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7af5240f-fe94-3113-937c-2738f3f8526f | -2.71368 | -45.5688 | 2024-12-12 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b774fa72-a99d-3c01-bc15-194f36a1a555 | -4.50098 | -46.05975 | 2024-12-12 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e009a35c-63ea-311d-8e9a-0e9380328633 | -5.71024 | -46.51189 | 2024-12-12 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daf59f82-2ef6-354d-9b63-1445e17fb383 | -5.22652 | -43.87787 | 2024-12-12 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae8d2850-181f-34cc-a5e8-bf3bbfc72ad5 | -4.17085 | -48.75646 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1c8ecd6-a6ea-33ea-a4fa-ab0ecbf1703c | -3.96086 | -42.16103 | 2024-12-12 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c8dbca3-3bb9-3b8f-8393-abca15082614 | -4.07045 | -54.30231 | 2024-12-12 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ee7d7b5-3839-3350-9b62-ef7501607654 | -3.43107 | -42.98431 | 2024-12-12 04:14:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0cc7d12-3df3-3e64-aeb5-68cc944f0ed5 | -5.98356 | -44.59849 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc5c0f0d-52a3-3a88-9f63-85539a2892c9 | -1.97504 | -48.69576 | 2024-12-12 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 200146ec-7ad5-3fba-a926-4dd794340673 | -2.95019 | -51.78269 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ec11c7a-9be9-36d3-af50-6f8f45a1c4bd | -4.49712 | -46.10606 | 2024-12-12 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc2d1b1b-e2b0-301f-99fc-2aa56a6ad1d3 | -4.09707 | -46.67335 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b352e257-64d1-3f56-a6fb-e6d77366d994 | -3.24899 | -46.8778 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 469c0568-eb3e-3c4c-84fe-f2735da957e1 | -7.10634 | -39.08242 | 2024-12-12 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83e0e074-0f98-3a84-99f0-1b4288a1654f | -5.96902 | -44.13126 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0052a339-7e98-3956-97f7-c25b64be26cc | -5.92887 | -44.60416 | 2024-12-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4b7514f-62b4-3505-9b51-4e5104c31f6c | -3.89589 | -42.55718 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d65a52ad-5297-369d-9618-b3243af0f6de | -3.95476 | -46.76011 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99d4a0e2-27a7-3d34-aeea-73da57eef8aa | -2.46751 | -47.83089 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ee22d24-9da0-37c6-9ccd-b82b3eb005ee | -4.36644 | -48.21869 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fffbc24-1430-3dff-beb1-ae764250603d | -6.90427 | -38.52069 | 2024-12-12 04:14:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dfa7951f-ff7f-3514-8797-a9fcd23c1f89 | -4.18697 | -42.43353 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ffa4254b-86ff-3c7d-995a-1068e4729228 | -3.85818 | -40.45331 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 28b7062d-ca0e-321b-a210-32e6334ce57b | -5.46076 | -46.47818 | 2024-12-12 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a9b19d-62f8-356d-8cdd-b9c043120f6c | -3.69964 | -45.29358 | 2024-12-12 04:14:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e84a20f-4a6b-3f88-b71e-49d9aacf5d3c | -6.12791 | -42.54855 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c41dd8ee-6f90-3ad6-8585-16f63c0fe2f8 | -3.82084 | -44.12328 | 2024-12-12 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01fa4ed8-4801-3f6f-a8e9-93b885ab33c6 | -3.7748 | -50.69418 | 2024-12-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c73cc352-a4c4-3d2c-8e7c-e39080ef2e3c | -4.74564 | -44.10089 | 2024-12-12 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6b3af3e-9768-3431-8802-377f332bc7c5 | -4.83613 | -44.21665 | 2024-12-12 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 354a6279-130a-394f-8277-22cb95c2b2cf | -4.13013 | -46.7067 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8a0eb2e-6b5f-35d4-a5e0-4bbe78a41d8e | -4.35741 | -49.74517 | 2024-12-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README13.md)
