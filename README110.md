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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4197e97b-7c00-371d-8746-5aeed03810f1 | -5.0399 | -43.6205 | 2024-11-29 13:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 68128b1d-4ee6-3ba0-b831-5ec81bdf5dad | -5.4546 | -43.2659 | 2024-11-29 13:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8239d578-3db8-3bf6-a9c7-5f637abeca89 | -4.1574 | -44.2726 | 2024-11-29 13:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7e5c8f97-693d-365d-b4ef-6d26ae3643c8 | -6.9422 | -42.8362 | 2024-11-29 13:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 185.8 |
| 741e1204-3956-3e8c-a6cb-cf5020442dc5 | -2.9844 | -53.2819 | 2024-11-29 13:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 47ec2bde-987a-30da-b3b3-707428510102 | -2.8851 | -45.5073 | 2024-11-29 13:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 711b3ead-c226-3ea7-a7f0-6632ff5b5e46 | -6.2417 | -45.2519 | 2024-11-29 13:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7d75a2f8-15ba-30ea-98b7-b1bb367fd5b3 | -3.223 | -41.1956 | 2024-11-29 13:00:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 9180931e-6a93-3d80-926f-9adb313330af | -6.9424 | -42.8126 | 2024-11-29 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| e74ccd36-5983-3c54-ba75-af86ff455f65 | -2.6498 | -48.7986 | 2024-11-29 13:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 3d40b0fd-f97c-34f8-8ad4-f53bef560d3b | -2.8426 | -46.7973 | 2024-11-29 13:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 91221823-3dd9-3c28-ab4e-569e66675029 | -3.74 | -42.12 | 2024-11-29 13:00:00 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1b11c58e-5141-35d5-b501-0b8748679ad7 | -3.77 | -42.12 | 2024-11-29 13:00:00 | MSG-03 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d429336-2015-3c4b-a623-22030e54789f | -2.6498 | -48.7986 | 2024-11-29 13:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 157.7 |
| d147aaaf-6633-34f8-baa8-740976b4b871 | -5.0399 | -43.6205 | 2024-11-29 13:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 281.2 |
| 2f3ba82e-31b2-351f-bdf0-8b64f453523b | -2.8425 | -46.8193 | 2024-11-29 13:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 10ce7985-e3da-3a24-a579-32e4641071f1 | -2.966 | -53.2824 | 2024-11-29 13:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 35cd3705-e45b-3d7b-baf2-d577823413b3 | -5.4546 | -43.2659 | 2024-11-29 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3feab316-4985-3ea8-8f0d-6268e8813b58 | -2.6683 | -48.7981 | 2024-11-29 13:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d4914f9b-c2ca-3169-b6e3-679d8b6f96a6 | -1.5869 | -53.8336 | 2024-11-29 13:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0d39d4db-4a44-396a-aa9f-6fe2ac252d40 | -6.9422 | -42.8362 | 2024-11-29 13:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 172.3 |
| 7fa65edf-e110-3860-8bb2-2a63227d183d | -5.0212 | -43.6218 | 2024-11-29 13:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 96d12c84-1ba2-3f0d-b569-81b47a2c420a | -2.6684 | -48.7767 | 2024-11-29 13:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 43f3833f-5a13-355d-a48c-8e38050aa10c | -3.0489 | -42.3254 | 2024-11-29 13:10:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 68ccc356-c014-3446-8f6b-2a33fc44e179 | -6.9613 | -42.8108 | 2024-11-29 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| ebfb6c6c-5aaf-3bc6-a6a9-c363cb5e1cb9 | -6.9424 | -42.8126 | 2024-11-29 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 2cea24fe-5dc2-3521-ae06-18fd1a4e26a4 | -4.0229 | -44.9176 | 2024-11-29 13:10:00 | GOES-16 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 57f4f63f-1303-36f8-afee-c7c09c587428 | -2.6499 | -48.7772 | 2024-11-29 13:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| feaa36cf-2404-3a14-8a37-2f6ddc68164d | -2.8795 | -46.84 | 2024-11-29 13:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 23471d85-1780-338f-812c-8a305805afcc | 1.6476 | -50.929 | 2024-11-29 13:10:00 | GOES-16 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 75b6fb9b-85a2-3759-9bd3-2096fa2100dc | -5.0586 | -43.6193 | 2024-11-29 13:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| b06a1513-dcf6-38dc-8dd1-f0b0550b98e3 | -8.3108 | -44.951 | 2024-11-29 13:10:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c399908d-6a86-39dc-a0dd-367073e692fa | -4.0546 | -49.0698 | 2024-11-29 13:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| a9643840-fb30-3509-88ec-6bba8505b52c | -5.0401 | -43.5973 | 2024-11-29 13:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 77149daa-952b-3589-a095-77c1b24254cd | -5.3789 | -43.3647 | 2024-11-29 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8948fb64-afeb-37b2-8a36-c29703306400 | -4.1761 | -44.2716 | 2024-11-29 13:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f9fa4c46-7a62-3e7c-bc2b-9e46bc517e37 | -10.2048 | -42.4744 | 2024-11-29 13:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 71a8cb65-b795-3df5-9487-f5fe555b3fb4 | -10.1861 | -42.4531 | 2024-11-29 13:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 125.5 |
| 49f3ba6a-430e-3d43-8692-d56232046a6a | -2.8851 | -45.5073 | 2024-11-29 13:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f6290ef6-b22d-3a8c-a439-9e10bfd5c6a9 | -3.7601 | -42.1257 | 2024-11-29 13:10:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| d6d12eac-a008-3517-acda-5b6a62e4b346 | -10.1857 | -42.4771 | 2024-11-29 13:10:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 192.7 |
| 7f12d16c-265a-3677-872a-004b497b7203 | -3.223 | -41.1956 | 2024-11-29 13:10:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 99.8 |
| d12e0c07-3c8c-3b13-ba38-cc9b3228007a | -2.9844 | -53.2819 | 2024-11-29 13:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 8facea91-af24-3ddb-b207-8582aff32b5d | -2.966 | -53.3027 | 2024-11-29 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ea1feb81-ed90-3008-8f29-6b8d968c2a09 | -2.8424 | -46.8413 | 2024-11-29 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fa33d6b4-afdc-3616-acb7-d17e03552687 | -2.6498 | -48.7986 | 2024-11-29 13:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 156.6 |
| df6598fc-f8e1-3f7b-87e4-ec7bbf27d41d | -2.966 | -53.2824 | 2024-11-29 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 95d84b2d-414f-3ed3-8d9d-6a705ed1c79b | -2.621 | -46.5618 | 2024-11-29 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| e44d83dd-691b-3c2f-9111-94776554c146 | -2.8426 | -46.7973 | 2024-11-29 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 55bc89a0-c039-3457-a235-06916c3a89fd | -5.3789 | -43.3647 | 2024-11-29 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 364fa957-080e-34e0-9253-84848ed66fbf | -3.7128 | -47.1379 | 2024-11-29 13:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fe7b3abc-10a6-32da-9b5d-66fc2a44d4d4 | -10.1857 | -42.4771 | 2024-11-29 13:20:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 116.5 |
| cf18473a-0018-3a69-a160-06608b04b45c | -1.6235 | -53.8733 | 2024-11-29 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 18b92791-4c74-35ee-903f-f86c1c5bd42b | -5.4546 | -43.2659 | 2024-11-29 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ca377fda-89b5-320b-b28d-18210ea62784 | -2.0439 | -54.6883 | 2024-11-29 13:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 36699483-089a-314c-99df-5a0729bf9065 | -3.3723 | -41.2848 | 2024-11-29 13:20:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 91.9 |
| b19e5d77-8d0c-3dc8-8a30-1c9175b175c3 | -2.8611 | -46.7966 | 2024-11-29 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d7b507af-6931-31d9-815d-00719da396c4 | -4.2342 | -46.8726 | 2024-11-29 13:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| bb481d15-ee75-313a-96f1-e3ab162c4caa | -2.8611 | -46.8186 | 2024-11-29 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| f95bb961-7eea-30ba-8a2e-361078aada1c | -2.8851 | -45.5073 | 2024-11-29 13:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| b74a904c-7aeb-3165-9bd0-aaee4d7dda5e | -3.223 | -41.1956 | 2024-11-29 13:20:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 02b12678-8329-3d04-94a5-3bf81c16f5ed | 1.6476 | -50.929 | 2024-11-29 13:20:00 | GOES-16 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 89.8 |
| e1de12a9-5732-3004-b192-998be237160f | -5.0399 | -43.6205 | 2024-11-29 13:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 0f63eadc-db16-36f4-8140-a30791ecd748 | -1.5869 | -53.8336 | 2024-11-29 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 7583f049-e748-3b58-83db-baccb5c37fa0 | -8.2737 | -48.0364 | 2024-11-29 13:20:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 189.8 |
| b8a5ac04-ec85-395c-b7a8-a4aed638605a | -5.0212 | -43.6218 | 2024-11-29 13:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 182a5c66-951b-3ec1-81d2-f1cf946be421 | -2.9844 | -53.2819 | 2024-11-29 13:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| fbc5b37a-21f0-30d2-96d5-d48e7f6345ee | -1.6419 | -53.8731 | 2024-11-29 13:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 974777cb-be8e-33c5-88e7-c943d487fb02 | -6.9422 | -42.8362 | 2024-11-29 13:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 181.4 |
| 60761a03-66f2-3950-886d-bafee1ac8750 | -2.6499 | -48.7772 | 2024-11-29 13:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 9cc939c4-82f2-38e1-960f-31981030cf89 | -4.1761 | -44.2716 | 2024-11-29 13:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| a6dfcbad-2e7e-3c40-b5d6-161cf5d41c6c | -10.1861 | -42.4531 | 2024-11-29 13:20:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 88.0 |
| a1749217-4c95-3ae1-9bd8-9f20d2f03e0d | -3.0489 | -42.3254 | 2024-11-29 13:20:00 | GOES-16 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 18d04915-3ab6-3c80-b3d1-79ca37fbab93 | -2.8425 | -46.8193 | 2024-11-29 13:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 05719cd5-a8fc-3a19-b2be-f3f2d217e8ec | -3.6942 | -47.1387 | 2024-11-29 13:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 273fa13c-3622-3931-a3c1-6bbf4f5049ca | -6.3687 | -45.6709 | 2024-11-29 13:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e55ccfb9-5cd4-357d-9741-29c09e5fa551 | -8.3108 | -44.951 | 2024-11-29 13:20:00 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| bd57cc24-7f07-3f5e-87ae-ba26752126c3 | -3.6943 | -47.1168 | 2024-11-29 13:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 4346fc02-0d01-3630-bf33-abf93031f195 | -4.2341 | -46.8947 | 2024-11-29 13:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 42e7b694-60fe-31fb-8164-87d649b4eb1c | -2.4662 | -48.4391 | 2024-11-29 13:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c80680ac-3364-32f3-828b-ac3648af691c | -5.0586 | -43.6193 | 2024-11-29 13:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0874382a-a8e4-3b37-be8d-0266b8859bd3 | -5.0401 | -43.5973 | 2024-11-29 13:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bc8a23dc-bf71-3868-a762-ceec61322a49 | -6.9424 | -42.8126 | 2024-11-29 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| ccaaff80-c236-3313-b60c-2a316d53c0ba | -6.7782 | -44.0876 | 2024-11-29 13:20:00 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| a0e5795d-5f05-3409-a854-f516a1fa343f | -3.0311 | -42.1604 | 2024-11-29 13:20:00 | GOES-16 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 1a9f585f-b090-3ba8-bf2d-48bcf799e524 | -6.9613 | -42.8108 | 2024-11-29 13:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 217b6f3c-a237-33dc-8052-eac97285d928 | -3.7129 | -47.116 | 2024-11-29 13:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 680208e9-df7e-3ec7-beca-2d9a42e95cd3 | -3.7601 | -42.1257 | 2024-11-29 13:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| c15cf289-7283-3900-9c4b-1af467c318af | -3.2515 | -46.6065 | 2024-11-29 13:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 1ab48f11-e771-3056-b1d0-8a0990cf9d53 | -2.6684 | -48.7767 | 2024-11-29 13:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| b27d6067-b7c9-3a8e-8837-c6106c2b94bc | -3.996 | -46.3094 | 2024-11-29 13:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 243.4 |
| b9312778-01e4-3708-a12d-c2a9ff6b827c | -8.2737 | -48.0364 | 2024-11-29 13:30:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 3dd558b9-6bf8-3224-ae0c-8de426b46f00 | -10.1861 | -42.4531 | 2024-11-29 13:30:00 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 96.0 |
| c3605133-baeb-3ce3-ab40-f2d57a219da0 | -3.2396 | -53.9216 | 2024-11-29 13:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 97c337ef-33db-374e-9644-ce5a70ec5333 | -2.8424 | -46.8413 | 2024-11-29 13:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d654ba66-960c-3062-a836-b26dac4269a1 | -2.9844 | -53.2819 | 2024-11-29 13:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 9a801ad2-4690-30de-ae46-c50090e5467a | -5.3789 | -43.3647 | 2024-11-29 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b08adc06-bb95-32e3-bfe4-808f88d9114b | -5.4546 | -43.2659 | 2024-11-29 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 850bcfff-b1e7-3356-9ee9-8891ec9008c6 | -3.996 | -46.3094 | 2024-11-29 13:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 15778384-6fb0-3a1c-b0c0-e9c08ed88316 | -3.6942 | -47.1387 | 2024-11-29 13:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |


[Clique aqui para ver as próximas entradas](README111.md)
