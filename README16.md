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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf89a88b-1f84-3400-80cf-c822a20a686a | -2.8013 | -53.043 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6ff272e4-400b-35a0-9c22-91125964ae1b | -3.2591 | -53.6186 | 2024-12-03 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 700fca4f-e7a0-3694-9f80-e656743d13d5 | -9.374 | -57.5553 | 2024-12-03 01:50:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ff39b410-3be2-3371-a177-93de0e1d2708 | -3.076 | -53.4011 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b8d9540e-da21-3456-ade1-049000e204c5 | -6.9911 | -43.5116 | 2024-12-03 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| afef0e8a-6088-3c42-bf2d-884824bd0191 | -2.7378 | -45.1976 | 2024-12-03 01:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| b9c5b04f-c1f5-3e6a-a329-fdf2b039aff2 | -3.183 | -54.3448 | 2024-12-03 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 19ef6c8a-9095-324c-ab7a-19ddf6dd6e1e | -3.259 | -53.659 | 2024-12-03 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 9329c3cc-49cb-35e6-ac2c-999615902dc9 | -5.8009 | -46.4941 | 2024-12-03 01:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ccd54e53-8a49-39b6-9ea5-a250e39a477c | -3.5496 | -50.191 | 2024-12-03 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 07caa2d7-d7b5-3c10-add1-2ee07e3800e8 | -5.8197 | -46.4706 | 2024-12-03 01:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ab0a17fb-7f5b-39f5-baea-1ed7599489e2 | -3.0945 | -53.3601 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 88d8e914-63c7-392d-b0f2-be8c5d91ffa9 | -1.7868 | -46.6494 | 2024-12-03 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7d833fed-334b-3f3b-a1cc-759d48f09772 | -2.8012 | -53.0633 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 0e5aa424-5bd2-3961-ba61-eb5cb216a6b0 | -4.1708 | -48.1842 | 2024-12-03 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 1cce5513-276f-36c2-9fb8-e69de0004587 | -3.0376 | -53.8664 | 2024-12-03 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 04e4d65a-d78e-319e-9d90-2137ce2ec6a3 | -1.7867 | -46.6714 | 2024-12-03 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 4d8a77d1-451b-3801-8733-c693fac932cd | -3.0949 | -53.2385 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5f0983cd-9863-36dc-b0c1-b1e55ba8b923 | -5.801 | -46.4719 | 2024-12-03 01:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 18ee443e-c594-371e-99f3-447fdc9d9222 | -3.5682 | -50.1693 | 2024-12-03 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0c15ef96-c9df-39ad-b0d5-1c364262ed55 | -5.8195 | -46.4929 | 2024-12-03 01:50:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 156245ff-1292-3af0-b68b-233c62bf86a7 | -2.8485 | -45.3963 | 2024-12-03 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2e525d45-9b6c-330a-9ff9-74edc02f41fd | -3.5497 | -50.1699 | 2024-12-03 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| ec841819-cc50-342a-aab5-63bbe19604f5 | -2.8196 | -53.0629 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fbaa1159-9233-3c23-aa53-651c7cd61a68 | 1.1256 | -55.9675 | 2024-12-03 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 381df948-4f86-3663-8344-ffd2f9298dbc | -3.0944 | -53.3804 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 9ed87876-3843-32f2-aa8d-9bf81ebd38c4 | -3.347 | -46.0486 | 2024-12-03 01:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 3a43822f-d40e-3da8-b535-f54209a23186 | 1.1256 | -55.9872 | 2024-12-03 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4318b2ea-0bb4-375c-b33e-b022eb82f8f6 | 2.7267 | -60.3916 | 2024-12-03 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 002b1d74-fabd-3f04-9b22-b70cfa2340d3 | -6.1229 | -43.9578 | 2024-12-03 01:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a4fd831d-2ad0-3fd5-94cd-b9500f3c1cdd | -3.0761 | -53.3606 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| e3c8c603-5588-37b6-b823-4f581b560861 | -1.8052 | -46.671 | 2024-12-03 01:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| cad03037-1d06-35c9-beb9-12ed535b6f0d | -1.7541 | -52.7993 | 2024-12-03 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a2777453-b9d6-371a-91d3-b682ad195fa3 | -2.7377 | -45.2201 | 2024-12-03 01:50:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 0ec6abe7-0deb-3741-b44a-5b25e0d6d536 | -3.3422 | -51.2007 | 2024-12-03 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 496eaa0c-b711-301d-bb60-fe299b906551 | -2.8197 | -53.0425 | 2024-12-03 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 8f5a02ca-67f5-33b4-8f9b-9843ce238393 | -4.5402 | -42.93 | 2024-12-03 01:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 540937a1-3672-3806-a184-1340b9971006 | -5.43137 | -60.18915 | 2024-12-03 01:51:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dd9b1491-2ec9-3135-ab4d-f9aa8549c6fb | -3.07698 | -53.38606 | 2024-12-03 01:51:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 81be7ba4-386b-3058-925c-76f2938f2b57 | -3.2612 | -53.63691 | 2024-12-03 01:51:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 47f08cba-c417-3239-889b-d8c46ed6584a | -10.05306 | -59.12103 | 2024-12-03 01:51:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 6524dd1c-2184-3d6c-9fd1-65c945ea4fca | -9.18954 | -62.39028 | 2024-12-03 01:51:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a62bc08d-cd33-3678-8b51-c85e10aca52c | -9.36532 | -57.55732 | 2024-12-03 01:51:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a1390d4a-8614-3bca-acb7-961fe895bfe0 | -9.18067 | -62.39157 | 2024-12-03 01:51:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9b4be020-28be-3cef-b40d-707bff6e9ff8 | -10.45849 | -58.68569 | 2024-12-03 01:51:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4ed79106-9c5e-34f1-bf4f-f18f06fe2498 | -3.02662 | -53.88836 | 2024-12-03 01:51:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| feecd6cf-ded5-3375-accf-47b3b752871c | -9.03488 | -63.53009 | 2024-12-03 01:51:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c6f4bdbf-3052-3bbf-a593-8073dff81a60 | -9.37667 | -57.55537 | 2024-12-03 01:51:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c84d661d-a8cf-36fc-b0d6-78cb630fe746 | -3.18604 | -54.34099 | 2024-12-03 01:51:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 5e77206a-520b-3308-8b0d-64ed7db8b0b0 | -2.55443 | -53.41104 | 2024-12-03 01:51:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 89d16cd6-2d69-38c7-94b4-f80546b24523 | -9.18835 | -63.44023 | 2024-12-03 01:51:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c9c2189-008b-3218-978b-29bfeee447b4 | -9.65787 | -62.44669 | 2024-12-03 01:51:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 06cca5b2-7fd8-3e4f-a0f6-1d964ee654b2 | -3.08361 | -53.42052 | 2024-12-03 01:51:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| e3226e41-d59d-3036-afa1-232dd515068f | -3.02967 | -53.88256 | 2024-12-03 01:51:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b79c863e-619c-3ab3-8902-743112f938c5 | -3.07712 | -53.37908 | 2024-12-03 01:51:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 171.2 |
| 3a6feba7-a8d9-361c-9185-f7fad15fb45c | -9.02591 | -63.53136 | 2024-12-03 01:51:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8286784b-cd06-379c-87fd-2ef56947497e | 3.13769 | -60.29362 | 2024-12-03 01:53:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e256b296-316d-3604-9176-02a3ac69aff5 | -2.21171 | -53.7805 | 2024-12-03 01:53:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 36a1197e-e8bb-3100-be33-0466fb313d99 | -1.51578 | -60.32663 | 2024-12-03 01:53:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 25b3639c-e1e3-331c-b7f0-e0bd821439d9 | 1.30815 | -60.41994 | 2024-12-03 01:53:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f20c46fe-17e2-36f5-a957-29e7a4aea1cd | 2.73571 | -60.37931 | 2024-12-03 01:53:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b94930c8-fe0b-3d5a-b75a-6c2f36c03016 | 1.30611 | -60.41381 | 2024-12-03 01:53:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 723d1463-ba86-38a4-88c8-61c9a7c938e3 | 2.73372 | -60.39383 | 2024-12-03 01:53:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1d365f13-a18b-308c-a3fe-1d6502af068b | -2.21025 | -53.78757 | 2024-12-03 01:53:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| cb704cdc-1ac4-37f3-9f7d-2f8627e31e90 | 2.57816 | -60.69627 | 2024-12-03 01:53:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3e9b1543-7c45-3694-9e13-3748500d8cbc | -5.8195 | -46.4929 | 2024-12-03 02:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 3c2703e6-7942-39e0-86f0-02e4c364ff45 | -2.7378 | -45.1976 | 2024-12-03 02:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| fddd7ebe-0d96-388d-9791-461a773f283b | -1.8053 | -46.649 | 2024-12-03 02:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| a859f64c-5520-342f-afb5-631b5c13b242 | -3.2591 | -53.6186 | 2024-12-03 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5b1c3608-4bbe-37a1-bc7d-a391d1685d69 | -3.347 | -46.0486 | 2024-12-03 02:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 68813b5b-2acd-3f71-8b3a-123eab3c3fb5 | -6.9911 | -43.5116 | 2024-12-03 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 493a8988-74f0-3c76-ab11-5d1a6b5357a5 | -3.0945 | -53.3601 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| da01007f-4088-3d36-af33-b148e430afdf | -2.8196 | -53.0629 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fec48b41-d4bc-31d6-8b29-f5cb1ba49a90 | -2.8853 | -45.4624 | 2024-12-03 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b91b45c4-7b12-322f-97e0-ee4f8da4c81b | -3.2775 | -53.6181 | 2024-12-03 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bf5c4e68-d7d5-34d8-8f4e-32490e20b734 | -2.7191 | -45.2208 | 2024-12-03 02:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c6584788-09cc-3c5e-92ac-fb3ac14c980e | -6.9908 | -43.5349 | 2024-12-03 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f50cd989-7a08-3b20-bda8-6ad28f3a33b4 | -3.5496 | -50.191 | 2024-12-03 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 0648c937-5eec-345b-8435-8d2e5bf04561 | -3.076 | -53.3808 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| eff87550-1224-3645-8ecf-ba6d38029dea | -3.259 | -53.659 | 2024-12-03 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| d12fd31b-4076-318f-bc00-731a3b2cc842 | -1.7541 | -52.7789 | 2024-12-03 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a592fbfe-2e40-3970-9a7d-d841f8e6702d | -1.7541 | -52.7993 | 2024-12-03 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 449b8a87-021c-36e8-a208-7c6f89ec3e72 | -3.0376 | -53.8664 | 2024-12-03 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d82c1ee2-e068-34e1-ba98-e7ab47f9975a | -3.0761 | -53.3606 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 56b8b7a5-bf7e-3e48-91e6-b13e8367dc34 | -2.8212 | -52.5741 | 2024-12-03 02:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 3fa179e6-6061-3d00-811a-cb8df0492835 | -11.4355 | -55.9098 | 2024-12-03 02:00:00 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| d79f9b18-731b-3c28-aba6-4df90d3972fe | -2.7192 | -45.1982 | 2024-12-03 02:00:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d0c877de-e102-3dc5-ae38-ca95eb6ad421 | -3.0944 | -53.3804 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 279cb092-6675-3412-855b-a7352daf800b | -4.1684 | -48.5937 | 2024-12-03 02:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0fe2727c-b1af-37f2-83aa-e3e1777cd3b9 | -2.8854 | -45.44 | 2024-12-03 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| cf1ed1fd-32ef-3694-8cec-45fdd1955a0e | -3.0949 | -53.2385 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d94fd7fe-0130-39bf-86ed-59a4a5820bfb | -10.0997 | -36.499 | 2024-12-03 02:00:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 43e27d47-7a24-3089-94e2-bb674dde0681 | -3.5497 | -50.1699 | 2024-12-03 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 5b27b44d-9fcd-315d-b5f8-f866705520c8 | -3.5681 | -50.1903 | 2024-12-03 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ce96608e-56ce-3510-a26a-898006410e63 | -5.8197 | -46.4706 | 2024-12-03 02:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 96283206-486a-3b95-b79b-b86afcd52161 | -3.3421 | -51.2215 | 2024-12-03 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| ab0748d3-4afc-3baa-96da-384026511e86 | -3.259 | -53.6388 | 2024-12-03 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 963091f9-1650-3121-80a6-8438366f7c17 | -2.8197 | -53.0425 | 2024-12-03 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| bc822cff-a5ec-33ba-aee6-db3bf590b97f | -5.8009 | -46.4941 | 2024-12-03 02:00:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| b0bd6d37-b255-3f17-a896-d07ce83e14f1 | -4.5402 | -42.93 | 2024-12-03 02:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |


[Clique aqui para ver as próximas entradas](README17.md)
