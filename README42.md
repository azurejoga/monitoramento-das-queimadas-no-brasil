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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a61a6d93-8647-3f9e-bf1c-375946d29582 | -7.67579 | -50.24895 | 2024-10-11 04:00:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4936ef7-3f0d-3f43-93e2-ba23f12fffa7 | -7.67512 | -50.25271 | 2024-10-11 04:00:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25e2b676-07af-3ffd-96a6-e95a0378b0ca | -7.17467 | -50.74441 | 2024-10-11 04:00:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f33cdae-7edf-3834-933a-ed21a755bdf0 | -7.17156 | -50.74379 | 2024-10-11 04:00:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc3f943-3cbc-31b3-9083-97260c1963ab | -7.17062 | -50.74907 | 2024-10-11 04:00:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56d9019a-3e47-3730-9e26-90b64eee4343 | -8.73684 | -50.77137 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee5329f3-db6d-3684-8b5b-21b5672e86d0 | -8.73606 | -50.7756 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8d21c15-4e02-3071-9ab0-836cbdd44ae5 | -8.57191 | -50.53398 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2a148cc-a10c-38bf-adae-ba6fed37ab06 | -8.57119 | -50.53793 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9794a48e-1135-3f5f-a687-271b52fcd25c | -8.56764 | -50.52503 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d51d8c-a8b2-349a-b792-2f28f9d9fa16 | -8.56693 | -50.5289 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d95bf47-3202-3705-97ae-387e7a776077 | -8.56621 | -50.53283 | 2024-10-11 04:00:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f29b878d-f649-37dd-9f83-17e9c96c1dba | -2.97657 | -51.35883 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5df18c79-8e70-32dc-9cf4-ab50d75153ee | -2.97563 | -51.36438 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ade2235-f912-36fa-b35a-1fbbb7d57be7 | -2.97471 | -51.36984 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 496a4458-cea6-3328-80f9-0bb283efa357 | -2.97471 | -51.35978 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a8a5346-5a68-3c95-9875-49f75bd6fded | -2.97374 | -51.36529 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 62621856-fa50-32df-bcdd-bfa078089b42 | -2.97278 | -51.37076 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 28b83d2b-c133-316f-81a9-87985b9ec98d | -2.97 | -51.3577 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 64e205f3-c8f7-3e49-afec-9f735fea4c74 | -2.96907 | -51.3632 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6322a6ab-5475-3306-921e-bef5dd15c898 | -2.96814 | -51.36866 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c80e9ad0-4e81-3e8e-a6eb-489b0e8c9258 | -2.80922 | -51.60069 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 159860d0-1ff2-3ae8-8db4-aac8f7a79b44 | -2.80826 | -51.60635 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c021aff-59f0-3721-87f0-c8fde9c2d5d8 | -2.80258 | -51.0103 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c2cea7c1-07e3-3c9b-8a2d-d07c544bf6e3 | -2.80165 | -51.01579 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 12ef9fe8-6669-332f-89f9-fb504a5ba718 | -2.64309 | -51.70753 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5b3559f-460e-3d1f-a554-1b48629d3d59 | -2.64206 | -51.7135 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4215c6b8-6928-3d0d-b412-7b1a46be0054 | -2.64142 | -51.708 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 143aa0fb-12ec-3869-ac96-82055d4e0e45 | -2.63635 | -51.70636 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f86a4778-a969-3ea7-aad9-6c618dbbdf21 | -3.33721 | -50.80453 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a9b5394-1e5a-31d7-acf3-b4098e0450c8 | -3.33633 | -50.8096 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ef15497-41e8-3e92-99db-77f1e427aa86 | -3.3309 | -50.80338 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2ab9ef8-44fe-3bec-9248-2c37d74a1570 | -3.28613 | -50.94821 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51c39e5c-506a-3bb2-ace3-0b8007dc0dba | -3.28433 | -50.94928 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4a20691-192f-3b82-abf2-f20ce1704173 | -3.28346 | -50.95449 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6646e459-1ef1-3e1f-b3af-a6508795b68a | -3.27975 | -50.94713 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc1f1b3c-e3ef-3498-aaee-92a253e8158e | -3.27884 | -50.95235 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a04d3078-1913-31c9-ae53-b56c6c6f19b2 | -3.27881 | -50.94302 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5a08888-b92c-3c19-aa6c-8d98bd0154ee | -3.27795 | -50.94817 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60a3a835-5124-394e-b465-00749813eb9d | -3.27707 | -50.9534 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b1e581fe-0e69-3630-b95c-7aef6c2bfd6a | -3.27338 | -50.946 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37eccd8c-1ab9-320f-9f9a-37b4a18677ad | -3.26698 | -50.94499 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8200305b-d092-3542-98bf-b03a570eb401 | -3.2355 | -50.85071 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b155cd2c-19d2-3fe8-b833-12166cd3ac0c | -3.23461 | -50.85587 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d72387a1-f7af-36c7-b616-96a0763ea133 | -3.22918 | -50.84943 | 2024-10-11 04:00:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b02794ab-f79e-38c2-8d71-b4af89ab2749 | -3.17041 | -51.30858 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ff3aaf5-6256-3e97-8092-e45fffac7ab6 | -3.16392 | -51.30716 | 2024-10-11 04:00:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9ebda31-d182-3a26-be20-5fa48b68e9e8 | -4.27412 | -50.9642 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 43cbea4e-8761-3159-8041-beebec583e3d | -4.26782 | -50.96312 | 2024-10-11 04:00:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 51cd6b6d-9123-38c9-bed1-670c9e33af24 | -4.08993 | -51.02278 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0e7be54-1e22-3567-b4e2-91d959eb8a0f | -4.089 | -51.02818 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 873223ca-1cd3-390d-a2aa-af1e94bbb908 | -4.08265 | -51.02714 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ab4c9b3-7d8d-3634-9b38-0ceb55f82dbc | -4.08174 | -51.0324 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b353a705-cd07-3287-9eb4-a6b4cf38141c | -4.06751 | -51.1148 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7fd4a4d-886a-3520-8f3b-8c17c0c496c2 | -4.06117 | -51.11349 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a06377a-2095-3f5f-bc92-4165096207f7 | -4.06039 | -51.11803 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c6f37ea1-b51f-38b5-950d-532cce1a27d5 | -3.80529 | -52.26157 | 2024-10-11 04:00:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7905ab4-f1ba-364d-b08e-3dcd91cbce86 | -3.68938 | -51.11445 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cae1c82-ee86-3812-a3c5-204c19b9ccff | -3.68848 | -51.11956 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5aedbbe-4dcf-3acb-aa78-5ad35b8269f8 | -3.68778 | -51.11787 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 248fa681-38af-3d7f-9832-a7f1ac9c1a47 | -3.68755 | -51.12485 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c61a444-695c-3c9d-aee5-33ac8f88db2e | -3.6869 | -51.1231 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c9376579-0b74-3c50-b317-36f8938c6182 | -3.68397 | -51.07023 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d160455-b771-3700-b06a-fd7e281a0af3 | -3.68306 | -51.0754 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c79d01b-008e-3b75-8a94-9a4d47b3297d | -3.68295 | -51.0684 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bfed1f9a-69ce-3ed7-a9c3-2668202e00d8 | -3.68208 | -51.07355 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 028df72b-0cc7-326a-ae31-34429189b2f1 | -3.68205 | -51.11856 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1ebd2be-a05c-3b46-ad87-d9ede44912cf | -3.67756 | -51.06922 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08e98dd1-744d-3d21-9dfe-49a430588fac | -3.67666 | -51.07429 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4394c0ed-72da-3d88-bf10-95775fa164d2 | -3.67569 | -51.07239 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9765508-0b58-3ae8-9f30-ab1bb1dc20cc | -3.67472 | -51.12266 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d132dee-1faa-3ed6-8a90-b8004cd929ae | -3.67378 | -51.12803 | 2024-10-11 04:00:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0314d11c-774c-3f71-9b4b-5d5c80c8eeb4 | -6.31545 | -52.78781 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca942a17-60d0-3654-930c-805498c8c634 | -6.31431 | -52.79397 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9608a47d-0329-3211-9f97-ff4271fb3db3 | -6.10063 | -51.22038 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72cace94-b6d1-3ff5-accf-6785b53ef3df | -6.09977 | -51.22521 | 2024-10-11 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b31e9c3b-283c-30e4-a2bd-e66cc24acf20 | -5.67938 | -51.2984 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a352a9f6-c66b-3c2a-b24c-230f1c11268d | -5.67851 | -51.30339 | 2024-10-11 04:00:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 141e0bad-d8b7-3b48-8680-beb0958b545e | -2.98731 | -52.9066 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 71e65f7c-acd0-39a5-8210-cdaee6b6313a | -2.98607 | -52.91372 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| cd77a9ab-3ed3-32f0-b0d9-bb3f30e77bd7 | -2.9801 | -52.90551 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a0c0bce3-3c1c-30dc-8bf2-81679de6156e | -2.97893 | -52.91222 | 2024-10-11 04:00:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 3a44a45f-92fa-3dcb-a01e-42293a435781 | -13.73537 | -41.81156 | 2024-10-11 04:02:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a765b83f-165b-34ac-9ed9-2d3ddc957b0f | -13.53116 | -42.55887 | 2024-10-11 04:02:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bf920815-1dcc-3375-801a-66de6155acf7 | -13.46872 | -42.58184 | 2024-10-11 04:02:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f52531f5-a91a-3f67-9e43-f004a8178401 | -13.6959 | -43.20134 | 2024-10-11 04:02:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5c79b38f-236f-3cc8-9e8a-0d2d1cc4a690 | -9.98608 | -45.14499 | 2024-10-11 04:02:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d7f83b0-b2be-393c-bd91-a405380c4a9e | -13.07755 | -43.37218 | 2024-10-11 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bbd548a-a702-3035-ae6d-6069451232cc | -13.07692 | -43.37602 | 2024-10-11 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6cb730d-213f-38da-af0b-4f24fa9a9c82 | -13.0741 | -43.37159 | 2024-10-11 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70d0b77c-b5db-3650-90f2-2345637b8719 | -13.11587 | -44.07533 | 2024-10-11 04:02:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 747052d2-4e54-35e3-b935-ad6993cace00 | -13.11518 | -44.07938 | 2024-10-11 04:02:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b417813-c31b-3f1c-a5ce-c37d4b0e9087 | -13.02158 | -43.75525 | 2024-10-11 04:02:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 87d23987-269c-35d0-976a-59298646d7c2 | -12.84434 | -44.61597 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d0e3294-3c94-3a22-b384-c059f2bf39d4 | -12.78314 | -44.8857 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d51ca664-c18f-3126-8844-0ca929a17b69 | -12.78174 | -44.8716 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6903eda-24a1-3865-a700-1f847af8b047 | -12.77944 | -44.88502 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 31377578-e5dd-31f8-9883-1de0f46dfb1c | -12.77882 | -44.86649 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| adc20457-6ee4-3cf6-be5e-bb8370761efd | -12.77867 | -44.88951 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d35fa146-e14f-3b97-8b88-9ff47bd85110 | -12.77805 | -44.87094 | 2024-10-11 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |


[Clique aqui para ver as próximas entradas](README43.md)
