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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31ac2752-82f1-3420-9330-74f14ac0be23 | -3.21443 | -53.00283 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b4d630b0-00b5-3241-a675-0d4ce5bd78d3 | -3.21324 | -46.16283 | 2024-11-02 05:48:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6ac3d9bc-a550-3568-8573-a1c37b382557 | -3.21049 | -46.18203 | 2024-11-02 05:48:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 03015d6e-e7f8-3a31-8731-e4602531854c | -3.20951 | -53.40153 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 9855e720-67b0-3e8f-a085-d38d15579016 | -3.20815 | -53.41053 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b938ffab-3f3e-351d-87f6-5887cccf70a1 | -3.20678 | -53.41954 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| c56ab16b-ae5d-34a0-90de-1a2e23e6b68b | -3.20616 | -53.84984 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d858e8d-5afd-3e8f-8dd9-1fc56fda66b3 | -3.19993 | -53.40274 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0776c13d-7370-3fc5-bce3-11d446e4b37c | -3.17951 | -51.07211 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8132a946-eaf7-3f21-af1b-a9876e78fdc5 | -3.17813 | -51.08134 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b6b91563-a687-30ca-9835-ea80b4e5083e | -3.17762 | -50.58015 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 659d0a1a-eb2d-31cd-8733-b05e42dcab8c | -3.17659 | -46.59259 | 2024-11-02 05:48:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| eedd72f7-b26e-339c-bf3d-d7719e2a4ae4 | -3.17621 | -50.5898 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 72a8faad-d6fe-3b76-bd75-a1e928094e18 | -3.17046 | -51.07079 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ef1dc494-a5c7-317d-8eb2-6154965e3de0 | -3.16908 | -51.08003 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7076a890-c6d2-37a3-9f11-635cb4f9849d | -3.14694 | -50.35071 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9be6120f-a584-30fe-837c-0a3f5a99bd37 | -3.13973 | -51.02847 | 2024-11-02 05:48:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 768247fa-e64a-3ad1-a158-506cd906b261 | -3.12653 | -54.25378 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 11584f48-5d21-3bc1-8436-ad2da5bded7c | -3.12508 | -54.26338 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9da5be98-b882-3ae5-a817-29b8bae7ae04 | -3.1207 | -54.2923 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4f147d02-d6d4-3897-ae37-84d29f54dc5f | -3.11923 | -54.302 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b272fca6-a8f7-3fee-b640-1bf20752f211 | -3.11731 | -54.25238 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 5e53f952-5357-361e-bd32-ac9481cb2ea7 | -3.11585 | -54.26199 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| a4721ee0-30f3-377c-b15d-f27023b92a8b | -3.11563 | -51.12889 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3f1630bd-c749-363c-b408-bc691f7bf8c5 | -3.11427 | -51.13807 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5b83bff3-7e5d-336a-a230-c8d041134833 | -3.11145 | -54.29094 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0e5f3089-7231-3e13-9475-b0f53d114380 | -3.10795 | -51.1184 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 87de9fc4-d8f9-3698-ba8f-67af815da42b | -3.10703 | -53.71507 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 06472876-8e61-38e4-81fb-7149b535bc4f | -3.1066 | -51.12757 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| d17fdb6c-929a-3b8b-b35b-327cc1bb412a | -3.10221 | -54.28959 | 2024-11-02 05:48:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 58719a8a-64f2-3b57-a2b8-2282187af3af | -3.098 | -53.71374 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4117f938-c0bc-3568-b95d-035fc6e2c006 | -3.08679 | -53.23331 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ab61e0a-c1a8-36ef-8e1c-6cea12e54343 | -3.07706 | -54.16143 | 2024-11-02 05:48:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 45e60be0-f5ef-33e4-8d70-bace6c8acfce | -3.07561 | -45.10848 | 2024-11-02 05:48:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 28.7 |
| c800873e-db36-3d10-a65b-2ebfbcdb2a1f | -3.07278 | -50.23182 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b23a03f-3f15-3161-bee6-7fe8ac5fae8e | -3.0723 | -45.13189 | 2024-11-02 05:48:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 99.6 |
| ea661fad-aa8d-3662-b0b4-eea62132461b | -3.07195 | -50.98458 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8235d981-b39b-38db-9b32-cec0875078ed | -3.06787 | -54.16003 | 2024-11-02 05:48:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 6ff6d309-1991-3da8-b383-981f7ba03db3 | -3.06644 | -54.16957 | 2024-11-02 05:48:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3f89a82-000a-3f24-8e39-86dbb7ae9780 | -3.06197 | -53.15649 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 61740388-8d51-3c6e-8f86-4c302ede53fa | -3.06143 | -50.50161 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 934dee23-775c-3a33-ae77-2aa2d481492e | -3.05868 | -54.15864 | 2024-11-02 05:48:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db339dfc-273f-3988-97f5-5c073b661fac | -3.05217 | -50.50029 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 77ac98ea-91a6-37d9-849e-fc2b628b85fd | -3.05199 | -53.15745 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d4bc64b1-fbcd-3da9-9064-bdf85eb133e3 | -3.02361 | -51.37077 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 74fb888b-b41d-37e8-b75b-f3c5ffbdf249 | -3.01027 | -53.43635 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e70db22-2ecf-3526-bd6a-2293ab1e16e1 | -3.00891 | -53.44546 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9d59a1c1-d236-306b-bb80-3bba9c467f2f | -3.00849 | -53.87486 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 495bb05d-4e28-3fad-8b6e-bb29b42212d5 | -3.00296 | -51.57006 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c4a26e2e-8ad7-3493-b46b-72fbfb63525a | -3.00161 | -51.57904 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 035cde63-38a3-33c3-ad3c-cb67d6fcf844 | -2.99995 | -53.44412 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7567c09e-2b3c-30f9-99b7-3af0b3a72c17 | -2.98759 | -52.9062 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6b0ae0a0-b185-35cb-93f7-852edcf3f88a | -2.98626 | -52.91506 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7f0a305c-1a1f-3edc-90ff-dcfaf1f1a20e | -2.98336 | -49.51609 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 88c6d2d5-05e7-30b1-b735-e510dc8d218b | -2.97206 | -53.2648 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7f40b89a-2e18-3d25-9d3e-8ad996527da1 | -2.96944 | -51.42751 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 062e5a64-47b6-3a09-bd2e-ab787233e6e8 | -2.96638 | -53.9071 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bb053023-a3eb-302e-af26-5f6745ceb4a6 | -2.96497 | -53.91641 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e204886f-3ea0-3af1-b53b-ee8fa5749af2 | -2.96442 | -53.85888 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8a1ac05f-a8c5-307e-bc70-a8553d3c39f1 | -2.96301 | -53.86819 | 2024-11-02 05:48:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bd6c65fc-3bfa-3e3d-bbbf-582b20f42c10 | -2.96041 | -53.28151 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b43921a7-c8a1-3af2-9e41-1c0681fb9ee2 | -2.96032 | -51.05641 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74954b3d-9a75-35e3-921d-c49bc8f3a55b | -2.95127 | -51.05511 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1601f2ac-3a10-3a12-b462-1ebb6af1a08d | -2.95011 | -53.28919 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fc9aaacb-32b6-3b41-ab3d-4192821639fa | -2.93402 | -49.42526 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a9455bb-e74e-3cc5-b0d4-ec61ec3fa212 | -2.90827 | -48.61745 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1d2242b9-0e24-3181-b40d-57329f37dee9 | -2.89992 | -51.7736 | 2024-11-02 05:48:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2e9edb6c-e455-3d73-b2f6-364b439d4f2e | -2.89472 | -49.41964 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 65f1ebfb-ac31-3dd3-bc96-2ba680600ecd | -2.89339 | -49.49765 | 2024-11-02 05:48:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 222e1cab-f4d9-3d92-b5f3-3efdabbc93b3 | -2.88921 | -51.65652 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a95aad6f-3046-3b56-85cf-3c09ccd7c438 | -2.88638 | -51.3073 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b77b09da-5639-37f8-94d4-8b16e491af72 | -2.87741 | -51.306 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 2828f2e0-e6d0-3d45-bb34-06673277eea6 | -2.87649 | -49.26276 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59b945d5-9420-3505-8382-48e4207a5832 | -2.87607 | -51.31506 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ce5f2fbe-38e6-3981-bce2-d9600d6f94c2 | -2.86971 | -53.32685 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 988a2bf5-5380-362a-8a75-fdd6b69fa933 | -2.85835 | -49.38515 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 512b4b71-48b6-347d-ac23-9f77ab60a10a | -2.85804 | -53.34351 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 25fc9665-54b5-3d7c-812a-54a96ae7cbb7 | -2.85666 | -53.35262 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 701e4ff0-4dc2-3cbf-b36a-b1bfe0b5db86 | -2.84909 | -53.3422 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| faf9cfd2-342e-310d-83cd-8beb46c0229b | -2.84851 | -49.38377 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 20377be9-bde8-3349-962c-47bc122f2f33 | -2.84517 | -49.33806 | 2024-11-02 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01d59dbc-cd7d-35f9-9a9c-d164c2635d17 | -2.84169 | -48.43556 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 621576f1-58e4-3ec3-bbc7-a0845ba54c71 | -2.84002 | -51.80367 | 2024-11-02 05:48:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dd3ebdde-c573-3360-bb3b-b225945421bc | -2.83987 | -48.44833 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a86fa1fa-a3af-3b5b-97b8-7fb46ed4f776 | -2.83952 | -53.34335 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 21bc531c-91e7-3876-ace5-42ff304b51ed | -2.83803 | -52.86863 | 2024-11-02 05:48:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| fe5595b7-15a0-3986-8cc9-14fede9fbf7c | -2.8367 | -52.87746 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9333fd03-9ed6-39b7-9da1-d6842f424679 | -2.83526 | -48.44097 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 9749d0de-2c71-3487-97dd-c55f58e4c4cc | -2.83337 | -48.45366 | 2024-11-02 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1d17a978-f416-352f-85c3-265ac0b8c6fd | -2.83114 | -51.80238 | 2024-11-02 05:48:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 35b2fe06-f69a-31fd-8d9a-3952eb1b350e | -2.82415 | -46.6134 | 2024-11-02 05:48:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3f0165bb-99a7-30af-81ec-2effb3d12e30 | -2.81042 | -52.99152 | 2024-11-02 05:48:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fe2a10d8-2c4c-376c-aa4e-40b51a6e2927 | -2.80622 | -51.34541 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ba820183-7bf9-3141-952a-639560f2a882 | -2.80449 | -51.60193 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3789da14-b89d-3ee2-951b-8d7413ff4577 | -2.80096 | -51.74689 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 240730d6-7026-3b94-a1ec-fec6bd429fe6 | -2.79963 | -51.75576 | 2024-11-02 05:48:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ae383dfb-57f4-3371-a933-7a7e64f3911a | -2.79559 | -51.60065 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 19683b1e-89dc-3e0a-ad68-4dff416cae92 | -2.79426 | -51.60957 | 2024-11-02 05:48:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fa079289-a89e-3f20-bd83-6b0cc0421698 | -2.78341 | -48.57472 | 2024-11-02 05:48:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 988d6ed2-2522-3b7c-a440-736c31ec7c9a | -2.77808 | -52.89037 | 2024-11-02 05:48:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README99.md)
