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
| b08e27ee-c75c-346d-b599-68ddcfe58036 | -2.766 | -52.5959 | 2024-11-19 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 57ccba35-b37d-3dc9-93ad-8f197df244e8 | -5.9975 | -45.3607 | 2024-11-19 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| eec5f69c-9c1a-3af1-b94f-7f5dfb6218e1 | -3.3677 | -54.0991 | 2024-11-19 00:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fafccb73-a76b-36d5-a8fb-e98c94ce80db | -3.5125 | -50.2343 | 2024-11-19 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 7500cb54-8e96-3a23-9f2b-1723b90def90 | -9.2543 | -45.0074 | 2024-11-19 00:50:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b3ef6e7d-1181-339d-a010-bf8ba74b0613 | -2.7844 | -52.5954 | 2024-11-19 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 54ed8d5c-6c1b-3f4e-a488-8337ac644001 | -6.2553 | -35.1708 | 2024-11-19 01:00:00 | GOES-16 | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| b0c6a0e5-4a66-3a3c-8a6b-ad1dfb656b2e | -5.9788 | -45.3621 | 2024-11-19 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 76bc6d8e-7781-354d-b55f-e9128f06468a | -6.2557 | -35.1434 | 2024-11-19 01:00:00 | GOES-16 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 0ae51e14-63b0-3ddc-929a-2044efb1f00d | -3.5125 | -50.2343 | 2024-11-19 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e3b07b18-4cd3-3290-982f-f01e3cebc11c | -5.9975 | -45.3607 | 2024-11-19 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a680be42-119c-3c85-bb5e-a6f13a6d8a9a | -2.7659 | -52.6163 | 2024-11-19 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ff611234-fb86-3617-b775-91e3daafb45f | -3.5126 | -50.2133 | 2024-11-19 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1403f29c-b176-3cf3-90a1-63f238a07fd8 | -2.8431 | -46.6651 | 2024-11-19 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d8e48c79-51d7-3a4e-a225-2429e1416f85 | -2.766 | -52.5959 | 2024-11-19 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 170.8 |
| c8fd3b92-191f-3403-906b-9c83ac67d838 | -9.2543 | -45.0074 | 2024-11-19 01:00:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |
| ae4b9af9-5dfb-328c-abdb-99795bac9891 | -2.5011 | -49.0375 | 2024-11-19 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 111c0914-d11e-33ee-81b9-4f912dd40ab0 | -2.5012 | -49.0162 | 2024-11-19 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e67f1e0b-897e-3477-a0ca-0e9915fcde9d | -3.5125 | -50.2343 | 2024-11-19 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e28fad4d-7ba3-3371-b5dc-c0dd72b96ba0 | -9.2543 | -45.0074 | 2024-11-19 01:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 4e5e1461-1ad9-39c0-b544-9839cad8e10e | -5.9788 | -45.3621 | 2024-11-19 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 078d4025-c1ca-3417-a1a8-e73296d281ab | -13.2638 | -56.8351 | 2024-11-19 01:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| dadd5312-be9b-37e5-ba6e-7816c464e8c7 | -2.8431 | -46.6651 | 2024-11-19 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7396910a-58d2-34fa-81d1-cec3418a59d8 | -9.2546 | -44.9845 | 2024-11-19 01:10:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| fa093fe9-8e34-3412-a0f9-32d5a51ef431 | -3.0351 | -45.2095 | 2024-11-19 01:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 1a0102f9-62ee-3d19-973e-2c0be54e65d3 | -13.2643 | -56.7947 | 2024-11-19 01:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| f6dc9467-d1b5-3790-a2da-75da62abf8f9 | -13.2452 | -56.7965 | 2024-11-19 01:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| e48738b0-ea70-362d-b415-8817e87f1e58 | -2.5012 | -49.0162 | 2024-11-19 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7a2297f0-29c7-3df5-b6c8-35ab27f3af9d | -13.245 | -56.8167 | 2024-11-19 01:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 392a29d9-7d43-3a5f-aa78-b00124175c53 | -13.264 | -56.8149 | 2024-11-19 01:10:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 233.9 |
| 0b23a7a1-cca7-3334-b3e3-d949ed0c5fdb | -2.7844 | -52.5954 | 2024-11-19 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 84777b6d-45e5-36cc-b2dd-c2b9813b1f3d | -2.7659 | -52.6163 | 2024-11-19 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 281af21e-7a60-39e9-9177-6e67c282820d | -3.5126 | -50.2133 | 2024-11-19 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| ad233eaa-7a26-338d-a94e-0f55f265ebf9 | -4.1182 | -51.0486 | 2024-11-19 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| d168d088-25f3-35fa-92b1-6998385b816d | -2.766 | -52.5959 | 2024-11-19 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| eafe2417-ef5a-3d2f-9f37-f739ec4ecc79 | -3.5622 | -51.5252 | 2024-11-19 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7899fbc6-9036-32e4-80f3-436fba99a2c2 | -4.1246 | -43.5833 | 2024-11-19 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| a8bfc81a-bf7f-3185-bb97-edda8cc72c7a | -5.979 | -45.3395 | 2024-11-19 01:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8c67cde5-b04b-3b8a-8a6b-efac134d638f | -23.9294 | -54.1011 | 2024-11-19 01:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| ccb8f362-91a5-3268-965d-f19dafd7a96b | -8.2662 | -44.0115 | 2024-11-19 01:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 479d0b8e-bd0c-35af-83a2-10294626c2b0 | -13.2452 | -56.7965 | 2024-11-19 01:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a97a5bc5-14d4-3341-ac80-3499a141463d | -13.264 | -56.8149 | 2024-11-19 01:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 2d83e22b-f8e2-3df3-a21f-c0fb9672036b | -2.6131 | -54.5381 | 2024-11-19 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 01eeb9a2-5bd2-3436-ae42-c1fd847dc33d | -3.5126 | -50.2133 | 2024-11-19 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 77377bf5-0e49-3f9b-a30f-cb86a2dbfe30 | -2.7844 | -52.5954 | 2024-11-19 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 36cdd7fd-ba5a-3a99-ab5e-3b1874327616 | -9.2546 | -44.9845 | 2024-11-19 01:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a749c9aa-8569-31e0-9a01-0969babeabd0 | -23.9089 | -54.083 | 2024-11-19 01:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| b6b9b916-574b-379f-b1b3-9ae026b6590c | -4.1246 | -43.5833 | 2024-11-19 01:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 8a7cdbe9-6227-3118-a004-395226b90d76 | -9.2543 | -45.0074 | 2024-11-19 01:20:00 | GOES-16 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 35247a66-5493-3b89-8655-fff3a2c0ad92 | -13.2643 | -56.7947 | 2024-11-19 01:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| d74f0e85-197a-3cf1-b01c-df820a67d68b | -23.95 | -54.1191 | 2024-11-19 01:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 4dde7667-d885-389c-99ad-67908a99ac24 | -2.8431 | -46.6651 | 2024-11-19 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a85e89b3-06fb-308e-a8ec-03a57af6587d | -23.9083 | -54.1053 | 2024-11-19 01:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 93.9 |
| f26eaac7-a3ae-3ef0-8d2c-28b9881e01f7 | -23.9711 | -54.1148 | 2024-11-19 01:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 67.7 |
| 6f8189d5-32be-3fad-ae18-9076805ccd07 | -4.1182 | -51.0486 | 2024-11-19 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8a6d1aba-1b8e-3dad-aa85-e447c9200bc0 | -5.979 | -45.3395 | 2024-11-19 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e3f7a090-e65d-3dde-8624-dabe41661dc1 | -2.7659 | -52.6163 | 2024-11-19 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| bcc7c255-7325-3df8-8d89-203153dcb7be | -8.2659 | -44.0348 | 2024-11-19 01:20:00 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 185.2 |
| ee8556af-d1c2-3156-8cf3-c7372ec5b4d2 | -3.5125 | -50.2343 | 2024-11-19 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 47795c17-478b-3058-be41-81513acfe786 | -13.245 | -56.8167 | 2024-11-19 01:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 56596311-d64c-3356-9fdc-6e342d2e1309 | -23.9706 | -54.1372 | 2024-11-19 01:20:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 0cfea532-b10b-3f50-8841-902b8918be9f | -2.766 | -52.5959 | 2024-11-19 01:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 187.9 |
| b3f76634-6dee-3bb1-8114-8aab0f449816 | -5.9788 | -45.3621 | 2024-11-19 01:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 184.4 |
| d58c9734-934f-36d0-98d2-9c43852bf3d6 | -13.2638 | -56.8351 | 2024-11-19 01:20:00 | GOES-16 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| bfb43add-6ffc-3d0e-8a48-6eb58691f8ed | -13.2463 | -56.807201 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a902c27-cbcb-3d4f-9e7a-140e9b016dc0 | -23.920099 | -54.108799 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1dc66909-746b-36ae-8708-139798aceaba | -23.893499 | -54.082901 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e2a13710-fcaf-3c9e-bd73-53a20bc082ff | -13.2578 | -56.812199 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29b2ac66-10a6-3f5c-8185-a226cd94ff05 | -23.896999 | -54.0984 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee53c8fd-8807-3c3b-868d-0c836cfa2b47 | -23.9599 | -54.147499 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48faed9e-4eba-3b27-b2a3-b993758e159b | -13.2446 | -56.7999 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e119bea1-e1a9-3476-bca7-c62c65717257 | -13.2595 | -56.8195 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34594d89-0caf-36cf-b435-456508384970 | -22.3013 | -49.746399 | 2024-11-19 01:23:00 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 695a83e3-f67b-3630-ad84-7f101e0692f0 | -22.3046 | -49.758999 | 2024-11-19 01:23:00 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfcff7c7-217f-3ef2-b8ac-1b81c7ae3887 | -23.954599 | -54.124298 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c4bb0411-8ab3-3ce0-b3c2-b875a5022feb | -22.295 | -49.761902 | 2024-11-19 01:23:00 | METOP-C | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4761183e-4acc-3215-9767-97634f611ce3 | -23.9049 | -54.088001 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae15b799-8315-348c-a97e-cc21d9b44f16 | -22.3307 | -52.0396 | 2024-11-19 01:23:00 | METOP-C | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2f1d1860-32a3-3349-bd85-ffe0c7d17d67 | -13.248 | -56.814499 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 707edaa9-cf22-3a7d-bf7e-15d5d87af48f | -13.2544 | -56.7976 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99eae482-5050-386b-bf43-396189d4c203 | -23.9067 | -54.095798 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d53afaf9-7971-3219-bf1d-e029b59e5459 | -23.918301 | -54.101002 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 570da1f2-5c4f-301e-bc78-62c1a7844162 | -23.941299 | -54.111301 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19a5dd12-4ba5-32d1-9074-a4813bef6760 | -23.952801 | -54.116501 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6bfb424f-90b6-3d6b-9d27-a5fc589a05e0 | -22.3284 | -52.030102 | 2024-11-19 01:23:00 | METOP-C | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 65f1dbc9-6f2f-3fa9-91d4-9262b923b059 | -13.2497 | -56.8218 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6013fb-f3e8-3b24-ba4d-ed0cd27e90d7 | -23.908501 | -54.1036 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f0c7609f-adde-37a4-bd4e-499dc33862e1 | -23.895201 | -54.090599 | 2024-11-19 01:23:00 | METOP-C | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc2d18ce-4dbd-3337-98de-18b1dd4139df | -13.2561 | -56.804901 | 2024-11-19 01:23:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 490315fe-0deb-332c-af0e-1f62a65b7d79 | -2.4294 | -54.620899 | 2024-11-19 01:25:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d54a3faf-7b2d-3d1c-a561-b799e65c2d4f | -2.6059 | -54.540901 | 2024-11-19 01:25:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1136255-4442-3b1c-ac08-e45987226a36 | -1.3425 | -55.7332 | 2024-11-19 01:25:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb069c89-2567-32db-95d7-e053ca218cb8 | -1.5305 | -60.335499 | 2024-11-19 01:25:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 301c5e50-a80c-37ae-b8ba-df29fa59158e | -2.603 | -54.5285 | 2024-11-19 01:25:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5034da0-e3a3-392f-8209-59f457f02b82 | -2.7697 | -52.592098 | 2024-11-19 01:25:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed89abda-52cb-3b50-8d78-deb52aabe205 | -1.7013 | -52.1488 | 2024-11-19 01:25:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0a4e1f1-cf55-303d-897b-7dd4d45a2c01 | -12.2833 | -57.7356 | 2024-11-19 01:25:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b32eff69-5c6d-3f4f-a417-3f707217a819 | -2.764 | -52.611099 | 2024-11-19 01:25:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba7fa281-5c81-3b71-9dab-3ce4fe982a9d | -3.5499 | -51.532101 | 2024-11-19 01:25:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd464792-b103-344c-83ee-e2d4dfdaa46f | -2.7737 | -52.608799 | 2024-11-19 01:25:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
