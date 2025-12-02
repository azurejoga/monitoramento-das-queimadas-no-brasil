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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd7f8082-9c03-3648-b274-977348313e53 | -17.5335 | -57.2107 | 2025-12-02 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| 48756df8-3938-31cf-8bbf-a3a588a4254a | -17.5138 | -57.2131 | 2025-12-02 02:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| afae661c-077d-3bdd-b8ec-89411420276f | -8.0516 | -43.0765 | 2025-12-02 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 982911cc-4783-30c9-b225-898c993f6b6f | -12.5213 | -56.9022 | 2025-12-02 02:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 29bfb355-52af-3332-96d4-f8f11b92da09 | -1.4923 | -45.7903 | 2025-12-02 02:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 47f233a4-d2d6-3605-bc46-3ab8e2674e84 | -8.0516 | -43.0765 | 2025-12-02 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 937950f1-c8a3-30ac-8307-4a51c863cad3 | -19.7873 | -56.6851 | 2025-12-02 02:20:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 5d06694a-6c7b-38fe-a288-9d4f18dec669 | -3.5481 | -50.5267 | 2025-12-02 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0bdf471e-0de5-3d62-b76e-007001ed85ec | -17.5338 | -57.1901 | 2025-12-02 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 8aa08c53-3df5-3d30-bb9a-1e9c2a97c832 | -19.7672 | -56.688 | 2025-12-02 02:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 8ec6637a-1c1a-3e86-814c-085d2dbfeef9 | -8.051 | -43.1237 | 2025-12-02 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 06ab15e4-a235-3fdf-9efc-610712cc4406 | -8.0703 | -43.0981 | 2025-12-02 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| a914343a-9e97-3151-a005-413769aa6189 | -17.5335 | -57.2107 | 2025-12-02 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 182.6 |
| ab5a21a0-01ee-346d-8904-5c86229eac17 | -19.7668 | -56.709 | 2025-12-02 02:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 9fd08e48-4062-3a37-a5d9-d3859d6c9f0f | -8.0513 | -43.1001 | 2025-12-02 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 228.1 |
| a971da9a-0334-3066-829e-c64e768509ee | -4.389 | -43.1497 | 2025-12-02 02:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d980310f-dad8-3313-805b-9eafbfb86bb6 | -17.5138 | -57.2131 | 2025-12-02 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| a68ef71b-d735-3471-9082-69075704dd09 | -17.5141 | -57.1925 | 2025-12-02 02:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| d8629d51-3f82-3373-9388-7184d9533481 | -11.1379 | -53.9429 | 2025-12-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 0ce1a99a-aeb8-3f8f-a8c4-b9d4eb9d6446 | -4.3703 | -43.1508 | 2025-12-02 02:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a578ba77-f264-3728-bd8f-a73dbdae6894 | -12.5211 | -56.9222 | 2025-12-02 02:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ad11c024-d5a8-3c43-89ce-4d8dc871938d | -11.1382 | -53.9223 | 2025-12-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 514ee922-2ea4-342c-9d06-3adbfd9e9d05 | -8.0324 | -43.1022 | 2025-12-02 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| 159c05c8-ad9c-3418-b2ab-c4ef2ce7c6ac | -8.0706 | -43.0745 | 2025-12-02 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| deaf434e-80b0-33b5-b859-f88c6ff80761 | -14.0755 | -56.1683 | 2025-12-02 02:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| ff4501d8-135b-39b0-8f3a-b4dcee8786b6 | -1.4737 | -45.7907 | 2025-12-02 02:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cd0d3d77-91d2-3048-839f-f24d8b0a775d | -11.119 | -53.9446 | 2025-12-02 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 79d23668-10c0-3d7d-bbd3-6ee032187a5c | -14.0755 | -56.1683 | 2025-12-02 02:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 31a1783d-ff1c-3939-9812-29365c8cde0c | -19.7873 | -56.6851 | 2025-12-02 02:30:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 101.7 |
| cd36a3f7-fea7-32ae-9cf9-8066f7a7f565 | -11.1379 | -53.9429 | 2025-12-02 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5d80aa70-8252-31be-aa97-79ee469d4b5e | -11.1382 | -53.9223 | 2025-12-02 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d0b53d70-5ca3-3e92-96f7-d3449698704a | -1.4923 | -45.7903 | 2025-12-02 02:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3a7fb4bf-48b8-39d8-9b70-6c8bd505bd42 | -8.0706 | -43.0745 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| a72ef111-ffbe-325a-bd71-d3c25843e903 | -1.4737 | -45.7907 | 2025-12-02 02:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 60023cad-d542-35ed-993e-1ed55ea574b3 | -8.051 | -43.1237 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 0a6da079-bb75-37fe-97e0-1fc708818c18 | -8.0513 | -43.1001 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 192.0 |
| 0147a485-2019-3203-9147-cfcb1b263b5c | -8.0703 | -43.0981 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 9a16ab3a-1166-3275-8c3e-6c64430b6fd0 | -19.7672 | -56.688 | 2025-12-02 02:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| 8f4c56e1-ecfa-38f8-8fcc-f48ce517dcb5 | -8.0516 | -43.0765 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| a355bdf8-0752-3048-900a-e8df0a2339ba | -12.5213 | -56.9022 | 2025-12-02 02:30:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d1fb6385-3ed6-3c77-b9a7-af20b8005c78 | -19.7869 | -56.7062 | 2025-12-02 02:30:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 2fe80e0e-6df7-382f-b003-748d82aacbe2 | -8.0324 | -43.1022 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| d61ebee0-d86c-365e-bd0b-3c073c37fff2 | -19.7668 | -56.709 | 2025-12-02 02:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.1 |
| ac7b007d-f8f8-3bef-9ab6-bbc1991e2f63 | -8.1633 | -43.2055 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 4a99c929-a611-377a-be46-6371c431b364 | -8.163 | -43.229 | 2025-12-02 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| be074f1c-1dd5-32a5-b785-2e70e8a792f4 | -17.5335 | -57.2107 | 2025-12-02 02:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 07498016-4561-37a2-9937-2cc850f93624 | -19.7877 | -56.6641 | 2025-12-02 02:40:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 3edd2d73-07f9-39a8-a5f5-b081f67c2792 | -19.7869 | -56.7062 | 2025-12-02 02:40:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 8fef22bf-e7dc-326d-832a-66fede88f403 | -11.119 | -53.9446 | 2025-12-02 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 9894e684-1522-31b0-85b8-e1b21075f9c1 | -17.5335 | -57.2107 | 2025-12-02 02:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 65c767c7-2fbe-3d6b-b50d-559513f14c45 | -19.7873 | -56.6851 | 2025-12-02 02:40:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 129.9 |
| a0ee4976-977f-3c8c-8523-904835718043 | -11.1379 | -53.9429 | 2025-12-02 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e75be9ba-e5bd-3e6c-897c-e1d229b20be2 | -1.4737 | -45.7907 | 2025-12-02 02:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 150c429d-f949-3f9c-840f-c1f8f9c8bb34 | -1.4923 | -45.7903 | 2025-12-02 02:40:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 4fcfa398-7cf0-305c-86ba-486b66b7d987 | -19.7668 | -56.709 | 2025-12-02 02:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| ddf9e414-95e0-3b76-aef9-9c7fc1831d4c | -19.7672 | -56.688 | 2025-12-02 02:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.5 |
| fb51d186-c70e-3d48-bebb-79c133782ecc | -8.0516 | -43.0765 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| e58c9d50-c774-3ce1-bc47-1f1e8f0cdf64 | -19.7873 | -56.6851 | 2025-12-02 02:50:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 182.5 |
| e2113277-43b0-328c-836b-49820e5a1e15 | -19.7672 | -56.688 | 2025-12-02 02:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 143.4 |
| c7396a33-2303-3a7f-aba5-19101ad07bae | -8.0324 | -43.1022 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| f9e3fb71-df2f-3103-9bf5-a31dbaff54a5 | -8.1633 | -43.2055 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.9 |
| 231bd7f9-e882-35ca-8e62-bfed744845ee | -8.051 | -43.1237 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| fe2a8710-8d4f-3350-85dc-0959859b3423 | -19.7668 | -56.709 | 2025-12-02 02:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| edc14f87-01d0-3b31-a04b-8565040be0ff | -1.4923 | -45.7903 | 2025-12-02 02:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 2975a41f-c18a-3a14-bfaa-3c4205878841 | -11.1382 | -53.9223 | 2025-12-02 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3c89fafa-d6e0-3d17-b997-3a9be7db17ba | -8.163 | -43.229 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 493837db-5da6-3e35-bf36-a3ec530506f3 | -8.0513 | -43.1001 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 265.2 |
| b27def9e-c208-3ea1-a250-52b8e1f0ee36 | -1.4737 | -45.7907 | 2025-12-02 02:50:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e4bd441d-32c0-39b6-9fd9-fb8457f8c5b4 | -19.7869 | -56.7062 | 2025-12-02 02:50:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 8162c4e5-14a1-31b2-9517-ef44bda52981 | -17.5335 | -57.2107 | 2025-12-02 02:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.9 |
| a906109d-f3b2-3427-ac9d-a9eb3f470ae7 | -8.0703 | -43.0981 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| c0f692af-a745-3464-97ac-605f1207cae5 | -8.0706 | -43.0745 | 2025-12-02 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| 27d9a778-5d3a-3ad6-ade1-684141a9d112 | -11.1379 | -53.9429 | 2025-12-02 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 780552d7-e0c4-3f61-9def-0c0b2e6fb0fb | -19.7668 | -56.709 | 2025-12-02 03:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 7b311b5c-9c5a-3af0-95e7-d7bee407c7c4 | -11.1379 | -53.9429 | 2025-12-02 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 65f21217-bb16-3a1b-9262-1faaa549fddf | -1.4923 | -45.7903 | 2025-12-02 03:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 17eba491-d3f1-33fd-83b4-cd791325e2bd | -8.1633 | -43.2055 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 5124771d-ad0e-3350-919f-7e7320b91c7e | -8.163 | -43.229 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 8f8099b1-7548-3038-aed0-4abb41087a1d | -11.119 | -53.9446 | 2025-12-02 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6edacb37-7c42-3e25-89bb-5abe3b59ea3d | -1.4737 | -45.7907 | 2025-12-02 03:00:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 975c9bb1-4b81-367c-95e5-f0d218337fea | -17.5335 | -57.2107 | 2025-12-02 03:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 3e461bcf-3c19-3226-98b5-4b7feb3e9e81 | -19.7873 | -56.6851 | 2025-12-02 03:00:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| 2202f976-f375-323a-aac0-6ce52f57fd74 | -8.0703 | -43.0981 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| c77068e3-c33c-3a29-9b28-2a44a7db14d4 | -19.7672 | -56.688 | 2025-12-02 03:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |
| 7e6db689-35ec-35f0-af80-d0f330d7c188 | -8.0513 | -43.1001 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 394.2 |
| 041ee437-2472-32b0-82b1-59b6516a860f | -8.051 | -43.1237 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.3 |
| 4fe95ca3-34b5-355a-bee3-c6cd6976f09b | -4.3918 | -45.4854 | 2025-12-02 03:00:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1fee5c12-a9e7-35ac-bf91-00e9999ef785 | -8.0324 | -43.1022 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| f14b8a3d-234a-3d92-a62c-f0be76b86ab5 | -8.0516 | -43.0765 | 2025-12-02 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 0a541978-f1ea-32f3-b38f-6670ec4f65a8 | -11.1379 | -53.9429 | 2025-12-02 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 89d45720-8ed6-3c64-8fb0-c4dd75de469b | -8.163 | -43.229 | 2025-12-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| adaa087e-91d9-37d1-9be5-87b6091dc98e | -8.1633 | -43.2055 | 2025-12-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 5debc43f-a4e8-33d6-a9c0-56e4a9b3bed1 | -8.0513 | -43.1001 | 2025-12-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 202.3 |
| e40bef3a-00e5-3fc9-8334-c0a0ead778ce | -19.7672 | -56.688 | 2025-12-02 03:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 8217e98e-1c1e-366a-be80-06f0d0742839 | -11.1382 | -53.9223 | 2025-12-02 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9f13efa5-5621-3af9-b48b-0e9bbd6db4ba | -8.0516 | -43.0765 | 2025-12-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 735781b6-a6bd-33f2-8646-4f845cfc105e | -19.7869 | -56.7062 | 2025-12-02 03:10:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| a500ad52-9dfa-3ccb-94fb-72589458f128 | -19.7873 | -56.6851 | 2025-12-02 03:10:00 | GOES-19 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 512b00e5-26d8-374a-8560-3c654a73d96b | -1.4737 | -45.7907 | 2025-12-02 03:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4835229e-35a8-32a8-8055-ba884158ef32 | -8.051 | -43.1237 | 2025-12-02 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |


[Clique aqui para ver as próximas entradas](README6.md)
