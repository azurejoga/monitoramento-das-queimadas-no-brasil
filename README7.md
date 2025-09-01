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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fafc9ea-3488-3048-bde7-4021dd3fb9e2 | -11.045 | -47.0514 | 2025-09-01 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 51dddcfd-51c4-30d2-892f-1fde6b9af001 | -11.026 | -47.0538 | 2025-09-01 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 251.5 |
| c6038bbb-ad19-3310-adb5-8f733ee1e4f9 | -6.4602 | -43.9764 | 2025-09-01 01:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5e789fd6-4df4-3f7a-883f-486f664d2d83 | -7.9335 | -73.0052 | 2025-09-01 01:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 59d22703-5815-31b1-9ed8-dd76bb99ab8e | -9.135 | -65.5453 | 2025-09-01 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| fe4514f1-b777-3ab4-89d3-e1698b6399f0 | -10.5937 | -44.331 | 2025-09-01 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 68bbb4f7-a43d-3cb9-9df8-97da5c126b72 | -12.9194 | -56.9672 | 2025-09-01 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 139.4 |
| e1750ce3-7152-3801-8e0f-974ada5db151 | -6.8095 | -52.8154 | 2025-09-01 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c8c2c269-c7a9-39b9-959c-481543a19084 | -11.0256 | -47.0762 | 2025-09-01 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b368f212-2cd8-37fd-87b5-ca11c9fc417e | -7.0948 | -44.3358 | 2025-09-01 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 2e9aed9a-1155-3ae2-b2b7-c48c3bec2611 | -7.0946 | -44.3589 | 2025-09-01 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| ee0503a5-d1a6-330b-8f8e-d1959b57ac6d | -11.0454 | -47.029 | 2025-09-01 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 74cb3a60-bef0-38f7-89fe-b553ef5ec691 | -6.4793 | -43.9516 | 2025-09-01 01:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 0e1c0a3b-fb4a-3e3c-911e-2ffda1b6f2d7 | -9.0799 | -65.4349 | 2025-09-01 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 6965c806-cf80-34f8-9ff4-722ff148dc09 | -6.8281 | -52.8143 | 2025-09-01 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a2bc25d5-9b4c-31ee-8cbf-a21595b1c8da | -15.5862 | -48.3435 | 2025-09-01 01:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 64e413ae-35a5-3f9d-b0d8-63cd463ca93f | -13.1644 | -45.2897 | 2025-09-01 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| ae6a420b-c19f-395b-968f-fdeea3348e76 | -6.8279 | -52.8348 | 2025-09-01 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| fa4a70c4-0015-3d4c-954b-e967451f651b | -11.0381 | -45.1256 | 2025-09-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6b05af8a-4b2b-30c9-a343-90953fff29d1 | -11.3705 | -43.5868 | 2025-09-01 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| e57e5df2-b062-3156-9ce0-584d9728db2e | -9.2825 | -47.1007 | 2025-09-01 01:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| a7a39f2b-0d2b-362c-948b-3e5d8a4fff04 | -15.6063 | -48.3177 | 2025-09-01 01:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 36a37808-bc66-397b-9526-665903cd17ba | -6.8466 | -52.8132 | 2025-09-01 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 13a42e79-3dd4-3da0-9bd8-a3f98ba1626a | -12.9387 | -56.9454 | 2025-09-01 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| ba691da5-cf62-3d00-a7d6-37b7e29c97b9 | -7.9335 | -72.987 | 2025-09-01 01:30:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 14ac3ef7-ff2e-3720-8f06-0a5872913a0e | -12.9197 | -56.9471 | 2025-09-01 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |
| 1fdd11c5-eabc-35df-8448-c4d665a6e0f9 | -11.0377 | -45.1487 | 2025-09-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 62131f85-d047-3994-80cf-9cd41692021d | -15.7112 | -48.9032 | 2025-09-01 01:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 8e953d83-72c1-33de-821b-bdccb92aca3b | -11.0263 | -47.0314 | 2025-09-01 01:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 9935aefa-2db0-3a0a-ac8b-f1393d620ebf | -6.7438 | -43.7898 | 2025-09-01 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| b92d5d5b-baf9-37bd-8f02-7e96fde12d05 | -10.043 | -48.1218 | 2025-09-01 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1b868229-c08c-35ec-ad41-ac02fca3e4c2 | -6.4605 | -43.9532 | 2025-09-01 01:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 38579fdb-cb12-3b33-b49f-2ec3ec6996c0 | -7.6783 | -61.0908 | 2025-09-01 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 37647d0a-3c53-3b1b-ae56-4ab374fd570c | -7.0757 | -44.3606 | 2025-09-01 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 3d3edd96-9a89-3f16-8150-aab4e402d391 | -12.9385 | -56.9655 | 2025-09-01 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 5aade9ab-5f2c-3017-ac27-4c180531465e | -12.9006 | -56.9488 | 2025-09-01 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d49309ae-b881-347b-97b3-9097acecc24d | -13.1648 | -45.2665 | 2025-09-01 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d125ad01-78c9-3feb-883a-0105e986f4cf | -15.6916 | -48.9065 | 2025-09-01 01:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 681232b1-53e5-3964-aeff-d771abfe50de | -10.0434 | -48.0998 | 2025-09-01 01:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f7e69287-04f1-3d9e-aea0-38082061a1e4 | -11.3709 | -43.5631 | 2025-09-01 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f998c641-644e-3a40-9955-e59ba9f0fe45 | -10.6128 | -44.3284 | 2025-09-01 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0c622f45-9e08-32d7-8bfd-6d3e5e79f480 | -11.3696 | -43.6341 | 2025-09-01 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 61769883-e58c-3ac6-8c8b-9530575eb4d0 | -15.6058 | -48.3402 | 2025-09-01 01:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 5b670c1f-027b-33f4-a3d8-da031133d54c | -13.1837 | -45.2865 | 2025-09-01 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 40148586-5913-33d0-b8cb-9a51464b3907 | -8.6468 | -67.2515 | 2025-09-01 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 285d6c39-6c42-35d8-b3d9-85d1353ebf4e | -9.1165 | -65.5459 | 2025-09-01 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 0213c797-115d-34e6-bf99-798606d9dd1c | -6.4793 | -43.9516 | 2025-09-01 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| e7b33d9c-443f-370a-bbfb-50830ab23451 | -7.9335 | -72.987 | 2025-09-01 01:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b82a2836-4de1-32b1-b184-f17f171afbd6 | -7.6783 | -61.0908 | 2025-09-01 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2e3acb3c-c2df-307e-afbe-e9b26b840af7 | -13.1648 | -45.2665 | 2025-09-01 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| a114c3d6-8e9a-3a89-9c54-9c9161d9e5da | -15.5862 | -48.3435 | 2025-09-01 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0050c73a-2445-35d3-a869-0ff26df54132 | -7.0946 | -44.3589 | 2025-09-01 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| dfeaf291-4469-354c-83bc-7055a49c9feb | -6.4602 | -43.9764 | 2025-09-01 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| f534a4cb-c2b6-3019-8b4b-456d44abf545 | -6.8095 | -52.8154 | 2025-09-01 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 65de8fe0-9e76-3d97-98cf-2959276c64a7 | -7.0965 | -63.0437 | 2025-09-01 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| be9f7704-787e-30eb-854c-4ff51e5c5475 | -11.0377 | -45.1487 | 2025-09-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d1313605-98a2-35dd-9cad-07000793c6b1 | -7.2929 | -60.667 | 2025-09-01 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7ab3a3c3-590b-382b-95db-a5e3834f04df | -7.0757 | -44.3606 | 2025-09-01 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 81b6989f-a671-390f-be20-d76fb7f9c502 | -15.6053 | -48.3627 | 2025-09-01 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fc660860-db6b-3000-bd7d-6c7b681deb36 | -8.6468 | -67.2515 | 2025-09-01 01:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 97495a7c-6173-3f51-b528-4fc9ac2f366d | -6.8279 | -52.8348 | 2025-09-01 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fa121e85-2329-36fb-8635-9e1eaa06bc24 | -11.0568 | -45.146 | 2025-09-01 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e918beb6-ecfc-3a5f-8e94-3dc1f862bc55 | -7.9335 | -73.0052 | 2025-09-01 01:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ea76dabd-3a48-3b1d-940b-04785b1d4ddd | -13.1644 | -45.2897 | 2025-09-01 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d5f3ec92-25be-33a8-a6a0-e603eaf3bbfd | -13.1837 | -45.2865 | 2025-09-01 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 75a97738-650f-3794-b3d2-57583bfc2d0f | -19.0724 | -48.3148 | 2025-09-01 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| adffb4d1-d94e-3ed9-b718-55ba1c93ab70 | -7.0948 | -44.3358 | 2025-09-01 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 180.4 |
| ffe2f9a8-e455-3d12-a9d3-5cc1a78aba96 | -6.4605 | -43.9532 | 2025-09-01 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 333.0 |
| d4f4598a-cb50-330e-8cb1-39e736958a62 | -7.076 | -44.3376 | 2025-09-01 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 6518a13c-3ffd-3be0-bd42-e47a120131b7 | -15.6058 | -48.3402 | 2025-09-01 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 172.0 |
| e69fe113-a47d-3c92-abb5-83a7ac1e2898 | -4.9124 | -43.187 | 2025-09-01 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 242d9199-5be9-33fa-9fe7-ddf7d032d4d8 | -13.1842 | -45.2633 | 2025-09-01 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| bb132538-104c-303a-bab4-659f32004299 | -11.0461 | -46.9842 | 2025-09-01 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c291f624-7ce1-3adc-976e-ac4ad2e8800c | -6.8281 | -52.8143 | 2025-09-01 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1691773e-cb0e-352c-9537-e1d8af25db92 | -15.5867 | -48.321 | 2025-09-01 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a7fcb12c-6fd0-3bcd-a0f9-5f453ede62fa | -12.9194 | -56.9672 | 2025-09-01 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 43fcc483-af57-33ad-879e-013b0e32ef3e | -11.045 | -47.0514 | 2025-09-01 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| c69cdba5-f008-3bca-a4cf-fab60c95e9bc | -4.9311 | -43.1857 | 2025-09-01 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 8d6d0384-6eb3-34f3-b8c3-28cd741f3e8f | -4.9125 | -43.1636 | 2025-09-01 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 64f371a0-a455-3bb4-a0d8-6d7e04359bfe | -12.9385 | -56.9655 | 2025-09-01 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9aafefdb-fc21-3d21-831f-5b9ae1a0ee3b | -9.135 | -65.5453 | 2025-09-01 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 684ae02d-e513-3b58-b088-40633c828e8d | -11.026 | -47.0538 | 2025-09-01 01:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 5173c499-ae99-342b-b3a1-fa779c4f0327 | -10.0434 | -48.0998 | 2025-09-01 01:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b31dc163-9a6c-3154-b0d7-481943bf8253 | -12.9197 | -56.9471 | 2025-09-01 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 240.4 |
| 551842ff-28d9-386b-a4fd-62b6ce4e346a | -6.4607 | -43.9301 | 2025-09-01 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| fb81757a-c5a6-354d-af20-ff8794b29570 | -10.6128 | -44.3284 | 2025-09-01 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3463dc42-7972-31c2-bcb0-49586f52ad1c | -12.9387 | -56.9454 | 2025-09-01 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e2a4d000-ddb8-3fcf-9689-997043145cf2 | -6.8466 | -52.8132 | 2025-09-01 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 71ad056b-ea88-3ab9-bcac-311bc0266f60 | -6.4417 | -43.9548 | 2025-09-01 01:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| eb787a36-33dd-3f31-b315-da0a8d2e7d61 | -4.9313 | -43.1624 | 2025-09-01 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 4b7ca1c5-5e31-33af-b3e5-0671b4516ac5 | -9.1337 | -65.844 | 2025-09-01 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 08de0cd3-5ece-3119-bdc9-03706142f726 | -6.7626 | -43.7881 | 2025-09-01 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e1cff013-e13a-3738-8ef2-3f48a46f04a1 | -9.1522 | -65.8434 | 2025-09-01 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 56bb3baa-e908-3a87-8d02-9162ba407c85 | -15.7112 | -48.9032 | 2025-09-01 01:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 127.5 |
| cd2d61ac-6a56-3b27-ab3e-bc21f5c5f827 | -6.7438 | -43.7898 | 2025-09-01 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 907a6937-af26-3d87-b980-989cb4068cef | -15.6063 | -48.3177 | 2025-09-01 01:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 915ee2f2-91cc-3152-b498-3534fd933d25 | -19.0522 | -48.3191 | 2025-09-01 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6827301f-3ac7-33c7-950a-2bcca53cf695 | -9.1522 | -65.8434 | 2025-09-01 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 55f7ce3f-62d6-3a80-b1fc-2f2a27f63818 | -7.076 | -44.3376 | 2025-09-01 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 51a3746a-f273-30b4-9f8d-9d75b04bcd88 | -15.6063 | -48.3177 | 2025-09-01 01:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |


[Clique aqui para ver as próximas entradas](README8.md)
