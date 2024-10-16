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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3e90e76-d55b-3654-b493-09fb21a1f39f | -2.19229 | -46.73703 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d57c255-88c5-3ada-9e5f-5bcab871c7dc | -2.19175 | -46.74047 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6343aa2-6eaf-3d49-9770-31a701fa3810 | -2.19121 | -46.7439 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b5f6de1-1702-3bed-83b6-cfe5dfbeaf3f | -2.19067 | -46.74733 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27cf168d-f51a-3a4e-9c3c-a557747a404c | -3.58637 | -46.33915 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 357e1f42-467b-36f9-8cd3-3dd336236b4e | -3.31412 | -47.0148 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08b81407-4bb7-3d21-b929-5e9b7c5fc687 | -3.28587 | -47.13002 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34c8a872-0a14-36e0-90da-f4befda74b6c | -3.28321 | -46.51944 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78bdf859-9899-38fe-bff7-3d4c3ed1d5dc | -3.28311 | -47.12607 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1de9bf2e-272f-3730-b834-6c2bda0e2fe6 | -3.25341 | -46.88203 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 146b4fd2-075e-3abc-a351-bf430b982c96 | -3.24296 | -46.88393 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb504a66-38dd-3d44-b718-6b4437223547 | -3.22525 | -46.52111 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64963ed7-3c91-3204-903b-3dd719754433 | -3.08122 | -45.94501 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6164b71-889a-3a47-896f-a32d4087c00f | -3.07732 | -45.94801 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f34fd892-f513-3d4d-9cc0-bda76cda9db3 | -3.07343 | -45.95103 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3532964b-e806-3c0d-ba02-82d120f9ca70 | -3.06619 | -45.95352 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 652ba086-ec31-37a8-abec-63e9ab775f6b | -3.06564 | -45.95703 | 2024-10-16 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90141ac5-fd19-3889-aa0e-2cd4e6189a14 | -3.06285 | -45.953 | 2024-10-16 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57907b4e-ce24-3c3f-b19b-d212c5976171 | -3.06229 | -45.95652 | 2024-10-16 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 574c8b00-b985-3692-b373-ad612de3d1fa | -2.71955 | -45.99779 | 2024-10-16 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ae36f55-f609-35df-b02a-5daf269db4e8 | -2.53661 | -47.22758 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3057e864-5308-31a3-a7b5-d9e473c3e413 | -2.53607 | -47.23102 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4a098e5-4636-371c-90fb-0765b338ff95 | -2.5333 | -47.22707 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1e0e4bfa-32d0-302c-884d-4fd83c8847d2 | -2.53276 | -47.23051 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 98ccf229-2436-3ed8-8e1a-f3370185d6e5 | -2.53054 | -47.22312 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 53c1b9a1-ed55-3ed4-b963-8c635ac5b8ed | -2.5177 | -47.34791 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f81be7d-3b7e-3366-8cb6-80de565ee0f2 | -2.44382 | -46.91033 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c5515bd-f194-32ad-8b12-a2861d352102 | -2.44051 | -46.90982 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c082c0fd-3e3d-3b1e-b101-f5d1b82f8239 | -2.34048 | -46.48552 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67eeadc0-d6f8-303c-908a-0bcd198c4d11 | -2.33865 | -47.25615 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fd3ac36-8bf3-3fd0-8107-b856982cf91a | -2.33717 | -46.485 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 161b47c0-480d-3963-95ef-8aeb41d9032f | -2.33333 | -46.48793 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ab942b4-522e-34c9-a3d2-701dd2ec9649 | -2.32948 | -46.49086 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 847e2960-88e5-3250-a7b2-5e1646a43cf7 | -2.29896 | -46.5989 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dfb3e82-a3ec-3867-b959-3f19130c9cb1 | -2.28502 | -45.88694 | 2024-10-16 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 226049c0-85b0-3cbb-bbfa-4a0e198b7b2c | -2.25486 | -46.75038 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 219db198-45f8-3d17-afbe-04f7636c1bfa | -2.25379 | -46.75724 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 502eb066-07a8-3ff8-80d3-81b600bcb3eb | -2.2488 | -46.74592 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e128544f-452c-3d2e-bd6a-5b4db225a595 | -2.2399 | -46.71641 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f46a13e1-1493-3bd2-9a48-9c0629df0716 | -2.22744 | -46.77424 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 80ad2853-71a0-3a0f-a2e6-57020536ecf9 | -2.20692 | -46.29873 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 319c6183-15ec-39c5-819c-6594d90dfe74 | -3.95923 | -46.43261 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 360a997d-5e9e-3183-8c79-4338df6993c0 | -3.95869 | -46.4361 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| e75bd4b0-d58f-3e6e-9bde-1c3c432edcb4 | -3.95814 | -46.43958 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 698bfe93-df9a-307e-b027-dd5036238f2f | -3.95591 | -46.43211 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9ca2b632-be34-3869-b774-068fac2226a0 | -3.95536 | -46.43562 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d8c37c65-bbba-3488-a3b5-40a3fbb5a862 | -3.95481 | -46.43911 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 2e03cfec-e6d4-33bc-bc36-e59be0a150a2 | -3.95203 | -46.43511 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 3a1672f0-43f7-3e16-bfbd-4c9ebf818d46 | -3.95148 | -46.43861 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 01c16e49-83b2-3f9c-a561-ef9e0e1a11ef | -3.94816 | -46.4381 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2ed3b4a-2574-3523-a962-9f071ffcd3d8 | -3.93591 | -46.40752 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca7670a3-e350-3710-881c-a504b7468dc9 | -3.93536 | -46.41103 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75da076-9bb3-37ce-ba89-bda6cbaa2ed1 | -3.93258 | -46.40701 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 93f22d40-e46f-3c36-9cd7-e74705c93674 | -3.93204 | -46.41052 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b9b5774b-e3c6-32b8-9da9-e7417f6fabf1 | -3.93149 | -46.41403 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ba3c1b74-55b7-33ac-be7b-63b31dd92cd6 | -3.91274 | -46.44691 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9546d8c3-3efa-3186-b7d3-244c34607165 | -3.8703 | -46.45789 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35ebb0cb-98f8-3f82-b2f3-4cc5f40db10e | -3.86866 | -46.46832 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de3862c6-f823-3c16-9a4c-1be4518171d6 | -3.86758 | -46.47523 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34f062cb-38ef-3172-988f-fc3837f28485 | -3.86698 | -46.45737 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 425c55ba-4de9-3402-82b1-e0d5a357e274 | -3.86588 | -46.46435 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46cbfdf3-8157-364d-b237-fb7a1e5dc8b7 | -3.86534 | -46.46782 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 287e7296-1aa2-300f-a816-6950b7c5dd7f | -3.86426 | -46.47473 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad5d5ad1-5299-380f-adfd-da1d916aa5a6 | -3.86372 | -46.47818 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2083b3a1-e215-340e-bcf0-142cb232a30f | -3.86311 | -46.46035 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6258a530-8e93-3758-965d-a19346eb8055 | -3.86256 | -46.46384 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b27bc833-a252-307d-b77b-0a41bc592fcb | -3.8604 | -46.47768 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47fa1167-517e-3bde-9ae6-a935a62cc847 | -3.85979 | -46.45982 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9d4f884-380a-3d04-a2d5-c928a0bd384f | -3.85957 | -46.91721 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dbf66b0-4fb3-3bfa-8193-2b8dcbcfa6be | -3.85924 | -46.46332 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6591b951-13cf-398b-951c-7e5e00183f8a | -3.85788 | -46.90639 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ad2b1e4-7921-36a3-8c3d-77a10eed4069 | -3.85734 | -46.90983 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd0bd58f-d370-3fb3-bc14-99e9eac69c38 | -3.8568 | -46.91327 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 012c51a5-59c1-3349-b1b1-0da7a580ffc6 | -3.85647 | -46.45929 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67ec2dcf-d988-339c-9e65-9fc63f6b7471 | -3.85572 | -46.92015 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a07cee81-b7ac-3610-bac1-02d0bb01b0fe | -3.8518 | -46.90192 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8b4bab6-f9e2-36e9-b78f-498eecba1a00 | -3.84904 | -46.89796 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a63397ba-39be-300b-84fb-d042bbd1adbd | -3.84796 | -46.90485 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76857998-0767-31df-8113-b1f67ac08208 | -3.84742 | -46.9083 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62d1ab6f-1852-3688-b096-6fac5f5944fa | -3.84473 | -46.92549 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 707a0035-4ceb-3b3d-8159-7d7455cb2917 | -3.84142 | -46.92498 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eadf97cc-e126-3e0b-9666-55efba9c69cc | -3.83865 | -46.92104 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 906e708d-416e-3032-b3de-067687b89f25 | -3.83804 | -46.9033 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b8164fe-bde9-3eb3-b550-7f405d02f2c2 | -3.83643 | -46.91365 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e8a6d2f-3b31-34ed-86a8-dce6c0e6a008 | -3.83589 | -46.91708 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d8f6dde-2173-390c-9f5d-f6d1f641ed45 | -3.83544 | -46.46324 | 2024-10-16 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dff7973e-7edf-3d15-9eac-d622a0a2159c | -3.8342 | -46.90623 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4cf5a54-e90b-3803-8cf8-fcc4cf8a72fc | -3.83312 | -46.91313 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 124a2e7f-1151-3bea-97b0-ecd37866d96a | -3.83035 | -46.90916 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c1d487c-d01d-391e-90ed-b2cbd7db94fe | -3.82982 | -46.91261 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dc1a580-8066-3be2-a925-d7341e64bfc2 | -3.56291 | -47.35711 | 2024-10-16 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48ac6cb2-19ee-3b68-b26b-c71ef4a7250d | -3.5596 | -47.35659 | 2024-10-16 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c157f7-7257-37d6-a5d9-4a1c142a5f06 | -5.01017 | -46.48753 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9858230-e4f3-383b-95a5-0199d2a22521 | -5.00962 | -46.49105 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88fa2042-74bb-34f9-a43a-cc5a920ab7d6 | -5.00908 | -46.49457 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c3b4d79-969d-36ce-aa5a-65105548b53f | -5.00295 | -46.49002 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf947885-bb52-3d40-8a3b-d5ad6289f73f | -4.99961 | -46.48952 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c2328f5-2348-35df-b698-542b94ebceab | -4.99628 | -46.48902 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8329979b-1914-3b35-b70e-c1ee043d8a2a | -4.98906 | -46.4915 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb4fc415-c7e7-3261-9d54-a1f1ef886a73 | -4.98572 | -46.491 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README44.md)
