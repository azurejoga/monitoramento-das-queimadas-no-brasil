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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bbf3fe4-593b-3ed2-abf2-b4770d5cc1d9 | -4.2701 | -50.2894 | 2026-10-04 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d4d73fe3-7833-3bc9-9acf-ebe87d81b160 | -3.8757 | -55.7986 | 2026-10-04 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 16d21157-c969-3caf-96ba-ceb55357eb53 | -3.1839 | -54.0839 | 2026-10-04 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| cbfe89db-70b6-3052-8539-c381d034e9a5 | -4.2702 | -50.2683 | 2026-10-04 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 196.7 |
| 8e6e6ae2-9364-304c-950b-4ce7c5480bed | -2.798 | -54.0933 | 2026-10-04 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 334ad7d2-7eae-3779-8c0e-c75fcda01e0f | -2.5842 | -51.8623 | 2026-10-04 01:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a266ab19-c736-3cb0-b1ac-e23dabf8f5c2 | -4.2558 | -46.3855 | 2026-10-04 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cfd11cc1-5691-34cd-be36-9f06600d9d31 | -4.2888 | -50.2465 | 2026-10-04 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| e374de0f-e89d-3b1a-b62d-553699544191 | -3.4762 | -50.0883 | 2026-10-04 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bd65834a-a637-323d-ba98-fd38a85713d1 | -2.8163 | -54.133 | 2026-10-04 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| d5e01c7c-a3d9-3be5-b3ee-ae2132dbbe5f | -4.2559 | -46.3633 | 2026-10-04 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.5 |
| d949e6a5-c18b-39bb-8418-ec55c31f39c6 | -3.1116 | -53.7234 | 2026-10-04 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 199.3 |
| 42ef74c2-6382-3a46-9156-9be78adeee07 | -3.8756 | -55.8184 | 2026-10-04 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 35c1f9f7-6e42-3e39-9c94-45a2c93ea9b4 | -3.7559 | -49.5711 | 2026-10-04 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 40fb04a6-5dec-3ed6-a2ce-2cfe1a50655b | -3.13 | -53.7229 | 2026-10-04 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 150.8 |
| a5e0e195-6dfd-3326-ae09-8ada9b2bd691 | -2.5842 | -51.8829 | 2026-10-04 01:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f44616e2-c275-3200-bf49-b7b9915a2bda | -3.4577 | -50.089 | 2026-10-04 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 48415885-5e66-368d-a7cc-13d36d24a90c | -3.1116 | -53.7436 | 2026-10-04 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 25605116-cf59-328b-b1b4-5822d3064d57 | -2.2113 | -53.7029 | 2026-10-04 01:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d645df83-22c3-3c83-998a-35bd625b8a9a | -3.0721 | -49.5313 | 2026-10-04 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 78bfade2-58d3-3954-9d9a-5739de6a823d | -4.2745 | -46.3624 | 2026-10-04 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| bd75f1c8-ccb5-3524-be7c-3c9536e3fea5 | -4.2887 | -50.2675 | 2026-10-04 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 505.5 |
| 246268a4-821b-31d9-b757-041dd6ccd7c3 | -3.8757 | -55.7986 | 2026-10-04 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 23c7856f-906c-3d45-9636-5001839e1750 | -3.1839 | -54.0839 | 2026-10-04 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| feaa9631-abdf-349d-99a8-d32d22906bd3 | -4.3072 | -50.2668 | 2026-10-04 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 68d87b89-b925-3787-967c-b5f46fb3a463 | -4.2702 | -50.2683 | 2026-10-04 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 192.6 |
| b73b0e42-1adc-3f62-99e0-de3ef62a5848 | -4.2745 | -46.3624 | 2026-10-04 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9b70c6b3-d5be-3605-8e99-c18169a11c79 | -4.2744 | -46.3846 | 2026-10-04 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 39.9 |
| e6880b88-8316-3757-8026-320829ab87eb | -3.072 | -49.5525 | 2026-10-04 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 20f4a6a6-7562-316a-af8f-55e1febd9649 | -4.2558 | -46.3855 | 2026-10-04 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7f875a1a-3753-3468-94c2-7f3bb027014e | -2.7979 | -54.1134 | 2026-10-04 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 59ab30f9-f38c-306d-bab3-1a1adc6563fa | -2.798 | -54.0933 | 2026-10-04 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 53893a3a-50fd-3a3e-bdf1-75c48c65ac6a | -3.4762 | -50.0883 | 2026-10-04 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| be5d8fe1-0efb-3742-a8d3-c0118a6fc10a | -2.8163 | -54.133 | 2026-10-04 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 4bddc2de-8d7e-36b9-b643-f537d8dc5895 | -3.8573 | -55.7992 | 2026-10-04 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 52bb29b3-b1b5-38f9-a637-f2cfb4ea7240 | -3.4761 | -50.1094 | 2026-10-04 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 864c84e0-a896-35b5-a8dc-a28f908d92d8 | -2.8163 | -54.1129 | 2026-10-04 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 8d12b551-4cc2-3975-b8b1-c8709024099b | -3.1299 | -53.7431 | 2026-10-04 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d0eacdc8-fd08-38e3-836f-fafcfeb607b5 | -3.0721 | -49.5313 | 2026-10-04 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e2736573-4c50-3f52-872e-dcefbcb28c15 | -4.2887 | -50.2675 | 2026-10-04 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 624.7 |
| 9a0253e8-4535-3691-b8a4-6c2a1da68bb8 | -3.9033 | -49.6925 | 2026-10-04 02:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 128edbfd-fc91-3b60-852b-b9d8cc99750c | -2.5843 | -51.8417 | 2026-10-04 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 5620934f-dfa3-3606-aa19-5717d14cf00a | -3.1116 | -53.7234 | 2026-10-04 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 207.7 |
| b07b84ff-6c7f-33a6-a1d8-fce42f380792 | -4.2559 | -46.3633 | 2026-10-04 02:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| f598b297-31ec-362b-850f-d8e32e1d30c8 | -4.2888 | -50.2465 | 2026-10-04 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 07d27363-6d38-353f-9169-ee6377739af4 | -2.5842 | -51.8829 | 2026-10-04 02:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9319710e-cdd9-39a5-aabf-36206055b991 | -2.5842 | -51.8623 | 2026-10-04 02:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 25f45c35-9574-3dd3-9e38-d282714401a9 | -2.8164 | -54.0929 | 2026-10-04 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 74d83550-0af3-3c30-b39a-ef635ac9a0b3 | -3.13 | -53.7229 | 2026-10-04 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 9f4a547e-c6c4-3075-bc20-6eca8efcbbbd | -3.8848 | -49.6933 | 2026-10-04 02:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 0897c48a-e7c8-3d3e-b9a1-a0ec4a684e6c | -4.2701 | -50.2894 | 2026-10-04 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 74a203bd-efb0-301e-acf5-3aa0bfea94d9 | -4.2886 | -50.2886 | 2026-10-04 02:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| d1da82c6-0acf-37fd-928d-9dabab545ca4 | -3.2951 | -53.8395 | 2026-10-04 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f85edf21-8109-343e-9ed8-949f9b662052 | -3.1116 | -53.7436 | 2026-10-04 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 199.5 |
| 9a5ee220-2ded-3c42-8085-d5cf946bf50f | -2.2297 | -53.7026 | 2026-10-04 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5c7b2a2c-b07d-3af7-ba9b-86e75e854d2e | -9.5137 | -54.6292 | 2026-10-04 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 19767575-0850-3127-8229-d57154950ffc | -3.0721 | -49.5313 | 2026-10-04 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 239e823a-3af0-3c50-81b8-514f7089b385 | -2.8163 | -54.1129 | 2026-10-04 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 7b333076-e7a4-369f-b654-168d2a203567 | -2.7979 | -54.1134 | 2026-10-04 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| efae9421-7261-3c4e-bbe4-3114b8b62349 | -3.072 | -49.5525 | 2026-10-04 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 40964d40-2d06-3c92-a9a5-8f864ce0a323 | -4.3072 | -50.2668 | 2026-10-04 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| abd61499-1b82-39fc-a474-23256a0ec053 | 0.3035 | -51.4389 | 2026-10-04 02:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5664f3c8-1821-3b9f-a13a-db3f2c999733 | -2.5843 | -51.8417 | 2026-10-04 02:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 993d4cd5-e5e8-3ae0-9a5e-a011b265f310 | -3.9033 | -49.6925 | 2026-10-04 02:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| fb5cd3ae-c745-3639-bf8d-b9a1af87a91c | -2.5842 | -51.8829 | 2026-10-04 02:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 85ce02a3-b0ba-33e6-9807-b3c23e1734e8 | -2.5842 | -51.8623 | 2026-10-04 02:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| d77e6358-908a-33af-b718-2c18a977274e | -2.8164 | -54.0929 | 2026-10-04 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b3d9f7f6-d9bb-3033-97da-02823a581f92 | -2.2297 | -53.7026 | 2026-10-04 02:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| dc3fd467-74e8-329d-907d-f0c5769e6d1c | -3.8573 | -55.8189 | 2026-10-04 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d990c912-fb2c-3c13-a8de-54fef7f93f09 | -4.2888 | -50.2465 | 2026-10-04 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| e4cd52e5-78aa-3049-98cc-ef2d409e72e8 | -3.1299 | -53.7431 | 2026-10-04 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 7799975c-f3f9-3d78-9cdb-36c9063463ca | -4.2559 | -46.3633 | 2026-10-04 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 5bede2e1-196d-3725-bd85-00d6aea69563 | -3.4761 | -50.1094 | 2026-10-04 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 33c8e27f-2501-38ff-9806-2689424654e0 | -4.2887 | -50.2675 | 2026-10-04 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 868.2 |
| 3b5e2d37-3413-33dc-ba9c-19c80a0e8df0 | -3.8757 | -55.7986 | 2026-10-04 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a19923fa-51af-3a52-83da-791e553b8ee8 | -3.1116 | -53.7234 | 2026-10-04 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 221.4 |
| fd0c858c-1fee-328c-88b3-d1683d9d2ac2 | -4.2702 | -50.2683 | 2026-10-04 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 183.2 |
| f763bba6-1cd7-3c1d-b556-3d07bc0722b4 | -4.2886 | -50.2886 | 2026-10-04 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 268.7 |
| d2cb5266-5683-3341-9655-18b58c3abd42 | -3.1116 | -53.7436 | 2026-10-04 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 193.8 |
| f4f39620-4014-377e-ad9b-ff982e3f63f1 | -3.1115 | -53.7637 | 2026-10-04 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 63de212b-80db-372e-98ee-36a45c9dea54 | -3.8756 | -55.8184 | 2026-10-04 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 3c7133e0-1c4c-31e1-89d2-6e9db04875b2 | -2.8163 | -54.133 | 2026-10-04 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 38ec00a3-bbc8-3888-8cee-664afec2f854 | -4.2745 | -46.3624 | 2026-10-04 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 173b28f4-11b6-30df-88cf-4159d54e9b77 | -3.8573 | -55.7992 | 2026-10-04 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5e9d93fd-bebe-31ea-9874-1a12adc6463d | -3.2951 | -53.8395 | 2026-10-04 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 05eaf04a-fa63-35a5-ba6b-1f5353d4d6e2 | -3.13 | -53.7229 | 2026-10-04 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 8e71467b-7f64-3e4f-bd20-c89ad40aa75f | -4.2558 | -46.3855 | 2026-10-04 02:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e0e18420-485b-3aed-b827-8cf0a39d3767 | -3.4762 | -50.0883 | 2026-10-04 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 938e6366-1f8e-3795-ac5c-b1c3842d25d7 | -4.2701 | -50.2894 | 2026-10-04 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 55728e1a-e0d9-3628-a8d2-a29c44aebf66 | -3.8848 | -49.6933 | 2026-10-04 02:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 8563337c-5e6a-3b10-b96b-6a23e1206faf | -4.28 | -50.32 | 2026-10-04 02:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0372f3dc-e6f4-3620-86b1-63047d18f2bb | -4.28 | -50.26 | 2026-10-04 02:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91b79a2c-ac96-35d9-9ed2-936fe09b6066 | -3.11 | -53.75 | 2026-10-04 02:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba4f3cac-4f0d-3cdb-993e-3eba76dfa06d | -2.8164 | -54.0929 | 2026-10-04 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 76e994a7-0e0c-30ad-9815-5f1790324230 | -3.072 | -49.5525 | 2026-10-04 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ebb826af-24aa-3d6e-8828-823ad6ffbc69 | -4.2559 | -46.3633 | 2026-10-04 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| fc3e04f7-b6f1-3e3a-a0c1-daa52969f44c | -2.2297 | -53.7026 | 2026-10-04 02:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a7c26545-213c-386a-920e-8d27afd1b985 | -2.5843 | -51.8417 | 2026-10-04 02:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ac655e76-477b-3310-94d3-284d45652fea | -3.2951 | -53.8395 | 2026-10-04 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cc0bb920-0ab9-3b90-bdb3-6ac8834f4d99 | -4.2744 | -46.3846 | 2026-10-04 02:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |


[Clique aqui para ver as próximas entradas](README19.md)
