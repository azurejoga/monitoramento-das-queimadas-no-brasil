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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e5ef99a-d83a-3116-9e4b-35f6f7659d83 | -7.34363 | -49.29289 | 2024-10-15 04:49:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c1759ed-c70b-31dc-8186-9dfa75f462f6 | -7.30716 | -48.60552 | 2024-10-15 04:49:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3631c9bb-081e-3c18-ad57-b291319f8483 | -9.27496 | -49.23192 | 2024-10-15 04:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1108b5b0-6b11-36c7-b3fc-4a0642b6880d | -9.16135 | -49.8294 | 2024-10-15 04:49:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7966207-d624-3d0f-83bd-69a911171bae | -8.60079 | -49.57993 | 2024-10-15 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3ce5788-d41b-3e1f-aac3-613e8c5a4352 | -8.55792 | -50.10226 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01fb20ab-f736-3a83-9ad2-85b363e47034 | -8.33451 | -49.66233 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12b1ba6-4f8d-3a3a-890a-45b5249c3c84 | -8.33087 | -49.98381 | 2024-10-15 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37a59a7f-71e4-306c-82d3-c15d6383a92e | -8.26334 | -49.61378 | 2024-10-15 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46c8bc65-d971-3039-b3c1-7b443af67797 | -8.20709 | -49.33994 | 2024-10-15 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b195b02-571c-3de9-8f65-40fd0ef0571a | -8.11604 | -49.35155 | 2024-10-15 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feddf5e2-0c4a-3bb8-b5f5-c4d5d2f8dcb1 | -8.11537 | -49.35597 | 2024-10-15 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 676004b5-9e46-3dbe-a9f7-82d090a3082f | -7.99305 | -49.84847 | 2024-10-15 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4192231-7172-3393-90d5-5734eee15221 | -10.82547 | -49.25009 | 2024-10-15 04:49:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe009f63-100a-3b14-a13a-798f5ff65ed8 | -10.51887 | -49.78964 | 2024-10-15 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8162641f-23d3-32bb-90e6-27dcbb69873f | -10.35147 | -49.61928 | 2024-10-15 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41ed649b-84c5-3817-bc75-c62b27cbb2c5 | -10.34634 | -49.62035 | 2024-10-15 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b582fad8-ab9b-3b6a-ba12-2c0bbb3d0872 | -10.15183 | -49.36611 | 2024-10-15 04:49:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7971f029-91fc-3d0d-a753-b0ac7be7bd77 | -9.77305 | -49.15712 | 2024-10-15 04:49:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e976db06-7945-3e68-89b9-6bc4c231ff5e | -9.77183 | -49.15877 | 2024-10-15 04:49:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc92aed0-7dfa-3bf4-b34e-474a00b58151 | -9.65616 | -48.97662 | 2024-10-15 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6725b3f4-f994-344a-a8a9-e0147c85ed29 | -9.62394 | -48.98171 | 2024-10-15 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30b3737c-be20-3934-8019-2764ed70ed73 | -9.62326 | -48.98647 | 2024-10-15 04:49:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7df4de83-63a7-31d6-9c9b-3b6dca022d3b | -9.53404 | -48.99097 | 2024-10-15 04:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f8d1233-ddf7-30c0-99a1-699fcbd6f7aa | -3.17403 | -50.47036 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6299743b-036c-334f-b917-2d067a38ba4a | -3.1955 | -50.45446 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2dba07e-ce20-3b68-ae81-0dbdf9764f27 | -3.19494 | -50.45806 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8c630b3-ed24-38bc-b855-5a1a733332f7 | -3.18821 | -50.45704 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5c04036-b7ad-39d6-93d8-33fee3885142 | -3.18428 | -50.46013 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60893ff1-f28f-3b5d-b4ee-d28ccf9e7158 | -3.18373 | -50.46372 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd48b626-c109-3185-a4fe-9e8eed9957f0 | -3.18092 | -50.45962 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2644998-ffd1-323c-b08f-30563b2bbd91 | -3.17908 | -50.46016 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c48bd426-574d-337d-a8de-35939c91b356 | -3.17572 | -50.45964 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f14114-65a4-3abe-9a90-41e2a509a4c0 | -3.17515 | -50.46321 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28b40ace-b875-3ab8-9c26-b3ab68124be0 | -3.17179 | -50.4627 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33e415e3-8476-3360-8424-0cd5268b59a5 | -3.17123 | -50.46628 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 726b2057-3677-35a7-80ba-4d2d81e297bf | -3.17067 | -50.46984 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 465ce229-3e3f-379c-8a13-e880b846eb41 | -3.1701 | -50.47342 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 156696d3-191c-3a91-91e4-347b405bd485 | -3.16842 | -50.46218 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d0b38a3-28cd-325f-b3f3-51c4eda52e82 | -3.16786 | -50.46576 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e60fe51c-4cd8-37f0-8cc5-9ac3acd3cde4 | -3.1673 | -50.46933 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8cf4ea0-a09c-3333-923c-295245355505 | -3.15833 | -50.46064 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98416407-9f60-390b-9f3d-56a1ed5b818f | -3.15497 | -50.46012 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79868754-a30b-3b64-919c-36b3c8b48fb7 | -3.15441 | -50.4637 | 2024-10-15 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21fb0705-8141-32d0-aa9c-09c39f6394e6 | -3.44196 | -50.17056 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f6bf99a-d4a4-3bd4-8743-1eb5eb93c04c | -3.42369 | -50.26475 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8dec738-82da-3158-b713-077c8a110760 | -3.37346 | -50.34222 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 58c94954-8e2f-38be-85fb-0d487a1ba6fa | -3.3729 | -50.34581 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8d6461b2-63b0-3c9b-9071-fca3eb1bcbd3 | -3.33287 | -50.3138 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e4a59d1-6886-3d11-a348-be9b47ef84a6 | -3.70255 | -50.11915 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74f43c98-520f-36cb-ac26-8ca6020897f4 | -3.70199 | -50.12284 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f1c94e3-0316-3566-8452-0a8bbe6bd24e | -3.69914 | -50.11863 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eb8ac12-e53b-32bd-87f9-9ac91a60e303 | -3.69857 | -50.12233 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a751adc8-c3a6-3f1e-b1d9-cbd1e73a2dd0 | -3.69573 | -50.1181 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dde11bae-9589-3953-b969-eb5798d46586 | -3.69516 | -50.12181 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04144c67-6929-35d1-a71a-ef022a60d2ea | -3.69459 | -50.1255 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c15b8deb-3bc3-3936-910b-b850373a36d9 | -3.69232 | -50.11758 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57da28af-261d-378b-a21c-3a095a1be999 | -3.69175 | -50.12128 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82e2e24e-a01a-33ad-beaf-fd961c5a65b0 | -4.37732 | -50.8071 | 2024-10-15 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c60c05fc-d9b9-3aee-9a9d-a580ea31d057 | -4.26122 | -50.58733 | 2024-10-15 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59b07911-9adf-31ac-ad10-d755647013f1 | -6.41007 | -50.78115 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73699019-2ba0-3f94-9b83-f7ab1d6e136a | -6.21605 | -50.90236 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1c76707-53c4-329e-911d-1fdbc1cdb159 | -6.21322 | -50.89816 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a47ebc7b-c8f6-353e-9c8d-babee15fa32e | -6.20757 | -50.88982 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e0478a2-95ab-37fd-a591-3e5ef9989f79 | -6.20474 | -50.88564 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7be6039-106f-311b-a85c-13bd179c1523 | -6.19796 | -50.88462 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c29125d-a37b-39f3-8805-bb10c166e7ea | -6.19457 | -50.88411 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 344f1a6f-9ebb-3c31-a4d5-e9f0b6dfbd50 | -6.19401 | -50.88775 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5cebbb22-1560-3b5c-931c-0442e2f66078 | -6.19118 | -50.88357 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c5350880-59e4-3e37-9252-700a5ac23d8d | -6.19062 | -50.88721 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c075ab7-e4da-3a32-99b1-cb429800068d | -6.19007 | -50.89084 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 584c7b8f-8b09-3f14-b96f-30c7e1e07b15 | -6.18724 | -50.88667 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12c67e9-3834-3918-8422-7ca4649f61e8 | -6.18668 | -50.8903 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4889a18a-1797-30da-9e91-686a2aff3fad | -6.13878 | -51.13506 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b91859d8-e30c-36b8-93f3-b9f684909814 | -6.11118 | -50.96837 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 406be7fb-e9f2-36cc-883a-b40440937b7f | -6.1078 | -50.96788 | 2024-10-15 04:49:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab89f882-fa94-305d-a568-8ca0d72a9c7f | -6.09105 | -51.09827 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc01a54b-4d3c-31b0-bdb1-6363adf54361 | -5.77104 | -51.10393 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cb09c2bf-e0d5-37e7-ab32-45b1f591724f | -5.77009 | -50.11071 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57b6010c-d977-3ff4-a646-625445ff65bf | -5.64463 | -50.33646 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5884e451-5c60-308b-9610-d10dc3c3231e | -5.64132 | -50.15002 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5b96005-687c-3427-9dc6-8803d9795379 | -5.63785 | -50.14949 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67f0710b-7d56-35b8-a458-899fbfc95e68 | -5.59235 | -50.15503 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 586ba333-7834-3ab5-ab44-a8f93c1e53ea | -5.45147 | -50.18044 | 2024-10-15 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f023838-bd53-3ce3-b8b7-19b16ff1e931 | -5.44821 | -51.01818 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 026dc07d-8232-390d-8e9d-774c9d55c9e2 | -5.34197 | -50.95774 | 2024-10-15 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b2f4da-2254-3cb6-9003-7c0660eefd11 | -5.26357 | -50.46989 | 2024-10-15 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6c5c84d-a32a-3cac-80f1-8b2225f4ec7c | -7.7966 | -50.21854 | 2024-10-15 04:49:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b9a8ed4-d3ef-3cf1-b425-26e79c9ddab3 | -7.07258 | -51.22856 | 2024-10-15 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db7bcd0c-675d-3a91-bf92-9780ca0b1732 | -6.90234 | -50.32602 | 2024-10-15 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 388c4e29-3e4f-30e5-963e-4106240cddb5 | -6.89887 | -50.32547 | 2024-10-15 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99a1cd3a-a0b8-33aa-ac47-e62f78db8307 | -6.85233 | -50.36306 | 2024-10-15 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb2d73c1-f1f2-3dfa-9d6b-4a96d4a5df21 | -6.6756 | -50.41478 | 2024-10-15 04:49:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca7269f4-4bba-3f34-a90b-ef20726f16f3 | -9.08057 | -51.52113 | 2024-10-15 04:49:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 063d8324-50ea-33af-94fc-66b4f6b9a860 | -8.42207 | -50.24252 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7167ec2a-f75f-3f4b-8e5d-809b65144d66 | -8.42145 | -50.24653 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb3b7632-b446-3493-a129-daa47ec57f8a | -8.4212 | -50.2453 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb89427b-d09c-3c02-8071-efd049127bea | -10.06064 | -51.40841 | 2024-10-15 04:49:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c1d943e-e43f-3072-b51c-19840de2efa6 | -3.2014 | -51.02971 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff1fe2b4-271c-3bf6-aa94-94f41c9c09f5 | -3.20086 | -51.03318 | 2024-10-15 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README62.md)
