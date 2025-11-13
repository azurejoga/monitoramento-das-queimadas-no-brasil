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
| 9f5874ed-d4a0-3457-afca-cee950373133 | -5.19303 | -44.27773 | 2025-11-13 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69c4b88e-d21c-30aa-b31b-2d2f40c23850 | -3.10646 | -45.76932 | 2025-11-13 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36fc33ee-21df-387a-ba5d-09cb2ae320ca | -2.64218 | -49.21641 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28dae5c3-1e20-383c-89fd-fd17e9c2cf7a | -2.00455 | -54.45785 | 2025-11-13 04:12:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37882d61-787c-30cb-afb2-2bd24547512f | -0.72039 | -48.64387 | 2025-11-13 04:12:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7caf2d06-005b-368a-b2b6-6c4288c7d098 | -5.64742 | -41.08591 | 2025-11-13 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d620a68a-5e61-3a1b-870b-bcdf5d4b83e7 | -4.71837 | -49.24514 | 2025-11-13 04:12:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64cd7748-c7f7-3099-bdc1-24df0d406302 | -4.77418 | -46.44644 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d79425c0-516b-38f6-9aa7-b565de275e01 | -4.67352 | -45.80169 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f41372b3-a423-3915-a447-6737fa2629c3 | -3.09015 | -49.26928 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7625ef79-9885-3cc8-9259-ec39c1845e4d | -1.94076 | -52.09648 | 2025-11-13 04:12:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb6d2616-b785-3c8e-b532-870b7ef807b1 | -5.04658 | -41.10923 | 2025-11-13 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2f2ce107-5066-3e55-ae63-821a4cfc7c98 | -3.094 | -49.2748 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 52e1891b-9aed-3c6d-ab33-6e429aa237dc | -3.40299 | -50.45247 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b90b267-7474-3b55-9fec-8ea38554c9c1 | -3.6739 | -45.69041 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85ff69f4-964b-3475-811b-468fc1767516 | -2.16985 | -48.36842 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b286d94e-6fbd-364a-aaf3-9279bcc4ce51 | -0.73185 | -48.56995 | 2025-11-13 04:12:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b290dcce-7988-3bd6-871a-3d470c38745c | -2.86526 | -51.4763 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05f90c7a-153d-3cd3-9385-52624d3e830f | -4.19555 | -46.22623 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e799d0aa-a241-365e-8ae2-b6fd1108dd4c | -4.61331 | -49.29298 | 2025-11-13 04:12:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fde4458-0ff1-3635-8aa5-e394e5f5972f | -1.69614 | -46.57236 | 2025-11-13 04:12:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e00a34a-3f30-3932-9e19-e5d87967cc08 | -3.06462 | -40.08423 | 2025-11-13 04:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 778a72de-191c-3e2f-ad03-f30fc52f6ba9 | -3.85861 | -42.74971 | 2025-11-13 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a11bc65-9a39-3b50-9d1d-5a0123c33853 | -1.63264 | -45.81339 | 2025-11-13 04:12:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ebf5bada-0e9d-3869-9926-ebec3b243b39 | -4.25698 | -44.59949 | 2025-11-13 04:12:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10f585ed-49fa-3f91-bec9-7bfd2c8e8c98 | -6.1047 | -41.6048 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04759b50-2120-30b3-808b-e3e9cb94f7e0 | -4.45976 | -38.39162 | 2025-11-13 04:12:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 1981ea76-e0e8-393c-86e2-e34337c7ec59 | -3.40251 | -50.45533 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38e856a8-175b-3df9-8327-35b2cddc5c6c | -2.72508 | -47.40966 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6c322a0-801b-3999-bc7d-0b896a5818b3 | -4.75805 | -48.8391 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34167a48-d1b5-33a0-83db-fa9b7b14f42e | -4.71203 | -46.44234 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 47ab0653-ff8a-3687-b61f-fd5617193f6d | -2.85565 | -51.28228 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9533a859-5c8d-3d96-afa5-52df9e70bb7a | -4.69796 | -49.65346 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb25970f-3998-3f5d-9e73-7c616cd0adb8 | -6.08802 | -41.62411 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aba29e68-aefd-3219-8958-91c7ff7ad702 | -3.15185 | -50.26573 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3589dbd-6055-37f9-800d-35eaf0946a33 | -6.1008 | -41.60787 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 884ec2eb-7675-389f-9740-6ab78386402a | -2.87661 | -51.47456 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec35cb4e-e4de-38a4-bc30-96c2a2fd2c9c | -3.09785 | -49.28031 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6da225d0-bc72-3d7f-8acc-1bc07863d6b7 | -5.58152 | -42.3055 | 2025-11-13 04:12:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ef5dbeec-e1a4-3fe8-80c7-2ceda94b5c02 | -4.71261 | -46.39154 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fc59637-ebf6-322e-ac7d-2af6cee94e22 | -5.57821 | -42.30498 | 2025-11-13 04:12:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ff8e9bd4-0095-339d-8c25-0fd2c9bdeddd | -5.45541 | -40.64399 | 2025-11-13 04:12:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a481211-dcf6-39b4-a7a4-6db146a5ea54 | -3.2065 | -43.47455 | 2025-11-13 04:12:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05265577-4ff0-3b63-858b-7151ced36ead | -2.4535 | -48.81545 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8662dde3-28b5-315e-aacc-f56f9c4c1402 | -3.36908 | -48.41334 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6af189e1-1415-3972-b49a-36fe6436e6bf | -3.08476 | -49.27332 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 27afe9f9-805a-3612-8a20-d335dcaa19cc | -4.24129 | -49.6775 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9f36fd7-198d-3163-9ce6-eb463052d8c2 | -5.41084 | -42.57211 | 2025-11-13 04:12:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 73b74390-4f1a-3715-91d1-0b47799ab6bc | -5.84412 | -38.34894 | 2025-11-13 04:12:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 078a807b-653b-382f-a8e7-f8b43fc9dc5a | -4.95352 | -41.57608 | 2025-11-13 04:12:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a6b64ed-98dc-3634-8553-76c959bf0d11 | -2.94635 | -45.55241 | 2025-11-13 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad0b823-269d-3142-a3f9-9179377495c5 | -2.82504 | -52.87232 | 2025-11-13 04:12:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3db6cc79-77ea-3b34-a469-d1bc6b3a2d71 | -3.27405 | -50.80088 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa0a6798-78c1-3315-95cb-457b6484fdf8 | -3.16402 | -50.62236 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef59c22d-b369-3528-a561-da40ec79e6bf | -6.07773 | -41.56442 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9091afb-f42c-39d0-9330-b9934740a890 | -4.25133 | -46.29309 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bcf9632-55b6-3bf0-b6e3-d1af38dcc5b0 | -5.02383 | -46.83938 | 2025-11-13 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80eef151-f1f0-32f6-b5d3-fe28a5ccd193 | -4.53089 | -46.43125 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4a81efa5-6d63-360d-bd81-a1fa2b82e200 | -4.67714 | -45.80222 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d577236-ca42-30d2-b35d-1c3064e90d60 | -3.78072 | -52.16509 | 2025-11-13 04:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 894356c8-15fb-3e09-80e5-55c47d28197d | -5.02142 | -46.83556 | 2025-11-13 04:12:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3908d46-75e2-3066-8691-8c444226932b | -5.49732 | -39.09949 | 2025-11-13 04:12:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1086a554-ec77-33d6-aa9c-16b2b4d65846 | -3.44098 | -42.54997 | 2025-11-13 04:12:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72eb3b61-cca0-39b6-b026-461cfbea6833 | -3.34091 | -48.38364 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e73697a4-e196-3a7b-9ebe-8140e4bbfed5 | -3.36543 | -48.40856 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b0c70827-ae61-33d3-9640-e2cada3e29e4 | -3.09476 | -49.27003 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ed3b01a-e5bd-32b4-8fdb-0b858677b916 | -3.08399 | -49.2781 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0105ee80-9cae-3a48-b3f4-682ea25e8c98 | -2.46911 | -49.0654 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b475f51-0aa8-3ab9-92fa-384d445abe00 | -4.75182 | -42.78167 | 2025-11-13 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5abd4241-e284-3961-86e9-fd4fa0dc6026 | -4.71504 | -46.44742 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 717c0238-6a85-34c0-a925-c1451abfeec6 | -3.81929 | -45.29709 | 2025-11-13 04:12:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30b28032-559e-300e-a494-de914bc4197d | -4.25354 | -44.59895 | 2025-11-13 04:12:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ff8b42a-d369-3adb-a497-21f4929c8742 | -3.21408 | -50.19638 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64115646-0777-3bd7-8647-dfbfaa8b4a64 | -3.78315 | -42.75203 | 2025-11-13 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 868e7b9b-4ebf-3703-89d1-97cd683f3440 | -3.15392 | -45.49303 | 2025-11-13 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fce205a-c434-3ad4-952c-45751abd5a02 | -4.33447 | -44.00219 | 2025-11-13 04:12:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7542d965-914c-389e-920b-034ca7962445 | -3.37341 | -48.41405 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1698f9a-b821-3596-81b1-cf5b153e664b | -4.86254 | -38.67449 | 2025-11-13 04:12:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 67b255ab-6b2f-3cd2-b4df-bf976ef3ba56 | -4.95004 | -47.03389 | 2025-11-13 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2033db4-7f81-31a3-922a-fc14e6fcbb77 | -2.00551 | -54.45205 | 2025-11-13 04:12:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7723950-3c14-39dd-a377-d9a6451d39aa | -6.0892 | -41.63874 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc61275d-aefa-3424-a81b-45112d1906c7 | -2.45385 | -49.26782 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4e978a0-b1ee-3e0d-a43b-f0e0a44468ee | -2.31462 | -48.45001 | 2025-11-13 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c21ece6-7ab6-3e2d-b504-19c6ad94f156 | -5.09193 | -40.23977 | 2025-11-13 04:12:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| bd662c33-dcdf-3d55-8e4b-619119354d0e | -1.48637 | -47.14253 | 2025-11-13 04:12:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed402a98-3044-3b7f-a7bf-abbefd9357fa | -3.05485 | -40.8118 | 2025-11-13 04:12:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 42e62448-ad0a-32b0-befd-c592976c6f7a | -4.4084 | -42.14985 | 2025-11-13 04:12:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f109216e-803e-3571-93c4-16d67907afb4 | -6.35254 | -39.79288 | 2025-11-13 04:12:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5819edbd-79b2-366e-9167-d11c644b4ec8 | -2.82722 | -52.86998 | 2025-11-13 04:12:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11435ff1-1609-32f6-a807-25297a8e2d30 | -2.72566 | -47.40602 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 638c39fc-caa1-3f5d-8dca-069c3e07cd76 | -2.45153 | -49.26486 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6001b0de-1ebd-327c-84ad-ddf875380e78 | -3.58632 | -46.46109 | 2025-11-13 04:12:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cca1e0f9-d37f-3cdb-b7ab-9fbb8514cf6a | -5.41745 | -42.57314 | 2025-11-13 04:12:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ccabda5-c6b7-3a43-989c-46a0e68b2072 | -5.31047 | -40.92269 | 2025-11-13 04:12:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f8314cd1-d6a5-38b8-a881-38ce832c1d89 | -3.12606 | -46.04212 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 715fed41-2add-39f5-a25f-df46ea210729 | -5.44573 | -44.65491 | 2025-11-13 04:12:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b5ecb69-3642-3274-b36f-271addf10da3 | -0.73257 | -48.56898 | 2025-11-13 04:12:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19f92ef0-e8f9-30c4-8a47-3b77c8e42c28 | -6.37834 | -39.49062 | 2025-11-13 04:12:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 46ee99e6-f250-3560-bca3-8116eb6d2257 | -3.09743 | -49.27789 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 245effed-1017-31e8-9d3b-ad0939e57e44 | -2.86583 | -51.47292 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README14.md)
