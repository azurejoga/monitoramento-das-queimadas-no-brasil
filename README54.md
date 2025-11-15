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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2074ebc3-755c-3a17-ab3f-a6382da374d4 | -9.81422 | -48.83941 | 2025-11-15 05:16:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56898d47-6b63-3fe1-b8f6-9570b7034cc7 | -6.16596 | -48.04847 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 775564be-b6a7-34cf-b254-295ef767d6d5 | -8.33718 | -46.6982 | 2025-11-15 05:16:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79f47707-362b-36e5-b632-fe932eb70176 | -3.01229 | -49.43236 | 2025-11-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbde88c6-8681-3071-b977-cb01e9c130f8 | -3.39527 | -52.44831 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e450c58f-9682-3677-943a-e96003486c40 | -3.23065 | -51.52335 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4060b98-31c3-36a2-a6c2-2626754e566c | -2.95647 | -48.5864 | 2025-11-15 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b70f4e-4264-3d58-9e38-1cab50316661 | -1.64565 | -55.81494 | 2025-11-15 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| eedecd90-2138-3249-b7dc-28337b4b36f8 | -2.20813 | -56.93582 | 2025-11-15 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9781b521-a205-3c01-84f5-1958b9e8ca5c | -6.17192 | -48.04908 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b75ab3e-b79d-374b-833c-dcdd1fa94b58 | -7.89102 | -48.39439 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3bb2aee-b8ac-35bf-ab00-6a04c00de5a2 | -8.32978 | -45.40687 | 2025-11-15 05:16:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b3801fe-e781-3d12-b159-28a6f1ad9b2f | -7.21553 | -47.97591 | 2025-11-15 05:16:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b38e854-f08d-36f1-b41d-42ee365d0c4e | -12.66066 | -46.74792 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cafd9063-8f8a-30cc-966e-43c5e738c617 | -11.84263 | -49.20922 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 5a78a711-089b-346c-b198-5fb8e48ed389 | -11.7996 | -48.08072 | 2025-11-15 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a655a17-8c4a-34be-af4c-593fe9227bdf | -12.15066 | -46.6694 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09caf7d4-c035-3da5-b7bf-79a21c152b0d | -10.34743 | -48.92191 | 2025-11-15 05:18:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ee5ba01-a0af-331c-acbd-883eefd665f4 | -11.32666 | -48.5161 | 2025-11-15 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8b22e14e-125f-36d0-a9a3-a5b3aaa45794 | -12.15027 | -46.66986 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f17f1f9b-9ff0-38b6-82f6-db57664a1b62 | -11.84211 | -49.21358 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5504303a-8a23-3b5c-8a3f-ca0fe5fee43e | -10.35389 | -48.91837 | 2025-11-15 05:18:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfa160b9-1370-3a80-815e-21223b287186 | -12.00689 | -46.76617 | 2025-11-15 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 405b0f57-8a98-3570-8632-18eeced07fb5 | -11.80018 | -48.07557 | 2025-11-15 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22ab92af-6e18-3c14-b661-168e5897df61 | -12.15761 | -46.67016 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51ab2d43-c846-37cd-95ff-30bfbd34893a | -12.44144 | -47.88371 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72e12736-8f0a-31c8-8277-686057967997 | -11.84569 | -49.21673 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 2a14a798-683b-317d-ac5f-ac7c84d64e61 | -11.85212 | -49.21318 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6eda72e5-0300-39bb-a25f-f0c901df3447 | -12.15654 | -46.67717 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 42027915-ce3f-3def-8cc0-6b20630ab250 | -10.33719 | -49.63545 | 2025-11-15 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 085a7f90-0120-3e8b-9593-1cbd3bda2eda | -10.34797 | -48.91749 | 2025-11-15 05:18:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6ecfe6da-e620-39fd-a4fa-8ffa5ec6b069 | -11.92128 | -46.19633 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 352bfbc5-821a-3474-90ca-639786c3d965 | -12.38319 | -48.10755 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f935eba-c4c6-3e00-b6f2-ffdc7a3acf66 | -11.70874 | -48.39498 | 2025-11-15 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6303e72-3d8b-3ed2-a1dc-dc6ccbfff69a | -11.66903 | -48.46509 | 2025-11-15 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9d8f18e-3283-3c9f-92c1-1e12e27a2aa3 | -12.23374 | -49.39277 | 2025-11-15 05:18:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98a53983-d135-30df-a908-87be302f2e24 | -11.80653 | -48.07649 | 2025-11-15 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb82c718-a989-35c6-8b11-7280035aad10 | -12.00715 | -46.7644 | 2025-11-15 05:18:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2389c294-6010-3a0f-9ad8-83dd24cc852f | -11.85238 | -49.2282 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1b4dd30-91d7-39b0-9146-94e96046b62a | -12.39005 | -48.10427 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 10eef0bf-3e5f-3c83-a285-f3617bf69de4 | -11.84803 | -49.21441 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| be413ac0-193a-3449-b6cf-66c0aa3c0f7b | -11.32504 | -48.53008 | 2025-11-15 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa435918-1a95-3994-9407-ad1111c957ae | -11.85162 | -49.21757 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a345baa8-b4c4-3d5e-82b2-22e7a36c894d | -11.85063 | -49.22624 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65b6eff5-9ab0-3ff6-b7ca-35058edd0e7d | -11.66282 | -48.46433 | 2025-11-15 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 632bec1f-8ecb-3c35-8752-06f2d8e381c5 | -11.71568 | -48.87175 | 2025-11-15 05:18:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9895375-a8d1-38de-8efe-3b0b5861a1e8 | -10.35816 | -48.7342 | 2025-11-15 05:18:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7fa11edc-34e3-3b62-a84a-193199e30cca | -11.84159 | -49.21783 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 84bca49e-25c7-309d-b40b-9fd0189cd292 | -12.44143 | -47.88824 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cc4a0e3-8c3f-3586-a5d1-efd1697010ca | -12.38891 | -48.11422 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65626ee0-655d-3311-97db-e5f50fbbf4f4 | -11.85343 | -49.21957 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 745e63ca-d9f4-3364-a74d-2a6eff736abc | -11.32612 | -48.52081 | 2025-11-15 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 427daec9-a897-3f0b-845d-cbef0266983d | -12.67305 | -46.76335 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed799720-cb45-3f31-8189-dbd41130c10c | -10.53744 | -47.93343 | 2025-11-15 05:18:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d27f496-bedd-36db-adc4-e3da108cebdf | -11.84619 | -49.21239 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 468674ef-49cb-37c0-978e-92c23cd54230 | -11.84751 | -49.21873 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f114261e-2043-33dd-8ed3-ef64fb5bd18a | -12.38524 | -48.10717 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7cb8f003-3cd9-3a76-9dde-5085d3341b83 | -12.67231 | -46.77009 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cb41abb-cf30-3367-950d-d7335f88c2e6 | -10.99256 | -47.73008 | 2025-11-15 05:18:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 938312af-b383-30d3-aaab-9d52fcf8921b | -10.35871 | -48.72966 | 2025-11-15 05:18:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1c9ffc30-8290-31de-88e6-fbfa358d7381 | -10.93621 | -48.70174 | 2025-11-15 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 409c9f44-16cb-31de-88d5-7292560f4414 | -11.84857 | -49.20999 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ee9aa148-9a49-3a3b-a70b-0b4e1f5792e0 | -12.39207 | -48.10399 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b960250-9b0c-34bd-9fa4-9c681460a466 | -11.39507 | -49.19678 | 2025-11-15 05:18:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b2e65f2-b768-33af-bab3-e38976d9692a | -11.17089 | -48.14126 | 2025-11-15 05:18:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee50d327-e562-345a-89c9-6973a520531b | -12.14994 | -46.67582 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3bae5d2-8c26-38cd-8077-9e51feae95bc | -12.15722 | -46.67065 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9aa3d133-0ade-32d2-963e-eb83e2353124 | -12.68619 | -46.77181 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c8ae9cf0-4570-3aaa-81a2-99158257122c | -12.67999 | -46.76424 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 528a7701-fa2b-3df4-bb9e-1cb31958b665 | -10.33671 | -49.63935 | 2025-11-15 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 875f7905-524e-39d8-8403-316c6effc40e | -11.8545 | -49.21076 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c51bc900-4519-3201-a473-36939de2c6b1 | -12.44204 | -47.88259 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3419ac1d-01cd-3cae-934e-38bca0e35fb6 | -11.8452 | -49.22103 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4752965b-ad05-31c5-b709-3a259cbe60fa | -12.67925 | -46.77097 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 490fe3a8-8981-3f2a-b2e9-ca7de26c99d2 | -11.85262 | -49.20871 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| aa907d52-2717-3e9a-8dd5-327941ae3a38 | -11.84669 | -49.20792 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 371bdbdd-df4e-31ed-be1c-b1c84197e481 | -12.4408 | -47.8893 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f1f1568-606a-3bdb-b8b0-57b63285ad44 | -11.32558 | -48.52543 | 2025-11-15 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a63e28ea-0688-38a5-a285-a385030e0e3a | -12.15688 | -46.67668 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed340d8b-541c-3529-a460-d3984850cacd | -9.24635 | -57.25529 | 2025-11-15 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a439d1cd-5a65-3f2d-a22a-627d2b8e5f21 | -11.8529 | -49.22391 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05553baf-646a-39fc-9237-65676163fed4 | -11.71512 | -48.87659 | 2025-11-15 05:18:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3561a85a-9427-3a2e-81dd-8dc551a9cc4c | -12.68694 | -46.76509 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0fa63861-843c-3dea-8906-4598fc4397ce | -11.70933 | -48.38996 | 2025-11-15 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf8bb224-a587-39e8-b7be-47cc088d3d6d | -11.85396 | -49.21518 | 2025-11-15 05:18:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acacf3c2-1f9e-3ea1-be20-879ebb8ab48d | -11.17147 | -48.13619 | 2025-11-15 05:18:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cd3bccf-71e7-34ae-b5ac-2076283c3012 | -12.38947 | -48.10936 | 2025-11-15 05:18:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7d9f6ee-e3e5-3357-b277-88929053570b | -12.23964 | -49.39344 | 2025-11-15 05:18:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c8daad4-f34c-3944-9cfa-447a2504edef | -11.9268 | -46.21199 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c2d74c32-c8d3-371f-9bd9-d36828cc91c7 | -12.67852 | -46.77754 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| de230c86-3181-39d1-86d7-cbfc882d5ae7 | -11.9199 | -46.2092 | 2025-11-15 05:18:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 166e817c-04b0-3b3e-9374-88d55d6fa44f | -12.6864 | -46.7632 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 1b1287f6-d5b0-3225-a6c5-1f085d902529 | -12.88176 | -50.1566 | 2025-11-15 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e40e93cd-eb85-3140-92e8-dd61ca48a76e | -12.99452 | -49.80101 | 2025-11-15 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb78da78-8e6f-369a-b9ed-65d3f26d0eb3 | -12.68569 | -46.76995 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 99e1333d-871e-3d0d-b95f-dc3e1d6d1495 | -12.65934 | -46.75264 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af20ca09-b52e-3068-9000-50e820a9ce78 | -12.77858 | -46.95453 | 2025-11-15 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b162efec-5c68-3cd9-84c7-390862d78d25 | -13.06622 | -53.95515 | 2025-11-15 05:18:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6f7069f-8503-3427-9962-6ecd984cf0b3 | -12.8761 | -50.15594 | 2025-11-15 05:18:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1fd3f75-f9d5-34d1-9ab9-0c4838f17a44 | -12.97159 | -48.84292 | 2025-11-15 05:18:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README55.md)
