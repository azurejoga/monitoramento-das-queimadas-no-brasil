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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2dbf300-fca6-3a40-b422-48bd543c6a8b | 1.38156 | -56.03442 | 2024-11-21 04:29:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f3feed7-3641-3fa6-9b10-b5c7f044520e | -2.59248 | -51.71581 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c34a18-847a-37be-bcb2-28d91df403d6 | -2.28648 | -48.40573 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5044b038-1ac1-3b4e-94ef-667129e3614f | -2.55143 | -47.28585 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f04c206-b83f-368c-bdf5-780bf1e22120 | -0.79692 | -51.78457 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 162d9000-8449-344c-a68e-a30b9eb0282c | 0.69717 | -51.44147 | 2024-11-21 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92898f57-86e3-3568-b954-6425c4ad0f36 | -1.61445 | -52.47591 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47635345-efca-3344-9e89-f70ebd16f170 | -3.35186 | -50.18237 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54a9fe72-844e-327b-824c-9f8c260d2cc8 | -1.2118 | -53.69886 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b873239c-6db6-3d85-85bc-6f831fd090a4 | -2.72893 | -51.74482 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64013e41-f7f6-3bcc-85e3-3bd675fad6bf | -2.1656 | -50.13134 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0378e07b-12db-30e0-b500-490ddbad8163 | -3.99529 | -46.3884 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d57f46f5-e9c7-3d99-bdaf-072fb084e125 | -1.12286 | -53.40673 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| acb41f75-3e83-3e34-b36f-6790378e1fe7 | -0.30439 | -51.56535 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4318c76-3115-3469-af67-2a89111bcfcb | -2.24542 | -46.82408 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e57d626-34e9-3f64-81b4-dd761d4e1e0c | -3.37692 | -50.28081 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3a0999d-827c-3f88-ac46-852fe958fb72 | -2.30772 | -45.6528 | 2024-11-21 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f26e00c4-ce3b-3eb9-8d71-e05d4ec59bba | -2.427 | -49.02094 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c39fe17b-d3a1-305a-87d7-4ef28e350b9f | -3.0063 | -51.312 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 66032b8b-b34a-3d61-8075-01d90825b9d0 | -2.65774 | -46.54625 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3f2893d-001c-3f40-93eb-ca39aa30c6bb | -1.26912 | -52.12684 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f562585-f49f-3889-a7d7-38e337d247d7 | -2.60577 | -46.2511 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17a1d4cb-30e7-37bb-94c8-316397557e46 | -2.89052 | -48.27393 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd11e107-df3a-3005-b200-c62368b7d49a | -3.35845 | -50.18761 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aaf99d5a-039c-33ad-8c2d-0d6d9a9047ef | -2.63032 | -48.06921 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d855671-1c9e-3628-a90b-28389d0fea07 | -1.58634 | -50.4388 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82536f7f-f3a4-379d-8b85-d3bcc3febd39 | -4.24731 | -46.11759 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 75c6fd50-0042-3754-a92f-dbee52255d4a | -3.09765 | -53.16694 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c09c1a9d-3140-322b-9172-b87ce5abd983 | -3.67219 | -45.23621 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20261a86-0e37-375b-a8e5-573380fe0869 | -2.56141 | -47.28741 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f280e417-e4db-36eb-97d8-468e7bb282e0 | -3.58435 | -50.5248 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 714d8dd5-7982-3bef-a696-75833cfe9041 | -1.2019 | -51.76445 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4a74422-42be-302f-8998-1b1b09b9aba1 | -3.27838 | -50.52591 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fb5d070-7247-350e-96d7-ff2098a2a893 | -2.55574 | -46.54802 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa660206-f72d-37e3-ac72-34f269f759d5 | -2.68812 | -46.17842 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 137052ae-a384-39ff-b3a7-4fe0ac9e002b | -2.66674 | -46.23209 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1898c97a-cfba-3804-8351-5ff4562e8e8f | -2.65322 | -46.14452 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8f942c1-ef05-306a-a9ba-83e3d6435633 | -2.28177 | -46.5933 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b3d92ef-c60f-38f6-aca1-38067d0612ff | -2.45933 | -47.03084 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6c0948d-8a16-30ee-b1c3-018b13e34469 | -2.65881 | -48.48181 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d47e8309-2a37-3113-9cd4-7483f694db52 | -3.39854 | -50.1004 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d7bac50-0fab-3724-861f-c34f0d5f480c | -2.01221 | -54.51917 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 03ac64cb-2dc5-3d20-9dc7-6cb5c37a751a | -2.78661 | -51.72469 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03aa72de-a490-3173-a92f-5449c269c192 | -2.62594 | -47.96688 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c842d14-6e32-361a-bae5-8c3621ec327b | -1.06725 | -48.00995 | 2024-11-21 04:29:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fbfa208f-4616-361f-a05f-14487dd51d8f | -0.77799 | -51.77018 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4ae4ec4-6ac4-3ae1-b0b6-87cd0671045f | -3.39688 | -50.24947 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc2733c4-e57f-3dd8-906d-b80e6b97dca0 | -0.17983 | -51.53896 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d4004db-cec5-3e4b-9cf9-4c1dfc81f9de | -3.56408 | -49.99499 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2789eae-c75d-3dc5-8da4-38563ea30b7d | -2.14364 | -50.64736 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90363c35-5678-3954-92fb-78021194e9a4 | -2.09638 | -48.94715 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4e05ba-6ade-3f06-84d3-a0c431d62765 | -1.61915 | -52.41954 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bf83c48-b2f7-3cba-b19e-109bb3417c07 | -3.30131 | -50.35728 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47884404-6530-3a53-80ba-31c48c2b38ca | -1.46862 | -51.11857 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03d900d9-9912-369a-9153-0d908dc08108 | -3.18523 | -46.54704 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef8bb235-df94-3039-b5a4-500b50e4a7fd | -3.53735 | -50.44239 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d519ae6c-b105-36d8-9a02-a4d7dabbb815 | -3.60309 | -49.86449 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc300ce-ca86-3385-8880-659e25e1812a | -2.20317 | -50.54358 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d7dd209b-aff9-3bc9-904e-749d920ac662 | -2.55961 | -46.54508 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb2bd959-900d-384a-9829-f52a02d3bd83 | -1.46099 | -55.45434 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d7031c1-134b-3eeb-8bab-a84091e8fca8 | -2.35768 | -48.92081 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfc320fd-466b-372d-9f1e-ec95b5275227 | -3.88849 | -46.66063 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32adcb3c-0235-311f-a0ba-d9bb9457dc74 | -2.14835 | -48.91955 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13b878b2-6422-33c0-a1ca-8646a94fc989 | -2.649 | -46.23645 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b78d9b-9111-3368-9726-83b241f33b1e | -2.33596 | -47.40848 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21a26aca-8275-3fd8-be95-cb193dd8a857 | -1.22719 | -51.79097 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4435734a-422d-3576-b695-749944fc1423 | -3.2706 | -50.62324 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a39b969d-f53e-3750-b7cc-63b3b3bf1de6 | 0.05496 | -49.53296 | 2024-11-21 04:29:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5dd3163e-2f00-3edf-b5ae-ad6c153aba84 | -2.83678 | -46.6771 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ef9da7b-31b5-3dac-a629-d75648d22997 | -2.64655 | -46.14348 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dd26076-808e-30f6-9cc3-8c1997264ae1 | -2.21372 | -48.91046 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db7d8bfa-0d49-34e9-9437-29e1e9738f5e | -2.55754 | -47.29035 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 484c9af1-a922-3964-a111-6168315da980 | -2.64114 | -46.19965 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f02de66e-ed1f-3a75-81c1-7c0356a36fa2 | -2.57971 | -51.9228 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1956cb0a-c173-36c9-83e5-185f706fd5c1 | -2.57638 | -49.21928 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7efeb1b-2968-3be6-a4f7-21d7763e3a87 | -1.56459 | -51.19696 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25e264d5-2f81-3e13-bf26-df2a046a6d02 | -4.48037 | -44.7494 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f1ce5b5-ad7e-3f4f-b2fb-ea0847c314e6 | -2.58286 | -47.45407 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9fa42ae9-d204-3534-9e0d-685f3f7a9253 | -2.20583 | -53.71846 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9a5feead-fa09-3817-b3fb-d8e95112eaeb | -3.2905 | -50.53486 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e7576d3-a382-397a-a9b4-97f4987b0aaf | -3.12262 | -45.44833 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb9e274c-711e-3036-8738-69af03972787 | -2.39727 | -49.05133 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8c264f1-3f03-3d91-b6c1-c40b5cc4bd1f | -1.41097 | -52.10569 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0abf847-f905-32f9-8a30-d4bf917d4ce7 | -2.63036 | -48.48529 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3611dd04-b72c-30ee-af97-08548171972b | -4.08428 | -46.83624 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0c1415c-0c50-363a-bfa1-cdae00accf50 | -4.10629 | -46.91051 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c5067d8-5a6d-3533-ac8c-48360cdb0de5 | -1.70941 | -52.72346 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f6445af-0d42-3bcf-8dbb-546862b1c60d | -1.64328 | -52.69166 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d7554c1-cc1d-386f-b55e-ae972b721973 | -1.42665 | -52.41141 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937bc37e-67c8-3fa0-a1f1-280f053e4c61 | -4.03067 | -43.75202 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 031741bf-918a-3769-b9a5-4b7bd0a823ed | -1.56536 | -51.19199 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70ca4370-4c0d-3441-ac29-8046b538a989 | -1.97629 | -48.686 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9ba2497a-bddb-38a3-aacd-a2af86a31469 | -2.932 | -54.09341 | 2024-11-21 04:29:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e952e16-0984-3e86-bd61-7b155c55a940 | -2.72105 | -47.97453 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0982a535-e3a2-3ee6-9a14-e06d3d7d3947 | -1.21824 | -51.74096 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a520e47-113e-3cfb-aca2-2f25b845885e | -4.2417 | -46.10948 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94f8d346-83be-35ed-bcc7-9cf1b691f546 | -2.80067 | -53.00358 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3af836cf-88ba-3807-93b3-ee7c150808ea | -1.74089 | -50.48488 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f81984-d2fd-3202-a075-b519b4a08971 | -2.14982 | -53.57022 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8aa24ba-0787-370e-99ae-a926fb4cb08f | -4.47144 | -42.95654 | 2024-11-21 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
