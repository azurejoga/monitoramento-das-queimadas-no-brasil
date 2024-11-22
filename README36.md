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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c6624dd-77a3-3d24-a2ca-fa1db42f44c1 | -3.55133 | -54.58528 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87e6b130-4fb7-3f65-9f04-2ab571894fc2 | -0.09518 | -51.74616 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cea1c609-82b5-3471-904d-7ac9d88cb82f | -2.39752 | -46.06542 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4ae4d51-a81c-3855-962c-05533afd4c4c | -3.55193 | -49.90811 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e4d51ca-9407-3a3e-a965-1ac1667766a4 | -4.92328 | -48.64408 | 2024-11-22 04:36:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28ca2d86-1700-32b9-8044-bd6d983fff81 | -3.23132 | -54.24073 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9c8cd7b9-a3c4-3642-a97d-5646f9a57c5f | -2.26336 | -50.80696 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b290d62-5b1c-345d-8dc3-5c470c1f323b | -3.73103 | -50.43419 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b2f4249-5a69-3d2d-9dc0-0c4acebb625e | -2.01716 | -46.96026 | 2024-11-22 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d18f036-f6e4-3cad-b9d7-98eeeb49bc94 | -2.15187 | -53.78399 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de58f230-8fb2-3fe2-9d5a-24ba848f9110 | -0.26614 | -51.5424 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15a114db-7004-366a-aff3-0aefbeafa674 | -1.19711 | -51.95487 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b2edb091-11ce-31e5-b84b-1f3a57721da4 | -1.27406 | -47.89012 | 2024-11-22 04:36:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d822ca7b-0082-3341-9f5f-1b08ad9408e3 | -1.9636 | -48.38789 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 078990a2-65d2-30b1-bd17-7eb94225a884 | -5.95954 | -48.05575 | 2024-11-22 04:36:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c0c73dd-211c-38fd-8440-5de6b88b0c25 | -2.94049 | -48.33398 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 648d7ae4-a1c0-34f4-a3f3-036d7183f7a9 | -3.10557 | -53.1062 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 785461a6-890d-3d5e-a1ee-ff59bfaf4f67 | -2.54417 | -46.20902 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7930697a-efe6-39b9-b6ff-7f0dfc44835e | -4.04068 | -49.28876 | 2024-11-22 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e50fe836-7218-3d11-a491-96e33218e7a4 | -2.73052 | -46.08685 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dddf3c74-16cc-3b1d-8138-228d87b06f56 | -2.00157 | -54.51957 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3dabecb7-c9a4-31a1-b8dd-8f5a902c8aac | -1.91764 | -52.08234 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63eb2650-33e3-3458-b58d-52038123f1ce | -3.01898 | -45.14017 | 2024-11-22 04:36:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0cb3baba-ee80-3635-a14e-34abd6d00e18 | -2.68777 | -54.9871 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26e2392a-e13a-34ed-882f-adb63a57746f | -4.98894 | -50.72746 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43c806fc-ffef-3ad4-a7b2-6eea610d2155 | -5.5941 | -43.74278 | 2024-11-22 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bab1aae-cfbd-3b72-8b8c-803c17e14ff4 | -3.28586 | -53.86218 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73dcd0ee-1de4-3150-8b9b-7ad9914866f8 | -5.4737 | -42.07185 | 2024-11-22 04:36:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3a0323d7-e981-3519-8e4e-d47288c1ac91 | -2.57656 | -49.22152 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57b68d67-1681-3b02-a0fe-3f4640ff9d86 | -1.23053 | -51.78923 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42f2c5d0-5261-3a7d-ad8d-a3a4657d791f | -1.50642 | -52.03424 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15525249-987c-3697-bc40-e2f3037d59b0 | -1.61226 | -53.27514 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bd4021ff-a7df-3edb-91ec-e86782b7a871 | -3.21007 | -42.68935 | 2024-11-22 04:36:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6349177-4d32-3853-8387-2cd4e4ec8bac | -3.21259 | -54.24183 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b1635a7-93d1-307d-a349-079e849aba31 | -2.64058 | -50.58937 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bd6fae9-9e2b-3748-bac4-f644c94572d5 | -1.44764 | -53.39479 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2911cbbe-a18b-3d15-bc48-a11f58d98436 | -1.19269 | -51.95871 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3aee55f2-f20d-36eb-b12b-768d1f39888a | -4.40039 | -43.71764 | 2024-11-22 04:36:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac77b3b8-5c24-3705-8f55-7310829da02b | -0.26876 | -51.57397 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cec0e425-7234-3d59-97f7-50a787aebbf5 | -3.22683 | -54.26001 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 309c0c16-677a-341d-8dc9-587a09039ff1 | -2.66159 | -46.55384 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00bc9936-8c31-34c9-9dfb-6774197d5b34 | -3.33765 | -53.30899 | 2024-11-22 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8be9486d-69d2-37c2-86c8-36ce6ed8e132 | -2.55547 | -48.16753 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 708208c2-0f85-37af-847e-328158507eb6 | -3.10681 | -53.70911 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b38a759c-36e6-3568-97cb-242d2f12af40 | -1.26072 | -53.36422 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ceb444e2-6592-35b3-9781-746c9b101b26 | -4.33225 | -50.428 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c12c26e-710f-30eb-b41d-e811760b54f2 | -3.50672 | -53.81011 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5827451d-561e-30b8-bba5-b967665ab5a2 | -3.10925 | -54.2922 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ab85113f-03d7-3c53-bf07-e520a48d9e96 | -2.44244 | -46.54359 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4a5699a-beb6-3651-8d9b-2897244158ce | -1.59966 | -52.25716 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d36526ee-e4e5-3035-8d26-7c5629706e95 | -2.73568 | -47.53806 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45c5df28-c4e8-3f71-9572-0842f3382d1b | -3.19484 | -54.32581 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c489d5b-424f-32d0-8e96-7542a009d414 | -1.20083 | -51.95545 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b6fcd74b-4c7a-3c71-a947-fdb874e66eee | -0.1665 | -51.63078 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2ea52c7-03d2-39dd-bd3b-3b2d9cdea1b3 | -5.14741 | -45.81829 | 2024-11-22 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa5ba050-8a49-30b3-9817-8a6e21932341 | -2.1568 | -50.91634 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a55b127-5d81-34db-aba8-b63ada448af6 | -3.10255 | -53.98977 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e610755b-514f-34e7-a226-be5aa626e15b | -3.00794 | -51.0098 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 310cec8d-e148-3d97-adbf-fbe29800391b | -1.60901 | -52.58752 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7e7f8ef-a445-3ea8-be0c-4e4c69b51a48 | 0.44315 | -50.77404 | 2024-11-22 04:36:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a69074d-2c6f-3d8f-b7a7-823e6b5e435a | -3.03445 | -54.84638 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2b7161e-f9c6-31e6-a39a-86396d11552d | -2.09362 | -50.34667 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e372603-5840-3bf6-94ec-f85b8cd84bcd | -2.2387 | -50.47079 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| deb9bd98-e7f9-36a9-b738-58ebbe835193 | -3.52986 | -50.7532 | 2024-11-22 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e7d2d8b-1ee0-333b-9029-eafd2161d032 | -2.95843 | -51.45186 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75103ca1-afc3-3816-88eb-9c64cfc975c1 | -2.66351 | -46.16424 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1af5d947-5375-346b-b4cd-42aa5e4585fb | -2.72762 | -46.08244 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cb35014-cf4a-39cd-97bf-2061127d80e7 | -3.27711 | -53.83871 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fec6abe-31a9-3b3e-8ae8-05c7b33bca4e | -2.44734 | -53.68489 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35ce935b-f8fb-31fa-bf92-18778089e6a2 | -2.69628 | -46.23904 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51f6a3a3-6423-3eef-b389-77d3ed73e243 | -2.65186 | -46.57133 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6cacdc-320b-3ea6-9492-ae860d754d74 | -2.45775 | -53.69767 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47d0fbc2-de14-33ed-90af-9bef1957bafe | -1.71069 | -52.38517 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 318b636e-565f-385c-8074-22fdd0eac211 | -4.12313 | -53.81674 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8828e069-5dc2-39d4-b55b-a1e47863a359 | -1.12702 | -48.34833 | 2024-11-22 04:36:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0e49ad4-a561-3501-806f-cfa33d905f43 | -3.81617 | -42.4516 | 2024-11-22 04:36:00 | NOAA-20 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4907d24-822c-3b3c-925c-0c6b61f0747a | -2.70546 | -46.08698 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6254bfe7-bc27-32b7-9a42-dedb3e1223b1 | -1.8022 | -48.46518 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64f3fd2a-bbf4-305e-9dd8-d697080adcf4 | -3.2307 | -54.1023 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f47070-9653-3330-ab3f-07f845683e01 | -4.07066 | -46.84451 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1bb79638-b8cd-3d8a-9ab4-66a259fdde48 | -2.30333 | -45.50664 | 2024-11-22 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf6b0db5-e334-37fe-adc6-4e06724827e3 | -3.87889 | -51.94682 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95153138-2337-3fcc-aa80-f5eb34b18818 | -3.51234 | -54.68916 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e20ea03-3158-37ff-95ae-922c1a668734 | -2.4326 | -49.87146 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fb8f905-6ea3-319a-9c18-527ed97ade7f | -3.48409 | -42.30154 | 2024-11-22 04:36:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 132b46ef-197a-35de-848b-19fa5a59f966 | -3.0038 | -51.30423 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0921282f-7efc-3d56-9c25-4a501fe8b1a7 | -4.63865 | -49.54566 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 539a1876-78c6-31ce-a39e-230c91f52f48 | -1.40527 | -47.44333 | 2024-11-22 04:36:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 65e4eac4-eb1d-37bd-8de2-5409a4ff6aab | -2.70145 | -46.25155 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b5d1bb4-bc34-3b65-adba-cb4ccc097f9b | -2.09842 | -48.89147 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d12ea326-7e72-3d06-9253-f42f55d65f2c | -1.49047 | -49.68493 | 2024-11-22 04:36:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c4b7b94-182d-3288-b538-3039fe32b4a0 | -2.17437 | -46.69113 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf2dc4d2-8466-3c86-9222-93b8db60669b | -4.82387 | -43.69291 | 2024-11-22 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d65322d-5d46-3301-b143-2a1b9a44feb1 | -0.64964 | -47.47486 | 2024-11-22 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fef17b15-0d70-3477-aba4-7022635d049d | -3.58695 | -55.45052 | 2024-11-22 04:36:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0ce5b7f4-755f-3245-8f11-5feb0d10eaa9 | -2.54591 | -53.97521 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fb90c51-9ac6-32ec-800e-84b0de6dbac8 | -3.88518 | -43.99477 | 2024-11-22 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 261e4a76-b782-362b-91dd-97cd42501236 | -2.90244 | -48.3175 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c388a780-41a0-376d-bd59-307b9e8ef60f | -1.26365 | -53.37194 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b51925e8-c918-3f07-aff6-e6012401d8af | -6.38333 | -47.1542 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
