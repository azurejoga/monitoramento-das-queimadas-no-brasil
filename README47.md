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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4197bed2-e602-31d6-bdcd-c0c044e0d3db | -0.10389 | -51.49789 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 97ae9630-1f68-3345-9f9a-c71a38052246 | -3.88927 | -46.09036 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c4a2d3d3-e0d1-3208-b81a-9d0055813819 | -2.64238 | -46.17546 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fff2221-4824-322c-9212-2a6355600227 | -2.12632 | -50.69434 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f4d2cd0f-752c-3d61-88f4-c5fb913cad61 | -1.35926 | -52.34519 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c857f306-67a4-306e-9220-4ef093d64547 | -2.98314 | -45.86644 | 2024-11-14 05:01:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 100a62db-6ca7-301f-b8a8-612db746d2fb | -1.63861 | -53.27243 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d80e13e7-73a9-3b12-a407-72a4739af648 | -3.46531 | -50.30753 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a21902d8-b6d9-347e-bb68-6b689e19f043 | -2.54209 | -47.12165 | 2024-11-14 05:01:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6141e684-f7a0-3a85-b00f-6420b1ef07af | -1.23147 | -52.52905 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f766c681-0499-3913-b4bf-5057559bd7e7 | -0.90546 | -51.7245 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d41a5e2f-45e6-3ef5-a289-d554e35a7dc6 | -0.9073 | -52.41972 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36059b3e-df92-3d37-a217-b0f1edc2b140 | -1.85601 | -47.8253 | 2024-11-14 05:01:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64d031cb-4f48-3618-8632-28c0aea0e536 | -1.66927 | -52.56406 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d4dc0e7-286d-3d42-a520-651f55765f9b | -1.1742 | -53.74468 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca736cd9-fa9a-33b3-b7a3-15d05d45ecb6 | -4.59078 | -47.06143 | 2024-11-14 05:01:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013fa56a-26f1-328b-bda0-3dd0737b276f | -1.08173 | -53.64513 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d9e70c3-e7d0-3203-9119-c8663a5180a0 | -2.37714 | -48.53157 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26c3a372-f1b3-3599-b563-10e7cc9728ae | -2.69665 | -51.79553 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 220418e2-c205-3736-b905-a8f198ef506f | -1.38116 | -51.5579 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52e18962-9e54-37fd-b753-79a3100135b3 | -2.37813 | -48.52148 | 2024-11-14 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3236bb9e-f37e-34c7-ad58-5ce445b1fcf5 | -2.64192 | -46.17859 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d672c544-8e02-350c-83aa-c3f9848b6d21 | -1.26304 | -52.13209 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e3bdcb3-850f-3d11-ba79-42a93b354fc8 | -0.89753 | -51.75165 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 884c05f7-375d-3eab-be16-3a9a206b234c | -1.95369 | -53.33176 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76074df4-6ab3-39a8-b5c6-dd61090988a6 | -3.16298 | -50.45594 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2170397-d5d6-30ed-882a-ecb547b38397 | -3.63757 | -50.59147 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c9e2f697-07e4-375b-9174-040dacc4e795 | -1.54573 | -52.05803 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| be3759e2-0725-328b-b064-df6ffb04d937 | -1.99505 | -52.08821 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b381174-05dd-334b-87cf-cebb0ac45811 | -3.40644 | -50.30702 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f097fb56-c71e-397d-b1c1-f96001eec5e5 | -2.11801 | -50.69777 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87b9726e-3ef4-3e71-95fb-eff7f5b3e0cf | -1.20822 | -51.772 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca06129-2036-3b84-8174-606c30e8d577 | -3.88976 | -46.08708 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c74d7efc-b2fb-3408-bff0-ab606fb1be36 | -4.51612 | -46.47631 | 2024-11-14 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 240f0d73-5dc5-3bcb-88bf-e5dcb920d067 | -1.97182 | -53.12873 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58a4804b-92f4-394c-9c89-f313b82c0c11 | -0.1657 | -51.7481 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd1d88c9-0915-3859-98e1-802f0c703d60 | 1.07389 | -59.23555 | 2024-11-14 05:01:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23c75e90-97c9-3105-8523-daf157eb9464 | -3.47005 | -50.30302 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd0c8677-837c-3b70-9786-39b1b3992605 | -1.47355 | -52.2608 | 2024-11-14 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04b64591-f405-3376-8026-0cb7b787327b | -0.89775 | -51.72736 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd746a04-5d0a-3086-9703-9423a78b4b81 | -1.24984 | -51.77795 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc90628-ccb3-383f-957f-b851d0c236f5 | -1.55492 | -51.85817 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f4b8d1f-fe3b-3312-9cd9-260950feb5ac | -4.27786 | -46.90318 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70ad43a8-6766-382d-bb0b-531a44a584b6 | -2.1059 | -50.8499 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3e937d4-bf0d-3a5c-9a0b-17908146c301 | -4.02486 | -46.54659 | 2024-11-14 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f657cabd-3ebd-318b-8aeb-d7a3d206a357 | -1.62148 | -52.51511 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce2de15c-b34c-3761-b769-07d1195db0e5 | -2.35373 | -51.98251 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e92ca22-2dfa-341e-95e6-80c24aefdef6 | -1.84888 | -53.69215 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a4e2daa9-6b60-37bb-873d-2936fc161da5 | -4.51578 | -46.47637 | 2024-11-14 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bad93c71-3e51-3f22-b486-07d44de339a6 | -1.61195 | -52.23412 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6d71c8f-2f77-38c9-8a93-4717a209a28e | -2.64227 | -46.16872 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b93a93c4-97e2-32bf-a222-418a8ac4e4f1 | -3.7362 | -50.44131 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cda450e9-5c75-3cac-8797-4a3493014c76 | -2.73021 | -51.74594 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4a4470b-c138-3488-b5d3-f69640aebaf0 | -1.39609 | -51.12119 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d76abf7-0ebf-3be7-8403-8fc93b07e2d6 | -3.86821 | -43.93572 | 2024-11-14 05:01:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49bfc006-6559-374a-bfcf-041278238067 | -1.39909 | -51.12605 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c53fded-913e-3273-82c6-83434d3372c4 | -1.94838 | -52.1569 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 338d8eca-7cb9-326b-af72-abf9df6978f1 | 0.31833 | -50.97499 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f9b41fc-457d-366b-b5c7-0e8e16de2ba4 | -2.4802 | -49.11228 | 2024-11-14 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 871d69c6-0051-33eb-ac04-1913d6dd879e | -2.64284 | -46.17234 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fedb741c-07ff-339d-b47f-61fc2cc85686 | -3.49239 | -50.83763 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c697b357-218b-32c3-81b1-821da68adb87 | -1.94898 | -52.15301 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a04b17d-e00f-3c63-85d3-c4c48e98d466 | -4.77222 | -45.73368 | 2024-11-14 05:01:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bcadd00-8cad-36ce-b151-b41a6fe250a1 | -4.42977 | -49.68608 | 2024-11-14 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9b84597-3785-31eb-9315-8d66d4b612c3 | -4.03261 | -44.67959 | 2024-11-14 05:01:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02fff573-5f78-33cc-8587-1fb17c616319 | -2.84092 | -56.78766 | 2024-11-14 05:01:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c7f7972d-808f-3b4b-abb1-ef37af5a6f37 | -3.94328 | -48.99145 | 2024-11-14 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bfb9491-825d-3930-b55e-87a7c5e2b974 | -1.41646 | -51.11118 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d313371-d65e-39c1-95a8-e7d50845fc81 | -2.89738 | -46.86104 | 2024-11-14 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6de7ac7-963f-37f9-881f-470765adb7b9 | -2.15404 | -50.91505 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca00fa14-2e5a-3ed3-8608-5b28a7d93ac9 | -1.68336 | -48.4642 | 2024-11-14 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce1b75c0-8cc4-3c61-bd8d-6ca166e4ccdd | -1.222 | -51.75377 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50c56601-3719-3ebe-ba06-b75177e86f1e | -1.98086 | -53.13752 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f5f7678-2a09-3716-b982-559311957dfa | -1.39141 | -51.10289 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e51202e4-46db-3980-8e30-490999810b1e | -3.17545 | -50.45275 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d52bea67-4a49-3339-9e06-8478530a9cd3 | -3.22313 | -50.58478 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee0d108c-e6ce-3268-b0f8-f4ccf502d4e6 | -1.21135 | -51.75212 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7b3affb-610b-307b-bda1-5f1822237d0f | -1.39008 | -51.11147 | 2024-11-14 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0189d5cf-27af-3b57-97d1-3d86d10d7227 | -0.90066 | -51.73188 | 2024-11-14 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c993af4-3774-349d-a027-10ffe0375cc4 | -5.19825 | -44.35915 | 2024-11-14 05:01:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1de0b265-0d48-3699-bce3-0d3e966c00c8 | -4.03127 | -44.67728 | 2024-11-14 05:01:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee8d5d57-d87e-3655-b18c-1a6751839a09 | -2.27389 | -51.3204 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62d1e331-c7d2-31ee-bd21-dc768194b4fe | -0.13917 | -51.4584 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2438aa2-3a48-3748-8b76-b2debea4bb0f | -3.89312 | -50.08341 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84829743-43ae-3294-982b-7957569e8825 | -3.04152 | -50.56784 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 540cbee7-eedb-38ea-9898-98e11b7de5e5 | -1.25298 | -51.62726 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 495944a4-a9b5-3b93-be2e-b382a66f7a9a | -2.63626 | -46.18097 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75b7a7a0-9a2b-340c-b7ad-7ece0dbe0cfa | -2.16578 | -50.66009 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34f28e2-1e09-31ee-98aa-d23337560ab2 | -3.70586 | -50.43476 | 2024-11-14 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3aecf1a-ade9-3be7-9290-1cc984b9adcb | -2.64146 | -46.18172 | 2024-11-14 05:01:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75d86676-4652-36d5-b9a3-1714d9f6dda4 | -2.20976 | -53.74775 | 2024-11-14 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6166755a-2a94-3529-b107-01207a70f4cb | -3.20428 | -44.43009 | 2024-11-14 05:01:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77acf3af-c9d4-3434-a110-1db51668073f | -4.15375 | -46.25175 | 2024-11-14 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83a15971-38f8-3e2a-85bc-dd0050707d54 | -2.31168 | -50.68991 | 2024-11-14 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb20b379-5e49-33c9-9cf8-c955476ea851 | -1.3349 | -51.85894 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2894f8c1-2264-38f4-b550-db03543f2a21 | -1.67042 | -52.55658 | 2024-11-14 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea26445c-afcf-30f0-9448-996cac953f58 | -0.20777 | -51.5002 | 2024-11-14 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5deb825c-94f3-32c5-a3f9-867a63bd376b | 0.32855 | -50.96913 | 2024-11-14 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8bd7ed6-7b0e-3f10-84cc-986dcc1edf2d | -2.89881 | -53.05238 | 2024-11-14 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d250a80e-3b67-36e3-bdb8-5eb789deca4e | -1.57229 | -52.02618 | 2024-11-14 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README48.md)
