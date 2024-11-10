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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8da94147-2145-38d8-a077-899260e28e41 | -5.4546 | -43.2659 | 2024-11-10 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5a356835-cd7b-37fa-933f-159b825e46be | -5.2996 | -46.2156 | 2024-11-10 13:50:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| befe29e2-0dc4-3fbb-90d7-5510bad84d21 | -5.7475 | -41.9927 | 2024-11-10 13:50:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 510c79a5-78d9-3d65-b5a4-4339389fb781 | -1.8942 | -48.0216 | 2024-11-10 13:50:00 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 192f0e9f-cab9-393b-b237-7d318f2b92a5 | -5.7473 | -42.0166 | 2024-11-10 13:50:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 53efe0b8-95e4-3041-9514-4ae8edeb23d8 | -2.6387 | -46.7817 | 2024-11-10 13:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| d9ffb617-4360-312e-a7d7-fb453a37cbb7 | -4.3978 | -41.9226 | 2024-11-10 13:50:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| d958b85b-4dc4-32dc-b2c8-5eac4729bcfc | -1.9911 | -46.4463 | 2024-11-10 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 9b0a4df4-288a-31ed-ae70-9640b0828b22 | -5.2485 | -48.0641 | 2024-11-10 13:50:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| ac915756-5668-388c-908c-04305565302b | -3.9485 | -48.1508 | 2024-11-10 13:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 185247ff-da33-3e10-a3f0-21c434c12617 | -5.5629 | -41.6486 | 2024-11-10 13:50:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 4935c169-c593-304b-8765-d2ae27510d4e | -3.9669 | -48.1716 | 2024-11-10 13:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4886e418-b847-3644-aa62-5c219d5a0997 | -5.561 | -43.9544 | 2024-11-10 13:50:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 690be34a-27b1-3b6f-99e3-c4f265571cea | -4.4349 | -44.6229 | 2024-11-10 13:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| cb7809fe-3b1c-3532-8382-26a68aeb59c1 | -0.1563 | -51.5631 | 2024-11-10 13:50:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ef634b6e-4f40-37cf-9f9d-2896ad60b87b | -2.0664 | -46.0899 | 2024-11-10 13:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 9fbee43d-741c-3e00-b770-e6cf63aa3164 | 0.1196 | -51.2531 | 2024-11-10 13:50:00 | GOES-16 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 86.5 |
| c050a115-d185-3d6b-8ea3-0660b68d5d50 | -17.6083 | -57.4482 | 2024-11-10 13:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.4 |
| 0a72063d-e2a5-3eae-a83c-cb771254c47c | -2.5782 | -48.1345 | 2024-11-10 13:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 65578e55-adbf-3981-9e3e-2385dfb0a3c2 | -5.652 | -44.2471 | 2024-11-10 13:50:00 | GOES-16 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 055fdc65-11b1-3667-a3e5-8cc7bee37b69 | -3.9955 | -46.3981 | 2024-11-10 13:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| ca6b32fa-e93a-3cee-874b-966a81e56f33 | -3.9953 | -46.4203 | 2024-11-10 13:50:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 909a5c5c-b102-330a-a6b4-b901f36a388b | -2.0953 | -48.8338 | 2024-11-10 13:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 2c8b9f1f-b9c9-3ea3-8f5b-c6da380dff60 | -1.5116 | -54.9944 | 2024-11-10 13:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 28633260-44b0-3d42-8eaf-57ea1c0fc015 | -3.2721 | -42.5044 | 2024-11-10 13:50:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| cde67b45-e149-33d1-a63d-8a4c412d7791 | -5.7146 | -43.5261 | 2024-11-10 13:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d29dc8ee-1ef0-3c3c-8f3d-6ee27b834206 | -4.3979 | -41.8987 | 2024-11-10 13:50:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 71ffa4a4-446e-3d02-a8dc-c8ae5807e70c | -3.1424 | -50.4143 | 2024-11-10 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| b109f336-a093-35ed-87e4-6162263c007b | -6.3689 | -45.6483 | 2024-11-10 13:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4d6795c1-09bb-3a04-aec3-c460f94f1bc4 | -2.1021 | -46.532 | 2024-11-10 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 10c12f2a-d11b-3d2c-8445-4e5a8e613fd7 | -2.0842 | -46.3334 | 2024-11-10 13:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 5088f85a-ee0d-38c5-9403-820be8e7ee32 | -5.2483 | -48.0857 | 2024-11-10 13:50:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 405b2f1d-f592-30a3-b953-5ecd8098da84 | -5.223 | -41.8663 | 2024-11-10 13:50:00 | GOES-16 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 2bc3cdcd-411a-3f96-8bc3-bd0cc3f2eba5 | -4.911 | -45.8374 | 2024-11-10 13:50:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 9d740081-c9ff-39e3-9708-fc03a6dd5fdc | -5.2848 | -43.4179 | 2024-11-10 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| daa6268d-08fa-3ab4-bba8-f2a23be72542 | -4.1099 | -49.1315 | 2024-11-10 13:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 171.9 |
| f6c75d2c-1f80-3be0-821f-6d7fde50974f | -5.5441 | -41.6501 | 2024-11-10 13:50:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| a7f58709-d711-3427-adc0-05964be3112d | -3.1239 | -50.4358 | 2024-11-10 13:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 462.6 |
| b9dfe9a3-bd68-3182-a17e-9be654b0e0ff | -2.2095 | -47.733 | 2024-11-10 13:50:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3106fa6e-9b0d-310c-ac2c-caf2223d9880 | -17.2933 | -57.4857 | 2024-11-10 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 183.4 |
| efbffdc3-f645-30d0-a8a9-da4e63f826f7 | -1.4944 | -54.2763 | 2024-11-10 13:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1e81603b-a425-3e5d-83b1-3b3bc22f2af7 | -3.2615 | -41.0005 | 2024-11-10 14:00:00 | GOES-16 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 98fc39d3-f4da-3310-a93f-37386a080a19 | -1.9726 | -46.4467 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 50a35461-b6d0-3366-a818-14847b06ff66 | -4.0913 | -49.1323 | 2024-11-10 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| b8f68270-4051-3dc5-8d6e-8b38585ac38b | -5.6598 | -43.3673 | 2024-11-10 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 88c2785d-2673-3d99-9537-e15bd56e7736 | -5.7789 | -42.6546 | 2024-11-10 14:00:00 | GOES-16 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 7ecf9ce8-8366-3634-8c41-4365c383666e | -5.7661 | -42.0151 | 2024-11-10 14:00:00 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 1006b7d8-6053-3847-9ee1-1caf05f0de9e | -4.4167 | -41.8975 | 2024-11-10 14:00:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 1e090d53-9501-3124-985d-eff94b7a34c6 | -2.931 | -52.7753 | 2024-11-10 14:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| a79092d3-cbf7-3f69-96c7-dc898a3ed81d | -2.0292 | -46.113 | 2024-11-10 14:00:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7559c8e7-9d55-3642-86f6-4f3db5fdc78f | -5.4501 | -41.6575 | 2024-11-10 14:00:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| fee78c97-1ceb-316a-9a6e-a24050737f46 | -2.3076 | -46.0614 | 2024-11-10 14:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ba12dc78-8ade-3429-a4e8-ec0bcc5b24d9 | -2.0841 | -46.3556 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| d1c5e51a-e2ab-34dd-af3e-4c99260857a8 | -3.9483 | -48.1724 | 2024-11-10 14:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| e416e391-1a38-34e0-821f-92b9e25381c5 | -1.5116 | -54.9944 | 2024-11-10 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 90bb6d56-8acb-35af-9d25-de092874c865 | -2.6388 | -46.7597 | 2024-11-10 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| a5c7c118-ee17-358b-a402-8f94ca81ccd3 | -5.7473 | -42.0166 | 2024-11-10 14:00:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 3d34f56c-e23f-3d80-8e2d-0b977028f68f | -2.2095 | -47.733 | 2024-11-10 14:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 7cc17e9d-3d17-3ad4-bae1-78854f18b8bf | -2.0953 | -48.8338 | 2024-11-10 14:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| 0fda694d-df5b-336a-b28f-f614329c8dd8 | -3.9485 | -48.1508 | 2024-11-10 14:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 66503118-2c38-3ab6-b94b-1c3b50c8d5c0 | -2.0842 | -46.3334 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 5590ecb2-cf03-31ad-85d7-c72ab9d880dc | -6.0096 | -46.1011 | 2024-11-10 14:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6f231444-fbb8-371e-9452-5daa86e0d66c | -17.5885 | -57.4506 | 2024-11-10 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 2aabcfb1-e943-3d94-8d0f-063084e2a822 | -3.8413 | -44.1283 | 2024-11-10 14:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 20739c93-77d2-3275-96c3-bdf26e60fee0 | -5.223 | -41.8663 | 2024-11-10 14:00:00 | GOES-16 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 809d57b2-6136-36ba-89ac-d651703abb1b | -1.9911 | -46.4463 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| c0299c80-efd1-3aa5-bee0-9ddb2eed8c07 | -2.2502 | -46.5723 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d5877dbe-d51d-3976-85aa-3b519be255e9 | -5.2483 | -48.0857 | 2024-11-10 14:00:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5a7cf88c-36d6-3e8f-a617-f15c4574352e | -5.7146 | -43.5261 | 2024-11-10 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| eb9dacd9-dd33-37c6-bf69-902c856d6d13 | -4.3228 | -44.6519 | 2024-11-10 14:00:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c3d83078-9c1d-380a-9ff7-9680a5e53dcc | -3.5209 | -44.7825 | 2024-11-10 14:00:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a631cea8-6692-344c-b860-7cea6a4c100b | -23.9095 | -54.0606 | 2024-11-10 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| b541e91c-b9f7-3202-a5bf-9c56608b70f7 | -4.3059 | -44.379 | 2024-11-10 14:00:00 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 0349acfa-be95-3353-8b9e-2923f7c02d3e | -4.1567 | -44.387 | 2024-11-10 14:00:00 | GOES-16 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bf3e6548-99d9-3926-8f90-af1086aba26f | -3.6701 | -44.7303 | 2024-11-10 14:00:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 659322dd-014e-31e4-b3fc-cea80b3cc1d9 | -2.0664 | -46.0899 | 2024-11-10 14:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| fac39217-b11e-3b16-af5a-37d4f8569bad | -5.7475 | -41.9927 | 2024-11-10 14:00:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 48ab7af9-a99c-390f-addb-fa38da1bcb94 | -4.911 | -45.8374 | 2024-11-10 14:00:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e68d6832-cfbe-37c6-beb7-2dc116abcd01 | -3.1597 | -42.58 | 2024-11-10 14:00:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c7b589e9-e5f4-3f35-b565-11a5f4951e02 | -1.6923 | -47.3963 | 2024-11-10 14:00:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 560762c6-d268-3aa1-8fff-e94896dffe8d | -3.1424 | -50.4143 | 2024-11-10 14:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 3f2f1888-fd1f-352f-87be-d86ebd9a1d3f | -2.931 | -52.7549 | 2024-11-10 14:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b2d5436b-4ae6-3f86-a805-13b0cf326280 | -5.2418 | -41.8649 | 2024-11-10 14:00:00 | GOES-16 | NOVO SANTO ANTÔNIO | PIAUÍ | Brasil | 2206951 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 091fbc59-95ea-3e4e-a3ab-68911ea576cb | -2.4191 | -45.9915 | 2024-11-10 14:00:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| af63ffcb-e2f1-3647-ac49-02daa36e6859 | -2.1021 | -46.532 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 2dced5c7-2fd3-3222-8e88-21a936eeeb77 | -2.0477 | -46.1125 | 2024-11-10 14:00:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 10b6d05b-3515-3d7a-9dc7-80fd90a21c6f | -3.8877 | -49.1194 | 2024-11-10 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b6895503-7e7f-33ab-b626-f05384007736 | -6.3772 | -44.7868 | 2024-11-10 14:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 43e716cf-0bf5-3d41-aa78-50ae9f687e61 | -8.4156 | -44.1344 | 2024-11-10 14:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 204.4 |
| 7c49f275-6168-3fa8-a761-f5af049d206d | -2.0954 | -48.8125 | 2024-11-10 14:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 185.1 |
| 1f914ae3-bbc9-368a-a5a6-fe634f16bf06 | -4.1099 | -49.1315 | 2024-11-10 14:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 0dcd85a9-0f69-3708-bf32-d8447655e64e | -2.6387 | -46.7817 | 2024-11-10 14:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| ea2befe9-12d5-32e7-ab43-8a214ae86a00 | -6.3689 | -45.6483 | 2024-11-10 14:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8411904f-fc10-35b5-a064-3a699a442a88 | -17.2933 | -57.4857 | 2024-11-10 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 169.2 |
| 5448a698-f9ce-307f-8f02-ae9ea820a706 | -5.9919 | -45.9906 | 2024-11-10 14:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 279b1e0b-3f3c-3181-8fed-1d947d982a38 | -17.6083 | -57.4482 | 2024-11-10 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 189.6 |
| 7aa138a0-a962-3939-831e-6f436634de02 | -2.0656 | -46.3339 | 2024-11-10 14:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 1a11a07a-1952-3d1e-ac8d-d5ff5d6b551c | -4.3978 | -41.9226 | 2024-11-10 14:00:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 353c4886-4539-3106-9439-5f8df14d759f | -1.1672 | -52.0918 | 2024-11-10 14:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 68.0 |
| fadb4df4-e1a9-386c-85bf-97fb829b0534 | -5.2485 | -48.0641 | 2024-11-10 14:00:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |


[Clique aqui para ver as próximas entradas](README131.md)
