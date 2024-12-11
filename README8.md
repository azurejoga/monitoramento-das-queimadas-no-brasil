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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1e83ef7-dc40-3485-acf8-05b68bba3181 | -12.5425 | -58.3561 | 2024-12-11 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 5527aaa9-0b27-37a1-9438-22ab7c7a9628 | -12.5427 | -58.3362 | 2024-12-11 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b156b717-dc62-3d99-9029-3acf5aa18bb5 | -6.9161 | -43.4952 | 2024-12-11 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 2f8d3f5d-a0ed-356e-9ef7-419475260275 | -15.0865 | -59.6487 | 2024-12-11 02:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 47164da3-ef9f-3719-a4bc-6b641362bd60 | -18.0062 | -52.9861 | 2024-12-11 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 8f72a1f6-b775-3d64-a7c1-83b9897251b4 | -6.9592 | -42.9994 | 2024-12-11 02:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 181.7 |
| 25953e1e-4e53-3c84-8cce-b1d2777a5416 | -6.9161 | -43.4952 | 2024-12-11 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 2b527402-cb05-3c8f-9d5d-34a0a7006635 | -6.9158 | -43.5185 | 2024-12-11 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 8e55d531-b107-3856-aadb-cdd5d8c4b74f | -6.897 | -43.5202 | 2024-12-11 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 39015e60-e9f8-30ef-a215-0433f9f1991e | -6.1366 | -42.5544 | 2024-12-11 02:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| a6f5632a-f805-3c09-88bb-462dca55f29f | -15.1058 | -59.647 | 2024-12-11 02:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| a2fcbc1b-8369-3c5d-a4dd-49273dcb65ed | 2.7444 | -60.6381 | 2024-12-11 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 346f3c8a-e0d1-3c2e-ae92-77100528bcea | -6.1368 | -42.5307 | 2024-12-11 02:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| 2fc439d5-0bad-3775-9f9b-00244c67ece2 | -6.9594 | -42.9759 | 2024-12-11 02:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 67c550a7-127a-32ca-8620-57651153eb09 | 2.7627 | -60.6378 | 2024-12-11 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 772f3034-4f2e-38bc-ae7a-6a4ed670eaea | -6.118 | -42.5323 | 2024-12-11 02:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 0d703683-9ddf-3a67-8382-461f39f9dfcf | -6.9783 | -42.9741 | 2024-12-11 02:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 379c4aba-8da8-3ec6-85cb-d5724632122e | -15.0867 | -59.6288 | 2024-12-11 02:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 59bd593a-552e-3505-9c4a-06fda2dee6fa | -6.8972 | -43.4969 | 2024-12-11 02:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 247.5 |
| 7666a867-6cc9-3f31-b77d-613535a7fca6 | -15.0865 | -59.6487 | 2024-12-11 02:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| d8089ebf-7728-36d3-b060-7184dd1491e1 | -18.0261 | -52.9829 | 2024-12-11 02:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 76031912-350d-34f6-8705-656351387c46 | -2.8196 | -53.0629 | 2024-12-11 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 1767dde2-6f65-30fa-a44f-243531543605 | -6.978 | -42.9977 | 2024-12-11 02:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 8e693345-9af6-397b-86d7-6e431709f94d | -6.1178 | -42.5559 | 2024-12-11 02:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 66aa617a-0ada-335c-bafa-b4487fec2ff3 | -6.8972 | -43.4969 | 2024-12-11 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 209.5 |
| 69d284e0-6194-315f-b4cf-01b7e7d043e1 | -6.1368 | -42.5307 | 2024-12-11 02:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 134.1 |
| cf00631d-9c55-30a6-9de1-53284fe6cc31 | -6.9161 | -43.4952 | 2024-12-11 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 74f8dad8-45d6-36d9-b868-c56753ce0b89 | -6.118 | -42.5323 | 2024-12-11 02:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 45c37109-12fb-3d5e-83ff-1663ff41db7b | -6.9783 | -42.9741 | 2024-12-11 02:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| f1bd4069-a7c5-3609-abd8-e85e88967cb4 | -6.897 | -43.5202 | 2024-12-11 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 239.7 |
| d67dfd5c-fb6f-3146-b8ee-2fd5f84c655c | -12.925 | -55.0615 | 2024-12-11 02:40:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 2f5d1076-db64-36e6-9e03-bf36d2f799a0 | -15.0865 | -59.6487 | 2024-12-11 02:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b440fb05-afcd-3c75-9e85-68c3e45062bb | -6.9592 | -42.9994 | 2024-12-11 02:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 193.8 |
| b43b9751-082e-34cb-a143-4fdd6543ccb7 | -12.9252 | -55.041 | 2024-12-11 02:40:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a31e60bb-9d40-32c7-8d22-1ad1d51aa794 | -6.1366 | -42.5544 | 2024-12-11 02:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 7a5025cc-7d55-303d-859c-35e29a031cbe | -15.0867 | -59.6288 | 2024-12-11 02:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 54d76ce3-06e7-3bc3-8f23-9079b6a864b8 | -6.978 | -42.9977 | 2024-12-11 02:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.0 |
| 63881d3f-fbef-3d17-a190-f302003d98a0 | -6.9594 | -42.9759 | 2024-12-11 02:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 8b990779-44a3-3010-98fa-0a2431d5288a | -6.1178 | -42.5559 | 2024-12-11 02:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| acf8483a-58b0-3f2a-bcfb-de49dd2fb759 | -6.9158 | -43.5185 | 2024-12-11 02:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 5bb9d398-3923-3b83-8334-1f8b683546b5 | -18.0261 | -52.9829 | 2024-12-11 02:40:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 487be360-d4e7-364e-97ee-fa99a35b6357 | -6.9592 | -42.9994 | 2024-12-11 02:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 197.9 |
| 6028a3b5-7e23-3f21-89b9-bc8389ecdaec | -3.2351 | -42.4353 | 2024-12-11 02:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 79e09ace-902c-3294-bedd-d98ad78f86ed | -6.118 | -42.5323 | 2024-12-11 02:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 1f12fed3-5d84-382e-ab69-53d8a2851ded | -12.9252 | -55.041 | 2024-12-11 02:50:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 384e6116-909a-3be9-8523-0ebebd833dbe | -6.978 | -42.9977 | 2024-12-11 02:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 152.0 |
| 9dfe3182-97d8-33bc-9dbf-1456afcff149 | -9.9492 | -36.3106 | 2024-12-11 02:50:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 203.7 |
| 3f7103a4-6a5b-3854-b91e-b1a785068aa8 | 2.7444 | -60.6381 | 2024-12-11 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 958b4ae8-c52c-343b-b8f3-5da4f24747a6 | -9.9497 | -36.2836 | 2024-12-11 02:50:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| 37910645-245d-3530-8c1d-0a975fbe2111 | -6.9594 | -42.9759 | 2024-12-11 02:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| faa90601-7e09-357f-96e1-7248bf0ef688 | -6.8972 | -43.4969 | 2024-12-11 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| b20232b6-7c27-31ad-be48-39d097b3ccb6 | -6.1368 | -42.5307 | 2024-12-11 02:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 0b894978-2cc7-3ec3-84b1-2882fbb89b9e | -2.9666 | -53.1201 | 2024-12-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 06e79a31-3a48-3293-bca0-9a21e2abd302 | -6.9161 | -43.4952 | 2024-12-11 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 5e5fe218-7caf-3a57-9a2d-4e4397484f4b | -15.0865 | -59.6487 | 2024-12-11 02:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 0f953a96-83ce-3568-b8ee-9ea6dcc3377a | -2.8196 | -53.0629 | 2024-12-11 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| da48262b-5ed6-3e76-a684-e8ee03b0c5c3 | -6.1366 | -42.5544 | 2024-12-11 02:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 3d3ddcb1-e65c-307e-af0c-a696cbb073ef | -6.1178 | -42.5559 | 2024-12-11 02:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 79.0 |
| c4da321c-8c35-369a-b406-aaf264ffde1a | -6.9158 | -43.5185 | 2024-12-11 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 68d6f984-4c2c-31ea-9ef9-e6313ff1ed32 | 2.7627 | -60.6378 | 2024-12-11 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 84c520ee-f6ed-3bd0-a6dd-de73eb84a9f3 | -15.0867 | -59.6288 | 2024-12-11 02:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 05c23cde-e3ca-3d71-b8fd-5000d2d54040 | -6.897 | -43.5202 | 2024-12-11 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 9eb8fb70-af40-3df8-8aa2-ac0bf8963349 | -5.58755 | -35.55907 | 2024-12-11 02:51:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 14.0 |
| eac02161-cf9d-3cf3-b1eb-4ee058dc06a7 | -6.18168 | -35.30735 | 2024-12-11 02:51:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 71744019-425e-3190-af13-5071af737145 | -5.58646 | -35.56506 | 2024-12-11 02:51:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 45148073-a638-31ba-860c-f20fee48b117 | -6.17505 | -35.30627 | 2024-12-11 02:51:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 1b09322b-f73f-33d4-867f-584bdd841715 | -6.1761 | -35.30048 | 2024-12-11 02:51:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| bf41c2b0-ac0e-383e-b7b0-786629f9fb9d | -6.18275 | -35.30147 | 2024-12-11 02:51:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1fd427fd-9e88-350f-ad4f-02c96130cf2b | -9.95147 | -36.30572 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 729f2aba-37ab-3d18-9ed6-ab58da08f318 | -9.94248 | -36.31655 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 08767296-e0d8-39be-8126-0ce877d82584 | -10.61367 | -37.00883 | 2024-12-11 02:53:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 19b21a65-090e-30cd-89aa-ddbe01cacdf9 | -9.94785 | -36.32408 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 71a6ce27-66b9-36c0-b327-c97e562a0234 | -9.94904 | -36.31802 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 17ec2d84-eaf1-3333-b116-88bae1dc64df | -10.21471 | -36.29457 | 2024-12-11 02:53:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b42bd454-2b09-36fa-90ca-0b78f2544367 | -9.16801 | -35.71151 | 2024-12-11 02:53:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5ccc142c-cbbb-3353-8de8-e2851c6fa837 | -10.21585 | -36.28892 | 2024-12-11 02:53:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f9469425-bb3b-30fb-ba6c-faa8f01c427f | -9.94128 | -36.3226 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 359330a3-1ef7-3188-be3d-d2bf8d712ea6 | -9.9437 | -36.31038 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 198aa2b1-7890-3985-8c20-47e886f0be75 | -9.16908 | -35.70606 | 2024-12-11 02:53:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4ff08b4f-8010-336f-a32c-aafbbfe941f5 | -10.61197 | -37.01056 | 2024-12-11 02:53:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9cd8219b-0f6b-3d79-891e-cd4157e03964 | -9.95028 | -36.31174 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 409f262f-bd7d-310a-b36c-a527d2cdbab6 | -10.21648 | -36.29373 | 2024-12-11 02:53:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| c001259e-0576-3555-91cc-ef7c319e37c8 | -9.94491 | -36.30427 | 2024-12-11 02:53:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| fcb4303a-3162-3bc5-b1ac-7e0531609ee0 | -10.60687 | -37.00753 | 2024-12-11 02:53:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ceee5a5c-3012-3fc9-b18d-a01089bd55ac | -10.61309 | -37.00494 | 2024-12-11 02:53:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 72152110-6f5d-3304-b81a-ea4577fac4ce | -6.978 | -42.9977 | 2024-12-11 03:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.8 |
| f20fc39a-1bed-3350-b490-5d480aab5e01 | -6.9783 | -42.9741 | 2024-12-11 03:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 0653548b-227c-3f1f-8a31-1cf8f00079a1 | -6.8972 | -43.4969 | 2024-12-11 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 13613b03-16cc-300f-b1e1-3c655f317380 | -2.838 | -53.0624 | 2024-12-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9d565b58-b7ad-3a5f-9106-145021943a32 | -6.9594 | -42.9759 | 2024-12-11 03:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 34d8ccb2-8f06-3eff-85ea-58d90ecc7b18 | -2.9666 | -53.1201 | 2024-12-11 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| cfa1eea0-a798-3152-bcb4-0708f762ad7a | -6.9158 | -43.5185 | 2024-12-11 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 57eda81a-9704-3386-88f3-af76b8672906 | -6.897 | -43.5202 | 2024-12-11 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 2a643deb-c9c8-384a-9da4-b25e2cdd0c67 | -6.9592 | -42.9994 | 2024-12-11 03:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 172.8 |
| 91a91f4a-3e0a-36ae-85dd-c90f6d6c675b | 2.7444 | -60.6381 | 2024-12-11 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0bc0072c-9793-32a0-97b1-ae69250bd314 | -6.118 | -42.5323 | 2024-12-11 03:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 31c7297e-c06b-3719-86c8-e2daf156bbd3 | -6.1368 | -42.5307 | 2024-12-11 03:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 133.4 |
| 0a1173c7-aa41-31d6-bbd8-b05c8eebc3b8 | 2.7627 | -60.6378 | 2024-12-11 03:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 2b37d109-2981-3a33-b2f7-16600a03ce0e | -6.9161 | -43.4952 | 2024-12-11 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 109.4 |
| e6e05167-b992-3dc8-877b-ae0115898c95 | -6.1366 | -42.5544 | 2024-12-11 03:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |


[Clique aqui para ver as próximas entradas](README9.md)
