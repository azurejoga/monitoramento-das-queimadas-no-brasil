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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 747f5786-88fb-3331-a277-4d20e28489de | -2.72399 | -46.68185 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b10c2e7-e8b4-34a5-a378-ebd0b3a8d858 | -2.72352 | -46.70645 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35cc0d10-5449-3517-a5cf-1fb36c85649a | -2.72298 | -46.70989 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bcbaa34-0d40-3d7b-b675-d55b39568261 | -2.72076 | -46.7025 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a03df18-4f0d-328e-bcd7-e2c68720d8f9 | -2.72069 | -46.68134 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf29ff66-41b2-3e3b-bd59-c6d9fff7e9a2 | -2.72015 | -46.68478 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95a2e0fc-0a4e-3224-b7f1-759a6068b1c0 | -2.71738 | -46.68082 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2385c8c-c87b-3012-bb53-3e22648b10ab | -2.71684 | -46.68427 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa97e154-5327-362d-b328-8965baa8da75 | -2.71637 | -46.70886 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84299d3a-d9b0-3a39-ba85-55c33eb76e28 | -2.71469 | -46.69803 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c94cfc4d-674f-327d-9fe9-674bcca3e45e | -2.71415 | -46.70147 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 994a2516-2c4a-330e-9f91-9b08db0ad26a | -2.71408 | -46.68031 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66e3c88a-cffd-348c-b6bf-f1f84a09984d | -2.71354 | -46.68375 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae5db0e-f456-3bea-867b-d6030eac5be7 | -2.71307 | -46.70835 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 297f7100-12df-3edf-bf49-7d1a6215d521 | -2.713 | -46.68719 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c7d6ea5-5f12-3d12-9a13-87e6e3ea1781 | -2.71246 | -46.69064 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60657907-f959-3d49-97a9-32985518ffc1 | -2.71084 | -46.70096 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bed8eb23-25ad-358c-b7fe-88782cd3ce59 | -2.7103 | -46.7044 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20949052-0bc3-3f7c-ad37-8209b110dea3 | -2.71023 | -46.68324 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c1e351d-02d3-35ad-93bc-fc94f14f1e07 | -2.70976 | -46.70784 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8acfe5ea-1d73-36d9-a1d1-ad846b529d46 | -2.70754 | -46.70044 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4468f129-f603-3279-9b4a-0f13c277872f | -2.68092 | -46.73847 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a99fa2d-b360-3305-9bfa-0954d5d8ff1d | -2.67978 | -46.72421 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78572e31-f58a-3866-9413-9441398411fa | -2.67924 | -46.72765 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 912fdb2e-f076-3127-9c68-1f7f7488c283 | -2.6787 | -46.73109 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c02c1c63-7164-3762-98a1-4fcc5c6bc336 | -2.67816 | -46.73452 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87d847ae-9fdd-3fa6-bbd5-ab9f939d45c0 | -2.67762 | -46.73796 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c74ffd4-c939-3135-84ca-4de6dde27bac | -2.67648 | -46.7237 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56dae198-6be3-3d37-a355-67bc14c25c58 | -2.67594 | -46.72713 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b902eb50-9105-3fe8-957d-4311b9100bcb | -2.6754 | -46.73057 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e06ddffe-7524-322c-b52a-07ecf3cdc0ac | -2.67486 | -46.73401 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7bdfe736-a3c6-3e26-9e61-cc54ff5bb339 | -2.67432 | -46.73745 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55065de6-427b-33c2-ab5b-13aa58d1d0f7 | -2.56797 | -46.11504 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02cfa081-48d9-380f-9127-26657e345d8e | -2.56572 | -46.10756 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 698ab110-9d50-3739-bebd-6188750a5e09 | -2.5657 | -45.8712 | 2024-11-01 04:29:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 451b2276-bf0b-37e6-8cd5-6354b4854ecd | -2.56464 | -46.11453 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8dd2dbd-7341-37a3-a59c-c152ec1f7d59 | -2.5641 | -46.11802 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df76be99-d20a-36ea-b9c5-e13aba9311b9 | -2.56379 | -46.10073 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae8ba67-93a5-3ecf-9556-2dabaeb24655 | -2.56104 | -46.11815 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f40d8d8-957e-3dbc-b082-2c4e43d496b6 | -2.55388 | -46.14202 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e8b6ec8-fa72-3b81-8ced-c6313ccca8d1 | -2.55141 | -45.98418 | 2024-11-01 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 282d383e-ca4b-3a09-9a54-12a00a138e4e | -2.55111 | -46.13801 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ded430bf-a585-30f2-a33c-88dde2e0b754 | -2.55056 | -46.1415 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3e12659-8834-3cf1-8b2c-e293ad82864b | -2.20959 | -46.49588 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d1eab1f-bdf3-39d3-b85c-5bb3e5759cc1 | -2.20905 | -46.49933 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a3d56f0-5b0c-3480-83a8-f464d71e72b3 | -2.20628 | -46.49537 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d420f9d5-8006-374c-b6c1-1b384dcc508b | -2.20575 | -46.49881 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e0bc47-6fbc-3b2e-aa42-a6a1f909fac8 | -2.19874 | -46.88815 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75233e13-9c42-3aa4-9453-64a23538c5ba | -2.19614 | -46.43032 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa0f0ef0-d394-3aed-b85b-8dfeff6dc331 | -2.19544 | -46.88763 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04253bd2-1821-37be-acf4-12c820afd652 | -2.19046 | -46.70414 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e092e300-62f6-385c-80d5-dcc746b978a0 | -2.17624 | -46.73006 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a074f812-344a-3a24-a49c-55276cc09af5 | -2.1757 | -46.7335 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7379ad42-d535-3d91-8ce2-b41b6e4c29c4 | -2.17516 | -46.73693 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bd77ddd-7fb6-3c15-b9a6-7772404261bd | -2.1751 | -46.71582 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49e4c6f8-aa5c-3cb0-bf9e-e4850107a6d9 | -2.17456 | -46.71926 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| faebc50a-dce2-3c8d-9619-e34f24dcd5a9 | -2.17402 | -46.72269 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48887ce8-f972-3e31-95bb-31f92d2fa5c3 | -2.17294 | -46.72955 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39c7e4f2-92ce-3f3b-bc5a-568b615428a5 | -2.1724 | -46.73298 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16ed1556-f432-3a75-9464-a9c60477e774 | -2.17132 | -46.73985 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0696c45d-69a6-3491-b918-6ebd54efe935 | -2.17126 | -46.71874 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebdd7c09-930c-338c-b9b5-7a8dd671c340 | -2.55563 | -47.32022 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 001f1f99-0a43-3683-9b80-fa91231d9b16 | -2.55503 | -47.30253 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78742086-c5cb-3a9f-835f-b501c5c6c0e3 | -2.5486 | -47.36491 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50295dca-42fe-31a9-b686-7fb9c4be0b81 | -2.54746 | -47.35064 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a738ebed-1f85-35fd-a365-a95d7a5341f3 | -2.54692 | -47.35408 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd250fab-c85b-3927-8e4b-c96654e57eeb | -2.5453 | -47.3644 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c933d27b-3a26-3f83-ab30-f1186f40f4cf | -2.9265 | -46.77723 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 621cd10b-95fe-3112-9774-a8162dce4d69 | -2.92596 | -46.78067 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22f25bdf-b8c1-3206-becb-0425f3a236eb | -2.92266 | -46.78016 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bf9ca30-e812-3540-a6ec-dd40a505d5bd | -2.34575 | -46.45 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32618aa1-469a-37a4-a0bb-92d0567ee36f | -2.34521 | -46.45345 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb29bd8c-b030-38b3-adb8-7f4dfa794ba0 | -2.34028 | -46.46328 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dde1bcf-dfda-36ac-9ff7-9b450dc216d2 | -2.33974 | -46.46673 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be50c19c-1d05-31fa-b52f-0937799663eb | -2.33737 | -46.58976 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ab0dcc5-8d90-3419-b866-43d2c8566ce8 | -2.33689 | -46.61433 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8540352-534a-3343-a20b-d2d6b9c9c9d6 | -2.33683 | -46.5932 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b15e4db8-db28-35ae-9733-de85b88f2438 | -2.33589 | -46.46964 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cf356b2-0667-3194-9acd-f8256b465ce1 | -2.33558 | -46.1257 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88f39882-755c-30d6-af26-c9f723e403fa | -2.33535 | -46.47309 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cb73316-cae4-37ec-b440-e9b50779cbb0 | -2.33503 | -46.12918 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e45fd5b7-265f-3703-bcf2-76a822b84d0a | -2.33359 | -46.61382 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b853670-a950-3040-84bb-1783d965a25b | -2.33352 | -46.59269 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b979435-39bb-3bbd-9b2a-6008cb3df2a3 | -2.33305 | -46.61725 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2695d9da-6838-3d9f-a9d3-53ddc4fdcc71 | -2.33022 | -46.59217 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29b2fedb-ef37-34df-9c2e-30cd0f3ea114 | -2.32974 | -46.61674 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57a4a4bc-d623-3ded-9b73-b63bd48d012f | -2.32644 | -46.61623 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6765a13b-5b1f-395c-a797-f7bf21766bbe | -2.31881 | -46.47053 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 833fcb27-9214-3ee5-aeb9-a660650d7914 | -2.3155 | -46.47002 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de2eb606-ca14-33b3-88ac-71d4a26c3d9e | -2.30957 | -46.50791 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc903648-6f43-3b8b-a4a5-40f03a2f9c3d | -2.30903 | -46.51135 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65767817-b8cc-3601-b89b-b331cf660e1e | -2.30171 | -46.31936 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e495f48d-6b28-3abb-8565-3e5073bf2e4d | -2.2984 | -46.31885 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f22628d-ada3-376f-8258-8f3d8dddfda6 | -2.28011 | -46.49976 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b9bd320-69f5-3299-a240-04974b82a2d8 | -2.27735 | -46.4958 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1678090-7ff4-344c-83f7-7d3dff281632 | -2.27681 | -46.49924 | 2024-11-01 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d10918e6-deb4-3f30-964f-d9db24593fc8 | -2.26304 | -46.30629 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d7ed2de-2778-3945-a447-f89368c7637f | -2.24736 | -46.60038 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 633a56ab-e399-3e58-8fd8-eabbb1499997 | -2.24682 | -46.60382 | 2024-11-01 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e69dfdf-9d4e-33e1-a4e5-d0aacfb23334 | -2.23281 | -46.34762 | 2024-11-01 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README30.md)
