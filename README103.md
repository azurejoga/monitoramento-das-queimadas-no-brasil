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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18754793-5aed-3894-8e27-f395e811d397 | -4.3537 | -48.6068 | 2024-11-02 13:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 97c99f7e-8a2c-3006-8b04-9bf0ca0803bf | -5.2297 | -48.0868 | 2024-11-02 13:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 49112711-5d4c-34ac-add5-59fafe30e557 | -6.3157 | -41.5844 | 2024-11-02 13:45:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 418ba5d0-99fb-376e-a037-9dcf4cde4d3e | -6.978 | -41.352 | 2024-11-02 13:45:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 13b2f294-f825-34b8-a281-a8ac548a8ee8 | -7.016 | -41.3239 | 2024-11-02 13:45:46 | GOES-16 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 7df64fa8-21e7-3a6a-bd2a-e96f88fcfd9a | -0.1196 | -51.3359 | 2024-11-02 13:55:07 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4e01ad70-6706-3d30-99b3-25834adffae2 | -1.2013 | -54.0188 | 2024-11-02 13:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 2cca3975-0797-393f-aca7-8644bf2670d9 | -1.2014 | -53.8983 | 2024-11-02 13:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9f620417-218e-3d3f-80db-eac6431316fa | -1.2014 | -53.9184 | 2024-11-02 13:55:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 37f99b74-8bfd-3ca7-83df-bea836bc0d71 | -1.3846 | -54.1172 | 2024-11-02 13:55:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b37a167f-5e3a-3191-b4bc-a969f06e7625 | -1.4244 | -52.1913 | 2024-11-02 13:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0750fe70-6d5f-3c63-b0bd-9becb2b274c4 | -1.406 | -52.2121 | 2024-11-02 13:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| b2f4bb37-4c76-3d74-9bba-65737bff24fc | -1.406 | -52.1916 | 2024-11-02 13:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a46132e7-4ed9-3df7-8ab2-d8e74ed08970 | -1.4244 | -52.2118 | 2024-11-02 13:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a4cdd448-f47d-3f2c-812d-2527758fb4b1 | -2.3245 | -46.5262 | 2024-11-02 13:55:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 1a17614d-9885-3978-8c9d-93f139ee8a94 | -2.2568 | -50.4376 | 2024-11-02 13:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| e640c6bc-45b5-3d36-9ed9-acb9944ea21a | -2.2703 | -46.1068 | 2024-11-02 13:55:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| b784f8a2-d0fd-3bc3-8a06-fa322ccd4218 | -2.1747 | -53.6633 | 2024-11-02 13:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 3e26a63d-3fbe-317c-81b1-7aedde10988c | -2.4365 | -46.3241 | 2024-11-02 13:55:20 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 98fa672f-6f10-3b26-b2bd-e30ab8012e56 | -2.4824 | -49.102 | 2024-11-02 13:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| f7fcdbb3-05ad-3d6b-8206-134bde630383 | -2.4825 | -49.0807 | 2024-11-02 13:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 200.1 |
| 2b852fa9-a55d-360e-a6b1-b3c98213b6c9 | -2.6759 | -46.7585 | 2024-11-02 13:55:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c40d3854-de40-3071-8a0b-2ae47cdc217a | -3.1098 | -54.2665 | 2024-11-02 13:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 42850828-ef48-30f7-880c-70472f883aac | -3.1282 | -54.2459 | 2024-11-02 13:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 946b8e26-4a34-3e64-817e-5fc280b11665 | -3.9474 | -48.3451 | 2024-11-02 13:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 93559fbb-1515-3c8d-b468-9981058ad3d4 | -3.9473 | -48.3666 | 2024-11-02 13:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b59dae1e-89bb-333d-9d5e-460ddc1a42e5 | -4.2628 | -55.5097 | 2024-11-02 13:55:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8223cb19-fc3a-3d70-b5f5-352acf0c3c67 | -4.8919 | -48.5803 | 2024-11-02 13:55:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6f23fb9a-784d-38d5-95ca-2c6a97616c61 | -5.2297 | -48.0868 | 2024-11-02 13:55:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6ca062a7-9869-3d78-ae0c-9dfe5486ca5a | -6.316 | -41.5603 | 2024-11-02 13:55:42 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 5fd07d4f-110b-3396-8f39-3dcb85fca3bb | -6.978 | -41.352 | 2024-11-02 13:55:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 64.9 |
| dff4bf33-cd6a-3158-b05d-fbf9b39af52a | -7.5813 | -39.9621 | 2024-11-02 13:55:49 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 99.0 |
| fe9b5489-cbd0-3183-9407-f0dc8a961449 | 2.2003 | -50.8773 | 2024-11-02 14:04:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ef74e736-f3c3-37e5-9941-b13f8fe3317e | 2.1819 | -50.8777 | 2024-11-02 14:04:54 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 3b333180-eb8d-3d4a-9e88-f7c0d92585a0 | -0.1196 | -51.3359 | 2024-11-02 14:05:07 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 145.6 |
| d28563d1-3325-310c-9e13-f5cfc6a07ced | -3.08 | -50.31 | 2024-11-02 14:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57bd5e6b-d962-3d82-b3fd-05a852ed8b6d | -3.11 | -50.25 | 2024-11-02 14:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a05bbcd9-cd1b-3711-855c-c3d839ed64f3 | -3.11 | -50.31 | 2024-11-02 14:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61cde1a6-fefe-3a36-af82-f0f4a0884717 | -3.11 | -50.36 | 2024-11-02 14:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d11a4192-3360-3961-9ecc-edf299491365 | -3.08 | -50.25 | 2024-11-02 14:05:09 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32dad0a4-c145-3705-9bcc-f1cbd83beb82 | -1.2013 | -54.0188 | 2024-11-02 14:05:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 84c8eed0-3658-314d-a669-d9aa0c168994 | -1.4244 | -52.1913 | 2024-11-02 14:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0196c119-d8f0-333d-8a40-6579384e0bfb | -1.3846 | -54.1172 | 2024-11-02 14:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e6172faf-898b-39b8-872f-18324f547eaf | -1.4427 | -52.2116 | 2024-11-02 14:05:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c3812564-7d84-3485-a650-26298f42aee6 | -2.45 | -46.3 | 2024-11-02 14:05:14 | MSG-03 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5ad2230-f56d-3f62-a9be-e15e92323ce7 | -1.5531 | -52.1896 | 2024-11-02 14:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1f3554b8-d275-3c65-b15d-ff039e7ce548 | -1.5127 | -54.2961 | 2024-11-02 14:05:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 96f2ffb1-497d-3a24-945c-2fa606043df8 | -1.5715 | -52.1689 | 2024-11-02 14:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8b0c9514-e767-3aca-af46-3cce2e3ae99f | -2.3246 | -46.5041 | 2024-11-02 14:05:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7fa3b8f3-c585-31c8-b615-2c4f1050fe48 | -2.2703 | -46.1068 | 2024-11-02 14:05:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 1b20e5f0-c5b5-310e-aa29-ec66b51dbfef | -2.2568 | -50.4376 | 2024-11-02 14:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 89805903-a1c3-3126-ad61-1f64744f67a1 | -2.3245 | -46.5262 | 2024-11-02 14:05:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| b320dba0-8933-304b-af42-5729cb3a68d7 | -2.4825 | -49.0807 | 2024-11-02 14:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 9a6d5c2f-c4c8-3a31-be18-c8fe2d090706 | -2.4824 | -49.102 | 2024-11-02 14:05:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 3dd2aef3-6aa9-3c3b-9d6d-9faa16c712f6 | -2.6574 | -46.7591 | 2024-11-02 14:05:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 46958386-ba09-3be3-a084-3f9ac3fb3f1c | -2.6759 | -46.7585 | 2024-11-02 14:05:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6d000a7f-0b0b-3ee9-a90d-beb1473d892f | -2.836 | -48.4501 | 2024-11-02 14:05:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 89c5e9eb-b595-3707-943b-01a99199e318 | -2.722 | -49.287 | 2024-11-02 14:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 5d7b3eb1-6f0d-393a-baa3-ea13e917a109 | -3.6421 | -50.1667 | 2024-11-02 14:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c8fc8a4e-a661-3f49-9ec5-ec474cfbf4e1 | -3.9473 | -48.3666 | 2024-11-02 14:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 250f1f6d-7b1b-3f00-98ad-b48fa2eee93b | -3.9474 | -48.3451 | 2024-11-02 14:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 2835a6f7-6a64-34ba-825d-8266e5f3178d | -4.2628 | -55.5097 | 2024-11-02 14:05:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 47ca3d6e-070f-3f8b-8877-8dfd7057a44d | -4.3537 | -48.6068 | 2024-11-02 14:05:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 75d69816-ce68-3692-b2c4-af45296e5ab3 | -4.8919 | -48.5803 | 2024-11-02 14:05:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0f2b0115-2882-327f-b5a5-0a33f7f5f634 | -6.9971 | -41.3258 | 2024-11-02 14:05:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 6e0512fe-bd7b-3134-bf6e-286657a4e2b8 | -6.9782 | -41.3277 | 2024-11-02 14:05:45 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| f6fa8213-9802-3860-adc6-0e6a8c714ba7 | -7.5813 | -39.9621 | 2024-11-02 14:05:49 | GOES-16 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 731b7a21-42c9-320c-a1d6-f64115544bd8 | 2.2003 | -50.8773 | 2024-11-02 14:14:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 3819de1e-e3aa-3c39-9c3a-2129b4c1a0ac | 2.2003 | -50.8981 | 2024-11-02 14:14:53 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 763c2037-1071-3cf0-b4f6-52ccdcbce72b | -0.1196 | -51.3359 | 2024-11-02 14:15:07 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a6209b85-64d4-3252-9c9a-6fca9b90b50d | -0.6896 | -51.6847 | 2024-11-02 14:15:10 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.1 |
| dce93898-7786-347c-8666-bad92de200e9 | -1.2724 | -55.6902 | 2024-11-02 14:15:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| ad63e4e9-83bc-3ef6-9e33-54c05de723f1 | -1.2013 | -54.0188 | 2024-11-02 14:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d745c6c4-350f-35a0-b8db-3caaa52c68b0 | -1.2014 | -53.8983 | 2024-11-02 14:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a9f444f3-e377-3cd0-b862-1e9cb190b829 | -1.2014 | -53.9184 | 2024-11-02 14:15:13 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1cf2a511-bca5-364f-b59d-b0116ae0290d | -1.2541 | -55.6904 | 2024-11-02 14:15:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 17f84306-75fc-3323-8385-9a8640830798 | -1.3846 | -54.1172 | 2024-11-02 14:15:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 449c852d-cf6d-3b16-8c84-5cf8ff3873d2 | -1.4244 | -52.1913 | 2024-11-02 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 9c616be5-dbce-3851-857a-1a4040ea0d24 | -1.406 | -52.2121 | 2024-11-02 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 53c1f16a-fe0b-3bf2-858f-87eb47cbc022 | -1.406 | -52.1916 | 2024-11-02 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1cca8acd-d8ff-3488-9902-22e7d05e2006 | -1.4427 | -52.2116 | 2024-11-02 14:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| f903a65a-085d-3d02-b91a-ffa5571c6e36 | -1.5531 | -52.1896 | 2024-11-02 14:15:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a22071b1-cd20-346f-8001-c4fbc5662718 | -2.1695 | -48.7252 | 2024-11-02 14:15:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| c8ccfc14-1988-3819-896b-df95b490c849 | -2.2703 | -46.1068 | 2024-11-02 14:15:19 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4b6fef81-a256-37d8-b76a-9c9bbdc6bed9 | -2.3246 | -46.5041 | 2024-11-02 14:15:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c600c9f9-438d-3f5f-b5fb-a9af026f5ee8 | -2.306 | -46.5267 | 2024-11-02 14:15:19 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 85ebc88d-a554-37e5-8591-1fe022d8f654 | -2.2384 | -50.438 | 2024-11-02 14:15:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 8feb9568-5414-3b4d-a0e6-bda2e1edadad | -2.3239 | -46.7247 | 2024-11-02 14:15:19 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c1dd7fe4-4dcb-329f-b40a-3ffada37ece4 | -2.4435 | -49.7182 | 2024-11-02 14:15:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7d734b8b-0b5f-352d-904d-b51c0aeb460e | -2.4251 | -49.6975 | 2024-11-02 14:15:20 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| b4918a30-d99e-3b75-b2ae-ecf807b8ae64 | -2.4103 | -48.5694 | 2024-11-02 14:15:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c77c150e-66a9-3094-9530-5e82d069bf0c | -2.4825 | -49.0807 | 2024-11-02 14:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5743a1f5-aaca-3030-8fe3-78d5d6dff2a9 | -2.4617 | -49.8022 | 2024-11-02 14:15:20 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 9b2fc2af-a733-395a-a666-38a03b21befc | -2.6759 | -46.7585 | 2024-11-02 14:15:21 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 620f5c07-b77a-3edd-968d-cf84da5a5f17 | -2.836 | -48.4501 | 2024-11-02 14:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 1645b078-1cdd-3bad-aab9-1779e06273a8 | -2.8361 | -48.4286 | 2024-11-02 14:15:22 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| a632e813-1bab-32ff-a0c7-74586537255e | -3.1097 | -54.2865 | 2024-11-02 14:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6b25103f-76a7-357e-9451-5caf32e655bb | -3.1098 | -54.2665 | 2024-11-02 14:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| deb31f3c-26c2-39a6-bff3-fe8cd1891f22 | -3.3841 | -46.0694 | 2024-11-02 14:15:25 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 96f8ff9b-c85b-3673-951f-a79d5e14aa3a | -3.6421 | -50.1667 | 2024-11-02 14:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |


[Clique aqui para ver as próximas entradas](README104.md)
