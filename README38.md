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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a13b49a8-efd0-30f3-9cb8-a83b226984f3 | -2.966 | -53.3027 | 2024-11-29 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 631b53ef-b95a-3429-b101-bb40b4bc0c92 | -3.259 | -53.6388 | 2024-11-29 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 136de994-694b-3e98-b2ef-0d4e01a8845f | -1.6081 | -52.2912 | 2024-11-29 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ff90aada-ee35-34ea-9145-faecaf8c2d1c | -1.5897 | -52.271 | 2024-11-29 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 55a35fd3-22b3-36e0-8d08-9ddc41a0aab5 | -3.2591 | -53.6186 | 2024-11-29 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 5b1665f5-f4f9-372c-ac87-9e6c09eaef7d | -4.4405 | -46.5754 | 2024-11-29 04:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c652575b-64fa-3027-939a-7d7204d4ebc6 | -17.5805 | -42.7483 | 2024-11-29 04:30:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 0e54ccdd-7558-3e59-8fec-c573995361cd | -1.9726 | -46.4467 | 2024-11-29 04:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 98d1bdc0-da68-3902-8f25-9da0366e9545 | -1.092 | -53.3954 | 2024-11-29 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 5dce5fe0-dc89-3b3c-aa4e-e23ea916f820 | -2.6499 | -48.7772 | 2024-11-29 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| d1cf3151-7995-3611-a25b-f0bde3aaa920 | -2.6498 | -48.7986 | 2024-11-29 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| a0dae397-f1f4-3080-9298-69f4c063d783 | -2.6683 | -48.7981 | 2024-11-29 04:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 9299e09e-02c8-3c79-8526-e8a9fd405577 | -1.5897 | -52.2915 | 2024-11-29 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 69a82e8a-1f85-3089-afa9-87848a9812a7 | 1.2171 | -55.9471 | 2024-11-29 04:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| fc95d9fa-0325-3f9c-81a1-cc6a1808e6af | -1.6997 | -52.433 | 2024-11-29 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 35c43957-d405-320b-a54b-6fa004db395a | -2.966 | -53.2824 | 2024-11-29 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| c9c6e2d3-f73c-3bf7-b6c1-5743d761fe9b | 1.2171 | -55.9667 | 2024-11-29 04:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ddbeb243-21c4-3e5f-b3a7-a4c6621ed415 | -1.6997 | -52.4535 | 2024-11-29 04:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 0ec2b8cb-b5cf-39ff-a6f6-f1fde27b76d7 | -2.9844 | -53.3022 | 2024-11-29 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 057b74c4-0b55-3919-b592-5941ea10c585 | -2.9844 | -53.2819 | 2024-11-29 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| abd6b43b-8113-3cc2-b12d-783b44d2234b | -4.7786 | -46.1131 | 2024-11-29 04:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3b0171d7-e78d-31d0-beec-c7fc99ba87ec | -2.6499 | -48.7772 | 2024-11-29 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| c01f69f3-5cc4-3e30-9842-0f5c176a769e | -1.092 | -53.3954 | 2024-11-29 04:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 003a7be7-5681-3c02-a68e-5a969da22d33 | -3.259 | -53.6388 | 2024-11-29 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d31cde76-05e9-341f-a85f-b438b92d61b0 | -2.966 | -53.3027 | 2024-11-29 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2ab5fc03-a48c-3bca-a364-b7b18e314bdb | -1.5897 | -52.2915 | 2024-11-29 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 99ec7a92-9fd6-326d-8403-19b2a6a0e63a | -2.9844 | -53.3022 | 2024-11-29 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 68d7a269-c555-39db-b89a-aa9ce490944d | -4.4405 | -46.5754 | 2024-11-29 04:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 042f7cfc-3c15-3ff9-a91f-43c471b50275 | -1.6081 | -52.2912 | 2024-11-29 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f4718106-0f7f-348a-91fd-2c25219090d2 | -2.9844 | -53.2819 | 2024-11-29 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| da0cb607-bd49-337f-84d9-33d86328973d | -2.6498 | -48.7986 | 2024-11-29 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| ab9a0ebe-9bcb-3731-bf8b-191f7c89da34 | -17.5805 | -42.7483 | 2024-11-29 04:40:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| efbed169-0b8e-308c-a268-5ee7a46d6dd4 | -1.6997 | -52.4535 | 2024-11-29 04:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 94e4e28c-4e24-3cdf-a6e0-9e8181fb9b86 | -2.966 | -53.2824 | 2024-11-29 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 8604b0c4-d0e8-3c06-ab82-c0767a0f7af1 | -2.6683 | -48.7981 | 2024-11-29 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| dfab214a-e1cb-3bb6-8597-c29cb8011888 | -2.6684 | -48.7767 | 2024-11-29 04:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 145.5 |
| ff817d5d-6afb-3384-89b6-5c5df046fc26 | -3.259 | -53.6388 | 2024-11-29 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| b28cac5c-aa75-3d75-a88a-0ed0272b4eb0 | -2.6498 | -48.7986 | 2024-11-29 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| f987c688-9a16-3210-bf40-acab44eb7f64 | -1.6081 | -52.2912 | 2024-11-29 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 847c4662-0490-3ae5-86e8-a62773abd768 | -2.966 | -53.3027 | 2024-11-29 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7571e4f4-52a6-332b-9491-48d906e59fc0 | -2.9844 | -53.3022 | 2024-11-29 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 983cdc6c-b21e-34b0-b30a-611b02f276d3 | -2.6499 | -48.7772 | 2024-11-29 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 911f8be2-8df7-3d0d-8e2e-75144008a996 | -2.9844 | -53.2819 | 2024-11-29 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 147.0 |
| ed03b4ff-c4e9-3c5d-8661-af36daa702ec | -2.6684 | -48.7767 | 2024-11-29 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| ccc6b3cd-d7f6-3d78-b817-e5770648e5e9 | -1.6997 | -52.4535 | 2024-11-29 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 112eda19-0800-3c20-82cd-8a72b264625d | -2.966 | -53.2824 | 2024-11-29 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 69963186-e904-344b-89a3-4813e421d1f8 | -1.9726 | -46.4467 | 2024-11-29 04:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 83c89b94-742f-3c1a-9b2d-71df49b5ec86 | -17.5805 | -42.7483 | 2024-11-29 04:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 6a06e51d-d85c-3e8e-bfbb-b93e3302292f | -4.4405 | -46.5754 | 2024-11-29 04:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ef617e83-ab24-3f11-b5c3-26342fc98f1c | -1.5897 | -52.2915 | 2024-11-29 04:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 643d899c-7bb5-3649-ae99-402e099b350d | -2.6683 | -48.7981 | 2024-11-29 04:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 166.0 |
| fa5c57fb-0a4b-380d-a782-4a90e7ccdb73 | -3.23042 | -53.63066 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db213479-6659-361d-8c9a-0b6af6af2b59 | -2.45174 | -54.02267 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27366671-85f5-3e81-8e50-2321ea83e26a | -1.08653 | -53.63535 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31fa8db4-7dd2-3e81-9871-99bbc93ee563 | -1.34489 | -52.13002 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 280ae131-25a7-31a1-892c-00cb0a726a1c | -3.25644 | -48.88734 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0242453-9e21-3260-951a-2b52a3ccc0e8 | -2.72254 | -48.63287 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b17ab89a-367c-3f0d-b008-cb9659fc4514 | -2.62306 | -54.05625 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7056de2-0041-3f89-86d2-dfb53234f1a7 | -1.65108 | -53.81217 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 519f20b4-7486-3b94-8fa5-17c8a5000f53 | -1.2384 | -51.61293 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfade73a-2f1a-3a2d-95ab-1863795605ad | -2.91136 | -52.59859 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15468249-3128-3edf-bd59-bd5f05e281b6 | -2.6286 | -54.06417 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa0f566e-837e-35c7-ad2c-456d19161633 | -1.88937 | -53.30776 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6ed7d26-29f4-3300-9250-7e930c335d99 | -3.12813 | -53.26228 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 439ab288-5321-391c-81ae-7007605e20a1 | -1.38295 | -53.63269 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3abbb322-5812-3e27-b36e-d39590cdb137 | -2.58397 | -54.24119 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b173748f-a908-3334-a824-0c5767a1c0ce | -1.45216 | -54.54021 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e54066c0-eafc-37cd-840a-fc807268e571 | 0.59733 | -60.46684 | 2024-11-29 04:57:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f6c43e0-4541-3bfb-b93a-f55860f7efdd | -2.8925 | -54.01049 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab4de4d1-647a-384b-a441-5cbb353edba9 | -1.09309 | -53.37638 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5564da50-2703-390a-9569-9189c86c301d | -3.06709 | -53.91436 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fa9d241-4b98-3698-8a17-1159527d39e5 | -3.7714 | -44.12583 | 2024-11-29 04:57:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8036a5af-4576-3f15-9b89-8837d8740c7c | -2.64564 | -54.28265 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c1c6fb2-c631-34bd-a3bc-7eaf7a014de2 | -4.30395 | -48.2378 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f8f181a-23be-3bec-b8b9-1a1d203dd914 | -3.51071 | -50.31414 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09582089-4dc4-3ced-bfe5-fa2c4ef8a8ee | -4.04299 | -53.34843 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2960879-5100-3ce9-a34d-ba019356764e | -2.97914 | -53.27803 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d75ea28-9809-3602-b926-62fe31e65bae | -2.8133 | -54.03699 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d75c162-4a2d-37a5-a989-8e3cab995ba4 | -4.00451 | -54.3367 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b584a06-65b2-3338-864f-4da6067a4a54 | -2.83494 | -48.4719 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9b50d73-8794-3757-8985-f1bd0cc06cec | -1.06817 | -53.21111 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1c7e246-eccc-3574-840b-90864d868983 | -2.20592 | -52.04426 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 544ff487-d446-319c-9c85-8cce2499dd50 | -1.19911 | -51.75472 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec2b95de-829b-3c4b-9592-f2f3846719a0 | -2.80442 | -47.58625 | 2024-11-29 04:57:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48c40f09-6822-3b5a-b294-6d985a701c8c | -3.76361 | -49.9003 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b254ee67-0db4-3436-ab74-cabb524743d3 | -2.82139 | -51.79232 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 877c11e3-f06a-3ded-b427-c64a25fa423e | -1.94078 | -52.95677 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdeb748b-202a-3eb9-86b4-770a44629ca7 | -3.49737 | -53.81699 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea67896-d4af-3447-b750-0dab8a0f0749 | -1.44603 | -52.44387 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d204f1db-0a9a-331e-a66d-dead6f040b8e | -2.58564 | -54.07877 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 326a0c8b-80e6-3402-a613-bc9b9bd14d98 | -2.67274 | -46.14734 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6890a01e-b4cb-3b5c-911d-9a6d4f3c9132 | -2.74147 | -52.5332 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 799169d4-df9d-3dbc-b552-662c49bbb8bb | -2.88292 | -54.11482 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5989d4ae-43bf-3ea9-94aa-2758f0d51fbc | 0.97012 | -50.12623 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0db57086-1d5e-3291-bab5-c47170d7fdb4 | -1.44609 | -47.11509 | 2024-11-29 04:57:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28dabca2-cbf9-3bb2-bf86-805b3340b06d | -1.42112 | -55.25613 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705635bc-ea7f-3a27-9f23-683c0203c350 | -1.59447 | -52.27685 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 156b0570-f8d9-30e8-93d6-a94b49ac7eb0 | -3.39693 | -50.29868 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 700c2029-b4bb-3faa-be4a-cfcf2cdb2627 | 1.28662 | -55.92507 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c811c44b-4656-30b4-9639-caea663f77f4 | -1.53639 | -51.61707 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README39.md)
