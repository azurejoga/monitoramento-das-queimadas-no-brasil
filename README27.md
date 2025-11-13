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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f29f8be9-46d0-39d5-b4e9-b6c9baa86cba | -7.22776 | -47.9827 | 2025-11-13 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 448411b0-884a-3d0b-80ef-07c223c94d5c | -4.40822 | -50.81962 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5e305c5a-4697-3356-bd60-0f6aa2301069 | -2.89077 | -48.08137 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e13621e9-2775-3d0c-80ae-6599911a2853 | -4.10865 | -48.01717 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 97411348-dd03-3de6-860f-2f241222de75 | -7.18573 | -44.9828 | 2025-11-13 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dbdd663-f0ff-342e-af65-78422d562250 | -3.34628 | -48.38681 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edaca53a-aedc-3e71-9a7b-8391b3ffc864 | -4.77734 | -45.42578 | 2025-11-13 04:42:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a28e36cd-85e4-3bab-85e6-5bedafb104dc | -2.93548 | -47.32518 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e2364da-d8e6-3cf3-bfe3-7688180b6c88 | -2.92806 | -51.7573 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa31e3a3-8a40-3f19-9044-3c24ef7fafff | -5.02198 | -46.83435 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67706e68-b25e-38a9-8c21-3427d9c24d70 | -4.71778 | -49.24321 | 2025-11-13 04:42:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b49244fa-cffd-3566-822f-7feabf4b6620 | -2.43831 | -49.23145 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 557b21cf-df0a-30d1-9336-8e60abad1ff1 | -3.44329 | -45.58252 | 2025-11-13 04:42:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f44ecefe-1391-307e-8a7c-17b800c35a99 | -2.63197 | -47.30055 | 2025-11-13 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a4bf067-bde7-333a-9d30-4872f6e07b49 | -6.38094 | -39.49404 | 2025-11-13 04:42:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef40ba60-d8c1-3934-a08d-45a3621b2cb9 | -4.44607 | -38.395 | 2025-11-13 04:42:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4bfd1619-5365-376f-9142-305ff8615c85 | -2.89131 | -48.0779 | 2025-11-13 04:42:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e9be9bd-f459-3f39-bc8a-b07289d272b5 | -4.92284 | -49.99924 | 2025-11-13 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3527e2e4-92ee-37d7-b3b5-7767f53bdac3 | -3.36682 | -48.40773 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f0e2336-b80b-397a-8a47-9ce26c930e31 | -6.16282 | -48.05466 | 2025-11-13 04:42:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ed019cd-3c38-3a81-b3b2-b5684830db29 | -2.63534 | -47.30108 | 2025-11-13 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80d1726e-c7d7-3059-bee9-e84651179a42 | -4.38498 | -50.87661 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95787c67-8719-3f39-8b4e-f5ae4d4e44a1 | -3.6694 | -45.92995 | 2025-11-13 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| db6cd6fb-3ecf-3c5c-80dc-62bf049ba5ea | -3.08445 | -49.2766 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| acb7458f-2283-3a9e-b2b9-ce30c1e21f47 | -4.17025 | -48.78527 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 335118f5-ba5d-3abc-9e9d-36a58df612d9 | -5.24335 | -42.64046 | 2025-11-13 04:42:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84a5d498-2828-339b-82ed-aae391d19fea | -2.55785 | -49.11853 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c65567d9-0a2d-3df5-8ff3-384ff9888c33 | -3.63931 | -50.58325 | 2025-11-13 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ad0a701-926e-3019-bf6d-71669865072c | -2.82353 | -45.44504 | 2025-11-13 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efd1a768-115d-3f76-be0d-a6cc6290d392 | -3.7013 | -49.03321 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bbef2c3-e378-3e32-bc8c-0c7ce8c5affa | -3.34961 | -48.38733 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9709ab0a-dbc1-32e1-be89-e550c1ef4e06 | -7.0775 | -41.58797 | 2025-11-13 04:42:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 081f3c85-8349-3c47-90a6-149a1cc0cc31 | -4.21398 | -48.57256 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 7ece895e-a497-33dd-bf11-21ec670a0f96 | -5.3889 | -46.76593 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fc51a90-11b2-38ac-a046-cc29216b2494 | -4.00502 | -48.80494 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e43e950-4396-3de1-9809-256c543c7e92 | -7.30097 | -45.28217 | 2025-11-13 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 124e607f-487b-32a5-a6f7-26893c0008e4 | -4.74562 | -49.89538 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71a4fa8f-272a-35b7-96e9-07137784a262 | -4.31027 | -48.24236 | 2025-11-13 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1ff666b-d7f8-3f36-aa1b-1e6e7c76b542 | -4.36057 | -46.13968 | 2025-11-13 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab74de34-f8f4-30b1-bee8-4cb7566a5ffe | -5.15035 | -50.87523 | 2025-11-13 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1da8b85-2438-3452-8d7f-c73312701288 | -2.37195 | -55.80263 | 2025-11-13 04:42:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd7d0315-6f66-37a1-b67f-8bca92687c31 | -3.03586 | -50.29152 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9867dcbf-9588-31d1-8bb7-92aa8984c579 | -3.2908 | -49.01805 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de34773e-82f3-33bf-a36c-72b3972c80bc | -4.72795 | -46.72826 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8841ee2d-0cdc-383a-90bb-bcad0a373165 | -6.8822 | -42.8526 | 2025-11-13 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5cdddb48-a10e-3216-ba0f-55bc49e5c8c6 | -3.31125 | -49.46529 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4823c83e-4e4e-354b-9d76-b5a6ccefb379 | -3.22937 | -45.59131 | 2025-11-13 04:42:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 12fc270d-dd9d-3525-827e-0f2f79f451a8 | -6.48674 | -48.3672 | 2025-11-13 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54da8e6f-a5eb-36cd-8677-775d24f4d6dc | -3.08887 | -49.27018 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e937323c-31e3-31fd-b1d7-2e4585879209 | -7.39433 | -48.66051 | 2025-11-13 04:42:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ee3969-5feb-3288-85fc-d5d0372225e6 | -5.2623 | -42.99641 | 2025-11-13 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09ff3c85-17b7-3f18-9222-9112cc1942bb | -1.70146 | -54.67452 | 2025-11-13 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fd0f5d5-8c27-3311-adeb-886cabc84a5b | -4.45199 | -38.39591 | 2025-11-13 04:42:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90e8009c-5f02-3f76-b5f3-59b3054a2643 | -4.84293 | -49.26272 | 2025-11-13 04:42:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c32fe290-399c-3ab7-b04b-9c71355c93e5 | -3.47087 | -43.19195 | 2025-11-13 04:42:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b940cae0-36cd-36e4-9ed8-64249918e487 | -1.93633 | -52.09887 | 2025-11-13 04:42:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9faf1a33-5438-317b-be7a-bf2b56cea465 | -2.63907 | -49.20275 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62001966-3cb8-3f29-a56b-7d29689780bf | -3.26237 | -50.03149 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d100c540-2fb2-3f14-82f0-034412dbf133 | -2.63186 | -49.20518 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ba4e29-4833-3705-b19b-fd698aa43573 | -3.08499 | -49.27313 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d86fd84-e46f-3e3b-a35b-33ecb9d7f7dc | -1.85642 | -55.29969 | 2025-11-13 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51e6139f-08d8-3149-925d-3375bc3c702c | -4.9326 | -48.54625 | 2025-11-13 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35bdbc4f-08d8-36f5-859d-364282e566b0 | -4.01497 | -48.8065 | 2025-11-13 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4985381-8ef8-315e-a1ba-ca445bff2722 | -0.88443 | -52.06227 | 2025-11-13 04:42:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed608383-a87a-3e9a-94ae-e63044fb21cc | -5.88524 | -46.44342 | 2025-11-13 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54c728d1-34d0-3d8d-9dfa-f89169ab25f0 | -3.09275 | -49.26724 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acaa483f-2a4b-3d83-a714-715ab172d4b1 | -4.89269 | -48.96952 | 2025-11-13 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fe9bcc6-a860-33c2-a42e-613ab6acf9f7 | -3.15106 | -50.26827 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2a713bdd-7853-3c09-8e12-85ce3d9fd7c5 | -2.45369 | -49.25878 | 2025-11-13 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 89099e1a-a749-3f23-b201-ed28bb344a9b | -6.15944 | -48.05412 | 2025-11-13 04:42:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c66fa06a-73ae-3b2e-be25-6fcc22697320 | -1.37644 | -55.39842 | 2025-11-13 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65c0706a-6dce-3d4d-be32-914eb7cbf5c5 | -5.75424 | -45.10625 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12e354b9-860c-3a48-96e2-0c464dc80165 | -3.37346 | -48.40877 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2c2fc6ed-b3ed-323e-9867-94ed3b0ac2c8 | -5.33102 | -44.78786 | 2025-11-13 04:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c468cff6-1415-39aa-8194-f52f6d0477d8 | -2.63574 | -49.20223 | 2025-11-13 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 428bbec3-d701-3a5c-a884-6db6827f7b45 | -5.55348 | -46.86835 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 964c9192-e1d5-3054-ad92-7f2237dc659f | -5.6215 | -46.91437 | 2025-11-13 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89304a9b-cafb-35c9-8dda-fd89fb2ffe3c | -3.66877 | -45.93402 | 2025-11-13 04:42:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca23f17b-a48c-3276-a6fe-7402f5c7b7b6 | -3.91255 | -52.12876 | 2025-11-13 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 597ea800-65de-3ddb-a408-1d3b6cd2db9b | -3.37237 | -48.41568 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e313df5-cdaf-3639-a03b-220ec3fec523 | -2.87305 | -51.47376 | 2025-11-13 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2379da83-aabe-3237-88ff-3546c3458c20 | -6.87766 | -42.85204 | 2025-11-13 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8f2c23c6-286a-37b1-8aa0-334cd141b947 | -5.36618 | -45.07723 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c828b0fb-7155-3c4f-a7e3-4040ac1fa03e | -4.25412 | -43.78632 | 2025-11-13 04:42:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| adc1b26a-c806-35f1-a8b7-9457f69203d1 | -4.10196 | -48.01611 | 2025-11-13 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f543e02-9787-37c5-a597-7583e26e6af8 | -7.22186 | -39.9564 | 2025-11-13 04:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| eaa7e2c3-e1de-373f-afc9-bf3d49eab424 | -7.80038 | -42.62309 | 2025-11-13 04:42:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| abefb4b4-2795-3179-bd4c-e40983d0dcaf | -3.03246 | -50.29101 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 716c0ea4-74f4-3ea2-bb34-5738784fe803 | -3.34378 | -48.38662 | 2025-11-13 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee9e5f4f-356c-3b52-9402-e4c3be2b0aa6 | -3.10579 | -45.77027 | 2025-11-13 04:42:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1d09617-9b20-3497-baad-9326fc8aa180 | -4.83564 | -48.08324 | 2025-11-13 04:42:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7df7099-85cf-3b8f-a97d-c6ea1d1d740c | -3.46787 | -50.58283 | 2025-11-13 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04655eaf-76a5-3229-869e-4dfaed64b39e | -6.2963 | -41.73955 | 2025-11-13 04:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 325d1e5b-1f49-3531-bb9c-51e7f07942e3 | -3.7844 | -42.75729 | 2025-11-13 04:42:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbe36899-a6fc-3e9e-8de7-46b6a9c4207f | -4.71086 | -46.44358 | 2025-11-13 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| b0d3c708-8531-3a7a-838a-91493b35dbf7 | -7.35819 | -47.81309 | 2025-11-13 04:42:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f60e7c7a-7311-3047-b1c8-6bc32b3773c7 | -6.34835 | -39.79256 | 2025-11-13 04:42:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b09c9c29-a4ea-3de3-9b40-8f2a6b791619 | -7.78184 | -43.7972 | 2025-11-13 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| edf99f00-7648-30da-bd00-56e2a251e59d | -7.13412 | -41.8836 | 2025-11-13 04:42:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e9380d5-deeb-33c9-8c5f-8e61b700d7c3 | -5.32843 | -45.19589 | 2025-11-13 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |


[Clique aqui para ver as próximas entradas](README28.md)
