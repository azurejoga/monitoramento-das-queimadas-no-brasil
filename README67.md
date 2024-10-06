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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e87cc538-24f4-3e2c-8bed-4d53232d121f | -8.10917 | -49.52872 | 2024-10-06 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efebc493-ae79-3586-9f1e-bf7f881c39e7 | -2.20981 | -48.84173 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a20b7366-6c77-3ca1-9222-2e731f3a1e01 | -2.204 | -48.85188 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eaa8c2e2-9171-3d43-ba31-c718c9bdcd9d | -2.19643 | -48.92497 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e686aaab-7e82-32a6-a134-3e823b07109a | -2.14157 | -48.90481 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d29215b8-943e-38c5-82a8-4ef045032f6e | -2.13748 | -48.90416 | 2024-10-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f885acca-3119-33b4-bd1f-3eaacf9bbef6 | -1.42279 | -49.3764 | 2024-10-06 04:17:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee477093-3c8e-3796-ab8d-21dc2c59331b | -1.42182 | -49.37555 | 2024-10-06 04:17:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b481a1c0-8813-35ce-a213-c60b75136f63 | -1.42117 | -49.37955 | 2024-10-06 04:17:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c0f0c14-593c-3a7c-9f93-6e737a3f1168 | -1.04424 | -48.70321 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd8c500d-4641-3db0-b7c1-73915c0139ec | -1.04366 | -48.70686 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 049869e2-4b9d-3539-9ca4-2122f86f2912 | -1.04308 | -48.71049 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c9613cb-f774-3334-b0d4-d284c11f5c55 | -1.04072 | -48.69889 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ca62c48-4fc8-3309-80a8-c5499dde207c | -1.04014 | -48.70253 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba815f1e-3397-3aa6-a2a1-0c3352e9c691 | -1.03956 | -48.70617 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b5a61c9-f9f3-3113-a43c-911feba67b8d | -1.03662 | -48.69824 | 2024-10-06 04:17:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70301893-09c5-3e36-93eb-8e9e018cd242 | -4.86956 | -50.76797 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32f67607-30f2-3282-b980-68d263ca1b09 | -4.86885 | -50.77228 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 745df569-4dc4-3ee8-95bd-3f8ff7154cd4 | -4.86512 | -50.76718 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d98948dd-154f-3c2a-aa10-caba689e33af | -4.86442 | -50.77149 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9047e501-3d26-3715-aac7-3c25e86bb953 | -4.94467 | -49.64202 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5cd9f01a-a07b-3374-9735-3ad95a96feea | -4.66215 | -49.52832 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 01ede123-2315-305c-9f0e-dcd72acb55b5 | -4.66153 | -49.53201 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1e891fa-6f30-3cb2-8864-d99a04d30f54 | -5.10662 | -49.82175 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddbd1103-3b7b-3149-a53a-eae5cf2a5215 | -5.0149 | -49.77151 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b4805c5a-d222-314b-ad07-7d57ee57320e | -5.01429 | -49.77524 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5f514276-67c9-375c-979d-ea5a188f87e8 | -5.01368 | -49.77897 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc944dee-3242-3331-846b-ab11bcc20865 | -5.01305 | -49.78279 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d792a01-4d13-36a6-96d3-dc9cec5acf2d | -5.01076 | -49.77082 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ee00cd7d-997f-319a-9ff1-b08e77f0c21d | -5.01015 | -49.77455 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| e31ccac7-f01f-35e5-862b-39ab39db3b76 | -4.9691 | -50.46655 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b52e72b3-aff7-3137-b654-ffc1493f7c36 | -4.96477 | -50.46577 | 2024-10-06 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0445e9c8-b9fa-3466-a7cd-a6aab10d2f1d | -4.86788 | -49.95553 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 611a8cdf-e08a-3de9-8258-3937baaddbfe | -4.86368 | -49.9548 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f78bc6e-8a83-3774-bfff-822544caf0a6 | -4.86305 | -49.95865 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a4182c-5e50-3072-8374-169c2521bb2c | -4.82874 | -49.95702 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43093741-48e9-377e-8b6d-ae5aefc72685 | -5.25955 | -50.88935 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da371a05-2d21-3667-8603-7478f8bf86e4 | -5.3387 | -49.52629 | 2024-10-06 04:17:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 283d3dd3-d205-317b-819d-57215c8ec62a | -6.06949 | -49.7989 | 2024-10-06 04:17:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbac5e73-e83d-34b5-9eb4-1e932d1d11bb | -7.81676 | -50.23119 | 2024-10-06 04:17:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9827bbb-c62e-300a-8dee-3a4e8607ba0a | -8.23436 | -51.00745 | 2024-10-06 04:17:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ea3b6a2-de5d-3965-a4f7-1504ffa1804d | -8.23016 | -51.00629 | 2024-10-06 04:17:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 073d8f54-9e23-350d-a028-45a8905eb555 | -8.22594 | -51.00525 | 2024-10-06 04:17:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 612d8337-54ed-315a-b76a-913bd4ac98ef | -4.66949 | -50.98954 | 2024-10-06 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4680326-9cef-3a90-9a1f-9fa1bffc0d1c | -4.66872 | -50.99416 | 2024-10-06 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83a31989-a12b-3a60-9275-8cce4fa620d3 | -4.66496 | -50.98878 | 2024-10-06 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54e07220-3049-318c-a42b-ecd20e439316 | -4.66419 | -50.9934 | 2024-10-06 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff7f941-0885-3de2-9cb8-d0f417411b4e | -4.66044 | -50.98802 | 2024-10-06 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75859a45-c25c-3acd-9471-ff9ec559bde0 | -5.6041 | -51.55413 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3178f11c-06f5-3893-a1a4-44f82cce980e | -4.16047 | -53.62624 | 2024-10-06 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6159ab0e-4b7e-3386-891c-b190b9e6dc4d | -6.22548 | -53.33009 | 2024-10-06 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94d0848e-bee9-353c-9cbc-f25cd5625ec3 | -6.22493 | -53.33327 | 2024-10-06 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af02c78d-ea1c-3414-a791-c3f28bcb1a5d | -6.21616 | -53.29201 | 2024-10-06 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd438a03-30e4-3b7a-bf20-679fee31dabf | -6.0738 | -53.36544 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d74ff5b4-9f09-3235-8e77-c0a6c83407db | -6.07326 | -53.3685 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af651fae-1c80-3b16-8edd-eaef21d95260 | -10.96709 | -54.02237 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 761d5078-276d-3ffc-acde-75a70a86d582 | -10.96654 | -54.02534 | 2024-10-06 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e6b3b2-46c7-3a2d-a85f-00442d9ed286 | -3.06632 | -54.77967 | 2024-10-06 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15caa8b4-bde1-354e-832b-09720a9fb11f | -2.80763 | -54.58935 | 2024-10-06 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d998e83a-e43d-3ad7-9db1-45554297f4da | -7.97986 | -54.76809 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1578b8e5-9dd5-3181-91ac-6069beeebfbc | -7.97931 | -54.7673 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6a37b4c-8eab-3142-a42a-e5714fc4fe3f | -7.97862 | -54.77101 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dc6435e-3b8f-30f9-a344-04a289bcf30e | -7.97857 | -54.77541 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77fbf130-76cd-3485-9325-db2395386a99 | -7.97795 | -54.77463 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b78d09ff-a047-328d-b764-6962fede3800 | -7.97662 | -54.78181 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf48b775-5c71-30ee-95c3-c21cef11133b | -7.9763 | -54.75603 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e81b53b6-be32-38d5-a40c-72cd02f2b7d8 | -7.97582 | -54.7553 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b8afdda-02ea-3aab-9587-311fcb23f0ae | -7.97565 | -54.7597 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 932ea9fd-bc5f-3c30-9d57-3c5c354522c8 | -7.97514 | -54.75896 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ccc489-40c2-3581-b1a7-36e359959d6b | -7.97499 | -54.76339 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e60eff56-af3f-395a-a8b7-b93e61851951 | -7.97446 | -54.76264 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5470cd98-561f-3488-bf11-6973b56df01b | -7.97434 | -54.76706 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3efb14b9-9b1c-347c-9eb6-4e1e3e606f11 | -7.97378 | -54.7663 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee58b017-0fa9-3a8e-9bdb-36cecc5f08d7 | -7.97369 | -54.77072 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 373dc912-c796-373f-8cc1-c0f50dd06bc0 | -7.97311 | -54.76994 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc22cfa5-71fa-34d9-8fbb-22c5072c31c3 | -7.97305 | -54.77436 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45e81210-a36e-3544-9212-4a3cf6e1b814 | -7.97243 | -54.77357 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caafcabf-eaf5-3621-9109-5a9e8071b5d3 | -7.9724 | -54.77801 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b20b7ea-bab0-3812-85f2-aa6794631a26 | -7.97176 | -54.77723 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd8e8d10-ac50-3bfc-85a8-422acdb00608 | -7.97144 | -54.75133 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 972eaa63-8a03-37e7-ab17-b0bdd1700e1e | -7.97098 | -54.75062 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f0b9720-abda-37bf-a452-43463fc541f9 | -7.97078 | -54.755 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 656704f6-4e15-3d44-a061-84f3c3d039ed | -7.9703 | -54.75428 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bdd1005-5d6b-3a56-84d9-3a554c1302a1 | -7.97012 | -54.75873 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fad39bb-a646-3ec2-9ee5-f384024af5de | -7.96962 | -54.75798 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d508051-0426-31d4-8c74-c2a6dc3df113 | -7.96946 | -54.76243 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af78cb65-37dd-3c91-81b9-f06c77addd05 | -7.96893 | -54.76168 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45e572e9-4fcb-39bd-ae73-63795e7073aa | -7.96881 | -54.76606 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44448402-21bc-3bdd-916c-70f48bc0f495 | -7.96826 | -54.76532 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b226086-8423-344d-8e4e-127beea4d276 | -7.96817 | -54.76968 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adc85ccb-2ad7-3683-8c0c-22353e2e9afa | -7.96758 | -54.76894 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b26d130-ade4-3280-9659-538cc9ab70bf | -7.96752 | -54.77333 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a675e531-99c4-31b0-9f8a-27f84bf8f5af | -7.96691 | -54.77257 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 364a2bff-d354-3cf9-bfad-be37f5deed31 | -7.96687 | -54.77699 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32457644-8661-3f71-bc70-a2bf67ad8658 | -7.96623 | -54.77621 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad01c739-a994-37cb-ac94-03f54485c1d2 | -7.96394 | -54.76138 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53cc429-6f74-3b3d-84e1-0bc9f5389529 | -7.96341 | -54.76065 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbde881f-aa52-3ded-8a36-2b9bfb8b3819 | -7.96329 | -54.76503 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2ccdcd5-1aee-33e5-80fc-3a9fbe2aa490 | -7.96274 | -54.7643 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 280f36c7-5199-37f7-bda9-fe41cdd3343c | -7.96264 | -54.76869 | 2024-10-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README68.md)
