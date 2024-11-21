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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cb1391c-bbe0-35ad-a9a8-ba82a2fcb028 | -2.28988 | -48.40627 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dcf09ae-43d0-3eb0-92c6-0d130e139dfb | -2.37587 | -45.49222 | 2024-11-21 04:29:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55d76a36-b156-38bd-bed6-d42ff51e25ab | -1.14204 | -53.40473 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3796cc3-9eea-3382-b76d-90804fe1d0f0 | -4.14445 | -43.88002 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a3d6a20e-44eb-3d67-bc1d-1a8b815c4ecc | -4.06604 | -46.84404 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b979cbd-6de2-3ad8-bc66-a95b544af4a3 | -2.74886 | -51.82673 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8276f3df-9873-3fe3-b3ec-9c18ee0273a0 | -2.67889 | -46.23751 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 291fe8cb-63c2-3fff-b877-80784b4be816 | -1.78981 | -47.19875 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87006f39-221f-3656-ad2a-aaf60f3ce094 | -2.10642 | -50.13183 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4215434b-1cde-3d5e-80c5-b2fd2c5e5ad2 | -1.43653 | -46.00554 | 2024-11-21 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bcab40b-38d8-316c-a951-7d206a8206d1 | -2.19889 | -48.5606 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06620482-aada-3c86-970b-905cf686d7ee | -2.4051 | -48.60394 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dd0e9c3-4117-38ca-a567-b5b9949fb493 | -3.35775 | -51.61331 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14fd42b4-8ba3-3cba-b1c3-3ab0b1f5d7e7 | -2.94787 | -48.07095 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8384e52e-5ddd-329c-afc2-cdd78f0025f7 | -3.26877 | -50.62098 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3563353-258a-3168-bfc9-cdcbf0e82182 | -3.78129 | -44.06388 | 2024-11-21 04:29:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26b39449-198a-36a5-bea4-0478313540fc | -2.78345 | -51.71891 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b42ba4b-a241-3729-a813-4603db49adb8 | -3.39857 | -49.78922 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7b04126-a709-3494-98ca-9d37bceb96b9 | -3.1057 | -53.17266 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2869e50f-b60f-36d4-9aeb-5ef6a2039780 | -2.29515 | -49.05892 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b4e97cc4-719c-332b-b065-dd2be0d16b83 | -2.82136 | -54.02343 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fb8202f-cc11-33a9-a893-d138bac4b470 | -2.22034 | -46.39999 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cc1e90e-c13c-3585-a500-6877066bd35c | -3.27908 | -50.52151 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ec160ac-7a0d-38f8-ab37-c0f1d7e47e62 | -2.6571 | -46.14156 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5f599e7-d6ae-3cfa-86f9-491ba557511c | -2.62233 | -48.18477 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2418da2-ec61-3682-81e3-ba75c3069414 | -3.2866 | -50.00795 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09ad7d0f-e06a-3cc7-b1dc-fc9d37497c76 | -2.36053 | -48.92512 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 171bc8ae-3725-3260-ae06-ef249e499d69 | -1.56392 | -51.19433 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 835788b7-ded0-3f56-ae2b-1ca8cd705662 | -2.61118 | -49.24849 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fe9eb1f-c006-374e-98a9-4f08bb000d4b | -2.24794 | -48.16334 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7b23a1d0-1dde-3c3e-bfb5-31b73892bb58 | -2.50854 | -46.39927 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07dbd791-cbad-3eec-8fb8-a4e00570461d | -2.40654 | -50.30706 | 2024-11-21 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c4f3149-2b31-3b1d-b14d-b7a210cccd38 | -2.22196 | -47.22736 | 2024-11-21 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00a8c116-b9e3-3893-8473-81962d4a4a7c | -4.48207 | -44.76166 | 2024-11-21 04:29:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbb953c4-1999-30c4-8b47-c3beb61199d6 | -3.88462 | -46.66358 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2392ae8-e62f-3510-9b1e-9cfb0b9b51e4 | -2.62359 | -48.06816 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5f9f8f4-209c-30c0-911a-278b8c392e71 | -4.25067 | -46.11809 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 1b8ade2b-e54c-3597-a1a4-5bd1ccf5590b | -2.64059 | -46.20313 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5077b9d-9d91-32fe-991d-cb4fddf1d02e | -2.08533 | -46.40041 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6511200e-ea87-3933-bedc-8af8557a3270 | -3.89002 | -46.60756 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b5b34a6-83b1-3844-ae1e-e540b2cd4304 | -3.18858 | -48.57864 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7db15629-db0d-351e-a74b-454ea249dbb9 | -4.01294 | -44.83631 | 2024-11-21 04:29:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d63cf82-1603-302a-98f5-7833491211b3 | -3.1819 | -46.54652 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 783ea630-218b-34af-9790-ef464e6c0d63 | -3.49339 | -50.11393 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f542ebdc-0e3b-3855-a5d6-069f2244dad7 | -2.61575 | -51.80161 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e0fcecf-6248-3724-a7ba-b386a3f372e2 | -2.21467 | -48.19856 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a1bb891-6716-3a36-b336-a8167b705bd9 | -2.61939 | -49.24187 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 584118fb-adb7-3754-8f57-11917bf718fa | -3.54104 | -50.53572 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 700859ba-3197-3042-b7bc-5469dc1c695c | -2.59784 | -46.19292 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8048a262-8394-3d95-8569-f72ac9e65c42 | -2.95775 | -51.4143 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f346f07-acc1-34fc-9c2b-71f2cfaa74e8 | -1.2064 | -51.9778 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bc65c33-514c-39bf-b9c3-da14ce64eb13 | 0.82025 | -51.26912 | 2024-11-21 04:29:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a91a0ef4-96c5-335e-8a59-5976538fa14b | -1.45017 | -47.12069 | 2024-11-21 04:29:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a423d566-66ad-3821-bf33-8f7f57859c0f | -1.72637 | -52.7008 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d5cc1023-a3cb-3c71-bb56-21817c3bce8a | -2.68671 | -46.25294 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14edc00-1dc5-3359-b939-9658cba13862 | -4.11944 | -46.87007 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eb14414-5163-3903-b311-f9c1de5e04fe | -3.92725 | -45.77013 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 330bd395-1e74-3060-8367-573ad76f416f | -3.51286 | -50.2234 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bac77d4-c5d4-377a-911c-e6b98fabe94f | -2.85229 | -46.68659 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2672e6e2-d1c2-30c3-a5a4-7805465720f2 | -2.27227 | -49.0906 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21da68ed-bb14-3cb9-8ec7-c495b0925af2 | -3.64091 | -50.21685 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be8f485d-a0cc-364a-b924-c8e8a101bfc0 | -3.48648 | -50.31818 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90ce50e1-f16f-3b6a-9b68-10e6284c359d | -2.64784 | -46.56592 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5e9927a-e399-3de6-8f7b-fdf755ce1c12 | -2.56902 | -46.55008 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0923acc1-e904-33ee-a7e0-ee896bfda796 | -1.45072 | -47.11723 | 2024-11-21 04:29:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6af4526c-37cd-35ee-9e0e-a5677e340335 | -2.47512 | -49.1767 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa18ce2b-4faa-337b-a1aa-96d86e5dcaa7 | -2.28308 | -48.4052 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d52ae3e1-0589-3528-a9b7-af890759ff8e | -2.62752 | -48.06514 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 491702f8-7d28-306d-8828-a0c7f6c0a7e5 | -3.10287 | -50.19806 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0c049ac-06e2-3e3c-b64b-46d3968f8421 | -1.63821 | -52.6879 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc028a99-ee43-3373-b023-e021540582a7 | -3.34662 | -46.6223 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78a5d2c6-98d3-3ccc-a328-80ba5f23830d | -1.22776 | -51.78732 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 867bbe7e-62b8-336a-82fe-f8d63df7c9d1 | -1.72702 | -52.69668 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b0a66f4c-adaf-3750-8d38-c89d3171788f | -1.97777 | -53.33529 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 790cf53b-1380-3bc7-895b-a1707270a179 | -2.15233 | -46.66138 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bcf0d96-ad39-388e-bc02-bf7b24c2ff4f | -2.15152 | -50.69544 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| db1671ab-9337-3e17-b8fb-d572e88681ae | -2.69391 | -46.2505 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5f616d3f-074d-3daf-a2fd-56b1ce807132 | -3.9529 | -46.89736 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1398ede7-9709-36e0-9eeb-7490b07b42f7 | -3.55446 | -50.24586 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9aac213d-e96e-3585-a416-bbad54e38b75 | -2.69979 | -47.97846 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 285d3b0e-340f-30bc-898b-3eefa3085d0a | -3.59097 | -43.63036 | 2024-11-21 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82dbbaf0-c7b0-361e-a729-e34d706bc0bf | -2.24597 | -46.82064 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9bbadf0-b33b-3be2-92f5-781af213d818 | -2.83346 | -46.67659 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2c18659-a6d6-37c3-adee-707ae8bd609c | -2.80737 | -54.02104 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b37f542-1b69-3ce9-a1ac-3e87c2d4ff4d | -1.97679 | -53.33271 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f42e7f1f-4218-3488-ae24-f9d0987b4e70 | -1.69975 | -50.20691 | 2024-11-21 04:29:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 431418a6-9f62-3528-9530-f1722acde1b1 | -3.43444 | -50.3621 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 286ded1f-b41c-3d1c-bd2d-056d5bbea225 | -1.20132 | -51.76809 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d0be990-8155-3c7d-9840-2e1789c6da95 | -2.656 | -46.14851 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcb6fa82-c133-3062-a2eb-ad2b481780c8 | -1.33829 | -51.40353 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41786a35-49da-342f-9095-09c946995429 | -2.7223 | -46.09093 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6717b7eb-cd10-3280-b3b7-bbeb4f8af689 | -2.69198 | -46.07193 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c99b9551-8497-37a7-a32c-30243bc8c1fe | -2.15086 | -50.91196 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62e28fcb-5aff-38bb-81a2-b68c93620959 | -3.18265 | -46.26588 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c7785f2-efd1-33b1-b6fb-e9085698edbd | -2.38536 | -48.92517 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fd31c84d-7334-348e-85d5-2fab16c964a1 | -2.92613 | -48.33794 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21234b6e-5e19-3644-9bb9-00e75f651a95 | -2.55906 | -46.54853 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5d5b033-a99f-380f-8995-6a9e577d3572 | -2.35616 | -49.04095 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbbdd29f-4fa5-3cc2-898c-8be972fd2e48 | -2.58334 | -51.72143 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34b75379-d8f3-3e63-a37a-b48eb07a9e7e | -2.41624 | -48.97649 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README26.md)
