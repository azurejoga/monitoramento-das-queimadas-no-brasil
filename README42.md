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
| 588937cb-0c07-39a7-9d6b-ed3cb894fa3f | -19.60952 | -56.73346 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.8 |
| a2da880c-84f6-3c73-9fc4-aa6b28c9a387 | -19.60861 | -56.7601 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 081fffc9-2cef-381d-a49a-4bd92152c1a2 | -19.6077 | -56.74461 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 248.2 |
| 963c06f4-6fb9-3ccd-9678-c64e9fae9417 | -19.60709 | -56.74833 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 248.2 |
| d7a562c7-e904-3850-9253-95f0490514d2 | -19.6068 | -56.72913 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.8 |
| eef02804-363d-3b6a-90a9-29ef61aa085e | -19.60558 | -56.73657 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 747e644e-feea-37bf-b4fc-4f8baf5e451e | -19.60527 | -56.75949 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9205bbd6-6973-375a-95d2-6da476454907 | -19.60346 | -56.72853 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 6281121b-af59-359e-9b26-f2b4d0dacdaa | -19.60254 | -56.75517 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.8 |
| dd67a833-c044-3586-8abb-9de68798c653 | -19.60195 | -56.71677 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 54a4e163-e10c-388f-b531-3c6616f5fb60 | -19.60193 | -56.75888 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b28e843d-e6bd-3fee-913e-137ce4e5d68b | -19.59708 | -56.74651 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 239.0 |
| 2f6f53e3-5c1a-3b4f-bf88-2b95afa95274 | -19.59465 | -56.76139 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 20147258-f8f0-3af5-88f9-2d12bd9e1f93 | -19.59041 | -56.7453 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 55a06771-b951-350b-a6ff-ac6c64f42388 | -19.58768 | -56.74098 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 2b5c7312-c31b-3c87-abdd-a181e236bf5d | -19.58678 | -56.7255 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 25.5 |
| de09cf9a-198e-3541-8582-f204ae4d8b69 | -19.58646 | -56.74841 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4b9d56f8-3653-33ee-b599-ccefa40e0a0e | -19.58561 | -56.71878 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f5e48366-2ef0-36d0-b94b-890efd48cd73 | -19.58381 | -56.72994 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4e422109-f96e-39ac-b7c0-10cccacee19e | -19.57894 | -56.71758 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fddd8296-52fe-314d-9016-9e95c4416f43 | -19.57834 | -56.72129 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 08567a27-d2a1-3d30-beb7-3eaee92f0338 | -19.56166 | -56.71826 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 89ba83bf-9047-3d1a-bf1d-c83c5e90737a | -19.53983 | -56.72578 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| fc983361-1eca-3fd9-8462-444820218166 | -19.53649 | -56.72517 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.8 |
| 777c2b65-cf47-3fec-9b0d-fe8168871a02 | -19.52709 | -56.71964 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| ac5f7b66-728c-39df-8e62-ba31d6f30296 | -19.50252 | -56.68077 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5770e61d-019f-30cc-9c2c-5c50cd341733 | -19.48644 | -56.71609 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| a4024173-d020-38fc-8cac-b199c2775cfb | -19.48576 | -56.62062 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e927187f-e083-355e-8b7b-80d3621f9350 | -19.48371 | -56.71177 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f6deeb4f-83cf-3c27-8d83-7407c9cc5ef2 | -19.48037 | -56.65399 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 1c9404a1-0045-3457-9e40-2aa8164480a5 | -19.4801 | -56.67686 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 88854c4e-067d-3b56-8413-14d72fcf6bda | -19.47742 | -56.71462 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ae074e69-d224-389e-beb8-ba365c7017f2 | -19.47676 | -56.67626 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ebda94eb-40f2-33e2-91fa-5929e285e87b | -19.54104 | -56.71835 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 1227eae8-62b1-335f-aedc-a6599261f19f | -19.53164 | -56.71281 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ac8fbfd7-3363-3260-b07a-a93de5573cf3 | -19.52769 | -56.71592 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| e8892a69-bbfa-3704-a130-30f277ae4986 | -19.51036 | -56.59064 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 8cf6e448-de51-3715-8651-eeddfcb135a3 | -19.50828 | -56.70858 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e004ffa5-4cea-3b42-b70c-d32efb8f7f72 | -19.50677 | -56.69683 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 64fbebb7-a602-3bd8-a49d-98f9efbfa69c | -19.50222 | -56.70365 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 39032728-9b18-3e3c-b57d-94b8456354c9 | -19.50189 | -56.60054 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c8ddea44-18ad-3e72-9b4e-056669c75abb | -19.50037 | -56.58884 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b736b772-22f4-3b50-afcf-dd536ced637c | -19.49959 | -56.5774 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a7546101-996b-31e9-805b-e1b44b5ba736 | -19.49916 | -56.59624 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 61d43728-83a5-338c-b51e-c55070173310 | -19.499 | -56.5811 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8a51e210-549e-395e-be1a-e40733e4f482 | -19.49828 | -56.70676 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9ac874b2-4077-380b-9722-d3a6d5c18f55 | -19.4978 | -56.5885 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7a77cac7-f338-35f4-97e1-5866351ecc49 | -19.49767 | -56.71047 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 77a8876e-882f-32ba-af66-a7677d61f028 | -19.49706 | -56.63016 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f244d864-5dbb-3a43-bbf8-5331a56f13c1 | -19.49661 | -56.59591 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| aa483452-6875-3b38-aee7-2550c4f11d10 | -19.49183 | -56.62553 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 398f8d7c-0d74-3652-8fd1-fc31f04db658 | -19.49054 | -56.591 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 99d27d7f-4d90-37b2-8f32-0ae06170ac45 | -19.48995 | -56.5947 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f32a8213-4f86-30ad-9af8-18a022ec8f9d | -19.48909 | -56.62122 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 348812e8-c7df-3117-897e-de02baf73e1d | -19.48643 | -56.65891 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 403fc7a2-cc74-3e50-847b-f339491499cd | -19.48583 | -56.66262 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e4f2d0d8-cb4d-3560-b423-6d4c5ba248c9 | -19.48523 | -56.66633 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c86b4a16-df80-3813-9173-e6fa4c664d27 | -19.48516 | -56.62433 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f0f1b382-495c-300b-8b54-5a0cc0ba844e | -19.48277 | -56.63915 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| aa63a559-b16f-38bb-a268-a5f9bf05130e | -19.4825 | -56.7192 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 00dd4cec-f96f-3aa0-a4f6-d98302a6158b | -19.48097 | -56.65028 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 905f1bc0-108e-39b9-8bc6-feabcb96a6fa | -19.47977 | -56.71488 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1f20e08b-8e44-3d8c-bd65-d0c97c2e3254 | -19.54225 | -56.71091 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 343de662-66c2-3d1e-8fa6-35a0d65ed6c5 | -19.53224 | -56.7091 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e025f7bb-8b9c-32d9-a972-565982808c93 | -19.50916 | -56.59804 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a2eac706-e139-341b-aeb1-fa6088f1514a | -19.50823 | -56.58265 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c4666aba-74fe-3c90-ad6b-c08b1a04227c | -19.50616 | -56.70054 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7fc8e0b7-b539-3af5-9686-26a4456c335e | -19.50582 | -56.59744 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ff7f0381-0700-3f46-85ee-a65eb6ba964b | -19.50551 | -56.57835 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8dc50543-2e2f-3f38-a505-e6af8b9ef335 | -19.50522 | -56.60114 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f1b2bfcd-94d1-3a6d-913a-eb563a8a4ef7 | -19.50462 | -56.60484 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 38a08413-65ff-3771-8afc-d47fb3b98d29 | -19.5037 | -56.58944 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 86017861-57da-30d8-839d-33b8af7a4a2c | -19.50343 | -56.69622 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e96c826f-2dac-3065-a7b4-c1ea5ca4d5d8 | -19.50338 | -56.57035 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| e9f956f7-26d0-3e5c-b295-c2dab852ed4d | -19.50218 | -56.57775 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3d78f0c6-a6a1-325c-a67d-5258845f9058 | -19.50097 | -56.58514 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f29b23b3-a047-3021-af3c-78ff8d2cda0e | -19.50019 | -56.5737 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 291d0b30-990a-34d4-8ad6-34a23eb53402 | -19.49721 | -56.5922 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| de2a4a81-d778-3dbc-9d17-0514d83eab2d | -19.49555 | -56.70244 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8b2ef5c6-338c-3e02-9ca2-5ea9d9259b34 | -19.49403 | -56.6907 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ce5aeeeb-279e-361a-aa90-239c06b809c7 | -19.48935 | -56.5984 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1603b8e2-8c96-3c29-9ddf-4ec0f44dd158 | -19.63404 | -56.64619 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c0ee9443-e0e7-312f-9356-81ede1f6d4be | -19.63226 | -56.69933 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b1da74cc-95d8-34f1-ad53-9df63ab13e36 | -19.63132 | -56.64188 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8bde3b11-ac47-3768-913b-7a311ec9a772 | -19.63071 | -56.64559 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 279cd0a1-4fd2-3105-8a90-7853749c129c | -19.63011 | -56.6493 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4756d484-7e86-3436-9982-349d037afd94 | -19.62984 | -56.71419 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 39b38d82-d04b-37ef-8ae9-58ab347d3eaf | -19.62953 | -56.69501 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 8eaf3e98-43d7-3df3-aa16-e22fcafc9a8f | -19.62923 | -56.7179 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cdbbdaab-2787-3274-85c9-5d839a139291 | -19.62893 | -56.69873 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| b09fda07-f98d-3aa4-8aa2-96402731fafa | -19.62738 | -56.64499 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1d10911a-a0f6-3fe0-add8-731befdff6c1 | -19.62529 | -56.72101 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eba21b2d-3b6b-39e5-87be-f0c1f40a9862 | -19.62226 | -56.69752 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 753e2d09-f5ca-3d1b-9b7d-b21d7f35b12a | -19.62135 | -56.72412 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a64b7d6d-6e1a-3b3c-9373-f2dd8f3e5342 | -19.62772 | -56.70616 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 34a18b4a-330b-3f3a-9209-b2a1d09fee99 | -19.6268 | -56.6907 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6b7b9384-e11c-3004-a04a-7be3223c215d | -19.62651 | -56.71358 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| ae2c91cc-402c-3299-9563-7c1281afe41d | -19.62499 | -56.70183 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 951e43cd-e5c8-37d8-bf2b-bad5b56e5b18 | -19.62378 | -56.70926 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 0ec78bea-365a-3429-bf8e-c9e5f18f75b6 | -19.62105 | -56.70494 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README43.md)
