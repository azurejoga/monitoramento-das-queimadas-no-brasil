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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d69d7c59-ac82-39aa-bb9a-6a7419f7bf93 | -18.34826 | -42.77064 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c253aacc-eca2-357c-8fdf-d53f6a1934b6 | -18.33399 | -43.05421 | 2024-09-29 04:04:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09c39cf6-8235-3f5e-a9bf-d030c1ac8650 | -18.33126 | -43.05001 | 2024-09-29 04:04:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc09e907-ad60-3be7-aa36-b381af76feb8 | -18.33068 | -43.05362 | 2024-09-29 04:04:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a864db29-2f41-3c92-822e-4864d95f3962 | -18.30648 | -42.55964 | 2024-09-29 04:04:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4a86125e-728f-3afa-88b0-75dfdade31e6 | -18.30217 | -42.17256 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 599a4283-2bfe-38bf-93b3-99193b25852e | -18.30161 | -42.1762 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 741c7aed-b0ad-330e-94f6-317f36e53851 | -18.30104 | -42.17986 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c19efe5-341b-399f-9e93-709e5eaf9a93 | -13.35568 | -42.06305 | 2024-09-29 04:04:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b45db799-3301-3acc-8d1d-727dc84fc4c0 | -18.29942 | -42.16836 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 81e7f29b-66e0-3ac9-8e51-6496c1bd912a | -18.29885 | -42.17203 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 042597f1-39f3-3bb1-a691-66bbeaea7e4c | -18.29829 | -42.17567 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 59820426-a970-3785-bcf8-354bcef5e931 | -18.29773 | -42.17932 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 74f41bc0-9e0b-33ff-b00a-c7918d6cb413 | -18.2961 | -42.16782 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 11ed2894-e786-3569-bf26-2a58899a5717 | -18.29554 | -42.1715 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 3fd3a88d-2399-389a-8768-2daef93cb9d5 | -18.29553 | -42.54293 | 2024-09-29 04:04:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 32446c17-2c50-3b58-93ec-edfa86f0662b | -18.29498 | -42.17515 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b01273f9-4905-3c41-8b1b-b81677101152 | -18.29442 | -42.1788 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8e364de2-54cf-3661-86b0-527a505e0734 | -18.29386 | -42.18243 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f4d4b2c3-0a10-31c2-af79-b91cc7a2f8f3 | -18.29336 | -42.1636 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c2f55d78-1ef5-31ad-9e26-d025f9925dfc | -18.29279 | -42.16729 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 423b75ed-4fb7-3803-974d-d47e8b1a5e22 | -18.29223 | -42.54237 | 2024-09-29 04:04:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e0a2ae78-f27e-3abd-8856-bfdc89481068 | -18.29223 | -42.17097 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 2a56606a-2f4e-33ac-ac81-b33c50a696f6 | -18.29167 | -42.17463 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| b60de175-44f9-3dd6-8983-098bf6278202 | -18.29111 | -42.17829 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 45a4f149-11ad-3565-9b9a-d4f2858edce3 | -18.29055 | -42.18192 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d4181900-f3dd-3fba-a6c8-3462e3a12c97 | -18.29004 | -42.16308 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a18bf13f-b283-3ffe-8a3f-67779a48ff8d | -18.28948 | -42.16677 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a324b688-46dc-3c05-a89a-64eeb4dd07b9 | -18.28892 | -42.17045 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 99dbffcd-54d2-3e45-9c24-b1d4487ad803 | -18.28836 | -42.17411 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| db67fb77-c5da-3f8d-8d94-8794a3860b49 | -18.2878 | -42.17777 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 75ecb2e3-8e92-3498-b0b7-283cfed51fa0 | -18.28673 | -42.16255 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| caf167c4-f390-3677-b11b-fa976370047d | -18.28617 | -42.16623 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b90fb7a8-1a35-313e-b64f-ce0234244071 | -18.28561 | -42.1699 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f422f6af-52bf-35fd-8e11-77fbb7a408c7 | -18.28505 | -42.17356 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0763c752-2cac-31be-a968-3f9e1f2a1fb8 | -18.28449 | -42.17722 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17537ea9-55e0-306c-9032-51b2a69a3a23 | -18.28286 | -42.16568 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 38df0b30-1830-3237-9267-776fca15c018 | -18.2823 | -42.16933 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1dff02e3-60eb-3ea9-a2b6-02f3058a9154 | -18.28174 | -42.173 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0183b9c-7dbc-318f-8240-f7876559eb6a | -18.28118 | -42.17666 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f289a39b-f96c-38f0-a810-1c780c412e57 | -18.27899 | -42.16877 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 68429d3b-67cd-3ac6-81eb-9a5b188701ae | -18.27843 | -42.17243 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b92ab2b-ecb7-3f8e-9e2c-0ab03aa35297 | -18.27787 | -42.17609 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58e62f33-ce48-378c-b3d1-f16f0f1f0a9b | -18.27732 | -42.17974 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05b6e875-e702-3e8a-b4ba-4b75fcb8687f | -18.27457 | -42.17551 | 2024-09-29 04:04:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5dcdf868-73b8-31fa-accb-56f83d3921b0 | -18.95038 | -42.08963 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0e99cc24-dc93-3bc3-9bbf-4d7101b66578 | -18.94483 | -42.10373 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1e8af758-0824-3a07-963f-d149a772c38e | -18.94042 | -42.08792 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a8f8c337-e808-3f0a-b388-0b51b0a0e606 | -18.93986 | -42.09158 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2157be40-f6a1-3ed9-953e-9b823409000d | -18.93819 | -42.10258 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d3670f73-86f1-3691-b8ca-1d0b29c3c61f | -18.9371 | -42.08735 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 16b6d5e1-e4b2-3e0e-b3ae-d05da3e700dc | -18.93654 | -42.09102 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 49308970-7446-3815-99d8-8cae98caf1a4 | -14.17419 | -46.4548 | 2024-09-29 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dfd16ff-639e-3ba3-b4b3-7cf8a396f763 | -18.81001 | -41.91947 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9f700e14-5363-3763-a78d-9126c25e9263 | -18.80668 | -41.9189 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c4baa647-fbc1-3d8d-8f53-c8072c513454 | -18.80115 | -41.91043 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23a21baf-277c-384e-a3ce-47cc48f1ffc1 | -18.79838 | -41.90621 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| dab7bc02-a179-3484-8e40-7ce00865854a | -18.79782 | -41.90989 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f23a76b-3f3e-3f4e-8b9e-12e62410bcc2 | -18.79726 | -41.91357 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 02e54b24-1ffb-359e-8928-7ba595d3113a | -18.79505 | -41.90567 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 99986e10-5377-3fb6-a247-d13f70ad8e3a | -18.79004 | -41.91612 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 579a09ee-cef4-3a7e-a4b0-8496c68e9234 | -18.78948 | -41.91983 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 52f2a6ec-bce2-3a9e-99bf-90a3c3e8025e | -18.78672 | -41.91556 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7d6facc9-3525-3567-b0dc-445c4a18f626 | -18.78616 | -41.91927 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d720368c-048b-3a8d-ba8e-c042d2b0e54c | -18.7856 | -41.92295 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| bdac05af-3043-3549-8944-07eb934f7e11 | -18.78448 | -41.93027 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| aa571347-13fc-323f-9e25-c371a6be90e0 | -18.78115 | -41.92973 | 2024-09-29 04:04:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 99ebfc03-4db4-334a-be57-70a3da2775cf | -19.08149 | -43.19138 | 2024-09-29 04:04:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 592f31b2-4ecf-3483-a917-3015f1a8deab | -19.07857 | -43.18742 | 2024-09-29 04:04:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 760a9010-db1f-3866-b691-0f17e5be2299 | -19.05414 | -42.95545 | 2024-09-29 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 22d8da56-75e5-3ea2-af47-766cb40b41d1 | -19.05356 | -42.95909 | 2024-09-29 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1821b40b-4a32-35ef-b9d8-0c999291538f | -19.05083 | -42.95488 | 2024-09-29 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 08c5a538-0b4b-3ed3-b077-567406d5dc83 | -19.05026 | -42.95851 | 2024-09-29 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6de4ec96-d4ee-3332-9ebb-5801924ec56f | -19.04969 | -42.96215 | 2024-09-29 04:04:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dba2d411-fbd4-34f3-8241-015520bdc00e | -20.20056 | -42.29087 | 2024-09-29 04:04:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e05990fc-bfcb-3aa4-a816-40aaebb2a748 | -20.19802 | -42.2873 | 2024-09-29 04:04:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fe862f6e-2c3d-3d66-a7b4-c086589d68d8 | -20.19745 | -42.291 | 2024-09-29 04:04:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a41c65c8-e9ab-3d56-8653-19e063b28b6f | -20.13711 | -42.26178 | 2024-09-29 04:04:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a8925e9c-86e3-35af-9d6e-de6674f194ed | -19.82249 | -42.40921 | 2024-09-29 04:04:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 963c8344-6c7f-3b01-8bf1-b5704107bbf8 | -19.81861 | -42.41231 | 2024-09-29 04:04:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aa0a43ff-93d5-31fe-ad8c-3508769212ab | -19.64215 | -42.09932 | 2024-09-29 04:04:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5eca4862-5303-32cb-bba2-ce9225fe19a0 | -19.88823 | -43.1893 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7568e5fd-73dd-33bf-95dd-3ed05639c3b0 | -19.88765 | -43.19294 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 58ef6d97-9c8f-3485-9fa1-45bca7786058 | -19.8865 | -43.20023 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ca4bf290-5577-342b-bb97-e20b5894fc84 | -19.88607 | -43.18142 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 68103888-ab0d-3961-94b1-e117c719d806 | -19.8855 | -43.18507 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 663b629f-19e6-3bfb-9bec-220f67430150 | -19.88493 | -43.18871 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 759fbdb9-93b1-3360-90c4-bb93c299fb21 | -19.88335 | -43.17719 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b8ae010-b1df-3b52-990a-1529d0e5fd88 | -19.88277 | -43.18084 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4c99a6cb-41f6-309d-ae5c-a8b4b947a9e3 | -19.8822 | -43.18449 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3d25ec3d-f020-353e-b46e-b951ba1867f9 | -19.88005 | -43.17661 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a3064768-7fce-3919-8e14-09152a7277a8 | -19.87947 | -43.18026 | 2024-09-29 04:04:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e381f772-1b35-3822-9e28-e80d9b725b7e | -19.87402 | -43.1718 | 2024-09-29 04:04:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| db0e7fdd-a36c-34dc-bf1e-fa3a3313f6de | -19.87072 | -43.17122 | 2024-09-29 04:04:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9ec68720-3b04-32e5-8338-5a1e90a9385e | -19.86743 | -43.17064 | 2024-09-29 04:04:00 | NOAA-21 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1f3f106e-60a5-377a-b465-152bf780ab3a | -19.5213 | -42.88279 | 2024-09-29 04:04:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 449266a0-f9fe-387f-9364-77b9d9eff4e5 | -19.52073 | -42.88643 | 2024-09-29 04:04:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b65bcf1e-bcb6-381d-904b-1f834efbb2d2 | -19.518 | -42.88222 | 2024-09-29 04:04:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e67fb9c3-1d6f-38ea-b9f9-9911f446312d | -19.51743 | -42.88585 | 2024-09-29 04:04:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 75e1680d-756b-3a96-8fad-d61a25701807 | -13.75259 | -42.60266 | 2024-09-29 04:04:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README33.md)
