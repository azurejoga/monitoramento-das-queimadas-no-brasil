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
| 3314f752-945f-3d94-9144-60c703450bac | -4.543 | -47.9934 | 2025-06-25 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4dcd8303-e4db-3122-a4c2-e644eccc4e88 | -7.0359 | -44.5708 | 2025-06-25 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 53d96e11-d995-3652-8c50-c87a56fc9a6c | -7.2028 | -43.0936 | 2025-06-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| d11aacd1-4690-37ad-a980-c5d2ba830f88 | -3.618 | -47.5352 | 2025-06-25 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1fa6d489-6a58-32a0-9a15-db4852af69db | -9.4993 | -56.0988 | 2025-06-25 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c6e1a576-ff18-3d4c-82db-965e4491d1f6 | -13.0601 | -48.8223 | 2025-06-25 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 5eddf5b1-2b05-3dc7-9f3a-2341450ba161 | -7.2025 | -43.1171 | 2025-06-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 5d71595b-e16d-31a5-b50c-55d43b0f8843 | -4.5429 | -48.0151 | 2025-06-25 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b16e6574-68e8-3884-a9cf-c7d66f3a21dc | -9.518 | -56.0975 | 2025-06-25 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a3b56bcc-6df8-3304-acd6-6171836c17a2 | -7.184 | -43.0954 | 2025-06-25 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 411db8b7-7a66-3bf5-a4aa-d84b19b2d682 | -9.577 | -49.107 | 2025-06-25 00:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 5cf76695-1d57-3a9a-a24b-948bbdeb2082 | -6.1792 | -48.0494 | 2025-06-25 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 316.4 |
| a6811c90-cb7c-37a0-bebb-2b39655c8e04 | -6.1604 | -48.0724 | 2025-06-25 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 9181bc24-a47b-37b2-934c-24e76c927ff6 | -6.1977 | -48.0699 | 2025-06-25 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f7e8d3dd-1fa4-3830-a8cd-6cd098368864 | -6.1791 | -48.0712 | 2025-06-25 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 331.2 |
| d32454c7-f230-3f6b-bd62-f4b5bbc90b86 | -7.0174 | -44.5495 | 2025-06-25 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 7677fc5c-a59d-3a53-8334-8f603f5bb1c4 | -6.1979 | -48.0482 | 2025-06-25 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 719463e7-4da9-37a7-aab1-882f31a20190 | -13.0408 | -48.825 | 2025-06-25 00:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2f3d8072-b8e3-3eb3-9e0f-1ebf7d82dc9b | -7.0171 | -44.5725 | 2025-06-25 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 3e24282e-0b21-3405-8fe4-8adb1da64eaf | -6.1606 | -48.0507 | 2025-06-25 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 97b0e222-a38b-3d40-b1cf-35693c810a5e | -9.5581 | -49.1089 | 2025-06-25 00:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5f9007ee-0708-315b-9e19-876c5737b6a1 | -4.543 | -47.9934 | 2025-06-25 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 330cc834-7135-303d-98c9-94455c24aacf | -3.618 | -47.5352 | 2025-06-25 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| adf7bac0-9d08-3617-ad96-7093e9631618 | -7.0174 | -44.5495 | 2025-06-25 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| b3327720-6a26-34e6-9c95-c73b05ffc008 | -7.2028 | -43.0936 | 2025-06-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| e72fb198-fce3-3cd5-b4b9-320c2bb727df | -6.1606 | -48.0507 | 2025-06-25 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 77aac0ed-4adf-3ee8-9ebc-014d6b24fe0e | -9.4993 | -56.0988 | 2025-06-25 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1b7933b0-7f52-3b4c-bdaf-974ea0acc448 | -13.0405 | -48.847 | 2025-06-25 00:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3f86e986-f3c1-3801-9572-e5f0f4c0c4c2 | -6.1979 | -48.0482 | 2025-06-25 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0f7787f2-b6a2-3750-add7-d1986fe5c4db | -7.2025 | -43.1171 | 2025-06-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| e7ae2ea0-808c-32bd-b865-ea48db1bfc17 | -6.2224 | -43.3693 | 2025-06-25 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| af4df49b-49ab-3aef-9270-0b33ed23bbd5 | -6.1791 | -48.0712 | 2025-06-25 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 287.1 |
| 0852b13f-3dac-327e-bbe1-e0622dbf46b8 | -4.5429 | -48.0151 | 2025-06-25 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| fba2bd49-0f88-3ae7-a42b-a0286bb7f795 | -6.1604 | -48.0724 | 2025-06-25 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 0aba0695-56a8-38f3-8768-d23ddebba394 | -6.1792 | -48.0494 | 2025-06-25 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 299.6 |
| fc97dd9f-7c7c-3854-bf4b-014399e13a96 | -7.184 | -43.0954 | 2025-06-25 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| cfd0c63b-7afc-30de-8431-edeecbeaedfa | -9.518 | -56.0975 | 2025-06-25 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d5093867-d4de-3e83-8a2a-1e97ac6dc966 | -7.0359 | -44.5708 | 2025-06-25 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1d26de4f-2fe2-32cb-80b6-8e929245db74 | -6.1977 | -48.0699 | 2025-06-25 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 3abc27ef-2b0b-325f-a047-dbcee5414634 | -13.0408 | -48.825 | 2025-06-25 00:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 121.0 |
| a59499a3-2c56-355a-bee9-4db7b3be6d9b | -7.0171 | -44.5725 | 2025-06-25 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 297a25f9-6929-315e-8aec-f1a9f64f9dad | -9.577 | -49.107 | 2025-06-25 00:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b85f1c11-1388-399c-8926-51e35c56b6f8 | -6.1979 | -48.0482 | 2025-06-25 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 24c9f251-d6da-322a-b81e-24f143653533 | -6.1791 | -48.0712 | 2025-06-25 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 59942e63-3602-337d-9160-102ff6ac5f31 | -7.0174 | -44.5495 | 2025-06-25 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 909621bd-6f4d-3ca0-990c-cbbe4d2313fb | -6.1606 | -48.0507 | 2025-06-25 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 00067415-5cb3-3ccf-bc87-33a22151b02d | -9.518 | -56.0975 | 2025-06-25 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| c0ed7397-1a8a-3160-8956-441c69de5ea9 | -6.2224 | -43.3693 | 2025-06-25 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| faba4776-8a97-3c6e-bae1-4c8fa6cca4a3 | -3.618 | -47.5352 | 2025-06-25 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| ae92b631-e2e0-374e-8854-6cc4fd87854a | -13.0601 | -48.8223 | 2025-06-25 00:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 65.0 |
| ecec69ce-43a6-3e23-9487-06ee5cb49875 | -7.2025 | -43.1171 | 2025-06-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| ed4e2e04-988a-3b56-8f6e-48318d3b25c8 | -7.184 | -43.0954 | 2025-06-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 49be826b-3d41-3297-9fc3-ce29a76a4800 | -7.0171 | -44.5725 | 2025-06-25 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 11684386-a5d1-370c-8e2d-f102cbfa1798 | -13.0408 | -48.825 | 2025-06-25 00:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 133.0 |
| f3e8cbee-7a26-30ad-8e18-7b67900073a0 | -6.1977 | -48.0699 | 2025-06-25 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| c2b10de7-99c4-3f06-b274-088fc6412480 | -6.1604 | -48.0724 | 2025-06-25 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 50dd3a83-12cf-3fc0-af6d-8fb40e90a3ab | -9.577 | -49.107 | 2025-06-25 00:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3347fb56-da60-36df-b33a-eb1536caf696 | -13.0405 | -48.847 | 2025-06-25 00:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 80c0754c-2dc2-3c55-89b0-948b2809c6da | -9.4993 | -56.0988 | 2025-06-25 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| bacc70c7-ae2b-33ff-9b38-492543162728 | -4.5429 | -48.0151 | 2025-06-25 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5c7abbae-2417-34f4-97c3-9c410bee02a1 | -6.1792 | -48.0494 | 2025-06-25 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 282.0 |
| 2b504ec6-dcd8-37bb-9dd7-6de99bd1a246 | -7.2028 | -43.0936 | 2025-06-25 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 184.4 |
| 1556bf10-9513-3bed-aa4b-1a2d0e85e480 | -4.543 | -47.9934 | 2025-06-25 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 6965ec0d-35d2-3bde-bee0-bfd26215e56f | -9.4993 | -56.0988 | 2025-06-25 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9aa12e33-4db1-3c63-9aa3-c48f937f5b15 | -13.0601 | -48.8223 | 2025-06-25 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 16d861d4-5039-3c55-9238-410a32aaff1f | -13.0408 | -48.825 | 2025-06-25 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 06c05280-092c-39df-b91e-81efb7b1b3f8 | -7.2025 | -43.1171 | 2025-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 669d6e89-b17e-39a8-b57a-792fd98c41e7 | -9.5581 | -49.1089 | 2025-06-25 00:30:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ff31f6ec-663e-3688-9213-4d9eff229e2b | -7.184 | -43.0954 | 2025-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 1ffee67b-7762-349a-a368-54d6c5e4465f | -7.0174 | -44.5495 | 2025-06-25 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| d6d89b4d-b008-36a3-85bb-ccdb3d32197f | -7.0171 | -44.5725 | 2025-06-25 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 29540fe7-1231-318c-bb3f-e35642ffd841 | -9.577 | -49.107 | 2025-06-25 00:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7195f5c7-c1ef-3426-b621-f7fc4ef747b1 | -13.0405 | -48.847 | 2025-06-25 00:30:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f9e54a21-a9d8-31d4-904a-c525525836cb | -9.518 | -56.0975 | 2025-06-25 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3a612f3a-0488-32f4-a7c5-948c2a1b11b3 | -7.2028 | -43.0936 | 2025-06-25 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 680317c6-9393-3da3-afe5-4ef234d7efa5 | -13.0763 | -48.83636 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7f4918fe-79c8-3d04-84f8-e1eb4cf63bf6 | -13.60855 | -43.97464 | 2025-06-25 00:39:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 3f1dcd11-0e55-3085-af0c-d21d2b0536bb | -17.14195 | -44.7884 | 2025-06-25 00:39:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f54c591b-6779-3d4e-b4eb-6217224b3818 | -14.13298 | -47.94446 | 2025-06-25 00:39:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f3c78b0a-03a9-33a8-b7d6-39443bbca0a1 | -13.04072 | -48.84151 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 96b6a5d2-4421-358b-a2ca-be12c9b971a9 | -13.03824 | -48.8232 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee852691-526c-37f1-9e30-b9c879ad209d | -16.3238 | -43.62956 | 2025-06-25 00:39:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9e3749d0-8afe-30e6-bd51-883686bfb72b | -17.13774 | -44.79502 | 2025-06-25 00:39:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4cd81b47-7881-325f-aa58-5471c421c369 | -21.20754 | -48.51685 | 2025-06-25 00:39:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| fc9a7002-8b16-34d9-ad72-0fd1876a3bc7 | -16.32177 | -43.61687 | 2025-06-25 00:39:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| f8582f89-b7b2-3c91-9cde-2d21918b280d | -13.04837 | -48.83105 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| a421703e-683d-3114-8eaf-5f19e388e227 | -13.0147 | -44.10236 | 2025-06-25 00:39:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b491a1a9-6535-3961-8bca-2295021160af | -17.14356 | -44.79892 | 2025-06-25 00:39:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 17df7889-2736-319e-9bc1-246453dbca74 | -15.39716 | -43.20124 | 2025-06-25 00:39:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 82610dd2-80f1-36ff-aae0-c563906ef418 | -13.03948 | -48.83236 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 3948b601-9d48-399e-afe4-b739d8c44859 | -13.05726 | -48.82977 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 569bbe47-22af-31cf-9694-a946086539a0 | -13.04713 | -48.82191 | 2025-06-25 00:39:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8ace9bdb-6838-34f6-b8e8-a335bbca22b3 | -12.75448 | -44.41268 | 2025-06-25 00:39:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9da63dd1-c7f9-3f6f-80ef-0d549adb693e | -13.6447 | -43.79187 | 2025-06-25 00:39:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bc872ae0-3e59-32ac-ac82-4a1fcd5b9864 | -21.20887 | -48.5274 | 2025-06-25 00:39:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3bc0a821-e4bb-3f5a-9f81-81037f0ef5d5 | -13.0601 | -48.8223 | 2025-06-25 00:40:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4b12b0e1-e93d-365d-92c5-0dc4fd822f1f | -7.2025 | -43.1171 | 2025-06-25 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| a052d46d-c0a2-3b59-8fd5-6dde2da10342 | -13.0405 | -48.847 | 2025-06-25 00:40:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 05ff0f77-23f8-3149-822d-69619017b2f6 | -9.518 | -56.0975 | 2025-06-25 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e47787e2-2911-3bcf-9da1-3ee908156d86 | -9.577 | -49.107 | 2025-06-25 00:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |


[Clique aqui para ver as próximas entradas](README2.md)
