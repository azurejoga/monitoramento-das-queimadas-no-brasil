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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3b2baf4-91d3-3b2c-880b-a82cb6646b3c | -3.9217 | -46.91215 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3e91ae0-cbdb-372d-a4c9-79ea33973e42 | -1.83133 | -46.22063 | 2024-12-22 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5526725a-8408-3fc7-88ff-d7262ec6918e | -1.31141 | -53.52289 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 542745f9-4490-3a1f-a010-82d0954981ad | -3.37685 | -52.8095 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f9191665-d124-3634-a633-d81615494214 | -2.97748 | -53.89162 | 2024-12-22 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a71090d5-bde7-33a3-871e-7ac5d57bbfd1 | -3.81064 | -46.71507 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9d5745a-04f8-33c1-8d62-aab02580e6bc | -1.53835 | -54.20637 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eabe46f8-b438-371b-87a0-c0dbe2080fe4 | -2.23764 | -46.26847 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69bd40fc-ee2a-33b1-86c0-af8960dff381 | -1.17622 | -52.54486 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d3767e4-90ff-3597-94ac-bcb8bdf0e3a3 | -3.78747 | -47.11193 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 547fa5c8-ba35-35f5-87b8-3346cac34c73 | -2.50268 | -49.06308 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc6f8183-0e91-3d2f-a2d4-da01791dafd6 | -4.0064 | -46.55969 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d899027b-7461-3415-9ea2-32db2ce48919 | -1.29691 | -47.75049 | 2024-12-22 04:50:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0694c13-28f0-3751-bd67-d3774634d933 | -1.70383 | -52.58733 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ad2207-9d55-3399-a243-44e8b7ad356f | -2.44773 | -51.79448 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ffe4113f-4cc2-305e-bce0-c31ec11725c5 | -2.63334 | -48.03397 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55cf36d5-8f9e-3833-9904-247df28293d4 | -3.90609 | -47.01326 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c302aa47-a05b-3897-9a91-d510a233ecf2 | -2.51955 | -54.22612 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c881588b-b518-3dc5-8276-baffb51aced9 | -1.18628 | -52.54642 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5f98bd8-82d8-3258-a893-71cd50734606 | -2.57732 | -49.46233 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20ba1ebb-4cbd-348c-b995-c3bda0ec9fa1 | -2.22859 | -53.79295 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f8a119d-5204-3c55-bd20-b5fe65396df0 | -2.80216 | -46.7494 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f748183-2ea1-3464-bc5e-e687bbe07f84 | -4.07875 | -46.62185 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4c83e62-1d8c-370c-b9b8-d28bd67ef201 | -4.03138 | -50.05511 | 2024-12-22 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c14a28d-50e4-3a1f-b527-64c15aa0273f | -1.70251 | -52.4222 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 558b18f2-7174-3b1e-bbef-7d69b8b1cdd6 | -3.50514 | -47.19772 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c48d50a8-749d-3660-a637-dc4302a5f46b | -1.86329 | -48.00324 | 2024-12-22 04:50:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e13ce525-c214-3af0-ade1-a6a713d46ef6 | -2.77695 | -54.35565 | 2024-12-22 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1d0d604f-fc88-36e3-899a-64e3d9f7e554 | -1.03921 | -47.22881 | 2024-12-22 04:50:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e6b6071-207c-3f82-9e2c-7935a968f1c3 | -2.04619 | -52.1099 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ba394130-494c-337f-b652-d145bd29566f | -1.70381 | -52.56575 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f94a6d0-92f4-38af-b5bd-b74e7ac62ab6 | -1.71278 | -52.59592 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44810b63-27eb-3447-b787-d394e245e49f | -1.53774 | -54.21026 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c447260b-bd89-33b9-905b-d279e33956db | -3.20973 | -52.86564 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70eb8f5b-1ba8-3064-ab11-faeb2d51cfe4 | -2.81928 | -52.97819 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bff3f63-4518-3363-893a-d31500447964 | -2.56623 | -49.46458 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23ba99bf-dadd-3d64-939e-e5250f4e71c0 | -1.36748 | -53.69614 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c336ea1f-5690-3675-8974-78043c029413 | -4.10512 | -46.81715 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926cef09-636d-389e-baf3-fb4aad2585af | -2.88349 | -51.79912 | 2024-12-22 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2b537a4-a3da-3c84-932f-623ea4fbb684 | -1.71668 | -52.59293 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1927112-24da-360a-ae7e-70d139fd2394 | -2.44441 | -51.79396 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26275c1c-3df3-3fe3-9a26-71b78ec92d58 | -2.90173 | -54.49858 | 2024-12-22 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83451c24-601b-33e0-be07-3b703fae4fe4 | -4.01866 | -47.05844 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9a146388-e92b-346d-8910-1f9095f72176 | -3.83724 | -46.68041 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4657167-6735-382f-ad25-9128de8327b2 | -1.30796 | -53.52237 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48ce6674-cd25-3e67-baf5-7cf248c67180 | -2.14835 | -53.5943 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e903f6f5-e1d2-374d-b7b6-5b8a044ce2d1 | -1.36587 | -53.68407 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d1a8029-afda-361c-9dbb-0c081d3135d4 | -1.57547 | -54.04066 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b525e864-3d70-3efa-92e4-23a0a354410b | -2.44109 | -51.79345 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 741f203d-d282-308d-b2bc-a951116eca30 | -4.09555 | -46.73916 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b3e7b48-31a9-31e6-8d8d-9788c5aa30a1 | -1.50318 | -52.63919 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6d2fa88-34f5-32bd-bffd-0488b87b08cd | -0.78393 | -48.78158 | 2024-12-22 04:50:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97e2a666-382c-327e-aa97-7749d8ba9f25 | -1.37318 | -53.70486 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b27b7061-6fec-3d81-97b7-e94ab3af6804 | -2.819 | -48.25421 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3d0a5fb-d4e1-326b-b056-e7ea44067227 | -1.32922 | -52.3031 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e947191-4768-3214-937c-c2678fbc659c | -4.81515 | -44.40995 | 2024-12-22 04:50:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1729e96c-77af-3bc6-8b54-cfcb938a32d2 | -2.81968 | -48.24981 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9aa9a002-48b4-36cb-94cf-7450d92cf76c | -2.68167 | -54.84358 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4a8420d-4088-3e2e-9527-fd6dbc05e11d | -3.36904 | -49.17085 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8291dfe8-f6c5-3b95-9b10-d44e34d6aa99 | -3.60043 | -50.63181 | 2024-12-22 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bda0212-1c86-36b5-a5f3-de25a3ebfa3f | -2.25087 | -48.31499 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a666621c-017e-372f-b46e-1da2de440d35 | -2.14492 | -53.59378 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd98c330-863f-30f9-a965-351d67f0ddcd | -2.56914 | -49.46897 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 83724e4e-ed80-331f-b57c-03b17cc8d374 | -4.5576 | -43.29855 | 2024-12-22 04:50:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 13ef3595-7bcd-3a32-bc00-9b1c607cf49a | -3.1734 | -45.9795 | 2024-12-22 04:50:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae0f2058-63af-345e-86b9-43c93aecd66d | -2.63404 | -48.02945 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9ffa556-462c-3a1c-9509-e6a2bda778e2 | -2.83087 | -54.56118 | 2024-12-22 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 141f99c3-c768-358d-a1e0-0f570b96b757 | -1.41294 | -46.48542 | 2024-12-22 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7077067c-c4f9-3fc8-9313-321af2e4d41a | -2.99533 | -54.09061 | 2024-12-22 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04ec4b52-14b4-3944-9c91-1c57349d781c | -2.56344 | -49.45729 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 626de43e-27ec-34f2-bf20-20da65302014 | -2.04013 | -52.1089 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68e1bab8-5fd3-3e0e-98d0-06c8a448232e | -2.74982 | -44.76753 | 2024-12-22 04:50:00 | NPP-375D | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6982fb59-40fd-374d-b567-0479b75fc265 | -2.0554 | -46.59332 | 2024-12-22 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95f1debe-597f-30b2-b614-226ddf97b34e | -2.68991 | -54.84782 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4270bcb2-6d28-3df1-ae42-4bf2ea5e2ff7 | -1.34523 | -53.53207 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f38e0026-3a80-3343-889c-c4b4d06b81b5 | -4.00218 | -46.55909 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 279d241a-b96e-3aa2-a852-2bbdbb83755d | -1.71944 | -52.57539 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 774a3620-4fe3-305a-a775-838ed60a80f4 | -2.57151 | -49.45353 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9bb0768b-f012-3f07-b2ce-d134d72c3fa2 | -1.37156 | -53.69282 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8281b80-2e6e-392b-8944-03e5810c9e45 | -3.83605 | -46.68815 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7786575-1d6f-3d88-8720-8983f1180fcc | -3.98116 | -48.39603 | 2024-12-22 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7622c74a-d1d3-3a0e-82a1-5ee953ddbf06 | 0.00198 | -51.19562 | 2024-12-22 04:50:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4712197-3a32-3c05-ad3b-b931a41509bd | -2.57323 | -49.46565 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2aa06531-d259-38c0-b9d7-50f5f9646a0f | -3.80278 | -46.84985 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa02c378-75e8-3e93-ba62-86eac23b87c3 | -4.95536 | -44.00677 | 2024-12-22 04:50:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5800f749-26b4-3805-bc7a-96c0e5af6a9b | -1.43496 | -52.63574 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2513b488-c10a-347d-9244-f4d31c4e0460 | -1.88973 | -52.07496 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bfcdb8a-d703-3719-997e-7f7a776800be | -2.80161 | -46.753 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4049296a-07ab-34e0-aba2-96086352f5f0 | -2.99801 | -48.0222 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f871ce6-6694-3382-8ee7-209030f8305b | -2.4976 | -48.06615 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47a84ffe-2471-3de3-8fce-666a025e4ca0 | -4.10154 | -46.81274 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52479927-1058-3033-9c0b-293f109eaa6d | -2.50204 | -48.06227 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6dc0d1ea-0b66-3571-aeec-4e20b207779d | -4.0151 | -47.05437 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8331a92-a6d2-3614-8cbe-6caec8177375 | -2.99103 | -51.44036 | 2024-12-22 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e677632-5286-3049-bbb2-ed081c7e5d6b | -3.98657 | -48.41077 | 2024-12-22 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4a571e3-6f64-3493-9947-540187164e9e | -2.72357 | -45.93325 | 2024-12-22 04:50:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 396c31e3-1d37-3317-8cd9-d75753c02062 | -4.1039 | -46.74034 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f2fdcdf-2140-37e5-9791-20b60704a6d9 | -2.57904 | -49.47443 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c1b563e-cde2-38ea-a799-06d22a050ed6 | -2.57964 | -49.47057 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2a447c6-38dd-32a7-8e48-7802a818786f | -3.17731 | -55.01294 | 2024-12-22 04:50:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
