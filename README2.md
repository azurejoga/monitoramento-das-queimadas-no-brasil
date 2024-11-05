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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f62d866-a611-35f2-ace1-e62309aa214f | -6.1229 | -43.9578 | 2024-11-05 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| bd9018cc-aca5-3e57-a255-b2db0aaa124c | -3.4798 | -45.5291 | 2024-11-05 00:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 6320a1bb-427f-3977-b45b-779dfa7b71ca | -5.0725 | -44.2182 | 2024-11-05 00:20:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 0b4b586a-1bce-3a9d-ab28-1ae46bf69b2a | -6.1041 | -43.9593 | 2024-11-05 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 282.3 |
| c2618329-4039-32b6-a0a2-184e3b2d2cfe | -8.915 | -65.0477 | 2024-11-05 00:20:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| fbc71d5b-3006-34c9-b776-5611751962fe | -3.1061 | -50.2686 | 2024-11-05 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 020b1ced-5a7e-393a-9d5c-0b4cb6c56804 | -2.7881 | -51.4859 | 2024-11-05 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6acc8120-0740-33bd-a9eb-b2ef317d2ab5 | -11.8639 | -43.8644 | 2024-11-05 00:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| e0d9b18d-464d-3ac0-a2b6-0c5df2d52f61 | -12.4015 | -63.2884 | 2024-11-05 00:20:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e4cd3791-f2c6-38e2-a0d0-c94692320288 | -2.8065 | -51.4855 | 2024-11-05 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| a2c18a09-3c5a-3c6d-af15-927a6848b510 | -6.1043 | -43.9362 | 2024-11-05 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 44260373-c808-3696-b689-20505380cadc | -3.967 | -48.15 | 2024-11-05 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 640c54ac-6231-3e27-8c25-c16ab18752dd | -8.9337 | -65.0283 | 2024-11-05 00:20:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7dcbc5ba-db92-37a7-bf6f-723c3da56a76 | -6.0853 | -43.9608 | 2024-11-05 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 9755b195-4678-3851-930d-ecf1b2b92440 | -4.4079 | -43.1252 | 2024-11-05 00:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 7323376a-4526-3300-a532-d8f5dadecf54 | -4.408 | -43.1018 | 2024-11-05 00:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e749cf9a-4032-33a4-a2ce-e4ca8aea0b65 | -4.2429 | -48.5474 | 2024-11-05 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 2d36eda0-8d17-3727-9334-ec764b397ed2 | -1.514 | -53.512 | 2024-11-05 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 637826e0-37a5-3f5f-a577-9b2e757a5cec | -11.8634 | -43.888 | 2024-11-05 00:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5446b675-cccd-3336-8a4b-96df6f94f24a | -3.1787 | -50.5807 | 2024-11-05 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fbfa0f1d-c303-3bb7-990e-f5b049646a48 | -8.9521 | -65.0464 | 2024-11-05 00:20:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 1a1e85b8-2c3f-33c4-86d1-067af2ef4876 | -3.563 | -47.4066 | 2024-11-05 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| bce23eec-5516-3244-bf03-c236c831c0de | -2.8064 | -51.5061 | 2024-11-05 00:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| beea3889-126a-3a34-9661-de0a89f79029 | -5.0724 | -44.2412 | 2024-11-05 00:20:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b0b6a770-42a3-3c62-ac1e-9aa929912bb7 | -3.0722 | -54.5077 | 2024-11-05 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f0a39a6f-43a4-3c7f-81ea-a8773e0df683 | -4.4268 | -43.1007 | 2024-11-05 00:20:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 545b7722-5e39-35a5-9396-8d0b5190e00a | -4.3806 | -47.2388 | 2024-11-05 00:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c516b013-e54b-3115-87f3-94fb511a85fa | -3.1062 | -50.2476 | 2024-11-05 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 160401b1-d2f8-3bb4-8066-f1b4bea37c33 | -12.1571 | -44.6147 | 2024-11-05 00:20:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 68cb2c56-e44e-303f-9390-5ddcccf8d722 | -8.915 | -65.0664 | 2024-11-05 00:20:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 646ece57-6716-3abf-a078-4f885d1011d0 | -6.1039 | -43.9824 | 2024-11-05 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 2574249a-3e9d-3141-a470-b9011e8ca50b | -4.606 | -46.8758 | 2024-11-05 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 48e282c0-5b8a-3b6f-a67d-2fffda8537cc | -4.843 | -44.9402 | 2024-11-05 00:20:00 | GOES-16 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| d2e06e38-2d28-3d4c-ad54-779ec2117366 | -8.9336 | -65.0471 | 2024-11-05 00:20:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 0d586c94-90e5-3138-8458-34a2dbf5e0f8 | -3.5631 | -47.3847 | 2024-11-05 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 265.0 |
| 5c721ea6-54a3-3bb4-a5c4-f1ec51484faf | -3.0906 | -54.5073 | 2024-11-05 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| dac17e71-696a-3fdc-86c2-88e6977b5d94 | -3.9669 | -48.1716 | 2024-11-05 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 9fea8e72-bd1e-38de-aeb8-7095b90f858b | -1.932 | -46.448601 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e60ec3-1e3d-3ac1-911b-ba8280283fcc | -2.8027 | -51.473801 | 2024-11-05 00:20:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0054714b-a938-3469-9f33-9709e9bbcdde | -11.9772 | -42.890301 | 2024-11-05 00:20:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1062b23b-5ef3-3ccd-8d58-c7560e9992bf | -4.8729 | -45.4188 | 2024-11-05 00:20:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff57e981-d724-3581-9f2c-a54307545c5e | -4.5828 | -48.060902 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6bed760-90a7-38ab-8a77-99787b9b20f4 | -11.979 | -42.898102 | 2024-11-05 00:20:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f1f2915-b60e-3fb6-bcda-5ae469da642c | -4.6015 | -46.8596 | 2024-11-05 00:20:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b737e831-4b19-3ed5-9fd3-22929db65db4 | -4.6046 | -46.873299 | 2024-11-05 00:20:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 166881f7-f026-3564-a39d-119ca56991f8 | -4.3566 | -48.614899 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf1233de-0844-3f4d-aaaa-e80c63734904 | -4.8713 | -45.411701 | 2024-11-05 00:20:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecfba133-7c67-3f42-a2a9-dc045fb86e05 | -5.3307 | -47.307701 | 2024-11-05 00:20:00 | METOP-B | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1f38cdbe-a6d9-38f6-9281-61a0c7a66568 | -3.0096 | -45.837101 | 2024-11-05 00:20:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42e88646-b998-374c-a8ca-717fefca4954 | -12.2682 | -43.525398 | 2024-11-05 00:20:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef13da39-50fd-3f93-a250-65bf85422f43 | -4.2551 | -45.557899 | 2024-11-05 00:20:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 002dadc9-a849-3d33-bc3f-188190301cf0 | -3.2073 | -50.613602 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2db58664-4b8f-372d-b63a-7d971554f625 | -3.1038 | -50.2411 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82fbbfbf-9d49-3d4b-a725-20a568497c6f | -1.4854 | -47.207901 | 2024-11-05 00:20:00 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf83b495-a8cd-3b25-81bd-f2ec8de10da3 | -11.9907 | -42.903599 | 2024-11-05 00:20:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4f5c11b4-62c6-3531-90eb-9a7797b43c17 | -4.8985 | -46.7145 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89f47380-d36a-395e-a7ca-aa68068af209 | -3.6993 | -47.611801 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5e37687-8cfa-3acb-8622-4d0cd53f5d17 | -0.7995 | -48.598499 | 2024-11-05 00:20:00 | METOP-B | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 035a195e-de9a-39d5-9264-80f580d83db0 | -4.1404 | -48.752899 | 2024-11-05 00:20:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6a4888-023e-35ba-a701-f8c82a329cec | -3.5917 | -50.2616 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16cb6582-48ca-35a4-95d8-317833287829 | -11.8601 | -43.861198 | 2024-11-05 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 817764f3-880a-38f2-99a2-8b77351b32e3 | -3.5526 | -47.372002 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32a45f31-02cb-3813-8d27-315faa5b51f4 | -3.9764 | -48.158199 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf51c6f9-f5d2-31a6-96b0-97db5b724a02 | -3.0976 | -50.2593 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a13f5e5-3006-3d54-9d5d-07f80301494c | -4.897 | -46.707699 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 356cb611-00fb-33cf-ad94-1bd574cb376e | -8.3164 | -43.5709 | 2024-11-05 00:20:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 871ee816-25cd-3dcd-9abc-c2555ddb403c | 0.1842 | -51.040199 | 2024-11-05 00:20:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| cfa55674-32f3-3a2c-8875-3356437e84ef | -3.5572 | -47.392502 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f499383-a1bb-332c-9cd1-0ce9fe9edfaf | -3.3033 | -46.997799 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f8153e1-8ef2-396e-9b62-772b35ef159b | -5.6975 | -45.826401 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e72a6d4b-a521-3be3-8068-f477b4c8bbe1 | -3.2771 | -44.433201 | 2024-11-05 00:20:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c522fed-a127-36ef-a23f-b8f14de2fcce | -5.1155 | -43.956699 | 2024-11-05 00:20:00 | METOP-B | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8232e77a-e921-3fc5-a53f-c3fc745c5d99 | -5.0599 | -44.1628 | 2024-11-05 00:20:00 | METOP-B | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55f46089-600d-38c5-8dd6-23268362cf20 | -4.1986 | -51.007999 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b232c32-1e28-3f2b-a59b-9880b7960dbf | -4.4241 | -45.847801 | 2024-11-05 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f241fe29-7370-397e-bb27-2d47e16b9ff7 | -13.3039 | -43.271999 | 2024-11-05 00:20:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aacb5609-5577-3c10-9ce5-c42fb99e8e1c | -5.4775 | -48.611099 | 2024-11-05 00:20:00 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b2414c-85c5-30e1-b132-12a637ad1e9f | -10.4545 | -44.937401 | 2024-11-05 00:20:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb1ad5d-5a57-3099-802c-471fd018088a | -10.7812 | -45.244099 | 2024-11-05 00:20:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 97ef58c4-3c1f-3b2f-b481-b4f5af6aa9f4 | -3.7008 | -47.618599 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b570162e-14b8-30c1-a1f4-7611bc5d0bc0 | -5.8383 | -46.266899 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d76ad6f5-21f0-3fa5-83ab-238f440e4906 | -6.1152 | -43.9547 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62ab5181-5e2b-3da8-b29c-2393312ed675 | -5.826 | -43.639801 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f0e8788-66e5-3580-be9a-e4a49348da58 | -11.7544 | -44.212601 | 2024-11-05 00:20:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96946ecd-de03-3356-9e55-5e23fc70d315 | -6.2527 | -43.5676 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad2b0528-5f59-395c-84bb-3e0c9688a2d5 | -5.3732 | -46.4431 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2d8cb6b-4061-3d9b-98a6-463314db9f1d | -10.7714 | -45.246399 | 2024-11-05 00:20:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82666b70-452c-3c0b-aeb1-ac6cff448d34 | -4.0811 | -48.303799 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88bac8f1-29cb-3e19-aab3-a8c12930989c | -3.9604 | -48.1325 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb80d5f-caf1-3655-9575-99a52bdff6e4 | -0.0399 | -50.756599 | 2024-11-05 00:20:00 | METOP-B | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f6a688-64a4-3648-bd2a-f6279486aa3c | -4.2476 | -44.937099 | 2024-11-05 00:20:00 | METOP-B | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60807ebc-1d9f-3955-bb4b-2d5b6127f1e7 | -3.4841 | -50.3792 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c49e8a-1898-3d8f-8e64-f6f0f2b7b116 | -3.8979 | -48.358898 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae8867c-cc61-39a7-8803-dd541c1f028d | -4.6059 | -48.902199 | 2024-11-05 00:20:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cad24ce6-2340-3683-9695-e8c2f3e633fd | -5.3002 | -46.257401 | 2024-11-05 00:20:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 145846dd-8b19-3fc9-8785-52efdc929bdf | -3.3049 | -47.0047 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f76034-2383-36b6-8044-f1a9519a8829 | -3.9549 | -46.369801 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1f4646e-ed77-3ce1-ba87-fbc7c070be90 | -5.4527 | -45.520199 | 2024-11-05 00:20:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2c5c98f-b385-3380-b15e-f2a620b0529c | -4.2486 | -48.0397 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea6fec26-cac4-36d6-96a7-6b566c639f49 | -3.3064 | -47.011501 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
