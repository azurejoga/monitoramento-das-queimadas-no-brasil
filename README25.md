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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 590762f6-e7dc-3ab0-add7-e297305aeb80 | -7.0615 | -59.406101 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5de05d37-6784-39fb-97cd-7218d1a39c8d | -7.039 | -59.350201 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a93e8e0e-e69c-344f-b766-62f5c1c02c0e | -7.0462 | -59.383301 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7b4b2a1d-efb9-3f9a-9d50-d85777064149 | -7.048 | -59.391602 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02f0fbb1-8413-3528-9191-4d44b5829e8d | -7.0499 | -59.399899 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12494a8d-4001-3c2f-bfd2-f19b112fb503 | -7.0517 | -59.408199 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19a2b5a2-f16e-3ef3-adf0-41b81b9d2ffe | -6.1635 | -55.462898 | 2024-10-10 01:06:46 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f045ebab-bd9b-340f-9e4e-0222c440314b | -6.1651 | -55.469799 | 2024-10-10 01:06:46 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 350cf078-617e-30b6-aa58-3b7ff53d4019 | -7.0274 | -59.344002 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15f30562-9c42-3135-9906-6f13aebdd515 | -7.0292 | -59.352299 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98140c41-1dd6-379f-b5ec-03b2edde3c34 | -7.031 | -59.3605 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c32fe33-2e64-3277-8a5e-0e88c5c7bba7 | -7.0364 | -59.385399 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7abb10b2-d709-38c9-b444-2a4bfe240b23 | -7.0382 | -59.3937 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c94e42b-1104-3bdc-a0fb-5785d395015e | -7.0401 | -59.402 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e9506931-350c-32d5-8799-099402e72bee | -7.0419 | -59.410301 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d24192eb-998b-3f5c-b2cf-eef7c3b9a312 | -7.0437 | -59.418701 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 104f821a-f702-3afe-93b1-ecf546ebd856 | -7.0205 | -59.4062 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b54fa357-f1ef-3c4b-b3b1-320fc7dcf0dd | -7.0168 | -59.389599 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dafd6998-f7e8-387f-b4c8-b1844e32e8a9 | -3.7935 | -45.469299 | 2024-10-10 01:06:47 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| baa6c275-425e-37de-9a3c-7eea9961f95f | -3.8005 | -45.498199 | 2024-10-10 01:06:47 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 350dfa75-0a52-3e58-a765-810ae109fe45 | -7.0248 | -59.3792 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dcdbc6f-36b4-3b25-92eb-b8e288ca681b | -7.0284 | -59.395802 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4da2d4cb-fb2c-300d-9409-de9aa604433d | -7.0303 | -59.404099 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6169736a-d97b-3ce6-b836-8067790ff6b0 | -7.0321 | -59.412399 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fffe8d62-a91e-389b-86b3-0196e264ecc9 | -7.0339 | -59.420799 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c68c99e-f5c5-3b99-97c2-b0e5029d59fe | -3.7839 | -45.4716 | 2024-10-10 01:06:47 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2d82e08-111e-3f17-b0a1-1815979f711a | -3.7909 | -45.5005 | 2024-10-10 01:06:47 | METOP-B | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4ae62d-eab4-372f-b58b-56ee2aec930c | -7.0223 | -59.414501 | 2024-10-10 01:06:47 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2290885-cc29-3d67-a5ee-f1bfe2360b60 | -3.9154 | -46.430801 | 2024-10-10 01:06:48 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0eae0e12-a484-3029-acd7-f21eb2edee75 | -6.8134 | -58.9758 | 2024-10-10 01:06:49 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d7d385b-d2a5-36e1-ac43-1eedc7ca271c | -6.8122 | -59.017502 | 2024-10-10 01:06:49 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97560ca0-9e3b-3406-9fd2-6949c4e3ae47 | -6.814 | -59.025398 | 2024-10-10 01:06:49 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9cbdfa3-591d-381a-87e0-27d89c307a52 | -3.8864 | -46.437698 | 2024-10-10 01:06:49 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f973b744-804e-38ab-9efd-bb6522d4a61c | -4.8631 | -50.5172 | 2024-10-10 01:06:49 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2396517-1cbe-3dca-87ae-6a409012f5b9 | -4.866 | -50.529701 | 2024-10-10 01:06:49 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdccda58-61ce-3738-875b-da4c77f9420f | -4.8689 | -50.542099 | 2024-10-10 01:06:49 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1816db-69a0-3135-b462-71a155d26534 | -6.8056 | -59.127701 | 2024-10-10 01:06:49 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf94ab6-733e-34bf-a49e-50abd2608b4c | -6.7991 | -59.333 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea36b2d1-22fd-34e1-bc5e-3eb20c70872e | -6.7804 | -59.2943 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 220a4770-8436-3d85-809c-1fdbe4b99521 | -6.7822 | -59.302502 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed517135-2efc-3182-97b3-a35681fa98b3 | -6.784 | -59.310699 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a939ac67-7596-32cc-a5ab-e9adbf89ae7d | -6.7706 | -59.296398 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 885dbf30-f30b-35a2-aeab-eb259922bb75 | -6.7724 | -59.3046 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a09804f-8339-3be4-8432-b9cea7767f84 | -6.7742 | -59.312801 | 2024-10-10 01:06:50 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 666098aa-36dc-3e9b-999b-0743d8bd4c22 | -4.8206 | -50.773102 | 2024-10-10 01:06:51 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c36fb7-f52a-3a4c-9023-5c8b2372bcc8 | -4.8234 | -50.785099 | 2024-10-10 01:06:51 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d02332a3-9c59-393b-b163-17435cdd5433 | -6.7608 | -59.2985 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 860a4648-6409-3af6-9a30-e8fc32e6088a | -6.7626 | -59.306702 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed60278-7801-39df-8509-bd945e45cb27 | -6.7644 | -59.314899 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0198d2a-6dd7-3819-ba19-5b9fc95e8fb8 | -4.8109 | -50.775398 | 2024-10-10 01:06:51 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b024039-e184-3d43-a803-3a7a60a02115 | -4.8137 | -50.787399 | 2024-10-10 01:06:51 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d94f4ac9-3284-3eea-90de-4175835a4ff9 | -6.751 | -59.300598 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f36b631-f7af-37bc-aedc-81a7419ca257 | -6.7528 | -59.3088 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b133186-8725-3ab1-9518-d8cab7136ce5 | -6.7546 | -59.317001 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3b2c998-0d2d-32e3-b997-c069097657cd | -6.7358 | -59.2784 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a553c0d6-522b-3ef2-84e5-8a1d336a4299 | -6.7376 | -59.286499 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26e04557-81ca-358a-82eb-4ac52a29240d | -6.743 | -59.311001 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2363a9a-f690-3be4-8740-698465e51823 | -6.7448 | -59.319199 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a840a364-010e-3aef-9309-b5efa378d48f | -5.0642 | -51.943401 | 2024-10-10 01:06:51 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68ca9475-848c-3ee3-85b1-1923cd4217e4 | -6.7278 | -59.288601 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8147222-7d57-36bb-a8eb-9afdf7aa4df2 | -6.7296 | -59.296799 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 907600f4-1d33-38b9-bd99-018109a2ba58 | -6.5198 | -58.388699 | 2024-10-10 01:06:51 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01e39c05-391d-394a-aeec-e3309219b484 | -6.5215 | -58.396198 | 2024-10-10 01:06:51 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f863c371-87c3-3cae-9618-0b9474c16d06 | -6.5231 | -58.403599 | 2024-10-10 01:06:51 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 292f8116-44be-324c-ac5c-70d6fc4cad25 | -6.5247 | -58.411098 | 2024-10-10 01:06:51 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8121ff7-cd47-3e81-940b-803ae7967a96 | -6.7162 | -59.2826 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37468291-3785-3801-b148-e488ed56d79d | -6.718 | -59.290699 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd555dc-7b6a-3564-97e5-2bab6b4c0d6a | -6.7198 | -59.298901 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6f0a5e-3b02-3b88-b373-38a437359a59 | -6.7216 | -59.306999 | 2024-10-10 01:06:51 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc2f8ed-d255-3ea4-82a9-a81dba8028b3 | -6.51 | -58.3909 | 2024-10-10 01:06:51 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00c8428e-6fe0-3057-bc14-eec7467632ac | -6.5117 | -58.398399 | 2024-10-10 01:06:51 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb50c9ba-3f1d-3c6c-8562-bb7dd315340a | -6.4741 | -58.414398 | 2024-10-10 01:06:52 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f92efa9-dc38-31b6-a029-5a0fd652289d | -6.4757 | -58.421902 | 2024-10-10 01:06:52 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcb80851-9dca-3b5f-8954-5f77f0a9ccec | -6.4774 | -58.429401 | 2024-10-10 01:06:52 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24c154f1-cef3-3ce2-82c3-0185cb07b035 | -6.4643 | -58.4165 | 2024-10-10 01:06:52 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6314c815-55d8-39cb-87a8-d76e0da23bec | -6.4659 | -58.424 | 2024-10-10 01:06:52 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cfb3558c-578f-3223-9571-c10fd75190a0 | -4.0941 | -48.233501 | 2024-10-10 01:06:53 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae516bda-a938-34f2-be1e-c35deb408a94 | -4.0985 | -48.2519 | 2024-10-10 01:06:53 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07c95d97-3724-38fe-9f94-fd9190e3c20c | -4.1029 | -48.270199 | 2024-10-10 01:06:53 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a83ce69-3a96-3a36-bb9e-de6dd92a4c5b | -4.0844 | -48.235802 | 2024-10-10 01:06:53 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2bc7aa0-b79d-3013-b285-3f497b419621 | -4.0888 | -48.2542 | 2024-10-10 01:06:53 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d452aa4-19c8-3e97-85ae-ce0978b4b950 | -4.0932 | -48.272499 | 2024-10-10 01:06:53 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7474af-30b2-3da0-9267-ca3452122659 | -6.7756 | -60.025799 | 2024-10-10 01:06:53 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71a1179b-c38d-3e86-b95d-cb59305b4475 | -6.7776 | -60.034698 | 2024-10-10 01:06:53 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc922089-6186-3475-8161-ea153d9788da | -6.7658 | -60.027901 | 2024-10-10 01:06:53 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15fd2756-2914-3ede-be6b-f0832ae766cf | -6.7678 | -60.0368 | 2024-10-10 01:06:53 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6c40878-ae20-3d69-b1e8-7062ee59e6a4 | -6.7187 | -60.094002 | 2024-10-10 01:06:54 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3d637d1-7c6c-3905-9d61-ff1e8cbcc711 | -6.7089 | -60.0961 | 2024-10-10 01:06:54 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42744b50-e811-350b-b5fe-2719c992b566 | -4.1047 | -49.050999 | 2024-10-10 01:06:56 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63970f58-5f20-35c1-9fab-11ef4971d2ec | -6.6016 | -59.9799 | 2024-10-10 01:06:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67ea2bd6-191b-3807-89c4-0776aab01f3d | -6.6035 | -59.988701 | 2024-10-10 01:06:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 138a093d-df47-3565-b8bb-f0529fb16775 | -4.091 | -49.037102 | 2024-10-10 01:06:56 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22d1220b-2590-3b40-ac0a-469eb3a4ec68 | -4.0949 | -49.053299 | 2024-10-10 01:06:56 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a69a4a5f-32db-3390-a246-96f2826d706b | -6.5507 | -59.981701 | 2024-10-10 01:06:56 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cebc3300-b73d-3443-80dd-a0c18801f50c | -6.5409 | -59.983898 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8040d52-1917-34e9-a181-08e4ec4aa0fd | -6.5428 | -59.992599 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80e89667-f126-37ab-87ff-7477ff55bde0 | -6.5447 | -60.0014 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe09eed-c06b-31ae-9a49-59e9e3ba8fa0 | -6.5466 | -60.010201 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a473c2e-0178-31d0-8543-17ce46da196b | -6.5211 | -60.034199 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5c8e03-479f-3b65-ab02-de87f1686a06 | -6.523 | -60.042999 | 2024-10-10 01:06:57 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README26.md)
