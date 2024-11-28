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
| 2e9419b2-df41-3afc-8be5-46374d5473f2 | -6.1735 | -42.6221 | 2024-11-28 06:10:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 308b94e2-e3d8-3fe5-958d-caca123a6ee4 | -5.979 | -45.3395 | 2024-11-28 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 52f3ed49-23f5-38c9-8fc7-70b0a2ac269b | -5.9788 | -45.3621 | 2024-11-28 06:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 142.4 |
| f74f7d30-56b4-3388-bf42-d1a9f7bd120c | -3.3852 | -45.8465 | 2024-11-28 06:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 211.2 |
| baf78ce4-cc47-3ca2-830f-0a5ef23f6d90 | -5.9788 | -45.3621 | 2024-11-28 06:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 8cc43686-4ef8-3d23-a161-3e5923f0690f | -3.3853 | -45.8241 | 2024-11-28 06:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 98042afd-5164-3ae8-9af0-8b068de5e215 | -5.979 | -45.3395 | 2024-11-28 06:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c096ac3a-d35f-3397-9adb-a703e53e5094 | -3.3852 | -45.8465 | 2024-11-28 06:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 262.7 |
| 7d05c26d-df4e-348c-9879-75b9c1e6e0b3 | -3.3666 | -45.8472 | 2024-11-28 06:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 06d08f94-aff8-37fa-8164-10007a183dc9 | -1.5897 | -52.271 | 2024-11-28 06:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d262a18d-d5a8-3d3f-aa06-a14652d800a7 | -5.9788 | -45.3621 | 2024-11-28 06:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9fe5dc8f-51e6-31d8-9a88-d086345370ba | -1.5897 | -52.271 | 2024-11-28 06:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 64b905a6-e33a-3d44-ab4e-f89ac0b08ae9 | -5.9975 | -45.3607 | 2024-11-28 06:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9ff9d0ff-4853-3acb-b87c-d971f8f712bc | -3.3852 | -45.8465 | 2024-11-28 06:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 3162b5e4-da48-30b9-8d08-66c31f5a6394 | -3.3667 | -45.8249 | 2024-11-28 06:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 50fc0c1e-d007-35b5-be61-129db23599f5 | -3.4039 | -45.8234 | 2024-11-28 06:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 956f893a-dbe9-3279-9da5-7e9ed7726740 | -5.979 | -45.3395 | 2024-11-28 06:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 92c7619b-9e3d-3a1d-b401-1ccc8f911399 | -3.3666 | -45.8472 | 2024-11-28 06:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 5c60cdec-90ce-33d0-a618-4889d688f0c5 | -3.4038 | -45.8457 | 2024-11-28 06:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1844e53e-edd2-334e-ba70-dcee47182e03 | -3.3853 | -45.8241 | 2024-11-28 06:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 35f04dd3-91b7-316b-9f5e-92bfaacdc67c | -6.1735 | -42.6221 | 2024-11-28 06:30:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| d7cd8227-7964-3a8c-b0bb-9b8d3fafb5e4 | 1.31299 | -60.4082 | 2024-11-28 06:39:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4caa4d0-053b-3fab-8fab-bfd55c78fd8a | -3.3666 | -45.8472 | 2024-11-28 06:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 5dce747f-09c5-30c2-8fb9-4d436c864b3c | -5.9788 | -45.3621 | 2024-11-28 06:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| a6b257b7-e023-35d0-a489-e710595ef91f | -1.5897 | -52.271 | 2024-11-28 06:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e94c444c-e997-3ca0-a14a-efa86ff03e95 | -3.3852 | -45.8465 | 2024-11-28 06:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 172.2 |
| 3cd7fd56-128a-3dd3-b173-0eb91f63fa7f | -3.1467 | -45.2053 | 2024-11-28 06:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 72d8ed31-0591-3dff-8273-9b02f2af5f34 | -5.979 | -45.3395 | 2024-11-28 06:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 40b7b6af-0b2c-3d3a-9416-ebd5a665f879 | -3.3853 | -45.8241 | 2024-11-28 06:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 94cf6785-c7f1-3acd-b905-6eaeef496628 | -6.1735 | -42.6221 | 2024-11-28 06:40:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 37511eef-d44d-384b-bc9d-d40c751c43b1 | -6.1735 | -42.6221 | 2024-11-28 06:50:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 20093d44-411a-3f71-832e-315f44631a08 | -3.3666 | -45.8472 | 2024-11-28 06:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 067c135f-d398-3230-9204-899d2fbe4aa4 | -2.8347 | -54.1125 | 2024-11-28 06:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 3a752fc4-4910-3ba1-a132-7e36fac16618 | -3.3853 | -45.8241 | 2024-11-28 06:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 129.6 |
| b3fa66d4-5626-3745-be3e-5c795ee54269 | -5.979 | -45.3395 | 2024-11-28 06:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 1973af2c-0bd2-3301-96f4-785512c4a8a9 | -1.5897 | -52.271 | 2024-11-28 06:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 83fdea62-5211-37e8-b060-a772106b4596 | -3.3852 | -45.8465 | 2024-11-28 06:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| bbdb3282-faa4-3b54-8e83-e2b0eb25a837 | -5.9788 | -45.3621 | 2024-11-28 06:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 20e88bf9-8fa9-34f8-971f-b2ca39b6342a | -5.9788 | -45.3621 | 2024-11-28 07:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 3b5f2557-4bbe-305d-812b-895d40411c03 | -3.3837 | -50.1125 | 2024-11-28 07:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| bbc48bc0-77fe-3f7a-a604-34ba64344d67 | -5.979 | -45.3395 | 2024-11-28 07:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 2e8d5da3-87c1-3ace-8fc3-efa34070b7b7 | -3.3852 | -45.8465 | 2024-11-28 07:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 0d64da1d-3d61-3740-a36c-81bd67f6217e | -2.8347 | -54.1125 | 2024-11-28 07:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c19329d6-7807-3717-b667-e3e326bb89e2 | -3.3853 | -45.8241 | 2024-11-28 07:00:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| c0ce1772-1aed-3740-9f04-85e9d671cb29 | -3.3852 | -45.8465 | 2024-11-28 07:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 91.8 |
| a58d395b-2549-34fe-a4ad-2d472b9d4a16 | -3.3853 | -45.8241 | 2024-11-28 07:10:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 09134921-e123-3ee1-8e1c-096a6fea47c9 | -2.8347 | -54.1125 | 2024-11-28 07:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a90e3113-f698-3377-bdbb-5e469e1c7ea8 | -1.5897 | -52.271 | 2024-11-28 07:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 1a6e18ab-fa06-36ad-8fb5-38ead9349ecc | -3.3852 | -45.8465 | 2024-11-28 07:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dfaac063-5f5d-397d-b84a-d1112fd2c214 | -5.979 | -45.3395 | 2024-11-28 07:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8112f91a-97d0-3a79-8d73-b9881ddafa89 | -5.9788 | -45.3621 | 2024-11-28 07:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 79285c4a-71ef-31e0-9d04-be6f6a11f252 | -3.0724 | -45.1856 | 2024-11-28 07:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| e916b1db-2992-35b1-841f-c36bd609a2f6 | -3.3853 | -45.8241 | 2024-11-28 07:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 27a7ad51-aa69-334e-81c3-c0cd7c3159d0 | -1.3329 | -51.9257 | 2024-11-28 07:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 87b90360-d0c1-3524-8c73-8741385a661b | -3.3852 | -45.8465 | 2024-11-28 07:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f83221ef-0029-38ba-a9a4-6f4012fdfb7a | -3.3853 | -45.8241 | 2024-11-28 07:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8dc2a8b8-fff1-3985-a1b2-0c267abe4dde | -1.5897 | -52.271 | 2024-11-28 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 71abd99d-ddbe-388e-93d4-711123b5264a | -5.9788 | -45.3621 | 2024-11-28 07:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7ae61d4d-2be7-32b3-aa7b-09143be74ff9 | -5.979 | -45.3395 | 2024-11-28 07:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 31df4666-1e0e-3249-81a6-d107ff45fa04 | -3.3853 | -45.8241 | 2024-11-28 07:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 280d41f6-7cb2-34c0-997b-7811c009a4d4 | -1.3329 | -51.9257 | 2024-11-28 07:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| da444ade-acc0-3253-9f43-b48fecd3ff1d | -3.3852 | -45.8465 | 2024-11-28 07:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b68eb92a-9da0-3916-a8b8-fe1400a7abc2 | -1.5897 | -52.271 | 2024-11-28 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 8768815c-09e3-323f-b06b-dac76bb0d572 | -1.5897 | -52.271 | 2024-11-28 07:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 031bc6af-edcb-31b8-9ded-f99ee82136fc | -3.3852 | -45.8465 | 2024-11-28 07:50:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 930c9446-0ecd-34fd-9bb2-d617e8d0f405 | -1.3329 | -51.9257 | 2024-11-28 07:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 45a2107c-4e9e-366d-b355-6253cccdef9a | -1.3329 | -51.9257 | 2024-11-28 08:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 19d798f8-bba4-36a3-9119-7142a6f27ca9 | -1.5897 | -52.271 | 2024-11-28 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8375b6f6-79c4-3917-b0c6-18e86e55abc8 | -1.3329 | -51.9257 | 2024-11-28 08:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 10e8d015-4e2b-3e26-9b45-db57d13ab402 | -1.5897 | -52.271 | 2024-11-28 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e0d4bda7-fecc-3e29-bdf4-bc515c8e22e3 | -1.3329 | -51.9257 | 2024-11-28 08:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 52a679be-4baf-34c8-952d-0205a8ce63dc | -1.3329 | -51.9463 | 2024-11-28 08:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| bdac2dce-d0f5-3c1c-a131-24475666f7e9 | -1.5897 | -52.271 | 2024-11-28 08:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| eb0aa1e1-f670-33e3-bfa6-7cd514532a93 | -1.3329 | -51.9257 | 2024-11-28 08:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| c356ef5c-21f3-3cbc-b490-881e48d9d898 | -1.5897 | -52.271 | 2024-11-28 08:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ac6a1149-138a-321b-be41-8654689cad84 | -17.4 | -44.88 | 2024-11-28 10:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9d6097-c1f7-3961-8c55-1a0a329fc02e | -1.544 | -47.5513 | 2024-11-28 10:30:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 22d1227d-9361-3286-90ab-98d723949c4d | -3.3311 | -45.5129 | 2024-11-28 10:50:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 6a7e8d8f-2261-3630-82d1-17bef27e8615 | -15.73 | -45.95 | 2024-11-28 11:00:00 | MSG-03 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0dda19b3-c302-333c-8769-53cbabda3151 | 1.2354 | -55.9666 | 2024-11-28 11:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 11dbae64-6d0d-301a-8504-fd7f64ec1316 | -18.764 | -55.8444 | 2024-11-28 11:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.5 |
| aecd880f-832e-37fe-9b44-6e3e57a95115 | -1.5897 | -52.271 | 2024-11-28 11:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3407277a-f56d-3b26-b08a-1df2a45c3339 | -1.5897 | -52.271 | 2024-11-28 11:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9a0f29b9-82dc-3d52-ba7e-4a60d106d311 | -18.764 | -55.8444 | 2024-11-28 11:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 967c933f-d1b1-34f4-ba0b-537f78282c1f | -18.7644 | -55.8234 | 2024-11-28 11:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 91ec4822-cf42-327f-b662-5725595ee877 | -18.7644 | -55.8234 | 2024-11-28 11:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.6 |
| f1d640ae-6b41-398c-a4f5-5d5f7fc34696 | -6.1041 | -43.9593 | 2024-11-28 11:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4a114b97-3e03-354b-ad51-33fb7aeaba14 | -18.764 | -55.8444 | 2024-11-28 11:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 5f7d5a9a-e057-3385-b1f9-287eb8365fbf | -4.4845 | -42.8631 | 2024-11-28 12:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4441a4a6-ef82-3b7f-8e37-7a6d3fcbc9af | -4.6753 | -42.3799 | 2024-11-28 12:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 75.0 |
| 1d1d1d3a-76a1-3c32-aa91-ed25fcbd9049 | -3.499 | -42.0203 | 2024-11-28 12:00:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 6a044660-fe0b-3b15-a1a5-d0a341405201 | -18.7644 | -55.8234 | 2024-11-28 12:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| cc1c9ef1-8f9e-3f03-9f54-dbebbd370e70 | -18.764 | -55.8444 | 2024-11-28 12:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.0 |
| c11998c7-cdff-3be5-b161-b4d6825313c5 | -6.09 | -43.94 | 2024-11-28 12:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e44726e-6fa0-3f04-9af3-1734b2b4c4e0 | -18.7644 | -55.8234 | 2024-11-28 12:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 41588189-1be3-3e2d-a35e-35d68e455f6e | -4.6753 | -42.3799 | 2024-11-28 12:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| b4c7a734-611b-3d04-9b11-fb9c105b281b | -4.6565 | -42.3811 | 2024-11-28 12:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 2008da28-005a-3940-9fc7-b0ec0f41d9a1 | -3.499 | -42.0203 | 2024-11-28 12:10:00 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| a2b63778-1bb1-39c3-9f6a-89155ba17c18 | -0.8962 | -47.9071 | 2024-11-28 12:10:00 | GOES-16 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 09771b5f-8f50-3d6b-8dc5-e19abe9c014c | -18.764 | -55.8444 | 2024-11-28 12:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.5 |


[Clique aqui para ver as próximas entradas](README99.md)
