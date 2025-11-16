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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06adde50-1c12-3e47-9f3c-256d1ad3c4f6 | -3.7762 | -53.72326 | 2025-11-16 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7af011a7-533e-37b1-b55d-dce8d4ee55f5 | -5.23482 | -49.08352 | 2025-11-16 12:38:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d8cf258b-7c67-3dee-800a-3f8a60f4d29a | -3.27484 | -42.07845 | 2025-11-16 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 09672995-ec6d-3038-ae00-ba7b07d08046 | -2.69713 | -45.08509 | 2025-11-16 12:38:00 | TERRA_M-T | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3653092c-6532-30bd-ad07-1ba0940dfeda | -4.86393 | -44.16042 | 2025-11-16 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 557b223e-ea86-3e31-84e0-d9eda1cdbfee | -4.04657 | -50.48442 | 2025-11-16 12:38:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 4a3d77a8-bffa-396a-9e10-3ff6820e6aa8 | -9.73149 | -43.96991 | 2025-11-16 12:38:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| e7d2cb54-aa9d-3502-b7a2-063db0dab121 | -9.74939 | -47.21062 | 2025-11-16 12:38:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 8305488a-b53b-38d6-9cf9-6044a574a185 | -9.45313 | -46.96493 | 2025-11-16 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3ed54b23-ace9-356d-a242-8cc9a28f93cf | -9.7134 | -48.90314 | 2025-11-16 12:38:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| b5d2e0ba-aa72-3f1f-93f9-28c103573e84 | -3.22799 | -42.4271 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| e0723996-873c-34ac-8fa8-e2d5adf1e78c | -6.72052 | -42.95183 | 2025-11-16 12:38:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 51.6 |
| 238f0dd7-63d6-3d8e-bf09-0ada57f6bf46 | -6.71729 | -42.94478 | 2025-11-16 12:38:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| ca73d8f6-81a3-3005-a7e4-e58f40ed6100 | -3.27698 | -42.08409 | 2025-11-16 12:38:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 185d0d23-e1db-36ff-ac20-32690e332ce4 | -9.69151 | -45.59639 | 2025-11-16 12:38:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 35c85acf-6915-3008-9fee-9043e0107c56 | -7.37511 | -50.02872 | 2025-11-16 12:38:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e734e830-a3c1-3e22-87d8-370a07e619ee | -3.61301 | -42.42944 | 2025-11-16 12:38:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 168.9 |
| 1a1711a7-2794-37f2-b5db-69a93e0595e4 | -3.43947 | -49.48943 | 2025-11-16 12:38:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a49617d9-ed53-352a-b168-d21326802129 | -4.40703 | -43.37666 | 2025-11-16 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| accacb57-b482-3853-b1c3-a5452c61257d | -3.61793 | -42.39098 | 2025-11-16 12:38:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 40880afa-fdfe-326e-9a39-f1b9b206f979 | -3.222 | -43.34695 | 2025-11-16 12:38:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 313.6 |
| e2d8a2bf-fd6c-33fc-81e5-95a0d7157a2e | -8.51919 | -45.37925 | 2025-11-16 12:38:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 21831886-3a85-374f-80de-04f21ce4a34d | -2.898 | -53.28616 | 2025-11-16 12:38:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| adaaf6f3-4129-38eb-b474-4fd435bdb6ad | -9.35513 | -50.7391 | 2025-11-16 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e8431fb5-4078-3c62-8a5a-e62a7067c652 | -2.705 | -45.09174 | 2025-11-16 12:38:00 | TERRA_M-T | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a6f9028b-ec8e-36ec-9f94-983a266fd1fd | -7.39859 | -45.51187 | 2025-11-16 12:38:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2824cc53-b4d2-3521-a2b4-5efca38c3443 | -6.89758 | -47.99065 | 2025-11-16 12:38:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5e026a3c-84fe-3d88-b4e6-5cc4bf8e10f9 | -9.71535 | -48.88826 | 2025-11-16 12:38:00 | TERRA_M-T | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 93b88974-2167-3f9b-9d29-400646604f71 | -2.37895 | -48.65787 | 2025-11-16 12:38:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4b5ebd5c-ccfb-3b7c-a4ae-4beca8b2ddc4 | -4.67333 | -46.93311 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 26533766-6e03-3cf3-8d64-0bbd4b2778e6 | -7.37354 | -50.03994 | 2025-11-16 12:38:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7c85771c-133f-39ff-8296-0404228756a9 | -8.33899 | -48.45175 | 2025-11-16 12:38:00 | TERRA_M-T | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d5ba404e-9a43-3567-9375-428d9d5e8365 | -2.84552 | -44.93157 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 58ca5b20-d1a6-3e7d-a8cf-dfaf9b98beb9 | -3.83551 | -49.81222 | 2025-11-16 12:38:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8250269e-3751-3b4a-8001-c5a3fe85bfa4 | -3.14912 | -45.42061 | 2025-11-16 12:38:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 1d202762-7d8c-3010-a359-1310b0b002d1 | -9.22569 | -50.64902 | 2025-11-16 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 032da68f-d4cf-3c5a-a77b-ae7a5e6212ef | -9.22714 | -50.63805 | 2025-11-16 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 338a3b81-7899-39eb-ad7e-a48a0b47519e | -8.12318 | -43.49002 | 2025-11-16 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 490560cf-ce39-31fe-a223-deb7dac2df44 | -5.4898 | -46.90032 | 2025-11-16 12:38:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 06fa1a3b-8f94-316e-9e3a-4a0b32fd1efb | -9.22386 | -50.64233 | 2025-11-16 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e592c6b7-493b-3b93-ae21-c062ace507e0 | -4.41611 | -43.38286 | 2025-11-16 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 2ebf7c78-f50a-3228-a2be-1461b5adb4cc | -3.22761 | -43.34082 | 2025-11-16 12:38:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 4731fb78-5442-301d-b208-8f5aba6f6871 | -8.52435 | -45.35769 | 2025-11-16 12:38:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 6ee8ddef-d8a4-3407-8e6f-6d71d9304dbe | -7.2221 | -47.12371 | 2025-11-16 12:38:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 563e0bc2-3143-32b8-ba0c-78cfe257ea46 | -3.92788 | -47.05241 | 2025-11-16 12:38:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 7fd840c0-3a6e-3452-b68e-50d63cc0ac68 | -4.42785 | -43.41749 | 2025-11-16 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| dc59b4e1-96cd-3095-87e0-a3d536b32deb | -5.12914 | -55.97331 | 2025-11-16 12:38:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8fbf6a17-975f-3642-b5a9-755d1e5dd62d | -8.67437 | -43.92164 | 2025-11-16 12:38:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 22e2a04b-b984-3fff-b78f-5fd51f735193 | -9.6929 | -45.60342 | 2025-11-16 12:38:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 66a98f03-c929-34c8-ad04-263ba7556272 | -3.21118 | -42.42488 | 2025-11-16 12:38:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 646e4fd8-8ccb-37e3-a606-6b56a9b41d77 | -3.0729 | -42.35677 | 2025-11-16 12:38:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 468bd85a-9ef4-36b7-82a6-77d381edb658 | -9.25692 | -50.56347 | 2025-11-16 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 3a28528a-2c46-36e0-bc13-7da529de8568 | -2.58345 | -51.87423 | 2025-11-16 12:38:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7317d62c-d843-33bf-8da6-283934430661 | -2.88907 | -53.28491 | 2025-11-16 12:38:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 3218a067-d17e-37e8-9b13-53b99cd0b7f2 | -4.40266 | -43.40922 | 2025-11-16 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 655a16b3-b76c-3b54-9314-7edff504bbab | -6.73431 | -42.9471 | 2025-11-16 12:38:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 85b90261-6a6b-359f-8497-c16f93c14874 | -6.06217 | -44.15726 | 2025-11-16 12:38:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 1ee9c77d-03c5-38de-b13d-ad55251da132 | -2.37728 | -48.66964 | 2025-11-16 12:38:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7ab0d5ec-31a3-38a8-bfd4-0f8c13b884b5 | -10.17211 | -44.50251 | 2025-11-16 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d6724f64-7b62-3250-a345-d2d0295bc8aa | -9.45062 | -46.98543 | 2025-11-16 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7eb9f9e5-78da-3439-a477-5275adb3bfc8 | -3.1461 | -45.44193 | 2025-11-16 12:38:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 634a2029-e562-3228-8b41-9f41a2308570 | -9.74945 | -47.20498 | 2025-11-16 12:38:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| f42f243f-1cde-399e-bc69-ab5ec4562eca | -9.06378 | -44.76284 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e9165219-fe47-3269-afd0-bf751f14fed3 | -7.22507 | -47.12974 | 2025-11-16 12:38:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 64e2b9e1-4bbe-3730-9741-f9ce130373c4 | -9.70224 | -45.26401 | 2025-11-16 12:38:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| c0075d5b-71ff-3f1b-8291-90ae332768c5 | -3.60892 | -42.42418 | 2025-11-16 12:38:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 217.6 |
| 9ff44975-d051-3262-96b9-e4465aeeaf04 | -7.37587 | -50.03467 | 2025-11-16 12:38:00 | TERRA_M-T | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 0e1af7a8-8748-3fbc-8d10-c6cad65ab4b7 | -4.41859 | -43.41106 | 2025-11-16 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 8f0ceaa8-dd08-359d-a1f3-5519e744d73b | -2.51978 | -47.81828 | 2025-11-16 12:38:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| da737490-eac4-394d-a7de-4b93bbcc0352 | -4.461 | -49.78381 | 2025-11-16 12:38:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aa2ffa3f-f357-3e1c-93e6-eb20bf96d1d1 | -5.49602 | -46.91262 | 2025-11-16 12:38:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1a1543d1-5ec0-3577-bef0-c16163ade8bf | -9.70123 | -45.27071 | 2025-11-16 12:38:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2ec904a5-4fb0-3100-9f13-26f1b4eb2675 | -9.72534 | -43.963 | 2025-11-16 12:38:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 76ac8b77-7608-36ba-9014-f215f44c1534 | -4.0258 | -48.81022 | 2025-11-16 12:38:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 35bc9f6c-9458-3d89-b19c-1b348a7c1ab2 | -9.06025 | -44.79322 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 718a3a28-b4bc-374a-8688-e667ae872176 | -6.06591 | -44.15113 | 2025-11-16 12:38:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 447492c3-6d1f-310e-a265-b7dc612d0ec6 | -8.11842 | -43.48272 | 2025-11-16 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| f8507d6d-d76b-38f3-9e11-5caea9946481 | -9.16457 | -45.19434 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8b91b0d7-8456-3122-b8a1-c67628bef785 | -10.00159 | -44.77305 | 2025-11-16 12:38:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| d0c36262-293c-3ebc-a54a-87bdbd858fb2 | -9.83086 | -47.07754 | 2025-11-16 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 8fdfe613-b933-3dc7-adbc-4f4403de6916 | -10.12507 | -43.89441 | 2025-11-16 12:38:00 | TERRA_M-T | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d75ad597-5e98-33eb-b7ed-2673e8e22b8f | -9.06731 | -44.75648 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 70af35db-97fa-3eed-99ce-1199a6b32603 | -9.06355 | -44.78685 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f9cfc378-da78-3fce-951d-283a9f2a480c | -5.48753 | -46.91805 | 2025-11-16 12:38:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 4a628ffb-4dda-398c-acfb-c1c31eab8ece | -3.2233 | -43.37207 | 2025-11-16 12:38:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| bc44c2cc-cb41-3cbb-9164-efecfdbefa0d | -8.52113 | -45.38498 | 2025-11-16 12:38:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| e820bdcf-4739-3f12-ae2c-38b70b217baf | -8.67125 | -43.8805 | 2025-11-16 12:38:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| e1a9e1ba-bbf5-3da7-a122-0c71c29ebcb1 | -5.13083 | -55.96174 | 2025-11-16 12:38:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 837f2e60-f983-3856-bbbb-58882e1e810f | -9.16403 | -45.20088 | 2025-11-16 12:38:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 81034e99-b896-366f-b0c5-23ef49d04c15 | -3.6141 | -42.38571 | 2025-11-16 12:38:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 125cf578-2647-347a-955c-936e95eb3c7b | -3.15846 | -45.42858 | 2025-11-16 12:38:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| d7bc4c93-556f-3d91-a84e-6fca6a8b5b72 | -3.1556 | -45.44987 | 2025-11-16 12:38:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| cce5f489-692c-3a95-ac2a-ddb71db662e5 | -5.00138 | -49.6623 | 2025-11-16 12:38:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 126fb882-5f2d-3286-9309-551c1507f84f | -3.48902 | -53.4779 | 2025-11-16 12:38:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 313fd426-3335-339b-9b8a-b60e66783480 | -5.65382 | -45.43996 | 2025-11-16 12:38:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| fccda9d4-32c7-3fc9-854c-4f560f2eb694 | -8.41701 | -49.42999 | 2025-11-16 12:38:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 72c0fd8f-127a-3931-8a9a-688fbd37d2ba | -3.01602 | -49.4339 | 2025-11-16 12:38:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ada21fcc-1bde-3bf6-8911-0b45cbbfca55 | -3.21793 | -43.3783 | 2025-11-16 12:38:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b61efab4-d72a-3610-b424-429f144baf48 | -2.58973 | -51.83048 | 2025-11-16 12:38:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5d4752a6-7896-3c06-b3b8-e0d2035c6a18 | -1.65253 | -53.66322 | 2025-11-16 12:38:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README68.md)
