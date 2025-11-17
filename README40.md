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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc88a17d-5e1f-3a26-98c8-a2548dc5f1af | -1.57901 | -48.64609 | 2025-11-17 05:05:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 444c5916-4779-3d46-9f1e-e5c90d515a48 | -2.59092 | -51.82906 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63d95e7c-db79-3300-801e-813ba27482f4 | -2.51675 | -47.82646 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7401c720-5483-3fb9-8add-e5516fbcc3dd | -3.07677 | -45.19577 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54587e25-ffd8-38eb-b5b5-df36e60b0e3a | -1.05993 | -53.03064 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25b0a083-bef8-342b-9560-c36f4c6def72 | -1.26894 | -55.39296 | 2025-11-17 05:05:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3504e19-bea7-3653-9a4c-6f6dc2777f22 | -3.34527 | -43.49679 | 2025-11-17 05:05:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7fe23d0-dc7b-3629-98d2-a3b449500fd1 | -2.20499 | -50.82514 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11eafee8-c8bc-3a66-94b3-6ba86c6d5a4b | -2.47649 | -50.24135 | 2025-11-17 05:05:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5cee1b7d-13ee-350e-a17f-b326e1d128da | -3.65918 | -44.7331 | 2025-11-17 05:05:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4d2383f-2a87-3ff2-9134-6434c7b09b36 | 1.72443 | -51.06579 | 2025-11-17 05:05:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7629228-c983-3e4a-ac4f-bb301ed3026d | -1.53028 | -55.51588 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b0ad81-9109-3e17-9b06-13f5b6bbacb2 | -2.68845 | -52.07186 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65e97ed8-9791-32a1-adb8-21c403853924 | -2.24855 | -53.62314 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 779b5d92-2c5b-3ccb-a1f8-495a3356dafb | -1.14732 | -54.10785 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0a1761-ef12-3199-b5f6-c7e0db813350 | -2.46341 | -48.55887 | 2025-11-17 05:05:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f667efa-7f19-33d3-8c04-8a05c74cacbd | -1.52972 | -55.51936 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6da7fb13-fa0c-35b8-accb-2b20da71dca0 | -3.07202 | -45.20403 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a61670b-1bd2-3a66-b102-7bba551cc246 | -1.46683 | -53.41544 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fe364c5-9605-3a19-bdac-ed1dec1afa4f | 1.01396 | -59.51717 | 2025-11-17 05:05:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b317c618-08b0-3add-976e-38b5fde1f05a | -3.3387 | -46.28834 | 2025-11-17 05:05:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10597005-0bba-3cc5-bf43-0ff011a744d2 | -3.21703 | -43.35924 | 2025-11-17 05:05:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d8a1662-1fe0-31ef-be00-4dd6e623f5e8 | -1.66654 | -56.0436 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc439b6-f37e-35d1-9a81-682b47f40ae4 | -1.77527 | -56.17036 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 218acd72-6c2b-317a-9188-e1c71e23dee9 | 1.64212 | -55.96452 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 323259a5-1a09-3cdc-8193-e91131b748f2 | -3.22101 | -43.36398 | 2025-11-17 05:05:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00e58f89-2620-3fd7-8a04-4c8f391f8efb | -0.82333 | -48.65041 | 2025-11-17 05:05:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d981176-5b1e-39d9-9b98-411810520acd | -3.37829 | -46.06535 | 2025-11-17 05:05:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5530ad05-807d-34d0-9d8f-720199d2e977 | -2.51429 | -47.81131 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3c10b2c-46f6-31ae-8131-6615f277cf56 | -2.50353 | -47.81936 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6302e07a-e498-3d26-bb96-1cedf156e64b | 0.25253 | -51.01244 | 2025-11-17 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3817e700-4b8b-3a28-9610-277e99a2440c | -1.29943 | -55.71378 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 699ce91d-bab0-3cbd-98af-06713b2dc6d4 | -1.17689 | -49.19147 | 2025-11-17 05:05:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbbed19e-af4e-3c69-ba28-1532af4224de | -1.26839 | -55.39644 | 2025-11-17 05:05:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73c93825-b3a4-3c87-99b2-19704d3e83e9 | -3.39807 | -44.17888 | 2025-11-17 05:05:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3f68c60-4d04-3fdd-bf84-e46b64e24794 | -2.51748 | -47.82167 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cf887eb1-440c-3f13-8757-f65b06f1e715 | -1.05685 | -52.40661 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29c88752-2409-39e2-b5f7-f342e65350a0 | -2.8911 | -50.40411 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1d31bcc-7183-3ff1-80ef-95a3b31cc866 | -3.07259 | -45.20029 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10d35e05-fc51-3b08-9423-a91993c642fa | -2.5837 | -51.8279 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0115d0f-1755-36ce-9c50-945cbda253ba | -3.34897 | -44.42704 | 2025-11-17 05:05:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a4e7870-6098-340c-aaaa-b427545e07fb | -3.37618 | -46.06823 | 2025-11-17 05:05:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad94f280-1e8d-3cd7-af6d-0012fafe2170 | 0.24161 | -51.01416 | 2025-11-17 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 47f9cbf0-0011-310c-8529-e4ef307f5711 | -3.09109 | -49.50456 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 432d751f-86b0-339b-b4cf-8de4893bca2a | -2.52214 | -47.8224 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 078ed7d8-5a87-398f-8ca1-4d9ce5b1cd59 | -1.57949 | -48.64875 | 2025-11-17 05:05:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebd34009-853b-37ae-986a-506e31afe9f0 | -1.46964 | -53.4195 | 2025-11-17 05:05:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47c04b5b-625b-3a9e-836d-8c415379cc72 | -3.34833 | -44.43137 | 2025-11-17 05:05:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1cb6792-8159-3f36-a5ec-5be86ec6a18f | -2.52362 | -47.81275 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c8f5502-35bf-3261-b69c-57bb03ffccae | -1.19466 | -55.82059 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e2dc49d-834c-369f-85c7-c029cdf9d6f8 | 0.14887 | -49.82509 | 2025-11-17 05:05:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ed216fa-fbf7-3735-bcbb-37c896924ac3 | -1.52638 | -55.51885 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4459126-90cd-3aba-8f3c-f50882b67a53 | -3.07821 | -45.20114 | 2025-11-17 05:05:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a6a1577-c6a7-3b46-aaf8-ded551ea5ab0 | -2.68969 | -52.06382 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e903a30f-9097-34d3-ad81-ca88a191d057 | -2.67199 | -51.88226 | 2025-11-17 05:05:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83c89d27-b132-3406-bddd-54ac67befd6d | -2.76119 | -48.42453 | 2025-11-17 05:05:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ee7b64a-b167-38c8-948b-480ba28edf5d | -2.52288 | -47.81758 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 54fa8366-7ad6-3f14-8817-5fe2ff0ef719 | -2.51895 | -47.81207 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 891d6e74-cdd0-3682-b897-207bac54a514 | -1.38219 | -53.8419 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f71806b-27b5-3915-9caa-daff97c20f91 | 0.23796 | -51.01472 | 2025-11-17 05:05:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8ed9f836-d818-3b41-b362-550bca8bc907 | -1.69777 | -53.68295 | 2025-11-17 05:05:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52862af2-eaa8-3e06-af98-cd8887029abd | -3.10829 | -49.47589 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a39cda2-56ac-39d1-85c1-7f1c91e804a5 | -2.68988 | -51.79187 | 2025-11-17 05:05:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bc86faf-1e6e-3050-a246-f74a8720fddf | -1.98286 | -51.99926 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9da45134-57a9-3c90-b0bd-917c8a0fd6a5 | -1.99344 | -56.58004 | 2025-11-17 05:05:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2834f93e-9137-3c6d-8634-669e01b0a76d | -2.68612 | -52.06326 | 2025-11-17 05:05:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f9fc426-dce5-36e2-83cc-1c720199b6ee | -2.51282 | -47.82096 | 2025-11-17 05:05:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 151c6aff-f478-3450-b289-a1ee3e6dd686 | -1.12242 | -54.11461 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fc8f2cb-9a27-3397-a679-dbca78e9ee1c | -2.47727 | -50.23631 | 2025-11-17 05:05:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d1d6345a-43e7-3eac-bafa-7f6879aabb83 | 1.19352 | -52.87705 | 2025-11-17 05:05:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d58534-557d-3d88-a9e0-82c346eeb67a | -1.52694 | -55.51536 | 2025-11-17 05:05:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d4abe10-2a24-37f3-a5d1-96b470d2d977 | -1.41562 | -54.46432 | 2025-11-17 05:05:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1e0f96a-3a9e-3120-a1bb-b3d472b34547 | -2.71883 | -49.34509 | 2025-11-17 05:05:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e03526e-1d3c-3f29-af33-155dc80af9e6 | 1.64615 | -55.96771 | 2025-11-17 05:05:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83c8e56c-e2f9-30d3-8378-739e526428c5 | -0.75847 | -48.64442 | 2025-11-17 05:05:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac252fe-8210-3873-bf2e-d1e45de17955 | -3.37666 | -46.06494 | 2025-11-17 05:05:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b585c4c-5088-352c-9e69-92da4cec2f28 | -3.51356 | -57.79005 | 2025-11-17 05:08:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e326a3da-f173-3bfe-b697-f992bd779a0c | -3.80059 | -51.09804 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed977018-a093-3723-a258-ca7fa24453f4 | -9.06427 | -44.79029 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ed9e320-c12c-3e91-8703-63ed7ffaaed0 | -6.80276 | -59.13864 | 2025-11-17 05:08:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc1a78cd-9795-3b2f-861a-a8a9582a31d2 | -3.96468 | -49.94138 | 2025-11-17 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e855e3-bf74-34a8-8776-42567e4b9d7d | -3.51856 | -50.32037 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 365a6540-0e12-3a7c-b296-23d9c5caa294 | -3.85589 | -51.14492 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c8f0dbf-42a6-34a3-ab4c-ad7a5916c34e | -3.2801 | -54.85226 | 2025-11-17 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9211e39-abda-369f-8083-81fbfd9259b0 | -11.40275 | -43.32371 | 2025-11-17 05:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88536c6c-a734-3953-b65d-692d311c87d1 | -5.12404 | -55.96803 | 2025-11-17 05:08:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab49f9d6-813e-3675-96e7-fbf822a71480 | -3.30217 | -53.85167 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a37768c5-f920-3340-82a1-56b1a12978d7 | -6.68174 | -42.03384 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 6d6b44c1-8d09-3862-a416-d92730cacdde | -3.81547 | -50.62981 | 2025-11-17 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa256918-834e-3a46-8d2a-b40bd09416d0 | -3.31226 | -53.85324 | 2025-11-17 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68460154-410a-3d49-b1b8-28adc124eddc | -3.54111 | -51.58768 | 2025-11-17 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 729ced03-861c-3041-8318-a786745bc09f | -4.16377 | -50.19276 | 2025-11-17 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c8187d2-d824-3546-b245-b9ad77d8a7ff | -6.68388 | -42.05055 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| be6df34f-a661-30ee-b474-37157f1530c6 | -5.68734 | -47.11283 | 2025-11-17 05:08:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d54123e-4391-3330-804e-261a377f85b1 | -4.69887 | -46.30623 | 2025-11-17 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a98f247f-9e1c-3c6d-8544-58517991968f | -3.57103 | -52.09792 | 2025-11-17 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d999f743-40d5-3b9b-8db7-948df8f1234f | -6.49992 | -52.82364 | 2025-11-17 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e468b09-4e25-3630-9ca5-902d60179886 | -6.6889 | -42.03497 | 2025-11-17 05:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 556d8110-e082-3178-8332-86602b194cc7 | -2.45844 | -56.09 | 2025-11-17 05:08:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3810f309-323c-3e9a-9b6b-b327de6232f1 | -9.06112 | -44.79639 | 2025-11-17 05:08:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README41.md)
