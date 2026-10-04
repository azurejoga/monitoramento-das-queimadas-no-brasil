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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccb8d59c-1844-3469-8c38-00b84ba95906 | -3.0721 | -49.5313 | 2026-10-04 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 5ecb01e0-277f-382a-b1ce-fdee0749a31d | -3.1299 | -53.7431 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 2554212d-a055-31c1-96a7-d949e39fd8f1 | -1.6215 | -55.0129 | 2026-10-04 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| b3694cf2-db5a-3abb-b293-b34db5ccf4b6 | -3.0548 | -54.2277 | 2026-10-04 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| cdd84480-706f-3c12-bfce-716e91bb39d1 | -2.798 | -54.0933 | 2026-10-04 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9d3d7241-1c67-328d-b3d5-b2ed5d4d0aa8 | -4.2745 | -46.3624 | 2026-10-04 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 136.1 |
| 9f457b8b-afa2-32ad-bbd3-c71b24e730f7 | -2.5842 | -51.8829 | 2026-10-04 01:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 46cd307f-b820-3aa2-a3f5-b651f94eed4a | -4.2887 | -50.2675 | 2026-10-04 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 269.3 |
| 16c47d2e-615f-37b2-b975-c386d28d39e7 | -3.1115 | -53.7637 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d0a13b4b-9132-352a-ac79-48fcc9ad2f91 | -2.7979 | -54.1134 | 2026-10-04 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e8b1e9cf-4391-3215-a2ca-ef853a1eb562 | -3.1116 | -53.7234 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 279.6 |
| 3cf5529f-d2ff-300d-b2e1-4e24fedbaee7 | -3.13 | -53.7229 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 98ce6577-f02a-362d-9356-f1832607f330 | -4.2886 | -50.2886 | 2026-10-04 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 2615c78e-6f39-33d8-916d-90aff788cc43 | -2.6026 | -51.8619 | 2026-10-04 01:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7ab1c954-bda6-3492-a126-a1ec381afae1 | -3.1116 | -53.7436 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 255.6 |
| 9ec3bb8a-b5fe-3a3f-8ce8-7a6c9222ec89 | -4.2702 | -50.2683 | 2026-10-04 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 512ddc76-720b-3c69-a25f-100c7768a437 | -3.4762 | -50.0883 | 2026-10-04 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 266e38d7-8138-3415-9388-44c039847644 | -2.8164 | -54.0929 | 2026-10-04 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 067b7c2a-b2cc-3df2-9cec-b311bffd61f0 | -1.0911 | -54.1001 | 2026-10-04 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 6b814087-b814-3864-b029-bf4f2cc5fe76 | -2.5843 | -51.8417 | 2026-10-04 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 19ceab13-8b58-3f31-a89b-72a4ee2d7b18 | -2.8163 | -54.133 | 2026-10-04 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| d936a725-48c0-330b-9113-5d7d26af01ba | -2.8163 | -54.1129 | 2026-10-04 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| c792c411-4482-3b99-95b2-36eec32f0df3 | -4.2559 | -46.3633 | 2026-10-04 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 03315721-5938-3414-92f4-bfebb8a0589d | -2.2297 | -53.7026 | 2026-10-04 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| aac0fd3b-0251-3bcf-b4f7-3717f5c48be8 | -9.0857 | -61.1629 | 2026-10-04 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 4a5c8514-fe10-3b25-8367-68d327b9f2b8 | -3.0721 | -49.5313 | 2026-10-04 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8eacd3cd-7a44-362d-ae75-079cbb79e63f | -3.2951 | -53.8395 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6d26b200-0968-32ab-a873-55239f825d12 | -2.5842 | -51.8623 | 2026-10-04 01:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 7e2e0c37-2a83-3d40-9c79-33eb2bdc341a | -3.5128 | -54.6162 | 2026-10-04 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3e600a16-2bf4-3d0d-989f-7a00d0b0eece | -4.2744 | -46.3846 | 2026-10-04 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 8b31247b-2db0-3c8e-946a-c635ba8bb20e | -3.072 | -49.5525 | 2026-10-04 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6bf9f57d-7355-3fe8-b131-9b90026d20ac | -4.2558 | -46.3855 | 2026-10-04 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 48c15247-f5dd-3584-83a2-8c55115a4afe | -4.2888 | -50.2465 | 2026-10-04 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3afc12a8-4c83-39d1-a1a4-35d11c004148 | -3.4761 | -50.1094 | 2026-10-04 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4b974d70-f236-362d-a959-fbbd8511ec6e | -3.1839 | -54.0839 | 2026-10-04 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| fcdb909b-c5fc-3454-9694-4e26c5be405b | -8.5551 | -67.0686 | 2026-10-04 01:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| f1d60c43-f300-3c04-8b4d-5d421f3c4fcf | -3.4761 | -50.1094 | 2026-10-04 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 23e41a3c-c72c-3cdf-baba-52b5505fb0f6 | -3.4762 | -50.0883 | 2026-10-04 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| cb0b2003-5497-3570-a656-fb9667d13c38 | -2.8163 | -54.133 | 2026-10-04 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| aa6c2e7f-a1ea-3497-abf4-840cd181a5a8 | -4.2745 | -46.3624 | 2026-10-04 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 848df93c-4e74-3073-800e-466ec106b35f | -3.5128 | -54.6162 | 2026-10-04 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3fc0f8b7-59b3-3225-9ddc-1b42e3e8f5aa | -4.2744 | -46.3846 | 2026-10-04 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 414625b6-db83-3b65-a56d-0306bd7a8384 | -4.2887 | -50.2675 | 2026-10-04 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 365.6 |
| ff515098-12db-3821-97c9-8f6946f2ae00 | -2.5842 | -51.8829 | 2026-10-04 01:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c5ea497d-d15d-327e-abed-73acc0932492 | -4.2558 | -46.3855 | 2026-10-04 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 91029a0b-2687-3bfd-aa52-ba970b580673 | -3.1115 | -53.7637 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3f8983a2-2164-36a4-b71b-d2c5091026e9 | -2.5842 | -51.8623 | 2026-10-04 01:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 64dd66b9-0d54-3057-aced-e036a1ed8aea | -8.5551 | -67.0686 | 2026-10-04 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 56997298-d0f9-3d2d-ae91-6dcf26754773 | -2.8164 | -54.0929 | 2026-10-04 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| eaa48f9d-00bf-3008-bb83-95e997ee54b1 | -3.1299 | -53.7431 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| a1201432-31c7-3f66-8992-af7046214fe5 | -3.1116 | -53.7436 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 273.9 |
| 1cf208f5-da3b-3507-ae61-411e5e904626 | -4.2559 | -46.3633 | 2026-10-04 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| a99a743e-a381-3695-ac01-e3b00f049055 | -2.7979 | -54.1134 | 2026-10-04 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 3f598c1d-2570-3faf-a234-9934261e73cd | -2.8163 | -54.1129 | 2026-10-04 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 72c48b0f-3cec-3229-953b-578cd03093e0 | -3.1116 | -53.7234 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 255.3 |
| 2afad319-c11e-318a-bde5-6fa29ace26d2 | -3.0548 | -54.2277 | 2026-10-04 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| d55e7d08-6bdc-32d2-b5d5-5b836c2b5ad4 | -2.5843 | -51.8417 | 2026-10-04 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 70c044e8-ee14-3a6b-8d8f-02152b171ada | -3.0906 | -49.5307 | 2026-10-04 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 091cb74f-3b95-31bf-8578-a9a2a18f56bb | -4.2702 | -50.2683 | 2026-10-04 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 4642f13f-9a39-356d-b5cf-cf0e9d89c49a | -2.798 | -54.0933 | 2026-10-04 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 0543007c-83f0-31ac-aa59-55c209769f41 | -2.2297 | -53.7026 | 2026-10-04 01:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ca358ab4-d465-3486-830d-82e6e6dac19c | -3.072 | -49.5525 | 2026-10-04 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 10a66304-3fd7-352e-80f1-91e817887fcb | -4.3072 | -50.2668 | 2026-10-04 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5fd04376-79a8-36f1-9e66-4c67097f4e3e | -4.2886 | -50.2886 | 2026-10-04 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| b1d31ae6-6d27-3674-8346-b53312d11673 | -3.0721 | -49.5313 | 2026-10-04 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 1ce8de19-d908-3526-b85e-bdc77596f11c | -3.1117 | -53.7032 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 011aff9e-ab83-32ab-a4ed-05bc878d5d0f | -3.13 | -53.7229 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 153.6 |
| a3051864-b682-36cd-ba59-b9d325755c7a | -4.2888 | -50.2465 | 2026-10-04 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| d9492686-4f5c-3e6d-83a0-d5b50307766a | -3.1839 | -54.0839 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 4544d3d5-0d58-37c5-b157-527ce9d5c398 | -3.2951 | -53.8395 | 2026-10-04 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 3aa8fd5d-cad6-3c31-a0b7-84131f0939a5 | -3.11 | -53.75 | 2026-10-04 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 924dad4f-76d1-34f2-b7e3-70bac218cdc8 | -4.28 | -50.26 | 2026-10-04 01:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566d9fab-78d2-3368-a65f-21bb52e259f2 | -4.2559 | -46.3633 | 2026-10-04 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 53c4be65-3bdb-356e-9a7b-da04fa3cacf9 | -4.2887 | -50.2675 | 2026-10-04 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 401.3 |
| 6faa70a7-88e5-3009-ba81-92ca3cd5e479 | -3.7559 | -49.5711 | 2026-10-04 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 8189fa84-fedf-3831-8f73-33f8ce0afe7e | -9.4578 | -40.3392 | 2026-10-04 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 294d9c58-7074-3eda-9d44-8aeea3771362 | -8.5551 | -67.0686 | 2026-10-04 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f5b72068-2694-3370-bab8-253a01d24fcf | -3.0721 | -49.5313 | 2026-10-04 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 445af397-c45c-352b-9833-9cc992270e02 | -2.7979 | -54.1134 | 2026-10-04 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| f15000f5-6d0f-34bc-8cad-0104d136c823 | -3.5128 | -54.6162 | 2026-10-04 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2bb901fa-06cd-35cb-bced-4a55efc8295e | -3.4761 | -50.1094 | 2026-10-04 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4045583c-31fa-3591-8bcd-37952cfdd278 | -4.2702 | -50.2683 | 2026-10-04 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9130cbf3-c21c-3dec-9442-9d32bcbb230a | -2.6026 | -51.8619 | 2026-10-04 01:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| b742775a-ba13-3e49-a627-56d85950f82b | -3.1839 | -54.0839 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c1721aad-5bc6-3152-87b9-2c6e182debfa | -4.2558 | -46.3855 | 2026-10-04 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 52288953-4a34-3b26-b5fd-d135bc238ae8 | -3.1299 | -53.7431 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| af81ee3a-4099-3d76-af8a-d49c2d4914ab | -3.756 | -49.5499 | 2026-10-04 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5e58212b-0d71-39f0-92b1-9430d0fb1078 | -4.2888 | -50.2465 | 2026-10-04 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 26dd05bb-c9e5-3874-a7b9-a94198787729 | -6.0818 | -53.4678 | 2026-10-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 9902f099-341f-3fc8-afc0-8bf427c511f2 | -4.2886 | -50.2886 | 2026-10-04 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 3d2e9cc5-7af5-3846-99f5-9380d38162e7 | -3.8756 | -55.8184 | 2026-10-04 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 51bc095a-eedf-3fef-83c2-327073e70a97 | -4.2745 | -46.3624 | 2026-10-04 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| a4421ac1-06c4-3814-972d-a3ac561b9289 | -2.5843 | -51.8417 | 2026-10-04 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 53c5053b-60de-3237-ab9e-2f55e6af5af6 | -3.1115 | -53.7637 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d224e802-9b38-316a-9f7d-6325360f4283 | -3.4762 | -50.0883 | 2026-10-04 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9474f7ef-7b13-3d42-867d-f86aace55129 | -3.1116 | -53.7234 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 254.1 |
| 7dfeee66-f092-3041-aa2d-bb9aacf5e3a3 | -3.13 | -53.7229 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 9da36f46-1dad-3198-a6a5-3918fe080a82 | -3.1116 | -53.7436 | 2026-10-04 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 251.8 |
| 9ba6f680-ac4a-3ee1-bcb6-202edad95632 | -2.2297 | -53.7026 | 2026-10-04 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a56fae8f-8bb0-3d51-8317-8bee62559e2f | -3.8757 | -55.7986 | 2026-10-04 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README17.md)
