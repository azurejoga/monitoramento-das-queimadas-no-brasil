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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7be5c278-3a3c-35f1-8556-5edf8446eba7 | 2.9463 | -60.198 | 2026-04-14 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| dec2b413-eca8-369b-af9e-2879072edbb2 | -21.3438 | -47.0474 | 2026-04-14 00:00:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 8ff5a121-c9d5-33c6-8d34-9a52bce38cb2 | 2.9281 | -60.1793 | 2026-04-14 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 622db217-0dd1-3b4e-a5bc-5f676ef977f1 | 2.0138 | -61.0826 | 2026-04-14 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 1c14fdc6-a1f5-3dc7-94e2-e892029dad6b | 1.1028 | -60.5414 | 2026-04-14 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 36f3254a-10a7-3ef9-9430-12491a4b7226 | 2.9281 | -60.1603 | 2026-04-14 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 9703401e-8070-3903-8f0d-fffa78e5b66b | 2.0138 | -61.1015 | 2026-04-14 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 48241083-9e6c-394c-85de-f97893e8fab3 | 2.9464 | -60.16 | 2026-04-14 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 5fb94f31-ac45-3113-9ec9-ec8cfa5fe6ac | 1.1028 | -60.5225 | 2026-04-14 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ba9775e4-555e-3581-830d-15d404785ec0 | 2.9463 | -60.179 | 2026-04-14 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 182.3 |
| 00c6b5b5-326e-345e-a66d-1764dae7a371 | 2.5807 | -60.3367 | 2026-04-14 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d48d11c8-6839-3b5c-825f-5df163245b85 | 2.9281 | -60.1793 | 2026-04-14 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 2faa8f06-bc3f-3cd7-9d56-01ec01d5d93d | -21.3438 | -47.0474 | 2026-04-14 00:10:00 | GOES-19 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 97f4f2d0-59d7-3a65-aab3-e55453ad30f5 | 2.9463 | -60.179 | 2026-04-14 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 168.7 |
| 4b37c745-6ea0-3942-95ad-f91c23493d2d | 1.1028 | -60.5225 | 2026-04-14 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 1e526262-c7d9-3aca-9bd5-d9c2c24512ca | 1.1028 | -60.5414 | 2026-04-14 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 3038b51a-f190-3495-b0a0-311dfcff964f | 2.5807 | -60.3367 | 2026-04-14 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |
| c0871b23-0eec-3916-8958-6dc16e9c9ce8 | 1.121 | -60.5224 | 2026-04-14 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 954cf100-521d-367c-aedb-12fd69ffb076 | 2.9281 | -60.1603 | 2026-04-14 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b7c628c0-2b7c-322f-8746-f4448fba1640 | 2.9464 | -60.16 | 2026-04-14 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 88.6 |
| d7672fc0-ff4f-308e-8abf-118682f3dd47 | 1.1028 | -60.5035 | 2026-04-14 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| fac7e94b-2064-35b9-b5e2-ce036a4fc76e | 2.0138 | -61.0826 | 2026-04-14 00:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 5e49b825-37e5-3e3f-b945-c6dfd87488f9 | -9.7971 | -37.471699 | 2026-04-14 00:14:00 | METOP-C | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 23d335ec-9030-358f-837a-e12ba256013b | -21.190001 | -48.593399 | 2026-04-14 00:14:00 | METOP-C | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8a55cb5-5f58-3b6a-93b3-f2dd52b4b5e8 | -7.8293 | -42.046902 | 2026-04-14 00:14:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18dec0a6-7c87-3bdc-82ea-9ddda0db3dc9 | -21.328199 | -47.045601 | 2026-04-14 00:14:00 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 581f79d4-ee54-3860-834d-c255ad98b8c4 | -9.4478 | -47.8092 | 2026-04-14 00:14:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af2cec03-bf75-3a3b-9a6f-14880ce5fd83 | -21.3379 | -47.0439 | 2026-04-14 00:14:00 | METOP-C | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bf3dc7ba-549b-3573-b84c-6aad00a5dfe3 | -11.7029 | -44.735901 | 2026-04-14 00:14:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e0b09a4-e52d-34fd-b1b7-aa13135c250e | -9.8069 | -37.469398 | 2026-04-14 00:14:00 | METOP-C | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 74c78e23-54f5-36d2-87d9-242ccf93e04c | 2.9281 | -60.1793 | 2026-04-14 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 143.4 |
| e423eb63-5608-3286-aa20-c0d00cd70ecb | 1.121 | -60.5224 | 2026-04-14 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1bd373c8-cb8a-3baf-8e05-39de01020042 | 2.928 | -60.1983 | 2026-04-14 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 70ff1c52-12bc-3f08-b038-c3fe08c9a3e3 | 1.1028 | -60.5414 | 2026-04-14 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 643ede0e-ecfd-33f5-9059-152a667aaf20 | 1.1028 | -60.5225 | 2026-04-14 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6ff00aaf-6ca7-3379-af35-e60d5ad2f921 | 2.9463 | -60.179 | 2026-04-14 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 1293140e-fd1e-353c-a545-215b9a972207 | 2.9464 | -60.16 | 2026-04-14 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9709d07a-819d-3dfd-bff0-c2da107a8777 | 1.0846 | -60.5226 | 2026-04-14 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6059cbcc-3b7b-3c18-b196-553cc0976dde | 2.9281 | -60.1603 | 2026-04-14 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 6f7d53a1-9def-3e89-b21e-c9334797c6b6 | 2.5807 | -60.3367 | 2026-04-14 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 28749e17-8592-3822-a496-bd209435cfe3 | 1.9235 | -60.4967 | 2026-04-14 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 131858c8-56ad-3b5f-b087-6d1c8999d698 | 2.9464 | -60.16 | 2026-04-14 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f1d45e48-cf98-3af4-8911-5afdfb604756 | 2.5807 | -60.3367 | 2026-04-14 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fcb513bb-7aa0-3922-bbce-7b7760f659b0 | 1.1028 | -60.5225 | 2026-04-14 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 47f2f27b-7d28-36c9-ae89-a7bbcd38509c | 2.9463 | -60.179 | 2026-04-14 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 172.2 |
| a889222c-3def-3fa4-a8de-a8e64c917ab1 | 2.9281 | -60.1793 | 2026-04-14 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 548890e1-e837-3fe8-be46-bb719bb62993 | 1.1028 | -60.5414 | 2026-04-14 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 87e05275-aaad-30cf-97cb-dafe3c85000b | 2.0138 | -61.0826 | 2026-04-14 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9baaf697-03c1-33b0-8b8a-881c36dab654 | 2.5807 | -60.3367 | 2026-04-14 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7b1cb7fc-7590-3f56-9c42-d1961f667f8a | 2.9464 | -60.16 | 2026-04-14 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 9bf64782-080c-3fc7-abfd-28ba4e246b59 | 1.1028 | -60.5414 | 2026-04-14 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9151cde6-a9d4-30d8-9c0c-8433568ae690 | 1.1028 | -60.5225 | 2026-04-14 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a442dbe5-d07f-3275-8339-aeff1760037a | 2.9281 | -60.1603 | 2026-04-14 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 712e3396-726b-3881-b6b9-4ad93883ce3b | 2.9463 | -60.179 | 2026-04-14 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 2802e2bd-b493-3dae-bde9-8f11b4936111 | 2.9281 | -60.1793 | 2026-04-14 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 38ba5181-b845-3b23-8f20-22267ca2c721 | 2.0138 | -61.0826 | 2026-04-14 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 35a9f329-406b-32b7-9eaf-ef0a82f97cfe | 2.0138 | -61.1015 | 2026-04-14 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b50f0265-5f73-350c-b75b-b49db5d73583 | 2.9281 | -60.1793 | 2026-04-14 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 94.0 |
| fcd0e62b-7e00-3546-8cab-04d9100f6e2e | 2.9463 | -60.198 | 2026-04-14 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 2a5d88da-db40-35ad-8449-3a80ef18e166 | 1.1028 | -60.5225 | 2026-04-14 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 631e8231-fcff-31ce-b137-e0cacb1bb45a | 2.9464 | -60.16 | 2026-04-14 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a7c57831-0b31-36b9-89ad-6edd40f80ded | 1.1028 | -60.5414 | 2026-04-14 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7744b8c0-70f7-33e5-bd51-0e52cc5e88a2 | 2.9463 | -60.179 | 2026-04-14 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 8de7bb79-1c5c-3754-aa61-e17cc0b7d4ab | -21.71268 | -57.04648 | 2026-04-14 00:54:00 | TERRA_M-M | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce6a26ae-0587-3dd1-9a10-322df820ffde | -11.43285 | -55.1002 | 2026-04-14 00:56:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b23289ee-be78-3de4-9d4d-e1a12cbe5ea2 | -11.4225 | -55.10178 | 2026-04-14 00:56:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4a1b9130-a73a-3f38-96bd-bef961d3871d | 1.1028 | -60.5035 | 2026-04-14 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 02d39361-3899-3e37-bea8-0138ad0d8f88 | 1.121 | -60.5224 | 2026-04-14 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d7260494-7707-3047-aaac-eedb54fd6718 | 2.0138 | -61.0826 | 2026-04-14 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ee7197b4-6c1c-30df-883d-6794eb5a2c46 | 1.1028 | -60.5414 | 2026-04-14 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b8f38ce3-de8d-3fbb-ab50-05c1cb609765 | 1.0846 | -60.5226 | 2026-04-14 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a3ce003c-6344-37dc-ae72-7f3377b1f2f6 | 2.9464 | -60.16 | 2026-04-14 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 5b0dd2e5-a986-39a5-9d73-944d53f14ca8 | 1.1028 | -60.5225 | 2026-04-14 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3cc9376e-fa73-3742-9c04-e6f44a7ca842 | 2.9463 | -60.179 | 2026-04-14 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 115.4 |
| ed7bee5d-2c82-3a21-80c4-4c5c3a29a748 | 2.9281 | -60.1793 | 2026-04-14 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 128.5 |
| b091645a-6cb4-3442-8a2e-5484a2c0150f | 1.09966 | -60.52176 | 2026-04-14 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| c163e2e7-fa67-322b-8587-a208d706c0d4 | 1.09843 | -60.53076 | 2026-04-14 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 205789cf-8524-3cc1-b0c5-e1a0e0c55cfa | 1.10858 | -60.52301 | 2026-04-14 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 7e0782cc-5ccf-3fd0-bb7f-6b89e863afd3 | 1.10611 | -60.541 | 2026-04-14 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0ec35901-9e41-3755-9a49-a95a918e6f76 | 1.10734 | -60.53201 | 2026-04-14 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| ce3d382c-3545-363c-b695-442f2a0f9f67 | 2.58932 | -60.3418 | 2026-04-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 40ebb76e-79a6-3df4-95cd-f893144d3ef2 | 2.23959 | -61.27623 | 2026-04-14 01:02:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 47c4867b-fa1c-3d5a-ac27-de60db8ce1bf | 1.4862 | -60.9185 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2425b2bd-b7de-3d81-a31b-339fc0820b8b | 2.93436 | -60.17749 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 43bfa4c1-fe8d-377a-97a2-fddb84e2368d | 1.32496 | -60.6202 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4c816a08-d183-3b25-bc24-50d1ee89957c | 2.40971 | -60.24138 | 2026-04-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 70ff2c4b-7584-33d2-9bfb-d17885fbf3bf | 1.85381 | -60.73059 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2c17f903-ca7d-3b62-b080-0f9235feab2e | 2.23077 | -61.27499 | 2026-04-14 01:02:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95f45142-217b-3b70-856f-f63c722258e6 | 2.95397 | -60.17047 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f5395815-2a2b-387a-8602-141b0aaeffd1 | 2.57991 | -60.34372 | 2026-04-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d6c7413a-85f6-33be-810e-30ec11d157e6 | 2.95266 | -60.18 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4ffc49cd-8628-33db-9ed4-39166ce7cbca | 2.06262 | -60.95985 | 2026-04-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55ef153e-86ec-3ab2-8fbd-da81d3cb9e60 | 1.83902 | -60.83797 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2abfa721-35ac-36bc-aea6-8f29223bfdde | 2.57215 | -60.33311 | 2026-04-14 01:02:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b9914d21-74b5-3224-96f3-ecaae6165fcb | 1.355 | -60.67611 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9f562de2-2bc5-3d0c-9c47-a711962a42a3 | 2.01667 | -61.08311 | 2026-04-14 01:02:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 08d9fbe7-48a5-3232-aa8f-26fa358cdc59 | 3.42762 | -61.02277 | 2026-04-14 01:02:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a8385c02-c0bf-3ae2-9bed-ad16b302f71b | 1.84025 | -60.82905 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8a9bf01e-988a-3df6-86df-219a642f2c59 | 1.32372 | -60.62918 | 2026-04-14 01:02:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9682e0b3-f64e-3edf-a7ef-4b44154d27ff | 2.94481 | -60.16923 | 2026-04-14 01:02:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 13.9 |


[Clique aqui para ver as próximas entradas](README2.md)
