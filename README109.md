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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70566d71-49be-3e82-a5f3-5e222384adfb | -2.53557 | -54.04247 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5943fdab-f09f-3af9-bfa9-53698c73648c | -1.34271 | -52.13245 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3abe6739-e5f1-3e57-911c-94af17828644 | -2.70094 | -46.12461 | 2024-11-30 05:01:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 265434cd-e646-3bdb-82ec-0695089cd4d7 | -3.76027 | -49.9416 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f27b36dd-7cd4-3ca1-98a8-ee0e1f7d01ba | -2.86266 | -54.00385 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83a48c85-24c7-3dd9-a2b3-f2ad4adbeb7f | -1.21235 | -51.76376 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac1a6f8f-6ae2-34d5-95af-e0aa6a9cc007 | -2.96798 | -52.11442 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1943aa8-fc1c-3446-a248-190e68da9b22 | -3.30847 | -54.11219 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85606cdd-9dfa-3c0a-8eeb-0cf605e6371d | -2.23777 | -53.62897 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa08880c-d786-392e-8c45-a9246ea04c3c | 0.62878 | -50.56875 | 2024-11-30 05:01:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 727519d9-a72d-3a4b-ba53-6793e09d721b | -2.6673 | -48.7966 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63ca1f80-b810-3578-953b-d54b5a5cb6c5 | -1.69392 | -52.46732 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb9d35af-2cb7-3ecd-8a6c-5d65542cae6a | 0.92921 | -50.26935 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8415c69-69ac-344d-a50d-13b938d555df | -3.40466 | -50.6579 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5ddd863d-2f14-3cfc-a502-5ffe22fc9ffa | -3.50054 | -50.2916 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52d298d-e0de-3625-8fd2-18e84cc75c9e | -0.95639 | -51.65355 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5a34e63-cab1-33aa-ab70-4b09ef338296 | -2.84886 | -54.06988 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5301de2-cdfc-30c4-a559-121b0788c4ef | -2.41636 | -56.43864 | 2024-11-30 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 639277ed-0030-37d8-9b8c-cf97880dfa62 | -1.67758 | -52.50354 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 431abd6f-8f6a-3f2f-9b74-5c1c8e179217 | -3.96337 | -50.19036 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 74525fc0-f471-37b0-b516-956f9f09e9d1 | -1.06989 | -53.63692 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 56724a40-0281-3c41-a5a8-eb14611afa0e | -1.10363 | -53.40082 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bca60fa-6dc0-3674-a615-782fefb483f0 | -4.67299 | -46.37491 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f5383ff4-f099-3c3f-89f8-55243d97c39d | -1.83022 | -54.52551 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 41d3ad10-19ca-3a5b-8fcb-6e5ac6b46bd5 | -3.70928 | -53.75285 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04787b5f-5cc9-3d50-b5f0-e2a318471823 | -3.10302 | -50.36341 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0287de62-90b9-3228-a19f-851a353e6787 | -2.89107 | -53.99749 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c899ca1-54ad-3a19-aa1b-04f01d4737c4 | -1.44218 | -55.20324 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82ca6be7-2e8b-3421-93cd-3f387de97ed3 | -3.33399 | -53.3592 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd37e6e2-f849-3a1c-96a8-925c0399cad7 | -1.60386 | -55.44262 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ae73edf-d4d5-3a6d-b78c-dc461fe53a22 | -3.68205 | -49.56893 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1a20a92-794f-3821-8aad-983e4b19f2aa | -1.20214 | -53.67878 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a835ebd8-d8fe-36a0-9581-229e3f9a50fe | -3.05626 | -54.04069 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a115338f-947e-3539-a216-6c752f996a06 | -2.72817 | -51.7455 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d48f5783-04df-3985-a559-dc95870f48a9 | -4.08995 | -51.11288 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91655275-ac6b-3b12-b786-81fc61df594d | -3.53791 | -50.18003 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56301e7a-b2b2-38ea-b369-46d8237fa9ee | -2.81071 | -48.61826 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b81f2916-b9fb-3996-99c3-dbb9bbbf1239 | -3.01502 | -54.04149 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34e3763-b325-3bf0-bc57-2694f39f103f | -1.03239 | -53.5485 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41134d3e-9d36-37a4-a2f0-f3887859e3ac | -2.47176 | -50.36208 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e59e700-0947-3a27-99bf-af6c4521cd57 | -1.66961 | -52.80042 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8b4a35f-9457-331c-bcea-6c10775ab275 | -3.74263 | -51.83604 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f459fb49-16bf-3a58-bd03-4da73e5e67a1 | -2.32242 | -49.0812 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 123da6bb-698a-3172-9627-6a868557b5fe | -3.16168 | -49.02375 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 648c084a-d459-3fbe-80b7-2d1300d7a226 | -1.75744 | -53.646 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56819bd9-0f8c-36e0-a45d-d6b1cf3c4d62 | -2.59242 | -53.97598 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8762b34f-5421-3166-82ca-488a110bd643 | -2.01274 | -51.19557 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa53e5d4-82ef-3eb1-a136-a87d1ef84b91 | -1.70947 | -52.48137 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 714925e0-5c83-3331-a6c1-80f1dc39fa1a | -1.68236 | -45.78637 | 2024-11-30 05:01:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c2949b5-554a-374d-80a5-fb11898fd8f9 | 0.98764 | -50.2487 | 2024-11-30 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4de014d9-9ee6-3e2c-96e4-da89b67e2ce5 | -1.36495 | -52.12796 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b03e872d-4dea-3e87-a1d3-b071b7311667 | -3.83045 | -46.47036 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd329d74-16a9-3358-b3e7-0277af46aa2f | -1.35334 | -54.63078 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2aec1991-6f0f-3458-b5c3-971eab737887 | -1.64205 | -53.86836 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| cf9b6dff-606d-350d-a8e1-b9560354751e | -2.95963 | -53.70408 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b40ff9af-dbbd-35e2-9b0c-bc07c5d79153 | -1.08989 | -53.13615 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50990329-ad41-3515-b73f-e3fa235f1713 | -4.25049 | -46.37749 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52a527eb-5723-36b2-b6d8-ea30b6115be9 | 1.48282 | -55.94466 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f93e7e85-69d1-3462-a767-ca4fe4e32354 | -2.7779 | -54.03037 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d23fe9b-11c8-3ca9-a1bf-8f46af0db548 | -3.54891 | -50.18871 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42b0988e-8ab5-31b6-83a0-4c62e5f3bc39 | -3.60811 | -49.99208 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e84b137e-ef9a-3b91-bc66-a699044457f1 | 0.88728 | -51.98123 | 2024-11-30 05:01:00 | NPP-375D | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a664c461-8451-3999-806e-6602f352a1a7 | -3.49863 | -53.80485 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fd3e175-16c4-30aa-bfaf-25d555582312 | -1.66751 | -52.40879 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 639798ae-1be8-3f1d-8c80-ee498606cd65 | -2.89772 | -53.95535 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbacacfa-a337-3da6-bde2-3a670027ce4b | -3.9329 | -51.17684 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a7c4b85-75cc-3541-b497-c9879fe57190 | -3.51153 | -53.78853 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f6207bfb-8543-3343-b827-407284be95d3 | -1.42914 | -54.30047 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8de21cb2-e8cb-35f0-b9ab-98b70da9805c | -3.25288 | -53.63245 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6028a02-bd0c-3b1a-ad94-e9fd4e20af1f | -3.02852 | -53.41708 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f74dc3-6947-36bb-bdbb-ee3dc66954e1 | -3.24785 | -51.34431 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9117370a-45c3-391f-bf9e-67867cd5f45b | -2.82941 | -54.08478 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59640506-efc6-3a53-863e-2e207151abb7 | -2.02083 | -51.19234 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e79580b-52e6-31d0-9d77-0dfee163e068 | -2.97396 | -53.87685 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0af139a1-fb72-3ba0-8d88-0070bc9502e7 | -3.09615 | -51.40872 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e7a6220-37e2-3801-9b43-e96cb9c0ba96 | -1.70504 | -52.44184 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01f73bb8-5164-31e5-abab-514c0faa9cc0 | 0.94197 | -50.7325 | 2024-11-30 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35e29b05-5944-30ef-9a79-99979f299394 | -3.09828 | -54.13735 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d219b24-1cd6-3542-9e3d-80687991bf7f | -3.40045 | -50.66414 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 698166f8-b85b-38f2-a800-391dcf686f26 | -2.60749 | -53.98908 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6cf5443-74de-3fa6-bd9b-d9fe46eecf7c | -1.71462 | -52.77643 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9852323-be0e-35cf-a7c9-c8733707fea5 | -0.14282 | -60.86417 | 2024-11-30 05:01:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 504bf733-6ede-3a70-a0e6-56383b30c806 | -3.29614 | -51.07993 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e805187-3163-3e3f-a45c-b3262793b80f | -1.32947 | -55.85051 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e8afdde-37e5-3cbe-9525-16ca2b9f99c7 | -2.09116 | -50.49515 | 2024-11-30 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 394e1426-6443-31a0-9069-ee2a01a69423 | -1.69833 | -52.64135 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b93b180f-b678-3a8e-bf12-301630d2718d | -1.20514 | -53.87189 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 14ea847b-1a3a-34e6-baf2-6d8c60f06542 | 1.87586 | -55.73398 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f52d0f9-6d5f-3428-bfae-c71d23efc479 | -4.86955 | -41.30574 | 2024-11-30 05:01:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 850643c8-d871-3ace-aabb-9cc511dc29a5 | -1.63964 | -52.42786 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5aad9871-5d9d-3229-868a-9cc78cbeff40 | -3.62095 | -42.73442 | 2024-11-30 05:01:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cdd13bd-9b58-3257-a1c8-84aa8567d8a4 | -3.28103 | -50.60731 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a979dd4-a1d8-3e71-abc0-e3ea1aa31e52 | -2.86766 | -53.99385 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e46137ee-9ce0-3afb-b3af-5168f54e12ff | -1.66909 | -54.02221 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 538f70aa-1863-3d31-bced-2b1fa56c8294 | -3.10171 | -53.8165 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01a69cde-cb66-3289-af8b-55a200d78db5 | -2.19337 | -53.78103 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b74913a9-8b45-360d-ac30-edd7aa8e2580 | -3.42303 | -53.88434 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1c4a459-b8de-3839-9f6f-28ad37180c16 | -3.03953 | -54.03811 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f24cd7e-21b9-3f44-9020-e683b5d8a30c | -2.03668 | -51.20179 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18a8bc9e-1ac7-35e5-8189-53e3817e1265 | -2.8627 | -54.0254 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README110.md)
