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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c8d7f55-9c78-37e9-99d9-6dc801774de4 | -3.14564 | -50.22679 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c091f1-ad12-3570-be2c-91255d2e3c46 | -3.14509 | -50.23042 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af95cac-c416-39ef-9c73-8258c615dc56 | -3.14282 | -50.22264 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4afd8456-9700-30f3-acee-e11631b1b250 | -3.14226 | -50.22627 | 2024-10-07 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e12ddb6-3dfb-3fc4-adf9-29dbce6baab2 | -3.00655 | -49.80748 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afabca61-bd8c-37cd-a900-49f75a43ea4f | -3.00313 | -49.80695 | 2024-10-07 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0075292d-f4ca-3ea1-b37b-b2aa1229e426 | -4.97454 | -49.76033 | 2024-10-07 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 674ccfc0-aa1f-3edd-9284-00f93fbda288 | -4.47633 | -49.58012 | 2024-10-07 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65e70b95-f540-3a83-b569-f44684693735 | -4.17024 | -50.75103 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26467520-3555-3173-8934-b84c1cfc5116 | -4.16969 | -50.75457 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17051d96-6827-3965-be7a-d86e55b976a7 | -4.16634 | -50.75407 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6724b15d-2083-312c-a3ca-a39f95b9f8f5 | -3.69896 | -49.84631 | 2024-10-07 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c696492c-a355-3df4-a495-d249e3b01af3 | -3.69553 | -49.84575 | 2024-10-07 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f30316c3-5632-32b3-87ea-5288d6b7a9a1 | -3.69495 | -49.8495 | 2024-10-07 04:51:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e8cec15-0267-3026-91b8-b37fd984c8ee | -3.57896 | -50.39639 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63773341-4947-3588-bb49-bc7d84c68fb9 | -4.95213 | -49.64125 | 2024-10-07 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f78c1db9-552f-326c-a175-f0fc317595a5 | -4.95152 | -49.64519 | 2024-10-07 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16348e0e-c9ca-3590-ac1e-72d0184a7a84 | -4.37403 | -50.81847 | 2024-10-07 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e125deca-28ef-36f7-a1a9-f65175da7c9a | -4.37068 | -50.81794 | 2024-10-07 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42c1a252-3f89-32df-a66a-7ee9ae5d2bd9 | -4.07328 | -49.94381 | 2024-10-07 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24c6344c-7eed-3f21-8fd7-334ff94dc8c9 | -3.68558 | -50.25279 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f77cf2c-5eaa-351c-8d01-925220de6319 | -3.68219 | -50.25229 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b647a3d-4561-3976-a44a-d61d735ebeaa | -3.56853 | -50.5527 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fba972b-028e-3979-9cb2-b993cceb4f55 | -3.568 | -50.57827 | 2024-10-07 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af9e2e36-1f14-3893-a90b-9fe8003dc254 | -5.29241 | -50.70911 | 2024-10-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 266caf07-b610-3df8-86c7-67794acb0c88 | -5.29185 | -50.71275 | 2024-10-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa956d11-b54c-3a2d-a5c6-9c87d4e48e7a | -5.15341 | -49.8492 | 2024-10-07 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 911edc27-4917-363b-a8cd-2f6dcf15f39e | -6.55996 | -50.05423 | 2024-10-07 04:51:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83d8bfb6-2042-3ee8-9002-b47a36f527c6 | -6.55937 | -50.05817 | 2024-10-07 04:51:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e02a5f4-5698-3a6e-b4e1-5f2fcba27555 | -5.29579 | -50.70962 | 2024-10-07 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 539b1206-7f15-32f6-b592-b238c31ff855 | -5.15282 | -49.85312 | 2024-10-07 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47391370-e340-366d-bf20-543b857b2e2f | -2.92659 | -51.93858 | 2024-10-07 04:51:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 381b66f1-743a-3f7e-9ef1-93a728c7c2cd | -5.77535 | -51.45514 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7fe2b91-af99-3093-aad1-c6d5560727eb | -5.77202 | -51.45462 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7b3ed98-37d6-3c02-a94c-b52df5797872 | -5.76609 | -51.45031 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 611122d1-d40b-39fd-b322-584df5fe029d | -5.61243 | -52.15187 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0db9c587-4135-3d6d-8b52-e0526f190f38 | -5.7759 | -51.45162 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f2deb5c-537c-3948-91b8-25aee04a143b | -5.77257 | -51.45111 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfcdbb6f-3298-341f-be70-d61a757b24d8 | -5.76664 | -51.44679 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5f04d58-82db-3d65-bcb0-031897609643 | -5.66416 | -51.31871 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6a97c51-194e-34a0-b651-faba365d8cbd | -6.95953 | -51.58126 | 2024-10-07 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a76c40dd-a4d4-3437-b880-efa7556a585e | -9.08343 | -53.26035 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25e70461-366f-306d-a732-5561acdd0698 | -9.08288 | -53.26382 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32e9186f-00bc-31a8-bd53-b1aaa9ed9d96 | -9.07957 | -53.25957 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c00fed53-b1e6-3a33-a5ec-2608fe654ce9 | -9.07903 | -53.26305 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d673a012-079a-3c99-bb66-94d4d16c87fe | -9.07848 | -53.26651 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bab4d81-f07d-3b26-923c-9f2a7459ef90 | -8.97902 | -52.7951 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98d22f16-dd28-3b15-a9ef-2db98c48546f | -8.97626 | -52.79109 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77b2b0ec-4edd-3ffa-8c61-8b95a09d4c90 | -8.97296 | -52.79057 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f30f4f1-17ac-39ff-9d2e-f62cb1ee050b | -8.96028 | -52.78501 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63c4acca-068d-3955-8126-c201d2ea01f7 | -8.95698 | -52.78449 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe74a679-f5d7-35e0-9447-90984569107d | -8.95314 | -52.78746 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ad38ed3-a280-3301-8638-395163322e04 | -8.91534 | -52.83139 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| baa7743e-dc78-328b-abb9-7f17759a0359 | -8.87992 | -52.99296 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b242dd5-009d-3d93-9fff-210e338ef0c9 | -8.87061 | -53.00925 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 686a8c76-f3d7-36e7-9380-36e5bef0ee51 | -8.86839 | -53.00181 | 2024-10-07 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81107f59-786b-3833-821f-a196b9f8242c | -8.86785 | -53.00527 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dec80b62-9df9-3d4d-bcee-a714a58cc678 | -8.86731 | -53.00873 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec4eeab2-f425-362e-b28e-4abf1a29e8d9 | -8.86627 | -53.03692 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5790b9e-a153-3e75-ae4c-f100caf989aa | -8.86573 | -53.04038 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48a0485f-37ec-3d81-a248-b3baa3a79b50 | -3.62668 | -52.27061 | 2024-10-07 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf0ce9c3-b2d5-3fb7-a74e-d27fa1c2f0d2 | -3.25912 | -52.85382 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b11c3137-7734-3167-a754-5ec391b76337 | -3.25634 | -52.84982 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10dd605d-6d9f-3c3a-8de7-739fae66874f | -3.25579 | -52.85331 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bab31967-2418-3e9a-9cb5-b8dda21ec8fe | -3.04178 | -53.04281 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbba8309-e8c6-3004-b220-0984dac48efd | -3.03844 | -53.04229 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05132eb4-904a-351d-b062-970024c5cc79 | -3.03566 | -53.03825 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 086bb73e-1d8f-3b2a-8021-e91909ab05f6 | -3.0351 | -53.04178 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd45a52b-ddf1-3d07-9f93-d12a61da07cd | -2.95293 | -52.78757 | 2024-10-07 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b79e5f99-65cb-33ab-b4d4-0041ee1c7492 | -2.95016 | -52.78358 | 2024-10-07 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 460373a7-6ff6-34d1-8054-49fa890e8882 | -2.88374 | -52.90236 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffcaada9-df87-3f81-b950-b85194cd7cae | -2.88319 | -52.90586 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7be2a62-70a4-3033-85ed-688227fe3211 | -2.88264 | -52.90937 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b0be73-d6c7-3d82-917c-3ce238ea3641 | -2.88208 | -52.91288 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42da9f7c-73d6-3b9e-b95f-e82f8c717f65 | -2.88096 | -52.89834 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d69642e7-336d-3ea8-af6c-8feab9420758 | -2.88041 | -52.90184 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04b8fd7a-43eb-3b9e-b774-ea2be933fc9d | -2.87985 | -52.90535 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fbec2ba3-df96-3f26-8763-4ab78e63c13f | -2.8793 | -52.90886 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b10ca4c5-1192-33d2-8267-f1702a5bcf4a | -2.87875 | -52.91236 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d1939438-ba2e-3266-8c03-5030a0845ef8 | -2.87763 | -52.89783 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1341f39e-61b8-381e-b984-a833b4cfefd9 | -2.87707 | -52.90134 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0ade5b2c-5462-395f-b99d-80d44a19c9b0 | -2.87652 | -52.90484 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25085c91-3727-3de5-9630-f8c925146fee | -2.87597 | -52.90835 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7401c1ba-fc4b-3f1a-9198-408035eaa08b | -2.87541 | -52.91186 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 051bdfa0-3702-315a-89c0-057aaa1a245b | -2.87486 | -52.91537 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c788611-2fd7-3f1a-a3c6-33ede3a83bf2 | -2.87429 | -52.89733 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b33a7ef9-9d37-35b5-8b35-767872514fc5 | -2.87374 | -52.90083 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27a4f225-43b2-396f-9180-78a024f6d447 | -2.87318 | -52.90434 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32e73a09-ad4f-3fca-a3c2-2fd3378defbe | -2.87263 | -52.90784 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc4a1d7b-5d74-349a-a1fc-cdf68c790685 | -2.87207 | -52.91135 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 76c7a635-505e-3443-9f8f-e112acd36eb6 | -2.87152 | -52.91486 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05bcd993-24a1-38d8-a7f7-d5c73d1cb0b1 | -2.87096 | -52.89681 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5556322e-ffd2-37f1-ba10-57ecc5428792 | -2.8704 | -52.90033 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9e8e2cc-744e-3ecd-b7d2-d78e42d2b634 | -2.86985 | -52.90383 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a5582d7f-992e-3bb4-acfe-6947ca3c983b | -2.86929 | -52.90734 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a23d2d07-cb93-3bf0-beb9-1914627be1aa | -2.86874 | -52.91085 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9c572f9b-8955-30f0-b7af-6ff3daddd814 | -2.86818 | -52.91436 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e9b63c9-50c5-39c5-a498-0a671d12c078 | -2.86762 | -52.89631 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 830ee784-5f01-3c81-9a6b-a961136ff651 | -2.86707 | -52.89981 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67919806-49a0-394e-bc6a-96de175dcffa | -2.86651 | -52.90332 | 2024-10-07 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README82.md)
