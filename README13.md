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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51055075-b185-333e-af2a-3a6af0ce8076 | -3.6402 | -50.5863 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 1f0cad9e-60cc-307e-ad55-5203ae9b82d6 | -1.3873 | -52.376 | 2024-11-14 00:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4c6cb41b-1267-3d38-b751-4b8b2b96ccaf | -3.781 | -52.0747 | 2024-11-14 00:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 280f07b7-cefd-3169-bc3f-06b26fcb4936 | -2.6565 | -46.9789 | 2024-11-14 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 74f4c50c-a282-3de4-a94b-d21902dd0e15 | -4.1451 | -46.2356 | 2024-11-14 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2f5d9339-1fce-3041-baac-8fd9352065cd | 2.6703 | -61.1879 | 2024-11-14 00:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e4f56c68-cd96-3727-a71a-4b68978b03b0 | -17.5872 | -57.5328 | 2024-11-14 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 185f77e7-fb73-3869-be2f-14e23577dd7c | -3.714 | -50.6046 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2e956982-972f-36d3-a91a-4c24278a3a44 | -4.0464 | -47.2328 | 2024-11-14 00:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| b72649b3-8358-3ac8-8e73-e01e822734ff | -3.2533 | -50.3899 | 2024-11-14 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3658c6dd-e371-386f-8df1-b4bcc2517fa3 | -3.4014 | -50.3011 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| fa9b1e66-3129-3b61-871f-d273cf27141d | -6.0472 | -44.0331 | 2024-11-14 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8d6d3012-e0bf-3dc3-a6c1-bcdd4b8fb23d | -1.6627 | -52.5561 | 2024-11-14 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| c5e44c1b-9af7-3406-9237-acb62c7350cf | -2.6751 | -46.9783 | 2024-11-14 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| f2d596eb-e857-3dac-8cfc-eaa81024bccf | -4.0682 | -50.0029 | 2024-11-14 00:50:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a0b1707d-6ca1-32ac-9025-097c471bcfcb | -5.3585 | -43.5522 | 2024-11-14 00:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| e2c1c977-cd0d-3a06-a13b-507baac8575e | 1.2852 | -60.4265 | 2024-11-14 00:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0d3cab97-983b-321a-bbe0-3fa893b60d69 | -4.0867 | -50.0021 | 2024-11-14 00:50:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1866a1b2-8617-3c31-b350-97387b7a1faa | -1.6627 | -52.5765 | 2024-11-14 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 3250f03a-79db-39d8-80c4-99df5538a71d | -3.4198 | -50.3005 | 2024-11-14 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6d4bd5b2-6843-3d4a-8453-3acf7c2faa04 | -2.0267 | -46.9519 | 2024-11-14 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 5ddce6fd-c0af-3148-b2b7-23b9112c4801 | -17.6066 | -57.551 | 2024-11-14 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |
| 7c7388a4-92c5-3b20-89f2-6deee3e62e5e | -5.2023 | -44.3473 | 2024-11-14 00:50:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ea6f4fcb-4c2c-32ea-a8c2-6a47de12ba32 | -17.5675 | -57.5351 | 2024-11-14 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| 07ed1c9a-51f5-3c71-9034-378a4d62bb3c | -4.145 | -46.2578 | 2024-11-14 00:50:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 438439ac-5f00-3919-8920-e89357c054b0 | -3.0504 | -50.3332 | 2024-11-14 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0b521206-a4d6-36c6-9318-e5a41745dce8 | -2.1953 | -46.3528 | 2024-11-14 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| ea467f0d-42b2-3a9d-89e0-f14d6f65576d | -2.0229 | -55.9178 | 2024-11-14 00:50:00 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 35c540fc-f6e5-32b8-b8db-b0dd165e717b | -17.2543 | -57.4698 | 2024-11-14 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 19376fde-8682-31d5-8759-799cbbc1a064 | -3.1244 | -50.31 | 2024-11-14 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 6cdf1c49-e128-3658-9822-ddb4c636618c | -3.0523 | -45.5237 | 2024-11-14 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 181.0 |
| 77dfeae0-b3e0-3489-901a-da4ae143f0cd | -2.0268 | -46.9299 | 2024-11-14 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 075247be-8db3-3bbf-981d-18d67a6bfab3 | -17.6263 | -57.5486 | 2024-11-14 00:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 31643333-77fc-3b2d-b659-ae0d09f33eab | -2.1953 | -46.3749 | 2024-11-14 00:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e8f648e5-a8ee-3002-8100-50e2fffbcec4 | -6.0472 | -44.0331 | 2024-11-14 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 823f11ac-8fe8-3004-9b8d-9473a72b7f1c | -17.5672 | -57.5557 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 97d6195e-f547-3b35-a8f1-52abdc90fb4b | -3.4013 | -50.3221 | 2024-11-14 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7799af7f-16e9-33d3-a4d4-ed18377f32ca | -3.7325 | -50.604 | 2024-11-14 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 2050288d-64e2-38de-b7ad-23c33aade9e4 | -2.1953 | -46.3528 | 2024-11-14 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 866c06b3-618b-38de-8609-50c057f9b51b | -17.6066 | -57.551 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 070531ca-17f4-39a2-a0db-9588e1a5c917 | -3.4014 | -50.3011 | 2024-11-14 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 77885af4-4293-37c4-94cd-bd8213c0af8b | -4.0682 | -50.0029 | 2024-11-14 01:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 1d8be8bb-5768-38f8-bce4-5b7bb159b042 | -4.0649 | -47.232 | 2024-11-14 01:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 8ff103b1-295e-3495-89d7-934c9abc15a8 | -17.5872 | -57.5328 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| a991890e-a5de-37a9-b92b-6543359948bf | -3.0524 | -45.5013 | 2024-11-14 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 61a27099-73c4-3e23-8bda-0079a1a520b2 | -1.8106 | -52.1652 | 2024-11-14 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 38cc9ea4-e7da-3477-a614-979f5ddca33c | -2.0267 | -46.9519 | 2024-11-14 01:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 93f62ba8-cfbf-356c-a4e3-1a2f36401bed | -2.898 | -46.8614 | 2024-11-14 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3ef28368-84ed-3095-940c-586135ae442e | -4.0003 | -45.5728 | 2024-11-14 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 3e727f7a-21fa-316f-ba61-e0fdb6eba8a3 | -3.1244 | -50.31 | 2024-11-14 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a3d34719-6778-3f5a-8717-7701a06d289f | 2.6703 | -61.1879 | 2024-11-14 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| cfd9c654-c08b-335d-9adf-c2aac971ce0e | -3.0709 | -45.523 | 2024-11-14 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 91c03d4b-0ea5-3880-a919-1fbe249072f8 | -17.7052 | -57.5392 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 2b6ad7dc-84a3-34d5-ab31-90ec80321c93 | -2.6751 | -46.9783 | 2024-11-14 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 188.6 |
| f9a8d867-dd8d-31e8-94bb-20c6f888b4ca | -4.0189 | -45.5719 | 2024-11-14 01:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 44155266-575f-37d3-a828-28183284b5b6 | -17.5675 | -57.5351 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| dbf6a63a-5507-3f1b-9ce1-6699493e84a2 | -3.714 | -50.6046 | 2024-11-14 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| bee07b12-c6b8-38f6-b791-7444e01b7fb4 | -17.2543 | -57.4698 | 2024-11-14 01:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 64146c31-408d-3f11-8bfc-2e17806200cb | -17.5869 | -57.5533 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 174.2 |
| dedb9fb8-74e6-3b74-bfb3-9457983a5dcb | -17.6263 | -57.5486 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 399abf03-b180-3833-b997-f4e3d6f9f1a3 | -3.0337 | -45.5244 | 2024-11-14 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| cb008987-029b-30c5-9d4f-aaea1790a1cb | -17.6076 | -57.4893 | 2024-11-14 01:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 32dda2d4-c7c9-37bc-9604-71fe7b738dbf | -2.0268 | -46.9299 | 2024-11-14 01:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| fbb38622-1c86-36f0-b677-996ccb3d3db7 | -2.6565 | -46.9789 | 2024-11-14 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 8c239cfd-334d-3d63-92ac-f12ad0b330da | -4.0464 | -47.2328 | 2024-11-14 01:00:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ed775a12-3d9e-3b3c-931f-1dda350bc47b | -2.6564 | -47.0008 | 2024-11-14 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 572c8be9-6e19-388f-9ba4-ee183cb9571c | -2.1953 | -46.3749 | 2024-11-14 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c2f4c595-0b2b-31b5-be28-63de16893d59 | -2.8791 | -51.7932 | 2024-11-14 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8bee5c37-ded3-307e-9312-65e40dee9c62 | -3.0504 | -50.3332 | 2024-11-14 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e33ac8f2-24df-3af4-b5b9-215b261b09f3 | -3.6402 | -50.5863 | 2024-11-14 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 682799b7-d1ea-3673-b785-cd73f55eb1a6 | -2.675 | -47.0003 | 2024-11-14 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 252.8 |
| cf15ce8a-f39c-309b-89df-3b3847c1052e | -3.0522 | -45.5461 | 2024-11-14 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| f15c7208-c136-39ed-abb0-9aac3d8ee3eb | -1.4078 | -51.1195 | 2024-11-14 01:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7766e0ec-4f71-3aef-b7c8-0fd7bbf2c07e | -4.0005 | -45.5503 | 2024-11-14 01:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 7411e786-9035-3b64-8db2-18a496201918 | -2.2139 | -46.3523 | 2024-11-14 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| eac436d1-2d7b-38bf-9895-136d51caaaf4 | -1.3894 | -51.1197 | 2024-11-14 01:00:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 494e9e17-e280-3d3d-85d7-9b32b458c559 | -5.2023 | -44.3473 | 2024-11-14 01:00:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 3653f7c2-cb27-3782-9a6c-ca706a80a9a9 | -3.0523 | -45.5237 | 2024-11-14 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 309.6 |
| e107d14d-a67e-3b2a-b511-60f454517505 | -1.6811 | -52.5558 | 2024-11-14 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 79f53655-e314-3430-87ad-96785d48e0bb | 2.6703 | -61.169 | 2024-11-14 01:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 9c7e56f5-9c91-3be1-b47d-061a122a179e | -3.6401 | -50.6073 | 2024-11-14 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ef8269e2-c9e9-3e7e-ba2a-408ada677c86 | -1.6627 | -52.5561 | 2024-11-14 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 0d6c73f2-b5d8-318a-85d1-b3f613773a80 | -3.05 | -45.53 | 2024-11-14 01:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5e496b-86f8-3056-bf93-83677e8d8d3e | -2.65 | -46.99 | 2024-11-14 01:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8c50631-03e1-3272-96e8-8bfe22db81e5 | -2.6751 | -46.9783 | 2024-11-14 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.6 |
| e5abf273-ce30-30dc-8b54-2ceec50e373e | -1.8105 | -52.1857 | 2024-11-14 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 7e92671c-2413-3577-b840-246f1e44f23a | -1.7921 | -52.186 | 2024-11-14 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 1136acc2-fbfc-3f70-8cb8-76d8f7a81731 | -17.2543 | -57.4698 | 2024-11-14 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 74c66263-c829-3619-8a57-e31f4bd025e0 | -1.6627 | -52.5561 | 2024-11-14 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 3f90d9ba-1702-3152-9603-141378da6212 | -3.0524 | -45.5013 | 2024-11-14 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b6bae182-f7a2-3596-bdf5-3c985a671ce1 | -3.0523 | -45.5237 | 2024-11-14 01:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 353.1 |
| 67a08b04-2a78-364d-871a-2ae7f1cf1d17 | -1.8106 | -52.1652 | 2024-11-14 01:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 729e6158-b628-3604-b127-c4b6a28f9ea2 | -17.6263 | -57.5486 | 2024-11-14 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| e80f6f34-02e0-303f-a926-ad445d932366 | -3.714 | -50.6046 | 2024-11-14 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| f392d41b-6f0c-38d5-995d-813c64a01356 | -2.0268 | -46.9299 | 2024-11-14 01:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 341203cc-8ca1-3b78-95d5-e32d0b6358d3 | -4.0189 | -45.5719 | 2024-11-14 01:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ffec8d47-88e6-3e13-9384-ea9a715cc2a7 | -2.1953 | -46.3749 | 2024-11-14 01:10:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ce1df113-738c-36ef-bb2e-49d89d53d367 | -1.3894 | -51.1197 | 2024-11-14 01:10:00 | GOES-16 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 9826db31-267e-3139-b21c-2cc938229576 | -17.5672 | -57.5557 | 2024-11-14 01:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| 3758b743-c21e-3127-9473-7c8193a45e66 | -1.9917 | -46.247 | 2024-11-14 01:10:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |


[Clique aqui para ver as próximas entradas](README14.md)
