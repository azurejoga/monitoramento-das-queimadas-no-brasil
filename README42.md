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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5028b670-0d0c-31e0-be94-d230ae485e23 | -12.17375 | -46.73756 | 2024-10-13 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a6ec032-d497-3c6f-8a75-5628a38abbc7 | -12.17317 | -46.74062 | 2024-10-13 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 419e358f-898f-303f-b258-30a62c7624ad | -12.16868 | -46.73651 | 2024-10-13 03:47:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec4979b8-82cb-3e04-8915-0bc7fe47a565 | -12.15997 | -47.52871 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424a4001-1047-319b-af96-66fa356976cf | -12.15933 | -47.5321 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d42197be-9024-3ff9-89a8-714c0c040a16 | -12.15748 | -47.52728 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26799036-4b68-33d8-a35a-6733631f7225 | -12.15682 | -47.53063 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44faa1f9-40a8-3fe6-9816-caf9360c2a4c | -12.15617 | -47.53395 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70a7fcc2-e472-33dc-9982-3a0d55dca716 | -12.15462 | -47.52764 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f183eaf7-26d0-3d5a-ba01-73dc33abeb15 | -12.15398 | -47.531 | 2024-10-13 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30a2f09b-5c05-3688-91ec-2579bf1c09f2 | -12.56781 | -47.28754 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04ff5295-377f-3dbc-ab11-0177a4c9850c | -12.56717 | -47.2908 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c09293b-e3e0-3d30-be84-9c7cb1e18fc1 | -12.52873 | -46.81879 | 2024-10-13 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d264152f-4b25-33d4-8633-821e3d55dceb | -12.52754 | -46.82496 | 2024-10-13 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c138f2fa-b69d-3b75-bdaf-21763b1c324d | -12.52305 | -46.82089 | 2024-10-13 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cd52c36-8ec8-306c-aee1-5fa14363b0af | -12.52246 | -46.82397 | 2024-10-13 03:47:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99e3e62e-b432-3465-bf1b-304999829e37 | -12.38353 | -47.31715 | 2024-10-13 03:47:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f48dce4a-2c2e-3662-abf3-11e8fee97e33 | -12.3829 | -47.32043 | 2024-10-13 03:47:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3920a617-11ea-3d81-bb4c-a1ecaaf019ea | -12.38227 | -47.32372 | 2024-10-13 03:47:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a0838b2-b6dd-3056-aec5-3ae88eec0533 | -12.28533 | -47.65494 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3eb0bc0-c2ca-3c78-9a69-f4c94d5d6cac | -12.28465 | -47.65847 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f06af56a-22cd-369c-aedf-dcbe29064c81 | -12.28395 | -47.66204 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53595ab3-feea-3799-8e7a-516848472bc8 | -12.27998 | -47.65372 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1edb9fde-ae71-312b-9823-3eae59654b65 | -12.27928 | -47.65731 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc27e3ad-1da5-356e-a453-a16f1259e4b5 | -12.27857 | -47.66095 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b55b9c48-913d-3e85-998d-0a47696d2508 | -12.27787 | -47.66455 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deb767d0-9523-3998-a7a1-f1620fc06de3 | -12.27461 | -47.65258 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c44c6d3e-a435-373a-a3ef-b98ada82a83d | -12.27391 | -47.65614 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c90a4958-78d6-36fc-bfa0-dab0793dfc27 | -12.27321 | -47.65973 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9288f23e-6d44-3c00-8584-50e6c714c00e | -12.26994 | -47.64786 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e6133964-45eb-3503-b4ff-cfaaa1d44c39 | -12.26923 | -47.65146 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8daa6a3e-ef9a-38c8-a5f4-b5f0478b9931 | -12.26853 | -47.65507 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1af9f59e-9846-3564-8365-58f0694faada | -12.26458 | -47.64668 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d344487-b5c2-3f08-8f21-95b187bde00c | -12.26386 | -47.65035 | 2024-10-13 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 981b361f-844d-3873-bf45-7e017140d80b | -2.23909 | -45.88148 | 2024-10-13 03:47:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848b15f0-1395-3aee-bc75-35956f9068de | -3.35199 | -47.31671 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 43716de0-8489-331a-9242-d38682f2d554 | -3.3517 | -47.31804 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c183be39-a136-3ce4-bf5f-9fbfb8adb05f | -3.35118 | -47.32135 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 342831a7-199d-33dd-a43b-323ebe3ec1e4 | -3.35092 | -47.32271 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5f371e92-80fa-3429-841b-22bd6c99fd01 | -3.35037 | -47.32598 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4effa5b8-53cd-35cd-b796-bbb38a19b697 | -3.34566 | -47.3165 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7f87ab5f-ade1-30a0-ae6a-9c119ee2acf6 | -3.34489 | -47.32108 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 05eb62de-9f5c-39fc-a4c5-8c2d2f031a3f | -3.34412 | -47.32566 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 42bb7d06-99fa-3562-a3c2-23206e4bc849 | -2.95844 | -47.37214 | 2024-10-13 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19015f0c-58da-37d2-8464-a6643e6347c5 | -2.61184 | -47.34408 | 2024-10-13 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 417dbead-e33d-3d96-998c-432df4d384a3 | -2.61101 | -47.34909 | 2024-10-13 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c5978e6-12ae-3239-b153-0ba3e93bdec7 | -2.61039 | -47.34315 | 2024-10-13 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d208006-6523-3ff6-bcf9-4fabb6074abd | -2.60954 | -47.34809 | 2024-10-13 03:47:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 916bdf02-d836-3d3e-a7cf-ae9db0a1e249 | -2.52944 | -47.27185 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45009406-6242-36cb-81fe-7df9a7f635ef | -2.5287 | -47.27018 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7a12d64-2942-3e61-9c61-f6fb5e6917f2 | -2.52866 | -47.27663 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52649cfa-6acb-30c4-8885-e22056c6a8ef | -2.52789 | -47.27494 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc3b1177-227a-318a-972a-e7f4ea99619b | -2.52786 | -47.28152 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1d282e3-41ac-3c78-abf0-35b85b33c54e | -2.52707 | -47.27974 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b377dc74-5188-3f18-9aaa-e9cec3c1bd82 | -2.52324 | -47.27087 | 2024-10-13 03:47:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0206b2bc-464b-31e1-aa47-2d94cad429fb | -4.89818 | -47.66617 | 2024-10-13 03:47:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90d399e5-5c27-3073-960b-2839265cf04f | -4.89796 | -47.66794 | 2024-10-13 03:47:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7c5da4b-c202-3b34-8b5b-fecb6a931596 | -4.89738 | -47.67082 | 2024-10-13 03:47:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac847b4-2a1e-3b96-9049-cd903d0a6d6f | -4.82066 | -46.87058 | 2024-10-13 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbd6649e-8b0f-33cb-a0b1-49f96dbd0154 | -4.81995 | -46.87474 | 2024-10-13 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c469f94-f672-33a5-8574-0a2264d9ee60 | -4.53416 | -46.55775 | 2024-10-13 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b6ab7e14-ed75-3588-8fdc-5145deba2241 | -4.53349 | -46.5617 | 2024-10-13 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0a028c82-354c-397f-87a1-f8b8c17554df | -4.52841 | -46.5569 | 2024-10-13 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 49d981b3-6036-34d3-89a5-a08a594d1b84 | -4.52773 | -46.56086 | 2024-10-13 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24b0becf-0ace-33ea-a9ff-aa9f1c0c6a9d | -4.28745 | -47.29911 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f83dc3d-0396-351d-aabd-a8d2fa695baa | -4.28671 | -47.30342 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4af001c8-6c82-3552-8c93-b60aefbb03d7 | -4.28598 | -47.30764 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d890c9b-3fb6-3f64-bc77-623de81b3f98 | -4.28142 | -47.29809 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| adf1f6a9-5227-360c-87e9-3e65826530d6 | -4.28068 | -47.30236 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c118ccad-3d4c-3b7e-a336-078307a082f7 | -4.07482 | -47.25327 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 029b8151-3e7d-3591-998d-7789fd50810f | -4.07405 | -47.25774 | 2024-10-13 03:47:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5217ae46-286f-33ce-af2d-a4fdb9bb968a | -3.94084 | -46.43905 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e01a832d-6c37-3aad-83b4-937a4a26ceca | -3.94015 | -46.44301 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36076ddc-5ec1-3979-8ba3-b6ba8b55445f | -3.9396 | -46.43899 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4049da2-0106-36ff-8b9f-7c7c66766a36 | -3.93945 | -46.447 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6e2f8a8-144c-3ee9-8667-a40c92453386 | -3.93893 | -46.44296 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 19940653-d547-3224-91fc-51f8e7f1eaea | -3.93827 | -46.44695 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 407292ce-98ff-3a7b-9c18-e45c2cbe1226 | -3.9358 | -46.43412 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d2264bd-804d-373e-adf4-ad2a9e3e6071 | -3.9351 | -46.4381 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69d69f43-eaae-38c6-bb6b-236fcf8c0ece | -3.93452 | -46.43407 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d94c5739-c981-3062-8c4b-d01603c6dd68 | -3.93385 | -46.43804 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2078dbb6-9d6a-35df-ba65-cb605fcdaf4e | -3.92876 | -46.43325 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6d69499c-4553-3a48-aac7-7ea24eb0a22e | -3.92811 | -46.43711 | 2024-10-13 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc9effa8-c86a-368a-982f-36d343ecc25e | -5.06883 | -46.84968 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82241b92-deec-37e1-98c2-05c3b601b6b0 | -5.06847 | -46.85143 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddbb759e-ac07-34b8-b361-7bc7bbc8e2f8 | -5.06809 | -46.85383 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eca4b98c-27b7-3865-8a5e-8a936cb95cf9 | -5.06777 | -46.85559 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90af0da6-016b-342d-b33b-9ab6361b6136 | -4.98034 | -46.80997 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 786b0259-e34c-3826-9de8-3e6397df90db | -4.9753 | -46.80478 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22276f68-5312-32f1-8bd5-b28976d64ef3 | -4.97481 | -46.80523 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1226607-d1d9-3a88-b725-f72874a7ed68 | -4.97454 | -46.80907 | 2024-10-13 03:47:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a258d3b-fed1-37ff-b52a-39d65701f8c0 | -6.2392 | -47.39288 | 2024-10-13 03:47:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8d26064-5d8d-3659-ae68-d037e0006177 | -6.23847 | -47.39703 | 2024-10-13 03:47:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b684b8-93bf-352d-a184-76e74fb639c7 | -6.23745 | -47.39271 | 2024-10-13 03:47:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c08cb0c7-d469-3152-8902-9b1f0de1cc16 | -6.23669 | -47.39685 | 2024-10-13 03:47:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54432395-62c0-3a6c-a0ea-666988a6e478 | -6.13389 | -47.27743 | 2024-10-13 03:47:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1628d5d-1946-3a93-82c0-7b5c08d48fb7 | -6.13315 | -47.28164 | 2024-10-13 03:47:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 99de53b0-c03d-38ac-bbc2-8bd787ecadb6 | -6.12804 | -47.27645 | 2024-10-13 03:47:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 60408dae-c2d1-3a44-929c-70bf4c8990ae | -6.12729 | -47.28065 | 2024-10-13 03:47:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b7b1a5e4-c1f0-3e39-a7ed-68b45bd8a698 | -5.12375 | -47.35316 | 2024-10-13 03:47:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README43.md)
